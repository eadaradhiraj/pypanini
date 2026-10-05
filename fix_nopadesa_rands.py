with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

k = k.replace('("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard")', '("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard", "ARand", "iRand", "aRand", "aR", "AR", "iR")')

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed rands!")
