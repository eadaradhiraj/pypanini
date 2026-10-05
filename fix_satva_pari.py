with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# I will replace the strict `pari` Satva block with one that ONLY blocks if there's no augment.
old_block = """    if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
        # We need to revert Satva! 
        if "zeD" in form or "ziD" in form: form = form.replace("zeD", "seD").replace("ziD", "siD")"""

new_block = """    if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
        # pari + siDati -> pariseDati (No Satva)
        # But pary + a + saD -> paryazeDat (Satva!)
        # So we only revert Satva if the prefix is exactly 'pari' directly attached to 's'
        # The form string here already has the prefix attached.
        # If the form contains 'pari', we revert. If it contains 'parya', we KEEP Satva!
        if "pariz" in form: 
            form = form.replace("pariz", "paris")
            # And also revert any internal zisiD to sisiD since it lost Satva
            form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD")"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pari satva exception!")
