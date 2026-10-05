with open("pypanini/tinanta.py", "r") as f:
    content = f.read()
content = content.replace("cands = [apply_upasargas(upasarga, c) for c in cands]", "cands_new = []\n            for c in cands:\n                res = apply_upasargas(upasarga, c)\n                if isinstance(res, list): cands_new.extend(res)\n                else: cands_new.append(res)\n            cands = cands_new")
with open("pypanini/tinanta.py", "w") as f: f.write(content)

with open("pypanini/krdanta.py", "r") as f:
    content = f.read()
content = content.replace("new_v.append(apply_upasargas(upasarga, c))", "res = apply_upasargas(upasarga, c)\n                    if isinstance(res, list): new_v.extend(res)\n                    else: new_v.append(res)")
content = content.replace("out[k] = apply_upasargas(upasarga, c)", "res = apply_upasargas(upasarga, c)\n                out[k] = res if isinstance(res, list) else [res]")
with open("pypanini/krdanta.py", "w") as f: f.write(content)
print("Wrappers fixed!")
