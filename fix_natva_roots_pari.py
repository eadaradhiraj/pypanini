with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_str = 'if p.endswith("r") or p.endswith("A") or p.endswith("a") or p.endswith("s"):'
new_str = 'if p.endswith("r") or p.endswith("A") or p.endswith("a") or p.endswith("s") or p.endswith("i"):'

k = k.replace(old_str, new_str)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pari!")
