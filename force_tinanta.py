with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import_str = "from .phonetics import apply_upasargas\nfrom .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN"
if "PADA_MAP_ID" not in content:
    content = content.replace("from .phonetics import apply_upasargas", import_str)

def inject_after(target, injection):
    if target in content and injection not in content:
        return content.replace(target, target + "\n" + injection)
    return content

target = """    ) -> Tuple[List[str], List[str]]:
        cands, log = self._derive_inner("""
        
injection = """        if prayoga == "kartari" and upasarga and not _force_pada:
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass"""
                
content = inject_after(target, injection)
with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Forced tinanta.py patch")
