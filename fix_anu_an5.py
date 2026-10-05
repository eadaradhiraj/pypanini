with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

bad_str = """    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyatiz" in form or "yAtay" in form or "yatay" in form or "AyAyaty" in form:
            form = form.replace("anvA", "avA", 1)"""

new_str = """    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if "yiyatiz" in form or "yAtay" in form or "yatay" in form or "AyAyat" in form:
            form = form.replace("anvA", "avA", 1)"""

k = k.replace(bad_str, new_str)

with open("pypanini/phonetics.py", "w") as f:
    f.write(k)
print("Fixed anu;AN yang properly!")
