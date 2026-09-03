"""
Phonetic and Sandhi rules (Pāṇinian morphophonemics in SLP1).
"""

def apply_guna(vowel: str) -> str:
    """Pāṇini 7.3.84: sArvaDAtukArDaDAtukayoH"""
    guna_map = {
        'i': 'e', 'I': 'e',
        'u': 'o', 'U': 'o',
        'f': 'ar', 'F': 'ar',
        'x': 'al', 'X': 'al'
    }
    return guna_map.get(vowel, vowel)


def apply_sandhi_eco_ayavayavah(vowel: str) -> str:
    """Pāṇini 6.1.78: eco'yavAyAvaH"""
    adesha_map = {
        'e': 'ay',
        'o': 'av',
        'E': 'Ay',
        'O': 'Av'
    }
    return adesha_map.get(vowel, vowel)


def apply_satva(preceding_char: str, s_char: str = "s") -> str:
    """
    Pāṇini 8.3.59: AdeSapratyayayoH
    's' becomes retroflex 'z' after iR (vowels except a/A, semivowels, h) or ku (velars).
    """
    in_ku_set = set("iufxeoEOyvrlhkKgGN")
    if preceding_char in in_ku_set and s_char == "s":
        return "z"
    return s_char


def apply_rutva_visarga(term: str) -> str:
    """Pāṇini 8.2.66 & 8.3.15"""
    if term.endswith("s"):
        return term[:-1] + "H"
    return term
