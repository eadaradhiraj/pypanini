import re

with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

old_block = """                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    # curAdi nich SAnac mUla-delegation (mUla grades + base + ay-twin; additive)."""

new_block = """                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    
                    _ay_base = sec + "amAna"
                    if (_natva_applies(orig_clean) or _natva_applies(sec)) and _ay_base.endswith("amAna"):
                        _ay_base = _ay_base[:-5] + "amARa"
                        
                    _ay_m = _ay_base + "H"
                    _ay_f = _ay_base[:-1]+"A" if _ay_base.endswith("a") else _ay_base+"A"
                    _ay_n = _ay_base + "m"
                    
                    m = [m, _ay_m]
                    f = [f, _ay_f]
                    n = [n, _ay_n]
                    
                    # curAdi nich SAnac mUla-delegation (mUla grades + base + ay-twin; additive)."""

content = content.replace(old_block, new_block)

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)

print("Patched nijanta SAnac!")
