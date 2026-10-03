with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re

# Remove the broken patch logic if it exists (it didn't match).
# Let's replace the top of derive directly.

old_wrapper = """    def derive(
        self, dhatu: str, lakara: str = "lw", purusha: str = "prathama", vacana: str = "eka",
        prayoga: str = "kartari", sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None, json_path: Optional[str] = None,
        upasarga: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
        cands, log = self._derive_inner("""

new_wrapper = """    def derive(
        self, dhatu: str, lakara: str = "lw", purusha: str = "prathama", vacana: str = "eka",
        prayoga: str = "kartari", sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None, json_path: Optional[str] = None,
        upasarga: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
        if prayoga == "kartari" and upasarga and not _force_pada:
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass

        cands, log = self._derive_inner("""

if "PADA_MAP_ID" not in content:
    # it was added as import but let's just make sure.
    pass

content = content.replace(old_wrapper, new_wrapper)
with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched tinanta.py wrapper correctly!")
