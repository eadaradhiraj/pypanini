"""
Bidirectional Transliteration: SLP1 <-> Devanagari
"""

SLP1_TO_DEV_VOWEL = {
    'a': 'अ', 'A': 'आ', 'i': 'इ', 'I': 'ई', 'u': 'उ', 'U': 'ऊ',
    'f': 'ऋ', 'F': 'ॠ', 'x': 'ऌ', 'X': 'ॡ', 'e': 'ए', 'E': 'ऐ',
    'o': 'ओ', 'O': 'औ',
}

SLP1_TO_DEV_MATRA = {
    'a': '', 'A': 'ा', 'i': 'ि', 'I': 'ी', 'u': 'ु', 'U': 'ू',
    'f': 'ृ', 'F': 'ॄ', 'x': 'ॢ', 'X': 'ॣ', 'e': 'े', 'E': 'ै',
    'o': 'ो', 'O': 'ौ',
}

SLP1_TO_DEV_CONS = {
    'k': 'क', 'K': 'ख', 'g': 'ग', 'G': 'घ', 'N': 'ङ',
    'c': 'च', 'C': 'छ', 'j': 'ज', 'J': 'झ', 'Y': 'ञ',
    'w': 'ट', 'W': 'ठ', 'q': 'ड', 'Q': 'ढ', 'R': 'ण',
    't': 'त', 'T': 'थ', 'd': 'द', 'D': 'ध', 'n': 'न',
    'p': 'प', 'P': 'फ', 'b': 'ब', 'B': 'भ', 'm': 'म',
    'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व',
    'S': 'श', 'z': 'ष', 's': 'स', 'h': 'ह',
}

SLP1_TO_DEV_MISC = {'M': 'ं', 'H': 'ः', '~': 'ँ', "'": 'ऽ'}

DEV_TO_SLP1_VOWEL = {v: k for k, v in SLP1_TO_DEV_VOWEL.items()}
DEV_TO_SLP1_MATRA = {v: k for k, v in SLP1_TO_DEV_MATRA.items() if v}
DEV_TO_SLP1_CONS = {v: k for k, v in SLP1_TO_DEV_CONS.items()}
DEV_TO_SLP1_MISC = {v: k for k, v in SLP1_TO_DEV_MISC.items()}
VIRAMA = '्'


def slp1_to_devanagari(text: str) -> str:
    res = []
    prev_was_cons = False
    for ch in text:
        if ch in SLP1_TO_DEV_VOWEL:
            if prev_was_cons:
                res[-1] = res[-1][:-1] + SLP1_TO_DEV_MATRA[ch]
            else:
                res.append(SLP1_TO_DEV_VOWEL[ch])
            prev_was_cons = False
        elif ch in SLP1_TO_DEV_CONS:
            res.append(SLP1_TO_DEV_CONS[ch] + VIRAMA)
            prev_was_cons = True
        elif ch in SLP1_TO_DEV_MISC:
            res.append(SLP1_TO_DEV_MISC[ch])
            prev_was_cons = False
        else:
            res.append(ch)
            prev_was_cons = False
    return "".join(res)


def devanagari_to_slp1(text: str) -> str:
    res = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c in DEV_TO_SLP1_VOWEL:
            res.append(DEV_TO_SLP1_VOWEL[c])
            i += 1
        elif c in DEV_TO_SLP1_CONS:
            if i + 1 < n and text[i + 1] == VIRAMA:
                res.append(DEV_TO_SLP1_CONS[c])
                i += 2
            elif i + 1 < n and text[i + 1] in DEV_TO_SLP1_MATRA:
                res.append(DEV_TO_SLP1_CONS[c] + DEV_TO_SLP1_MATRA[text[i + 1]])
                i += 2
            else:
                res.append(DEV_TO_SLP1_CONS[c] + "a")
                i += 1
        elif c in DEV_TO_SLP1_MISC:
            res.append(DEV_TO_SLP1_MISC[c])
            i += 1
        else:
            res.append(c)
            i += 1
    return "".join(res)
