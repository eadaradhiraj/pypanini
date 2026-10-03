with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

import re

old_wrapper = """        # apply sandhi
        out = {}
        for k, v in res.items():
            if isinstance(v, list):
                out[k] = list(dict.fromkeys([apply_upasargas(upasarga, c) for c in v]))
            else:
                out[k] = apply_upasargas(upasarga, v)
        return out"""

new_wrapper = """        # apply sandhi
        out = {}
        for k, v in res.items():
            if k == "gender":
                out[k] = v
                continue
                
            if isinstance(v, list):
                new_v = []
                for c in v:
                    # Strip hardcoded "pra" or "saM" from legacy lyap cache/hacks
                    if pratyaya == "lyap" and c.startswith("pra") and not c.startswith("prac"):
                        c = c[3:]
                    elif pratyaya == "lyap" and c.startswith("saM"):
                        c = c[3:]
                    new_v.append(apply_upasargas(upasarga, c))
                out[k] = list(dict.fromkeys(new_v))
            else:
                c = v
                if pratyaya == "lyap" and c.startswith("pra") and not c.startswith("prac"):
                    c = c[3:]
                elif pratyaya == "lyap" and c.startswith("saM"):
                    c = c[3:]
                out[k] = apply_upasargas(upasarga, c)
        return out"""

content = content.replace(old_wrapper, new_wrapper)

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)
print("Patched krdanta wrapper 2")
