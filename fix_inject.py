with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

bad_block = """        cands, log = self._derive_inner(
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
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,"""
            
good_block = """        if prayoga == "kartari" and upasarga and not _force_pada:
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass
        cands, log = self._derive_inner(
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,"""

content = content.replace(bad_block, good_block)
with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Fixed injection order")
