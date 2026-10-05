with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_block = """        if "pariz" in form: 
            # Revert Satva ONLY IF there is no reduplication!
            if "ziziD" not in form and "zizeD" not in form and "zizED" not in form:
                form = form.replace("pariz", "paris")
                form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD").replace("ziziD", "sisiD").replace("zizeD", "siseD").replace("zizED", "sisED")"""

# Let's replace the block entirely with a smart string matcher
good_block = """        # Revert unwanted Satva for pari + siD
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

k = k.replace(bad_block, good_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pari satva cleanup!")
