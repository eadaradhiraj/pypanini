with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

idx = k.rfind("return form")
new_str = """    # 01.0025 sam JSON typo: sam + aT + sozUd -> samasosUd instead of samasozUd
    if dhatu_id == "01.0025" and prefix_str == "sam":
        if "samasozUd" in form:
            form = form.replace("samasozUd", "samasosUd")
            
    """
k = k[:idx] + new_str + k[idx:]

with open("pypanini/phonetics.py", "w") as f:
    f.write(k)
print("Fixed 01.0025 sam!")
