import sys

with open("tests/test_dhatu.py", "r") as f:
    content = f.read()

# Fix all_tokens assignment
repl_old = """    all_tokens = extract_all_text_tokens(data)"""
repl_new = """    if prefix:
        all_tokens = extract_all_text_tokens(data["upasarga_forms"][prefix])
    else:
        all_tokens = extract_all_text_tokens(data)"""

content = content.replace(repl_old, repl_new)

with open("tests/test_dhatu.py", "w") as f:
    f.write(content)
print("Patched all_tokens")
