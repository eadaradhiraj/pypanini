import json
from pypanini import KrdantaEngine
ke = KrdantaEngine()

# derive krdantas for hu with pra
res_base = ke.derive_all_krdantas("hu", upasarga="pra", dhatu_id="03.0001")
res_san = ke.derive_all_krdantas("hu", sanadi="sannanta", upasarga="pra", dhatu_id="03.0001")
res_nic = ke.derive_all_krdantas("hu", sanadi="nijanta", upasarga="pra", dhatu_id="03.0001")
res_yan = ke.derive_all_krdantas("hu", sanadi="yananta", upasarga="pra", dhatu_id="03.0001")
res_ylk = ke.derive_all_krdantas("hu", sanadi="yanluganta", upasarga="pra", dhatu_id="03.0001")

engine_res = {
    "krut": res_base,
    "san_krut": res_san,
    "nich_krut": res_nic,
    "yang_krut": res_yan,
    "yangluk_krut": res_ylk
}

with open("skt-morph-data/03/03.0001.json", "r") as f:
    data = json.load(f)

expected_res = data["upasarga_forms"]["pra"]["participles"]

for anta, forms in expected_res.items():
    engine_forms = engine_res[anta]
    for prat, expected_list in forms.items():
        if not expected_list or expected_list == "-":
            continue
            
        gen = engine_forms.get(prat, {})
        # Extract generated strings
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
            
        # Extract expected strings
        for expected_item in expected_list:
            for k, expected_str in expected_item.items():
                if expected_str:
                    for x in expected_str.split("/"):
                        if x not in gen_strs:
                            print(f"{anta} | {prat} | Expected: {x} | Generated: {gen_strs}")
