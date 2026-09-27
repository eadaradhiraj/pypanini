import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """            if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                for _kb in ("cikraMs", "cikraMsi"):
                    if _kb not in alt_sann:
                        alt_sann.append(_kb)"""

new_block = """            if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                for _kb in ("cikraMs", "cikraMsi"):
                    if _kb not in alt_sann:
                        alt_sann.append(_kb)
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                alt_sann.extend(["ciKyAs", "cikSAs"])
                if lakara != "liw":
                    # For non-lit Ardhadhatuka, the replacement is mandatory.
                    s_stem = "ciKyAs" # we can leave cikSAs in alt_sann"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
