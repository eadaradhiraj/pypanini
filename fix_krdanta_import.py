with open("pypanini/krdanta.py", "r") as f:
    content = f.read()

# Revert the bad replacement
content = content.replace("apply_sandhi_eco_ayavayavah, apply_upasargas", "apply_sandhi_eco_ayavayavah")

# Only replace the import statement!
import_stmt = "from .phonetics import apply_guna, apply_vriddhi, apply_sandhi_eco_ayavayavah"
new_import = "from .phonetics import apply_guna, apply_vriddhi, apply_sandhi_eco_ayavayavah, apply_upasargas"
content = content.replace(import_stmt, new_import)

with open("pypanini/krdanta.py", "w") as f:
    f.write(content)
print("Fixed krdanta import")
