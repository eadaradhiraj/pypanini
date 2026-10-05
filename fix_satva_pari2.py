with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_str = 'form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD")'
new_str = 'form = form.replace("zisiD", "sisiD").replace("ziseD", "siseD").replace("ziziD", "sisiD").replace("zizeD", "siseD")'

k = k.replace(old_str, new_str)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed pariziziDe!")
with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

k = k.replace('.replace("zizeD", "siseD")', '.replace("zizeD", "siseD").replace("zizED", "sisED")')
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed parisisEDva!")
