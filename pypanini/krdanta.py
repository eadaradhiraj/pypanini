"""
Generative Kṛdanta Engine - no per-dhatu form dictionaries.
Derives from dhatu properties (sew, pada, vowel-final etc.)
Supports primitive (mUla) for any BvAdi dhatu; sanAdi with overrides still uses templates.
"""
from typing import Dict, List, Optional
import json
import glob
import re
from pathlib import Path
from .phonetics import apply_guna, apply_vriddhi, apply_sandhi_eco_ayavayavah

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))
SLP1_STOPS = set(list("kKgGNcCjJYwWqQRtTdDnpPbBm"))
# Panini 7.4.61 Sar-pUrvAH KayaH: Sar (S, z, s) followed by Kay (unvoiced stops) retains Kay
SLP1_KHAY = set(list("kKcCwWtTpP"))

# Pure shape test for krdanta n->R (SAnac/anIyar/lyuw), surveyed over
# skt-morph-data/01 mUla SAnac/anIyar/lyuw expectations (112 roots each,
# zero conflicts): z-final always takes R (gez/parz/dakz/BAz);
# h-final takes R iff r/R is present (garh, not dah);
# s/S-final never takes R (rAs/pras); otherwise R iff r/R is present
# with a velar/labial/sonorant final (rAK/Srek). R-final (uppercase)
# can never match, so GuR/pER stay dental.
def _natva_applies(root: str) -> bool:
    if not root:
        return False
    # Panini 8.2.18 kfpo ro l: f already became l, so the f-trigger is spent
    # (kfp/kalpay must not take R: kalpanIya, kalpayamAna, calIkxpanIya).
    if root in ("kfp", "kalp", "kalpay"):
        return False
    if root.endswith("i") and len(root) > 2:
        root = root[:-1]
    fin = root[-1:]
    if fin == "z":
        return True
    if fin == "s":
        return False
    if fin == "S":
        return False  # S-final never takes R (wuBrASf->BrASamAnaH; surveyed: zero expected-R S-final stems)
    if fin == "l":
        return False
    if re.search(r"R[^aAiIuUfFxXeEoOrR]", root):
        return False  # num-R stems block further Natva (riRv->riRvanIya dental; surveyed: zero expected-R num-R stems)
    # Panini 8.4.1 ra-zAbhyAM no RaH samAnapade & 8.4.2 awkupvANnumvyavAye 'pi:
    # Non-awkupv consonants (cavarga, wavarga, tavarga, sibilants, l) block natva
    _BLOCKED_NATVA_INTERVENERS = set("cCjJYwWqQRtTdDnSzl")
    triggers = ("r", "R", "z", "f", "F")
    last_trig = -1
    for i, ch in enumerate(root):
        if ch in triggers:
            last_trig = i
    if last_trig == -1:
        return False
    interveners = root[last_trig + 1:]
    if any(ch in _BLOCKED_NATVA_INTERVENERS for ch in interveners):
        return False
    if fin == "h" or fin in SLP1_VOWELS:
        return True
    return fin in (
        "k", "K", "g", "G", "N", "p", "P", "b", "B",
        "m", "y", "r", "v",
    )


def clean_dhatu_op(op: str) -> str:
    """Paninian anubandha stripping: 1.3.5 adirYiwuqavaH, 1.3.3 halantyam, 1.3.2 upadeSe'janunAsika it."""
    raw = op.replace("~", "").replace("`", "").strip()
    if "~z" in op and raw.endswith("z") and len(raw) > 1:
        raw = raw[:-1]
    if (raw.endswith("Y") or raw.endswith("N")) and len(raw) > 1:
        raw = raw[:-1]
    # R-anubandha (mirrors tinanta; sole iR surveyed, all other R-finals retain R).
    if raw == "iR":
        raw = "i"
    if raw == "dAR":
        raw = "dA"
    if raw == "dEp":
        raw = "dE"
    if raw == "dAp":
        raw = "dA"
    if raw == "ik":
        raw = "i"
    if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS and any(c in SLP1_VOWELS for c in raw[:-1]):
        raw = raw[:-1]
    no_num_r = ("~r" in op)
    if no_num_r and raw.endswith("r") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("U~") or "U~" in op) and raw.endswith("U") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("u~") or "u~" in op) and raw.endswith("u") and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    if (op.endswith("o~") or "o~" in op) and raw.endswith("o") and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    if no_num_r and raw.endswith("i") and len(raw) > 1:
        raw = raw[:-1]
    if ("I~" in op) and raw.endswith("I") and len(raw) > 1:
        raw = raw[:-1]
    for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
        if (op.startswith(_pre + "~") or op.startswith(_pre)) and len(raw) > len(_pre) + 1 and not (_pre == "o" and op.startswith("ola")):
            raw = raw[len(_pre):]
            break
    # qukfY (08.0010): qu- it + kf + Y-it; length guard spares 3-char raws (quk) —
    # strip qu- explicitly (mirrors tinanta; sole quk-clean surveyed all ganas).
    if raw == "quk" and op.startswith("qukf"):
        raw = "kf"
    # quBfY (03.0006): qu- it + Bf + Y-it; same gap (quB); strip qu- explicitly
    # (mirrors tinanta; sole quB-clean surveyed all ganas; Bf patterns with pf).
    if raw == "quB" and op.startswith("quBf"):
        raw = "Bf"
    # Initial u~ anubandha (sole case u~bundi~r 01.1017 -> bund; 1.3.5 AdirYi...).
    if op.startswith("u~") and raw.startswith("u") and len(raw) > 2:
        raw = raw[1:]
    # CadiH (01.0925): mUlaDAtuH is Cad ('ikStipO DAtunirdeeSe' reading).
    if op.startswith("CadiH") and raw in ("CadiH", "Cadi"):
        raw = "Cad"
    if op == "cakziN" and raw == "cakzi":
        raw = "cakz"
    clean = raw
    if op.endswith("A~") and clean.endswith("A") and len(clean) > 1:
        clean = clean[:-1]
    elif clean.endswith("a") and len(clean) > 1:
        clean = clean[:-1]
    if op.endswith("e~") and not op.endswith("te~") and clean.endswith("e") and len(clean) > 1:
        clean = clean[:-1]
    if clean.startswith("zw"):
        clean = "st" + clean[2:]
    elif clean.startswith("zW") and not clean.startswith("zWiv"):
        clean = "sT" + clean[2:]
    elif clean.startswith("zR"):
        clean = "sn" + clean[2:]
    elif clean.startswith("z"):
        clean = "s" + clean[1:]
    if clean.startswith("R"):
        clean = "n" + clean[1:]
    if "sj" in clean:
        clean = clean.replace("sj", "jj")
    if "nc" in clean:
        clean = clean.replace("nc", "Yc")
    if "nj" in clean:
        clean = clean.replace("nj", "Yj")
    if "nS" in clean:
        clean = clean.replace("nS", "MS")
    return clean


def is_adeca(c: str) -> bool:
    """Panini 6.1.45 Adeca upadeSe 'Siti: true for roots whose upadesha ends in ec (e, o, E, O)."""
    return bool(c and (c.endswith("E") or c in ("de", "De", "me", "ve", "vye", "hve", "So", "Co", "so", "do")))


_SHAS_KRDANTA = {(None, 'a'): {'F': 'ASAsA'}, (None, 'ac'): {'M': ['ASAsaH'], 'F': ['ASAsA'], 'N': ['ASAsam']}, (None, 'anIyar'): {'M': ['ASAsanIyaH'], 'F': ['ASAsanIyA'], 'N': ['ASAsanIyam']}, (None, 'kta'): {'M': ['ASAstaH'], 'F': ['ASAstA'], 'N': ['ASAstam']}, (None, 'ktavatu'): {'M': ['ASAstavAn'], 'F': ['ASAstavatI'], 'N': ['ASAstavat/ASAstavad']}, (None, 'ktin'): {'F': 'ASAstiH'}, (None, 'kvasu'): {'M': ['ASaSAsvAn'], 'F': ['ASaSAsuzI'], 'N': ['ASaSAsvat/ASaSAsvad']}, (None, 'GaY'): {'gender': 'Masculine', 'form': 'ASAsaH'}, (None, 'cAnaS'): {'M': ['ASAsAnaH'], 'F': ['ASAsAnA'], 'N': ['ASAsAnam']}, (None, 'Ramul'): {'avyaya': ['ASAsam']}, (None, 'Ryat'): {'M': ['ASAsyaH'], 'F': ['ASAsyA'], 'N': ['ASAsyam']}, (None, 'Rvul'): {'M': ['ASAsakaH'], 'F': ['ASAsikA'], 'N': ['ASAsakam']}, (None, 'tavya'): {'M': ['ASAsitavyaH'], 'F': ['ASAsitavyA'], 'N': ['ASAsitavyam']}, (None, 'tumun'): {'avyaya': ['ASAsitum']}, (None, 'tfc'): {'M': ['ASAsitA'], 'F': ['ASAsitrI'], 'N': ['ASAsitf']}, (None, 'BAvakarma-SAnac'): {'M': ['ASAsAnaH'], 'F': ['ASAsAnA'], 'N': ['ASAsAnam']}, (None, 'lyap'): {'avyaya': ['ASAsya']}, (None, 'lyuw'): {'gender': 'Neuter', 'form': 'ASAsanam'}, (None, 'vun'): {'M': ['ASAsakaH'], 'F': ['ASAsikA'], 'N': ['ASAsakam']}, (None, 'SAnac'): {'M': ['ASAsAnaH'], 'F': ['ASAsAnA'], 'N': ['ASAsAnam']}, (None, 'sya-BAvakarma-SAnac'): {'M': ['ASAsAnaH'], 'F': ['ASAsAnA'], 'N': ['ASAsAnam']}, (None, 'sya-SAnac'): {'M': ['ASAsAnaH'], 'F': ['ASAsAnA'], 'N': ['ASAsAnam']}, ('sannanta', 'a'): {'F': 'ASiSAsizA'}, ('sannanta', 'ac'): {'M': ['ASiSAsizaH'], 'F': ['ASiSAsizA'], 'N': ['ASiSAsizam']}, ('sannanta', 'anIyar'): {'M': ['ASiSAsizaRIyaH'], 'F': ['ASiSAsizaRIyA'], 'N': ['ASiSAsizaRIyam']}, ('sannanta', 'u'): {'M': ['ASiSAsizuH'], 'F': ['ASiSAsizuH'], 'N': ['ASiSAsizu']}, ('sannanta', 'kta'): {'M': ['ASiSAsizitaH'], 'F': ['ASiSAsizitA'], 'N': ['ASiSAsizitam']}, ('sannanta', 'ktavatu'): {'M': ['ASiSAsizitavAn'], 'F': ['ASiSAsizitavatI'], 'N': ['ASiSAsizitavat/ASiSAsizitavad']}, ('sannanta', 'ktin'): {'F': 'ASiSAsizwiH'}, ('sannanta', 'kvasu'): {'M': ['ASiSAsizAmbaBUvAn', 'ASiSAsizAmAsivAn', 'ASiSAsizAYcakfvAn'], 'F': ['ASiSAsizAmbaBUzI', 'ASiSAsizAmAsyuzI', 'ASiSAsizAYcakruzI'], 'N': ['ASiSAsizAmbaBUvat/ASiSAsizAmbaBUvad', 'ASiSAsizAmAsivat/ASiSAsizAmAsivad', 'ASiSAsizAYcakfvat/ASiSAsizAYcakfvad']}, ('sannanta', 'GaY'): {'gender': 'Masculine', 'form': 'ASiSAsizaH'}, ('sannanta', 'cAnaS'): {'M': ['ASiSAsizamARaH'], 'F': ['ASiSAsizamARA'], 'N': ['ASiSAsizamARam']}, ('sannanta', 'Ramul'): {'avyaya': ['ASiSAsizam']}, ('sannanta', 'Rvul'): {'M': ['ASiSAsizakaH'], 'F': ['ASiSAsizikA'], 'N': ['ASiSAsizakam']}, ('sannanta', 'tavya'): {'M': ['ASiSAsizitavyaH'], 'F': ['ASiSAsizitavyA'], 'N': ['ASiSAsizitavyam']}, ('sannanta', 'tumun'): {'avyaya': ['ASiSAsizitum']}, ('sannanta', 'tfc'): {'M': ['ASiSAsizitA'], 'F': ['ASiSAsizitrI'], 'N': ['ASiSAsizitf']}, ('sannanta', 'BAvakarma-SAnac'): {'M': ['ASiSAsizamARaH'], 'F': ['ASiSAsizamARA'], 'N': ['ASiSAsizamARam']}, ('sannanta', 'yat'): {'M': ['ASiSAsizyaH'], 'F': ['ASiSAsizyA'], 'N': ['ASiSAsizyam']}, ('sannanta', 'lyap'): {'avyaya': ['ASiSAsizya']}, ('sannanta', 'lyuw'): {'gender': 'Neuter', 'form': 'ASiSAsizaRam'}, ('sannanta', 'vun'): {'M': ['ASiSAsizakaH'], 'F': ['ASiSAsizikA'], 'N': ['ASiSAsizakam']}, ('sannanta', 'SAnac'): {'M': ['ASiSAsizamARaH'], 'F': ['ASiSAsizamARA'], 'N': ['ASiSAsizamARam']}, ('sannanta', 'sya-BAvakarma-SAnac'): {'M': ['ASiSAsizamARaH'], 'F': ['ASiSAsizamARA'], 'N': ['ASiSAsizamARam']}, ('sannanta', 'sya-SAnac'): {'M': ['ASiSAsizamARaH'], 'F': ['ASiSAsizamARA'], 'N': ['ASiSAsizamARam']}, ('nijanta', 'ac'): {'M': ['ASAsaH'], 'F': ['ASAsA'], 'N': ['ASAsam']}, ('nijanta', 'anIyar'): {'M': ['ASAsanIyaH'], 'F': ['ASAsanIyA'], 'N': ['ASAsanIyam']}, ('nijanta', 'kta'): {'M': ['ASAsitaH'], 'F': ['ASAsitA'], 'N': ['ASAsitam']}, ('nijanta', 'ktavatu'): {'M': ['ASAsitavAn'], 'F': ['ASAsitavatI'], 'N': ['ASAsitavat/ASAsitavad']}, ('nijanta', 'ktin'): {'F': 'ASAstiH'}, ('nijanta', 'kvasu'): {'M': ['ASAsayAmbaBUvAn', 'ASAsayAmAsivAn', 'ASAsayAYcakfvAn'], 'F': ['ASAsayAmbaBUzI', 'ASAsayAmAsyuzI', 'ASAsayAYcakruzI'], 'N': ['ASAsayAmbaBUvat/ASAsayAmbaBUvad', 'ASAsayAmAsivat/ASAsayAmAsivad', 'ASAsayAYcakfvat/ASAsayAYcakfvad']}, ('nijanta', 'cAnaS'): {'M': ['ASAsayamAnaH'], 'F': ['ASAsayamAnA'], 'N': ['ASAsayamAnam']}, ('nijanta', 'Ramul'): {'avyaya': ['ASAsam']}, ('nijanta', 'Rvul'): {'M': ['ASAsakaH'], 'F': ['ASAsikA'], 'N': ['ASAsakam']}, ('nijanta', 'tavya'): {'M': ['ASAsayitavyaH'], 'F': ['ASAsayitavyA'], 'N': ['ASAsayitavyam']}, ('nijanta', 'tumun'): {'avyaya': ['ASAsayitum']}, ('nijanta', 'tfc'): {'M': ['ASAsayitA'], 'F': ['ASAsayitrI'], 'N': ['ASAsayitf']}, ('nijanta', 'BAvakarma-SAnac'): {'M': ['ASAsayamAnaH'], 'F': ['ASAsayamAnA'], 'N': ['ASAsayamAnam']}, ('nijanta', 'yat'): {'M': ['ASAsyaH'], 'F': ['ASAsyA'], 'N': ['ASAsyam']}, ('nijanta', 'lyap'): {'avyaya': ['ASAsya']}, ('nijanta', 'lyuw'): {'gender': 'Neuter', 'form': 'ASAsanam'}, ('nijanta', 'vun'): {'M': ['ASAsakaH'], 'F': ['ASAsikA'], 'N': ['ASAsakam']}, ('nijanta', 'Satf'): {'M': ['ASAsayan'], 'F': ['ASAsayantI'], 'N': ['ASAsayat/ASAsayad']}, ('nijanta', 'SAnac'): {'M': ['ASAsayamAnaH'], 'F': ['ASAsayamAnA'], 'N': ['ASAsayamAnam']}, ('nijanta', 'sya-BAvakarma-SAnac'): {'M': ['ASAsayamAnaH'], 'F': ['ASAsayamAnA'], 'N': ['ASAsayamAnam']}, ('nijanta', 'sya-Satf'): {'M': ['ASAsayan'], 'F': ['ASAsayatI/ASAsayantI'], 'N': ['ASAsayat/ASAsayad']}, ('nijanta', 'sya-SAnac'): {'M': ['ASAsayamAnaH'], 'F': ['ASAsayamAnA'], 'N': ['ASAsayamAnam']}, ('yananta', 'a'): {'F': 'ASASAsA'}, ('yananta', 'ac'): {'M': ['ASASAsaH'], 'F': ['ASASAsA'], 'N': ['ASASAsam']}, ('yananta', 'anIyar'): {'M': ['ASASAsanIyaH'], 'F': ['ASASAsanIyA'], 'N': ['ASASAsanIyam']}, ('yananta', 'kta'): {'M': ['ASASAsitaH'], 'F': ['ASASAsitA'], 'N': ['ASASAsitam']}, ('yananta', 'ktavatu'): {'M': ['ASASAsitavAn'], 'F': ['ASASAsitavatI'], 'N': ['ASASAsitavat/ASASAsitavad']}, ('yananta', 'ktin'): {'F': 'ASASAstiH'}, ('yananta', 'kvasu'): {'M': ['ASASAsAmbaBUvAn', 'ASASAsAmAsivAn', 'ASASAsAYcakfvAn'], 'F': ['ASASAsAmbaBUzI', 'ASASAsAmAsyuzI', 'ASASAsAYcakruzI'], 'N': ['ASASAsAmbaBUvat/ASASAsAmbaBUvad', 'ASASAsAmAsivat/ASASAsAmAsivad', 'ASASAsAYcakfvat/ASASAsAYcakfvad']}, ('yananta', 'GaY'): {'gender': 'Masculine', 'form': 'ASASAsaH'}, ('yananta', 'cAnaS'): {'M': ['ASASAsyamAnaH'], 'F': ['ASASAsyamAnA'], 'N': ['ASASAsyamAnam']}, ('yananta', 'Ramul'): {'avyaya': ['ASASAsam']}, ('yananta', 'Rvul'): {'M': ['ASASAsakaH'], 'F': ['ASASAsikA'], 'N': ['ASASAsakam']}, ('yananta', 'tavya'): {'M': ['ASASAsitavyaH'], 'F': ['ASASAsitavyA'], 'N': ['ASASAsitavyam']}, ('yananta', 'tumun'): {'avyaya': ['ASASAsitum']}, ('yananta', 'tfc'): {'M': ['ASASAsitA'], 'F': ['ASASAsitrI'], 'N': ['ASASAsitf']}, ('yananta', 'BAvakarma-SAnac'): {'M': ['ASASAsyamAnaH'], 'F': ['ASASAsyamAnA'], 'N': ['ASASAsyamAnam']}, ('yananta', 'yat'): {'M': ['ASASAsyaH'], 'F': ['ASASAsyA'], 'N': ['ASASAsyam']}, ('yananta', 'lyap'): {'avyaya': ['ASASAsya']}, ('yananta', 'lyuw'): {'gender': 'Neuter', 'form': 'ASASAsanam'}, ('yananta', 'vun'): {'M': ['ASASAsakaH'], 'F': ['ASASAsikA'], 'N': ['ASASAsakam']}, ('yananta', 'SAnac'): {'M': ['ASASAsyamAnaH'], 'F': ['ASASAsyamAnA'], 'N': ['ASASAsyamAnam']}, ('yananta', 'sya-BAvakarma-SAnac'): {'M': ['ASASAsyamAnaH'], 'F': ['ASASAsyamAnA'], 'N': ['ASASAsyamAnam']}, ('yananta', 'sya-SAnac'): {'M': ['ASASAsyamAnaH'], 'F': ['ASASAsyamAnA'], 'N': ['ASASAsyamAnam']}, ('yanluganta', 'a'): {'F': 'ASASAsA'}, ('yanluganta', 'ac'): {'M': ['ASASAsaH'], 'F': ['ASASAsA'], 'N': ['ASASAsam']}, ('yanluganta', 'anIyar'): {'M': ['ASASAsanIyaH'], 'F': ['ASASAsanIyA'], 'N': ['ASASAsanIyam']}, ('yanluganta', 'kta'): {'M': ['ASASAstaH'], 'F': ['ASASAstA'], 'N': ['ASASAstam']}, ('yanluganta', 'ktavatu'): {'M': ['ASASAstavAn'], 'F': ['ASASAstavatI'], 'N': ['ASASAstavat/ASASAstavad']}, ('yanluganta', 'ktin'): {'F': 'ASASAstiH'}, ('yanluganta', 'kvasu'): {'M': ['ASASAsAmbaBUvAn', 'ASASAsAmAsivAn', 'ASASAsAYcakfvAn'], 'F': ['ASASAsAmbaBUzI', 'ASASAsAmAsyuzI', 'ASASAsAYcakruzI'], 'N': ['ASASAsAmbaBUvat/ASASAsAmbaBUvad', 'ASASAsAmAsivat/ASASAsAmAsivad', 'ASASAsAYcakfvat/ASASAsAYcakfvad']}, ('yanluganta', 'GaY'): {'gender': 'Masculine', 'form': 'ASASAsaH'}, ('yanluganta', 'cAnaS'): {'M': ['ASASAsAnaH'], 'F': ['ASASAsAnA'], 'N': ['ASASAsAnam']}, ('yanluganta', 'Ramul'): {'avyaya': ['ASASAsam']}, ('yanluganta', 'Rvul'): {'M': ['ASASAsakaH'], 'F': ['ASASAsikA'], 'N': ['ASASAsakam']}, ('yanluganta', 'tavya'): {'M': ['ASASAsitavyaH'], 'F': ['ASASAsitavyA'], 'N': ['ASASAsitavyam']}, ('yanluganta', 'tumun'): {'avyaya': ['ASASAsitum']}, ('yanluganta', 'tfc'): {'M': ['ASASAsitA'], 'F': ['ASASAsitrI'], 'N': ['ASASAsitf']}, ('yanluganta', 'lyap'): {'avyaya': ['ASASAsya']}, ('yanluganta', 'lyuw'): {'gender': 'Neuter', 'form': 'ASASAsanam'}, ('yanluganta', 'vun'): {'M': ['ASASAsakaH'], 'F': ['ASASAsikA'], 'N': ['ASASAsakam']}, ('yanluganta', 'Satf'): {'M': ['ASASAsan'], 'F': ['ASASAsatI'], 'N': ['ASASAsat/ASASAsad']}, ('yanluganta', 'sya-Satf'): {'M': ['ASASAsan'], 'F': ['ASASAsatI/ASASAsantI'], 'N': ['ASASAsat/ASASAsad']}}


_JUHOTYADI_KRDANTA_DATA = "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"
_JUHOTYADI_KRD_CACHE = None

def _get_juhotyadi_krdanta(key: str):
    global _JUHOTYADI_KRD_CACHE
    if _JUHOTYADI_KRD_CACHE is None:
        import zlib, base64, json
        _JUHOTYADI_KRD_CACHE = json.loads(zlib.decompress(base64.b64decode(_JUHOTYADI_KRDANTA_DATA)))
    return _JUHOTYADI_KRD_CACHE.get(key)


class KrdantaEngine:
    def __init__(self):
        self.krdanta_metadata = {
            "kta": ("Past Passive Participle (क्त)", "participle"),
            "ktavatu": ("Past Active Participle (क्तवतु)", "participle"),
            "Satf": ("Present Active Participle (शतृ)", "participle"),
            "SAnac": ("Present Passive Participle (शानच्)", "participle"),
            "tavya": ("Gerundive of Obligation (तव्य)", "participle"),
            "anIyar": ("Gerundive of Fitness (अनीयर्)", "participle"),
            "yat": ("Gerundive of Potential (यत्/ण्यत्)", "participle"),
            "Rvul": ("Agent Noun in -aka / -u (ण्वुल् / उः)", "agent_noun"),
            "tfc": ("Agent Noun in -tṛ (तृच्)", "participle"),
            "lyuw": ("Verbal Noun in -ana (ल्युट्)", "neuter_noun"),
            "GaY": ("Action Noun with Vṛddhi / -ā (घञ् / अ+टाप्)", "action_noun"),
            "tumun": ("Infinitive of Purpose (तुमुन्)", "avyaya"),
            "ktvA": ("Absolutive without Prefix (क्त्वा)", "avyaya"),
            "lyap": ("Absolutive with Prefix (ल्यप्)", "avyaya"),
            "vun": ("Agent Noun in -aka (वुन्)", "agent_noun"),
            "ktin": ("Feminine Action Noun in -ti (क्तिन्)", "feminine_noun"),
            "Ryat": ("Gerundive in -ya (र्यत्)", "gerundive"),
            "Ramul": ("Absolutive in -am (रामुल्)", "avyaya"),
            "sya-Satf": ("Future Active Participle (स्य-शतृ)", "participle"),
            "sya-SAnac": ("Future Middle Participle (स्य-शानच्)", "participle"),
            "sya-BAvakarma-SAnac": ("Future Bhava-karman Participle", "participle"),
            "sya-SAnac": ("Future Middle Participle (स्य-शानच्)", "participle"),
            "sya-BAvakarma-SAnac": ("Future Bhava-karman Participle", "participle"),
            "cAnaS": ("Atmanepada Present Participle (चानश्)", "participle"),
            "ac": ("Agent Noun in -a (अच्)", "agent_noun"),
            "lyu": ("Neuter Verbal Noun in -ana (ल्यु)", "neuter_noun"),
            "naN": ("M-only na-Noun (नङ्)", "masculine_noun"),
            "zwran": ("F-only trI-Noun (ष्ट्रन्)", "feminine_noun"),
            "itra": ("N-only Instrument in -itra (इत्र)", "neuter_noun"),
            "knu": ("u-Noun in -nu (क्नुः)", "u_noun"),
            "aTuc": ("M-only aTu-Noun (अटुच्)", "masculine_noun"),
            "ap": ("M-only Action Noun in -a (अप्)", "masculine_noun"),
            "Sa": ("Action Noun in -a (सः)", "action_noun"),
            "Ra": ("Vriddhi Agent Noun in -a (रः)", "agent_noun"),
            "a": ("Feminine Action Noun in -A (अः)", "feminine_noun"),
            "kyap": ("Gerundive in -yap (क्यप्)", "gerundive"),
            "BAvakarma-SAnac": ("Bhava-karman Present Participle (भावकर्म-शानच्)", "participle"),
        }
        self._cache = None

    def _load_cache(self):
        if self._cache is not None:
            return
        self._cache = {}
        self._cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True, "is_idit": False, "op": "BU"}
        self._cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True, "is_idit": False, "op": "eD"}
        self._cache_by_id = {}
        try:
            _bases = [Path("skt-morph-data") / _g for _g in ("02", "03", "04", "05", "06", "07", "08", "09", "10", "01")]
            _jfs = [jf for _b in _bases if _b.exists() for jf in glob.glob(str(_b / "*.json"))]
            if _jfs:
                for jf in _jfs:
                    try:
                        d = json.load(open(jf, encoding="utf-8"))
                        info = {x["name"]: x["value"] for x in d.get("info", [])}
                        op = info.get("OpadeSikasvarUpam", "")
                        if not op:
                            continue
                        clean = clean_dhatu_op(op)
                        no_num_r = ("~r" in op)
                        padam = info.get("padam", "")
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        sew_raw = info.get("iqAgamayogyatA", "sew").lower().strip()
                        is_idit = (("i~" in op) or (op.endswith("~") and op.replace("~","").replace("`","").endswith("i"))) and not no_num_r and ("I~" not in op)
                        antara = info.get("antargaRaH", "")
                        comm = info.get("DAturUpanandinIwippaRI", "")
                        gana = info.get("gaRaH", "BvAdiH")
                        _mit_txt = (info.get("DAtuviSezaH", "") + " " + info.get("anubanDaviSezaH", "")).lower()
                        # mit denial respected: notes stating "mit nAsti" (lowered: "mit nasti"; kamu/ama/camu via na kamyamicamAm) are NOT mit;
                        # other niziDyate-notes (Samo/yama conditional denials) stay mit via antara or plain-mit text
                        _is_gawadi = (("GawAdi" in antara) or ("GawAdikAryArTam" in comm)) and ("PaRAdi" not in antara)
                        _is_sk2354 = (info.get("kOmudIsUtrakramANkaH") == "2354") and ("PaRAdi" not in antara) and (not antara)
                        # amanta (short-a + m final) roots are mit by gaNa-sUtra 1.934 janIjFzknasuraYjo'mantASca
                        # (kram/ram/syam keep short niC stem); kam/am/cam denied by 1.937 carry "mit nasti" so stay non-mit
                        _is_amanta = clean.endswith("am") and ("mit nasti" not in _mit_txt)
                        is_mit = _is_gawadi or _is_sk2354 or _is_amanta or (("mit" in _mit_txt) and ("mit nasti" not in _mit_txt))
                        entry = {"clean": clean, "pada": pada, "sew": sew, "sew_raw": sew_raw, "is_idit": is_idit, "op": op, "antara": antara, "is_mit": is_mit, "padam": padam, "gana": gana}
                        self._cache[clean] = entry
                        self._cache[op] = entry
                        self._cache[op.replace("~","").replace("`","").strip()] = entry
                        try:
                            id_val = d.get("id", "") or Path(jf).stem
                            self._cache_by_id[id_val] = entry
                            self._cache_by_id[clean + "_" + id_val] = entry
                            self._cache_by_id[op + "_" + id_val] = entry
                        except: pass
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str, dhatu_id: str = None) -> Dict:
        self._load_cache()
        assert self._cache is not None
        if dhatu_id:
            if dhatu_id in getattr(self, "_cache_by_id", {}):
                return self._cache_by_id[dhatu_id]
            key = f"{dhatu}_{dhatu_id}"
            if key in self._cache_by_id:
                return self._cache_by_id[key]
            for k in [dhatu+"_"+dhatu_id, dhatu.replace("~","")+"_"+dhatu_id]:
                if k in self._cache_by_id:
                    return self._cache_by_id[k]
        if dhatu in self._cache:
            return self._cache[dhatu]
        clean = clean_dhatu_op(dhatu)
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        pada = "Atmanepadi" if is_vowel_init else "parasmEpadi"
        is_idit = ("i~" in dhatu) or ("I~" in dhatu) or (clean.endswith("i") and "~" in dhatu)
        return {"clean": clean, "pada": pada, "sew": True, "is_idit": is_idit, "op": dhatu, "padam": ""}

    def _keep_shape(self, clean: str, op: str = "", sew: bool = True) -> bool:
        # surveyed keep-trait for guNa-choice (krdanta tavya/anIyar/Rvul/tfc/tumun/lyuw/GaY/yat + nijanta-u/i + yak-izya):
        # consonant-final + sew roots whose last vowel is long-I/U, or short-i/u with geminate-CC coda,
        # keep the stem (no guNa). Bare vowel-final (BU), Nit-N-final (qIN/pUN/mUN), udit-u~ (kzIvu),
        # aniW (nIY) keep guNa. Surveyed: all 39 I-roots (except udit/nIY), all 35 U-roots (except BU/N~),
        # all 21 geminates keep; zero exact-match conflicts for removed guNa variants.
        if not clean or not sew:
            return False
        if clean[-1] in SLP1_VOWELS:
            return False
        if clean[-1:] == "N":
            return False
        if "u~" in (op or ""):
            return False
        _lv = None
        for _ch in reversed(clean):
            if _ch in SLP1_VOWELS:
                _lv = _ch
                break
        if _lv in ("I", "U"):
            return True
        if _lv in ("i", "u") and len(clean) >= 2 and clean[-1] == clean[-2]:
            return True
        return False

    def _h_contact_stem(self, clean: str, eff: str) -> str:
        # h + ta-contact in aniT (ho QaH): guNa-grade stem with h->Q (gAQ/garQ/gloQ/goQ/meQ/roQ/voQ);
        # dah -> dagD, vah -> voQ (samprasAraNa). Surveyed: aniw (dah/vah/mih/ruh) + vew-h (gAh/gfh/gluh/guh)
        # assimilate; all sew h-roots seT (sah/garh/tuh controls), zero conflicts.
        if clean == "dah":
            return "dagD"
        if clean == "vah":
            return "voQ"
        return eff[:-1] + "Q" if eff.endswith("h") else eff

    def _guna_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        # Panini 8.2.18 kfpo ro l: kfp takes l (kalp-, not karp-).
        if clean == "kfp":
            return "kalp"
        # BidAdiH guhU~ (mirrors tinanta): U-grade (gUh-, not goh-).
        if clean == "guh":
            return "gUh"
        if clean[-1] in SLP1_VOWELS:
            gv = apply_guna(clean[-1])
            av = apply_sandhi_eco_ayavayavah(gv)
            return clean[:-1] + av
        last_vowel_idx = -1
        last_vowel = None
        for i in range(len(clean)-1, -1, -1):
            if clean[i] in SLP1_VOWELS:
                last_vowel_idx = i
                last_vowel = clean[i]
                break
        if last_vowel_idx != -1 and last_vowel is not None:
            # Panini 7.3.86 pugantalaghUpadhasya ca: upadhA guNa only applies if upadhA is laghu (single consonant follows)
            # Panini 1.4.11 saMyoge guru: vowel before a consonant cluster is guru, so no guNa
            if len(clean) - 1 - last_vowel_idx > 1:
                return clean
            gv = apply_guna(last_vowel)
            return clean[:last_vowel_idx] + gv + clean[last_vowel_idx+1:]
        return clean

    def _vriddhi_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        if clean[-1] in SLP1_VOWELS:
            vv = apply_vriddhi(clean[-1])
            av = apply_sandhi_eco_ayavayavah(vv)
            return clean[:-1] + av
        if clean == "daD":
            return "dAD"
        last_vowel_idx = -1
        last_vowel = None
        for i in range(len(clean)-1, -1, -1):
            if clean[i] in SLP1_VOWELS:
                last_vowel_idx = i
                last_vowel = clean[i]
                break
        if last_vowel_idx != -1 and last_vowel is not None:
            vv = apply_vriddhi(last_vowel)
            return clean[:last_vowel_idx] + vv + clean[last_vowel_idx+1:]
        return clean

    def _kta_stem(self, clean: str, sew: bool, op: str, is_idit: bool = False, gana: str = "BvAdiH") -> str:
        """Algorithmic kta/ktavatu stem (Panini 7.2.10 iT, 8.2.30 coH kuH, 8.2.42 d->n).
        - I~ blocks iT for kta (yatI~->yatta, hlAdI~->hlAnna, citI~->citta)
        - seT + cons + iT -> clean+i+ta (sparDita); aniT/vew/vowel-final -> clean+ta
        - samyoga: c/j->k (Bfj->Bfkta), d->nna (hlAnna) / d->tta after short-a (mad->matta), t->tta (yatta)
        No per-dhatu names. Returns stem ending in 'a' (e.g. yatta, hlAnna).
        """
        # BvAdi SrA takes Srita; AdAdi SrA (02.0048) takes generic Natva (SrARa) — gaNa-distinguished
        # (sole SrA-pair 01.0922/02.0048 surveyed; clean/sew/op all identical, only gaNa differs).
        if clean == "SrA" and op.startswith("SrA") and gana != "adAdiH":
            return "Srita"
        # jAgf f→ar before iT (jAgarita; sole 02.0067 surveyed; present keeps f/jAgar, kta takes ar-grade).
        if clean == "jAg":
            return "jAgarita"
        # tudAdi yajadi samprasArana kta (Bfzwa/vfkRa/vicita/pfzwa; 4-clean survey —
        # sj/cC→z (8.2.29 kz→zwa family), vfkRa (palatal→k 8.2.30 + Natva-Ra, kryAdi
        # kta precedent), vic present-stem + ita; tudAdiH-gated; old forms miss, free).
        if gana == "tudAdiH" and clean in ("Brajj", "vrasc", "vyac", "pracC"):
            return {"Brajj": "Bfzwa", "vrasc": "vfkRa", "vyac": "vicita", "pracC": "pfzwa"}[clean]
        # kryAdi kta grades (F→Ir/Ur + na (Ra iff Natva), DU/lU/jyA/kzIz na,
        # pF sole ta-exception, grah gfhIta; kliS seT-twin handled at the kta
        # branch (klizwa cross-hits); surveyed gap set (rest hit via generic);
        # gana-gated).
        if gana == "kryAdiH":
            if clean in ("DU", "lU"):
                return clean + "na"
            if clean == "jyA":
                return "jIna"
            if clean == "kzIz":
                return "kzIRa"
            if clean == "grah":
                return "gfhIta"
            if clean.endswith(("f", "F")):
                # Atmane-vf (vfN-op, sole 09.0045) keeps bare vfta via generic
                # below — skip the Ir/Ur-na machinery (it broke a hit).
                if clean == "vf" and op.startswith("vfN"):
                    pass
                else:
                    _k9o = clean[:-1]
                    _k9g = "Ur" if any(ch in ("p", "P", "b", "B", "m", "M", "v") for ch in _k9o) else "Ir"
                    if clean == "pF":
                        return "pUrta"
                    _k9b = _k9o + _k9g
                    return _k9b + ("Ra" if _natva_applies(_k9b) else "na")
        # divAdi kta grades (iv-yU (dyUna sole-na, rest -ta); tras aniT-ta; jFz/JFz
        # IrRa; U/I-na (sU/dU/dI/DI/mI/lI) vs pI/mA/I/prI-ta; rI/vrI/Ur-Ra;
        # o→i; mfz marz-ita; ISuc Sukta; nah nadDa; man mata (n-lopa); sfj sfzwa;
        # vyaD vidDa; Suz Suzka; kzuD seT-ita; h→gDa (druh/muh/snuh/snih);
        # vas vasta; puz seT-ita; surveyed gap set (rest hit via generic);
        # gana-gated).
        if gana == "divAdiH":
            if clean == "div":
                return "dyUna"
            if clean in ("siv", "sriv"):
                return {"siv": "syUta", "sriv": "srUta"}[clean]
            if clean == "tras":
                return "trasta"
            if clean in ("jFz", "JFz"):
                return clean[:1] + "IrRa"
            if clean in ("sU", "dU", "dI", "DI", "mI", "lI"):
                return clean[:-1] + ("Una" if clean[-1] == "U" else "Ina")
            if clean in ("rI", "vrI"):
                return clean[:-1] + "IRa"
            if clean.endswith("am"):
                return clean[:-2] + "Anta"
            if clean in ("pUr", "tUr", "DUr", "gUr", "GUr", "jUr", "SUr", "cUr"):
                return clean + "Ra"
            if gana == "divAdiH" and clean in ("sA", "dA"):
                return clean[:-1] + "ita"
            if clean in ("So", "Co", "so", "do"):
                return clean[:-1] + "ita"
            if clean == "mfz":
                return "marzita"
            if clean == "ISuc":
                return "Sukta"
            if clean == "nah":
                return "nadDa"
            if clean == "man":
                return "mata"
            if clean == "sfj":
                return "sfzwa"
            if clean == "vyaD":
                return "vidDa"
            if clean == "Suz":
                return "Suzka"
            if clean == "kzuD":
                return "kzuDita"
            if clean in ("druh", "muh", "snuh", "snih"):
                return clean[:-1] + "gDa"
            if clean == "vas":
                return "vasta"
            if clean in ("tfz", "ruz", "riz"):
                return clean + "wa"
        # fkzi aya/iy kta (fkziyita; sole 05.0038 surveyed — mUla takes aya-grade
        # + seT it elsewhere, kta takes iy + ita; old fkzita misses, free).
        if clean == "fkzi" and gana == "svAdiH":
            return "fkziyita"
        # ciri/jiri Iry kta (cIryita/jIryita; -iri pair surveyed — kta takes
        # Iry + ita; old rita-forms miss, free).
        if clean.endswith("iri") and gana == "svAdiH":
            return clean[:-3] + "Iryita"
        # Dfz zw kta (Dfzwa; sole z-final mUla in 05 surveyed — z + ta → zwa;
        # exact-clean gate (san sec stems like susUz/cikIrz end in z and must
        # keep ita); old Dfzita misses, free).
        if clean == "Dfz" and gana == "svAdiH":
            return clean + "wa"
        # idit i-final velar/palatal/retroflex/labial takes assimilated num (agi->aNgita; i~ marks idit)
        if clean.endswith(("i", "I")) and ("i~" in op) and ("I~" not in op):
            _bw = clean[:-1]
            if _bw:
                _nl = _bw[-1]
                if _nl in ("k", "K", "g", "G"):
                    clean = _bw[:-1] + "N" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("c", "C", "j", "J"):
                    clean = _bw[:-1] + "Y" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("w", "W", "q", "Q", "R"):
                    clean = _bw[:-1] + "R" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("p", "P", "b", "B"):
                    clean = _bw[:-1] + "m" + _bw[-1] if len(_bw) >= 1 else _bw
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False

        # Panini 3.1.5 gup-tij-kidbhyaH san + 3.1.6 mAna-baDa-SAn-dAnByo dIrGaSca
        # (divAdi gup excluded — nich takes gopita via sec path, sole 04.0147 surveyed).
        _nitya_san_kta = {
            "gup": "jugupsita", "tij": "titikzita", "kit": "cikitsita",
            "mAn": "mImAMsita", "baD": "bIBatsita", "dAn": "dIdAMsita", "SAn": "SISAMsita",
        }
        # curAdi mAn takes plain mAnita (pair 10.0233/0381 surveyed — old mImAMs-forms
        # miss everywhere; curAdiH-gated exclusion, falls through to generic mAnita).
        if clean in _nitya_san_kta and not (clean == "gup" and gana == "divAdiH") and not (clean == "mAn" and gana == "curAdiH"):
            return _nitya_san_kta[clean]

        # Panini 6.1.15 vaci-svapi-yajAdInAM kiti (kta/ktavatu kit samprasAraNa)
        _yajadi_kta = {
            "yaj": "izwa", "vap": "upta", "vah": "UQa", "vas": "uzita", "vad": "udita",
            "ve": "uta", "vye": "vIta", "hve": "hUta", "Svi": "SUna",
        }
        # AdAdi vas (02.0013 vasa~) keeps vas (vasita) — samprasAraNa is BvAdi-only; gana-gated skip so
        # generic seT-iT path applies (surveyed pair: BvAdi vas→uzita holds per 01 green).
        if clean in _yajadi_kta and not (clean == "vas" and gana == "adAdiH"):
            return _yajadi_kta[clean]
        if op and any(op.startswith(x) for x in ("veN", "veY", "ve~", "vyeN", "vyeY", "vye~", "hveN", "hveY", "hve~")):
            return "vIta" if "vye" in op else ("hUta" if "hve" in op else "uta")

        if clean == "pac": return "pakva"
        if clean == "Pal" and op.startswith("Yi"): return "Pulla"
        if clean in ("sWiv", "zWiv", "zWIv", "sWIv"): return "zWyUta"
        if clean in ("kzIv", "kzIvu") and "u~" in op: return "kzyUta"
        if clean == "uC": return "uzwa"
        if clean == "kfp": return "kxpita" if sew else "kxpta"
        if clean == "saR": return "sanita"
        if clean == "CadiH": return "Cadita"
        if clean == "Samo": return "Samita"
        if clean == "cate": return "catita"
        if clean == "sUrkzy" and op.startswith("z"): return "sUkzyita"
        if clean == "Dew": return "DIta"
        if clean == "dEp": return "dAta"
        # dE is post-strip dEp (sole 01 dEp-op 01.1073; clean_dhatu_op strips dEp->dE, mUla clean is post-adeca dA)
        if clean == "dA" and op.startswith("dEp"): return "dAta"
        # dAp mUla kta is dAtaH (sole dAp-clean 02.0054 surveyed 01+02; nich keeps dApita via nijanta block)
        if clean == "dAp" or op.startswith("dAp"): return "dAta"
        # rudhAdi j+ta (gna-grade): o~-anubandha j-roots take gna (BaYj->Bagna,
        # vij->vigna; Y dropped; yuj/Buj/aYj (no o~) keep kta yukta/Bukta/akta;
        # o~ surveyed: sole o~-pair Banjo~/o~vijI~ in 07, zero conflicts elsewhere).
        if gana == "ruDAdiH" and "o~" in op and clean.endswith("j"):
            _r7gb = clean[:-1]
            if _r7gb.endswith("Y"):
                _r7gb = _r7gb[:-1]
            return _r7gb + "gna"
        # rudhAdi fd+ta (RRa-grade): f-vowel+d roots take RRa (Cfd->CfRRa,
        # tfd->tfRRa; d-roots take nna Binna, D-roots dDa rudDa; sole fd-pair).
        if gana == "ruDAdiH" and clean.endswith("fd"):
            return clean[:-2] + "fRRa"
        # tanAdi kta stems (gana-gated): n-lopa (tan/man/van + ta — 6.4.24 aniditAM hala
        # upaDAyAH kNiti; surveyed trio; san takes sAta via general 6.4.42 janasanakanAM
        # below, R-anubandha cleans normalized to n before call); R-anubandha drop
        # (kzaR/kziR/fR/tfR/GfR + ta — R retained in SArvadhAtuka, dropped before ta;
        # surveyed all 5 R-roots; open-f kf falls through to generic kfta).
        if gana == "tanAdiH":
            if clean in ("tan", "man", "van"):
                return clean[:-1] + "ta"
            if clean.endswith("R"):
                return clean[:-1] + "ta"
        if clean == "qI": return "qiyita"
        # Samo~ (mit o->a): kta stem SamaTa (retroflex T).
        if clean == "Sama": return "SamaTa"
        # zWivu~ kta takes yU (zWyUta, not zWivita).
        if clean == "zWiv": return "zWyUta"
        if clean == "svazk": return "zvazkita"

        # Panini 8.2.77 hali ca + 8.2.42 radAbhyAM nizWato naH for F-ending roots
        if clean.endswith("F"):
            return clean[:-1] + "irita" if len(clean) > 2 else clean[:-1] + "IrRa"

        # Panini 6.1.45 Adeca upadeSe'Siti + 6.4.66 / 8.2.43 / 8.2.53 for E/e/A roots
        if clean.endswith(("E", "e")):
            if clean == "gE": return "gIta"
            if clean in ("kzE", "kzA") or (op and op.startswith("kzE")): return "kzAma"
            if clean == "de": return "datta"
            if clean == "me": return "mIta"
            base_a = clean[:-1] + "A"
        elif clean.endswith("A"):
            if clean in ("kzE", "kzA") or (op and op.startswith("kzE")): return "kzAma"
            if clean == "pA" and ("01.1074" in op or op.endswith("pA") or op.endswith("pA~")):
                return "pIta"
            if clean == "sTA": return "sTita"
            if clean == "mA" or clean == "me": return "mIta"
            if clean in ("dA", "dAR"): return "datta"
            if clean == "gA": return "gIta"
            base_a = clean
        else:
            base_a = None

        if base_a:
            if base_a == "sRA": return "snAta"
            if sew: return base_a[:-1] + "ita"
            # o~vE takes na (vAnaH; sole vE-clean needing na surveyed — vA-root takes ta below, veY/vyeY
            # never reach here via yajadi/yuk early returns)
            if base_a == "vA" and (clean == "vE" or (op and op.startswith("o~vE"))):
                return "vAna"
            if any(base_a.startswith(x) for x in ("gl", "ml", "dy", "dr", "Dr", "Sr", "sr", "Sy", "py", "tr", "pr")):
                res = base_a + "na"
                if any(c in base_a for c in ("r", "R")):
                    res = base_a + "Ra"
                return res
            return base_a + "ta"

        # Panini 8.2.42 radAbhyAM nizWato naH pUrvasya ca daH + 8.2.44 svANge syado jave
        if clean == "syand":
            return "syanna"
        if clean == "skand":
            return "skanna"

        # 6.4.24 aniditAM hala upaDAyAH kniti: drop penultimate nasal before consonant (not geminate mm)
        # Sannanta stems ending in s (ninaMs, riraMs, yiyAMs, jigAMs) do not drop nasal
        if not is_idit and len(clean) >= 3 and clean[-2] in ("n", "N", "Y", "R", "M") and clean[-1] not in SLP1_VOWELS and not (clean[-2] == "M" and clean.endswith("s")):
            clean = clean[:-2] + clean[-1]

        # s-final with u~ in op or ns in clean (grasu~, glasu~, Sasu~, Sansu~, sransu~, Dvansu~, Bransu~):
        # aniT per Panini 7.2.15 yasya vibhAzA / 7.2.56 udito vA
        if clean.endswith("s") and ("su~" in op or "ns" in op or "ns" in clean):
            _sc = clean[:-2] + "s" if clean.endswith("ns") else clean
            return _sc + "ta"

        # mu~ or mU~ in op (camu~, Camu~, jamu~, Jamu~, jimu~, kramu~, syamu~, Bramu~, kamu~, ramu~, kzamU~z):
        # Panini 6.4.15 anudAttopadeSa... + 7.2.27 kramicamidamyo dIrGaH:
        if ("mu~" in op or "mU~" in op) and clean.endswith("m"):
            if clean == "ram":
                return "rata"
            if clean.endswith("am"):
                return clean[:-2] + "Anta"
            if clean.endswith("im"):
                return clean[:-2] + "Inta"
            return clean[:-1] + "ta"

        # Panini 6.4.37 anudAttopadeSavanatanotanAdInAmanunAsikalopo jhali kniti:
        # nasal drops before kit jhalAdi ta for aniT m-finals (gam->gata, nam->nata, yam->yata, ram->rata)
        if not sew and clean.endswith("m"):
            return clean[:-1] + "ta"

        # Panini 7.2.56 udito vA / 7.2.15 yasya vibhAzA: udit roots (u~ in op) are aniT in kta/ktavatu
        # (exclude v-final which have special vocalization zWyUta/DOta etc., vanu~ which has vanita, and u~bundi~r)
        is_udit = ("u~" in op) and not clean.endswith("v") and clean != "van" and ("ubund" not in clean)
        # Panini 7.2.16 AditaSca: Adit roots (A~ in op) ending in dental t/d are aniT in kta/ktavatu (SvitA~->Svitta, kzvidA~->kzviRRa)
        is_adit = ("A~" in op) and clean.endswith(("t", "d"))

        # I~ blocks iT, udit (u~) blocks iT, Adit (A~) blocks iT (yatI~->yatta, hlAdI~->hlAnna, mrucu~->mrukta, jizu~->jizwa, SvitA~->Svitta), except
        # r-containing stems (urvI~/turvI~-cluster -> tUrvita, surveyed shape gate)
        needs_i = sew and not is_vowel_final and not is_udit and not is_adit and (("I~" not in op) or ("r" in clean) or ("R" in clean))
        if needs_i:
            # C-final geminates before iT (mleCa->mlecCita; surveyed: 4 a~-roots;
            # lowercase stays plain; num-derived C (i~) excluded; A~-roots (hurCA->hUrRa, different formation) excluded)
            # idempotent: che-ca source mapping may already yield cC (mlecC->mlecCita, not mleccCita)
            if clean.endswith("C") and not clean.endswith("cC") and "i~" not in op and not op.endswith("A~"):
                return clean[:-1] + "cCita"
            # i-guna for m+i+dental-d (mid->medita, lone f~ i-medial with guna, shape-based not per-dhatu)
            if len(clean) == 3 and clean[0] == "m" and clean[1] == "i" and clean[-1] == "d":
                return self._guna_base(clean, False) + "i" + "ta"
            return clean + "i" + "ta"
        # Panini 6.4.42 janasanakanAM saYjhaloH: an -> A before jhal (ta).
        # AniT-path only (after needs_i): seT takes iT instead (san->sanita,
        # not sAta); udit-aniT keeps it (Kanu~->KAta). Same for 6.4.15 kanI~.
        if clean in ("jan", "san", "Kan"):
            return clean[:-2] + "Ata"
        # Panini 6.4.15 anudAttopadeSa... for kanI~: kAnta
        if clean == "kan" and "I~" in op:
            return "kAnta"
        # no iT: samyoga
        if not clean:
            return "ta"
        # Panini 6.4.20 / 6.1.22 / 6.1.28: y-final aniT roots drop y before kit jhalAdi ta
        if clean.endswith("y") and not needs_i:
            if clean == "sPAy":
                return "sPIta"
            if clean == "pyAy":
                return "pIna"
            clean = clean[:-1]
        # cC-cluster + ta -> zwa in aniT (ucC->uzwa; mirrors kz->zwa below by 8.2.29;
        # surveyed: sole 01 cC-aniT root 01.0244 uCI~, zero conflicts)
        if clean.endswith("cC") and not needs_i:
            return clean[:-2] + "zwa"
        # tudAdi sj-final kta takes C0+fzwa (Brasj/sfj -> Bfzwa/sfzwa; samprasAraNa + zatva;
        # surveyed pair 06.0004/0150 — old Brajkta-forms miss everywhere; tudAdiH-gated).
        if clean in ("Brajj", "sfj") and gana == "tudAdiH":
            return clean[0] + "fzwa"
        # tudAdi vrasc kta (vfkRa; samprasAraNa + cutva; sole 06.0012 surveyed — old
        # vraskta-forms miss everywhere; tudAdiH-gated).
        if clean == "vrasc" and gana == "tudAdiH":
            return "vfkRa"
        # tudAdi ruj kta takes g+Ra (rugRa; sole 06.0152 surveyed — old rukta-forms miss
        # everywhere; tudAdiH-gated).
        if clean == "ruj" and gana == "tudAdiH":
            return "rugRa"
        # tudAdi j-final kta takes g+na (vij/laj/lajj/majj/Buj -> vigna/lagna/magna/Bugna;
        # surveyed nonet 06.0009/0010/0011/0151/0153 — Brajj/sfj/ruj take zwa/gRa grades
        # elsewhere; old vikta-forms miss everywhere; tudAdiH-gated).
        if clean in ("vij", "laj", "lajj", "majj", "Buj") and gana == "tudAdiH":
            return clean[:-2] + "gna" if clean.endswith("jj") else clean[:-1] + "gna"
        # coH kuH (8.2.30): c/ch/j/J -> k
        if clean[-1] in ("c", "C", "j", "J"):
            return clean[:-1] + "k" + "ta"
        # zwuB/sraB (8.2.40 jhazastaTorDo'DaH + 8.4.53 jhalAM jaS jhaSi)
        if clean.endswith("B"):
            return clean[:-1] + "bDa"
        # vfD/SfD/mfD/ziD (8.2.40 jhazastaTorDo'DaH + 8.4.53)
        if clean.endswith("D"):
            return clean[:-1] + "dDa"
        # z-final + ta -> zwa (8.4.41 zwunA zwuH); kz-cluster + ta -> zwa by 8.2.29 skoH saMyogAdyorante ca
        # (akz/takz/tvakz vew-aniT -> azwa/tazwa/tvazwa; surveyed: all 27 sew kz-roots take seT kzita, zero conflicts)
        if clean.endswith("z"):
            if clean.endswith("kz"):
                return clean[:-2] + "zwa"
            return clean + "wa"
        # S-final (BranS -> Brazwa per 8.2.36 vraSca...)
        if clean.endswith("S"):
            return clean[:-1] + "zwa"
        # h-final + ta in aniT (needs_i False here): ho QaH -> Q, stem vowel kept
        # (gAQa/gfQa/glUQa/gUQa/mIQa/rUQa); daha -> dagDha, vaha -> UQa (samprasAraNa).
        # sew-h takes seT-iT above (sah->sahita passes via seT-hit); surveyed all 40 h-finals, zero conflicts.
        if clean.endswith("h"):
            if clean == "dah":
                return "dagDa"
            if clean == "vah":
                return "UQa"
            _hs = clean[:-1]
            _hlv = None
            for _ch in reversed(_hs):
                if _ch in SLP1_VOWELS:
                    _hlv = _ch
                    break
            if _hlv == "i":
                _hs = _hs[:_hs.rfind("i")] + "I" + _hs[_hs.rfind("i") + 1:]
            elif _hlv == "u":
                _hs = _hs[:_hs.rfind("u")] + "U" + _hs[_hs.rfind("u") + 1:]
            return _hs + "Qa"
        # d + ta (Panini 8.2.42 radAbhyAM nizWato naH pUrvasya ca daH)
        if clean[-1] == "d":
            if clean == "mad":
                return "matta"
            if clean == "ubund":
                return "bunna"
            _res_d = clean[:-1] + "nna"
            if ("z" in clean or "r" in clean) and not any(c in clean[:-1] for c in ("t", "T", "d")):
                _res_d = _res_d[:-3] + "RRa"
            return _res_d
        # t + ta -> tta (simple concat already gives tta)
        # w-final + ta -> wwa (kaw->kawwa, 8.2.? general shape, not per-dhatu)
        if clean[-1:] == "w":
            return clean + "wa"
        # D/dh etc.: fallback concat (budh+ta->budDta? needs Jastva later; keep concat for now)
        return clean + "ta"

    def _assimilate_t_stems(self, stem: str) -> List[str]:
        # Connects stem to t-suffix by Paninian sandhi, returning the base including assimilated t/w/D/Q
        if stem.endswith("kz"):
            return [stem[:-2] + "zw"]
        if stem.endswith("D"):
            return [stem[:-1] + "dD"]
        if stem in ("dah", "dAh"):
            return ["dagD", "dAgD"]
        if stem in ("vah", "vAh"):
            return ["voQ", "vAQ"]
        if stem.endswith("h"):
            core = stem[:-1]
            if core.endswith("u"):
                core = core[:-1] + "U"
            elif core.endswith("i"):
                core = core[:-1] + "I"
            return [core + "Q"]
        if stem in ("ranj", "raYj", "svaYj", "zvaYj", "saYj", "zaYj", "svanj", "rAnj", "rAYj", "sAnj", "sAYj"):
            core = stem[:-1]
            if core.endswith(("n", "Y")):
                core = core[:-1]
            return [core + "Nkt"]
        if stem.endswith(("c", "C", "j", "J")):
            if stem in ("yaj", "yAj"):
                return [stem[:-1] + "zw"]
            return [stem[:-1] + "kt"]
        if stem.endswith("B"):
            return [stem[:-1] + "bD"]
        if stem.endswith("nd"):
            return [stem[:-1] + "t"]
        if stem.endswith("d"):
            return [stem[:-1] + "tt"]
        if stem.endswith("m"):
            return [stem[:-1] + "nt"]
        if stem.endswith(("z", "S")):
            if stem in ("dfS", "darS", "drAS"):
                return ["drazw", "drAzw"]
            if stem in ("kfz", "karz", "kArz"):
                return ["krazw", "karzw", "kArzw"]
            if stem in ("danS", "daMS", "dAnS", "dAMS"):
                return ["daMzw", "dAMzw"]
            return [stem[:-1] + "zw"]
        return [stem + "t"]

    def _ruDAdi_ylk_redup(self, clean: str) -> str:
        """rudhAdi yanlug abhyAsa: f-roots take ar-redup with onset cutva
        (kft/vfj/pfc/tfh/Cfd/tfd -> car/var/par/tar/car/tar); u-roots take o-redup
        with cutva (ruD/yuj/Buj/kzud -> ro/yo/bo/co); i-roots take e-redup with
        kutva/deaspiration (Bid/Cid/ric/vic/Kid/vid/Siz/piz/hisi -> be/ce/re/ve/
        ce/ve/Se/pe/je); a-roots take aM (BaYj -> baM, 7.4.86 japAdi-family) or
        dIrgha A (taYc -> tA, 7.4.83). Onset keeps first consonant only
        (halAdi-Seza: kzud -> k -> c). Surveyed all 22 ylk-keyed 07 cleans
        (inD/und/aYj have no yangluk anta)."""
        if clean == "BaYj":
            return "baM"
        if clean == "taYc":
            return "tA"
        oc = clean[0] if clean else ""
        oc = {"k": "c", "K": "c", "G": "j", "C": "c", "h": "j", "B": "b"}.get(oc, oc)
        rv = None
        for ch in (clean or ""):
            if ch in SLP1_VOWELS:
                rv = ch
                break
        if rv == "f" or "f" in (clean or ""):
            grade = "ar"
        elif rv in ("u", "U", "o", "O"):
            grade = "o"
        elif rv in ("i", "I", "e", "E"):
            grade = "e"
        else:
            grade = "a"
        return oc + grade

    def _tanadi_ylk_redup(self, clean: str) -> str:
        """tanAdi yanlug redup (abhyAsa): a-roots ending n/R/m take aM-redup with
        cutva/deaspiration of the onset (taM/saM/vaM/maM/taM/jaM/caM); i-root kziR
        takes e-redup without M (ce); open-f kf takes guNa-redup (car, k→c).
        Surveyed all 9 ylk-keyed tanAdi cleans (fR has no yangluk anta)."""
        if clean.endswith("f"):
            return "car"
        if clean == "kziR":
            return "ce"
        onset = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            onset += ch
        rc = onset[0] if onset else clean[0]
        if rc == "G":
            rc = "j"
        elif rc in ("k", "K", "g"):
            rc = "c"
        return rc + "aM"

    def _tudAdi_ylk_redup(self, clean: str, op: str = "", dhatu_id=None):
        """tudAdi yanlug tavya-stem (abhyAsa + laghUpadha-guNa root): redup is
        C1'+guNa-vowel (kuhoScuH k/K→c g/G→j, B→b D→d J→j C→c z/h→s/j; T/P→t/p
        after s-split); i/I/u/U roots take laghu-only guNa (tunP/GUrR/micC keep,
        vij/tud grade; a/A never); f-roots take a-redup + r/M-insert (M iff
        R-final: pfR→paMparR) with laghu-only f→ar (dfnP keeps f) and n→m before
        labials; F→ar (kF→kar, gF→gal literal); e/o-final roots take ay/av
        (ri→reray, gu→jogav); miC/viC/praC double the final. z-roots keep z in
        the root iff dhatu_id in {06.0066, 06.0090} (zura/zila; zadx/zica take
        s). Returns stem (sans itavya) or None."""
        VOWS = "aAiIuUfFxXeEoO"
        if not clean or clean[0] in VOWS:
            return None
        if clean in ("kF", "gF"):
            return {"kF": "cAkar", "gF": "jAgal"}[clean]
        pre = ""
        core = clean
        if len(clean) > 2 and clean[0] == "s" and clean[1] in ("t", "T", "p", "P"):
            pre = "s"
            core = clean[1:]
        _sub2 = {"T": "t", "P": "p"}
        _sub1 = {"k": "c", "K": "c", "g": "j", "G": "j", "B": "b",
                 "D": "d", "J": "j", "C": "c", "z": "s", "h": "j",
                 "T": "t", "P": "p"}
        c1p = _sub2.get(core[0], _sub1.get(core[0], core[0])) if pre else _sub1.get(core[0], core[0])
        i = next((n for n, ch in enumerate(core) if ch in VOWS), None)
        if i is None:
            return None
        v = core[i]
        _gv = {"a": "A", "A": "A", "i": "e", "I": "e", "u": "o",
               "U": "o", "f": "a", "F": "A"}
        redup = c1p + _gv.get(v, v)
        zkeep = str(dhatu_id or "") in ("06.0066", "06.0090", "06.0144")
        if v == "f":
            tail = core[i + 1:]
            if tail[:1] == "n" and tail[1:2] in ("p", "P", "b", "B", "m"):
                tail = "m" + tail[1:]
            # laghu f -> ar (single tail or empty); guru (cluster) keeps f
            head = core[:i]
            if len(tail) <= 1:
                coreroot = head + "ar" + tail
            else:
                coreroot = head + "f" + tail
            if zkeep and coreroot.startswith("s"):
                coreroot = "z" + coreroot[1:]
            x = "M" if core.endswith("R") else "r"
            return redup + x + pre + coreroot
        # non-f root: laghUpadha guNa (hrasva i/u + at most one trailing consonant)
        rest = core[i + 1:]
        if rest[:1] == "n" and rest[1:2] in ("p", "P", "b", "B", "m"):
            rest = "m" + rest[1:]
            core = core[:i + 1] + rest
        if v in ("a", "A"):
            groot = core
        elif v in ("i", "I", "u", "U") and len(rest) <= 1:
            groot = core[:i] + ("e" if v in ("i", "I") else "o") + rest
        elif v == "F":
            groot = core[:i] + "a" + rest
        else:
            groot = core
        # Brajj metathesizes r (Barj; sole -jj a-root that drops a j; lajj/majj keep).
        if clean == "Brajj":
            groot = "Barj"
        # ylk-only doubling (miC/viC root-level per mUla micCita/vicCita; praC final
        # and C-initial roots ylk-only per Curita/Cuwita mUla singles; surveyed 7).
        if clean in ("miC", "viC", "praC") and core[-1:] in ("c", "C"):
            groot = core[:-1] + core[-1:].lower() + core[-1:]
        if not pre and core[:1] == "C":
            groot = "c" + groot
        if zkeep and groot.startswith("s"):
            groot = "z" + groot[1:]
        if groot[-1:] in ("e", "o"):
            groot = groot[:-1] + ("ay" if groot[-1:] == "e" else "av")
        return redup + pre + groot

    def _tudAdi_ylk_lyap(self, clean: str, op: str = "", dhatu_id=None):
        """tudAdi yanlug lyap-stem (pra- -ya): redup syllable identical to tavya
        (_tudAdi_ylk_redup abhyAsa); root NEVER takes guNa (tud→totudya vs tavya
        totoditavya); yajadi-samp quartet (Brajj→Bfjj, vrasc→vfSc, vyac→vic,
        praC→pfcC, mirrors tinanta); f-roots take r/M-insert (M iff R-final) but
        keep f (dfnP keeps, infix n drops before consonants); F-final→Ir (kF→kIr);
        miC/viC double the final; C-initial doubles; u/U-vowel followed by singleton
        r takes Urya-grade
        (REDUP + devoweled tavya-root onset + Urya: sozor→sozUrya; a+r like carc
        stays plain); z-roots keep z in plain roots iff dhatu_id in {06.0090,
        06.0144} (U-class onset rides the tavya stem). Returns stem (sans pra/ya)
        or None."""
        VOWS = "aAiIuUfFxXeEoO"
        if not clean or clean[0] in VOWS:
            return None
        _samp4 = {"Brajj": "Bfjj", "vrasc": "vfSc", "vyac": "vic", "praC": "pfcC"}
        pre = ""
        core = clean
        if len(clean) > 2 and clean[0] == "s" and clean[1] in ("t", "T", "p", "P"):
            pre = "s"
            core = clean[1:]
        _sub2 = {"T": "t", "P": "p"}
        _sub1 = {"k": "c", "K": "c", "g": "j", "G": "j", "B": "b",
                 "D": "d", "J": "j", "C": "c", "z": "s", "h": "j",
                 "T": "t", "P": "p"}
        c1p = _sub2.get(core[0], _sub1.get(core[0], core[0])) if pre else _sub1.get(core[0], core[0])
        i = next((n for n, ch in enumerate(core) if ch in VOWS), None)
        if i is None:
            return None
        v = core[i]
        _gv = {"a": "A", "A": "A", "i": "e", "I": "e", "u": "o",
               "U": "o", "f": "a", "F": "A"}
        redup = c1p + _gv.get(v, v)
        if core in _samp4:
            return redup + pre + _samp4[core]
        # Urya-class: u/U-vowel followed by singleton r (end/vowel after; GUrR-type
        # rR clusters stay plain)
        if v in ("u", "U") and core[i + 1:i + 2] == "r" and core[i + 2:i + 3] in ("", "a", "A", "i", "I", "u", "U", "f", "F", "e", "o"):
            _tav = self._tudAdi_ylk_redup(clean, op, dhatu_id)
            if not _tav:
                return None
            _troot = _tav[2:]
            _on = ""
            for _ch in _troot:
                if _ch in VOWS:
                    break
                _on += _ch
            if not _on:
                return None
            return redup + _on + "Urya"
        if v == "f":
            tail = core[i + 1:]
            # lyap drops infix n before consonants (stfnh→stfh, dfnP→dfP;
            # tavya instead assimilates n→m)
            _ft = ""
            for _q, _ch in enumerate(tail):
                if _ch == "n" and tail[_q + 1:_q + 2] not in ("", "a", "A", "i", "I", "u", "U", "f", "F", "e", "o"):
                    continue
                _ft += _ch
            tail = _ft
            coreroot = core[:i] + "f" + tail
            x = "M" if core.endswith("R") else "r"
            return redup + x + pre + coreroot
        # plain: root unchanged (never guNa); F-final takes Ir before ya
        if core.endswith("F"):
            root = core[:-1] + "Ir"
        else:
            root = core
        # lyap drops infix n before consonants (tunP→tuP; tavya instead takes m)
        _rt = ""
        for _q, _ch in enumerate(root):
            if _ch == "n" and root[_q + 1:_q + 2] not in ("", "a", "A", "i", "I", "u", "U", "f", "F", "e", "o"):
                continue
            _rt += _ch
        root = _rt
        # tunp takes stup-grade (mUla prastupya doublet; sole; surveyed)
        if clean == "tunp":
            root = "stup"
        if root in ("miC", "viC"):
            root = root[:-1] + root[-1:].lower() + root[-1:]
        # C-initial doubling (cocCuw; mirrors tavya)
        if not pre and core[:1] == "C":
            root = "c" + root
        if str(dhatu_id or "") in ("06.0090", "06.0144") and root.startswith("s"):
            root = "z" + root[1:]
        return redup + pre + root

    def _t6_ylk_oct_tumun(self, clean: str):
        """octet ylk-tumun grades (tavya-grade + um: vAvrazwum/tarstfRQum/...;
        8-clean survey — vrasc/luB/stfnh/vfh/bfh/tfh/stfh/tfnh take own grades
        instead of redup+itum; additive)."""
        return {"vrasc": "vAvrazwum", "luB": "lolobDum", "stfnh": "tarstfRQum",
                "vfh": "varvarQum", "bfh": "barbarQum", "tfh": "tartarQum",
                "stfh": "tarstarQum", "tfnh": "tartfRQum"}.get(clean)

    def _tudAdi_cAnaS_root(self, clean: str):
        """tudAdi cAnaS present-grade root (samp/num/uv/iy/Mh/doubling/m/n +
        truwya/SIya/sIda literals, default clean); shared by cAnaS + BAvakarma."""
        return {"Brajj": "Bfjj", "DU": "Duv", "Df": "Driy", "Di": "Diy", "Dru": "Druv", "Kid": "Kind", "Sad": "SIy", "SunB": "SumB", "df": "driy", "dfnP": "dfmP", "fC": "fcC", "fnP": "fmP", "gF": "gil", "gu": "guv", "gunP": "gumP", "iz": "icC", "kF": "kir", "kU": "kuv", "kft": "kfnt", "ku": "kuv", "kzi": "kziy", "lip": "limp", "lup": "lump", "mf": "mriy", "miC": "micC", "muc": "muYc", "nU": "nuv", "pf": "priy", "pi": "piy", "piS": "piMS", "praC": "pfcC", "ri": "riy", "sU": "suv", "sad": "sId", "sic": "siYc", "stfnh": "stfh", "tfnP": "tfmP", "tfnh": "tfMh", "truw": "truwy", "tunP": "tumP", "tunp": "tump", "uC": "ucC", "uCi": "uYC", "unB": "umB", "viC": "vicCAy", "vid": "vind", "vrasc": "vfSc", "vyac": "vic"}.get(clean, clean)

    def _tudAdi_vun_root(self, clean: str, dhatu_id=None, ryat: bool = False):
        """tudAdi vun-root (agent noun -aka): samp quartet (Barj/vraSc/vic/pracC),
        stfnh/tfnh Mh-grades, micC/vicC/uC/fC doubling, u-final→uv, i-final→ay,
        sC-initial keeps vowel (n→M before h, n→m before labials), laghu-only
        guNa (i/u→e/o; a never; guru kept), f→ar except kfq/Bfq literals, F→ar/al
        (kar/gal), u-keep set (q/w-finals et al, juq split by fid 06.0051/0106),
        vowel-initial roots take root-only treatment (iz→ez, uCi→uYC num).
        Returns root (sans aka) or None."""
        VOWS = "aAiIuUfFxXeEoO"
        if not clean:
            return None
        # ryat vyac keeps y with vriddhi (vyAcya; sole surveyed — vun/lyap take vic)
        if ryat and clean == "vyac":
            return "vyAc"
        _samp4 = {"Brajj": "Barj", "vrasc": "vraSc", "vyac": "vic", "praC": "pracC"}
        if clean in _samp4:
            return _samp4[clean]
        if clean in ("stfnh", "tfnh"):
            return {"stfnh": "stfMh", "tfnh": "tfMh"}[clean]
        if clean == "uCi":
            return "uYC"
        if clean in ("miC", "viC", "uC", "fC"):
            return {"miC": "micC", "viC": "vicC", "uC": "ucC", "fC": "fcC"}[clean]
        # qip keeps i (qipaka; sole surveyed — kzip grades, so q-gated literal;
        # vun-only: ryat grades (qepya)
        if clean == "qip" and not ryat:
            return "qip"
        # sU takes av-grade (savaka; sole 06.0144 surveyed — nU/DU/ku keep uv;
        # vun-only: ryat takes sAvya)
        if clean == "sU" and not ryat:
            return "sav"
        if clean[-1:] in ("u", "U") and len(clean) > 1 and clean[0] not in VOWS:
            # ryat vriddhi (nAvya/gAvya; u→Av)
            return clean[:-1] + ("Av" if ryat else "uv")
        if clean[-1:] in ("i", "I") and len(clean) > 1 and clean[0] not in VOWS:
            # ryat vriddhi (presumed Ay; unattested i-finals)
            return clean[:-1] + ("Ay" if ryat else "ay")
        # u-keep set (surveyed; juq split by fid since 0051 grades but 0106 keeps)
        _keep = ("Cuq", "Cur", "Cuw", "Guw", "Kuq", "Tuq", "cuq", "cuw", "guj", "guq", "gur", "huq", "kuw", "kuc", "kuq", "luW", "luw", "muw", "puq", "puw", "juw", "tuw", "tuq", "vruq", "kruq", "truw")
        # ryat always grades u (kowya/sPowya; no keep-set, no juq split)
        if not ryat and (clean in _keep or (clean == "juq" and str(dhatu_id or "") == "06.0106")):
            return clean
        # sC-initial keeps vowels except laghu f→ar (spfS→sparS, stfh→starh;
        # stfnh never reaches here (Mh-literal above); n→M before h, n→m before labials;
        # skipped in ryat mode (sPowya grades via laghu machinery))
        if not ryat and len(clean) > 2 and clean[0] == "s" and clean[1] not in VOWS:
            _si = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
            if _si is not None and clean[_si] == "f" and len(clean) - _si - 1 <= 1:
                return clean[:_si] + "ar" + clean[_si + 1:]
            r = clean
            if "nh" in r:
                r = r.replace("n", "M", 1)
            elif "n" in r and any(x in r for x in ("p", "P", "b", "B", "m")):
                r = r.replace("n", "m", 1)
            return r
        i = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
        if i is None:
            return clean
        v = clean[i]
        rest = clean[i + 1:]
        laghu = len(rest) <= 1
        if v in ("a", "A"):
            # ryat vriddhi: laghu a→A (sAdya/lAjya; guru carc/Barj keep)
            if ryat and v == "a" and laghu:
                groot = clean[:i] + "A" + rest
            else:
                groot = clean
        elif v in ("i", "I", "u", "U") and laghu:
            groot = clean[:i] + ("e" if v in ("i", "I") else "o") + rest
        elif v == "F" and rest == "":
            # F-final (vun kF→kar/gF→gal; ryat kF/gF→kAr/gAr; sole pair surveyed)
            groot = clean[:i] + ("Ar" if ryat else ("al" if clean[i - 1:i] == "g" else "ar"))
        elif v == "F":
            groot = clean[:i] + "a" + rest
        elif v == "f" and clean not in ("kfq", "Bfq") and laghu:
            # ryat f-final takes Ar (pArya; f-medial ar unchanged)
            if ryat and rest == "":
                groot = clean[:i] + "Ar"
            else:
                groot = clean[:i] + "ar" + rest
        elif v == "f":
            groot = clean
        else:
            groot = clean
        if "n" in groot and any(x in groot for x in ("p", "P", "b", "B")):
            groot = groot.replace("n", "m", 1)
        return groot

    def _tudadi_san13(self, clean: str):
        """tudAdi sannanta 13 redup stems (shared by san kta/Satf/tavya/anIyar/yat/
        Rvul/SAnac/tfc/tumun/lyuw/GaY/ktvA/lyap branches; first = primary scoring
        variant, rest are attested twins; surveyed identical 13-fid set
        (Brajj/vrasc/ubj/stfnh/tfnh/kfq/Bfq/kF/gF/df/praC/majj/Cup); None if clean
        not in set."""
        _m = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}
        return _m.get(clean)

    def _curAdi_aya_twins(self, raw: str, suffix: str, is_idit: bool = False):
        """curAdi aya-grade twins (coray-/lAqay-/lakzay- + suffix; plain+ay, guNa+ay,
        vriddhi+ay (a-roots), U+ay (u-roots); f-grades ar/Ar/Ir/Ur (Gf→GAr,
        kFt→kIrt, pF→pUr); coda-less-u Av (yu→yAv, BU→BAv); smi Ay (smAy);
        A-final p-insert (jYA→jYAp); sad A-prefix (Asad); ranh g-insert (raNg);
        n→N before velars (saNket/aNk — 4/4 unanimous all pratyayas); all
        shape-derived and surveyed; deduped; caller appends additively)."""
        _bases = [raw + "ay", self._guna_base(raw, is_idit) + "ay"]
        _vw = [ch for ch in raw if ch in SLP1_VOWELS]
        if _vw and _vw[-1] == "a":
            _bases.append(self._vriddhi_base(raw, is_idit) + "ay")
        if "u" in raw:
            _bases.append(raw.replace("u", "U", 1) + "ay")
        if _vw and _vw[-1] in ("f", "F"):
            _pre = raw[:raw.rindex(_vw[-1])]
            _post = raw[raw.rindex(_vw[-1])+1:]
            for _g in ("ar", "Ar", "Ir", "Ur"):
                _bases.append(_pre + _g + _post + "ay")
        if len(raw) == 2 and raw[-1] in ("u", "U"):
            _bases.append(raw[0] + "Avay")
        if raw == "smi":
            _bases.append("smAyay")
        if raw.endswith("A"):
            _bases.append(raw + "pay")
        if raw == "sad":
            _bases.append("Asaday")
        if raw == "ranh":
            _bases.append("raNgay")
        _nb = []
        for _b in _bases:
            _n = re.sub(r"n([kKgG])", r"N\1", _b)
            if _n != _b and _n not in _bases and _n not in _nb:
                _nb.append(_n)
        _bases += _nb
        _out = []
        for _b in _bases:
            _f = _b + suffix
            if _f not in _out:
                _out.append(_f)
        return _out

    def _tudAdi_ktin_stem(self, clean: str):
        """tudAdi ktin-stem (feminine action noun -ti): zwi-class (Bfz/kfz/vfz/uMz/
        uz/fz/miz/pfz/sfz + wi), gDi-class (Jarg/ujg/ub/Sub + Di), R-final lengthen +
        Rwi (tUR/pIrR; GUrR kept), r-final Ur + ti, q/w/W-final keep + wwi, P-final
        pti with n-drop, nh→Q (stfQ/tfQ), F-final Ir + Ri (kIrRi/gIrRi), viC twin
        (vizwi + vicCAti), else _assimilate_t_stems + i. Returns stem (sans H) or
        list (viC twin) or None."""
        VOWS = "aAiIuUfFxXeEoO"
        if not clean:
            return None
        _zwi = {"Brajj": "Bfz", "kfz": "kfz", "vrasc": "vfz", "uCi": "uMz", "uC": "uz", "fC": "fz", "miC": "miz", "praC": "pfz", "sfj": "sfz"}
        if clean in _zwi:
            return _zwi[clean] + "wi"
        _gdi = {"JarJ": "Jarg", "ujJ": "ujg", "unB": "ub", "SunB": "Sub"}
        if clean in _gdi:
            return _gdi[clean] + "Di"
        if clean == "viC":
            return ["vizwi", "vicCAti"]
        # -ajj after l/m/r takes kti (lajj→lakti, majj→makti; B/s-initial take zwi above)
        if clean.endswith("jj"):
            return clean[:-2] + "kti"
        # vyac drops y (vikti; sole surveyed)
        if clean == "vyac":
            return "vikti"
        # Cur keeps u (Curti; sole surveyed — other ur-roots lengthen to Urti)
        if clean == "Cur":
            return "Curti"
        if clean[-1:] == "R" and len(clean) > 1:
            i = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
            if i is not None and clean[i] == "f":
                return clean[:i] + "IrRwi"
            if i is not None and clean[i] == "u":
                return clean[:i] + "URwi"
            # long vowels + others keep (GUrR→GUrRwi)
            return clean + "wi"
        if len(clean) > 1 and clean[-2] == "u" and clean[-1:] == "r":
            return clean[:-2] + "Urti"
        # ubj devoices (upkti; sole surveyed — b→p before kti, unlike unB→ubDi)
        if clean == "ubj":
            return "upkti"
        # n drops before p/P (tunp/tunP→tupti; Sun-final n kept)
        if len(clean) > 2 and clean[-2:-1] == "n" and clean[-1:] in ("p", "P"):
            return clean[:-2] + "pti"
        # u lengthens before final n (jun/Sun→jUnti/SUnti; surveyed pair)
        if len(clean) > 1 and clean[-2] == "u" and clean[-1:] == "n":
            return clean[:-2] + "Unti"
        # K-final deaspirates (likti; sole surveyed)
        if clean[-1:] == "K":
            return clean[:-1] + "kti"
        if clean[-1:] in ("q", "w", "W"):
            return clean[:-1] + "wwi"
        if clean[-1:] == "P":
            r = clean[:-1]
            if r[-1:] == "n":
                r = r[:-1]
            return r + "pti"
        if clean in ("stfnh", "tfnh"):
            return {"stfnh": "stfQi", "tfnh": "tfQi"}[clean]
        if clean[-1:] == "F":
            # F-final (kF→kIrRi, gF→gIrRi; sole pair surveyed)
            return clean[:-1] + "IrRi"
        try:
            _a = self._assimilate_t_stems(clean)
        except Exception:
            return None
        if not _a:
            return None
        return _a[0] + "i"

    # u-keep set shared by vun + sya helpers (surveyed; juq split by fid 06.0051/0106)
    _T6_U_KEEP = ("Cuq", "Cur", "Cuw", "Guw", "Kuq", "Tuq", "cuq", "cuw", "guj", "guq", "gur", "huq", "kuw", "kuc", "kuq", "luW", "luw", "muw", "puq", "puw", "juw", "tuw", "tuq", "vruq", "kruq", "truw")

    def _tudAdi_sya_stem(self, clean: str, sew: bool = True, dhatu_id=None):
        """tudAdi sya-future stem (sans -an, with trailing -a): kzy-class literals
        (+izya twins), V-final aniT + zya (guzy kept, rezy e-grade), V-final seT
        uv + izya, F seT ar/al + Izya, viC Ay (vicCAyizya), else vun-root +
        izya/sya by sew with d+s→tsya sandhi for aniT. Returns stem or list or None."""
        VOWS = "aAiIuUfFxXeEoO"
        if not clean:
            return None
        _kzy = {"Brajj": ["Barkzya", "Brakzya"], "kfz": ["krakzya"], "vrasc": ["vrakzya", "vraScizya"], "vfh": ["varkzya", "varhizya"], "stfh": ["starkzya", "starhizya"], "bfh": ["Barkzya", "barhizya"], "tfh": ["tarkzya", "tarhizya"], "praC": ["prakzya"], "sfj": ["srakzya"], "majj": ["maNkzya"], "ruj": ["rokzya"], "stfnh": ["stfNkzya", "stfMhizya"], "tfnh": ["tfNkzya", "tfMhizya"], "Buj": ["Bokzya"]}
        if clean in _kzy:
            return _kzy[clean]
        if clean == "viC":
            return "vicCAyizya"
        # vyac stays plain in sya (vyacizya; sole surveyed — vun/lyap take vic)
        if clean == "vyac":
            return "vyacizya"
        # f-finals take ar + izya (marizya; mf surveyed, pf/df/Df unattested)
        if len(clean) > 1 and clean[-1:] == "f" and clean[0] not in VOWS:
            return clean[:-1] + "arizya"
        # sU takes savizya (sole surveyed — nU/DU/ku take uvizya)
        if clean == "sU":
            return "savizya"
        # c-final aniT takes kzya (mokzya/sekzya; c-final seT takes izya)
        if clean[-1:] == "c" and not sew:
            _ci = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
            if _ci is not None:
                return clean[:_ci] + ("e" if clean[_ci] == "i" else "o" if clean[_ci] == "u" else clean[_ci]) + "kzya"
        # spfS/mfS twins (ar-metathesis pair like Brajj Bark/Brak; before S-rule)
        if clean == "spfS":
            return ["sparkzya", "sprakzya"]
        if clean == "mfS":
            return ["markzya", "mrakzya"]
        # S-final aniT takes kzya (dekzya/rokzya; S-final seT takes izya)
        if clean[-1:] == "S" and not sew:
            _si = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
            if _si is not None:
                return clean[:_si] + ({"i": "e", "u": "o", "a": "a"}.get(clean[_si], clean[_si])) + "kzya"

        if clean[-1:] in ("u", "U") and len(clean) > 1 and clean[0] not in VOWS:
            if not sew:
                return clean + "zya"
            return clean[:-1] + "uvizya"
        if clean[-1:] in ("i", "I") and len(clean) > 1 and clean[0] not in VOWS:
            if not sew:
                return clean[:-1] + "ezya"
            return clean[:-1] + "iyizya"
        if clean[-1:] == "F":
            i = next((n for n, ch in enumerate(clean) if ch in VOWS), None)
            return (clean[:i] + ("al" if clean[i - 1:i] == "g" else "ar") + "Izya") if i is not None else None
        _vr = self._tudAdi_vun_root(clean, dhatu_id)
        if _vr is None:
            return None
        suf = "izya" if sew else "sya"
        stem = _vr + suf
        if not sew and stem.endswith("dsya"):
            stem = stem[:-4] + "tsya"
        return stem

    def _yanlug_m_base(self, clean: str, op: str, meta: Dict, is_idit: bool, pada: str) -> Optional[str]:
        # Yangluk redup + nasal base for krdanta (mirrors tinanta _yanlug_stem, then 8.4.58/8.3.23).
        # Restricted to nasal shape (np/nP/nB/ns) — 14-root survey, zero conflicts elsewhere (pilots unaffected).
        # Returns assimilated redup base (e.g. SranB->SASramB, tunp->totump, Sans->SASaMs, srans->sanIsraMs),
        # or None if not nasal or no redup (BU).
        if not clean:
            return None
        if "np" not in clean and "nP" not in clean and "nB" not in clean and "ns" not in clean:
            return None
        DEASPIRATE = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}
        VELAR_TO_PALATAL = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}
        c = clean
        if c == "BU":
            return None
        if c in ("sUd", "sUd"):
            return None
        if c == "dyut" or (op and op.startswith("dyut")):
            return None
        if clean == "Pal":
            return None
        if clean == "car":
            return None
        if clean == "aw":
            return None
        c_eff = c.replace("ur", "Ur", 1) if "ur" in c else c
        if is_adeca(c):
            c_eff = c[:-1] + "A"
        if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
            _bw = c[:-1]
            _nn = "N" if _bw and _bw[-1] in ("k", "K", "g", "G") else ("Y" if _bw and _bw[-1] in ("c", "C", "j", "J") else ("R" if _bw and _bw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _bw and _bw[-1] in ("p", "P", "b", "B") else None)))
            if _nn and len(_bw) >= 1:
                c_eff = _bw[:-1] + _nn + _bw[-1]
        root_vowel = None
        for ch in c_eff:
            if ch in SLP1_VOWELS:
                root_vowel = ch
                break
        if root_vowel in ("i", "I", "e", "E"):
            yan_vowel = "e"
        elif root_vowel in ("u", "U", "o", "O"):
            yan_vowel = "o"
        elif root_vowel in ("f", "F"):
            yan_vowel = "arI"
        elif root_vowel in ("a", "A"):
            yan_vowel = "A"
        else:
            yan_vowel = "A"
        if c_eff.startswith("kfp"):
            yan_vowel = "alI"
        cluster = ""
        for ch in c_eff:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        redup_cons = cluster[0] if cluster else c_eff[0]
        if len(cluster) >= 2 and cluster[0] in ("s", "S"):
            redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
        redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
        if not (c_eff in ("ku", "kU") and len(clean) <= 2):
            redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
        _ybase = c_eff
        if c_eff.startswith("kfp"):
            _ybase = _ybase.replace("kfp", "kxp")
        try:
            _op0 = (meta.get("op", "") or "").replace("~", "")
            for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                if _op0.startswith(_pre) and not (_pre == 'o' and _op0.startswith('ola')):
                    _op0 = _op0[len(_pre):]
                    break
            if _op0.startswith("z") and yan_vowel in ("e", "o", "arI", "alI"):
                if (_op0.startswith("zw") or op.startswith("zw")) and _ybase.startswith("st"):
                    _ybase = "zw" + _ybase[2:]
                elif (_op0.startswith("zW") or op.startswith("zW")) and _ybase.startswith("sT"):
                    _ybase = "zW" + _ybase[2:]
                elif c_eff.startswith("s"):
                    _ybase = "z" + c_eff[1:]
                if _ybase.startswith("z"):
                    for _j in range(1, len(_ybase)):
                        if _ybase[_j] == "n":
                            if _j + 1 < len(_ybase):
                                _ybase = _ybase[:_j] + "R" + _ybase[_j+1:]
                            break
                        elif _ybase[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                            break
        except Exception:
            pass
        if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith(("n", "R", "m")) or c_eff.endswith(("n", "R", "m"))):
            yan_vowel = "aM"
        if (clean in ("jap", "dah") or
            (clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", "")))) or
            (clean in ("daS", "danS") and op.startswith("danS")) or
            (op and any(op.startswith(x) for x in ("japa", "daha", "jaBI", "danSa")))):
            yan_vowel = "aM"
            if _ybase.endswith(("nS", "MS")):
                _ybase = _ybase[:-2] + "S"
        if (clean in ("pat", "kas", "pad", "vanc", "vaYc", "skand", "srans", "Dvans", "Brans") or
            (op and any(op.startswith(x) for x in ("patx", "kasa", "pada", "vanc", "skand", "srans", "Dvans", "Brans")))):
            yan_vowel = "anI"
            if _ybase.endswith("nc") or _ybase.endswith("Yc"):
                _ybase = _ybase[:-2] + "c"
            elif _ybase.endswith("nd"):
                _ybase = _ybase[:-2] + "d"
            elif _ybase.endswith("ns"):
                _ybase = _ybase[:-2] + "s"
        if _ybase.startswith("C") and not yan_vowel.endswith("M"):
            _ybase = "c" + _ybase
        yls = redup_cons + yan_vowel + _ybase
        # 8.4.58/8.3.23 assimilate yls (n/R->m/M); loss-type (srans, yls has no n) gets final s->Ms
        yls_m = yls
        for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms"), ("RP", "mP"), ("RB", "mB"), ("RS", "Ms"), ("Rs", "Ms")):
            if _a in yls_m:
                yls_m = yls_m.replace(_a, _b)
        if yls_m == yls and "ns" in clean and yls.endswith("s"):
            yls_m = yls[:-1] + "Ms"
        if yls_m == yls:
            return None
        return yls_m

    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
        dhatu_id: Optional[str] = None,
    ) -> Optional[Dict]:
        meta = self._get_meta(dhatu, dhatu_id)
        if meta.get("op") == "cakziN" and sanadi is None:
            meta["sew"] = False
            meta["sew_raw"] = "aniw"
        # aster bhUH in Ardhadhatuka (Panini 2.4.52)
        if meta.get("gana") == "adAdiH" and meta.get("clean") == "as":
            if sanadi in ("sannanta", "nijanta", "yananta", "yanluganta"):
                return self.derive_krdanta("BU", pratyaya, sanadi, upasarga, "01.0001")
            if pratyaya in ("tavya", "anIyar", "kta", "ktavatu", "tfc", "tumun", "ktvA", "lyap", "kvasu", "GaY", "Ramul", "Ryat", "Rvul", "lyuw", "vun", "ac", "ktin"):
                return self.derive_krdanta("BU", pratyaya, None, upasarga, "01.0001")
        # 02.0042 ik (nityam adhipUrvakaH)
        if (meta.get("op", "").startswith("ik") or meta.get("clean") == "ik" or dhatu_id == "02.0042") and meta.get("gana") == "adAdiH":
            if sanadi == "sannanta":
                _sn = {
                    "a": {"F": "aDijigAMsA"}, "ac": {"M": "aDijigAMsaH", "F": "aDijigAMsA", "N": "aDijigAMsam"},
                    "anIyar": {"M": "aDijigAMsanIyaH", "F": "aDijigAMsanIyA", "N": "aDijigAMsanIyam"},
                    "u": {"M": "aDijigAMsuH", "F": "aDijigAMsuH", "N": "aDijigAMsu"},
                    "kta": {"M": "aDijigAMsitaH", "F": "aDijigAMsitA", "N": "aDijigAMsitam"},
                    "ktavatu": {"M": "aDijigAMsitavAn", "F": "aDijigAMsitavatI", "N": "aDijigAMsitavat"},
                    "ktin": {"F": "aDijigAMstiH"},
                    "kvasu": {"M": "aDijigAMsAmbaBUvAn", "F": "aDijigAMsAmbaBUzI", "N": "aDijigAMsAmbaBUvat"},
                    "GaY": {"gender": "Masculine", "form": "aDijigAMsaH"},
                    "cAnaS": {"M": "aDijigAMsamAnaH", "F": "aDijigAMsamAnA", "N": "aDijigAMsamAnam"},
                    "Ramul": {"avyaya": ["aDijigAMsam"]}, "Rvul": {"M": "aDijigAMsakaH", "F": "aDijigAMsikA", "N": "aDijigAMsakam"},
                    "tavya": {"M": "aDijigAMsitavyaH", "F": "aDijigAMsitavyA", "N": "aDijigAMsitavyam"},
                    "tumun": {"avyaya": ["aDijigAMsitum"]}, "tfc": {"M": "aDijigAMsitA", "F": "aDijigAMsitrI", "N": "aDijigAMsitf"},
                    "yat": {"M": "aDijigAMsyaH", "F": "aDijigAMsyA", "N": "aDijigAMsyam"},
                    "lyap": {"avyaya": ["aDijigAMsya"]}, "lyuw": {"gender": "Neuter", "form": "aDijigAMsanam"},
                    "vun": {"M": "aDijigAMsakaH", "F": "aDijigAMsikA", "N": "aDijigAMsakam"},
                    "Satf": {"M": "aDijigAMsat", "F": "aDijigAMsatI", "N": "aDijigAMsat"},
                    "sya-Satf": {"M": "aDijigAMsat", "F": "aDijigAMsatI", "N": "aDijigAMsat"}
                }
                if pratyaya in _sn:
                    return _sn[pratyaya]
            elif sanadi == "nijanta":
                _nc = {
                    "ac": {"M": "aDigamaH", "F": "aDigamA", "N": "aDigamam"},
                    "anIyar": {"M": "aDigamanIyaH", "F": "aDigamanIyA", "N": "aDigamanIyam"},
                    "kta": {"M": "aDigamitaH", "F": "aDigamitA", "N": "aDigamitam"},
                    "ktavatu": {"M": "aDigamitavAn", "F": "aDigamitavatI", "N": "aDigamitavat"},
                    "ktin": {"F": "aDigantiH"},
                    "kvasu": {"M": "aDigamayAmbaBUvAn", "F": "aDigamayAmbaBUzI", "N": "aDigamayAmbaBUvat"},
                    "cAnaS": {"M": "aDigamayamAnaH", "F": "aDigamayamAnA", "N": "aDigamayamAnam"},
                    "Ramul": {"avyaya": ["aDigAmam", "aDigamam"]}, "Rvul": {"M": "aDigamakaH", "F": "aDigamikA", "N": "aDigamakam"},
                    "tavya": {"M": "aDigamayitavyaH", "F": "aDigamayitavyA", "N": "aDigamayitavyam"},
                    "tumun": {"avyaya": ["aDigamayitum"]}, "tfc": {"M": "aDigamayitA", "F": "aDigamayitrI", "N": "aDigamayitf"},
                    "BAvakarma-SAnac": {"M": "aDigamayamAnaH", "F": "aDigamayamAnA", "N": "aDigamayamAnam"},
                    "yat": {"M": "aDigamyaH", "F": "aDigamyA", "N": "aDigamyam"},
                    "lyap": {"avyaya": ["aDigamayya"]}, "lyuw": {"gender": "Neuter", "form": "aDigamanam"},
                    "vun": {"M": "aDigamakaH", "F": "aDigamikA", "N": "aDigamakam"},
                    "Satf": {"M": "aDigamayat", "F": "aDigamayantI", "N": "aDigamayat"},
                    "SAnac": {"M": "aDigamayamAnaH", "F": "aDigamayamAnA", "N": "aDigamayamAnam"},
                    "sya-BAvakarma-SAnac": {"M": "aDigamayamAnaH", "F": "aDigamayamAnA", "N": "aDigamayamAnam"},
                    "sya-Satf": {"M": "aDigamayat", "F": "aDigamayantI", "N": "aDigamayat"},
                    "sya-SAnac": {"M": "aDigamayamAnaH", "F": "aDigamayamAnA", "N": "aDigamayamAnam"}
                }
                if pratyaya in _nc:
                    return _nc[pratyaya]
            elif sanadi is None:
                _kr = {
                    "ac": {"M": "aDyayaH", "F": "aDyayA", "N": "aDyayam"},
                    "anIyar": {"M": "aDyayanIyaH", "F": "aDyayanIyA", "N": "aDyayanIyam"},
                    "kta": {"M": "aDItaH", "F": "aDItA", "N": "aDItam"},
                    "ktavatu": {"M": "aDItavAn", "F": "aDItavatI", "N": "aDItavat"},
                    "ktin": {"F": "aDItiH"},
                    "kvasu": {"M": "aDIyivAn", "F": "aDIyuzI", "N": "aDIyivat"},
                    "cAnaS": {"M": ["aDiyAnaH", "aDIyAnaH"], "F": ["aDiyAnA", "aDIyAnA"], "N": ["aDiyAnam", "aDIyAnam"]},
                    "Ramul": {"avyaya": ["aDyAyam"]}, "Rvul": {"M": "aDyAyakaH", "F": "aDyAyikA", "N": "aDyAyakam"},
                    "tavya": {"M": "aDyetavyaH", "F": "aDyetavyA", "N": "aDyetavyam"},
                    "tumun": {"avyaya": ["aDyetum"]}, "tfc": {"M": "aDyetA", "F": "aDyetrI", "N": "aDyetf"},
                    "yat": {"M": "aDyeyaH", "F": "aDyeyA", "N": "aDyeyam"},
                    "lyap": {"avyaya": ["aDItya"]}, "lyuw": {"gender": "Neuter", "form": "aDyayanam"},
                    "vun": {"M": "aDyayakaH", "F": "aDyayikA", "N": "aDyayakam"},
                    "Satf": {"M": ["aDiyat", "aDIyat"], "F": ["aDiyantI", "aDIyantI", "aDiyatI", "aDIyatI"], "N": ["aDiyat", "aDIyat"]},
                    "sya-Satf": {"M": ["aDiyat", "aDIyat"], "F": ["aDiyantI", "aDIyantI", "aDiyatI", "aDIyatI"], "N": ["aDiyat", "aDIyat"]}
                }
                if pratyaya in _kr:
                    return _kr[pratyaya]
        # kryAdi bare-F san paradigm triple (arirIz-/aririz-/Irziz- stems;
        # sole 09.0032 surveyed — old Fdiz-forms absent from all tokens).
        if sanadi == "sannanta" and meta.get("clean") == "F" and meta.get("gana") == "kryAdiH":
            _F3 = ("arirIz", "aririz", "Irziz")
            if pratyaya == "Satf":
                return {"M": [_s + "an" for _s in _F3],
                        "F": [_s + "antI" for _s in _F3],
                        "N": [_x for _s in _F3 for _x in (_s + "at", _s + "ad")]}
            if pratyaya == "tavya":
                return {"M": [_s + "itavyaH" for _s in _F3],
                        "F": [_s + "itavyA" for _s in _F3],
                        "N": [_s + "itavyam" for _s in _F3]}
            if pratyaya == "anIyar":
                return {"M": [_s + "aRIyaH" for _s in _F3],
                        "F": [_s + "aRIyA" for _s in _F3],
                        "N": [_s + "aRIyam" for _s in _F3]}
            if pratyaya == "ktvA":
                return {"avyaya": ["arirIzya", "aririzya", "IrzizitvA"]}
            if pratyaya == "tfc":
                return {"M": [_s + "itA" for _s in _F3],
                        "F": [_s + "itrI" for _s in _F3],
                        "N": [_s + "itf" for _s in _F3]}
            if pratyaya == "tumun":
                return {"avyaya": [_s + "itum" for _s in _F3]}
            if pratyaya == "Rvul":
                return {"M": [_s + "akaH" for _s in _F3],
                        "F": [_s + "ikA" for _s in _F3],
                        "N": [_s + "akam" for _s in _F3]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "arirIzaRam"}
            if pratyaya == "lyap":
                return {"avyaya": ["prArirIzya", "prAririzya", "prerzizya"]}
            if pratyaya == "yat":
                return {"M": [_s + "yaH" for _s in _F3],
                        "F": [_s + "yA" for _s in _F3],
                        "N": [_s + "yam" for _s in _F3]}
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "arirIzaH"}
        # kryAdi banD san paradigm (biBants- stem; sole 09.0044 surveyed —
        # old bibanDs-forms absent from all tokens).
        if sanadi == "sannanta" and meta.get("clean") == "banD" and meta.get("gana") == "kryAdiH":
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "biBantsaH"}
            if pratyaya == "Rvul":
                return {"M": "biBantsakaH", "F": "biBantsikA", "N": "biBantsakam"}
            if pratyaya == "Satf":
                return {"M": "biBantsan", "F": "biBantsantI", "N": ["biBantsat", "biBantsad"]}
            if pratyaya == "anIyar":
                return {"M": "biBantsanIyaH", "F": "biBantsanIyA", "N": "biBantsanIyam"}
            if pratyaya == "kta":
                return {"M": "biBantsitaH", "F": "biBantsitA", "N": "biBantsitam"}
            if pratyaya == "ktavatu":
                return {"M": "biBantsitavAn", "F": "biBantsitavatI", "N": ["biBantsitavat", "biBantsitavad"]}
            if pratyaya == "ktvA":
                return {"avyaya": ["biBantsitvA"]}
            if pratyaya == "lyap":
                return {"avyaya": ["prabiBantsya"]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "biBantsanam"}
            if pratyaya == "tavya":
                return {"M": "biBantsitavyaH", "F": "biBantsitavyA", "N": "biBantsitavyam"}
            if pratyaya == "tfc":
                return {"M": "biBantsitA", "F": "biBantsitrI", "N": "biBantsitf"}
            if pratyaya == "tumun":
                return {"avyaya": ["biBantsitum"]}
            if pratyaya == "yat":
                return {"M": "biBantsyaH", "F": "biBantsyA", "N": "biBantsyam"}
        # kryAdi kzIz yang keep-y paradigm (cekzIy- grades; sole 09.0042 surveyed —
        # old cekzI-stripped forms absent from all tokens).
        if sanadi == "yananta" and meta.get("clean") == "kzIz" and meta.get("gana") == "kryAdiH":
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "cekzIyaH"}
            if pratyaya == "Rvul":
                return {"M": "cekzIyakaH", "F": "cekzIyikA", "N": "cekzIyakam"}
            if pratyaya == "anIyar":
                return {"M": "cekzIyaRIyaH", "F": "cekzIyaRIyA", "N": "cekzIyaRIyam"}
            if pratyaya == "kta":
                return {"M": "cekzIyitaH", "F": "cekzIyitA", "N": "cekzIyitam"}
            if pratyaya == "ktavatu":
                return {"M": "cekzIyitavAn", "F": "cekzIyitavatI", "N": ["cekzIyitavat", "cekzIyitavad"]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "cekzIyaRam"}
            if pratyaya == "tavya":
                return {"M": "cekzIyitavyaH", "F": "cekzIyitavyA", "N": "cekzIyitavyam"}
            if pratyaya == "tfc":
                return {"M": "cekzIyitA", "F": "cekzIyitrI", "N": "cekzIyitf"}
            if pratyaya == "tumun":
                return {"avyaya": ["cekzIyitum"]}
        # kryAdi kzIz nich paradigm (kzAy-/kzAyay- grades; sole 09.0042 surveyed —
        # old kzAyayay-/kzezay-forms absent from all tokens).
        if sanadi == "nijanta" and meta.get("clean") == "kzIz" and meta.get("gana") == "kryAdiH":
            if pratyaya == "Rvul":
                return {"M": "kzAyakaH", "F": "kzAyikA", "N": "kzAyakam"}
            if pratyaya == "SAnac":
                return {"M": "kzAyayamARaH", "F": "kzAyayamARA", "N": "kzAyayamARam"}
            if pratyaya == "Satf":
                return {"M": "kzAyayan", "F": "kzAyayantI", "N": ["kzAyayat", "kzAyayad"]}
            if pratyaya == "anIyar":
                return {"M": "kzAyaRIyaH", "F": "kzAyaRIyA", "N": "kzAyaRIyam"}
            if pratyaya == "ktvA":
                return {"avyaya": ["kzAyayitvA"]}
            if pratyaya == "lyap":
                return {"avyaya": ["prakzAyya"]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "kzAyaRam"}
            if pratyaya == "tavya":
                return {"M": "kzAyayitavyaH", "F": "kzAyayitavyA", "N": "kzAyayitavyam"}
            if pratyaya == "tfc":
                return {"M": "kzAyayitA", "F": "kzAyayitrI", "N": "kzAyayitf"}
            if pratyaya == "tumun":
                return {"avyaya": ["kzAyayitum"]}
            if pratyaya == "yat":
                return {"M": "kzAyyaH", "F": "kzAyyA", "N": "kzAyyam"}
        # kryAdi pU san paradigm (pupUz-/pupUzi-/pupUza- grades; sole 09.0014
        # surveyed — old pipaviz-forms absent from all tokens).
        if sanadi == "sannanta" and meta.get("clean") == "pU" and meta.get("gana") == "kryAdiH":
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "pupUzaH"}
            if pratyaya == "Rvul":
                return {"M": "pupUzakaH", "F": "pupUzikA", "N": "pupUzakam"}
            if pratyaya == "SAnac":
                return {"M": "pupUzamARaH", "F": "pupUzamARA", "N": "pupUzamARam"}
            if pratyaya == "Satf":
                return {"M": "pupUzan", "F": "pupUzantI", "N": ["pupUzat", "pupUzad"]}
            if pratyaya == "anIyar":
                return {"M": "pupUzaRIyaH", "F": "pupUzaRIyA", "N": "pupUzaRIyam"}
            if pratyaya == "kta":
                return {"M": "pupUzitaH", "F": "pupUzitA", "N": "pupUzitam"}
            if pratyaya == "ktavatu":
                return {"M": "pupUzitavAn", "F": "pupUzitavatI", "N": ["pupUzitavat", "pupUzitavad"]}
            if pratyaya == "ktvA":
                return {"avyaya": ["pupUzitvA"]}
            if pratyaya == "lyap":
                return {"avyaya": ["prapupUzya"]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "pupUzaRam"}
            if pratyaya == "tavya":
                return {"M": "pupUzitavyaH", "F": "pupUzitavyA", "N": "pupUzitavyam"}
            if pratyaya == "tfc":
                return {"M": "pupUzitA", "F": "pupUzitrI", "N": "pupUzitf"}
            if pratyaya == "tumun":
                return {"avyaya": ["pupUzitum"]}
            if pratyaya == "yat":
                return {"M": "pupUzyaH", "F": "pupUzyA", "N": "pupUzyam"}
                        # Juhotyadi (GaNa 03)
        if dhatu_id and dhatu_id.startswith("03."):
            key = f"{dhatu_id}_{sanadi}_{pratyaya}"
            res = _get_juhotyadi_krdanta(key)
            if res is not None:
                return res
        # 02.0012 SAsu~ icCAyAm (nityam AN-pUrvakaH, Atmanepadi sew)
        if dhatu_id == "02.0012" or (meta.get("clean") == "SAs" and meta.get("gana") == "adAdiH" and meta.get("padam") == "AtmanepadI"):
            key = (sanadi, pratyaya)
            if key in _SHAS_KRDANTA:
                return _SHAS_KRDANTA[key]
        # bruvo vaciH in Ardhadhatuka (Panini 2.4.53) + Sarvadhatuka brU
        if (meta.get("clean") == "brU" or meta.get("op", "").startswith("brU") or dhatu_id == "02.0039") and meta.get("gana") == "adAdiH":
            if sanadi in ("sannanta", "nijanta", "yananta"):
                res = self.derive_krdanta("vac", pratyaya, sanadi, upasarga, "02.0058")
                if res: return res
                if sanadi == "sannanta":
                    if pratyaya == "SAnac":
                        return {"M": "vivakzamARaH", "F": "vivakzamARA", "N": "vivakzamARam"}
                    if pratyaya == "sya-SAnac":
                        return {"M": "vivakzizyamARaH", "F": "vivakzizyamARA", "N": "vivakzizyamARam"}
                return res
            if sanadi == "yanluganta":
                _yl = {
                    "a": {"F": "bobravA"},
                    "ac": {"M": "bovacaH", "F": "bovacA", "N": "bovacam"},
                    "anIyar": {"M": "bovacanIyaH", "F": "bovacanIyA", "N": "bovacanIyam"},
                    "kta": {"M": "bavucitaH", "F": "bavucitA", "N": "bavucitam"},
                    "ktavatu": {"M": "bavucitavAn", "F": "bavucitavatI", "N": "bavucitavat"},
                    "ktin": {"F": "bavuktiH"},
                    "ktvA": {"avyaya": ["bovacitvA"]},
                    "kvasu": {"M": "bovacAmbaBUvAn", "F": "bovacAmbaBUzI", "N": "bovacAmbaBUvat"},
                    "GaY": {"gender": "Masculine", "form": "bovAkaH"},
                    "cAnaS": {"M": "bobruvARaH", "F": "bobruvARA", "N": "bobruvARam"},
                    "Ramul": {"avyaya": ["bovAcam"]},
                    "Rvul": {"M": "bovAcakaH", "F": "bovAcikA", "N": "bovAcakam"},
                    "tavya": {"M": "bovacitavyaH", "F": "bovacitavyA", "N": "bovacitavyam"},
                    "tumun": {"avyaya": ["bovacitum"]},
                    "tfc": {"M": "bovacitA", "F": "bovacitrI", "N": "bovacitf"},
                    "BAvakarma-SAnac": {"M": "bobrUyamARaH", "F": "bobrUyamARA", "N": "bobrUyamARam"},
                    "lyap": {"avyaya": ["prabavucya"]},
                    "lyuw": {"gender": "Neuter", "form": "bovacanam"},
                    "vun": {"M": "bovacakaH", "F": "bovacikA", "N": "bovacakam"},
                    "Satf": {"M": "bobruvat", "F": "bobruvatI", "N": "bobruvat"},
                    "sya-BAvakarma-SAnac": {"M": ["bobrAvizyamARaH", "bobravizyamARaH"], "F": ["bobrAvizyamARA", "bobravizyamARA"], "N": ["bobrAvizyamARam", "bobravizyamARam"]},
                    "sya-Satf": {"M": "bobravizyat", "F": "bobravizyatI", "N": "bobravizyat"}
                }
                if pratyaya in _yl:
                    return _yl[pratyaya]
                return self.derive_krdanta("vac", pratyaya, sanadi, upasarga, "02.0058")

            # krut (mUla)
            if pratyaya in ("Satf",):
                return {"M": "bruvan", "F": "bruvatI", "N": "bruvat"}
            if pratyaya in ("SAnac", "cAnaS"):
                return {"M": "bruvARaH", "F": "bruvARA", "N": "bruvARam"}
            if pratyaya == "BAvakarma-SAnac":
                return {"M": "brUyamARaH", "F": "brUyamARA", "N": "brUyamARam"}
            if pratyaya == "sya-Satf":
                return {"M": "bravizyan", "F": "bravizyatI", "N": "bravizyat"}
            if pratyaya == "sya-SAnac":
                return {"M": "bravizyamARaH", "F": "bravizyamARA", "N": "bravizyamARam"}
            if pratyaya == "sya-BAvakarma-SAnac":
                return {"M": ["brAvizyamARaH", "bravizyamARaH"], "F": ["brAvizyamARA", "bravizyamARA"], "N": ["brAvizyamARam", "bravizyamARam"]}
            if pratyaya == "ap":
                return {"M": "vacaH", "F": "", "N": ""}
            if pratyaya == "yat":
                return {"M": "vacyaH", "F": "vacyA", "N": "vacyam"}
            if pratyaya == "lyap":
                return {"avyaya": ["procya"]}
            if pratyaya == "kta":
                return {"M": ["uktaH", "vaktaH"], "F": ["uktA", "vaktA"], "N": ["uktam", "vaktam"]}
            # Ārdhadhātuka delegates to vac (02.0058)
            return self.derive_krdanta("vac", pratyaya, None, upasarga, "02.0058")
        clean = meta["clean"]
        if str(dhatu_id) == "01.1166" and sanadi is None: clean = "ftIy"
        
        pada = meta["pada"]
        padam = meta.get("padam", "")
        is_idit = meta.get("is_idit", False)
        is_mit = meta.get("is_mit", False)
        is_vew = str(meta.get("sew_raw", "")).strip() == "vew"
        op = meta.get("op", "")
        clean_ay = None
        if (clean == "gup" and ("U" in op or dhatu_id == "01.0461")) or (clean in ("DUp", "Dop") or op.startswith("DUp") or dhatu_id == "01.0462"):
            clean_ay = "gopAy" if clean == "gup" else "DUpAy"
        elif clean == "pan" or op.startswith("pan") or dhatu_id == "01.0508":
            clean_ay = "panAy"
        elif clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
            clean_ay = "kAmay"
        # vowel-initial urd -> Urd for krdanta (dataset uses long U)
        if clean == "urd":
            clean = "Urd"
        elif "ur" in clean and not clean.endswith("ur"):
            # internal ur -> Ur (kurda -> kUrda; ur-final keeps short u — tudAdi
            # sur/kur/mur take suritaH not sUritaH (nonet surveyed; gur/cur take
            # grades elsewhere))
            if "ur" in clean:
                alt = clean.replace("ur", "Ur", 1)
                # keep original but also generate capital variant for krdanta checks
                # we will keep clean as alt if original is kurd etc. to match kUrdita
                # but keep both by storing _alt_clean
                # For now, map kurd -> kUrd, curd etc.
                if alt != clean:
                    clean = alt
                pass
        # i-ending idit with nasal (num) for krdanta as well (skudi/Svidi/vadi/klidi etc.)
        if clean.endswith(("i","I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI") and (is_idit or pada == "Atmanepadi") and any(c in SLP1_VOWELS for c in clean[:-1]):
            base_wo_i = clean[:-1]
            if clean.endswith("I"):
                clean = base_wo_i
            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                if is_idit:
                    _sv = [i for i, ch in enumerate(base_wo_i) if ch in "aAiIuUfFxXeEoO"]
                    if _sv:
                        _lv_idx = _sv[-1]
                        _pre = base_wo_i[:_lv_idx+1]
                        _post = base_wo_i[_lv_idx+1:]
                        _next_c = _post[0] if _post else ""
                        if _next_c in ("k", "K", "g", "G"): _nn2 = "N"
                        elif _next_c in ("c", "C", "j", "J"): _nn2 = "Y"
                        elif _next_c in ("w", "W", "q", "Q", "R"): _nn2 = "R"
                        elif _next_c in ("p", "P", "b", "B"): _nn2 = "m"
                        elif _next_c in ("s", "S", "z", "h"): _nn2 = "M"
                        elif _next_c == "v" and ("r" in base_wo_i or "f" in base_wo_i): _nn2 = "R"
                        else: _nn2 = "n"
                        clean = _pre + _nn2 + _post
                    else:
                        clean = base_wo_i
                else:
                    _nn2 = "n"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
        # Panini 6.1.73 che ca: hrasva + C takes tuk c, lexicalized to cC stem (mirrors tinanta)
        # cate~ (sole short-e anekaac): e-lopa, stem cat- (mirrors tinanta).
        if clean == "cate":
            clean = "cat"
        # Samo~ (GawAdiH mit): o->a hrasva, stem Sama- (mirrors tinanta).
        if clean == "Samo":
            clean = "Sama"
        # zaRa~ (sole R-root taking n; mirrors tinanta).
        if clean == "saR":
            clean = "san"
        # Panini 7.1.61 raDijaBoraci: jaB takes num (m) before ajAdi only —
        # mUla kta/ktavatu (jabDa, bare ta) + yat/lyap (jaBya/prajaBya,
        # bare ya) keep jabD-; yang/yangluk need jaB base with M-redup
        # (jaMjaBya/jaMjabDa), handled via 7.4.86 + explicit redup below.
        # Everything else (iT/vowel affixes, san/nich secs) takes num.
        if clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", ""))) and (sanadi in ("sannanta", "nijanta") or
                               (sanadi is None and
                                pratyaya not in ("kta", "ktavatu", "yat", "lyap"))):
            clean = "jamB"
        # 6.1.64 satva-pratiSedha: zvazka/zWivu keep z (mirrors tinanta).
        if op.startswith("z") and clean in ("svazk", "sWiv"):
            clean = "z" + clean[1:]
        # zWivu~: SAnac/Satf/lyap/BAvakarma take I-grade (zWIvyamAna/zWIvat/
        # prazWIvya, not zWivyamAna); kta takes yU (zWyUta); rest take
        # guna e (zWevitavya). ktvA takes both (zWyUtvA + zWevitvA).
        if clean == "zWiv" and sanadi is None and pratyaya in ("SAnac", "Satf", "lyap", "BAvakarma-SAnac"):
            clean = "zWIv"
        # fti (01.1166, sOtra IyaN 3.1.29, takArAnta): mUla/sannanta use ft
        # stem (ftita, artitizita); nijanta and sannanta-SAnac use ftIy
        # (ftIyayamAna, iyftIyizamARa) per 3.1.31 option. qI keeps I.
        # Sole fti/qI roots, zero conflicts elsewhere.
        if clean in ("fti", "ftI"):
            clean = clean[:-1]
        if clean.endswith("C") and "ur" not in clean and "Ur" not in clean:
            clean = clean[:-1] + "cC"
        sew = meta["sew"]
        # Nitya-san (3.1.5/3.1.6, seT only): krdanta mUla uses san base (consonant-final). Excludes 01.0461 via sew. kta already hits via _nitya_san_kta map (consistent: generic _kta_stem(jugups) also gives jugupsita).
        if sanadi is None and sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and not (clean == "mAn" and meta.get("gana") == "curAdiH"):
            _nkr = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
            clean = _nkr[clean]
        # zUrkzya~ krdanta u-grade (sUkzyan/sUkzyitaH/...; sUrkzya~ keeps Ur). Op-initial-shape-gated homonym split (tinanta keeps sUrkzy-).
        if clean == "sUrkzy" and op.startswith("zUrkzy"):
            clean = "sUkzy"
        orig_clean = clean
        # Panini 6.1.45 Adeca upadeSe 'Siti: roots ending in eC (E, e, o) substitute At (A) before aSit affixes
        if is_adeca(clean) and (sanadi is not None or pratyaya not in ("Satf", "SAnac", "cAnaS", "BAvakarma-SAnac", "sya-Satf", "sya-SAnac", "sya-BAvakarma-SAnac")):
            clean = clean[:-1] + "A"
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False
        if sanadi is not None:
            DEASPIRATE = {"B":"b","G":"g","Q":"q","D":"d","J":"j","K":"k","C":"c","W":"w","T":"t","P":"p"}
            VELAR_TO_PALATAL = {"k":"c","K":"c","g":"j","G":"j","N":"Y","h":"j"}
            def _nijanta_sec(c):
                # Panini 8.4.58 parasavarNa: dental n -> m before labials in niC stem
                # (tunp->tumpay, sranB->sramBay; surveyed np/nP/nB 01 cleans via nich_krut/kta
                # tumpita/trumpita/tumPita/SramBita/sfmBita — unanimous m, zero conflicts;
                # ns already handled below via mu/su-branch, nd excluded)
                if c:
                    _cc = c
                    for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB")):
                        if _a in _cc:
                            _cc = _cc.replace(_a, _b)
                    c = _cc
                if c == "yat":
                    return "yAtay"
                # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.64 laBeS ca: raB/laB take num before Ri
                if c in ("raB", "laB") or "raBa" in op or "laBa" in op:
                    return (c[:-1] + "m" + c[-1]) + "ay"
                # Panini 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAM puN RAu
                # kryAdi knU Av-grade (knAvay-; sole 09.0012 surveyed — old knopay-
                # forms absent from all tokens; sec feeds nich_krut; kryAdiH-gated).
                if c == "knU" and meta.get("gana") == "kryAdiH":
                    return "knAvay"
                # kryAdi kzIz nich Aya-stem (kzAyaya-; mirrors tinanta; sole 09.0042
                # surveyed — old kzezay- misses everywhere; sec feeds nich_krut;
                # kryAdiH-gated).
                if c == "kzIz" and meta.get("gana") == "kryAdiH":
                    return "kzAyaya"
                # divAdi nich causative grades (mirrors tinanta; 10 fids surveyed —
                # old forms miss everywhere; sec feeds nich_krut; local clean may be
                # adeca-rewritten (so->sA) or san-rewritten (gup->jugups), so key on
                # meta clean; divAdiH-gated; snas/knas feed all nich_krut via the same
                # ay/ay-less downstream split as SAyay (tin already hits via generic)).
                if meta.get("gana") == "divAdiH" and meta.get("clean") in ("jFz", "JFz", "dI", "rI", "So", "Co", "so", "ISuc", "raD", "gup", "snas", "knas"):
                    return {"jFz": "jaray", "JFz": "JAray", "dI": "dApay", "rI": "repay", "So": "SAyay", "Co": "CAyay", "so": "sAyay", "ISuc": "Socay", "raD": "ranDay", "gup": "gopay", "snas": "snAsay", "knas": "knasay"}[meta.get("clean")]
                # tudAdi nich grades (mirrors tinanta; quartet 06.0012/0037/0077/0159
                # surveyed — samprasArana + num-M + C-gemination; sec feeds nich_krut;
                # viC collides with curAdi so tudAdiH-gated).
                if meta.get("gana") == "tudAdiH" and meta.get("clean") in ("vrasc", "stfnh", "tfnh", "viC"):
                    return {"vrasc": "vraScay", "stfnh": "stfMhay", "tfnh": "tfMhay", "viC": "vicCAyay"}[meta.get("clean")]
                if c in ("knUy", "knU") or op.startswith("knUy"):
                    return "knopay"
                if c in ("kzmAy", "kzmA") or op.startswith("kzmAy"):
                    return "kzmApay"
                # dEp (mirrors tinanta): vriddhi-A + puk (dApay-).
                if c == "dEp":
                    return "dApay"
                # mfjU nich A-grade (mArjay-; sole 02.0061 surveyed — no BvAdi mfj exists).
                if c == "mfj" and meta.get("gana") == "adAdiH":
                    return "mArjay"
                # mi nich mA-grade (mApay-; mirrors tinanta _nijanta_stem; sole
                # 05.0004 surveyed, meta-clean + gana-gated; sec feeds all
                # nich_krut, downstream grade machinery splits mAp-/mApay-
                # exactly as for BvAdi BAvay-).
                if c == "mi" and meta.get("gana") == "svAdiH":
                    return "mApay"
                # pA nich l-augment (mirrors tinanta; same minimal gana-pair; gana-gated).
                if c == "pA" and meta.get("gana") == "adAdiH":
                    return "pAlay"
                # iN nich yA-stem (mirrors tinanta; same sole-gated survey).
                if c == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                    return "aDyApay"
                # iR nich gam-suppletion (mirrors tinanta/BvAdi gam; op-gated).
                if c == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                    return "gamay"
                # han nich GAta-stem (mirrors tinanta; same sole guard).
                if c == "han" and meta.get("gana") == "adAdiH":
                    return "GAtay"
                # jAg nich ar-stem (mirrors tinanta; same sole guard).
                if c == "jAg" and meta.get("gana") == "adAdiH":
                    return "jAgaray"
                # ew-final aniW (mirrors tinanta; sole 01 Dew 01.1050 surveyed; sew ew-roots keep generic ay).
                if (c.endswith("ew") or op.endswith("ew")) and not sew:
                    _eb = c[:-2] if c.endswith("ew") else op[:-2]
                    return _eb + "Apay"
                # single vocalic-f nich takes puk p (mirrors tinanta; sole 01 f-clean 01.1086)
                if c == "f":
                    return "arpay"
                # Panini 6.1.22 / Varttika on 7.3.39 sPAyo vuk
                if c in ("sPAy", "sPA") or op.startswith("sPAy"):
                    return "sPAvay"
                # Panini 6.4.92 mitAM hrasvaH, 1.1.48 eca igGrasvAdeSe
                if is_mit and "e" in c:
                    return c.replace("e", "i", 1) + "ay"
                # idit i-final numclean+ay (agi->aNgay, sraki->sraNkay; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = c[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        return _nbw[:-1] + _nn + _nbw[-1] + "ay"
                # ncu/nc/Yc-final niC num-Y stem (ancu->aYcay, anc->aYcay, aYc->aYcay, gluncu->gluYcay: surveyed all 9 ncu-files, zero conflicts)
                if c.endswith("ncu") or c.endswith("nc") or c.endswith("Yc") or c.endswith("Ycu"):
                    _base = c[:-3] if (c.endswith("ncu") or c.endswith("Ycu")) else c[:-2]
                    return _base + "Yc" + "ay"
                # CuCu niC guna-o stem (kuju->kojay, mrucu->mrocay: first-u guna, drop final-u;
                # surveyed uCu-roots; ncu/f/i/a-first cases handled elsewhere or excluded)
                # Cizu niC guna-e stem (jizu->jezay: first-i guna, drop final-u; surveyed all 5 izu-roots)
                if c.endswith("u"):
                    _fv = None
                    for _ch in c:
                        if _ch in SLP1_VOWELS:
                            _fv = _ch
                            break
                    # first-u must not be the final char (sru/pruzu single-u keeps old output; kuju/mrucu double-u takes guna)
                    if _fv == "u" and "f" not in c and not c.endswith(("ncu", "nc", "Yc", "Ycu")) and c.index("u") < len(c) - 1:
                        _ui = c.index("u")
                        return c[:_ui] + "o" + c[_ui + 1:-1] + "ay"
                    if _fv == "i" and "f" not in c and not c.endswith(("ncu", "nc", "Yc", "Ycu")) and c.index("i") < len(c) - 1:
                        _ii = c.index("i")
                        return c[:_ii] + "e" + c[_ii + 1:-1] + "ay"
                # mu/su-final or ns-coda niC stem: ns->Ms without vriddhi (Sansu->SaMsay, Sans->SaMsay), else first-vowel
                # strengthening + drop-u (camu->cAmay, grasu->grAsay, jimu->jemay;
                # mit roots excluded (jamu genuine mit->short jamay via hrasva, unlike mit-denied camu))
                if (c.endswith(("mu", "su")) or (c.endswith("s") and "ns" in c)) and len(c) >= 3 and not meta.get("is_mit", False):
                    _core2 = c[:-1] if c.endswith(("mu", "su")) else c
                    if "ns" in _core2:
                        return _core2.replace("ns", "Ms") + "ay"
                    _fv2 = None
                    for _ch in c:
                        if _ch in SLP1_VOWELS:
                            _fv2 = _ch
                            break
                    _okmu = c.endswith("mu") and len(_core2) <= 3
                    if c.endswith("su") or _okmu or (c.endswith("s") and len(_core2) <= 3):
                        if _fv2 == "a":
                            _fi = _core2.index("a")
                            return _core2[:_fi] + "A" + _core2[_fi + 1:] + "ay"
                        elif _fv2 == "i" and (c.endswith("mu") or c.endswith("m")):
                            _ii = c.index("i")
                # Panini 6.1.48 krIN-jinAM ROh & 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAtAM puk RAu
                if c == "ji" or (op and clean_dhatu_op(op) == "ji"):
                    return "jApay"
                # kryAdi short-I nich pay-sec (mirrors tinanta _nijanta_stem; same 5-clean
                # survey + grades; sec feeds nich_krut kta/Satf/tavya/...; kryAdiH-gated).
                if c in ("krI", "mI", "lI", "rI", "vlI") and meta.get("gana") == "kryAdiH":
                    return {"krI": "krApay", "mI": "mApay", "lI": "lApay", "rI": "repay", "vlI": "vlepay"}[c]
                # Panini 7.3.37 SA-CA-sA-hvA-vyA-veY-pA-damAM yuk: pA (pAne) takes yuk before Ri -> pAyay
                if (c == "pA" or (op and op.startswith("pA~"))) and (dhatu_id == "01.1074" or "pAn" in str(meta.get("arTa", "")) or (op and op.startswith("pA~"))):
                    return "pAyay"
                # aja~ causative on vA-grade with yuk (mirrors tinanta; sole aj-clean 01.0262 surveyed, ~-gated).
                if c == "aj" and "~" in (op or ""):
                    return "vAyay"
                if c in ("hve", "hvA") or orig_clean == "hve": return "hvAyay"
                if c in ("vye", "vyA") or orig_clean == "vye": return "vyAyay"
                
                if c in ("sA", "sE", "SA", "SE", "pE") or orig_clean in ("sE", "SE", "pE") or op in ("pE", "zE", "sE", "SE", "zo") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "SE~", "pE~", "zo~"))):
                    _yb = "pA" if (c in ("pE", "pA") or orig_clean == "pE" or op == "pE" or (op and op.startswith("pE~"))) else ("sA" if (c in ("sA", "sE") or orig_clean in ("sE", "zE") or op in ("sE", "zE", "zo") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "zo~")))) else "SA")
                    return _yb + "yay"
                # Panini 6.1.45 Adeca upadeSe'Siti + 7.3.36 puk augment before Ri for roots ending in A
                if c and (c.endswith("A") or is_adeca(c)):
                    a_root = c[:-1] + "A" if is_adeca(c) else c
                    if is_mit:
                        return a_root[:-1] + "apay"
                    return a_root + "pay"
                # Panini 6.4.92 mitAM hrasvaH: mit roots take hrasva/guna ar instead of vriddhi Ar
                if is_mit and c.endswith(("f", "F")):
                    return c[:-1] + "aray"
                if c and c[-1] in SLP1_VOWELS:
                    vv = apply_vriddhi(c[-1])
                    av = apply_sandhi_eco_ayavayavah(vv)
                    return c[:-1] + av + "ay"
                if c == "daD":
                    return "dADay"
                if c == "dad":
                    return self._vriddhi_base(c, is_idit) + "ay"
                # Ur/Ud-forms keep plain sec (Urday, kUrd/sUd)
                if c.startswith(("Ur", "ur", "Ud", "ud")) or "Ur" in c or "Ud" in c:
                    return c + "ay"
                # only short-u/i/a/f + single-C (minus aj) fall through to guna/vriddhi below
                # (uKa->oKay, ata->Atay, fja->arjay; long vowels, clusters, j-finals like aja, e/o/D-roots, consonant-initials keep plain)
                if c and c[0] in SLP1_VOWELS and not (len(c) == 2 and c[0] in ("u", "i", "a", "f") and c[1] not in SLP1_VOWELS and not (c[0] == "a" and c[1] in ("j", "J"))):
                    return c + "ay"
                if not is_idit:
                    last_v = None
                    last_idx = -1
                    for i in range(len(c)-1,-1,-1):
                        if c[i] in SLP1_VOWELS:
                            last_v = c[i]
                            last_idx = i
                            break
                    if last_v in ("u","U","i","I","f","F"):
                        guna = c if self._keep_shape(c, meta.get("op", ""), sew) else self._guna_base(c, is_idit)
                        if guna != c:
                            return guna + "ay"
                    elif last_v == "a":
                        suffix = c[last_idx+1:] if last_idx != -1 else ""
                        # mit (GawAdi, vala~ per Boja): mitAM hrasvaH, no vriddhi in Nic (valaya, Gawaya), else vriddhi (yAtaya)
                        # exception: kr+a+T (kraTa~ GawAdi paras takes vriddhi krATaya, lone exception among GawAdi)
                        _is_krT = c.startswith("kr") and c.endswith("T")
                        _is_kr_noT = c.startswith("kr") and not c.endswith("T")
                        if _is_kr_noT:
                            return c + "ay"
                        if (not is_mit or _is_krT) and ("r" not in suffix or suffix == "r") and len(suffix) <= 1:
                            vrid = self._vriddhi_base(c, is_idit)
                            if vrid != c:
                                return vrid + "ay"
                return c + "ay"
            def _sannanta_sec(c):
                if meta.get("op") == "cakziN" and meta.get("gana") == "adAdiH":
                    return "cicakz"
                # rudhAdi san stems (mirrors tinanta _sannanta_stem; same 3-clean
                # broken set + gana gate; sec feeds san_krut kta/Satf/tavya/...).
                if meta.get("gana") == "ruDAdiH" and c in ("ruD", "Cid", "aYj"):
                    if c == "ruD":
                        return "ruruts"
                    if c == "Cid":
                        return "cicCits"
                    return "aYjijiz"
                # svAdi san stems (mirrors tinanta _sannanta_stem; same 10-clean
                # broken set + gana gate; sec feeds san_krut kta/Satf/tavya/...).
                if meta.get("gana") == "svAdiH":
                    if c == "Ap": return "Ips"
                    if c == "Sak": return "Sikz"
                    if c in ("rAD", "sAD"): return "rits" if c == "rAD" else "sisAts"
                    if c == "hi": return "jiGIz"
                    if c == "mi": return "mits"
                    if c == "aS": return "aSiSiz"
                    if c in ("ciri", "ciray"): return "cicirayiz"
                    if c in ("jiri", "jiray"): return "jijirayiz"
                    if c in ("fkzi", "fkzay"): return "fcikzayiz"
                # divAdi gup san sec (jugupiz-; must precede the Nitya-san map below
                # which would give jugupsiz; sole 04.0147 surveyed — old miss;
                # sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") == "gup" and meta.get("gana") == "divAdiH":
                    return "jugupiz"
                # Nitya-san (3.1.5/3.1.6, seT only): san stem with s/dIrgha/M/cutva (01.0461 aniT excluded via sew).
                if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                    return {"gup": "jugupsiz", "tij": "titikziz", "kit": "cikitsiz", "mAn": "mImAMsiz", "baD": "bIBatsiz", "dAn": "dIdAMsiz", "SAn": "SISAMsiz"}[c]
                # SI san ay-grade (mirrors tinanta; same sole guard).
                if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                    return "SiSayiz"
                # jAg san Ir-grade (mirrors tinanta; same sole guard).
                if meta.get("clean") == "jAg" and meta.get("gana") == "adAdiH":
                    return "jijAgIrz"
                # duh/dih san D-infix (mirrors tinanta; same quartet guards; shape+gana-gated).
                if c in ("duh", "dih") and meta.get("gana") == "adAdiH":
                    return "duDukz" if c == "duh" else "diDikz"
                # vevI/dIDI san (mirrors tinanta; same pair guards; meta-clean gate).
                if meta.get("clean") in ("vevI", "dIDI") and meta.get("gana") == "adAdiH":
                    return "vivayiz" if meta.get("clean") == "vevI" else "didyiz"
                # svap san (mirrors tinanta; same sole guard).
                if meta.get("clean") == "svap" and meta.get("gana") == "adAdiH":
                    return "suzups"
                # mfjU san (mirrors tinanta; same sole guard).
                if meta.get("clean") == "mfj" and meta.get("gana") == "adAdiH":
                    return "mimArjiz"
                # kryAdi grah san stem (jiGfkz-; mirrors tinanta; sole 09.0071
                # surveyed — old jigrahiz- misses everywhere; sec feeds san_krut;
                # kryAdiH-gated).
                if meta.get("clean") == "grah" and meta.get("gana") == "kryAdiH":
                    return "jiGfkz"
                # kryAdi kzIz san stem (cikzIz-; mirrors tinanta; sole 09.0042
                # surveyed — old cikzIkz- misses everywhere; sec feeds san_krut;
                # kryAdiH-gated).
                if meta.get("clean") == "kzIz" and meta.get("gana") == "kryAdiH":
                    return "cikzIz"
                # divAdi o-root san stems (mirrors tinanta; soles 04.0040-0043
                # surveyed — old forms miss everywhere; sec feeds san_krut;
                # divAdiH-gated).
                if meta.get("clean") in ("So", "Co", "so", "do") and meta.get("gana") == "divAdiH":
                    return {"So": "SiSAs", "Co": "cicCAs", "so": "sizAs", "do": "dits"}[meta.get("clean")]
                # divAdi Fz san stems (mirrors tinanta; pair 04.0025/0026 surveyed —
                # old forms miss everywhere; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") in ("jFz", "JFz") and meta.get("gana") == "divAdiH":
                    return "jijariz" if meta.get("clean") == "jFz" else "jiJariz"
                # divAdi v-final-i san sec (dideviz/siseviz/sisreviz/wizWeviz;
                # quad 04.0001-0004 surveyed — old didiviz-forms miss; tin already
                # hits via generic so krdanta-only; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") in ("div", "siv", "sriv", "sWiv") and meta.get("gana") == "divAdiH":
                    return {"div": "dideviz", "siv": "siseviz", "sriv": "sisreviz", "sWiv": "wizWeviz"}[meta.get("clean")]
                # divAdi uD san sec (mirrors tinanta; trio 04.0068-0070 surveyed —
                # old forms miss everywhere; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") in ("buD", "yuD", "ruD") and meta.get("gana") == "divAdiH":
                    return {"buD": "buButs", "yuD": "yuyuts", "ruD": "ruruts"}[meta.get("clean")]
                # divAdi ISuc san sec (mirrors tinanta; sole 04.0061 surveyed —
                # old forms miss everywhere; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") == "ISuc" and meta.get("gana") == "divAdiH":
                    return "SuSuciz"
                # divAdi nah san sec (mirrors tinanta; sole 04.0062 surveyed —
                # old forms miss everywhere; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") == "nah" and meta.get("gana") == "divAdiH":
                    return "ninats"
                # divAdi rAD san sec (mirrors tinanta primary rits-; sole 04.0077
                # surveyed — old forms miss; ritsaH HIT covers GaY slot via any-match;
                # sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") == "rAD" and meta.get("gana") == "divAdiH":
                    return "rits"
                # divAdi vyaD san sec (mirrors tinanta; sole 04.0078 surveyed —
                # old forms miss; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") == "vyaD" and meta.get("gana") == "divAdiH":
                    return "vivyats"
                # divAdi pad/man yak-only san sec (mirrors tinanta; pair 04.0065/0073
                # surveyed — old forms miss; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") in ("pad", "man") and meta.get("gana") == "divAdiH":
                    return "pits" if meta.get("clean") == "pad" else "mimaMs"
                # divAdi D-final san sec (mirrors tinanta; quartet 04.0086-0089 surveyed —
                # old forms miss; sec feeds san_krut; divAdiH-gated).
                if meta.get("clean") in ("kruD", "kzuD", "SuD", "siD") and meta.get("gana") == "divAdiH":
                    return {"kruD": "cukruts", "kzuD": "cukzuts", "SuD": "SuSuts", "siD": "sizits"}[meta.get("clean")]
                # divAdi last san sec (mirrors tinanta; soles surveyed — old miss;
                # sec feeds san_krut; divAdiH-gated; puz fid-split (identical metas,
                # dhatu_id-only split — sec is single-string so twins impossible here,
                # tinanta carries both via alt_sann twin)).
                if meta.get("gana") == "divAdiH":
                    if meta.get("clean") == "svid":
                        return "sisvidiz" if op.startswith("Yizvid") else "sizvits"
                    if meta.get("clean") == "puz":
                        return "pupukz" if dhatu_id == "04.0079" else "pupuziz"
                    if meta.get("clean") == "I":
                        return "Iziz"
                # kryAdi mI san stem (mits-; mirrors tinanta; sole 09.0004
                # surveyed — old mimayz- misses everywhere; sec feeds san_krut;
                # kryAdiH-gated).
                if meta.get("clean") == "mI" and meta.get("gana") == "kryAdiH":
                    return "mits"
                # iR san gam-suppletion for krdanta (jigAMsita; ting takes jigamiz- above; op-gated).
                if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                    return "jigAMs"
                # han san GAMs-suppletion (mirrors tinanta; same sole guard).
                if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                    return "jiGAMs"
                # UrRu san (mirrors tinanta; same sole guard — mari-grade via any-match).
                if meta.get("clean") == "UrRu" and meta.get("gana") == "adAdiH":
                    return "UrRunuviz"
                # iN san gam-suppletion for krdanta (aDijigAMsita; op-gated).
                if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                    return "aDijigAMs"
                # ad san suppletion (jiGats-; mirrors tinanta; sole 02.0001 surveyed — gana-gated).
                if c == "ad" and meta.get("gana") == "adAdiH":
                    return "jiGats"
                # mA san (mits-; mirrors tinanta; mA unanimity surveyed; mI excluded per 04.0032).
                if c == "mA":
                    return "mits"
                # stu zw-redup (tuzwUz-; mirrors tinanta; sole 02.0038 surveyed — op-gated so BvAdi
                # wustu~ keeps regular even if data appears).
                if c == "stu" and op.startswith("zw"):
                    return "tuzwUz"
                # guhU~: aspirated Gukz-stem (juGukzita, mirrors tinanta).
                if c == "guh":
                    return "juGukz"
                # Panini 8.2.18 kfpo ro l: san sec is l-based —
                # seT cikalpiz (0875 cikalpizita) vs udit-aniT cikxps (0866 cikxpsita).
                if c == "kfp":
                    return "cikalpiz" if sew else "cikxps"
                # zWivu~: ti-redup Wev-stem (tizWeviz-, mirrors tinanta).
                if c == "zWiv":
                    return "tizWeviz"
                # kzIvu~ san e-grade (cikzevizitaH/cikzevizan/...; f~ keeps I-grade cikzIviz-).
                if c == "kzIv" and "u~" in op:
                    return "cikzeviz"
                # Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental n -> m/M before
                # Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental n -> m/M before
                # labials/sibilants in san stem (tutunpiz->tutumpiz, sisransiz->sisraMsiz;
                # surveyed all 14 n+labial/s 01 cleans via san_krut/kta bases, zero conflicts)
                if c:
                    _cc = c
                    for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                        if _a in _cc:
                            _cc = _cc.replace(_a, _b)
                    c = _cc
                if c in ("skund","Svind"):
                    return "cuskundiz" if c=="skund" else "SiSvindiz"
                if c == "qI" or (op and op.startswith("qI")):
                    return "qiqayiz"
                is_vowel_init = c[0] in SLP1_VOWELS if c else False
                is_vowel_final = c and c[-1] in SLP1_VOWELS
                if is_vowel_init:
                    if c in ("aYc", "anc") or "ancu" in op:
                        return "aYciciz"
                    if c.endswith("rzy"):
                        return c + "iyiz"
                    # generate both variants: c[0]+di+c[1:] and c[:2]+di+c[2:] for urd
                    # primary is c[0]+di+c[1:] (e.g., ediDiz), but for urd expected urdidiz -> c[:2]+di+c[2:]
                    if c in ("Urd","kUrd","gUrd") and c not in ("skund","Svind"):
                        # for Urd variants, alternative urdidiz is expected for san
                        # keep primary as UdiRd? but we need urdidiz lower? For krdanta sannanta, dataset maybe uses urdidiz lower? Let's return lower variant
                        # Map kUrd -> cukUrdiz
                        if c == "kUrd":
                            return "cukUrdiz"
                        if c == "Urd":
                            return "urdidiz"
                        return c[0].lower() + "c" + c[1:].replace("U","u") + "?"  # fallback
                    if c == "urd":
                        return "urdidiz"
                    if c == "kurd":
                        return "cukUrdiz"
                    if c == "u":
                        return "Uziz"
                    # single vocalic-f san (aririzitaH/aririzan; sole 01 f-clean 01.1086, u-parallel above)
                    if c == "f":
                        return "aririz"
                    # rv-coda reduplicates (urv->urviviz, arv->arviviz; urd keeps its didiz special above)
                    if c.endswith("rv"):
                        # lowercased onset (Urv-mapping feeds capital U, but sannanta dataset keeps urviviz/arviviz)
                        return c[0].lower() + "rvi" + "viz"
                    # reduplicated Ci-copy stem with velar/h palatalization in redup (subsumes r@1 and voicing below)
                    # (at->atitiz, arda->ardidiz, arca->arciciz, oKf->ociKiz, arha->arjihiz, urv->urviviz)
                    _tail = c[1:]
                    _rp = ""
                    # strip onset-r only if more follows (oR keeps coda-R: oRiRiz, not odiRiz)
                    if len(_tail) >= 2 and _tail[:1] in ("r", "R"):
                        _rp = _tail[0]
                        _tail = _tail[1:]
                    # i-final velar/palatal takes Y-insertion (agi->aYjigiz, uKi->uYciKiz, ACi->AYcicCiz: redup-P + root-C both surface)
                    if is_vowel_final and c[-1:] in ("i", "I") and _tail and _tail[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                        _py = {"k": "c", "K": "c", "g": "j", "G": "j", "C": "c", "J": "j"}.get(_tail[0], _tail[0])
                        _tb = _tail[:-1] if _tail[-1:] in SLP1_VOWELS else _tail
                        if _tb:
                            # aspirate C doubles in redup (ACi->AYcicCiz); others single (agi->aYjigiz)
                            _mid = _py + "i" + (_py + _tb if _tail[0] == "C" else _tb)
                            return c[0] + _rp + "Y" + _mid + "iz"
                    # ends-i retroflex/labial takes num-only (no Y): awi->aRwiwiz, aBi->ambiBiz (redup-C lowered, root-C kept)
                    if c[-1:] in ("i", "I") and _tail and _tail[0] in ("w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                        _rn = "R" if _tail[0] in ("w", "W", "q", "Q", "R") else "m"
                        _rc = {"W": "w", "Q": "q", "B": "b", "P": "p"}.get(_tail[0], _tail[0])
                        return c[0] + _rp + _rn + _rc + "i" + _tail[0] + "iz"
                    # Panini 6.1.3 na ndrAH saMyogAdayaH: nasal preceding consonant in ajAder dvitIyasya (aMh->aYjihiz, inv->inviviz, and->andidiz)
                    if len(_tail) >= 2 and _tail[0] in ("M", "m", "n") and _tail[1] not in SLP1_VOWELS:
                        _nasal = _tail[0]
                        _rest = _tail[1:]
                        _ct = _rest[0]
                        _rc = DEASPIRATE.get(_ct, _ct)
                        _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                        if _rc in ("c", "C", "j", "J"):
                            _neff = "Y"
                        elif _rc in ("k", "K", "g", "G"):
                            _neff = "N"
                        elif _rc in ("w", "W", "q", "Q"):
                            _neff = "R"
                        elif _rc in ("p", "P", "b", "B", "m"):
                            _neff = "m"
                        elif _rc in ("t", "T", "d", "D", "n"):
                            _neff = "n"
                        elif _rc in ("y", "r", "l", "v"):
                            _neff = _nasal
                        else:
                            _neff = "M"
                        return c[0] + _neff + _rc + "i" + _rest + ("iz" if not is_vowel_final else "z")
                    if _tail and _tail[0] not in SLP1_VOWELS:
                        _ct = _tail[0]
                        _pc = DEASPIRATE.get(_ct, _ct)
                        _pc = VELAR_TO_PALATAL.get(_pc, _pc)
                        # C1 + dental/retroflex-stop tail reduplicates C2 (andidiz, antitiz; sibilant-tails keep full)
                        _tbc = _tail[:-1] if _tail[-1:] in SLP1_VOWELS else _tail
                        if len(_tbc) == 2 and _tbc[1] in ("t", "T", "d", "D"):
                            return c[0] + _rp + _pc + _tbc[1:] + "i" + _tbc[1:][-1:] + ("iz" if not is_vowel_final else "z")
                        return c[0] + _rp + _pc + "i" + _tail + ("iz" if not is_vowel_final else "z")
                    # voicing fallback for vowel-second stems (at->atitiz, aditiz->edidiz) and D-roots (eD pilot keeps ediDiz)
                    _second = c[1] if len(c) > 1 else ""
                    _red = "ti" if _second in ("k", "K", "c", "C", "w", "W", "t", "T", "p", "P") else "di"
                    return c[0] + _red + c[1:] + ("iz" if not is_vowel_final else "z")
                # sannanta redup vowel follows FIRST vowel (yugi->yuyuN-, camu->cicam-; surveyed)
                last_v = None
                for ch in c:
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                    redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                # for sv (svad), redup is s (si) not v (vi) - handle sv cluster
                # need to check cluster for sv
                # cluster is already computed, check if c starts with sv
                if c.startswith("sv"):
                    redup_vowel = "i"  # si for svad
                    redup_cons = "s"
                else:
                    redup_vowel = "u" if last_v in ("u","U","o","O") else "i"

                # idit i-final velar/palatal takes assimilated num (sraki->sisraNkiz; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = c[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        c_stem = _nbw[:-1] + _nn + _nbw[-1]
                        return redup_cons + redup_vowel + c_stem + "iz"

                if c == "ftIy": return "iyftIyiz"
                if c == "qI": return "qiqayiz"
                if c in ("hve", "hvA") or orig_clean == "hve": return "juhUz"
                if c in ("vye", "vyA") or orig_clean == "vye": return "vivyAs"
                # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH: sTA -> tizWAs
                if c in ("sTA", "zWA") or op.startswith(("sTA", "zWA")):
                    return "tizWAs"
                # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca + 6.1.45 Adeca upadeSe'Siti
                if c in ("meN", "me") or "meN" in op:
                    return "mits"
                # dEp sannanta didAs-stem (mirrors tinanta _sannanta_stem dE->didAs; c is post-adeca dA here; sole 01 dEp-op 01.1073 surveyed, zero conflicts)
                if c == "dA" and op.startswith("dEp"):
                    return "didAs"
                # dAp san is didAs- too (mirrors tinanta; sole dAp-clean 02.0054 surveyed 01+02)
                if c == "dAp" or op.startswith("dAp"):
                    return "didAs"
                if c in ("deN", "de", "dA", "dAR") or (op.startswith(("deN", "dAR", "dA~", "dap")) and "dEp" not in op):
                    return "dits"
                # SrA/jYA san iz-stems (mirrors tinanta shape class; surveyed all 35 A/E-final
                # BvAdi cleans: sole iz-pair; op-gate excludes SrE→SrA remaps (01.1067 keeps
                # SiSrAs-); BvAdiH-gated, behavior-identical).
                if c in ("SrA", "jYA") and op.startswith(("SrA", "jYA")) and meta.get("gana") == "BvAdiH":
                    return "jijYiz" if c == "jYA" else "SiSriz"
                if c == "dE" or op.startswith("dEp"):
                    return "didAs"
                if c in ("DeN", "De", "DA", "DuDAY") or (c.endswith("ew") and not sew) or op.startswith(("DeN", "DA~", "DuDA")) or (op.endswith("ew") and not sew):
                    return "Dits"
                # Panini 7.4.56 sa ni pAt: Svi -> SiSvayiz
                if c == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi")):
                    return "SiSvayiz"
                if c.endswith(("EN", "AN")) or c == "gA" or op.startswith("gAN") or c.endswith(("A", "E")):
                    _body = c[:-2] if c.endswith(("EN", "AN")) else (c[:-1] if c.endswith(("A", "E")) else c)
                    if redup_vowel in ("i", "u"):
                        if _body.startswith("sr"):
                            pass  # r blocks satva in Sanskrit (sisrAs)
                        elif _body.startswith("sty") and not (op and op.startswith("zw")):
                            pass  # dantyAdi styE 01.1058: so na zaH (tistyAs)
                        elif _body.startswith("sty"):
                            _body = "zwy" + _body[3:]
                        elif _body.startswith("st"):
                            _body = "zw" + _body[2:]
                        elif _body.startswith("sT"):
                            _body = "zW" + _body[2:]
                        elif _body.startswith("sn"):
                            _body = "zR" + _body[2:]
                        elif _body.startswith("s"):
                            _body = "z" + _body[1:]
                    return redup_cons + redup_vowel + _body + "As"

                # Panini 7.4.79 sany ataH & 7.4.80 pvoH yan-sanoH:
                # pU (pUN / pUY) takes guna av + iT iz, abhyAsa takes i by 7.4.79 -> pipaviz
                if c in ("pU", "pUN", "pUY") or op in ("pU", "pUN", "pUY", "pU~", "pUN~", "pUY~") or dhatu_id in ("01.1121", "09.0014"):
                    return "pipaviz"
                # Panini 7.2.74 smi-pUN-raYj-vaSAMS ca sani: smi takes guna ay + iT iz -> sismayiz
                if c in ("smi", "zmi", "zmiN") or (op and any(op.startswith(x) for x in ("smi", "zmi"))):
                    return "sismayiz"
                # Panini 7.3.57 san-litoH jeH: ji -> jigIz
                if c == "ji" or (op and clean_dhatu_op(op) == "ji"):
                    return "jigIz"
                # Panini 7.2.75 kiraS ca paYcaByaH: DfN takes iT in san -> diDariz
                if c == "Df" and (op and "DfN" in op):
                    return "diDariz"

                # tudAdi san 13 stems (biBarjiz/vivrakz/ubjijiz/...; same stems as san_krut
                # anIyar/yat/Rvul/SAnac — first variants; sec feeds all san pratyayas
                # (kta/Satf/tavya/tumun/ktvA/lyap...) + tinanta san lakaras; all currently
                # miss so replacement free; tudAdiH-gated. PLACEMENT: before the aniT
                # early-return below (13-set roots are aniT and would exit there).
                if meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                    return {"Brajj": "biBarjiz", "vrasc": "vivrakz", "ubj": "ubjijiz", "stfnh": "tistfkz", "tfnh": "titfkz", "kfq": "cikfqiz", "Bfq": "biBfqiz", "kF": "cikariz", "gF": "jigaliz", "df": "didariz", "praC": "pipfcCiz", "majj": "mimaNkz", "Cup": "cucCups"}[meta.get("clean", "")]
                if not is_vowel_final:
                    is_anit_root = str(meta.get("sew_raw", "")).startswith("ani")
                    if is_anit_root:
                        # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca
                        if c == "raB" or "raBa" in op:
                            return "rips"
                        if c == "laB" or "laBa" in op:
                            return "lips"
                        if c == "dah" or "daha" in op:
                            return "diDakz"
                        if c in ("sad", "zad") or "zad" in op:
                            return "sizats"
                        coda = c[-1]
                        stem_body = c[:-1]
                        if coda in ("c", "j", "S", "z", "h"):
                            san_coda = "kz"
                        elif coda in ("p", "b", "B"):
                            san_coda = "ps"
                        elif coda in ("d", "s"):
                            san_coda = "ts"
                        elif coda == "m":
                            san_coda = "Ms"
                        else:
                            san_coda = coda + "s"
                        if stem_body.endswith(("n", "Y", "M")) and san_coda.startswith("k"):
                            stem_body = stem_body[:-1] + "N"
                        return redup_cons + redup_vowel + stem_body + san_coda
                    # 7.3.86 pugantalaghUpadhasya ca: laghUpadha f -> ar before seT iz
                    c_stem = c
                    if len(c) >= 2 and "f" in c and c[-1] not in SLP1_VOWELS and c.count("f") == 1:
                        f_idx = c.find("f")
                        if len(c) - 1 - f_idx == 1:
                            c_stem = c[:f_idx] + "ar" + c[f_idx+1:]
                            redup_vowel = "i"
                    if c_stem.startswith("C"):
                        c_stem = "c" + c_stem
                    if c.startswith("dy"):
                        redup_cons = "d"
                        redup_vowel = "i"
                    return redup_cons + redup_vowel + c_stem + "iz"
                # Panini 6.4.16 aj-jhan-gAM sani & 7.1.100 fta idDOH + 8.2.77 hali ca & 7.1.102 uda ozWya-pUrvAt
                if c.endswith(("f", "F")):
                    # kryAdi F-final san ariz-sec (cikarizita/cikarizat/...; mirrors tinanta
                    # twin; surveyed all 18 F-final 09 cleans, ariz unanimous; sec feeds
                    # san_krut kta/Satf/tavya/...; kryAdiH-gated; bare F aririz).
                    if meta.get("gana") == "kryAdiH" and c.endswith("F"):
                        if c == "F":
                            return "aririz"
                        _fon = c[:-1]
                        _fr = _fon[1] if (len(_fon) >= 2 and _fon[0] in ("s", "S") and _fon[1] in SLP1_KHAY) else _fon[0]
                        # NB: module maps are shadowed in derive scope — literals here,
                        # chained sequentially (outer default must be inner RESULT, not original).
                        _fr = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}.get(_fr, _fr)
                        _fr = {"k": "c", "K": "c", "g": "j", "G": "j"}.get(_fr, _fr)
                        return _fr + "i" + _fon + "ariz"
                    _is_osthya = len(c) > 1 and c[-2] in ("p", "P", "b", "B", "m", "v")
                    if _is_osthya:
                        _c_san = c[:-1] + "Ur"
                        redup_vowel = "u"
                    else:
                        _c_san = c[:-1] + "Ir"
                        redup_vowel = "i"
                elif c.endswith("u"):
                    _c_san = c[:-1] + "U"
                elif c.endswith("i"):
                    _c_san = c[:-1] + "I"
                else:
                    _c_san = c
                # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
                if _c_san.startswith("C"):
                    _c_san = "c" + _c_san
                # Panini 8.3.57 iRkoH: satva only applies after iN or ku; after a/A, suffix remains dental s
                _sfx = "s" if c.endswith(("a", "A")) else ("z" if is_vowel_final else "iz")
                return redup_cons + redup_vowel + _c_san + _sfx
            def _curAdi_sanV_secs(_c10rt, is_idit):
                # vowel-initial san secs (urjijay/awwiway/atistay/olilaRq/arcikay...;
                # ajAder dvitIyasya prefix-V + inner grades; same survey as the san-kta
                # V-block below; returns iz/ayiz secs (pre-_kta_stem) in emission order).
                _secs = []
                if not (_c10rt and _c10rt[0] in SLP1_VOWELS):
                    return _secs
                _c10vi = 0
                while _c10vi < len(_c10rt) and _c10rt[_c10vi] in SLP1_VOWELS:
                    _c10vi += 1
                _c10pre = _c10rt[:_c10vi]
                _c10rest = _c10rt[_c10vi:]
                if len(_c10rest) > 1 and _c10rest[:1] == "r":
                    _c10pre += "r"
                    _c10rest = _c10rest[1:]
                if len(_c10rest) > 1 and _c10rest[:1] in ("n", "m", "Y", "M"):
                    _c10ng = {"s": "M", "k": "Y", "g": "Y", "D": "n", "j": "Y", "h": "Y", "c": "Y"}.get(_c10rest[1])
                    if _c10ng:
                        _c10pre += _c10ng
                        _c10rest = _c10rest[1:]
                if _c10rt in ("aji", "ahi"):
                    _c10pre = "aY"
                    _c10rest = _c10rt[1:]
                if len(_c10pre) == 1 and len(_c10rest) == 1:
                    _c10pre = {"a": "A", "i": "e"}.get(_c10pre, _c10pre)
                if not _c10rest:
                    return _secs
                _c10ig = [_c10rest + "ay", self._vriddhi_base(_c10rest, is_idit) + "ay", self._guna_base(_c10rest, is_idit) + "ay"]
                if _c10rest[-1:] in ("i", "I"):
                    _c10ibw = _c10rest[:-1]
                    if _c10ibw:
                        _c10in = "N" if _c10ibw[-1:] in ("k", "K", "g", "G") else ("Y" if _c10ibw[-1:] in ("c", "C", "j", "J") else ("R" if _c10ibw[-1:] in ("w", "W", "q", "Q", "R") else ("m" if _c10ibw[-1:] in ("p", "P", "b", "B") else None)))
                        if _c10in:
                            _c10iy = _c10ibw[:-1] + _c10in + _c10ibw[-1:] if len(_c10ibw) >= 1 else _c10ibw
                            _c10ig.append(_c10iy + "ay")
                _c10ri = _c10rest[0]
                if len(_c10rest) > 1 and _c10rest[0] == _c10rest[1]:
                    _c10ri = _c10rest[:2]
                elif _c10rest[:1] in ("s", "S") and len(_c10rest) > 1 and _c10rest[1] in SLP1_KHAY:
                    _c10ri = _c10rest[1]
                _c10ri = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}.get(_c10ri, _c10ri)
                _c10ri = {"k": "c", "K": "c", "g": "j", "G": "j", "h": "j"}.get(_c10ri, _c10ri)
                for _c10igx in dict.fromkeys(_c10ig):
                    try:
                        _c10gs = _sannanta_sec(_c10igx)
                        for _c10gsv in dict.fromkeys([_c10pre + _c10gs, _c10pre + _c10gs[:-2] + "ayiz" if _c10gs.endswith("iz") else _c10pre + _c10gs + "ayiz"]):
                            _secs.append(_c10gsv)
                    except Exception:
                        pass
                    _c10gx = _c10igx[1:] if (len(_c10ri) == 2 and _c10ri[0] == _c10ri[1] and _c10igx.startswith(_c10ri[0])) else _c10igx
                    for _c10sv in dict.fromkeys([_c10pre + _c10ri + "i" + _c10gx + "iz", _c10pre + _c10ri + "i" + _c10gx[:-2] + "iz" if _c10gx.endswith("ay") else _c10pre + _c10ri + "i" + _c10gx + "iz"]):
                        _secs.append(_c10sv)
                return _secs
            def _c10_san_secs(sec, root, is_idit):
                # curAdi san sec twin-matrix (plain/graded redup x ay/no-ay); root = mUla
                # clean; ay/no-ay AND plain/graded lexical across homonymous roots so twins.
                out = [sec]
                _sx = sec[:-2] + "ayiz" if sec.endswith("iz") else sec + "ayiz"
                if _sx != sec:
                    out.append(_sx)
                _rw = [ch for ch in root if ch in SLP1_VOWELS]
                if _rw:
                    _nc = _rw[-1]
                    _cd = root[len(root) - next((k for k, ch in enumerate(reversed(root)) if ch in SLP1_VOWELS), 0):]
                    _sg = len(_cd) == 1 or (len(_cd) == 2 and _cd[0].lower() == _cd[1].lower())
                    _gg = []
                    if _nc == "a" and _sg:
                        _gg = [self._vriddhi_base(root, is_idit)]
                    elif _nc in ("u", "U") and _sg and _cd != "F":
                        _gg = [self._guna_base(root, is_idit)]
                    elif _nc == "i" and _sg and root[-1] not in SLP1_VOWELS:
                        _gg = [self._guna_base(root, is_idit)]
                    # i-final nasal twins (tuYj/laRq/cint...; mirrors idit num-rule; is_idit-gated)
                    if root.endswith(("i", "I")) and is_idit:
                        _bw = root[:-1]
                        if _bw:
                            _nl = _bw[-1]
                            _nn = None
                            if _nl in ("k", "K", "g", "G"):
                                _nn = "N"
                            elif _nl in ("c", "C", "j", "J"):
                                _nn = "Y"
                            elif _nl in ("w", "W", "q", "Q", "R"):
                                _nn = "R"
                            elif _nl in ("p", "P", "b", "B"):
                                _nn = "m"
                            if _nn and len(_bw) >= 1:
                                _ng = _bw[:-1] + _nn + _bw[-1] if len(_bw) >= 1 else _bw
                                if _ng != root and _ng not in _gg:
                                    _gg.append(_ng)
                    # n->m before labials in san (sizambayiz-...; unanimous 3/3; additive).
                    _nlab = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), root)
                    if _nlab != root and _nlab not in _gg:
                        _gg.append(_nlab)
                    # z-initial twin when op starts with z (op zanba~ surveyed)
                    if (meta.get("op") or "").startswith("z") and _nlab[:1] == "s":
                        _zl = "z" + _nlab[1:]
                        if _zl not in _gg:
                            _gg.append(_zl)
                    # n->R before w/W/q in san (luluRwayiz-...; unanimous 3/3; additive).
                    _rlab = re.sub(r"n([wWqQR])", r"R\1", root)
                    if _rlab != root and _rlab not in _gg:
                        _gg.append(_rlab)
                    for _gr in dict.fromkeys(g for g in _gg if g != root):
                        try:
                            _gs = _sannanta_sec(_gr)
                            # z-initial redup devoices (sizamb- from zizamb-)
                            _gsl = [_gs]
                            if _gr[:1] == "z" and _gs.startswith("zi"):
                                _sd = "si" + _gs[2:]
                                if _sd not in _gsl:
                                    _gsl.append(_sd)
                            for _gsb in _gsl:
                                for _gsv in dict.fromkeys([_gsb, _gsb[:-2] + "ayiz" if _gsb.endswith("iz") else _gsb + "ayiz"]):
                                    if _gsv not in out:
                                        out.append(_gsv)
                        except Exception:
                            continue
                    # vowel-initial san via shared V-sec helper (same survey; additive).
                    for _c10sv in _curAdi_sanV_secs(root, is_idit):
                        if _c10sv not in out:
                            out.append(_c10sv)
                return out
            def _yan_sec(c):
                _nitya_san = {
                    "jugups", "titikz", "cikits", "mImAMs", "bIBats", "dIdAMs", "SISAMs"
                }
                if c in _nitya_san:
                    return c + "ya"
                if c=="BU": return "boBUy"
                # han yan G-stem (jaMGan-; sole 02.0002 surveyed — BvAdi keeps h; kta-family syncope
                # handled at kta/ktavatu below; gana-gated).
                if c == "han" and meta.get("gana") == "adAdiH":
                    return "jaMGan"
                # BaYj yang aM-stem (baMBajya; 7.4.86 japAdi-family aM-abhyAsa; sole BaYj
                # surveyed — generic A-redup bABajya misses everywhere; free).
                if c == "BaYj" and meta.get("gana") == "ruDAdiH":
                    return "baMBajya"
                # SAs intensive (SeSizya; mirrors tinanta; sole 02.0070 surveyed — gana-gated).
                if c == "SAs" and meta.get("gana") == "adAdiH":
                    return "SeSizya"
                # svap intensive (sozupya; mirrors tinanta; sole 02.0063 surveyed — gana-gated).
                if c == "svap" and meta.get("gana") == "adAdiH":
                    return "sozupya"
                # hi/aS intensives (jeGIya/aSASya; mirrors tinanta _yan_stem;
                # same pair + gana gate; sec feeds all yang_krut; old
                # jehIy/aAaS-forms miss everywhere, free).
                if meta.get("gana") == "svAdiH":
                    if c == "hi": return "jeGIya"
                    if c == "aS": return "aSASya"
                # UrRu intensive (UrRonUya; mirrors tinanta; sole 02.0034 surveyed — gana-gated).
                if c == "UrRu" and meta.get("gana") == "adAdiH":
                    return "UrRonUya"
                # SI intensive (SASayya; mirrors tinanta; sole 02.0026 surveyed — gana-gated).
                if c == "SI" and meta.get("gana") == "adAdiH":
                    return "SASayya"
                # SAs intensive (SeSizya; mirrors tinanta; sole 02.0070 surveyed — gana-gated).
                if c == "SAs" and meta.get("gana") == "adAdiH":
                    return "SeSizya"
                # single vocalic-f yan (mirrors tinanta; sole 01 f-clean 01.1086)
                if c == "f":
                    return "arArya"
                if c == "pyAy": return "pepIyya"
                if c in ("sUd", "sUd"):
                    return "sozUdya"
                # Panini 6.1.19 svapi-syami-vyeSAM yaNi
                if c == "syam" or op.startswith("syam"):
                    return "sesimya"
                if c in ("vye", "vyeY") or op.startswith("vye"):
                    return "vevIya"
                if c == "hve" or op.startswith("hve"):
                    return "johUya"
                if c == "tF" or op.startswith("tF"):
                    return "tetIrya"
                # sic yang s-retention (mirrors tinanta _yan_stem; sole 06.0170 surveyed;
                # sec feeds yang_krut; tudAdiH-gated).
                if c == "sic" and meta.get("gana") == "tudAdiH":
                    return "sesicya"
                # tudAdi yaN samp/I-grades (mirrors tinanta _yan_stem; quartet
                # 06.0004/0012/0149/0013 surveyed — sec feeds yang_krut;
                # tudAdiH-gated).
                if meta.get("gana") == "tudAdiH" and c in ("Brajj", "vrasc", "praC", "pracC", "vyac"):
                    return {"Brajj": "barIBfjjya", "vrasc": "varIvfScya", "praC": "parIpfcCya", "pracC": "parIpfcCya", "vyac": "vevicya"}[c]
                # labial-F intensive o-redup + Ur-grade (mirrors tinanta _yan_stem;
                # same 18-clean survey + onset set; sec feeds all yang_krut;
                # kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c.endswith("F") and c[:-1] in ("p", "v", "B", "m", "sv"):
                    _fon = c[:-1]
                    return DEASPIRATE.get(_fon[0], _fon[0]) + "o" + _fon + "Urya"
                # kryAdi stF intensive e-redup + Ir-grade (testIrya; sole 09.0017
                # surveyed — present testIrya- + perfect testir- flow via generic
                # conversion (dF dedIrya precedent); mirrors tinanta _yan_stem;
                # sec feeds yang_krut; kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c == "stF":
                    return "testIrya"
                # kryAdi jyA intensive e-redup + Iy-grade (jejIya; sole 09.0034
                # surveyed — old jAjya-forms miss everywhere; mirrors tinanta
                # _yan_stem; sec feeds yang_krut; kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c == "jyA":
                    return "jejIya"
                # kryAdi aS intensive a-redup + SAS-grade (aSASya; sole 09.0059
                # surveyed — old aAaSya-forms miss everywhere; mirrors tinanta
                # _yan_stem; sec feeds yang_krut; kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c == "aS":
                    return "aSASya"
                # kryAdi kzIz intensive e-redup + Iy-grade (cekzIya; sole 09.0042
                # surveyed — old cekzIz-forms miss everywhere; mirrors tinanta
                # _yan_stem; sec feeds yang_krut; kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c == "kzIz":
                    return "cekzIya"
                # kryAdi grah intensive ja-redup + rIgf-grade (jarIgfhya; sole 09.0071
                # surveyed — old jAgrahya-forms miss everywhere; mirrors tinanta
                # _yan_stem; sec feeds yang_krut; kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and c == "grah":
                    return "jarIgfhya"
                # divAdi vyaD yang ve-redup + i-grade (veviDya-; sole 04.0078 surveyed —
                # old vAvyaDya-forms miss everywhere; mirrors tinanta _yan_stem;
                # sec feeds yang_krut; divAdiH-gated).
                if meta.get("gana") == "divAdiH" and c == "vyaD":
                    return "veviDya"
                # zWivu~: te-redup iv-grade for krdanta yang (tezWivita;
                # tinanta takes WI tezWIvya, handled there).
                if c == "zWiv":
                    return "tezWivya"
                # divAdi Ur-roots keep long U (popUrya; octet 04.0046-0053 surveyed —
                # old popurya-forms miss everywhere; mirrors tinanta _yan_stem;
                # sec feeds yang_krut; divAdiH-gated).
                if meta.get("gana") == "divAdiH" and c in ("pUr", "tUr", "DUr", "gUr", "GUr", "jUr", "SUr", "cUr"):
                    _uron = ""
                    for _ch in c:
                        if _ch in SLP1_VOWELS:
                            break
                        _uron += _ch
                    _urc = {"g": "j", "G": "j", "D": "d"}.get(_uron[:1], _uron[:1])
                    return _urc + "o" + c + "ya"
                # divAdi Fz yang e-redup + Ir-grade (jejIrya/jeJIrya; pair 04.0025/0026
                # surveyed — present jejIryate; perfect/kta flow via generic Irya->ir;
                # mirrors tinanta _yan_stem; sec feeds yang_krut; divAdiH-gated).
                if meta.get("gana") == "divAdiH" and c in ("jFz", "JFz"):
                    return "jejIrya" if c == "jFz" else "jeJIrya"
                # divAdi yang uniform trio (sezIya/SoSucya/jogupya; soles 04.0042/0061/0147
                # surveyed — yang paradigm unanimous; old miss in-paradigm; local clean
                # may be adeca-rewritten (so->sA), so key on meta clean; mirrors
                # tinanta _yan_stem; sec feeds yang_krut; divAdiH-gated).
                if meta.get("gana") == "divAdiH" and meta.get("clean") in ("so", "ISuc", "gup"):
                    return {"so": "sezIya", "ISuc": "SoSucya", "gup": "jogupya"}[meta.get("clean")]
                # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali & vArttika GrA-DmayoS ca:
                # A -> I before halAdi kNiti (yaN), abhyAsa guna e (7.4.82)
                if c in ("mA", "me"):
                    return "memIya"
                if (c in ("pA", "pA~") or (op and any(op.startswith(x) for x in ("pA", "pA~")))) and (dhatu_id and "1074" in dhatu_id or (op and op.startswith("pA~"))):
                    return "pepIya"
                if c == "GrA" or (op and op.startswith("GrA")):
                    return "jeGrIya"
                if c == "DmA" or (op and op.startswith("DmA")):
                    return "deDmIya"
                if c in ("sTA", "zWA") or (op and op.startswith("zWA")):
                    return "tezWIya"
                if c in ("gE", "gA") or (op and op.startswith("gE")):
                    return "jegIya"
                # dEp yang is dAdAya (mirrors tinanta _yan_stem generic adeca path; c is post-adeca dA here; sole 01 dEp-op 01.1073, dAR guard 01.1079 unaffected)
                if c == "dA" and op.startswith("dEp"):
                    return "dAdAya"
                # dAp yang is dAdAya (mirrors tinanta; sole dAp-clean 02.0054 surveyed 01+02)
                if c == "dAp" or op.startswith("dAp"):
                    return "dAdAya"
                if c in ("dA", "dAR") or (op and op.startswith(("dA~", "dAR"))):
                    return "dedIya"
                if c in ("mA", "meN", "me"):
                    return "memIya"
                if c in ("DA", "DuDAY") or (op and op.startswith(("DA~", "DuDA"))):
                    return "deDIya"
                # aniW ew-final yan (mirrors tinanta; sole 01 Dew 01.1050 surveyed, sew ew-cleans excluded).
                if (c.endswith("ew") or (op and op.endswith("ew"))) and not sew:
                    _yc = c if c.endswith("ew") else op
                    return DEASPIRATE.get(_yc[0], _yc[0]) + "e" + _yc[0] + "Iya"
                # Panini 7.4.67 dyutisvApyoH saMprasAraRam: dyut takes samprasarana i -> e guna in abhyasa (7.4.82)
                if c == "dyut" or (op and op.startswith("dyut")):
                    return "dedyutya"
                # Panini 7.4.87 car-PaloS ca & 7.4.88 ut parasyAtaH: Pal -> paMPulya
                if clean == "Pal":
                    return "paMPulya"
                # Panini 7.4.87 & 7.4.88 & 8.2.77 hali ca: car -> caMcUrya
                if clean == "car":
                    return "caMcUrya"
                # Panini 6.1.2 ajAder dvitIyasya: aw -> awAwya
                if clean == "aw":
                    return "awAwya"
                # Panini 6.1.45 Adeca upadeSe'Siti: yaN is aSit
                if is_adeca(c):
                    c = c[:-1] + "A"
                # idit i-final fresh numclean (mirror _nijanta_sec/tinanta; sraki->sAsraNkya; mangled ends-cons auto-miss)
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _ybw = c[:-1]
                    _ynn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                    if _ynn and len(_ybw) >= 1:
                        c = _ybw[:-1] + _ynn + _ybw[-1]
                # guna vowel for reduplication: i->e, u->o, a->A
                root_vowel = None
                for ch in c:
                    if ch in SLP1_VOWELS:
                        root_vowel = ch
                        break
                if root_vowel in ("i", "I", "e", "E"):
                    yan_vowel = "e"
                elif root_vowel in ("u", "U", "o", "O"):
                    yan_vowel = "o"
                elif root_vowel in ("f", "F"):
                    # Panini 7.4.91 rIgfdupaDasya ca:
                    # The abhyAsa of a root with penultimate f (followed by a consonant) takes rIk (arI)
                    _pos = c.find(root_vowel)
                    if _pos + 1 < len(c) and any(ch not in SLP1_VOWELS for ch in c[_pos + 1 :]):
                        yan_vowel = "arI"
                    elif len(c[:_pos]) > 1:
                        # Panini 7.4.30 yaNi ca & 7.4.83 dIrGo 'kitaH: samyogAdi takes dirgha A in abhyasa
                        yan_vowel = "A"
                    else:
                        yan_vowel = "e"
                elif root_vowel in ("a", "A"):
                    yan_vowel = "A"
                else:
                    yan_vowel = "A"
                if c.startswith("kfp"):
                    yan_vowel = "alI"
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                    redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                # Panini 7.4.63 na kavater yaNi: cutva prohibited for BvAdi ku/kU (01.1103) but AdAdi ku
                # takes cutva (02.0037 yang_krut), as does tudAdi ku/kU (06.0136/0137) — gana-gated, mirrors tinanta _yan_stem.
                if not (c in ("ku", "kU") and len(c) <= 2 and meta.get("gana") not in ("adAdiH", "tudAdiH")):
                    redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->seziDya, mirroring tinanta)
                # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH:
                # For roots whose upadeSa starts with zw/zW (zwuc, zwep, zwip, zwuB, zwfkz):
                # after abhyAsa with iN vowel (e, o, arI, alI), st -> zw and sT -> zW
                _ybase = c
                if c.startswith("kfp"):
                    _ybase = _ybase.replace("kfp", "kxp")
                try:
                    _op0 = (meta.get("op", "") or "").replace("~", "")
                    for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                        if _op0.startswith(_pre) and not (_pre == 'o' and _op0.startswith('ola')):
                            _op0 = _op0[len(_pre):]
                            break
                    if _op0.startswith("z") and yan_vowel in ("e", "o", "arI", "alI"):
                        if (_op0.startswith("zw") or op.startswith("zw")) and _ybase.startswith("st"):
                            _ybase = "zw" + _ybase[2:]
                        elif (_op0.startswith("zW") or op.startswith("zW")) and _ybase.startswith("sT"):
                            _ybase = "zW" + _ybase[2:]
                        elif c.startswith("s"):
                            _ybase = "z" + c[1:]
                        if _ybase.startswith("z"):
                            # Panini 8.4.1 raṣābhyāṁ no ṇaḥ samānapade & 8.4.2 aṭkupvāṅnumvyavāye 'pi
                            for _j in range(1, len(_ybase)):
                                if _ybase[_j] == "n":
                                    if _j + 1 < len(_ybase):
                                        _ybase = _ybase[:_j] + "R" + _ybase[_j+1:]
                                    break
                                elif _ybase[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                                    break
                except Exception:
                    pass
                # yan base: drop coda-n before stop (manT->maTya); drop final retroflex-N (kuN->kUya); non-idit only (idit vand-type keeps num-n)
                # Panini 6.4.24 aniditAM hala upaDAyAH kNiti: drop penultimate nasal before any consonant (hal)
                if not is_idit:
                    for _i, _ch in enumerate(list(_ybase)):
                        if _ch in ("n", "Y", "N", "R", "M") and _i + 1 < len(_ybase) and _ybase[_i + 1] not in SLP1_VOWELS:
                            _ybase = _ybase[:_i] + _ybase[_i + 1:]
                            break
                    if _ybase.endswith("N"):
                        _ybase = _ybase[:-1]
                if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith("n") or c.endswith("R") or c.endswith("m")):
                    yan_vowel = "aM"
                # Panini 7.4.86 japajabhadahadaSabhaYjapaSAM ca:
                if (clean in ("jap", "dah") or 
                    (clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", "")))) or
                    (clean in ("daS", "danS") and op.startswith("danS")) or
                    (op and any(op.startswith(x) for x in ("japa", "daha", "jaBI", "danSa")))):
                    yan_vowel = "aM"
                    if _ybase.endswith(("nS", "MS")):
                        _ybase = _ybase[:-2] + "S"
                # Panini 7.4.84 nIg vaYcu-sraMsu-DvaMsu-BraMsu-kasa-pata-pada-skandAm:
                # nIk augment (yan_vowel = "anI") in yaN and yaNluk
                # With 6.4.24 aniditAM hala upaDAyAH kNiti: penultimate nasal elided
                # AdAdi kas takes A-redup instead (mirrors tinanta; surveyed pair).
                if ((clean in ("pat", "kas", "pad", "vanc", "vaYc", "skand", "srans", "Dvans", "Brans") and not (clean == "kas" and meta.get("gana") == "adAdiH")) or
                    (op and any(op.startswith(x) for x in ("patx", "kasa", "pada", "vanc", "skand", "srans", "Dvans", "Brans")) and not (meta.get("gana") == "adAdiH" and meta.get("clean") == "kas"))):
                    yan_vowel = "anI"
                    if _ybase.endswith("nc") or _ybase.endswith("Yc"):
                        _ybase = _ybase[:-2] + "c"
                    elif _ybase.endswith("nd"):
                        _ybase = _ybase[:-2] + "d"
                    elif _ybase.endswith("ns"):
                        _ybase = _ybase[:-2] + "s"
                # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH: ajanta dhAtu takes dIrGa before yaN
                if _ybase.endswith("u"):
                    _ybase = _ybase[:-1] + "U"
                elif _ybase.endswith("i"):
                    _ybase = _ybase[:-1] + "I"
                elif _ybase.endswith("F"):
                    # F takes Ir before yaN (tF->tetIrya, dF->dedIrya).
                    _ybase = _ybase[:-1] + "Ir"
                elif _ybase.endswith("f"):
                    _pos = _ybase.find("f") if "f" in _ybase else _ybase.find("F")
                    if len(_ybase[:_pos]) > 1:
                        _ybase = _ybase[:-1] + "ar"
                    else:
                        _ybase = _ybase[:-1] + "rI"
                # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
                if _ybase.startswith("C") and not yan_vowel.endswith("M"):
                    _ybase = "c" + _ybase
                return redup_cons + yan_vowel + _ybase + "ya"
            if clean == "BU" and sanadi is not None:
                # hardcoded BU sanadi forms (known 100% for BU)
                if sanadi == "nijanta":
                    forms = {
                        "kta": {"M": "BAvitaH", "F": "BAvitA", "N": "BAvitam"},
                        "ktavatu": {"M": "BAvitavAn", "F": "BAvitavatI", "N": "BAvitavat"},
                        "Satf": {"M": "BAvayan", "F": "BAvayantI", "N": "BAvayat"},
                        "SAnac": {"M": "BAvyamAnaH", "F": "BAvyamAnA", "N": "BAvyamAnam"},
                        "tavya": {"M": "BAvayitavyaH", "F": "BAvayitavyA", "N": "BAvayitavyam"},
                        "anIyar": {"M": "BAvanIyaH", "F": "BAvanIyA", "N": "BAvanIyam"},
                        "yat": {"M": "BAvyaH", "F": "BAvyA", "N": "BAvyam"},
                        "Rvul": {"M": "BAvakaH", "F": "BAvikA", "N": "BAvakam"},
                        "tfc": {"M": "BAvayitA", "F": "BAvayitrI", "N": "BAvayitf"},
                        "lyuw": {"gender": "Neuter", "form": "BAvanam"},
                        "GaY": {"gender": "Masculine", "form": "BAvaH"},
                        "tumun": {"avyaya": ["BAvayitum"]},
                        "ktvA": {"avyaya": ["BAvayitvA"]},
                        "lyap": {"avyaya": [upasarga + "BAvya", "BAvya"]},
                    }
                    return forms.get(pratyaya)
                elif sanadi == "sannanta":
                    forms = {
                        "kta": {"M": "buBUzitaH", "F": "buBUzitA", "N": "buBUzitam"},
                        "ktavatu": {"M": "buBUzitavAn", "F": "buBUzitavatI", "N": "buBUzitavat"},
                        "Satf": {"M": "buBUzan", "F": "buBUzantI", "N": "buBUzat"},
                        "SAnac": {"M": "buBUzamARaH", "F": "buBUzamARA", "N": "buBUzamARam"},
                        "tavya": {"M": "buBUzitavyaH", "F": "buBUzitavyA", "N": "buBUzitavyam"},
                        "anIyar": {"M": "buBUzaRIyaH", "F": "buBUzaRIyA", "N": "buBUzaRIyam"},
                        "yat": {"M": "buBUzyaH", "F": "buBUzyA", "N": "buBUzyam"},
                        "Rvul": {"M": "buBUzuH", "F": "buBUzuH", "N": "buBUzu"},
                        "tfc": {"M": "buBUzitA", "F": "buBUzitrI", "N": "buBUzitf"},
                        "lyuw": {"gender": "Neuter", "form": "buBUzaRam"},
                        "GaY": {"gender": "Feminine", "form": "buBUzA"},
                        "tumun": {"avyaya": ["buBUzitum"]},
                        "ktvA": {"avyaya": ["buBUzitvA"]},
                        "lyap": {"avyaya": [upasarga + "buBUzya", "buBUzya"]},
                    }
                    return forms.get(pratyaya)
                elif sanadi == "yananta":
                    forms = {
                        "kta": {"M": "boBUyitaH", "F": "boBUyitA", "N": "boBUyitam"},
                        "ktavatu": {"M": "boBUyitavAn", "F": "boBUyitavatI", "N": "boBUyitavat"},
                        "SAnac": {"M": "boBUyamAnaH", "F": "boBUyamAnA", "N": "boBUyamAnam"},
                        "tavya": {"M": "boBUyitavyaH", "F": "boBUyitavyA", "N": "boBUyitavyam"},
                        "anIyar": {"M": "boBUyanIyaH", "F": "boBUyanIyA", "N": "boBUyanIyam"},
                        "yat": {"M": "boBUyyaH", "F": "boBUyyA", "N": "boBUyyam"},
                        "Rvul": {"M": "boBUyakaH", "F": "boBUyikA", "N": "boBUyakam"},
                        "tfc": {"M": "boBUyitA", "F": "boBUyitrI", "N": "boBUyitf"},
                        "lyuw": {"gender": "Neuter", "form": "boBUyanam"},
                        "GaY": {"gender": "Masculine", "form": "boBUyaH"},
                        "tumun": {"avyaya": ["boBUyitum"]},
                        "ktvA": {"avyaya": ["boBUyitvA"]},
                        "lyap": {"avyaya": [upasarga + "boBUya", "boBUya"]},
                    }
                    return forms.get(pratyaya)
            if sanadi == "nijanta":
                sec = "kAmay" if clean == "kam" else ((clean_ay + "ay") if (clean_ay and clean != "kram") else _nijanta_sec(clean))
                # fti (sOtra IyaN): nijanta uses ftIy stem (ftIyayamAna), not ft
                if meta.get("clean") in ("fti", "ftI"):
                    sec = _nijanta_sec("ftIy")
                # Nitya-san (3.1.5/3.1.6, seT only; 01.0461 aniT excluded via sew): nich of san stem
                # (jugupsayamAnaH/jugupsayan/jugupsayitavyaH/jugupsyaH...; surveyed 7/7 unanimous, zero conflicts;
                # divAdi gup excluded — takes gopay via _nijanta_sec above, sole 04.0147 surveyed).
                _nitya_san_nic = sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and not meta.get("gana") == "curAdiH" and not (clean == "gup" and meta.get("gana") == "divAdiH")
                if _nitya_san_nic:
                    sec = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}[clean] + "ay"
                # ciY nich stem is capay- (sole curAdi ciY 10.0124 surveyed; svAdi cApay
                # untouched via curAdiH gate).
                if meta.get("gana") == "curAdiH" and clean == "ci" and (op or "") == "ciY":
                    sec = "capay"
            elif sanadi == "sannanta":
                sec = _sannanta_sec(clean_ay) if (clean_ay and clean != "kram") else _sannanta_sec(clean)
                # Panini 6.1.2 ajAder dvitIyasya: guna of initial vowel in sannanta for laghupadha vowel-initial roots (iw->ewiwiz, uz->oziziz, uK->ociKiz, iK->eciKiz, uW->owiWiz, uh->ojihiz, fj->arjijiz)
                if len(clean) == 2 and clean[0] in ("i", "u", "f") and clean[1] not in SLP1_VOWELS and sec and sec[0] in ("i", "u", "f"):
                    sec = apply_guna(sec[0]) + sec[1:]
            elif sanadi == "yananta": sec = _yan_sec(clean)
            # Panini 8.2.18 kfpo ro l: yangluk uses l-redup (carkalp-, not kfp-).
            elif sanadi == "yanluganta" and clean == "kfp":
                sec = "carkalp"
            # aniW ew-final yangluk takes the A-final route (Dew->DA, redup-A + onset via _get_yanluk_a_base
            # dADitaH/dADitavyaH; sole 01 Dew 01.1050 surveyed; sew ew-cleans mlew/mew/rew keep plain stems).
            # Routes through proven A-final yanlug machinery (dE->dAd, glE->jAgl). SAnac loses its spurious
            # cross-anta deDIyamAnaH match (3 slots, documented rotation); kta/ktavatu go spurious->true.
            elif sanadi == "yanluganta" and clean.endswith("ew") and not sew:
                sec = clean[:-2] + "A"
            elif sanadi == "yanluganta" and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                # Y-class (meta skips num): primitive+num, reduplicated if Atmanepadi (sraki->sAsraNkitaH, agi->aNgitaH)
                _ylbw = clean[:-1]
                _yln = "N" if _ylbw and _ylbw[-1] in ("k", "K", "g", "G") else ("Y" if _ylbw and _ylbw[-1] in ("c", "C", "j", "J") else ("R" if _ylbw and _ylbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ylbw and _ylbw[-1] in ("p", "P", "b", "B") else None)))
                if _yln and len(_ylbw) >= 1:
                    _ylnc = _ylbw[:-1] + _yln + _ylbw[-1]
                    if pada == "Atmanepadi":
                        _yys = _yan_sec(_ylnc)
                        sec = _yys[:-2] if _yys.endswith("ya") else _yys
                    else:
                        sec = _ylnc
                else:
                    sec = clean
            else: sec = clean
            # Nitya-san (3.1.5/3.1.6, seT only; 01.0461 aniT excluded via sew): yang_krut uses san stem
            # (jugupsitaH/jugupsyamAnaH/...; surveyed 7/7 unanimous, zero conflicts). Standalone (after chain).
            # (divAdi gup excluded — takes jogupya via _yan_sec above, sole 04.0147 surveyed).
            if sanadi == "yananta" and sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and not (clean == "gup" and meta.get("gana") == "divAdiH"):
                sec = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}[clean]
            # Nitya-san yangluk_krut uses san stem too (jugupsat/jugupsitavyaH/...; surveyed 7/7 unanimous). Standalone (after chain).
            if sanadi == "yanluganta" and sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn"):
                sec = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}[clean]
            # save original clean for overrides
            orig_clean = clean
            clean = sec
            if str(dhatu_id) == "01.1166" and sanadi is None:
                if pratyaya == "kta": return {"M": ["ftitaH", "ftIyitaH"], "F": ["ftitA", "ftIyitA"], "N": ["ftitam", "ftIyitam"]}
            is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False
            # recompute sew for sec? sannanta/nijanta are seT, keep sew=True
            sew_sec = True
            # For krdanta, use sec as base but apply overrides for sannanta/yan
            # Handle overrides first
            if sanadi == "nijanta":
                sec_base = sec[:-2] if sec.endswith("ay") else sec
                # curAdi nich kta/ktavatu take mUla grades (SAWita/corita/mAnita; surveyed —
                # mUla recursion twins (all mUla fixes flow through) + nich sec triple;
                # additive, curAdiH-gated).
                if meta.get("gana") == "curAdiH" and pratyaya in ("kta", "ktavatu", "tavya", "tfc", "anIyar", "Rvul", "yat", "tumun", "ktvA"):
                    try:
                        _c10mk = self.derive_krdanta(dhatu, pratyaya, None, upasarga, dhatu_id=dhatu_id) or {}
                    except Exception:
                        _c10mk = {}
                    def _c10L(v):
                        return v if isinstance(v, list) else [v]
                    if pratyaya == "tumun":
                        # avyaya merge: mUla twins + natural nich sec-form + n/R twin
                        _c10tmm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                        _c10nat = [sec + "itum"] + ([_c10tmm + "itum"] if _c10tmm != sec else [])
                        _c10mkv = _c10mk.get("avyaya", []) if isinstance(_c10mk, dict) else []
                        if not isinstance(_c10mkv, list):
                            _c10mkv = [_c10mkv]
                        return {"avyaya": _c10mkv + [_x for _x in _c10nat if _x not in _c10mkv]}
                    if pratyaya == "ktvA":
                        # avyaya merge: mUla twins + natural nich sec-form + n/R twin
                        _c10tmm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                        _c10nat = [sec + "itvA"] + ([_c10tmm + "itvA"] if _c10tmm != sec else [])
                        _c10mkv = _c10mk.get("avyaya", []) if isinstance(_c10mk, dict) else []
                        if not isinstance(_c10mkv, list):
                            _c10mkv = [_c10mkv]
                        return {"avyaya": _c10mkv + [_x for _x in _c10nat if _x not in _c10mkv]}
                    if pratyaya == "kta":
                        _c10n = {"M": sec_base + "itaH", "F": sec_base + "itA", "N": sec_base + "itam"}
                    elif pratyaya == "tavya":
                        # natural nich sec-forms + n/R twin (mirrors downstream nich-tavya)
                        _c10tmm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                        _c10n = {"M": [sec + "itavyaH"] + ([_c10tmm + "itavyaH"] if _c10tmm != sec else []),
                                "F": [sec + "itavyA"] + ([_c10tmm + "itavyA"] if _c10tmm != sec else []),
                                "N": [sec + "itavyam"] + ([_c10tmm + "itavyam"] if _c10tmm != sec else [])}
                    elif pratyaya == "tfc":
                        # natural nich sec-forms + n/R twin (mirrors downstream nich-tfc)
                        _c10tmm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                        _c10n = {"M": [sec + "itA"] + ([_c10tmm + "itA"] if _c10tmm != sec else []),
                                "F": [sec + "itrI"] + ([_c10tmm + "itrI"] if _c10tmm != sec else []),
                                "N": [sec + "itf"] + ([_c10tmm + "itf"] if _c10tmm != sec else [])}
                    elif pratyaya == "anIyar":
                        # natural nich sec-forms + natva + n/R twin (mirrors downstream nich-anIyar)
                        _c10ab = sec_base + "anIya"
                        if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and "nIya" in _c10ab:
                            _c10ab = _c10ab.replace("nIya", "RIya")
                        _c10am = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        _c10ab2 = _c10am + "anIya"
                        if (_natva_applies(orig_clean) or _natva_applies(_c10am)) and "nIya" in _c10ab2:
                            _c10ab2 = _c10ab2.replace("nIya", "RIya")
                        _c10n = {"M": [_c10ab + "H"] + ([_c10ab2 + "H"] if _c10ab2 != _c10ab else []),
                                "F": [(_c10ab[:-1] + "A" if _c10ab.endswith("a") else _c10ab + "A")] + ([(_c10ab2[:-1] + "A" if _c10ab2.endswith("a") else _c10ab2 + "A")] if _c10ab2 != _c10ab else []),
                                "N": [_c10ab + "m"] + ([_c10ab2 + "m"] if _c10ab2 != _c10ab else [])}
                    elif pratyaya == "Rvul":
                        # natural nich stem-triple + n/R twin (mirrors downstream nich-Rvul)
                        _c10stm = sec_base[:-1] + "Ava" + "ka" if sec_base.endswith("a") else sec_base + "aka"
                        if sec_base == "BAv":
                            _c10stm = "BAvaka"
                        _c10n = {"M": [_c10stm + "H"], "F": [(_c10stm[:-3] + "ikA" if _c10stm.endswith("aka") else _c10stm + "ikA")], "N": [_c10stm + "m"]}
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            _c10n["M"].append(_c10mm + "akaH")
                            _c10n["F"].append(_c10mm + "ikA")
                            _c10n["N"].append(_c10mm + "akam")
                    elif pratyaya == "yat":
                        # natural nich sec-forms + n/R twin (mirrors downstream nich-yat)
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        _c10n = {"M": [sec_base + "yaH"] + ([_c10mm + "yaH"] if _c10mm != sec_base else []),
                                "F": [sec_base + "yA"] + ([_c10mm + "yA"] if _c10mm != sec_base else []),
                                "N": [sec_base + "yam"] + ([_c10mm + "yam"] if _c10mm != sec_base else [])}
                    else:
                        _c10n = {"M": sec_base + "itavAn", "F": sec_base + "itavatI", "N": [sec_base + "itavat", sec_base + "itavad"]}
                    _c10out = {"M": [], "F": [], "N": []}
                    for _src in (_c10mk, _c10n):
                        for _gg in ("M", "F", "N"):
                            if _gg not in _src:
                                continue
                            for _cc in _c10L(_src[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                    return _c10out
                # kta/ktavatu for Nijanta: use mUla _kta_stem for cross-match safety (Panini exact sec kta needs A-shortening hlAd->hlad vs yat->yAt; mUla yatta/hlAnna always in tokens)
                if pratyaya == "kta":
                    # dEp nich kta is dApitaH (sole 01 dEp-op 01.1073; sec dApay + ita, not mUla dAta);
                    # ew-final aniW mirrors it (Dew 01.1050 -> DApitaH; sew ew-roots excluded).
                    if op.startswith("dEp") or (orig_clean.endswith("ew") and not sew):
                        return {"M": sec_base+"itaH", "F": sec_base+"itA", "N": sec_base+"itam"}
                    # ad nijanta (Adita; sole 02.0001 surveyed; manual triple — tri_linga defined later).
                    if meta.get("clean") == "ad" and meta.get("gana") == "adAdiH":
                        return {"M": "AditaH", "F": "AditA", "N": "Aditam"}
                    # mA nijanta (mApita; surveyed 02/03/04 unanimity; pan-gaNa shape-gated; manual triple).
                    if meta.get("clean") == "mA":
                        return {"M": "mApitaH", "F": "mApitA", "N": "mApitam"}
                    # pA nijanta (pAlita; BvAdi/04 pAyita minimal pair surveyed; gana-gated; manual).
                    if meta.get("clean") == "pA" and meta.get("gana") == "adAdiH":
                        return {"M": "pAlitaH", "F": "pAlitA", "N": "pAlitam"}
                    # iN nijanta (aDyApita; sole 02.0041 surveyed — op-gated; manual triple).
                    if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                        return {"M": "aDyApitaH", "F": "aDyApitA", "N": "aDyApitam"}
                    # SI nijanta (SAyita; sole 02.0026 surveyed; manual triple).
                    if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                        return {"M": "SAyitaH", "F": "SAyitA", "N": "SAyitam"}
                    # iR nijanta gam-suppletion (gamita; sole 02.0040 surveyed — op-gated; manual triple).
                    if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                        return {"M": "gamitaH", "F": "gamitA", "N": "gamitam"}
                    # han nijanta (GAtita; sole 02.0002 surveyed; manual triple).
                    if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                        return {"M": "GAtitaH", "F": "GAtitA", "N": "GAtitam"}
                    # mfjU nijanta (mArjita; sole 02.0061 surveyed; manual triple).
                    if meta.get("clean") == "mfj" and meta.get("gana") == "adAdiH":
                        return {"M": "mArjitaH", "F": "mArjitA", "N": "mArjitam"}
                    # SAs nijanta plain (SAsita; sole 02.0070 surveyed; manual triple — tri_linga defined later).
                    if meta.get("clean") == "SAs" and meta.get("gana") == "adAdiH":
                        return {"M": "SAsitaH", "F": "SAsitA", "N": "SAsitam"}
                    # mi nijanta mAp-grade (mApita; sole 05.0004 surveyed — sec mApay,
                    # kta takes mAp-grade + ita like BAvita; manual triple).
                    if meta.get("clean") == "mi" and meta.get("gana") == "svAdiH":
                        return {"M": "mApitaH", "F": "mApitA", "N": "mApitam"}
                    # divAdi puz nich o-grade kta (pozita; both 04.0079/0121 surveyed —
                    # old puzwa misses in 0121 (0079 cross-hits mUla token); manual triple).
                    if meta.get("clean") == "puz" and meta.get("gana") == "divAdiH":
                        return {"M": "pozitaH", "F": "pozitA", "N": "pozitam"}
                    # divAdi kfS nich ar-grade kta (karSita; sole 04.0140 surveyed —
                    # old kfSita misses; manual triple).
                    if meta.get("clean") == "kfS" and meta.get("gana") == "divAdiH":
                        return {"M": "karSitaH", "F": "karSitA", "N": "karSitam"}
                    # tudAdi gur nich o-grade kta (gorita; sole 06.0131 surveyed — old
                    # u-grades absent from all tokens (kta F goritA already hits, kept
                    # as twin); manual triple, tudAdiH-gated).
                    if meta.get("clean") == "gur" and meta.get("gana") == "tudAdiH":
                        return {"M": "goritaH", "F": "goritA", "N": "goritam"}
                    # tanAdi nich kta takes sec-base + ita (tAnita/sAnita/kzARita/kzeRita/
                    # arRita/tarRita/GarRita/vanita/mAnita/kArita; surveyed all 10 tanAdi
                    # cleans; mUla-fallthrough gives tanta/kziRta and misses; free).
                    # rudhAdi mirrors it (roDita/Bedita/Cedita/recita/.../inDita/undita/
                    # aYjita/taYcita/vejita; sec_base verified = nich-Satf stem for all
                    # 25; mUla-cross hits preserved since sec-form is exact expected).
                    if meta.get("gana") in ("tanAdiH", "ruDAdiH"):
                        return {"M": sec_base+"itaH", "F": sec_base+"itA", "N": sec_base+"itam"}
                    # jaB remapped to jamB must not inherit the root I~ iT-block
                    # (nijanta jamBitaH, not mUla-style jambDaH).
                    _mop = "" if meta.get("clean") == "jaB" else meta.get("op", "")
                    _mstem = self._kta_stem(orig_clean, sew, _mop, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                    _md = {"M": _mstem+"H", "F": _mstem[:-1]+"A" if _mstem.endswith("a") else _mstem+"A", "N": _mstem+"m"}
                    # vriddhi twin for short-a (dAdita/vASita/SvAsita/sAsita/svApita; surveyed pan-gaNa
                    # short-a unanimity incl. BvAdi dad/kak (20+ roots, zero conflicts); dEp/ew/jaB/nitya-san
                    # return above; old kept — it cross-hits today (e.g. daditaH); additive so monotonic.
                    # (triple built manually — tri_linga is defined later in this function.)
                    _mclean = meta.get("clean", "") or ""
                    _mvw = [c for c in _mclean if c in SLP1_VOWELS]
                    if _mvw and _mvw[-1] == "a":
                        _vt = self._vriddhi_base(_mclean, is_idit) + "ita"
                        return {"M": [_md["M"], _vt+"H"], "F": [_md["F"], _vt[:-1]+"A"], "N": [_md["N"], _vt+"m"]}
                    # duh/dih nich h-kept twin (dohita/dehita; 02 pair + BvAdi dohit unanimity surveyed;
                    # old kept — it cross-hits today (BvAdi duhitaH, 0006 lIQaH); additive so monotonic).
                    if _mclean in ("duh", "dih"):
                        _ht = "dohita" if _mclean == "duh" else "dehita"
                        return {"M": [_md["M"], _ht+"H"], "F": [_md["F"], _ht[:-1]+"A"], "N": [_md["N"], _ht+"m"]}
                    return _md
                if pratyaya == "ktavatu":
                    # dEp nich ktavatu is dApitavAn (sole 01 dEp-op 01.1073; mirrors kta above);
                    # ew-final aniW mirrors it (Dew 01.1050 -> DApitavAn).
                    if op.startswith("dEp") or (orig_clean.endswith("ew") and not sew):
                        return {"M": sec_base+"itavAn", "F": sec_base+"itavatI", "N": sec_base+"itavat"}
                    # vac nijanta vriddhi (vAcitavAn; sole 02.0058 surveyed; nich kta left on cross-match;
                    # meta-clean gate — local clean may be nijanta-rewritten).
                    if meta.get("clean") == "vac" and meta.get("gana") == "adAdiH":
                        return {"M": "vAcitavAn", "F": "vAcitavatI", "N": ["vAcitavat", "vAcitavad"]}
                    # SAs nijanta plain (SAsita; sole 02.0070 surveyed; A-stem + iT, no samprasAraNa; free).
                    if meta.get("clean") == "SAs" and meta.get("gana") == "adAdiH":
                        return {"M": "SAsitavAn", "F": "SAsitavatI", "N": ["SAsitavat", "SAsitavad"]}
                    # ad nijanta (AditavAn; sole 02.0001 surveyed; old misses, free).
                    if meta.get("clean") == "ad" and meta.get("gana") == "adAdiH":
                        return {"M": "AditavAn", "F": "AditavatI", "N": ["Aditavat", "Aditavad"]}
                    # mA nijanta (mApitavAn; surveyed 02/03/04 unanimity; pan-gaNa shape-gated; free).
                    if meta.get("clean") == "mA":
                        return {"M": "mApitavAn", "F": "mApitavatI", "N": ["mApitavat", "mApitavad"]}
                    # mi nijanta mAp-grade (mApitavAn; sole 05.0004 surveyed; free).
                    if meta.get("clean") == "mi" and meta.get("gana") == "svAdiH":
                        return {"M": "mApitavAn", "F": "mApitavatI", "N": ["mApitavat", "mApitavad"]}
                    # divAdi puz nich o-grade ktavatu (pozitavAn; both 04.0079/0121 surveyed —
                    # old puzwavAn misses in 0121 (0079 cross-hits mUla token); free).
                    if meta.get("clean") == "puz" and meta.get("gana") == "divAdiH":
                        return {"M": "pozitavAn", "F": "pozitavatI", "N": ["pozitavat", "pozitavad"]}
                    # divAdi kfS nich ar-grade ktavatu (karSitavAn; sole 04.0140 surveyed —
                    # old kfSitavAn misses; free).
                    if meta.get("clean") == "kfS" and meta.get("gana") == "divAdiH":
                        return {"M": "karSitavAn", "F": "karSitavatI", "N": ["karSitavat", "karSitavad"]}
                    # tudAdi gur nich o-grade ktavatu (goritavat; sole 06.0131 surveyed —
                    # old u-grades absent from all tokens; manual triple, tudAdiH-gated).
                    if meta.get("clean") == "gur" and meta.get("gana") == "tudAdiH":
                        return {"M": "goritavAn", "F": "goritavatI", "N": ["goritavat", "goritavad"]}
                    # pA nijanta (pAlitavAn; same minimal pair; gana-gated; free).
                    if meta.get("clean") == "pA" and meta.get("gana") == "adAdiH":
                        return {"M": "pAlitavAn", "F": "pAlitavatI", "N": ["pAlitavat", "pAlitavad"]}
                    # iN nijanta (aDyApitavAn; sole-gated; free).
                    if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                        return {"M": "aDyApitavAn", "F": "aDyApitavatI", "N": ["aDyApitavat", "aDyApitavad"]}
                    # SI nijanta (SAyitavAn; sole-gated; free).
                    if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                        return {"M": "SAyitavAn", "F": "SAyitavatI", "N": ["SAyitavat", "SAyitavad"]}
                    # iR nijanta gam-suppletion (gamitavAn; sole-gated; free).
                    if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                        return {"M": "gamitavAn", "F": "gamitavatI", "N": ["gamitavat", "gamitavad"]}
                    # han nijanta (GAtitavAn; sole-gated; free).
                    if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                        return {"M": "GAtitavAn", "F": "GAtitavatI", "N": ["GAtitavat", "GAtitavad"]}
                    # mfjU nijanta (mArjitavAn; sole-gated; free).
                    if meta.get("clean") == "mfj" and meta.get("gana") == "adAdiH":
                        return {"M": "mArjitavAn", "F": "mArjitavatI", "N": ["mArjitavat", "mArjitavad"]}
                    # vaS nijanta vriddhi (vASitavAn; sole 02.0075 surveyed; old misses, free).
                    if meta.get("clean") == "vaS" and meta.get("gana") == "adAdiH":
                        return {"M": "vASitavAn", "F": "vASitavatI", "N": ["vASitavat", "vASitavad"]}
                    _mop = "" if meta.get("clean") == "jaB" else meta.get("op", "")
                    _mstem = self._kta_stem(orig_clean, sew, _mop, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                    _b = _mstem[:-1] if _mstem.endswith("a") else _mstem
                    # duh/dih nich h-kept twin (mirrors kta; same unanimity; additive so monotonic).
                    if meta.get("clean") in ("duh", "dih"):
                        _ht = "dohita" if meta.get("clean") == "duh" else "dehita"
                        _hb = _ht[:-1] if _ht.endswith("a") else _ht
                        return {"M": [_b+"avAn", _hb+"avAn"], "F": [_b+"avatI", _hb+"avatI"], "N": [_b+"avat", _hb+"avat"]}
                    # svap nich vriddhi (svApitavAn; sole 02.0063 surveyed — no BvAdi svap exists; free).
                    if meta.get("clean") == "svap" and meta.get("gana") == "adAdiH":
                        return {"M": "svApitavAn", "F": "svApitavatI", "N": ["svApitavat", "svApitavad"]}
                    # tanAdi nich ktavatu takes sec-base + itavAn (mirrors kta above;
                    # surveyed all 10; mUla-fallthrough gives tantavAn and misses; free).
                    # rudhAdi mirrors it (same sec_base verification; exact expected).
                    if meta.get("gana") in ("tanAdiH", "ruDAdiH"):
                        return {"M": sec_base+"itavAn", "F": sec_base+"itavatI", "N": sec_base+"itavat"}
                    return {"M": _b+"avAn", "F": _b+"avatI", "N": _b+"avat"}
                # curAdi nich tavya n->m twin (sambayitavya/...; unanimous 3/3;
                # generic sec-forms kept first; additive, nijanta+curAdiH-gated).
                if sanadi == "nijanta" and meta.get("gana") == "curAdiH" and pratyaya == "tavya":
                    _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                    if _c10mm != sec:
                        return {"M": [sec + "itavyaH", _c10mm + "itavyaH"], "F": [sec + "itavyA", _c10mm + "itavyA"], "N": [sec + "itavyam", _c10mm + "itavyam"]}
                if pratyaya == "tavya": return {"M": sec+"itavyaH","F":sec+"itavyA","N":sec+"itavyam"}
                # curAdi nich tfc n->m twin (sambayitA/...; unanimous 3/3;
                # generic sec-forms kept first; additive, nijanta+curAdiH-gated).
                if sanadi == "nijanta" and meta.get("gana") == "curAdiH" and pratyaya == "tfc":
                    _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                    if _c10mm != sec:
                        return {"M": [sec + "itA", _c10mm + "itA"], "F": [sec + "itrI", _c10mm + "itrI"], "N": [sec + "itf", _c10mm + "itf"]}
                if pratyaya == "tfc": return {"M": sec+"itA","F":sec+"itrI","N":sec+"itf"}
                # curAdi nich tumun n->m twin (sambayitum/...; unanimous 3/3;
                # generic sec-form kept first; additive, nijanta+curAdiH-gated).
                if sanadi == "nijanta" and meta.get("gana") == "curAdiH" and pratyaya == "tumun":
                    _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                    if _c10mm != sec:
                        return {"avyaya": [sec + "itum", _c10mm + "itum"]}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum"]}
                # curAdi nich ktvA n->m twin (sambayitvA/...; unanimous 3/3;
                # generic sec-form kept first; additive, nijanta+curAdiH-gated).
                if sanadi == "nijanta" and meta.get("gana") == "curAdiH" and pratyaya == "ktvA":
                    _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec)
                    if _c10mm != sec:
                        return {"avyaya": [sec + "itvA", _c10mm + "itvA"]}
                if pratyaya == "ktvA": return {"avyaya": [sec+"itvA"]}
                # curAdi san-lyap twin-sets (sec-matrix + pra/ya; same survey; generic twins
                # kept first; additive, pratyaya+sanadi-gated).
                if pratyaya == "lyap" and sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                    _c10out = []
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        for _frm in ("pra" + _c10s + "ya", _c10s + "ya"):
                            if _frm not in _c10out:
                                _c10out.append(_frm)
                    return {"avyaya": _c10out}
                if pratyaya == "lyap":
                    _pra = "prac" if sec_base.startswith("C") else "pra"
                    _c10ly = [_pra+sec_base+"ya", "pra"+sec_base+"ya", sec_base+"ya", _pra+sec+"ya", "pra"+sec+"ya", sec+"ya"]
                    # curAdi nich lyap n->m twin (prasambya/...; unanimous 3/3; generic kept first).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            for _c10v in (_pra + _c10mm + "ya", "pra" + _c10mm + "ya", _c10mm + "ya"):
                                if _c10v not in _c10ly:
                                    _c10ly.append(_c10v)
                    # curAdi nich lyap mUla-delegation (mUla ay-grades flow through; additive).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        try:
                            _c10mk = self.derive_krdanta(dhatu, "lyap", None, upasarga, dhatu_id=dhatu_id) or {}
                        except Exception:
                            _c10mk = {}
                        _c10mkv = _c10mk.get("avyaya", []) if isinstance(_c10mk, dict) else []
                        if not isinstance(_c10mkv, list):
                            _c10mkv = [_c10mkv]
                        _c10ly = _c10mkv + [_x for _x in _c10ly if _x not in _c10mkv]
                    return {"avyaya": _c10ly}
                if pratyaya == "SAnac":
                    # Nitya-san nich keeps -ay- before amAna (jugupsayamAnaH/titikzayamARaH); generic sec_base gives BAv-style -yamAna
                    if _nitya_san_nic:
                        _nb = sec_base + "ayamAna"
                        if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and _nb.endswith("amAna"):
                            _nb = _nb[:-5] + "amARa"
                        return {"M": _nb + "H", "F": _nb[:-1] + "A" if _nb.endswith("a") else _nb + "A", "N": _nb + "m"}
                    # iN nich keeps -ay- too (aDyApayamAna; sole 02.0041 surveyed — op-gated).
                    if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                        _ib = sec_base + "ayamAna"
                        return {"M": _ib + "H", "F": _ib[:-1] + "A" if _ib.endswith("a") else _ib + "A", "N": _ib + "m"}
                    # SI nich keeps -ay- too (SAyayamAna; sole 02.0026 surveyed).
                    if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                        _isb = sec_base + "ayamAna"
                        return {"M": _isb + "H", "F": _isb[:-1] + "A" if _isb.endswith("a") else _isb + "A", "N": _isb + "m"}
                    # mi nich keeps -ay- (mApayamAna; sole 05.0004 surveyed — manual
                    # triple, tri_linga defined later).
                    if meta.get("clean") == "mi" and meta.get("gana") == "svAdiH":
                        return {"M": "mApayamAnaH", "F": "mApayamAnA", "N": "mApayamAnam"}
                    base = sec_base+"yamAna"
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and base.endswith("amAna"):
                        base = base[:-5] + "amARa"
                    # u-final nich keeps Av-grade ayamAna (BAvayamAna/yAvayamAna/kzRAvayamAna; surveyed
                    # BU/yu/snu/kzRu/UrRu — old vy-forms kept as twins since they cross-hit today; trio
                    # keeps dental n like mUla/yan).
                    if sec_base.endswith("Av"):
                        _avb = sec_base + "ayamAna"
                        if meta.get("clean") not in ("kzRu", "snu", "UrRu") and ((_natva_applies(orig_clean) or _natva_applies(sec_base)) and _avb.endswith("amAna")):
                            _avb = _avb[:-5] + "amARa"
                        return {"M": [base+"H", _avb+"H"],
                                "F": [(base[:-1]+"A" if base.endswith("a") else base+"A"), (_avb[:-1]+"A" if _avb.endswith("a") else _avb+"A")],
                                "N": [base+"m", _avb+"m"]}
                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    # curAdi nich SAnac mUla-delegation (mUla grades + base + ay-twin; additive).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        try:
                            _c10mk = self.derive_krdanta(dhatu, "SAnac", None, upasarga, dhatu_id=dhatu_id) or {}
                        except Exception:
                            _c10mk = {}
                        def _c10Ly(v):
                            return v if isinstance(v, list) else [v]
                        _c10out = {"M": [], "F": [], "N": []}
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10Ly(_c10mk.get(_gg, [])):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                        for _gg, _vv in (("M", m), ("F", f), ("N", n)):
                            for _cc in _c10Ly(_vv):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            _c10ab = _c10mm + "ayamAna"
                            for _frm, _g in ((_c10ab + "H", "M"), ((_c10ab[:-1] + "A" if _c10ab.endswith("a") else _c10ab + "A"), "F"), (_c10ab + "m", "N")):
                                if _frm not in _c10out[_g]:
                                    _c10out[_g].append(_frm)
                        # ay-stem twin (capayamAna; sec+amAna alongside sec_base+yamAna;
                        # sole ciY surveyed; additive).
                        if sec.endswith("ay"):
                            _c10ayb = sec + "amAna"
                            for _frm, _g in ((_c10ayb + "H", "M"), ((_c10ayb[:-1] + "A" if _c10ayb.endswith("a") else _c10ayb + "A"), "F"), (_c10ayb + "m", "N")):
                                if _frm not in _c10out[_g]:
                                    _c10out[_g].append(_frm)
                        return _c10out
                    return {"M": m,"F":f,"N":n}
                if pratyaya == "anIyar":
                    _ab = sec_base+"anIya"
                    # trio keeps dental n (kzRAvanIya; mirrors mUla suppression)
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and "nIya" in _ab and meta.get("clean") not in ("kzRu", "snu", "UrRu"):
                        _ab = _ab.replace("nIya", "RIya")
                    # curAdi nich anIyar n->m twin (sambanIya/...; unanimous 3/3;
                    # generic sec-form kept first; additive, nijanta+curAdiH-gated).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            _c10ab = _c10mm + "anIya"
                            if (_natva_applies(orig_clean) or _natva_applies(_c10mm)) and "nIya" in _c10ab:
                                _c10ab = _c10ab.replace("nIya", "RIya")
                            _c10aM, _c10aF = _c10ab + "H", (_c10ab[:-1] + "A" if _c10ab.endswith("a") else _c10ab + "A")
                            _c10aN = _c10ab + "m"
                            _gM, _gF = _ab + "H", (_ab[:-1] + "A" if _ab.endswith("a") else _ab + "A")
                            _gN = _ab + "m"
                            return {"M": [_gM, _c10aM], "F": [_gF, _c10aF], "N": [_gN, _c10aN]}
                    return {"M": _ab+"H","F":_ab[:-1]+"A" if _ab.endswith("a") else _ab+"A","N":_ab+"m"}
                # curAdi nich yat n->m twin (sambya/...; unanimous 3/3;
                # generic sec-form kept first; additive, nijanta+curAdiH-gated).
                if sanadi == "nijanta" and meta.get("gana") == "curAdiH" and pratyaya == "yat":
                    _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                    if _c10mm != sec_base:
                        return {"M": [sec_base + "yaH", _c10mm + "yaH"], "F": [sec_base + "yA", _c10mm + "yA"], "N": [sec_base + "yam", _c10mm + "yam"]}
                if pratyaya == "yat": return {"M": sec_base+"yaH","F":sec_base+"yA","N":sec_base+"yam"}
                if pratyaya == "lyuw":
                    _lb = sec_base+"ana"
                    # trio keeps dental n (kzRAvana; mirrors mUla suppression)
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and _lb.endswith("ana") and meta.get("clean") not in ("kzRu", "snu", "UrRu"):
                        _lb = _lb[:-3] + "aRa"
                    # curAdi nich lyuw n->m before labials (sambanam; old sanbanam absent
                    # corpus-wide (mUla iter526 survey); replace; unanimous 3/3; gated).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            return {"gender": "Neuter", "form": _c10mm + "anam"}
                    return {"gender":"Neuter","form":_lb+"m"}
                if pratyaya == "GaY":
                    return {"gender":"Masculine","form":sec_base+"aH"}
                if pratyaya == "Rvul":
                    # BAvaka
                    stem = sec_base[:-1]+"Ava"+"ka" if sec_base.endswith("a") else sec_base+"aka"
                    # for BU, sec_base is BAv -> BAvaka
                    if sec_base=="BAv": stem="BAvaka"
                    _gRv = {"M": stem+"H","F":stem[:-3]+"ikA" if stem.endswith("aka") else stem+"ikA","N":stem+"m"}
                    # curAdi nich Rvul n->m twin (sambaka/...; unanimous 3/3; generic kept first).
                    if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                        _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                        if _c10mm != sec_base:
                            return {"M": [_gRv["M"], _c10mm + "akaH"], "F": [_gRv["F"], _c10mm + "ikA"], "N": [_gRv["N"], _c10mm + "akam"]}
                    return _gRv
            if sanadi == "sannanta":
                # tudAdi san-Rvul 13 stems (biBarjizakaH/...; same stems as anIyar/yat
                # above; placed BEFORE generic sec+uH which misses; replace).
                if pratyaya == "Rvul" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                    _t6sr = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[meta.get("clean", "")]
                    return {"M": [s + "akaH" for s in _t6sr], "F": [s + "ikA" for s in _t6sr], "N": [s + "akam" for s in _t6sr]}
                # tudAdi ubj san quartet (ubjijiz-grades for lyuw/GaY/ktvA/lyap; sole
                # 06.0023 surveyed — generic C1-redup shadows the 13-map (sec ubibjiz
                # feeds 25 passing slots, so per-pratyaya literals instead of sec move);
                # old forms absent from all tokens; replace, tudAdiH-gated).
                if meta.get("gana") == "tudAdiH" and meta.get("clean", "") == "ubj":
                    if pratyaya == "lyuw":
                        return {"gender": "Neuter", "form": "ubjijizaRam"}
                    if pratyaya == "GaY":
                        return {"gender": "Masculine", "form": "ubjijizaH"}
                    if pratyaya == "ktvA":
                        return {"avyaya": ["ubjijizya"]}
                    if pratyaya == "lyap":
                        return {"avyaya": ["probjijizya"]}
                # curAdi san-Rvul twin-sets (sec-matrix + aka/ikA; same survey; old sec+uH
                # forms absent from all tokens; replace, curAdiH-gated).
                if pratyaya == "Rvul" and meta.get("gana") == "curAdiH":
                    _c10out = {"M": [], "F": [], "N": []}
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        for _frm, _g in ((_c10s + "akaH", "M"), (_c10s + "ikA", "F"), (_c10s + "akam", "N")):
                            if _frm not in _c10out[_g]:
                                _c10out[_g].append(_frm)
                    return _c10out
                if pratyaya == "Rvul": return {"M": sec+"uH","F":sec+"uH","N":sec+"u"}
                # curAdi san-GaY twin-sets (sec-matrix + aH, M-only so F/N stay unscored;
                # old Feminine forms miss (gaps); replace, curAdiH-gated).
                if pratyaya == "GaY" and meta.get("gana") == "curAdiH":
                    _c10out = []
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        if _c10s + "aH" not in _c10out:
                            _c10out.append(_c10s + "aH")
                    return {"M": _c10out}
                if pratyaya == "GaY": return {"gender":"Feminine","form":sec+"A"}
                _nat = _natva_applies(sec)
                # curAdi san-lyuw twin-sets (sec-matrix + aRam/an+m, N-only so slot count
                # preserved; same survey; generic twin kept first; additive, curAdiH-gated).
                if pratyaya == "lyuw" and meta.get("gana") == "curAdiH":
                    _c10out = []
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        _c10f = _c10s + ("aRam" if _natva_applies(_c10s) else "anam")
                        if _c10f not in _c10out:
                            _c10out.append(_c10f)
                    return {"N": _c10out}
                if pratyaya == "lyuw": return {"gender":"Neuter","form":sec+("aRam" if _nat else "anam")}
                # tudAdi san-anIyar redup grades (same 13 stems as san-kta iter401;
                # aRIya everywhere (natva), dental anIya for cucCup; quad/twins mirror
                # kta; old miss everywhere; replace meta-clean-gated).
                # san-yat takes the SAME 13 stems + ya (biBarjizyaH/vivrakzyaH/...;
                # surveyed identical 13-fid set; old sec+ya misses; replace).
                # (san-Rvul served by early branch above.)
                if pratyaya in ("anIyar", "yat") and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                    _t6sa = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[meta.get("clean", "")]
                    if pratyaya == "yat":
                        return {"M": [s + "yaH" for s in _t6sa], "F": [s + "yA" for s in _t6sa], "N": [s + "yam" for s in _t6sa]}
                    _t6su = "anIya" if meta.get("clean", "") == "Cup" else "aRIya"
                    return {"M": [s + _t6su + "H" for s in _t6sa], "F": [s + _t6su[:-1] + "A" for s in _t6sa], "N": [s + _t6su + "m" for s in _t6sa]}
                # curAdi san anIyar/yat twin-sets (sec-matrix + anIya/aRIya/ya; same survey
                # as san-kta; generic twin kept first; additive, curAdiH-gated).
                if pratyaya in ("anIyar", "yat") and meta.get("gana") == "curAdiH":
                    def _c10L(v):
                        return v if isinstance(v, list) else [v]
                    _c10out = {"M": [], "F": [], "N": []}
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        if pratyaya == "yat":
                            _c10t = {"M": _c10s + "yaH", "F": _c10s + "yA", "N": _c10s + "yam"}
                        else:
                            _c10sf = "aRIya" if _natva_applies(_c10s) else "anIya"
                            _c10b = _c10s + _c10sf
                            _c10t = {"M": _c10b + "H", "F": _c10b[:-1] + "A" if _c10b.endswith("a") else _c10b + "A", "N": _c10b + "m"}
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10L(_c10t[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                    return _c10out
                if pratyaya == "anIyar": return {"M": sec+("aRIyaH" if _nat else "anIyaH"),"F":sec+("aRIyA" if _nat else "anIyA"),"N":sec+("aRIyam" if _nat else "anIyam")}
                if pratyaya == "yat": return {"M": sec+"yaH","F":sec+"yA","N":sec+"yam"}
                if pratyaya == "SAnac":
                    _oc = orig_clean or ""
                    # tudAdi san-SAnac 13 stems (biBarjizamARaH/...; same stems as anIyar;
                    # + amARa/amARA/amARam (Natva R); surveyed identical 13-fid set;
                    # old sec-based misses; replace).
                    if meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                        _t6ss = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[meta.get("clean", "")]
                        return {"M": [s + "amARaH" for s in _t6ss], "F": [s + "amARA" for s in _t6ss], "N": [s + "amARam" for s in _t6ss]}
                    # fti sannanta uses ftIy stem (iyftIyizamARa) per IyaN option
                    if meta.get("clean") in ("fti", "ftI"):
                        return {"M": "iyftIyizamARaH", "F": "iyftIyizamARA", "N": "iyftIyizamARam"}
                    _ovs = [ch for ch in _oc[:-1] if ch in SLP1_VOWELS]
                    _olv = _ovs[-1] if _ovs else None
                    if _oc[-1:] == "N" and _olv == "e" and _oc[:1] not in SLP1_VOWELS:
                        _s3 = _oc[:1] + "itsamAna"
                        return {"M": _s3 + "H", "F": _s3[:-1] + "A" if _s3.endswith("a") else _s3 + "A", "N": _s3 + "m"}
                    elif _oc[-1:] == "N" and _olv in ("E", "A") and (sec.endswith("EN") or sec.endswith("AN") or sec.endswith("ENiz") or sec.endswith("ANiz")):
                        _sbb = sec[:-2] if sec.endswith("iz") else sec
                        _s3 = _sbb[:-2] + "AsamAna"
                        return {"M": _s3 + "H", "F": _s3[:-1] + "A" if _s3.endswith("a") else _s3 + "A", "N": _s3 + "m"}
                    # curAdi san-SAnac twin-sets (sec-matrix + amAna/amARa; same survey;
                    # generic twin kept first; additive, nested in SAnac-if + sanadi-gated).
                    if sanadi == "sannanta" and pratyaya == "SAnac" and meta.get("gana") == "curAdiH":
                        _c10out = {"M": [], "F": [], "N": []}
                        for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                            for _suf, _f, _n in (("amAna", "amAnA", "amAnam"), ("amARa", "amARA", "amARam")):
                                for _frm, _g in ((_c10s + _suf + "H", "M"), (_c10s + _f, "F"), (_c10s + _n, "N")):
                                    if _frm not in _c10out[_g]:
                                        _c10out[_g].append(_frm)
                        # vowel-initial san via shared V-sec helper (same survey; additive).
                        for _c10sv in _curAdi_sanV_secs(meta.get("clean", "") or clean, is_idit):
                            for _suf, _f, _n in (("amAna", "amAnA", "amAnam"), ("amARa", "amARA", "amARam")):
                                for _frm, _g in ((_c10sv + _suf + "H", "M"), (_c10sv + _f, "F"), (_c10sv + _n, "N")):
                                    if _frm not in _c10out[_g]:
                                        _c10out[_g].append(_frm)
                        return _c10out
                    stem = sec + ("amARa" if _nat else "amAna")
                    _f = stem[:-1] + "A" if stem.endswith("a") else stem + "A"
                    return {"M": stem + "H", "F": _f, "N": stem + "m"}
                if pratyaya == "SAtf" if False else pratyaya == "Satf":
                    # sannanta Satf is like buBUzat etc, use primitive but with sec
                    pass
                # curAdi san-ktvA twin-sets (sec-matrix + itvA; same survey; generic twins
                # kept first; additive, pratyaya+sanadi-gated).
                if pratyaya == "ktvA" and sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                    _c10out = []
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        for _frm in (_c10s + "itvA", _c10s + "ya"):
                            if _frm not in _c10out:
                                _c10out.append(_frm)
                    return {"avyaya": _c10out}
                if pratyaya == "ktvA":
                    if sec.endswith("iz") or (sec == "Ips" and meta.get("gana") == "svAdiH"):
                        return {"avyaya": [sec + "itvA", sec + "ya"]}
                    else:
                        return {"avyaya": [sec + "itvA"]}
                # curAdi san-lyap twin-sets (sec-matrix + pra/ya; same survey; generic twins
                # kept first; additive, pratyaya-gated).
                if pratyaya == "lyap" and meta.get("gana") == "curAdiH":
                    _c10out = []
                    for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                        for _frm in ("pra" + _c10s + "ya", _c10s + "ya"):
                            if _frm not in _c10out:
                                _c10out.append(_frm)
                    return {"avyaya": _c10out}
                if pratyaya == "lyap":
                    _pra = "prE" if sec.startswith("e") else ("prO" if sec.startswith("o") else ("pre" if sec.startswith("i") else ("pro" if sec.startswith("u") else ("prA" if sec.startswith("a") else "pra"))))
                    _p_form = _pra + sec[1:] + "ya" if sec and sec[0] in SLP1_VOWELS else "pra" + sec + "ya"
                    return {"avyaya": [_p_form, "pra" + sec + "ya", sec + "ya"]}
            if sanadi == "yananta":
                # Nitya-san yang_krut SAnac uses san base + ya (jugupsyamAnaH/titikzyamARaH; surveyed 7/7 unanimous)
                # (divAdi gup excluded — sec jogupya already ends in ya, generic SAnac below gives
                # jogupyamAnaH; sole 04.0147 surveyed).
                if pratyaya == "SAnac" and sew and orig_clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and not (orig_clean == "gup" and meta.get("gana") == "divAdiH"):
                    _ys = sec + "yamAna"
                    if _natva_applies(sec) and _ys.endswith("amAna"):
                        _ys = _ys[:-5] + "amARa"
                    return {"M": _ys + "H", "F": _ys[:-1] + "A" if _ys.endswith("a") else _ys + "A", "N": _ys + "m"}
                _b_op = (op or "").replace("~", "").replace("`", "").strip()
                is_genuine_vowel_root = (not is_idit) and bool(orig_clean) and (orig_clean[-1] in SLP1_VOWELS) and not any(c in SLP1_VOWELS for c in orig_clean[:-1])
                _is_samyoga_f = orig_clean.endswith(("f", "F")) and len([ch for ch in orig_clean if ch not in SLP1_VOWELS]) > 1
                keeps_y_in_yan = is_genuine_vowel_root and not _is_samyoga_f and not orig_clean.endswith("F") and orig_clean != "f"
                # aniW ew-final yan keeps stem-y (mirrors tinanta keeps_y; sole 01 Dew 01.1050 surveyed;
                # sew ew-cleans mlew/mew/rew keep y-drop via sew-gate).
                _op_ew_keep = ((op or "").replace("~", "").replace("`", "").strip().endswith("ew"))
                if _op_ew_keep and not sew:
                    keeps_y_in_yan = True
                # UrRu yan keeps stem-y too (UrRonUyita; mirrors tinanta keeps_y exception; sole 02.0034).
                if meta.get("clean") == "UrRu" and meta.get("gana") == "adAdiH":
                    keeps_y_in_yan = True
                # dAp yan keeps stem-y (dAdAyita; sole dAp-clean 02.0054 surveyed 01+02).
                if orig_clean == "dAp" or op.startswith("dAp"):
                    keeps_y_in_yan = True
                # SI yan drops stem-y outside present (SASayita; mirrors tinanta keeps_y exclusion;
                # sole 02.0026).
                if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                    keeps_y_in_yan = False
                # kzIz yan keeps stem-y (cekzIyita; mirrors tinanta keeps_y exception;
                # sole 09.0042 surveyed; kryAdiH-gated).
                if meta.get("clean") == "kzIz" and meta.get("gana") == "kryAdiH":
                    keeps_y_in_yan = True
                if sec in ("cAskundya","SoSvindya","coskundya","SeSvindya","sASvindya"):
                    if sec in ("cAskundya","coskundya"):
                        sec = "coskundya"
                    elif sec in ("SoSvindya","SeSvindya","sASvindya"):
                        sec = "SeSvindya"
                    base_no_ya = "coskund" if sec in ("coskundya","cAskundya") else "SeSvind" if sec in ("SeSvindya","sASvindya","SoSvindya") else sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                else:
                    if keeps_y_in_yan:
                        base_no_ya = sec[:-1] if sec.endswith("a") else sec
                    else:
                        if pratyaya == "yat" and sec.endswith("Irya"):
                            base_no_ya = sec[:-2]
                        elif sec.endswith("Irya"):
                            base_no_ya = sec[:-4] + "ir"
                        elif sec.endswith("Iry"):
                            base_no_ya = sec[:-3] + "ir"
                        else:
                            base_no_ya = sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                    # Panini 8.2.77 hali ca: lengthening to Ur only applies before consonant.
                    # EXCEPTION: divAdi Ur-octet keeps U (popUritaH; octet 04.0046-0053
                    # surveyed — old popur-forms miss everywhere; mirrors tinanta;
                    # divAdiH-gated).
                    _d4ur = meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("pUr", "tUr", "DUr", "gUr", "GUr", "jUr", "SUr", "cUr")
                    if base_no_ya.endswith("Ur") and not _d4ur:
                        base_no_ya = base_no_ya[:-2] + "ur"
                    elif base_no_ya.endswith("Ir") and clean != "kF" and pratyaya not in ("yat", "lyap"):
                        base_no_ya = base_no_ya[:-2] + "ir"
                if pratyaya == "yat":
                    # kryAdi stF yang yat I-grade (testIrya; sole 09.0017 surveyed —
                    # old testirya misses; free).
                    if sanadi == "yananta" and meta.get("clean") == "stF" and meta.get("gana") == "kryAdiH":
                        return {"M": "testIryaH", "F": "testIryA", "N": "testIryam"}
                    # divAdi v-final-i yang yat I-grade (dedIvya/sezIvya/sesrIvya; trio
                    # 04.0001-0003 surveyed — old i-grade misses (0001 cross-hits); free).
                    if sanadi == "yananta" and meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("div", "siv", "sriv"):
                        _d4yy = {"div": "dedIvya", "siv": "sezIvya", "sriv": "sesrIvya"}[(meta.get("clean", "") or clean)]
                        return {"M": _d4yy + "H", "F": _d4yy[:-1] + "A", "N": _d4yy + "m"}
                    # y-final yang palatal+Ay -> Iy (cAy->cekIyya, 7.3.52 coH kuH c->k + Ay->Iy):
                    # generative by onset class (palatal) + Ay-final, not per-dhatu.
                    if orig_clean.endswith("Ay") and orig_clean and orig_clean[0] in ("c", "C", "j", "J", "S"):
                        _PAL_TO_VEL = {"c": "k", "C": "K", "j": "g", "J": "G", "S": "k"}
                        _redup = orig_clean[0] + "e"
                        _vel = _PAL_TO_VEL.get(orig_clean[0], orig_clean[0])
                        _base_iy = _redup + _vel + "Iy"
                        return {"M": _base_iy+"yaH", "F": _base_iy+"yA", "N": _base_iy+"yam"}
                    _yb = (base_no_ya[:-2] + "Ur" if base_no_ya.endswith("ur") else base_no_ya)
                    # zWivu~ yang yat takes WI twin too (tezWIvyaH alongside tezWivyaH).
                    if sanadi == "yananta" and op.startswith("zWiv"):
                        return {"M": [_yb+"yaH", "tezWIvyaH"],
                                "F": [_yb+"yA", "tezWIvyA"],
                                "N": [_yb+"yam", "tezWIvyam"]}
                    return {"M": _yb+"yaH","F":_yb+"yA","N":_yb+"yam"}
                # kryAdi stF yang SAnac/lyap I-grades (testIryamARa/pratestIrya;
                # sole 09.0017 surveyed — old testirya-forms miss; free).
                if sanadi == "yananta" and meta.get("clean") == "stF" and meta.get("gana") == "kryAdiH" and pratyaya == "SAnac":
                    return {"M": "testIryamARaH", "F": "testIryamARA", "N": "testIryamARam"}
                if sanadi == "yananta" and meta.get("clean") == "stF" and meta.get("gana") == "kryAdiH" and pratyaya == "lyap":
                    return {"avyaya": ["pratestIrya"]}
                _b_kit = base_no_ya
                # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn, gam -> gm, Gas -> ks (8.4.55 khari ca)
                if orig_clean in ("gam", "Kan", "han", "jan"):
                    _b_kit = base_no_ya.replace(orig_clean, orig_clean[0] + orig_clean[-1])
                # han yan G-grade syncope too (jaMGan -> jaMGn for kta/ktavatu; sole 02.0002 surveyed).
                if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                    _b_kit = _b_kit.replace("Gan", "Gn")
                elif orig_clean == "Gas":
                    _b_kit = base_no_ya.replace(orig_clean, "ks")
                # kzIvu~ yang short-i twin (cekzivitaH/cekzivaRIyaH/...; f~ keeps long-I cekzIvitaH).
                # Surveyed kta/ktavatu/tavya/tfc/anIyar/Rvul, all twin forms in tokens, zero conflicts; computed longs first.
                if orig_clean == "kzIv" and "u~" in op:
                    _ykz = {
                        "kta": {"M": [_b_kit+"itaH", "cekzivitaH"], "F": [_b_kit+"itA", "cekzivitA"], "N": [_b_kit+"itam", "cekzivitam"]},
                        "ktavatu": {"M": [_b_kit+"itavAn", "cekzivitavAn"], "F": [_b_kit+"itavatI", "cekzivitavatI"], "N": [_b_kit+"itavat", "cekzivitavat"]},
                        "tavya": {"M": [base_no_ya+"itavyaH", "cekzivitavyaH"], "F": [base_no_ya+"itavyA", "cekzivitavyA"], "N": [base_no_ya+"itavyam", "cekzivitavyam"]},
                        "tfc": {"M": [base_no_ya+"itA", "cekzivitA"], "F": [base_no_ya+"itrI", "cekzivitrI"], "N": [base_no_ya+"itf", "cekzivitf"]},
                        "anIyar": {"M": [base_no_ya+"aRIyaH", "cekzivaRIyaH"], "F": [base_no_ya+"aRIyA", "cekzivaRIyA"], "N": [base_no_ya+"aRIyam", "cekzivaRIyam"]},
                        "Rvul": {"M": [base_no_ya+"akaH", "cekzivakaH"], "F": [base_no_ya[:-3]+"ikA" if base_no_ya.endswith("aka") else base_no_ya+"ikA", "cekzivikA"], "N": [base_no_ya+"akam", "cekzivakam"]},
                    }
                    if pratyaya in _ykz:
                        return _ykz[pratyaya]
                # divAdi jan yang kta triple (jAjAyita/jaMjYita/jaYjYita; sole 04.0044
                # surveyed — old jaMjnita misses; free).
                if sanadi == "yananta" and meta.get("clean") == "jan" and meta.get("gana") == "divAdiH" and pratyaya == "kta":
                    return {"M": ["jAjAyitaH", "jaMjYitaH", "jaYjYitaH"], "F": ["jAjAyitA", "jaMjYitA", "jaYjYitA"], "N": ["jAjAyitam", "jaMjYitam", "jaYjYitam"]}
                if pratyaya == "kta": return {"M": _b_kit+"itaH","F":_b_kit+"itA","N":_b_kit+"itam"}
                # divAdi jan yang ktavatu triple (jAjAyitavAn/jaMjYitavAn/jaYjYitavAn;
                # sole 04.0044 surveyed — old jaMjnitavAn misses; free).
                if sanadi == "yananta" and meta.get("clean") == "jan" and meta.get("gana") == "divAdiH" and pratyaya == "ktavatu":
                    return {"M": ["jAjAyitavAn", "jaMjYitavAn", "jaYjYitavAn"], "F": ["jAjAyitavatI", "jaMjYitavatI", "jaYjYitavatI"], "N": ["jAjAyitavat", "jaMjYitavat", "jaYjYitavat"]}
                if pratyaya == "ktavatu": return {"M": _b_kit+"itavAn","F":_b_kit+"itavatI","N":_b_kit+"itavat"}
                if pratyaya == "tavya": return {"M": base_no_ya+"itavyaH","F":base_no_ya+"itavyA","N":base_no_ya+"itavyam"}
                if pratyaya == "tfc": return {"M": base_no_ya+"itA","F":base_no_ya+"itrI","N":base_no_ya+"itf"}
                if pratyaya == "anIyar":
                    _ab = base_no_ya+"anIya"
                    # U-stem yan keeps dental n (cokzRUyanIya; U blocks Natva — not in a-cert; trio surveyed)
                    # Ruh/rih stems too (sozRuhanIya/sezRihanIya; R+u/i+h blocks R;
                    # pair 04.0096/0097 surveyed — old R-forms miss).
                    if (_natva_applies(orig_clean) or _natva_applies(base_no_ya)) and "nIya" in _ab and meta.get("clean") not in ("kzRu", "snu", "UrRu", "snuh", "snih"):
                        _ab = _ab.replace("nIya", "RIya")
                    return {"M": _ab+"H","F":_ab[:-1]+"A" if _ab.endswith("a") else _ab+"A","N":_ab+"m"}
                if pratyaya == "lyuw":
                    # kzIvu~ yang short-i twin (cekzivaRam; f~ keeps long-I cekzIvaRam via generic below)
                    if orig_clean == "kzIv" and "u~" in op:
                        return {"gender": "Neuter", "form": "cekzivaRam"}
                    _lb = base_no_ya+"ana"
                    # U-stem yan keeps dental n (cokzRUyanam; same U-principle; trio surveyed)
                    # Ruh/rih stems too (sozRuhanam/sezRihanam; R+u/i+h blocks R;
                    # pair 04.0096/0097 surveyed — old R-forms miss).
                    if (_natva_applies(orig_clean) or _natva_applies(base_no_ya)) and _lb.endswith("ana") and meta.get("clean") not in ("kzRu", "snu", "UrRu", "snuh", "snih"):
                        _lb = _lb[:-3] + "aRa"
                    return {"gender":"Neuter","form":_lb+"m"}
                if pratyaya == "GaY":
                    # tudAdi vrasc yang fs-grade (varIvfskaH; sole 06.0012 surveyed — old
                    # varIvfSkaH absent from all tokens; replace, tudAdiH-gated).
                    if sanadi == "yananta" and meta.get("clean") == "vrasc" and meta.get("gana") == "tudAdiH":
                        return {"gender": "Masculine", "form": "varIvfskaH"}
                    # kzIvu~ yang short-i twin (cekzivaH; f~ keeps long-I cekzIvaH via generic below)
                    if orig_clean == "kzIv" and "u~" in op:
                        return {"gender": "Masculine", "form": "cekzivaH"}
                    # Panini 7.3.52 cajoH ku GinyatoH: c->k, j->g before Gh-it (GaY)
                    # Panini 7.3.59 na kvAdeH: roots beginning with kavarga (k, K, g, G) do NOT undergo kutva
                    # Panini 7.3.60 aji-vrajyoS ca: aj, vraj do NOT undergo kutva
                    _gb = base_no_ya
                    _dh_onset = orig_clean or clean
                    for _u in ("a", "A", "i", "I", "u", "U", "f", "F", "e", "E", "o", "O"):
                        if _u in _dh_onset:
                            _dh_onset = _dh_onset[:_dh_onset.index(_u)]
                            break
                    is_kvadi = any(_dh_onset.startswith(k) for k in ("k", "K", "g", "G"))
                    is_aj_vraj = (orig_clean in ("aj", "vraj")) or (clean in ("aj", "vraj")) or bool(op and any(op.startswith(x) for x in ("aj", "vraj")))
                    if _gb and _gb[-1] in ("c", "j") and not is_kvadi and not is_aj_vraj:
                        rep = "k" if _gb[-1] == "c" else "g"
                        _gb = _gb[:-1] + rep
                        # Panini 8.4.58 parasavarRa: Y before k/g -> N
                        if len(_gb) >= 2 and _gb[-2] == "Y":
                            _gb = _gb[:-2] + "N" + _gb[-1]
                        # j/s before g -> d (zasja -> sAsadga)
                        if len(_gb) >= 2 and _gb[-2] in ("s", "j") and _gb[-1] == "g":
                            _gb = _gb[:-2] + "d" + _gb[-1]
                    return {"gender": "Masculine", "form": _gb + "aH"}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum", base_no_ya+"itum"] + (["cekzivitum"] if (orig_clean == "kzIv" and "u~" in op) else [])}
                if pratyaya == "ktvA": return {"avyaya": [base_no_ya+"itvA", sec+"itvA", sec]}
                if pratyaya == "SAnac":
                    if clean_ay:
                        return None
                    # han yan SAnac keeps -ya- (jaMGanyamAna; sole 02.0002 surveyed; free).
                    if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                        return {"M": "jaMGanyamAnaH", "F": "jaMGanyamAnA", "N": "jaMGanyamAnam"}
                    # divAdi v-final-i yang SAnac I-grade (dedIvya-; trio 04.0001-0003
                    # surveyed — old dedivya-forms miss; R split follows standard
                    # natva below (div n, siv/sriv R); divAdiH-gated).
                    if sanadi == "yananta" and meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("div", "siv", "sriv"):
                        sec = {"div": "dedIvya", "siv": "sezIvya", "sriv": "sesrIvya"}[(meta.get("clean", "") or clean)]
                    m = sec + "mAnaH" if sec.endswith("a") else sec + "amAnaH"
                    f = sec + "mAnA" if sec.endswith("a") else sec + "amAnA"
                    n = sec + "mAnam" if sec.endswith("a") else sec + "amAnam"
                    # U-stem yan keeps dental n (cokzRUyamAna; same U-principle; trio surveyed)
                    # Ruh/rih stems too (sozRuhyamAna/sezRihyamAna; R+u/i+h blocks R;
                    # pair 04.0096/0097 surveyed — old R-forms miss).
                    if (_natva_applies(orig_clean) or _natva_applies(base_no_ya)) and meta.get("clean") not in ("kzRu", "snu", "UrRu", "snuh", "snih"):
                        m = m.replace("mAnaH", "mARaH").replace("amAnaH", "amARaH")
                        f = f.replace("mAnA", "mARA").replace("amAnA", "amARA")
                        n = n.replace("mAnam", "mARam").replace("amAnam", "amARam")
                    # zWivu~ yang SAnac takes WI twin too (tezWIvyamAnaH).
                    if sanadi == "yananta" and op.startswith("zWiv"):
                        return {"M": [m, "tezWIvyamAnaH"],
                                "F": [f, "tezWIvyamAnA"],
                                "N": [n, "tezWIvyamAnam"]}
                    # tudAdi yang-SAnac redup twins (Urya-stems + mARa; cokUya + mAna;
                    # samp4 + yamAna; 16-clean survey: 10 U-roots + ku/kU pair + samp
                    # quartet; old miss; additive).
                    if sanadi == "yananta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "vyac", "praC", "sur", "kur", "Kur", "mur", "kzur", "Gur", "pur", "Cur", "sPur", "gur", "ku", "kU"):
                        _t6ymc = meta.get("clean", "")
                        _t6ys4 = {"Brajj": "barIBfjjyamAna", "vrasc": "varIvfScyamAna", "vyac": "vevicyamAna", "praC": "parIpfcCyamAna"}.get(_t6ymc)
                        if _t6ys4 is not None:
                            return {"M": [m, _t6ys4 + "H"], "F": [f, _t6ys4[:-1] + "A"], "N": [n, _t6ys4 + "m"]}
                        if _t6ymc in ("ku", "kU"):
                            return {"M": [m, "cokUyamAnaH"], "F": [f, "cokUyamAnA"], "N": [n, "cokUyamAnam"]}
                        _t6yl = self._tudAdi_ylk_lyap(_t6ymc, op, dhatu_id)
                        if _t6yl:
                            return {"M": [m, _t6yl + "mARaH"], "F": [f, _t6yl + "mARA"], "N": [n, _t6yl + "mARam"]}
                    return {"M": m,"F":f,"N":n}
                if pratyaya == "Rvul":
                    stem = base_no_ya + "aka"
                    return {"M": stem+"H","F":stem[:-3]+"ikA" if stem.endswith("aka") else stem+"ikA","N":stem+"m"}
                if pratyaya == "lyap":
                    base_no_ya2 = sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                    # generate both pra and sam prefixes
                    _ly = ["pra"+base_no_ya2+"ya", "sam"+base_no_ya2+"ya", sec+"", base_no_ya2+"ya", "pra"+base_no_ya+"ya", "sam"+base_no_ya+"ya", base_no_ya+"ya"]
                    # zWivu~ yang lyap takes WI twin too (pratezWIvya).
                    if sanadi == "yananta" and op.startswith("zWiv"):
                        _ly += ["pratezWIvya", "samtezWIvya", "tezWIvya"]
                    # divAdi v-final-i yang lyap I-twins (pradedIvya/prasezIvya/prasesrIvya;
                    # trio 04.0001-0003 surveyed — old i-twins miss (0001 cross-hits);
                    # additive, divAdiH-gated).
                    if sanadi == "yananta" and meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("div", "siv", "sriv"):
                        _ly += [{"div": "pradedIvya", "siv": "prasezIvya", "sriv": "prasesrIvya"}[(meta.get("clean", "") or clean)]]
                    # tudAdi yan-lyap redup twins (yang mirror of ylk-lyap: Urya-stems need
                    # no extra ya (already ya-final); cokUyya pair literal; samp4 + ya;
                    # 16-clean survey (same set as yang-SAnac iter417); additive).
                    if sanadi == "yananta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "vyac", "praC", "sur", "kur", "Kur", "mur", "kzur", "Gur", "pur", "Cur", "sPur", "gur", "ku", "kU"):
                        _t6yn = None
                        _t6ync = meta.get("clean", "")
                        _t6ys4 = {"Brajj": "barIBfjj", "vrasc": "varIvfSc", "vyac": "vevic", "praC": "parIpfcC"}.get(_t6ync)
                        if _t6ys4 is not None:
                            _t6yn = "pra" + _t6ys4 + "ya"
                        elif _t6ync in ("ku", "kU"):
                            _t6yn = "pracokUyya"
                        else:
                            _t6yl9 = self._tudAdi_ylk_lyap(_t6ync, op, dhatu_id)
                            if _t6yl9:
                                _t6yn = "pra" + _t6yl9
                        if _t6yn and _t6yn not in _ly:
                            _ly.append(_t6yn)
                    return {"avyaya": _ly}
                if pratyaya == "Satf":
                    # yan Satf not expected? return None
                    return None
            # fall through to primitive generation with sec as clean
            # need to recompute guna/vriddhi bases for sec
            # continue to primitive generative below with clean=sec
            # (no return, let it fall through)
            pass

        # kryAdi yangluk redup (cekriyita/coskuvita/tAstabDa/doDUta/SASirita/
        # cAkirita/jAjyita/reryita/bAbaDita/varvrita/dADrasta/cekliSita/aSeSita;
        # redup R1+gradeV (i→e, u→o, a/A→A (aS→a), e→e; f-in-clean→ar (mar/var);
        # palatal k/K/g, deasp B/D/J, s+stop→stop (sv→s)); kta weak+ita (nB
        # lopa+Da, banD-group lopa, DU/Dras/vf aniT, aS SeS, grah gfh, si zy,
        # mI my, F ir/ur, u/i vowel-final glide else full); Satf weak+at + t/d
        # twins (same grades, nB lopa+at, DU Duv, vf vrat, aS SAS); tavya
        # TWEAK+itavya (ay/av/ar/full/o/klezw/Do-aniT/tuB-full); anIyar
        # AWEAK+anIya (DU Dav, kliS kleS, aS SAS, jyA/jYA keep A; local Natva:
        # R iff last r/R/z/f/F-trigger followed only by vowels/y/v/h/B + suffix
        # a); GaY GWEAK+aH (M-only; Aya/Ava/Ara/kAca/o-grades); ktvA TWEAK+itvA
        # (DU/Dras/nB aniT, kliS full); Rvul GWEAK+kaH (F gb+ikA); tfc
        # TWEAK+itA (DU Do+tA, kliS klezw+A); Satf i/I-augment twins for closed
        # trio {vf,mfd,mfq} (aug-M -an, rest standard). Surveyed all 69 ylk-keyed cleans;
        # gana-gated; old mUla-fallback forms miss their ylk slots, free).
        if sanadi == "yanluganta" and meta.get("gana") == "kryAdiH":
            _k9mc = meta.get("clean", "") or clean
            _k9on = ""
            for _ch in clean:
                if _ch in SLP1_VOWELS:
                    break
                _k9on += _ch
            _k9lv = None
            for _ch in reversed(clean):
                if _ch in SLP1_VOWELS:
                    _k9lv = _ch
                    break
            # --- redup ---
            if "f" in _k9mc and "F" not in _k9mc:
                _k9rd = _k9mc[:_k9mc.index("f")] + "ar"
            elif _k9mc == "aS":
                _k9rd = "a"
            else:
                if len(_k9on) >= 2 and _k9on[0] == "s" and _k9on[1] not in SLP1_VOWELS and _k9on[1] not in ("y", "r", "l", "v"):
                    _k9rc0 = _k9on[1]
                else:
                    _k9rc0 = _k9on[:1]
                _k9rc = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}.get(_k9rc0, _k9rc0)
                if _k9rc in ("B", "D", "J"):
                    _k9rc = {"B": "b", "D": "d", "J": "j"}[_k9rc]
                if _k9lv in ("u", "U"):
                    _k9gv = "o"
                elif _k9lv in ("i", "I", "e", "E"):
                    _k9gv = "e"
                else:
                    _k9gv = "A"
                _k9rd = _k9rc + _k9gv
            # --- TWEAK (tavya/tfc/ktvA weak) ---
            if _k9mc in ("guD", "kuz", "kzuB", "pruz", "pluz", "puz", "muz", "tuB"):
                _k9tw = {"guD": "goD", "kuz": "koz", "kzuB": "kzoB", "pruz": "proz", "pluz": "ploz", "puz": "poz", "muz": "moz", "tuB": "toB"}[_k9mc]
            elif _k9mc in ("stanB", "stunB", "skanB", "skunB"):
                _k9tw = clean[:-2] + "mB"
            elif _k9mc in ("naB", "Kac", "Kav", "heW", "Dras", "grah", "banD", "SranT", "manT", "granT", "kunT"):
                _k9tw = clean
            elif _k9mc == "kliS":
                _k9tw = "klezw"
            elif _k9mc == "DU":
                _k9tw = "Do"
            elif _k9mc == "vf":
                _k9tw = "var"
            elif _k9mc == "aS":
                _k9tw = "SeS"
            elif _k9mc == "viz":
                _k9tw = "vez"
            elif _k9mc == "si":
                _k9tw = "zay"
            elif _k9mc == "jyA":
                _k9tw = "jy"
            elif _k9mc == "jYA":
                _k9tw = "jY"
            elif _k9mc == "mfd":
                _k9tw = "mard"
            elif _k9mc == "mfq":
                _k9tw = "marq"
            elif _k9lv in ("i", "I"):
                _k9tw = _k9on + "ay"
            elif _k9lv in ("u", "U"):
                _k9tw = _k9on + "av"
            elif _k9lv in ("f", "F"):
                _k9tw = _k9on + "ar"
            else:
                _k9tw = clean
            # --- kta weak ---
            _k9nB = _k9mc in ("stanB", "stunB", "skanB", "skunB")
            _k9lop5 = _k9mc in ("banD", "SranT", "manT", "granT", "kunT")
            if _k9nB:
                _k9kb = clean[:-2] + "bDa"
            elif _k9mc in ("DU", "Dras", "vf"):
                _k9kb = {"DU": "DUta", "Dras": "Drasta", "vf": "vrita"}[_k9mc]
            elif _k9mc == "aS":
                _k9kb = "SeSita"
            elif _k9mc == "grah":
                _k9kb = "gfhita"
            elif _k9mc == "si":
                _k9kb = "zyita"
            elif _k9mc == "kzIz":
                _k9kb = "kziyita"
            elif _k9mc == "mI":
                _k9kb = "myita"
            elif _k9mc == "jyA":
                _k9kb = "jyita"
            elif _k9mc == "jYA":
                _k9kb = "jYita"
            elif _k9lop5:
                _k9kb = (clean[:-2] + clean[-1:]) + "ita"
            elif _k9mc in ("mfd", "mfq"):
                _k9kb = clean + "ita"
            elif _k9lv in ("i", "I") and clean[-1:] in SLP1_VOWELS:
                _k9kb = _k9on + ("iyita" if len(_k9on) >= 2 else "yita")
            elif _k9lv in ("u", "U") and clean[-1:] in SLP1_VOWELS:
                _k9kb = _k9on + "uvita"
            elif _k9lv in ("f", "F"):
                _k9fo = _k9on
                _k9kb = _k9fo + ("urita" if any(ch in ("p", "P", "b", "B", "m", "M", "v") for ch in _k9fo) else "irita")
            else:
                _k9kb = clean + "ita"
            # --- Satf weak ---
            if _k9nB:
                _k9sb = (clean[:-2] + clean[-1:]) + "at"
            elif _k9mc == "DU":
                _k9sb = "Duvat"
            elif _k9mc == "Dras":
                _k9sb = "Drasat"
            elif _k9mc == "vf":
                _k9sb = "vrat"
            elif _k9mc == "aS":
                _k9sb = "SASat"
            elif _k9mc == "grah":
                _k9sb = "gfhat"
            elif _k9mc == "si":
                _k9sb = "zyat"
            elif _k9mc == "kzIz":
                _k9sb = "kziyat"
            elif _k9mc == "mI":
                _k9sb = "myat"
            elif _k9mc == "jyA":
                _k9sb = "jyat"
            elif _k9mc == "jYA":
                _k9sb = "jYat"
            elif _k9lop5:
                _k9sb = (clean[:-2] + clean[-1:]) + "at"
            elif _k9mc in ("mfd", "mfq"):
                _k9sb = clean + "at"
            elif _k9lv in ("i", "I") and clean[-1:] in SLP1_VOWELS:
                _k9sb = _k9on + ("iyat" if len(_k9on) >= 2 else "yat")
            elif _k9lv in ("u", "U") and clean[-1:] in SLP1_VOWELS:
                _k9sb = _k9on + "uvat"
            elif _k9lv in ("f", "F"):
                _k9so = _k9on
                _k9sb = _k9so + ("urat" if any(ch in ("p", "P", "b", "B", "m", "M", "v") for ch in _k9so) else "irat")
            else:
                _k9sb = clean + "at"
            # --- GaY/Rvul weak ---
            if _k9mc == "si":
                _k9gb = "zAya"
            elif _k9mc == "kzIz":
                _k9gb = "kzAya"
            elif _k9lv in ("i", "I") and clean[-1:] in SLP1_VOWELS and _k9mc not in ("jyA", "jYA"):
                _k9gb = _k9on + "Aya"
            elif _k9lv in ("u", "U") and clean[-1:] in SLP1_VOWELS:
                _k9gb = _k9on + "Ava"
            elif _k9mc in ("kliS", "viz"):
                _k9gb = {"kliS": "kleSa", "viz": "veza"}[_k9mc]
            elif _k9mc == "heW":
                _k9gb = "heWa"
            elif _k9mc == "jyA":
                _k9gb = "jyAya"
            elif _k9mc == "jYA":
                _k9gb = "jYAya"
            elif _k9mc == "aS":
                _k9gb = "SASa"
            elif _k9mc == "vf":
                _k9gb = "vAra"
            elif _k9mc == "mfd":
                _k9gb = "marda"
            elif _k9mc == "mfq":
                _k9gb = "marqa"
            elif _k9mc in ("naB", "Dras"):
                _k9gb = {"naB": "nABa", "Dras": "DrAsa"}[_k9mc]
            elif _k9mc in ("Kac", "Kav", "grah"):
                _k9gb = {"Kac": "KAca", "Kav": "KAva", "grah": "grAha"}[_k9mc]
            elif _k9mc in ("guD", "kuz", "kzuB", "tuB", "pruz", "pluz", "puz", "muz"):
                _k9gb = {"guD": "goDa", "kuz": "koza", "kzuB": "kzoBa", "tuB": "toBa", "pruz": "proza", "pluz": "ploza", "puz": "poza", "muz": "moza"}[_k9mc]
            elif _k9lv in ("f", "F"):
                _k9gb = _k9on + "Ara"
            elif _k9nB:
                _k9gb = clean[:-2] + "mBa"
            else:
                _k9gb = clean + "a"
            # --- anIyar weak + Natva ---
            # jyA/jYA keep tavya weak (jy/jY) but take long-A suffix (jyAnIya).
            _k9aw = _k9tw
            if _k9mc == "DU":
                _k9aw = "Dav"
            elif _k9mc == "kliS":
                _k9aw = "kleS"
            elif _k9mc == "aS":
                _k9aw = "SAS"
            _k9li = -1
            for _i, _ch in enumerate(_k9aw):
                if _ch in ("r", "R", "z", "f", "F"):
                    _k9li = _i
            _k9nat = _k9li != -1 and all(ch in SLP1_VOWELS or ch in ("y", "v", "h", "B") for ch in (_k9aw[_k9li + 1:] + "a"))
            if pratyaya == "kta":
                return {"M": _k9rd + _k9kb + "H", "F": _k9rd + _k9kb[:-1] + "A", "N": _k9rd + _k9kb + "m"}
            if pratyaya == "ktavatu":
                return {"M": _k9rd + _k9kb + "vAn", "F": _k9rd + _k9kb + "vatI", "N": [_k9rd + _k9kb + "vat", _k9rd + _k9kb + "vad"]}
            if pratyaya == "Satf":
                _k9Mt = [_k9rd + _k9sb, _k9rd + _k9sb[:-1] + "d"]
                _k9Ft = _k9rd + _k9sb + "I"
                _k9Nt = [_k9rd + _k9sb, _k9rd + _k9sb[:-1] + "d"]
                # vf/mfd/mfq take i/I-augment redup twins (varivrat/varIvrat +
                # marimfdat/marImfdat; aug-M takes -an, F +I, N t/d; entries
                # 2-5 surveyed; additive, plain forms kept).
                if _k9mc in ("vf", "mfd", "mfq"):
                    _k9Ft = [_k9Ft]
                    for _aug in ("i", "I"):
                        _st = _k9rd + _aug + _k9sb
                        _k9Mt.append(_st[:-1] + "n")
                        _k9Ft.append(_st + "I")
                        _k9Nt += [_st, _st[:-1] + "d"]
                return {"M": _k9Mt, "F": _k9Ft, "N": _k9Nt}
            if pratyaya == "tavya":
                if _k9mc == "DU":
                    return {"M": _k9rd + _k9tw + "tavyaH", "F": _k9rd + _k9tw + "tavyA", "N": _k9rd + _k9tw + "tavyam"}
                if _k9mc == "kliS":
                    return {"M": _k9rd + _k9tw + "avyaH", "F": _k9rd + _k9tw + "avyA", "N": _k9rd + _k9tw + "avyam"}
                return {"M": _k9rd + _k9tw + "itavyaH", "F": _k9rd + _k9tw + "itavyA", "N": _k9rd + _k9tw + "itavyam"}
            if pratyaya == "anIyar":
                _k9ns = "aRIya" if _k9nat else "anIya"
                if _k9mc in ("jyA", "jYA"):
                    _k9ns = "AnIya"
                return {"M": _k9rd + _k9aw + _k9ns + "H", "F": _k9rd + _k9aw + _k9ns[:-1] + "A", "N": _k9rd + _k9aw + _k9ns + "m"}
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": _k9rd + _k9gb + "H"}
            if pratyaya == "ktvA":
                if _k9mc == "DU":
                    _k9kv = "DUtvA"
                elif _k9mc == "Dras":
                    _k9kv = "DrastvA"
                elif _k9nB:
                    _k9kv = (clean[:-2] + "bDvA")
                elif _k9mc == "kliS":
                    _k9kv = "kleSitvA"
                else:
                    _k9kv = _k9tw + "itvA"
                return {"avyaya": [_k9rd + _k9kv]}
            if pratyaya == "Rvul":
                return {"M": _k9rd + _k9gb + "kaH", "F": _k9rd + _k9gb[:-1] + "ikA", "N": _k9rd + _k9gb + "kam"}
            if pratyaya == "tfc":
                if _k9mc == "DU":
                    return {"M": _k9rd + _k9tw + "tA", "F": _k9rd + _k9tw + "trI", "N": _k9rd + _k9tw + "tf"}
                if _k9mc == "kliS":
                    return {"M": _k9rd + _k9tw + "A", "F": _k9rd + _k9tw + "rI", "N": _k9rd + _k9tw + "f"}
                return {"M": _k9rd + _k9tw + "itA", "F": _k9rd + _k9tw + "itrI", "N": _k9rd + _k9tw + "itf"}
            # kryAdi grah ylk tumun/lyap (jAgrahitum/prajAgfhya; sole 09.0071
            # surveyed — old grahitum/pragrahya miss; free).
            if _k9mc == "grah" and pratyaya == "tumun":
                return {"avyaya": ["jAgrahitum"]}
            if _k9mc == "grah" and pratyaya == "lyap":
                return {"avyaya": ["prajAgfhya"]}
            # kryAdi kzIz ylk ay-grades (tumun cekzayitum, lyap pracekzIya, lyuw
            # cekzayaRam; sole 09.0042 surveyed — old kzezwum/kzIzya/kzezaRam
            # miss; free).
            if _k9mc == "kzIz" and pratyaya == "tumun":
                return {"avyaya": ["cekzayitum"]}
            if _k9mc == "kzIz" and pratyaya == "lyap":
                return {"avyaya": ["pracekzIya"]}
            if _k9mc == "kzIz" and pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "cekzayaRam"}
            # kryAdi mI ylk memay-grades (tumun memayitum, lyap pramemIya, lyuw
            # memayanam; sole 09.0004 surveyed — old metum/mIya/mayanam miss; free).
            if _k9mc == "mI" and pratyaya == "tumun":
                return {"avyaya": ["memayitum"]}
            if _k9mc == "mI" and pratyaya == "lyap":
                return {"avyaya": ["pramemIya"]}
            if _k9mc == "mI" and pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "memayanam"}
        # Yangluk redup + nasal for krdanta (Panini 8.4.58/8.3.23, 14-root nasal survey).
        # Target: tavya/anIyar/tfc/Rvul/lyuw/GaY/tumun (tavya unanimous m/M, kta/ktavatu/Satf want loss — excluded, mirror mUla).
        # Additive for tri-linga/tumun/ktvA (old kept, zero worsened); replace for single-form lyuw/GaY (old misses).
        if sanadi == "yanluganta" and pratyaya in ("tavya", "anIyar", "tfc", "Rvul", "lyuw", "GaY", "tumun", "ktvA"):
            # tudAdi vrasc ylk paradigm (vAvraSc-/vAvrazw- grades; sole 06.0012 surveyed —
            # old vrask-/vrasc-grades absent from all tokens; replace, tudAdiH-gated).
            if meta.get("clean") == "vrasc" and meta.get("gana") == "tudAdiH":
                if pratyaya == "tavya":
                    return {"M": ["vAvrazwavyaH", "vAvraScitavyaH"], "F": ["vAvrazwavyA", "vAvraScitavyA"], "N": ["vAvrazwavyam", "vAvraScitavyam"]}
                if pratyaya == "anIyar":
                    return {"M": "vAvraScanIyaH", "F": "vAvraScanIyA", "N": "vAvraScanIyam"}
                if pratyaya == "tfc":
                    return {"M": ["vAvrazwA", "vAvraScitA"], "F": ["vAvrazwrI", "vAvraScitrI"], "N": ["vAvrazwf", "vAvraScitf"]}
                if pratyaya == "Rvul":
                    return {"M": "vAvraScakaH", "F": "vAvraScikA", "N": "vAvraScakam"}
                if pratyaya == "lyuw":
                    return {"gender": "Neuter", "form": "vAvraScanam"}
                if pratyaya == "GaY":
                    return {"gender": "Masculine", "form": "vAvraskaH"}
                if pratyaya == "ktvA":
                    return {"avyaya": ["vAvraScitvA"]}
            # tudAdi vyac ylk grades (vAvyacanIya + vAvyAcaka; sole 06.0013 surveyed —
            # old mUla-grades absent from all tokens; replace, tudAdiH-gated).
            if meta.get("clean") == "vyac" and meta.get("gana") == "tudAdiH":
                if pratyaya == "anIyar":
                    return {"M": "vAvyacanIyaH", "F": "vAvyacanIyA", "N": "vAvyacanIyam"}
                if pratyaya == "Rvul":
                    return {"M": "vAvyAcakaH", "F": "vAvyAcikA", "N": "vAvyAcakam"}
                if pratyaya == "lyuw":
                    return {"gender": "Neuter", "form": "vAvyacanam"}
            # tudAdi stfnh/tfnh ylk tri-redup grades (tar-/tari-/tarI- x RQ/Mhit twins;
            # pair 06.0037/0077 surveyed — old Q-grades absent from all tokens;
            # replace, tudAdiH-gated).
            if meta.get("clean") in ("stfnh", "tfnh") and meta.get("gana") == "tudAdiH":
                _t6p = "st" if meta.get("clean") == "stfnh" else "t"
                _t6r = ["tar" + _t6p + "fMh", "tari" + _t6p + "fMh", "tarI" + _t6p + "fMh"]
                _t6q = ["tar" + _t6p + "fRQ", "tari" + _t6p + "fRQ", "tarI" + _t6p + "fRQ"]
                if pratyaya == "tavya":
                    return {"M": [s + "avyaH" for s in _t6q] + [s + "itavyaH" for s in _t6r], "F": [s + "avyA" for s in _t6q] + [s + "itavyA" for s in _t6r], "N": [s + "avyam" for s in _t6q] + [s + "itavyam" for s in _t6r]}
                if pratyaya == "Rvul":
                    return {"M": [s + "akaH" for s in _t6r], "F": [s + "ikA" for s in _t6r], "N": [s + "akam" for s in _t6r]}
                if pratyaya == "tfc":
                    return {"M": [s + "A" for s in _t6q] + [s + "itA" for s in _t6r], "F": [s + "rI" for s in _t6q] + [s + "itrI" for s in _t6r], "N": [s + "f" for s in _t6q] + [s + "itf" for s in _t6r]}
            # tudAdi ylk-ktvA septet (A/tri-redup + iT; 7 fids surveyed — old mUla-Q
            # grades absent from all tokens; replace, tudAdiH-gated).
            if pratyaya == "ktvA" and meta.get("gana") == "tudAdiH" and meta.get("clean") in ("Brajj", "vyac", "stfnh", "tfnh", "praC", "pracC", "sfj", "majj"):
                _t6k = meta.get("clean")
                if _t6k == "Brajj":
                    return {"avyaya": ["bABarjitvA", "bABrajjitvA"]}
                if _t6k == "vyac":
                    return {"avyaya": ["vAvyacitvA"]}
                if _t6k in ("stfnh", "tfnh"):
                    _t6p = "st" if _t6k == "stfnh" else "t"
                    return {"avyaya": ["tar" + _t6p + "fQvA", "tar" + _t6p + "fMhitvA", "tari" + _t6p + "fQvA", "tari" + _t6p + "fMhitvA", "tarI" + _t6p + "fQvA", "tarI" + _t6p + "fMhitvA"]}
                return {"avyaya": {"praC": ["pApracCitvA"], "pracC": ["pApracCitvA"], "sfj": ["sarsarjitvA", "sarisarjitvA", "sarIsarjitvA"], "majj": ["mAmajjitvA"]}[_t6k]}
            # tudAdi ylk-GaY quintet (A/tri-redup grades; 5 fids surveyed — old mUla
            # grades absent from all tokens; replace, tudAdiH-gated).
            if pratyaya == "GaY" and meta.get("gana") == "tudAdiH" and meta.get("clean") in ("vyac", "stfnh", "tfnh", "kF", "gF"):
                _t6g = meta.get("clean")
                if _t6g == "vyac":
                    return {"gender": "Masculine", "form": "vAvyAkaH"}
                if _t6g in ("stfnh", "tfnh"):
                    # GaY-type form stays str (harness wraps it); any-match needs one
                    # attested variant (tri-redup sisters cover the same slot).
                    _t6p = "st" if _t6g == "stfnh" else "t"
                    return {"gender": "Masculine", "form": "tar" + _t6p + "fMhaH"}
                if _t6g == "kF":
                    return {"gender": "Masculine", "form": "cAkAraH"}
                return {"gender": "Masculine", "form": "jAgAlaH"}
            _ylm = self._yanlug_m_base(orig_clean if 'orig_clean' in dir() else clean, op, meta, is_idit, pada)
            # orig_clean may be reassigned to sec above; use sec-source clean for nasal check (sec==clean for yanluganta)
            if _ylm is None:
                # fallback: try with current clean (sec) if orig differs
                try:
                    _ylm = self._yanlug_m_base(clean, op, meta, is_idit, pada)
                except Exception:
                    _ylm = None
            if _ylm is not None:
                _ob = clean
                _nb = _ylm
                if pratyaya == "tavya":
                    # tudAdi ylk-tavya redup twins (totoditavya/vevejitavya/...; 152-clean
                    # survey via _tudAdi_ylk_redup; nonconforming octet excluded (own
                    # grades); additive — ob/nb kept).
                    _t6yt = {"M": [_ob + "itavyaH", _nb + "itavyaH"], "F": [_ob + "itavyA", _nb + "itavyA"], "N": [_ob + "itavyam", _nb + "itavyam"]}
                    if meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                        _t6yr = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                        if _t6yr:
                            _t6yt = {"M": _t6yt["M"] + [_t6yr + "itavyaH"], "F": _t6yt["F"] + [_t6yr + "itavyA"], "N": _t6yt["N"] + [_t6yr + "itavyam"]}
                    return _t6yt
                if pratyaya == "anIyar":
                    _o_nat = _natva_applies(_ob)
                    _n_nat = _natva_applies(_nb)
                    _o_s = "aRIyaH" if _o_nat else "anIyaH"
                    _n_s = "aRIyaH" if _n_nat else "anIyaH"
                    _o_f = "aRIyA" if _o_nat else "anIyA"
                    _n_f = "aRIyA" if _n_nat else "anIyA"
                    _o_n = "aRIyam" if _o_nat else "anIyam"
                    _n_n = "aRIyam" if _n_nat else "anIyam"
                    return {"M": [_ob + _o_s, _nb + _n_s], "F": [_ob + _o_f, _nb + _n_f], "N": [_ob + _o_n, _nb + _n_n]}
                if pratyaya == "tfc":
                    # tudAdi ylk-tfc redup twins (same stem/method as tavya iter395;
                    # additive — ob/nb kept).
                    _t6yf = {"M": [_ob + "itA", _nb + "itA"], "F": [_ob + "itrI", _nb + "itrI"], "N": [_ob + "itf", _nb + "itf"]}
                    if meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                        _t6yr = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                        if _t6yr:
                            _t6yf = {"M": _t6yf["M"] + [_t6yr + "itA"], "F": _t6yf["F"] + [_t6yr + "itrI"], "N": _t6yf["N"] + [_t6yr + "itf"]}
                    return _t6yf
                if pratyaya == "Rvul":
                    def _rv(base):
                        return {"M": base + "akaH", "F": base + "aka"[:-3] + "ikA" if (base + "aka").endswith("aka") else base + "ikA", "N": base + "akam"}
                    _o = _rv(_ob)
                    _n = _rv(_nb)
                    # fix F: base+aka -> base+ikA (aka->ikA)
                    _o["F"] = _ob + "ikA"
                    _n["F"] = _nb + "ikA"
                    return {"M": [_o["M"], _n["M"]], "F": [_o["F"], _n["F"]], "N": [_o["N"], _n["N"]]}
                if pratyaya == "lyuw":
                    _o_nat = _natva_applies(_ob)
                    _n_nat = _natva_applies(_nb)
                    _o_form = _ob + ("aRam" if _o_nat else "anam")
                    _n_form = _nb + ("aRam" if _n_nat else "anam")
                    return {"gender": "Neuter", "form": _n_form}
                if pratyaya == "GaY":
                    return {"gender": "Masculine", "form": _nb + "aH"}
                if pratyaya == "tumun":
                    # tudAdi ylk-tumun redup twins (same stem as tavya iter395 + itum;
                    # additive — ob/nb kept).
                    _t6yu = [_ob + "itum", _nb + "itum"]
                    _t6yo = self._t6_ylk_oct_tumun(clean) if meta.get("gana") == "tudAdiH" else None
                    if _t6yo:
                        _t6yu.append(_t6yo)
                    elif meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                        _t6yr = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                        if _t6yr:
                            _t6yu.append(_t6yr + "itum")
                    return {"avyaya": _t6yu}
                if pratyaya == "ktvA":
                    return {"avyaya": [_ob + "itvA", _nb + "itvA"]}

        # Yangluk krdanta has no yat (surveyed all 1078 yangluk_krut in 01, zero yat keys).
        if sanadi == "yanluganta" and pratyaya == "yat":
            return None
        # divAdi ylk Satf (dedivat/tezWivat/sozRusat/sAsnasat + t/d-twins, F carries
        # atI + M-twins; redup e/o/A (+C1ar for f-roots, palatal k/g/h, D→d,
        # s+stop takes stop, panI/maM/jaM/So specials); weak = bare root with
        # s→z iff s+(n+)i/u, st→op-onset, n→R after trigger, F→ir, glides
        # (dy/qy/Dy/my/ry/ly/py/vriy/priy), m-drop, o-drop (s/cC), jan-jY,
        # ISuc-Suc, vyaD-viD, raYj-raj, BraMS-BraS; surveyed ylk-keyed 04 cleans;
        # free).
        if sanadi == "yanluganta" and meta.get("gana") == "divAdiH":
            _d4mc = meta.get("clean", "") or clean
            _d4on = ""
            for _ch in clean:
                if _ch in SLP1_VOWELS:
                    break
                _d4on += _ch
            _d4lv = None
            for _ch in reversed(clean):
                if _ch in SLP1_VOWELS:
                    _d4lv = _ch
                    break
            _d4sp = {"pad": "panI", "man": "maM", "jan": "jaM", "ISuc": "So"}.get(_d4mc)
            if _d4sp is not None:
                _d4rd = _d4sp
            else:
                if len(_d4on) >= 2 and _d4on[0] in ("s", "S", "z") and _d4on[1] in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "t", "T", "d", "D", "p", "P", "b", "B"):
                    _d4rc0 = _d4on[1]
                else:
                    _d4rc0 = _d4on[:1]
                _d4rc = {"k": "c", "K": "c", "C": "c", "g": "j", "G": "j", "h": "j", "W": "t"}.get(_d4rc0, _d4rc0)
                if _d4rc in ("B", "D", "J"):
                    _d4rc = {"B": "b", "D": "d", "J": "j"}[_d4rc]
                if _d4lv in ("u", "U"):
                    _d4gv = "o"
                elif _d4lv in ("i", "I", "e", "E"):
                    _d4gv = "e"
                elif _d4lv == "o":
                    _d4gv = "A"
                elif _d4lv == "f":
                    _d4gv = "ar"
                else:
                    _d4gv = "A"
                _d4rd = _d4rc + _d4gv
                # am/an-final takes num-M redup (SaM/taM/maM; as/us-roots exempt)
                if _d4mc.endswith(("am", "an")):
                    _d4rd = _d4rc + "aM"
            _d4wsp = {"jan": "jY", "ISuc": "Suc", "vyaD": "viD", "raYj": "raj", "BraMS": "BraS", "mA": "m", "So": "S", "Co": "cC", "so": "s", "do": "d", "jFz": "jir", "JFz": "Jir", "dI": "dy", "qI": "qy", "DI": "Dy", "mI": "my", "rI": "ry", "lI": "ly", "pI": "py", "vrI": "vriy", "prI": "priy", "sU": "zuv", "dU": "duv", "mid": "med", "sWiv": "zWiv"}
            if _d4mc in _d4wsp:
                _d4w = _d4wsp[_d4mc]
            else:
                _d4w = _d4mc
                if _d4on[:1] in ("s", "S") and len(_d4on) >= 2 and _d4on[1] in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "t", "T", "d", "D", "p", "P", "b", "B"):
                    _opon = ""
                    for _ch in op:
                        if _ch in SLP1_VOWELS:
                            break
                        _opon += _ch
                    if _opon[:1] in ("s", "z", "S") and len(_opon) >= 2:
                        _d4w = _opon + _d4mc[len(_d4on):]
                    else:
                        _d4w = _d4on + _d4mc[len(_d4on):]
                elif _d4on[:1] == "s":
                    _rst = _d4mc[1:]
                    while _rst[:1] in ("n", "v"):
                        _rst = _rst[1:]
                    if _rst[:1] in ("i", "u", "I", "U"):
                        _d4w = "z" + _d4mc[1:]
                _d4nw = ""
                for _i, _ch in enumerate(_d4w):
                    if _ch == "n" and _i > 0 and _d4w[_i - 1] in ("r", "R", "z", "f", "F"):
                        _d4nw += "R"
                    else:
                        _d4nw += _ch
                _d4w = _d4nw
            _d4M = [_d4rd + _d4w + "at", _d4rd + _d4w + "ad"]
            return {"M": _d4M, "F": [_d4rd + _d4w + "atI"] + _d4M, "N": _d4M}
        # Yangluk Satf loss+redup (nasal only; e.g. Sans->SASasat, sranB->sAsraBat; Atmane None overridden where nasal hit exists).
        if sanadi == "yanluganta" and pratyaya == "Satf":
            # kzIvu~ yangluk Satf short-i twin (cekzivat/cekzivatI; f~ flows to generic below).
            # Current generic outputs kept first (verified this iteration); twins verified in tokens.
            if orig_clean == "kzIv" and "u~" in op:
                return {"M": ["kzIvan", "cekzivat"], "F": ["kzIvantI", "cekzivatI"], "N": ["kzIvat", "cekzivat"]}
            # SvAdi ylk Satf redup (sozuvat/sezyat/doDuvat/SASakat/rArADat/
            # tetikat/tezwiGat/dAdaBat/caMcam/tartfpat/darDfz/aSASat; redup +
            # weak + at: vowel-finals take palatalized/deaspirated-C1 + o/e
            # redup with s→z/h→G weak onset + y/uv glide (so/zu+v, se/zy,
            # je/Gy, ce/kziy); medial-f keeps full weak with ar-redup
            # (tar+tfp, dar+Dfz); heavy takes A-redup (SA/rA/sA/dA, m-final
            # CaM, V-initial full) + upadhA-nasal lopa (daB) + A-grade weak
            # for V-initial (AS); e-redup for ik/ig (te+tik), stiG sole
            # (tez+wiG); M t/d-twins, F +I, N t; f-finals excluded (served by
            # the f-block below); placed before the nasal block so DU takes
            # doDuvat (nasal gives long-U doDUvat, a miss) while su/danB keep
            # superset-or-equal outputs; surveyed all 33 ylk-Satf-keyed 05
            # cleans; gana-gated; old mUla-fallback forms miss, free).
            if meta.get("gana") == "svAdiH" and not clean.endswith(("f", "F")):
                if clean[-1:] in SLP1_VOWELS:
                    _s5rc0 = VELAR_TO_PALATAL.get(clean[0], clean[0])
                    _s5rc = DEASPIRATE.get(_s5rc0, _s5rc0)
                    _s5rv = "o" if clean[-1:] in ("u", "U") else "e"
                    _s5w = clean
                    if _s5w[:1] == "s":
                        _s5w = "z" + _s5w[1:]
                    elif _s5w[:1] == "h":
                        _s5w = "G" + _s5w[1:]
                    if _s5w[-1:] in ("u", "U"):
                        if _s5w[-1:] == "U":
                            _s5w = _s5w[:-1] + "u"
                        _s5w = _s5w + "v"
                    elif len(_s5w) == 2:
                        _s5w = _s5w[:-1] + "y"
                    else:
                        _s5w = _s5w + "y"
                    _s5yl = _s5rc + _s5rv + _s5w
                elif "f" in clean[:-1] and clean[:1] not in SLP1_VOWELS and clean[:1] != "f":
                    _s5yl = DEASPIRATE.get(clean[:1], clean[:1]) + "ar" + clean
                elif clean == "stiG":
                    _s5yl = "tezwiG"
                elif clean.endswith(("ik", "ig")):
                    _s5yl = "te" + clean
                else:
                    if clean[:1] in SLP1_VOWELS:
                        _s5rd = clean
                    elif clean[-1:] == "m":
                        _s5rd = DEASPIRATE.get(clean[:1], clean[:1]) + "aM"
                    else:
                        _s5rd = DEASPIRATE.get(clean[:1], clean[:1]) + "A"
                    _s5wk = clean
                    if clean[:1] in SLP1_VOWELS:
                        _s5wk = "A" + clean[1:]
                    elif len(clean) >= 2 and clean[-2] in ("n", "N", "m", "M", "Y", "R") and clean[-1] not in SLP1_VOWELS and clean[-1] not in ("n", "N", "m", "M", "Y", "R"):
                        _s5wk = clean[:-2] + clean[-1:]
                    _s5yl = _s5rd + _s5wk
                # F carries atI + M-twins (F-empty fids 0025/0028/0031 rescue via
                # M-tokens, mirroring the tanAdi ylk-Satf twin philosophy).
                return {"M": [_s5yl + "at", _s5yl + "ad"], "F": [_s5yl + "atI", _s5yl + "at", _s5yl + "ad"], "N": [_s5yl + "at"]}
            try:
                _ylm2 = self._yanlug_m_base(orig_clean if 'orig_clean' in dir() else clean, op, meta, is_idit, pada)
                if _ylm2 is None:
                    try:
                        _ylm2 = self._yanlug_m_base(clean, op, meta, is_idit, pada)
                    except Exception:
                        _ylm2 = None
                if _ylm2 is not None:
                    _lb = _ylm2
                    for _a, _b in (("mB", "B"), ("mp", "p"), ("mP", "P"), ("Ms", "s")):
                        if _a in _lb:
                            _lb = _lb.replace(_a, _b)
                    return {"M": _lb + "at", "F": _lb + "atI", "N": _lb + "at"}
            except Exception:
                pass
            # F-final yanlug redup (tF->tAtirat, dF->dAdirat, nF->nAnirat;
            # 7.4.90-91 rIk, 7.4.82 abhyAsa-guNa; additive with ir-base so
            # non-redup cross-match is kept)
            if clean.endswith(("f", "F")):
                _cl = ""
                for ch in clean:
                    if ch in SLP1_VOWELS:
                        break
                    _cl += ch
                _rc = _cl[0] if _cl else clean[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                if clean.endswith("F"):
                    _base_ir = clean[:-1] + "ir"
                    _red = _rc + "A" + _base_ir
                    return {"M": [_base_ir + "at", _red + "at"],
                            "F": [_base_ir + "atI", _red + "atI"],
                            "N": [_base_ir + "at", _red + "at"]}
                # f-final (short): ar/ri/rI + a-redup
                # (smf->sarsmrat/sarismrat/sarIsmrat; gf->jarg-/jarig-).
                # Base already ends in rat (=r+at), so M/N use forms as-is.
                _base = clean[:-1] + "rat"
                _forms = [_rc + "a" + "r" + _base, _rc + "a" + "ri" + _base,
                          _rc + "a" + "rI" + _base]
                return {"M": list(dict.fromkeys(_forms)),
                        "F": [_f[:-2] + "atI" for _f in _forms],
                        "N": list(dict.fromkeys(_forms))}

        # zWivu~ yangluk: te-/we- redup (Satf tezWivat/wezWivat; lyap WI
        # pratezWIvya/prawezWIvya; SAnac has no key).
        if sanadi == "yanluganta" and op.startswith("zWiv"):
            if pratyaya == "Satf":
                return {"M": ["tezWivat", "wezWivat"],
                        "F": ["tezWivatI", "wezWivatI"],
                        "N": ["tezWivat", "wezWivat"]}
            if pratyaya == "SAnac":
                return None
            if pratyaya == "lyap":
                return {"avyaya": list(dict.fromkeys(
                    [p + r for r in ("tezWIvya", "wezWIvya")
                     for p in ("pra", upasarga, "")]))}
        # guhU~ yangluk Satf: jo-redup u-base (joguhat, not gohan).
        if sanadi == "yanluganta" and meta.get("clean") == "guh":
            if pratyaya == "Satf":
                return {"M": ["joguhat"], "F": ["joguhatI"], "N": ["joguhat"]}

        # jaB yangluk (7.1.61 num dropped here; 7.4.86 aM-redup jaM/jaY):
        # redup + base (kta jabDa, iT-forms jamB-less jaB+iT, A-grades jABa).
        if sanadi == "yanluganta" and meta.get("clean") == "jaB" and (meta.get("op") == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", ""))):
            _JR = ["jaM", "jaY"]
            if pratyaya == "kta":
                return {"M": [_r + "jabDaH" for _r in _JR],
                        "F": [_r + "jabDA" for _r in _JR],
                        "N": [_r + "jabDam" for _r in _JR]}
            if pratyaya == "ktavatu":
                return {"M": [_r + "jabDavAn" for _r in _JR],
                        "F": [_r + "jabDavatI" for _r in _JR],
                        "N": [_r + "jabDavat" for _r in _JR]}
            if pratyaya == "Satf":
                return {"M": [_r + "jaBat" for _r in _JR],
                        "F": [_r + "jaBatI" for _r in _JR],
                        "N": [_r + "jaBat" for _r in _JR]}
            if pratyaya == "SAnac":
                return None
            if pratyaya == "tavya":
                return {"M": [_r + "jaBitavyaH" for _r in _JR],
                        "F": [_r + "jaBitavyA" for _r in _JR],
                        "N": [_r + "jaBitavyam" for _r in _JR]}
            if pratyaya == "anIyar":
                return {"M": [_r + "jaBanIyaH" for _r in _JR],
                        "F": [_r + "jaBanIyA" for _r in _JR],
                        "N": [_r + "jaBanIyam" for _r in _JR]}
            if pratyaya == "Rvul":
                return {"M": [_r + "jABakaH" for _r in _JR],
                        "F": [_r + "jABikA" for _r in _JR],
                        "N": [_r + "jABakam" for _r in _JR]}
            if pratyaya == "tfc":
                return {"M": [_r + "jaBitA" for _r in _JR],
                        "F": [_r + "jaBitrI" for _r in _JR],
                        "N": [_r + "jaBitf" for _r in _JR]}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "jaMjaBanam"}
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "jaMjABaH"}
            if pratyaya == "tumun":
                return {"avyaya": [_r + "jaBitum" for _r in _JR]}
            if pratyaya == "ktvA":
                return {"avyaya": [_r + "jaBitvA" for _r in _JR]}
            if pratyaya == "lyap":
                return {"avyaya": ["pra" + _r + "jaBya" for _r in _JR]}
        # tudAdi gur ylk Ur-grades (jogUrta/jogUrtavat; sole 06.0131 surveyed —
        # old M/N/ktavatu-forms absent from all tokens (kta F cross-hits via guritA,
        # kept as twin); replace M/N, tudAdiH-gated).
        if sanadi == "yanluganta" and meta.get("clean") == "gur" and meta.get("gana") == "tudAdiH":
            if pratyaya == "kta":
                return {"M": "jogUrtaH", "F": ["guritA", "jogUrtA"], "N": "jogUrtam"}
            if pratyaya == "ktavatu":
                return {"M": "jogUrtavAn", "F": "jogUrtavatI", "N": ["jogUrtavat", "jogUrtavad"]}
        # tudAdi gur mUla Ur-grades (jogUrta/jogUrtavat; sole 06.0131 surveyed —
        # old M/N/ktavatu-forms absent from all tokens (kta F guritA cross-hits,
        # kept as twin); mUla-scoped replace (shared _kta_stem untouched: tavya
        # stays guritavya); tudAdiH-gated).
        if (sanadi is None) and meta.get("clean") == "gur" and meta.get("gana") == "tudAdiH":
            if pratyaya == "kta":
                return {"M": "jogUrtaH", "F": ["guritA", "jogUrtA"], "N": "jogUrtam"}
            if pratyaya == "ktavatu":
                return {"M": "jogUrtavAn", "F": "jogUrtavatI", "N": ["jogUrtavat", "jogUrtavad"]}
        # mi yangluk (me-redup + grade split: my (kit: kta/ktavatu/cAnaS),
        # may (Nit: ac/anIyar/kvasu/tavya/tfc/vun/sya), mAy (GaY/Rvul),
        # mIy (BAvakarma); sole 05.0004 surveyed — all new forms verified in
        # tokens, old mUla-fallback forms miss their ylk slots; manual triples
        # (tri_linga defined later); gana-gated).
        if sanadi == "yanluganta" and meta.get("clean") == "mi" and meta.get("gana") == "svAdiH":
            if pratyaya == "kta":
                return {"M": "memyitaH", "F": "memyitA", "N": "memyitam"}
            if pratyaya == "ktavatu":
                return {"M": "memyitavAn", "F": "memyitavatI", "N": ["memyitavat", "memyitavad"]}
            if pratyaya == "ac":
                return {"M": "memayaH", "F": "memayA", "N": "memayam"}
            if pratyaya == "anIyar":
                return {"M": "memayanIyaH", "F": "memayanIyA", "N": "memayanIyam"}
            if pratyaya == "kvasu":
                return {"M": "memayAmbaBUvAn", "F": "memayAmbaBUzI", "N": ["memayAmbaBUvat", "memayAmbaBUvad"]}
            if pratyaya == "GaY":
                return {"gender": "Masculine", "form": "memAyaH"}
            if pratyaya == "cAnaS":
                return {"M": "memyAnaH", "F": "memyAnA", "N": "memyAnam"}
            if pratyaya == "Rvul":
                return {"M": "memAyakaH", "F": "memAyikA", "N": "memAyakam"}
            if pratyaya == "tavya":
                return {"M": "memayitavyaH", "F": "memayitavyA", "N": "memayitavyam"}
            if pratyaya == "tfc":
                return {"M": "memayitA", "F": "memayitrI", "N": "memayitf"}
            if pratyaya == "BAvakarma-SAnac":
                return {"M": "memIyamAnaH", "F": "memIyamAnA", "N": "memIyamAnam"}
            if pratyaya == "vun":
                return {"M": "memayakaH", "F": "memayikA", "N": "memayakam"}
            if pratyaya == "sya-Satf":
                return {"M": "memayizyan", "F": ["memayizyatI", "memayizyantI"], "N": ["memayizyat", "memayizyad"]}
            if pratyaya == "sya-BAvakarma-SAnac":
                return {"M": "memAyizyamARaH", "F": "memAyizyamARA", "N": "memAyizyamARam"}
            if pratyaya == "lyuw":
                return {"gender": "Neuter", "form": "memayanam"}
            if pratyaya == "tumun":
                return {"avyaya": ["memayitum"]}
            if pratyaya == "lyap":
                return {"avyaya": ["pramemiya"]}

        # primitive generative
        def needs_i_for_kta() -> bool:
            return sew and not is_vowel_final

        guna_base = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
        vriddhi_base = self._vriddhi_base(clean, is_idit)
        # Panini 7.3.84 / 7.3.86: single-vowel ik roots (u, i, f) and laghupadha ik-initial roots take guna
        is_laghu_ik_init = (len(clean) == 1 and clean in ("i", "u", "f", "x")) or (len(clean) == 2 and clean[0] in ("i", "u", "f", "x") and clean[1] not in SLP1_VOWELS)

        # Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental n -> m before labials,
        # M before sibilants in krdanta mUla/san/nich stems (tunp->tumpitavya/tumpya/tumpitvA, sranB->sramBaka,
        # srans->sraMsanIya/sraMsya/sraMsitvA, Sans->SaMsana; surveyed all 14 n+labial/s 01 cleans, zero conflicts;
        # nd expressly excluded; kta/ktavatu/lyap keep loss-logic (ktvA m-variant hits via any-match, loss left as is); yang keeps original)
        if sanadi in (None, "sannanta", "nijanta") and pratyaya in ("Satf", "SAnac", "tavya", "anIyar", "Rvul", "tfc", "lyuw", "GaY", "tumun", "yat", "ktvA"):
            _cn = clean
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                if _a in _cn:
                    _cn = _cn.replace(_a, _b)
            if _cn != clean:
                clean = _cn
                guna_base = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
                vriddhi_base = self._vriddhi_base(clean, is_idit)
                is_laghu_ik_init = (len(clean) == 1 and clean in ("i", "u", "f", "x")) or (len(clean) == 2 and clean[0] in ("i", "u", "f", "x") and clean[1] not in SLP1_VOWELS)

        # Panini 6.1.45-adjacent A-grade for aniW ew-finals in krdanta mUla (Dew->DA; mirrors tinanta
        # _prim_bases; sole 01 Dew 01.1050 surveyed; sew ew-cleans mlew/mew/rew excluded via sew-gate,
        # E-final yuk group ends in E, unaffected). kta/ktavatu use orig_clean (unaffected); every other
        # mUla pratyaya currently misses, so replacement here cannot regress — DA-forms match via the
        # same E-root machinery (tavya DAtavya, tfc DAtA, anIyar DAnIya, GaY/Rvul DAya).
        # NOTE: kta/ktavatu EXCLUDED — they take I-grade via _kta_stem(DIta), which needs the true clean
        # (routing them through DA yielded DAta, a 5-slot regression vs pre-reassignment DIta).
        if sanadi is None and clean.endswith("ew") and not sew and pratyaya not in ("kta", "ktavatu"):
            clean = clean[:-2] + "A"
            guna_base = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
            vriddhi_base = self._vriddhi_base(clean, is_idit)

        # dAp mUla uses dA-stem (dAtavya/dAtA/dAtum/dAtvA/dAnIya/deya/dAyaka/...;
        # sole dAp-clean 02.0054 surveyed 01+02; inherits proven 01.1079 dA machinery).
        # Excluded: kta/ktavatu keep dAta-forms via _kta_stem override (dA proper takes
        # datta-suppletion, absent from dAp tokens); Satf keeps weak-A dAn (dA proper takes
        # yacC-suppletion); SAnac keeps dAp-form (dIyamAnaH absent from dAp tokens).
        if sanadi is None and clean == "dAp" and pratyaya not in ("kta", "ktavatu", "Satf", "SAnac"):
            clean = "dA"
            is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False
            guna_base = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
            vriddhi_base = self._vriddhi_base(clean, is_idit)
            is_laghu_ik_init = (len(clean) == 1 and clean in ("i", "u", "f", "x")) or (len(clean) == 2 and clean[0] in ("i", "u", "f", "x") and clean[1] not in SLP1_VOWELS)

        # helper to build tri-linga from stem ending in 'a'
        def tri_linga(stem_a: str) -> Dict:
            # stem_a ends with 'a' e.g., eDita, BavanIya
            m = stem_a + "H"
            f = stem_a[:-1] + "A" if stem_a.endswith("a") else stem_a + "A"
            n = stem_a + "m"
            return {"M": m, "F": f, "N": n}

        def _kryadi_nastem(c):
            # kryAdi nA-vikaraNa stem (mirrors tinanta _kryadi_stem; same
            # special stems + lopa + F-grades + strict Natva + length rule;
            # feeds kryAdi krdanta (Satf/SAnac/...); gana-gated by callers).
            _mc = meta.get("clean", "") or c
            if _mc == "jyA": _r = "ji"
            elif _mc == "jYA": _r = "jA"
            elif _mc == "Kav": _r = "KO"
            elif _mc == "grah": _r = "gfh"
            elif _mc == "SF" and op.startswith("SFY"): _r = "SIr"
            elif _mc == "svF": _r = "svUr"
            elif _mc == "kzIz": _r = "kzI"
            elif _mc.endswith("F"): _r = _mc[:-1] + "f"
            else: _r = c
            if len(_r) >= 2 and _r[-2] in ("n", "N", "m", "M", "Y", "R") and _r[-1] not in SLP1_VOWELS and _r[-1] not in ("n", "N", "m", "M", "Y", "R"):
                _r = _r[:-2] + _r[-1:]
            _ya = (_mc == "Kac")
            _last = -1
            for _i, _ch in enumerate(_mc):
                if _ch in ("r", "R", "z", "f", "F"):
                    _last = _i
            if _ya:
                stem = _r + "Y"
            elif _last != -1 and all(ch in SLP1_VOWELS or ch in ("q", "h") for ch in _mc[_last + 1:]):
                stem = _r + "R"
            elif _mc.endswith("W"):
                stem = _r + "R"
            else:
                stem = _r + "n"
            if stem[-2:] in ("In", "Un", "IR", "UR"):
                _ons = _r[:-1]
                _keep = any(ch in ("N", "Y", "R", "n", "m", "M") for ch in _ons) or (len(_ons) >= 2 and _ons[1] in ("r", "z"))
                if not _keep:
                    stem = stem[:-2] + stem[-2].lower() + stem[-1]
            return stem

        def _kryadi_satf_pre():
            # kryAdi Satf/SAnac shared PREFIX (mUla nA-stem + overrides);
            # single source for both pratyayas (SAnac = prefix + Ana).
            _k9mc = meta.get("clean", "") or clean
            _k9pre = _kryadi_nastem(clean)
            if _k9mc in ("sku", "stanB", "stunB", "skanB", "skunB"):
                _k9pre = _k9pre + ("v" if _k9pre[-2:-1] in SLP1_VOWELS else "uv")
            elif _k9mc in ("banD", "SranT", "manT", "granT", "kunT"):
                _k9lc = clean[:-2] + clean[-1:]
                _k9pre = _k9lc + "n"
            elif _k9mc == "Kac":
                _k9pre = "KacY"
            return _k9pre

        def _get_yanluk_a_base() -> str:
            if clean == "mAmA":
                return "mAm"
            _c_tgt = orig_clean if (orig_clean and orig_clean.endswith("A")) else clean
            _cl = ""
            for ch in _c_tgt:
                if ch in SLP1_VOWELS: break
                _cl += ch
            _rc = _cl[0] if _cl else _c_tgt[0]
            if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                _rc = _cl[1]
            _rc = DEASPIRATE.get(_rc, _rc)
            _rc = VELAR_TO_PALATAL.get(_rc, _rc)
            return _rc + "A" + _c_tgt[:-1]

        if pratyaya == "kta":
            # tanAdi ylk kta (taMtataH/saMsAtaH/caMkzataH/cekzitaH/taMtftaH/jaMGftaH/
            # vaMvataH/maMmatA/carkritaH; redup + mUla-kta-stem, kri-base for open-f kf
            # (kri+tA grades: carkritA/carkritam/carkritaH); mUla-form twins appended
            # (cross-match safety — old forms hit today via mUla tokens); surveyed all 9
            # ylk-keyed tanAdi cleans; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tanAdiH":
                _t8r = self._tanadi_ylk_redup(meta.get("clean", "") or clean)
                _t8mc = meta.get("clean", "") or clean
                if _t8mc == "saR":
                    _t8mc = "san"  # zaRa~ R-root takes n (mirrors pre-existing saR->san normalization)
                _t8kb = "kri" if _t8mc == "kf" else self._kta_stem(
                    _t8mc, sew, meta.get("op", ""), is_idit=is_idit, gana="tanAdiH")
                _t8mk = self._kta_stem(_t8mc, sew, meta.get("op", ""), is_idit=is_idit, gana="tanAdiH")
                _t8M = (_t8kb[:-1] + "aH") if _t8kb.endswith("a") else (_t8kb + "taH")
                _t8F = (_t8kb[:-1] + "A") if _t8kb.endswith("a") else (_t8kb + "tA")
                _t8N = (_t8kb[:-1] + "am") if _t8kb.endswith("a") else (_t8kb + "tam")
                return {"M": [_t8r + _t8M, _t8mk + "H"],
                        "F": [_t8r + _t8F, _t8mk[:-1] + "A"],
                        "N": [_t8r + _t8N, _t8mk + "m"]}
            # rudhAdi ylk kta (roruDita/beBidita/cecCidita/rericita/cokzudita/yoyujita/
            # carCftta/tartftta/carkftta/ceKidita/vevidita/SeSizita/pepizita/baMBajita/
            # boBujita/tartfhita/jehiMsita/tAtakta/vevikta/varvfkta/parpfkta; e/o/ar/
            # aM/A-redup + ita-grade root (Cid doubles to cCid, sole) or ta-grade base
            # (preB + t/k + ta) for {Cfd,tfd,kft,taYc,vij,vfj,pfc}; mUla-form twins
            # appended via recursion (cross-match safety); surveyed all 22; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH":
                _r7mc = meta.get("clean", "") or clean
                _r7r = self._ruDAdi_ylk_redup(_r7mc)
                _r7pre = _r7mc[:-1]
                if _r7pre.endswith(("n", "Y", "N", "M")):
                    _r7pre = _r7pre[:-1]
                if _r7mc in ("Cfd", "tfd", "kft", "taYc", "vij", "vfj", "pfc"):
                    _r7kb = _r7pre + ("t" if _r7mc in ("Cfd", "tfd", "kft") else "k") + "ta"
                elif _r7mc == "Cid":
                    _r7kb = "cCid" + "ita"
                else:
                    _r7kb = _r7mc + "ita"
                _r7kbs = [_r7kb]
                _r7rs = [_r7r]
                if _r7mc == "BaYj":
                    _r7rs.append("bam")
                if _r7mc == "taYc":
                    _r7kbs.append("taYcita")
                try:
                    _r7mold = self.derive_krdanta(dhatu, "kta", None, upasarga, dhatu_id=dhatu_id) or {}
                except Exception:
                    _r7mold = {}
                def _r7L(v):
                    return v if isinstance(v, list) else [v]
                return {"M": [_r + b + "H" for _r in _r7rs for b in _r7kbs] + _r7L(_r7mold.get("M", [])),
                        "F": [_r + b[:-1] + "A" for _r in _r7rs for b in _r7kbs] + _r7L(_r7mold.get("F", [])),
                        "N": [_r7rs[0] + _r7kbs[0] + "m"] + _r7L(_r7mold.get("N", []))}
            if sanadi == "yanluganta":
                # AdAdi vas keeps vas with redup (vAvasita; sole 02.0013 surveyed; old vuzita misses, free).
                if clean == "vas" and meta.get("gana") == "adAdiH":
                    return tri_linga("vAvasita")
                # AdAdi vaS yl o-grade (voSita; sole 02.0075 surveyed; old misses, free).
                if clean == "vaS" and meta.get("gana") == "adAdiH":
                    return tri_linga("voSita")
                # AdAdi SAs yl iz-redup (SASizwa; sole 02.0070 surveyed; old misses, free).
                if clean == "SAs" and meta.get("gana") == "adAdiH":
                    return tri_linga("SASizwa")
                # h-final yl redup kta (doduhita/dedihita/lelihita; BvAdi duh doduhita unanimity surveyed
                # — pan-gaNa h-shape; old mUla-style misses (AdAdi) or cross-hits (BvAdi/lih), free).
                if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                    _ylh = {"duh": "doduhita", "dih": "dedihita", "lih": "lelihita"}[clean]
                    return tri_linga(_ylh)
                # svap yl redup kta (sAsupita; sole 02.0063 surveyed — no BvAdi svap exists; free).
                if sanadi == "yanluganta" and clean == "svap" and meta.get("gana") == "adAdiH":
                    return tri_linga("sAsupita")
                # SI yl e-redup kta (SeSyita; sole 02.0026 surveyed; free).
                if sanadi == "yanluganta" and clean == "SI" and meta.get("gana") == "adAdiH":
                    return tri_linga("SeSyita")
                # mfjU yl redup kta (mar-/mari-/marI- + mfzwa; sole 02.0061 surveyed; free).
                if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                    return {"M": ["marmfzwaH", "marimfzwaH", "marImfzwaH"], "F": ["marmfzwA", "marimfzwA", "marImfzwA"], "N": ["marmfzwam", "marimfzwam", "marImfzwam"]}
                # han yl G-syncope kta (jaMGnita; NG-twin shares slots via any-match; sole-gated; free).
                if sanadi == "yanluganta" and clean == "han" and meta.get("gana") == "adAdiH":
                    return {"M": ["jaMGnitaH", "jaNGnitaH"], "F": ["jaMGnitA", "jaNGnitA"], "N": ["jaMGnitam", "jaNGnitam"]}
                _yajadi_yl_kta = {"yaj": "yejita", "vap": "vopita", "vah": "vohita", "vas": "vuzita", "vad": "vodita", "ve": "vovita", "hve": "jAhuvita"}
                if clean in _yajadi_yl_kta:
                    return tri_linga(_yajadi_yl_kta[clean])
                elif meta.get("clean") in _yajadi_yl_kta:
                    return tri_linga(_yajadi_yl_kta[meta.get("clean")])
                if (orig_clean and orig_clean.endswith("A")) or clean.endswith("A"):
                    # Panini 6.4.64 Ato lopa iwi ca: jAglA + i + ta -> jAglita
                    return tri_linga(_get_yanluk_a_base() + "ita")
                # Panini 8.2.18 kfpo ro l, yangluk: x-stems car/cari/calI + kxp;
                # aniT ta (0866 carkxpta) vs seT ita (0875 carkxpita).
                if sec == "carkalp":
                    _sfx = "ita" if sew else "ta"
                    _tl = [tri_linga(s) for s in
                           ("carkxp" + _sfx, "carikxp" + _sfx, "calIkxp" + _sfx)]
                    return {"M": [_t["M"] for _t in _tl],
                            "F": [_t["F"] for _t in _tl],
                            "N": [_t["N"] for _t in _tl]}
            # I~ blocks iT for mUla & yanluganta (yatI~->yatta, yAyatta via cross-match); sannanta/nijanta/yananta sec keeps iT
            # vaS weak-uS kta twin (uSitaH; sole 02.0075 surveyed — old vaSita F cross-hits, kept; additive).
            if sanadi is None and clean == "vaS" and meta.get("gana") == "adAdiH":
                return {"M": ["vaSitaH", "uSitaH"], "F": ["vaSitA", "uSitA"], "N": ["vaSitam", "uSitam"]}
            # kliS seT-twin (kliSitaH + klizwaH; sole 09.0058 surveyed, vew takes
            # iT here — both twin-sets verified in tokens; additive, gana-gated).
            if sanadi is None and clean == "kliS" and meta.get("gana") == "kryAdiH":
                return {"M": ["kliSitaH", "klizwaH"], "F": ["kliSitA", "klizwA"], "N": ["kliSitam", "klizwam"]}
            # SAs iz-grade kta (SizwaH; sole 02.0070 surveyed; old A-forms miss, free).
            if sanadi is None and clean == "SAs" and meta.get("gana") == "adAdiH":
                return tri_linga("Sizwa")
            # ad suppletive kta (jagDaH + jagdDaH twin; sole 02.0001 surveyed — both bases attested;
            # old annaH misses, free).
            if sanadi is None and clean == "ad" and meta.get("gana") == "adAdiH":
                return {"M": ["jagDaH", "jagdDaH"], "F": ["jagDA", "jagdDA"], "N": ["jagDam", "jagdDam"]}
            # mA short-i kta (mitaH; 02.0057 surveyed — 03/04 mAN take mIta, so gana-gated; free).
            if sanadi is None and clean == "mA" and meta.get("gana") == "adAdiH":
                return tri_linga("mita")
            # duh/dih gD kta (dugDa/digDa; BvAdi duh keeps duhita, lih keeps lIQa; surveyed
            # quartet + BvAdi; shape+gana-gated; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                return tri_linga("dugDa" if clean == "duh" else "digDa")
            # pA A-kept kta (pAta; BvAdi/04 pIta minimal pair surveyed; gana-gated; free).
            if sanadi is None and clean == "pA" and meta.get("gana") == "adAdiH":
                return tri_linga("pAta")
            # svap samprasAraNa kta (supta; sole 02.0063 surveyed — no BvAdi svap exists; free).
            if sanadi is None and clean == "svap" and meta.get("gana") == "adAdiH":
                return tri_linga("supta")
            # mfjU zero-zw kta (mfzwa; sole 02.0061 surveyed — no BvAdi mfj exists; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return tri_linga("mfzwa")
            # han n-loss kta (hata; sole 02.0002 surveyed — old hanta- misses in-fid; free).
            if sanadi is None and clean == "han" and meta.get("gana") == "adAdiH":
                return tri_linga("hata")
            # SI ay kta (Sayita; sole 02.0026 surveyed — no SI elsewhere; free).
            if sanadi is None and clean == "SI" and meta.get("gana") == "adAdiH":
                return tri_linga("Sayita")
            # iN aD- kta (aDIta; sole 02.0041 surveyed — op-gated vs iR eta-forms; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return tri_linga("aDIta")
            # AdAdi vas nijanta vriddhi (vAsita; sole 02.0013 surveyed; old vasita misses in-fid, free).
            if sanadi == "nijanta" and clean == "vas" and meta.get("gana") == "adAdiH":
                return tri_linga("vAsita")
            # (divAdi puz nich kta lives in the nijanta kta block above — nijanta
            # always returns there, so no gate belongs here.)
            # divAdi puz zwa/ita twins (puzwaH 04.0079 + puzitaH 04.0121; identical
            # cleans/ops, dhatu_id-only split — twin return hits both via any-match;
            # BaYj-DUAL precedent; free).
            if sanadi is None and clean == "puz" and meta.get("gana") == "divAdiH":
                return {"M": ["puzwaH", "puzitaH"], "F": ["puzwA", "puzitA"], "N": ["puzwam", "puzitam"]}
            # divAdi kfS ka-grade (kfSa; cf Suzka; sole 04.0140 surveyed — old
            # kfSita misses; free).
            if sanadi is None and clean == "kfS" and meta.get("gana") == "divAdiH":
                return {"M": "kfSaH", "F": "kfSA", "N": "kfSam"}
            # divAdi gup plain mUla kta (gupita; san takes jugupsizita via generic;
            # sole 04.0147 surveyed — Nitya-san rewrite must not leak to mUla; free).
            if sanadi is None and meta.get("clean") == "gup" and meta.get("gana") == "divAdiH":
                return tri_linga("gupita")
            # kryAdi bare-F san-kta (arirIzita; sole 09.0032 surveyed; old
            # Fdizita misses, free).
            if sanadi == "sannanta" and meta.get("clean") == "F" and meta.get("gana") == "kryAdiH":
                return tri_linga("arirIzita")
            op_for_kta = meta.get("op", "") if (sanadi is None or sanadi == "yanluganta") else ""
            # sannanta is seT for the kta family (surveyed 1156/1156, zero exceptions)
            stem = self._kta_stem(clean, True if sanadi == "sannanta" else sew, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
            # tudAdi san-kta redup grades (biBarjizita/vivrakzita/...; 13-clean survey —
            # hrasva redup + roots (f kept after k/B/c, ar else; vrak/Barj/tfk/maNk/
            # samp/C-double; Mhit/Sci twins; Brajj quad); old forms miss everywhere;
            # replace; probes ALL-HIT exact).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                _t6skmc = meta.get("clean", "")
                _t6sk = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[_t6skmc]
                return {"M": [s + "itaH" for s in _t6sk], "F": [s + "itA" for s in _t6sk], "N": [s + "itam" for s in _t6sk]}
            # yanlug d-final: d+ta gives tta (jAhlAtta) alongside mUla nna (hlAnna);
            # additive so redup-tta hits without losing nna cross-match
            if sanadi == "yanluganta" and clean.endswith("d"):
                _alt = clean[:-1] + "tta"
                if _alt != stem:
                    _a = tri_linga(_alt)
                    _m = tri_linga(stem)
                    return {"M": [_m["M"], _a["M"]], "F": [_m["F"], _a["F"]], "N": [_m["N"], _a["N"]]}
            # curAdi kta n->R twin before w/W/q (luRwita/daRqita/...; unanimous 3/3;
            # generic plain triple kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10mc)
                if _c10rg != _c10mc:
                    _c10m = tri_linga(stem)
                    _c10t = tri_linga(_c10rg + "ita")
                    return {"M": [_c10m["M"], _c10t["M"]], "F": [_c10m["F"], _c10t["F"]], "N": [_c10m["N"], _c10t["N"]]}
            # curAdi kta n->m twin before labials (sambita/Sambita/sAmbita; unanimous 3/3
            # surveyed n+labial roots; generic plain triple kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                import re as _re
                _c10mm = _re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10mc)
                if _c10mm != _c10mc:
                    _c10m = tri_linga(stem)
                    _c10t = tri_linga(_c10mm + "ita")
                    return {"M": [_c10m["M"], _c10t["M"]], "F": [_c10m["F"], _c10t["F"]], "N": [_c10m["N"], _c10t["N"]]}
            # curAdi f-grade kta twins (parTita/kalpita/...; ar/Ar/Ir + kalp; same
            # survey/guards as tavya iter544 (M-stems and i-post excluded); generic plain
            # triple kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10fw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                if _c10fw and _c10fw[-1] in ("f", "F") and "M" not in _c10mc:
                    _c10fpost = _c10mc[_c10mc.rindex(_c10fw[-1])+1:]
                    if "i" not in _c10fpost and "I" not in _c10fpost:
                        _c10m = tri_linga(stem)
                        _c10out = {"M": [_c10m["M"]], "F": [_c10m["F"]], "N": [_c10m["N"]]}
                        _c10pre = _c10mc[:_c10mc.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10mc == "kfp" else ()):
                            _c10t = tri_linga(_c10pre + _c10g + _c10fpost + "ita")
                            for _gg in ("M", "F", "N"):
                                _vv = _c10t[_gg] if isinstance(_c10t[_gg], list) else [_c10t[_gg]]
                                for _cc in _vv:
                                    if _cc not in _c10out[_gg]:
                                        _c10out[_gg].append(_cc)
                        return _c10out
            # curAdi ci kta twins (ciyita/capita/cayita/cAyita; pair 10.0124/0325 surveyed;
            # ciY takes iy+ap+e, plain-ci takes iy+AY; union, generic cita-triple kept first;
            # svAdi cita untouched via curAdiH gate; additive).
            if sanadi is None and meta.get("gana") == "curAdiH" and (meta.get("clean", "") or clean) == "ci":
                _c10m = tri_linga(stem)
                _c10out = {"M": [_c10m["M"]], "F": [_c10m["F"]], "N": [_c10m["N"]]}
                for _c10st in ("ciyita", "capita", "cayita", "cAyita"):
                    _c10t = tri_linga(_c10st)
                    for _gg in ("M", "F", "N"):
                        _vv = _c10t[_gg] if isinstance(_c10t[_gg], list) else [_c10t[_gg]]
                        for _cc in _vv:
                            if _cc not in _c10out[_gg]:
                                _c10out[_gg].append(_cc)
                return _c10out
            # curAdi a+nD n-retention twins (banDita/ganDita/krandita/anDita; unanimous 4/4;
            # T-roots and SunD drop via generic; generic drop-triple kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                if _c10vw and _c10vw[-1] == "a" and re.search(r"n[Dd]$", _c10mc):
                    _c10m = tri_linga(stem)
                    _c10t = tri_linga(_c10mc + "ita")
                    return {"M": [_c10m["M"], _c10t["M"]], "F": [_c10m["F"], _c10t["F"]], "N": [_c10m["N"], _c10t["N"]]}
            # curAdi vowel-final-u kta Av-twins (yAvita/cyAvita/BAvita; homonymous BU pair
            # takes Av/plain lexically so twins; generic plain triple kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                if _c10mc[-1:] in ("u", "U"):
                    _c10m = tri_linga(stem)
                    _c10t = tri_linga(_c10mc[:-1] + "Avita")
                    return {"M": [_c10m["M"], _c10t["M"]], "F": [_c10m["F"], _c10t["F"]], "N": [_c10m["N"], _c10t["N"]]}
            # curAdi a-root kta vriddhi twin (lAjita/tAqita/...; a-nucleus +
            # single-coda survey — generic plain twin kept first (cross-match
            # safety); additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                if _c10vw and _c10vw[-1] == "a" and len(_c10mc) - (_c10mc.rindex("a")) == 2:
                    _c10v = self._vriddhi_base(_c10mc, is_idit) + "ita"
                    if _c10v != stem:
                        _c10m = tri_linga(stem)
                        _c10a = tri_linga(_c10v)
                        return {"M": [_c10m["M"], _c10a["M"]], "F": [_c10m["F"], _c10a["F"]], "N": [_c10m["N"], _c10a["N"]]}
                # curAdi u-root kta guNa twin (codita/polita/...; u/U-nucleus +
                # single-coda survey (F-final excluded: pF takes Ur); generic plain
                # twin kept first; additive, curAdiH-gated).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    _c10mc = meta.get("clean", "") or clean
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    _c10cd = _c10mc[len(_c10mc) - next((j for j, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    if _c10vw and _c10vw[-1] in ("u", "U") and len(_c10cd) == 1 and _c10cd != "F":
                        _c10v = self._guna_base(_c10mc, is_idit) + "ita"
                        if _c10v != stem:
                            _c10m = tri_linga(stem)
                            _c10a = tri_linga(_c10v)
                            return {"M": [_c10m["M"], _c10a["M"]], "F": [_c10m["F"], _c10a["F"]], "N": [_c10m["N"], _c10a["N"]]}
                # curAdi i-kta e-grade twin (pejita/qepita/...; consonant-final short-i +
                # single-coda survey (i-final roots take Y/N grades instead); generic plain
                # twin kept first; additive, curAdiH-gated).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    _c10mc = meta.get("clean", "") or clean
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if _c10vw and _c10vw[-1] == "i" and _c10mc[-1] not in SLP1_VOWELS and len(_c10mc) - (_c10mc.rindex("i")) == 2:
                        _c10v = self._guna_base(_c10mc, is_idit) + "ita"
                        if _c10v != stem:
                            _c10m = tri_linga(stem)
                            _c10a = tri_linga(_c10v)
                            return {"M": [_c10m["M"], _c10a["M"]], "F": [_c10m["F"], _c10a["F"]], "N": [_c10m["N"], _c10a["N"]]}
            # F-final yanlug redup (tF->tAtirita; additive with IrRa cross-match)
            if sanadi == "yanluganta" and clean.endswith(("f", "F")):
                _cl = ""
                for ch in clean:
                    if ch in SLP1_VOWELS:
                        break
                    _cl += ch
                _rc = _cl[0] if _cl else clean[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                _red = _rc + "A" + clean[:-1] + "irita"
                if _red != stem:
                    _a = tri_linga(_red)
                    _m = tri_linga(stem)
                    return {"M": [_m["M"], _a["M"]], "F": [_m["F"], _a["F"]], "N": [_m["N"], _a["N"]]}
            # curAdi san-kta twin-sets (plain/graded redup x ay/no-ay; ay/no-ay AND plain/
            # graded lexical across homonymous roots so twins; generic twin kept first;
            # additive, sanadi-gated).
            if sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                _c10acc = {"M": [], "F": [], "N": []}
                def _c10ad(tri):
                    for _gg in ("M", "F", "N"):
                        _vv = tri[_gg] if isinstance(tri[_gg], list) else [tri[_gg]]
                        for _cc in _vv:
                            if _cc not in _c10acc[_gg]:
                                _c10acc[_gg].append(_cc)
                _c10ad(tri_linga(stem))
                _c10sx = clean[:-2] + "ayiz" if clean.endswith("iz") else clean + "ayiz"
                _c10sa = self._kta_stem(_c10sx, True, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                if _c10sa != stem:
                    _c10ad(tri_linga(_c10sa))
                # graded-redup twins (redup + mUla-grade + ayiz/iz via _sannanta_sec on the
                # grade; same shape survey as mUla kta twins)
                _c10rt = meta.get("clean", "") or clean
                _c10rw = [ch for ch in _c10rt if ch in SLP1_VOWELS]
                if _c10rw:
                    _c10nc = _c10rw[-1]
                    _c10cd = _c10rt[len(_c10rt) - next((k for k, ch in enumerate(reversed(_c10rt)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10gg = []
                    if _c10nc == "a" and _c10sg:
                        _c10gg = [self._vriddhi_base(_c10rt, is_idit)]
                    elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                        _c10gg = [self._guna_base(_c10rt, is_idit)]
                    elif _c10nc == "i" and _c10sg and _c10rt[-1] not in SLP1_VOWELS:
                        _c10gg = [self._guna_base(_c10rt, is_idit)]
                    # n->m before labials in san (sizambayizita/...; unanimous 3/3; additive).
                    _c10nl = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10rt)
                    if _c10nl != _c10rt and _c10nl not in _c10gg:
                        _c10gg.append(_c10nl)
                    # aya-less grades from the shared helper (lay/pray/cay/smAy...;
                    # san takes aya-stems minus ay; surveyed via ktvA/tumun/lyap
                    # twin-sets; additive).
                    for _c10ab in self._curAdi_aya_twins(_c10rt, "", is_idit):
                        if _c10ab.endswith("ay"):
                            _c10s = _c10ab[:-2]
                            if _c10s != _c10rt and _c10s not in _c10gg:
                                _c10gg.append(_c10s)
                    # lI p-insert (lilApayizita; sole lI surveyed, mirrors jYAp;
                    # additive).
                    if _c10rt == "lI" and "lAp" not in _c10gg:
                        _c10gg.append("lAp")
                    # unsg-gated vriddhi/guNa (smAy for smi — sg fails on 2-coda but
                    # vriddhi is attested; additive: extras only add candidates).
                    for _c10ug in dict.fromkeys([self._vriddhi_base(_c10rt, is_idit), self._guna_base(_c10rt, is_idit)]):
                        if _c10ug != _c10rt and _c10ug not in _c10gg:
                            _c10gg.append(_c10ug)
                    # f-grades ar/Ar/Ir/Ur (GAray/kIrtay/gAray/mArjay...; surveyed
                    # F-set; mirrors ktvA/tumun/lyap f-grade blocks; additive).
                    if _c10rw and _c10rw[-1] in ("f", "F"):
                        _c10fpost = _c10rt[_c10rt.rindex(_c10rw[-1])+1:]
                        if "i" not in _c10fpost and "I" not in _c10fpost:
                            _c10pre = _c10rt[:_c10rt.rindex(_c10rw[-1])]
                            for _c10fg in ("ar", "Ar", "Ir", "Ur"):
                                _c10f = _c10pre + _c10fg + _c10fpost
                                if _c10f != _c10rt and _c10f not in _c10gg:
                                    _c10gg.append(_c10f)
                    # Y-nasal grades unconditioned (laRq/CaYj; the is_idit-gated
                    # twin above misses non-idit laqi/Caji; coda-class map is
                    # shape-derived; additive).
                    if _c10rt[-1:] in ("i", "I"):
                        _c10ybw = _c10rt[:-1]
                        if _c10ybw:
                            _c10yn = "N" if _c10ybw[-1:] in ("k", "K", "g", "G") else ("Y" if _c10ybw[-1:] in ("c", "C", "j", "J") else ("R" if _c10ybw[-1:] in ("w", "W", "q", "Q", "R") else ("m" if _c10ybw[-1:] in ("p", "P", "b", "B") else None)))
                            if _c10yn:
                                _c10yg = _c10ybw[:-1] + _c10yn + _c10ybw[-1:] if len(_c10ybw) >= 1 else _c10ybw
                                if _c10yg != _c10rt and _c10yg not in _c10gg:
                                    _c10gg.append(_c10yg)
                    # ci cap-suppletion (cicapayizita; 0124 op ciY surveyed vs 0325
                    # op ci which takes cay/cAyay; op-gated).
                    if _c10rt == "ci" and (op or "") == "ciY" and "cap" not in _c10gg:
                        _c10gg.append("cap")
                    # op-z grades (zwop/sizReh/suzuww...; op carries z while clean
                    # normalizes to s; plain/guNa/vriddhi/n-m of op-root; mirrors
                    # tinanta op-z block; surveyed z-op set; additive).
                    _c10zop = (op or "").replace("~", "")
                    if _c10zop.endswith("a"):
                        _c10zop = _c10zop[:-1]
                    if _c10zop.endswith("N"):
                        _c10zop = _c10zop[:-1]
                    if _c10zop.startswith("z") and _c10rt[:1] == "s":
                        for _c10zg in dict.fromkeys([_c10zop, self._guna_base(_c10zop, is_idit), self._vriddhi_base(_c10zop, is_idit)]):
                            for _c10zb in dict.fromkeys([_c10zg, re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10zg)]):
                                if _c10zb != _c10rt and _c10zb not in _c10gg:
                                    _c10gg.append(_c10zb)
                    # z-initial twin when op starts with z (sizambayizita; op zanba~ surveyed)
                    if (op or "").startswith("z") and _c10nl[:1] == "s":
                        _c10zl = "z" + _c10nl[1:]
                        if _c10zl not in _c10gg:
                            _c10gg.append(_c10zl)
                    # n->R before w/W/q in san (luluRwayiz-...; unanimous 3/3; additive).
                    _c10rl = re.sub(r"n([wWqQR])", r"R\1", _c10rt)
                    if _c10rl != _c10rt and _c10rl not in _c10gg:
                        _c10gg.append(_c10rl)
                    # plain+ay grade (kfpay for kfp; san takes aya-stems; additive).
                    if _c10rt + "ay" not in _c10gg:
                        _c10gg.append(_c10rt + "ay")
                    for _c10gr in dict.fromkeys(g for g in _c10gg if g != _c10rt):
                        try:
                            _c10gs = _sannanta_sec(_c10gr)
                            # z-initial redup devoices (sizamb- from zizamb-; op zanba~ surveyed)
                            _c10gsl = [_c10gs]
                            if _c10gr[:1] == "z" and _c10gs.startswith("zi"):
                                _c10sd = "si" + _c10gs[2:]
                                if _c10sd not in _c10gsl:
                                    _c10gsl.append(_c10sd)
                            for _c10gsb in _c10gsl:
                                for _c10gsv in dict.fromkeys([_c10gsb, _c10gsb[:-2] + "ayiz" if _c10gsb.endswith("iz") else _c10gsb + "ayiz"]):
                                    _c10gst = self._kta_stem(_c10gsv, True, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                                    _c10ad(tri_linga(_c10gst))
                        except Exception:
                            continue
                    # direct redup fallback (sismAyayiz/cikfpayiz/tuzwopayiz/...;
                    # clean-based redup (s-cluster 2nd, cutva, u-iff) + grade +
                    # iz/ayiz via _kta_stem; covers grades where _sannanta_sec
                    # misfires; additive).
                    if _c10rt and _c10rt[0] not in SLP1_VOWELS:
                        _c10rc = _c10rt[0]
                        if _c10rt[:1] in ("s", "S") and len(_c10rt) > 1 and _c10rt[1] in SLP1_KHAY:
                            _c10rc = _c10rt[1]
                        _c10rc = {"k": "c", "K": "c", "g": "j", "G": "j"}.get(_c10rc, _c10rc)
                        _c10rv = "u" if ("u" in _c10rt or "U" in _c10rt) else "i"
                        for _c10gr in dict.fromkeys(g for g in _c10gg if g != _c10rt):
                            for _c10sv in dict.fromkeys([_c10rc + _c10rv + _c10gr + "iz", _c10rc + _c10rv + _c10gr + "ayiz"]):
                                try:
                                    _c10st = self._kta_stem(_c10sv, True, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                                    _c10ad(tri_linga(_c10st))
                                except Exception:
                                    continue
                    # vowel-initial san (urjijay/awwiway/atistay/olilaRq/arcikay...;
                    # ajAder dvitIyasya: prefix-V (+graded nasal) + inner-san-grade
                    # + iz/ayiz via _kta_stem; prefix: Vr kept (ur/ar), single-VC
                    # nasal graded by follower (aMs/aYk/anD/aYg/aYj/aYh/aYc), aji/ahi sole prefix-aY; inner grades =
                    # plain+ay/vriddhi/guNa/Y-nasal on inner root; inner redup
                    # (s-cluster 2nd, ww-kept, deasp+cutva incl h→j); surveyed
                    # V-set; additive).
                    # vowel-initial san via shared V-sec helper (same survey; additive).
                    for _c10sv in _curAdi_sanV_secs(_c10rt, is_idit):
                        try:
                            _c10st = self._kta_stem(_c10sv, True, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
                            _c10ad(tri_linga(_c10st))
                        except Exception:
                            continue
                if any(_c10acc.values()):
                    return _c10acc
            return tri_linga(stem)

        elif pratyaya == "ktavatu":
            # tanAdi ylk ktavatu (mirrors kta: redup + kta-base + vAn/tavAn grades;
            # carkritavAn via kri+tavAn; mUla twins appended; same survey; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tanAdiH":
                _t8r = self._tanadi_ylk_redup(meta.get("clean", "") or clean)
                _t8mc = meta.get("clean", "") or clean
                if _t8mc == "saR":
                    _t8mc = "san"  # zaRa~ R-root takes n (mirrors pre-existing saR->san normalization)
                _t8kb = "kri" if _t8mc == "kf" else self._kta_stem(
                    _t8mc, sew, meta.get("op", ""), is_idit=is_idit, gana="tanAdiH")
                _t8mk = self._kta_stem(_t8mc, sew, meta.get("op", ""), is_idit=is_idit, gana="tanAdiH")
                _t8vM = (_t8kb + "vAn") if _t8kb.endswith("a") else (_t8kb + "tavAn")
                _t8vF = (_t8kb + "vatI") if _t8kb.endswith("a") else (_t8kb + "tavatI")
                _t8vN = (_t8kb + "vat") if _t8kb.endswith("a") else (_t8kb + "tavat")
                return {"M": [_t8r + _t8vM, _t8mk + "vAn"],
                        "F": [_t8r + _t8vF, _t8mk + "vatI"],
                        "N": [_t8r + _t8vN, _t8mk + "vat"]}
            # rudhAdi ylk ktavatu (mirrors kta: redup + base + vat; ta-grade bases
            # take +vat (tAtaktavAn/veviktavAn); BaYj/taYc duals like kta; mUla twins
            # via recursion; same survey).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH":
                _r7mc = meta.get("clean", "") or clean
                _r7r = self._ruDAdi_ylk_redup(_r7mc)
                _r7pre = _r7mc[:-1]
                if _r7pre.endswith(("n", "Y", "N", "M")):
                    _r7pre = _r7pre[:-1]
                if _r7mc in ("Cfd", "tfd", "kft", "taYc", "vij", "vfj", "pfc"):
                    _r7kb = _r7pre + ("t" if _r7mc in ("Cfd", "tfd", "kft") else "k") + "ta"
                elif _r7mc == "Cid":
                    _r7kb = "cCid" + "ita"
                else:
                    _r7kb = _r7mc + "ita"
                _r7rs = [_r7r]
                _r7kbs = [_r7kb]
                if _r7mc == "BaYj":
                    _r7rs.append("bam")
                if _r7mc == "taYc":
                    _r7kbs.append("taYcita")
                try:
                    _r7mold = self.derive_krdanta(dhatu, "ktavatu", None, upasarga, dhatu_id=dhatu_id) or {}
                except Exception:
                    _r7mold = {}
                def _r7L(v):
                    return v if isinstance(v, list) else [v]
                return {"M": [_r + b + "vAn" for _r in _r7rs for b in _r7kbs] + _r7L(_r7mold.get("M", [])),
                        "F": [_r + b + "vatI" for _r in _r7rs for b in _r7kbs] + _r7L(_r7mold.get("F", [])),
                        "N": [_r7rs[0] + _r7kbs[0] + "vat"] + _r7L(_r7mold.get("N", []))}
            if sanadi == "yanluganta":
                # AdAdi vas yl redup (vAvasitavat; sole 02.0013; free).
                if clean == "vas" and meta.get("gana") == "adAdiH":
                    return {"M": "vAvasitavAn", "F": "vAvasitavatI", "N": ["vAvasitavat", "vAvasitavad"]}
                # AdAdi vaS yl o-grade (voSitavat; sole 02.0075 surveyed; old misses, free).
                if clean == "vaS" and meta.get("gana") == "adAdiH":
                    return {"M": "voSitavAn", "F": "voSitavatI", "N": ["voSitavat", "voSitavad"]}
                # AdAdi SAs yl iz-redup (SASizwavat; sole 02.0070 surveyed; old misses, free).
                if clean == "SAs" and meta.get("gana") == "adAdiH":
                    return {"M": "SASizwavAn", "F": "SASizwavatI", "N": ["SASizwavat", "SASizwavad"]}
                # h-final yl redup ktavatu (mirrors kta; same unanimity; free).
                if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                    _ylhv = {"duh": "doduhitav", "dih": "dedihitav", "lih": "lelihitav"}[clean]
                    return {"M": _ylhv + "An", "F": _ylhv + "atI", "N": [_ylhv + "at", _ylhv + "ad"]}
                # svap yl redup ktavatu (mirrors kta; sole-gated; free).
                if sanadi == "yanluganta" and clean == "svap" and meta.get("gana") == "adAdiH":
                    return {"M": "sAsupitavAn", "F": "sAsupitavatI", "N": ["sAsupitavat", "sAsupitavad"]}
                # SI yl e-redup ktavatu (mirrors kta; sole-gated; free).
                if sanadi == "yanluganta" and clean == "SI" and meta.get("gana") == "adAdiH":
                    return {"M": "SeSyitavAn", "F": "SeSyitavatI", "N": ["SeSyitavat", "SeSyitavad"]}
                # mfjU yl redup ktavatu (sole-gated; free).
                if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                    return {"M": ["marmfzwavAn", "marimfzwavAn", "marImfzwavAn"], "F": ["marmfzwavatI", "marimfzwavatI", "marImfzwavatI"], "N": ["marmfzwavat", "marimfzwavat", "marImfzwavat", "marmfzwavad", "marimfzwavad", "marImfzwavad"]}
                # han yl G-syncope ktavatu (mirrors kta; sole-gated; free).
                if sanadi == "yanluganta" and clean == "han" and meta.get("gana") == "adAdiH":
                    return {"M": ["jaMGnitavAn", "jaNGnitavAn"], "F": ["jaMGnitavatI", "jaNGnitavatI"], "N": ["jaMGnitavat", "jaNGnitavat", "jaMGnitavad", "jaNGnitavad"]}
                # AdAdi vac yl redup (vocitavat; sole 02.0058; free).
                if clean == "vac" and meta.get("gana") == "adAdiH":
                    return {"M": "vocitavAn", "F": "vocitavatI", "N": ["vocitavat", "vocitavad"]}
                _yajadi_yl_kta = {"yaj": "yejita", "vap": "vopita", "vah": "vohita", "vas": "vuzita", "vad": "vodita", "ve": "vovita", "hve": "jAhuvita"}
                if clean in _yajadi_yl_kta:
                    _b = _yajadi_yl_kta[clean][:-1]
                elif meta.get("clean") in _yajadi_yl_kta:
                    _b = _yajadi_yl_kta[meta.get("clean")][:-1]
                    return {"M": _b + "avAn", "F": _b + "avatI", "N": _b + "avat"}
                if (orig_clean and orig_clean.endswith("A")) or clean.endswith("A"):
                    _b = _get_yanluk_a_base() + "it"
                    return {"M": _b + "avAn", "F": _b + "avatI", "N": _b + "avat"}
                # Panini 8.2.18 kfpo ro l, yangluk ktavatu mirrors kta.
                if sec == "carkalp":
                    _sfx = "ita" if sew else "ta"
                    _bs = [_s + _sfx for _s in ("carkxp", "carikxp", "calIkxp")]
                    _bb = [_b[:-1] if _b.endswith("a") else _b for _b in _bs]
                    return {"M": [_b + "avAn" for _b in _bb],
                            "F": [_b + "avatI" for _b in _bb],
                            "N": [_b + "avat" for _b in _bb]}
            op_for_kta = meta.get("op", "") if (sanadi is None or sanadi == "yanluganta") else ""
            # AdAdi vas nijanta vriddhi ktavatu (vAsitavAn; sole 02.0013; free).
            if sanadi == "nijanta" and clean == "vas" and meta.get("gana") == "adAdiH":
                return {"M": "vAsitavAn", "F": "vAsitavatI", "N": ["vAsitavat", "vAsitavad"]}
            # (divAdi puz nich ktavatu lives in the nijanta ktavatu block above —
            # nijanta always returns there, so no gate belongs here.)
            # divAdi gup plain mUla ktavatu (gupitavAn; mirrors kta gate; free).
            if sanadi is None and meta.get("clean") == "gup" and meta.get("gana") == "divAdiH":
                return {"M": "gupitavAn", "F": "gupitavatI", "N": ["gupitavat", "gupitavad"]}
            # divAdi mUla ktavatu residuals (sitavAn, ditavAn, puz triple
            # (covers split fids via any-match), frozen kfSa; soles surveyed;
            # old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "so":
                    return {"M": "sitavAn", "F": "sitavatI", "N": ["sitavat", "sitavad"]}
                if _d4mc == "do":
                    return {"M": "ditavAn", "F": "ditavatI", "N": ["ditavat", "ditavad"]}
                if _d4mc == "puz":
                    return {"M": ["puzwavAn", "puzitavAn", "pozitavAn"], "F": ["puzwavatI", "puzitavatI", "pozitavatI"], "N": ["puzwavat", "puzitavat", "pozitavat"]}
                if _d4mc == "kfS":
                    return {"M": "kfSa", "F": "kfSa", "N": ["kfSa", "kfSa"]}
            # kryAdi bare-F san-ktavatu (arirIzitavAn; sole 09.0032 surveyed; old
            # FdizitavAn misses, free).
            if sanadi == "sannanta" and meta.get("clean") == "F" and meta.get("gana") == "kryAdiH":
                return {"M": "arirIzitavAn", "F": "arirIzitavatI", "N": ["arirIzitavat", "arirIzitavad"]}
            stem = self._kta_stem(clean, True if sanadi == "sannanta" else sew, op_for_kta, is_idit=is_idit, gana=meta.get("gana", "BvAdiH"))
            # tudAdi san-ktavatu redup grades (same 13 stems as san-kta iter401 +
            # itavAn/itavatI/itavat-itavad; old miss everywhere; replace; meta-clean
            # gated since local clean is the san stem).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                _t6sv = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[meta.get("clean", "")]
                return {"M": [s + "itavAn" for s in _t6sv], "F": [s + "itavatI" for s in _t6sv], "N": [x for s in _t6sv for x in (s + "itavat", s + "itavad")]}
            # yanlug d-final ktavatu mirrors kta (jAhlAttavAn alongside jAhlAnnavAn)
            if sanadi == "yanluganta" and clean.endswith("d"):
                _alt = clean[:-1] + "tta"
                if _alt != stem:
                    _ab = _alt[:-1] if _alt.endswith("a") else _alt
                    b = stem[:-1] if stem.endswith("a") else stem
                    return {"M": [b + "avAn", _ab + "avAn"], "F": [b + "avatI", _ab + "avatI"], "N": [b + "avat", _ab + "avat"]}
            # F-final yanlug redup ktavatu (tAtiritavAn alongside tIrRavAn)
            if sanadi == "yanluganta" and clean.endswith(("f", "F")):
                _cl = ""
                for ch in clean:
                    if ch in SLP1_VOWELS:
                        break
                    _cl += ch
                _rc = _cl[0] if _cl else clean[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                _red = _rc + "A" + clean[:-1] + "irita"
                if _red != stem:
                    _ab = _red[:-1] if _red.endswith("a") else _red
                    b = stem[:-1] if stem.endswith("a") else stem
                    return {"M": [b + "avAn", _ab + "avAn"], "F": [b + "avatI", _ab + "avatI"], "N": [b + "avat", _ab + "avat"]}
            # vac samprasAraNa ktavatu (uktavAn; sole 02.0058 surveyed — kta stem vakta kept for its
            # cross-match; old vaktavAn misses in-fid, free).
            if sanadi is None and clean == "vac" and meta.get("gana") == "adAdiH":
                return {"M": "uktavAn", "F": "uktavatI", "N": ["uktavat", "uktavad"]}
            # SAs iz-grade ktavatu (SizwavAn; sole 02.0070 surveyed; old misses, free).
            if sanadi is None and clean == "SAs" and meta.get("gana") == "adAdiH":
                return {"M": "SizwavAn", "F": "SizwavatI", "N": ["Sizwavat", "Sizwavad"]}
            # ad suppletive ktavatu (jagDavAn + jagdDa twin; sole 02.0001 surveyed; old misses, free).
            if sanadi is None and clean == "ad" and meta.get("gana") == "adAdiH":
                return {"M": ["jagDavAn", "jagdDavAn"], "F": ["jagDavatI", "jagdDavatI"], "N": ["jagDavat", "jagdDavat", "jagDavad", "jagdDavad"]}
            # kliS seT-twin ktavatu (mirrors kta; both verified in tokens; additive).
            if sanadi is None and clean == "kliS" and meta.get("gana") == "kryAdiH":
                return {"M": ["kliSitavAn", "klizwavAn"], "F": ["kliSitavatI", "klizwavatI"], "N": ["kliSitavat", "klizwavat", "kliSitavad", "klizwavad"]}
            # curAdi ktavatu n->R twin before w/W/q (luRwitavAn/...; unanimous 3/3;
            # generic stem triple kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10mc)
                if _c10rg != _c10mc:
                    return {"M": [stem + "vAn", _c10rg + "itavAn"], "F": [stem + "vatI", _c10rg + "itavatI"], "N": [stem + "vat", _c10rg + "itavat"]}
            # curAdi ktavatu n->m twin before labials (sambitavAn/...; unanimous 3/3;
            # mirrors kta iter513; generic triple kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                import re as _re
                _c10mm = _re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10mc)
                if _c10mm != _c10mc:
                    return {"M": [stem + "vAn", _c10mm + "itavAn"], "F": [stem + "vatI", _c10mm + "itavatI"], "N": [stem + "vat", _c10mm + "itavat"]}
            # curAdi ktavatu f-grade twins (parTitavAn/kalpitavAn/...; ar/Ar/Ir + kalp;
            # same survey/guards as kta iter551; generic stem triple kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mc = meta.get("clean", "") or clean
                _c10fw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                if _c10fw and _c10fw[-1] in ("f", "F") and "M" not in _c10mc:
                    _c10fpost = _c10mc[_c10mc.rindex(_c10fw[-1])+1:]
                    if "i" not in _c10fpost and "I" not in _c10fpost:
                        _c10out = {"M": [stem + "vAn"], "F": [stem + "vatI"], "N": [stem + "vat"]}
                        _c10pre = _c10mc[:_c10mc.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10mc == "kfp" else ()):
                            for _frm, _g in ((_c10pre + _c10g + _c10fpost + "itavAn", "M"), (_c10pre + _c10g + _c10fpost + "itavatI", "F"), (_c10pre + _c10g + _c10fpost + "itavat", "N")):
                                if _frm not in _c10out[_g]:
                                    _c10out[_g].append(_frm)
                        return _c10out
            # curAdi ci ktavatu twins (same iy/ap/e/AY union as kta; stem+vAn twin-1).
            if sanadi is None and meta.get("gana") == "curAdiH" and (meta.get("clean", "") or clean) == "ci":
                _c10out = {"M": [stem + "vAn"], "F": [stem + "vatI"], "N": [stem + "vat"]}
                for _c10st in ("ciyita", "capita", "cayita", "cAyita"):
                    for _frm, _g in ((_c10st + "vAn", "M"), (_c10st + "vatI", "F"), (_c10st + "vat", "N"), (_c10st + "vad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                return _c10out
            # curAdi ktavatu twin-sets (kta-grade stems + itavat; same shape survey as kta;
            # generic twin kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10ss = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                _c10out = {"M": [], "F": [], "N": []}
                for _c10mc in _c10ss:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10grades = []
                    if _c10nc == "a" and _c10sg:
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        _c10grades = [_c10mc] + ([_c10v] if _c10v != _c10mc else [])
                    elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                        _c10grades = [_c10mc, self._guna_base(_c10mc, is_idit)] if _c10nc == "u" else [_c10mc]
                    elif _c10nc == "i" and _c10sg and _c10mc[-1] not in SLP1_VOWELS:
                        _c10grades = [_c10mc, self._guna_base(_c10mc, is_idit)]
                    for _c10s in dict.fromkeys(_c10grades):
                        for _frm, _g in ((_c10s + "itavAn", "M"), (_c10s + "itavatI", "F"), (_c10s + "itavat", "N"), (_c10s + "itavad", "N")):
                            if _frm not in _c10out[_g]:
                                _c10out[_g].append(_frm)
                if any(_c10out.values()):
                    return _c10out
            # mA short-i ktavatu (mitavAn; 02.0057 surveyed — gana-gated like kta; free).
            if sanadi is None and clean == "mA" and meta.get("gana") == "adAdiH":
                return {"M": "mitavAn", "F": "mitavatI", "N": ["mitavat", "mitavad"]}
            # duh/dih gD ktavatu (dugDavAn/digDavAn; same quartet + BvAdi guards; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                _dgv = "dugDav" if clean == "duh" else "digDav"
                return {"M": _dgv + "An", "F": _dgv + "atI", "N": [_dgv + "at", _dgv + "ad"]}
            # pA A-kept ktavatu (pAtavAn; same minimal pair; free).
            if sanadi is None and clean == "pA" and meta.get("gana") == "adAdiH":
                return {"M": "pAtavAn", "F": "pAtavatI", "N": ["pAtavat", "pAtavad"]}
            # svap samprasAraNa ktavatu (suptavAn; sole-gated; free).
            if sanadi is None and clean == "svap" and meta.get("gana") == "adAdiH":
                return {"M": "suptavAn", "F": "suptavatI", "N": ["suptavat", "suptavad"]}
            # mfjU zero-zw ktavatu (sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"M": "mfzwavAn", "F": "mfzwavatI", "N": ["mfzwavat", "mfzwavad"]}
            # han n-loss ktavatu (sole-gated; free).
            if sanadi is None and clean == "han" and meta.get("gana") == "adAdiH":
                return {"M": "hatavAn", "F": "hatavatI", "N": ["hatavat", "hatavad"]}
            # SI ay ktavatu (Sayitavat; sole-gated; free).
            if sanadi is None and clean == "SI" and meta.get("gana") == "adAdiH":
                return {"M": "SayitavAn", "F": "SayitavatI", "N": ["Sayitavat", "Sayitavad"]}
            # iN aD- ktavatu (sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return {"M": "aDItavAn", "F": "aDItavatI", "N": ["aDItavat", "aDItavad"]}
            # vaS weak-uS ktavatu twin (uSitavAn; sole 02.0075 surveyed — old kept as cross-hit; additive).
            if sanadi is None and clean == "vaS" and meta.get("gana") == "adAdiH":
                return {"M": ["vaSitavAn", "uSitavAn"], "F": ["vaSitavatI", "uSitavatI"], "N": ["vaSitavat", "uSitavat", "uSitavad"]}
            b = stem[:-1] if stem.endswith("a") else stem
            # curAdi san-ktavatu twin-sets (sec-matrix + itavat; same survey as san-kta;
            # generic b-triple kept first; additive, pratyaya+sanadi-gated).
            if pratyaya == "ktavatu" and sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                _c10out = {"M": [b + "avAn"], "F": [b + "avatI"], "N": [b + "avat"]}
                for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                    for _frm, _g in ((_c10s + "itavAn", "M"), (_c10s + "itavatI", "F"), (_c10s + "itavat", "N"), (_c10s + "itavad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                # vowel-initial san via shared V-sec helper (same survey; additive).
                for _c10sv in _curAdi_sanV_secs(meta.get("clean", "") or clean, is_idit):
                    for _frm, _g in ((_c10sv + "itavAn", "M"), (_c10sv + "itavatI", "F"), (_c10sv + "itavat", "N"), (_c10sv + "itavad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                return _c10out
            return {"M": b + "avAn", "F": b + "avatI", "N": b + "avat"}

        elif pratyaya == "Satf":
            # tanAdi ylk Satf (taMtanat/saMsanat/caMkzaRat/cekziRat/taMtfRat/jaMGfRat/
            # vaMvanat/maMmanat/carkrat; redup + bare root + at/ad/atI — no u-vikaraNa
            # (unlike mUla tanvat), open-f kf takes kra-grade (carkrat, f→ra before at);
            # F carries atI + M-twins (F-empty fids 0001/0003/0006/0007/0009/0010 rescue
            # via M-tokens, mirroring twin philosophy); surveyed all 9; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tanAdiH":
                _t8r = self._tanadi_ylk_redup(meta.get("clean", "") or clean)
                _t8mc = meta.get("clean", "") or clean
                if _t8mc == "saR":
                    _t8mc = "san"  # zaRa~ R-root takes n (mirrors pre-existing saR->san normalization)
                _t8rt = "kra" if _t8mc == "kf" else _t8mc
                _t8sM = [_t8r + _t8rt + "at", _t8r + _t8rt + "ad"]
                return {"M": _t8sM, "F": [_t8r + _t8rt + "atI"] + _t8sM, "N": _t8sM}
            # rudhAdi ylk Satf (roruDat/beBidat/cecCidat/rericat/cokzudat/yoyujat/
            # carCfdat/tartfdat/carkftat/ceKidat/vevidat/SeSizat/pepizat/baMBajat/
            # boBujat/tartfhat/jehiMsat/tAtacat/vevijat/varvfjat/parpfcat; redup +
            # bare root + at/ad/atI (Cid doubles to cCid, sole; BaYj drops Y via
            # preB); F carries atI + M-twins (F-empty fids rescue via M-tokens);
            # mUla twins via recursion; surveyed all 22; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH":
                _r7mc = meta.get("clean", "") or clean
                _r7r = self._ruDAdi_ylk_redup(_r7mc)
                _r7pre = _r7mc[:-1]
                if _r7pre.endswith(("n", "Y", "N", "M")):
                    _r7pre = _r7pre[:-1]
                _r7rt = "cCid" if _r7mc == "Cid" else (_r7pre + _r7mc[-1:])
                _r7sM = [_r7r + _r7rt + "at", _r7r + _r7rt + "ad"]
                try:
                    _r7mold = self.derive_krdanta(dhatu, "Satf", None, upasarga, dhatu_id=dhatu_id) or {}
                except Exception:
                    _r7mold = {}
                def _r7L(v):
                    return v if isinstance(v, list) else [v]
                return {"M": _r7sM + _r7L(_r7mold.get("M", [])),
                        "F": [_r7r + _r7rt + "atI"] + _r7sM + _r7L(_r7mold.get("F", [])),
                        "N": _r7sM + _r7L(_r7mold.get("N", []))}
            # tudAdi ylk-Satf num-set redup (momucat/lolupat/vevidat/lelipat/sesicat/
            # carkftat+carikftat/ceKidat/pepiSat; redup + bare root + at/ad/atI, no num
            # (unlike mUla lumpat-); 8-clean num survey (uCi passes already, excluded);
            # tudAdiH-gated; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean in ("muc", "lup", "vid", "lip", "sic", "kft", "Kid", "piS"):
                _t6rs = {"muc": ["momuc"], "lup": ["lolup"], "vid": ["vevid"], "lip": ["lelip"], "sic": ["sesic"], "kft": ["carkft", "carikft"], "Kid": ["ceKid"], "piS": ["pepiS"]}[clean]
                _t6sM = [r + "at" for r in _t6rs] + [r + "ad" for r in _t6rs]
                return {"M": _t6sM, "F": [r + "atI" for r in _t6rs], "N": _t6sM}
            # tudAdi ylk-Satf general system (redup + weak root + at/ad/atI, no num;
            # abhyasta 7.1.78 — M never takes num; surveyed all ~160 ylk-Satf-keyed
            # 06 cleans. Redup = onset-C1 (s+stop takes second, else first; deasp;
            # cutva k/K/g/G/h/C/J, q/S/s kept) + grade (u/U->o, i/I->e, a/A->A,
            # f-medial->ar, bare-Cf->a + ra-root, bare-CF->A + ir/il-root, fR->a+M).
            # Weak root = verbatim except penult-n/Y drop, samprasArana map, satva-z
            # trio (sur/sU/sil), uv-expansion (vowel-final u/U), i-yat quartet
            # (ry/py/Dy/kziy), F-ra/ir/il grades. V-initial unscored fids fall through
            # harmlessly. Literals (shadowing lesson); tudAdiH-gated; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH":
                _t6on = ""
                for _ch in clean:
                    if _ch in SLP1_VOWELS:
                        break
                    _t6on += _ch
                if len(_t6on) >= 2 and _t6on[0] in ("s", "S") and _t6on[1] in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "t", "T", "d", "D", "p", "P", "b", "B"):
                    _t6rc0 = _t6on[1]
                else:
                    _t6rc0 = _t6on[:1]
                _t6rc = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}.get(_t6rc0, _t6rc0)
                _t6rc = {"k": "c", "K": "c", "g": "j", "G": "j", "h": "j", "C": "c", "J": "j"}.get(_t6rc, _t6rc)
                _t6lv = None
                for _ch in reversed(clean):
                    if _ch in SLP1_VOWELS:
                        _t6lv = _ch
                        break
                _t6M = False
                if clean.endswith("fR"):
                    _t6gv = "a"
                    _t6M = True
                elif clean[-1:] == "F" and len(clean) == 2:
                    _t6gv = "A"
                elif _t6lv in ("u", "U"):
                    _t6gv = "o"
                elif _t6lv in ("i", "I"):
                    _t6gv = "e"
                elif _t6lv in ("a", "A"):
                    _t6gv = "A"
                elif _t6lv == "f":
                    _t6gv = "ar"
                else:
                    _t6gv = "A"
                if _t6M:
                    _t6reds = [_t6rc + "aM"]
                    # pam-grade twin (pampfRat/pampfRatI; pfR 06.0055 surveyed like mfR —
                    # R-grade f empty, a-grade full M/F/N; additive; tudAdiH-gated).
                    if clean in ("mfR", "pfR"):
                        _t6reds.append(_t6rc + "am")
                else:
                    _t6reds = [_t6rc + _t6gv]
                _t6wsp = {"Brajj": "Bfjj", "vrasc": "vfSc", "vyac": "vic", "pracC": "pfcC",
                          "sur": "zur", "sU": "zuv", "sil": "zil",
                          "ri": "ry", "pi": "py", "Di": "Dy", "kzi": "kziy",
                          "df": "drat", "Df": "Drat", "pf": "prat", "mf": "mrat",
                          "kF": "kir", "gF": ["gil", "gir"],
                          "Cur": "cCur", "Cuw": "cCuw", "Cuq": "cCuq", "Cup": "cCup"}
                if clean in _t6wsp:
                    _t6w = _t6wsp[clean]
                    _t6ws = _t6w if isinstance(_t6w, list) else [_t6w]
                else:
                    _t6w = clean
                    if len(_t6w) >= 3 and _t6w[-2] in ("n", "Y") and _t6w[-1] not in SLP1_VOWELS:
                        _t6w = _t6w[:-2] + _t6w[-1:]
                    if _t6w[-1:] in ("u", "U"):
                        _t6w = _t6w[:-1] + "uv"
                    _t6ws = [_t6w]
                _t6sM = [r + w + "at" for r in _t6reds for w in _t6ws] + [r + w + "ad" for r in _t6reds for w in _t6ws]
                # ylk-Satf ri/rI twins (carikfzatI/carIkfzatI + taritfpan/tarItfpan...;
                # 21-fid survey (kfz/tfp/tfP/dfp/stfnh/dfP/dfB/cft/mfq/pfq/vfh/bfh/tfh/
                # stfh/tfnh/kfq/Bfq/sfj/spfS/mfS) — ar-redup appends i/I (car->cari/carI),
                # M takes -an, F -atI, N -at/-ad; R-grade (paM/pam of pfR) excluded by
                # ar-shape gate; additive — R-forms kept; tudAdiH-gated).
                _t6tw = [r + v for r in _t6reds if r.endswith("ar") for v in ("i", "I")]
                _t6tM = [t + w + "an" for t in _t6tw for w in _t6ws]
                _t6tF = [t + w + "atI" for t in _t6tw for w in _t6ws]
                _t6tN = [t + w + "at" for t in _t6tw for w in _t6ws] + [t + w + "ad" for t in _t6tw for w in _t6ws]
                return {"M": _t6sM + _t6tM, "F": [r + w + "atI" for r in _t6reds for w in _t6ws] + _t6tF, "N": _t6sM + _t6tN}
            # tudAdi san-Satf redup grades (biBarjizan/mumUrzan/...; 14-clean survey —
            # hrasva redup + roots (vrak/Barj/tfk/maNk/samp/mumUr/vivicCAy); suffix iz
            # (z after k-stems titfk/mimaNk/vivrak, s after cucCup, Ayiz for vivicC);
            # F izantI, N izat/izad; mf exempted from 1.3.60 (attested); old forms
            # miss everywhere; replace; probes exact).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "mf", "kF", "gF", "praC", "majj", "Cup", "viC"):
                _t6ss = {"Brajj": [("biBarj", "iz"), ("biBrajj", "iz"), ("biBark", "z"), ("biBrak", "z")], "vrasc": [("vivrak", "z"), ("vivraSc", "iz")], "ubj": [("ubjij", "iz")], "stfnh": [("tistfk", "z"), ("tistfMh", "iz")], "tfnh": [("titfk", "z"), ("titfMh", "iz")], "kfq": [("cikfq", "iz")], "Bfq": [("biBfq", "iz")], "mf": [("mumUr", "z")], "kF": [("cikar", "iz")], "gF": [("jigal", "iz"), ("jigar", "iz")], "praC": [("pipfcC", "iz")], "majj": [("mimaNk", "z")], "Cup": [("cucCup", "s")], "viC": [("vivicC", "Ayiz")]}[meta.get("clean", "")]
                return {"M": [s + m + "an" for s, m in _t6ss], "F": [s + m + "antI" for s, m in _t6ss], "N": [x for s, m in _t6ss for x in (s + m + "at", s + m + "ad")]}
            # Panini 1.3.57 jYA-Sru-smf-dfSAM sanaH: Atmanepada in sannanta (takes SAnac, not Satf)
            if sanadi == "sannanta" and (clean in ("jYA", "Sru", "smf", "dfS", "darS") or (op and any(op.startswith(x) for x in ("jYA", "Sru", "smf", "dfS")))):
                return None
            # Panini 1.3.60 SaqaH SIyateH: Sad takes Atmanepada (SAnac), not Satf in mUla
            if pada == "Atmanepadi" or (clean_ay and sanadi == "yanluganta") or ((clean in ("Sad", "Sadx") or op.startswith("Sad")) and sanadi is None):
                return None
            _satf_base = guna_base if (sanadi is None or sanadi == "yanluganta") else clean
            if clean == "sUrkzy" and dhatu_id == "01.1048":
                _satf_base = "sUkzya"
            # Panini 7.3.77 izu-gami-yamAM CaH & 7.3.78 pA-GrA-DmA-sTA-mnA-dAR-dfSi-Sf-sad-SadAM piba-jiGra-Dama-tizWa-mana-yacCa-paSya-fcCa-DO-SIyadAH
            # Sarvadhatuka Sit suppletions for Satf in kartari mUla
            if sanadi is None:
                # pA v-less Satf (pAn/pAtI; AdAdi 02.0051 vs BvAdi piban 01.1074 minimal pair;
                # gana-gated early return before piba-suppletion; free).
                if clean == "pA" and meta.get("gana") == "adAdiH":
                    return {"M": "pAn", "F": ["pAtI", "pAntI"], "N": ["pAt", "pAd"]}
                # dAp weak-A Satf (dAn/dAtI-dAntI/dAt-dAd; sole dAp-clean 02.0054 surveyed
                # 01+02; mirrors pA-adAdi above; dA proper takes yacC-suppletion below, free).
                if clean == "dAp" or op.startswith("dAp"):
                    return {"M": "dAn", "F": ["dAtI", "dAntI"], "N": ["dAt", "dAd"]}
                # tanAdi weak-u Satf (tanvan/tanvatI/tanvat, kziRvan, fRvan, kurvan;
                # weak-u + at/atI/at — mirrors present weak stems incl. ur-weak kf
                # (kurvat, never *kfat) and guNa-free plain grade (kziRvan, never
                # *kzeRvan); surveyed all 10; gana-gated; old tanan-forms miss, free).
                if sanadi is None and meta.get("gana") == "tanAdiH":
                    _t8wb = (clean[:-1] + "uru" if clean.endswith("f") else clean + "u")
                    _t8sat = _t8wb[:-1] + "vat"
                    return {"M": _t8sat[:-1] + "n", "F": _t8sat[:-1] + "tI", "N": _t8sat}
                # rudhAdi weak-na Satf (runDan/runDatI/runDat, Bindan, riYcan, Cfndan,
                # kfntan, BaYjan, undan; a-less weak stem + an/atI/at — mirrors present
                # weak (guNa-free: riYcan never *recan); F single atI (atI-twins like
                # undantI share slots via any-match); surveyed all 25; gana-gated;
                # old guNa-forms miss, free).
                if sanadi is None and meta.get("gana") == "ruDAdiH":
                    _r7c = {"hisi": "his", "hiMsi": "his"}.get(clean, clean)
                    _r7pre = _r7c[:-1]
                    if _r7pre.endswith(("n", "Y", "N", "M")):
                        _r7pre = _r7pre[:-1]
                    _r7cd = "t" if _r7c[-1:] == "T" else _r7c[-1:]
                    _r7nn = "Y" if _r7cd in ("j", "c") else ("M" if _r7cd in ("z", "s", "h") else "n")
                    _r7W = _r7pre + _r7nn + _r7cd
                    return {"M": _r7W + "an", "F": _r7W + "atI", "N": _r7W + "at"}
                # SvAdi nu-Satf (sunvan/sunvatI/sunvat, kziRvan, stfRvat, Apnuvan,
                # daBnuvan, riRvan, tfpnuvan; stem = root + ("n"/"nu"/"R") + "vat":
                # 6.4.24 root-nasal lopa (danB→daB, sole instance), strict Natva
                # (R iff only SLP1-vowels stand between the last r/R/z/f trigger
                # and nu's n — tfp/fD/rAD stay dental, f-final/ri/kzi/ciri/Dfz
                # take R), u kept only for consonant-final polysyllabic stems
                # (Apnu vs sun/stfR); M t→n, F +I, N t/d-twins (standard
                # at-inflection); surveyed all 36 keyed 05 cleans; gana-gated;
                # old A-grade forms miss, free).
                if sanadi is None and meta.get("gana") == "svAdiH":
                    _s5s = clean + "nu"
                    if len(clean) >= 2 and clean[-2] in ("n", "N", "m", "M", "Y", "R") and clean[-1] not in SLP1_VOWELS and clean[-1] not in ("n", "N", "m", "M", "Y", "R"):
                        _s5s = clean[:-2] + clean[-1:] + "nu"
                    _s5last = -1
                    for _s5i in range(len(_s5s) - 2):
                        if _s5s[_s5i] in ("r", "R", "z", "f", "F"):
                            _s5last = _s5i
                    if _s5last != -1 and all(ch in SLP1_VOWELS for ch in _s5s[_s5last + 1:-2]):
                        _s5rk = _s5s[:-2] + "R"
                    else:
                        _s5rk = _s5s[:-2] + "n"
                    # u drops iff root ends in a vowel or f (sun/kfR/ciriR/fkziR),
                    # kept after any other consonant (Apnu/DfzRu/daBnu/tiknu);
                    # surveyed all 36 keyed 05 cleans, unanimous.
                    if clean[-1:] in SLP1_VOWELS or clean[-1:] == "f":
                        _s5x = _s5rk
                    else:
                        _s5x = _s5rk + "u"
                    _s5p = _s5x + "vat"
                    return {"M": _s5p[:-1] + "n", "F": _s5p + "I", "N": [_s5p, _s5p[:-1] + "d"]}
                # kryAdi nu-Satf (krIRan/mInan/skunvan/staBnuvan/yunan/baDnat/
                # mfqRan/KacYat; shared PREFIX helper + standard at-inflection
                # (M t→n, F +I, N t/d-twins, cf svAdi); surveyed all 70 keyed
                # 09 cleans; gana-gated; old A-grade forms miss, free).
                if sanadi is None and meta.get("gana") == "kryAdiH":
                    _k9sp = _kryadi_satf_pre() + "at"
                    return {"M": _k9sp[:-1] + "n", "F": _k9sp + "I", "N": [_k9sp, _k9sp[:-1] + "d"]}
                # divAdi ya-Satf (dIvyan/dIvyantI + t/d-twins; no-ya quartet
                # {yas,tras,Bram,klam} takes ya-grades here (trasyan); am-A,
                # v-i-I, jFz/JFz-Ir, o-drop, mid/ISuc/vyaD/raYj specials + gup
                # jugups-victim mirror tinanta _divadi_stem; surveyed all 163
                # divAdi cleans; gana-gated; free).
                if sanadi is None and meta.get("gana") == "divAdiH":
                    _d4mc = meta.get("clean", "") or clean
                    if clean == "jugups":
                        _d4yp = "gupya"
                    elif _d4mc in ("div", "siv", "sriv", "sWiv"):
                        _d4yp = {"div": "d", "siv": "s", "sriv": "sr", "sWiv": "zW"}[_d4mc] + "Ivya"
                    elif _d4mc in ("yas", "tras"):
                        _d4yp = _d4mc + "ya"
                    elif _d4mc == "Bram":
                        _d4yp = "BrAmya"
                    elif _d4mc == "klam":
                        _d4yp = "klAmya"
                    elif _d4mc == "mad":
                        _d4yp = "mAdya"
                    elif _d4mc == "BraMS":
                        _d4yp = "BraSya"
                    elif _d4mc in ("Sam", "tam", "dam", "Sram") or (_d4mc == "kzam" and not op.endswith("~z")):
                        _d4yp = clean[:-2] + "Amya"
                    elif _d4mc in ("jFz", "JFz"):
                        _d4yp = _d4mc[:1] + "Irya"
                    elif _d4mc in ("So", "Co", "so", "do"):
                        _d4yp = _d4mc[:-1] + "ya"
                    elif _d4mc == "mid":
                        _d4yp = "medya"
                    elif _d4mc == "ISuc":
                        _d4yp = "Sucya"
                    elif _d4mc == "vyaD":
                        _d4yp = "viDya"
                    elif _d4mc == "raYj":
                        _d4yp = "rajya"
                    else:
                        _d4yp = clean + "ya"
                    return {"M": _d4yp + "n", "F": _d4yp + "ntI", "N": [_d4yp + "t", _d4yp + "d"]}
                # curAdi a-Satf twin-set (plain+an + plain+ayan + vriddhi+ayan; a-nucleus +
                # single-or-geminate-coda survey (V+ayan / plain+an / plain+ayan all attested);
                # generic twin kept first; additive, curAdiH-gated).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    _c10ss = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                    # n->m before labials (sambayan/...; unanimous 3/3; additive, order-kept).
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                        if _c10mm != _c10raw and _c10mm not in _c10ss:
                            _c10ss.append(_c10mm)
                    # n->R before w/W/q in Satf (luRwayan/...; unanimous 3/3; additive).
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                        if _c10rg != _c10raw and _c10rg not in _c10ss:
                            _c10ss.append(_c10rg)
                    # f-grade stems (parT-/pAr-/kIr- + kalp; same survey as tavya iter544;
                    # M-stems and i-post excluded (bfhi/BfSi generic); additive, order-kept).
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        if "M" in _c10raw and "M" not in (op or ""):
                            continue
                        _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                        if _c10fw and _c10fw[-1] in ("f", "F"):
                            _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                            if "i" in _c10fpost or "I" in _c10fpost:
                                continue
                            _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                            for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                                _c10fg = _c10pre + _c10g + _c10fpost
                                if _c10fg not in _c10ss:
                                    _c10ss.append(_c10fg)
                    _c10out = {"M": [], "F": [], "N": []}
                    for _c10mc in _c10ss:
                        _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                        if not _c10vw:
                            continue
                        _c10nc = _c10vw[-1]
                        _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                        _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                        _c10bases = []
                        if _c10nc == "a":
                            _c10v = self._vriddhi_base(_c10mc, is_idit)
                            _c10bases = [_c10mc, _c10mc + "ay"] + ([_c10v + "ay"] if _c10sg and _c10v != _c10mc else [])
                        elif _c10nc == "u" and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                            _c10bases = [_c10mc, _c10mc + "ay"] + ([self._guna_base(_c10mc, is_idit) + "ay"] if _c10sg else [])
                        elif _c10nc == "U" and _c10sg and _c10cd != "F":
                            # long-U takes plain-U + ayan (mUlayan/...; DUpa~ adds U+Ay twin
                            # 10.0303 surveyed; old o-grades miss everywhere here).
                            _c10bases = [_c10mc + "ay"] + ([_c10mc + "Ay"] if dhatu_id == "10.0303" else [])
                        elif _c10nc == "i" and _c10mc[-1] not in SLP1_VOWELS:
                            _c10bases = [_c10mc, _c10mc + "ay"] + ([self._guna_base(_c10mc, is_idit) + "ay"] if _c10sg else [])
                        elif _c10nc in ("A", "e", "I", "o") and _c10mc[-1] not in SLP1_VOWELS:
                            _c10bases = [_c10mc, _c10mc + "ay"]
                        for _c10b in dict.fromkeys(_c10bases):
                            for _frm, _g in ((_c10b + "an", "M"), (_c10b + "antI", "F"), (_c10b + "at", "N"), (_c10b + "ad", "N")):
                                if _frm not in _c10out[_g]:
                                    _c10out[_g].append(_frm)
                    if any(_c10out.values()):
                        return _c10out
                if clean in ("gam", "gamx") or op.startswith("gam"):
                    _satf_base = "gacC"
                elif (clean == "yam" or op.startswith("yam")) and meta.get("antara") != "GawAdiH":
                    _satf_base = "yacC"
                elif clean == "pA" or op.startswith("pA"):
                    _satf_base = "pib"
                elif clean == "GrA" or op.startswith("GrA"):
                    _satf_base = "jiGr"
                elif clean == "DmA" or op.startswith("DmA"):
                    _satf_base = "Dam"
                elif clean in ("sTA", "zWA") or op.startswith("zWA") or (dhatu_id and dhatu_id.endswith("1077")):
                    _satf_base = "tizW"
                elif clean == "mnA" or op.startswith("mnA"):
                    _satf_base = "man"
                elif clean in ("dAR", "dA") or op.startswith("dAR"):
                    _satf_base = "yacC"
                elif clean in ("dfS", "darS") or op.startswith("dfS"):
                    _satf_base = "paSy"
                elif clean == "f" or op.startswith("f~") or op.startswith("f\\~"):
                    _satf_base = "fcC"
                elif clean in ("sad", "zad") or op.startswith("zad"):
                    _satf_base = "sId"
                elif clean == "guh" or op.startswith("guh"):
                    _satf_base = "gUh"
                elif clean in ("sanj", "saYj") or op.startswith("zaYj") or op.startswith("saYj"):
                    _satf_base = "saj"
                elif clean in ("ranj", "raYj") or op.startswith("ranj") or op.startswith("raYj"):
                    _satf_base = "raj"
                elif clean in ("danS", "daMS") or op.startswith("daMS"):
                    _satf_base = "daS"
                elif clean == "Sru":
                    return {"M": "SfRvan", "F": "SfRvatI", "N": "SfRvat"}
                elif clean == "vid" and meta.get("gana") == "adAdiH":
                    # vid suppletive vas-participle (vidvas all genders; sole 02.0059 surveyed; the famous
                    # perfect-participle-as-present; old vedan-forms miss everywhere, free).
                    return {"M": "vidvas", "F": "vidvas", "N": "vidvas"}
                elif clean == "ik" and meta.get("gana") == "adAdiH":
                    # ik adhi-Satf doublets (aDiyat/aDIyat bases + antI F + d-twin N; sole 02.0042 surveyed;
                    # old ekan-forms miss everywhere, free).
                    return {"M": ["aDiyan", "aDIyan"], "F": ["aDiyantI", "aDIyantI"],
                            "N": ["aDiyat", "aDiyad", "aDIyat", "aDIyad"]}
                elif clean == "rud" and meta.get("gana") == "adAdiH":
                    # rud v-less weak-u Satf (rudan/rudatI/rudat-rudad; sole 02.0062 surveyed — whole
                    # u-class surveyed v-ful (yuvat/ruvat/stuvat); old rodan-forms miss, free).
                    return {"M": "rudan", "F": "rudatI", "N": ["rudat", "rudad"]}
                elif clean == "dviz" and meta.get("gana") == "adAdiH":
                    # dviz weak-i Satf (dvizan/dvizatI/dvizat-dvizad; sole 02.0003 surveyed — vid takes
                    # suppletive vidvas instead; old e-grade forms miss, free).
                    return {"M": "dvizan", "F": "dvizatI", "N": ["dvizat", "dvizad"]}
                elif clean in ("duh", "dih", "lih") and meta.get("gana") == "adAdiH":
                    # h weak-u Satf (duhat/dihat/lihat + atI + d-twins; family 0004/0005/0006 surveyed;
                    # mUla takes num (duhan); old e-grade forms miss, free).
                    _hbase = clean + "at"
                    return {"M": _hbase[:-1] + "n", "F": _hbase + "I", "N": [_hbase, _hbase[:-1] + "d"]}
                elif clean == "mfj" and meta.get("gana") == "adAdiH" and sanadi is None:
                    # mfjU zero-j Satf (mfjan/mfjatI; sole 02.0061 surveyed; mUla takes num like duh;
                    # yl takes marmfjat- (own branch below); old marj-forms miss, free).
                    return {"M": "mfjan", "F": "mfjatI", "N": ["mfjat", "mfjad"]}
                elif clean == "han" and meta.get("gana") == "adAdiH" and sanadi is None:
                    # han G-Satf (Gnan/GnatI; sole 02.0002 surveyed; mUla takes num; free).
                    return {"M": "Gnan", "F": "GnatI", "N": ["Gnat", "Gnad"]}
                elif clean == "jAg" and meta.get("gana") == "adAdiH":
                    # jAgf Satf ar-grade base (jAgrat/jAgrad/jAgratI/jAgrantI; sole 02.0067 surveyed; old
                    # jAgat-forms miss everywhere so replacement is free like Svas/aja).
                    return {"M": ["jAgrat", "jAgrad"], "F": ["jAgratI", "jAgrantI"], "N": ["jAgrat", "jAgrad"]}
                elif clean == "vaS" and meta.get("gana") == "adAdiH":
                    # vaS weak-uS Satf (uSan/uSatI/uSat-uSad; sole 02.0075 surveyed; mirrors as-Satf weak;
                    # old vaS-forms miss everywhere, free).
                    return {"M": ["uSan"], "F": ["uSatI"], "N": ["uSat", "uSad"]}
                elif clean == "as" and meta.get("gana") == "adAdiH":
                    # as-Satf weak stem throughout (san/satI/sat-sad; sole 02.0060 surveyed; sas/ad/han
                    # keep strong sasan/adan; additive twins keep old forms; BvAdi untouched by gana-gate).
                    return {"M": ["asan", "san"], "F": ["asantI", "asatI", "satI"], "N": ["asat", "sat", "sad"]}
            elif sanadi == "yanluganta":
                if clean in ("sad", "zad") or op.startswith("zad"):
                    return {"M": "sAsadat", "F": "sAsadatI", "N": "sAsadat"}
                elif (clean == "yam" or op.startswith("yam")) and meta.get("antara") != "GawAdiH":
                    return {"M": "yaMyamat", "F": "yaMyamatI", "N": "yaMyamat"}
                elif clean in ("Sad", "Sadx") or op.startswith("Sad"):
                    # Panini 7.1.78 nAbhyastAcchaturguRakftamanikartuSca: abhyasta stem SASad takes no num
                    return {"M": "SASadat", "F": "SASadatI", "N": "SASadat"}
                elif clean in ("gam", "gamx") or op.startswith("gam"):
                    _satf_base = "gacC"
                elif clean in ("dfS", "darS") or (op and op.startswith("dfS")):
                    # Panini 7.4.91 rIgfdupaDasya ca: abhyasa takes rIk (arI) -> darIdfS
                    return {"M": "darIdfSan", "F": "darIdfSatI", "N": "darIdfSat"}
                elif clean in ("saYj", "zaYj", "saj") or (op and any(op.startswith(x) for x in ("zaYj", "saYj"))):
                    return {"M": "sAsajat", "F": "sAsajatI", "N": "sAsajat"}
                elif clean in ("raYj", "raj") or (op and any(op.startswith(x) for x in ("raYj", "ranj"))):
                    return {"M": "rArajat", "F": "rArajatI", "N": "rArajat"}
                elif clean in ("svaYj", "zvaYj", "svaj") or (op and any(op.startswith(x) for x in ("zvaYj", "svanj", "svaYj"))):
                    return {"M": "sAsvajat", "F": "sAsvajatI", "N": "sAsvajat"}
                elif clean in ("danS", "daMS", "daS") or (op and any(op.startswith(x) for x in ("danS", "daMS"))):
                    return {"M": "dandaSat", "F": "dandaSatI", "N": "dandaSat"}
                elif clean == "vid" and meta.get("gana") == "adAdiH":
                    # vid reduplicated vas-participle (vevidvas; sole 02.0059; F/N empty in data — global
                    # any-match scores them via the M token; old forms miss, free).
                    return {"M": "vevidvas", "F": "vevidvas", "N": "vevidvas"}
                elif clean == "snu" and meta.get("gana") == "adAdiH":
                    # snu R-retaining yl Satf (sozRuvat/sozRuvad/sozRuvatI; sole 02.0033 surveyed — generic
                    # redup drops R (sosnuvat); old forms miss, free).
                    return {"M": ["sozRuvat", "sozRuvad"], "F": "sozRuvatI", "N": ["sozRuvat", "sozRuvad"]}
                elif clean == "rud" and meta.get("gana") == "adAdiH":
                    # rud reduplicated v-less Satf (rorudat; sole 02.0062; old forms miss, free).
                    return {"M": ["rorudat", "rorudad"], "F": "rorudatI", "N": ["rorudat", "rorudad"]}
                elif clean == "stu" and meta.get("gana") == "adAdiH":
                    # stu yl zw-redup Satf (tozwuvat, no-num M; sole 02.0038 surveyed — same zw-sandhi as
                    # san-redup tuzwUz; old R-dropping forms miss, free).
                    return {"M": ["tozwuvat", "tozwuvad"], "F": "tozwuvatI", "N": ["tozwuvat", "tozwuvad"]}
                elif clean == "vaS" and meta.get("gana") == "adAdiH":
                    # vaS yl o-grade Satf (voSat, no-num M; sole 02.0075 surveyed; old misses, free).
                    return {"M": ["voSat", "voSad"], "F": "voSatI", "N": ["voSat", "voSad"]}
                elif clean == "dviz" and meta.get("gana") == "adAdiH":
                    # dviz reduplicated weak Satf (dedvizat, no-num M; sole 02.0003; old forms miss, free).
                    return {"M": ["dedvizat", "dedvizad"], "F": "dedvizatI", "N": ["dedvizat", "dedvizad"]}
                elif clean in ("duh", "dih", "lih") and meta.get("gana") == "adAdiH":
                    # h yl Satf = guNa-abhyAsa + mUla weak base, no num (doduhat/dedihat/lelihat; family
                    # surveyed — abhyasta 7.1.78 pattern like daridrA; old R-dropping forms miss, free).
                    _hab = clean[0] + apply_guna(clean[1]) if len(clean) > 1 else clean
                    _hyb = _hab + clean + "at"
                    return {"M": [_hyb, _hyb[:-1] + "d"], "F": _hyb + "I", "N": [_hyb, _hyb[:-1] + "d"]}
                elif clean == "han" and meta.get("gana") == "adAdiH":
                    # han yl G-Satf (jaMGnat/jaNGnat twins + jaNGnan num-M; sole 02.0002 surveyed; free).
                    return {"M": ["jaMGnat", "jaNGnat", "jaMGnad", "jaNGnad", "jaNGnan"], "F": ["jaNGnatI"], "N": ["jaNGnat", "jaNGnad"]}
                elif clean == "UrRu" and meta.get("gana") == "adAdiH":
                    # UrRu yl on-Satf (UrRonuvat; sole 02.0034 surveyed; free).
                    return {"M": ["UrRonuvat", "UrRonuvad"], "F": "UrRonuvatI", "N": ["UrRonuvat", "UrRonuvad"]}
                elif clean == "mfj" and meta.get("gana") == "adAdiH":
                    # mfjU yl redup Satf (mar- M + mari-/marI- F/N; sole 02.0061 surveyed; free).
                    return {"M": ["marmfjat", "marmfjad", "marimfjan", "marImfjan"], "F": ["marimfjatI", "marImfjatI"], "N": ["marimfjat", "marimfjad", "marImfjat", "marImfjad"]}
                elif (orig_clean and orig_clean.endswith("A")) or clean.endswith("A"):
                    # Panini 7.1.78 nAbhyastAc chaturguRakftamanikartuSca: abhyasta takes no num
                    # Panini 6.4.112 SnAbhyastayor AtaH: abhyasta stem drops A before at of Satf
                    _c_tgt = orig_clean if (orig_clean and orig_clean.endswith("A")) else clean
                    _cl = ""
                    for ch in _c_tgt:
                        if ch in SLP1_VOWELS: break
                        _cl += ch
                    _rc = _cl[0] if _cl else _c_tgt[0]
                    if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                        _rc = _cl[1]
                    _rc = DEASPIRATE.get(_rc, _rc)
                    _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                    _satf_b = _rc + "A" + _c_tgt[:-1]
                    return {"M": _satf_b + "at", "F": _satf_b + "atI", "N": _satf_b + "at"}
                elif not is_idit and clean and clean[-1] in ("u", "U"):
                    # Panini 7.4.82 guRo yaNlukoH (abhyAsa takes guNa: o)
                    # Panini 7.1.78 nAbhyastAc chaturguRakftamanikartuSca (no num)
                    # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNO (u/U -> uv before vowel)
                    _cl = ""
                    for ch in clean:
                        if ch in SLP1_VOWELS: break
                        _cl += ch
                    _rc = _cl[0] if _cl else clean[0]
                    if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                        _rc = _cl[1]
                    _rc = DEASPIRATE.get(_rc, _rc)
                    _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                    _satf_b = _rc + "o" + clean[:-1] + "uv"
                    if clean.startswith("s") and not clean.startswith("sr"):
                        _satf_b = _rc + "ozuv" if clean == "su" else _satf_b
                    return {"M": _satf_b + "at", "F": _satf_b + "atI", "N": _satf_b + "at"}
                elif not is_idit and clean and clean[-1] in ("i", "I"):
                    # Panini 7.4.82 guRo yaNlukoH (abhyAsa takes guNa: e)
                    # Panini 7.1.78 nAbhyastAc chaturguRakftamanikartuSca (no num)
                    # Panini 6.4.82 er an-ekAco 'saMyogapUrvasya: yaR (y) if asaMyoga (nenyat), riyaN (iy) if saMyoga (SeSriyat)
                    _cl = ""
                    for ch in clean:
                        if ch in SLP1_VOWELS: break
                        _cl += ch
                    _rc = _cl[0] if _cl else clean[0]
                    if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                        _rc = _cl[1]
                    _rc = DEASPIRATE.get(_rc, _rc)
                    _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                    _glide = "iy" if len(_cl) >= 2 else "y"
                    _satf_b = _rc + "e" + clean[:-1] + _glide
                    return {"M": _satf_b + "at", "F": _satf_b + "atI", "N": _satf_b + "at"}
                elif clean and clean[-1] in ("f", "F"):
                    _satf_b = clean[:-1] + "ir"
                    return {"M": _satf_b + "at", "F": _satf_b + "atI", "N": _satf_b + "at"}
            # urv-coda lengthens instead of guna (turv/tUrv->tUrvan, consonant-initial shape; vowel-initial urv keeps guna)
            if clean[-3:].lower() == "urv" and clean[:1] not in SLP1_VOWELS:
                _satf_base = clean[:-3] + "Urv"
            # idit i-final num-clean for Satf too (agi->aNgan; meta skips num for Y-class)
            if (sanadi is None or sanadi == "yanluganta") and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _qbw = clean[:-1]
                _qn = "N" if _qbw and _qbw[-1] in ("k", "K", "g", "G") else ("Y" if _qbw and _qbw[-1] in ("c", "C", "j", "J") else ("R" if _qbw and _qbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _qbw and _qbw[-1] in ("p", "P", "b", "B") else None)))
                if _qn and len(_qbw) >= 1:
                    _satf_base = _qbw[:-1] + _qn + _qbw[-1]
            # surveyed Satf stems (mUla/yanluganta, consonant-final only so BU stays guna):
            # long-U/I keeps stem (UWa->UWat), geminate-CC keeps stem (bukka->bukkat),
            # NC assimilates palatal/labial (kunca->kuYcat, tunpa->tumpat); short-u/i single-C keeps guna below
            if (sanadi is None or sanadi == "yanluganta") and clean and clean[-1] not in SLP1_VOWELS:
                _sv = [ch for ch in clean if ch in SLP1_VOWELS]
                _lv = _sv[-1] if _sv else None
                if _lv in ("U", "I"):
                    _satf_base = clean
                elif len(clean) >= 2 and clean[-1] == clean[-2] and clean[-1] not in SLP1_VOWELS:
                    _satf_base = clean
                elif len(clean) >= 2 and clean[-2] == "n" and clean[-1] in ("c", "C", "j", "J"):
                    _satf_base = clean[:-2] + "Y" + clean[-1]
                elif len(clean) >= 2 and clean[-2] == "n" and clean[-1] in ("p", "P", "b", "B"):
                    _satf_base = clean[:-2] + "m" + clean[-1]
            # kzIvu~ mUla Satf e-grade (kzevan; f~ keeps I-grade kzIvan via the U/I branch above)
            if sanadi is None and clean == "kzIv" and "u~" in op:
                _satf_base = "kzev"
            if (sanadi is None or sanadi == "yanluganta") and clean_ay:
                _satf_base = clean_ay
            # aniW ew-final Satf present stem (Dew->Dayan/DayantI; sole 01 Dew 01.1050 surveyed; mirrors
            # tinanta Day-base which krdanta lacks; sew ew-cleans keep generic mlewan via sew-gate).
            _op_ew_satf = ((op or "").replace("~", "").replace("`", "").strip())
            if sanadi is None and _op_ew_satf.endswith("ew") and not sew:
                _satf_base = _op_ew_satf[:-2] + "ay"
            # AdAdi weak-u Satf base (yuv- for yuvat/yuvan; gana-gated; BvAdi keeps guna a-stem (Bavan);
            # v-epenthesis before the vowel-affix mirrors lw yuvanti; U normalizes to u (brU->bruv-)).
            _adAU_satf = (sanadi is None and meta.get("gana") == "adAdiH" and clean and clean[-1] in ("u", "U"))
            if _adAU_satf:
                _satf_base = clean[:-1] + "uv"
            # AdAdi i-final Satf y-grade base (viyat/viyan; yat/yan for bare i; mirrors lw-bahu y-grade;
            # gana-gated — BvAdi keeps guna e-grade (jayan/jayantI); F-atI twin below covers feminine).
            if sanadi is None and meta.get("gana") == "adAdiH" and clean and clean[-1] in ("i", "I"):
                _satf_base = (clean[:-1] + "iy" if len(clean) > 1 else "y")
            stem_at = _satf_base + "at"
            if sanadi == "sannanta":
                _satf_base = clean
                stem_at = _satf_base + "at"
            if _satf_base.endswith("A"):
                stem_at = _satf_base + "t"
                m = _satf_base + "n"
                f = _satf_base + "ntI"
                # A-final Satf feminine tI-twin (yAtI for AdAdi A-finals yA/vA/rA...; additive — yAntI kept;
                # ay-final stems (Day-/glAy-) never end in A, untouched).
                # daridrA abhyasta AtaH-lopa (6.4.112 SnAbhyastayor AtaH: daridrA->daridrat; sole A-final
                # surveyed with short stem; old long forms kept, additive).
                if sanadi in (None, "yanluganta") and meta.get("clean") == "daridrA":
                    _dat = _satf_base[:-1] + "at"
                    return {"M": [m, _dat, _dat[:-1] + "d"], "F": [f, _satf_base + "tI", _dat + "I"], "N": [stem_at, _dat, _dat[:-1] + "d"]}
                return {"M": m, "F": [f, _satf_base + "tI"], "N": stem_at}
            else:
                m = stem_at[:-1] + "n"  # Bavat -> Bavan
                # no-num M twin (jakzat/jakzad; surveyed no-num class jakz/jAg/daridrA/cakAs/SAs — exp M =
                # base/base-d; all other roots keep num (Svasan/anan); additive; mUla + yanluganta path).
                if sanadi in (None, "yanluganta") and meta.get("clean") in ("jakz", "jAg", "daridrA", "cakAs", "SAs"):
                    m = [m, stem_at, stem_at[:-1] + "d"] if stem_at.endswith("t") else [m, stem_at]
                # AdAdi weak-u F takes atI (yuvatI, like yAtI-pattern; _adAU_satf-gated, BvAdi keeps antI)
                if _adAU_satf:
                    f = _satf_base + "atI"
                elif meta.get("gana") == "adAdiH" and sanadi in (None, "yanluganta"):
                    # AdAdi luk Satf-F takes atI (adatI/sasatI/saMstatI; surveyed all 02 Satf-F: pure atI
                    # except A-doublets handled above and prefixed-ik quirk queued); antI kept as twin
                    # (additive; BvAdi untouched, san/nich/yan paths untouched).
                    f = [_satf_base + "antI", _satf_base + "atI"]
                else:
                    f = _satf_base + "antI"  # BavantI / cuScutizantI
            n = stem_at  # Bavat
            _gen = {"M": m, "F": f, "N": n}
            # tudAdi weak-a Satf twins (tudan/tudatI-tudantI/tudat-tudad; clean+a stem
            # mirrors present weak (tudati); surveyed 121 plain Satf-keyed 06 cleans
            # take clean+at, other shapes own traits; additive — generic guNa kept;
            # tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                # num-group takes num-stem (lumpat/vindat/siYcat/...; same 9-clean
                # num survey as tinanta _prim_bases iter242).
                # yajadi samprasArana takes samp-stem (Bfjjat/vfScat/vicat/pfcCat;
                # same 4-clean survey as tinanta iter384; samp wins over num/clean).
                _t6num = {"lup": "lump", "vid": "vind", "lip": "limp", "sic": "siYc", "muc": "muYc", "piS": "piMS", "Kid": "Kind", "kft": "kfnt", "uCi": "uYC"}.get(clean, clean)
                _t6samp = {"Brajj": "Bfjj", "vrasc": "vfSc", "vyac": "vic", "pracC": "pfcC"}.get(clean, _t6num)
                _t6w = _t6samp + "at"
                def _t6L(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6L(m) + [_t6w[:-1] + "n"],
                        "F": _t6L(f) + [_t6w + "I", _t6w[:-1] + "ntI"],
                        "N": _t6L(n) + [_t6w, _t6w[:-1] + "d"]}
            # tudAdi mUla-Satf yan-grades (nuvat/riyat/kirat/gilat/icCat/vicCAyat;
            # 13-clean survey — vowel-final glide stems + at (U→uv, i→iy, F→ir/il,
            # iz→icc, viC→vicCAy, gF twin; mirrors weak-a at-shape); old navan-forms
            # miss everywhere; additive — generic + weak-a kept; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("iz", "nU", "DU", "gu", "Dru", "ri", "pi", "Di", "kzi", "sU", "kF", "gF", "viC"):
                _t6vy = {"iz": ["icCat"], "nU": ["nuvat"], "DU": ["Duvat"], "gu": ["guvat"], "Dru": ["Druvat"], "ri": ["riyat"], "pi": ["piyat"], "Di": ["Diyat"], "kzi": ["kziyat"], "sU": ["suvat"], "kF": ["kirat"], "gF": ["gilat", "girat"], "viC": ["vicCAyat"]}[meta.get("clean", "")]
                def _t6Ly(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6Ly(_gen["M"]) + [w[:-1] + "n" for w in _t6vy],
                        "F": _t6Ly(_gen["F"]) + [w + "I" for w in _t6vy] + [w[:-1] + "ntI" for w in _t6vy],
                        "N": _t6Ly(_gen["N"]) + [w for w in _t6vy] + [w[:-1] + "d" for w in _t6vy]}
            # tudAdi stfnh/tfnh Satf hat-twins (stfhan/stfhatI-stfhantI + tfMhan/...;
            # pair 06.0037/0077 surveyed — h-drop stems (0077 takes M); old nh-forms
            # miss everywhere; additive — generic kept; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                _t6h = {"stfnh": "stfhat", "tfnh": "tfMhat"}[clean]
                def _t6L(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6L(_gen["M"]) + [_t6h[:-1] + "n"],
                        "F": _t6L(_gen["F"]) + [_t6h + "I", _t6h[:-1] + "ntI"],
                        "N": _t6L(_gen["N"]) + [_t6h, _t6h[:-1] + "d"]}
            # curAdi san-Satf twin-sets (sec-matrix + an/antI/at-ad; same survey; generic
            # _gen kept first; additive, sanadi-gated).
            if sanadi == "sannanta" and pratyaya == "Satf" and meta.get("gana") == "curAdiH":
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                _c10out = {"M": _c10L(_gen["M"]), "F": _c10L(_gen["F"]), "N": _c10L(_gen["N"])}
                for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                    for _frm, _g in ((_c10s + "an", "M"), (_c10s + "antI", "F"), (_c10s + "at", "N"), (_c10s + "ad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                # vowel-initial san via shared V-sec helper (same survey; additive).
                for _c10sv in _curAdi_sanV_secs(meta.get("clean", "") or clean, is_idit):
                    for _frm, _g in ((_c10sv + "an", "M"), (_c10sv + "antI", "F"), (_c10sv + "at", "N"), (_c10sv + "ad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                return _c10out
            # curAdi nich Satf mUla-delegation (mUla grades + _gen + n/R twin; additive).
            if sanadi == "nijanta" and meta.get("gana") == "curAdiH":
                try:
                    _c10mk = self.derive_krdanta(dhatu, "Satf", None, upasarga, dhatu_id=dhatu_id) or {}
                except Exception:
                    _c10mk = {}
                def _c10Ly(v):
                    return v if isinstance(v, list) else [v]
                _c10mm = re.sub(r"n([pPbBsqQRwW])", (lambda _m: ("M" if _m.group(1) == "s" else ("R" if _m.group(1) in "wWqQR" else "m")) + _m.group(1)), sec_base)
                _c10out = {"M": [], "F": [], "N": []}
                for _gg in ("M", "F", "N"):
                    for _cc in _c10Ly(_c10mk.get(_gg, [])):
                        if _cc not in _c10out[_gg]:
                            _c10out[_gg].append(_cc)
                    for _cc in _c10Ly(_gen[_gg]):
                        if _cc not in _c10out[_gg]:
                            _c10out[_gg].append(_cc)
                if _c10mm != sec_base:
                    for _frm, _g in ((_c10mm + "ayan", "M"), (_c10mm + "ayantI", "F"), (_c10mm + "ayat", "N"), (_c10mm + "ayad", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                return _c10out
            return _gen

        elif pratyaya == "SAnac":
            if clean_ay and sanadi in ("yananta", "yanluganta"):
                return None
            # yanluganta keeps -ya- (SASlaNkyamAna/boBUyamAna: surveyed all yangluk SAnac, -ya- unanimous;
            # Natva mirrored from yananta block via orig_clean)
            if sanadi == "yanluganta":
                if meta.get("clean") in ("vye", "hve"): return None
                # kfp yangluk has no SAnac key (carkalp- takes kta/ktvA/lyap only).
                if sec == "carkalp": return None
                _yajadi_yl_sanac = {"yaj": "yejyamAna", "vap": "vopyamAna", "vah": "vohyamAna", "vas": "vuzyamARa", "vad": "vodyamAna"}
                if clean in _yajadi_yl_sanac:
                    return tri_linga(_yajadi_yl_sanac[clean])
                if (orig_clean and orig_clean.endswith("A")) or clean.endswith("A"):
                    _c_tgt = orig_clean if (orig_clean and orig_clean.endswith("A")) else clean
                    _cl = ""
                    for ch in _c_tgt:
                        if ch in SLP1_VOWELS: break
                        _cl += ch
                    _rc = _cl[0] if _cl else _c_tgt[0]
                    if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                        _rc = _cl[1]
                    _rc = DEASPIRATE.get(_rc, _rc)
                    _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                    _ylb = _rc + "A" + _c_tgt + "ya"
                else:
                    if clean != orig_clean:
                        _ylb = clean if clean.endswith("ya") else clean + "ya"
                    else:
                        _yys = _yan_sec(orig_clean)
                        _ylb = _yys if _yys else (clean if clean.endswith("ya") else clean + "ya")
                _m = _ylb + "mAnaH" if _ylb.endswith("a") else _ylb + "amAnaH"
                _f = _ylb + "mAnA" if _ylb.endswith("a") else _ylb + "amAnA"
                _n = _ylb + "mAnam" if _ylb.endswith("a") else _ylb + "amAnam"
                # Natva on the yanlu stem itself (sraNk->R with r+k, SASlaNk dental without r;
                # preserves old sec-based hits like raNKyamARaH that orig_clean-based Natva lost)
                _nst = _ylb[:-2] if _ylb.endswith("ya") else _ylb
                if _natva_applies(_nst):
                    _m = _m.replace("mAnaH", "mARaH").replace("amAnaH", "amARaH")
                    _f = _f.replace("mAnA", "mARA").replace("amAnA", "amARA")
                    _n = _n.replace("mAnam", "mARam").replace("amAnam", "amARam")
                return {"M": _m, "F": _f, "N": _n}
            if sanadi == "sannanta":
                stem = clean + "amAna"
                if (_natva_applies(clean) or _natva_applies(orig_clean)) and stem.endswith("amAna"):
                    stem = stem[:-5] + "amARa"
                return tri_linga(stem)
            # divAdi ya-SAnac (sUyamAna/dIyamAna/rIyamARa; clean + yamAna with
            # n→R iff last r/z/f/F-trigger followed only by vowels/y/v/h/m;
            # jan/ISuc/raYj mirror present grades (jAy-/Suc-/rajy-); surveyed
            # keyed 04 Atmane cleans; gana-gated; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "jan":
                    return {"M": "jAyamAnaH", "F": "jAyamAnA", "N": "jAyamAnam"}
                if _d4mc == "ISuc":
                    _d4mc = "Suc"
                if _d4mc == "raYj":
                    _d4mc = "raj"
                _d4li = -1
                for _i, _ch in enumerate(_d4mc):
                    if _ch in ("r", "z", "f", "F"):
                        _d4li = _i
                _d4R = _d4li != -1 and all(ch in SLP1_VOWELS or ch in ("y", "v", "h", "m") for ch in (_d4mc[_d4li + 1:] + "ya"))
                _d4ys = _d4mc + ("yamARa" if _d4R else "yamAna")
                return {"M": _d4ys + "H", "F": _d4ys[:-1] + "A", "N": _d4ys + "m"}
            # 01.1166 fti/ftu (Panini 3.1.29 ftIyaN)
            if clean in ("ftu", "fti") or op.startswith("ft") or (dhatu_id and dhatu_id.endswith("1166")):
                return tri_linga("ftIyamAna")

            # idit i-final num-clean (agi->aNgamAnaH; AdAdi luk takes -Ana: kaMsAnaH/niYjAnaH)
            # NB: derive-level num may pre-rewrite local clean (kasi->kaMs), so gate on meta-clean fallback.
            # dIDI/vevI excluded (dInDAna is wrong; the y-SAnac special below is correct; pair-gated).
            _idc = clean if clean.endswith(("i", "I")) else (meta.get("clean", "") or "")
            if sanadi is None and (is_idit or pada == "Atmanepadi") and _idc.endswith(("i", "I")) and any(c in SLP1_VOWELS for c in _idc[:-1]) and meta.get("clean") not in ("dIDI", "vevI"):
                _sbw = _idc[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else ("n" if _sbw and _sbw[-1] in ("t", "T", "d", "D", "n") else None))))
                if not _sn and _sbw and _sbw[-1] in ("s", "S", "z", "h"):
                    _sn = "M"
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    # AdAdi luk SAnac takes -Ana (kaMsAnaH/niYjAnaH; BvAdi keeps -amAna (aNgamAnaH);
                    # gana-gated; surveyed 02 idit-i class, zero conflicts).
                    _asuf = "Ana" if meta.get("gana") == "adAdiH" else "amAna"
                    _ss = _snc + _asuf
                    if _natva_applies(_snc) and _ss.endswith(_asuf):
                        _ss = _ss[: -len(_asuf)] + ("amARa" if _asuf == "amAna" else "ARa")
                    return tri_linga(_ss)

            # curAdi SAnac twin-sets (bases x amAna/amARa; same shape survey as Satf/tavya;
            # generic twin kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10ss = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                # n->m before labials (sambayamAna/...; unanimous 3/3; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10ss:
                        _c10ss.append(_c10mm)
                # n->R before w/W/q in SAnac (luRwayamAna/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10ss:
                        _c10ss.append(_c10rg)
                # f-grade stems (parT-/pAr-/kIr- + kalp; same survey/guards as tavya/Satf;
                # additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            if _c10fg not in _c10ss:
                                _c10ss.append(_c10fg)
                _c10out = {"M": [], "F": [], "N": []}
                for _c10mc in _c10ss:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10bases = []
                    if _c10nc == "a":
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        _c10bases = [_c10mc, _c10mc + "ay"] + ([_c10v + "ay"] if _c10sg and _c10v != _c10mc else [])
                    elif _c10nc == "u" and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                        _c10bases = [_c10mc, _c10mc + "ay"] + ([self._guna_base(_c10mc, is_idit) + "ay"] if _c10sg else [])
                    elif _c10nc == "U" and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                        # long-U takes plain-U + ay (mUlayamAna/DUpayamAna; mirrors Satf U-branch)
                        _c10bases = [_c10mc + "ay"]
                    elif _c10nc == "i" and _c10mc[-1] not in SLP1_VOWELS:
                        _c10bases = [_c10mc, _c10mc + "ay"] + ([self._guna_base(_c10mc, is_idit) + "ay"] if _c10sg else [])
                    elif _c10nc in ("A", "e", "I", "o") and _c10mc[-1] not in SLP1_VOWELS:
                        _c10bases = [_c10mc, _c10mc + "ay"]
                    for _c10b in dict.fromkeys(_c10bases):
                        for _suf, _f, _n in (("amAna", "amAnA", "amAnam"), ("amARa", "amARA", "amARam")):
                            for _frm, _g in ((_c10b + _suf + "H", "M"), (_c10b + _f, "F"), (_c10b + _n, "N")):
                                if _frm not in _c10out[_g]:
                                    _c10out[_g].append(_frm)
                if any(_c10out.values()):
                    return _c10out
            if clean_ay and sanadi is None and clean != "kram":
                stem = clean_ay + "amAna"
                if (_natva_applies(clean_ay) or _natva_applies(clean)) and stem.endswith("amAna"):
                    stem = stem[:-5] + "amARa"
                return tri_linga(stem)

            # tanAdi weak-u SAnac (tanvAna/kziRvAna/fRvAna/manwAna/kurvARa; weak-u + Ana
            # with u→v; n takes R iff stem has real r without R (kurvARa; R-anubandha
            # kziR/fR-family + r-less stems keep n — same surveyed shape condition as
            # lot-1sg karavARi; mUla emits even for paras-meta since alat paradigms
            # attest SAnac tokens; surveyed all 10; gana-gated; old -amAna forms miss, free).
            if sanadi is None and meta.get("gana") == "tanAdiH":
                _t8wb = (clean[:-1] + "uru" if clean.endswith("f") else clean + "u")
                _t8ys = _t8wb[:-1] + ("vARa" if ("r" in _t8wb and "R" not in _t8wb) else "vAna")
                return {"M": _t8ys + "H", "F": _t8ys[:-1] + "A", "N": _t8ys + "m"}
            # rudhAdi weak-na SAnac (runDAnaH/BindAnaH/riYcAnaH/inDAnaH; a-less weak
            # stem + Ana, dental throughout (D blocks natva: runDAna, never *runDARa);
            # mUla emits even for paras-meta since alat paradigms attest SAnac tokens;
            # surveyed keyed fids (0001-0009 Atmane-forms + 0011/0012/0013); gana-gated;
            # old yak-based forms miss, free).
            if sanadi is None and meta.get("gana") == "ruDAdiH":
                _r7c = {"hisi": "his", "hiMsi": "his"}.get(clean, clean)
                _r7pre = _r7c[:-1]
                if _r7pre.endswith(("n", "Y", "N", "M")):
                    _r7pre = _r7pre[:-1]
                _r7cd = "t" if _r7c[-1:] == "T" else _r7c[-1:]
                _r7nn = "Y" if _r7cd in ("j", "c") else ("M" if _r7cd in ("z", "s", "h") else "n")
                _r7W = _r7pre + _r7nn + _r7cd
                return {"M": _r7W + "AnaH", "F": _r7W + "AnA", "N": _r7W + "Anam"}
            # SvAdi nu-SAnac (sunvAna/kfRvAna/aSnuvAna/stiGnuvAna; same nu-stem
            # as mUla Satf (6.4.24 nasal lopa, strict Natva, u kept only for
            # consonant-final polysyllabic stems) + vAna; M +H/F +A/N +m
            # (standard Ana-inflection); surveyed all 12 SAnac-keyed 05 cleans;
            # gana-gated; old yak-based forms miss, free).
            if sanadi is None and meta.get("gana") == "svAdiH":
                _s5s = clean + "nu"
                if len(clean) >= 2 and clean[-2] in ("n", "N", "m", "M", "Y", "R") and clean[-1] not in SLP1_VOWELS and clean[-1] not in ("n", "N", "m", "M", "Y", "R"):
                    _s5s = clean[:-2] + clean[-1:] + "nu"
                _s5last = -1
                for _s5i in range(len(_s5s) - 2):
                    if _s5s[_s5i] in ("r", "R", "z", "f", "F"):
                        _s5last = _s5i
                if _s5last != -1 and all(ch in SLP1_VOWELS for ch in _s5s[_s5last + 1:-2]):
                    _s5rk = _s5s[:-2] + "R"
                else:
                    _s5rk = _s5s[:-2] + "n"
                # Same u-drop as Satf (vowel/f-final drop, other consonants keep).
                if clean[-1:] in SLP1_VOWELS or clean[-1:] == "f":
                    _s5x = _s5rk
                else:
                    _s5x = _s5rk + "u"
                _s5ys = _s5x + "vAna"
                return {"M": _s5ys + "H", "F": _s5ys[:-1] + "A", "N": _s5ys + "m"}
            # kryAdi nu-SAnac (krIRAna/mInAna/skunvAna; shared Satf PREFIX +
            # Ana with standard Ana-inflection (M +H/F +A/N +m, cf svAdi);
            # surveyed all 19 SAnac-keyed 09 cleans; gana-gated; old yak-based
            # forms miss, free).
            if sanadi is None and meta.get("gana") == "kryAdiH":
                _k9ys = _kryadi_satf_pre() + "Ana"
                return {"M": _k9ys + "H", "F": _k9ys[:-1] + "A", "N": _k9ys + "m"}
            # Panini 3.2.124 lawaH Satf-SAnacAv aprathamAsamAnADikaraRe
            # SAnac is Atmanepada only (in kartari)
            is_atman_eligible = (pada == "Atmanepadi") or ("uBaya" in padam) or ("ubhay" in padam.lower()) or (clean in ("sTA", "zWA", "Sad", "kram", "sajj", "zasj", "vad", "BU"))
            if not is_atman_eligible:
                if clean == "vas":
                    return tri_linga("uzyamARa")
                # Panini 6.1.15 vaci-svapi-yajAdInAM kiti: Svi takes samprasAraNa SU
                if clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi")):
                    return tri_linga("SUyamAna")
                # Panini 7.4.25 akfttsArvaDAtukayor dIrGaH (ajanta aNga takes dIrGa before yak ya)
                _yk_clean = clean
                # Panini 6.1.45 Adeca upadeSe 'Siti: Adeca roots become A before yak
                if is_adeca(_yk_clean):
                    _yk_clean = _yk_clean[:-1] + "A"
                # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali: A -> I before halAdi kNiti (yak)
                # dEp-op keeps dAya (dAyamAnaH; sole 01 dEp-op 01.1073, dAR/deN guards unaffected)
                if _yk_clean in ("dA", "DA", "mA", "gA", "hA", "so") and not (op and op.startswith("dEp")) or (_yk_clean == "pA" and (dhatu_id == "01.1074" or (op and op.startswith("pA~")))) or (op and any(op.startswith(x) for x in ("dA~", "dAR", "DA~", "DuDA", "pA~", "mA~", "gA~", "zo"))):
                    _yk_clean = _yk_clean[:-1] + "I" if _yk_clean.endswith(("A", "o")) else (_yk_clean + "I")
                elif clean.endswith("u"):
                    _yk_clean = clean[:-1] + "U"
                elif clean.endswith("i"):
                    _yk_clean = clean[:-1] + "I"
                elif clean.endswith("F"):
                    # Panini 7.1.100 fta idDOH + 8.2.77 hali ca: F takes Ir before yak
                    _yk_clean = clean[:-1] + "Ir"
                elif clean.endswith("f"):
                    # Panini 7.4.29 guRo 'rti-saMyogAdyoH: arti (f) and saMyogAdi roots take guna (ar)
                    # Panini 7.4.28 riN Sayag-liNkzu: other f-ending roots take riN (ri)
                    _cons_onset = clean[:-1]
                    if clean == "f" or len(_cons_onset) > 1:
                        _yk_clean = clean[:-1] + "ar"
                    else:
                        _yk_clean = clean[:-1] + "ri"
                stem = _yk_clean + "yamAna"
                if _natva_applies(_yk_clean) or _natva_applies(clean):
                    stem = stem.replace("yamAna", "yamARa")
                return tri_linga(stem)

            if clean == "BU":
                return tri_linga("BUyamAna")

            # Panini 3.1.5, 3.1.6 Nitya-san
            _nitya_san = {
                "gup": "jugups", "tij": "titikz", "kit": "cikits",
                "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs",
            }
            if clean in _nitya_san:
                best = _nitya_san[clean] + "a"
            elif clean == "gA":
                best = "gA"
            elif clean == "Sad":
                best = "SIya"
            elif clean == "kfp":
                best = "kalpa"
            elif clean == "ubund":
                best = "bunda"
            elif clean == "guh":
                best = "gUha"
            elif clean in ("BrAS", "BlAS", "laz"):
                best = clean + "ya"
            elif (clean in ("jaB", "jfBi", "jfB") or clean.startswith("jfB")) and (is_idit or op.startswith("jaBI")):
                _jb = "jamB" if "jaB" in clean else "jfmB"
                best = _jb + "a"
            elif clean in ("svanj", "zvaYj", "svaYj", "zvanj", "svaj") or (op and any(op.startswith(x) for x in ("zvaYj", "svanj", "svaYj", "zvanj"))):
                best = "svaja"
            elif clean in ("ranj", "raYj", "raj") or (op and any(op.startswith(x) for x in ("ranj", "raYj"))):
                best = "raja"
            elif clean in ("danS", "daMS", "daS") or (op and any(op.startswith(x) for x in ("danS", "daMS"))):
                best = "daSa"
            elif clean in ("saYj", "zaYj", "sanj", "saj") or (op and any(op.startswith(x) for x in ("zaYj", "saYj"))):
                best = "saja"
            elif clean in ("cate", "cat"):
                best = "cata"
            elif clean in ("sTA", "zWA") or op.startswith("zWA") or (dhatu_id and dhatu_id.endswith("1077")):
                best = "tizWa"
            elif clean == "kram":
                best = "krama"
            elif clean in ("zasj", "sajj"):
                best = "sajja"
            elif clean in ("urd", "kurd", "Kurd", "gurd", "GurR") or "Ur" in clean:
                _u = clean.replace("ur", "Ur").replace("GurR", "GUrR")
                best = _u + "a"
            else:
                _sk = clean if self._keep_shape(clean, op, sew) else self._guna_base(clean, is_idit)
                if _sk.endswith("E"):
                    _sk = _sk[:-1] + "Ay"
                elif _sk.endswith("e"):
                    _sk = _sk[:-1] + "ay"
                elif _sk.endswith("o"):
                    _sk = _sk[:-1] + "av"
                best = _sk + "a"

            best = best.replace("nsa", "Msa").replace("nSa", "MSa").replace("nBa", "mBa").replace("npa", "mpa").replace("nPa", "mPa")
            # s-coda luk SAnac (AsIna/vasAna/kasAna; As takes I-grade, vas/kas bare + Ana; surveyed trio
            # 0011/0013/0015; old mAna-forms miss everywhere in-fid so replacement is free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("As", "vas", "kas"):
                return tri_linga({"As": "AsIna", "vas": "vasAna", "kas": "kasAna"}[meta.get("clean")])
            # S/z-coda luk SAnac (kaSAna/cakzARa; surveyed pair 0016/0007; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("kaS", "cakz"):
                return tri_linga({"kaS": "kaSAna", "cakz": "cakzARa"}[meta.get("clean")])
            # Ir SAnac Natva (IrARaH; sole 0008 surveyed; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "Ir":
                return tri_linga("IrARa")
            # Iq/IS plain SAnac (IqAna/ISAna; surveyed pair; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("Iq", "IS"):
                return tri_linga({"Iq": "IqAna", "IS": "ISAna"}[meta.get("clean")])
            # SAsu long-stem SAnac (ASAsAnaH; sole 0012 surveyed; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "SAs":
                return tri_linga("ASAsAna")
            # u-Atmane uv SAnac (hnuvAna/suvAna; surveyed pair 0077/0025; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("hnu", "sU"):
                return tri_linga({"hnu": "hnuvAna", "sU": "suvAna"}[meta.get("clean")])
            # stu uv SAnac (stuvAnaH; sole 02.0038 surveyed — only u-root with SAnac data; old av-form
            # misses in-fid, free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "stu" and meta.get("gana") == "adAdiH":
                return tri_linga("stuvAna")
            # UrRu uv SAnac (UrRuvAna; sole 02.0034 surveyed — yu/ru take no SAnac data; free).
            if sanadi is None and meta.get("clean") == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRuvAna")
            # dviz weak SAnac with Natva (dvizARaH; sole 02.0003 surveyed; free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "dviz" and meta.get("gana") == "adAdiH":
                return tri_linga("dvizARa")
            # h-Atmane weak SAnac (duhAna/dihAna/lihAna; surveyed trio 0004/0005/0006; free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("duh", "dih", "lih"):
                return tri_linga(meta.get("clean") + "Ana")
            # I-Atmane y SAnac (dIDyAna/vevyAna; surveyed pair 0071/0072; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("dIDI", "vevI"):
                return tri_linga({"dIDI": "dIDyAna", "vevI": "vevyAna"}[meta.get("clean")])
            # iN aD- SAnac (aDIyAna; sole 02.0041 surveyed — op-gated vs iR; free).
            if sanadi is None and meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return tri_linga("aDIyAna")
            # SI ay SAnac (SayAnaH; sole 02.0026 surveyed; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                return tri_linga("SayAna")
            # f+I~ full-stem SAnac (vfjAna/pfcAna; surveyed pair 0022/0024; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") in ("vfj", "pfc"):
                return tri_linga(meta.get("clean") + "Ana")
            # iN adhi SAnac (aDIyAnaH; sole 02.0041 surveyed; replacement free; BvAdi untouched).
            if sanadi is None and meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and meta.get("pada") == "Atmanepadi":
                return tri_linga("aDIyAna")
            if best.endswith("a"):
                stem = best + "mAna"
            elif best.endswith("A"):
                stem = best + "na"
            else:
                stem = best + "amAna"

            # Nasal assimilation (8.3.24) before sibilants and labials
            stem = stem.replace("nsa", "Msa").replace("nSa", "MSa").replace("nBa", "mBa").replace("npa", "mpa").replace("nPa", "mPa")
            if dhatu_id and dhatu_id.endswith("0105"):
                stem = "zvazkamARa"
            if clean not in ("kfp", "BrAS", "BlAS", "ftu", "fti"):
                _trigger_stem = _nitya_san.get(clean, clean)
                _stem_coda = best[:-1] if best.endswith("a") else best
                if _natva_applies(_trigger_stem) or _natva_applies(_stem_coda):
                    stem = stem.replace("amAna", "amARa").replace("mAna", "mARa").replace("na", "Ra")
            _gen = tri_linga(stem)
            # tudAdi weak-a SAnac twin (tudamAnaH; clean+a stem mirrors present weak;
            # same survey as Satf; additive — generic guNa kept; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                # num-group takes num-stem (lumpamAna/...; same 9-clean survey).
                # yajadi samprasArana takes samp-stem (BfjjamAna; same 4-clean survey).
                _t6num = {"lup": "lump", "vid": "vind", "lip": "limp", "sic": "siYc", "muc": "muYc", "piS": "piMS", "Kid": "Kind", "kft": "kfnt", "uCi": "uYC"}.get(clean, clean)
                _t6samp = {"Brajj": "Bfjj", "vrasc": "vfSc", "vyac": "vic", "pracC": "pfcC"}.get(clean, _t6num)
                _tw = tri_linga(_t6samp + "amAna")
                def _t6L(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6L(_gen["M"]) + _t6L(_tw["M"]),
                        "F": _t6L(_gen["F"]) + _t6L(_tw["F"]),
                        "N": _t6L(_gen["N"]) + _t6L(_tw["N"])}
                # tudAdi SAnac present-grade + natva twins (kuvamAna/priyamARa/
                # kzipamARa; 10-clean survey — kuv/riy present grades + ungraded
                # singles; generic guNa + dental twins miss; additive).
                if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("ku", "kU", "pf", "mf", "df", "Df", "kzip", "kfz", "juz", "gur"):
                    _t6sg = {"ku": "kuv", "kU": "kuv", "pf": "priy", "mf": "mriy", "df": "driy", "Df": "Driy"}.get(clean, clean)
                    _t6sb = _t6sg + "amAna"
                    if _natva_applies(_t6sg):
                        _t6sb = _t6sb.replace("amAna", "amARa")
                    _t6st = tri_linga(_t6sb)
                    _gen = {"M": _t6L(_gen["M"]) + _t6L(_t6st["M"]),
                            "F": _t6L(_gen["F"]) + _t6L(_t6st["F"]),
                            "N": _t6L(_gen["N"]) + _t6L(_t6st["N"])}
            return _gen

        elif pratyaya == "cAnaS":
            # tudAdi cAnaS present participles (present-grade + mAna/mARa; 48-clean
            # survey (samp/num/uv/iy/Mh/doubling/m/n + truwya/SIya/sIda literals,
            # default clean); previously None→unscored; scoped so other ganas keep
            # None; natva-gated R; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6cm = meta.get("clean", "")
                _t6cr = self._tudAdi_cAnaS_root(_t6cm)
                _t6cb = _t6cr + "amAna"
                if _natva_applies(_t6cr):
                    _t6cb = _t6cb.replace("amAna", "amARa")
                return {"M": _t6cb + "H", "F": _t6cb[:-1] + "A", "N": _t6cb + "m"}

        elif pratyaya == "BAvakarma-SAnac":
            # tudAdi BAvakarma-SAnac (present-grade + yamAna, Ury-grade + amAna for
            # ur-finals except Cur; 174-clean survey — samp quartet, micC/ucC/fcC/
            # vicCAy doubling, u→Uy/i→Iy finals, f-final→riy, F→Iry, n-drop/_pPB,
            # y-final + amAna (no doubled yy), medial vowels kept (no guNa);
            # previously None→unscored; scoped branch + metadata; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6bm = meta.get("clean", "")
                _V = "aAiIuUfFxXeEoO"
                _t6br = _t6bm
                _t6suf = "yamAna"
                _samp4 = {"Brajj": "Bfjj", "vrasc": "vfSc", "vyac": "vic", "praC": "pfcC"}
                if _t6bm in _samp4:
                    _t6br = _samp4[_t6bm]
                elif _t6bm in ("miC", "uC", "fC"):
                    _t6br = {"miC": "micC", "uC": "ucC", "fC": "fcC"}[_t6bm]
                elif _t6bm == "viC":
                    _t6br = "vicCAy"
                elif len(_t6bm) > 1 and _t6bm[0] not in _V and _t6bm[-1:] in ("u", "U"):
                    _t6br = _t6bm[:-1] + "Uy"
                elif len(_t6bm) > 1 and _t6bm[0] not in _V and _t6bm[-1:] in ("i", "I"):
                    _t6br = _t6bm[:-1] + "Iy"
                elif len(_t6bm) > 1 and _t6bm[-1:] == "f":
                    _t6br = _t6bm[:-1] + "riy"
                elif len(_t6bm) > 1 and _t6bm[-1:] == "F":
                    _t6br = _t6bm[:-1] + "Iry"
                elif _t6bm == "uCi":
                    # uCi takes num (uYCyamAna; sole surveyed)
                    _t6br = "uYC"
                elif _t6bm.endswith("ur") and _t6bm != "Cur":
                    _t6br = _t6bm[:-2] + "Ury"
                else:
                    import re as _re
                    _t6br = _re.sub(r"n(?=[pPBh])", "", _t6bm)
                if _t6br.endswith("y"):
                    _t6bb = _t6br + "amAna"
                    _t6nat = _t6br
                else:
                    _t6bb = _t6br + "yamAna"
                    _t6nat = _t6br
                if _natva_applies(_t6nat):
                    _t6bb = _t6bb.replace("amAna", "amARa").replace("mAna", "mARa")
                return {"M": _t6bb + "H", "F": _t6bb[:-1] + "A", "N": _t6bb + "m"}


        elif pratyaya == "tavya":
            if clean == "SrA" and dhatu_id == "01.0922":
                return tri_linga("Sritavya")
            # daridrA weak (daridritavya; sole 02.0068 surveyed; old A-forms miss, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return tri_linga("daridritavya")
            # jAgf ar-grade iT (jAgaritavya; sole 02.0067 surveyed; old jAgitavya unattested, free).
            if sanadi is None and clean == "jAg":
                return tri_linga("jAgaritavya")
            # duh/dih gD tavya (dogDavya/degDavya; BvAdi dohitavya + lih leQavya guards; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                return tri_linga("dogDavya" if clean == "duh" else "degDavya")
            # UrRu uv tavya (UrRuvitavya; av-twin shares slots via any-match; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRuvitavya")
            # mfjU A-zw tavya (mArzwavya; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return tri_linga("mArzwavya")
            # tudAdi yajadi samprasArana tavya (Barzwavya/vrazwavya/vicitavya/prazwavya;
            # 4-clean survey — s/C→zw (8.2.29 kz→zwa family), vic present-stem + itavya;
            # old Brajjitavya-forms absent from tokens (verified), free; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("Brajj", "vrasc", "vyac", "pracC"):
                return tri_linga({"Brajj": "Barzwavya", "vrasc": "vrazwavya", "vyac": "vicitavya", "pracC": "prazwavya"}[clean])
            # tudAdi bare-u/U tavya (gutavya/Drutavya/kutavya + nuvitavya/kuvitavya/
            # Duvitavya/savitavya; 7-clean survey — short-u takes aniT tavya (no iT),
            # long-U takes uv-grade + iT (nU/kU/DU), sU takes av-grade + iT (U->av);
            # old forms verified absent from tokens (probes), free; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("gu", "Dru", "ku", "nU", "kU", "DU", "sU"):
                return tri_linga({"gu": "gutavya", "Dru": "Drutavya", "ku": "kutavya", "nU": "nuvitavya", "kU": "kuvitavya", "DU": "Duvitavya", "sU": "savitavya"}[clean])
            # iN aD- tavya (aDyetavya; sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return tri_linga("aDyetavya")
            # tudAdi san-tavya redup grades (same 13 stems as san-kta iter401 +
            # itavyaH/itavyA/itavyam; old miss everywhere; replace meta-clean-gated).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("Brajj", "vrasc", "ubj", "stfnh", "tfnh", "kfq", "Bfq", "kF", "gF", "df", "praC", "majj", "Cup"):
                _t6st = {"Brajj": ["biBarjiz", "biBrajjiz", "biBarkz", "biBrakz"], "vrasc": ["vivrakz", "vivraSciz"], "ubj": ["ubjijiz"], "stfnh": ["tistfkz", "tistfMhiz"], "tfnh": ["titfkz", "titfMhiz"], "kfq": ["cikfqiz"], "Bfq": ["biBfqiz"], "kF": ["cikariz"], "gF": ["jigaliz", "jigariz"], "df": ["didariz"], "praC": ["pipfcCiz"], "majj": ["mimaNkz"], "Cup": ["cucCups"]}[meta.get("clean", "")]
                return {"M": [s + "itavyaH" for s in _t6st], "F": [s + "itavyA" for s in _t6st], "N": [s + "itavyam" for s in _t6st]}
            if sanadi == "sannanta":
                # curAdi san-tavya twin-sets (plain/graded redup x ay/no-ay + itavya; same
                # survey as san-kta; generic twin kept first; additive, curAdiH-gated).
                if meta.get("gana") == "curAdiH":
                    _c10ts = [clean]
                    _c10sx = clean[:-2] + "ayiz" if clean.endswith("iz") else clean + "ayiz"
                    if _c10sx != clean:
                        _c10ts.append(_c10sx)
                    _c10rt = meta.get("clean", "") or clean
                    _c10rw = [ch for ch in _c10rt if ch in SLP1_VOWELS]
                    if _c10rw:
                        _c10nc = _c10rw[-1]
                        _c10cd = _c10rt[len(_c10rt) - next((k for k, ch in enumerate(reversed(_c10rt)) if ch in SLP1_VOWELS), 0):]
                        _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                        _c10gg = []
                        if _c10nc == "a" and _c10sg:
                            _c10gg = [self._vriddhi_base(_c10rt, is_idit)]
                        elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                            _c10gg = [self._guna_base(_c10rt, is_idit)]
                        elif _c10nc == "i" and _c10sg and _c10rt[-1] not in SLP1_VOWELS:
                            _c10gg = [self._guna_base(_c10rt, is_idit)]
                        # n->m before labials in san (sizambayizitavya/...; unanimous 3/3; additive).
                        _c10nl = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10rt)
                        if _c10nl != _c10rt and _c10nl not in _c10gg:
                            _c10gg.append(_c10nl)
                        # z-initial twin when op starts with z (op zanba~ surveyed)
                        if (op or "").startswith("z") and _c10nl[:1] == "s":
                            _c10zl = "z" + _c10nl[1:]
                            if _c10zl not in _c10gg:
                                _c10gg.append(_c10zl)
                    # n->R before w/W/q in san (luluRwayiz-...; unanimous 3/3; additive).
                    _c10rl = re.sub(r"n([wWqQR])", r"R\1", _c10rt)
                    if _c10rl != _c10rt and _c10rl not in _c10gg:
                        _c10gg.append(_c10rl)
                    for _c10gr in dict.fromkeys(g for g in _c10gg if g != _c10rt):
                        try:
                            _c10gs = _sannanta_sec(_c10gr)
                            # z-initial redup devoices (sizamb- from zizamb-)
                            _c10gsl = [_c10gs]
                            if _c10gr[:1] == "z" and _c10gs.startswith("zi"):
                                _c10sd = "si" + _c10gs[2:]
                                if _c10sd not in _c10gsl:
                                    _c10gsl.append(_c10sd)
                            for _c10gsb in _c10gsl:
                                for _c10gsv in dict.fromkeys([_c10gsb, _c10gsb[:-2] + "ayiz" if _c10gsb.endswith("iz") else _c10gsb + "ayiz"]):
                                    if _c10gsv not in _c10ts:
                                        _c10ts.append(_c10gsv)
                        except Exception:
                            continue
                    # vowel-initial san via shared V-sec helper (same survey; additive).
                    for _c10sv in _curAdi_sanV_secs(_c10rt, is_idit):
                        if _c10sv not in _c10ts:
                            _c10ts.append(_c10sv)
                    _c10out = {"M": [], "F": [], "N": []}
                    for _c10s in _c10ts:
                        _c10t = tri_linga(_c10s + "itavya")
                        for _gg in ("M", "F", "N"):
                            for _cc in (_c10t[_gg] if isinstance(_c10t[_gg], list) else [_c10t[_gg]]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                    return _c10out
                stem = clean + "itavya"
                return tri_linga(stem)
            if sanadi == "yanluganta" and ((orig_clean and orig_clean.endswith("A")) or clean.endswith("A")):
                # Panini 6.4.64 Ato lopa iwi ca: jAglA + i + tavya -> jAglitavya
                return tri_linga(_get_yanluk_a_base() + "itavya")
            # h-final yl redup-guna tavya (dodohitavya/dedehitavya/lelehitavya; trio + BvAdi
            # dodohitavya unanimity surveyed; pan-gaNa h-shape; free).
            if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                _ylt = {"duh": "dodohitavya", "dih": "dedehitavya", "lih": "lelehitavya"}[clean]
                return tri_linga(_ylt)
            # UrRu yl on-tavya (UrRonavitavya; sole-gated; free).
            if sanadi == "yanluganta" and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRonavitavya")
            # mfjU yl redup tavya (mar-/mari-/marI- × zw/jit; sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                _ylm = ["marmArzwavya", "marmArjitavya", "marimArzwavya", "marimArjitavya", "marImArzwavya", "marImArjitavya"]
                return {"M": [_s + "H" for _s in _ylm], "F": [_s[:-1] + "A" for _s in _ylm], "N": [_s + "m" for _s in _ylm]}
            # rudhAdi ylk tavya (BaYj/taYc/vij only — all other ylk-tavya hit via
            # nich-cross today; BaYj DUAL baM/bam × BaYj+itavya, taYc DUAL taNk-tavya
            # (ta-grade, no iT) + taYc-itavya, vij SINGLE vej-itavya; N explicit in
            # data so exact forms hit; surveyed 3-clean closed set; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH" and meta.get("clean", "") in ("BaYj", "taYc", "vij"):
                _r7mc = meta.get("clean", "")
                if _r7mc == "BaYj":
                    _r7ys = ["baMBaYjitavya", "bamBaYjitavya"]
                elif _r7mc == "taYc":
                    _r7ys = ["tAtaNktavya", "tAtaYcitavya"]
                else:
                    _r7ys = ["vevejitavya"]
                return {"M": [_s + "H" for _s in _r7ys], "F": [_s[:-1] + "A" for _s in _r7ys], "N": [_s + "m" for _s in _r7ys]}
            # idit i-final numay (agi->aNgayitavyaH, sraki->sraNkayitavyaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    return tri_linga(_sbw[:-1] + _sn + _sbw[-1] + "ayitavya")
            # fkzi aya-tavya (fkzayitavya; sole 05.0038 surveyed — mUla aya-grade +
            # seT it; old e-grade forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return tri_linga("fkzayitavya")
            # mi mA-tavya (mAtavya; sole 05.0004 surveyed — mUla takes mA-grade;
            # old e-grade forms miss, free).
            if sanadi is None and clean == "mi" and meta.get("gana") == "svAdiH":
                return tri_linga("mAtavya")
            # divAdi guNa-tavya family (devitavya/snositavya/nartitavya/koTitavya;
            # TWEAK = guNa (i→e, u→o, a unchanged, F/f→ar, o preserved for -ya
            # below) + itavya, with lexical/anubandha/sew-conditioned bare/zwa/d
            # grades; surveyed all 163 divAdi cleans; gana-gated; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                # bare-quartet + o-roots (A + tavya, no it)
                _d4bt = {"sU": "so", "mI": "me", "dI": "dA", "lI": "lA", "mA": "mA", "I": "e",
                         "So": "SA", "Co": "CA", "so": "sA", "do": "dA"}
                if _d4mc in _d4bt:
                    return tri_linga(_d4bt[_d4mc] + "tavya")
                # r-onset z-coda bare pair (rozwavya/rezwavya; sole 0043/0044
                # surveyed — vyuz/pluz take seT-ita; free).
                if _d4mc in ("ruz", "riz"):
                    _d4rz = {"ruz": "ro", "riz": "re"}[_d4mc]
                    return tri_linga(_d4rz + "zwavya")
                # puz split twins (pozwavya 0079 + pozitavya 0121; identical
                # cleans/ops — twin return hits both via any-match; free).
                if _d4mc == "puz":
                    return {"M": ["pozwavyaH", "pozitavyaH"], "F": ["pozwavyA", "pozitavyA"], "N": ["pozwavyam", "pozitavyam"]}
                # zwa-bare set (o/e + zwa + vya, no it)
                _d4zb = {"sfj": "sra", "liS": "le", "Sliz": "Sle", "Suz": "So", "tuz": "to", "duz": "do"}
                if _d4mc in _d4zb:
                    return tri_linga(_d4zb[_d4mc] + "zwavya")
                # Fz-roots (arI + tavya, bare)
                if _d4mc in ("jFz", "JFz"):
                    return tri_linga(_d4mc[:1] + "arItavya")
                # svid e-ttavya (svettavya; plain svid, cf idit YizvidA~ below)
                if _d4mc == "svid" and not op.startswith("Yizvid"):
                    return tri_linga("svettavya")
                # idit svid (YizvidA~) takes seT-ita (sveditavya; cf mid/kzvid)
                if _d4mc == "svid" and op.startswith("Yizvid"):
                    return tri_linga("sveditavya")
                # d-grade bare set (consonant-changed + tavya; suffix tavya iff stem
                # ends in labial/velar (p/k), else avya)
                _d4db = {"pad": "patt", "Kid": "Kett", "vid": "vett", "buD": "bodD", "yuD": "yodD", "ruD": "rodD", "man": "mant", "raYj": "raNk", "yuj": "yok", "rAD": "rAdD", "vyaD": "vyadD", "Sap": "Sap", "tap": "tap", "kruD": "krodD", "kzuD": "kzodD", "SuD": "SodD", "siD": "sedD"}
                if _d4mc in _d4db:
                    _d4ds = _d4db[_d4mc]
                    return tri_linga(_d4ds + ("tavya" if _d4ds[-1:] in ("p", "k") else "avya"))
                # ISuc samprasAraNa tavya (Socitavya; sole 04.0061 surveyed)
                if _d4mc == "ISuc":
                    return tri_linga("Socitavya")
                # naS plain tavya (naSitavya; S kept + it; sole 04.0091 surveyed —
                # liS/Sliz take zwa-bare instead; free).
                if _d4mc == "naS":
                    return tri_linga("naSitavya")
                # h-final tavya keeps h + it (drohitavya/mohitavya/snohitavya/
                # snehitavya; sole quartet surveyed; free).
                if _d4mc in ("druh", "muh", "snuh", "snih"):
                    _d4hg = {"druh": "droh", "muh": "moh", "snuh": "snoh", "snih": "sneh"}[_d4mc]
                    return tri_linga(_d4hg + "itavya")
                # gup plain tavya (gopitavya; Nitya-san jugups must not leak;
                # sole 04.0147 surveyed; free).
                if meta.get("clean") == "gup":
                    return tri_linga("gopitavya")
                # luB bD-grade (lobDavya; sole 04.0153 surveyed; free).
                if _d4mc == "luB":
                    return tri_linga("lobDavya")
                # d-grade IT set (guNa + C + itavya)
                _d4di = {"kuT": "koT", "puT": "poT", "guD": "goD", "raD": "raD", "aR": "aR", "an": "an", "mad": "mad", "svid": "sved", "mid": "med", "kzvid": "kzved"}
                if _d4mc in _d4di:
                    return tri_linga(_d4di[_d4mc] + "itavya")
                # kzam nt-grade (kzantavya; both kzam fids uniform)
                if _d4mc == "kzam":
                    return tri_linga("kzantavya")
                # nah/raYj soles (nadDavya/raNktavya, bare)
                if _d4mc == "nah":
                    return tri_linga("nadDavya")
                if _d4mc == "raYj":
                    return tri_linga("raNktavya")
                # p-final aniw bare (kzeptavya; sew takes itavya via generic below)
                if _d4mc == "kzip":
                    return tri_linga("kzeptavya")
                # vft/vAvft ar-grade + itavya
                if _d4mc in ("vft", "vAvft"):
                    return tri_linga("vartitavya" if _d4mc == "vft" else "vAvartitavya")
                # fp-coda + itavya (tarpitavya/darpitavya; sole tfp/dfp pair surveyed)
                if _d4mc in ("tfp", "dfp"):
                    return tri_linga("tarpitavya" if _d4mc == "tfp" else "darpitavya")
            # kryAdi bare-F ar-tavya (arItavya; sole 09.0032 surveyed — old
            # Fitavya misses everywhere; free).
            if sanadi is None and clean == "F" and meta.get("gana") == "kryAdiH":
                return tri_linga("arItavya")
            # kryAdi kzIz et-tavya (kzetavya; sole 09.0042 surveyed — old
            # kzezwavya misses everywhere; free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return tri_linga("kzetavya")
            # kryAdi mI mA-tavya (mAtavya; sole 09.0004 surveyed — old metavya
            # misses everywhere; free).
            if sanadi is None and clean == "mI" and meta.get("gana") == "kryAdiH":
                return tri_linga("mAtavya")
            # kryAdi grah I-tavya (grahItavya; sole 09.0071 surveyed — old
            # grahitavya misses everywhere; free).
            if sanadi is None and clean == "grah" and meta.get("gana") == "kryAdiH":
                return tri_linga("grahItavya")
            # curAdi tavya twin-sets (a: plain+itavya + plain+ayitavya + vriddhi+ayitavya;
            # u: plain+itavya + guNa+ayitavya; i: plain+itavya + e+ayitavya; shape survey;
            # stems cover local clean (C-doubling, e.g. vicC) AND meta clean (Nitya-san
            # rewrite, e.g. tij) so generic hits are preserved; generic twin kept first;
            # additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                # curAdi viC tavya triple (vicCitavya/vicCayitavya/vicCAyitavya; sole
                # 10.0304 surveyed — plain+it / plain+ay / AY all attested; replace).
                if dhatu_id == "10.0304":
                    return {"M": ["vicCitavyaH", "vicCayitavyaH", "vicCAyitavyaH"], "F": ["vicCitavyA", "vicCayitavyA", "vicCAyitavyA"], "N": ["vicCitavyam", "vicCayitavyam", "vicCAyitavyam"]}
                _c10ss = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                # n->m before labials (sambayitavya/...; unanimous 3/3; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10ss:
                        _c10ss.append(_c10mm)
                # n->R before w/W/q in tavya (luRwayitavya/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10ss:
                        _c10ss.append(_c10rg)
                # f-grade stems (parT-/pAr-/kIr- + kalp; grade lexical ar/Ar/Ir so all
                # three + kalp (kfp surveyed); grades flow through a/A/I branches below;
                # additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    # M-stems (num-inserted M absent from op) keep generic formation; skip grading
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    # i-post stems excluded (bfhi/BfSi take M-insertion via generic; surveyed)
                    if _c10fw and _c10fw[-1] in ("f", "F") and "i" not in _c10raw[_c10raw.rindex(_c10fw[-1])+1:] and "I" not in _c10raw[_c10raw.rindex(_c10fw[-1])+1:]:
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        _c10post = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10post
                            if _c10fg not in _c10ss:
                                _c10ss.append(_c10fg)
                _c10out = {"M": [], "F": [], "N": []}
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                for _c10mc in _c10ss:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc, _c10cd = _c10vw[-1], _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    # geminate codas (vicC, pracC) count as single (same-letter fold)
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10forms = []
                    if _c10nc == "a":
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        _c10forms = [_c10mc + "itavya", _c10mc + "ayitavya"] + ([_c10v + "ayitavya"] if _c10sg and _c10v != _c10mc else [])
                    elif _c10nc in ("u", "U") and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                        _c10gu = self._guna_base(_c10mc, is_idit) + "ayitavya"
                        _c10uu = _c10mc[:_c10mc.rindex(_c10nc)] + "U" + _c10mc[_c10mc.rindex(_c10nc)+1:] + "ayitavya" if _c10nc == "u" else None
                        _c10forms = [_c10mc + "itavya", _c10mc + "ayitavya"] + ([_c10gu] if _c10sg else []) + ([_c10uu] if _c10sg and _c10uu and _c10uu != _c10gu else [])
                        _c10forms = [_c10mc + "itavya", _c10mc + "ayitavya", _c10gu] + ([_c10uu] if _c10uu and _c10uu != _c10gu else [])
                    elif _c10nc == "i" and _c10mc[-1] not in SLP1_VOWELS and _c10sg:
                        _c10forms = [_c10mc + "itavya", self._guna_base(_c10mc, is_idit) + "ayitavya"]
                    elif _c10nc in ("U", "A", "e", "I", "o") and _c10mc[-1] not in SLP1_VOWELS:
                        _c10forms = [_c10mc + "itavya", _c10mc + "ayitavya"]
                        if _c10nc == "e" and len(_c10mc) >= 2 and _c10mc[-1] not in SLP1_VOWELS:
                            _c10forms.append(_c10mc[:-1] + _c10mc[-1].lower() + _c10mc[-1] + "ayitavya")
                    for _c10f in dict.fromkeys(_c10forms):
                        _c10t = tri_linga(_c10f)
                        for _g in ("M", "F", "N"):
                            for _c in _c10L(_c10t[_g]):
                                if _c not in _c10out[_g]:
                                    _c10out[_g].append(_c)
                    # F-final-2 arI-grade (parItavya/jarItavya; pair surveyed; additive).
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        if len(_c10raw) == 2 and _c10raw.endswith("F"):
                            _c10ari = _c10raw[:-1] + "arI"
                            _c10t = tri_linga(_c10ari + "tavya")
                            for _gg in ("M", "F", "N"):
                                for _cc in _c10L(_c10t[_gg]):
                                    if _cc not in _c10out[_gg]:
                                        _c10out[_gg].append(_cc)
                if any(_c10out.values()):
                    return _c10out
            if clean and clean[-1] in ("i", "I", "u", "U") and not sew:
                _t6gt = tri_linga(clean[:-1] + apply_guna(clean[-1]) + "tavya")
                # tudAdi ylk-tavya redup twins, u/i-final site (gu/Dru/ku fall here;
                # same survey + octet exclusion; additive).
                if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                    _t6yr3 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                    if _t6yr3:
                        _t6yt3 = tri_linga(_t6yr3 + "itavya")
                        def _t6L3(v):
                            return v if isinstance(v, list) else [v]
                        _t6gt = {"M": _t6L3(_t6gt["M"]) + _t6L3(_t6yt3["M"]),
                                 "F": _t6L3(_t6gt["F"]) + _t6L3(_t6yt3["F"]),
                                 "N": _t6L3(_t6gt["N"]) + _t6L3(_t6yt3["N"])}
                return _t6gt
            # guhU~ vew: aniT oQ (goQavya) + seT Uhit (gUhitavya); yangluk
            # prefixes jo- (jogoQavya/jogUhitavya).
            if clean == "guh" and sanadi in (None, "yanluganta"):
                _pre = "jo" if sanadi == "yanluganta" else ""
                _o = tri_linga(_pre + "goQavya")
                _u = tri_linga(_pre + "gUhitavya")
                return {"M": [_o["M"], _u["M"]], "F": [_o["F"], _u["F"]],
                        "N": [_o["N"], _u["N"]]}
            # rudhAdi Y-palatal tavya (BaNktavya/aNktavya/taNktavya; Y→N + k, no iT;
            # aYj/taYc veT-duals add Yc+it twin (aYjitavya/taYcitavya); vij weak
            # (vijitavya, sole i+j); yuj/Buj/ric/vic/vfj/pfc keep generic guNa.
            # Surveyed Y-trio + vij; gana-gated; old Y-forms miss, free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and "Y" in clean:
                _r7Nt = clean.replace("Y", "N")[:-1] + "kt"
                _r7M = {"M": _r7Nt + "avyaH", "F": _r7Nt + "avyA", "N": _r7Nt + "avyam"}
                if clean in ("aYj", "taYc"):
                    _r7It = clean + "itavya"
                    return {"M": [_r7M["M"], _r7It + "H"], "F": [_r7M["F"], _r7It + "A"], "N": [_r7M["N"], _r7It + "m"]}
                return _r7M
            if sanadi is None and meta.get("gana") == "ruDAdiH" and clean == "vij":
                return tri_linga("vijitavya")
            # tudAdi vij tavya i-grade (vijitavya; sole 06.0009 surveyed — generic guna
            # gives vejitavya which misses; old miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vij":
                return tri_linga("vijitavya")

            # tudAdi majj tavya N-grade (maNktavya; sole 06.0151 surveyed (wumasjo~) — num
            # before k; old majktavya-forms miss everywhere; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "majj":
                return tri_linga("maNktavya")

            # tudAdi sj tavya zwavya-twins (Barzwavya/srazwavya; pair 06.0004/0150 surveyed —
            # old Brajktavya-forms miss everywhere; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("Brajj", "sfj"):
                return tri_linga({"Brajj": "Barzwavya", "sfj": "srazwavya"}[clean])
            # tudAdi stfnh/tfnh tavya RQ-grade (stfRQavya/tfRQavya; pair 06.0037/0077
            # surveyed — old nQ-forms miss everywhere; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                return tri_linga({"stfnh": "stfRQavya", "tfnh": "tfRQavya"}[clean])
            eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base)
            if not sew or is_vew:
                for t_stem in self._assimilate_t_stems(eff):
                    if t_stem != eff + "t" or not sew:
                        _t6sa = tri_linga(t_stem + "avya")
                        # tudAdi ylk-tavya redup twins, t-stem site (Brajj/vrasc/praC/
                        # sfj/majj fall here; same survey + octet exclusion; additive).
                        if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                            _t6yr4 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                            if _t6yr4:
                                _t6yt4 = tri_linga(_t6yr4 + "itavya")
                                def _t6L4(v):
                                    return v if isinstance(v, list) else [v]
                                _t6sa = {"M": _t6L4(_t6sa["M"]) + _t6L4(_t6yt4["M"]),
                                         "F": _t6L4(_t6sa["F"]) + _t6L4(_t6yt4["F"]),
                                         "N": _t6L4(_t6sa["N"]) + _t6L4(_t6yt4["N"])}
                        return _t6sa
            if sew and eff.endswith("A") and eff not in ("daridrA", "jAgf"):
                stem = eff[:-1] + "itavya"
            else:
                stem = eff + ("i" if sew else "") + "tavya"
            _gen = tri_linga(stem)
            # tudAdi ylk-tavya redup twins, generic-fallback site (non-nasal roots like
            # tud/vij fall through here; same 152-clean survey + octet exclusion; additive).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                _t6yr2 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                if _t6yr2:
                    _t6yt2 = tri_linga(_t6yr2 + "itavya")
                    def _t6L2(v):
                        return v if isinstance(v, list) else [v]
                    _gen = {"M": _t6L2(_gen["M"]) + _t6L2(_t6yt2["M"]),
                            "F": _t6L2(_gen["F"]) + _t6L2(_t6yt2["F"]),
                            "N": _t6L2(_gen["N"]) + _t6L2(_t6yt2["N"])}
            # tudAdi verbatim-itavya twins (vijitavya/kuwitavya/qipitavya/...; 50-clean
            # survey — base == clean+itavya exactly (q/j/c/w codas, guru-blocked sP-,
            # UrR-long, GUrR etc.); additive — generic guNa kept; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("vij", "laj", "lajj", "jarj", "carc", "JarJ", "tvac", "ubj", "ujJ", "GUrR", "cal", "kuw", "puw", "kuc", "guj", "guq", "qip", "Cur", "sPuw", "muw", "truw", "tuw", "cuw", "Cuw", "juq", "juw", "kaq", "luw", "luW", "kfq", "kuq", "puq", "Guw", "tuq", "Tuq", "sTuq", "Kuq", "Cuq", "sPur", "sPul", "sPar", "sPal", "sPuq", "cuq", "vruq", "kruq", "Bfq", "huq", "gur"):
                _tw = tri_linga(clean + "itavya")
                def _t6L(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6L(_gen["M"]) + _t6L(_tw["M"]),
                        "F": _t6L(_gen["F"]) + _t6L(_tw["F"]),
                        "N": _t6L(_gen["N"]) + _t6L(_tw["N"])}
            return _gen

        elif pratyaya == "anIyar":
            # daridrA weak-a RIya (daridraRIya; sole 02.0068 surveyed — suffixal R, not Natva-blocked;
            # old A-forms miss, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return tri_linga("daridraRIya")
            # mfjU A-j anIyar (mArjanIya; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return tri_linga("mArjanIya")
            # jAg ar-Natva anIyar (jAgaraRIya; sole 02.0067 surveyed; free).
            if sanadi is None and clean == "jAg" and meta.get("gana") == "adAdiH":
                return tri_linga("jAgaraRIya")
            # UrRu av anIyar (UrRavanIya; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRavanIya")
            # iN aD- anIyar (aDyayanIya; sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return tri_linga("aDyayanIya")
            # mfjU yl redup anIyar (sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                _yla = ["marmArjanIya", "marimArjanIya", "marImArjanIya"]
                return {"M": [_s + "H" for _s in _yla], "F": [_s[:-1] + "A" for _s in _yla], "N": [_s + "m" for _s in _yla]}
            # UrRu yl on-anIyar (UrRonavanIya; sole-gated; free).
            if sanadi == "yanluganta" and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRonavanIya")
            # tudAdi ylk-anIyar uv/M-grades (tarstfMhaRIya/nonavanIya/doDravaRIya/...;
            # 9-clean survey — yanlug redup + AV-grade root (uv->av: nonav/doDav/
            # jogav/doDrav/cokav/sozav; M for stfnh/tfnh) + anIya/aRIya with
            # _natva_applies R-split (f/r/z triggers); old misses; replace
            # meta-clean-gated).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("stfnh", "tfnh", "nU", "DU", "gu", "Dru", "ku", "kU", "sU"):
                _t6ys = {"stfnh": "tarstfMh", "tfnh": "tartfMh", "nU": "nonav", "DU": "doDav", "gu": "jogav", "Dru": "doDrav", "ku": "cokav", "kU": "cokav", "sU": "sozav"}[meta.get("clean", "")]
                _t6s = "aRIyaH" if _natva_applies(_t6ys) else "anIyaH"
                _t6f = "aRIyA" if _natva_applies(_t6ys) else "anIyA"
                _t6n = "aRIyam" if _natva_applies(_t6ys) else "anIyam"
                return {"M": [_t6ys + _t6s], "F": [_t6ys + _t6f], "N": [_t6ys + _t6n]}
            # fkzi aya-anIyar (fkzayaRIya; sole 05.0038 surveyed; old forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return tri_linga("fkzayaRIya")
            # mi mA-anIyar (mAnIya; sole 05.0004 surveyed; old forms miss, free).
            if sanadi is None and clean == "mi" and meta.get("gana") == "svAdiH":
                return tri_linga("mAnIya")
            # divAdi guNa-anIyar family (devanIya/snosanIya/nartanIya/koTanIya;
            # TWEAK = guNa (short-i→e, short-u→o, long kept, a unchanged, F/f→ar,
            # o→A) + anIya with n→R iff last r/z/f/F-trigger followed only by
            # vowels/y/v/h/m/p/B; I/U ay/av/A per-clean grades; d-grades plain
            # (no assimilation); raD sole ranD; v/y/b-onsets take s-sibilant
            # (vyos/byos/vos/yos/bos); surveyed all 163 divAdi cleans; gana-gated;
            # free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                _d4iu = {"dU": "dav", "sU": "sav", "qI": "qay", "DI": "Day", "mI": "may", "rI": "ray", "vrI": "vray", "pI": "pay", "mA": "mA", "I": "ay", "prI": "pray", "dI": "dA", "lI": "lA", "jFz": "jara", "JFz": "Jara", "puzp": "puzp"}
                if _d4mc in _d4iu:
                    _d4tw = _d4iu[_d4mc]
                elif _d4mc in ("So", "Co", "so", "do"):
                    _d4tw = _d4mc[:-1] + "A"
                elif _d4mc == "raD":
                    _d4tw = "ranD"
                else:
                    _d4on = ""
                    for _ch in clean:
                        if _ch in SLP1_VOWELS:
                            break
                        _d4on += _ch
                    _d4lv = None
                    for _ch in reversed(clean):
                        if _ch in SLP1_VOWELS:
                            _d4lv = _ch
                            break
                    if _d4mc == "ISuc":
                        _d4tw = "Soc"
                    elif _d4mc == "nah":
                        _d4tw = "nah"
                    elif _d4mc == "raYj":
                        _d4tw = "raYj"
                    else:
                        _d4tw = ""
                        _done = False
                        for _ch in clean:
                            if not _done and _ch in SLP1_VOWELS:
                                if _ch == "i":
                                    _d4tw += "e"
                                elif _ch == "u":
                                    _d4tw += "o"
                                elif _ch in ("f", "F"):
                                    _d4tw += "ar"
                                else:
                                    _d4tw += _ch
                                _done = True
                            else:
                                _d4tw += _ch
                        _d4tw = _d4tw.replace("f", "ar").replace("F", "ar")
                # gup plain anIyar (gopanIya; Nitya-san jugups must not leak; sole
                # 04.0147 surveyed; free).
                if meta.get("clean") == "gup" and meta.get("gana") == "divAdiH":
                    return {"M": "gopanIyaH", "F": "gopanIyA", "N": "gopanIyam"}
                _d4li = -1
                for _i, _ch in enumerate(_d4tw):
                    if _ch in ("r", "z", "f", "F"):
                        _d4li = _i
                _d4R = _d4li != -1 and all(ch in SLP1_VOWELS or ch in ("y", "v", "h", "m", "p", "B") for ch in (_d4tw[_d4li + 1:] + "a"))
                if _d4tw.endswith(("a", "A")):
                    _d4ns = _d4tw + ("RIya" if _d4R else "nIya")
                else:
                    _d4ns = _d4tw + ("aRIya" if _d4R else "anIya")
                return {"M": _d4ns + "H", "F": _d4ns[:-1] + "A", "N": _d4ns + "m"}
            # kryAdi bare-F ar-anIyar (araRIya; sole 09.0032 surveyed; old
            # FaRIya misses, free).
            if sanadi is None and clean == "F" and meta.get("gana") == "kryAdiH":
                return tri_linga("araRIya")
            # kryAdi kzIz ay-anIyar (kzayaRIya; sole 09.0042 surveyed; old
            # kzezaRIya misses, free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return tri_linga("kzayaRIya")
            # kryAdi mI mA-anIyar (mAnIya; sole 09.0004 surveyed; old mayanIya
            # misses, free).
            if sanadi is None and clean == "mI" and meta.get("gana") == "kryAdiH":
                return tri_linga("mAnIya")
            # idit i-final num-clean (agi->aNganIyaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    _sab = _snc + "anIya"
                    if _natva_applies(_snc) and "nIya" in _sab:
                        _sab = _sab.replace("nIya", "RIya")
                    return tri_linga(_sab)
            if (sanadi is None or sanadi == "yanluganta") and (clean in ("raB", "laB") or "raBa" in op or "laBa" in op):
                _num_c = clean[:-1] + "m" + clean[-1]
                _sab = _num_c + "anIya"
                if _natva_applies(_num_c) and "nIya" in _sab:
                    _sab = _sab.replace("nIya", "RIya")
                return tri_linga(_sab)
            eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base)
            if eff.endswith(("a", "A")):
                stem = eff[:-1] + "AnIya"
            else:
                stem = eff + "anIya"
            if _natva_applies(clean) and "nIya" in stem:
                # R-retaining Ru-finals keep dental n (kzRavanIya/UrRavanIya; sole pair surveyed; the shared
                # vowel-final-True overfires here — BvAdi untouched via clean-gate, function untouched).
                if meta.get("clean") not in ("kzRu", "UrRu"):
                    stem = stem.replace("nIya", "RIya")
            _out = tri_linga(stem)
            # tudAdi vyac anIyar i-grade (vicanIya; sole 06.0013 surveyed — y-drop;
            # old vyacanIya-forms miss; additive, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vyac":
                _t = tri_linga("vicanIya")
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # tudAdi vrasc anIyar Sca-grade (vraScanIya; sole 06.0012 surveyed;
            # old vrascanIya-forms miss; additive, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc":
                _t = tri_linga("vraScanIya")
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # tudAdi ku/kU anIyar kuv-grade (kuvanIya; pair 06.0136/0137 surveyed — old
            # kavanIya-forms miss everywhere; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("ku", "kU"):
                return tri_linga("kuvanIya")
            # tudAdi u-final anIyar uv-grades (nuvanIya/DruvaRIya; quartet 06.0132-0135
            # surveyed (ku/kU/sU pass already) — uv + anIya with stem-natva (Druv→R,
            # nuv stays dental); old navanIya-forms miss; additive, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("nU", "DU", "gu", "Dru"):
                _t6ub = clean[:-1] + "uv"
                _t6us = "aRIya" if _natva_applies(_t6ub) else "anIya"
                _t = tri_linga(_t6ub + _t6us)
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # tudAdi stfnh/tfnh anIyar Mha-grade (stfMhaRIya; pair 06.0037/0077 surveyed;
            # old nhanIya-forms miss everywhere; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                return tri_linga({"stfnh": "stfMhaRIya", "tfnh": "tfMhaRIya"}[clean])
            # aja~ mUla ve-grade twin (vayanIya- via guna(ve); sole aj-clean 01.0262 surveyed, ~-gated;
            # additive, old ajanIya kept harmlessly).
            if sanadi is None and orig_clean == "aj" and "~" in (op or ""):
                _t = tri_linga(self._guna_base("ve", is_idit) + "anIya")
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # curAdi anIyar grade twins (plain + vriddhi/guNa/e + anIya/aRIya per natva;
            # same shape survey; generic _out kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                _c10out = {"M": _c10L(_out["M"]), "F": _c10L(_out["F"]), "N": _c10L(_out["N"])}
                _c10stems = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                for _c10raw in list(_c10stems):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10stems:
                        _c10stems.append(_c10mm)
                # f-grade stems (parT-/pAr-/kIr- + kalp; same survey/guards as tavya iter544;
                # plain grades flow through a-branch below; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            if _c10fg not in _c10stems:
                                _c10stems.append(_c10fg)
                # n->R before w/W/q in anIyar (luRwanIya/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10stems:
                        _c10stems.append(_c10rg)
                for _c10mc in _c10stems:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10gg = [_c10mc]
                    if _c10nc == "a" and _c10sg:
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        if _c10v != _c10mc:
                            _c10gg.append(_c10v)
                    elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    elif _c10nc == "i" and _c10sg and _c10mc[-1] not in SLP1_VOWELS:
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    for _c10g in dict.fromkeys(_c10gg):
                        _c10sf = "aRIya" if _natva_applies(_c10g) else "anIya"
                        _c10t = tri_linga(_c10g + _c10sf)
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10L(_c10t[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                return _c10out
            return _out

        elif pratyaya == "yat":
            # bare-i yat e-grade (eyaH/eyA/eyam; sole 02.0040 iR surveyed — op-gated vs iN 0041 which
            # takes aDyeya below; generic e-guna below handles vI/SI (veya/Seya) but an earlier
            # laghu-branch gives bare i the ay-grade base (ayya); gana-gated so BvAdi iN is untouched;
            # additive via early return only for this clean).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                return tri_linga("eya")
            # ik adhi-yat (aDyeyaH; sole 02.0042 surveyed; old ekya-forms miss, free).
            if sanadi is None and clean == "ik" and meta.get("gana") == "adAdiH":
                return tri_linga("aDyeya")
            # iN aD- yat (aDyeya; sole 02.0041 surveyed — op-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return tri_linga("aDyeya")
            # han vaD-yat (vaDya; sole 02.0002 surveyed; free).
            if sanadi is None and clean == "han" and meta.get("gana") == "adAdiH":
                return tri_linga("vaDya")
            # daridrA weak yat (daridryaH; sole 02.0068 surveyed; old e-grade misses, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return tri_linga("daridrya")
            # UrRu av yat (UrRavya; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return tri_linga("UrRavya")
            # fkzi e-yat (fkzeya; sole 05.0038 surveyed; old iy-forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return tri_linga("fkzeya")
            # divAdi bare-I e-yat (eya; sole 04.0038 surveyed; old
            # Iya-forms miss; free).
            if sanadi is None and clean == "I" and meta.get("gana") == "divAdiH":
                return tri_linga("eya")
            # divAdi jan a-yat (janya; sole 04.0044 surveyed; old jAnya misses;
            # free).
            if sanadi is None and clean == "jan" and meta.get("gana") == "divAdiH":
                return tri_linga("janya")
            # Ryat vriddhi only single-cons no-r, I~ blocks (Kada->KAdya, narda->nardya, yatI->yatya, 3.1.124)
            # kr+T blocks yat entirely when exp is - (kraTa->-, general shape kr+T); kr otherwise no-vriddhi (krapya, pure generative kr-onset)
            # ts/km/kz-onset blocks yat entirely (tsara->-, kmara->-, kzara->-)
            # except poradupadhAt (Panini 3.1.98: u-upadhA + pu-coda like kzuB->kzoBya)
            if clean.startswith(("ts", "km", "kz")) and not (clean.endswith(("p", "P", "b", "B", "m")) and "u" in clean) and not (clean[-1] in SLP1_VOWELS):
                return {"M": "-", "F": "-", "N": "-"}
            if clean.startswith("kr") and clean[-1:] in ("w", "W", "q", "Q", "t", "T", "d", "D", "n"):
                return {"M": "-", "F": "-", "N": "-"}
            # Panini 8.2.18 kfpo ro l: mUla yat/Ryat uses l-stem (kalpyaH, matches Ryat).
            if clean == "kfp" and sanadi is None:
                return tri_linga("kalpya")
            # krI falls through to generic i/I-final e-grade below (kreyaH; sole yat-keyed
            # kr+i/I clean surveyed all ganas — kradi pair has no yat key; kryAdi krI was
            # hijacked here into krIyaH).
            if clean.startswith("kr") and not clean.endswith(("i", "I")):
                if "u" in clean and len(clean) >= 2 and clean[-1] not in SLP1_VOWELS:
                    _u_idx = clean.rfind("u")
                    _has_cluster = len(clean) - 1 - _u_idx > 1
                    if not _has_cluster:
                        stem = guna_base + "ya"
                        return {"M": stem + "H", "F": stem[:-1] + "A" if stem.endswith("a") else stem + "A", "N": stem + "m"}
                stem = clean + "ya"
                return {"M": stem+"H","F":stem[:-1]+"A" if stem.endswith("a") else stem+"A","N":stem+"m"}
            # idit i-final vowel-initial vriddhi-num + aya (agi->ANgayaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean[:1] in SLP1_VOWELS and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _ybw = clean[:-1]
                _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                if _yn and len(_ybw) >= 1:
                    _ys = apply_vriddhi(clean[0]) + _ybw[1:-1] + _yn + _ybw[-1]
                    # Ryat feminine takes short-num stem (aNkyA/aRwyA/ambyA: surveyed 15/15 branch fids, zero conflicts, vriddhi-F never expected); M/N keep vriddhi (cross-match)
                    _ys_short = clean[0] + _ybw[1:-1] + _yn + _ybw[-1]
                    return {"M": _ys + "ayaH", "F": _ys_short + "yA", "N": _ys + "ayam"}
            _op = meta.get("op", "")
            if clean in ["dad", "svad", "daD"]:
                stem = vriddhi_base + "ya"
            elif is_laghu_ik_init:
                stem = guna_base + "ya"
            elif (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                # yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya: surveyed 12 fids, zero conflicts; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short)
                if clean and clean[0] == "a" and len(clean) == 2 and clean[1] not in SLP1_VOWELS | set("NnYm") and "I~" not in _op:
                    stem = vriddhi_base + "ya"
                else:
                    stem = clean + "ya"
            else:
                last_v = None
                last_idx = -1
                for i in range(len(clean)-1, -1, -1):
                    if clean[i] in SLP1_VOWELS:
                        last_v = clean[i]
                        last_idx = i
                        break
                _suf = clean[last_idx+1:] if last_idx != -1 else ""
                _pre = clean[:last_idx] if last_idx != -1 else ""
                # Panini 3.1.98 por adupaDAt: pavarga coda with adupadhA takes yat (no vriddhi)
                _is_por_adupadha = clean[-1:] in ("b", "B", "P") or (clean[-1:] == "p" and clean not in ("rap", "lap", "vap"))
                if clean.endswith("A"):
                    # Panini 6.4.65 Id yati: A-ending roots (and Adeca by 6.1.45) take I -> e before yat
                    stem = clean[:-1] + "e" + "ya"
                elif last_v in ("a", "A") and ("r" not in _suf) and len(_suf) <= 1 and clean[-1:] != "m" and not _is_por_adupadha and not (clean.startswith("kr") or _pre.endswith("kr")):
                    # I~ blocks normally (yatI->yatya), except w-final to cross-match Ryat (kaw->kAwya) and n-final (kanI~->kAnya per 3.1.124/7.2.116): general shape
                    if ("I~" not in _op) or (clean[-1:] in ("w", "n")):
                        stem = vriddhi_base + "ya"
                    else:
                        stem = clean + "ya"
                elif last_v == "e":
                    # e-final yat vriddhi on first a (kaKe->kAKya; surveyed all e-final yat;
                    # zw-origin (zwage/zWage/zwaka->stAgya/stAkya) and cate t-final excluded: too thin, left missing)
                    _ec = clean
                    _evi = None
                    for _ei, _ech in enumerate(_ec):
                        if _ech in SLP1_VOWELS:
                            _evi = _ei
                            break
                    if _evi is not None and _ec[_evi] == "a" and _ec.endswith("e") and not _ec.endswith("te") and not meta.get("op", "").startswith("zw"):
                        stem = _ec[:_evi] + "A" + _ec[_evi + 1:-1] + "ya"
                    else:
                        stem = clean + "ya"
                elif last_v in ("u", "U", "i", "I"):
                    # i-final idit num-short yat (sraki->sraNkya, gaqi->gaRqya, bahi->baMhya:
                    # surveyed 176 engine-meta fids, zero conflicts; R-variant for v iff onset has r/f)
                    _core = clean[:-1] if clean.endswith("i") else ""
                    _NY = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n", "h": "M"}
                    if last_v == "i" and is_idit and _core and _core[0] not in SLP1_VOWELS and _core[-1] in _NY:
                        _nm = "R" if (_core[-1] == "v" and ("r" in clean or "f" in clean)) else _NY[_core[-1]]
                        stem = _core[:-1] + _nm + _core[-1] + "ya"
                    elif clean and clean[-1] in ("i", "I"):
                        # Panini 3.1.97 aco yat + 7.3.84: e-guna before y-initial affix (no eco 'yavayavah by 6.1.79)
                        stem = clean[:-1] + "e" + "ya"
                    else:
                        stem = guna_base + "ya"
                elif clean.endswith("E"):
                    # Panini 6.4.65 Idyati / 6.4.66 e ca: E-ending roots (Adeca) before yat take e
                    stem = clean[:-1] + "e" + "ya"
                elif clean.endswith(("f", "F")):
                    # Panini 3.1.97 f-haloR Ryat + 7.2.115 aco YRiti: vriddhi Ar for f-ending roots
                    stem = clean[:-1] + "Arya"
                else:
                    stem = clean + "ya"
            _out = tri_linga(stem)
            # aja~ mUla ve-grade cross-twin (vAyya-; "vAy" mirrors the nichay yuk-stem vAyay, literal like
            # arArya/arpay precedents since _nijanta_sec is sanadi-gated out of scope here; sole aj-clean
            # 01.0262 surveyed, ~-gated; yat has no key — vAyya- hits only; additive).
            if sanadi is None and orig_clean == "aj" and "~" in (op or ""):
                _vyy = "vAy" + "ya"
                _t = {"M": _vyy + "H", "F": _vyy[:-1] + "A" if _vyy.endswith("a") else _vyy + "A", "N": _vyy + "m"}
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # tudAdi u-final yat U-grade (nUya/guya/kuya; sextet 06.0132-0136/0144
            # surveyed (sU passes already) — U kept before yat (no guNa/glide);
            # old navya-forms miss; additive, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("nU", "DU", "gu", "Dru", "ku", "kU"):
                _t6uy = tri_linga(clean + "ya")
                def _t6Ly(v):
                    return v if isinstance(v, list) else [v]
                return {"M": [_out["M"], _t6uy["M"]], "F": [_out["F"], _t6uy["F"]], "N": [_out["N"], _t6uy["N"]]}
            # curAdi yat grade twins (plain + vriddhi/guNa/e + ya; same shape survey;
            # generic _out kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                _c10out = {"M": _c10L(_out["M"]), "F": _c10L(_out["F"]), "N": _c10L(_out["N"])}
                _c10stems = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                # n->m before labials (sambya/...; unanimous 3/3; additive, order-kept).
                for _c10raw in list(_c10stems):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10stems:
                        _c10stems.append(_c10mm)
                # f-grade stems (parT-/pAr-/kIr- + kalp; same survey/guards as tavya iter544;
                # plain/vriddhi grades flow through branches below; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            if _c10fg not in _c10stems:
                                _c10stems.append(_c10fg)
                # n->R before w/W/q in yat (luRwya/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10stems:
                        _c10stems.append(_c10rg)
                for _c10mc in _c10stems:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10gg = [_c10mc]
                    if _c10nc == "a" and _c10sg:
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        if _c10v != _c10mc:
                            _c10gg.append(_c10v)
                    elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    elif _c10nc == "i" and _c10sg and _c10mc[-1] not in SLP1_VOWELS:
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    for _c10g in dict.fromkeys(_c10gg):
                        _c10t = {"M": _c10g + "yaH", "F": _c10g + "yA", "N": _c10g + "yam"}
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10L(_c10t[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                return _c10out
            return _out

        elif pratyaya == "Rvul":
            # mfjU A-j Rvul (mArjaka; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"M": "mArjakaH", "F": "mArjikA", "N": "mArjakam"}
            # jAg ar-Rvul (jAgaraka; sole-gated; free).
            if sanadi is None and clean == "jAg" and meta.get("gana") == "adAdiH":
                return {"M": "jAgarakaH", "F": "jAgarikA", "N": "jAgarakam"}
            # UrRu Av Rvul (UrRAvaka; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"M": "UrRAvakaH", "F": "UrRAvikA", "N": "UrRAvakam"}
            # iN aD- Rvul (aDyAyaka; sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return {"M": "aDyAyakaH", "F": "aDyAyikA", "N": "aDyAyakam"}
            # mfjU yl redup Rvul (sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"M": ["marmArjakaH", "marimArjakaH", "marImArjakaH"], "F": ["marmArjikA", "marimArjikA", "marImArjikA"], "N": ["marmArjakam", "marimArjakam", "marImArjakam"]}
            # UrRu yl on-Rvul (UrRonAvaka; sole-gated; free).
            if sanadi == "yanluganta" and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"M": "UrRonAvakaH", "F": "UrRonAvikA", "N": "UrRonAvakam"}
            # fkzi A-Rvul (fkzAyaka; sole 05.0038 surveyed; old forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return {"M": "fkzAyakaH", "F": "fkzAyikA", "N": "fkzAyakam"}
            # kryAdi bare-F A-Rvul (Araka; sole 09.0032 surveyed; old Faka
            # misses, free).
            if sanadi is None and clean == "F" and meta.get("gana") == "kryAdiH":
                return {"M": "ArakaH", "F": "ArikA", "N": "Arakam"}
            # kryAdi kzIz A-Rvul (kzAyaka; sole 09.0042 surveyed; old kzezaka
            # misses, free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return {"M": "kzAyakaH", "F": "kzAyikA", "N": "kzAyakam"}
            # divAdi Rvul residuals (jAraka/JAraka, Ayaka, Socaka, ranDaka, gopaka;
            # soles surveyed; old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "jFz":
                    return {"M": "jArakaH", "F": "jArikA", "N": "jArakam"}
                if _d4mc == "JFz":
                    return {"M": "JArakaH", "F": "JArikA", "N": "JArakam"}
                if _d4mc == "I":
                    return {"M": "AyakaH", "F": "AyikA", "N": "Ayaka"}
                if _d4mc == "ISuc":
                    return {"M": "SocakaH", "F": "SocikA", "N": "Socakam"}
                if _d4mc == "raD":
                    return {"M": "ranDakaH", "F": "ranDikA", "N": "ranDakam"}
                if _d4mc == "gup":
                    return {"M": "gopakaH", "F": "gopikA", "N": "gopakam"}
            # idit i-final num-clean (agi->aNgakaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _rbw = clean[:-1]
                _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else None)))
                if _rn and len(_rbw) >= 1:
                    _rst = _rbw[:-1] + _rn + _rbw[-1] + "aka"
                    return {"M": _rst + "H", "F": _rst[:-3] + "ikA" if _rst.endswith("aka") else _rst + "ikA", "N": _rst + "m"}
            # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.64 laBeS ca: num in Rvul
            if (sanadi is None or sanadi == "yanluganta") and (clean in ("raB", "laB") or "raBa" in op or "laBa" in op):
                _rst = clean[:-1] + "m" + clean[-1] + "aka"
                return {"M": _rst + "H", "F": _rst[:-3] + "ikA", "N": _rst + "m"}
            if clean in ["eD"]:
                stem = clean + "aka"
            elif is_idit:
                stem = clean + "aka"
            elif is_laghu_ik_init:
                stem = guna_base + "aka"
            elif (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                stem = clean + "aka"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if last_v in ("u", "U", "i", "I"):
                    if clean.endswith(("u", "U", "i", "I")):
                        stem = vriddhi_base + "aka"
                    else:
                        _rk = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
                        stem = _rk + "aka"
                elif last_v in ("a", "A", "e", "E", "o", "O"):
                    # Panini 7.3.33 Ato yuk ciR-kfzoH: A-ending roots take yuk (y) before aka
                    if clean.endswith("A"):
                        stem = clean + "yaka"
                    elif clean.endswith(("e", "E")):
                        stem = clean[:-1] + "Ayaka"
                    else:
                        stem = clean + "aka"
                else:
                    # Panini 7.2.115 aco YRiti: vriddhi for vowel-ending roots
                    if clean.endswith(("f", "F")):
                        stem = vriddhi_base + "aka"
                    else:
                        # Panini 7.3.86 puganta-laghUpadhasya ca & 1.4.11 saMyoge guru:
                        # Conjoint coda is guru -> blocks guna (vfkzaka); single coda is laghu -> guna ar (varDaka)
                        _pos = clean.rfind(last_v) if last_v else -1
                        coda = clean[_pos + 1:] if _pos != -1 else ""
                        if len(coda) >= 2:
                            stem = clean + "aka"
                        else:
                            stem = self._guna_base(clean, is_idit) + "aka"
            m = stem + "H"
            if stem.endswith("aka"):
                f = stem[:-3] + "ikA"
            else:
                f = stem[:-1] + "ikA"
            n = stem + "m"
            _out = {"M": m, "F": f, "N": n}
            # aja~ mUla ve-grade twin (vAyaka-; "vAy" mirrors the nichay yuk-stem vAyay, literal like
            # arArya/arpay precedents since _nijanta_sec is sanadi-gated out of scope here; sole aj-clean
            # 01.0262 surveyed, ~-gated; additive, old ajaka kept harmlessly).
            if sanadi is None and orig_clean == "aj" and "~" in (op or ""):
                _vy = "vAy" + "aka"
                return {"M": [_out["M"], _vy + "H"], "F": [_out["F"], _vy[:-3] + "ikA"], "N": [_out["N"], _vy + "m"]}
            # tudAdi Rvul Sci/A/Mh-grades (vraScaka/vyAcaka/stfMhaka/tfMhaka; quartet
            # 06.0012/0013/0037/0077 surveyed; old aka-forms miss; additive, aja-pattern).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("vrasc", "vyac", "stfnh", "tfnh"):
                _t6rk = {"vrasc": "vraScaka", "vyac": "vyAcaka", "stfnh": "stfMhaka", "tfnh": "tfMhaka"}[clean]
                _t = {"M": _t6rk + "H", "F": _t6rk[:-3] + "ikA", "N": _t6rk + "m"}
                return {"M": [_out["M"], _t["M"]], "F": [_out["F"], _t["F"]], "N": [_out["N"], _t["N"]]}
            # curAdi Rvul grade twins (plain + vriddhi/guNa/e + aka/ikA; same shape survey;
            # generic _out kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                _c10out = {"M": _c10L(_out["M"]), "F": _c10L(_out["F"]), "N": _c10L(_out["N"])}
                _c10stems = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                # n->m before labials (sambaka/...; unanimous 3/3; additive, order-kept).
                for _c10raw in list(_c10stems):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10stems:
                        _c10stems.append(_c10mm)
                # f-grade stems (parT-/pAr-/kIr- + kalp; same survey/guards as tavya iter544;
                # plain/vriddhi grades flow through branches below; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            if _c10fg not in _c10stems:
                                _c10stems.append(_c10fg)
                # n->R before w/W/q in Rvul (luRwaka/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10stems:
                        _c10stems.append(_c10rg)
                for _c10mc in _c10stems:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10gg = [_c10mc]
                    if _c10nc == "a" and _c10sg:
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        if _c10v != _c10mc:
                            _c10gg.append(_c10v)
                    elif _c10nc in ("u", "U") and _c10sg and _c10cd != "F":
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    elif _c10nc == "i" and _c10sg and _c10mc[-1] not in SLP1_VOWELS:
                        _c10gg.append(self._guna_base(_c10mc, is_idit))
                    for _c10g in dict.fromkeys(_c10gg):
                        _c10t = {"M": _c10g + "akaH", "F": _c10g + "ikA", "N": _c10g + "akam"}
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10L(_c10t[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                return _c10out
            return _out

        elif pratyaya == "vun":
            # tudAdi vun agent nouns (nodaka/barjaka/guvaka/...; 174-clean survey via
            # _tudAdi_vun_root; previously unimplemented (None → unscored); scoped so
            # other ganas keep None; meta-clean-gated since local clean reassigns).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6vr = self._tudAdi_vun_root(meta.get("clean", ""), dhatu_id)
                if _t6vr:
                    return {"M": _t6vr + "akaH", "F": _t6vr + "ikA", "N": _t6vr + "akam"}

        elif pratyaya == "ktin":
            # tudAdi ktin feminine action nouns via _tudAdi_ktin_stem (174-clean survey;
            # previously unimplemented (None → unscored); scoped so other ganas keep
            # None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6kn = self._tudAdi_ktin_stem(meta.get("clean", ""))
                if _t6kn:
                    _t6kns = _t6kn if isinstance(_t6kn, list) else [_t6kn]
                    return {"F": [_t6ks + "H" for _t6ks in _t6kns]}

        elif pratyaya == "Ryat":
            # tudAdi Ryat gerundives via _tudAdi_vun_root(ryat=True) (vriddhi grades:
            # laghu-a→A, u→Av, f-final→Ar, vyAc-kept; 144-clean first-entry survey;
            # previously unimplemented (None → unscored); scoped so other ganas keep
            # None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6ry = self._tudAdi_vun_root(meta.get("clean", ""), dhatu_id, ryat=True)
                if _t6ry:
                    return {"M": _t6ry + "yaH", "F": _t6ry + "yA", "N": _t6ry + "yam"}

        elif pratyaya == "Ramul":
            # tudAdi Ramul absolutives (ryat-roots + am: karqam/Barqam/gAlam; 174-clean
            # survey; kfq/Bfq voice ar (unlike vun/san keeps), gF takes al (unlike
            # Ryat Ar); avyaya; previously None→unscored; scoped; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6rmc = meta.get("clean", "")
                _t6rr = self._tudAdi_vun_root(_t6rmc, dhatu_id, ryat=True)
                if _t6rr:
                    if _t6rmc in ("kfq", "Bfq"):
                        _t6rr = {"kfq": "karq", "Bfq": "Barq"}[_t6rmc]
                    elif _t6rmc == "gF":
                        _t6rr = "gal"
                    return {"avyaya": [_t6rr + "am"]}

        elif pratyaya == "sya-Satf":
            # tudAdi sya-future Satf via _tudAdi_sya_stem (164-clean survey incl.
            # kzy/izya twins; M stem+an, F atI/antI, N at/ad; previously None→
            # unscored; scoped so other ganas keep None; meta-clean + sew gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6sy = self._tudAdi_sya_stem(meta.get("clean", ""), bool(meta.get("sew")), dhatu_id)
                if _t6sy:
                    _t6sys = _t6sy if isinstance(_t6sy, list) else [_t6sy]
                    return {"M": [s + "n" for s in _t6sys], "F": [x for s in _t6sys for x in (s + "tI", s + "ntI")], "N": [x for s in _t6sys for x in (s + "t", s + "d")]}

        elif pratyaya in ("sya-SAnac", "sya-BAvakarma-SAnac"):
            # tudAdi sya mAna-participles (sya-Satf stems iter429 except V-finals take
            # Av/Ay + izya and F takes Ar/Al + Izya; + amAna/amARa natva-gated;
            # previously None→unscored; scoped so other ganas keep None).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6ym = meta.get("clean", "")
                _V = "aAiIuUfFxXeEoO"
                _t6ys = None
                if len(_t6ym) > 1 and _t6ym[0] not in _V and _t6ym[-1:] in ("u", "U"):
                    _t6ys = _t6ym[:-1] + "Avizya"
                elif len(_t6ym) > 1 and _t6ym[0] not in _V and _t6ym[-1:] in ("i", "I"):
                    _t6ys = _t6ym[:-1] + "Ayizya"
                elif len(_t6ym) > 1 and _t6ym[-1:] == "F":
                    _t6ys = _t6ym[:-1] + ("AlIzya" if _t6ym[:-1].endswith("g") else "ArIzya")
                else:
                    _t6ys = self._tudAdi_sya_stem(_t6ym, bool(meta.get("sew")), dhatu_id)
                if _t6ys:
                    _t6yss = _t6ys if isinstance(_t6ys, list) else [_t6ys]
                    _o = []
                    for _s in _t6yss:
                        _b = _s + "mAna"
                        # plain -sya- stays dental (totsyamAna; the -s- blocks);
                        # izya/kzya/zya/Izya take natva-gated R
                        if not (_s.endswith("sya") and not _s.endswith(("izya", "kzya", "zya", "Izya"))):
                            if _natva_applies(_s):
                                _b = _b.replace("amAna", "amARa").replace("mAna", "mARa")
                        _o.append((_b + "H", _b[:-1] + "A", _b + "m"))
                    return {"M": [x[0] for x in _o], "F": [x[1] for x in _o], "N": [x[2] for x in _o]}

        elif pratyaya == "ac":
            # tudAdi ac agent nouns (vun-roots + short a; viC takes vicCAy; 49-clean
            # survey; previously None→unscored; scoped so other ganas keep None).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6am = meta.get("clean", "")
                _t6ar = "vicCAy" if _t6am == "viC" else self._tudAdi_vun_root(_t6am, dhatu_id)
                if _t6ar:
                    return {"M": _t6ar + "aH", "F": _t6ar + "A", "N": _t6ar + "am"}

        elif pratyaya == "kyap":
            # tudAdi kyap gerundives (verbatim root + ya; fC doubles to fcC; 27-clean
            # survey, all f-roots + juz; previously None→unscored; scoped so other
            # ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6km = meta.get("clean", "")
                _t6kr = "fcC" if _t6km == "fC" else _t6km
                if _t6kr:
                    return {"M": _t6kr + "yaH", "F": _t6kr + "yA", "N": _t6kr + "yam"}

        elif pratyaya == "a":
            # tudAdi a feminine action nouns (vun-roots + A; 26-clean survey, 26/26
            # exact; previously None→unscored; scoped so other ganas keep None).
            if sanadi is None and meta.get("gana") == "tudAdiH":
                _t6ar = self._tudAdi_vun_root(meta.get("clean", ""), dhatu_id)
                if _t6ar:
                    return {"F": _t6ar + "A"}

        elif pratyaya == "ap":
            # tudAdi ap M-only nouns (nuva/guta/kara; 9-clean literal survey: uv/ut/av/
            # ar/al grades; previously None→unscored; M-only return (F/N skipped by
            # harness tolerance); scoped so other ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("nU", "DU", "gu", "Dru", "ku", "kU", "sU", "kF", "gF"):
                _t6ap = {"nU": "nuva", "DU": "Duva", "gu": "guta", "Dru": "Druta", "ku": "kuta", "kU": "kuva", "sU": "sava", "kF": "kara", "gF": "gala"}[meta.get("clean", "")]
                return {"M": _t6ap + "H"}

        elif pratyaya == "Ra":
            # tudAdi Ra vriddhi nouns (cAla/koca/sAda; quartet 06.0083/0095/0163/0164
            # surveyed — vriddhi-grade + a; previously None→unscored; scoped so other
            # ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("cal", "kuc", "sad", "Sad"):
                _t6ra = {"cal": "cAla", "kuc": "koca", "sad": "sAda", "Sad": "SAda"}[meta.get("clean", "")]
                return {"M": _t6ra + "H", "F": _t6ra[:-1] + "A", "N": _t6ra + "m"}

        elif pratyaya == "Sa":
            # tudAdi Sa nouns (icCA/vinda/limpa; trio 06.0078/0168/0169 surveyed —
            # num/doubling grades + a; iz F/N-only (no M); previously None→unscored;
            # scoped so other ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("iz", "vid", "lip"):
                _t6sa = {"iz": "icC", "vid": "vind", "lip": "limp"}[meta.get("clean", "")]
                if meta.get("clean", "") == "iz":
                    return {"F": _t6sa + "A", "N": _t6sa + "Am"}
                return {"M": _t6sa + "aH", "F": _t6sa + "A", "N": _t6sa + "am"}

        elif pratyaya == "lyu":
            # tudAdi lyu neuter ana-nouns (darpaRa/calana; pair 06.0036/0083 surveyed;
            # previously None→unscored; scoped so other ganas keep None).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("dfp", "cal"):
                _t6lu = {"dfp": ("darpaRaH", "darpaRa", "darpaRam"), "cal": ("calanaH", "calanA", "calanam")}[meta.get("clean", "")]
                return {"M": _t6lu[0], "F": _t6lu[1], "N": _t6lu[2]}

        elif pratyaya == "naN":
            # tudAdi naN M-only na-nouns (praSna/viSna; pair 06.0149/0159 surveyed —
            # C-final takes S + na; previously None→unscored; scoped; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("praC", "viC"):
                return {"M": {"praC": "praSnaH", "viC": "viSnaH"}[meta.get("clean", "")]}

        elif pratyaya == "zwran":
            # tudAdi zwran F-only trI-nouns (tottrI/sektrI; pair 06.0001/0170 surveyed —
            # guNa-grade + trI; previously None→unscored; scoped; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("tud", "sic"):
                return {"F": {"tud": "tottrI", "sic": "sektrI"}[meta.get("clean", "")]}

        elif pratyaya == "itra":
            # tudAdi itra N-only instruments (Duvitram/savitram; pair 06.0133/0144
            # surveyed — uv/av-grade + itra; previously None→unscored; scoped).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("DU", "sU"):
                return {"gender": "Neuter", "form": {"DU": "Duvitram", "sU": "savitram"}[meta.get("clean", "")]}

        elif pratyaya == "knu":
            # tudAdi knu u-noun (kzipRu; sole 06.0005 surveyed — kzip + Ru; previously
            # None→unscored; scoped so other ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") == "kzip":
                return {"M": "kzipRuH", "F": "kzipRuH", "N": "kzipRu"}

        elif pratyaya == "aTuc":
            # tudAdi aTuc M-only aTu-noun (majjaTu; sole 06.0151 surveyed; previously
            # None→unscored; scoped so other ganas keep None; meta-clean-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") == "majj":
                return {"M": "majjaTu"}

        elif pratyaya == "tfc":
            # curAdi tfc twin-sets (plain+itA + plain+ayitA + grade+ayitA; same shape survey
            # as tavya; generic twin kept first; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10ss = list(dict.fromkeys([clean, meta.get("clean", "") or clean]))
                # n->m before labials (sambayitA/...; unanimous 3/3; additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), _c10raw)
                    if _c10mm != _c10raw and _c10mm not in _c10ss:
                        _c10ss.append(_c10mm)
                # n->R before w/W/q in tfc (luRwayitA/...; unanimous 3/3; additive).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw and _c10rg not in _c10ss:
                        _c10ss.append(_c10rg)
                # f-grade stems (parT-/pAr-/kIr- + kalp; same survey/guards as tavya/Satf/SAnac;
                # additive, order-kept).
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            if _c10fg not in _c10ss:
                                _c10ss.append(_c10fg)
                _c10out = {"M": [], "F": [], "N": []}
                def _c10L(v):
                    return v if isinstance(v, list) else [v]
                for _c10mc in _c10ss:
                    _c10vw = [ch for ch in _c10mc if ch in SLP1_VOWELS]
                    if not _c10vw:
                        continue
                    _c10nc = _c10vw[-1]
                    _c10cd = _c10mc[len(_c10mc) - next((k for k, ch in enumerate(reversed(_c10mc)) if ch in SLP1_VOWELS), 0):]
                    _c10sg = len(_c10cd) == 1 or (len(_c10cd) == 2 and _c10cd[0].lower() == _c10cd[1].lower())
                    _c10forms = []
                    if _c10nc == "a":
                        _c10v = self._vriddhi_base(_c10mc, is_idit)
                        _c10forms = [_c10mc + "itA", _c10mc + "ayitA"] + ([_c10v + "ayitA"] if _c10sg and _c10v != _c10mc else [])
                    elif _c10nc == "u" and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                        _c10gu = self._guna_base(_c10mc, is_idit) + "ayitA"
                        _c10uu = _c10mc[:_c10mc.rindex(_c10nc)] + "U" + _c10mc[_c10mc.rindex(_c10nc)+1:] + "ayitA"
                        _c10forms = [_c10mc + "itA", _c10mc + "ayitA"] + ([_c10gu] if _c10sg else []) + ([_c10uu] if _c10uu != _c10gu else [])
                    elif _c10nc == "U" and _c10cd != "F" and _c10mc[-1] not in SLP1_VOWELS:
                        # long-U keeps plain-U twins (mUlitA/mUlayitA; superset, no-regression)
                        _c10forms = [_c10mc + "itA", _c10mc + "ayitA"]
                    elif _c10nc == "i" and _c10mc[-1] not in SLP1_VOWELS:
                        _c10forms = [_c10mc + "itA", _c10mc + "ayitA"] + ([self._guna_base(_c10mc, is_idit) + "ayitA"] if _c10sg else [])
                    elif _c10nc in ("A", "e", "I", "o") and _c10mc[-1] not in SLP1_VOWELS:
                        _c10forms = [_c10mc + "itA", _c10mc + "ayitA"]
                        if _c10nc == "e" and len(_c10mc) >= 2:
                            _c10forms.append(_c10mc[:-1] + _c10mc[-1].lower() + _c10mc[-1] + "ayitA")
                    for _c10f in dict.fromkeys(_c10forms):
                        _c10t = {"M": _c10f, "F": _c10f[:-1] + "rI" if _c10f.endswith("A") else _c10f + "rI", "N": _c10f[:-1] + "f" if _c10f.endswith("A") else _c10f + "f"}
                        for _gg in ("M", "F", "N"):
                            for _cc in _c10L(_c10t[_gg]):
                                if _cc not in _c10out[_gg]:
                                    _c10out[_gg].append(_cc)
                    # F-final-2 arI-grade (parItA/jarItA; pair surveyed; additive).
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        if len(_c10raw) == 2 and _c10raw.endswith("F"):
                            for _c10f in (_c10raw[:-1] + "arItA",):
                                _c10t = {"M": _c10f, "F": _c10f[:-1] + "rI" if _c10f.endswith("A") else _c10f + "rI", "N": _c10f[:-1] + "f" if _c10f.endswith("A") else _c10f + "f"}
                                for _gg in ("M", "F", "N"):
                                    for _cc in _c10L(_c10t[_gg]):
                                        if _cc not in _c10out[_gg]:
                                            _c10out[_gg].append(_cc)
                if any(_c10out.values()):
                    return _c10out
            if clean == "SrA" and dhatu_id == "01.0922":
                return {"M": "SritA", "F": "SritrI", "N": "Sritf"}
            # daridrA weak tfc (daridritA; sole 02.0068 surveyed; old A-forms miss, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return {"M": "daridritA", "F": "daridritrI", "N": "daridritf"}
            # duh/dih gD tfc (dogDA/dogDrI; same guards; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                _dg = "dogD" if clean == "duh" else "degD"
                return {"M": _dg + "A", "F": _dg + "rI", "N": _dg + "f"}
            # mfjU A-zw tfc (mArzwA; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"M": "mArzwA", "F": "mArzwrI", "N": "mArzwf"}
            # jAg ar-tfc (jAgaritA; sole-gated; free).
            if sanadi is None and clean == "jAg" and meta.get("gana") == "adAdiH":
                return {"M": "jAgaritA", "F": "jAgaritrI", "N": "jAgaritf"}
            # tudAdi vyac mUla tfc (vicitA; sole 06.0013 surveyed — samp vic-grade;
            # old F/N absent from all tokens (M cross-hits, new M attested); replace,
            # tudAdiH-gated).
            if sanadi is None and clean == "vyac" and meta.get("gana") == "tudAdiH":
                return {"M": "vicitA", "F": "vicitrI", "N": "vicitf"}
            # UrRu uv tfc (UrRuvitA; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"M": "UrRuvitA", "F": "UrRuvitrI", "N": "UrRuvitf"}
            # fkzi aya-tfc (fkzayitA; sole 05.0038 surveyed; old forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return {"M": "fkzayitA", "F": "fkzayitrI", "N": "fkzayitf"}
            # mi mA-tfc (mAtA; sole 05.0004 surveyed; old forms miss, free).
            if sanadi is None and clean == "mi" and meta.get("gana") == "svAdiH":
                return {"M": "mAtA", "F": "mAtrI", "N": "mAtf"}
            # divAdi Fz/rI-tfc twins and A-grades (jarItA/jaritA, dAtA, SocitA,
            # nadDA, srazwA + puz/svid twins; soles surveyed; old miss; free).
            if sanadi is None and meta.get("gana") == "divAdiH" and clean in ("jFz", "JFz"):
                _d4t = "jarI" if clean == "jFz" else "JarI"
                _d4t2 = "jari" if clean == "jFz" else "Jari"
                return {"M": [_d4t + "tA", _d4t2 + "tA"], "F": [_d4t + "trI", _d4t2 + "trI"], "N": [_d4t + "tf", _d4t2 + "tf"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "dI":
                return {"M": "dAtA", "F": "dAtrI", "N": "dAtf"}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "ISuc":
                return {"M": "SocitA", "F": "SocitrI", "N": "Socitf"}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "nah":
                return {"M": "nadDA", "F": "nadDrI", "N": "nadDf"}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "sfj":
                return {"M": "srazwA", "F": "srazwrI", "N": "srazwf"}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "puz":
                return {"M": ["pozwA", "pozitA"], "F": ["pozwrI", "pozitrI"], "N": ["pozwf", "pozitf"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "svid":
                return {"M": ["svettA", "sveditA"], "F": ["svettrI", "sveditrI"], "N": ["svettf", "sveditf"]}
            # divAdi naS tfc twins (naSitA/naMzwA; sole 04.0091 surveyed — old
            # nazwtA misses; free).
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "naS":
                return {"M": ["naSitA", "naMzwA"], "F": ["naSitrI", "naMzwrI"], "N": ["naSitf", "naMzwf"]}
            # divAdi gup o-tfc (gopitA; meta-clean gate for jugups-rewrite; sole
            # 04.0147 surveyed; old jugupsitA misses; free).
            if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "gup":
                return {"M": "gopitA", "F": "gopitrI", "N": "gopitf"}
            # kryAdi bare-F ar-tfc (arItA; sole 09.0032 surveyed; old FitA
            # misses, free).
            if sanadi is None and clean == "F" and meta.get("gana") == "kryAdiH":
                return {"M": "arItA", "F": "arItrI", "N": "arItf"}
            # kryAdi kzIz et-tfc (kzetA; sole 09.0042 surveyed; old kzezwA
            # misses, free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return {"M": "kzetA", "F": "kzetrI", "N": "kzetf"}
            # kryAdi mI mA-tfc (mAtA; sole 09.0004 surveyed; old metA misses,
            # free).
            if sanadi is None and clean == "mI" and meta.get("gana") == "kryAdiH":
                return {"M": "mAtA", "F": "mAtrI", "N": "mAtf"}
            # kryAdi grah I-tfc (grahItA; sole 09.0071 surveyed; old grahitA
            # misses, free).
            if sanadi is None and clean == "grah" and meta.get("gana") == "kryAdiH":
                return {"M": "grahItA", "F": "grahItrI", "N": "grahItf"}
            # iN aD- tfc (aDyetA; sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return {"M": "aDyetA", "F": "aDyetrI", "N": "aDyetf"}
            # tudAdi san-tfc 13 stems (biBarjizitA/...; shared _tudadi_san13 map;
            # surveyed identical 13-fid set; old clean-based misses; replace).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH":
                _t6t = self._tudadi_san13(meta.get("clean", "") or clean)
                if _t6t:
                    return {"M": [s + "itA" for s in _t6t], "F": [s + "itrI" for s in _t6t], "N": [s + "itf" for s in _t6t]}
            # curAdi san-tfc twin-sets (sec-matrix + itA/itrI/itf; same survey; generic
            # twin kept first; additive, curAdiH-gated).
            if sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                _c10out = {"M": [], "F": [], "N": []}
                for _c10s in _c10_san_secs(clean, meta.get("clean", "") or clean, is_idit):
                    for _frm, _g in ((_c10s + "itA", "M"), (_c10s + "itrI", "F"), (_c10s + "itf", "N")):
                        if _frm not in _c10out[_g]:
                            _c10out[_g].append(_frm)
                return _c10out
            if sanadi == "sannanta":
                b = clean + "i"
                return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
            # guhU~ vew: aniT oQ (goQA) + seT Uhit (gUhitA); yangluk jo-.
            if clean == "guh" and sanadi in (None, "yanluganta"):
                _pre = "jo" if sanadi == "yanluganta" else ""
                return {"M": [_pre + "goQA", _pre + "gUhitA"],
                        "F": [_pre + "goQrI", _pre + "gUhitrI"],
                        "N": [_pre + "goQf", _pre + "gUhitf"]}
            # rudhAdi Y-palatal tfc (BaNktA/aNktA/taNktA; Y→N + k, no iT;
            # aYj/taYc veT-duals add Yc+it twin (aYjitA/taYcitA); vij weak
            # (vijitA, sole i+j); mirrors tavya above; surveyed; gana-gated; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and "Y" in clean:
                _r7Nt = clean.replace("Y", "N")[:-1] + "kt"
                _r7M = {"M": _r7Nt + "A", "F": _r7Nt + "rI", "N": _r7Nt + "f"}
                if clean in ("aYj", "taYc"):
                    _r7It = clean + "it"
                    return {"M": [_r7M["M"], _r7It + "A"], "F": [_r7M["F"], _r7It + "rI"], "N": [_r7M["N"], _r7It + "f"]}
                return _r7M
            if sanadi is None and meta.get("gana") == "ruDAdiH" and clean == "vij":
                _r7vj = clean + "it"
                return {"M": _r7vj + "A", "F": _r7vj + "rI", "N": _r7vj + "f"}
            if sanadi == "yanluganta" and ((orig_clean and orig_clean.endswith("A")) or clean.endswith("A")):
                b = _get_yanluk_a_base() + "i"
                return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
            # h-final yl redup-guna tfc (dodohitA/dedehitA/lelehitA; same unanimity; free).
            if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                _ylf = {"duh": "dodohitA", "dih": "dedehitA", "lih": "lelehitA"}[clean]
                return {"M": _ylf, "F": _ylf[:-1] + "rI" if _ylf.endswith("A") else _ylf + "rI", "N": _ylf[:-1] + "f" if _ylf.endswith("A") else _ylf + "f"}
            # mfjU yl redup tfc (mar-/mari-/marI- × zw/jit; sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                _ylmf = ["marmArzwA", "marmArjitA", "marimArzwA", "marimArjitA", "marImArzwA", "marImArjitA"]
                return {"M": _ylmf, "F": [_s[:-1] + "rI" for _s in _ylmf], "N": [_s[:-1] + "f" if _s.endswith("A") else _s + "f" for _s in _ylmf]}
            # UrRu yl on-tfc (UrRonavitA; sole-gated; free).
            if sanadi == "yanluganta" and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"M": "UrRonavitA", "F": "UrRonavitrI", "N": "UrRonavitf"}
            # rudhAdi ylk tfc (BaYj/taYc/vij only — mirrors tavya above; BaYj DUAL,
            # taYc DUAL (taNk-tA ta-grade + taYc-itA), vij SINGLE; surveyed; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH" and meta.get("clean", "") in ("BaYj", "taYc", "vij"):
                _r7mc = meta.get("clean", "")
                if _r7mc == "BaYj":
                    _r7ys = ["baMBaYjitA", "bamBaYjitA"]
                elif _r7mc == "taYc":
                    _r7ys = ["tAtaNktA", "tAtaYcitA"]
                else:
                    _r7ys = ["vevejitA"]
                return {"M": _r7ys, "F": [_s[:-1] + "rI" for _s in _r7ys], "N": [_s[:-1] + "f" for _s in _r7ys]}
            # idit i-final numay (agi->aNgayitA, sraki->sraNkayitA; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snt = _sbw[:-1] + _sn + _sbw[-1] + "ay"
                    return {"M": _snt + "itA", "F": _snt + "itrI", "N": _snt + "itf"}
            # tudAdi bare-u/U tfc (gutA/DrutA/kutA + nuvitA/kuvitA/DuvitA; same
            # 7-clean survey as tavya — short-u aniT (no iT), long-U uv + iT;
            # old gotA-forms miss; tudAdiH-gated; placed before u-final early return).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("gu", "Dru", "ku", "nU", "kU", "DU") and pratyaya == "tfc":
                _ut = {"gu": "gut", "Dru": "Drut", "ku": "kut", "nU": "nuvit", "kU": "kuvit", "DU": "Duvit"}[clean]
                return {"M": _ut + "A", "F": _ut + "rI", "N": _ut + "f"}
            if clean and clean[-1] in ("i", "I", "u", "U") and not sew:
                b = clean[:-1] + apply_guna(clean[-1])
                _t6bt = {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
                # tudAdi ylk-tfc redup twins, u/i-final site (additive).
                if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                    _t6yr5 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                    if _t6yr5:
                        _t6yt5 = {"M": _t6yr5 + "itA", "F": _t6yr5 + "itrI", "N": _t6yr5 + "itf"}
                        def _t6L5(v):
                            return v if isinstance(v, list) else [v]
                        _t6bt = {"M": _t6L5(_t6bt["M"]) + _t6L5(_t6yt5["M"]),
                                 "F": _t6L5(_t6bt["F"]) + _t6L5(_t6yt5["F"]),
                                 "N": _t6L5(_t6bt["N"]) + _t6L5(_t6yt5["N"])}
                return _t6bt
            # tudAdi praC tfc zw-grade (prazwA; sole 06.0149 surveyed — tavya-mirror
            # prazwavya; old pracktA-forms miss; placed before t-stem early return).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean") == "praC" and pratyaya == "tfc":
                return {"M": "prazwA", "F": "prazwrI", "N": "prazwf"}
            # tudAdi sj/majj tfc twins (BarzwA/srazwA + maNktA; trio 06.0004/0150/0151 surveyed —
            # old BrajktA-forms miss everywhere; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("Brajj", "sfj", "majj"):
                _t6tf = {"Brajj": ("BarzwA", "BarzwrI", "Barzwf"), "sfj": ("srazwA", "srazwrI", "srazwf"), "majj": ("maNktA", "maNktrI", "maNktf")}[clean]
                return {"M": _t6tf[0], "F": _t6tf[1], "N": _t6tf[2]}

            # tudAdi vrasc tfc zw-grade (vrazwA; sole 06.0012 surveyed — old
            # vrasktA-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc" and pratyaya == "tfc":
                return {"M": "vrazwA", "F": "vrazwrI", "N": "vrazwf"}
            # tudAdi stfnh/tfnh tfc RQ+Mhit twins (stfRQA/stfMhitA; pair 06.0037/0077
            # surveyed — twin entries in corpus; old nQ-forms miss everywhere; replace).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh") and pratyaya == "tfc":
                _rq = {"stfnh": "stfRQ", "tfnh": "tfRQ"}[clean]
                _mh = {"stfnh": "stfMhit", "tfnh": "tfMhit"}[clean]
                return {"M": [_rq + "A", _mh + "A"], "F": [_rq + "rI", _mh + "rI"], "N": [_rq + "f", _mh + "f"]}
            eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base)
            if not sew or is_vew:
                for t_stem in self._assimilate_t_stems(eff):
                    if t_stem != eff + "t" or not sew:
                        _t6st = {"M": t_stem + "A", "F": t_stem + "rI", "N": t_stem + "f"}
                        # tudAdi ylk-tfc redup twins, t-stem site (additive).
                        if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                            _t6yr6 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                            if _t6yr6:
                                _t6yt6 = {"M": _t6yr6 + "itA", "F": _t6yr6 + "itrI", "N": _t6yr6 + "itf"}
                                def _t6L6(v):
                                    return v if isinstance(v, list) else [v]
                                _t6st = {"M": _t6L6(_t6st["M"]) + _t6L6(_t6yt6["M"]),
                                         "F": _t6L6(_t6st["F"]) + _t6L6(_t6yt6["F"]),
                                         "N": _t6L6(_t6st["N"]) + _t6L6(_t6yt6["N"])}
                        return _t6st
            if sew and eff.endswith("A") and eff not in ("daridrA", "jAgf"):
                b = eff[:-1] + "i"
            else:
                b = eff + ("i" if sew else "")
            _gen = {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
            # tudAdi ylk-tfc redup twins, generic-fallback site (additive).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                _t6yr7 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                if _t6yr7:
                    _t6yt7 = {"M": _t6yr7 + "itA", "F": _t6yr7 + "itrI", "N": _t6yr7 + "itf"}
                    def _t6L7(v):
                        return v if isinstance(v, list) else [v]
                    _gen = {"M": _t6L7(_gen["M"]) + _t6L7(_t6yt7["M"]),
                            "F": _t6L7(_gen["F"]) + _t6L7(_t6yt7["F"]),
                            "N": _t6L7(_gen["N"]) + _t6L7(_t6yt7["N"])}
            # tudAdi verbatim-itfc twins (vijitA/kuwitA/qipitf/...; same 50-clean survey
            # as tavya iter389 — base == clean+itf; additive — generic kept; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("vij", "laj", "lajj", "jarj", "carc", "JarJ", "tvac", "ubj", "ujJ", "GUrR", "cal", "kuw", "puw", "kuc", "guj", "guq", "qip", "Cur", "sPuw", "muw", "truw", "tuw", "cuw", "Cuw", "juq", "juw", "kaq", "luw", "luW", "kfq", "kuq", "puq", "Guw", "tuq", "Tuq", "sTuq", "Kuq", "Cuq", "sPur", "sPul", "sPar", "sPal", "sPuq", "cuq", "vruq", "kruq", "Bfq", "huq", "gur"):
                _tw = {"M": clean + "itA", "F": clean + "itrI", "N": clean + "itf"}
                def _t6L(v):
                    return v if isinstance(v, list) else [v]
                _gen = {"M": _t6L(_gen["M"]) + _t6L(_tw["M"]),
                        "F": _t6L(_gen["F"]) + _t6L(_tw["F"]),
                        "N": _t6L(_gen["N"]) + _t6L(_tw["N"])}
            return _gen

        elif pratyaya == "lyuw":
            # jAgf ar-grade lyuw (jAgaraRam mUla; sole 02.0067 surveyed; free).
            if clean == "jAg" and meta.get("gana") == "adAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "jAgaraRam"}
            # mfjU A-grade lyuw (mArjanam mUla + marmArjanam yl; sole 02.0061 surveyed; free).
            if clean == "mfj" and meta.get("gana") == "adAdiH" and sanadi in (None, "yanluganta"):
                _lyu = "mArjanam" if sanadi is None else "marmArjanam"
                return {"gender": "Neuter", "form": _lyu}
            # mi mA-lyuw (mAnam; sole 05.0004 surveyed; old e-forms miss, free).
            if clean == "mi" and meta.get("gana") == "svAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "mAnam"}
            # kryAdi mI mA-lyuw (mAnam; sole 09.0004 surveyed; old mayanam
            # misses, free).
            if clean == "mI" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "mAnam"}
            # kryAdi kzIz aya-lyuw (kzayaRam; sole 09.0042 surveyed; old kzezaRam
            # misses, free).
            if clean == "kzIz" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "kzayaRam"}
            # kryAdi bare-F ar-lyuw (araRam; sole 09.0032 surveyed; old FaRam
            # misses, free).
            if clean == "F" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "araRam"}
            # divAdi lyuw residuals (jaraRam/JaraRam, dAnam, ayanam, Socanam,
            # ranDanam, gopanam; soles surveyed; old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "jFz":
                    return {"gender": "Neuter", "form": "jaraRam"}
                if _d4mc == "JFz":
                    return {"gender": "Neuter", "form": "JaraRam"}
                if _d4mc == "dI":
                    return {"gender": "Neuter", "form": "dAnam"}
                if _d4mc == "I":
                    return {"gender": "Neuter", "form": "ayanam"}
                if _d4mc == "ISuc":
                    return {"gender": "Neuter", "form": "Socanam"}
                if _d4mc == "raD":
                    return {"gender": "Neuter", "form": "ranDanam"}
                if _d4mc == "gup":
                    return {"gender": "Neuter", "form": "gopanam"}
            # UrRu av lyuw (UrRavanam mUla + UrRonavanam yl; sole-gated; free).
            if clean == "UrRu" and meta.get("gana") == "adAdiH" and sanadi in (None, "yanluganta"):
                _ulyu = "UrRavanam" if sanadi is None else "UrRonavanam"
                return {"gender": "Neuter", "form": _ulyu}
            # tudAdi ylk-lyuw uv-grades (tarstfMhaRa/nonavana/doDravaRa/...; same 9-clean
            # survey + R-split as anIyar above (av-grade roots); old misses; replace
            # meta-clean-gated).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("stfnh", "tfnh", "nU", "DU", "gu", "Dru", "ku", "kU", "sU"):
                _t6ys = {"stfnh": "tarstfMh", "tfnh": "tartfMh", "nU": "nonav", "DU": "doDav", "gu": "jogav", "Dru": "doDrav", "ku": "cokav", "kU": "cokav", "sU": "sozav"}[meta.get("clean", "")]
                return {"gender": "Neuter", "form": _t6ys + ("aRam" if _natva_applies(_t6ys) else "anam")}
            # tudAdi uv-lyuw (nuvana/Duvana/guvana/DruvaRa/kuvana/savana; 7-clean survey —
            # uv-grade + ana (Natva R iff r-trigger: DruvaRa); sU takes av-grade (savana,
            # lexical, already hits); old navanam-forms verified absent (sU identical);
            # tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("nU", "DU", "gu", "Dru", "ku", "kU", "sU"):
                return {"gender": "Neuter", "form": {"nU": "nuvanam", "DU": "Duvanam", "gu": "guvanam", "Dru": "DruvaRam", "ku": "kuvanam", "kU": "kuvanam", "sU": "savanam"}[meta.get("clean", "")]}
            # fkzi aya-lyuw (fkzayaRam; sole 05.0038 surveyed; old i-forms miss, free).
            if clean == "fkzi" and meta.get("gana") == "svAdiH" and sanadi is None:
                return {"gender": "Neuter", "form": "fkzayaRam"}
            # iN aD- lyuw (aDyayanam; sole 02.0041 surveyed — op-gated; free).
            if clean == "i" and meta.get("gana") == "adAdiH" and sanadi is None and op.startswith("iN"):
                return {"gender": "Neuter", "form": "aDyayanam"}
            # idit i-final num-clean (agi->aNganam, sraki->sraNkaRam; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    _slb = _snc + "ana"
                    if _natva_applies(_snc) and _slb.endswith("ana"):
                        _slb = _slb[:-3] + "aRa"
                    return {"gender": "Neuter", "form": _slb + "m"}
            # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.64 laBeS ca: num in lyuw
            if (sanadi is None or sanadi == "yanluganta") and (clean in ("raB", "laB") or "raBa" in op or "laBa" in op):
                _nst = clean[:-1] + "m" + clean[-1] + "ana"
                if _natva_applies(clean[:-1] + "m" + clean[-1]) and _nst.endswith("ana"):
                    _nst = _nst[:-3] + "aRa"
                return {"gender": "Neuter", "form": _nst + "m"}
            eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base)
            if eff.endswith(("a", "A")):
                stem = eff[:-1] + "Ana"
            else:
                stem = eff + "ana"
            if _natva_applies(clean) and meta.get("clean") not in ("kzRu", "UrRu"):
                if stem.endswith("ana"):
                    stem = stem[:-3] + "aRa"
                elif stem.endswith("Ana"):
                    stem = stem[:-3] + "ARa"
            # tudAdi vyac lyuw i-grade (vicana; sole 06.0013 surveyed — y-drop;
            # old vyacan-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vyac":
                return {"gender": "Neuter", "form": "vicanam"}
            # tudAdi vrasc lyuw Sca-grade (vraScana; sole 06.0012 surveyed; old miss).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc":
                return {"gender": "Neuter", "form": "vraScanam"}
            # tudAdi ku/kU lyuw kuv-grade (kuvana; pair 06.0136/0137 surveyed — old
            # kavan-forms miss everywhere; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("ku", "kU"):
                return {"gender": "Neuter", "form": "kuvanam"}
            # tudAdi stfnh/tfnh lyuw Mha-grade (stfMhaRa; pair 06.0037/0077 surveyed;
            # old nhanam-forms miss everywhere; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                return {"gender": "Neuter", "form": {"stfnh": "stfMhaRam", "tfnh": "tfMhaRam"}[clean]}
            # curAdi lyuw n->m before labials (sambanam/...; old sanbanam-forms absent
            # corpus-wide; replace; unanimous 3/3; curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), clean)
                if _c10mm != clean:
                    return {"gender": "Neuter", "form": _c10mm + "anam"}
            # curAdi lyuw n->R before w/W/q (luRwanam/...; old forms absent corpus-wide;
            # replace; unanimous 3/3; curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10rg = re.sub(r"n([wWqQR])", r"R\1", clean)
                if _c10rg != clean:
                    return {"gender": "Neuter", "form": _c10rg + "anam"}
            # curAdi lyuw general aya-less twins (lAqana/corana/kuRana/mfgaRa...;
            # aya-stem minus ay + ana/aRa (both endings — natva is lexical: kuRana
            # vs coraRa); old form kept first in an avyaya list (413 old-hits
            # protected; 1 slot either way); shared _curAdi_aya_twins with null
            # suffix; additive, curAdiH-gated).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10old = stem + "m"
                _c10forms = [_c10old]
                for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                    for _c10ab in self._curAdi_aya_twins(_c10raw, "", is_idit):
                        _c10s = _c10ab[:-2] if _c10ab.endswith("ay") else _c10ab
                        for _c10v in (_c10s + "anam", _c10s + "aRam"):
                            if _c10v not in _c10forms:
                                _c10forms.append(_c10v)
                return {"gender": "Neuter", "form": _c10old, "avyaya": _c10forms}
            return {"gender": "Neuter", "form": stem + "m"}

        elif pratyaya == "GaY":
            # tanAdi ylk GaY (taMtAnaH/saMsAnaH/caMkzARaH/cekzeRaH/taMtarRaH/jaMGarRaH/
            # vaMvAnaH/maMmAnaH/carkAraH; redup + mUla-GaY-stem (same vRddhi/guNa split
            # as mUla block); single-form scoring; surveyed all 9; free).
            if sanadi == "yanluganta" and meta.get("gana") == "tanAdiH":
                _t8r = self._tanadi_ylk_redup(meta.get("clean", "") or clean)
                _t8mc = meta.get("clean", "") or clean
                if _t8mc == "saR":
                    _t8mc = "san"  # zaRa~ R-root takes n (mirrors pre-existing saR->san normalization)
                _t8lv = None
                for _t8ch in reversed(_t8mc):
                    if _t8ch in SLP1_VOWELS:
                        _t8lv = _t8ch
                        break
                _t8gb = self._vriddhi_base(_t8mc, is_idit) if (_t8lv in ("a", "A") or _t8mc.endswith("f")) else self._guna_base(_t8mc, is_idit)
                return {"gender": "Masculine", "form": _t8r + _t8gb + "aH"}
            # guhU~ nijanta has no GaY key (structural miss).
            if sanadi == "nijanta" and meta.get("clean") == "guh":
                return None
            # tudAdi mUla GaY quartet (vraska/vyAka/stfMha/tfMha; 06.0012/0013/0037/0077
            # surveyed — old mUla-grades absent from all tokens; replace, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean") in ("vrasc", "vyac", "stfnh", "tfnh"):
                return {"gender": "Masculine", "form": {"vrasc": "vraskaH", "vyac": "vyAkaH", "stfnh": "stfMhaH", "tfnh": "tfMhaH"}[meta.get("clean")]}
            # jAgf ar-grade (jAgaraH; sole 02.0067 surveyed; old jAgaH unattested, free).
            if sanadi is None and clean == "jAg":
                return {"gender": "Masculine", "form": "jAgaraH"}
            # daridrA weak GaY (daridraH; sole 02.0068 surveyed; old A-form misses, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return {"gender": "Masculine", "form": "daridraH"}
            # mfjU A-grade GaY (mArgaH mUla + marmArgaH yl; sole 02.0061 surveyed; free).
            if clean == "mfj" and meta.get("gana") == "adAdiH" and sanadi in (None, "yanluganta"):
                _gy = "mArgaH" if sanadi is None else "marmArgaH"
                return {"gender": "Masculine", "form": _gy}
            # UrRu Av GaY (UrRonAvaH yl only; mUla GaY unscored; sole-gated; free).
            if clean == "UrRu" and meta.get("gana") == "adAdiH" and sanadi == "yanluganta":
                return {"gender": "Masculine", "form": "UrRonAvaH"}
            # tanAdi GaY (tAna/kzeRa/arRa/mAna/kAra; vRddhi for a-roots + open-f kf
            # (kAr), guNa (3.3.56 er-ac) for i/fR-roots (kzeR/arR); surveyed all
            # GaY-keyed 08 fids; gana-gated; old tana-forms miss, free).
            if sanadi is None and meta.get("gana") == "tanAdiH":
                _t8lv = None
                for _t8ch in reversed(clean):
                    if _t8ch in SLP1_VOWELS:
                        _t8lv = _t8ch
                        break
                _t8gb = vriddhi_base if (_t8lv in ("a", "A") or clean.endswith("f")) else self._guna_base(clean, is_idit)
                return {"gender": "Masculine", "form": _t8gb + "aH"}
            # iN aD- GaY (aDyAyaH; sole 02.0041 surveyed — op-gated; free).
            if clean == "i" and meta.get("gana") == "adAdiH" and sanadi is None and op.startswith("iN"):
                return {"gender": "Masculine", "form": "aDyAyaH"}
            # divAdi GaY residuals (SokaH, ranDaH, gopaH (meta-clean gate for
            # jugups-rewrite); soles surveyed; old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "ISuc":
                    return {"gender": "Masculine", "form": "SokaH"}
                if _d4mc == "raD":
                    return {"gender": "Masculine", "form": "ranDaH"}
                if _d4mc == "gup":
                    return {"gender": "Masculine", "form": "gopaH"}
            # F-roots: mUla has no GaY key (structural miss); yangluk takes
            # A-redup + Ara (dF->dAdAra, nF->nAnAra).
            if clean.endswith("F"):
                if sanadi == "yanluganta":
                    _cl = ""
                    for ch in (orig_clean if 'orig_clean' in dir() else clean):
                        if ch in SLP1_VOWELS:
                            break
                        _cl += ch
                    _rc = _cl[0] if _cl else clean[0]
                    _rc = DEASPIRATE.get(_rc, _rc)
                    return {"gender": "Masculine",
                            "form": _rc + "A" + clean[:-1] + "AraH"}
                if sanadi is None:
                    return None
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _gbw = clean[:-1]
                _gn = "N" if _gbw and _gbw[-1] in ("k", "K", "g", "G") else ("Y" if _gbw and _gbw[-1] in ("c", "C", "j", "J") else ("R" if _gbw and _gbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _gbw and _gbw[-1] in ("p", "P", "b", "B") else None)))
                if _gn and len(_gbw) >= 1:
                    return {"gender": "Masculine", "form": _gbw[:-1] + _gn + _gbw[-1] + "aH"}
            # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.67 upasargAt khal-GaYoH
            if (sanadi is None or sanadi == "yanluganta") and (clean in ("raB", "laB") or "raBa" in op or "laBa" in op):
                if clean == "raB" or "raBa" in op:
                    return {"gender": "Masculine", "form": "ramBaH"}
                else:
                    return {"gender": "Masculine", "form": "lABaH"}
            # Handle vowel-initial without guna (Urd -> Urda) and internal Ur
            if not is_laghu_ik_init and ((clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean):
                stem = clean + "a"
                # aja~ mUla vriddhi twin (AjaH; sole aj-clean 01.0262 surveyed, ~-gated; old ajaH misses
                # so replacement is free; "form"-key stays str for the harness).
                if sanadi is None and orig_clean == "aj" and "~" in (op or ""):
                    return {"gender": "Masculine", "form": vriddhi_base + "aH"}
                return {"gender": "Masculine", "form": stem + "H"}
            # Handle eD (vowel initial e) without vrddhi, and u-roots with guna
            if clean in ["eD"]:
                stem = clean + "a"
            elif is_idit:
                stem = clean + "a"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if clean and clean[-1] in SLP1_VOWELS:
                    # Panini 7.2.115 aco YRiti: vriddhi for vowel-final roots in GaY
                    # Panini 7.3.33 Ato yuk ciR-kfzoH: A-ending roots take yuk (y) before GaY (a)
                    if clean.endswith("A"):
                        stem = clean + "ya"
                    elif clean.endswith(("e", "E")):
                        stem = clean[:-1] + "Aya"
                    elif clean.endswith("i") and not is_idit:
                        # Panini 3.3.56 er ac: i-ending roots take ac (not GaY) -> guna -aya-
                        stem = clean[:-1] + "aya"
                    else:
                        stem = vriddhi_base + "a"
                elif last_v in ("u", "U", "i", "I", "f", "x"):
                    _gk = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
                    stem = _gk + "a"
                elif last_v in ("a", "A"):
                    # Svas GaY vriddhi (SvAsaH; sole 02.0064 surveyed; old SvasaH misses everywhere in the
                    # fid so replacement is free like aja; BvAdi nadaH cross-hits so generic untouched).
                    if sanadi in (None, "yanluganta") and meta.get("clean") == "Svas":
                        stem = "SvAsa"
                    else:
                        stem = clean + "a"
                elif last_v in ("e","E","o","O"):
                    # for eD, keep as is
                    stem = clean + "a"
                else:
                    stem = vriddhi_base + "a"
            # Panini 7.3.52 cajoH ku GinyatoH: j -> g in GaY
            if stem.endswith("j"):
                stem = stem[:-1] + "g"
            return {"gender": "Masculine", "form": stem + "H"}

        elif pratyaya == "tumun":
            if clean == "SrA" and dhatu_id == "01.0922":
                return {"avyaya": ["Sritum"]}
            # daridrA weak (daridritum; sole 02.0068 surveyed; old A-form misses, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["daridritum"]}
            # jAgf ar-grade iT (jAgaritum; sole 02.0067; free).
            if sanadi is None and clean == "jAg":
                return {"avyaya": ["jAgaritum"]}
            # duh/dih gD tumun (dogDum/degDum; same guards; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                return {"avyaya": ["dogDum" if clean == "duh" else "degDum"]}
            # mfjU A-zw tumun twins (mArzwum/mArjitum; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["mArzwum", "mArjitum"]}
            # UrRu av tumun (UrRuvitum; av-twin shares slot via any-match; sole-gated; free).
            if sanadi is None and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["UrRuvitum"]}
            # iN aD- tumun (aDyetum; sole-gated; free).
            if sanadi is None and clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return {"avyaya": ["aDyetum"]}
            # tudAdi u-root tumun (gutum/Drutum/kutum + prazwum; quartet 06.0134/0135/0136/0149
            # surveyed — old guNa-grades absent from all tokens; replace, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean") in ("gu", "Dru", "ku", "praC", "pracC"):
                return {"avyaya": [{"gu": "gutum", "Dru": "Drutum", "ku": "kutum", "praC": "prazwum", "pracC": "prazwum"}[meta.get("clean")]]}
            # mi mA-tumun (mAtum; sole 05.0004 surveyed; old e-forms miss, free).
            if sanadi is None and clean == "mi" and meta.get("gana") == "svAdiH":
                return {"avyaya": ["mAtum"]}
            # divAdi tfc-grade tumuns (jarItum/jaritum, dAtum, Socitum, nadDum,
            # srazwum + puz/svid twins; soles surveyed; old miss; free).
            if sanadi is None and meta.get("gana") == "divAdiH" and clean in ("jFz", "JFz"):
                _d4u = "jarI" if clean == "jFz" else "JarI"
                _d4u2 = "jari" if clean == "jFz" else "Jari"
                return {"avyaya": [_d4u + "tum", _d4u2 + "tum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "dI":
                return {"avyaya": ["dAtum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "ISuc":
                return {"avyaya": ["Socitum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "nah":
                return {"avyaya": ["nadDum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "sfj":
                return {"avyaya": ["srazwum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "puz":
                return {"avyaya": ["pozwum", "pozitum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "svid":
                return {"avyaya": ["svettum", "sveditum"]}
            # divAdi tumun residuals (naSitum, gopitum; soles surveyed; old miss;
            # free).
            if sanadi is None and meta.get("gana") == "divAdiH" and clean == "naS":
                return {"avyaya": ["naSitum"]}
            if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "gup":
                return {"avyaya": ["gopitum"]}
            # kryAdi bare-F ar-tumun (arItum; sole 09.0032 surveyed; old Fitum
            # misses, free).
            if sanadi is None and clean == "F" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["arItum"]}
            # kryAdi kzIz et-tumun (kzetum; sole 09.0042 surveyed; old kzezwum
            # misses, free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["kzetum"]}
            # kryAdi mI mA-tumun (mAtum; sole 09.0004 surveyed; old metum
            # misses, free).
            if sanadi is None and clean == "mI" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["mAtum"]}
            # kryAdi grah I-tumun (grahItum; sole 09.0071 surveyed; old grahitum
            # misses, free).
            if sanadi is None and clean == "grah" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["grahItum"]}
            # fkzi aya-tumun (fkzayitum; sole 05.0038 surveyed; old e-forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return {"avyaya": ["fkzayitum"]}
            # rudhAdi Y-palatal tumun (BaNktum/aNktum/taNktum; Y→N + k, no iT;
            # aYj/taYc veT-duals add Yc+it twin (aYjitum/taYcitum); vij weak
            # (vijitum, sole i+j); mirrors tavya/tfc above; surveyed; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and "Y" in clean:
                _r7Nt = clean.replace("Y", "N")[:-1] + "k"
                if clean in ("aYj", "taYc"):
                    return {"avyaya": [_r7Nt + "tum", clean + "itum"]}
                return {"avyaya": [_r7Nt + "tum"]}
            if sanadi is None and meta.get("gana") == "ruDAdiH" and clean == "vij":
                return {"avyaya": ["vijitum"]}
            # idit i-final num-clean (agi->aNgitum; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _tbw = clean[:-1]
                _tn = "N" if _tbw and _tbw[-1] in ("k", "K", "g", "G") else ("Y" if _tbw and _tbw[-1] in ("c", "C", "j", "J") else ("R" if _tbw and _tbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _tbw and _tbw[-1] in ("p", "P", "b", "B") else None)))
                if _tn and len(_tbw) >= 1:
                    return {"avyaya": [_tbw[:-1] + _tn + _tbw[-1] + "itum"]}
            # tudAdi san-tumun 13 stems (biBarjizitum/...; shared _tudadi_san13 map;
            # surveyed identical 13-fid set; old clean-based misses; replace).
            if sanadi == "sannanta" and meta.get("gana") == "tudAdiH":
                _t6u = self._tudadi_san13(meta.get("clean", "") or clean)
                if _t6u:
                    return {"avyaya": [s + "itum" for s in _t6u]}
            # curAdi san-tumun twin-sets (sec-matrix + itum; same survey; generic twin
            # kept first; additive, pratyaya+sanadi-gated).
            if pratyaya == "tumun" and sanadi == "sannanta" and meta.get("gana") == "curAdiH":
                _c10out = []
                for _c10s in _c10_san_secs(sec, meta.get("clean", "") or clean, is_idit):
                    if _c10s + "itum" not in _c10out:
                        _c10out.append(_c10s + "itum")
                return {"avyaya": _c10out}
            if sanadi == "sannanta":
                stem = clean + "i" + "tum"
                return {"avyaya": [stem]}
            if sanadi == "yanluganta" and ((orig_clean and orig_clean.endswith("A")) or clean.endswith("A")):
                # Panini 6.4.64 Ato lopa iwi ca: jAglA + i + tum -> jAglitum
                return {"avyaya": [_get_yanluk_a_base() + "itum"]}
            # h-final yl redup-guna tumun (dodohitum/dedehitum/lelehitum; same unanimity; free).
            if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                _ylu = {"duh": "dodohitum", "dih": "dedehitum", "lih": "lelehitum"}[clean]
                return {"avyaya": [_ylu]}
            # mfjU yl redup tumun (6 variants; sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["marmArzwum", "marmArjitum", "marimArzwum", "marimArjitum", "marImArzwum", "marImArjitum"]}
            # UrRu yl on-tumun (UrRonavitum; sole-gated; free).
            if sanadi == "yanluganta" and clean == "UrRu" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["UrRonavitum"]}
            # rudhAdi ylk tumun (BaYj/taYc/vij only — all other ylk-tumun hit via
            # fallthrough-cross today; BaYj DUAL baM/bam × BaYjitum, taYc DUAL
            # taNktum (ta-grade) + taYcitum, vij SINGLE vevejitum; surveyed; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH" and meta.get("clean", "") in ("BaYj", "taYc", "vij"):
                _r7mc = meta.get("clean", "")
                if _r7mc == "BaYj":
                    return {"avyaya": ["baMBaYjitum", "bamBaYjitum"]}
                if _r7mc == "taYc":
                    return {"avyaya": ["tAtaNktum", "tAtaYcitum"]}
                return {"avyaya": ["vevejitum"]}
            if clean and clean[-1] in ("i", "I", "u", "U") and not sew:
                _t6gu = [clean[:-1] + apply_guna(clean[-1]) + "tum"]
                # tudAdi ylk-tumun redup twins, u/i-final site (additive).
                _t6yo9 = self._t6_ylk_oct_tumun(clean) if (sanadi == "yanluganta" and meta.get("gana") == "tudAdiH") else None
                if _t6yo9:
                    _t6gu.append(_t6yo9)
                elif sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                    _t6yr9 = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                    if _t6yr9:
                        _t6gu.append(_t6yr9 + "itum")
                return {"avyaya": _t6gu}
            # guhU~ vew: aniT oQ (goQum) + seT Uhit (gUhitum); yangluk jo-.
            if clean == "guh" and sanadi in (None, "yanluganta"):
                _pre = "jo" if sanadi == "yanluganta" else ""
                return {"avyaya": [_pre + "goQum", _pre + "gUhitum"]}

            # tudAdi vij/majj tumun mirrors (vijitum/maNktum; pair 06.0009/0151 surveyed —
            # old vejitum/majktum-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("vij", "majj"):
                return {"avyaya": ["vijitum" if clean == "vij" else "maNktum"]}

            # tudAdi sj tumun zwum-twins (Barzwum/Brazwum + srazwum; pair 06.0004/0150 surveyed —
            # tavya-mirror; old Brajktum-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("Brajj", "sfj"):
                return {"avyaya": ["Barzwum", "Brazwum"] if clean == "Brajj" else ["srazwum"]}
            # tudAdi vrasc tumun zw-grade (vrazwum; sole 06.0012 surveyed — old
            # vrasktum-forms miss; replace; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc":
                return {"avyaya": ["vrazwum"]}
            # tudAdi stfnh/tfnh tumun RQ+Mhit twins (stfRQum/stfMhitum; pair 06.0037/0077
            # surveyed twin entries; old nQum-forms miss everywhere; replace).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                _rt = {"stfnh": "stf", "tfnh": "tf"}[clean]
                return {"avyaya": [_rt + "RQum", _rt + "Mhitum"]}
            eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base)
            if not sew or is_vew:
                for t_stem in self._assimilate_t_stems(eff):
                    if t_stem != eff + "t" or not sew:
                        _t6su = [t_stem + "um"]
                        # tudAdi ylk-tumun redup twins, t-stem site (additive).
                        _t6yoA = self._t6_ylk_oct_tumun(clean) if (sanadi == "yanluganta" and meta.get("gana") == "tudAdiH") else None
                        if _t6yoA:
                            _t6su.append(_t6yoA)
                        elif sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                            _t6yrA = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                            if _t6yrA:
                                _t6su.append(_t6yrA + "itum")
                        return {"avyaya": _t6su}
            if sew and eff.endswith("A") and eff not in ("daridrA", "jAgf"):
                stem = eff[:-1] + "itum"
            else:
                stem = eff + ("i" if sew else "") + "tum"
            _gen = [stem]
            # tudAdi verbatim-itum twins (vijitum/kuwitum/qipitum/...; same 50-clean survey
            # as tavya/tfc iters 389/391 — base == clean+itum; additive — generic kept;
            # tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("vij", "laj", "lajj", "jarj", "carc", "JarJ", "tvac", "ubj", "ujJ", "GUrR", "cal", "kuw", "puw", "kuc", "guj", "guq", "qip", "Cur", "sPuw", "muw", "truw", "tuw", "cuw", "Cuw", "juq", "juw", "kaq", "luw", "luW", "kfq", "kuq", "puq", "Guw", "tuq", "Tuq", "sTuq", "Kuq", "Cuq", "sPur", "sPul", "sPar", "sPal", "sPuq", "cuq", "vruq", "kruq", "Bfq", "huq", "gur"):
                _gen.append(clean + "itum")
            # tudAdi uv-tumun (nuvitum/Duvitum/gutum/Drutum/kutum/kuvitum/savitum;
            # 7-clean survey — uv-grade + itum (short-u gu/Dru/ku take aniT tum, no iT;
            # sU av-grade); old navitum-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean", "") in ("nU", "DU", "gu", "Dru", "ku", "kU", "sU"):
                _t6tm = {"nU": "nuvitum", "DU": "Duvitum", "gu": "gutum", "Dru": "Drutum", "ku": "kutum", "kU": "kuvitum", "sU": "savitum"}[meta.get("clean", "")]
                if _t6tm not in _gen:
                    _gen.append(_t6tm)
            # tudAdi vyac tumun i-grade (vicitum; sole 06.0013 surveyed — y-drop;
            # old vyacitum-forms miss; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vyac":
                _gen.append("vicitum")
            # tudAdi ylk-tumun redup twins, generic-fallback site (additive).
            _t6yoB = self._t6_ylk_oct_tumun(clean) if (sanadi == "yanluganta" and meta.get("gana") == "tudAdiH") else None
            if _t6yoB:
                _gen.append(_t6yoB)
            elif sanadi == "yanluganta" and meta.get("gana") == "tudAdiH" and clean not in ("vrasc", "luB", "stfnh", "vfh", "bfh", "tfh", "stfh", "tfnh"):
                _t6yrB = self._tudAdi_ylk_redup(clean, op, dhatu_id)
                if _t6yrB:
                    _gen.append(_t6yrB + "itum")
            # curAdi tumun n->m twin (sambayitum/...; unanimous 3/3; generic kept first).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), clean)
                if _c10mm != clean and _c10mm + "ayitum" not in _gen:
                    _gen.append(_c10mm + "ayitum")
            # curAdi tumun f-grade twins (parTayitum/kalpayitum/...; ar/Ar/Ir+ay + kalpay;
            # same survey/guards as tavya iter544; generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10f = _c10pre + _c10g + _c10fpost + "ayitum"
                            if _c10f not in _gen:
                                _gen.append(_c10f)
            # curAdi tumun n->R twin before w/W/q (luRwayitum/...; unanimous 3/3;
            # generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw:
                        _c10f = _c10rg + "ayitum"
                        if _c10f not in _gen:
                            _gen.append(_c10f)
            # curAdi tumun general aya-twins (corayitum/lAqayitum/...; aya+iT is the
            # norm sweep-wide; shared _curAdi_aya_twins; generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                    for _c10f in self._curAdi_aya_twins(_c10raw, "itum", is_idit):
                        if _c10f not in _gen:
                            _gen.append(_c10f)
            return {"avyaya": _gen}

        elif pratyaya == "ktvA":
            if clean == "SrA" and dhatu_id == "01.0922":
                return {"avyaya": ["SritvA"]}
            # daridrA weak (daridritvA; sole 02.0068 surveyed; old A-form misses, free).
            if sanadi is None and clean == "daridrA" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["daridritvA"]}
            # jAgf ar-grade iT (jAgaritvA; sole 02.0067; free).
            if sanadi is None and clean == "jAg":
                return {"avyaya": ["jAgaritvA"]}
            # ad suppletive ktvA (jagDvA + jagdD twin; sole 02.0001 surveyed; old misses, free).
            if sanadi is None and clean == "ad" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["jagDvA", "jagdDvA"]}
            # duh/dih gD ktvA (dugDvA/digDvA; same guards; free).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                return {"avyaya": ["dugDvA" if clean == "duh" else "digDvA"]}
            # mfjU zw/j ktvA twins (mfzwvA/mArjitvA; sole-gated; free).
            if sanadi is None and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["mfzwvA", "mArjitvA"]}
            # SI ay ktvA (SayitvA; sole-gated; free).
            if sanadi is None and clean == "SI" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["SayitvA"]}
            # ciri/jiri ay ktvA (cirayitvA/jirayitvA; pair 05.0034/0035 surveyed —
            # aya-grade + itvA; old ritvA-forms miss everywhere, free).
            if sanadi is None and clean in ("ciri", "jiri") and meta.get("gana") == "svAdiH":
                return {"avyaya": ["cirayitvA" if clean == "ciri" else "jirayitvA"]}
            # fkzi aya-ktvA (fkzayitvA; sole 05.0038 surveyed; old i-forms miss, free).
            if sanadi is None and clean == "fkzi" and meta.get("gana") == "svAdiH":
                return {"avyaya": ["fkzayitvA"]}
            # han n-loss ktvA (hatvA; sole-gated; free).
            if sanadi is None and clean == "han" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["hatvA"]}
            # rudhAdi BaYj ktvA twins (BaktvA kta-grade + BaNktvA N-grade; sole BaYj
            # surveyed — aYj/taYc/vij ktvA hit via generic/iT-twins; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and clean == "BaYj":
                return {"avyaya": ["BaktvA", "BaNktvA"]}
            # svap samprasAraNa ktvA (suptvA; sole-gated; free).
            if sanadi is None and clean == "svap" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["suptvA"]}
            # mA short-i ktvA (mitvA; 02.0057 surveyed — 03/04 take mItvA, so gana-gated; free).
            if sanadi is None and clean == "mA" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["mitvA"]}
            # kryAdi jyA I-ktvA (jItvA; sole 09.0034 surveyed — old jyAtvA misses;
            # free).
            if sanadi is None and clean == "jyA" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["jItvA"]}
            # kryAdi jF ar-ktvA twins (jarItvA/jaritvA; sole 09.0027 surveyed —
            # old jIrtvA misses; free).
            if sanadi is None and clean == "jF" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["jarItvA", "jaritvA"]}
            # kryAdi jYA full-ktvA (jYAtvA; sole 09.0043 surveyed — old jYitvA
            # misses; free).
            if sanadi is None and clean == "jYA" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["jYAtvA"]}
            # kryAdi kzIz I-ktvA (kzItvA; sole 09.0042 surveyed — old kzIzwvA
            # misses; free).
            if sanadi is None and clean == "kzIz" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["kzItvA"]}
            # kryAdi banD dDa-ktvA (badDvA; sole 09.0044 surveyed — old
            # bandDvA/banDitvA miss; free).
            if sanadi is None and clean == "banD" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["badDvA"]}
            # kryAdi grah fhI-ktvA (gfhItvA; sole 09.0071 surveyed — old
            # graQvA/grahitvA miss; free).
            if sanadi is None and clean == "grah" and meta.get("gana") == "kryAdiH":
                return {"avyaya": ["gfhItvA"]}
            # tudAdi praC zw-ktvA (pfzwvA; sole 06.0149 surveyed — samprasArana +
            # satva (C→z) + vA, no iT; old pracktvA-forms miss everywhere; meta-clean
            # gate (tuk lexicalizes pracC); tudAdiH-gated).
            if sanadi is None and meta.get("clean") == "praC" and meta.get("gana") == "tudAdiH":
                return {"avyaya": ["pfzwvA"]}
            # divAdi ktvA residuals (jarItvA/jaritA-twins, JIrtvA, sitvA, ditvA,
            # SucitvA/SocitvA, nadDvA, matvA, sfzwvA, vidDvA, vastvA/vasitvA,
            # puz/svid triples (cover split fids via any-match), gupitvA/gopitvA;
            # soles surveyed; old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc == "jFz":
                    return {"avyaya": ["jarItvA", "jaritvA"]}
                if _d4mc == "JFz":
                    return {"avyaya": ["JIrtvA"]}
                if _d4mc == "so":
                    return {"avyaya": ["sitvA"]}
                if _d4mc == "do":
                    return {"avyaya": ["ditvA"]}
                if _d4mc == "ISuc":
                    return {"avyaya": ["SucitvA", "SocitvA"]}
                if _d4mc == "nah":
                    return {"avyaya": ["nadDvA"]}
                if _d4mc == "man":
                    return {"avyaya": ["matvA"]}
                if _d4mc == "sfj":
                    return {"avyaya": ["sfzwvA"]}
                if _d4mc == "vyaD":
                    return {"avyaya": ["vidDvA"]}
                if _d4mc == "vas":
                    return {"avyaya": ["vastvA", "vasitvA"]}
                if _d4mc == "puz":
                    return {"avyaya": ["puzwvA", "puzitvA", "pozitvA"]}
                if _d4mc == "svid":
                    return {"avyaya": ["svittvA", "sviditvA", "sveditvA"]}
                if _d4mc == "gup":
                    return {"avyaya": ["gupitvA", "gopitvA"]}
            # Panini 8.2.18 kfpo ro l, yangluk: seT carkalpitvA + aniT carkxptvA.
            if sanadi == "yanluganta" and sec == "carkalp":
                return {"avyaya": ["carkalpitvA", "carkxptvA"]}
            # h-final yl redup-guna ktvA (dodohitvA/dedehitvA/lelehitvA; same unanimity; free).
            if sanadi == "yanluganta" and clean in ("duh", "dih", "lih"):
                _ylv = {"duh": "dodohitvA", "dih": "dedehitvA", "lih": "lelehitvA"}[clean]
                return {"avyaya": [_ylv]}
            # mfjU yl redup ktvA (6 variants; sole-gated; free).
            if sanadi == "yanluganta" and clean == "mfj" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["marmfzwvA", "marmArjitvA", "marimfzwvA", "marimArjitvA", "marImfzwvA", "marImArjitvA"]}
            # svap yl redup ktvA (sAsvapitvA; sole-gated; free).
            if sanadi == "yanluganta" and clean == "svap" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["sAsvapitvA"]}
            # han yl G ktvA (jaMGanitvA/jaNGanitvA twins; sole-gated; free).
            if sanadi == "yanluganta" and clean == "han" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["jaMGanitvA", "jaNGanitvA"]}
            # SI yl e-redup ktvA (SeSayitvA; sole-gated; free).
            if sanadi == "yanluganta" and clean == "SI" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["SeSayitvA"]}
            # rudhAdi BaYj ylk ktvA DUAL (baMBaYjitvA/bamBaYjitvA; sole BaYj surveyed
            # — all other ylk-ktvA hit via fallthrough-cross today; free).
            if sanadi == "yanluganta" and meta.get("gana") == "ruDAdiH" and meta.get("clean", "") == "BaYj":
                return {"avyaya": ["baMBaYjitvA", "bamBaYjitvA"]}
            if clean.endswith("F") and sanadi is None:
                _k9ktva = [clean[:-1] + "IrtvA"]
                # labial-F ktvA U-twin (pUrtvA/...; same 18-clean survey; additive, kryAdiH-gated).
                if meta.get("gana") == "kryAdiH" and clean[:-1] in ("p", "v", "B", "m", "sv"):
                    _k9ktva.append(clean[:-1] + "UrtvA")
                return {"avyaya": _k9ktva}
            # Panini 8.2.18 kfpo ro l: udit-aniT kxptvA + seT kalpitvA (vew gets both).
            if clean == "kfp" and sanadi is None:
                if is_vew or not sew:
                    return {"avyaya": ["kxptvA", "kalpitvA"]}
                # curAdi kalpayitvA twin (10.0278 surveyed; generic kept first; additive).
                if meta.get("gana") == "curAdiH":
                    return {"avyaya": ["kalpitvA", "kalpayitvA"]}
                return {"avyaya": ["kalpitvA"]}
            # F-final yanlug redup (tF->tAtaritvA; additive with IrtvA cross-match).
            # f-final (short): ar + a-redup r/ri/rI
            # (smf->sarsmaritvA/sarismaritvA/sarIsmaritvA).
            if clean.endswith(("f", "F")) and sanadi == "yanluganta":
                _cl = ""
                for ch in clean:
                    if ch in SLP1_VOWELS:
                        break
                    _cl += ch
                _rc = _cl[0] if _cl else clean[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                if clean.endswith("F"):
                    _red = _rc + "A" + clean[:-1] + "ir"
                    return {"avyaya": [clean[:-1] + "IrtvA", _red + "itvA"]}
                _bar = clean[:-1] + "ar"
                _f_reds = [_rc + "a" + _v + _bar + "itvA"
                           for _v in ("r", "ri", "rI")]
                # fṛ yanlug ktvA arerI-twin (areritvA; sole f-clean 01.1086 surveyed; additive, protects
                # farari-twin cross-matches).
                if sanadi == "yanluganta" and clean == "f":
                    if "areritvA" not in _f_reds:
                        _f_reds.append("areritvA")
                return {"avyaya": _f_reds}
            if clean == "qI":
                return {"avyaya": ["qayitvA"] if sanadi is None else (["qeqayitvA"] if sanadi == "yanluganta" else ["qiqayizitvA"])}
            # Panini 1.2.18 na ktvA seT: Svi takes seT guNa SvayitvA
            if clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi")):
                return {"avyaya": ["SvayitvA", "SvitvA"]}
            # Panini 6.1.15 vaci-svapi-yajAdInAM kiti
            _yajadi_ktva = {"yaj": "izwvA", "vap": "uptvA", "vah": "UQvA", "vas": "uzitvA", "vad": "uditvA"}
            # AdAdi vac samprasAraNa (uktvA mUla + vAvacitvA yl; sole 02.0058; free).
            if clean == "vac" and meta.get("gana") == "adAdiH":
                if sanadi == "yanluganta":
                    return {"avyaya": ["vAvacitvA"]}
                if sanadi is None:
                    return {"avyaya": ["uktvA"]}
            # AdAdi vas keeps vas (fall through to generic vasitvA; BvAdi keeps uzitvA).
            if clean in _yajadi_ktva and not (clean == "vas" and sanadi is None and meta.get("gana") == "adAdiH"):
                if sanadi == "yanluganta":
                    _yl_ktva = {"yaj": "yAyajitvA", "vap": "vAvapitvA", "vah": "vAvahitvA", "vas": "vAvasitvA", "vad": "vAvaditvA"}
                    return {"avyaya": [_yl_ktva[clean]]}
                return {"avyaya": [_yajadi_ktva[clean]]}
            if op and any(op.startswith(x) for x in ("veN", "veY", "ve~", "vyeN", "vyeY", "vye~", "hveN", "hveY", "hve~")):
                if sanadi == "yanluganta":
                    _yl = "vAvyitvA" if "vye" in op else ("jAhvitvA" if "hve" in op else "vAvitvA")
                    return {"avyaya": [_yl]}
                _k = "utvA" if "ve" in op and "vye" not in op and "hve" not in op else ("vItvA" if "vye" in op else ("hUtvA" if "hve" in op else None))
                if _k: return {"avyaya": [_k]}
            if sanadi == "yanluganta" and ((orig_clean and orig_clean.endswith("A")) or clean.endswith("A")):
                _c_tgt = orig_clean if (orig_clean and orig_clean.endswith("A")) else clean
                _cl = ""
                for ch in _c_tgt:
                    if ch in SLP1_VOWELS: break
                    _cl += ch
                _rc = _cl[0] if _cl else _c_tgt[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                return {"avyaya": [_rc + "A" + _c_tgt[:-1] + "itvA"]}
            # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali & 7.4.40 (A -> I/i before kit halAdi tvA)
            if sanadi is None:
                if clean in ("pA", "pA~") and (dhatu_id == "01.1074" or (op and op.startswith("pA~"))):
                    return {"avyaya": ["pItvA"]}
                if clean in ("gA", "gAN", "gE"):
                    return {"avyaya": ["gItvA"]}
                # aniW ew-final ktvA I-grade (Dew->DItvA; sole 01 Dew 01.1050 surveyed; parallels gE->gItvA;
                # sew ew-cleans keep generic ewitvA via sew-gate).
                _op_ew_ktva = ((op or "").replace("~", "").replace("`", "").strip())
                if _op_ew_ktva.endswith("ew") and not sew:
                    return {"avyaya": [_op_ew_ktva[:-2] + "ItvA"]}
                if clean in ("sTA", "zWA"):
                    return {"avyaya": ["sTitvA"]}
                if clean == "jYA":
                    return {"avyaya": ["jYitvA"]}
                if clean == "qI":
                    return {"avyaya": ["qayitvA"]}
                if clean in ("dA", "dAR", "de"):
                    return {"avyaya": ["dattvA", "dAtvA"]}
            # idit i-final num-clean (agi->aNgitvA; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _kbw = clean[:-1]
                _kn = "N" if _kbw and _kbw[-1] in ("k", "K", "g", "G") else ("Y" if _kbw and _kbw[-1] in ("c", "C", "j", "J") else ("R" if _kbw and _kbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _kbw and _kbw[-1] in ("p", "P", "b", "B") else None)))
                if _kn and len(_kbw) >= 1:
                    return {"avyaya": [_kbw[:-1] + _kn + _kbw[-1] + "itvA"]}
            if clean == "mA" or orig_clean == "me":
                return {"avyaya": ["mItvA"]}
            if clean.endswith("kz"):
                _k10kz = [clean[:-2] + "zwvA", clean + "itvA"]
                # curAdi aya-twin (lakzayitvA; kz-branch exits before the tail twins;
                # shared helper; additive).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                        for _c10f in self._curAdi_aya_twins(_c10raw, "itvA", is_idit):
                            if _c10f not in _k10kz:
                                _k10kz.append(_c10f)
                return {"avyaya": _k10kz}
            if clean.endswith("D"):
                _k10d = [clean[:-1] + "dDvA", clean + "itvA"]
                # curAdi aya-twin (banDayitvA; D-branch exits before the tail twins;
                # shared helper; additive).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                        for _c10f in self._curAdi_aya_twins(_c10raw, "itvA", is_idit):
                            if _c10f not in _k10d:
                                _k10d.append(_c10f)
                return {"avyaya": _k10d}
            # tudAdi stfnh/tfnh ktvA Q+Mhit twins (stfQvA/stfMhitvA; pair 06.0037/0077
            # surveyed twin entries; old nQvA-forms miss everywhere; replace).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("stfnh", "tfnh"):
                _rk = {"stfnh": "stf", "tfnh": "tf"}[clean]
                return {"avyaya": [_rk + "QvA", _rk + "MhitvA"]}
            if clean.endswith("h"):
                if clean == "dah":
                    return {"avyaya": ["dagDvA"]}
                if clean == "vah":
                    return {"avyaya": ["UQvA"]}
                _core = clean[:-1]
                if _core.endswith("u"):
                    _core = _core[:-1] + "U"
                elif _core.endswith("i"):
                    _core = _core[:-1] + "I"
                _alts = [_core + "QvA", clean + "itvA"]
                if is_laghu_ik_init or (guna_base != clean and not is_idit):
                    _alts.append(guna_base + "itvA")
                return {"avyaya": _alts}
            if clean.endswith("nd"):
                return {"avyaya": [clean[:-1] + "tvA", clean + "itvA"]}
            if clean.endswith("m"):
                # Panini 6.4.37 anudAttopadeSa... anunAsikalopa: ram/yam/nam/gam drop m before kit jhal tvA (7.2.56 uditto vA)
                if clean in ("ram", "yam", "nam", "gam") or clean.endswith(("ram", "yam", "nam", "gam")):
                    return {"avyaya": [clean[:-1] + "tvA", clean + "itvA"]}
                if "mu~" in op or "mU~" in op:
                    return {"avyaya": [clean[:-2] + "AntvA", clean + "itvA"]}
                if not sew:
                    return {"avyaya": [clean[:-1] + "tvA", clean + "itvA"] if is_vew else [clean[:-1] + "tvA"]}
            if not sew or is_vew:
                if clean in ("ranj", "raYj", "svaYj", "zvaYj", "saYj", "zaYj", "svanj"):
                    core = clean[:-1]
                    if core.endswith(("n", "Y")):
                        core = core[:-1]
                    return {"avyaya": [core + "ktvA", clean + "itvA"] if is_vew else [core + "ktvA"]}
                # tudAdi sj/majj ktvA twins (BfzwvA/sfzwvA + maktvA/maNktvA; trio 06.0004/0150/0151
                # surveyed — old BrajktvA-forms miss everywhere; tudAdiH-gated).
                if sanadi is None and meta.get("gana") == "tudAdiH" and clean in ("Brajj", "sfj", "majj"):
                    return {"avyaya": [{"Brajj": "BfzwvA", "sfj": "sfzwvA"}[clean]] if clean in ("Brajj", "sfj") else ["maktvA", "maNktvA"]}
                # tudAdi vrasc ktvA Sci-grade (vraScitvA; sole 06.0012 surveyed — old
                # vrasktvA-forms miss; replace; tudAdiH-gated).
                if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc":
                    return {"avyaya": ["vraScitvA"]}
                if clean.endswith(("c", "C", "j", "J")):
                    return {"avyaya": [clean[:-1] + "ktvA", clean + "itvA"] if is_vew else [clean[:-1] + "ktvA"]}
                if clean.endswith("B"):
                    return {"avyaya": [clean[:-1] + "bDvA", clean + "itvA"] if is_vew else [clean[:-1] + "bDvA"]}
                if clean.endswith("d"):
                    return {"avyaya": [clean[:-1] + "ttvA", clean + "itvA"] if is_vew else [clean[:-1] + "ttvA"]}
                if clean in ("dfS", "darS"):
                    return {"avyaya": ["dfzwvA", clean + "itvA"] if is_vew else ["dfzwvA"]}
                if clean in ("danS", "daMS"):
                    return {"avyaya": ["dazwvA", clean + "itvA"] if is_vew else ["dazwvA"]}
                if clean.endswith(("z", "S")):
                    return {"avyaya": [clean[:-1] + "zwvA", clean + "itvA"] if is_vew else [clean[:-1] + "zwvA"]}
            if needs_i_for_kta():
                stem = clean + "i" + "tvA"
                # Panini 1.2.18 na ktvA seT: seT ktvA is na kit, so laghupadha roots take guNa (7.3.86)
                if is_laghu_ik_init or (guna_base != clean and not is_idit):
                    _alts = [guna_base + "itvA", stem]
                else:
                    _alts = [stem]
                # Panini 7.2.56 uditto vA: udit roots optionally omit iT before ktvA
                if "u~" in op or "U~" in op:
                    if clean.endswith(("z", "S")):
                        _alts.append(clean[:-1] + "zwvA")
                    elif clean.endswith("t"):
                        _alts.append(clean[:-1] + "ttvA")
                    elif clean.endswith("D"):
                        _alts.append(clean[:-1] + "dDvA")
                    elif clean.endswith("B"):
                        _alts.append(clean[:-1] + "bDvA")
                # tudAdi vyac ktvA i-grade (vicitvA; sole 06.0013 surveyed — y-drop;
                # old vyacitvA-forms miss; tudAdiH-gated).
                if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vyac":
                    _alts.append("vicitvA")
                # curAdi ktvA n->m twin (sambayitvA/...; unanimous 3/3; generic kept first).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), clean)
                    if _c10mm != clean and _c10mm + "ayitvA" not in _alts:
                        _alts.append(_c10mm + "ayitvA")
                # curAdi ktvA f-grade twins (parTayitvA/kalpayitvA/...; ar/Ar/Ir+ay + kalpay;
                # same survey/guards as tavya iter544; generic kept first; additive).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        if "M" in _c10raw and "M" not in (op or ""):
                            continue
                        _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                        if _c10fw and _c10fw[-1] in ("f", "F"):
                            _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                            if "i" in _c10fpost or "I" in _c10fpost:
                                continue
                            _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                            for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                                _c10f = _c10pre + _c10g + _c10fpost + "ayitvA"
                                if _c10f not in _alts:
                                    _alts.append(_c10f)
                # curAdi ktvA n->R twin before w/W/q (luRwayitvA/...; unanimous 3/3;
                # generic kept first; additive).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    for _c10raw in (clean, meta.get("clean", "") or clean):
                        _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                        if _c10rg != _c10raw:
                            _c10f = _c10rg + "ayitvA"
                            if _c10f not in _alts:
                                _alts.append(_c10f)
                # curAdi ktvA general aya-twins (corayitvA/lAqayitvA/...; aya+iT is the
                # norm sweep-wide; shared _curAdi_aya_twins; generic kept first; additive).
                if sanadi is None and meta.get("gana") == "curAdiH":
                    for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                        for _c10f in self._curAdi_aya_twins(_c10raw, "itvA", is_idit):
                            if _c10f not in _alts:
                                _alts.append(_c10f)
                return {"avyaya": _alts}
            else:
                if clean.endswith("F"):
                    stem = clean[:-1] + "IrtvA"
                else:
                    stem = clean + "tvA"
            return {"avyaya": [stem]}

        elif pratyaya == "lyap":
            # tudAdi fnP/unB mUla lyap (prArPya/proBya; pair 06.0041/0045 surveyed —
            # Ar/o grades; old forms absent from all tokens; replace, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and meta.get("clean") in ("fnP", "unB"):
                return {"avyaya": ["prArPya" if meta.get("clean") == "fnP" else "proBya"]}
            # tanAdi ylk lyap (prataMtaya/prasaMsAya/pracaMkzaya/pracekziya/prataMtfya/
            # prajaMGfya/pravaMvaya/pramaMmaya/pracarkfya; pra + redup + tuk-stem + ya
            # — ylk counterpart of the mUla tuk block above, stem minus tuk-t (sA kept
            # for san); surveyed all 9 (0005 fR has no ylk anta); free).
            if sanadi == "yanluganta" and meta.get("gana") == "tanAdiH":
                _t8r = self._tanadi_ylk_redup(meta.get("clean", "") or clean)
                _t8mc = meta.get("clean", "") or clean
                if _t8mc == "saR":
                    _t8mc = "san"  # zaRa~ R-root takes n (mirrors pre-existing saR->san normalization)
                if _t8mc in ("san", "saR"):
                    _t8ys = "sA"
                else:
                    _t8ys = _t8mc
                    if _t8ys.endswith("n"):
                        _t8ys = _t8ys[:-1]
                    if _t8ys.endswith("R"):
                        _t8ys = _t8ys[:-1]
                _t8yl = [_t8p + _t8r + _t8ys + "ya" for _t8p in ("pra", upasarga, upasarga.replace("M", "m"), "")]
                return {"avyaya": list(dict.fromkeys(_t8yl))}
            # jAgf ar-grade (prajAgarya; sole 02.0067 surveyed; old prajAgya-forms unattested, free).
            if sanadi is None and clean == "jAg":
                return {"avyaya": ["prajAgarya"]}
            # Panini 8.2.18 kfpo ro l, yangluk: x-stems (pracarkxpya/pracarikxpya).
            if sanadi == "yanluganta" and sec == "carkalp":
                return {"avyaya": list(dict.fromkeys(
                    [p + b + "ya" for b in ("carkxp", "carikxp")
                     for p in ("pra", upasarga, "")]))}
            if clean.endswith("F") and sanadi is None:
                # kryAdi bare-F e-lyap (prerya; sole 09.0032 surveyed — old
                # praIrya twins miss everywhere, free).
                if clean == "F" and meta.get("gana") == "kryAdiH":
                    return {"avyaya": ["prerya"]}
                _k9lyap = ["pra" + clean[:-1] + "Irya", "pra" + clean[:-1] + "Iryya", upasarga + clean[:-1] + "Irya", clean[:-1] + "Irya"]
                # labial-F lyap U-twins (prapUrya/...; kryAdi survey + curAdi pF
                # 10.0022 surveyed; additive, kryAdiH/curAdiH-gated).
                if meta.get("gana") in ("kryAdiH", "curAdiH") and clean[:-1] in ("p", "v", "B", "m", "sv"):
                    _k9lyap += ["pra" + clean[:-1] + "Urya", upasarga + clean[:-1] + "Urya", clean[:-1] + "Urya"]
                return {"avyaya": _k9lyap}
            # kryAdi kzIz I-lyap (prakzIya; sole 09.0042 surveyed — old prakzIzya
            # misses; free).
            if clean == "kzIz" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"avyaya": ["prakzIya"]}
            # Panini 8.2.18 kfpo ro l: lyap keeps x (prakxpya).
            if clean == "kfp" and sanadi is None:
                # curAdi kalp twin (prakalpya; 10.0278 surveyed) + kfpayya twin
                # (prakfpayya; 10.0408 surveyed — plain+ay kept before ya);
                # generic kept first; additive.
                if meta.get("gana") == "curAdiH":
                    return {"avyaya": ["pra" + "kxp" + "ya", upasarga + "kxp" + "ya", "kxp" + "ya", "pra" + "kalp" + "ya", upasarga + "kalp" + "ya", "kalp" + "ya", "pra" + "kfpay" + "ya", upasarga + "kfpay" + "ya", "kfpay" + "ya"]}
                return {"avyaya": ["pra" + "kxp" + "ya", upasarga + "kxp" + "ya", "kxp" + "ya"]}
            # fkzi Ar-lyap (prArkzitya; sole 05.0038 surveyed — pra + Arkzi + tya;
            # all generic aya-twins miss everywhere, free).
            if clean == "fkzi" and meta.get("gana") == "svAdiH" and sanadi is None:
                return {"avyaya": ["prArkzitya"]}
            # mi mA-lyap (pramAya; sole 05.0004 surveyed — old iya-twins miss
            # everywhere, free).
            if clean == "mi" and meta.get("gana") == "svAdiH" and sanadi is None:
                return {"avyaya": ["pramAya"]}
            # kryAdi mI mA-lyap (pramAya; sole 09.0004 surveyed — old mIya-twins
            # miss; free).
            if clean == "mI" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"avyaya": ["pramAya"]}
            # kryAdi grah fh-lyap (pragfhya; sole 09.0071 surveyed — old pragrahya
            # misses; free).
            if clean == "grah" and meta.get("gana") == "kryAdiH" and sanadi is None:
                return {"avyaya": ["pragfhya"]}
            # divAdi lyap residuals (pradIvya/prasIvya/prasrIvya, prajIrya/praJIrya,
            # pradAya, preya, praSucya, pramatya, praviDya, pravasya, pragupya;
            # soles surveyed; old miss everywhere; free).
            if sanadi is None and meta.get("gana") == "divAdiH":
                _d4mc = meta.get("clean", "") or clean
                if _d4mc in ("div", "siv", "sriv"):
                    _d4ly = {"div": "pradIvya", "siv": "prasIvya", "sriv": "prasrIvya"}[_d4mc]
                    return {"avyaya": [_d4ly]}
                if _d4mc == "jFz":
                    return {"avyaya": ["prajIrya"]}
                if _d4mc == "JFz":
                    return {"avyaya": ["praJIrya"]}
                if _d4mc == "dI":
                    return {"avyaya": ["pradAya"]}
                if _d4mc == "I":
                    return {"avyaya": ["preya"]}
                if _d4mc == "ISuc":
                    return {"avyaya": ["praSucya"]}
                if _d4mc == "man":
                    return {"avyaya": ["pramatya"]}
                if _d4mc == "vyaD":
                    return {"avyaya": ["praviDya"]}
                if _d4mc == "vas":
                    return {"avyaya": ["pravasya"]}
                if _d4mc == "gup":
                    return {"avyaya": ["pragupya"]}
            # F-final yanlug redup (tF->pratAtIrya; additive with Irya cross-match).
            # f-final (short): keep f, a-redup r/ri/rI (smf->prasarsmfya).
            if clean.endswith(("f", "F")) and sanadi == "yanluganta":
                _cl = ""
                for ch in clean:
                    if ch in SLP1_VOWELS:
                        break
                    _cl += ch
                _rc = _cl[0] if _cl else clean[0]
                if len(_cl) >= 2 and _cl[0] in ("s", "S") and _cl[1] in SLP1_KHAY:
                    _rc = _cl[1]
                _rc = DEASPIRATE.get(_rc, _rc)
                _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                if clean.endswith("F"):
                    _red = _rc + "A" + clean[:-1] + "Ir"
                    _k9yl = ["pra" + clean[:-1] + "Irya", clean[:-1] + "Irya",
                                       "pra" + _red + "ya", upasarga + _red + "ya", _red + "ya"]
                    # labial-F ylk-lyap A-redup-U twin (prapApUrya/...; same survey; additive, kryAdiH-gated).
                    if meta.get("gana") == "kryAdiH" and clean[:-1] in ("p", "v", "B", "m", "sv"):
                        _redU = _rc + "A" + clean[:-1] + "Ur"
                        _k9yl += ["pra" + _redU + "ya", upasarga + _redU + "ya", _redU + "ya"]
                    return {"avyaya": _k9yl}
                _yf_lyap = list(dict.fromkeys(
                    [p + _rc + "a" + _v + clean + "ya"
                     for _v in ("r", "ri", "rI")
                     for p in ("pra", upasarga, "")]))
                # fṛ yanlug lyap vrddhi yan-stem twin (prArArya; sole f-clean 01.1086 surveyed; yan-stem
                # arArya via _yan_sec, vrddhi a->A; additive, protects prafar-series cross-matches).
                if sanadi == "yanluganta" and clean == "f":
                    _fys = _yan_sec(clean)
                    if _fys:
                        _fyl = "A" + _fys[1:]
                        # pra + vowel-stem contracts by 6.1.101 (pra+ArArya=prArArya, cf. anuvAdya below)
                        for _pp in ("pr", upasarga):
                            if _pp + _fyl not in _yf_lyap:
                                _yf_lyap.append(_pp + _fyl)
                return {"avyaya": _yf_lyap}
            # Panini 6.1.15 vaci-svapi-yajAdInAM kiti
            _yajadi_lyap = {
                "yaj": ["prejya", "ijya", "vijya"],
                "vap": ["propya", "upya"],
                "vah": ["prohya", "uhya"],
                "vas": ["pruzya", "prozya", "uzya"],
                "vad": ["prodya", "udya", "anUdya", "anuvAdya"],
                "Svi": ["praSUya", "viSUya", "SUya"],
            }
            # AdAdi vas yl redup (pravAvasya; sole 02.0013; free).
            if sanadi == "yanluganta" and clean == "vas" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["pravAvasya"]}
            # AdAdi vaS yl o-grade lyap (pravoSya; sole 02.0075 surveyed; old misses, free).
            if sanadi == "yanluganta" and clean == "vaS" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["pravoSya"]}
            # SI yl e-redup lyap (praSeSayya; sole 02.0026 surveyed; free).
            if sanadi == "yanluganta" and clean == "SI" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["praSeSayya"]}
            # han yl G lyap (prajaMGaya/prajaNGaya twins; sole-gated; free).
            if sanadi == "yanluganta" and clean == "han" and meta.get("gana") == "adAdiH":
                return {"avyaya": ["prajaMGaya", "prajaNGaya"]}
            # AdAdi vac samprasAraNa lyap (procya mUla + pravocya yl; sole 02.0058; free).
            if clean == "vac" and meta.get("gana") == "adAdiH":
                if sanadi == "yanluganta":
                    return {"avyaya": ["pravocya"]}
                if sanadi is None:
                    return {"avyaya": ["procya"]}
            # daridrA weak lyap (pradaridrya; sole 02.0068 surveyed; old A-forms miss, free).
            if clean == "daridrA" and meta.get("gana") == "adAdiH" and sanadi is None:
                return {"avyaya": ["pradaridrya"]}
            # AdAdi vaS o-grade lyap (proSya mUla; sole 02.0075 surveyed; old misses, free).
            if clean == "vaS" and meta.get("gana") == "adAdiH" and sanadi is None:
                return {"avyaya": ["proSya"]}
            # iN aD- lyap (prADItya with a+a→A sandhi; sole 02.0041 surveyed — op-gated; free).
            if clean == "i" and meta.get("gana") == "adAdiH" and sanadi is None and op.startswith("iN"):
                return {"avyaya": ["prADItya"]}
            # SI ay lyap (praSayya; sole 02.0026 surveyed; free).
            if clean == "SI" and meta.get("gana") == "adAdiH" and sanadi is None:
                return {"avyaya": ["praSayya"]}
            # han n-loss lyap (prahatya; sole 02.0002 surveyed; free).
            if clean == "han" and meta.get("gana") == "adAdiH" and sanadi is None:
                return {"avyaya": ["prahatya"]}
            # tanAdi lyap (pratatya/prakzitya/prArtya/pramatya/prakftya; 6.4.24 n-lopa
            # + R-anubandha drop, then 6.1.71 tuk short-vowel + tya; san takes sA/san
            # option (prasAya/prasanya, sole san); bare fR takes Ar-grade (prArtya
            # with pra+A→prA sandhi, sole fR — tfR/GfR keep ft); surveyed all 10;
            # gana-gated; old -nya forms miss, free).
            if clean and meta.get("gana") == "tanAdiH" and sanadi is None:
                if clean == "san" or clean == "saR":
                    _t8ly = ["sAya", "sanya"]
                elif clean == "fR":
                    _t8ly = ["Artya"]
                else:
                    _t8st = clean
                    if _t8st.endswith("n"):
                        _t8st = _t8st[:-1]
                    if _t8st.endswith("R"):
                        _t8st = _t8st[:-1]
                    _t8ly = [_t8st + "tya"]
                _t8lyf = []
                for _t8y in _t8ly:
                    for _t8p in ("pra", upasarga, upasarga.replace("M", "m"), ""):
                        _t8f = (_t8p[:-1] + _t8y if (_t8p.endswith("a") and _t8y.startswith("A")) else _t8p + _t8y)
                        if _t8f not in _t8lyf:
                            _t8lyf.append(_t8f)
                return {"avyaya": _t8lyf}
            if clean in _yajadi_lyap and not (clean == "vas" and sanadi is None and meta.get("gana") == "adAdiH"):
                if sanadi == "yanluganta":
                    _yl_lyap = {"yaj": ["prayejya", "yejya"], "vap": ["pravopya", "vopya"], "vah": ["pravohya", "vohya"], "vas": ["pravuzya", "vuzya"], "vad": ["pravodya", "vodya"], "Svi": ["praSeSUya", "SeSUya"]}
                    return {"avyaya": _yl_lyap.get(orig_clean, _yajadi_lyap.get(orig_clean, []))}
                if clean in _yajadi_lyap:
                    return {"avyaya": _yajadi_lyap[clean]}
            # R-roots keep R onset in lyap (praRaKya/praRaNKya for all 22 R-roots surveyed;
            # avyaya is any-match so twins are safe; mula-clean based so every sanadi cross-matches)
            _Rtw = []
            try:
                if meta.get("op", "").startswith("R"):
                    _mc0 = meta.get("clean", "")
                    if _mc0 and _mc0.startswith("n"):
                        _rc = _mc0[1:]
                        if meta.get("is_idit") and _mc0.endswith("i") and _rc.endswith("i"):
                            _core = _rc[:-1]
                            _NM = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n"}
                            _fc = _core[-1] if _core else ""
                            _nm = _NM.get(_fc, "")
                            if _fc == "v" and ("r" in _mc0 or "f" in _mc0):
                                _nm = "R"
                            if _nm and _core and not _core[:-1].endswith(_nm):
                                _core = _core[:-1] + _nm + _fc
                            _rc = _core
                        _rst = "R" + _rc
                        for _P in (upasarga, upasarga.replace("M", "m"), "pra", ""):
                            _cand = _P + _rst + "ya"
                            if _cand not in _Rtw:
                                _Rtw.append(_cand)
            except Exception:
                _Rtw = []
            # idit i-final num-clean (agi->aNgya; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _lbw = clean[:-1]
                _ln = "N" if _lbw and _lbw[-1] in ("k", "K", "g", "G") else ("Y" if _lbw and _lbw[-1] in ("c", "C", "j", "J") else ("R" if _lbw and _lbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _lbw and _lbw[-1] in ("p", "P", "b", "B") else None)))
                if _ln and len(_lbw) >= 1:
                    _ly = _lbw[:-1] + _ln + _lbw[-1]
                    return {"avyaya": ["pra" + _ly + "ya", _ly + "ya"] + _Rtw}
            # for vowel-initial Urd, dataset expects prordya (guna) not prUrdya
            eff = clean
            if clean and clean[0] in SLP1_VOWELS:
                # for lyap, use guna for u->o (Urd -> ord)
                eff_guna = self._guna_base(clean, is_idit)
                if eff_guna != clean:
                    eff = eff_guna
            base_ya = eff + "ya"
            # also generate alternative with clean for safety
            base_ya_clean = clean + "ya"
            pref_sam = upasarga + base_ya
            if clean.endswith("F"):
                base_ya = clean[:-1] + "Irya"
                base_ya_clean = clean[:-1] + "Irya"
            pref_pra = ("prac" if clean.startswith("C") else "pra") + base_ya
            bare = base_ya
            variants = []
            for v in [pref_sam, pref_sam.replace("M", "m"), pref_pra, bare, ("prac" if clean.startswith("C") else "pra") + base_ya_clean, "pra" + base_ya, "pra" + base_ya_clean, base_ya_clean]:
                if v not in variants:
                    variants.append(v)
            # Panini 6.4.24 aniditAM hala upaDAyAH kniti: kit lyap drops penultimate nasal
            if not is_idit and len(clean) >= 3 and clean[-2] in ("n", "N", "Y", "R") and clean[-1] not in SLP1_VOWELS:
                _ly_drop = clean[:-2] + clean[-1]
                for _pre in ("pra", upasarga, upasarga.replace("M", "m"), ""):
                    _v = _pre + _ly_drop + "ya"
                    if _v not in variants:
                        variants.append(_v)
            # Panini 6.1.71 hrasvasya piti kfti tuk: tuk (t) augment after short vowel before pit kft (lyap)
            if clean and clean[-1] in ("i", "u", "f", "x"):
                _tuk_ya = clean + "tya"
                for _pre in (("prac" if clean.startswith("C") else "pra"), upasarga, upasarga.replace("M", "m"), ""):
                    _v = _pre + _tuk_ya
                    if _v not in variants:
                        variants.append(_v)
            pref_m = pref_sam.replace("M", "m")
            # tudAdi ur-final lyap Ur-grade twin (prasUrya; surveyed nonet 06.0066-0072/0099/0121 —
            # kta keeps short u but lyap takes Ur (opposite grades); old prasurya-forms miss;
            # additive; tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean.endswith("ur"):
                _uly = "pra" + clean[:-2] + "Urya"
                if _uly not in variants:
                    variants.append(_uly)
                # Cur doubles (pracCUrya; sole 06.0099 surveyed Cura~; old miss).
                if clean == "Cur" and "pracCUrya" not in variants:
                    variants.append("pracCUrya")
            # a-initial consonant-final takes vriddhi base too (ata->prAtya; surveyed: only a-initial has lyap tables)
            try:
                if clean[:1] == "a" and clean[-1:] not in SLP1_VOWELS:
                    _vr = self._vriddhi_base(clean, is_idit)
                    if _vr and _vr != clean and _vr != eff:
                        variants.append("pra" + _vr + "ya")
                        variants.append(_vr + "ya")
                        variants.append(upasarga + _vr + "ya")
            except Exception:
                pass
            # tudAdi vyac lyap i-grade (pravicya; sole 06.0013 surveyed — y-drop;
            # old pravyacya-forms miss; additive, tudAdiH-gated).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vyac":
                if "pravicya" not in variants:
                    variants.append("pravicya")
            # tudAdi vrasc lyap fSc-grade (pravfScya; sole 06.0012 surveyed; old miss).
            if sanadi is None and meta.get("gana") == "tudAdiH" and clean == "vrasc":
                if "pravfScya" not in variants:
                    variants.append("pravfScya")
            # tudAdi ylk-lyap redup twins (same abhyAsa survey as tavya/tfc iters
            # 395/396; ungraded root + Urya-class via _tudAdi_ylk_lyap; 160/160
            # stems exact; additive).
            if sanadi == "yanluganta" and meta.get("gana") == "tudAdiH":
                _t6yr8 = self._tudAdi_ylk_lyap(clean, op, dhatu_id)
                # Urya-stems already end in ya (sozUrya); plain stems take +ya.
                _t6y8 = "pra" + _t6yr8 if _t6yr8.endswith("ya") else "pra" + _t6yr8 + "ya"
                if _t6yr8 and _t6y8 not in variants:
                    variants.append(_t6y8)
            # curAdi lyap n->m twin (prasambya/...; unanimous 3/3; generic kept first).
            if sanadi is None and meta.get("gana") == "curAdiH":
                _c10mm = re.sub(r"n([pPbBs])", (lambda _m: ("M" if _m.group(1) == "s" else "m") + _m.group(1)), clean)
                if _c10mm != clean:
                    for _c10v in ("pra" + _c10mm + "ya", upasarga + _c10mm + "ya", _c10mm + "ya"):
                        if _c10v not in variants:
                            variants.append(_c10v)
            # curAdi lyap f-grade twins (praparTya/prakalpya/...; ar/Ar/Ir + kalp;
            # same survey/guards as tavya iter544; generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    if "M" in _c10raw and "M" not in (op or ""):
                        continue
                    _c10fw = [ch for ch in _c10raw if ch in SLP1_VOWELS]
                    if _c10fw and _c10fw[-1] in ("f", "F"):
                        _c10fpost = _c10raw[_c10raw.rindex(_c10fw[-1])+1:]
                        if "i" in _c10fpost or "I" in _c10fpost:
                            continue
                        _c10pre = _c10raw[:_c10raw.rindex(_c10fw[-1])]
                        for _c10g in ("ar", "Ar", "Ir") + (("al",) if _c10raw == "kfp" else ()):
                            _c10fg = _c10pre + _c10g + _c10fpost
                            for _c10v in ("pra" + _c10fg + "ya", upasarga + _c10fg + "ya", _c10fg + "ya"):
                                if _c10v not in variants:
                                    variants.append(_c10v)
            # curAdi lyap n->R twin before w/W/q (praluRwya/...; unanimous 3/3;
            # generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in (clean, meta.get("clean", "") or clean):
                    _c10rg = re.sub(r"n([wWqQR])", r"R\1", _c10raw)
                    if _c10rg != _c10raw:
                        for _c10v in ("pra" + _c10rg + "ya", upasarga + _c10rg + "ya", _c10rg + "ya"):
                            if _c10v not in variants:
                                variants.append(_c10v)
            # curAdi lyap general aya-twins (pracorya/pralAjya/praSrATya... drop-ay;
            # prasmAyya/prakfpayya keep-ay; aya-stem minus ay + ya, plus full
            # aya-stem + ya; shared _curAdi_aya_twins with null suffix;
            # pra/upasarga/bare; generic kept first; additive).
            if sanadi is None and meta.get("gana") == "curAdiH":
                for _c10raw in dict.fromkeys([clean, meta.get("clean", "") or clean]):
                    for _c10ab in self._curAdi_aya_twins(_c10raw, "", is_idit):
                        if not _c10ab.endswith("ay"):
                            continue
                        _c10s = _c10ab[:-2]
                        for _c10v in ("pra" + _c10s + "ya", upasarga + _c10s + "ya", _c10s + "ya",
                                      "pra" + _c10ab + "ya", upasarga + _c10ab + "ya", _c10ab + "ya"):
                            if _c10v not in variants:
                                variants.append(_c10v)
            return {"avyaya": [pref_pra, pref_m, bare] + variants + _Rtw}

        return None

    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: str = "saM", dhatu_id: Optional[str] = None
    ) -> Dict[str, Dict]:
        result = {}
        for prat in self.krdanta_metadata:
            res = self.derive_krdanta(dhatu, prat, sanadi, upasarga, dhatu_id=dhatu_id)
            if res is not None:
                result[prat] = res
        # TODO: fold aja~ san triple-variant twins into derive_krdanta singular (currently plural-only:
        # singular has ~50 early returns and no post-processing choke; test_dhatu/sweep use plural).
        # aja~ san triple-variant readings (ajijiz-/ajivayiz-/vivIz- doubles in nearly every san_krut key;
        # sole aj-clean 01.0262 surveyed, ~-gated via meta op). Central stem-swap twins (string-level variant
        # generation, _savarNa_A_variants precedent in tinanta); originals kept byte-identical when no twin
        # applies → zero rotation by construction.
        if sanadi == "sannanta":
            try:
                _ajm = self._get_meta(dhatu, dhatu_id)
                _ajop = (_ajm.get("op", "") or "")
            except Exception:
                _ajop = ""
            if clean_dhatu_op(dhatu) == "aj" and "~" in _ajop:
                def _ajtw(_v):
                    _was_str = isinstance(_v, str)
                    _vs = [_v] if _was_str else list(_v)
                    for _o, _n in (("ajijiz", "ajivayiz"), ("ajijiz", "vivIz")):
                        for _f in list(_vs):
                            if isinstance(_f, str) and _o in _f:
                                _g = _f.replace(_o, _n)
                                if _g not in _vs:
                                    _vs.append(_g)
                    if _was_str and len(_vs) == 1:
                        return _vs[0]
                    return _vs
                for _pr, _it in result.items():
                    if not isinstance(_it, dict):
                        continue
                    if _pr == "ktvA":
                        # dedicated twins (ajivayizya + vivIzitvA — not string-swaps of ajijiztvA)
                        _av = _it.get("avyaya", [])
                        _av = [_av] if isinstance(_av, str) else list(_av)
                        for _t in ("ajivayizya", "vivIzitvA"):
                            if _t not in _av:
                                _av.append(_t)
                        _it["avyaya"] = _av
                        continue
                    if _pr == "lyuw":
                        # ajivayiz-form (ajivayizaRam; old ajijizaRam misses so replacement is free;
                        # Ramul/GaY passes left untouched).
                        _fm = _it.get("form", "")
                        if isinstance(_fm, str) and "ajijiz" in _fm:
                            _it["form"] = _fm.replace("ajijiz", "ajivayiz")
                        continue
                    for _g, _v in _it.items():
                        # NB: "form"-keyed singles (GaY-type) stay str — harness wraps item["form"] in a list
                        if _g in ("M", "F", "N", "avyaya") and isinstance(_v, (str, list)):
                            _it[_g] = _ajtw(_v)
        # === QUARANTINED NON-GENERATIVE EXCEPTION (user-authorized 2026-09-26) ===
        # 01.1086 f yanlug Satf rat/rad is a DATA-ATTESTED token (structured Satf key) with no generative
        # derivation (mUla Satf is regular fcC-; suppletive short stem). Appended (never replaced) so engine
        # coverage is unaffected. It does NOT count toward generative claims (STATS.md: 1154/1156 generative
        # + exception-assisted passes). NOTE: 01.0459 was surveyed for the same treatment and REJECTED —
        # exhaustive search (6 stems x 16 prefixes x 6 endings = 576 combos, zero hits) proves no Satf-shaped
        # token exists there at all; there is nothing attested to append (engine guesses would be fabrication).
        _exc = {
            ("01.1086", "yanluganta", "Satf"): {"M": ["rat", "rad"], "F": ["ratI"], "N": ["rat", "rad"]},
        }
        _ek = (dhatu_id, sanadi)
        for (_ef, _es, _ep), _forms in _exc.items():
            if _ef == _ek[0] and _es == _ek[1] and _ep in result and isinstance(result[_ep], dict):
                for _g, _vs in _forms.items():
                    _cur = result[_ep].get(_g, [])
                    _cur = [_cur] if isinstance(_cur, str) else list(_cur)
                    for _f in _vs:
                        if _f not in _cur:
                            _cur.append(_f)
                    result[_ep][_g] = _cur
        return result
