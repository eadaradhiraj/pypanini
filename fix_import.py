with open("pypanini/tinanta.py", "r") as f:
    t = f.read()
t = t.replace("from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN", "from pypanini.pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN")
with open("pypanini/tinanta.py", "w") as f: f.write(t)

with open("pypanini/krdanta.py", "r") as f:
    k = f.read()
k = k.replace("from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN", "from pypanini.pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN")
with open("pypanini/krdanta.py", "w") as f: f.write(k)
