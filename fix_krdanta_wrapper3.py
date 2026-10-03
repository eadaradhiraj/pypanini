with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

import re

# Add imports
if "from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN" not in content:
    content = "from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN\n" + content

# Fix _derive_krdanta_inner signature
old_sig = """    def _derive_krdanta_inner(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: Optional[str] = None,
        dhatu_id: Optional[str] = None,
    ) -> Optional[Dict]:"""

new_sig = """    def _derive_krdanta_inner(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        _force_pada: Optional[str] = None,
    ) -> Optional[Dict]:"""

content = content.replace(old_sig, new_sig)

# Fix derive_krdanta wrapper
old_wrap = """    def derive_krdanta(
        self, dhatu: str, pratyaya: str = "kta", sanadi: Optional[str] = None,
        upasarga: Optional[str] = None, dhatu_id: Optional[str] = None
    ) -> Optional[Dict]:
        res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, "", dhatu_id)"""

new_wrap = """    def derive_krdanta(
        self, dhatu: str, pratyaya: str = "kta", sanadi: Optional[str] = None,
        upasarga: Optional[str] = None, dhatu_id: Optional[str] = None,
        _force_pada: Optional[str] = None
    ) -> Optional[Dict]:
        if upasarga and not _force_pada:
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass
        res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, "", dhatu_id, _force_pada)"""

content = content.replace(old_wrap, new_wrap)

# Fix derive_all_krdantas
old_all = """    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: Optional[str] = None, dhatu_id: Optional[str] = None
    ) -> Dict[str, Dict]:
        result = {}
        for prat in self.krdanta_metadata:
            res = self.derive_krdanta(dhatu, prat, sanadi, upasarga, dhatu_id=dhatu_id)"""

new_all = """    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: Optional[str] = None, dhatu_id: Optional[str] = None,
        _force_pada: Optional[str] = None
    ) -> Dict[str, Dict]:
        result = {}
        for prat in self.krdanta_metadata:
            res = self.derive_krdanta(dhatu, prat, sanadi, upasarga, dhatu_id=dhatu_id, _force_pada=_force_pada)"""

content = content.replace(old_all, new_all)

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)
print("Patched krdanta wrapper!")
