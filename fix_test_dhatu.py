with open("tests/test_dhatu.py", "r") as f:
    content = f.read()
content = content.replace("if check_slot([item[\"form\"]]):", "cand = item[\"form\"] if isinstance(item[\"form\"], list) else [item[\"form\"]]\n                if check_slot(cand):")
with open("tests/test_dhatu.py", "w") as f: f.write(content)
print("Fixed test_dhatu.py")
