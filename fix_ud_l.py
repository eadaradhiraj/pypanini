with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    if p_end == "d" and prefix == "ud":
        if form.startswith("sT"): return "utT" + form[2:]
        if form.startswith("sw"): return "uww" + form[2:] 
        if f_start in "cC": return "uc" + form
        if f_start in "jJ": return "uj" + form
        if f_start in "wW": return "uw" + form
        if f_start in "nNmMYR": return "un" + form"""

new_block = """    if p_end == "d" and prefix == "ud":
        if form.startswith("sT"): return "utT" + form[2:]
        if form.startswith("sw"): return "uww" + form[2:] 
        if f_start in "cC": return "uc" + form
        if f_start in "jJ": return "uj" + form
        if f_start in "wW": return "uw" + form
        if f_start in "nNmMYR": return "un" + form
        if f_start == "l": return "ul" + form"""

if old_block in k:
    k = k.replace(old_block, new_block)
    with open("pypanini/phonetics.py", "w") as f: f.write(k)
    print("Fixed tor li!")
