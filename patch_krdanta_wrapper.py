import re

with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

# Add apply_upasargas import
content = content.replace(
    "apply_sandhi_eco_ayavayavah",
    "apply_sandhi_eco_ayavayavah, apply_upasargas"
)

# Extract original derive_krdanta signature
sig_match = re.search(r'    def derive_krdanta\([\s\S]*?\) -> Optional\[Dict\]:', content)
orig_sig = sig_match.group(0)

inner_sig = orig_sig.replace("def derive_krdanta(", "def _derive_krdanta_inner(")

wrapper = """    def derive_krdanta(
        self, dhatu: str, pratyaya: str = "kta", sanadi: Optional[str] = None,
        upasarga: Optional[str] = None, dhatu_id: Optional[str] = None
    ) -> Optional[Dict]:
        res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, upasarga, dhatu_id)
        if not res or not upasarga:
            return res
        
        # apply sandhi
        out = {}
        for k, v in res.items():
            if isinstance(v, list):
                out[k] = list(dict.fromkeys([apply_upasargas(upasarga, c) for c in v]))
            else:
                out[k] = apply_upasargas(upasarga, v)
        return out

""" + inner_sig

# Notice: krdanta.py's original signature had `upasarga: str = "saM"`. We should change it to Optional[str] = None
old_sig_1 = 'upasarga: str = "saM",'
new_sig_1 = 'upasarga: Optional[str] = None,'
content = content.replace(old_sig_1, new_sig_1)

# same for derive_all_krdantas
old_sig_all = 'upasarga: str = "saM",'
content = content.replace(old_sig_all, new_sig_1)

# Now apply wrapper replacement
# Need to fetch the updated orig_sig after old_sig_1 replacement
sig_match = re.search(r'    def derive_krdanta\([\s\S]*?\) -> Optional\[Dict\]:', content)
orig_sig = sig_match.group(0)
inner_sig = orig_sig.replace("def derive_krdanta(", "def _derive_krdanta_inner(")

wrapper = """    def derive_krdanta(
        self, dhatu: str, pratyaya: str = "kta", sanadi: Optional[str] = None,
        upasarga: Optional[str] = None, dhatu_id: Optional[str] = None
    ) -> Optional[Dict]:
        res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, upasarga, dhatu_id)
        if not res or not upasarga:
            return res
        
        # apply sandhi
        out = {}
        for k, v in res.items():
            if isinstance(v, list):
                out[k] = list(dict.fromkeys([apply_upasargas(upasarga, c) for c in v]))
            else:
                out[k] = apply_upasargas(upasarga, v)
        return out

""" + inner_sig

content = content.replace(orig_sig, wrapper)

# Now we need to remove the hardcoded `upasarga` prepending in `krdanta.py` for lyap etc.!
# If we don't, it will be prepended twice!

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)

print("Patched krdanta.py wrapper")
