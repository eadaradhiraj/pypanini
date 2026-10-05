with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    if inner in ("pra", "parA", "nir", "antar", "pari") and form.startswith("n"):
        form = "R" + form[1:]"""

new_block = """    if inner in ("pra", "parA", "nir", "antar", "pari") and form.startswith("n"):
        if not form.startswith(("nand", "nfd", "nfc", "nrt", "nard", "naw", "nA", "nind")):
            form = "R" + form[1:]"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed nopadesa pre-sandhi natva!")
