with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old_wrapper = """    ) -> Tuple[List[str], List[str]]:
        cands, log = self._derive_inner(
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,
            _force_pada, _cakz_bypass
        )"""

new_wrapper = """    ) -> Tuple[List[str], List[str]]:
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
        cands, log = self._derive_inner(
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,
            _force_pada, _cakz_bypass
        )"""

if old_wrapper in content:
    content = content.replace(old_wrapper, new_wrapper)
    with open("pypanini/tinanta.py", "w") as f:
        f.write(content)
    print("Added pada override to wrapper")
else:
    print("FAILED TO FIND TARGET STRING")
