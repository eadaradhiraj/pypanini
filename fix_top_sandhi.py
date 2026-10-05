with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

old_code = """def apply_upasargas(upasargas_str: str, form: str) -> str:
    if not upasargas_str or not form:
        return form"""

new_code = """def apply_upasargas(upasargas_str: str, form: str):
    if not upasargas_str or not form:
        return form
    if isinstance(form, list):
        out = []
        for f in form:
            res = apply_upasargas(upasargas_str, f)
            if isinstance(res, list): out.extend(res)
            else: out.append(res)
        return out"""

content = content.replace(old_code, new_code)
with open("pypanini/phonetics.py", "w") as f: f.write(content)
print("Fixed top sandhi!")
