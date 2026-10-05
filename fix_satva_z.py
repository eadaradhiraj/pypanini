with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

k = k.replace('if "z" in form: form = form.replace("z", "s")', 'if "zeD" in form or "ziD" in form: form = form.replace("zeD", "seD").replace("ziD", "siD")')

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed aggressive z revert!")
