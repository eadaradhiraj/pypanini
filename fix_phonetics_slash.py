with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

# We need to change `apply_upasargas` to distribute over slashes.
old_func = """def apply_upasargas(prefix_str: str, form: str) -> str:
    \"\"\"
    Applies one or more upasargas (separated by ';') to a given word form.
    It recursively handles inner-to-outer sandhi. 
    It also applies basic Natva and Satva on the boundary.
    \"\"\"
    if not prefix_str:
        return form"""

new_func = """def apply_upasargas(prefix_str: str, form: str) -> str:
    \"\"\"
    Applies one or more upasargas (separated by ';') to a given word form.
    It recursively handles inner-to-outer sandhi. 
    It also applies basic Natva and Satva on the boundary.
    \"\"\"
    if not prefix_str:
        return form
        
    if "/" in form:
        return "/".join(apply_upasargas(prefix_str, f.strip()) for f in form.split("/"))
"""
content = content.replace(old_func, new_func)

with open("pypanini/phonetics.py", "w") as f:
    f.write(content)
print("Patched apply_upasargas for slashes")
