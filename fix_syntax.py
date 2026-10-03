with open("pypanini/tinanta.py", "r") as f:
    lines = f.readlines()

out = []
for i, line in enumerate(lines):
    if "_sad_c10_recurse: bool = False," in line and i > 0 and lines[i-1] == line:
        continue
    out.append(line)

with open("pypanini/tinanta.py", "w") as f:
    f.writelines(out)
