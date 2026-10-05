import re
with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

# We can't easily know it's ziDu~, but we can block Satva for prati+seD and vi+prati+seD if it's not generating them.
# Actually, since ziDa~ and ziDU~ DO get Satva, but ziDu~ DOES NOT... wait, this means the exact same string (e.g. ni + seDati) 
# sometimes needs Satva and sometimes doesn't based on the dhatu! 
# But apply_upasargas only receives the string! So it can't distinguish ziDa~ from ziDu~. 
# This means a purely phonological apply_upasargas without dhatu_id CANNOT achieve 100% accuracy here.
