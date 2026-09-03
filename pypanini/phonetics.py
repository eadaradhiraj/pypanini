"""Phonetic rules (SLP1)"""
def apply_guna(vowel: str) -> str:
    return {'i': 'e', 'I': 'e', 'u': 'o', 'U': 'o', 'f': 'ar', 'F': 'ar', 'x': 'al', 'X': 'al'}.get(vowel, vowel)

def apply_sandhi_eco_ayavayavah(vowel: str) -> str:
    return {'e': 'ay', 'o': 'av', 'E': 'Ay', 'O': 'Av'}.get(vowel, vowel)

def apply_rutva_visarga(term: str) -> str:
    return term[:-1] + "H" if term.endswith("s") else term
