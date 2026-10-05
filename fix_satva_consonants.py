import re

with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    if inner.endswith(("i", "u", "I", "U")):
        if form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
            if not form.startswith("sf"):
                form = "z" + form[1:]"""

new_block = """    if inner.endswith(("i", "u", "I", "U")):
        if form.startswith("s") and len(form) > 1:
            if form[1] in "aAiIuUfFeEoOyvr" and not form.startswith("sf"):
                form = "z" + form[1:]
            elif form.startswith("st"):
                form = "zw" + form[2:]
            elif form.startswith("sT"):
                form = "zW" + form[2:]
            elif form.startswith("sn"):
                form = "zR" + form[2:]"""

if old_block in k:
    k = k.replace(old_block, new_block)
    with open("pypanini/phonetics.py", "w") as f: f.write(k)
    print("Fixed satva for consonants st, sT, sn!")
else:
    print("Block not found!")
