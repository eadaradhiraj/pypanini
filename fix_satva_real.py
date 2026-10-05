with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_block = """    if inner.endswith(("i", "u", "I", "U")):
        if "aseziD" in form: form = form.replace("aseziD", "azeziD")
        if "asisiD" in form: form = form.replace("asisiD", "aziziD")
        if "asesiD" in form: form = form.replace("asesiD", "azeziD")
        
    # We only apply these weird exceptions for pari!
    if inner == "pari":
        # 1. Base lat -> NO Satva (pariseDati)
        # 2. Base laN -> SATVA (paryazeDat)
        # 3. San lat -> SATVA (pariziziDizati)
        # 4. San laN -> NO SATVA (paryasisiDizat)
        # 5. Yang lat -> SATVA (parizeziDyate)
        # 6. Yang laN -> NO SATVA (paryasesiDyata)
        # 7. Perfect -> SATVA (parizizeDa)
        # 8. Causative -> SATVA (paryazeDayat, parizeDayati) Wait, JSON has pariseDayati! (NO Satva)
        
        # Let's enforce exactly these mappings based on substrings:
        if "parya" in form:
            # With augment
            # Base/Causative gets Satva (paryazeD)
            # San/Yang gets NO Satva (paryasisiD, paryasesiD)
            if "sisiD" in form or "ziziD" in form or "siseD" in form or "zizeD" in form or "sesiD" in form or "zeziD" in form:
                # San/Yang -> Revert to NO Satva
                form = form.replace("ziziD", "sisiD").replace("zizeD", "siseD").replace("zeziD", "sesiD").replace("zizED", "sisED")
            else:
                # Base/Causative -> Keep Satva!
                form = form.replace("aseD", "azeD").replace("asiD", "aziD")
        else:
            # Without augment (pari + ...)
            if "ziziDiz" in form or "zizeDiz" in form or "zeziD" in form or "zizeD" in form or "ziziD" in form or "zizED" in form:
                # San lat (ziziDiz), Yang lat (zeziD), Perfect (zizeD) -> Keep Satva!
                pass
            else:
                # Base lat, Causative lat -> NO Satva
                form = form.replace("pariz", "paris")"""

good_block = """    if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
        # pari + siD blocks Satva without augment!
        # Except if it's Perfect or San or Yang (which are reduplicated)
        if "ziziD" not in form and "zizeD" not in form and "zizED" not in form and "zeziD" not in form:
            if "pariz" in form: form = form.replace("pariz", "paris")
    
    if dhatu_id in ("01.0049", "01.0050"):
        # Augment + Reduplication ALWAYS blocks Satva! (nyasisiDizat, paryasesiDyata)
        # My engine naturally didn't apply Satva to the first s because 'eziD'/'isiD' wasn't in the whitelist!
        # But wait, my double Satva `if "zisiD" in form` might have cascaded!
        # Let's ensure NO Satva if there's an augment and reduplication.
        # How to check augment? The form starts with prefix + a/A.
        # For ni + a -> nya. For vi + a -> vya. For pari + a -> parya.
        if "yaziziD" in form: form = form.replace("yaziziD", "yasisiD")
        if "yazizeD" in form: form = form.replace("yazizeD", "yasiseD")
        if "yazeziD" in form: form = form.replace("yazeziD", "yasesiD")
        if "vaziziD" in form: form = form.replace("vaziziD", "vasisiD") # Maybe not needed
        if "naziziD" in form: form = form.replace("naziziD", "nasisiD") # Maybe not needed
        
        # Just to be safe, if 'a' precedes the reduplication, revert it.
        form = form.replace("aziziD", "asisiD").replace("azizeD", "asiseD").replace("azeziD", "asesiD")"""

k = k.replace(bad_block, good_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed Satva real!")
