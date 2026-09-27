import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    n_stems_all.extend(["KyAy", "kSAy"])
                    n_stem = "KyAy" """

new_block = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    n_stems_all = ["KyAy", "kSAy"]
                    n_stem = "KyAy" """

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
