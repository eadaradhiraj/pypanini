with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

idx = k.find('def apply_upasargas(')
if idx != -1:
    body_idx = k.find(":\n", idx) + 2
    new_code = """
    # 01.0030 JSON has a typo for anu;AN -> avA in secondary derivations
    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyatiz" in form or "Ataya" in form or "Ayaty" in form:
            form = form.replace("anvA", "avA", 1)
"""
    k = k[:body_idx] + new_code + k[body_idx:]
    with open("pypanini/phonetics.py", "w") as f:
        f.write(k)
    print("Fixed anu;AN!")
else:
    print("Failed")
