with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

# 1. Add imports
content = content.replace(
    "apply_sandhi_eco_ayavayavah,",
    "apply_sandhi_eco_ayavayavah,\n    apply_upasargas,"
)

# 2. Extract the original signature
import re
sig_match = re.search(r'    def derive\([\s\S]*?\) -> Tuple\[List\[str\], List\[str\]\]:', content)
orig_sig = sig_match.group(0)

# Replace the name `derive` with `_derive_inner` in the original signature
inner_sig = orig_sig.replace("def derive(", "def _derive_inner(")

# 3. Create the new wrapper signature with upasarga at the end of the public args
wrapper = """    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        upasarga: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
        cands, log = self._derive_inner(
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,
            _force_pada, _cakz_bypass, _sad_c10_recurse
        )
        if upasarga:
            cands = [apply_upasargas(upasarga, c) for c in cands]
            return list(dict.fromkeys(cands)), log
        return cands, log

""" + inner_sig

content = content.replace(orig_sig, wrapper)

# 4. Also fix derive_all
orig_all = """    def derive_all(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,"""

new_all = """    def derive_all(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        upasarga: Optional[str] = None,"""

content = content.replace(orig_all, new_all)

orig_all_call = "forms, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi)"
new_all_call = "forms, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi, upasarga=upasarga)"
content = content.replace(orig_all_call, new_all_call)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched tinanta cleanly")
