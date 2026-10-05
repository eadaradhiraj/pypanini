with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

k = k.replace('("and", "anand", "aw", "An", "fd", "rt", "ind", "fc", "ard")', '("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard")')

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed inand!")
