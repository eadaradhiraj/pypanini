import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """            # Use first as n_stem for backward compat, but will generate for all below
            is_atman = (pada == "Atmanepadi")
            # For the per-lakara handling below, we will need to handle multiple n_stems"""

new_block = """            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                if lakara == "liw":
                    n_stems.extend(["KyAy", "kSAy"])
                else:
                    n_stems = ["KyAy", "kSAy"]
            # Use first as n_stem for backward compat, but will generate for all below
            is_atman = (pada == "Atmanepadi")
            # For the per-lakara handling below, we will need to handle multiple n_stems"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
