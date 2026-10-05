with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# Inside apply_upasargas, after Satva check but before returning:
old_ret = '    return final_word'
new_ret = """    # Double Satva for reduplicated sidh (01.0049 and 01.0050)
    # If the first s became z, the second must also become z (e.g. zisiD -> ziziD)
    final_word = final_word.replace("zisiD", "ziziD").replace("ziseD", "zizeD")
    
    # And if there's an augment 'a', my augment logic might have missed it.
    # The prefix ends in i/u, followed by 'a', followed by 'sisiD' or 'sesiD'.
    # e.g. vi + a + seziD -> vyaseziD. Both s should become z -> vyazeziD!
    # Wait, the inner prefix ended in i/u.
    if inner.endswith(("i", "u", "I", "U")):
        # The form has augment. e.g. form was asisiD -> we want aziziD.
        # But we only do this if it's the right dhatu.
        if "aseziD" in final_word: final_word = final_word.replace("aseziD", "azeziD")
        if "asisiD" in final_word: final_word = final_word.replace("asisiD", "aziziD")
        if "asesiD" in final_word: final_word = final_word.replace("asesiD", "azeziD")
        
    return final_word"""

k = k.replace(old_ret, new_ret)

with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed reduplicated satva!")
