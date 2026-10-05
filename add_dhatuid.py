with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

k = k.replace("def apply_upasargas(prefix_str: str, form: str) -> str:", "def apply_upasargas(prefix_str: str, form: str, dhatu_id: str = None) -> str:")
k = k.replace("return \"/\".join(apply_upasargas(prefix_str, f.strip()) for f in form.split(\"/\"))", "return \"/\".join(apply_upasargas(prefix_str, f.strip(), dhatu_id) for f in form.split(\"/\"))")

# Add the bypass logic for 01.0450
bypass_logic = """    inner = prefixes[-1]
    
    if dhatu_id == "01.0450":
        # ziDu~ gatyAm does NOT get Satva with any prefix!
        pass
    elif inner.endswith(("i", "u", "I", "U"))"""

k = k.replace("    inner = prefixes[-1]\n    if inner.endswith((\"i\", \"u\", \"I\", \"U\"))", bypass_logic)

with open("pypanini/phonetics.py", "w") as f: f.write(k)

with open("pypanini/tinanta.py", "r") as f:
    t = f.read()
t = t.replace("cands = [apply_upasargas(upasarga, c) for c in cands]", "cands = [apply_upasargas(upasarga, c, d_id) for c in cands]")
with open("pypanini/tinanta.py", "w") as f: f.write(t)

with open("pypanini/krdanta.py", "r") as f:
    krd = f.read()
krd = krd.replace("new_v.append(apply_upasargas(upasarga, c))", "new_v.append(apply_upasargas(upasarga, c, dhatu_id))")
krd = krd.replace("out[k] = apply_upasargas(upasarga, c)", "out[k] = apply_upasargas(upasarga, c, dhatu_id)")
with open("pypanini/krdanta.py", "w") as f: f.write(krd)

print("Added dhatu_id plumbing!")
