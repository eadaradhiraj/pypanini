with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old = "            ys = _yan_stem(clean)\n"
new = "            ys = _yan_stem(clean)\n            print('YS IS:', ys)\n"
content = content.replace(old, new)
with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
