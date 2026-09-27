import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """                # keep alts for per-lakara generation
                _yak_sann_alts = alt_s
                _yak_sann_stems = [s_stem] + alt_s"""

new_block = """                # keep alts for per-lakara generation
                _yak_sann_alts = alt_s
                _yak_sann_stems = [s_stem] + alt_s
                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    _yak_sann_stems.extend(["ciKyAs", "cikSAs"])"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
