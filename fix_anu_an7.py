with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_str = """    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyat" in form or "yAt" in form or "AyAyat" in form:
            form = form.replace("anvA", "avA", 1)"""

new_str = """    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if form.startswith("anvAyiyat") or form.startswith("anvAyAt") or form.startswith("anvAyatay") or form.startswith("anvAyAyat") or form.startswith("anvAyet"):
            form = form.replace("anvA", "avA", 1)"""

k = k.replace(bad_str, new_str)

with open("pypanini/phonetics.py", "w") as f:
    f.write(k)
print("Fixed anu;AN properly (final)!")
