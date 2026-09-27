import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """        if sanadi == "yananta":
            ys = _yan_stem(clean)
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                ys = "cAKyAy"  # only one stem needed for the sweep to pass, or should we do cAkSAy too?
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem"""

new_block = """        if sanadi == "yananta":
            ys = _yan_stem(clean)
            _cakz_yan_alt = []
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                if lakara == "liw":
                    _cakz_yan_alt = ["cAKyAy", "cAkSAy"]
                else:
                    ys = "cAKyAy"
                    _cakz_yan_alt = ["cAkSAy"]
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("Could not find block 1")

old_block2 = """            # Surveyed zWiv perfect paradigm (we-/te- redup × i-grade); additive list, consumed per-branch below.
            _yan_perf = []
            if clean == "zWiv":
                _yan_perf = ["wezWiv", "tezWiv"]"""

new_block2 = """            # Surveyed zWiv perfect paradigm (we-/te- redup × i-grade); additive list, consumed per-branch below.
            _yan_perf = []
            if clean == "zWiv":
                _yan_perf = ["wezWiv", "tezWiv"]
            _yan_perf.extend(_cakz_yan_alt)"""

if old_block2 in content:
    content = content.replace(old_block2, new_block2)
else:
    print("Could not find block 2")

with open('pypanini/tinanta.py', 'w') as f:
    f.write(content)
print("Patched successfully")
