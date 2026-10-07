"""Lint gate: 100% clean on owned code (pyflakes-subset + style).

STRICT (imports, unused vars/locals, dup keys, <=100 cols, whitespace):
  pypanini/search.py, pypanini/subanta.py, pypanini/__init__.py,
  demo.py, tests/test_search*.py, tests/test_subanta*.py,
  tests/test_krdanta_subanta.py, tests/test_lint.py
GRANDFATHERED (compile-only; pre-existing engines, thousands of
long lines, untouched deliberately):
  tinanta.py, krdanta.py, pada_rules.py, phonetics.py, pratyahara.py,
  tests/test_dhatu.py
Run: python3 -m unittest tests.test_lint -v
"""
import ast
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

STRICT = [
    "pypanini/search.py", "pypanini/subanta.py", "pypanini/__init__.py",
    "demo.py", "tests/test_search.py", "tests/test_search_complete.py",
    "tests/test_subanta.py", "tests/test_subanta_full.py",
    "tests/test_krdanta_subanta.py", "tests/test_lint.py",
]
GRANDFATHERED = [
    "pypanini/tinanta.py", "pypanini/krdanta.py", "pypanini/pada_rules.py",
    "pypanini/phonetics.py", "pypanini/pratyahara.py",
    "tests/test_dhatu.py",
]
MAXCOL = 100


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class _UseCollector(ast.NodeVisitor):
    """Per-function assigned-vs-loaded names + module imports."""

    def __init__(self):
        self.assigns = {}
        self.loads = {}
        self.imports = {}
        self.scope = "<module>"
        self.assigns["<module>"] = set()
        self.loads["<module>"] = set()
        self._global_declared = set()

    def visit_FunctionDef(self, node):
        outer = self.scope
        self.scope = node.name
        self.assigns.setdefault(node.name, set())
        self.loads.setdefault(node.name, set())
        for a in node.args.args:
            self.loads[node.name].add(a.arg)
        for child in ast.walk(node):
            if isinstance(child, ast.Global):
                self._global_declared.update(child.names)
        self.generic_visit(node)
        self.scope = outer

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigns[self.scope].add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.loads[self.scope].add(node.id)

    def visit_Import(self, node):
        for a in node.names:
            name = (a.asname or a.name).split(".")[0]
            self.imports[name] = node.lineno

    def visit_ImportFrom(self, node):
        if node.module == "__future__":
            return
        for a in node.names:
            if a.name == "*":
                continue
            self.imports[a.asname or a.name] = node.lineno


def _check_file(rel: str):
    """Returns list of smell strings (empty == clean)."""
    src = _read(rel)
    smells = []
    try:
        tree = ast.parse(src, filename=rel)
    except SyntaxError as e:
        return [f"{rel}:{e.lineno}: E999 syntax error: {e.msg}"]
    lines = src.splitlines()
    for i, ln in enumerate(lines, 1):
        if len(ln) > MAXCOL:
            smells.append(f"{rel}:{i}: E501 line too long ({len(ln)} > {MAXCOL})")
        if ln != ln.rstrip():
            smells.append(f"{rel}:{i}: W291 trailing whitespace")
        if "\t" in ln:
            smells.append(f"{rel}:{i}: W191 tab indentation")
    if not src.endswith("\n"):
        smells.append(f"{rel}: W292 no newline at end of file")
    col = _UseCollector()
    col.visit(tree)
    # names used anywhere (any scope) + __all__-listed count as used
    used_anywhere = set()
    for s in col.loads.values():
        used_anywhere |= s
    dunder_all = set()
    for node in ast.walk(tree):
        if (isinstance(node, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets)):
            val = node.value
            if isinstance(val, (ast.List, ast.Tuple)):
                for elt in val.elts:
                    if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                        dunder_all.add(elt.value)
    for name, lineno in col.imports.items():
        if name not in used_anywhere and name not in dunder_all \
                and name not in col._global_declared:
            smells.append(f"{rel}:{lineno}: F401 unused import '{name}'")
    # unused locals per function (simple Name stores never loaded;
    # tuple-unpacking and for-targets share the loaded set, loop
    # variables conventionally live so only flag clear dead stores)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        loaded = set()
        for a in node.args.args:
            loaded.add(a.arg)

        class _V(ast.NodeVisitor):
            def visit_Name(self, n):
                if isinstance(n.ctx, ast.Load):
                    loaded.add(n.id)

        _V().visit(node)
        simple = set()
        for child in ast.walk(node):
            if isinstance(child, ast.Assign):
                for t in child.targets:
                    if isinstance(t, ast.Name):
                        simple.add(t.id)
            elif isinstance(child, ast.AnnAssign) and \
                    isinstance(child.target, ast.Name):
                simple.add(child.target.id)
            elif isinstance(child, ast.For):
                for t in ast.walk(child.target):
                    if isinstance(t, ast.Name) and isinstance(t.ctx, ast.Store):
                        loaded.add(t.id)
            elif isinstance(child, ast.ExceptHandler) and child.name:
                loaded.add(child.name)
        for name in sorted(simple - loaded - col._global_declared):
            if name == "_":
                continue
            smells.append(f"{rel}:{node.lineno}: F841 unused local "
                          f"'{name}' in {node.name}()")
    # duplicate constant dict keys
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            seen = {}
            for k in node.keys:
                if isinstance(k, ast.Constant):
                    key = repr(k.value)
                    if key in seen:
                        smells.append(f"{rel}:{node.lineno}: F601 duplicate "
                                      f"dict key {key}")
                    seen[key] = True
    # dead code markers (AST-level: statement conditions only, so pattern
    # tables and string literals can never self-flag)
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.IfExp)) and \
                isinstance(node.test, ast.Constant) \
                and node.test.value in (True, False):
            smells.append(f"{rel}:{node.lineno}: W0101 dead 'if "
                          f"{node.test.value}'")
    return sorted(smells)


class TestLint(unittest.TestCase):
    def test_strict_files_lint_clean(self):
        smells = []
        for rel in STRICT:
            smells += _check_file(rel)
        self.assertEqual(smells, [], "\n".join(smells[:30]))

    def test_grandfathered_files_compile(self):
        for rel in GRANDFATHERED:
            src = _read(rel)
            try:
                compile(src, rel, "exec")
            except SyntaxError as e:
                self.fail(f"{rel}:{e.lineno}: E999 {e.msg}")


if __name__ == "__main__":
    unittest.main()
