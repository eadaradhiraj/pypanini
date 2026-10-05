with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """        if "pariz" in form: 
            form = form.replace("pariz", "paris")
            # And also revert any internal zisiD to sisiD since it lost Satva
            form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD").replace("ziziD", "sisiD").replace("zizeD", "siseD").replace("zizED", "sisED")"""

new_block = """        if "pariz" in form: 
            # Revert Satva ONLY IF there is no reduplication!
            if "ziziD" not in form and "zizeD" not in form and "zizED" not in form:
                form = form.replace("pariz", "paris")
                form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD").replace("ziziD", "sisiD").replace("zizeD", "siseD").replace("zizED", "sisED")"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pari satva correctly!")
