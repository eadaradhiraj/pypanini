with open("pypanini/krdanta.py", "r") as f:
    k = f.read()

k = k.replace(
    'pada = meta["pada"]',
    'pada = _force_pada or meta["pada"]'
)

with open("pypanini/krdanta.py", "w") as f: f.write(k)
