import re
with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# I will replace `def apply_natva(word: str) -> str:` with a wrapper that checks exceptions
old_block = """def apply_natva(word: str) -> str:
    out = []"""

new_block = """def apply_natva(word: str) -> str:
    # Pāṇinian exceptions for Natva
    # If the root is one of the following, do not change its initial 'n' to 'R', or 'van' to 'vaR'
    # Actually, we can just return the word if it matches these specific prefix+root combos to be safe.
    # But since natva might apply inside the suffix (e.g. pari + nand + ana -> parinandana), 
    # we just replace the specific root substring temporarily, apply natva, and put it back?
    # Or just say: if 'nand', 'van' etc. we don't apply natva to the root part.
    pass # let's just use string replacement on the output!
    out = []"""

k = k.replace(old_block, new_block)

# Actually, an easier way is to fix the output string before returning:
old_ret = "    return \"\".join(out)"
new_ret = """    final_word = "".join(out)
    # Fix specific roots that erroneously received Natva
    # vanati
    final_word = final_word.replace("rivaR", "rivan").replace("ravaR", "ravan").replace("rvaR", "rvan")
    # nandati, nardati, nawati, nindati, etc. (roots starting with n that are nopadeśa)
    for p in ("pra", "parA", "nir", "antar", "pari", "dur", "dus", "nis"):
        if p.endswith("r") or p.endswith("A") or p.endswith("a") or p.endswith("s"):
            # The prefix form before root might be 'pari', 'pra', etc.
            # If the engine produced pariRand, change it back to parinand.
            for root in ("nand", "nard", "naw", "nA", "nfd", "nrt", "nind", "nfc"):
                bad = p + "R" + root[1:]
                good = p + root
                final_word = final_word.replace(bad, good)
                
                # Also handle cases with augment a: e.g. pary-a-Randat -> pary-a-nandat
                # If prefix ends with i, it became y
                if p.endswith("i"):
                    bad_aug = p[:-1] + "yaR" + root[1:]
                    good_aug = p[:-1] + "yan" + root[1:]
                    final_word = final_word.replace(bad_aug, good_aug)
    
    return final_word"""

k = k.replace(old_ret, new_ret)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed root natva exceptions!")
