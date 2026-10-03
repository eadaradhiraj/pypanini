import json
import glob
import os

out = {}

for fpath in glob.glob("skt-morph-data/*/*.json"):
    if "skt-morph-data/data" in fpath: continue # duplicate or wrong
    dhatu_id = os.path.basename(fpath).replace(".json", "")
    with open(fpath) as f:
        data = json.load(f)
    
    # Base pada?
    base_ting = data.get("conjugations", {}).get("ting", {})
    base_pada = set()
    for k in base_ting.keys():
        if k.startswith("p"): base_pada.add("parasmEpadi")
        elif k.startswith("a"): base_pada.add("Atmanepadi")
    
    if "parasmEpadi" in base_pada and "Atmanepadi" in base_pada:
        base_pada_str = "uBayapadi"
    elif "parasmEpadi" in base_pada:
        base_pada_str = "parasmEpadi"
    elif "Atmanepadi" in base_pada:
        base_pada_str = "Atmanepadi"
    else:
        base_pada_str = None

    upasarga_forms = data.get("upasarga_forms", {})
    for up, up_data in upasarga_forms.items():
        ting = up_data.get("conjugations", {}).get("ting", {})
        up_pada = set()
        for k in ting.keys():
            if k.startswith("p"): up_pada.add("parasmEpadi")
            elif k.startswith("a"): up_pada.add("Atmanepadi")
        
        if "parasmEpadi" in up_pada and "Atmanepadi" in up_pada:
            up_pada_str = "uBayapadi"
        elif "parasmEpadi" in up_pada:
            up_pada_str = "parasmEpadi"
        elif "Atmanepadi" in up_pada:
            up_pada_str = "Atmanepadi"
        else:
            up_pada_str = None
            
        if up_pada_str and up_pada_str != base_pada_str:
            if dhatu_id not in out:
                out[dhatu_id] = {}
            out[dhatu_id][up] = up_pada_str

print(f"Found overrides for {len(out)} roots.")
with open("pypanini/pada_map.json", "w") as f:
    json.dump(out, f, indent=2)
