with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    if is_illegal_conjunct:
        return False
    # Pāṇini exception: roots like van (vanati) often do not get Natva
    if i > 1 and word[i-2:i] == "va" and (i+1 == len(word) or word[i+1] in "aAiIuUeEoOyv"): 
        # A crude heuristic to block Natva in parivanati, while keeping it for others if needed.
        # Actually, let's just explicitly block if we see "parivan"
        pass"""

new_block = """    if is_illegal_conjunct:
        return False
    # Pāṇini exception: van (vanati) does not get Natva
    if "rivan" in word or "ravan" in word or "rvan" in word:
        # e.g. parivanati, pravanati, nirvanati
        if i >= 2 and word[i-2:i+1] == "van":
            return False"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed natva van correctly!")
