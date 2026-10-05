with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_1 = 'final_word = p_sandhi + "n" + root_start'
new_1 = 'final_word = p_sandhi + "n" + root_start.replace("R", "n")'
k = k.replace(old_1, new_1)

old_2 = 'final_word = p_aug + "n" + root_start'
new_2 = 'final_word = p_aug + "n" + root_start.replace("R", "n")'
k = k.replace(old_2, new_2)

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed root R!")
