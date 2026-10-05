with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# Replace the blind .replace("R", "n") with specific root fixes
old_str = 'final_word = p_sandhi + "n" + root_start.replace("R", "n")'
new_str = 'final_word = p_sandhi + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand")'
k = k.replace(old_str, new_str)

old_str2 = 'final_word = p_aug + "n" + root_start.replace("R", "n")'
new_str2 = 'final_word = p_aug + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand")'
k = k.replace(old_str2, new_str2)

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed clobber!")
with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

new_replace = '.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand").replace("aRaw", "anaw").replace("iRind", "inind").replace("aRard", "anard").replace("aRfc", "anfc").replace("aRrt", "anrt")'

k = k.replace('.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand")', new_replace)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed more roots!")
