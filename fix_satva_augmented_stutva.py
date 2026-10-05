with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O", "ev", "evi")):
                form = form[0] + "z" + form[2:]"""

new_block = """            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O", "ev", "evi")):
                z_core = core
                if z_core.startswith("t"): z_core = "w" + z_core[1:]
                elif z_core.startswith("T"): z_core = "W" + z_core[1:]
                elif z_core.startswith("n"): z_core = "R" + z_core[1:]
                form = form[0] + "z" + z_core"""

if old_block in k:
    k = k.replace(old_block, new_block)
    with open("pypanini/phonetics.py", "w") as f: f.write(k)
    print("Fixed augmented stutva!")
else:
    print("Block not found!")
