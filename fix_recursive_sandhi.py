with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

old_code = """    prefixes = upasargas_str.split(";")
    if len(prefixes) > 1:
        for prefix in reversed(prefixes):
            form = apply_upasargas(prefix, form)
        return form"""

new_code = """    prefixes = upasargas_str.split(";")
    if len(prefixes) > 1:
        forms = [form]
        for prefix in reversed(prefixes):
            new_forms = []
            for f in forms:
                res = apply_upasargas(prefix, f)
                if isinstance(res, list): new_forms.extend(res)
                else: new_forms.append(res)
            forms = new_forms
        return forms"""

content = content.replace(old_code, new_code)
with open("pypanini/phonetics.py", "w") as f: f.write(content)
print("Fixed recursive sandhi!")
