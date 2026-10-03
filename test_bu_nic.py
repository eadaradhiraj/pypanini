import json
from pypanini import KrdantaEngine
ke = KrdantaEngine()

res_nic = ke.derive_all_krdantas("BU", sanadi="nijanta", upasarga="pra", dhatu_id="01.0001")
with open("skt-morph-data/01/01.0001.json", "r") as f:
    data = json.load(f)

expected_res = data["upasarga_forms"]["pra"]["participles"]["nich_krut"]

for prat, expected_list in expected_res.items():
    if not expected_list or expected_list == "-":
        continue
    gen = res_nic.get(prat, {})
    gen_strs = set()
    if isinstance(gen, dict):
        for k, v in gen.items():
            if isinstance(v, list):
                for x in v:
                    gen_strs.add(x)
                    gen_strs.update(x.split("/"))
            else:
                gen_strs.add(v)
                gen_strs.update(v.split("/"))
    elif isinstance(gen, list):
        for x in gen:
            gen_strs.add(x)
            gen_strs.update(x.split("/"))
    else:
        gen_strs.add(gen)
        gen_strs.update(gen.split("/"))
        
    for expected_item in expected_list:
        for k, expected_str in expected_item.items():
            if expected_str:
                for x in expected_str.split("/"):
                    if x not in gen_strs:
                        print(f"nich_krut | {prat} | Expected: {x} | Generated: {gen_strs}")
