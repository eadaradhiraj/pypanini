with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# I will fix apply_upasargas to revert the first 'R' to 'n' for the specific nopadesa roots
old_ret = """    final_word = final_word.replace("rivaR", "rivan").replace("ravaR", "ravan").replace("rvaR", "rvan")
    # nandati, nardati, nawati, nindati, etc. (roots starting with n that are nopadeśa)
    for p in ("pra", "parA", "nir", "antar", "pari", "dur", "dus", "nis"):
        if p.endswith("r") or p.endswith("A") or p.endswith("a") or p.endswith("s") or p.endswith("i"):
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

new_ret = """    final_word = final_word.replace("rivaR", "rivan").replace("ravaR", "ravan").replace("rvaR", "rvan")
    
    # Check if this is a nopadesa root (nand, nard, etc.)
    # Since we don't have the original root, we look at the generated final_word.
    # The first letter of the root is right after the prefix (or prefix + augment).
    for p in ("pra", "parA", "nir", "antar", "pari", "dur", "dus", "nis"):
        if p.endswith("s"): p_sandhi = p[:-1] + "r"
        else: p_sandhi = p
        
        # Check direct prefix attachment: e.g. pariRand
        if final_word.startswith(p_sandhi + "R"):
            root_start = final_word[len(p_sandhi)+1:]
            # Only revert if it's one of our nopadesa root stems (including reduplicated ones like nanand)
            if root_start.startswith(("and", "anand", "aw", "An", "fd", "rt", "ind", "fc", "ard")):
                final_word = p_sandhi + "n" + root_start
                
        # Check augmented prefix attachment: e.g. paryaRand
        if p.endswith("i"):
            p_aug = p[:-1] + "ya"
        elif p.endswith("a") or p.endswith("A"):
            p_aug = p[:-1] + "A"
        elif p.endswith("r") or p.endswith("s"):
            p_aug = p_sandhi + "a"
        else:
            p_aug = p + "a"
            
        if final_word.startswith(p_aug + "R"):
            root_start = final_word[len(p_aug)+1:]
            if root_start.startswith(("and", "anand", "aw", "An", "fd", "rt", "ind", "fc", "ard")):
                final_word = p_aug + "n" + root_start
                
    return final_word"""

k = k.replace(old_ret, new_ret)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed nopadesa final!")
