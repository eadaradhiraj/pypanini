with open("pypanini/krdanta.py", "r") as f:
    k = f.read()

k = k.replace(
    'is_atman_eligible = ((pada == "Atmanepadi" and _force_pada is None)) or ("uBaya" in padam)',
    'is_atman_eligible = (pada == "Atmanepadi") or ("uBaya" in padam)'
)

with open("pypanini/krdanta.py", "w") as f: f.write(k)
