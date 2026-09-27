import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    _yak_sann_stems.extend(["ciKyAs", "cikSAs"])"""

new_block = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    _yak_sann_stems = ["ciKyAs", "cikSAs"]"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
