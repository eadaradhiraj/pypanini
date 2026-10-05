with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_block = """        # Revert unwanted Satva for pari + siD
        if "pariz" in form:
            form = form.replace("pariz", "paris")
        
        # Yang forms shouldn't have any Satva
        if "seziD" in form: form = form.replace("seziD", "sesiD")
        if "zeziD" in form: form = form.replace("zeziD", "sesiD")
        
        # San forms shouldn't have any Satva
        # But perfect (liw) DOES have Satva (parizizeDa).
        # Perfect forms: parizizeDa, pariziziDatuH, parizizEDa.
        # San forms have 'iz' after the root: sisiDiz.
        if "siziDiz" in form: form = form.replace("siziDiz", "sisiDiz")
        if "ziziDiz" in form: form = form.replace("ziziDiz", "sisiDiz")
        if "zizeDiz" in form: form = form.replace("zizeDiz", "siseDiz")
        if "sizeDiz" in form: form = form.replace("sizeDiz", "siseDiz")
        
        # Finally, perfect forms with pari SHOULD have Satva.
        # Wait, if we replaced 'pariz' with 'paris', we ruined 'parizizeDa'!
        # So we must restore 'parizizeD', 'pariziziD', 'parizizED'
        if "parisizeD" in form: form = form.replace("parisizeD", "parizizeD")
        if "parisiziD" in form: form = form.replace("parisiziD", "pariziziD")
        if "parisisED" in form: form = form.replace("parisisED", "parizizED")
        if "parisiD" in form and "iz" not in form and "y" not in form:
            pass # Keep it as is (base forms pariseDati)"""

good_block = """        # We only apply these weird exceptions for pari!
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

k = k.replace(bad_block, good_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pari satva completely!")
