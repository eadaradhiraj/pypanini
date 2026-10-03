with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

# Fix the call in the wrapper
old_call = "res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, None, dhatu_id)"
new_call = "res = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, \"\", dhatu_id)"

content = content.replace(old_call, new_call)

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)
print("Patched to pass empty string")
