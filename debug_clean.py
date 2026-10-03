with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old = "def _yan_stem(c):"
new = "def _yan_stem(c):\n            print('YAN_STEM called with:', c)"
content = content.replace(old, new)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched yan_stem debug")
