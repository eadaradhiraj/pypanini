with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old = "ys = _yan_stem(clean)"
new = "print('CLEAN IS', clean); ys = _yan_stem(clean)"
content = content.replace(old, new)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
