import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

# Fix nich
old_nich = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    n_stems_all = ["KyAy", "kSAy"]
                    n_stem = "KyAy" """

new_nich = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    if lakara == "liw":
                        n_stems_all.extend(["KyAy", "kSAy"])
                    else:
                        n_stems_all = ["KyAy", "kSAy"]
                        n_stem = "KyAy" """

content = content.replace(old_nich, new_nich)

# Fix san_yak
old_sy = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    _yak_sann_stems = ["ciKyAs", "cikSAs"]"""

new_sy = """                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    if lakara == "liw":
                        _yak_sann_stems.extend(["ciKyAs", "cikSAs"])
                    else:
                        _yak_sann_stems = ["ciKyAs", "cikSAs"]"""

content = content.replace(old_sy, new_sy)

with open('pypanini/tinanta.py', 'w') as f:
    f.write(content)
print("Patched successfully")
