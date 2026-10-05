with open("pypanini/phonetics.py", "r") as f:
    lines = f.readlines()

# find where "# Let's explicitly block pari Satva" starts
idx = -1
for i, l in enumerate(lines):
    if "# Let's explicitly block pari Satva" in l:
        idx = i
        break

if idx != -1:
    lines = lines[:idx]
    
    new_code = """    # Revert unwanted Satva for pari + siD
    if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
        if "ziziD" not in form and "zizeD" not in form and "zizED" not in form and "zeziD" not in form:
            if "pariz" in form: form = form.replace("pariz", "paris")
    
    if dhatu_id in ("01.0049", "01.0050"):
        form = form.replace("aziziD", "asisiD").replace("azizeD", "asiseD").replace("azeziD", "asesiD")
        
    return form
"""
    with open("pypanini/phonetics.py", "w") as f:
        f.writelines(lines)
        f.write(new_code)
    print("Fixed brute 2!")
else:
    print("Could not find line!")
