with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O"))"""
new_block = """            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O", "ev", "evi"))"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed satva sev!")
