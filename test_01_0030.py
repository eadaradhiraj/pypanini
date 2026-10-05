import json
from pypanini import KrdantaEngine, clean_dhatu_op

with open("skt-morph-data/01/01.0030.json") as f:
    data = json.load(f)

expected = data["upasarga_forms"]["anu;AN"]["participles"]["nich_krut"]
ke = KrdantaEngine()
dhatu = clean_dhatu_op("yatI~")

out = ke.derive_all_krdantas(dhatu, sanadi="nijanta", upasarga="anu;AN", dhatu_id="01.0030")

for k, evs in expected.items():
    if k not in out:
        print("Missing krudanta:", k)
        continue
        
    for ev in evs:
        for g in [("m", "M"), ("f", "F"), ("n", "N")]:
            e_val = ev.get(g[0], "")
            if e_val and e_val != "-":
                # check if e_val in our output
                if g[1] in out[k]:
                    ov = out[k][g[1]]
                    if isinstance(ov, str): ov = [ov]
                    if not any(e == v for e in e_val.split("/") for v in ov):
                        print(f"Fail: {k} {g[0]} -> Expected {e_val}, Got {ov}")
                elif "avyaya" in out[k]:
                    ov = out[k]["avyaya"]
                    if isinstance(ov, str): ov = [ov]
                    if not any(e == v for e in e_val.split("/") for v in ov):
                        print(f"Fail: {k} {g[0]} -> Expected {e_val}, Got {ov}")

