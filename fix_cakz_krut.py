import re
with open('pypanini/krdanta.py', 'r') as f:
    content = f.read()

# 1. Force aniT for cakziN
old_meta = """    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
        dhatu_id: Optional[str] = None,
    ) -> Optional[Dict]:
        meta = self._get_meta(dhatu, dhatu_id)
        clean = meta["clean"]
        pada = meta["pada"]"""

new_meta = """    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
        dhatu_id: Optional[str] = None,
    ) -> Optional[Dict]:
        meta = self._get_meta(dhatu, dhatu_id)
        if meta.get("op") == "cakziN" and sanadi is None:
            meta["sew"] = False
            meta["sew_raw"] = "aniw"
        clean = meta["clean"]
        pada = meta["pada"]"""

if old_meta in content:
    content = content.replace(old_meta, new_meta)
else:
    print("Could not find meta block")

# 2. Add cicakz to _sannanta_sec
old_sann = """            def _sannanta_sec(c):
                # Nitya-san (3.1.5/3.1.6, seT only): san stem with s/dIrgha/M/cutva (01.0461 aniT excluded via sew)."""

new_sann = """            def _sannanta_sec(c):
                if meta.get("op") == "cakziN" and meta.get("gana") == "adAdiH":
                    return "cicakz"
                # Nitya-san (3.1.5/3.1.6, seT only): san stem with s/dIrgha/M/cutva (01.0461 aniT excluded via sew)."""

if old_sann in content:
    content = content.replace(old_sann, new_sann)
else:
    print("Could not find sann block")

with open('pypanini/krdanta.py', 'w') as f:
    f.write(content)
print("Patched successfully")
