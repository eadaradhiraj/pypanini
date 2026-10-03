import sys

with open("tests/test_dhatu.py", "r") as f:
    content = f.read()

# Modify the signature of validate_dhatu
content = content.replace(
    "def validate_dhatu(arg: str, verbose: bool = True) -> tuple[int, int]:",
    "def validate_dhatu(arg: str, verbose: bool = True, prefix: str = None) -> tuple[int, int]:"
)

# Extract correct conjugations and participles
repl_old = """    conjugations = data.get("conjugations", {})"""
repl_new = """    if prefix:
        if "upasarga_forms" not in data or prefix not in data["upasarga_forms"]:
            if verbose: print(f"Prefix {prefix} not found in {arg}")
            return 0, 0
        conjugations = data["upasarga_forms"][prefix].get("conjugations", {})
    else:
        conjugations = data.get("conjugations", {})"""
content = content.replace(repl_old, repl_new)

repl_old2 = """    participles = data.get("participles", {})"""
repl_new2 = """    if prefix:
        participles = data["upasarga_forms"][prefix].get("participles", {})
    else:
        participles = data.get("participles", {})"""
content = content.replace(repl_old2, repl_new2)

# Add prefix argument to derive calls
content = content.replace(
    "forms, _ = te.derive(dhatu, code, p, v, prayoga=prayoga, sanadi=sanadi, dhatu_id=dhatu_id, json_path=str(json_path))",
    "forms, _ = te.derive(dhatu, code, p, v, prayoga=prayoga, sanadi=sanadi, upasarga=prefix, dhatu_id=dhatu_id, json_path=str(json_path))"
)
content = content.replace(
    "krd_anta = ke.derive_all_krdantas(dhatu, sanadi=sanadi_k, dhatu_id=dhatu_id)",
    "krd_anta = ke.derive_all_krdantas(dhatu, sanadi=sanadi_k, upasarga=prefix, dhatu_id=dhatu_id)"
)

# In main, we can add a --prefix argument
main_old = """    parser.add_argument("-q", "--quiet", action="store_true")"""
main_new = """    parser.add_argument("-q", "--quiet", action="store_true")\n    parser.add_argument("-p", "--prefix", help="Test a specific prefix from upasarga_forms")"""
content = content.replace(main_old, main_new)

main_call_old = """    matched, total = validate_dhatu(arg, verbose=verbose)"""
main_call_new = """    matched, total = validate_dhatu(arg, verbose=verbose, prefix=args.prefix)"""
content = content.replace(main_call_old, main_call_new)

with open("tests/test_dhatu.py", "w") as f:
    f.write(content)
print("Patched test_dhatu.py")
