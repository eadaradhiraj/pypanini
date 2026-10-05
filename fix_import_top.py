import re

for filename in ["pypanini/tinanta.py", "pypanini/krdanta.py"]:
    with open(filename, "r") as f:
        content = f.read()
    
    # Remove local import
    content = content.replace("            from pypanini.pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN\n", "")
    content = content.replace("            from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN\n", "")
    
    # Add top-level import
    if "PADA_MAP_ID" not in content[:500]:
        content = "from pypanini.pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN\n" + content
        
    with open(filename, "w") as f:
        f.write(content)
print("Fixed!")
