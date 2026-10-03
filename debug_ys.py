with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

old = "ys = _yan_stem(clean)"
new = "ys = _yan_stem(clean)\n            print('YS IS', ys)"
content = content.replace(old, new)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
