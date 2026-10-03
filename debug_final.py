with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old = "return list(dict.fromkeys(cands)), log"
new = "print('CANDS ARE', cands); return list(dict.fromkeys(cands)), log"
content = content.replace(old, new)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
