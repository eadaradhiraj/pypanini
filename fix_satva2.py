with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    inner = prefixes[-1]
    if inner.endswith(("i", "u", "I", "U")) and form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
        # Some roots resist this (e.g. sfp, sfj, etc.) but we apply a broad approximation first.
        # Let's skip 'sf' roots for now, they are notoriously complex. 
        if not form.startswith("sf"):
            form = "z" + form[1:]"""

new_block = """    inner = prefixes[-1]
    if inner.endswith(("i", "u", "I", "U")):
        if form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
            if not form.startswith("sf"):
                form = "z" + form[1:]
        elif (form.startswith("a") or form.startswith("A")) and len(form) > 2 and form[1] == "s":
            core = form[2:]
            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O")):
                form = form[0] + "z" + form[2:]"""

if old_block in k:
    k = k.replace(old_block, new_block)
    with open("pypanini/phonetics.py", "w") as f: f.write(k)
    print("Fixed satva properly!")
else:
    print("Failed to find block!")
