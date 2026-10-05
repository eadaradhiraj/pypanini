with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_str = """    if not prefix_str:
        # Double Satva for reduplicated sidh (01.0049 and 01.0050)
    if "zisiD" in form: form = form.replace("zisiD", "ziziD")
    if "ziseD" in form: form = form.replace("ziseD", "zizeD")
    
    if inner.endswith(("i", "u", "I", "U")):
        if "aseziD" in form: form = form.replace("aseziD", "azeziD")
        if "asisiD" in form: form = form.replace("asisiD", "aziziD")
        if "asesiD" in form: form = form.replace("asesiD", "azeziD")
        
    # Wait, 01.0049 (ziDa~) gets NO SATVA with pari! 
    # Actually, pari + ziDa~ = pariseDati, but ni + ziDa~ = nizeDati.
    # Let's explicitly block pari Satva for 01.0049 and 01.0050!
    if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
        # We need to revert Satva! 
        if "z" in form: form = form.replace("z", "s")
        
    return form"""

good_str = """    if not prefix_str:
        return form"""

k = k.replace(bad_str, good_str)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed indentation error!")
