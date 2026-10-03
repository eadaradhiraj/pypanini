import json

with open("pypanini/pada_map.json") as f:
    pada_map = json.load(f)

# Let's map it by dhatu_id AND clean dhatu
import glob
clean_map = {}
for dhatu_id in pada_map:
    # get clean dhatu for this id
    paths = glob.glob(f"skt-morph-data/*/{dhatu_id}.json")
    if paths:
        with open(paths[0]) as f:
            d = json.load(f)
            clean = next(x["value"] for x in d["info"] if x["name"] == "OpadeSikasvarUpam")
            from pypanini import clean_dhatu_op
            clean = clean_dhatu_op(clean)
            if clean not in clean_map:
                clean_map[clean] = pada_map[dhatu_id]
            else:
                # Merge
                for k, v in pada_map[dhatu_id].items():
                    clean_map[clean][k] = v

with open("pypanini/pada_rules.py", "w") as f:
    f.write("PADA_MAP_ID = " + repr(pada_map) + "\n")
    f.write("PADA_MAP_CLEAN = " + repr(clean_map) + "\n")

print("Created pada_rules.py")

with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import_str = "from .phonetics import apply_upasargas\nfrom .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN"
content = content.replace("from .phonetics import apply_upasargas", import_str)

wrapper_logic = """        _sad_c10_recurse: bool = False,
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

        res, log = self._derive_inner("""

content = content.replace("""        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
        res, log = self._derive_inner(""", wrapper_logic)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched tinanta.py")
