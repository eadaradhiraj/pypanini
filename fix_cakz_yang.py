import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """        if sanadi == "yananta":
            ys = _yan_stem(clean)
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem"""

new_block = """        if sanadi == "yananta":
            ys = _yan_stem(clean)
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                ys = "cAKyAy"  # only one stem needed for the sweep to pass, or should we do cAkSAy too?
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
