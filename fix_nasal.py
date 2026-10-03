with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

content = content.replace('or pada == "Atmanepadi"', 'or (pada == "Atmanepadi" and _force_pada is None)')

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched nasal logic")
