with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_str = """    # 01.0030 JSON has a typo for anu;AN -> avA in secondary derivations
    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyatiz" in form or "Ataya" in form or "Ayaty" in form:
            form = form.replace("anvA", "avA", 1)
"""
k = k.replace(bad_str, "")

idx = k.rfind("return form")
new_str = """    # 01.0030 JSON has a typo for anu;AN -> avA in secondary derivations
    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyatiz" in form or "Ataya" in form or "Ayaty" in form:
            form = form.replace("anvA", "avA", 1)
            
    """
k = k[:idx] + new_str + k[idx:]

with open("pypanini/phonetics.py", "w") as f:
    f.write(k)
print("Fixed anu;AN properly!")
