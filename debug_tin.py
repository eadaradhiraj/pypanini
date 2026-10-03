with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

import re
old = "if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:\n                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]"
new = "if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:\n                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]\n                print('PADA OVERRIDE HIT:', _force_pada)"
content = content.replace(old, new)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Added print statement")
