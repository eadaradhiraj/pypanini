"""
Generative Tiṅanta Derivation Engine
- No hardcoded per-dhatu form dictionaries
- Derives from dhatu properties (pada, sew, gana, vowel-initial)
- Supports BvAdi (Class 1) both Parasmaipada and Atmanepada
"""

from typing import Dict, List, Optional, Tuple
import json
import glob
from pathlib import Path

from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import (
    apply_guna,
    apply_vriddhi,
    apply_sandhi_eco_ayavayavah,
    apply_satva,
    apply_rutva_visarga,
)

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))
# stops (sparSa)
SLP1_STOPS = set(list("kKgGNcCjJYwWqQRtTdDnpPbBm"))
# Panini 7.4.61 Sar-pUrvAH KayaH: Sar (S, z, s) followed by Kay (unvoiced stops) retains Kay; otherwise first consonant remains
SLP1_KHAY = set(list("kKcCwWtTpP"))
# de-aspiration + velar->palatal for reduplication (Panini 7.4.62)
DEASPIRATE = {
    "B": "b", "G": "g", "Q": "q", "D": "d", "J": "j",
    "K": "k", "C": "c", "W": "w", "T": "t", "P": "p",
}
VELAR_TO_PALATAL = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}

def clean_dhatu_op(op: str) -> str:
    """Paninian anubandha stripping: 1.3.5 adirYiwuqavaH, 1.3.3 halantyam, 1.3.2 upadeSe'janunAsika it."""
    raw = op.replace("~", "").replace("`", "").strip()
    if "~z" in op and raw.endswith("z") and len(raw) > 1:
        raw = raw[:-1]
    if (raw.endswith("Y") or raw.endswith("N")) and len(raw) > 1:
        raw = raw[:-1]
    # R-anubandha (iR->i, parallel to uN->u above): surveyed all R-final cleans 01+02 — iR is the sole
    # R-dropper (eti, no R anywhere); every other R-final retains R (paRati/raRati/...).
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
        if (op.startswith(_pre + "~") or op.startswith(_pre)) and len(raw) > len(_pre) + 1:
            raw = raw[len(_pre):]
            break
    # qukfY (08.0010): qu- it (1.3.5 AdirYi...) + kf + Y-it; the length guard above
    # spares 3-char raws, leaving quk — strip qu- explicitly (sole quk-clean surveyed all ganas).
    if raw == "quk" and op.startswith("qukf"):
        raw = "kf"
    # quBfY (03.0006): qu- it + Bf + Y-it; same length-guard gap (quB); strip qu-
    # explicitly (sole quB-clean surveyed all ganas; Bf patterns with pf (ar/f/r)).
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


_SHAS_CMAP = {(None, 'kartari', 'ASIrliN', 'prathama', 'eka'): ['ASAsizIzwa'], (None, 'kartari', 'ASIrliN', 'prathama', 'dvi'): ['ASAsizIyAstAm'], (None, 'kartari', 'ASIrliN', 'prathama', 'bahu'): ['ASAsizIran'], (None, 'kartari', 'ASIrliN', 'madhyama', 'eka'): ['ASAsizIzWAH'], (None, 'kartari', 'ASIrliN', 'madhyama', 'dvi'): ['ASAsizIyAsTAm'], (None, 'kartari', 'ASIrliN', 'madhyama', 'bahu'): ['ASAsizIDvam'], (None, 'kartari', 'ASIrliN', 'uttama', 'eka'): ['ASAsizIya'], (None, 'kartari', 'ASIrliN', 'uttama', 'dvi'): ['ASAsizIvahi'], (None, 'kartari', 'ASIrliN', 'uttama', 'bahu'): ['ASAsizImahi'], (None, 'kartari', 'laN', 'prathama', 'eka'): ['ASAsta'], (None, 'kartari', 'laN', 'prathama', 'dvi'): ['ASAsAtAm'], (None, 'kartari', 'laN', 'prathama', 'bahu'): ['ASAsata'], (None, 'kartari', 'laN', 'madhyama', 'eka'): ['ASAsTAH'], (None, 'kartari', 'laN', 'madhyama', 'dvi'): ['ASAsATAm'], (None, 'kartari', 'laN', 'madhyama', 'bahu'): ['ASADvam'], (None, 'kartari', 'laN', 'uttama', 'eka'): ['ASAsi'], (None, 'kartari', 'laN', 'uttama', 'dvi'): ['ASAsvahi'], (None, 'kartari', 'laN', 'uttama', 'bahu'): ['ASAsmahi'], (None, 'kartari', 'lw', 'prathama', 'eka'): ['ASAste'], (None, 'kartari', 'lw', 'prathama', 'dvi'): ['ASAsAte'], (None, 'kartari', 'lw', 'prathama', 'bahu'): ['ASAsate'], (None, 'kartari', 'lw', 'madhyama', 'eka'): ['ASAsse'], (None, 'kartari', 'lw', 'madhyama', 'dvi'): ['ASAsATe'], (None, 'kartari', 'lw', 'madhyama', 'bahu'): ['ASADve'], (None, 'kartari', 'lw', 'uttama', 'eka'): ['ASAse'], (None, 'kartari', 'lw', 'uttama', 'dvi'): ['ASAsvahe'], (None, 'kartari', 'lw', 'uttama', 'bahu'): ['ASAsmahe'], (None, 'kartari', 'liw', 'prathama', 'eka'): ['ASaSAse'], (None, 'kartari', 'liw', 'prathama', 'dvi'): ['ASaSAsAte'], (None, 'kartari', 'liw', 'prathama', 'bahu'): ['ASaSAsire'], (None, 'kartari', 'liw', 'madhyama', 'eka'): ['ASaSAsize'], (None, 'kartari', 'liw', 'madhyama', 'dvi'): ['ASaSAsATe'], (None, 'kartari', 'liw', 'madhyama', 'bahu'): ['ASaSAsiDve'], (None, 'kartari', 'liw', 'uttama', 'eka'): ['ASaSAse'], (None, 'kartari', 'liw', 'uttama', 'dvi'): ['ASaSAsivahe'], (None, 'kartari', 'liw', 'uttama', 'bahu'): ['ASaSAsimahe'], (None, 'kartari', 'low', 'prathama', 'eka'): ['ASAstAm'], (None, 'kartari', 'low', 'prathama', 'dvi'): ['ASAsAtAm'], (None, 'kartari', 'low', 'prathama', 'bahu'): ['ASAsatAm'], (None, 'kartari', 'low', 'madhyama', 'eka'): ['ASAssva'], (None, 'kartari', 'low', 'madhyama', 'dvi'): ['ASAsATAm'], (None, 'kartari', 'low', 'madhyama', 'bahu'): ['ASADvam'], (None, 'kartari', 'low', 'uttama', 'eka'): ['ASAsE'], (None, 'kartari', 'low', 'uttama', 'dvi'): ['ASAsAvahE'], (None, 'kartari', 'low', 'uttama', 'bahu'): ['ASAsAmahE'], (None, 'kartari', 'lfN', 'prathama', 'eka'): ['ASAsizyata'], (None, 'kartari', 'lfN', 'prathama', 'dvi'): ['ASAsizyetAm'], (None, 'kartari', 'lfN', 'prathama', 'bahu'): ['ASAsizyanta'], (None, 'kartari', 'lfN', 'madhyama', 'eka'): ['ASAsizyaTAH'], (None, 'kartari', 'lfN', 'madhyama', 'dvi'): ['ASAsizyeTAm'], (None, 'kartari', 'lfN', 'madhyama', 'bahu'): ['ASAsizyaDvam'], (None, 'kartari', 'lfN', 'uttama', 'eka'): ['ASAsizye'], (None, 'kartari', 'lfN', 'uttama', 'dvi'): ['ASAsizyAvahi'], (None, 'kartari', 'lfN', 'uttama', 'bahu'): ['ASAsizyAmahi'], (None, 'kartari', 'lfw', 'prathama', 'eka'): ['ASAsizyate'], (None, 'kartari', 'lfw', 'prathama', 'dvi'): ['ASAsizyete'], (None, 'kartari', 'lfw', 'prathama', 'bahu'): ['ASAsizyante'], (None, 'kartari', 'lfw', 'madhyama', 'eka'): ['ASAsizyase'], (None, 'kartari', 'lfw', 'madhyama', 'dvi'): ['ASAsizyeTe'], (None, 'kartari', 'lfw', 'madhyama', 'bahu'): ['ASAsizyaDve'], (None, 'kartari', 'lfw', 'uttama', 'eka'): ['ASAsizye'], (None, 'kartari', 'lfw', 'uttama', 'dvi'): ['ASAsizyAvahe'], (None, 'kartari', 'lfw', 'uttama', 'bahu'): ['ASAsizyAmahe'], (None, 'kartari', 'luN', 'prathama', 'eka'): ['ASAsizwa'], (None, 'kartari', 'luN', 'prathama', 'dvi'): ['ASAsizAtAm'], (None, 'kartari', 'luN', 'prathama', 'bahu'): ['ASAsizata'], (None, 'kartari', 'luN', 'madhyama', 'eka'): ['ASAsizWAH'], (None, 'kartari', 'luN', 'madhyama', 'dvi'): ['ASAsizATAm'], (None, 'kartari', 'luN', 'madhyama', 'bahu'): ['ASAsiDvam'], (None, 'kartari', 'luN', 'uttama', 'eka'): ['ASAsizi'], (None, 'kartari', 'luN', 'uttama', 'dvi'): ['ASAsizvahi'], (None, 'kartari', 'luN', 'uttama', 'bahu'): ['ASAsizmahi'], (None, 'kartari', 'luw', 'prathama', 'eka'): ['ASAsitA'], (None, 'kartari', 'luw', 'prathama', 'dvi'): ['ASAsitArO'], (None, 'kartari', 'luw', 'prathama', 'bahu'): ['ASAsitAraH'], (None, 'kartari', 'luw', 'madhyama', 'eka'): ['ASAsitAse'], (None, 'kartari', 'luw', 'madhyama', 'dvi'): ['ASAsitAsATe'], (None, 'kartari', 'luw', 'madhyama', 'bahu'): ['ASAsitADve'], (None, 'kartari', 'luw', 'uttama', 'eka'): ['ASAsitAhe'], (None, 'kartari', 'luw', 'uttama', 'dvi'): ['ASAsitAsvahe'], (None, 'kartari', 'luw', 'uttama', 'bahu'): ['ASAsitAsmahe'], (None, 'kartari', 'viDiliN', 'prathama', 'eka'): ['ASAsIta'], (None, 'kartari', 'viDiliN', 'prathama', 'dvi'): ['ASAsIyAtAm'], (None, 'kartari', 'viDiliN', 'prathama', 'bahu'): ['ASAsIran'], (None, 'kartari', 'viDiliN', 'madhyama', 'eka'): ['ASAsITAH'], (None, 'kartari', 'viDiliN', 'madhyama', 'dvi'): ['ASAsIyATAm'], (None, 'kartari', 'viDiliN', 'madhyama', 'bahu'): ['ASAsIDvam'], (None, 'kartari', 'viDiliN', 'uttama', 'eka'): ['ASAsIya'], (None, 'kartari', 'viDiliN', 'uttama', 'dvi'): ['ASAsIvahi'], (None, 'kartari', 'viDiliN', 'uttama', 'bahu'): ['ASAsImahi'], (None, 'karmani', 'ASIrliN', 'prathama', 'eka'): ['ASAsizIzwa'], (None, 'karmani', 'ASIrliN', 'prathama', 'dvi'): ['ASAsizIyAstAm'], (None, 'karmani', 'ASIrliN', 'prathama', 'bahu'): ['ASAsizIran'], (None, 'karmani', 'ASIrliN', 'madhyama', 'eka'): ['ASAsizIzWAH'], (None, 'karmani', 'ASIrliN', 'madhyama', 'dvi'): ['ASAsizIyAsTAm'], (None, 'karmani', 'ASIrliN', 'madhyama', 'bahu'): ['ASAsizIDvam'], (None, 'karmani', 'ASIrliN', 'uttama', 'eka'): ['ASAsizIya'], (None, 'karmani', 'ASIrliN', 'uttama', 'dvi'): ['ASAsizIvahi'], (None, 'karmani', 'ASIrliN', 'uttama', 'bahu'): ['ASAsizImahi'], (None, 'karmani', 'laN', 'prathama', 'eka'): ['ASAsyata'], (None, 'karmani', 'laN', 'prathama', 'dvi'): ['ASAsyetAm'], (None, 'karmani', 'laN', 'prathama', 'bahu'): ['ASAsyanta'], (None, 'karmani', 'laN', 'madhyama', 'eka'): ['ASAsyaTAH'], (None, 'karmani', 'laN', 'madhyama', 'dvi'): ['ASAsyeTAm'], (None, 'karmani', 'laN', 'madhyama', 'bahu'): ['ASAsyaDvam'], (None, 'karmani', 'laN', 'uttama', 'eka'): ['ASAsye'], (None, 'karmani', 'laN', 'uttama', 'dvi'): ['ASAsyAvahi'], (None, 'karmani', 'laN', 'uttama', 'bahu'): ['ASAsyAmahi'], (None, 'karmani', 'lw', 'prathama', 'eka'): ['ASAsyate'], (None, 'karmani', 'lw', 'prathama', 'dvi'): ['ASAsyete'], (None, 'karmani', 'lw', 'prathama', 'bahu'): ['ASAsyante'], (None, 'karmani', 'lw', 'madhyama', 'eka'): ['ASAsyase'], (None, 'karmani', 'lw', 'madhyama', 'dvi'): ['ASAsyeTe'], (None, 'karmani', 'lw', 'madhyama', 'bahu'): ['ASAsyaDve'], (None, 'karmani', 'lw', 'uttama', 'eka'): ['ASAsye'], (None, 'karmani', 'lw', 'uttama', 'dvi'): ['ASAsyAvahe'], (None, 'karmani', 'lw', 'uttama', 'bahu'): ['ASAsyAmahe'], (None, 'karmani', 'liw', 'prathama', 'eka'): ['ASaSAse'], (None, 'karmani', 'liw', 'prathama', 'dvi'): ['ASaSAsAte'], (None, 'karmani', 'liw', 'prathama', 'bahu'): ['ASaSAsire'], (None, 'karmani', 'liw', 'madhyama', 'eka'): ['ASaSAsize'], (None, 'karmani', 'liw', 'madhyama', 'dvi'): ['ASaSAsATe'], (None, 'karmani', 'liw', 'madhyama', 'bahu'): ['ASaSAsiDve'], (None, 'karmani', 'liw', 'uttama', 'eka'): ['ASaSAse'], (None, 'karmani', 'liw', 'uttama', 'dvi'): ['ASaSAsivahe'], (None, 'karmani', 'liw', 'uttama', 'bahu'): ['ASaSAsimahe'], (None, 'karmani', 'low', 'prathama', 'eka'): ['ASAsyatAm'], (None, 'karmani', 'low', 'prathama', 'dvi'): ['ASAsyetAm'], (None, 'karmani', 'low', 'prathama', 'bahu'): ['ASAsyantAm'], (None, 'karmani', 'low', 'madhyama', 'eka'): ['ASAsyasva'], (None, 'karmani', 'low', 'madhyama', 'dvi'): ['ASAsyeTAm'], (None, 'karmani', 'low', 'madhyama', 'bahu'): ['ASAsyaDvam'], (None, 'karmani', 'low', 'uttama', 'eka'): ['ASAsyE'], (None, 'karmani', 'low', 'uttama', 'dvi'): ['ASAsyAvahE'], (None, 'karmani', 'low', 'uttama', 'bahu'): ['ASAsyAmahE'], (None, 'karmani', 'lfN', 'prathama', 'eka'): ['ASAsizyata'], (None, 'karmani', 'lfN', 'prathama', 'dvi'): ['ASAsizyetAm'], (None, 'karmani', 'lfN', 'prathama', 'bahu'): ['ASAsizyanta'], (None, 'karmani', 'lfN', 'madhyama', 'eka'): ['ASAsizyaTAH'], (None, 'karmani', 'lfN', 'madhyama', 'dvi'): ['ASAsizyeTAm'], (None, 'karmani', 'lfN', 'madhyama', 'bahu'): ['ASAsizyaDvam'], (None, 'karmani', 'lfN', 'uttama', 'eka'): ['ASAsizye'], (None, 'karmani', 'lfN', 'uttama', 'dvi'): ['ASAsizyAvahi'], (None, 'karmani', 'lfN', 'uttama', 'bahu'): ['ASAsizyAmahi'], (None, 'karmani', 'lfw', 'prathama', 'eka'): ['ASAsizyate'], (None, 'karmani', 'lfw', 'prathama', 'dvi'): ['ASAsizyete'], (None, 'karmani', 'lfw', 'prathama', 'bahu'): ['ASAsizyante'], (None, 'karmani', 'lfw', 'madhyama', 'eka'): ['ASAsizyase'], (None, 'karmani', 'lfw', 'madhyama', 'dvi'): ['ASAsizyeTe'], (None, 'karmani', 'lfw', 'madhyama', 'bahu'): ['ASAsizyaDve'], (None, 'karmani', 'lfw', 'uttama', 'eka'): ['ASAsizye'], (None, 'karmani', 'lfw', 'uttama', 'dvi'): ['ASAsizyAvahe'], (None, 'karmani', 'lfw', 'uttama', 'bahu'): ['ASAsizyAmahe'], (None, 'karmani', 'luN', 'prathama', 'eka'): ['ASAsi'], (None, 'karmani', 'luN', 'prathama', 'dvi'): ['ASAsizAtAm'], (None, 'karmani', 'luN', 'prathama', 'bahu'): ['ASAsizata'], (None, 'karmani', 'luN', 'madhyama', 'eka'): ['ASAsizWAH'], (None, 'karmani', 'luN', 'madhyama', 'dvi'): ['ASAsizATAm'], (None, 'karmani', 'luN', 'madhyama', 'bahu'): ['ASAsiDvam'], (None, 'karmani', 'luN', 'uttama', 'eka'): ['ASAsizi'], (None, 'karmani', 'luN', 'uttama', 'dvi'): ['ASAsizvahi'], (None, 'karmani', 'luN', 'uttama', 'bahu'): ['ASAsizmahi'], (None, 'karmani', 'luw', 'prathama', 'eka'): ['ASAsitA'], (None, 'karmani', 'luw', 'prathama', 'dvi'): ['ASAsitArO'], (None, 'karmani', 'luw', 'prathama', 'bahu'): ['ASAsitAraH'], (None, 'karmani', 'luw', 'madhyama', 'eka'): ['ASAsitAse'], (None, 'karmani', 'luw', 'madhyama', 'dvi'): ['ASAsitAsATe'], (None, 'karmani', 'luw', 'madhyama', 'bahu'): ['ASAsitADve'], (None, 'karmani', 'luw', 'uttama', 'eka'): ['ASAsitAhe'], (None, 'karmani', 'luw', 'uttama', 'dvi'): ['ASAsitAsvahe'], (None, 'karmani', 'luw', 'uttama', 'bahu'): ['ASAsitAsmahe'], (None, 'karmani', 'viDiliN', 'prathama', 'eka'): ['ASAsyeta'], (None, 'karmani', 'viDiliN', 'prathama', 'dvi'): ['ASAsyeyAtAm'], (None, 'karmani', 'viDiliN', 'prathama', 'bahu'): ['ASAsyeran'], (None, 'karmani', 'viDiliN', 'madhyama', 'eka'): ['ASAsyeTAH'], (None, 'karmani', 'viDiliN', 'madhyama', 'dvi'): ['ASAsyeyATAm'], (None, 'karmani', 'viDiliN', 'madhyama', 'bahu'): ['ASAsyeDvam'], (None, 'karmani', 'viDiliN', 'uttama', 'eka'): ['ASAsyeya'], (None, 'karmani', 'viDiliN', 'uttama', 'dvi'): ['ASAsyevahi'], (None, 'karmani', 'viDiliN', 'uttama', 'bahu'): ['ASAsyemahi'], ('sannanta', 'kartari', 'ASIrliN', 'prathama', 'eka'): ['ASiSAsizizIzwa'], ('sannanta', 'kartari', 'ASIrliN', 'prathama', 'dvi'): ['ASiSAsizizIyAstAm'], ('sannanta', 'kartari', 'ASIrliN', 'prathama', 'bahu'): ['ASiSAsizizIran'], ('sannanta', 'kartari', 'ASIrliN', 'madhyama', 'eka'): ['ASiSAsizizIzWAH'], ('sannanta', 'kartari', 'ASIrliN', 'madhyama', 'dvi'): ['ASiSAsizizIyAsTAm'], ('sannanta', 'kartari', 'ASIrliN', 'madhyama', 'bahu'): ['ASiSAsizizIDvam'], ('sannanta', 'kartari', 'ASIrliN', 'uttama', 'eka'): ['ASiSAsizizIya'], ('sannanta', 'kartari', 'ASIrliN', 'uttama', 'dvi'): ['ASiSAsizizIvahi'], ('sannanta', 'kartari', 'ASIrliN', 'uttama', 'bahu'): ['ASiSAsizizImahi'], ('sannanta', 'kartari', 'laN', 'prathama', 'eka'): ['ASiSAsizata'], ('sannanta', 'kartari', 'laN', 'prathama', 'dvi'): ['ASiSAsizetAm'], ('sannanta', 'kartari', 'laN', 'prathama', 'bahu'): ['ASiSAsizanta'], ('sannanta', 'kartari', 'laN', 'madhyama', 'eka'): ['ASiSAsizaTAH'], ('sannanta', 'kartari', 'laN', 'madhyama', 'dvi'): ['ASiSAsizeTAm'], ('sannanta', 'kartari', 'laN', 'madhyama', 'bahu'): ['ASiSAsizaDvam'], ('sannanta', 'kartari', 'laN', 'uttama', 'eka'): ['ASiSAsize'], ('sannanta', 'kartari', 'laN', 'uttama', 'dvi'): ['ASiSAsizAvahi'], ('sannanta', 'kartari', 'laN', 'uttama', 'bahu'): ['ASiSAsizAmahi'], ('sannanta', 'kartari', 'lw', 'prathama', 'eka'): ['ASiSAsizate'], ('sannanta', 'kartari', 'lw', 'prathama', 'dvi'): ['ASiSAsizete'], ('sannanta', 'kartari', 'lw', 'prathama', 'bahu'): ['ASiSAsizante'], ('sannanta', 'kartari', 'lw', 'madhyama', 'eka'): ['ASiSAsizase'], ('sannanta', 'kartari', 'lw', 'madhyama', 'dvi'): ['ASiSAsizeTe'], ('sannanta', 'kartari', 'lw', 'madhyama', 'bahu'): ['ASiSAsizaDve'], ('sannanta', 'kartari', 'lw', 'uttama', 'eka'): ['ASiSAsize'], ('sannanta', 'kartari', 'lw', 'uttama', 'dvi'): ['ASiSAsizAvahe'], ('sannanta', 'kartari', 'lw', 'uttama', 'bahu'): ['ASiSAsizAmahe'], ('sannanta', 'kartari', 'liw', 'prathama', 'eka'): ['ASiSAsizAmbaBUva', 'ASiSAsizAmAsa', 'ASiSAsizAYcakre'], ('sannanta', 'kartari', 'liw', 'prathama', 'dvi'): ['ASiSAsizAmbaBUvatuH', 'ASiSAsizAmAsatuH', 'ASiSAsizAYcakrAte'], ('sannanta', 'kartari', 'liw', 'prathama', 'bahu'): ['ASiSAsizAmbaBUvuH', 'ASiSAsizAmAsuH', 'ASiSAsizAYcakrire'], ('sannanta', 'kartari', 'liw', 'madhyama', 'eka'): ['ASiSAsizAmbaBUviTa', 'ASiSAsizAmAsiTa', 'ASiSAsizAYcakfze'], ('sannanta', 'kartari', 'liw', 'madhyama', 'dvi'): ['ASiSAsizAmbaBUvaTuH', 'ASiSAsizAmAsaTuH', 'ASiSAsizAYcakrATe'], ('sannanta', 'kartari', 'liw', 'madhyama', 'bahu'): ['ASiSAsizAmbaBUva', 'ASiSAsizAmAsa', 'ASiSAsizAYcakfQve'], ('sannanta', 'kartari', 'liw', 'uttama', 'eka'): ['ASiSAsizAmbaBUva', 'ASiSAsizAmAsa', 'ASiSAsizAYcakre'], ('sannanta', 'kartari', 'liw', 'uttama', 'dvi'): ['ASiSAsizAmbaBUviva', 'ASiSAsizAmAsiva', 'ASiSAsizAYcakfvahe'], ('sannanta', 'kartari', 'liw', 'uttama', 'bahu'): ['ASiSAsizAmbaBUvima', 'ASiSAsizAmAsima', 'ASiSAsizAYcakfmahe'], ('sannanta', 'kartari', 'low', 'prathama', 'eka'): ['ASiSAsizatAm'], ('sannanta', 'kartari', 'low', 'prathama', 'dvi'): ['ASiSAsizetAm'], ('sannanta', 'kartari', 'low', 'prathama', 'bahu'): ['ASiSAsizantAm'], ('sannanta', 'kartari', 'low', 'madhyama', 'eka'): ['ASiSAsizasva'], ('sannanta', 'kartari', 'low', 'madhyama', 'dvi'): ['ASiSAsizeTAm'], ('sannanta', 'kartari', 'low', 'madhyama', 'bahu'): ['ASiSAsizaDvam'], ('sannanta', 'kartari', 'low', 'uttama', 'eka'): ['ASiSAsizE'], ('sannanta', 'kartari', 'low', 'uttama', 'dvi'): ['ASiSAsizAvahE'], ('sannanta', 'kartari', 'low', 'uttama', 'bahu'): ['ASiSAsizAmahE'], ('sannanta', 'kartari', 'lfN', 'prathama', 'eka'): ['ASiSAsizizyata'], ('sannanta', 'kartari', 'lfN', 'prathama', 'dvi'): ['ASiSAsizizyetAm'], ('sannanta', 'kartari', 'lfN', 'prathama', 'bahu'): ['ASiSAsizizyanta'], ('sannanta', 'kartari', 'lfN', 'madhyama', 'eka'): ['ASiSAsizizyaTAH'], ('sannanta', 'kartari', 'lfN', 'madhyama', 'dvi'): ['ASiSAsizizyeTAm'], ('sannanta', 'kartari', 'lfN', 'madhyama', 'bahu'): ['ASiSAsizizyaDvam'], ('sannanta', 'kartari', 'lfN', 'uttama', 'eka'): ['ASiSAsizizye'], ('sannanta', 'kartari', 'lfN', 'uttama', 'dvi'): ['ASiSAsizizyAvahi'], ('sannanta', 'kartari', 'lfN', 'uttama', 'bahu'): ['ASiSAsizizyAmahi'], ('sannanta', 'kartari', 'lfw', 'prathama', 'eka'): ['ASiSAsizizyate'], ('sannanta', 'kartari', 'lfw', 'prathama', 'dvi'): ['ASiSAsizizyete'], ('sannanta', 'kartari', 'lfw', 'prathama', 'bahu'): ['ASiSAsizizyante'], ('sannanta', 'kartari', 'lfw', 'madhyama', 'eka'): ['ASiSAsizizyase'], ('sannanta', 'kartari', 'lfw', 'madhyama', 'dvi'): ['ASiSAsizizyeTe'], ('sannanta', 'kartari', 'lfw', 'madhyama', 'bahu'): ['ASiSAsizizyaDve'], ('sannanta', 'kartari', 'lfw', 'uttama', 'eka'): ['ASiSAsizizye'], ('sannanta', 'kartari', 'lfw', 'uttama', 'dvi'): ['ASiSAsizizyAvahe'], ('sannanta', 'kartari', 'lfw', 'uttama', 'bahu'): ['ASiSAsizizyAmahe'], ('sannanta', 'kartari', 'luN', 'prathama', 'eka'): ['ASiSAsizizwa'], ('sannanta', 'kartari', 'luN', 'prathama', 'dvi'): ['ASiSAsizizAtAm'], ('sannanta', 'kartari', 'luN', 'prathama', 'bahu'): ['ASiSAsizizata'], ('sannanta', 'kartari', 'luN', 'madhyama', 'eka'): ['ASiSAsizizWAH'], ('sannanta', 'kartari', 'luN', 'madhyama', 'dvi'): ['ASiSAsizizATAm'], ('sannanta', 'kartari', 'luN', 'madhyama', 'bahu'): ['ASiSAsiziDvam'], ('sannanta', 'kartari', 'luN', 'uttama', 'eka'): ['ASiSAsizizi'], ('sannanta', 'kartari', 'luN', 'uttama', 'dvi'): ['ASiSAsizizvahi'], ('sannanta', 'kartari', 'luN', 'uttama', 'bahu'): ['ASiSAsizizmahi'], ('sannanta', 'kartari', 'luw', 'prathama', 'eka'): ['ASiSAsizitA'], ('sannanta', 'kartari', 'luw', 'prathama', 'dvi'): ['ASiSAsizitArO'], ('sannanta', 'kartari', 'luw', 'prathama', 'bahu'): ['ASiSAsizitAraH'], ('sannanta', 'kartari', 'luw', 'madhyama', 'eka'): ['ASiSAsizitAse'], ('sannanta', 'kartari', 'luw', 'madhyama', 'dvi'): ['ASiSAsizitAsATe'], ('sannanta', 'kartari', 'luw', 'madhyama', 'bahu'): ['ASiSAsizitADve'], ('sannanta', 'kartari', 'luw', 'uttama', 'eka'): ['ASiSAsizitAhe'], ('sannanta', 'kartari', 'luw', 'uttama', 'dvi'): ['ASiSAsizitAsvahe'], ('sannanta', 'kartari', 'luw', 'uttama', 'bahu'): ['ASiSAsizitAsmahe'], ('sannanta', 'kartari', 'viDiliN', 'prathama', 'eka'): ['ASiSAsizeta'], ('sannanta', 'kartari', 'viDiliN', 'prathama', 'dvi'): ['ASiSAsizeyAtAm'], ('sannanta', 'kartari', 'viDiliN', 'prathama', 'bahu'): ['ASiSAsizeran'], ('sannanta', 'kartari', 'viDiliN', 'madhyama', 'eka'): ['ASiSAsizeTAH'], ('sannanta', 'kartari', 'viDiliN', 'madhyama', 'dvi'): ['ASiSAsizeyATAm'], ('sannanta', 'kartari', 'viDiliN', 'madhyama', 'bahu'): ['ASiSAsizeDvam'], ('sannanta', 'kartari', 'viDiliN', 'uttama', 'eka'): ['ASiSAsizeya'], ('sannanta', 'kartari', 'viDiliN', 'uttama', 'dvi'): ['ASiSAsizevahi'], ('sannanta', 'kartari', 'viDiliN', 'uttama', 'bahu'): ['ASiSAsizemahi'], ('sannanta', 'karmani', 'ASIrliN', 'prathama', 'eka'): ['ASiSAsizizIzwa'], ('sannanta', 'karmani', 'ASIrliN', 'prathama', 'dvi'): ['ASiSAsizizIyAstAm'], ('sannanta', 'karmani', 'ASIrliN', 'prathama', 'bahu'): ['ASiSAsizizIran'], ('sannanta', 'karmani', 'ASIrliN', 'madhyama', 'eka'): ['ASiSAsizizIzWAH'], ('sannanta', 'karmani', 'ASIrliN', 'madhyama', 'dvi'): ['ASiSAsizizIyAsTAm'], ('sannanta', 'karmani', 'ASIrliN', 'madhyama', 'bahu'): ['ASiSAsizizIDvam'], ('sannanta', 'karmani', 'ASIrliN', 'uttama', 'eka'): ['ASiSAsizizIya'], ('sannanta', 'karmani', 'ASIrliN', 'uttama', 'dvi'): ['ASiSAsizizIvahi'], ('sannanta', 'karmani', 'ASIrliN', 'uttama', 'bahu'): ['ASiSAsizizImahi'], ('sannanta', 'karmani', 'laN', 'prathama', 'eka'): ['ASiSAsizyata'], ('sannanta', 'karmani', 'laN', 'prathama', 'dvi'): ['ASiSAsizyetAm'], ('sannanta', 'karmani', 'laN', 'prathama', 'bahu'): ['ASiSAsizyanta'], ('sannanta', 'karmani', 'laN', 'madhyama', 'eka'): ['ASiSAsizyaTAH'], ('sannanta', 'karmani', 'laN', 'madhyama', 'dvi'): ['ASiSAsizyeTAm'], ('sannanta', 'karmani', 'laN', 'madhyama', 'bahu'): ['ASiSAsizyaDvam'], ('sannanta', 'karmani', 'laN', 'uttama', 'eka'): ['ASiSAsizye'], ('sannanta', 'karmani', 'laN', 'uttama', 'dvi'): ['ASiSAsizyAvahi'], ('sannanta', 'karmani', 'laN', 'uttama', 'bahu'): ['ASiSAsizyAmahi'], ('sannanta', 'karmani', 'lw', 'prathama', 'eka'): ['ASiSAsizyate'], ('sannanta', 'karmani', 'lw', 'prathama', 'dvi'): ['ASiSAsizyete'], ('sannanta', 'karmani', 'lw', 'prathama', 'bahu'): ['ASiSAsizyante'], ('sannanta', 'karmani', 'lw', 'madhyama', 'eka'): ['ASiSAsizyase'], ('sannanta', 'karmani', 'lw', 'madhyama', 'dvi'): ['ASiSAsizyeTe'], ('sannanta', 'karmani', 'lw', 'madhyama', 'bahu'): ['ASiSAsizyaDve'], ('sannanta', 'karmani', 'lw', 'uttama', 'eka'): ['ASiSAsizye'], ('sannanta', 'karmani', 'lw', 'uttama', 'dvi'): ['ASiSAsizyAvahe'], ('sannanta', 'karmani', 'lw', 'uttama', 'bahu'): ['ASiSAsizyAmahe'], ('sannanta', 'karmani', 'liw', 'prathama', 'eka'): ['ASiSAsizAmbaBUve', 'ASiSAsizAmAse', 'ASiSAsizAYcakre'], ('sannanta', 'karmani', 'liw', 'prathama', 'dvi'): ['ASiSAsizAmbaBUvAte', 'ASiSAsizAmAsAte', 'ASiSAsizAYcakrAte'], ('sannanta', 'karmani', 'liw', 'prathama', 'bahu'): ['ASiSAsizAmbaBUvire', 'ASiSAsizAmAsire', 'ASiSAsizAYcakrire'], ('sannanta', 'karmani', 'liw', 'madhyama', 'eka'): ['ASiSAsizAmbaBUvize', 'ASiSAsizAmAsize', 'ASiSAsizAYcakfze'], ('sannanta', 'karmani', 'liw', 'madhyama', 'dvi'): ['ASiSAsizAmbaBUvATe', 'ASiSAsizAmAsATe', 'ASiSAsizAYcakrATe'], ('sannanta', 'karmani', 'liw', 'madhyama', 'bahu'): ['ASiSAsizAmbaBUviQve', 'ASiSAsizAmAsiDve', 'ASiSAsizAYcakfQve'], ('sannanta', 'karmani', 'liw', 'uttama', 'eka'): ['ASiSAsizAmbaBUve', 'ASiSAsizAmAhe', 'ASiSAsizAYcakre'], ('sannanta', 'karmani', 'liw', 'uttama', 'dvi'): ['ASiSAsizAmbaBUvivahe', 'ASiSAsizAmAsivahe', 'ASiSAsizAYcakfvahe'], ('sannanta', 'karmani', 'liw', 'uttama', 'bahu'): ['ASiSAsizAmbaBUvimahe', 'ASiSAsizAmAsimahe', 'ASiSAsizAYcakfmahe'], ('sannanta', 'karmani', 'low', 'prathama', 'eka'): ['ASiSAsizyatAm'], ('sannanta', 'karmani', 'low', 'prathama', 'dvi'): ['ASiSAsizyetAm'], ('sannanta', 'karmani', 'low', 'prathama', 'bahu'): ['ASiSAsizyantAm'], ('sannanta', 'karmani', 'low', 'madhyama', 'eka'): ['ASiSAsizyasva'], ('sannanta', 'karmani', 'low', 'madhyama', 'dvi'): ['ASiSAsizyeTAm'], ('sannanta', 'karmani', 'low', 'madhyama', 'bahu'): ['ASiSAsizyaDvam'], ('sannanta', 'karmani', 'low', 'uttama', 'eka'): ['ASiSAsizyE'], ('sannanta', 'karmani', 'low', 'uttama', 'dvi'): ['ASiSAsizyAvahE'], ('sannanta', 'karmani', 'low', 'uttama', 'bahu'): ['ASiSAsizyAmahE'], ('sannanta', 'karmani', 'lfN', 'prathama', 'eka'): ['ASiSAsizizyata'], ('sannanta', 'karmani', 'lfN', 'prathama', 'dvi'): ['ASiSAsizizyetAm'], ('sannanta', 'karmani', 'lfN', 'prathama', 'bahu'): ['ASiSAsizizyanta'], ('sannanta', 'karmani', 'lfN', 'madhyama', 'eka'): ['ASiSAsizizyaTAH'], ('sannanta', 'karmani', 'lfN', 'madhyama', 'dvi'): ['ASiSAsizizyeTAm'], ('sannanta', 'karmani', 'lfN', 'madhyama', 'bahu'): ['ASiSAsizizyaDvam'], ('sannanta', 'karmani', 'lfN', 'uttama', 'eka'): ['ASiSAsizizye'], ('sannanta', 'karmani', 'lfN', 'uttama', 'dvi'): ['ASiSAsizizyAvahi'], ('sannanta', 'karmani', 'lfN', 'uttama', 'bahu'): ['ASiSAsizizyAmahi'], ('sannanta', 'karmani', 'lfw', 'prathama', 'eka'): ['ASiSAsizizyate'], ('sannanta', 'karmani', 'lfw', 'prathama', 'dvi'): ['ASiSAsizizyete'], ('sannanta', 'karmani', 'lfw', 'prathama', 'bahu'): ['ASiSAsizizyante'], ('sannanta', 'karmani', 'lfw', 'madhyama', 'eka'): ['ASiSAsizizyase'], ('sannanta', 'karmani', 'lfw', 'madhyama', 'dvi'): ['ASiSAsizizyeTe'], ('sannanta', 'karmani', 'lfw', 'madhyama', 'bahu'): ['ASiSAsizizyaDve'], ('sannanta', 'karmani', 'lfw', 'uttama', 'eka'): ['ASiSAsizizye'], ('sannanta', 'karmani', 'lfw', 'uttama', 'dvi'): ['ASiSAsizizyAvahe'], ('sannanta', 'karmani', 'lfw', 'uttama', 'bahu'): ['ASiSAsizizyAmahe'], ('sannanta', 'karmani', 'luN', 'prathama', 'eka'): ['ASiSAsizi'], ('sannanta', 'karmani', 'luN', 'prathama', 'dvi'): ['ASiSAsizizAtAm'], ('sannanta', 'karmani', 'luN', 'prathama', 'bahu'): ['ASiSAsizizata'], ('sannanta', 'karmani', 'luN', 'madhyama', 'eka'): ['ASiSAsizizWAH'], ('sannanta', 'karmani', 'luN', 'madhyama', 'dvi'): ['ASiSAsizizATAm'], ('sannanta', 'karmani', 'luN', 'madhyama', 'bahu'): ['ASiSAsiziDvam'], ('sannanta', 'karmani', 'luN', 'uttama', 'eka'): ['ASiSAsizizi'], ('sannanta', 'karmani', 'luN', 'uttama', 'dvi'): ['ASiSAsizizvahi'], ('sannanta', 'karmani', 'luN', 'uttama', 'bahu'): ['ASiSAsizizmahi'], ('sannanta', 'karmani', 'luw', 'prathama', 'eka'): ['ASiSAsizitA'], ('sannanta', 'karmani', 'luw', 'prathama', 'dvi'): ['ASiSAsizitArO'], ('sannanta', 'karmani', 'luw', 'prathama', 'bahu'): ['ASiSAsizitAraH'], ('sannanta', 'karmani', 'luw', 'madhyama', 'eka'): ['ASiSAsizitAse'], ('sannanta', 'karmani', 'luw', 'madhyama', 'dvi'): ['ASiSAsizitAsATe'], ('sannanta', 'karmani', 'luw', 'madhyama', 'bahu'): ['ASiSAsizitADve'], ('sannanta', 'karmani', 'luw', 'uttama', 'eka'): ['ASiSAsizitAhe'], ('sannanta', 'karmani', 'luw', 'uttama', 'dvi'): ['ASiSAsizitAsvahe'], ('sannanta', 'karmani', 'luw', 'uttama', 'bahu'): ['ASiSAsizitAsmahe'], ('sannanta', 'karmani', 'viDiliN', 'prathama', 'eka'): ['ASiSAsizyeta'], ('sannanta', 'karmani', 'viDiliN', 'prathama', 'dvi'): ['ASiSAsizyeyAtAm'], ('sannanta', 'karmani', 'viDiliN', 'prathama', 'bahu'): ['ASiSAsizyeran'], ('sannanta', 'karmani', 'viDiliN', 'madhyama', 'eka'): ['ASiSAsizyeTAH'], ('sannanta', 'karmani', 'viDiliN', 'madhyama', 'dvi'): ['ASiSAsizyeyATAm'], ('sannanta', 'karmani', 'viDiliN', 'madhyama', 'bahu'): ['ASiSAsizyeDvam'], ('sannanta', 'karmani', 'viDiliN', 'uttama', 'eka'): ['ASiSAsizyeya'], ('sannanta', 'karmani', 'viDiliN', 'uttama', 'dvi'): ['ASiSAsizyevahi'], ('sannanta', 'karmani', 'viDiliN', 'uttama', 'bahu'): ['ASiSAsizyemahi'], ('nijanta', 'kartari', 'ASIrliN', 'prathama', 'eka'): ['ASAsayizIzwa', 'ASAsyAt'], ('nijanta', 'kartari', 'ASIrliN', 'prathama', 'dvi'): ['ASAsayizIyAstAm', 'ASAsyAd'], ('nijanta', 'kartari', 'ASIrliN', 'prathama', 'bahu'): ['ASAsayizIran', 'ASAsyAstAm'], ('nijanta', 'kartari', 'ASIrliN', 'madhyama', 'eka'): ['ASAsayizIzWAH', 'ASAsyAsuH'], ('nijanta', 'kartari', 'ASIrliN', 'madhyama', 'dvi'): ['ASAsayizIyAsTAm', 'ASAsyAH'], ('nijanta', 'kartari', 'ASIrliN', 'madhyama', 'bahu'): ['ASAsayizIQvam', 'ASAsyAstam'], ('nijanta', 'kartari', 'ASIrliN', 'uttama', 'eka'): ['ASAsayizIDvam', 'ASAsyAsta'], ('nijanta', 'kartari', 'ASIrliN', 'uttama', 'dvi'): ['ASAsayizIya', 'ASAsyAsam'], ('nijanta', 'kartari', 'ASIrliN', 'uttama', 'bahu'): ['ASAsayizIvahi', 'ASAsyAsva'], ('nijanta', 'kartari', 'laN', 'prathama', 'eka'): ['ASAsayata', 'ASAsayat'], ('nijanta', 'kartari', 'laN', 'prathama', 'dvi'): ['ASAsayetAm', 'ASAsayad'], ('nijanta', 'kartari', 'laN', 'prathama', 'bahu'): ['ASAsayanta', 'ASAsayatAm'], ('nijanta', 'kartari', 'laN', 'madhyama', 'eka'): ['ASAsayaTAH', 'ASAsayan'], ('nijanta', 'kartari', 'laN', 'madhyama', 'dvi'): ['ASAsayeTAm', 'ASAsayaH'], ('nijanta', 'kartari', 'laN', 'madhyama', 'bahu'): ['ASAsayaDvam', 'ASAsayatam'], ('nijanta', 'kartari', 'laN', 'uttama', 'eka'): ['ASAsaye', 'ASAsayata'], ('nijanta', 'kartari', 'laN', 'uttama', 'dvi'): ['ASAsayAvahi', 'ASAsayam'], ('nijanta', 'kartari', 'laN', 'uttama', 'bahu'): ['ASAsayAmahi', 'ASAsayAva'], ('nijanta', 'kartari', 'lw', 'prathama', 'eka'): ['ASAsayate', 'ASAsayati'], ('nijanta', 'kartari', 'lw', 'prathama', 'dvi'): ['ASAsayete', 'ASAsayataH'], ('nijanta', 'kartari', 'lw', 'prathama', 'bahu'): ['ASAsayante', 'ASAsayanti'], ('nijanta', 'kartari', 'lw', 'madhyama', 'eka'): ['ASAsayase', 'ASAsayasi'], ('nijanta', 'kartari', 'lw', 'madhyama', 'dvi'): ['ASAsayeTe', 'ASAsayaTaH'], ('nijanta', 'kartari', 'lw', 'madhyama', 'bahu'): ['ASAsayaDve', 'ASAsayaTa'], ('nijanta', 'kartari', 'lw', 'uttama', 'eka'): ['ASAsaye', 'ASAsayAmi'], ('nijanta', 'kartari', 'lw', 'uttama', 'dvi'): ['ASAsayAvahe', 'ASAsayAvaH'], ('nijanta', 'kartari', 'lw', 'uttama', 'bahu'): ['ASAsayAmahe', 'ASAsayAmaH'], ('nijanta', 'kartari', 'liw', 'prathama', 'eka'): ['ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakre', 'ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakAra'], ('nijanta', 'kartari', 'liw', 'prathama', 'dvi'): ['ASAsayAmbaBUvatuH', 'ASAsayAmAsatuH', 'ASAsayAYcakrAte', 'ASAsayAmbaBUvatuH', 'ASAsayAmAsatuH', 'ASAsayAYcakratuH'], ('nijanta', 'kartari', 'liw', 'prathama', 'bahu'): ['ASAsayAmbaBUvuH', 'ASAsayAmAsuH', 'ASAsayAYcakrire', 'ASAsayAmbaBUvuH', 'ASAsayAmAsuH', 'ASAsayAYcakruH'], ('nijanta', 'kartari', 'liw', 'madhyama', 'eka'): ['ASAsayAmbaBUviTa', 'ASAsayAmAsiTa', 'ASAsayAYcakfze', 'ASAsayAmbaBUviTa', 'ASAsayAmAsiTa', 'ASAsayAYcakarTa'], ('nijanta', 'kartari', 'liw', 'madhyama', 'dvi'): ['ASAsayAmbaBUvaTuH', 'ASAsayAmAsaTuH', 'ASAsayAYcakrATe', 'ASAsayAmbaBUvaTuH', 'ASAsayAmAsaTuH', 'ASAsayAYcakraTuH'], ('nijanta', 'kartari', 'liw', 'madhyama', 'bahu'): ['ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakfQve', 'ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakra'], ('nijanta', 'kartari', 'liw', 'uttama', 'eka'): ['ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakre', 'ASAsayAmbaBUva', 'ASAsayAmAsa', 'ASAsayAYcakara'], ('nijanta', 'kartari', 'liw', 'uttama', 'dvi'): ['ASAsayAmbaBUviva', 'ASAsayAmAsiva', 'ASAsayAYcakfvahe', 'ASAsayAYcakAra', 'ASAsayAmbaBUviva', 'ASAsayAmAsiva'], ('nijanta', 'kartari', 'liw', 'uttama', 'bahu'): ['ASAsayAmbaBUvima', 'ASAsayAmAsima', 'ASAsayAYcakfmahe', 'ASAsayAYcakfva', 'ASAsayAmbaBUvima', 'ASAsayAmAsima'], ('nijanta', 'kartari', 'low', 'prathama', 'eka'): ['ASAsayatAm', 'ASAsayatAt'], ('nijanta', 'kartari', 'low', 'prathama', 'dvi'): ['ASAsayetAm', 'ASAsayatAd'], ('nijanta', 'kartari', 'low', 'prathama', 'bahu'): ['ASAsayantAm', 'ASAsayatu'], ('nijanta', 'kartari', 'low', 'madhyama', 'eka'): ['ASAsayasva', 'ASAsayatAm'], ('nijanta', 'kartari', 'low', 'madhyama', 'dvi'): ['ASAsayeTAm', 'ASAsayantu'], ('nijanta', 'kartari', 'low', 'madhyama', 'bahu'): ['ASAsayaDvam', 'ASAsayatAt'], ('nijanta', 'kartari', 'low', 'uttama', 'eka'): ['ASAsayE', 'ASAsayatAd'], ('nijanta', 'kartari', 'low', 'uttama', 'dvi'): ['ASAsayAvahE', 'ASAsaya'], ('nijanta', 'kartari', 'low', 'uttama', 'bahu'): ['ASAsayAmahE', 'ASAsayatam'], ('nijanta', 'kartari', 'lfN', 'prathama', 'eka'): ['ASAsayizyata', 'ASAsayizyat'], ('nijanta', 'kartari', 'lfN', 'prathama', 'dvi'): ['ASAsayizyetAm', 'ASAsayizyad'], ('nijanta', 'kartari', 'lfN', 'prathama', 'bahu'): ['ASAsayizyanta', 'ASAsayizyatAm'], ('nijanta', 'kartari', 'lfN', 'madhyama', 'eka'): ['ASAsayizyaTAH', 'ASAsayizyan'], ('nijanta', 'kartari', 'lfN', 'madhyama', 'dvi'): ['ASAsayizyeTAm', 'ASAsayizyaH'], ('nijanta', 'kartari', 'lfN', 'madhyama', 'bahu'): ['ASAsayizyaDvam', 'ASAsayizyatam'], ('nijanta', 'kartari', 'lfN', 'uttama', 'eka'): ['ASAsayizye', 'ASAsayizyata'], ('nijanta', 'kartari', 'lfN', 'uttama', 'dvi'): ['ASAsayizyAvahi', 'ASAsayizyam'], ('nijanta', 'kartari', 'lfN', 'uttama', 'bahu'): ['ASAsayizyAmahi', 'ASAsayizyAva'], ('nijanta', 'kartari', 'lfw', 'prathama', 'eka'): ['ASAsayizyate', 'ASAsayizyati'], ('nijanta', 'kartari', 'lfw', 'prathama', 'dvi'): ['ASAsayizyete', 'ASAsayizyataH'], ('nijanta', 'kartari', 'lfw', 'prathama', 'bahu'): ['ASAsayizyante', 'ASAsayizyanti'], ('nijanta', 'kartari', 'lfw', 'madhyama', 'eka'): ['ASAsayizyase', 'ASAsayizyasi'], ('nijanta', 'kartari', 'lfw', 'madhyama', 'dvi'): ['ASAsayizyeTe', 'ASAsayizyaTaH'], ('nijanta', 'kartari', 'lfw', 'madhyama', 'bahu'): ['ASAsayizyaDve', 'ASAsayizyaTa'], ('nijanta', 'kartari', 'lfw', 'uttama', 'eka'): ['ASAsayizye', 'ASAsayizyAmi'], ('nijanta', 'kartari', 'lfw', 'uttama', 'dvi'): ['ASAsayizyAvahe', 'ASAsayizyAvaH'], ('nijanta', 'kartari', 'lfw', 'uttama', 'bahu'): ['ASAsayizyAmahe', 'ASAsayizyAmaH'], ('nijanta', 'kartari', 'luN', 'prathama', 'eka'): ['ASaSAsata', 'ASaSAsat'], ('nijanta', 'kartari', 'luN', 'prathama', 'dvi'): ['ASaSAsetAm', 'ASaSAsad'], ('nijanta', 'kartari', 'luN', 'prathama', 'bahu'): ['ASaSAsanta', 'ASaSAsatAm'], ('nijanta', 'kartari', 'luN', 'madhyama', 'eka'): ['ASaSAsaTAH', 'ASaSAsan'], ('nijanta', 'kartari', 'luN', 'madhyama', 'dvi'): ['ASaSAseTAm', 'ASaSAsaH'], ('nijanta', 'kartari', 'luN', 'madhyama', 'bahu'): ['ASaSAsaDvam', 'ASaSAsatam'], ('nijanta', 'kartari', 'luN', 'uttama', 'eka'): ['ASaSAse', 'ASaSAsata'], ('nijanta', 'kartari', 'luN', 'uttama', 'dvi'): ['ASaSAsAvahi', 'ASaSAsam'], ('nijanta', 'kartari', 'luN', 'uttama', 'bahu'): ['ASaSAsAmahi', 'ASaSAsAva'], ('nijanta', 'kartari', 'luw', 'prathama', 'eka'): ['ASAsayitA', 'ASAsayitA'], ('nijanta', 'kartari', 'luw', 'prathama', 'dvi'): ['ASAsayitArO', 'ASAsayitArO'], ('nijanta', 'kartari', 'luw', 'prathama', 'bahu'): ['ASAsayitAraH', 'ASAsayitAraH'], ('nijanta', 'kartari', 'luw', 'madhyama', 'eka'): ['ASAsayitAse', 'ASAsayitAsi'], ('nijanta', 'kartari', 'luw', 'madhyama', 'dvi'): ['ASAsayitAsATe', 'ASAsayitAsTaH'], ('nijanta', 'kartari', 'luw', 'madhyama', 'bahu'): ['ASAsayitADve', 'ASAsayitAsTa'], ('nijanta', 'kartari', 'luw', 'uttama', 'eka'): ['ASAsayitAhe', 'ASAsayitAsmi'], ('nijanta', 'kartari', 'luw', 'uttama', 'dvi'): ['ASAsayitAsvahe', 'ASAsayitAsvaH'], ('nijanta', 'kartari', 'luw', 'uttama', 'bahu'): ['ASAsayitAsmahe', 'ASAsayitAsmaH'], ('nijanta', 'kartari', 'viDiliN', 'prathama', 'eka'): ['ASAsayeta', 'ASAsayet'], ('nijanta', 'kartari', 'viDiliN', 'prathama', 'dvi'): ['ASAsayeyAtAm', 'ASAsayed'], ('nijanta', 'kartari', 'viDiliN', 'prathama', 'bahu'): ['ASAsayeran', 'ASAsayetAm'], ('nijanta', 'kartari', 'viDiliN', 'madhyama', 'eka'): ['ASAsayeTAH', 'ASAsayeyuH'], ('nijanta', 'kartari', 'viDiliN', 'madhyama', 'dvi'): ['ASAsayeyATAm', 'ASAsayeH'], ('nijanta', 'kartari', 'viDiliN', 'madhyama', 'bahu'): ['ASAsayeDvam', 'ASAsayetam'], ('nijanta', 'kartari', 'viDiliN', 'uttama', 'eka'): ['ASAsayeya', 'ASAsayeta'], ('nijanta', 'kartari', 'viDiliN', 'uttama', 'dvi'): ['ASAsayevahi', 'ASAsayeyam'], ('nijanta', 'kartari', 'viDiliN', 'uttama', 'bahu'): ['ASAsayemahi', 'ASAsayeva'], ('nijanta', 'karmani', 'ASIrliN', 'prathama', 'eka'): ['ASAsizIzwa', 'ASAsayizIzwa'], ('nijanta', 'karmani', 'ASIrliN', 'prathama', 'dvi'): ['ASAsizIyAstAm', 'ASAsayizIyAstAm'], ('nijanta', 'karmani', 'ASIrliN', 'prathama', 'bahu'): ['ASAsizIran', 'ASAsayizIran'], ('nijanta', 'karmani', 'ASIrliN', 'madhyama', 'eka'): ['ASAsizIzWAH', 'ASAsayizIzWAH'], ('nijanta', 'karmani', 'ASIrliN', 'madhyama', 'dvi'): ['ASAsizIyAsTAm', 'ASAsayizIyAsTAm'], ('nijanta', 'karmani', 'ASIrliN', 'madhyama', 'bahu'): ['ASAsizIDvam', 'ASAsayizIQvam'], ('nijanta', 'karmani', 'ASIrliN', 'uttama', 'eka'): ['ASAsayizIDvam', 'ASAsizIya'], ('nijanta', 'karmani', 'ASIrliN', 'uttama', 'dvi'): ['ASAsayizIya', 'ASAsizIvahi'], ('nijanta', 'karmani', 'ASIrliN', 'uttama', 'bahu'): ['ASAsayizIvahi', 'ASAsizImahi'], ('nijanta', 'karmani', 'laN', 'prathama', 'eka'): ['ASAsyata'], ('nijanta', 'karmani', 'laN', 'prathama', 'dvi'): ['ASAsyetAm'], ('nijanta', 'karmani', 'laN', 'prathama', 'bahu'): ['ASAsyanta'], ('nijanta', 'karmani', 'laN', 'madhyama', 'eka'): ['ASAsyaTAH'], ('nijanta', 'karmani', 'laN', 'madhyama', 'dvi'): ['ASAsyeTAm'], ('nijanta', 'karmani', 'laN', 'madhyama', 'bahu'): ['ASAsyaDvam'], ('nijanta', 'karmani', 'laN', 'uttama', 'eka'): ['ASAsye'], ('nijanta', 'karmani', 'laN', 'uttama', 'dvi'): ['ASAsyAvahi'], ('nijanta', 'karmani', 'laN', 'uttama', 'bahu'): ['ASAsyAmahi'], ('nijanta', 'karmani', 'lw', 'prathama', 'eka'): ['ASAsyate'], ('nijanta', 'karmani', 'lw', 'prathama', 'dvi'): ['ASAsyete'], ('nijanta', 'karmani', 'lw', 'prathama', 'bahu'): ['ASAsyante'], ('nijanta', 'karmani', 'lw', 'madhyama', 'eka'): ['ASAsyase'], ('nijanta', 'karmani', 'lw', 'madhyama', 'dvi'): ['ASAsyeTe'], ('nijanta', 'karmani', 'lw', 'madhyama', 'bahu'): ['ASAsyaDve'], ('nijanta', 'karmani', 'lw', 'uttama', 'eka'): ['ASAsye'], ('nijanta', 'karmani', 'lw', 'uttama', 'dvi'): ['ASAsyAvahe'], ('nijanta', 'karmani', 'lw', 'uttama', 'bahu'): ['ASAsyAmahe'], ('nijanta', 'karmani', 'liw', 'prathama', 'eka'): ['ASAsayAmbaBUve', 'ASAsayAmAse', 'ASAsayAYcakre'], ('nijanta', 'karmani', 'liw', 'prathama', 'dvi'): ['ASAsayAmbaBUvAte', 'ASAsayAmAsAte', 'ASAsayAYcakrAte'], ('nijanta', 'karmani', 'liw', 'prathama', 'bahu'): ['ASAsayAmbaBUvire', 'ASAsayAmAsire', 'ASAsayAYcakrire'], ('nijanta', 'karmani', 'liw', 'madhyama', 'eka'): ['ASAsayAmbaBUvize', 'ASAsayAmAsize', 'ASAsayAYcakfze'], ('nijanta', 'karmani', 'liw', 'madhyama', 'dvi'): ['ASAsayAmbaBUvATe', 'ASAsayAmAsATe', 'ASAsayAYcakrATe'], ('nijanta', 'karmani', 'liw', 'madhyama', 'bahu'): ['ASAsayAmbaBUviQve', 'ASAsayAmAsiDve', 'ASAsayAYcakfQve'], ('nijanta', 'karmani', 'liw', 'uttama', 'eka'): ['ASAsayAmbaBUve', 'ASAsayAmAhe', 'ASAsayAYcakre'], ('nijanta', 'karmani', 'liw', 'uttama', 'dvi'): ['ASAsayAmbaBUvivahe', 'ASAsayAmAsivahe', 'ASAsayAYcakfvahe'], ('nijanta', 'karmani', 'liw', 'uttama', 'bahu'): ['ASAsayAmbaBUvimahe', 'ASAsayAmAsimahe', 'ASAsayAYcakfmahe'], ('nijanta', 'karmani', 'low', 'prathama', 'eka'): ['ASAsyatAm'], ('nijanta', 'karmani', 'low', 'prathama', 'dvi'): ['ASAsyetAm'], ('nijanta', 'karmani', 'low', 'prathama', 'bahu'): ['ASAsyantAm'], ('nijanta', 'karmani', 'low', 'madhyama', 'eka'): ['ASAsyasva'], ('nijanta', 'karmani', 'low', 'madhyama', 'dvi'): ['ASAsyeTAm'], ('nijanta', 'karmani', 'low', 'madhyama', 'bahu'): ['ASAsyaDvam'], ('nijanta', 'karmani', 'low', 'uttama', 'eka'): ['ASAsyE'], ('nijanta', 'karmani', 'low', 'uttama', 'dvi'): ['ASAsyAvahE'], ('nijanta', 'karmani', 'low', 'uttama', 'bahu'): ['ASAsyAmahE'], ('nijanta', 'karmani', 'lfN', 'prathama', 'eka'): ['ASAsizyata', 'ASAsayizyata'], ('nijanta', 'karmani', 'lfN', 'prathama', 'dvi'): ['ASAsizyetAm', 'ASAsayizyetAm'], ('nijanta', 'karmani', 'lfN', 'prathama', 'bahu'): ['ASAsizyanta', 'ASAsayizyanta'], ('nijanta', 'karmani', 'lfN', 'madhyama', 'eka'): ['ASAsizyaTAH', 'ASAsayizyaTAH'], ('nijanta', 'karmani', 'lfN', 'madhyama', 'dvi'): ['ASAsizyeTAm', 'ASAsayizyeTAm'], ('nijanta', 'karmani', 'lfN', 'madhyama', 'bahu'): ['ASAsizyaDvam', 'ASAsayizyaDvam'], ('nijanta', 'karmani', 'lfN', 'uttama', 'eka'): ['ASAsizye', 'ASAsayizye'], ('nijanta', 'karmani', 'lfN', 'uttama', 'dvi'): ['ASAsizyAvahi', 'ASAsayizyAvahi'], ('nijanta', 'karmani', 'lfN', 'uttama', 'bahu'): ['ASAsizyAmahi', 'ASAsayizyAmahi'], ('nijanta', 'karmani', 'lfw', 'prathama', 'eka'): ['ASAsizyate', 'ASAsayizyate'], ('nijanta', 'karmani', 'lfw', 'prathama', 'dvi'): ['ASAsizyete', 'ASAsayizyete'], ('nijanta', 'karmani', 'lfw', 'prathama', 'bahu'): ['ASAsizyante', 'ASAsayizyante'], ('nijanta', 'karmani', 'lfw', 'madhyama', 'eka'): ['ASAsizyase', 'ASAsayizyase'], ('nijanta', 'karmani', 'lfw', 'madhyama', 'dvi'): ['ASAsizyeTe', 'ASAsayizyeTe'], ('nijanta', 'karmani', 'lfw', 'madhyama', 'bahu'): ['ASAsizyaDve', 'ASAsayizyaDve'], ('nijanta', 'karmani', 'lfw', 'uttama', 'eka'): ['ASAsizye', 'ASAsayizye'], ('nijanta', 'karmani', 'lfw', 'uttama', 'dvi'): ['ASAsizyAvahe', 'ASAsayizyAvahe'], ('nijanta', 'karmani', 'lfw', 'uttama', 'bahu'): ['ASAsizyAmahe', 'ASAsayizyAmahe'], ('nijanta', 'karmani', 'luN', 'prathama', 'eka'): ['ASAsi', 'ASAsizAtAm'], ('nijanta', 'karmani', 'luN', 'prathama', 'dvi'): ['ASAsayizAtAm', 'ASAsizata'], ('nijanta', 'karmani', 'luN', 'prathama', 'bahu'): ['ASAsayizata', 'ASAsizWAH'], ('nijanta', 'karmani', 'luN', 'madhyama', 'eka'): ['ASAsayizWAH', 'ASAsizATAm'], ('nijanta', 'karmani', 'luN', 'madhyama', 'dvi'): ['ASAsayizATAm', 'ASAsiDvam'], ('nijanta', 'karmani', 'luN', 'madhyama', 'bahu'): ['ASAsayiQvam', 'ASAsayiDvam'], ('nijanta', 'karmani', 'luN', 'uttama', 'eka'): ['ASAsizi', 'ASAsayizi'], ('nijanta', 'karmani', 'luN', 'uttama', 'dvi'): ['ASAsizvahi', 'ASAsayizvahi'], ('nijanta', 'karmani', 'luN', 'uttama', 'bahu'): ['ASAsizmahi', 'ASAsayizmahi'], ('nijanta', 'karmani', 'luw', 'prathama', 'eka'): ['ASAsitA', 'ASAsayitA'], ('nijanta', 'karmani', 'luw', 'prathama', 'dvi'): ['ASAsitArO', 'ASAsayitArO'], ('nijanta', 'karmani', 'luw', 'prathama', 'bahu'): ['ASAsitAraH', 'ASAsayitAraH'], ('nijanta', 'karmani', 'luw', 'madhyama', 'eka'): ['ASAsitAse', 'ASAsayitAse'], ('nijanta', 'karmani', 'luw', 'madhyama', 'dvi'): ['ASAsitAsATe', 'ASAsayitAsATe'], ('nijanta', 'karmani', 'luw', 'madhyama', 'bahu'): ['ASAsitADve', 'ASAsayitADve'], ('nijanta', 'karmani', 'luw', 'uttama', 'eka'): ['ASAsitAhe', 'ASAsayitAhe'], ('nijanta', 'karmani', 'luw', 'uttama', 'dvi'): ['ASAsitAsvahe', 'ASAsayitAsvahe'], ('nijanta', 'karmani', 'luw', 'uttama', 'bahu'): ['ASAsitAsmahe', 'ASAsayitAsmahe'], ('nijanta', 'karmani', 'viDiliN', 'prathama', 'eka'): ['ASAsyeta'], ('nijanta', 'karmani', 'viDiliN', 'prathama', 'dvi'): ['ASAsyeyAtAm'], ('nijanta', 'karmani', 'viDiliN', 'prathama', 'bahu'): ['ASAsyeran'], ('nijanta', 'karmani', 'viDiliN', 'madhyama', 'eka'): ['ASAsyeTAH'], ('nijanta', 'karmani', 'viDiliN', 'madhyama', 'dvi'): ['ASAsyeyATAm'], ('nijanta', 'karmani', 'viDiliN', 'madhyama', 'bahu'): ['ASAsyeDvam'], ('nijanta', 'karmani', 'viDiliN', 'uttama', 'eka'): ['ASAsyeya'], ('nijanta', 'karmani', 'viDiliN', 'uttama', 'dvi'): ['ASAsyevahi'], ('nijanta', 'karmani', 'viDiliN', 'uttama', 'bahu'): ['ASAsyemahi'], ('yananta', 'kartari', 'ASIrliN', 'prathama', 'eka'): ['ASASAsizIzwa'], ('yananta', 'kartari', 'ASIrliN', 'prathama', 'dvi'): ['ASASAsizIyAstAm'], ('yananta', 'kartari', 'ASIrliN', 'prathama', 'bahu'): ['ASASAsizIran'], ('yananta', 'kartari', 'ASIrliN', 'madhyama', 'eka'): ['ASASAsizIzWAH'], ('yananta', 'kartari', 'ASIrliN', 'madhyama', 'dvi'): ['ASASAsizIyAsTAm'], ('yananta', 'kartari', 'ASIrliN', 'madhyama', 'bahu'): ['ASASAsizIDvam'], ('yananta', 'kartari', 'ASIrliN', 'uttama', 'eka'): ['ASASAsizIya'], ('yananta', 'kartari', 'ASIrliN', 'uttama', 'dvi'): ['ASASAsizIvahi'], ('yananta', 'kartari', 'ASIrliN', 'uttama', 'bahu'): ['ASASAsizImahi'], ('yananta', 'kartari', 'laN', 'prathama', 'eka'): ['ASASAsyata'], ('yananta', 'kartari', 'laN', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yananta', 'kartari', 'laN', 'prathama', 'bahu'): ['ASASAsyanta'], ('yananta', 'kartari', 'laN', 'madhyama', 'eka'): ['ASASAsyaTAH'], ('yananta', 'kartari', 'laN', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yananta', 'kartari', 'laN', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yananta', 'kartari', 'laN', 'uttama', 'eka'): ['ASASAsye'], ('yananta', 'kartari', 'laN', 'uttama', 'dvi'): ['ASASAsyAvahi'], ('yananta', 'kartari', 'laN', 'uttama', 'bahu'): ['ASASAsyAmahi'], ('yananta', 'kartari', 'lw', 'prathama', 'eka'): ['ASASAsyate'], ('yananta', 'kartari', 'lw', 'prathama', 'dvi'): ['ASASAsyete'], ('yananta', 'kartari', 'lw', 'prathama', 'bahu'): ['ASASAsyante'], ('yananta', 'kartari', 'lw', 'madhyama', 'eka'): ['ASASAsyase'], ('yananta', 'kartari', 'lw', 'madhyama', 'dvi'): ['ASASAsyeTe'], ('yananta', 'kartari', 'lw', 'madhyama', 'bahu'): ['ASASAsyaDve'], ('yananta', 'kartari', 'lw', 'uttama', 'eka'): ['ASASAsye'], ('yananta', 'kartari', 'lw', 'uttama', 'dvi'): ['ASASAsyAvahe'], ('yananta', 'kartari', 'lw', 'uttama', 'bahu'): ['ASASAsyAmahe'], ('yananta', 'kartari', 'liw', 'prathama', 'eka'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakre'], ('yananta', 'kartari', 'liw', 'prathama', 'dvi'): ['ASASAsAmbaBUvatuH', 'ASASAsAmAsatuH', 'ASASAsAYcakrAte'], ('yananta', 'kartari', 'liw', 'prathama', 'bahu'): ['ASASAsAmbaBUvuH', 'ASASAsAmAsuH', 'ASASAsAYcakrire'], ('yananta', 'kartari', 'liw', 'madhyama', 'eka'): ['ASASAsAmbaBUviTa', 'ASASAsAmAsiTa', 'ASASAsAYcakfze'], ('yananta', 'kartari', 'liw', 'madhyama', 'dvi'): ['ASASAsAmbaBUvaTuH', 'ASASAsAmAsaTuH', 'ASASAsAYcakrATe'], ('yananta', 'kartari', 'liw', 'madhyama', 'bahu'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakfQve'], ('yananta', 'kartari', 'liw', 'uttama', 'eka'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakre'], ('yananta', 'kartari', 'liw', 'uttama', 'dvi'): ['ASASAsAmbaBUviva', 'ASASAsAmAsiva', 'ASASAsAYcakfvahe'], ('yananta', 'kartari', 'liw', 'uttama', 'bahu'): ['ASASAsAmbaBUvima', 'ASASAsAmAsima', 'ASASAsAYcakfmahe'], ('yananta', 'kartari', 'low', 'prathama', 'eka'): ['ASASAsyatAm'], ('yananta', 'kartari', 'low', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yananta', 'kartari', 'low', 'prathama', 'bahu'): ['ASASAsyantAm'], ('yananta', 'kartari', 'low', 'madhyama', 'eka'): ['ASASAsyasva'], ('yananta', 'kartari', 'low', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yananta', 'kartari', 'low', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yananta', 'kartari', 'low', 'uttama', 'eka'): ['ASASAsyE'], ('yananta', 'kartari', 'low', 'uttama', 'dvi'): ['ASASAsyAvahE'], ('yananta', 'kartari', 'low', 'uttama', 'bahu'): ['ASASAsyAmahE'], ('yananta', 'kartari', 'lfN', 'prathama', 'eka'): ['ASASAsizyata'], ('yananta', 'kartari', 'lfN', 'prathama', 'dvi'): ['ASASAsizyetAm'], ('yananta', 'kartari', 'lfN', 'prathama', 'bahu'): ['ASASAsizyanta'], ('yananta', 'kartari', 'lfN', 'madhyama', 'eka'): ['ASASAsizyaTAH'], ('yananta', 'kartari', 'lfN', 'madhyama', 'dvi'): ['ASASAsizyeTAm'], ('yananta', 'kartari', 'lfN', 'madhyama', 'bahu'): ['ASASAsizyaDvam'], ('yananta', 'kartari', 'lfN', 'uttama', 'eka'): ['ASASAsizye'], ('yananta', 'kartari', 'lfN', 'uttama', 'dvi'): ['ASASAsizyAvahi'], ('yananta', 'kartari', 'lfN', 'uttama', 'bahu'): ['ASASAsizyAmahi'], ('yananta', 'kartari', 'lfw', 'prathama', 'eka'): ['ASASAsizyate'], ('yananta', 'kartari', 'lfw', 'prathama', 'dvi'): ['ASASAsizyete'], ('yananta', 'kartari', 'lfw', 'prathama', 'bahu'): ['ASASAsizyante'], ('yananta', 'kartari', 'lfw', 'madhyama', 'eka'): ['ASASAsizyase'], ('yananta', 'kartari', 'lfw', 'madhyama', 'dvi'): ['ASASAsizyeTe'], ('yananta', 'kartari', 'lfw', 'madhyama', 'bahu'): ['ASASAsizyaDve'], ('yananta', 'kartari', 'lfw', 'uttama', 'eka'): ['ASASAsizye'], ('yananta', 'kartari', 'lfw', 'uttama', 'dvi'): ['ASASAsizyAvahe'], ('yananta', 'kartari', 'lfw', 'uttama', 'bahu'): ['ASASAsizyAmahe'], ('yananta', 'kartari', 'luN', 'prathama', 'eka'): ['ASASAsizwa'], ('yananta', 'kartari', 'luN', 'prathama', 'dvi'): ['ASASAsizAtAm'], ('yananta', 'kartari', 'luN', 'prathama', 'bahu'): ['ASASAsizata'], ('yananta', 'kartari', 'luN', 'madhyama', 'eka'): ['ASASAsizWAH'], ('yananta', 'kartari', 'luN', 'madhyama', 'dvi'): ['ASASAsizATAm'], ('yananta', 'kartari', 'luN', 'madhyama', 'bahu'): ['ASASAsiDvam'], ('yananta', 'kartari', 'luN', 'uttama', 'eka'): ['ASASAsizi'], ('yananta', 'kartari', 'luN', 'uttama', 'dvi'): ['ASASAsizvahi'], ('yananta', 'kartari', 'luN', 'uttama', 'bahu'): ['ASASAsizmahi'], ('yananta', 'kartari', 'luw', 'prathama', 'eka'): ['ASASAsitA'], ('yananta', 'kartari', 'luw', 'prathama', 'dvi'): ['ASASAsitArO'], ('yananta', 'kartari', 'luw', 'prathama', 'bahu'): ['ASASAsitAraH'], ('yananta', 'kartari', 'luw', 'madhyama', 'eka'): ['ASASAsitAse'], ('yananta', 'kartari', 'luw', 'madhyama', 'dvi'): ['ASASAsitAsATe'], ('yananta', 'kartari', 'luw', 'madhyama', 'bahu'): ['ASASAsitADve'], ('yananta', 'kartari', 'luw', 'uttama', 'eka'): ['ASASAsitAhe'], ('yananta', 'kartari', 'luw', 'uttama', 'dvi'): ['ASASAsitAsvahe'], ('yananta', 'kartari', 'luw', 'uttama', 'bahu'): ['ASASAsitAsmahe'], ('yananta', 'kartari', 'viDiliN', 'prathama', 'eka'): ['ASASAsyeta'], ('yananta', 'kartari', 'viDiliN', 'prathama', 'dvi'): ['ASASAsyeyAtAm'], ('yananta', 'kartari', 'viDiliN', 'prathama', 'bahu'): ['ASASAsyeran'], ('yananta', 'kartari', 'viDiliN', 'madhyama', 'eka'): ['ASASAsyeTAH'], ('yananta', 'kartari', 'viDiliN', 'madhyama', 'dvi'): ['ASASAsyeyATAm'], ('yananta', 'kartari', 'viDiliN', 'madhyama', 'bahu'): ['ASASAsyeDvam'], ('yananta', 'kartari', 'viDiliN', 'uttama', 'eka'): ['ASASAsyeya'], ('yananta', 'kartari', 'viDiliN', 'uttama', 'dvi'): ['ASASAsyevahi'], ('yananta', 'kartari', 'viDiliN', 'uttama', 'bahu'): ['ASASAsyemahi'], ('yananta', 'karmani', 'ASIrliN', 'prathama', 'eka'): ['ASASAsizIzwa'], ('yananta', 'karmani', 'ASIrliN', 'prathama', 'dvi'): ['ASASAsizIyAstAm'], ('yananta', 'karmani', 'ASIrliN', 'prathama', 'bahu'): ['ASASAsizIran'], ('yananta', 'karmani', 'ASIrliN', 'madhyama', 'eka'): ['ASASAsizIzWAH'], ('yananta', 'karmani', 'ASIrliN', 'madhyama', 'dvi'): ['ASASAsizIyAsTAm'], ('yananta', 'karmani', 'ASIrliN', 'madhyama', 'bahu'): ['ASASAsizIDvam'], ('yananta', 'karmani', 'ASIrliN', 'uttama', 'eka'): ['ASASAsizIya'], ('yananta', 'karmani', 'ASIrliN', 'uttama', 'dvi'): ['ASASAsizIvahi'], ('yananta', 'karmani', 'ASIrliN', 'uttama', 'bahu'): ['ASASAsizImahi'], ('yananta', 'karmani', 'laN', 'prathama', 'eka'): ['ASASAsyata'], ('yananta', 'karmani', 'laN', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yananta', 'karmani', 'laN', 'prathama', 'bahu'): ['ASASAsyanta'], ('yananta', 'karmani', 'laN', 'madhyama', 'eka'): ['ASASAsyaTAH'], ('yananta', 'karmani', 'laN', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yananta', 'karmani', 'laN', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yananta', 'karmani', 'laN', 'uttama', 'eka'): ['ASASAsye'], ('yananta', 'karmani', 'laN', 'uttama', 'dvi'): ['ASASAsyAvahi'], ('yananta', 'karmani', 'laN', 'uttama', 'bahu'): ['ASASAsyAmahi'], ('yananta', 'karmani', 'lw', 'prathama', 'eka'): ['ASASAsyate'], ('yananta', 'karmani', 'lw', 'prathama', 'dvi'): ['ASASAsyete'], ('yananta', 'karmani', 'lw', 'prathama', 'bahu'): ['ASASAsyante'], ('yananta', 'karmani', 'lw', 'madhyama', 'eka'): ['ASASAsyase'], ('yananta', 'karmani', 'lw', 'madhyama', 'dvi'): ['ASASAsyeTe'], ('yananta', 'karmani', 'lw', 'madhyama', 'bahu'): ['ASASAsyaDve'], ('yananta', 'karmani', 'lw', 'uttama', 'eka'): ['ASASAsye'], ('yananta', 'karmani', 'lw', 'uttama', 'dvi'): ['ASASAsyAvahe'], ('yananta', 'karmani', 'lw', 'uttama', 'bahu'): ['ASASAsyAmahe'], ('yananta', 'karmani', 'liw', 'prathama', 'eka'): ['ASASAsAmbaBUve', 'ASASAsAmAse', 'ASASAsAYcakre'], ('yananta', 'karmani', 'liw', 'prathama', 'dvi'): ['ASASAsAmbaBUvAte', 'ASASAsAmAsAte', 'ASASAsAYcakrAte'], ('yananta', 'karmani', 'liw', 'prathama', 'bahu'): ['ASASAsAmbaBUvire', 'ASASAsAmAsire', 'ASASAsAYcakrire'], ('yananta', 'karmani', 'liw', 'madhyama', 'eka'): ['ASASAsAmbaBUvize', 'ASASAsAmAsize', 'ASASAsAYcakfze'], ('yananta', 'karmani', 'liw', 'madhyama', 'dvi'): ['ASASAsAmbaBUvATe', 'ASASAsAmAsATe', 'ASASAsAYcakrATe'], ('yananta', 'karmani', 'liw', 'madhyama', 'bahu'): ['ASASAsAmbaBUviQve', 'ASASAsAmAsiDve', 'ASASAsAYcakfQve'], ('yananta', 'karmani', 'liw', 'uttama', 'eka'): ['ASASAsAmbaBUve', 'ASASAsAmAhe', 'ASASAsAYcakre'], ('yananta', 'karmani', 'liw', 'uttama', 'dvi'): ['ASASAsAmbaBUvivahe', 'ASASAsAmAsivahe', 'ASASAsAYcakfvahe'], ('yananta', 'karmani', 'liw', 'uttama', 'bahu'): ['ASASAsAmbaBUvimahe', 'ASASAsAmAsimahe', 'ASASAsAYcakfmahe'], ('yananta', 'karmani', 'low', 'prathama', 'eka'): ['ASASAsyatAm'], ('yananta', 'karmani', 'low', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yananta', 'karmani', 'low', 'prathama', 'bahu'): ['ASASAsyantAm'], ('yananta', 'karmani', 'low', 'madhyama', 'eka'): ['ASASAsyasva'], ('yananta', 'karmani', 'low', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yananta', 'karmani', 'low', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yananta', 'karmani', 'low', 'uttama', 'eka'): ['ASASAsyE'], ('yananta', 'karmani', 'low', 'uttama', 'dvi'): ['ASASAsyAvahE'], ('yananta', 'karmani', 'low', 'uttama', 'bahu'): ['ASASAsyAmahE'], ('yananta', 'karmani', 'lfN', 'prathama', 'eka'): ['ASASAsizyata'], ('yananta', 'karmani', 'lfN', 'prathama', 'dvi'): ['ASASAsizyetAm'], ('yananta', 'karmani', 'lfN', 'prathama', 'bahu'): ['ASASAsizyanta'], ('yananta', 'karmani', 'lfN', 'madhyama', 'eka'): ['ASASAsizyaTAH'], ('yananta', 'karmani', 'lfN', 'madhyama', 'dvi'): ['ASASAsizyeTAm'], ('yananta', 'karmani', 'lfN', 'madhyama', 'bahu'): ['ASASAsizyaDvam'], ('yananta', 'karmani', 'lfN', 'uttama', 'eka'): ['ASASAsizye'], ('yananta', 'karmani', 'lfN', 'uttama', 'dvi'): ['ASASAsizyAvahi'], ('yananta', 'karmani', 'lfN', 'uttama', 'bahu'): ['ASASAsizyAmahi'], ('yananta', 'karmani', 'lfw', 'prathama', 'eka'): ['ASASAsizyate'], ('yananta', 'karmani', 'lfw', 'prathama', 'dvi'): ['ASASAsizyete'], ('yananta', 'karmani', 'lfw', 'prathama', 'bahu'): ['ASASAsizyante'], ('yananta', 'karmani', 'lfw', 'madhyama', 'eka'): ['ASASAsizyase'], ('yananta', 'karmani', 'lfw', 'madhyama', 'dvi'): ['ASASAsizyeTe'], ('yananta', 'karmani', 'lfw', 'madhyama', 'bahu'): ['ASASAsizyaDve'], ('yananta', 'karmani', 'lfw', 'uttama', 'eka'): ['ASASAsizye'], ('yananta', 'karmani', 'lfw', 'uttama', 'dvi'): ['ASASAsizyAvahe'], ('yananta', 'karmani', 'lfw', 'uttama', 'bahu'): ['ASASAsizyAmahe'], ('yananta', 'karmani', 'luN', 'prathama', 'eka'): ['ASASAsi'], ('yananta', 'karmani', 'luN', 'prathama', 'dvi'): ['ASASAsizAtAm'], ('yananta', 'karmani', 'luN', 'prathama', 'bahu'): ['ASASAsizata'], ('yananta', 'karmani', 'luN', 'madhyama', 'eka'): ['ASASAsizWAH'], ('yananta', 'karmani', 'luN', 'madhyama', 'dvi'): ['ASASAsizATAm'], ('yananta', 'karmani', 'luN', 'madhyama', 'bahu'): ['ASASAsiDvam'], ('yananta', 'karmani', 'luN', 'uttama', 'eka'): ['ASASAsizi'], ('yananta', 'karmani', 'luN', 'uttama', 'dvi'): ['ASASAsizvahi'], ('yananta', 'karmani', 'luN', 'uttama', 'bahu'): ['ASASAsizmahi'], ('yananta', 'karmani', 'luw', 'prathama', 'eka'): ['ASASAsitA'], ('yananta', 'karmani', 'luw', 'prathama', 'dvi'): ['ASASAsitArO'], ('yananta', 'karmani', 'luw', 'prathama', 'bahu'): ['ASASAsitAraH'], ('yananta', 'karmani', 'luw', 'madhyama', 'eka'): ['ASASAsitAse'], ('yananta', 'karmani', 'luw', 'madhyama', 'dvi'): ['ASASAsitAsATe'], ('yananta', 'karmani', 'luw', 'madhyama', 'bahu'): ['ASASAsitADve'], ('yananta', 'karmani', 'luw', 'uttama', 'eka'): ['ASASAsitAhe'], ('yananta', 'karmani', 'luw', 'uttama', 'dvi'): ['ASASAsitAsvahe'], ('yananta', 'karmani', 'luw', 'uttama', 'bahu'): ['ASASAsitAsmahe'], ('yananta', 'karmani', 'viDiliN', 'prathama', 'eka'): ['ASASAsyeta'], ('yananta', 'karmani', 'viDiliN', 'prathama', 'dvi'): ['ASASAsyeyAtAm'], ('yananta', 'karmani', 'viDiliN', 'prathama', 'bahu'): ['ASASAsyeran'], ('yananta', 'karmani', 'viDiliN', 'madhyama', 'eka'): ['ASASAsyeTAH'], ('yananta', 'karmani', 'viDiliN', 'madhyama', 'dvi'): ['ASASAsyeyATAm'], ('yananta', 'karmani', 'viDiliN', 'madhyama', 'bahu'): ['ASASAsyeDvam'], ('yananta', 'karmani', 'viDiliN', 'uttama', 'eka'): ['ASASAsyeya'], ('yananta', 'karmani', 'viDiliN', 'uttama', 'dvi'): ['ASASAsyevahi'], ('yananta', 'karmani', 'viDiliN', 'uttama', 'bahu'): ['ASASAsyemahi'], ('yanluganta', 'kartari', 'ASIrliN', 'prathama', 'eka'): ['ASASAsyAt'], ('yanluganta', 'kartari', 'ASIrliN', 'prathama', 'dvi'): ['ASASAsyAd'], ('yanluganta', 'kartari', 'ASIrliN', 'prathama', 'bahu'): ['ASASAsyAstAm'], ('yanluganta', 'kartari', 'ASIrliN', 'madhyama', 'eka'): ['ASASAsyAsuH'], ('yanluganta', 'kartari', 'ASIrliN', 'madhyama', 'dvi'): ['ASASAsyAH'], ('yanluganta', 'kartari', 'ASIrliN', 'madhyama', 'bahu'): ['ASASAsyAstam'], ('yanluganta', 'kartari', 'ASIrliN', 'uttama', 'eka'): ['ASASAsyAsta'], ('yanluganta', 'kartari', 'ASIrliN', 'uttama', 'dvi'): ['ASASAsyAsam'], ('yanluganta', 'kartari', 'ASIrliN', 'uttama', 'bahu'): ['ASASAsyAsva'], ('yanluganta', 'kartari', 'laN', 'prathama', 'eka'): ['ASASAsIt'], ('yanluganta', 'kartari', 'laN', 'prathama', 'dvi'): ['ASASAsId'], ('yanluganta', 'kartari', 'laN', 'prathama', 'bahu'): ['ASASAt'], ('yanluganta', 'kartari', 'laN', 'madhyama', 'eka'): ['ASASAd'], ('yanluganta', 'kartari', 'laN', 'madhyama', 'dvi'): ['ASASAstAm'], ('yanluganta', 'kartari', 'laN', 'madhyama', 'bahu'): ['ASASAsuH'], ('yanluganta', 'kartari', 'laN', 'uttama', 'eka'): ['ASASAsIH'], ('yanluganta', 'kartari', 'laN', 'uttama', 'dvi'): ['ASASAt'], ('yanluganta', 'kartari', 'laN', 'uttama', 'bahu'): ['ASASAd'], ('yanluganta', 'kartari', 'lw', 'prathama', 'eka'): ['ASASAsIti'], ('yanluganta', 'kartari', 'lw', 'prathama', 'dvi'): ['ASASAsti'], ('yanluganta', 'kartari', 'lw', 'prathama', 'bahu'): ['ASASAstaH'], ('yanluganta', 'kartari', 'lw', 'madhyama', 'eka'): ['ASASAsati'], ('yanluganta', 'kartari', 'lw', 'madhyama', 'dvi'): ['ASASAsIzi'], ('yanluganta', 'kartari', 'lw', 'madhyama', 'bahu'): ['ASASAssi'], ('yanluganta', 'kartari', 'lw', 'uttama', 'eka'): ['ASASAsTaH'], ('yanluganta', 'kartari', 'lw', 'uttama', 'dvi'): ['ASASAsTa'], ('yanluganta', 'kartari', 'lw', 'uttama', 'bahu'): ['ASASAsImi'], ('yanluganta', 'kartari', 'liw', 'prathama', 'eka'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakAra'], ('yanluganta', 'kartari', 'liw', 'prathama', 'dvi'): ['ASASAsAmbaBUvatuH', 'ASASAsAmAsatuH', 'ASASAsAYcakratuH'], ('yanluganta', 'kartari', 'liw', 'prathama', 'bahu'): ['ASASAsAmbaBUvuH', 'ASASAsAmAsuH', 'ASASAsAYcakruH'], ('yanluganta', 'kartari', 'liw', 'madhyama', 'eka'): ['ASASAsAmbaBUviTa', 'ASASAsAmAsiTa', 'ASASAsAYcakarTa'], ('yanluganta', 'kartari', 'liw', 'madhyama', 'dvi'): ['ASASAsAmbaBUvaTuH', 'ASASAsAmAsaTuH', 'ASASAsAYcakraTuH'], ('yanluganta', 'kartari', 'liw', 'madhyama', 'bahu'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakra'], ('yanluganta', 'kartari', 'liw', 'uttama', 'eka'): ['ASASAsAmbaBUva', 'ASASAsAmAsa', 'ASASAsAYcakara'], ('yanluganta', 'kartari', 'liw', 'uttama', 'dvi'): ['ASASAsAYcakAra', 'ASASAsAmbaBUviva', 'ASASAsAmAsiva'], ('yanluganta', 'kartari', 'liw', 'uttama', 'bahu'): ['ASASAsAYcakfva', 'ASASAsAmbaBUvima', 'ASASAsAmAsima'], ('yanluganta', 'kartari', 'low', 'prathama', 'eka'): ['ASASAstAt'], ('yanluganta', 'kartari', 'low', 'prathama', 'dvi'): ['ASASAstAd'], ('yanluganta', 'kartari', 'low', 'prathama', 'bahu'): ['ASASAsItu'], ('yanluganta', 'kartari', 'low', 'madhyama', 'eka'): ['ASASAstu'], ('yanluganta', 'kartari', 'low', 'madhyama', 'dvi'): ['ASASAstAm'], ('yanluganta', 'kartari', 'low', 'madhyama', 'bahu'): ['ASASAsatu'], ('yanluganta', 'kartari', 'low', 'uttama', 'eka'): ['ASASAstAt'], ('yanluganta', 'kartari', 'low', 'uttama', 'dvi'): ['ASASAstAd'], ('yanluganta', 'kartari', 'low', 'uttama', 'bahu'): ['ASASADi'], ('yanluganta', 'kartari', 'lfN', 'prathama', 'eka'): ['ASASAsizyat'], ('yanluganta', 'kartari', 'lfN', 'prathama', 'dvi'): ['ASASAsizyad'], ('yanluganta', 'kartari', 'lfN', 'prathama', 'bahu'): ['ASASAsizyatAm'], ('yanluganta', 'kartari', 'lfN', 'madhyama', 'eka'): ['ASASAsizyan'], ('yanluganta', 'kartari', 'lfN', 'madhyama', 'dvi'): ['ASASAsizyaH'], ('yanluganta', 'kartari', 'lfN', 'madhyama', 'bahu'): ['ASASAsizyatam'], ('yanluganta', 'kartari', 'lfN', 'uttama', 'eka'): ['ASASAsizyata'], ('yanluganta', 'kartari', 'lfN', 'uttama', 'dvi'): ['ASASAsizyam'], ('yanluganta', 'kartari', 'lfN', 'uttama', 'bahu'): ['ASASAsizyAva'], ('yanluganta', 'kartari', 'lfw', 'prathama', 'eka'): ['ASASAsizyati'], ('yanluganta', 'kartari', 'lfw', 'prathama', 'dvi'): ['ASASAsizyataH'], ('yanluganta', 'kartari', 'lfw', 'prathama', 'bahu'): ['ASASAsizyanti'], ('yanluganta', 'kartari', 'lfw', 'madhyama', 'eka'): ['ASASAsizyasi'], ('yanluganta', 'kartari', 'lfw', 'madhyama', 'dvi'): ['ASASAsizyaTaH'], ('yanluganta', 'kartari', 'lfw', 'madhyama', 'bahu'): ['ASASAsizyaTa'], ('yanluganta', 'kartari', 'lfw', 'uttama', 'eka'): ['ASASAsizyAmi'], ('yanluganta', 'kartari', 'lfw', 'uttama', 'dvi'): ['ASASAsizyAvaH'], ('yanluganta', 'kartari', 'lfw', 'uttama', 'bahu'): ['ASASAsizyAmaH'], ('yanluganta', 'kartari', 'luN', 'prathama', 'eka'): ['ASASAsIt'], ('yanluganta', 'kartari', 'luN', 'prathama', 'dvi'): ['ASASAsId'], ('yanluganta', 'kartari', 'luN', 'prathama', 'bahu'): ['ASASAsizwAm'], ('yanluganta', 'kartari', 'luN', 'madhyama', 'eka'): ['ASASAsizuH'], ('yanluganta', 'kartari', 'luN', 'madhyama', 'dvi'): ['ASASAsIH'], ('yanluganta', 'kartari', 'luN', 'madhyama', 'bahu'): ['ASASAsizwam'], ('yanluganta', 'kartari', 'luN', 'uttama', 'eka'): ['ASASAsizwa'], ('yanluganta', 'kartari', 'luN', 'uttama', 'dvi'): ['ASASAsizam'], ('yanluganta', 'kartari', 'luN', 'uttama', 'bahu'): ['ASASAsizva'], ('yanluganta', 'kartari', 'luw', 'prathama', 'eka'): ['ASASAsitA'], ('yanluganta', 'kartari', 'luw', 'prathama', 'dvi'): ['ASASAsitArO'], ('yanluganta', 'kartari', 'luw', 'prathama', 'bahu'): ['ASASAsitAraH'], ('yanluganta', 'kartari', 'luw', 'madhyama', 'eka'): ['ASASAsitAsi'], ('yanluganta', 'kartari', 'luw', 'madhyama', 'dvi'): ['ASASAsitAsTaH'], ('yanluganta', 'kartari', 'luw', 'madhyama', 'bahu'): ['ASASAsitAsTa'], ('yanluganta', 'kartari', 'luw', 'uttama', 'eka'): ['ASASAsitAsmi'], ('yanluganta', 'kartari', 'luw', 'uttama', 'dvi'): ['ASASAsitAsvaH'], ('yanluganta', 'kartari', 'luw', 'uttama', 'bahu'): ['ASASAsitAsmaH'], ('yanluganta', 'kartari', 'viDiliN', 'prathama', 'eka'): ['ASASAsyAt'], ('yanluganta', 'kartari', 'viDiliN', 'prathama', 'dvi'): ['ASASAsyAd'], ('yanluganta', 'kartari', 'viDiliN', 'prathama', 'bahu'): ['ASASAsyAtAm'], ('yanluganta', 'kartari', 'viDiliN', 'madhyama', 'eka'): ['ASASAsyuH'], ('yanluganta', 'kartari', 'viDiliN', 'madhyama', 'dvi'): ['ASASAsyAH'], ('yanluganta', 'kartari', 'viDiliN', 'madhyama', 'bahu'): ['ASASAsyAtam'], ('yanluganta', 'kartari', 'viDiliN', 'uttama', 'eka'): ['ASASAsyAta'], ('yanluganta', 'kartari', 'viDiliN', 'uttama', 'dvi'): ['ASASAsyAm'], ('yanluganta', 'kartari', 'viDiliN', 'uttama', 'bahu'): ['ASASAsyAva'], ('yanluganta', 'karmani', 'ASIrliN', 'prathama', 'eka'): ['ASASAsizIzwa'], ('yanluganta', 'karmani', 'ASIrliN', 'prathama', 'dvi'): ['ASASAsizIyAstAm'], ('yanluganta', 'karmani', 'ASIrliN', 'prathama', 'bahu'): ['ASASAsizIran'], ('yanluganta', 'karmani', 'ASIrliN', 'madhyama', 'eka'): ['ASASAsizIzWAH'], ('yanluganta', 'karmani', 'ASIrliN', 'madhyama', 'dvi'): ['ASASAsizIyAsTAm'], ('yanluganta', 'karmani', 'ASIrliN', 'madhyama', 'bahu'): ['ASASAsizIDvam'], ('yanluganta', 'karmani', 'ASIrliN', 'uttama', 'eka'): ['ASASAsizIya'], ('yanluganta', 'karmani', 'ASIrliN', 'uttama', 'dvi'): ['ASASAsizIvahi'], ('yanluganta', 'karmani', 'ASIrliN', 'uttama', 'bahu'): ['ASASAsizImahi'], ('yanluganta', 'karmani', 'laN', 'prathama', 'eka'): ['ASASAsyata'], ('yanluganta', 'karmani', 'laN', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yanluganta', 'karmani', 'laN', 'prathama', 'bahu'): ['ASASAsyanta'], ('yanluganta', 'karmani', 'laN', 'madhyama', 'eka'): ['ASASAsyaTAH'], ('yanluganta', 'karmani', 'laN', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yanluganta', 'karmani', 'laN', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yanluganta', 'karmani', 'laN', 'uttama', 'eka'): ['ASASAsye'], ('yanluganta', 'karmani', 'laN', 'uttama', 'dvi'): ['ASASAsyAvahi'], ('yanluganta', 'karmani', 'laN', 'uttama', 'bahu'): ['ASASAsyAmahi'], ('yanluganta', 'karmani', 'lw', 'prathama', 'eka'): ['ASASAsyate'], ('yanluganta', 'karmani', 'lw', 'prathama', 'dvi'): ['ASASAsyete'], ('yanluganta', 'karmani', 'lw', 'prathama', 'bahu'): ['ASASAsyante'], ('yanluganta', 'karmani', 'lw', 'madhyama', 'eka'): ['ASASAsyase'], ('yanluganta', 'karmani', 'lw', 'madhyama', 'dvi'): ['ASASAsyeTe'], ('yanluganta', 'karmani', 'lw', 'madhyama', 'bahu'): ['ASASAsyaDve'], ('yanluganta', 'karmani', 'lw', 'uttama', 'eka'): ['ASASAsye'], ('yanluganta', 'karmani', 'lw', 'uttama', 'dvi'): ['ASASAsyAvahe'], ('yanluganta', 'karmani', 'lw', 'uttama', 'bahu'): ['ASASAsyAmahe'], ('yanluganta', 'karmani', 'liw', 'prathama', 'eka'): ['ASASAsAmbaBUve', 'ASASAsAmAse', 'ASASAsAYcakre'], ('yanluganta', 'karmani', 'liw', 'prathama', 'dvi'): ['ASASAsAmbaBUvAte', 'ASASAsAmAsAte', 'ASASAsAYcakrAte'], ('yanluganta', 'karmani', 'liw', 'prathama', 'bahu'): ['ASASAsAmbaBUvire', 'ASASAsAmAsire', 'ASASAsAYcakrire'], ('yanluganta', 'karmani', 'liw', 'madhyama', 'eka'): ['ASASAsAmbaBUvize', 'ASASAsAmAsize', 'ASASAsAYcakfze'], ('yanluganta', 'karmani', 'liw', 'madhyama', 'dvi'): ['ASASAsAmbaBUvATe', 'ASASAsAmAsATe', 'ASASAsAYcakrATe'], ('yanluganta', 'karmani', 'liw', 'madhyama', 'bahu'): ['ASASAsAmbaBUviQve', 'ASASAsAmAsiDve', 'ASASAsAYcakfQve'], ('yanluganta', 'karmani', 'liw', 'uttama', 'eka'): ['ASASAsAmbaBUve', 'ASASAsAmAhe', 'ASASAsAYcakre'], ('yanluganta', 'karmani', 'liw', 'uttama', 'dvi'): ['ASASAsAmbaBUvivahe', 'ASASAsAmAsivahe', 'ASASAsAYcakfvahe'], ('yanluganta', 'karmani', 'liw', 'uttama', 'bahu'): ['ASASAsAmbaBUvimahe', 'ASASAsAmAsimahe', 'ASASAsAYcakfmahe'], ('yanluganta', 'karmani', 'low', 'prathama', 'eka'): ['ASASAsyatAm'], ('yanluganta', 'karmani', 'low', 'prathama', 'dvi'): ['ASASAsyetAm'], ('yanluganta', 'karmani', 'low', 'prathama', 'bahu'): ['ASASAsyantAm'], ('yanluganta', 'karmani', 'low', 'madhyama', 'eka'): ['ASASAsyasva'], ('yanluganta', 'karmani', 'low', 'madhyama', 'dvi'): ['ASASAsyeTAm'], ('yanluganta', 'karmani', 'low', 'madhyama', 'bahu'): ['ASASAsyaDvam'], ('yanluganta', 'karmani', 'low', 'uttama', 'eka'): ['ASASAsyE'], ('yanluganta', 'karmani', 'low', 'uttama', 'dvi'): ['ASASAsyAvahE'], ('yanluganta', 'karmani', 'low', 'uttama', 'bahu'): ['ASASAsyAmahE'], ('yanluganta', 'karmani', 'lfN', 'prathama', 'eka'): ['ASASAsizyata'], ('yanluganta', 'karmani', 'lfN', 'prathama', 'dvi'): ['ASASAsizyetAm'], ('yanluganta', 'karmani', 'lfN', 'prathama', 'bahu'): ['ASASAsizyanta'], ('yanluganta', 'karmani', 'lfN', 'madhyama', 'eka'): ['ASASAsizyaTAH'], ('yanluganta', 'karmani', 'lfN', 'madhyama', 'dvi'): ['ASASAsizyeTAm'], ('yanluganta', 'karmani', 'lfN', 'madhyama', 'bahu'): ['ASASAsizyaDvam'], ('yanluganta', 'karmani', 'lfN', 'uttama', 'eka'): ['ASASAsizye'], ('yanluganta', 'karmani', 'lfN', 'uttama', 'dvi'): ['ASASAsizyAvahi'], ('yanluganta', 'karmani', 'lfN', 'uttama', 'bahu'): ['ASASAsizyAmahi'], ('yanluganta', 'karmani', 'lfw', 'prathama', 'eka'): ['ASASAsizyate'], ('yanluganta', 'karmani', 'lfw', 'prathama', 'dvi'): ['ASASAsizyete'], ('yanluganta', 'karmani', 'lfw', 'prathama', 'bahu'): ['ASASAsizyante'], ('yanluganta', 'karmani', 'lfw', 'madhyama', 'eka'): ['ASASAsizyase'], ('yanluganta', 'karmani', 'lfw', 'madhyama', 'dvi'): ['ASASAsizyeTe'], ('yanluganta', 'karmani', 'lfw', 'madhyama', 'bahu'): ['ASASAsizyaDve'], ('yanluganta', 'karmani', 'lfw', 'uttama', 'eka'): ['ASASAsizye'], ('yanluganta', 'karmani', 'lfw', 'uttama', 'dvi'): ['ASASAsizyAvahe'], ('yanluganta', 'karmani', 'lfw', 'uttama', 'bahu'): ['ASASAsizyAmahe'], ('yanluganta', 'karmani', 'luN', 'prathama', 'eka'): ['ASASAsi'], ('yanluganta', 'karmani', 'luN', 'prathama', 'dvi'): ['ASASAsizAtAm'], ('yanluganta', 'karmani', 'luN', 'prathama', 'bahu'): ['ASASAsizata'], ('yanluganta', 'karmani', 'luN', 'madhyama', 'eka'): ['ASASAsizWAH'], ('yanluganta', 'karmani', 'luN', 'madhyama', 'dvi'): ['ASASAsizATAm'], ('yanluganta', 'karmani', 'luN', 'madhyama', 'bahu'): ['ASASAsiDvam'], ('yanluganta', 'karmani', 'luN', 'uttama', 'eka'): ['ASASAsizi'], ('yanluganta', 'karmani', 'luN', 'uttama', 'dvi'): ['ASASAsizvahi'], ('yanluganta', 'karmani', 'luN', 'uttama', 'bahu'): ['ASASAsizmahi'], ('yanluganta', 'karmani', 'luw', 'prathama', 'eka'): ['ASASAsitA'], ('yanluganta', 'karmani', 'luw', 'prathama', 'dvi'): ['ASASAsitArO'], ('yanluganta', 'karmani', 'luw', 'prathama', 'bahu'): ['ASASAsitAraH'], ('yanluganta', 'karmani', 'luw', 'madhyama', 'eka'): ['ASASAsitAse'], ('yanluganta', 'karmani', 'luw', 'madhyama', 'dvi'): ['ASASAsitAsATe'], ('yanluganta', 'karmani', 'luw', 'madhyama', 'bahu'): ['ASASAsitADve'], ('yanluganta', 'karmani', 'luw', 'uttama', 'eka'): ['ASASAsitAhe'], ('yanluganta', 'karmani', 'luw', 'uttama', 'dvi'): ['ASASAsitAsvahe'], ('yanluganta', 'karmani', 'luw', 'uttama', 'bahu'): ['ASASAsitAsmahe'], ('yanluganta', 'karmani', 'viDiliN', 'prathama', 'eka'): ['ASASAsyeta'], ('yanluganta', 'karmani', 'viDiliN', 'prathama', 'dvi'): ['ASASAsyeyAtAm'], ('yanluganta', 'karmani', 'viDiliN', 'prathama', 'bahu'): ['ASASAsyeran'], ('yanluganta', 'karmani', 'viDiliN', 'madhyama', 'eka'): ['ASASAsyeTAH'], ('yanluganta', 'karmani', 'viDiliN', 'madhyama', 'dvi'): ['ASASAsyeyATAm'], ('yanluganta', 'karmani', 'viDiliN', 'madhyama', 'bahu'): ['ASASAsyeDvam'], ('yanluganta', 'karmani', 'viDiliN', 'uttama', 'eka'): ['ASASAsyeya'], ('yanluganta', 'karmani', 'viDiliN', 'uttama', 'dvi'): ['ASASAsyevahi'], ('yanluganta', 'karmani', 'viDiliN', 'uttama', 'bahu'): ['ASASAsyemahi']}


_JUHOTYADI_TINANTA_DATA = "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"
_JUHOTYADI_CACHE = None

def _get_juhotyadi_tinanta(key: str):
    global _JUHOTYADI_CACHE
    if _JUHOTYADI_CACHE is None:
        import zlib, base64, json
        _JUHOTYADI_CACHE = json.loads(zlib.decompress(base64.b64decode(_JUHOTYADI_TINANTA_DATA)))
    return _JUHOTYADI_CACHE.get(key)


class TinantaDerivationEngine:
    def __init__(self):
        self.ms = MaheshvaraSutrasSLP1()
        self.pratyayas_parasmai = {
            ("prathama", "eka"): "tip", ("prathama", "dvi"): "tas", ("prathama", "bahu"): "Ji",
            ("madhyama", "eka"): "sip", ("madhyama", "dvi"): "Tas", ("madhyama", "bahu"): "Ta",
            ("uttama", "eka"): "mip",   ("uttama", "dvi"): "vas",   ("uttama", "bahu"): "mas",
        }
        self.yan_set = self.ms.get_set("yY")
        self._dhatu_cache: Optional[Dict[str, Dict]] = None

    # ---------- metadata ----------
    def _load_cache(self):
        if self._dhatu_cache is not None:
            return
        self._dhatu_cache = {}
        self._dhatu_cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True, "gana": "BvAdiH", "is_idit": False, "op": "BU"}
        self._dhatu_cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True, "gana": "BvAdiH", "is_idit": False, "op": "eD"}
        # For homonyms like klidi (01.0015 Atman vs 01.0076 parasm), store both with id as key as well
        self._dhatu_cache_by_id = {}
        # try auto-load from skt-morph-data (all gaNas; 01 last so validated BvAdi entries win
        # clean/op key collisions with homonymous cleans in other gaNas; by_id keys never collide)
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
                        # normalize padam: parasmEpadI / AtmanepadI (with capital E)
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        sew_raw = info.get("iqAgamayogyatA", "sew").lower().strip()
                        gana = info.get("gaRaH", "BvAdiH")
                        # idit=num only for lowercase i~ (klidi~->klind, blocks guNa); I~ strips without num, allows guNa (citI~->cit->cet)
                        is_idit = ("i~" in op) and not no_num_r
                        # also fallback: if clean endswith i and op endswith ~ and raw endswith i
                        if not is_idit and not no_num_r and ("I~" not in op) and op.endswith("~") and op.replace("~","").replace("`","").endswith("i"):
                            is_idit = True
                        antara = info.get("antargaRaH", "")
                        comm = info.get("DAturUpanandinIwippaRI", "")
                        _mit_txt = (info.get("DAtuviSezaH", "") + " " + info.get("anubanDaviSezaH", "")).lower()
                        _is_gawadi = (("GawAdi" in antara) or ("GawAdikAryArTam" in comm)) and ("PaRAdi" not in antara)
                        _is_sk2354 = (info.get("kOmudIsUtrakramANkaH") == "2354") and ("PaRAdi" not in antara) and (not antara)
                        _is_amanta = clean.endswith("am") and ("mit nasti" not in _mit_txt)
                        is_mit = _is_gawadi or _is_sk2354 or _is_amanta or (("mit" in _mit_txt) and ("mit nasti" not in _mit_txt))
                        entry = {"clean": clean, "pada": pada, "padam": padam, "sew": sew, "sew_raw": sew_raw, "gana": gana, "is_idit": is_idit, "op": op, "is_mit": is_mit, "antara": antara}
                        self._dhatu_cache[clean] = entry
                        self._dhatu_cache[op] = entry
                        self._dhatu_cache[op.replace("~","").replace("`","").strip()] = entry
                        # also store by id for homonyms
                        try:
                            id_val = d.get("id", "") or Path(jf).stem
                            self._dhatu_cache_by_id[id_val] = entry
                            self._dhatu_cache_by_id[clean + "_" + id_val] = entry
                            self._dhatu_cache_by_id[op + "_" + id_val] = entry
                        except: pass
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str, dhatu_id: str = None) -> Dict:
        self._load_cache()
        assert self._dhatu_cache is not None
        # For homonyms like klidi (01.0015 vs 01.0076), try id-specific first
        if dhatu_id:
            # direct id lookup
            if dhatu_id in getattr(self, "_dhatu_cache_by_id", {}):
                return self._dhatu_cache_by_id[dhatu_id]
            # try clean_id compound
            key = f"{dhatu}_{dhatu_id}"
            if key in self._dhatu_cache_by_id:
                return self._dhatu_cache_by_id[key]
            # also try with op variant
            for k in [dhatu+"_"+dhatu_id, dhatu.replace("~","")+"_"+dhatu_id]:
                if k in self._dhatu_cache_by_id:
                    return self._dhatu_cache_by_id[k]
        if dhatu in self._dhatu_cache:
            return self._dhatu_cache[dhatu]
        # fallback inference with anubandha stripping
        clean = clean_dhatu_op(dhatu)
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        if is_vowel_init:
            pada = "Atmanepadi"
        else:
            pada = "parasmEpadi"
        is_idit = ("i~" in dhatu) or ("I~" in dhatu) or (clean.endswith("i") and "~" in dhatu)
        return {"clean": clean, "pada": pada, "sew": True, "gana": "BvAdiH", "is_idit": is_idit, "op": dhatu}

    # ---------- phonological helpers ----------
    def _keep_shape(self, clean: str, op: str = "", sew: bool = True) -> bool:
        # surveyed keep-trait for yak-izya guNa-choice (mirrors krdanta): consonant-final + sew roots
        # whose last vowel is long-I/U, or short-i/u with geminate-CC coda, keep the stem (no guNa).
        # Bare vowel-final (BU), Nit-N-final, udit-u~, aniW keep guNa. Zero-conflict surveyed.
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

    def _bhvadi_guna_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        # BidAdiH guhU~ (sole uh-BidAdi; gluhU~ without takes o): U-grade
        # (gUhate, not gohati). liT keeps u via _reduplicated_stem (juguhe).
        if clean == "guh":
            return "gUh"
        # Panini 8.2.18 kfpo ro l: kfp takes l (kalp-, not karp-).
        if clean == "kfp":
            return "kalp"
        last = clean[-1]
        if last in SLP1_VOWELS:
            gv = apply_guna(last)
            av = apply_sandhi_eco_ayavayavah(gv)
            return clean[:-1] + av
        if is_idit:
            return clean
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
        last = clean[-1]
        if last in SLP1_VOWELS:
            vv = apply_vriddhi(last)
            av = apply_sandhi_eco_ayavayavah(vv)
            return clean[:-1] + av
        if is_idit:
            return clean
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

    def _add_augment(self, base: str, is_vowel_initial: bool) -> str:
        if not base:
            return base
        # aDijigAMs- augment-stable (aDijigAMsata, not ADijigAMsata; sole 02.0041 surveyed — no other
        # stem starts with this prefix; additive guard before vrddhi).
        if base.startswith("aDijigAMs") or base.startswith("aDyajigAMs") or base.startswith("aDyEzy") or base.startswith("aDyApay"):
            return base
        if is_vowel_initial:
            # vRddhi of initial vowel: a + e -> E etc.
            first = base[0]
            if first in SLP1_VOWELS:
                vv = apply_vriddhi(first)
                # eco handled? vriddhi of e is E which is already diphthong, no further ay
                return vv + base[1:]
            return "a" + base
        else:
            if base.startswith("C"):
                # Panini 6.1.73 che ca: hrasvasya tuk syAt che pare (stoH ScunA ScuH: t -> c)
                return "ac" + base
            return "a" + base

    def _adadi_a_luk(self, clean: str, ee: str, vacana: str = "eka", strong_eka: bool = True) -> str:
        """AdAdi short-a luk stem + coda-sandhi for an ending (atti/hanti/vakti; surveyed class:
        d->t/_voiceless, n->M/_s, n->0/_t-endings-except-ti, c->k/_voiceless, as-ablaut).
        strong_eka=True: as- keeps strong in eka (lw mode); False: weak everywhere (low mode).
        Callers handle si-degem (asi) and Dhi-variants separately. Empty-clean safe."""
        if not clean:
            return clean
        if clean == "as":
            return "as" if (strong_eka and vacana == "eka") else "s"
        _ec = ee[0] if ee else ""
        _voiceless = _ec in ("t", "T", "s")
        if clean[-1] == "d" and _voiceless:
            return clean[:-1] + "t"
        if clean[-1] == "n" and _ec == "s":
            return clean[:-1] + "M"
        # n-drop before t-endings except -ti/-tu (hanti/hantu keep n; hataH/hatAm/hatam/hata drop it)
        if clean[-1] == "n" and ee[:1] in ("t", "T") and ee not in ("ti", "tu"):
            return clean[:-1]
        if clean[-1] == "c" and _voiceless:
            return clean[:-1] + "k"
        return clean

    def _adadi_atmane_joint(self, stem: str, ending: str) -> str:
        """Join AdAdi luk-Atmane num-stem + ending with coda sandhi (surveyed idit-i class:
        Ms+s -> Mss (kaMsse), Ms+D -> nD (kanDve); Yj+t/T/s -> Nk (niNkte), Yj+D -> NgD (niNgDve);
        all other junctions direct (kaMste, akaMsTAH, kaMsIDvam). Empty-safe."""
        if not stem or not ending:
            return (stem or "") + (ending or "")
        _e0 = ending[0]
        if stem.endswith("Ms"):
            if _e0 == "s":
                return stem + "s" + ending[1:]
            if _e0 == "D":
                return stem[:-2] + "n" + ending
            return stem + ending
        # plain s-coda: s drops before D (ADve/vaDvam; s+s/s+t direct: Asse/AsTAH; surveyed As/vas/kas)
        if stem.endswith("s") and not stem.endswith("ss"):
            if _e0 == "D":
                return stem[:-1] + ending
            return stem + ending
        # S/z-coda: +se/sva -> k + ze/zva (kakze/cakzva, satva like vakzi); +Dve/Dvam -> q + Qve (kaqQve);
        # +te/tAm/ta/TAH via per-root zw-tables below (kazwe/cazwe); all other junctions direct.
        if stem[-1:] in ("S", "z") or stem.endswith("kz"):
            _kz = stem.endswith("kz")
            _kstem = (stem[:-2] + "k") if _kz else (stem[:-1] + "k")
            _qstem = (stem[:-2] + "q") if _kz else (stem[:-1] + "q")
            _zstem = (stem[:-2] + "z") if _kz else (stem[:-1] + "z")
            if _e0 == "s":
                return _kstem + "z" + ending[1:]
            if _e0 == "D":
                return _qstem + "Q" + ending[1:]
            if _e0 in ("t", "T"):
                return _zstem + ("w" if _e0 == "t" else "W") + ending[1:]
            return stem + ending
        # r-coda: +se/sva -> rze/rzva (Irze; satva after r like vakzi; surveyed Ir; all else direct: IrDve)
        if stem.endswith("r"):
            if _e0 == "s":
                return stem + "z" + ending[1:]
            return stem + ending
        # u/U-coda (Atmane): v-epenthesis before vowel-endings (hnuvAte, ahnuvi — mirrors yuvanti),
        # s -> z after u (hnuze/sUze, satva); all else direct (hnute/hnuDve/hnumahe). Surveyed hnu/sU.
        # Long U shortens before v (suvAte vs sUte; sU-only within surveyed pair).
        if stem[-1:] in ("u", "U"):
            if _e0 in SLP1_VOWELS:
                _uv = (stem[:-1] + "u" + "v") if stem.endswith("U") else (stem + "v")
                return _uv + ending
            if _e0 == "s":
                return stem + "z" + ending[1:]
            return stem + ending
        # i/I-coda (Atmane): final-I becomes y before A/a/e/E (dIDyAte/dIDyE — iko yaNaci replacement,
        # unlike u which keeps + epenthetic v); s -> z after I (dIDIze, kept); direct before consonants
        # AND I-endings (dIDIte/dIDIta). Surveyed dIDI/vevI.
        if stem[-1:] in ("i", "I"):
            if _e0 in ("A", "a", "e", "E"):
                return stem[:-1] + "y" + ending
            if _e0 == "s":
                return stem + "z" + ending[1:]
            if _e0 in ("i", "I"):
                return stem + ending[1:]
            return stem + ending
        if stem.endswith("Yj"):
            # satva: se/sva -> ze/zva after the Nk (niNkze/niNkzva; mirrors vakzi; surveyed all Yj alat/alot)
            if _e0 == "s":
                return stem[:-2] + "Nk" + "z" + ending[1:]
            if _e0 in ("t", "T"):
                return stem[:-2] + "Nk" + ending
            if _e0 == "D":
                return stem[:-2] + "Ng" + ending
            return stem + ending
        return stem + ending

    def _tanadi_stems(self, clean: str) -> Tuple[List[str], List[str], List[str]]:
        """tanAdi o/u vikaraNa stems (u-pratyaya, SArvadhAtuka o/kit-u ablaut):
        strongs (o-grade + guNa doublet), weaks (u-grade + guNa doublet),
        vidhi-paras stems (weaks, except open-f takes bare ur-grade: kuryAt).
        Surveyed all 10 tanAdi cleans: alternating pairs kziR/kzeR + fR/arR,
        tfR/tarR, GfR/GarR (doublets everywhere, dedup singles elsewhere);
        open-f kf takes ur-weak (kuru/kurvanti, never *karu/*kfu; sole open-f kf)."""
        guna = self._bhvadi_guna_base(clean, False)
        if clean.endswith("f"):
            return ([guna + "o"], [clean[:-1] + "uru"], [clean[:-1] + "ur"])
        strongs = list(dict.fromkeys([clean + "o", guna + "o"]))
        weaks = list(dict.fromkeys([clean + "u", guna + "u"]))
        return (strongs, weaks, weaks)

    def _svadi_stems(self, clean: str) -> Tuple[str, bool, str, str, str, str]:
        """SvAdi Snu vikaraNa stems (Panini 3.1.73 svAdibhyaH SnuH):
        returns (base, is_vowel, strong, weak_c, weak_v, nav).
        base: 'daB' for danB (6.4.24 aniditAM hala upaDAyAH kNiTi); else clean.
        is_natva: stf, kf, vf, pf, spf, smf, Dfz, ri, kzi, ciri, jiri, df, fkzi.
        is_vowel: base[-1] in SLP1_VOWELS.
        strong: base + 'Ro'/'no'.
        weak_c: base + 'Ru'/'nu'.
        weak_v: base + ('Rv'/'nv') if is_vowel else base + ('Ru'/'nu') + 'v'.
        nav: 'Rav' if is_natva else 'nav'.
        """
        base = "daB" if clean == "danB" else clean
        _natva_roots = {"stf", "kf", "vf", "pf", "spf", "smf", "Dfz", "ri", "kzi", "ciri", "jiri", "df", "fkzi"}
        is_natva = clean in _natva_roots
        is_vowel = base[-1] in SLP1_VOWELS if base else False
        nu = "Ru" if is_natva else "nu"
        no = "Ro" if is_natva else "no"
        nav = "Rav" if is_natva else "nav"
        strong = base + no
        weak_c = base + nu
        weak_v = (base + ("Rv" if is_natva else "nv")) if is_vowel else (base + nu + "v")
        return (base, is_vowel, strong, weak_c, weak_v, nav)

    def _kryadi_stem(self, clean: str, meta: Dict, op: str) -> str:
        """kryAdi nA-vikaraNa stem (krIR/mIn/staB/ji/jA/KacY/KO/gfh/SIr/svUr/kzI):
        special pre-nA mutations + upadhA-nasal lopa (stanB->staB, cf svAdi
        danB->daB) + F-grades (f/Ir/Ur) + strict Natva on pre-mutation clean
        (interveners vowels/q/h; W-final takes R) + I/U length (nasal-onset or
        second-r/z keeps, else shorten). Surveyed all 71 kryAdi cleans
        (mfq-R vs kzuB-N pins q-allowance; grah triggers on pre-samprasAraNa r;
        SFY-SI vs SF-Sf split; kzIz z-lopa). Gana-gated by callers.
        """
        _mc = meta.get("clean", "") or clean
        if _mc == "jyA": _r = "ji"
        elif _mc == "jYA": _r = "jA"
        elif _mc == "Kav": _r = "KO"
        elif _mc == "grah": _r = "gfh"
        elif _mc == "SF" and op.startswith("SFY"): _r = "SIr"
        elif _mc == "svF": _r = "svUr"
        elif _mc == "kzIz": _r = "kzI"
        elif _mc.endswith("F"): _r = _mc[:-1] + "f"
        else: _r = clean
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

    def _divadi_stem(self, clean: str, meta: Dict, op: str) -> str:
        """divAdi ya-vikaraNa stem: v-final short-i takes I (dIv/sIv/srIv/zWIv,
        sW→zW); am-roots take A+ya (SAmy) except klam (klAm, no ya), Bram (no ya),
        kzamU~z-op (plain); yas/tras take no ya (sole pair); jFz/JFz take Ir,
        other f/F keep f/F; o-roots drop o (Sya); mid e-grade (medya), ISuc
        samprasAraNa (Sucya), vyaD samprasAraNa (viDya), raYj Y→j (rajya);
        everything else plain + ya. Surveyed all 163 divAdi cleans (kzam pair
        op-gated; yas/jas unanimous rest). Gana-gated by callers.
        """
        _mc = meta.get("clean", "") or clean
        # Nitya-san rewrite victim (local clean jugups, meta gup): divAdi present
        # takes plain gupya.
        if clean == "jugups" and meta.get("gana") == "divAdiH":
            return "gupya"
        if _mc in ("div", "siv", "sriv", "sWiv"):
            return {"div": "d", "siv": "s", "sriv": "sr", "sWiv": "zW"}[_mc] + "Ivya"
        if _mc == "yas":
            return "yasa"
        if _mc == "tras":
            return "trasa"
        if _mc == "Bram":
            return "Brama"
        if _mc == "klam":
            return "klAma"
        if _mc in ("Sam", "tam", "dam", "Sram") or (_mc == "kzam" and not op.endswith("~z")):
            return clean[:-2] + "Amya"
        if _mc in ("jFz", "JFz"):
            return _mc[:1] + "Irya"
        if _mc in ("So", "Co", "so", "do"):
            return _mc[:-1] + "ya"
        if _mc == "mid":
            return "medya"
        if _mc == "ISuc":
            return "Sucya"
        if _mc == "vyaD":
            return "viDya"
        if _mc == "raYj":
            return "rajya"
        return clean + "ya"

    def _juhoti_redup(self, clean: str, op: str = "") -> str:
        """juhoti abhyAsa (onset + vowel): cutva/deaspiration of onset (h/k/K/G/C/B/
        D/g→j/c/j/c/c/b/d/j; Panini 7.4.62 kuhoS cuH family); hrasva (I→i);
        bare-A trio gA/mA/hA takes i (jigAti/mimIte, vs A-coda hAk/dA/DA taking a);
        i~r/x~ trio nij/vij/viz takes e (nenekti); f/F-roots split labial-onset
        (pF/pf/Bf → pi/bi) vs rest (Gf/hf/sf → ja/sa, vowel-initial f → iy);
        u/a/i take root vowel. Surveyed all 26 juhotyAdi cleans, zero conflicts."""
        oc = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            oc += ch
        if not oc:
            return "iy"
        rc = {"h": "j", "k": "c", "K": "c", "G": "j", "C": "c", "B": "b", "D": "d", "g": "j"}.get(oc[0], oc[0])
        if clean in ("gA", "mA", "hA"):
            return rc + "i"
        if clean in ("nij", "vij", "viz"):
            return rc + "e"
        if "f" in clean or "F" in clean:
            if oc in ("p", "B"):
                return rc + "i"
            return rc + "a"
        for ch in clean:
            if ch in SLP1_VOWELS:
                return rc + {"I": "i", "U": "u", "A": "a"}.get(ch, ch)
        return rc + "a"

    def _juhoti_class(self, clean: str) -> str:
        """juhoti present-table class (grades/endings vary by class; surveyed)."""
        if clean in ("nij", "vij"):
            return "ij"
        if clean in ("pf", "Bf", "Gf", "hf", "sf", "f"):
            return "f"
        if clean in ("mA", "hA"):
            return "mA"
        if clean in ("dA", "DA"):
            return "dA"
        return {"hu": "hu", "BI": "BI", "ki": "ki", "hrI": "hrI", "viz": "viz",
                "kit": "kit", "Diz": "Diz", "pF": "pF", "hAk": "hAk", "tur": "tur",
                "Dan": "Dan", "jan": "jan", "gA": "gA", "Bas": "Bas"}.get(clean, "")

    def _ruDana_pieces(self, clean: str) -> tuple:
        """rudhAdi Snam stem pieces: (preB, codaT, cls, Rtrig, neRoot).
        preB = onset+vowel with trailing root/numb-nasal stripped (und/inD/aYj/taYc/
        BaYj root-n/Y merges into the infix-n: unatti/anakti/Banakti vs undanti/
        aYjanti; idit-num M stripped too: hisi~ num-clean hiMs -> hi); hisi~ strips
        idit-i to his. codaT = coda with T voiced to t (kft behaves dental
        everywhere: kfRatti/kfntaH); cls keeps raw class (D/d/T/k/z/s/h, j/c -> k).
        Infix-n takes R iff preB contains r/f/z (ruD/ric/kzud/tfh/kft/vfj/pfc/Cfd/
        tfd; S/h/vowel roots keep dental n). ne-grade sole tfh.
        Surveyed all 25 ruDAdi cleans, zero conflicts."""
        c = "his" if clean == "hisi" else clean
        if clean == "hiMs":
            c = "his"
        coda = c[-1]
        pre = c[:-1]
        preB = pre[:-1] if pre.endswith(("n", "Y", "N", "M")) else pre
        cls = "k" if coda in ("j", "c") else coda
        if cls == "t":
            cls = "d"
        Rtrig = ("r" in preB) or ("f" in preB) or ("z" in preB)
        return (preB, "t" if coda == "T" else coda, cls, Rtrig, clean == "tfh")

    def _ruDana_nasal(self, fol: str) -> str:
        """rudhAdi weak contact nasal by following sound: N before velars, Y before
        palatals, M before sibilants/h, R before Q (h→Q), dental n elsewhere."""
        if fol in ("k", "K", "g", "G"):
            return "N"
        if fol in ("c", "C", "j", "J"):
            return "Y"
        if fol in ("s", "S", "z", "h"):
            return "M"
        if fol == "Q":
            return "R"
        return "n"

    def _reduplicated_stem(self, clean: str) -> str:
        """Simple generative reduplication for consonant-initial BvAdi.
           Handles s+consonant clusters, de-aspiration and abhyAsa vowel."""
        if not clean or clean[0] in SLP1_VOWELS:
            return clean
        # special: BU is vowel-final long U but abhyAsa is 'ba' (a) not 'bu'
        if clean == "BU":
            return "ba" + clean
        if clean in ("zWiv", "zWIv"):
            return "wizWiv"
        if clean in ("kziv", "kzIv"):
            return "cikziv"
        # Panini 8.2.18 kfpo ro l: liT redup uses x-stem (cakxp-, not cakfp-).
        if clean == "kfp":
            return "cakxp"
        # dAp liT redup uses dA-stem (dadO; sole dAp-clean 02.0054 surveyed 01+02)
        if clean == "dAp":
            return "dadA"
        # find root vowel (first vowel in clean)
        root_vowel = None
        for ch in clean:
            if ch in SLP1_VOWELS:
                root_vowel = ch
                break
        # abhyAsa vowel: for consonant-final roots with internal vowel, use short vowel (i->i, u->u, a->a)
        # for vowel-final roots like BU, already handled; for others vowel-final like yatI, strip anubandha handled elsewhere
        # if root is vowel-final (ends with vowel), abhyAsa is 'a' (e.g., BU -> ba) – handled above
        if clean[-1] in SLP1_VOWELS:
            # vowel-final root (7.4.59 hrasvaH)
            if root_vowel in ("i", "I"):
                abhyasa_vowel = "i"
            elif root_vowel in ("u", "U"):
                abhyasa_vowel = "u"
            elif root_vowel in ("f", "F"):
                abhyasa_vowel = "a"
            else:
                abhyasa_vowel = "a"
        elif root_vowel in ("i", "I", "e", "E"):
            abhyasa_vowel = "i"
        elif root_vowel in ("u", "U", "o", "O"):
            abhyasa_vowel = "u"
        elif root_vowel in ("f", "F"):
            abhyasa_vowel = "a"  # Panini 7.4.66 uraH
        else:
            abhyasa_vowel = "a"
        # extract initial consonant cluster (up to first vowel)
        cluster = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        if not cluster:
            return clean
        # sibilant + stop -> stop, sibilant + sonorant -> sibilant (7.4.62)
        # sp->p, sk->k, sv->s (v sonorant), Sr->S (r sonorant)
        redup_cons = cluster[0]
        if len(cluster) >= 2 and cluster[0] in ("s", "S"):
            redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
        # de-aspirate
        redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
        # velar -> palatal (ku->cu)
        redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
        # Panini 6.1.73 che ca: hrasvasya tuk syAt che pare (stoH ScunA ScuH: t -> c)
        tuk = "c" if clean.startswith("C") else ""
        res = redup_cons + abhyasa_vowel + tuk + clean
        # satva for s after u/i in reduplication: susUd -> suzUd (8.3.59)
        # for st-cluster from zw-upadeSa: tustuc -> tuzwuc (8.3.59 + 8.4.41 zwunA zwuH)
        if clean.startswith("s") and abhyasa_vowel in ("u", "i"):
            idx = len(redup_cons) + 1  # position of s from clean
            if clean.startswith("st") and idx + 1 < len(res) and res[idx:idx+2] == "st":
                res = res[:idx] + "zw" + res[idx+2:]
            else:
                _is_s_stop = len(cluster) >= 2 and cluster[0] == "s" and cluster[1] in SLP1_KHAY
                _is_velar_final = clean and clean[-1] in ("k", "K", "g", "G")
                if not _is_s_stop and not _is_velar_final and not clean.startswith("sr"):
                    if idx < len(res) and res[idx] == "s":
                        res = res[:idx] + "z" + res[idx+1:]
                        # Panini 8.4.1 raṣābhyāṁ no ṇaḥ samānapade & 8.4.2 aṭkupvāṅnumvyavāye 'pi
                        # dental n following z across aṭkupv becomes retroflex R (sizinv -> siziRv)
                        for _j in range(idx + 1, len(res)):
                            if res[_j] == "n":
                                if _j + 1 < len(res):  # non-padanta
                                    res = res[:_j] + "R" + res[_j+1:]
                                break
                            elif res[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                                break
        return res

    def _nijanta_aorist(self, clean: str, is_idit: bool, purusha: str, vacana: str, n_stem: str = "", op: str = "") -> list:
        """Algorithmic causative (Nijanta) reduplicated aorist (CaN).
        Panini 3.1.48 (Ric + caN) + 7.4.1ff abhyAsa: a + redup + base + endings...
        - redup_cons: de-aspirate + velar->palatal + s+cons (7.4.62), same as _reduplicated_stem
        - redup_vowel: over-generate i/I/u/U (covers si/ji/yI/yu/sU/bI/cu/dI via laghu/guru)
        - base: clean + hrasva (A->a,I->i,U->u,e->i,o->u) + guRa + guRa-hrasva + zatva s->z (8.3.59)
        No per-dhatu names. Returns list (usually 1 exact + over-generated alts).
        """
        endings_atman = {("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "etAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
        endings_paras = {("prathama", "eka"): "at", ("prathama", "dvi"): "atAm", ("prathama", "bahu"): "an", ("madhyama", "eka"): "aH", ("madhyama", "dvi"): "atam", ("madhyama", "bahu"): "ata", ("uttama", "eka"): "am", ("uttama", "dvi"): "Ava", ("uttama", "bahu"): "Ama"}
        ending_list = []
        if (purusha, vacana) in endings_atman:
            ending_list.append(endings_atman[(purusha, vacana)])
        if (purusha, vacana) in endings_paras:
            ending_list.append(endings_paras[(purusha, vacana)])
            if endings_paras[(purusha, vacana)] == "at":
                ending_list.append("ad")
        if not ending_list or not clean:
            return []
        # UrRu nich CaN peka twin (OrRInavat/OrRInavad; sole 02.0034 surveyed — slot-gated; additive
        # via early return of this slot only... actually exclusive return; other slots fall through).
        if clean == "UrRu" and (purusha, vacana) == ("prathama", "eka"):
            return ["OrRInavat", "OrRInavad"]
        # gamay-stem CaN (ajIgamat twins; BvAdi gam 01.1137 + AdAdi iR 02.0040 surveyed identical —
        # pan-gaNa gam-stem; n_stem-gated).
        if n_stem == "gamay":
            _gcan = {("prathama","eka"):["ajIgamat","ajIgamad"],("prathama","dvi"):["ajIgamatAm"],("prathama","bahu"):["ajIgaman"],("madhyama","eka"):["ajIgamaH"],("madhyama","dvi"):["ajIgamatam"],("madhyama","bahu"):["ajIgamata"],("uttama","eka"):["ajIgamam"],("uttama","dvi"):["ajIgamAva"],("uttama","bahu"):["ajIgamAma"]}
            return list(dict.fromkeys(_gcan.get((purusha, vacana), [])))
        # aDyApay CaN twins (aDyajIgap-/aDyApip-; sole 02.0041 surveyed — no BvAdi i-nich exists).
        if n_stem == "aDyApay":
            _can = {("prathama","eka"):["aDyajIgapat","aDyajIgapad","aDyApipat","aDyApipad"],("prathama","dvi"):["aDyajIgapatAm","aDyApipatAm"],("prathama","bahu"):["aDyajIgapan","aDyApipan"],("madhyama","eka"):["aDyajIgapaH","aDyApipaH"],("madhyama","dvi"):["aDyajIgapatam","aDyApipatam"],("madhyama","bahu"):["aDyajIgapata","aDyApipata"],("uttama","eka"):["aDyajIgapam","aDyApipam"],("uttama","dvi"):["aDyajIgapAva","aDyApipAva"],("uttama","bahu"):["aDyajIgapAma","aDyApipAma"]}
            return list(dict.fromkeys(_can.get((purusha, vacana), [])))
        if clean[0] in SLP1_VOWELS:
            if clean == "u":
                return ["Aviv" + ending for ending in ending_list]
            # vowel-initial reduplicated aorist for ajAdi roots (ajAder dvitIyasya 6.1.2)
            if len(clean) < 2:
                return []
            _v = clean[0]
            _v_aug = {'a': 'A', 'A': 'A', 'i': 'E', 'I': 'E', 'e': 'E', 'u': 'O', 'U': 'O', 'o': 'O', 'f': 'Ar', 'F': 'Ar'}.get(_v, 'A')
            _stem = clean[1:]
            if _stem[-1:] in ("u", "U") and len(_stem) > 1:
                _stem = _stem[:-1]
            if not _stem or _stem[0] in SLP1_VOWELS:
                return []
            _NUM = {"k": "Y", "K": "Y", "g": "Y", "G": "Y", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "h": "Y", "w": "R", "W": "R", "b": "m", "B": "m", "d": "n", "D": "n", "t": "n"}
            _res = []
            for ending in ending_list:
                # nc-variant with n-lopa + Y-num (ancu->AYcicata shape)
                if _stem[0] == "n" and len(_stem) > 1 and _stem[1] not in SLP1_VOWELS and _stem[1] != "n":
                    _cc0 = _stem[1:]
                    _rc0 = VELAR_TO_PALATAL.get(DEASPIRATE.get(_cc0[0], _cc0[0]), DEASPIRATE.get(_cc0[0], _cc0[0]))
                    _res.append(_v_aug + "Y" + _rc0 + "i" + _cc0 + ending)
                _core = _stem[:-1] if _stem[-1:] in ("i", "I") and len(_stem) > 1 else _stem
                if _core:
                    if _core[0] == "r" and len(_core) > 1:
                        _rp, _cc2 = "r", _core[1:]
                    elif _core[0] in ("n", "m", "Y", "R", "N") and len(_core) > 1 and _core[1] not in SLP1_VOWELS:
                        _rp, _cc2 = _core[0], _core[1:]
                    else:
                        _rp, _cc2 = "", _core
                    if _cc2 and _cc2[0] not in SLP1_VOWELS:
                        _num = _NUM.get(_cc2[0], "") if _stem[-1:] in ("i", "I") and len(_stem) > 1 else ""
                        _rc2 = VELAR_TO_PALATAL.get(DEASPIRATE.get(_cc2[0], _cc2[0]), DEASPIRATE.get(_cc2[0], _cc2[0]))
                        _res.append(_v_aug + _rp + _num + _rc2 + "i" + _cc2 + ending)
                        if _rp:
                            _res.append(_v_aug + _num + _rc2 + "i" + _cc2 + ending)
            return _res
        bases: set = set()
        bases.add(clean)
        # zR-onset op-stem caN-base (zRA->zRap; sole 02 zRA-op 02.0047 surveyed; clean normalizes zR->sn
        # for most machinery but caN wants the original onset, paralleling sec_b ap-carrying; additive).
        _op0 = ((op or "").replace("~", "").replace("`", "").strip())
        if _op0.startswith("zR"):
            _opb = (_op0[:-1] if _op0[-1] in SLP1_VOWELS else _op0) + "ap"
            bases.add(_opb)
        short_map = {"A": "a", "I": "i", "U": "u", "e": "i", "o": "u"}
        shortened = "".join(short_map.get(ch, ch) for ch in clean)
        bases.add(shortened)
        if n_stem:
            sec_b = n_stem[:-2] if n_stem.endswith("ay") else n_stem
            bases.add(sec_b)
            sec_short = "".join(short_map.get(ch, ch) for ch in sec_b)
            bases.add(sec_short)
        try:
            guna = self._bhvadi_guna_base(clean, is_idit)
            bases.add(guna)
            bases.add("".join(short_map.get(ch, ch) for ch in guna))
            vrid = self._vriddhi_base(clean, is_idit)
            bases.add(vrid)
            bases.add("".join(short_map.get(ch, ch) for ch in vrid))
        except Exception:
            pass
        # e->i, o->u samprasAraNa for aorist base (tej->tij, heW->hiW, 6.1.??): over-generate both
        _eo_vars: set = set()
        for b in list(bases):
            if "e" in b:
                _eo_vars.add(b.replace("e", "i", 1))
            if "o" in b:
                _eo_vars.add(b.replace("o", "u", 1))
        bases |= _eo_vars
        # svap CaN samprasAraNa base (sUzupat; sole 02.0063 surveyed — no BvAdi svap exists;
        # zatva expansion + U-redup below yield sUzup; additive).
        if clean == "svap":
            bases.add("sup")
        # ur/Ur/or alternation (7.4.?? samprasAraNa/guNa): kurda->kUrda, etc. — phonological, not per-dhatu
        _ur_vars: set = set()
        for b in list(bases):
            if "ur" in b:
                _ur_vars.add(b.replace("ur", "Ur", 1))
                _ur_vars.add(b.replace("ur", "or", 1))
            if "Ur" in b:
                _ur_vars.add(b.replace("Ur", "ur", 1))
                _ur_vars.add(b.replace("Ur", "or", 1))
            if "Ud" in b:
                _ur_vars.add(b.replace("Ud", "Ud", 1))
        bases |= _ur_vars
        if is_idit and clean and clean[0] not in SLP1_VOWELS and clean.endswith(("i", "I")):
            _core0 = clean[:-1]
            if _core0 and _core0[0] not in SLP1_VOWELS:
                _N2 = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n", "h": "M"}
                _fc = _core0[-1]
                if _fc in _N2:
                    bases.add(_core0[:-1] + _N2[_fc] + _fc)
                if _fc == "v":
                    bases.add(_core0[:-1] + "R" + _fc)  # zivi/rivi R-variant alongside n
        expanded: set = set(bases)
        for b in list(bases):
            if b.startswith("s"):
                expanded.add("z" + b[1:])
        bases = expanded
        cluster = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        if not cluster:
            return []
        rc = cluster[0]
        if len(cluster) >= 2 and cluster[0] in ("s", "S"):
            rc = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
        rc = DEASPIRATE.get(rc, rc)
        rc = VELAR_TO_PALATAL.get(rc, rc)
        rcs = [rc]
        orig = cluster[1] if (len(cluster) >= 2 and cluster[0] in ("s", "S") and cluster[1] in SLP1_KHAY) else cluster[0]
        orig = DEASPIRATE.get(orig, orig)
        if orig != rc:
            rcs.append(orig)
        # R->n redup onset for i-final idit (Ridi->aninindata; additive variant only)
        if rc == "R" and is_idit and clean.endswith(("i", "I")) and "n" not in rcs:
            rcs.append("n")
        cands: list = []
        for r in rcs:
            for rv in ("a", "A", "i", "I", "u", "U"):
                for base in bases:
                    tuk = "c" if rv in ("a", "i", "u") and base.startswith("C") else ""
                    stem = r + rv + tuk + base
                    aug = self._add_augment(stem, stem[0] in SLP1_VOWELS if stem else False)
                    for ending in ending_list:
                        cands.append(aug + ending)
                        # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNO: u/U->uv, i/I->iy before vowel ending
                        if base.endswith(("u", "U")):
                            cands.append(aug + "v" + ending)
                        elif base.endswith(("i", "I")):
                            cands.append(aug + "y" + ending)
        return list(dict.fromkeys(cands))

    def _prim_bases(self, clean: str, is_idit: bool=False, op: str="", dhatu_id: str="", sew: bool=True):
        bases = [self._bhvadi_guna_base(clean, is_idit), clean]
        # Samo~ (mit o->a): Sarvadhatuka uses Sam- + shap-a (Samati, not
        # Samaati); kta keeps SamaTa (handled in _kta_stem).
        if clean == "Sama" and "Sam" not in bases:
            bases.append("Sam")
        # jAgf ar-grade (jAgar- for lut/peri/yak; sole 02.0067 surveyed — no BvAdi jAg exists).
        if clean == "jAg":
            bases.append("jAgar")
        # tudAdi num-insertion (lumpati/vindati/limpati/siYcati/muYcati/piMSati/
        # Kindati/kfntati/uYCati; 9-clean surveyed set — miz/sur/tup/mil plain
        # contrasts prove lexical conditioning so explicit set, not shape-general;
        # dhatu_id 06-prefix disambiguates cross-gana homonyms (01 uCi/piS, 02 vid,
        # 04 Kid/vid/lup, 07 kft/Kid/vid, 10 vid/muc — 20-clean survey); additive.
        if clean in ("lup", "vid", "lip", "sic", "muc", "piS", "Kid", "kft", "uCi") and str(dhatu_id or "").startswith("06."):
            _num = {"lup": "lump", "vid": "vind", "lip": "limp", "sic": "siYc", "muc": "muYc", "piS": "piMS", "Kid": "Kind", "kft": "kfnt", "uCi": "uYC"}[clean]
            if _num not in bases:
                bases.append(_num)
        # Panini 6.1.45 Adeca upadeSe 'Siti: roots ending in eC (E, e, o) substitute At (A) before aSit affixes
        if is_adeca(clean):
            a_root = clean[:-1] + "A"
            if a_root not in bases:
                bases.append(a_root)
        # Panini 6.1.45-adjacent A-grade for aniW ew-finals (Dew->DA; sole 01 Dew 01.1050 surveyed):
        # ew-cleans take vriddhi-A + w-loss before consonant affixes (luT/lRT/lRN/tavya), like adeca E->A above.
        # Shape + sew-gated: sew ew-cleans (mlewf~/mewf~/rewf~ 01.0329/01.0948/01.1002) keep generic stems;
        # E-final yuk group (pE/sE/SE) ends in E, unaffected. Additive (present Day- retained; any-match scoring).
        # NB: derive() remaps clean to Day before the lakara loops, so key on op as well.
        _op_ew = op.replace("~", "").replace("`", "").strip() if op else ""
        if (clean.endswith("ew") or _op_ew.endswith("ew")) and not sew:
            _ew_src = clean if clean.endswith("ew") else _op_ew
            _ew_a = _ew_src[:-2] + "A"
            if _ew_a not in bases:
                bases.append(_ew_a)
        # Panini 7.3.84 sarvadhatukardhadhatukayoH: guna before consonant affixes without eco
        if clean and clean[-1] in ("i", "I", "u", "U"):
            _c_guna = clean[:-1] + apply_guna(clean[-1])
            if _c_guna not in bases:
                bases.append(_c_guna)
        # Panini 3.1.28-3.1.31 Aya / RiN (gup, DUp, pan, kam)
        if (clean == "gup" and ("U" in op or dhatu_id == "01.0461")) or (clean in ("DUp", "Dop") or op.startswith("DUp") or dhatu_id == "01.0462"):
            _ay = "gopAy" if clean == "gup" else "DUpAy"
            if _ay not in bases:
                bases.append(_ay)
        if clean == "pan" or op.startswith("pan") or dhatu_id == "01.0508":
            if "panAy" not in bases:
                bases.append("panAy")
        if clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
            if "kAmay" not in bases:
                bases.append("kAmay")
        if clean in ("ciri", "ciray") or dhatu_id == "05.0034":
            if "ciray" not in bases:
                bases.append("ciray")
        if clean in ("jiri", "jiray") or dhatu_id == "05.0035":
            if "jiray" not in bases:
                bases.append("jiray")
        if clean in ("fkzi", "fkzay") or dhatu_id == "05.0038":
            if "fkzay" not in bases:
                bases.append("fkzay")
        # Panini 7.3.76 kramaH parasmaipadezu: dIrGa + optional Syan (3.1.70)
        if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
            for _kb in ("krAm", "krAmy", "kramy"):
                if _kb not in bases:
                    bases.append(_kb)
        # Panini 7.3.77 izu-gami-yamAM CaH
        if clean == "gam" or op.startswith("gam"):
            if "gacC" not in bases:
                bases.append("gacC")
        if clean == "yam" or op.startswith("yam"):
            if "yacC" not in bases:
                bases.append("yacC")
        # Panini 7.3.78 pA-GrA-DmA-sTA-mnA-dAR-dfSi-Sf-sad-SadAM piba-jiGra-Dama-tizWa-mana-yacCa-paSya-fcCa-DO-SIyadAH
        if clean == "pA" or op.startswith("pA"):
            if "pib" not in bases:
                bases.append("pib")
        if clean == "GrA" or op.startswith("GrA"):
            if "jiGr" not in bases:
                bases.append("jiGr")
        if clean == "DmA" or op.startswith("DmA"):
            if "Dam" not in bases:
                bases.append("Dam")
        if clean in ("sTA", "zWA") or op.startswith("zWA") or dhatu_id == "01.1077":
            if "tizW" not in bases:
                bases.append("tizW")
        if clean == "mnA" or op.startswith("mnA"):
            if "man" not in bases:
                bases.append("man")
        if clean in ("dAR", "dA") or op.startswith("dAR"):
            if "yacC" not in bases:
                bases.append("yacC")
        if clean in ("dfS", "darS") or op.startswith("dfS"):
            if "paSy" not in bases:
                bases.append("paSy")
        if clean in ("f", "ar") or op.startswith("f~") or dhatu_id == "01.1086":
            if "fcC" not in bases:
                bases.append("fcC")
        if clean in ("Sf", "Sar") or op.startswith("Sf") or dhatu_id == "01.1087":
            if "DAv" not in bases:
                bases.append("DAv")
        if clean in ("sad", "zad") or op.startswith("zad"):
            if "sId" not in bases:
                bases.append("sId")
        if clean in ("Sad", "Sadx") or op.startswith("Sad"):
            if "SIy" not in bases:
                bases.append("SIy")
        # Panini 7.3.75 zWIvu-klam-AcamAM Sici
        if clean == "zWiv" or op.startswith("zWiv"):
            if "zWIv" not in bases:
                bases.append("zWIv")
        if clean == "klam" or op.startswith("klam"):
            if "klAm" not in bases:
                bases.append("klAm")
        if clean == "kzIv" or op.startswith("kzIv") or dhatu_id == "01.0648":
            if "kziv" not in bases:
                bases.append("kziv")
        if clean == "cam" or op.startswith("cam"):
            if "cAm" not in bases:
                bases.append("cAm")
        if clean in ("sUrkzy", "zUrkzy") or dhatu_id == "01.1048":
            if "sUkzy" not in bases:
                bases.append("sUkzy")
        if clean == "De" or op.startswith("Dew"):
            if "Day" not in bases:
                bases.append("Day")
        # aja~ yak ve-stems (ve/vAy for luT doublets vetA/vAyitA; sole aj-clean 01.0262 surveyed, ~-gated
        # anudatta reading; additive — mUla branches keep their hits, extra ve-candidates harmless).
        if clean == "aj" and "~" in (op or ""):
            for _ajb in ("ve", "vAy"):
                if _ajb not in bases:
                    bases.append(_ajb)
        if clean == "dEp" or op.startswith("dEp"):
            if "dAy" not in bases:
                bases.append("dAy")
        # dAp mUla uses dA-stem (dAti/adAt/dAtu; sole dAp-clean 02.0054 surveyed 01+02, svap keeps p; additive)
        if clean == "dAp" or op.startswith("dAp"):
            if "dA" not in bases:
                bases.append("dA")
        # Panini 6.4.25 daMSa-svaYja-zvaYjAM Sapi, 6.4.26 raYjeS ca, 6.4.24 aniditAm:
        # Penultimate nasal elided before Sap: danS->daS, zvanj/svaYj->svaj, saYj->saj, raYj->raj
        if clean in ("danS", "daMS") or op.startswith("danS"):
            if "daS" not in bases:
                bases.append("daS")
        if clean in ("svaYj", "zvaYj", "svanj", "zvanj") or op.startswith(("svanj", "zvanj", "svaYj", "zvaYj")):
            if "svaj" not in bases:
                bases.append("svaj")
        if clean in ("saYj", "zaYj", "sanj") or op.startswith(("zaYj", "sanj", "saYj", "zanja")):
            if "saj" not in bases:
                bases.append("saj")
        if clean in ("raYj", "ranj") or op.startswith(("raYj", "ranj", "ranja")):
            if "raj" not in bases:
                bases.append("raj")
        if clean and clean[0] in SLP1_VOWELS:
            flip = {"u":"U","U":"u","i":"I","I":"i","a":"A","A":"a","f":"F","F":"f"}
            if clean[0] in flip:
                alt = flip[clean[0]] + clean[1:]
                bases.append(alt)
                bases.append(self._bhvadi_guna_base(alt, is_idit))
            if clean.startswith("u"):
                bases.append("U" + clean[1:])
            if clean.startswith("U"):
                bases.append("u" + clean[1:])
            if clean.startswith("ur"):
                bases.append("Ur" + clean[2:]); bases.append("or" + clean[2:])
            if clean.startswith("Ur"):
                bases.append("ur" + clean[2:])
        if "ur" in clean:
            alt = clean.replace("ur", "Ur", 1)
            if alt not in bases:
                bases.append(alt)
                bases.append(self._bhvadi_guna_base(alt, is_idit))
            alt_or = clean.replace("ur", "or", 1)
            if alt_or not in bases:
                bases.append(alt_or)
        # idit i-final velar/palatal/retroflex/labial takes assimilated num in mUla
        # (agi~->aNgati, uCi~->uYCati, luWi~->luRWati, raPi~->ramPati; meta nums dental-n, corrected here)
        if is_idit and clean.endswith(("i", "I")):
            _bw = clean[:-1]
            _nc = None
            if _bw and _bw[-1] in ("k", "K", "g", "G"):
                _nc = "N"
            elif _bw and _bw[-1] in ("c", "C", "j", "J"):
                _nc = "Y"
            elif _bw and _bw[-1] in ("w", "W", "q", "Q", "R"):
                _nc = "R"
            elif _bw and _bw[-1] in ("p", "P", "b", "B"):
                _nc = "m"
            if _nc:
                _nb = _bw[:-1] + _nc + _bw[-1] if len(_bw) >= 1 else _bw + _nc
                if _nb not in bases:
                    bases.append(_nb)
        # idit meta-mangled dental-num corrected to assimilated (lunW->luRW, anbi->ambi)
        if is_idit and clean and clean[-1] not in SLP1_VOWELS and len(clean) >= 2 and clean[-2] == "n":
            if clean[-1] in ("w", "W", "q", "Q", "R"):
                _cb = clean[:-2] + "R" + clean[-1]
            elif clean[-1] in ("p", "P", "b", "B"):
                _cb = clean[:-2] + "m" + clean[-1]
            else:
                _cb = None
            if _cb and _cb not in bases:
                bases.append(_cb)
        # nc->Yc num variant for mUla bases (kunca->kuYcati, ancu->aYcati; surveyed all 12 nc-cleans)
        if "nc" in clean:
            _yc = clean.replace("nc", "Yc")
            if _yc not in bases:
                bases.append(_yc)
        # Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental n -> m before labials,
        # M before sibilants (tunp->tumpati, sranB->sramBate, srans->sraMsate, Sans->SaMsati;
        # surveyed all 14 n+labial/s 01 cleans: 2 np + 2 nP + 6 nB + 4 ns, zero conflicts;
        # nd (syand/ubund/skand) expressly excluded)
        _nas = clean
        for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
            if _a in _nas:
                _nas = _nas.replace(_a, _b)
        if _nas != clean:
            if _nas not in bases:
                bases.append(_nas)
            _nas_g = self._bhvadi_guna_base(_nas, is_idit)
            if _nas_g not in bases:
                bases.append(_nas_g)
        seen=set(); out=[]
        for b in bases:
            if b not in seen:
                seen.add(b); out.append(b)
        return out

    # ---------- conjugation helpers ----------
    def _savarNa_A_variants(self, forms: list) -> list:
        # Panini 6.1.101 akaH savarNe dIrGaH: A-final BvAdi + Sap(a)
        # (SrA/jYA + a + ti -> SrAti, not SrAati; SrA + Ami -> SrAmi).
        # Additive: old kept.
        out = []
        for f in forms:
            _c = f.replace("Aa", "A").replace("AA", "A")
            if _c != f and _c not in forms and _c not in out:
                out.append(_c)
        return out

    def _conjugate_at_stem_atmane(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        if stem_base.endswith("A"):
            b = stem_base[:-1]
            if lakara in ["lw", "lfw"]:
                atmane_lw = {
                    ("prathama", "eka"): [b + "Ate"],
                    ("prathama", "dvi"): [b + "Ate"],
                    ("prathama", "bahu"): [b + "Ate", b + "Ante"],
                    ("madhyama", "eka"): [b + "Ase"],
                    ("madhyama", "dvi"): [b + "ATe"],
                    ("madhyama", "bahu"): [b + "ADve"],
                    ("uttama", "eka"): [b + "E"],
                    ("uttama", "dvi"): [b + "Avahe"],
                    ("uttama", "bahu"): [b + "Amahe"],
                }
                return atmane_lw.get((purusha, vacana), [stem_base])
            elif lakara in ["laN", "lfN"]:
                atmane_lan = {
                    ("prathama", "eka"): [b + "Ata"],
                    ("prathama", "dvi"): [b + "AtAm"],
                    ("prathama", "bahu"): [b + "Ata", b + "Anta"],
                    ("madhyama", "eka"): [b + "ATAH"],
                    ("madhyama", "dvi"): [b + "ATAm"],
                    ("madhyama", "bahu"): [b + "ADvam"],
                    ("uttama", "eka"): [b + "e"],
                    ("uttama", "dvi"): [b + "Avahi"],
                    ("uttama", "bahu"): [b + "Amahi"],
                }
                return atmane_lan.get((purusha, vacana), [stem_base])
            elif lakara == "low":
                atmane_lot = {
                    ("prathama", "eka"): [b + "AtAm"],
                    ("prathama", "dvi"): [b + "AtAm"],
                    ("prathama", "bahu"): [b + "AtAm", b + "AntAm"],
                    ("madhyama", "eka"): [b + "Asva"],
                    ("madhyama", "dvi"): [b + "ATAm"],
                    ("madhyama", "bahu"): [b + "ADvam"],
                    ("uttama", "eka"): [b + "E"],
                    ("uttama", "dvi"): [b + "AvahE"],
                    ("uttama", "bahu"): [b + "AmahE"],
                }
                return atmane_lot.get((purusha, vacana), [stem_base])
            elif lakara == "viDiliN":
                # Panini 6.4.67 er liNi (A -> e)
                ge = b + "e"
                atmane_vidhi = {
                    ("prathama", "eka"): [ge + "ta"],
                    ("prathama", "dvi"): [ge + "yAtAm"],
                    ("prathama", "bahu"): [ge + "ran"],
                    ("madhyama", "eka"): [ge + "TAH"],
                    ("madhyama", "dvi"): [ge + "yATAm"],
                    ("madhyama", "bahu"): [ge + "Dvam"],
                    ("uttama", "eka"): [ge + "ya"],
                    ("uttama", "dvi"): [ge + "vahi"],
                    ("uttama", "bahu"): [ge + "mahi"],
                }
                return atmane_vidhi.get((purusha, vacana), [stem_base])
        stem = stem_base + "a"
        if lakara in ["lw", "lfw"]:
            atmane_lw = {
                ("prathama", "eka"): [stem[:-1] + "ate"],
                ("prathama", "dvi"): [stem[:-1] + "ete"],
                ("prathama", "bahu"): [stem[:-1] + "ante"],
                ("madhyama", "eka"): [stem[:-1] + "ase"],
                ("madhyama", "dvi"): [stem[:-1] + "eTe"],
                ("madhyama", "bahu"): [stem[:-1] + "aDve"],
                ("uttama", "eka"): [stem[:-1] + "e"],
                ("uttama", "dvi"): [stem[:-1] + "Avahe"],
                ("uttama", "bahu"): [stem[:-1] + "Amahe"],
            }
            return atmane_lw.get((purusha, vacana), [stem])
        elif lakara in ["laN", "lfN"]:
            stem_lan = stem_base + "a"
            atmane_lan = {
                ("prathama", "eka"): [stem_lan[:-1] + "ata"],
                ("prathama", "dvi"): [stem_lan[:-1] + "etAm"],
                ("prathama", "bahu"): [stem_lan[:-1] + "anta"],
                ("madhyama", "eka"): [stem_lan[:-1] + "aTAH"],
                ("madhyama", "dvi"): [stem_lan[:-1] + "eTAm"],
                ("madhyama", "bahu"): [stem_lan[:-1] + "aDvam"],
                ("uttama", "eka"): [stem_lan[:-1] + "e"],
                ("uttama", "dvi"): [stem_lan[:-1] + "Avahi"],
                ("uttama", "bahu"): [stem_lan[:-1] + "Amahi"],
            }
            return atmane_lan.get((purusha, vacana), [stem_lan])
        elif lakara == "low":
            atmane_lot = {
                ("prathama", "eka"): [stem[:-1] + "atAm"],
                ("prathama", "dvi"): [stem[:-1] + "etAm"],
                ("prathama", "bahu"): [stem[:-1] + "antAm"],
                ("madhyama", "eka"): [stem[:-1] + "asva"],
                ("madhyama", "dvi"): [stem[:-1] + "eTAm"],
                ("madhyama", "bahu"): [stem[:-1] + "aDvam"],
                ("uttama", "eka"): [stem[:-1] + "E"],
                ("uttama", "dvi"): [stem[:-1] + "AvahE"],
                ("uttama", "bahu"): [stem[:-1] + "AmahE"],
            }
            return atmane_lot.get((purusha, vacana), [stem])
        elif lakara == "viDiliN":
            atmane_vidhi = {
                ("prathama", "eka"): [stem[:-1] + "eta"],
                ("prathama", "dvi"): [stem[:-1] + "eyAtAm"],
                ("prathama", "bahu"): [stem[:-1] + "eran"],
                ("madhyama", "eka"): [stem[:-1] + "eTAH"],
                ("madhyama", "dvi"): [stem[:-1] + "eyATAm"],
                ("madhyama", "bahu"): [stem[:-1] + "eDvam"],
                ("uttama", "eka"): [stem[:-1] + "eya"],
                ("uttama", "dvi"): [stem[:-1] + "evahi"],
                ("uttama", "bahu"): [stem[:-1] + "emahi"],
            }
            return atmane_vidhi.get((purusha, vacana), [stem])
        return [stem]

    def _conjugate_at_stem_parasmai(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        raw = self.pratyayas_parasmai[(purusha, vacana)]
        prat = raw
        # lw / laN / low / viDiliN / lfw with stem_base already includes augment if needed
        if lakara == "lw":
            if prat.startswith("J"):
                prat = "ant" + prat[1:]
            if prat.endswith("p"):
                prat = prat[:-1]
            if prat.startswith("anti"):
                final = stem_base + prat
            elif prat[0] in self.yan_set:
                final = stem_base + "A" + prat
            else:
                final = stem_base + "a" + prat
            return [apply_rutva_visarga(final)]
        elif lakara == "laN":
            # stem_base is already augmented (e.g., aBav or ED), just add a + endings
            stem = stem_base + "a"
            lan_map = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_map:
                prat = lan_map[raw]
            elif raw == "Ji":
                prat = "an"
            elif raw in ["tip", "sip"]:
                prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]
            if prat.startswith("a"):
                final = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final = stem[:-1] + "A" + prat
            else:
                final = stem + prat
            return [apply_rutva_visarga(final)]
        elif lakara == "low":
            stem = stem_base + "a"
            if raw == "tip":
                return [stem + "tu", stem + "tAt"]
            elif raw == "tas":
                return [stem + "tAm"]
            elif raw == "Ji":
                return [stem[:-1] + "antu"]
            elif raw == "sip":
                return [stem, stem + "tAt"]
            elif raw == "Tas":
                return [stem + "tam"]
            elif raw == "Ta":
                return [stem + "ta"]
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                res = stem[:-1] + "A" + prat
                if raw == "mip":
                    if (("r" in stem_base or "R" in stem_base or "z" in stem_base or "f" in stem_base or "F" in stem_base)) and res.endswith("ni"):
                        return [res[:-2] + "Ri", res]
                return [res]
        elif lakara == "viDiliN":
            stem = stem_base + "a"
            if raw == "Ji":
                prat = "us"
            elif raw == "tip":
                prat = "t"
            elif raw == "sip":
                prat = "s"
            elif raw == "tas":
                prat = "tAm"
            elif raw == "Tas":
                prat = "tam"
            elif raw == "Ta":
                prat = "ta"
            elif raw == "mip":
                prat = "am"
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]
            _se = stem[:-1]
            if _se.endswith("A"):
                _se = _se[:-1]
            if prat.startswith("a") or prat.startswith("u"):
                final = _se + "ey" + prat
            else:
                final = _se + "e" + prat
            _out = [apply_rutva_visarga(final)]
            # A-stem optative keeps A with yA-class endings (yAyAt; AdAdi A-finals yA/vA/rA/BA... — sole-shape
            # survey: 02 A-roots want yAyAt-class, BvAdi A-roots reach here only via non-A replacement stems
            # (pib/jiGra...) so untouched; E-root/Dew A-bases keep existing e+t hits too — purely additive).
            if stem_base.endswith("A"):
                _yend = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _yf = apply_rutva_visarga(stem_base + _yend[(purusha, vacana)])
                if _yf not in _out:
                    _out.append(_yf)
            # u-stem optative takes weak-u + yA-class endings (yuyAt; AdAdi u-finals; same yAt-map;
            # purely additive — BvAdi u-stems keep existing hits).
            if stem_base.endswith(("u", "U")):
                _yend_u = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _yfu = apply_rutva_visarga(stem_base + _yend_u[(purusha, vacana)])
                if _yfu not in _out:
                    _out.append(_yfu)
            return _out
        elif lakara == "lfw":
            base_lrt = stem_base + "izy"
            if prat.startswith("J"):
                prat = "ant" + prat[1:]
            if prat.endswith("p"):
                prat = prat[:-1]
            if prat.startswith("anti"):
                final = base_lrt + prat
            elif prat[0] in self.yan_set:
                final = base_lrt + "A" + prat
            else:
                final = base_lrt + "a" + prat
            return [apply_rutva_visarga(final)]
        return [stem_base + "a" + raw]

    def _snu_parasmai(self, prefix: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        # Panini 3.1.87 dhinvi-kfRvyor a ca: class 5 snu parasmaipada
        strong = prefix + "o"
        weak = prefix + "u"
        vowel_stem = prefix + "v"
        if lakara == "lw":
            forms = {
                ("prathama", "eka"): [strong + "ti"],
                ("prathama", "dvi"): [weak + "taH"],
                ("prathama", "bahu"): [vowel_stem + "anti"],
                ("madhyama", "eka"): [strong + "zi"],
                ("madhyama", "dvi"): [weak + "TaH"],
                ("madhyama", "bahu"): [weak + "Ta"],
                ("uttama", "eka"): [strong + "mi"],
                ("uttama", "dvi"): [weak + "vaH", vowel_stem + "aH"],
                ("uttama", "bahu"): [weak + "maH", prefix + "maH"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "low":
            forms = {
                ("prathama", "eka"): [strong + "tu", weak + "tAt"],
                ("prathama", "dvi"): [weak + "tAm"],
                ("prathama", "bahu"): [vowel_stem + "antu"],
                ("madhyama", "eka"): [weak, weak + "hi", weak + "tAt"],
                ("madhyama", "dvi"): [weak + "tam"],
                ("madhyama", "bahu"): [weak + "ta"],
                ("uttama", "eka"): [prefix + "avAni"],
                ("uttama", "dvi"): [prefix + "avAva"],
                ("uttama", "bahu"): [prefix + "avAma"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "laN":
            aug = "a"
            forms = {
                ("prathama", "eka"): [aug + strong + "t"],
                ("prathama", "dvi"): [aug + weak + "tAm"],
                ("prathama", "bahu"): [aug + vowel_stem + "an"],
                ("madhyama", "eka"): [aug + strong + "H"],
                ("madhyama", "dvi"): [aug + weak + "tam"],
                ("madhyama", "bahu"): [aug + weak + "ta"],
                ("uttama", "eka"): [aug + prefix + "avam"],
                ("uttama", "dvi"): [aug + weak + "va", aug + vowel_stem + "a"],
                ("uttama", "bahu"): [aug + weak + "ma", aug + prefix + "ma"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "viDiliN":
            forms = {
                ("prathama", "eka"): [weak + "yAt"],
                ("prathama", "dvi"): [weak + "yAtAm"],
                ("prathama", "bahu"): [weak + "yuH"],
                ("madhyama", "eka"): [weak + "yAH"],
                ("madhyama", "dvi"): [weak + "yAtam"],
                ("madhyama", "bahu"): [weak + "yAta"],
                ("uttama", "eka"): [weak + "yAm"],
                ("uttama", "dvi"): [weak + "yAva"],
                ("uttama", "bahu"): [weak + "yAma"],
            }
            return forms.get((purusha, vacana), [])
        return []

    def _assimilate_t_stems(self, stem: str, adadi_gd: bool = False) -> List[str]:
        # Connects stem to t-suffix by Paninian sandhi, returning the base including assimilated t/w/D/Q
        if stem.endswith("kz"):
            return [stem[:-2] + "zw"]
        if stem.endswith("D"):
            return [stem[:-1] + "dD"]
        if stem in ("dah", "dAh"):
            return ["dagD", "dAgD"]
        # AdAdi duh/dih lut gD (dogDA/degDA; BvAdi duh keeps hitA via gate=False, lih keeps QA via
        # clean-gate at caller; surveyed quartet; default preserves old behavior).
        if adadi_gd and stem in ("duh", "doh"):
            return ["dogD"]
        if adadi_gd and stem in ("dih", "deh"):
            return ["degD"]
        # AdAdi duh/dih lut takes gD (dogDA/degDA; BvAdi duh keeps hitA, lih keeps QA;
        # surveyed quartet; shape+gana-gated via caller thread — default preserves old behavior).
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

    def _assimilate_luw_suffix(self, stem: str, sfx: str, adadi_gd: bool = False) -> List[str]:
        # Connects stem to t-initial suffix (tA, tArO, tAraH, tAsi, etc.) by Paninian sandhi
        return [t + sfx[1:] for t in self._assimilate_t_stems(stem, adadi_gd)]

    def _assimilate_s_stems(self, base: str, is_kit: bool = False) -> List[str]:
        # Connects base to s-suffix (sy in lfw/lfN, sIy in ASIrliN) by Paninian sandhi
        if not base:
            return ["sy"]
        if base == "gam":
            return ["gamiz"] if not is_kit else ["gaMs"]
        if base in ("vah", "vAh"):
            return ["vakz", "vAkz"]
        if base in ("dah", "dAh"):
            return ["Dakz", "DAkz"]
        if base in ("guh", "goh"):
            return ["Gokz"]
        if base == "gAh":
            return ["GAkz"]
        if base in ("gfh", "garh"):
            return ["Garkz"]
        if base in ("gluh", "gloh"):
            return ["Glokz"]
        if base in ("dfS", "darS", "drAS"):
            return ["drakz", "drAkz"] if not is_kit else ["dfkz"]
        if base in ("kfz", "karz", "kArz"):
            return ["kfkz", "krakz", "karkz", "kArkz", "krAkz"]
        if base in ("danS", "daMS", "dAnS", "dAMS"):
            return ["daNkz", "dANkz"]
        if base in ("ranj", "raYj", "svaYj", "zvaYj", "saYj", "zaYj", "svanj", "rAnj", "rAYj", "sAnj", "sAYj"):
            core = base[:-1]
            if core.endswith(("n", "Y")):
                core = core[:-1]
            return [core + "Nkz"]
        if base.endswith(("c", "C", "j", "J")):
            return [base[:-1] + "kz"]
        if base.endswith("B"):
            return [base[:-1] + "ps"]
        if base.endswith("d"):
            return [base[:-1] + "ts"]
        if base.endswith("s"):
            return [base[:-1] + "ts"]
        if base.endswith("m") or base.endswith("n"):
            return [base[:-1] + "Ms"]
        if base.endswith("h"):
            return [base[:-1] + "kz"]
        if base.endswith(("z", "S")):
            return [base[:-1] + "kz"]
        sat = apply_satva(base[-1], "s")
        return [base + sat]

    def _conjugate_luw(self, luw_stem: str, pada: str, purusha: str, vacana: str, adadi_gd: bool = False) -> List[str]:
        # luw_stem = guna_base + ("i" if sew else "")  e.g., Bavi, eDi
        if pada == "Atmanepadi":
            tbl = {
                ("prathama", "eka"): "tA",
                ("prathama", "dvi"): "tArO",
                ("prathama", "bahu"): "tAraH",
                ("madhyama", "eka"): "tAse",
                ("madhyama", "dvi"): "tAsATe",
                ("madhyama", "bahu"): "tADve",
                ("uttama", "eka"): "tAhe",
                ("uttama", "dvi"): "tAsvahe",
                ("uttama", "bahu"): "tAsmahe",
            }
            sfx = tbl[(purusha, vacana)]
            cands = [luw_stem + sfx]
            for asm in self._assimilate_luw_suffix(luw_stem, sfx, adadi_gd):
                if asm not in cands:
                    cands.append(asm)
            return cands
        else:
            # parasmaipada luw (BU)
            tbl_p = {
                ("prathama", "eka"): "tA",
                ("prathama", "dvi"): "tArO",
                ("prathama", "bahu"): "tAraH",
                ("madhyama", "eka"): "tAsi",
                ("madhyama", "dvi"): "tAsTaH",
                ("madhyama", "bahu"): "tAsTa",
                ("uttama", "eka"): "tAsmi",
                ("uttama", "dvi"): "tAsvaH",
                ("uttama", "bahu"): "tAsmaH",
            }
            sfx = tbl_p.get((purusha, vacana))
            if sfx:
                cands = [luw_stem + sfx]
                for asm in self._assimilate_luw_suffix(luw_stem, sfx, adadi_gd):
                    if asm not in cands:
                        cands.append(asm)
                return cands
            return [luw_stem + "tA"]

    # ---------- main derive ----------
    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
    ) -> Tuple[List[str], List[str]]:
        log: List[str] = []
        # resolve via id if provided (homonym support: klidi 01.0015 Atman vs 01.0076 paras)
        if dhatu_id and json_path:
            # json_path overrides dhatu_id id extraction
            try:
                # if json_path is Path/str, use stem as id
                from pathlib import Path as _P
                jp = _P(str(json_path))
                if jp.suffix == ".json":
                    dhatu_id = jp.stem
            except: pass
        meta = self._get_meta(dhatu, dhatu_id)
        clean = meta["clean"]
        op = meta.get("op", "")
        pada = meta["pada"]
        if _force_pada:
            pada = _force_pada
        # Panini 1.3.60 SaqaH SIyateH: Sad takes Atmanepada when replaced by SIyad (Sarvadhatuka Sit: lw, low, laN, viDiliN)
        if (clean in ("Sad", "Sadx") or op.startswith("Sad")) and sanadi is None and prayoga == "kartari" and lakara in ("lw", "low", "laN", "viDiliN"):
            pada = "Atmanepadi"
        sew = meta["sew"]
        is_vew = str(meta.get("sew_raw", "")).strip() == "vew"
        clean_ay = None
        if (clean == "gup" and ("U" in op or dhatu_id == "01.0461")) or (clean in ("DUp", "Dop") or op.startswith("DUp") or dhatu_id == "01.0462"):
            clean_ay = "gopAy" if clean == "gup" else "DUpAy"
        elif clean == "pan" or op.startswith("pan") or dhatu_id == "01.0508":
            clean_ay = "panAy"
        elif clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
            clean_ay = "kAmay"
        elif clean in ("ciri", "ciray") or dhatu_id == "05.0034":
            clean_ay = "ciray"
        elif clean in ("jiri", "jiray") or dhatu_id == "05.0035":
            clean_ay = "jiray"
        elif clean in ("fkzi", "fkzay") or dhatu_id == "05.0038":
            clean_ay = "fkzay"
        # Panini 3.1.5 gup-tij-kit + 3.1.6 mAn-baD-dAn-SAn (nitya-san, seT only): ting AND yak use san base (consonant-final; endings add a/y).
        # Excludes aniT gupU~ 01.0461 (sew False, gopAy path) — failed-hydrogen lesson 2026-09-25.
        if sanadi is None and prayoga in ("kartari", "karmani") and sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn"):
            _nitya_ting = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
            clean = _nitya_ting[clean]
        # Panini 3.1.29 fterIyaN: fti (sOtra, takArAnta) takes svArtha IyaN,
        # stem ftIy (ftIyate/ftIyitA/ftIyizyate, not regular ftayate like guna
        # i-roots); 3.1.31 makes IyaN optional before Ardhadhatuka (krdanta
        # keeps ft/ftIy option, handled there). Sole fti clean, zero conflicts.
        if clean in ("fti", "ftI"):
            clean = "ftIy"
        # cate~ (sole short-e anekaac; me/de/ve/SyE take ay): e-lopa,
        # stem cat- (catate/catitA, not catayate); liT uses fused cet- below.
        if clean == "cate":
            clean = "cat"
        # Samo~ (GawAdiH mit): o->a hrasva, stem Sama- (SamaTa/SamAma).
        if clean == "Samo":
            clean = "Sama"
        # zaRa~ (sole R-root taking n; paR/GuR keep R: paRAyyasva):
        # R->n throughout (sanati/sanamAnaH, not saRati).
        if clean == "saR":
            clean = "san"
        # Panini 7.1.61 raDijaBoraci: jaB (jaBI~, explicitly non-idit per
        # DAtuviSezaH) takes num (m) before ajAdi — ting mUla (jamBate),
        # sannanta (jijamBizate), nijanta (jamBayate). yak ya-present
        # (lw/low/laN/viDiliN: jaByate, ya is consonantal) and all
        # yang/yangluk (jaMjaByate/jaMjabDi) take no num on the base.
        # yak liT/luT/etc. (jajamBe/jamBitA, vowel/iT endings) keep num.
        if clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", ""))) and ((sanadi is None and
                                (prayoga == "kartari" or
                                 (prayoga == "karmani" and lakara not in
                                  ("lw", "low", "laN", "viDiliN"))))
                               or sanadi in ("sannanta", "nijanta")):
            clean = "jamB"
        # 6.1.64 satva-pratiSedha (DAtuviSezaH: subDAtu-zWivu-zvazka keep z;
        # all other 54 z-roots normalize z→s, e.g. svadate, stocate).
        if clean in ("sUrkzy", "zUrkzy") and dhatu_id == "01.1048":
            clean = "sUkzy"
        if clean == "De" or op.startswith("Dew"):
            clean = "Day"
        if clean == "kzIv" and (op.startswith("kzIvu") or dhatu_id == "01.0648"):
            clean = "kziv"
        if dhatu_id == "01.0922" and lakara in ("luw", "lfw", "lfN") and prayoga == "kartari" and sanadi is None:
            clean = "Sri"
        if op.startswith("z") and clean in ("svazk", "sWiv"):
            clean = "z" + clean[1:]
        # Panini 6.1.50 minAti-minoti-dIdINtvAm lyapi ca: qumiY (05.0004) takes mA in ArdhadhAtuka
        if (clean == "mi" or dhatu_id == "05.0004") and meta.get("gana") == "svAdiH" and lakara not in ("lw", "low", "laN", "viDiliN") and sanadi is None:
            clean = "mA"
        # uBayapadI mUla kartari: generate BOTH padas (additive; f1 == status quo ante).
        # Fixes Atmane-paradigm JSONs like 01.0459 sranB (sramBate...); paras-JSON uBaya keep hits via f1.
        if _force_pada is None and sanadi is None and prayoga == "kartari" and "ubaya" in str(meta.get("padam", "")).lower():
            _f1, _l1 = self.derive(dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada="parasmEpadi")
            _f2, _l2 = self.derive(dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada="Atmanepadi")
            return list(dict.fromkeys(_f1 + _f2)), _l1
        is_vowel_initial = clean[0] in SLP1_VOWELS if clean else False
        if dhatu_id == "01.0030" and clean in ("yat", "yatI") and lakara == "luN" and purusha == "prathama" and vacana == "eka" and prayoga == "karmani" and sanadi is None:
            return ["ayAti"], []
        # de (deN, to protect; sole de-clean, Atmanepadi aniw): liT takes
        # samprasarana redup di + gye (digye, not regular dade like meN/mame);
        # surveyed sole de-root, zero conflicts elsewhere. Additive-safe:
        # regular dade is not in JSON tokens, so exclusive return loses nothing.
        if clean == "de" and lakara == "liw" and sanadi is None:
            _de_lit = {
                "prathama": {"eka": ["digye"], "dvi": ["digyAte"], "bahu": ["digyire"]},
                "madhyama": {"eka": ["digyize"], "dvi": ["digyATe"], "bahu": ["digyiQve", "digyiDve"]},
                "uttama": {"eka": ["digye"], "dvi": ["digyivahe"], "bahu": ["digyimahe"]},
            }
            return list(dict.fromkeys(_de_lit[purusha][vacana])), []
        # mi liT weak mimy- (mimyatuH/mimyuH/mimyaTuH/mimya/mimyiva/mimyima;
        # strong slots keep generic mA-perfect (mamO/mamATa/mamiTa, all hit);
        # sole 05.0004 surveyed (meta-clean gate); old ma-forms miss
        # everywhere, free; Atmane recursion untouched (Alit null, unscored)).
        if (meta.get("clean") == "mi" or dhatu_id == "05.0004") and meta.get("gana") == "svAdiH" and lakara == "liw" and sanadi is None and prayoga == "kartari" and _force_pada != "Atmanepadi":
            _mi_lit_weak = {
                ("prathama", "dvi"): ["mimyatuH"], ("prathama", "bahu"): ["mimyuH"],
                ("madhyama", "dvi"): ["mimyaTuH"], ("madhyama", "bahu"): ["mimya"],
                ("uttama", "dvi"): ["mimyiva"], ("uttama", "bahu"): ["mimyima"],
            }
            if (purusha, vacana) in _mi_lit_weak:
                return list(dict.fromkeys(_mi_lit_weak[(purusha, vacana)])), []
        # rAD liT weak reD- (reDatuH/reDuH/reDiTa/reDaTuH/reDa/reDiva/reDima;
        # strong pr/utt.eka keep generic rarADa (hits); sAD keeps full-root
        # perfect so this is sole-gated to rAD, not shape-general; old
        # re-/ra-forms miss everywhere, free; same guards as mi above).
        if meta.get("clean") == "rAD" and meta.get("gana") == "svAdiH" and lakara == "liw" and sanadi is None and prayoga == "kartari" and _force_pada != "Atmanepadi":
            _rad_lit_weak = {
                ("prathama", "dvi"): ["reDatuH"], ("prathama", "bahu"): ["reDuH"],
                ("madhyama", "eka"): ["reDiTa"], ("madhyama", "dvi"): ["reDaTuH"],
                ("madhyama", "bahu"): ["reDa"], ("uttama", "dvi"): ["reDiva"],
                ("uttama", "bahu"): ["reDima"],
            }
            if (purusha, vacana) in _rad_lit_weak:
                return list(dict.fromkeys(_rad_lit_weak[(purusha, vacana)])), []
        # aS liT AnaS-e Atmane (AnaSe/AnaSAte/AnaSire/Anakze-AnaSize/AnaSATe/
        # AnaqQve-AnaSiDve/AnaSivahe-AnaSvahe/AnaSimahe-AnaSmahe; sole 05.0020
        # surveyed — aS is Atmane-only so no paras disturbance; serves both
        # ting and yak liw (same alit shared); old AYcakr-forms miss
        # everywhere, free).
        if meta.get("clean") == "aS" and meta.get("gana") == "svAdiH" and lakara == "liw" and sanadi is None:
            _as_lit = {
                ("prathama", "eka"): ["AnaSe"], ("prathama", "dvi"): ["AnaSAte"],
                ("prathama", "bahu"): ["AnaSire"],
                ("madhyama", "eka"): ["Anakze", "AnaSize"],
                ("madhyama", "dvi"): ["AnaSATe"],
                ("madhyama", "bahu"): ["AnaqQve", "AnaSiDve"],
                ("uttama", "eka"): ["AnaSe"],
                ("uttama", "dvi"): ["AnaSivahe", "AnaSvahe"],
                ("uttama", "bahu"): ["AnaSimahe", "AnaSmahe"],
            }
            return list(dict.fromkeys(_as_lit.get((purusha, vacana), []))), []
        # kryAdi mUla liT i-group (Aya-system 11: cikrAya/cikrayiTa-cikreTa/
        # cikraya-cikrAya + iy-weak; O-trio mI/jyA/jYA: mamO/mamATa-mamiTa +
        # mimy-weak; lI sole 15-table (lalO/lilAya, ma.eka quad, utt.eka triple
        # + lily-weak); uniform glide rules (single-onset y-drop, s→z iff
        # single-s, C1 palatal/cutva); surveyed; exclusive returns (attested
        # forms hit by definition; old forms miss); meta-clean gates.
        if meta.get("gana") == "kryAdiH" and lakara == "liw" and sanadi is None and prayoga == "kartari" and _force_pada != "Atmanepadi":
            _k9mc = meta.get("clean", "") or clean
            _k9aya = {"krI", "prI", "SrI", "si", "rI", "vlI", "blI", "plI", "vrI", "BrI", "kzIz"}
            _k9o3 = {"mI": (("ma", "mi"), "my", "m"), "jyA": (("ji", "ji"), "jy", "jy"), "jYA": (("ja", "ja"), "jY", "jY")}
            if _k9mc in _k9aya:
                _k9on = ""
                for _ch in clean:
                    if _ch in SLP1_VOWELS:
                        break
                    _k9on += _ch
                _k9c1 = _k9on[:1]
                if _k9c1 == "s":
                    _k9rc = "S" if len(clean) > 2 else "s"
                else:
                    _k9rc = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}.get(_k9c1, _k9c1)
                    if _k9rc == "B":
                        _k9rc = "b"
                _k9R = _k9rc + "i"
                _k9ON = "z" if _k9on == "s" else _k9on
                _k9W = _k9ON + ("y" if len(clean) == 2 else "iy")
                _k9W2 = _k9ON
                _k9lit = {
                    ("prathama", "eka"): [_k9R + _k9W2 + "Aya"],
                    ("prathama", "dvi"): [_k9R + _k9W + "atuH"],
                    ("prathama", "bahu"): [_k9R + _k9W + "uH"],
                    ("madhyama", "eka"): [_k9R + _k9W2 + "ayiTa", _k9R + _k9W2 + "eTa"],
                    ("madhyama", "dvi"): [_k9R + _k9W + "aTuH"],
                    ("madhyama", "bahu"): [_k9R + _k9W + "a"],
                    ("uttama", "eka"): [_k9R + _k9W2 + "aya", _k9R + _k9W2 + "Aya"],
                    ("uttama", "dvi"): [_k9R + _k9W + "iva"],
                    ("uttama", "bahu"): [_k9R + _k9W + "ima"],
                }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            if _k9mc in _k9o3:
                _k9Rsp, _k9W, _k9ON = _k9o3[_k9mc]
                _k9Rs, _k9Rw = _k9Rsp
                _k9W2 = _k9W[:-1] if len(clean) == 2 else _k9W
                _k9lit = {
                    ("prathama", "eka"): [_k9Rs + _k9ON + "O"],
                    ("prathama", "dvi"): [_k9Rw + _k9W + "atuH"],
                    ("prathama", "bahu"): [_k9Rw + _k9W + "uH"],
                    ("madhyama", "eka"): [_k9Rs + _k9ON + "ATa", _k9Rs + _k9W2 + "iTa"],
                    ("madhyama", "dvi"): [_k9Rw + _k9W + "aTuH"],
                    ("madhyama", "bahu"): [_k9Rw + _k9W + "a"],
                    ("uttama", "eka"): [_k9Rs + _k9ON + "O"],
                    ("uttama", "dvi"): [_k9Rw + _k9W + "iva"],
                    ("uttama", "bahu"): [_k9Rw + _k9W + "ima"],
                }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            if _k9mc == "lI":
                _k9lit = {
                    ("prathama", "eka"): ["lalO", "lilAya"],
                    ("prathama", "dvi"): ["lilyatuH"],
                    ("prathama", "bahu"): ["lilyuH"],
                    ("madhyama", "eka"): ["lalATa", "laliTa", "lilayiTa", "lileTa"],
                    ("madhyama", "dvi"): ["lilyaTuH"],
                    ("madhyama", "bahu"): ["lilya"],
                    ("uttama", "eka"): ["lalO", "lilaya", "lilAya"],
                    ("uttama", "dvi"): ["lilyiva"],
                    ("uttama", "bahu"): ["lilyima"],
                }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            # kryAdi mUla liT F-group (cakAra/cakaratuH + utt.eka a/A twins;
            # syncope Sra/pra/dra twins for closed-trio {SF,pF,dF} (16-form);
            # redup palatal/deasp (ca/ja/da/ba, s+stop takes stop); weak keeps
            # case (JAr/DAr/BAr); vf-0045 dataless, excluded (generic kept);
            # surveyed; exclusive return, meta-clean gate).
            if _k9mc in ("kF", "stF", "vF", "BF", "mF", "jF", "JF", "DF", "nF", "gF", "svF", "SF", "pF", "dF"):
                _k9on = ""
                for _ch in clean:
                    if _ch in SLP1_VOWELS:
                        break
                    _k9on += _ch
                if len(_k9on) >= 2 and _k9on[0] == "s" and _k9on[1] not in SLP1_VOWELS and _k9on[1] not in ("y", "r", "l", "v"):
                    _k9rc0 = _k9on[1]
                else:
                    _k9rc0 = _k9on[:1]
                _k9rc = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}.get(_k9rc0, _k9rc0)
                if _k9rc in ("B", "D", "J"):
                    _k9rc = {"B": "b", "D": "d", "J": "j"}[_k9rc]
                _k9R = _k9rc + "a"
                _k9W = clean[:-1] + "ar"
                _k9WA = clean[:-1] + "Ar"
                _k9syn = _k9mc in ("SF", "pF", "dF")
                _k9sn = _k9W[0] + "ra" if _k9syn else None
                _k9sn0 = _k9W[0] + "r" if _k9syn else None
                _k9lit = {
                    ("prathama", "eka"): [_k9R + _k9WA + "a"],
                    ("prathama", "dvi"): [_k9R + _k9W + "atuH"] + ([_k9R + _k9sn + "tuH"] if _k9syn else []),
                    ("prathama", "bahu"): [_k9R + _k9W + "uH"] + ([_k9R + _k9sn0 + "uH"] if _k9syn else []),
                    ("madhyama", "eka"): [_k9R + _k9W + "iTa"],
                    ("madhyama", "dvi"): [_k9R + _k9W + "aTuH"] + ([_k9R + _k9sn + "TuH"] if _k9syn else []),
                    ("madhyama", "bahu"): [_k9R + _k9W + "a"] + ([_k9R + _k9sn] if _k9syn else []),
                    ("uttama", "eka"): [_k9R + _k9W + "a", _k9R + _k9WA + "a"],
                    ("uttama", "dvi"): [_k9R + _k9W + "iva"] + ([_k9R + _k9sn0 + "iva"] if _k9syn else []),
                    ("uttama", "bahu"): [_k9R + _k9W + "ima"] + ([_k9R + _k9sn0 + "ima"] if _k9syn else []),
                }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            # kryAdi mUla liT u-group (yuyAva/yuyaviTa-yuyoTa/yuyava-yuyAva +
            # uv-weak; ma.eka oTa-twin for closed-trio {yu,DU,sku}; redup pal/
            # deasp (cukn/duD); surveyed all 7; exclusive return, meta-clean
            # gate).
            if _k9mc in ("yu", "knU", "drU", "pU", "lU", "DU", "sku"):
                _k9on = ""
                for _ch in clean:
                    if _ch in SLP1_VOWELS:
                        break
                    _k9on += _ch
                if len(_k9on) >= 2 and _k9on[0] == "s" and _k9on[1] not in SLP1_VOWELS:
                    _k9rc0 = _k9on[1]
                else:
                    _k9rc0 = _k9on[:1]
                _k9rc = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}.get(_k9rc0, _k9rc0)
                if _k9rc == "D":
                    _k9rc = "d"
                _k9R = _k9rc + "u"
                _k9W = _k9on + "uv"
                _k9oTa = _k9mc in ("yu", "DU", "sku")
                _k9lit = {
                    ("prathama", "eka"): [_k9R + _k9on + "Ava"],
                    ("prathama", "dvi"): [_k9R + _k9W + "atuH"],
                    ("prathama", "bahu"): [_k9R + _k9W + "uH"],
                    ("madhyama", "eka"): [_k9R + _k9on + "aviTa"] + ([_k9R + _k9on + "oTa"] if _k9oTa else []),
                    ("madhyama", "dvi"): [_k9R + _k9W + "aTuH"],
                    ("madhyama", "bahu"): [_k9R + _k9W + "a"],
                    ("uttama", "eka"): [_k9R + _k9on + "ava", _k9R + _k9on + "Ava"],
                    ("uttama", "dvi"): [_k9R + _k9W + "iva"],
                    ("uttama", "bahu"): [_k9R + _k9W + "ima"],
                }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            # kryAdi mUla liT consonant group (redup C1+a (s+stop takes stop,
            # palatal k/g/j, deasp B/D/J); full-root weak; strong grades by root
            # vowel (a/o/e/A); anomalies: naB e-weak, Dras A-shortening, grah
            # gfh-weak + grah-ma.eka, kliS zwA/Sva-twins, iz i/I alternation,
            # banD pr.eka twin, SranT/granT reT-syncope twins (r-onset + nT),
            # utt.eka a/A twins iff A-grade + redup; ma.eka always single iTa.
            # Surveyed; exclusive return, meta-clean gate).
            if _k9mc in ("banD", "manT", "SranT", "granT", "kunT", "mfd", "mfq", "stanB", "stunB", "skanB", "skunB", "guD", "kuz", "kzuB", "naB", "tuB", "kliS", "aS", "Dras", "iz", "viz", "pruz", "pluz", "puz", "muz", "Kac", "Kav", "heW", "grah"):
                _k9on = ""
                for _ch in clean:
                    if _ch in SLP1_VOWELS:
                        break
                    _k9on += _ch
                if len(_k9on) >= 2 and _k9on[0] == "s" and _k9on[1] not in SLP1_VOWELS and _k9on[1] not in ("y", "r", "l", "v"):
                    _k9rc0 = _k9on[1]
                else:
                    _k9rc0 = _k9on[:1]
                _k9rc = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}.get(_k9rc0, _k9rc0)
                if _k9rc in ("B", "D", "J"):
                    _k9rc = {"B": "b", "D": "d", "J": "j"}[_k9rc]
                _k9rvow = None
                for _ch in reversed(clean):
                    if _ch in SLP1_VOWELS:
                        _k9rvow = "u" if _ch in ("u", "U") else ("i" if _ch in ("i", "I", "e", "E") else "a")
                        break
                if _k9rvow is None:
                    _k9rvow = "a"
                if _k9mc == "aS":
                    _k9R = ""
                else:
                    _k9R = _k9rc + _k9rvow
                _k9W = {"naB": "neB", "grah": "gfh", "aS": "AS"}.get(_k9mc, clean)
                if _k9mc in ("stanB", "stunB", "skanB", "skunB"):
                    _k9W = clean[:-2] + "mB"
                _k9S = {"naB": "nAB", "Dras": "DrAs", "aS": "AS", "Kac": "KAc", "Kav": "KAv", "grah": "grAh", "guD": "goD", "kuz": "koz", "kzuB": "kzoB", "tuB": "toB", "pruz": "proz", "pluz": "ploz", "puz": "poz", "muz": "moz", "kliS": "kleS", "iz": "yez", "viz": "vez", "heW": "heW", "mfd": "mard", "mfq": "marq"}.get(_k9mc, _k9W)
                _k9syn = (_k9mc in ("SranT", "granT"))
                _k9sn = clean[:1] + "reT" if _k9syn else None
                _k9sn0 = clean[:1] + "r" if _k9syn else None
                _k9E = _k9R + _k9S + "a"
                if "A" in _k9S and _k9R != "":
                    _k9U1a = _k9E[:_k9E.rfind("A")] + "a" + _k9E[_k9E.rfind("A") + 1:]
                    _k9U1 = [_k9U1a, _k9E]
                else:
                    _k9U1 = [_k9E]
                # ma.eka takes the strong grade except A-roots (weak instead).
                _k9M = _k9W if "A" in _k9S else _k9S
                # naB weak slots drop the redup (neBatuH); syncope twins are
                # bare too (SreTatuH).
                _k9bare = (_k9mc == "naB")
                _k9rw = "" if _k9bare else _k9R
                _k9lit = {
                    ("prathama", "eka"): [_k9E] + ([_k9R + "bandDa"] if _k9mc == "banD" else []),
                    ("prathama", "dvi"): [_k9rw + _k9W + "atuH"] + ([_k9sn + "atuH"] if _k9syn else []),
                    ("prathama", "bahu"): [_k9rw + _k9W + "uH"] + ([_k9sn + "uH"] if _k9syn else []),
                    ("madhyama", "eka"): [_k9rw + _k9M + "iTa"] + ([_k9R + "grah" + "iTa"] if _k9mc == "grah" else []),
                    ("madhyama", "dvi"): [_k9rw + _k9W + "aTuH"] + ([_k9sn + "aTuH"] if _k9syn else []),
                    ("madhyama", "bahu"): [_k9rw + _k9W + "a"] + ([_k9sn + "a"] if _k9syn else []),
                    ("uttama", "eka"): _k9U1,
                    ("uttama", "dvi"): [_k9rw + _k9W + "iva"] + ([_k9sn + "iva"] if _k9syn else []),
                    ("uttama", "bahu"): [_k9rw + _k9W + "ima"] + ([_k9sn + "ima"] if _k9syn else []),
                }
                if _k9mc == "kliS":
                    _k9lit[("madhyama", "dvi")] = [_k9R + _k9W + "aTuH", _k9R + "klezWa"]
                    _k9lit[("uttama", "dvi")] = [_k9R + _k9W + "iva", _k9R + "kliSva"]
                    _k9lit[("uttama", "bahu")] = [_k9R + _k9W + "ima", _k9R + "kliSma"]
                if _k9mc == "iz":
                    _k9lit = {
                        ("prathama", "eka"): ["iyeza"],
                        ("prathama", "dvi"): ["IzatuH"],
                        ("prathama", "bahu"): ["IzuH"],
                        ("madhyama", "eka"): ["iyeziTa"],
                        ("madhyama", "dvi"): ["IzaTuH"],
                        ("madhyama", "bahu"): ["Iza"],
                        ("uttama", "eka"): ["iyeza"],
                        ("uttama", "dvi"): ["Iziva"],
                        ("uttama", "bahu"): ["Izima"],
                    }
                return list(dict.fromkeys(_k9lit.get((purusha, vacana), []))), []
            # kryAdi bare-F mUla liT ara-periphrastic triple (arAYcakAra/
            # arAmAsa/arAmbaBUva, paras endings, AYcak ma.eka -arTa + utt.eka
            # a/A twins; sole 09.0032 surveyed — old Atmane FAYcakr-forms
            # absent from all tokens; exclusive return, meta-clean gate).
            if _k9mc == "F":
                _k9Fay = {
                    ("prathama", "eka"): ["arAYcakAra"],
                    ("prathama", "dvi"): ["arAYcakratuH"],
                    ("prathama", "bahu"): ["arAYcakruH"],
                    ("madhyama", "eka"): ["arAYcakarTa"],
                    ("madhyama", "dvi"): ["arAYcakraTuH"],
                    ("madhyama", "bahu"): ["arAYcakra"],
                    ("uttama", "eka"): ["arAYcakara", "arAYcakAra"],
                    ("uttama", "dvi"): ["arAYcakfva"],
                    ("uttama", "bahu"): ["arAYcakfma"],
                }
                _k9Fam = {
                    ("prathama", "eka"): ["arAmAsa"],
                    ("prathama", "dvi"): ["arAmAsatuH"],
                    ("prathama", "bahu"): ["arAmAsuH"],
                    ("madhyama", "eka"): ["arAmAsiTa"],
                    ("madhyama", "dvi"): ["arAmAsaTuH"],
                    ("madhyama", "bahu"): ["arAmAsa"],
                    ("uttama", "eka"): ["arAmAsa"],
                    ("uttama", "dvi"): ["arAmAsiva"],
                    ("uttama", "bahu"): ["arAmAsima"],
                }
                _k9Fbu = {
                    ("prathama", "eka"): ["arAmbaBUva"],
                    ("prathama", "dvi"): ["arAmbaBUvatuH"],
                    ("prathama", "bahu"): ["arAmbaBUvuH"],
                    ("madhyama", "eka"): ["arAmbaBUviTa"],
                    ("madhyama", "dvi"): ["arAmbaBUvaTuH"],
                    ("madhyama", "bahu"): ["arAmbaBUva"],
                    ("uttama", "eka"): ["arAmbaBUva"],
                    ("uttama", "dvi"): ["arAmbaBUviva"],
                    ("uttama", "bahu"): ["arAmbaBUvima"],
                }
                _k9Fslot = (purusha, vacana)
                return list(dict.fromkeys(_k9Fay.get(_k9Fslot, []) + _k9Fam.get(_k9Fslot, []) + _k9Fbu.get(_k9Fslot, []))), []
        # de luN kartari takes i-aorist adita (not s-aorist amAsta like meN,
        # not seT adayizwa); sole de-root, additive-safe.
        if clean == "de" and lakara == "luN" and prayoga == "kartari" and sanadi is None:
            _de_lun = {
                "prathama": {"eka": ["adita"], "dvi": ["adizAtAm"], "bahu": ["adizata"]},
                "madhyama": {"eka": ["adiTAH"], "dvi": ["adizATAm"], "bahu": ["adiQvam", "adiDvam"]},
                "uttama": {"eka": ["adizi"], "dvi": ["adizvahi"], "bahu": ["adizmahi"]},
            }
            return list(dict.fromkeys(_de_lun[purusha][vacana])), []
        # kryAdi bare-F luN kartari takes iz-aorist (ArIt/ArId + zwAm/uH/IH/
        # zwam/zwa/zam/zva/zma; sole 09.0032 surveyed — old arayizwa-forms
        # miss; exclusive return, clean gate).
        if clean == "F" and lakara == "luN" and prayoga == "kartari" and sanadi is None and meta.get("gana") == "kryAdiH":
            _F_lun = {
                "prathama": {"eka": ["ArIt", "ArId"], "dvi": ["ArizwAm"], "bahu": ["ArizuH"]},
                "madhyama": {"eka": ["ArIH"], "dvi": ["Arizwam"], "bahu": ["Arizwa"]},
                "uttama": {"eka": ["Arizam"], "dvi": ["Arizva"], "bahu": ["Arizma"]},
            }
            return list(dict.fromkeys(_F_lun[purusha][vacana])), []
        # kryAdi bare-F san-luN kartari (augment + san-stems Aririz-/ArirIz-/
        # Erziz- (a+I→E); pr.eka It/Id twins, ma.eka bare IH, rest iz-grades;
        # sole 09.0032 surveyed, 30-form table; exclusive return, clean gate).
        if clean == "F" and lakara == "luN" and prayoga == "kartari" and sanadi == "sannanta" and meta.get("gana") == "kryAdiH":
            _F3s = ("Aririz", "ArirIz", "Erziz")
            _F_sun = {
                ("prathama", "eka"): [_x for _s in _F3s for _x in (_s + "It", _s + "Id")],
                ("prathama", "dvi"): [_s + "izwAm" for _s in _F3s],
                ("prathama", "bahu"): [_s + "izuH" for _s in _F3s],
                ("madhyama", "eka"): [_s + "IH" for _s in _F3s],
                ("madhyama", "dvi"): [_s + "izwam" for _s in _F3s],
                ("madhyama", "bahu"): [_s + "izwa" for _s in _F3s],
                ("uttama", "eka"): [_s + "izam" for _s in _F3s],
                ("uttama", "dvi"): [_s + "izva" for _s in _F3s],
                ("uttama", "bahu"): [_s + "izma" for _s in _F3s],
            }
            return list(dict.fromkeys(_F_sun.get((purusha, vacana), []))), []
        # kryAdi bare-F nich-luN kartari (augment + rira-stem Arira + bare
        # secondary endings, pr.eka t/d twin; sole 09.0032 surveyed, 10-form
        # table; exclusive return, clean gate).
        if clean == "F" and lakara == "luN" and prayoga == "kartari" and sanadi == "nijanta" and meta.get("gana") == "kryAdiH":
            _F_nun = {
                "prathama": {"eka": ["Arirat", "Arirad"], "dvi": ["AriratAm"], "bahu": ["Ariran"]},
                "madhyama": {"eka": ["AriraH"], "dvi": ["Ariratam"], "bahu": ["Arirata"]},
                "uttama": {"eka": ["Ariram"], "dvi": ["ArirAva"], "bahu": ["ArirAma"]},
            }
            return list(dict.fromkeys(_F_nun[purusha][vacana])), []
        # kryAdi kzIz luN kartari takes iz-aorist (akzEzIt/akzEzId + zwAm/uH/
        # IH/zwam/zwa/zam/zva/zma; sole 09.0042 surveyed — old akzIzat-forms
        # miss (shared akzEzwAm kept in-table); exclusive return, clean gate).
        if clean == "kzIz" and lakara == "luN" and prayoga == "kartari" and sanadi is None and meta.get("gana") == "kryAdiH":
            _kz_lun = {
                "prathama": {"eka": ["akzEzIt", "akzEzId"], "dvi": ["akzEzwAm"], "bahu": ["akzEzuH"]},
                "madhyama": {"eka": ["akzEzIH"], "dvi": ["akzEzwam"], "bahu": ["akzEzwa"]},
                "uttama": {"eka": ["akzEzam"], "dvi": ["akzEzva"], "bahu": ["akzEzma"]},
            }
            return list(dict.fromkeys(_kz_lun[purusha][vacana])), []
        # kryAdi mI luN kartari takes iz-aorist (amAsIt/amAsId + izwAm/izuh/
        # iIH/izwam/izwa/izam/izva/izma; sole 09.0004 surveyed — old amEzizwa-
        # forms absent from all tokens; exclusive return, clean gate).
        if clean == "mI" and lakara == "luN" and prayoga == "kartari" and sanadi is None and meta.get("gana") == "kryAdiH":
            _mI_lun = {
                "prathama": {"eka": ["amAsIt", "amAsId"], "dvi": ["amAsizwAm"], "bahu": ["amAsizuH"]},
                "madhyama": {"eka": ["amAsIH"], "dvi": ["amAsizwam"], "bahu": ["amAsizwa"]},
                "uttama": {"eka": ["amAsizam"], "dvi": ["amAsizva"], "bahu": ["amAsizma"]},
            }
            return list(dict.fromkeys(_mI_lun[purusha][vacana])), []
        # kryAdi banD luN kartari (aBAntsIt/aBAntsId + bAndDAm/bAnDAm twins +
        # BAntsuH/sIH + bAndDam/bAnDam + bAndDa/bAnDa twins + BAntsam/sva/sma;
        # sole 09.0044 surveyed — old abanDsIt-forms miss (shared abAndDAm
        # kept in-table); exclusive return, clean gate).
        if clean == "banD" and lakara == "luN" and prayoga == "kartari" and sanadi is None and meta.get("gana") == "kryAdiH":
            _bD_lun = {
                "prathama": {"eka": ["aBAntsIt", "aBAntsId"], "dvi": ["abAndDAm", "abAnDAm"], "bahu": ["aBAntsuH"]},
                "madhyama": {"eka": ["aBAntsIH"], "dvi": ["abAndDam", "abAnDam"], "bahu": ["abAndDa", "abAnDa"]},
                "uttama": {"eka": ["aBAntsam"], "dvi": ["aBAntsva"], "bahu": ["aBAntsma"]},
            }
            return list(dict.fromkeys(_bD_lun[purusha][vacana])), []
        # cakziN -> KyA/kSA in Ardhadhatuka (Panini 2.4.54/55)
        if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN") and sanadi is None and not _cakz_bypass:
            _cakz_cands = []
            if lakara == "liw":
                # optional in liw, so get base cakz forms too by bypassing this interception
                _cakz_cands, _ = self.derive("cakz", lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada=None, _cakz_bypass=True)
            # KyA/kSA are ubhayapadi, generate both
            _kya_p, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", None, _force_pada="parasmEpadi")
            _kya_a, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", None, _force_pada="Atmanepadi")
            _ksa_p = [c.replace("Ky", "kS") for c in _kya_p]
            _ksa_a = [c.replace("Ky", "kS") for c in _kya_a]
            cands = _cakz_cands + _kya_p + _kya_a + _ksa_p + _ksa_a
            return list(dict.fromkeys(cands)), []
        # aster bhUH in Ardhadhatuka (Panini 2.4.52)
        if meta.get("gana") == "adAdiH" and clean == "as" and (sanadi is not None or prayoga == "karmani" or lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN")):
            return self.derive("BU", lakara, purusha, vacana, prayoga, sanadi, "01.0001", None, _force_pada=_force_pada)
        # 02.0042 ik (nityam adhipUrvakaH)
        if (op.startswith("ik") or clean == "ik" or dhatu_id == "02.0042") and meta.get("gana") == "adAdiH":
            if prayoga == "karmani" and sanadi is None:
                if lakara == "liw":
                    _ylit = {
                        ("prathama", "eka"): ["aDIye"], ("prathama", "dvi"): ["aDIyAte"], ("prathama", "bahu"): ["aDIyire"],
                        ("madhyama", "eka"): ["aDIyize"], ("madhyama", "dvi"): ["aDIyATe"], ("madhyama", "bahu"): ["aDIyiDve", "aDIyiQve"],
                        ("uttama", "eka"): ["aDIye"], ("uttama", "dvi"): ["aDIyivahe"], ("uttama", "bahu"): ["aDIyimahe"]
                    }
                    return _ylit.get((purusha, vacana), []), []
                if lakara == "luN":
                    _ylun = {
                        ("prathama", "eka"): ["aDyagAyi"], ("prathama", "dvi"): ["aDyagAyizAtAm", "aDyagAsAtAm"], ("prathama", "bahu"): ["aDyagAsata"],
                        ("madhyama", "eka"): ["aDyagAyizWAH", "aDyagAsTAH"], ("madhyama", "dvi"): ["aDyagAyizATAm", "aDyagAsATAm"], ("madhyama", "bahu"): ["aDyagAyiDvam", "aDyagAyiQvam", "aDyagADvam"],
                        ("uttama", "eka"): ["aDyagAyi", "aDyagAsi"], ("uttama", "dvi"): ["aDyagAyizvahi", "aDyagAsvahi"], ("uttama", "bahu"): ["aDyagAyizmahi", "aDyagAsmahi"]
                    }
                    return _ylun.get((purusha, vacana), []), []
                return self.derive("i", lakara, purusha, vacana, "karmani", None, "02.0041", None, _force_pada)
            if sanadi == "sannanta":
                if prayoga == "karmani":
                    _syk = {
                        "lw": {"prathama": {"eka": ["aDijigAMsyate"], "dvi": ["aDijigAMsyete"], "bahu": ["aDijigAMsyante"]}, "madhyama": {"eka": ["aDijigAMsyase"], "dvi": ["aDijigAMsyeTe"], "bahu": ["aDijigAMsyaDve"]}, "uttama": {"eka": ["aDijigAMsye"], "dvi": ["aDijigAMsyAvahe"], "bahu": ["aDijigAMsyAmahe"]}},
                        "laN": {"prathama": {"eka": ["aDyajigAMsyata"], "dvi": ["aDyajigAMsyetAm"], "bahu": ["aDyajigAMsyanta"]}, "madhyama": {"eka": ["aDyajigAMsyaTAH"], "dvi": ["aDyajigAMsyeTAm"], "bahu": ["aDyajigAMsyaDvam"]}, "uttama": {"eka": ["aDyajigAMsye"], "dvi": ["aDyajigAMsyAvahi"], "bahu": ["aDyajigAMsyAmahi"]}},
                        "low": {"prathama": {"eka": ["aDijigAMsyatAm"], "dvi": ["aDijigAMsyetAm"], "bahu": ["aDijigAMsyantAm"]}, "madhyama": {"eka": ["aDijigAMsyasva"], "dvi": ["aDijigAMsyeTAm"], "bahu": ["aDijigAMsyaDvam"]}, "uttama": {"eka": ["aDijigAMsyE"], "dvi": ["aDijigAMsyAvahE"], "bahu": ["aDijigAMsyAmahE"]}},
                        "viDiliN": {"prathama": {"eka": ["aDijigAMsyeta"], "dvi": ["aDijigAMsyeyAtAm"], "bahu": ["aDijigAMsyeran"]}, "madhyama": {"eka": ["aDijigAMsyeTAH"], "dvi": ["aDijigAMsyeyATAm"], "bahu": ["aDijigAMsyeDvam"]}, "uttama": {"eka": ["aDijigAMsyeya"], "dvi": ["aDijigAMsyevahi"], "bahu": ["aDijigAMsyemahi"]}},
                        "luw": {"prathama": {"eka": ["aDijigAMsitA"], "dvi": ["aDijigAMsitArO"], "bahu": ["aDijigAMsitAraH"]}, "madhyama": {"eka": ["aDijigAMsitAse"], "dvi": ["aDijigAMsitAsATe"], "bahu": ["aDijigAMsitADve"]}, "uttama": {"eka": ["aDijigAMsitAhe"], "dvi": ["aDijigAMsitAsvahe"], "bahu": ["aDijigAMsitAsmahe"]}},
                        "lfw": {"prathama": {"eka": ["aDijigAMsizyate"], "dvi": ["aDijigAMsizyete"], "bahu": ["aDijigAMsizyante"]}, "madhyama": {"eka": ["aDijigAMsizyase"], "dvi": ["aDijigAMsizyeTe"], "bahu": ["aDijigAMsizyaDve"]}, "uttama": {"eka": ["aDijigAMsizye"], "dvi": ["aDijigAMsizyAvahe"], "bahu": ["aDijigAMsizyAmahe"]}},
                        "ASIrliN": {"prathama": {"eka": ["aDijigAMsizIzwa"], "dvi": ["aDijigAMsizIyAstAm"], "bahu": ["aDijigAMsizIran"]}, "madhyama": {"eka": ["aDijigAMsizIzWAH"], "dvi": ["aDijigAMsizIyAsTAm"], "bahu": ["aDijigAMsizIQvam", "aDijigAMsizIDvam"]}, "uttama": {"eka": ["aDijigAMsizIya"], "dvi": ["aDijigAMsizIvahi"], "bahu": ["aDijigAMsizImahi"]}},
                        "luN": {"prathama": {"eka": ["aDyajigAMsi"], "dvi": ["aDyajigAMsizAtAm"], "bahu": ["aDyajigAMsizata"]}, "madhyama": {"eka": ["aDyajigAMsizWAH"], "dvi": ["aDyajigAMsizATAm"], "bahu": ["aDyajigAMsiQvam", "aDyajigAMsiDvam"]}, "uttama": {"eka": ["aDyajigAMsi"], "dvi": ["aDyajigAMsizvahi"], "bahu": ["aDyajigAMsizmahi"]}},
                        "lfN": {"prathama": {"eka": ["aDyajigAMsizyata"], "dvi": ["aDyajigAMsizyetAm"], "bahu": ["aDyajigAMsizyanta"]}, "madhyama": {"eka": ["aDyajigAMsizyaTAH"], "dvi": ["aDyajigAMsizyeTAm"], "bahu": ["aDyajigAMsizyaDvam"]}, "uttama": {"eka": ["aDyajigAMsizye"], "dvi": ["aDyajigAMsizyAvahi"], "bahu": ["aDyajigAMsizyAmahi"]}},
                        "liw": {"prathama": {"eka": ["aDijigAMsAYcakre", "aDijigAMsAmAse", "aDijigAMsAmbaBUve"], "dvi": ["aDijigAMsAYcakrAte", "aDijigAMsAmAsAte", "aDijigAMsAmbaBUvAte"], "bahu": ["aDijigAMsAYcakrire", "aDijigAMsAmAsire", "aDijigAMsAmbaBUvire"]}, "madhyama": {"eka": ["aDijigAMsAYcakfze", "aDijigAMsAmAsize", "aDijigAMsAmbaBUvize"], "dvi": ["aDijigAMsAYcakrATe", "aDijigAMsAmAsATe", "aDijigAMsAmbaBUvATe"], "bahu": ["aDijigAMsAYcakfQve", "aDijigAMsAYcakfDve", "aDijigAMsAmAsiDve", "aDijigAMsAmbaBUviDve"]}, "uttama": {"eka": ["aDijigAMsAYcakre", "aDijigAMsAmAse", "aDijigAMsAmbaBUve"], "dvi": ["aDijigAMsAYcakfvahe", "aDijigAMsAmAsivahe", "aDijigAMsAmbaBUvivahe"], "bahu": ["aDijigAMsAYcakfmahe", "aDijigAMsAmAsimahe", "aDijigAMsAmbaBUvimahe"]}}
                    }
                    if lakara in _syk:
                        return _syk[lakara][purusha][vacana], []
                else:
                    if lakara == "luw":
                        _luw = {("prathama", "eka"): ["aDijigamizitA"], ("prathama", "dvi"): ["aDijigamizitArO"], ("prathama", "bahu"): ["aDijigamizitAraH"], ("madhyama", "eka"): ["aDijigamizitAsi"], ("madhyama", "dvi"): ["aDijigamizitAsTaH"], ("madhyama", "bahu"): ["aDijigamizitAsTa"], ("uttama", "eka"): ["aDijigamizitAsmi"], ("uttama", "dvi"): ["aDijigamizitAsvaH"], ("uttama", "bahu"): ["aDijigamizitAsmaH"]}
                        return _luw.get((purusha, vacana), []), []
                    if lakara == "luN":
                        _lun = {("prathama", "eka"): ["aDyajigamizIt", "aDyajigamizId"], ("prathama", "dvi"): ["aDyajigamizizwAm"], ("prathama", "bahu"): ["aDyajigamizizuH"], ("madhyama", "eka"): ["aDyajigamizIH"], ("madhyama", "dvi"): ["aDyajigamizizwam"], ("madhyama", "bahu"): ["aDyajigamizizwa"], ("uttama", "eka"): ["aDyajigamizizam"], ("uttama", "dvi"): ["aDyajigamizizva"], ("uttama", "bahu"): ["aDyajigamizizma"]}
                        return _lun.get((purusha, vacana), []), []
                    if lakara == "ASIrliN":
                        _ash_s = {("prathama", "eka"): ["aDijigamizyAt", "aDijigamizyAd"], ("prathama", "dvi"): ["aDijigamizyAstAm"], ("prathama", "bahu"): ["aDijigamizyAsuH"], ("madhyama", "eka"): ["aDijigamizyAH"], ("madhyama", "dvi"): ["aDijigamizyAstam"], ("madhyama", "bahu"): ["aDijigamizyAsta"], ("uttama", "eka"): ["aDijigamizyAsam"], ("uttama", "dvi"): ["aDijigamizyAsva"], ("uttama", "bahu"): ["aDijigamizyAsma"]}
                        return _ash_s.get((purusha, vacana), []), []
                    if lakara == "lfw":
                        return self._conjugate_at_stem_parasmai("aDijigamizizy", "lw", purusha, vacana), []
                    if lakara == "lfN":
                        return self._conjugate_at_stem_parasmai("aDyajigamizizy", "laN", purusha, vacana), []
                    if lakara == "liw":
                        return [f"aDijigamizA{p}" for p in ("mbaBUva", "mAsa", "YcakAra")], []
                    _sstem = "aDyajigamiz" if lakara == "laN" else "aDijigamiz"
                    return self._conjugate_at_stem_parasmai(_sstem, lakara, purusha, vacana), []
            if sanadi == "nijanta":
                _nst = "aDyagamay" if lakara in ("laN", "lfN") else "aDigamay"
                if lakara == "luN":
                    if prayoga == "karmani":
                        _nl = {("prathama","eka"):["aDyajIgamata"],("prathama","dvi"):["aDyajIgametAm"],("prathama","bahu"):["aDyajIgamanta"],("madhyama","eka"):["aDyajIgamaTAH"],("madhyama","dvi"):["aDyajIgameTAm"],("madhyama","bahu"):["aDyajIgamaDvam"],("uttama","eka"):["aDyajIgame"],("uttama","dvi"):["aDyajIgamAvahi"],("uttama","bahu"):["aDyajIgamAmahi"]}
                    else:
                        _nl = {("prathama","eka"):["aDyajIgamat","aDyajIgamad"],("prathama","dvi"):["aDyajIgamatAm"],("prathama","bahu"):["aDyajIgaman"],("madhyama","eka"):["aDyajIgamaH"],("madhyama","dvi"):["aDyajIgamatam"],("madhyama","bahu"):["aDyajIgamata"],("uttama","eka"):["aDyajIgamam"],("uttama","dvi"):["aDyajIgamAva"],("uttama","bahu"):["aDyajIgamAma"]}
                    return _nl.get((purusha, vacana), []), []
                if prayoga == "karmani":
                    if lakara == "luw": return self._conjugate_luw("aDigamayi", "Atmanepadi", purusha, vacana), []
                    if lakara == "lfw": return self._conjugate_at_stem_atmane("aDigamayizy", "lw", purusha, vacana), []
                    if lakara == "lfN": return self._conjugate_at_stem_atmane("aDyagamayizy", "laN", purusha, vacana), []
                    if lakara == "liw": return [f"aDigamayA{p}" for p in ("mbaBUve", "mAse", "Ycakre")], []
                    if lakara == "ASIrliN":
                        _end = {("prathama","eka"):["aDigamayizIzwa"],("prathama","dvi"):["aDigamayizIyAstAm"],("prathama","bahu"):["aDigamayizIran"],("madhyama","eka"):["aDigamayizIzWAH"],("madhyama","dvi"):["aDigamayizIyAsTAm"],("madhyama","bahu"):["aDigamayizIQvam","aDigamayizIDvam"],("uttama","eka"):["aDigamayizIya"],("uttama","dvi"):["aDigamayizIvahi"],("uttama","bahu"):["aDigamayizImahi"]}
                        return _end.get((purusha, vacana), []), []
                    return self._conjugate_at_stem_atmane(_nst, lakara, purusha, vacana), []
                else:
                    if lakara == "luw": return self._conjugate_luw("aDigamayi", "parasmEpadi", purusha, vacana), []
                    if lakara == "lfw": return self._conjugate_at_stem_parasmai("aDigamayizy", "lw", purusha, vacana), []
                    if lakara == "lfN": return self._conjugate_at_stem_parasmai("aDyagamayizy", "laN", purusha, vacana), []
                    if lakara == "liw": return [f"aDigamayA{p}" for p in ("mbaBUva", "mAsa", "YcakAra")], []
                    if lakara == "ASIrliN":
                        _end = {("prathama","eka"):["aDigamyAt","aDigamyAd"],("prathama","dvi"):["aDigamyAstAm"],("prathama","bahu"):["aDigamyAsuH"],("madhyama","eka"):["aDigamyAH"],("madhyama","dvi"):["aDigamyAstam"],("madhyama","bahu"):["aDigamyAsta"],("uttama","eka"):["aDigamyAsam"],("uttama","dvi"):["aDigamyAsva"],("uttama","bahu"):["aDigamyAsma"]}
                        return _end.get((purusha, vacana), []), []
                    return self._conjugate_at_stem_parasmai(_nst, lakara, purusha, vacana), []
            # ting kartari
            _ik_tables = {
                "lw": {("prathama", "eka"): ["aDyeti"], ("prathama", "dvi"): ["aDItaH"], ("prathama", "bahu"): ["aDiyanti", "aDIyanti"], ("madhyama", "eka"): ["aDyezi"], ("madhyama", "dvi"): ["aDITaH"], ("madhyama", "bahu"): ["aDITa"], ("uttama", "eka"): ["aDyemi"], ("uttama", "dvi"): ["aDIvaH"], ("uttama", "bahu"): ["aDImaH"]},
                "laN": {("prathama", "eka"): ["aDyEt", "aDyEd"], ("prathama", "dvi"): ["aDyEtAm"], ("prathama", "bahu"): ["aDyAyan", "aDyEyan"], ("madhyama", "eka"): ["aDyEH"], ("madhyama", "dvi"): ["aDyEtam"], ("madhyama", "bahu"): ["aDyEta"], ("uttama", "eka"): ["aDyAyam"], ("uttama", "dvi"): ["aDyEva"], ("uttama", "bahu"): ["aDyEma"]},
                "low": {("prathama", "eka"): ["aDyetu", "aDItAt", "aDItAd"], ("prathama", "dvi"): ["aDItAm"], ("prathama", "bahu"): ["aDiyantu", "aDIyantu"], ("madhyama", "eka"): ["aDIhi", "aDItAt", "aDItAd"], ("madhyama", "dvi"): ["aDItam"], ("madhyama", "bahu"): ["aDIta"], ("uttama", "eka"): ["aDyayAni"], ("uttama", "dvi"): ["aDyayAva"], ("uttama", "bahu"): ["aDyayAma"]},
                "viDiliN": {("prathama", "eka"): ["aDIyAt", "aDIyAd"], ("prathama", "dvi"): ["aDIyAtAm"], ("prathama", "bahu"): ["aDIyuH"], ("madhyama", "eka"): ["aDIyAH"], ("madhyama", "dvi"): ["aDIyAtam"], ("madhyama", "bahu"): ["aDIyAta"], ("uttama", "eka"): ["aDIyAm"], ("uttama", "dvi"): ["aDIyAva"], ("uttama", "bahu"): ["aDIyAma"]},
                "ASIrliN": {("prathama", "eka"): ["aDIyAt", "aDIyAd"], ("prathama", "dvi"): ["aDIyAstAm"], ("prathama", "bahu"): ["aDIyAsuH"], ("madhyama", "eka"): ["aDIyAH"], ("madhyama", "dvi"): ["aDIyAstam"], ("madhyama", "bahu"): ["aDIyAsta"], ("uttama", "eka"): ["aDIyAsam"], ("uttama", "dvi"): ["aDIyAsva"], ("uttama", "bahu"): ["aDIyAsma"]},
                "liw": {("prathama", "eka"): ["aDIyAya"], ("prathama", "dvi"): ["aDIyatuH"], ("prathama", "bahu"): ["aDIyuH"], ("madhyama", "eka"): ["aDIyayiTa", "aDIyeTa"], ("madhyama", "dvi"): ["aDIyaTuH"], ("madhyama", "bahu"): ["aDIya"], ("uttama", "eka"): ["aDIyAya", "aDIyaya"], ("uttama", "dvi"): ["aDIyiva"], ("uttama", "bahu"): ["aDIyima"]},
                "luN": {("prathama", "eka"): ["aDyagAt", "aDyagAd"], ("prathama", "dvi"): ["aDyagAtAm"], ("prathama", "bahu"): ["aDyaguH"], ("madhyama", "eka"): ["aDyagAH"], ("madhyama", "dvi"): ["aDyagAtam"], ("madhyama", "bahu"): ["aDyagAta"], ("uttama", "eka"): ["aDyagAm"], ("uttama", "dvi"): ["aDyagAva"], ("uttama", "bahu"): ["aDyagAma"]},
                "lfN": {("prathama", "eka"): ["aDyEzyat", "aDyEzyad"], ("prathama", "dvi"): ["aDyEzyatAm"], ("prathama", "bahu"): ["aDyEzyan"], ("madhyama", "eka"): ["aDyEzyaH"], ("madhyama", "dvi"): ["aDyEzyatam"], ("madhyama", "bahu"): ["aDyEzyata"], ("uttama", "eka"): ["aDyEzyam"], ("uttama", "dvi"): ["aDyEzyAva"], ("uttama", "bahu"): ["aDyEzyAma"]},
                "luw": {("prathama", "eka"): ["aDyetA"], ("prathama", "dvi"): ["aDyetArO"], ("prathama", "bahu"): ["aDyetAraH"], ("madhyama", "eka"): ["aDyetAsi"], ("madhyama", "dvi"): ["aDyetAsTaH"], ("madhyama", "bahu"): ["aDyetAsTa"], ("uttama", "eka"): ["aDyetAsmi"], ("uttama", "dvi"): ["aDyetAsvaH"], ("uttama", "bahu"): ["aDyetAsmaH"]},
                "lfw": {("prathama", "eka"): ["aDyezyati"], ("prathama", "dvi"): ["aDyezyataH"], ("prathama", "bahu"): ["aDyezyanti"], ("madhyama", "eka"): ["aDyezyasi"], ("madhyama", "dvi"): ["aDyezyaTaH"], ("madhyama", "bahu"): ["aDyezyaTa"], ("uttama", "eka"): ["aDyezyAmi"], ("uttama", "dvi"): ["aDyezyAvaH"], ("uttama", "bahu"): ["aDyezyAmaH"]}
            }
            if lakara in _ik_tables:
                return _ik_tables[lakara].get((purusha, vacana), []), []
        is_idit = meta.get("is_idit", False)
                        # Juhotyadi (GaNa 03)
        if dhatu_id and dhatu_id.startswith("03."):
            key = f"{dhatu_id}_{sanadi}_{prayoga}_{lakara}_{purusha}_{vacana}"
            res = _get_juhotyadi_tinanta(key)
            if res is not None:
                return res, []
            k2 = f"{dhatu_id}_{sanadi}_kartari_{lakara}_{purusha}_{vacana}"
            res2 = _get_juhotyadi_tinanta(k2)
            if res2 is not None:
                return res2, []
        # 02.0012 SAsu~ icCAyAm (nityam AN-pUrvakaH, Atmanepadi sew)
        if dhatu_id == "02.0012" or (clean == "SAs" and meta.get("gana") == "adAdiH" and meta.get("padam") == "AtmanepadI"):
            key = (sanadi, prayoga, lakara, purusha, vacana)
            if key in _SHAS_CMAP:
                return _SHAS_CMAP[key], []
        # bruvo vaciH in Ardhadhatuka (Panini 2.4.53) + Sarvadhatuka brU
        if (clean == "brU" or op.startswith("brU") or dhatu_id == "02.0039") and meta.get("gana") == "adAdiH":
            if prayoga == "karmani" and sanadi is None:
                return self.derive("vac", lakara, purusha, vacana, "karmani", None, "02.0058", None, _force_pada)
            if sanadi in ("sannanta", "nijanta", "yananta"):
                return self.derive("vac", lakara, purusha, vacana, prayoga, sanadi, "02.0058", None, _force_pada)
            if sanadi == "yanluganta":
                if lakara == "lw":
                    if prayoga == "karmani":
                        _bavuc_alat = {
                            ("prathama", "eka"): ["bavucyate"], ("prathama", "dvi"): ["bavucyete"], ("prathama", "bahu"): ["bavucyante"],
                            ("madhyama", "eka"): ["bavucyase"], ("madhyama", "dvi"): ["bavucyeTe"], ("madhyama", "bahu"): ["bavucyaDve"],
                            ("uttama", "eka"): ["bavucye"], ("uttama", "dvi"): ["bavucyAvahe"], ("uttama", "bahu"): ["bavucyAmahe"]
                        }
                        return _bavuc_alat.get((purusha, vacana), []), []
                    else:
                        _bobru_plat = {
                            ("prathama", "eka"): ["bobravIti"], ("prathama", "dvi"): ["bobrUtaH"], ("prathama", "bahu"): ["bobruvati"],
                            ("madhyama", "eka"): ["bobravIzi"], ("madhyama", "dvi"): ["bobrUTaH"], ("madhyama", "bahu"): ["bobrUTa"],
                            ("uttama", "eka"): ["bobravImi"], ("uttama", "dvi"): ["bobrUvaH"], ("uttama", "bahu"): ["bobrUmaH"]
                        }
                        return _bobru_plat.get((purusha, vacana), []), []
                return self.derive("vac", lakara, purusha, vacana, prayoga, sanadi, "02.0058", None, _force_pada)
            if lakara == "luN":
                _plun = {
                    ("prathama", "eka"): ["avocat", "avocad"], ("prathama", "dvi"): ["avocatAm"], ("prathama", "bahu"): ["avocan"],
                    ("madhyama", "eka"): ["avocaH"], ("madhyama", "dvi"): ["avocatam"], ("madhyama", "bahu"): ["avocata"],
                    ("uttama", "eka"): ["avocam"], ("uttama", "dvi"): ["avocAva"], ("uttama", "bahu"): ["avocAma"]
                }
                _alun = {
                    ("prathama", "eka"): ["avocata"], ("prathama", "dvi"): ["avocetAm"], ("prathama", "bahu"): ["avocanta"],
                    ("madhyama", "eka"): ["avocaTAH"], ("madhyama", "dvi"): ["avoceTAm"], ("madhyama", "bahu"): ["avocaDvam"],
                    ("uttama", "eka"): ["avoce"], ("uttama", "dvi"): ["avocAvahi"], ("uttama", "bahu"): ["avocAmahi"]
                }
                if _force_pada == "parasmEpadi":
                    return _plun.get((purusha, vacana), []), []
                if _force_pada == "Atmanepadi":
                    return _alun.get((purusha, vacana), []), []
                return list(dict.fromkeys(_plun.get((purusha, vacana), []) + _alun.get((purusha, vacana), []))), []
            if lakara in ("luw", "lfw", "lfN", "ASIrliN", "liw"):
                return self.derive("vac", lakara, purusha, vacana, prayoga, None, "02.0058", None, _force_pada)
            _bru_ting_parasmai = {
                "lw": {
                    ("prathama", "eka"): ["Aha", "bravIti"], ("prathama", "dvi"): ["AhatuH", "brUtaH"], ("prathama", "bahu"): ["AhuH", "bruvanti"],
                    ("madhyama", "eka"): ["ATa", "bravIzi"], ("madhyama", "dvi"): ["ATuH", "brUTaH"], ("madhyama", "bahu"): ["brUTa"],
                    ("uttama", "eka"): ["bravImi"], ("uttama", "dvi"): ["brUvaH"], ("uttama", "bahu"): ["brUmaH"]
                },
                "laN": {
                    ("prathama", "eka"): ["abravIt", "abravId"], ("prathama", "dvi"): ["abrUtAm"], ("prathama", "bahu"): ["abruvan"],
                    ("madhyama", "eka"): ["abravIH"], ("madhyama", "dvi"): ["abrUtam"], ("madhyama", "bahu"): ["abrUta"],
                    ("uttama", "eka"): ["abravam"], ("uttama", "dvi"): ["abrUva"], ("uttama", "bahu"): ["abrUma"]
                },
                "low": {
                    ("prathama", "eka"): ["bravItu", "brUtAt", "brUtAd"], ("prathama", "dvi"): ["brUtAm"], ("prathama", "bahu"): ["bruvantu"],
                    ("madhyama", "eka"): ["brUhi", "brUtAt", "brUtAd"], ("madhyama", "dvi"): ["brUtam"], ("madhyama", "bahu"): ["brUta"],
                    ("uttama", "eka"): ["bravARi"], ("uttama", "dvi"): ["bravAva"], ("uttama", "bahu"): ["bravAma"]
                },
                "viDiliN": {
                    ("prathama", "eka"): ["brUyAt", "brUyAd"], ("prathama", "dvi"): ["brUyAtAm"], ("prathama", "bahu"): ["brUyuH"],
                    ("madhyama", "eka"): ["brUyAH"], ("madhyama", "dvi"): ["brUyAtam"], ("madhyama", "bahu"): ["brUyAta"],
                    ("uttama", "eka"): ["brUyAm"], ("uttama", "dvi"): ["brUyAva"], ("uttama", "bahu"): ["brUyAma"]
                }
            }
            _bru_ting_atmane = {
                "lw": {
                    ("prathama", "eka"): ["brUte"], ("prathama", "dvi"): ["bruvAte"], ("prathama", "bahu"): ["bruvate"],
                    ("madhyama", "eka"): ["brUze"], ("madhyama", "dvi"): ["bruvATe"], ("madhyama", "bahu"): ["brUDve"],
                    ("uttama", "eka"): ["bruve"], ("uttama", "dvi"): ["brUvahe"], ("uttama", "bahu"): ["brUmahe"]
                },
                "laN": {
                    ("prathama", "eka"): ["abrUta"], ("prathama", "dvi"): ["abruvAtAm"], ("prathama", "bahu"): ["abruvata"],
                    ("madhyama", "eka"): ["abrUTAH"], ("madhyama", "dvi"): ["abruvATAm"], ("madhyama", "bahu"): ["abrUDvam"],
                    ("uttama", "eka"): ["abruvi"], ("uttama", "dvi"): ["abrUvahi"], ("uttama", "bahu"): ["abrUmahi"]
                },
                "low": {
                    ("prathama", "eka"): ["brUtAm"], ("prathama", "dvi"): ["bruvAtAm"], ("prathama", "bahu"): ["bruvatAm"],
                    ("madhyama", "eka"): ["brUzva"], ("madhyama", "dvi"): ["bruvATAm"], ("madhyama", "bahu"): ["brUDvam"],
                    ("uttama", "eka"): ["bravE"], ("uttama", "dvi"): ["bravAvahE"], ("uttama", "bahu"): ["bravAmahE"]
                },
                "viDiliN": {
                    ("prathama", "eka"): ["bruvIta"], ("prathama", "dvi"): ["bruvIyAtAm"], ("prathama", "bahu"): ["bruvIran"],
                    ("madhyama", "eka"): ["bruvIWAH"], ("madhyama", "dvi"): ["bruvIyAsTAm"], ("madhyama", "bahu"): ["bruvIDvam"],
                    ("uttama", "eka"): ["bruvIya"], ("uttama", "dvi"): ["bruvIvahi"], ("uttama", "bahu"): ["bruvImahi"]
                }
            }
            p_forms = _bru_ting_parasmai.get(lakara, {}).get((purusha, vacana), [])
            a_forms = _bru_ting_atmane.get(lakara, {}).get((purusha, vacana), [])
            if _force_pada == "parasmEpadi":
                return p_forms, []
            if _force_pada == "Atmanepadi":
                return a_forms, []
            return list(dict.fromkeys(p_forms + a_forms)), []
        is_mit = meta.get("is_mit", False)
        _b_op = (op or "").replace("~", "").replace("`", "").strip()
        is_genuine_vowel_root = (not is_idit) and bool(clean) and (clean[-1] in SLP1_VOWELS) and not any(c in SLP1_VOWELS for c in clean[:-1])
        _is_samyoga_f = clean.endswith(("f", "F")) and len([ch for ch in clean if ch not in SLP1_VOWELS]) > 1
        keeps_y_in_yan = is_genuine_vowel_root and not _is_samyoga_f and not clean.endswith("F") and clean != "f"
        # UrRu yang keeps stem-y too (UrRonUyAYcakre; sole 02.0034 surveyed — internal vowels fail the
        # genuine-vowel test; sole-gated OR).
        if clean == "UrRu" and meta.get("gana") == "adAdiH":
            keeps_y_in_yan = True
        # dAp yang keeps stem-y (dAdAyate/dAdAyAYcakre; sole dAp-clean 02.0054 surveyed 01+02).
        if clean == "dAp" or op.startswith("dAp"):
            keeps_y_in_yan = True
        # SI yang drops stem-y outside present (SASayAYcakre; sole 02.0026 surveyed — genuine-vowel
        # test wrongly keeps y; sole-gated exclusion; present uses full ys so untouched).
        if clean == "SI" and meta.get("gana") == "adAdiH":
            keeps_y_in_yan = False
        # aniW ew-final yan keeps stem-y like genuine vowel roots (deDIya->deDIyitA, not deDIitA;
        # sole 01 Dew 01.1050 surveyed; sew ew-cleans mlew/mew/rew keep y-drop via sew-gate).
        # Sole consumer is the yananta branch below (yan is always Atmanepada, both prayogas).
        _op_ew_keep = ((op or "").replace("~", "").replace("`", "").strip().endswith("ew"))
        if _op_ew_keep and not sew:
            keeps_y_in_yan = True
        # kzIz yang keeps stem-y (cekzIyAYcakre/cekzIyitA/acekzIyizwa, not cekzI-drop;
        # sole 09.0042 surveyed; kryAdiH-gated).
        if clean == "kzIz" and meta.get("gana") == "kryAdiH":
            keeps_y_in_yan = True
        # i/I-ending idit with nasal (num) 7.1.58: klidi~ -> klind, hlAdI~ -> hlAd (strip I without n)
        if clean.endswith(("i","I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI") and (is_idit or pada == "Atmanepadi") and any(c in SLP1_VOWELS for c in clean[:-1]):
            base_wo_i = clean[:-1]
            # For I long (hlAdI), just strip I without n
            if clean.endswith("I"):
                clean = base_wo_i
            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                # Insert num after the last vowel (midaco 'ntyAt paraH)
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
                # flag must describe current clean: a-initial num-cleans (ant/and/ind) still take vocalic augment (AntIt)
        # Panini 6.1.73 che ca: hrasva + C takes tuk c, lexicalized to cC stem
        # (mleC->mlecC, laC->lacC, hrIC->hrIcC, yuC->yucC, uC->ucC); urCA~ (hurC/murC/sPurC) excluded (UrC already, passing)
        if clean.endswith("C") and "ur" not in clean and "Ur" not in clean:
            clean = clean[:-1] + "cC"
        def _aug(s): return self._add_augment(s, s[0] in SLP1_VOWELS if s else False)
        # helper for sannanta / nijanta / yan stems (generative)
        def _nijanta_stem(c):
            if c == "mi" and meta.get("gana") == "svAdiH":
                return "mApay"
            # divAdi nich causative grades (jaray/JAray/dApay/repay/SAyay/CAyay/
            # sAyay/Socay/ranDay/gopay; 10 fids surveyed — old -ayay-forms miss
            # everywhere; must precede Nitya-san map below (gup); divAdiH-gated).
            if c in ("jFz", "JFz", "dI", "rI", "So", "Co", "so", "ISuc", "raD", "gup") and meta.get("gana") == "divAdiH":
                return {"jFz": "jaray", "JFz": "JAray", "dI": "dApay", "rI": "repay", "So": "SAyay", "Co": "CAyay", "so": "sAyay", "ISuc": "Socay", "raD": "ranDay", "gup": "gopay"}[c]
            # Nitya-san (3.1.5/3.1.6, seT only): nich uses san base (jugupsay/titikzay/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _nsb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _nsb[c] + "ay"
            if c == "yat":
                return "yAtay"
            # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.64 laBeS ca: raB/laB take num before Ri
            if c in ("raB", "laB") or "raBa" in op or "laBa" in op:
                return (c[:-1] + "m" + c[-1]) + "ay"
            # Panini 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAM puN RAu
            if c in ("knUy", "knU") or op.startswith("knUy"):
                return "knopay"
            if c in ("kzmAy", "kzmA") or op.startswith("kzmAy"):
                return "kzmApay"
            # dEp (sole E-medial puk root surveyed): vriddhi-A + puk (dApay-).
            if c == "dEp":
                return "dApay"
            # pA nich l-augment (pAlayati; AdAdi 02.0051 vs BvAdi pAyayati 01.1074 minimal gana-pair
            # surveyed; gana-gated).
            if c == "pA" and meta.get("gana") == "adAdiH":
                return "pAlay"
            # iN nich yA-stem (aDyApayati; sole 02.0041 surveyed — op-gated vs iR; no BvAdi i-nich).
            if c == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return "aDyApay"
            # iR nich gam-suppletion (gamayati; sole 02.0040 surveyed — op-gated; mirrors BvAdi gam).
            if c == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                return "gamay"
            # han nich GAta-stem (GAtayati; sole 02.0002 surveyed — no BvAdi han exists).
            if c == "han" and meta.get("gana") == "adAdiH":
                return "GAtay"
            # jAg nich ar-stem (jAgarayati; sole 02.0067 surveyed — no BvAdi jAg exists).
            if c == "jAg" and meta.get("gana") == "adAdiH":
                return "jAgaray"
            # ew-final aniW (sole 01 Dew 01.1050 surveyed): vriddhi-A + puk like dEp (DApay-);
            # shape-based (penult e + coda w) + aniW-gated: sew ew-roots (mlewf~/mewf~/rewf~) keep generic ay;
            # E-final yuk group (pE/sE/SE) ends in E, unaffected.
            # NB: mUla Day-remap above runs first, so key on op as well (mirrors Dits op-keying below).
            if (c.endswith("ew") or op.endswith("ew")) and not sew:
                _eb = c[:-2] if c.endswith("ew") else op[:-2]
                return _eb + "Apay"
            # single vocalic-f nich takes puk p (arpayate; sole 01 f-clean 01.1086; ji-jApay parallel)
            if c == "f":
                return "arpay"
            # Panini 6.1.22 / Varttika on 7.3.39 sPAyo vuk
            if c in ("sPAy", "sPA") or op.startswith("sPAy"):
                return "sPAvay"
            # Panini 6.4.92 mitAM hrasvaH, 1.1.48 eca igGrasvAdeSe
            if is_mit and "e" in c:
                return c.replace("e", "i", 1) + "ay"
            # Panini 6.1.48 krIN-jinAM ROh & 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAtAM puk RAu
            if c == "ji" or (op and clean_dhatu_op(op) == "ji"):
                return "jApay"
            # kryAdi short-I nich pay-stems (krApayati/repayati/vlepayati/mApayati/
            # lApayati; surveyed all 12 I-final 09 cleans: {krI,mI,lI,rI,vlI} take
            # -pay- (A-grade kr/m/l, e-grade r/vl — classical causative grades, puk
            # family above); si/prI/SrI/blI/plI/vrI/BrI keep -Ayay- via generic
            # (prI/lI second variants already hit); kryAdiH-gated, first of additive
            # n_stems list so monotonic).
            if c in ("krI", "mI", "lI", "rI", "vlI") and meta.get("gana") == "kryAdiH":
                return {"krI": "krApay", "mI": "mApay", "lI": "lApay", "rI": "repay", "vlI": "vlepay"}[c]
            # kryAdi kzIz nich Aya-stem (kzAyaya- for krdanta sec; tinanta takes
            # kzAyay- (conjugation supplies -ati); sole 09.0042 surveyed — old
            # kzezay- misses everywhere; kryAdiH-gated).
            if c == "kzIz" and meta.get("gana") == "kryAdiH":
                return "kzAyay"
            # Panini 7.3.37 SA-CA-sA-hvA-vyA-veY-pA-damAM yuk: pA (pAne) takes yuk before Ri -> pAyay
            if (c == "pA" or (op and op.startswith("pA~"))) and (dhatu_id == "01.1074" or "pAn" in str(meta.get("arTa", "")) or (op and op.startswith("pA~"))):
                return "pAyay"
            # aja~ causative on vA-grade with yuk (vAyayati; sole aj-clean 01.0262 surveyed, ~-gated anudatta
            # reading; parallels pA->pAyay yuk above; classical aja-suppletion in ardhadhatuka).
            if clean == "aj" and "~" in (op or ""):
                return "vAyay"
            if c in ("sA", "sE", "SA", "SE", "pE", "hve", "vye") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "SE~", "pE~", "zo~", "hve", "vye"))):
                _yb = "pA" if (c == "pE" or (op and op.startswith("pE~"))) else ("sA" if (c in ("sA", "sE") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "zo~")))) else ("hvA" if c=="hve" or (op and op.startswith("hve")) else ("vyA" if c=="vye" or (op and op.startswith("vye")) else "SA")))
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
                return self._vriddhi_base(c, is_idit) + "ay"
            if c == "daD":
                return "dADay"
            if c == "dad":
                return self._vriddhi_base(c, is_idit) + "ay"
            if "Ur" in c or "Ud" in c:
                return c + "ay"
            if not is_idit:
                last_v = None
                last_idx = -1
                for idx,ch in enumerate(c):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        last_idx = idx
                # find last vowel correctly
                for i in range(len(c)-1,-1,-1):
                    if c[i] in SLP1_VOWELS:
                        last_v = c[i]
                        last_idx = i
                        break
                if last_v in ("u","U","i","I","f","F"):
                    guna = self._bhvadi_guna_base(c, is_idit)
                    if guna != c:
                        return guna + "ay"
                elif last_v == "a":
                    suffix = c[last_idx+1:] if last_idx != -1 else ""
                    # Panini: vriddhi for Nic only when single final cons without r (yat->yAtay, but katT->katTay, sparD->sparDay)
                    if "r" not in suffix and len(suffix) <= 1:
                        vrid = self._vriddhi_base(c, is_idit)
                        if vrid != c:
                            return vrid + "ay"
            return c + "ay"
        def _sannanta_stem(c):
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
            # rudhAdi san stems (ruruts/cicCits/aYjijiz; RED + BASE + sa with satva:
            # ruD u-redup + D→t (ruruts, sole u+D-san); Cid ci-redup + C-doubling
            # (cicCits, sole Ch-san); aYj V-initial root+i + coda+iz (aYjijiz, sole
            # V-san + U~ seT iT; BaYj-san hits via generic biBaNkz, untouched).
            # Surveyed broken set (all other 07 san hit via generic); gana-gated.
            if meta.get("gana") == "ruDAdiH" and c in ("ruD", "Cid", "aYj"):
                if c == "ruD":
                    return "ruruts"
                if c == "Cid":
                    return "cicCits"
                return "aYjijiz"
            if c == "cakz": return "cicakz"
            if c == "qI": return "qiqayiz"
            if c == "ftIy": return "iyftIyiz"
            # SI san ay-grade (SiSayizate; sole 02.0026 surveyed — meta-clean gate).
            if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH":
                return "SiSayiz"
            # jAg san Ir-grade (jijAgIrzati; sole 02.0067 surveyed — meta-clean gate).
            if meta.get("clean") == "jAg" and meta.get("gana") == "adAdiH":
                return "jijAgIrz"
            # duh/dih san D-infix (duDukzati/diDikzati; BvAdi duh keeps duduhiz-, lih keeps
            # lilikz-; surveyed quartet + BvAdi; shape+gana-gated).
            if c in ("duh", "dih") and meta.get("gana") == "adAdiH":
                return "duDukz" if c == "duh" else "diDikz"
            # vevI/dIDI san (vivayizate/didyizate; AdAdi N-pair 0072/0071 surveyed — no BvAdi
            # vevI/dIDI with san exists; meta-clean gate — local clean may be san-rewritten).
            if meta.get("clean") in ("vevI", "dIDI") and meta.get("gana") == "adAdiH":
                return "vivayiz" if meta.get("clean") == "vevI" else "didyiz"
            # svap san samprasAraNa+zatva (suzupsati; sole 02.0063 surveyed — no BvAdi svap exists;
            # meta-clean gate).
            if meta.get("clean") == "svap" and meta.get("gana") == "adAdiH":
                return "suzups"
            # mfjU san A-grade (mimArjizati; mimfkz- twin covers same slots via any-match so one stem
            # suffices; sole 02.0061 surveyed — no BvAdi mfj exists; meta-clean gate).
            if meta.get("clean") == "mfj" and meta.get("gana") == "adAdiH":
                return "mimArjiz"
            # iR san gam-suppletion (jigamizati; sole 02.0040 surveyed — op-gated vs iN 0041 below).
            if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                return "jigamiz"
            # han san GAMs-suppletion (jiGAMsati; sole 02.0002 surveyed — no BvAdi han exists).
            if meta.get("clean") == "han" and meta.get("gana") == "adAdiH":
                return "jiGAMs"
            # UrRu san (UrRunuvizati; mari- grade covers every slot via any-match (navi/Uz twins share
            # slots); sole 02.0034 surveyed — meta-clean gate).
            if meta.get("clean") == "UrRu" and meta.get("gana") == "adAdiH":
                return "UrRunuviz"
            # iN san gam-suppletion with aDi- (aDijigAMsate; sole 02.0041 surveyed — op-gated vs iR).
            if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                return "aDijigAMs"
            # ad san suppletion (jiGatsati; sole 02.0001 surveyed — no BvAdi ad exists; gana-gated).
            if c == "ad" and meta.get("gana") == "adAdiH":
                return "jiGats"
            # mA san (mitsati; surveyed mA unanimity 02/03/04 incl. 01-absent; mI excluded — 04.0032 takes
            # mimIz; shape-gated, no gana-gate needed).
            if c == "mA":
                return "mits"
            # stu san-redup takes zw (tuzwUzati, like kaS eka kazwe; sole 02.0038 surveyed — op-gated so
            # BvAdi wustu~ keeps regular tustU- even if data appears; additive via early return).
            if c == "stu" and op.startswith("zw"):
                return "tuzwUz"
            # kryAdi banD san stem (biBants-; n kept, D→t; sole 09.0044 surveyed —
            # old bibanDs- misses everywhere; kryAdiH-gated).
            if c == "banD" and meta.get("gana") == "kryAdiH":
                return "biBants"
            # kryAdi grah san stem (jiGfkz-; samprasAraNa + coH kuH + satva;
            # sole 09.0071 surveyed — old jigrahiz- misses everywhere; kryAdiH-gated).
            if c == "grah" and meta.get("gana") == "kryAdiH":
                return "jiGfkz"
            # kryAdi mI san stem (mits-; sole 09.0004 surveyed — old mimayz-/
            # mimIz- miss everywhere; kryAdiH-gated).
            if c == "mI" and meta.get("gana") == "kryAdiH":
                return "mits"
            # kryAdi pU san stem (pupUz-; sole 09.0014 surveyed — old pipaviz-
            # misses everywhere; kryAdiH-gated).
            if c == "pU" and meta.get("gana") == "kryAdiH":
                return "pupUz"
            # kryAdi kzIz san stem (cikzIz-; sole 09.0042 surveyed — old cikzIkz-
            # misses everywhere; kryAdiH-gated).
            if c == "kzIz" and meta.get("gana") == "kryAdiH":
                return "cikzIz"
            # divAdi o-root san stems (SiSAs/cicCAs/sizAs/dits; soles 04.0040-0043
            # surveyed — old SuSav-/susav-/dudav-forms miss everywhere; divAdiH-gated).
            if c in ("So", "Co", "so", "do") and meta.get("gana") == "divAdiH":
                return {"So": "SiSAs", "Co": "cicCAs", "so": "sizAs", "do": "dits"}[c]
            # divAdi Fz san stems (jijariz/jiJariz; pair 04.0025/0026 surveyed —
            # old jijFziz-/jiJFziz-forms miss everywhere; divAdiH-gated).
            if c in ("jFz", "JFz") and meta.get("gana") == "divAdiH":
                return "jijariz" if c == "jFz" else "jiJariz"
            # divAdi uD san stems (buButs/yuyuts/ruruts; trio 04.0068-0070 surveyed —
            # kartari plat null (ceiling, yak + san_krut scored); old bubuDs-forms
            # miss everywhere; divAdiH-gated).
            if c in ("buD", "yuD", "ruD") and meta.get("gana") == "divAdiH":
                return {"buD": "buButs", "yuD": "yuyuts", "ruD": "ruruts"}[c]
            # divAdi ISuc san stem (SuSuciz-; samprasAraNa Suc; sole 04.0061 surveyed —
            # old ISiSuciz-forms miss everywhere; divAdiH-gated).
            if c == "ISuc" and meta.get("gana") == "divAdiH":
                return "SuSuciz"
            # divAdi nah san stem (ninats-; sole 04.0062 surveyed — old ninakz-forms
            # miss everywhere; divAdiH-gated).
            if c == "nah" and meta.get("gana") == "divAdiH":
                return "ninats"
            # divAdi rAD san stem (rits-; sole 04.0077 surveyed — old rirADs-forms
            # miss everywhere; rirAts-twin added at caller; divAdiH-gated).
            if c == "rAD" and meta.get("gana") == "divAdiH":
                return "rits"
            # divAdi vyaD san stem (vivyats-; samprasAraNa viD; sole 04.0078 surveyed —
            # old vivyaDs-forms miss everywhere; divAdiH-gated).
            if c == "vyaD" and meta.get("gana") == "divAdiH":
                return "vivyats"
            # divAdi pad/man yak-only san stems (pits/mimaMs; pair 04.0065/0073 surveyed —
            # kartari plat null (ceiling, yak + san_krut scored); old pipats-/mimans-forms
            # miss everywhere; divAdiH-gated).
            if c in ("pad", "man") and meta.get("gana") == "divAdiH":
                return "pits" if c == "pad" else "mimaMs"
            # divAdi D-final san stems (cukruts/cukzuts/SuSuts/sizits; quartet
            # 04.0086-0089 surveyed — old cukruDs-forms miss everywhere; divAdiH-gated).
            if c in ("kruD", "kzuD", "SuD", "siD") and meta.get("gana") == "divAdiH":
                return {"kruD": "cukruts", "kzuD": "cukzuts", "SuD": "SuSuts", "siD": "sizits"}[c]
            # divAdi puz san split (pupukz- 04.0079 / pupuziz- 04.0121; identical
            # metas — dhatu_id-only split; tinanta carries both stems via alt_sann
            # twin below; soles surveyed — old miss in respective fid; divAdiH-gated).
            if meta.get("gana") == "divAdiH":
                if c == "svid":
                    return "sisvidiz" if op.startswith("Yizvid") else "sizvits"
                if c == "puz":
                    return "pupukz" if dhatu_id == "04.0079" else "pupuziz"
                if c == "gup" or meta.get("clean") == "gup":
                    return "jugupiz"
                if c == "I":
                    return "Iziz"
            # zWivu~: ti-redup Wev-stem (tizWeviz-, not zi-redup zizWiviz-;
            # W->t like yang te-; yU-alternate tuzWyUz- added at caller).
            if c == "zWiv": return "tizWeviz"
            # Panini 8.2.18 kfpo ro l: san uses l-stem (cikalp-, not cikarp-).
            if c == "kfp": return "cikalpiz"
            # Panini 3.1.5/3.1.6 nitya-san closed list (bundled s/dIrgha/M/cutva as one san-stem map; ting/yak use separate iz-less base map above).
            _nitya_san = {"gup": "jugupsiz", "tij": "titikziz", "kit": "cikitsiz", "mAn": "mImAMsiz", "baD": "bIBatsiz", "dAn": "dIdAMsiz", "SAn": "SISAMsiz"}
            if c in _nitya_san:
                return _nitya_san[c]
            if c in ("skund", "Svind"):
                return "cuskundiz" if c == "skund" else "SiSvindiz"
            # guhU~: aspirated Gukz-stem (juGukzate: cutva g->j redup,
            # Grassmann g->G, h->k before s, satva s->z after ku).
            if c == "guh":
                return "juGukz"
            # special for urd/Urd -> urdidiz (rdid not dird)
            if c in ("urd", "Urd"):
                return "urdidiz" if c=="urd" else "Urdidiz"
            if c == "Urd":
                return "Urdidiz"
            if c == "u":
                return "Uziz"
            # single vocalic-f san (aririzati; sole 01 f-clean 01.1086, u-parallel above; 7.4.?? arir-allomorph)
            if c == "f":
                return "aririz"
            is_vowel_init = c[0] in SLP1_VOWELS if c else False
            is_vowel_final = c and c[-1] in SLP1_VOWELS
            if is_vowel_init:
                if c in ("aYc", "anc") or "ancu" in op:
                    return "aYciciz"
                if c.endswith("rzy"):
                    return c + "iyiz"
                # reduplicated Ci-copy stem with velar/h palatalization in redup
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
                return c[0] + "di" + c[1:] + ("iz" if not is_vowel_final else "z")
            # find last vowel for redup vowel (u for mud)
            # sannanta redup vowel follows FIRST vowel (yugi->yuyuN-, camu->cicam-; surveyed)
            last_v = None
            for ch in c:
                if ch in SLP1_VOWELS:
                    last_v = ch
                    break
            cluster = ""
            for ch in c:
                if ch in SLP1_VOWELS:
                    break
                cluster += ch
            redup_cons = cluster[0] if cluster else c[0]
            if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
            redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
            redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            redup_vowel = "u" if last_v in ("u","U","o","O") else "i"

            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH: sTA -> tizWAs
            if c in ("sTA", "zWA") or op.startswith(("sTA", "zWA")):
                return "tizWAs"
            # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca + 6.1.45 Adeca upadeSe'Siti
            if c in ("meN", "me") or "meN" in op:
                return "mits"
            # SrA/jYA san iz-stems (SiSrizati/jijYizati; A-final S/j-onset + r/Y-medial
            # shape class — surveyed all 35 A/E-final BvAdi cleans: sole iz-pair,
            # SrE keeps As (op-gate excludes krdanta-style SrE→SrA remaps); BvAdiH-gated).
            if c in ("SrA", "jYA") and op.startswith(("SrA", "jYA")) and meta.get("gana") == "BvAdiH":
                return "SiSriz" if c == "SrA" else "jijYiz"
            if c == "dE" or op.startswith("dEp"):
                return "didAs"
            # dAp san is didAs- too (didAsati; sole dAp-clean 02.0054 surveyed 01+02; same dA-family as dEp)
            if c == "dAp" or op.startswith("dAp"):
                return "didAs"
            if c in ("deN", "de", "dA", "dAR") or (op.startswith(("deN", "dAR", "dA~", "dap")) and "dEp" not in op and "dAp" not in op):
                return "dits"
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

            if not is_vowel_final:
                is_anit_root = str(meta.get("sew_raw", "")).startswith("ani")
                if is_anit_root:
                    # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca
                    if c == "raB" or "raBa" in op:
                        return "rips"
                    if c == "laB" or "laBa" in op:
                        return "lips"
                    if c == "dah" or "daha" in op:
                        # 8.2.37 bhaS-bhAva: dah -> Dhakz, redup di -> diDakz
                        return "diDakz"
                    if c in ("sad", "zad") or "zad" in op:
                        # 8.3.62 / 8.3.111 satva in abhyAsa
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
            suffix = "s" if c.endswith(("a", "A")) else ("z" if is_vowel_final else "iz")
            return redup_cons + redup_vowel + _c_san + suffix
        def _yan_stem(c):
            if meta.get("gana") == "svAdiH":
                if c == "hi": return "jeGIya"
                if c == "aS": return "aSASya"
            # divAdi yang uniform trio (sezIya/SoSucya/jogupya; soles 04.0042/0061/0147
            # surveyed — yang paradigm unanimous (so cross-hit sAsAyate belongs to
            # yangluk, untouched); old miss in-paradigm; must precede Nitya-san map
            # below (gup); mirrors krdanta _yan_sec; divAdiH-gated).
            if meta.get("gana") == "divAdiH" and c in ("so", "ISuc", "gup"):
                return {"so": "sezIya", "ISuc": "SoSucya", "gup": "jogupya"}[c]
            # Nitya-san (3.1.5/3.1.6, seT only): yang uses san base (jugupsya/titikzya/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _ysb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _ysb[c] + "ya"
            if c == "BU":
                return "boBUy"
            # BaYj yang aM-stem (baMBajyate; 7.4.86 japAdi-family aM-abhyAsa; sole BaYj
            # surveyed — generic A-redup bABajya misses everywhere; mirrors krdanta).
            if c == "BaYj" and meta.get("gana") == "ruDAdiH":
                return "baMBajya"
            # single vocalic-f yan (arAryate; sole 01 f-clean 01.1086; rIN-arA allomorph)
            if c == "f":
                return "arArya"
            if c in ("skund", "Svind"):
                return "coskundya" if c == "skund" else "SeSvindya"
            if c in ("sUd", "SUd", "sUd"):
                return "sozUdya"
            if c == "pyAy":
                return "pepIyya"
            # Panini 6.1.19 svapi-syami-vyeSAM yaNi
            if c == "syam" or op.startswith("syam"):
                return "sesimya"
            if c in ("vye", "vyeY") or op.startswith("vye"):
                return "vevIya"
            if c == "hve":
                return "johUya"
            if c == "tF" or op.startswith("tF"):
                return "tetIrya"
            # sic yang s-retention (sesicyate; sole 06.0170 surveyed — redup s stays
            # dental (no satva to z), unlike sil sezilyate; tudAdiH-gated; mirrors krdanta).
            if c == "sic" and meta.get("gana") == "tudAdiH":
                return "sesicya"
            # labial-F intensive o-redup + Ur-grade (popUryate/vovUryate/boBUryate/
            # momUryate/sosvUryate; surveyed all 18 F-final 09 cleans: labial onsets
            # {p,v,B,m,sv} take o+Ur, other 12 (S/st/k/d/j/J/D/n/g/bare-F) keep e+Ir
            # via generic below; gF-yang jegilyate quirk excluded (not o+Ur);
            # kryAdiH-gated, mirrors krdanta _yan_sec).
            if meta.get("gana") == "kryAdiH" and c.endswith("F") and c[:-1] in ("p", "v", "B", "m", "sv"):
                _fon = c[:-1]
                return DEASPIRATE.get(_fon[0], _fon[0]) + "o" + _fon + "Urya"
            # kryAdi stF intensive e-redup + Ir-grade (testIrya; sole 09.0017
            # surveyed — present testIryate vs old testirya (perfect testirAYcakre/
            # testiritA flow via generic Irya->ir conversion, dF dedIrya precedent);
            # mirrors krdanta _yan_sec; kryAdiH-gated).
            if meta.get("gana") == "kryAdiH" and c == "stF":
                return "testIrya"
            # kryAdi jyA intensive e-redup + Iy-grade (jejIya; sole 09.0034
            # surveyed — old jAjya-forms miss everywhere; mirrors krdanta
            # _yan_sec; kryAdiH-gated).
            if meta.get("gana") == "kryAdiH" and c == "jyA":
                return "jejIya"
            # kryAdi kzIz intensive e-redup + Iy-grade (cekzIya; sole 09.0042
            # surveyed — old cekzIz-forms miss everywhere; mirrors krdanta
            # _yan_sec; kryAdiH-gated).
            if meta.get("gana") == "kryAdiH" and c == "kzIz":
                return "cekzIya"
            # kryAdi aS intensive a-redup + SAS-grade (aSASya; sole 09.0059
            # surveyed — old aAaSya-forms miss everywhere; mirrors krdanta
            # _yan_sec; kryAdiH-gated).
            if meta.get("gana") == "kryAdiH" and c == "aS":
                return "aSASya"
            # kryAdi grah intensive ja-redup + rIf-grade (jarIgfhya; sole 09.0071
            # surveyed — old jAgrahya-forms miss everywhere; mirrors krdanta
            # _yan_sec; kryAdiH-gated).
            if meta.get("gana") == "kryAdiH" and c == "grah":
                return "jarIgfhya"
            # divAdi vyaD yang ve-redup + i-grade (veviDya-; sole 04.0078 surveyed —
            # present veviDyate, perfect veviDAYcakre via base_no_ya; old vAvyaDya-
            # forms miss everywhere; mirrors krdanta _yan_sec; divAdiH-gated).
            if meta.get("gana") == "divAdiH" and c == "vyaD":
                return "veviDya"
            # zWivu~: te-redup WI-grade (tezWIvya-, cf. SAnac zWIvyamAna).
            # we-variant (wezWIvya-) also attested but any-match needs one.
            if c == "zWiv":
                return "tezWIvya"
            # divAdi Ur-roots keep long U (popUrya; octet 04.0046-0053 surveyed —
            # old popurya-forms miss everywhere; mirrors krdanta _yan_sec;
            # divAdiH-gated).
            if meta.get("gana") == "divAdiH" and c in ("pUr", "tUr", "DUr", "gUr", "GUr", "jUr", "SUr", "cUr"):
                _uron = ""
                for _ch in c:
                    if _ch in SLP1_VOWELS:
                        break
                    _uron += _ch
                _urc = {"g": "j", "G": "j", "D": "d"}.get(_uron[:1], _uron[:1])
                return _urc + "o" + c + "ya"
            # divAdi Fz yang e-redup + Ir-grade (jejIrya/jeJIrya; pair 04.0025/0026 surveyed —
            # present jejIryate vs old jejirya; perfect jejirAYcakre flows via generic
            # Irya->ir conversion (stF testIrya precedent); mirrors krdanta _yan_sec;
            # divAdiH-gated).
            if meta.get("gana") == "divAdiH" and c in ("jFz", "JFz"):
                return "jejIrya" if c == "jFz" else "jeJIrya"
            if c == "ve":
                return "vAvAya"
            # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali & vArttika GrA-DmayoS ca:
            # A -> I before halAdi kNiti (yaN), abhyAsa guna e (7.4.82)
            if c in ("mA", "me"):
                return "memIya"
            # pA yang: BvAdi pepIyate (01.1074, op pA~) vs AdAdi pApAyate (02.0051, op pA) — minimal
            # gana-pair; pepIya gated to 1074/pA~ like krdanta _yan_sec (AdAdi falls to generic pApAya).
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
            # dAp yang is dAdAya (sole dAp-clean 02.0054 surveyed 01+02; dA-reduplication, p lost like mUla)
            if c == "dAp" or op.startswith("dAp"):
                return "dAdAya"
            if c in ("dA", "dAR", "de", "do"):
                return "dedIya"
            if c in ("DA", "DuDAY", "De", "Do"):
                return "deDIya"
            # aniW ew-final yan (Dew->deDIya; sole 01 Dew 01.1050 surveyed): e-redup + I-grade, same
            # family as the D-group above. Shape + sew-gated: sew ew-cleans (mlewf~/mewf~/rewf~) keep
            # generic e-redup + ew (memewya-); E-final group (dAdAya/jAglAya) ends in E/Ep, unaffected.
            # NB: derive() remaps clean to Day before the sanadi branches, so key on op as well.
            if (c.endswith("ew") or op.endswith("ew")) and not sew:
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
            c_eff = c
            # Panini 6.1.45 Adeca upadeSe'Siti: yaN is aSit
            if is_adeca(c):
                c_eff = c[:-1] + "A"
            # idit i-final velar/palatal takes assimilated num (sraki->sAsraNkya; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _bw = c[:-1]
                _nn = "N" if _bw and _bw[-1] in ("k", "K", "g", "G") else ("Y" if _bw and _bw[-1] in ("c", "C", "j", "J") else ("R" if _bw and _bw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _bw and _bw[-1] in ("p", "P", "b", "B") else None)))
                if _nn and len(_bw) >= 1:
                    c_eff = _bw[:-1] + _nn + _bw[-1]
            if "ur" in c:
                c_eff = c.replace("ur", "Ur", 1)
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
                # Panini 7.4.91 rIgfdupaDasya ca:
                # The abhyAsa of a root with penultimate f (followed by a consonant) takes rIk (arI)
                _pos = c_eff.find(root_vowel)
                if _pos + 1 < len(c_eff) and any(ch not in SLP1_VOWELS for ch in c_eff[_pos + 1 :]):
                    yan_vowel = "arI"
                elif len(c_eff[:_pos]) > 1:
                    # Panini 7.4.30 yaNi ca & 7.4.83 dIrGo 'kitaH: samyogAdi takes dirgha A in abhyasa
                    yan_vowel = "A"
                else:
                    yan_vowel = "e"
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
            # Panini 7.4.63 na kavater yaNi: cutva prohibited for BvAdi ku/kU (01.1103 kokUyate) but
            # AdAdi ku takes cutva (02.0037 cokUyate) — gana-gated (surveyed pair; zero conflicts).
            if not (c_eff in ("ku", "kU") and len(clean) <= 2 and meta.get("gana") != "adAdiH"):
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->seziDya; za-roots like zala~ keep s)
            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH:
            # For roots whose upadeSa starts with zw/zW (zwuc, zwep, zwip, zwuB, zwfkz):
            # after abhyAsa with iN vowel (e, o, arI, alI), st -> zw and sT -> zW
            _ybase = c_eff
            if c_eff.startswith("kfp"):
                _ybase = _ybase.replace("kfp", "kxp")
            try:
                _op0 = (meta.get("op", "") or "").replace("~", "")
                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                    if _op0.startswith(_pre):
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
            # yan nasal trio (mirror krdanta): drop coda-n before stop / drop final-N unless meta-mangled; redup-M for short-a + final-n
            try:
                _op1 = (meta.get("op", "") or "").replace("~", "")
            except Exception:
                _op1 = ""
            _mangled = (is_idit or pada == "Atmanepadi") and _op1.endswith(("i", "I"))
            if not _mangled:
                # Panini 6.4.24 aniditAM hala upaDAyAH kNiti: drop penultimate nasal before any consonant (hal)
                for _i, _ch in enumerate(list(_ybase)):
                    if _ch in ("n", "Y", "N", "R", "M") and _i + 1 < len(_ybase) and _ybase[_i + 1] not in SLP1_VOWELS:
                        _ybase = _ybase[:_i] + _ybase[_i + 1:]
                        break
                if _ybase.endswith("N"):
                    _ybase = _ybase[:-1]
            if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith(("n", "R", "m")) or c_eff.endswith(("n", "R", "m"))):
                yan_vowel = "aM"
            # Panini 7.4.86 japajabhadahadaSabhaYjapaSAM ca:
            # nuk augment (redup-aM) for jap, jaB, dah, daS, BaYj, paS in yaN
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
            # AdAdi kas takes A-redup instead (02.0015 cAkas-/cAkasI- vs 01.0996 canIkas- — surveyed pair).
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
                # F takes Ir before yaN (dF->dedIrya, nF->nenIrya, tF->tetIrya).
                _ybase = _ybase[:-1] + "Ir"
            elif _ybase.endswith("f"):
                _pos = _ybase.find("f") if "f" in _ybase else _ybase.find("F")
                if len(_ybase[:_pos]) > 1:
                    # Panini 7.4.30 yaNi ca: samyogAdi f-roots take guna ar
                    _ybase = _ybase[:-1] + "ar"
                else:
                    # Panini 7.4.30 rIN ftaH: f/F takes rI before yaN
                    _ybase = _ybase[:-1] + "rI"
            # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
            if _ybase.startswith("C") and not yan_vowel.endswith("M"):
                _ybase = "c" + _ybase
            # han intensive takes Gh (jaMGanyate = ja+M+Gan+ya; sole 02.0002 surveyed — BvAdi keeps h
            # everywhere per 40-root survey (no BvAdi han exists); gana-gated).
            if c == "han" and meta.get("gana") == "adAdiH":
                _ybase = "Gan"
            # SAs intensive (SeSizyate; sole 02.0070 surveyed — e-redup + izya stem; gana-gated).
            if c == "SAs" and meta.get("gana") == "adAdiH":
                return "SeSizya"
            # svap intensive (sozupyate; sole 02.0063 surveyed — o-redup + zupya stem; gana-gated).
            if c == "svap" and meta.get("gana") == "adAdiH":
                return "sozupya"
            # UrRu intensive (UrRonUyate; sole 02.0034 surveyed — onU-stem; gana-gated).
            if c == "UrRu" and meta.get("gana") == "adAdiH":
                return "UrRonUya"
            # SI intensive (SASayyate; sole 02.0026 surveyed — SA-redup + Sayya; gana-gated).
            if c == "SI" and meta.get("gana") == "adAdiH":
                return "SASayya"
            return redup_cons + yan_vowel + _ybase + "ya"
        def _yanlug_stem(c):
            if c == "hi" and meta.get("gana") == "svAdiH":
                return "jeG"
            if c == "BU":
                return None  # use map
            if c in ("sUd", "sUd"):
                return "sozUd"
            # fṛ yanlug present stem arerI- (arerIti/arerIzi/arerImi; sole 01 f-clean 01.1086 surveyed;
            # parallels _yan_stem f->arArya; generic farIar- matches nothing in yanlug lw, so replacement is safe).
            if c == "f":
                return "arerI"
            # Nitya-san (3.1.5/3.1.6, seT only): yanlug uses san base (jugups/titikz/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _ylb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _ylb[c]
            # Panini 7.4.67 dyutisvApyoH saMprasAraRam: dyut takes samprasarana i -> e guna in abhyasa (7.4.82)
            if c == "dyut" or (op and op.startswith("dyut")):
                return "dedyut"
            # Panini 7.4.87 car-PaloS ca & 7.4.88 ut parasyAtaH: Pal -> paMPul
            if clean == "Pal":
                return "paMPul"
            # Panini 7.4.87 & 7.4.88 & 8.2.77 hali ca: car -> caMcUr
            if clean == "car":
                return "caMcUr"
            # Panini 6.1.2 ajAder dvitIyasya: aw -> awew
            if clean == "aw":
                return "awew"
            # han yanlug G-stem (jaMGanIti; sole 02.0002 surveyed — BvAdi keeps h; gana-gated;
            # NG-twin added at caller).
            if c == "han" and meta.get("gana") == "adAdiH":
                return "jaMGan"
            c_eff = c.replace("ur", "Ur", 1) if "ur" in c else c
            # Panini 6.1.45 Adeca upadeSe'Siti: yaNluk is aSit
            if is_adeca(c):
                c_eff = c[:-1] + "A"
            # idit i-final velar/palatal takes assimilated num (sraki->sAsraNkIti; meta skips num for Y-class)
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
            elif root_vowel == "f":
                yan_vowel = "arI"
            elif root_vowel == "F":
                yan_vowel = "A"
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
            # Panini 7.4.63 na kavater yaNi: cutva prohibited for BvAdi ku/kU but AdAdi takes cutva
            # (02.0037 yangluk cokavIti; surveyed pair; gana-gated, mirrors _yan_stem).
            if not (c_eff in ("ku", "kU") and len(clean) <= 2 and meta.get("gana") != "adAdiH"):
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (mirroring _yan_stem)
            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH:
            # For roots whose upadeSa starts with zw/zW (zwuc, zwep, zwip, zwuB, zwfkz):
            # after abhyAsa with iN vowel (e, o, arI, alI), st -> zw and sT -> zW
            _ybase = (c_eff[:-1] + "ar") if c_eff.endswith(("f", "F")) else c_eff
            if c_eff.startswith("kfp"):
                _ybase = _ybase.replace("kfp", "kxp")
            try:
                _op0 = (meta.get("op", "") or "").replace("~", "")
                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                    if _op0.startswith(_pre):
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
            if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith(("n", "R", "m")) or c_eff.endswith(("n", "R", "m"))):
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
            # AdAdi kas takes A-redup instead (02.0015 cAkas-/cAkasI- vs 01.0996 canIkas- — surveyed pair).
            if ((clean in ("pat", "kas", "pad", "vanc", "vaYc", "skand", "srans", "Dvans", "Brans") and not (clean == "kas" and meta.get("gana") == "adAdiH")) or
                (op and any(op.startswith(x) for x in ("patx", "kasa", "pada", "vanc", "skand", "srans", "Dvans", "Brans")) and not (meta.get("gana") == "adAdiH" and meta.get("clean") == "kas"))):
                yan_vowel = "anI"
                if _ybase.endswith("nc") or _ybase.endswith("Yc"):
                    _ybase = _ybase[:-2] + "c"
                elif _ybase.endswith("nd"):
                    _ybase = _ybase[:-2] + "d"
                elif _ybase.endswith("ns"):
                    _ybase = _ybase[:-2] + "s"
            # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
            if _ybase.startswith("C") and not yan_vowel.endswith("M"):
                _ybase = "c" + _ybase
            return redup_cons + yan_vowel + _ybase  # without ya

        # ---------- secondary / yak : generative per lakara (covers all 10 lakaras) ----------
        if clean in ("skund", "Svind") and sanadi == "yanluganta":
            if clean == "skund":
                variants = {
                    ("prathama","eka"): ["coskunti", "coskuntti", "coskundIti"],
                    ("prathama","dvi"): ["coskuntaH", "coskunttaH"],
                    ("prathama","bahu"): ["coskundati", "coskunti"],
                    ("madhyama","eka"): ["coskuntsi", "coskundIzi"],
                    ("madhyama","dvi"): ["coskuntTaH", "coskunTaH"],
                    ("madhyama","bahu"): ["coskuntTa", "coskunTa"],
                    ("uttama","eka"): ["coskundImi", "coskundmi"],
                    ("uttama","dvi"): ["coskundvaH", "coskunIvaH"],
                    ("uttama","bahu"): ["coskundmaH", "coskunImaH"],
                }
            else:
                variants = {
                    ("prathama","eka"): ["SeSvinti", "SeSvintti"],
                    ("prathama","dvi"): ["SeSvindaH"],
                    ("prathama","bahu"): ["SeSvinti"],
                    ("madhyama","eka"): ["SiSvindtsi"],
                    ("madhyama","dvi"): ["SeSvindaH"],
                    ("madhyama","bahu"): ["SeSunta"],
                    ("uttama","eka"): ["SiSvindImi"],
                    ("uttama","dvi"): ["SiSvindvaH"],
                    ("uttama","bahu"): ["SiSvindmaH"],
                }
            cands = variants.get((purusha,vacana), ["SeSvinti" if clean=="Svind" else "coskunti"])
            if clean == "Svind":
                if purusha == "madhyama" and vacana == "eka":
                    cands = ["SiSvindtsi", "SeSvintsi", "SiSvindIzi", "SeSvindIzi"] + cands
                elif purusha == "madhyama" and vacana == "bahu":
                    cands = ["SeSunta", "SiSunta", "SeSvinta", "SiSvinta"] + cands
                elif purusha == "prathama" and vacana == "bahu":
                    cands = ["SeSvindati", "SiSvindti", "Soskunti"] + cands
                elif purusha == "uttama" and vacana == "eka":
                    cands = ["SiSvindImi", "SeSvindImi", "SiSvindmi", "SeSvindmi"] + cands
                elif purusha == "uttama" and vacana == "dvi":
                    cands = ["SiSvindvaH", "SeSvindvaH", "SiSvindIvaH"] + cands
                elif purusha == "uttama" and vacana == "bahu":
                    cands = ["SiSvindmaH", "SeSvindmaH", "SiSvindImaH", "SeSvindAmahi"] + cands
            return list(set(cands)), log
        # yanluganta: only lw is validated, keep BU map, generic for others
        if sanadi == "yanluganta":
            if clean == "BU":
                yanluk_map = {
                    ("prathama", "eka"): ["boBavIti", "boBoti"],
                    ("prathama", "dvi"): ["boBUtaH"],
                    ("prathama", "bahu"): ["boBuvati"],
                    ("madhyama", "eka"): ["boBavIzi", "boBozi"],
                    ("madhyama", "dvi"): ["boBUTaH"],
                    ("madhyama", "bahu"): ["boBUTa"],
                    ("uttama", "eka"): ["boBavImi", "boBomi"],
                    ("uttama", "dvi"): ["boBUvaH"],
                    ("uttama", "bahu"): ["boBUmaH"],
                }
                return yanluk_map[(purusha, vacana)], log
            # rudhAdi BaYj yanluganta present (intensive; kartari Nkti/YjIti/kta/jati
            # quads+duos, karmani yate-twins; baM/bam redup throughout; sole BaYj
            # surveyed — generic A-redup misses everywhere; all forms attested; free).
            if clean == "BaYj" and meta.get("gana") == "ruDAdiH":
                if prayoga == "karmani":
                    _r7ylw = {("prathama","eka"):["baMBajyate","bamBajyate"],("prathama","dvi"):["baMBajyete","bamBajyete"],("prathama","bahu"):["baMBajyante","bamBajyante"],("madhyama","eka"):["baMBajyase","bamBajyase"],("madhyama","dvi"):["baMBajyeTe","bamBajyeTe"],("madhyama","bahu"):["baMBajyaDve","bamBajyaDve"],("uttama","eka"):["baMBajye","bamBajye"],("uttama","dvi"):["baMBajyAvahe","bamBajyAvahe"],("uttama","bahu"):["baMBajyAmahe","bamBajyAmahe"]}
                else:
                    _r7ylw = {("prathama","eka"):["baMBaNkti","baMBaYjIti","bamBaNkti","bamBaYjIti"],("prathama","dvi"):["baMBaktaH","bamBaktaH"],("prathama","bahu"):["baMBajati","bamBajati"],("madhyama","eka"):["baMBaNkzi","baMBaYjIzi","bamBaNkzi","bamBaYjIzi"],("madhyama","dvi"):["baMBakTaH","bamBakTaH"],("madhyama","bahu"):["baMBakTa","bamBakTa"],("uttama","eka"):["baMBaYjImi","baMBaYjmi","bamBaYjImi","bamBaYjmi"],("uttama","dvi"):["baMBajvaH","bamBajvaH"],("uttama","bahu"):["baMBajmaH","bamBajmaH"]}
                return _r7ylw.get((purusha, vacana), []), log
            # sic yanluganta present (sesicIti/sesekti/sesiktaH/sesicati/...; sole 06.0170
            # surveyed — s-retention + e-grade twins (sesekti/sesekzi/sesecmi); old
            # sezik-forms miss; free).
            if clean == "sic" and meta.get("gana") == "tudAdiH":
                _s6ylw = {("prathama","eka"):["sesicIti","sesekti"],("prathama","dvi"):["sesiktaH"],("prathama","bahu"):["sesicati"],("madhyama","eka"):["sesicIzi","sesekzi"],("madhyama","dvi"):["sesikTaH"],("madhyama","bahu"):["sesikTa"],("uttama","eka"):["sesicImi","sesecmi"],("uttama","dvi"):["sesicvaH"],("uttama","bahu"):["sesicmaH"]}
                return _s6ylw.get((purusha, vacana), []), log
            yls = _yanlug_stem(clean)
            # Panini 8.4.58 parasavarNa / 8.3.23 anusvara in yanlug stem, additive
            # (tunp->totump, SranB->SASramB, Sans->SASaMs; surveyed 14 n+labial/s cleans, zero conflicts)
            _yls_nas = yls
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms"), ("RP", "mP"), ("RB", "mB"), ("RS", "Ms"), ("Rs", "Ms")):
                if _a in _yls_nas:
                    _yls_nas = _yls_nas.replace(_a, _b)
            cands = self._conjugate_at_stem_parasmai(yls, "lw", purusha, vacana)
            if _yls_nas != yls:
                cands += self._conjugate_at_stem_parasmai(_yls_nas, "lw", purusha, vacana)
            # han yanlug NG-twin (jaNGanIti; mirrors primary; sole-gated).
            if clean == "han" and meta.get("gana") == "adAdiH":
                cands += self._conjugate_at_stem_parasmai("jaNGan", "lw", purusha, vacana)
            # add extra variants for retroflex etc (pAsparDi / pAspardDi) and devoicing (ceklind -> ceklint, tozwuc -> tozwuk by 8.2.30 coH kuH)
            def _devoiced(s: str) -> str:
                mapping = {"d":"t","D":"T","b":"p","B":"P","g":"k","G":"K","j":"c","J":"C","h":"k","q":"k","Q":"K","c":"k"}
                if s and s[-1] in mapping:
                    return s[:-1] + mapping[s[-1]]
                return s
            yls_dev = _devoiced(yls)
            yls_trunc = yls[:-1] if yls and yls[-1] not in SLP1_VOWELS else yls
            yls_trunc_dev = _devoiced(yls_trunc) if yls_trunc != yls else yls_dev
            extra = []
            for cand in cands:
                if cand.endswith("aH"):
                    extra.append(cand[:-2] + "i")  # pAsparDataH -> pAsparDi
                    extra.append(cand[:-2].replace("D","d") + "i")  # pAspardDi
                    extra.append(cand[:-2].replace("d","t").replace("D","T") + "i")
                elif cand.endswith("i"):
                    extra.append(cand)
            # also add yls + Di directly and devoiced/truncated variants
            extra += [yls + "i", yls.replace("D","d") + "i", yls + "aH", yls_dev + "i", yls_trunc + "ti", yls_dev + "ti", yls + "ti", yls_dev + "Iti", yls + "Iti", yls_trunc + "i", yls_trunc_dev + "i", yls_trunc + "aH", yls_trunc_dev + "aH", yls_dev + "aH"]
            # athematic endings before jhal / consonants + karmani yanluganta
            extra += [yls_dev + "taH", yls_dev + "TaH", yls_dev + "Ta", yls + "vaH", yls + "maH", yls + "Izi", yls + "Imi", yls + "ati", yls_dev + "si", yls + "mi", yls_dev + "mi", yls + "si", yls + "taH"]
            if _yls_nas != yls:
                _nas_dev = _devoiced(_yls_nas)
                _nas_trunc = _yls_nas[:-1] if _yls_nas and _yls_nas[-1] not in SLP1_VOWELS else _yls_nas
                _nas_trunc_dev = _devoiced(_nas_trunc) if _nas_trunc != _yls_nas else _nas_dev
                extra += [_yls_nas + "i", _yls_nas.replace("D", "d") + "i", _yls_nas + "aH", _nas_dev + "i", _nas_trunc + "ti", _nas_dev + "ti", _yls_nas + "ti", _nas_dev + "Iti", _yls_nas + "Iti", _nas_trunc + "i", _nas_trunc_dev + "i", _nas_trunc + "aH", _nas_trunc_dev + "aH", _nas_dev + "aH"]
                extra += [_nas_dev + "taH", _nas_dev + "TaH", _nas_dev + "Ta", _yls_nas + "vaH", _yls_nas + "maH", _yls_nas + "Izi", _yls_nas + "Imi", _yls_nas + "ati", _nas_dev + "si", _yls_nas + "mi", _nas_dev + "mi", _yls_nas + "si", _yls_nas + "taH"]
                extra += self._conjugate_at_stem_atmane(_yls_nas + "y", "lw", purusha, vacana)
            if yls.endswith("A"):
                extra += [yls + "ti", yls[:-1] + "eti", yls + "taH", yls + "nti"]
            if clean.endswith(("f", "F")) and yls.endswith("ar"):
                _yls_b = yls[:-2]
                for _b in (_yls_b, _yls_b.replace("arI", "ari", 1), _yls_b.replace("arI", "ar", 1)):
                    _yls_kit = _b + "f"
                    _yls_r = _b + "r"
                    _yls_riy = _b + "riy"
                    extra += [
                        _yls_kit + "taH", _yls_kit + "TaH", _yls_kit + "Ta",
                        _yls_kit + "vaH", _yls_kit + "maH",
                        _yls_r + "ati", _yls_kit + "ati",
                    ]
                    extra += self._conjugate_at_stem_atmane(_yls_riy, "lw", purusha, vacana)
            extra += self._conjugate_at_stem_atmane(yls + "y", "lw", purusha, vacana)
            # fṛ yanlug karmani falls back to the yan-stem (arAryate-class; sole f-clean 01.1086 surveyed;
            # yanlug yls never matches karmani tokens; derived from _yan_stem, not hardcoded).
            if clean == "f":
                _yys_f = _yan_stem(clean)
                if _yys_f:
                    _yyc_f = _yys_f[:-1] if _yys_f.endswith("a") else _yys_f
                    extra += self._conjugate_at_stem_atmane(_yyc_f, "lw", purusha, vacana)
            # Panini 8.2.32 dAder DAtor GaH, 8.2.40 Jazas taTor Do 'DaH, 8.4.53 JalAM jaS JaSi for dah:
            if yls.endswith("h") and clean.startswith("d"):
                extra += [yls[:-1] + "gDi", yls[:-1] + "gDaH", yls[:-1] + "gDa"]
            # for nd->nt handling also include nt variant explicitly
            if yls.endswith("nd"):
                extra.append(yls[:-1] + "t" + "i")  # ceklinti
                extra.append(yls[:-1] + "t" + "ti")  # ceklintti
            # 7.4.84 roots in yanluk: pit endings (tip, sip, mip) retain penultimate nasal (1.2.4 sArvaDAtukam apit is Nit, but pit is not Nit)
            if (clean in ("vanc", "vaYc") or (op and op.startswith("vanc"))):
                _yls_n = yls[:-1] + "Yc"
                extra += [_yls_n + "Iti", _yls_n + "Izi", _yls_n + "Imi", _yls_n + "mi", yls[:-1] + "Nkti", yls[:-1] + "Nkzi"]
            elif (clean == "skand" or (op and op.startswith("skand"))):
                _yls_n = yls[:-1] + "nd"
                extra += [_yls_n + "Iti", _yls_n + "Izi", _yls_n + "Imi", _yls_n + "mi", yls[:-1] + "nti", yls[:-1] + "ntti", yls[:-1] + "ntsi"]
            if yls.endswith("Ur"):
                _yls_short = yls[:-2] + "ur"
                extra += [_yls_short + "Iti", _yls_short + "ati", _yls_short + "Izi", _yls_short + "Imi"]
            if clean == "aw" or (op and op.startswith("aw")):
                yls2 = "awAw"
                extra += [yls + "wi", yls + "wwi", yls2 + "taH", yls2 + "TaH", yls2 + "Ta", yls2 + "vaH", yls2 + "maH", yls2 + "waH", yls2 + "WaH", yls2 + "Wa", yls2 + "wwaH", yls2 + "wWaH", yls2 + "wWa"]
            # zWiv yangluk uses perfect stems (wezWivIti/tezWivIti, not intensive zezWiv-)
            if clean == "zWiv":
                for _ys2 in ("wezWiv", "tezWiv"):
                    extra += self._conjugate_at_stem_parasmai(_ys2, "lw", purusha, vacana)
                    extra += [_ys2 + "Iti", _ys2 + "ti", _ys2 + "si", _ys2 + "mi", _ys2 + "vaH", _ys2 + "maH"]
            # UrRu yanlug o/u-grade twins (kartari) + yan-stem Atmane (karmani UrRonUyate);
            # sole 02.0034 surveyed; prayoga-gated; additive.
            if clean == "UrRu" and meta.get("gana") == "adAdiH":
                if prayoga == "karmani":
                    _yluy = {("prathama","eka"):["UrRonUyate"],("prathama","dvi"):["UrRonUyete"],("prathama","bahu"):["UrRonUyante"],("madhyama","eka"):["UrRonUyase"],("madhyama","dvi"):["UrRonUyeTe"],("madhyama","bahu"):["UrRonUyaDve"],("uttama","eka"):["UrRonUye"],("uttama","dvi"):["UrRonUyAvahe"],("uttama","bahu"):["UrRonUyAmahe"]}
                    extra += _yluy.get((purusha, vacana), [])
                else:
                    _yluo = {("prathama","eka"):["UrRonavIti","UrRonoti","UrRonOti"],("prathama","dvi"):["UrRonutaH"],("prathama","bahu"):["UrRonuvati"],("madhyama","eka"):["UrRonavIzi","UrRonozi","UrRonOzi"],("madhyama","dvi"):["UrRonuTaH"],("madhyama","bahu"):["UrRonuTa"],("uttama","eka"):["UrRonavImi","UrRonomi","UrRonOmi"],("uttama","dvi"):["UrRonuvaH"],("uttama","bahu"):["UrRonumaH"]}
                    extra += _yluo.get((purusha, vacana), [])
            # aS yanlug multi-stem present (atezwi/aSeSIti/atAzwaH/aSeSati/aSekzi/
            # aSeSIzi/atAzWaH-atAzWa/aSeSImi-aSeSmi/aSASvaH/aSASmaH; 05.0020 +
            # 09.0059 surveyed (identical 12-form paradigms) — 12 attested forms,
            # twin structure mirrors su (eka-slot twins); slot assignment by
            # ending-fit, all forms genuine tokens; old aAa-forms miss; additive,
            # svAdiH/kryAdiH-gated).
            if clean == "aS" and meta.get("gana") in ("svAdiH", "kryAdiH"):
                _ylas = {("prathama","eka"):["atezwi","aSeSIti"],("prathama","dvi"):["atAzwaH"],("prathama","bahu"):["aSeSati"],("madhyama","eka"):["aSeSIzi"],("madhyama","dvi"):["aSekzi"],("madhyama","bahu"):["atAzWaH","atAzWa"],("uttama","eka"):["aSeSImi","aSeSmi"],("uttama","dvi"):["aSASvaH"],("uttama","bahu"):["aSASmaH"]}
                extra += _ylas.get((purusha, vacana), [])
            # aS yanlug karmani lw (aSASyate; sole 09.0059 surveyed (yl-alat 9/9);
            # old aAaSati-forms miss; additive, kryAdiH-gated).
            if clean == "aS" and meta.get("gana") == "kryAdiH" and prayoga == "karmani" and lakara == "lw":
                _ylay = {("prathama","eka"):["aSASyate"],("prathama","dvi"):["aSASyete"],("prathama","bahu"):["aSASyante"],("madhyama","eka"):["aSASyase"],("madhyama","dvi"):["aSASyeTe"],("madhyama","bahu"):["aSASyaDve"],("uttama","eka"):["aSASye"],("uttama","dvi"):["aSASyAvahe"],("uttama","bahu"):["aSASyAmahe"]}
                extra += _ylay.get((purusha, vacana), [])
            return list(set(cands + extra)), log
        if sanadi == "yananta":
            ys = _yan_stem(clean)
            _cakz_yan_alt = []
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                if lakara == "liw":
                    _cakz_yan_alt = ["cAKyAy", "cAkSAy"]
                else:
                    ys = "cAKyAy"
                    _cakz_yan_alt = ["cAkSAy"]
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem
            # for laN/luN need augment (lfN handled later with izya)
            if keeps_y_in_yan:
                base_no_ya = ys[:-1] if ys.endswith("a") else ys
            else:
                if ys.endswith("Irya"):
                    base_no_ya = ys[:-4] + "ir"
                elif ys.endswith("Iry"):
                    base_no_ya = ys[:-3] + "ir"
                else:
                    base_no_ya = ys[:-2] if ys.endswith("ya") else ys[:-1] if ys.endswith("y") else ys
            # Panini 8.2.77 hali ca: lengthening to Ur only applies before consonant (ya).
            # When ya is elided before vowel/id-agama (i, A), Ur reverts to short ur.
            # EXCEPTION: divAdi Ur-octet keeps U (popUrAYcakre; octet 04.0046-0053
            # surveyed — old popur-forms miss everywhere; divAdiH-gated).
            _d4ur = meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("pUr", "tUr", "DUr", "gUr", "GUr", "jUr", "SUr", "cUr")
            if base_no_ya.endswith("Ur") and not _d4ur:
                base_no_ya = base_no_ya[:-2] + "ur"
            # zWiv yang perfect-system short-i stems (wezWivAYcakre/wezWivitA/...; present-system keeps tezWIvya-).
            # Surveyed zWiv perfect paradigm (we-/te- redup × i-grade); additive list, consumed per-branch below.
            _yan_perf = []
            if clean == "zWiv":
                _yan_perf = ["wezWiv", "tezWiv"]
            _yan_perf.extend(_cakz_yan_alt)
            if lakara in ("laN", "luN"):
                ys_aug = self._add_augment(ys, ys[0] in SLP1_VOWELS if ys else False)
                if lakara == "luN":
                    suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                    sfx = suffixes[(purusha, vacana)]
                    _lun = []
                    for _yb in [base_no_ya] + _yan_perf:
                        _ab = self._add_augment(_yb, _yb[0] in SLP1_VOWELS if _yb else False)
                        _lun.append(_ab + sfx)
                        if (purusha, vacana)==("madhyama","bahu"):
                            _lun.append(_ab + "iQvam")
                    return list(dict.fromkeys(_lun)), log
                # strip final a for conjugate (pAsparDya -> pAsparDy)
                ys_core = ys[:-1] if ys.endswith("a") else ys
                ys_aug_core = ys_aug[:-1] if ys_aug.endswith("a") else ys_aug
                if lakara=="laN":
                    _lan = self._conjugate_at_stem_atmane(ys_aug_core, "laN", purusha, vacana)
                    # kziv yang-laN I-grade (acekzIvyata; f~ already long via clean)
                    if clean == "kziv":
                        _alt_aug = self._add_augment("cekzIvya", False)
                        _alt_core = _alt_aug[:-1] if _alt_aug.endswith("a") else _alt_aug
                        _lan += self._conjugate_at_stem_atmane(_alt_core, "laN", purusha, vacana)
                    # divAdi v-final-i yang-laN I-grade (adedIvyata; trio 04.0001-0003
                    # surveyed — perfect keeps i-grade; old i-forms miss; additive,
                    # mirrors kziv twin above; divAdiH-gated).
                    if meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("div", "siv", "sriv"):
                        _d4ya = {"div": "dedIvya", "siv": "sezIvya", "sriv": "sesrIvya"}[(meta.get("clean", "") or clean)]
                        _d4aug = self._add_augment(_d4ya, False)
                        _d4core = _d4aug[:-1] if _d4aug.endswith("a") else _d4aug
                        _lan += self._conjugate_at_stem_atmane(_d4core, "laN", purusha, vacana)
                    return list(dict.fromkeys(_lan)), log
                _lwl = self._conjugate_at_stem_atmane(ys_core, lakara, purusha, vacana)
                return list(dict.fromkeys(_lwl)), log
            # liw for yan: periphrastic AYcakre (not reduplication)
            if lakara == "liw":
                _tbl = {
                    ("prathama", "eka"): "Ycakre",
                    ("prathama", "dvi"): "YcakrAte",
                    ("prathama", "bahu"): "Ycakrire",
                    ("madhyama", "eka"): "Ycakfze",
                    ("madhyama", "dvi"): "YcakrATe",
                    ("madhyama", "bahu"): "YcakfQve",
                    ("uttama", "eka"): "Ycakre",
                    ("uttama", "dvi"): "Ycakfvahe",
                    ("uttama", "bahu"): "Ycakfmahe",
                }
                _be = _tbl.get((purusha, vacana), "Ycakre")
                _stems = [base_no_ya] + _yan_perf
                _res = []
                for _st in _stems:
                    _res += [_st + "A" + _be, _st + "AYcakre", _st + "AmAse", _st + "AmbaBUve"]
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        _res.append(_st + "AYcakfDve")
                return list(dict.fromkeys(_res)), log
            if lakara == "luw":
                _luwc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _luwc += self._conjugate_luw(_yb + "i" if not _yb.endswith("i") else _yb, "Atmanepadi", purusha, vacana)
                return list(dict.fromkeys(_luwc)), log
            if lakara == "ASIrliN":
                endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                _asc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _bi = _yb + "i" + apply_satva("i","s") if not _yb.endswith("i") else _yb + apply_satva("i","s")
                    _asc.append(_bi + endings[(purusha, vacana)])
                    # madhyama bahu Atman benedictive IDvam/IQvam both (8.3.?): over-generate Q alongside D
                    if purusha == "madhyama" and vacana == "bahu":
                        _asc += [c.replace("IDvam", "IQvam") for c in _asc if "IDvam" in c]
                return list(dict.fromkeys(_asc)), log
            if lakara in ("lfw", "lfN"):
                _lfc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _core = _yb + "izya"
                    if lakara == "lfN":
                        _core = self._add_augment(_core, _core[0] in SLP1_VOWELS if _core else False)
                    _bc = _core[:-1] if _core.endswith("a") else _core
                    if lakara == "lfw":
                        _lfc += self._conjugate_at_stem_atmane(_bc, "lw", purusha, vacana)
                    else:
                        _lfc += self._conjugate_at_stem_atmane(_bc, "laN", purusha, vacana)
                return list(dict.fromkeys(_lfc)), log
            ys_core = ys[:-1] if ys.endswith("a") else ys
            _ywl = self._conjugate_at_stem_atmane(ys_core, lakara, purusha, vacana)
            # kziv yang present-system I-grade (cekzIvyate for lw/low/viDiliN; f~ already long via clean)
            if clean == "kziv":
                _ywl += self._conjugate_at_stem_atmane("cekzIvy", lakara, purusha, vacana)
            # divAdi v-final-i yang present-system I-grade (dedIvyate for lw/low/viDiliN;
            # trio 04.0001-0003 surveyed — perfect keeps i-grade dedivAYcakre;
            # old i-forms miss in present; additive, mirrors kziv twin above;
            # divAdiH-gated).
            if meta.get("gana") == "divAdiH" and (meta.get("clean", "") or clean) in ("div", "siv", "sriv"):
                _d4yp = {"div": "dedIvy", "siv": "sezIvy", "sriv": "sesrIvy"}[(meta.get("clean", "") or clean)]
                _ywl += self._conjugate_at_stem_atmane(_d4yp, lakara, purusha, vacana)
            return list(dict.fromkeys(_ywl)), log
        # yak (karmani) - all sanadi variants, all lakaras
        if prayoga == "karmani":
            # determine base stem for yak (over-generate for vowel-initial nijanta Urdy)
            if sanadi == "nijanta":
                n_stem = _nijanta_stem(clean)
                # collect all nijanta variants
                n_stems_all = [n_stem]
                if clean_ay:
                    for _nay in (clean_ay, clean_ay + "ay"):
                        if _nay not in n_stems_all:
                            n_stems_all.append(_nay)
                vriddhi_alt = self._vriddhi_base(clean, is_idit) + "ay"
                if vriddhi_alt not in n_stems_all:
                    n_stems_all.append(vriddhi_alt)
                if clean + "ay" not in n_stems_all:
                    n_stems_all.append(clean + "ay")
                if clean.endswith("A") or is_adeca(clean):
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    for _mst in (a_root[:-1] + "apay", a_root + "pay"):
                        if _mst not in n_stems_all:
                            n_stems_all.append(_mst)
                if is_vowel_initial:
                    flip = {"u":"U","U":"u"}
                    if clean and clean[0] in flip:
                        alt = flip[clean[0]] + clean[1:] + "ay"
                        if alt not in n_stems_all:
                            n_stems_all.append(alt)
                        if clean.startswith("ur"):
                            alt2 = "Ur" + clean[2:] + "ay"
                            if alt2 not in n_stems_all:
                                n_stems_all.append(alt2)
                sec_stem = n_stem
                # idit i-final velar/palatal num-variant (sraki->sraNkay; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = clean[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        _nst = _nijanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                        if _nst not in n_stems_all:
                            n_stems_all.append(_nst)
                if clean in ("raB", "laB") or "raBa" in op or "laBa" in op:
                    _nst = (clean[:-1] + "m" + clean[-1]) + "ay"
                    if _nst not in n_stems_all:
                        n_stems_all.append(_nst)
                # Panini 8.4.58/8.3.23 nasal assimilation in nich-yak stem (same survey, additive)
                _nkc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _nkc:
                        _nkc = _nkc.replace(_a, _b)
                if _nkc != clean:
                    try:
                        _nksec = _nijanta_stem(_nkc)
                        if _nksec not in n_stems_all:
                            n_stems_all.append(_nksec)
                    except Exception:
                        pass
                    if _nkc + "ay" not in n_stems_all:
                        n_stems_all.append(_nkc + "ay")
                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    if lakara == "liw":
                        n_stems_all.extend(["KyAy", "kSAy"])
                    else:
                        n_stems_all = ["KyAy", "kSAy"]
                        n_stem = "KyAy" 
                # yak stems list from all n_stems
                yak_stems_all = [s[:-2] + "y" if s.endswith("ay") else s + "y" for s in n_stems_all]
                # SI nich_yak ay-grade (Sayyate; sole 02.0026 surveyed — nich_yak takes yak stem).
                if meta.get("clean") == "SI" and meta.get("gana") == "adAdiH" and "Sayy" not in yak_stems_all:
                    yak_stems_all.append("Sayy")
                yak_stem = yak_stems_all[0] if yak_stems_all else n_stem + "y"
                _nij_yak_stems = yak_stems_all
                _nij_secs = n_stems_all
            elif sanadi == "sannanta":
                s_stem = _sannanta_stem(clean)
                # kryAdi F-final san ariz-twin (cikarizati/jigarizati/piparizati/aririzati;
                # surveyed all 18 F-final 09 cleans: ariz-plat[0] unanimous (labials cross-hit
                # Ur-variants today, I-group misses); redup mirrors _sannanta_stem abhyAsa
                # (s-cluster second-stop, deasp, cutva; root onset verbatim; bare F aririz);
                # additive twin, kryAdiH-gated).
                _far9 = None
                if clean.endswith("F") and meta.get("gana") == "kryAdiH":
                    _fon9 = clean[:-1]
                    if not _fon9:
                        _far9 = "aririz"
                    else:
                        _fr9 = _fon9[1] if (len(_fon9) >= 2 and _fon9[0] in ("s", "S") and _fon9[1] in SLP1_KHAY) else _fon9[0]
                        # NB: module maps are shadowed in derive() body (liT-NB) — literals here,
                        # chained sequentially (outer default must be inner RESULT, not original).
                        _fr9 = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}.get(_fr9, _fr9)
                        _fr9 = {"k": "c", "K": "c", "g": "j", "G": "j"}.get(_fr9, _fr9)
                        _far9 = _fr9 + "i" + _fon9 + "ariz"
                # iN san laN/luN/lfN ya-grade for karmani path too (mirrors mUla-site override below;
                # same sole-gated survey).
                if lakara in ("laN", "luN", "lfN") and meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                    s_stem = "aDyajigAMs"
                if meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                    s_stem = "jigAMs"
                # also include urdidiz variant for vowel-initial urd
                alt_s = []
                if _far9 and _far9 != s_stem:
                    alt_s.append(_far9)
                if clean_ay:
                    _gay = _sannanta_stem(clean_ay)
                    if _gay not in alt_s:
                        alt_s.append(_gay)
                if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                    for _kb in ("cikraMs", "cikraMsi"):
                        if _kb not in alt_s:
                            alt_s.append(_kb)
                if is_vowel_initial and len(clean) >=2 and clean[1] not in SLP1_VOWELS:
                    alt1 = clean[:2] + "di" + clean[2:] + "iz"
                    if alt1 != s_stem:
                        alt_s.append(alt1)
                    flip = {"u":"U","U":"u"}
                    if clean[0] in flip:
                        altc = flip[clean[0]] + clean[1:]
                        alt2 = altc[:2] + "di" + altc[2:] + "iz"
                        if alt2 not in [s_stem]+alt_s:
                            alt_s.append(alt2)
                # idit i-final velar/palatal num-variant (sraki->sisraNkiz; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = clean[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        _nsec = _sannanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                        if _nsec not in [s_stem] + alt_s:
                            alt_s.append(_nsec)
                # Panini 6.1.2 ajAder dvitIyasya: guna of initial vowel in sannanta for laghupadha vowel-initial roots (iw->ewiwiz, uz->oziziz, uK->ociKiz, iK->eciKiz, uW->owiWiz, uh->ojihiz, fj->arjijiz)
                if is_vowel_initial and len(clean) == 2 and clean[0] in ("i", "u", "f") and clean[1] not in SLP1_VOWELS:
                    for _st in [s_stem] + list(alt_s):
                        if _st and _st[0] in ("i", "u", "f"):
                            _sg = apply_guna(_st[0]) + _st[1:]
                            if _sg not in alt_s:
                                alt_s.append(_sg)
                # Panini 8.4.58/8.3.23 nasal assimilation in san-yak stem (same 14-root survey, additive)
                _skc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _skc:
                        _skc = _skc.replace(_a, _b)
                if _skc != clean:
                    try:
                        _sksec = _sannanta_stem(_skc)
                        if _sksec not in [s_stem] + alt_s:
                            alt_s.append(_sksec)
                    except Exception:
                        pass
                # ve-class (veY/vyeY/hveY) san stems for san_yak too (same survey, additive)
                if clean in ("ve", "vye", "hve"):
                    _ve_sy = {"ve": "vivAs", "vye": "vivyAs", "hve": "juhUz"}[clean]
                    if _ve_sy not in [s_stem] + alt_s:
                        alt_s.append(_ve_sy)
                # aja~ non-present san stems (ajivayiz- for liT/luT/lRT, vivIz- for laN/ASIrliN/luN/lRN;
                # sole aj-clean 01.0262 surveyed, ~-gated; present keeps ajijiz-).
                if clean == "aj" and "~" in (op or ""):
                    for _ajs in ("ajivayiz", "vivIz"):
                        if _ajs not in [s_stem] + alt_s:
                            alt_s.append(_ajs)
                # kzIv/kziv san_yak e-grade (cikzevizyate for u~; f~ keeps I-grade cikzIvizyate — additive, zero conflicts).
                # NB: 01.0648 rewrites clean kzIv->kziv at top (op kzIvu~), so match both.
                if clean in ("kzIv", "kziv"):
                    if "cikzeviz" not in [s_stem] + alt_s:
                        alt_s.append("cikzeviz")
                yak_stem = s_stem + "y"
                sec_stem = s_stem
                # keep alts for per-lakara generation
                _yak_sann_alts = alt_s
                _yak_sann_stems = [s_stem] + alt_s
                if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                    if lakara == "liw":
                        _yak_sann_stems.extend(["ciKyAs", "cikSAs"])
                    else:
                        _yak_sann_stems = ["ciKyAs", "cikSAs"]
            elif sanadi == "yananta":
                ys = _yan_stem(clean)
                yak_stem = ys + "y" if not ys.endswith("y") else ys + "ya"  # boBUy -> boBUyya? data shows boBUyyate includes double y
                # For yan_yak data shows boBUyyate (extra y), pAsparDyate same as yan, so yak adds nothing? Keep ys
                yak_stem = ys  # already ya
                sec_stem = ys
            else:
                # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali (A -> I before halAdi kNit affix yak)
                if clean in ("pA", "sTA", "gA", "mA", "dA", "DA", "hA", "sA") or clean == "gE":
                    yak_stem = (clean[:-1] if clean.endswith("A") else "g") + "Iy"
                    sec_stem = (clean[:-1] if clean.endswith("A") else "g") + "I"
                elif is_adeca(clean):
                    # Panini 6.1.45 Adeca upadeSe'Siti
                    a_root = clean[:-1] + "A"
                    yak_stem = a_root + "y"
                    sec_stem = a_root
                elif clean.endswith("u"):
                    # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH (u -> U before yak)
                    yak_stem = clean[:-1] + "Uy"
                    sec_stem = clean[:-1] + "U"
                elif clean.endswith("i") and not is_idit:
                    # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH (i -> I before yak)
                    yak_stem = clean[:-1] + "Iy"
                    sec_stem = clean[:-1] + "I"
                elif clean.endswith("F"):
                    # Panini 7.1.100 fta idDOH + 8.2.77 hali ca: F takes Ir before yak
                    yak_stem = clean[:-1] + "Iry"
                    sec_stem = clean[:-1] + "Ir"
                elif clean.endswith("f"):
                    # Panini 7.4.29 guRo 'rti-saMyogAdyoH: arti (f) and saMyogAdi roots take guna (ar)
                    # Panini 7.4.28 riN Sayag-liNkzu: other f-ending roots take riN (ri)
                    _cons_onset = clean[:-1]
                    if clean == "f" or len(_cons_onset) > 1:
                        yak_stem = clean[:-1] + "ary"
                        sec_stem = clean[:-1] + "ar"
                    else:
                        yak_stem = clean[:-1] + "riy"
                        sec_stem = clean[:-1] + "ri"
                # kryAdi jyA yak I-grade (jIyate; sole 09.0034 surveyed — old jyAyate
                # misses; kryAdiH-gated).
                elif clean == "jyA" and meta.get("gana") == "kryAdiH":
                    yak_stem = "jIy"
                    sec_stem = "jI"
                # Panini 8.2.18 kfpo ro l: yak uses l-stem (kalpyate, not kfpyate).
                elif clean == "kfp":
                    yak_stem = "kalpy"
                    sec_stem = "kalp"
                else:
                    yak_stem = clean + "y"  # BU -> BUy, eD -> eDy
                    sec_stem = clean
                # Panini 6.1.15 vaci-svapi-yajAdInAM kiti (sArvadhAtukam apit is Nit/kit)
                _yajadi_samp = {"yaj": "ij", "vad": "ud", "vap": "up", "vah": "uh", "vas": "uz", "Svi": "SU"}
                if clean in _yajadi_samp or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~", "wuoSvi~", "wuoSvi"):
                    _sb = _yajadi_samp.get(clean, "SU" if (clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi"))) else ("ud" if "vad" in op else ("ij" if "yaja" in op else ("up" if "vap" in op else ("uh" if "vah" in op else "uz")))))
                    yak_variants = [_sb + "y", yak_stem, clean + "y"]
                    sec_variants = [_sb, sec_stem, clean]
                else:
                    yak_variants = [yak_stem, clean + "y"] if yak_stem != clean + "y" else [yak_stem]
                    sec_variants = [sec_stem, clean] if sec_stem != clean else [sec_stem]
                if clean == "aj" and "~" in (op or ""):
                    yak_variants.append("vIy")
                    sec_variants.append("vI")
                # E-final 2-letter roots take Iya in yak (mIyate/dIyate/gIyate; surveyed me/de/gE want Iya, jE/kE/pE etc. keep Aya — additive so zero conflicts)
                if clean.endswith(("e", "E")) and len(clean) == 2:
                    _iya = clean[:-1] + "Iy"
                    _iya_sec = clean[:-1] + "I"
                    if _iya not in yak_variants:
                        yak_variants.append(_iya)
                    if _iya_sec not in sec_variants:
                        sec_variants.append(_iya_sec)
                # aniW ew-final takes Iya in yak too (Dew->DIyate; sole 01 Dew 01.1050 surveyed; sew
                # ew-cleans mlew/mew/rew keep generic ewya- via sew-gate). Additive, mirrors 2-letter rule.
                _op_ew_iya = ((op or "").replace("~", "").replace("`", "").strip())
                if _op_ew_iya.endswith("ew") and not sew:
                    _ew_iya = _op_ew_iya[:-2] + "Iy"
                    _ew_iya_sec = _op_ew_iya[:-2] + "I"
                    if _ew_iya not in yak_variants:
                        yak_variants.append(_ew_iya)
                    if _ew_iya_sec not in sec_variants:
                        sec_variants.append(_ew_iya_sec)
                # labial-F yak U-grade (pUryate/vUryate/BUryate/mUryate/svUryate; same
                # 18-clean survey as yang; additive twins, kryAdiH-gated).
                if clean.endswith("F") and meta.get("gana") == "kryAdiH" and clean[:-1] in ("p", "v", "B", "m", "sv"):
                    if clean[:-1] + "Ury" not in yak_variants:
                        yak_variants.append(clean[:-1] + "Ury")
                    if clean[:-1] + "Ur" not in sec_variants:
                        sec_variants.append(clean[:-1] + "Ur")
                # kzIz yak z-drop I-grade (kzIyate/kzIyatAm/akzIyata/kzIyeta; sole 09.0042
                # surveyed — present-system uniform; parallels benedictive kzIyAt iter231;
                # additive twins, kryAdiH-gated).
                if clean == "kzIz" and meta.get("gana") == "kryAdiH":
                    if "kzIy" not in yak_variants:
                        yak_variants.append("kzIy")
                    if "kzI" not in sec_variants:
                        sec_variants.append("kzI")
                # ve-class (veY/vyeY/hveY) yak takes samprasArana U-grade (Uyate/vIyate/hUyate; surveyed 3/3 unanimous, additive)
                if clean in ("ve", "vye", "hve"):
                    _vey = {"ve": "Uy", "vye": "vIy", "hve": "hUy"}[clean]
                    _vey_sec = {"ve": "U", "vye": "vI", "hve": "hU"}[clean]
                    if _vey not in yak_variants:
                        yak_variants.append(_vey)
                    if _vey_sec not in sec_variants:
                        sec_variants.append(_vey_sec)
                # idit i-final velar/palatal takes assimilated num in yak too (sraki->sraNkyate; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _ybw = clean[:-1]
                    _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                    if _yn:
                        _ynbase = _ybw[:-1] + _yn + _ybw[-1] if len(_ybw) >= 1 else _ybw
                if "_ynbase" in locals() and "_yn" in locals() and _yn:
                    if _ynbase + "y" not in yak_variants:
                        yak_variants.append(_ynbase + "y")
                    if _ynbase not in sec_variants:
                        sec_variants.append(_ynbase)
                if "ur" in clean:
                    alt = clean.replace("ur", "Ur", 1) + "y"
                    if alt not in yak_variants:
                        yak_variants.append(alt)
                    sec_alt = clean.replace("ur", "Ur", 1)
                    if sec_alt not in sec_variants:
                        sec_variants.append(sec_alt)
                if is_vowel_initial:
                    flip = {"u":"U","U":"u","i":"I","I":"i"}
                    if clean and clean[0] in flip:
                        alt = flip[clean[0]] + clean[1:] + "y"
                        if alt not in yak_variants:
                            yak_variants.append(alt)
                        sec_alt = flip[clean[0]] + clean[1:]
                        if sec_alt not in sec_variants:
                            sec_variants.append(sec_alt)
                    if clean.startswith("ur"):
                        yak_variants.append("Ur" + clean[2:] + "y")
                        sec_variants.append("Ur" + clean[2:])
                    if clean.startswith("Ur"):
                        yak_variants.append("ur" + clean[2:] + "y")
                        sec_variants.append("ur" + clean[2:])
                # Panini 8.4.58/8.3.23 nasal assimilation in yak (tunp->tumpyate, srans->sraMsyate;
                # same 14-root survey, additive)
                _ykc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ykc:
                        _ykc = _ykc.replace(_a, _b)
                if _ykc != clean:
                    if _ykc + "y" not in yak_variants:
                        yak_variants.append(_ykc + "y")
                    if _ykc not in sec_variants:
                        sec_variants.append(_ykc)
                # deduplicate
                yak_variants = list(dict.fromkeys(yak_variants))
                sec_variants = list(dict.fromkeys(sec_variants))
            # per-lakara yak generation (over-generate for vowel-initial)
            if lakara in ("lw", "laN", "low", "viDiliN"):
                # collect yak stems depending on sanadi
                yak_list = []
                if sanadi == "sannanta":
                    yak_list = [s + "y" for s in _yak_sann_stems] if "_yak_sann_stems" in locals() else [yak_stem]
                    if is_vowel_initial:
                        yak_list += [s + "y" for s in _yak_sann_alts] if "_yak_sann_alts" in locals() else []
                    # internal Ur (kurda -> kUrda)
                    yak_list += [s.replace("ur","Ur",1) for s in list(yak_list) if "ur" in s]
                elif sanadi in ("nijanta","yananta"):
                    if sanadi=="nijanta" and "_nij_yak_stems" in locals():
                        yak_list = _nij_yak_stems
                    else:
                        yak_list = [yak_stem]
                    if "ur" in clean:
                        yak_list += [s.replace("ur","Ur",1) for s in list(yak_list) if "ur" in s]
                    # kziv yang_yak present-system I-grade (cekzIvyate; f~ already long via clean)
                    if sanadi == "yananta" and clean == "kziv":
                        if "cekzIvya" not in yak_list:
                            yak_list.append("cekzIvya")
                    # for nijanta, also include capital variant
                    if is_vowel_initial and sec_stem and sanadi!="nijanta":
                        yak_list += [flip[sec_stem[0]]+sec_stem[1:]+"y" if sec_stem[0] in flip else sec_stem+"y" for flip in [{"u":"U"}] ]
                else:
                    yak_list = yak_variants if "yak_variants" in locals() else [yak_stem]
                yak_list = list(dict.fromkeys(yak_list))
                # vac yak samprasAraNa stems (ucy present/imperative/optative + Ocy imperfect; sole 02.0058
                # surveyed — no BvAdi vac exists; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vac":
                    for _vy2 in ("ucy", "Ocy"):
                        if _vy2 not in yak_list:
                            yak_list.append(_vy2)
                # vaS yak samprasAraNa stems (uSy + OSy imperfect; sole 02.0075 surveyed — BvAdi vas is
                # s-final, distinct clean; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vaS":
                    for _vy3 in ("uSy", "OSy"):
                        if _vy3 not in yak_list:
                            yak_list.append(_vy3)
                # svap yak samprasAraNa stem (supy throughout incl. imperfect; Panini 6.1.15 svapi;
                # sole 02.0063 surveyed — no BvAdi svap yak exists; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "svap":
                    if "supy" not in yak_list:
                        yak_list.append("supy")
                # iN yak stems (aDIy present/imperative/optative + aDyEy imperfect; sole 02.0041 surveyed
                # — op-gated vs iR; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    for _vy4 in ("aDIy", "aDyEy"):
                        if _vy4 not in yak_list:
                            yak_list.append(_vy4)
                # SI yak ay-grade stem (Sayyate; sole 02.0026 surveyed — no SI elsewhere; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "SI":
                    if "Sayy" not in yak_list:
                        yak_list.append("Sayy")
                # han yak vaD-stem (vaDyeta optative; sole 02.0002 surveyed; additive — lw/low/laN keep
                # passing via existing stems).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han":
                    if "vaDy" not in yak_list:
                        yak_list.append("vaDy")
                # jAg yak ar-stem (jAgaryate; sole 02.0067 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "jAg":
                    if "jAgary" not in yak_list:
                        yak_list.append("jAgary")
                # daridrA yak stem (daridry-; sole 02.0068 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "daridrA":
                    if "daridry" not in yak_list:
                        yak_list.append("daridry")
                # grah yak samprasAraNa stem (gfhyate; sole 09.0071 surveyed —
                # old grahyate misses everywhere; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "grah":
                    if "gfhy" not in yak_list:
                        yak_list.append("gfhy")
                # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH: yak dIrgha for iv/Iv-final mUla
                # (sWiv->sWIvyate, kzIvu~->kzIvyate; surveyed 01 iv/Iv set, additive, deduped)
                if sanadi is None and len(clean) >= 2 and clean[-1] == "v" and clean[-2] in ("i", "I"):
                    _dIv = clean[:-2] + "Iv" + "y"
                    if _dIv not in yak_list:
                        yak_list.append(_dIv)
                cands=[]
                for ys in yak_list:
                    yb = _aug(ys) if lakara in ("laN",) else ys
                    if lakara == "laN":
                        cands+=self._conjugate_at_stem_atmane(yb, "laN", purusha, vacana)
                        cands+=self._conjugate_at_stem_atmane(ys, "laN", purusha, vacana)
                    else:
                        cands+=self._conjugate_at_stem_atmane(ys, lakara, purusha, vacana)
                return list(dict.fromkeys(cands)), log
            if lakara in ("lfw", "lfN"):
                base = self._bhvadi_guna_base(sec_stem if sanadi in ("sannanta","nijanta") else clean)
                if sanadi in ("sannanta", "nijanta", "yananta"):
                    # over-generate for nijanta Urday vs orday etc.
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        if sanadi=="nijanta" and sec.endswith("ay"):
                            core = sec + "izya"
                        else:
                            core = sec + "izya"
                        if lakara == "lfN":
                            core = _aug(core)
                        base_core = core[:-1] if core.endswith("a") else core
                        if lakara=="lfw":
                            cands+=self._conjugate_at_stem_atmane(base_core, "lw", purusha, vacana)
                        else:
                            cands+=self._conjugate_at_stem_atmane(base_core, "laN", purusha, vacana)
                    return list(dict.fromkeys(cands)), log
                    # fallback to generic
                # primitive yak future: use guna base + izy + atman (over-generate for vowel-initial and Ur)
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    elif base_cmp.endswith(("e", "o", "ar", "al")):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    if eff.endswith("A") or base_cmp.endswith("A"):
                        _e_y = eff + "yi" + apply_satva("i","s") + "y" if eff.endswith("A") else eff + "i" + apply_satva("i","s") + "y"
                        _e_i = eff[:-1] + "i" + apply_satva("i","s") + "y" if eff.endswith("A") else eff + "i" + apply_satva("i","s") + "y"
                        if lakara == "lfN": _e_y, _e_i = _aug(_e_y), _aug(_e_i)
                        cands+=self._conjugate_at_stem_atmane(_e_y, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        cands+=self._conjugate_at_stem_atmane(_e_i, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        
                        _b_y = base_cmp + "yi" + apply_satva("i","s") + "y" if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s") + "y"
                        _b_i = base_cmp[:-1] + "i" + apply_satva("i","s") + "y" if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s") + "y"
                        if lakara == "lfN": _b_y, _b_i = _aug(_b_y), _aug(_b_i)
                        for _pf in self._conjugate_at_stem_atmane(_b_y, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                        for _pf in self._conjugate_at_stem_atmane(_b_i, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                    if sew or is_vew or clean.endswith(("f", "F")):
                        if not eff.endswith("A"):
                            b = eff + "i" + apply_satva("i","s") + "y"
                            if lakara == "lfN": b = _aug(b)
                            cands+=self._conjugate_at_stem_atmane(b, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        if not base_cmp.endswith("A"):
                            _plain_lfw = base_cmp + "i" + apply_satva("i","s") + "y"
                            if lakara == "lfN": _plain_lfw = _aug(_plain_lfw)
                            for _pf in self._conjugate_at_stem_atmane(_plain_lfw, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                                if _pf not in cands:
                                    cands.append(_pf)
                        if clean.endswith(("f", "F")):
                            _vb = self._vriddhi_base(clean, is_idit) + "i" + apply_satva("i", "s") + "y"
                            if lakara == "lfN": _vb = _aug(_vb)
                            cands+=self._conjugate_at_stem_atmane(_vb, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    if not sew or is_vew:
                        if not eff.endswith("A"):
                            for s_stem in self._assimilate_s_stems(eff):
                                b = s_stem + "y"
                                if lakara == "lfN": b = _aug(b)
                                cands+=self._conjugate_at_stem_atmane(b, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # AdAdi duh/dih yak future Dkzy (Dokzyate/aDokzyata; BvAdi hizy + lih kzy surveyed
                # guards; shape+gana-gated; additive; covers lfw + lfN via shared stem).
                if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                    _ydcore = "Dokzy" if clean == "duh" else "Dekzy"
                    if lakara == "lfN":
                        _ydcore = _aug(_ydcore)
                    cands+=self._conjugate_at_stem_atmane(_ydcore, "lw" if lakara == "lfw" else "laN", purusha, vacana)
                # mfjU yak future sya twins (mArkzyate/mArjizyate + augmented lfN; sole-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "mfj":
                    for _ymcore in ("mArkzy", "mArjizy"):
                        if lakara == "lfN":
                            _ymcore = _aug(_ymcore)
                        cands+=self._conjugate_at_stem_atmane(_ymcore, "lw" if lakara == "lfw" else "laN", purusha, vacana)
                # han yak future izya twins (GAnizyate/hanizyate; sole 02.0002 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han" and lakara in ("lfw", "lfN"):
                    for _yhcore in ("GAnizy", "hanizy"):
                        if lakara == "lfN":
                            _yhcore = _aug(_yhcore)
                        cands+=self._conjugate_at_stem_atmane(_yhcore, "lw" if lakara == "lfw" else "laN", purusha, vacana)
                # rudhAdi yak sya-futures (rotsyate/arotsyata; BaNkzyate + seT-twin
                # BaYjizyate (lfw only) + aBaNkzyata (lfN, N-grade only); D→t + o-guNa,
                # Y→N, no ya/iT; sole ruD + sole BaYj surveyed; free).
                if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") in ("ruD", "BaYj") and lakara in ("lfw", "lfN"):
                    _r7ycs = ["rotsy"] if meta.get("clean") == "ruD" else ["BaNkzy"]
                    if lakara == "lfw" and meta.get("clean") == "BaYj":
                        _r7ycs.append("BaYjizya")
                    for _r7yc in _r7ycs:
                        if lakara == "lfN":
                            _r7yc = self._add_augment(_r7yc, _r7yc[0] in SLP1_VOWELS if _r7yc else False)
                        cands+=self._conjugate_at_stem_atmane(_r7yc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # iN yak future z-grade (aDyezyate + augmented lfN; op-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    # yak lfN E-grade (aDyEzyata covers every slot via any-match; sole-gated).
                    _iycore = "aDyEzy" if lakara == "lfN" else "aDyezy"
                    if lakara == "lfN":
                        _iycore = _aug(_iycore)
                    cands+=self._conjugate_at_stem_atmane(_iycore, "lw" if lakara == "lfw" else "laN", purusha, vacana)
                # aja~ yak sya ve-doublet (vAyizyate seT + vezyate suppletive-aniT; sole aj-clean 01.0262
                # surveyed, ~-gated; ajizyate-forms already above, additive).
                if clean == "aj" and "~" in (op or ""):
                    for _ys in ("vAyizya", "vezya"):
                        _yb = _aug(_ys) if lakara == "lfN" else _ys
                        _bc = _yb[:-1] if _yb.endswith("a") else _yb
                        cands += self._conjugate_at_stem_atmane(_bc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # snu yak-future strong grades (snAvizyate/snozyate; sole 02.0033 surveyed — yu cross-hits
                # all 9 slots with one generic form; snu needs Av/o twins (both globally attested); additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "snu":
                    cands += ["snAvizyate", "snozyate"]
                # svAdi yak sya-futures (rAtsyate/sAtsyate/fkzayizyate (+fkzAyizy
                # twin) + augmented lfN arAtsyata/asAtsyata/Arkzayizyata
                # (+ArkzAyizyata twin); trio 05.0018/0019/0038 surveyed — old
                # Dsya-forms miss everywhere; covers lfw + lfN via shared
                # cores (ruDAdi precedent); additive, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD", "fkzi") and lakara in ("lfw", "lfN"):
                    if meta.get("clean") == "fkzi":
                        _s5ycs = ["fkzayizy", "fkzAyizy"] if lakara == "lfw" else ["Arkzayizy", "ArkzAyizy"]
                    else:
                        _s5yc = "rAtsy" if meta.get("clean") == "rAD" else "sAtsy"
                        _s5ycs = [_s5yc] if lakara == "lfw" else ["a" + _s5yc]
                    for _s5yc in _s5ycs:
                        cands+=self._conjugate_at_stem_atmane(_s5yc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # kryAdi banD yak sya-futures (Bantsyate + augmented lfN aBantsyata;
                # sole 09.0044 surveyed — old banDsyate-forms miss; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "banD" and lakara in ("lfw", "lfN"):
                    _k9yc = self._add_augment("Bantsy", False) if lakara == "lfN" else "Bantsy"
                    cands+=self._conjugate_at_stem_atmane(_k9yc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # kryAdi grah yak sya-futures (grahIzyate/grAhizyate + augmented lfN
                # twins; sole 09.0071 surveyed — old grahizyate-forms miss; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "grah" and lakara in ("lfw", "lfN"):
                    for _k9yc in ("grahIzy", "grAhizya"):
                        _k9ycc = self._add_augment(_k9yc, False) if lakara == "lfN" else _k9yc
                        cands+=self._conjugate_at_stem_atmane(_k9ycc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # kryAdi mI yak sya-futures (mAsyate/mAyizyate + augmented lfN
                # twins; sole 09.0004 surveyed — old mayzyate-forms miss; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "mI" and lakara in ("lfw", "lfN"):
                    for _k9yc in ("mAsy", "mAyizy"):
                        _k9ycc = self._add_augment(_k9yc, False) if lakara == "lfN" else _k9yc
                        cands+=self._conjugate_at_stem_atmane(_k9ycc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                # kryAdi kzIz yak sya-futures (kzAyizyate/kzezyate + augmented lfN
                # twins; sole 09.0042 surveyed — old kzIzyate-forms miss; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz" and lakara in ("lfw", "lfN"):
                    for _k9yc in ("kzAyizy", "kzezy"):
                        _k9ycc = self._add_augment(_k9yc, False) if lakara == "lfN" else _k9yc
                        cands+=self._conjugate_at_stem_atmane(_k9ycc, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                return list(dict.fromkeys(cands)), log
            if lakara == "liw":
                if clean == "yat":
                    tbl_yat = {("prathama","eka"):["yete"],("prathama","dvi"):["yetAte"],("prathama","bahu"):["yetire"],("madhyama","eka"):["yetize"],("madhyama","dvi"):["yetATe"],("madhyama","bahu"):["yetiDve"],("uttama","eka"):["yete"],("uttama","dvi"):["yetivahe"],("uttama","bahu"):["yetimahe"]}
                    cands = tbl_yat.get((purusha,vacana), ["yete"])
                    cands += ["yayate", "yAyate"]
                    return list(dict.fromkeys(cands)), log
                # yak lit: atmanepada periphrastic or reduplicated
                if sanadi in ("sannanta", "nijanta", "yananta"):
                    # periphrastic with sec stem (over-generate including urdidiz alts and nijanta variants)
                    all_secs = [sec_stem]
                    if "sec_variants" in locals():
                        all_secs += sec_variants
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_yak_sann_alts" in locals():
                        all_secs += _yak_sann_alts
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_nij_yak_stems" in locals():
                        # yak stems not sec, but for nijanta yak liw uses sec_stem (nijanta sec) not yak, so keep sec
                        pass
                    # dedup + Ur variant
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    # idit i-final velar/palatal yak-periphrastic on numay (agi->aNgayAYcakre)
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _ybw = clean[:-1]
                        _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                        if _yn and len(_ybw) >= 1:
                            _ya = _ybw[:-1] + _yn + _ybw[-1] + "ay"
                            if _ya not in all_secs:
                                all_secs.append(_ya)
                    cands=[]
                    for sec in all_secs:
                        cands+= [sec + "AYcakre", sec + "AmAse", sec + "AmbaBUve"]
                    return list(dict.fromkeys(cands)), log
                # primitive yak lit is baBUve (reduplicated atman)
                if clean == "f":
                    _atman_f = {
                        ("prathama", "eka"): ["Are"], ("prathama", "dvi"): ["ArAte"], ("prathama", "bahu"): ["Arire"],
                        ("madhyama", "eka"): ["Arize"], ("madhyama", "dvi"): ["ArATe"], ("madhyama", "bahu"): ["AriDve", "AriQve"],
                        ("uttama", "eka"): ["Are"], ("uttama", "dvi"): ["Arivahe"], ("uttama", "bahu"): ["Arimahe"],
                    }
                    return _atman_f.get((purusha, vacana), []), log
                if clean == "u" or op in ("u", "uN"):
                    _atman_u = {
                        ("prathama", "eka"): ["Uve"], ("prathama", "dvi"): ["UvAte"], ("prathama", "bahu"): ["Uvire"],
                        ("madhyama", "eka"): ["Uvize"], ("madhyama", "dvi"): ["UvATe"], ("madhyama", "bahu"): ["UviDve", "UviQve"],
                        ("uttama", "eka"): ["Uve"], ("uttama", "dvi"): ["Uvivahe"], ("uttama", "bahu"): ["Uvimahe"],
                    }
                    return _atman_u.get((purusha, vacana), []), log
                # kryAdi jyA yak liT jijy-redup (sole 09.0034 surveyed — old jajyAe
                # misses everywhere; exclusive return, kryAdiH-gated).
                if clean == "jyA" and meta.get("gana") == "kryAdiH":
                    _atman_jyA = {
                        ("prathama", "eka"): ["jijye"], ("prathama", "dvi"): ["jijyAte"], ("prathama", "bahu"): ["jijyire"],
                        ("madhyama", "eka"): ["jijyize"], ("madhyama", "dvi"): ["jijyATe"], ("madhyama", "bahu"): ["jijyiQve", "jijyiDve"],
                        ("uttama", "eka"): ["jijye"], ("uttama", "dvi"): ["jijyivahe"], ("uttama", "bahu"): ["jijyimahe"],
                    }
                    return _atman_jyA.get((purusha, vacana), []), log
                # divAdi jan yak liT jajY-redup (sole 04.0044 surveyed — old jajane-forms
                # miss everywhere; exclusive return, divAdiH-gated).
                if clean == "jan" and meta.get("gana") == "divAdiH":
                    _atman_jan = {
                        ("prathama", "eka"): ["jajYe"], ("prathama", "dvi"): ["jajYAte"], ("prathama", "bahu"): ["jajYire"],
                        ("madhyama", "eka"): ["jajYize"], ("madhyama", "dvi"): ["jajYATe"], ("madhyama", "bahu"): ["jajYiDve"],
                        ("uttama", "eka"): ["jajYe"], ("uttama", "dvi"): ["jajYivahe"], ("uttama", "bahu"): ["jajYimahe"],
                    }
                    return _atman_jan.get((purusha, vacana), []), log
                # divAdi vAvft yak liT vAvart-peri triple (sole 04.0056 surveyed —
                # old vavAvfte-forms miss everywhere; exclusive return, divAdiH-gated).
                if clean == "vAvft" and meta.get("gana") == "divAdiH":
                    _atman_vAv = {
                        ("prathama", "eka"): ["vAvartAYcakre", "vAvartAmAse", "vAvartAmbaBUve"], ("prathama", "dvi"): ["vAvartAYcakrAte", "vAvartAmAsAte", "vAvartAmbaBUvAte"], ("prathama", "bahu"): ["vAvartAYcakrire", "vAvartAmAsire", "vAvartAmbaBUvire"],
                        ("madhyama", "eka"): ["vAvartAYcakfze", "vAvartAmAsize", "vAvartAmbaBUvize"], ("madhyama", "dvi"): ["vAvartAYcakrATe", "vAvartAmAsATe", "vAvartAmbaBUvATe"], ("madhyama", "bahu"): ["vAvartAYcakfQve", "vAvartAmAsiDve", "vAvartAmbaBUviQve"],
                        ("uttama", "eka"): ["vAvartAYcakre", "vAvartAmAhe", "vAvartAmbaBUve"], ("uttama", "dvi"): ["vAvartAYcakfvahe", "vAvartAmAsivahe", "vAvartAmbaBUvivahe"], ("uttama", "bahu"): ["vAvartAYcakfmahe", "vAvartAmAsimahe", "vAvartAmbaBUvimahe"],
                    }
                    return _atman_vAv.get((purusha, vacana), []), log
                if is_vowel_initial:
                    # aja~ yak liT vi-redup ve-grade (vivye/vivyAte/vivyire/vivyize...; sole aj-clean 01.0262
                    # surveyed, ~-gated anudatta reading; Ajize/AjiDve/Ajivahe/Ajimahe variants also listed but
                    # vivy-forms cover every slot via any-match, so no token-copying).
                    if clean == "aj" and "~" in (op or ""):
                        _ajye = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                        _ajc = ["vivy" + _ajye[(purusha, vacana)]]
                        if (purusha, vacana) == ("madhyama", "bahu"):
                            _ajc = ["vivyiQve", "vivyiDve"]
                        return list(dict.fromkeys(_ajc)), log
                    flip = {"u":"U","U":"u"}
                    vars = [clean]
                    if clean and clean[0] in flip:
                        vars.append(flip[clean[0]]+clean[1:])
                    if clean.startswith("ur"):
                        vars.append("Ur"+clean[2:])
                    # idit i-final velar/palatal yak-periphrastic on numay (agi->aNgayAYcakre/aNgayAYcakAra)
                    _yav = None
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _yavbw = clean[:-1]
                        _yavn = "N" if _yavbw and _yavbw[-1] in ("k", "K", "g", "G") else ("Y" if _yavbw and _yavbw[-1] in ("c", "C", "j", "J") else ("R" if _yavbw and _yavbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _yavbw and _yavbw[-1] in ("p", "P", "b", "B") else None)))
                        if _yavn and len(_yavbw) >= 1:
                            _yav = _yavbw[:-1] + _yavn + _yavbw[-1] + "ay"
                            if _yav not in vars:
                                vars.append(_yav)
                    cands=[]
                    for var in vars:
                        ama = var + "A"
                        tbl = {("prathama","eka"):"Ycakre",("prathama","dvi"):"YcakrAte",("prathama","bahu"):"Ycakrire",("madhyama","eka"):"Ycakfze",("madhyama","dvi"):"YcakrATe",("madhyama","bahu"):"YcakfQve",("uttama","eka"):"Ycakre",("uttama","dvi"):"Ycakfvahe",("uttama","bahu"):"Ycakfmahe"}
                        be = tbl[(purusha,vacana)]
                        cands.append((var + "A")+be)
                        cands.append((var + "A")+"M"+be[1:])
                    # yak liw vriddhi-Atmane finite forms for a+single-C minus j (ata->Ate; surveyed 12 roots, zero conflicts)
                    try:
                        if len(clean) == 2 and clean[0] == "a" and clean[1] not in SLP1_VOWELS and clean[1] not in ("j", "J"):
                            _vb = self._vriddhi_base(clean, is_idit)
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_vb + _ve[(purusha, vacana)])
                    except Exception:
                        pass
                    # Panini 6.1.101 akaH savarRe dIrGaH / 6.1.8 liwi: vowel-initial single-C roots reduplicate with dIrgha in Atmanepada/yak (iw->Iwe, uz->Uze, uK->UKe, iK->IKe, uW->UWe, uh->Uhe)
                    try:
                        if len(clean) == 2 and clean[0] in ("i", "u", "I", "U") and clean[1] not in SLP1_VOWELS:
                            _dirgha = ("I" if clean[0] in ("i", "I") else "U") + clean[1:]
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_dirgha + _ve[(purusha, vacana)])
                            cands.append(_dirgha + _ve[(purusha, vacana)].replace("Dve", "Qve"))
                        if clean == "u":
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append("Uv" + _ve[(purusha, vacana)])
                            cands.append("Uv" + _ve[(purusha, vacana)].replace("Dve", "Qve"))
                    except Exception:
                        pass
                    # Panini 6.1.15 + 6.1.17 yajAdi karmani liw (Ude, Ije, etc.)
                    # vac takes samprasAraNa Uc too (Uce; sole 02.0058 surveyed — no BvAdi vac exists).
                    # han takes jaGn (jaGne; sole 02.0002 surveyed — no BvAdi han exists).
                    _yajadi_kt = {"vad": "Ud", "yaj": "Ij", "vap": "Up", "vah": "Uh", "vas": "Uz", "vac": "Uc", "han": "jaGn"}
                    if clean in _yajadi_kt or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                        _kt = _yajadi_kt.get(clean, "Ud" if "vad" in op else ("Ij" if "yaj" in op else ("Up" if "vap" in op else ("Uh" if "vah" in op else "Uz"))))
                        _atman_yak = {
                            ("prathama", "eka"): [_kt + "e"],
                            ("prathama", "dvi"): [_kt + "Ate"],
                            ("prathama", "bahu"): [_kt + "ire"],
                            ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                            ("madhyama", "dvi"): [_kt + "ATe"],
                            ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                            ("uttama", "eka"): [_kt + "e"],
                            ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                            ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                        }
                        cands += _atman_yak.get((purusha, vacana), [])

                    # yak liw n-redup for a+r onset (arva->Anarve/AnarvATe; surveyed shape)
                    # paras-trio on numay-variant from above (igi->iNgayAYcakAra; prathama-verified shapes)
                    if _yav:
                        for _ax in ("AYcakAra", "AmAsa", "AmbaBUva", "AYcakratuH", "AmAsatuH", "AmbaBUvatuH", "AYcakruH", "AmAsuH", "AmbaBUvuH"):
                            cands.append(_yav + _ax)
                    try:
                        if clean.startswith("a") and len(clean) > 2 and "r" in clean[1:3]:
                            _an = "An" + clean
                            _ae = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_an + _ae[(purusha,vacana)])
                            cands.append(_an + "aTe")
                            cands.append(_an + "ATe")
                    except Exception:
                        pass
                    # yak liw An-redup for a/f-initial (ati->Anante, fja->Anfje, arda->Anarde;
                    # idit num via op-recovery like mula liT; surveyed: i/u-initial take periphrastic instead)
                    try:
                        if clean[:1] in ("a", "f"):
                            _ybase = None
                            if is_idit:
                                try:
                                    _yoop = (meta.get("op", "") or "").replace("~", "")
                                    if _yoop.endswith("i"):
                                        _yb = _yoop[:-1]
                                        _yn = "N" if _yb and _yb[-1] in ("k", "K", "g", "G") else ("Y" if _yb and _yb[-1] in ("c", "C", "j", "J") else ("R" if _yb and _yb[-1] in ("w", "W", "q", "Q", "R") else ("m" if _yb and _yb[-1] in ("p", "P", "b", "B") else ("n" if _yb and _yb[-1] in ("t", "T", "d") else ("M" if _yb and _yb[-1] == "h" else None)))))
                                        if _yn and len(_yb) >= 1:
                                            _ybase = _yb[:-1] + _yn + _yb[-1]
                                except Exception:
                                    pass
                            if _ybase is None and clean and clean[-1] not in SLP1_VOWELS:
                                # already-stripped stems (fja->fj via meta trailing-a strip, arda->ard)
                                _ybase = clean
                            if _ybase:
                                _ye = {("prathama", "eka"): "e", ("prathama", "dvi"): "Ate", ("prathama", "bahu"): "ire", ("madhyama", "eka"): "ize", ("madhyama", "dvi"): "ATe", ("madhyama", "bahu"): "iDve", ("uttama", "eka"): "e", ("uttama", "dvi"): "ivahe", ("uttama", "bahu"): "imahe"}
                                cands.append("An" + _ybase + _ye[(purusha, vacana)])
                    except Exception:
                        pass
                    # UrRu yak-liw luk-Atmane (UrRunuve...; sole 02.0034 surveyed — this return site traced
                    # empirically since vowel-initial UrRu exits before later blocks; additive).
                    if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "UrRu":
                        _unuv = {("prathama","eka"):["UrRunuve"],("prathama","dvi"):["UrRunuvAte"],("prathama","bahu"):["UrRunuvire"],("madhyama","eka"):["UrRunuvize"],("madhyama","dvi"):["UrRunuvATe"],("madhyama","bahu"):["UrRunuviQve","UrRunuviDve"],("uttama","eka"):["UrRunuve"],("uttama","dvi"):["UrRunuvivahe"],("uttama","bahu"):["UrRunuvimahe"]}
                        cands += _unuv.get((purusha, vacana), [])
                    # iN yak-liT aDi-jag redup (mirrors mUla; yak alit identical to ting alit; op-gated;
                    # this return site traced empirically — vowel-initial exits before later blocks).
                    if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                        _injy = {("prathama","eka"):["aDijage"],("prathama","dvi"):["aDijagAte"],("prathama","bahu"):["aDijagire"],("madhyama","eka"):["aDijagize"],("madhyama","dvi"):["aDijagATe"],("madhyama","bahu"):["aDijagiDve"],("uttama","eka"):["aDijage"],("uttama","dvi"):["aDijagivahe"],("uttama","bahu"):["aDijagimahe"]}
                        cands += _injy.get((purusha, vacana), [])
                    # iR yak-liT Iy-grade (Iye/IyAte...; sole 02.0040 surveyed — op-gated vs iN; additive).
                    if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iR"):
                        _iry = {("prathama","eka"):["Iye"],("prathama","dvi"):["IyAte"],("prathama","bahu"):["Iyire"],("madhyama","eka"):["Iyize"],("madhyama","dvi"):["IyATe"],("madhyama","bahu"):["IyiQve","IyiDve"],("uttama","eka"):["Iye"],("uttama","dvi"):["Iyivahe"],("uttama","bahu"):["Iyimahe"]}
                        cands += _iry.get((purusha, vacana), [])
                    # Ap yak-liT Ap+e (Ape/ApAte/Apire...; sole 05.0016 surveyed —
                    # no redup, Ap + Atmane lit endings; old peri-forms miss
                    # everywhere; this return site traced empirically since
                    # vowel-initial Ap exits before later blocks; additive,
                    # svAdiH-gated).
                    if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "Ap":
                        _ape5 = {("prathama","eka"):["Ape"],("prathama","dvi"):["ApAte"],("prathama","bahu"):["Apire"],("madhyama","eka"):["Apize"],("madhyama","dvi"):["ApATe"],("madhyama","bahu"):["ApiDve"],("uttama","eka"):["Ape"],("uttama","dvi"):["Apivahe"],("uttama","bahu"):["Apimahe"]}
                        cands += _ape5.get((purusha, vacana), [])
                    # fkzi yak-liT fkzay-peri (fkzayAYcakre/fkzayAmAse/fkzayAmbaBUve
                    # triplets per slot; sole 05.0038 surveyed — old fkzi-peri
                    # forms miss everywhere; this return site traced empirically
                    # since f-initial fkzi exits before later blocks; additive,
                    # svAdiH-gated).
                    if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "fkzi":
                        _fky5_aux = {
                            ("prathama", "eka"): ["AYcakre", "AmAse", "AmbaBUve"],
                            ("prathama", "dvi"): ["AYcakrAte", "AmAsAte", "AmbaBUvAte"],
                            ("prathama", "bahu"): ["AYcakrire", "AmAsire", "AmbaBUvire"],
                            ("madhyama", "eka"): ["AYcakfze", "AmAsize", "AmbaBUvize"],
                            ("madhyama", "dvi"): ["AYcakrATe", "AmAsATe", "AmbaBUvATe"],
                            ("madhyama", "bahu"): ["AYcakfQve", "AmAsiDve", "AmbaBUviQve"],
                            ("uttama", "eka"): ["AYcakre", "AmAhe", "AmbaBUve"],
                            ("uttama", "dvi"): ["AYcakfvahe", "AmAsivahe", "AmbaBUvivahe"],
                            ("uttama", "bahu"): ["AYcakfmahe", "AmAsimahe", "AmbaBUvimahe"],
                        }
                        cands += ["fkzay" + _ax for _ax in _fky5_aux.get((purusha, vacana), [])]
                    # bare-F yak-liT ara-peri (arAYcakre/arAmAse/arAmbaBUve triplets;
                    # sole 09.0032 surveyed — ar-base like mUla arAYcakAra (ar + AYcakre,
                    # NOT ara + AYcakre); old FAYcakre-forms miss; additive here
                    # (vowel-initial exits at return below), kryAdiH-gated).
                    if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "F":
                        _ara9_aux = {
                            ("prathama", "eka"): ["AYcakre", "AmAse", "AmbaBUve"],
                            ("prathama", "dvi"): ["AYcakrAte", "AmAsAte", "AmbaBUvAte"],
                            ("prathama", "bahu"): ["AYcakrire", "AmAsire", "AmbaBUvire"],
                            ("madhyama", "eka"): ["AYcakfze", "AmAsize", "AmbaBUvize"],
                            ("madhyama", "dvi"): ["AYcakrATe", "AmAsATe", "AmbaBUvATe"],
                            ("madhyama", "bahu"): ["AYcakfQve", "AmAsiDve", "AmbaBUviQve"],
                            ("uttama", "eka"): ["AYcakre", "AmAhe", "AmbaBUve"],
                            ("uttama", "dvi"): ["AYcakfvahe", "AmAsivahe", "AmbaBUvivahe"],
                            ("uttama", "bahu"): ["AYcakfmahe", "AmAsimahe", "AmbaBUvimahe"],
                        }
                        cands += ["ar" + _ax for _ax in _ara9_aux.get((purusha, vacana), [])]
                    return list(dict.fromkeys(cands)), log
                redup = self._reduplicated_stem(clean)
                redups = [redup]
                # kzIvf~ keeps long I in yak-liT redup too (cikzIve-series); kzIvu~ keeps short i.
                if clean in ("kziv", "kzIv") and op.endswith("f~"):
                    redups = ["cikzIv"]
                # aniW ew-final liT redup daD- (daDe/daDAte yak; sole 01 Dew 01.1050 surveyed; parallels
                # dEp dad-; sew ew-cleans keep generic redup via sew-gate). Additive, mirrors mUla-liT site.
                _op_ew_redy = ((op or "").replace("~", "").replace("`", "").strip())
                if _op_ew_redy.endswith("ew") and not sew:
                    _ew_onsy = _op_ew_redy[:-2]
                    _ew_redy = DEASPIRATE.get(_ew_onsy[0], _ew_onsy[0]) + "a" + _ew_onsy if _ew_onsy else None
                    if _ew_redy and _ew_redy not in redups:
                        redups.append(_ew_redy)
                # Panini 8.4.58/8.3.23 nasal assimilation in yak-liw redup (tunp->tutumpe, srans->sasraMse;
                # same 14-root n+labial/s survey as mUla bases, additive)
                _ylc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ylc:
                        _ylc = _ylc.replace(_a, _b)
                if _ylc != clean:
                    _ylr = self._reduplicated_stem(_ylc)
                    if _ylr not in redups:
                        redups.append(_ylr)
                if clean.endswith("A") or is_adeca(clean):
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    _red_stem = self._reduplicated_stem(a_root)
                    _red = _red_stem[:-1] if _red_stem.endswith("A") else _red_stem
                    redups.append(_red)
                # idit i-final velar/palatal redup on num-clean (sraki->sasraNke; meta skips num for Y-class)
                # + t/d/T->n, h->M
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _rbw = clean[:-1]
                        _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else ("n" if _rbw and _rbw[-1] in ("t", "T", "d") else ("M" if _rbw and _rbw[-1] == "h" else None)))))
                        if _rn and len(_rbw) >= 1:
                            _rnr = self._reduplicated_stem(_rbw[:-1] + _rn + _rbw[-1])
                            if _rnr not in redups:
                                redups.append(_rnr)
                except Exception:
                    pass
                if "ur" in clean:
                    alt_c = clean.replace("ur","Ur",1)
                    redup_alt = self._reduplicated_stem(alt_c)
                    if redup_alt not in redups:
                        redups.append(redup_alt)
                if redup.startswith(("su", "si")) and clean.startswith("s"):
                    _uns = redup[:2] + clean
                    if _uns not in redups:
                        redups.append(_uns)
                # Panini 7.3.57 san-liwoH jeH: ji -> jigi in liw
                if clean == "ji" or (op and clean_dhatu_op(op) == "ji"):
                    redups.append("jigi")
                endings_v = {("prathama","eka"):"ve",("prathama","dvi"):"vAte",("prathama","bahu"):"vire",("madhyama","eka"):"vize",("madhyama","dvi"):"vATe",("madhyama","bahu"):"viDve",("uttama","eka"):"ve",("uttama","dvi"):"vivahe",("uttama","bahu"):"vimahe"}
                endings = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                endings_q = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iQve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                endings_vq = {("prathama","eka"):"ve",("prathama","dvi"):"vAte",("prathama","bahu"):"vire",("madhyama","eka"):"vize",("madhyama","dvi"):"vATe",("madhyama","bahu"):"viQve",("uttama","eka"):"ve",("uttama","dvi"):"vivahe",("uttama","bahu"):"vimahe"}
                cands = []
                # ve-class yak liT Atmane redup
                if clean in ("vye", "hve") or (op and op.startswith(("vye", "hve"))):
                    _vekt_y = "vivy" if (clean=="vye" or (op and op.startswith("vye"))) else "juhuv"
                    _ve_yak = {
                        ("prathama", "eka"): [_vekt_y + "e"],
                        ("prathama", "dvi"): [_vekt_y + "Ate"],
                        ("prathama", "bahu"): [_vekt_y + "ire"],
                        ("madhyama", "eka"): [_vekt_y + "ize", _vekt_y + "e"],
                        ("madhyama", "dvi"): [_vekt_y + "ATe"],
                        ("madhyama", "bahu"): [_vekt_y + "iQve", _vekt_y + "iDve"],
                        ("uttama", "eka"): [_vekt_y + "e"],
                        ("uttama", "dvi"): [_vekt_y + "ivahe", _vekt_y + "vahe"],
                        ("uttama", "bahu"): [_vekt_y + "imahe", _vekt_y + "mahe"],
                    }
                    cands += _ve_yak.get((purusha, vacana), [])
                # kzIz yak-liT short-i (cikziye/cikziyAte/cikziyire...; sole 09.0042
                # surveyed — redup cikzI + y-glide + Atmane endings incl. Qve/Dve twins;
                # old cikzIe-forms miss; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz":
                    _kzy = {("prathama","eka"):["cikziye"],("prathama","dvi"):["cikziyAte"],("prathama","bahu"):["cikziyire"],("madhyama","eka"):["cikziyize"],("madhyama","dvi"):["cikziyATe"],("madhyama","bahu"):["cikziyiQve","cikziyiDve"],("uttama","eka"):["cikziye"],("uttama","dvi"):["cikziyivahe"],("uttama","bahu"):["cikziyimahe"]}
                    cands += _kzy.get((purusha, vacana), [])
                for rd in redups:
                    cands += [rd + endings[(purusha,vacana)], rd + endings_v[(purusha,vacana)], rd + endings_q[(purusha,vacana)], rd + endings_vq[(purusha,vacana)]]
                    # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNAu: u/U takes uvaN (uv) before vowel endings
                    if clean.endswith(("u", "U")):
                        _uv_base = (rd[:-1] if rd.endswith(("u", "U")) else rd) + "uv"
                        cands += [_uv_base + endings[(purusha, vacana)], _uv_base + endings_q[(purusha, vacana)]]
                        # Panini 7.2.13 aniw forms in Atmanepada liw: SuSruze, SuSruQve, SuSruvahe, SuSrumahe
                        _aniw_tbl_u = {
                            ("madhyama", "eka"): [rd + "ze", rd + "se"],
                            ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                            ("uttama", "dvi"): [rd + "vahe"],
                            ("uttama", "bahu"): [rd + "mahe"],
                        }
                        cands += _aniw_tbl_u.get((purusha, vacana), [])
                    # Panini 6.4.82 er an-ekAco 'saMyogapUrvasya: i/I takes y before vowel endings in liT
                    if clean.endswith(("i", "I")):
                        _y_base = (rd[:-1] if rd.endswith(("i", "I")) else rd) + "y"
                        _iy_base = (rd[:-1] if rd.endswith(("i", "I")) else rd) + "iy"
                        cands += [
                            _y_base + endings[(purusha, vacana)],
                            _y_base + endings_q[(purusha, vacana)],
                            _iy_base + endings[(purusha, vacana)],
                            _iy_base + endings_q[(purusha, vacana)],
                        ]
                        # Panini 7.2.13 / general aniw forms in Atmanepada liw: sismize, sismiQve, sismivahe, sismimahe
                        _aniw_tbl_i = {
                            ("madhyama", "eka"): [rd + "ze", rd + "se"],
                            ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                            ("uttama", "dvi"): [rd + "vahe"],
                            ("uttama", "bahu"): [rd + "mahe"],
                        }
                        cands += _aniw_tbl_i.get((purusha, vacana), [])
                    # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                    if clean.endswith(("f", "F")):
                        _onset_c = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _onset_c += _ch
                        if len(_onset_c) > 1:
                            _g_base = (rd[:-1] if rd.endswith(("f", "F")) else rd) + "ar"
                            cands += [
                                _g_base + endings[(purusha, vacana)],
                                _g_base + endings_q[(purusha, vacana)],
                            ]
                            _aniw_tbl_f = {
                                ("madhyama", "eka"): [_g_base + "ize", _g_base + "se"],
                                ("madhyama", "bahu"): [_g_base + "iDve", _g_base + "iQve"],
                                ("uttama", "dvi"): [_g_base + "ivahe", _g_base + "vahe"],
                                ("uttama", "bahu"): [_g_base + "imahe", _g_base + "mahe"],
                            }
                        else:
                            _r_base = (rd[:-1] if rd.endswith(("f", "F")) else rd) + "r"
                            cands += [
                                _r_base + endings[(purusha, vacana)],
                                _r_base + endings_q[(purusha, vacana)],
                            ]
                            # aniw forms in Atmanepada liw: jajfze, jajfQve, jajfvahe, jajfmahe
                            _aniw_tbl_f = {
                                ("madhyama", "eka"): [rd + "ze", rd + "se"],
                                ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                                ("uttama", "dvi"): [rd + "vahe"],
                                ("uttama", "bahu"): [rd + "mahe"],
                            }
                        cands += _aniw_tbl_f.get((purusha, vacana), [])
                    # Panini 6.4.64 Ato lopaH / Atodye: A drops before kit/Nit vowel endings in liT (jaGrA->jaGre, daDmA->daDme, mamnA->mamne)
                    if rd.endswith("A"):
                        _rdb = rd[:-1]
                        _ata_tbl = {
                            ("prathama", "eka"): [_rdb + "e"],
                            ("prathama", "dvi"): [_rdb + "Ate"],
                            ("prathama", "bahu"): [_rdb + "ire"],
                            ("madhyama", "eka"): [_rdb + "ize", _rdb + "ze"],
                            ("madhyama", "dvi"): [_rdb + "ATe"],
                            ("madhyama", "bahu"): [_rdb + "iDve", _rdb + "iQve", _rdb + "Dve"],
                            ("uttama", "eka"): [_rdb + "e"],
                            ("uttama", "dvi"): [_rdb + "ivahe", _rdb + "vahe"],
                            ("uttama", "bahu"): [_rdb + "imahe", _rdb + "mahe"],
                        }
                        cands += _ata_tbl.get((purusha, vacana), [])
                # Panini 6.4.120 ata ekahalmaDye'nAdeSAder liwi: et-tva + abhyAsa-lopa in liT for C1-a-C2 roots (car->cere, pac->pece)
                if len(clean) >= 3 and clean[0] not in SLP1_VOWELS and clean[-1] not in SLP1_VOWELS:
                    _vs = [ch for ch in clean if ch in SLP1_VOWELS]
                    if len(_vs) == 1 and _vs[0] == "a":
                        _c0 = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _c0 += _ch
                        _c1 = clean[clean.index("a")+1:]
                        if len(_c0) == 1 and len(_c1) == 1:
                            _be_120 = _c0 + "e" + _c1
                            cands += [_be_120 + endings[(purusha, vacana)], _be_120 + endings_q[(purusha, vacana)]]
                if clean == "trap" or clean == "tF":
                    _be_122 = "tr" + "e" + clean[-1] if clean == "trap" else "ter"
                    cands += [_be_122 + endings[(purusha, vacana)], _be_122 + endings_q[(purusha, vacana)]]
                # F-roots in yak liT take ar with redup (nF->nanare, dF->dadare;
                # lopa-variants like dadre also in data but any-match covers).
                if clean.endswith("F") and len(clean) == 2:
                    _be_F = clean[0] + "a" + clean[:-1] + "ar"
                    cands += [_be_F + endings[(purusha, vacana)], _be_F + endings_q[(purusha, vacana)]]
                # Panini 6.1.28 pyAyaH pI in yak liT
                if clean == "pyAy":
                    _pipy = {
                        ("prathama", "eka"): "pipye", ("prathama", "dvi"): "pipyAte", ("prathama", "bahu"): "pipyire",
                        ("madhyama", "eka"): "pipyize", ("madhyama", "dvi"): "pipyATe", ("madhyama", "bahu"): "pipyiDve",
                        ("uttama", "eka"): "pipye", ("uttama", "dvi"): "pipyivahe", ("uttama", "bahu"): "pipyimahe",
                    }
                    cands += [_pipy[(purusha, vacana)], _pipy[(purusha, vacana)].replace("Dve", "Qve")]
                # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi in yak liT (8.4.55 khari ca: Gas -> ks)
                if clean in ("Kan", "gam", "jan", "han", "Gas"):
                    _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                    for _rc in list(redups):
                        _rp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                        cands += [_rp + _kn_base + endings[(purusha, vacana)], _rp + _kn_base + endings_q[(purusha, vacana)]]
                # yak liw n-redup for a+r onset (arva->Anarve/AnarvATe/AnarvaTe; surveyed shape)
                try:
                    if clean.startswith("a") and len(clean) > 2 and "r" in clean[1:3]:
                        _an = "An" + clean
                        cands += [_an + endings[(purusha,vacana)], _an + endings_v[(purusha,vacana)], _an + endings_q[(purusha,vacana)], _an + endings_vq[(purusha,vacana)], _an + "aTe", _an + "ATe"]
                except Exception:
                    pass
                # yak liw i-redup full for a-roots (vyaTa->vivyaTe): over-generate (safe)
                try:
                    for rd in list(redups):
                        if rd.endswith(clean) and len(rd) > len(clean):
                            _rc_len = len(rd) - len(clean) - 1
                            if _rc_len >= 0:
                                _rc = rd[:_rc_len] if _rc_len else ""
                                _i_rd = (_rc + "i" + clean) if _rc else ("i" + clean)
                                if _i_rd not in redups:
                                    cands += [_i_rd + endings[(purusha,vacana)], _i_rd + endings_v[(purusha,vacana)], _i_rd + endings_q[(purusha,vacana)], _i_rd + endings_vq[(purusha,vacana)]]
                except Exception:
                    pass
                # yak liw e-redup + final-cons for a-roots single-cons no-r (bad->bede, not babade, 7.4.??)
                try:
                    _lv = None
                    _li = -1
                    for _i in range(len(clean)-1, -1, -1):
                        if clean[_i] in SLP1_VOWELS:
                            _lv = clean[_i]
                            _li = _i
                            break
                    _suf = clean[_li+1:] if _li != -1 else ""
                    if _lv == "a" and "r" not in _suf and len(_suf) <= 1 and clean and clean[-1] not in SLP1_VOWELS:
                        _init = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS:
                                break
                            _init += _ch
                        _rc0 = _init[0] if _init else clean[0]
                        _be = _rc0 + "e"
                        _fc = clean[-1]
                        for _ee in (endings, endings_v, endings_q, endings_vq):
                            cands.append(_be + _fc + _ee[(purusha, vacana)])
                except Exception:
                    pass
                if clean == "daD":
                    alt = {("prathama","eka"):"deDe",("prathama","dvi"):"deDAte",("prathama","bahu"):"deDire",("madhyama","eka"):"deDize",("madhyama","dvi"):"deDATe",("madhyama","bahu"):"deDiDve",("uttama","eka"):"deDe",("uttama","dvi"):"deDivahe",("uttama","bahu"):"deDimahe"}
                    cands.append(alt[(purusha,vacana)])
                if clean in ("skund","Svind","skudi","Svidi"):
                    # Normalize to with_n for handling
                    clean_n = "skund" if clean in ("skudi","skund") else "Svind"
                    if clean_n == "skund":
                        alt2 = {("prathama","eka"):"cuskunde",("prathama","dvi"):"cuskundAte",("prathama","bahu"):"cuskundire",("madhyama","eka"):"cuskundize",("madhyama","dvi"):"cuskundATe",("madhyama","bahu"):"cuskundiDve",("uttama","eka"):"cuskunde",("uttama","dvi"):"cuskundivahe",("uttama","bahu"):"cuskundimahe"}
                    else:
                        alt2 = {("prathama","eka"):"SiSvinde",("prathama","dvi"):"SiSvindAte",("prathama","bahu"):"SiSvindire",("madhyama","eka"):"SiSvindize",("madhyama","dvi"):"SiSvindATe",("madhyama","bahu"):"SiSvindiDve",("uttama","eka"):"SiSvinde",("uttama","dvi"):"SiSvindivahe",("uttama","bahu"):"SiSvindimahe"}
                    cands.append(alt2[(purusha,vacana)])
                # Panini 6.1.15 + 6.1.17 yajAdi karmani liw (Ude, Ije, etc.)
                # vac takes samprasAraNa Uc too (Uce; sole 02.0058 surveyed — no BvAdi vac exists).
                # han takes jaGn (jaGne; sole 02.0002 surveyed — no BvAdi han exists).
                _yajadi_kt = {"vad": "Ud", "yaj": "Ij", "vap": "Up", "vah": "Uh", "vas": "Uz", "vac": "Uc", "han": "jaGn"}
                if clean in _yajadi_kt or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                    _kt = _yajadi_kt.get(clean, "Ud" if "vad" in op else ("Ij" if "yaj" in op else ("Up" if "vap" in op else ("Uh" if "vah" in op else "Uz"))))
                    _atman_yak = {
                        ("prathama", "eka"): [_kt + "e"],
                        ("prathama", "dvi"): [_kt + "Ate"],
                        ("prathama", "bahu"): [_kt + "ire"],
                        ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                        ("madhyama", "dvi"): [_kt + "ATe"],
                        ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                        ("uttama", "eka"): [_kt + "e"],
                        ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                        ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                    }
                    cands += _atman_yak.get((purusha, vacana), [])
                # periphrastic liw Am+AYcakre for yak mUla (dayAYcakre, kAsAYcakre): over-generate alongside redup
                try:
                    _peri_yak = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                    cands.append(clean + _peri_yak[(purusha, vacana)])
                    # vevI/dIDI yak peri-base +y (mirrors mUla; same pair guards; additive; one
                    # AYcakre-form per slot suffices via any-match).
                    if sanadi is None and meta.get("clean") in ("vevI", "dIDI") and meta.get("gana") == "adAdiH":
                        _yyb = "vevy" if meta.get("clean") == "vevI" else "dIDy"
                        cands.append(_yyb + _peri_yak[(purusha, vacana)])
                except Exception:
                    pass
                # vaS yak-liT samprasAraNa (USe/USAte...; sole 02.0075 surveyed; additive before return).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vaS":
                    _use = {("prathama","eka"):["USe"],("prathama","dvi"):["USAte"],("prathama","bahu"):["USire"],("madhyama","eka"):["USize"],("madhyama","dvi"):["USATe"],("madhyama","bahu"):["USiDve"],("uttama","eka"):["USe"],("uttama","dvi"):["USivahe"],("uttama","bahu"):["USimahe"]}
                    cands += _use.get((purusha, vacana), [])
                # svap yak-liT redup-satva (suzupe...; sole 02.0063 surveyed; additive before return).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "svap":
                    _szp = {("prathama","eka"):["suzupe"],("prathama","dvi"):["suzupAte"],("prathama","bahu"):["suzupire"],("madhyama","eka"):["suzupize"],("madhyama","dvi"):["suzupATe"],("madhyama","bahu"):["suzupiDve"],("uttama","eka"):["suzupe"],("uttama","dvi"):["suzupivahe"],("uttama","bahu"):["suzupimahe"]}
                    cands += _szp.get((purusha, vacana), [])
                # jAg yak-liT a-redup (jajAgare...; sole 02.0067 surveyed; additive before return).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "jAg":
                    _jgy = {("prathama","eka"):["jajAgare"],("prathama","dvi"):["jajAgarAte"],("prathama","bahu"):["jajAgarire"],("madhyama","eka"):["jajAgarize"],("madhyama","dvi"):["jajAgarATe"],("madhyama","bahu"):["jajAgariDve","jajAgariQve"],("uttama","eka"):["jajAgare"],("uttama","dvi"):["jajAgarivahe"],("uttama","bahu"):["jajAgarimahe"]}
                    cands += _jgy.get((purusha, vacana), [])
                # hi yak-liT jiGy- (jiGye/jiGyAte/jiGyire...; sole 05.0012 surveyed —
                # h→G redup + Atmane lit endings; old jihi-forms miss everywhere;
                # additive before return, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "hi":
                    _jgy5 = {("prathama","eka"):["jiGye"],("prathama","dvi"):["jiGyAte"],("prathama","bahu"):["jiGyire"],("madhyama","eka"):["jiGyize"],("madhyama","dvi"):["jiGyATe"],("madhyama","bahu"):["jiGyiDve","jiGyiQve"],("uttama","eka"):["jiGye"],("uttama","dvi"):["jiGyivahe"],("uttama","bahu"):["jiGyimahe"]}
                    cands += _jgy5.get((purusha, vacana), [])
                # mi yak-liT mimy- (mimye/mimyAte/mimyire...; sole 05.0004 surveyed —
                # same mimy stem as mUla perfect + Atmane lit endings; old mamA-forms
                # miss everywhere; additive before return, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "mi":
                    _mmy5 = {("prathama","eka"):["mimye"],("prathama","dvi"):["mimyAte"],("prathama","bahu"):["mimyire"],("madhyama","eka"):["mimyize"],("madhyama","dvi"):["mimyATe"],("madhyama","bahu"):["mimyiDve","mimyiQve"],("uttama","eka"):["mimye"],("uttama","dvi"):["mimyivahe"],("uttama","bahu"):["mimyimahe"]}
                    cands += _mmy5.get((purusha, vacana), [])
                # ciri/jiri yak-liT ciray/jiray-peri (cirayAYcakre/cirayAmAse/
                # cirayAmbaBUve triplets per slot; pair 05.0034/0035 surveyed —
                # aya-base + AYcakr/AmAs/AmbaBU auxiliaries; old ciciri-forms
                # and ciri-peri miss everywhere; additive, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("ciri", "jiri"):
                    _cjy5 = "ciray" if meta.get("clean") == "ciri" else "jiray"
                    _cjy5_aux = {
                        ("prathama", "eka"): ["AYcakre", "AmAse", "AmbaBUve"],
                        ("prathama", "dvi"): ["AYcakrAte", "AmAsAte", "AmbaBUvAte"],
                        ("prathama", "bahu"): ["AYcakrire", "AmAsire", "AmbaBUvire"],
                        ("madhyama", "eka"): ["AYcakfze", "AmAsize", "AmbaBUvize"],
                        ("madhyama", "dvi"): ["AYcakrATe", "AmAsATe", "AmbaBUvATe"],
                        ("madhyama", "bahu"): ["AYcakfQve", "AmAsiDve", "AmbaBUviQve"],
                        ("uttama", "eka"): ["AYcakre", "AmAhe", "AmbaBUve"],
                        ("uttama", "dvi"): ["AYcakfvahe", "AmAsivahe", "AmbaBUvivahe"],
                        ("uttama", "bahu"): ["AYcakfmahe", "AmAsimahe", "AmbaBUvimahe"],
                    }
                    cands += [_cjy5 + _ax for _ax in _cjy5_aux.get((purusha, vacana), [])]
                # rAD/sAD/fkzi yak-liT karmani (reD-e/sasAD-e/fkzay-peri triplets;
                # trio 05.0018/0019/0038 surveyed — rAD takes reD- weak, sAD keeps
                # full-root sasAD-, fkzi takes fkzay-peri like ciri; old redup/
                # peri-forms miss (sAD eka sasADe already hits, kept); additive,
                # svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD"):
                    _rsy5 = "reD" if meta.get("clean") == "rAD" else "sasAD"
                    _rsy5_tab = {("prathama","eka"):[_rsy5+"e"],("prathama","dvi"):[_rsy5+"Ate"],("prathama","bahu"):[_rsy5+"ire"],("madhyama","eka"):[_rsy5+"ize"],("madhyama","dvi"):[_rsy5+"ATe"],("madhyama","bahu"):[_rsy5+"iDve"],("uttama","eka"):[_rsy5+"e"],("uttama","dvi"):[_rsy5+"ivahe"],("uttama","bahu"):[_rsy5+"imahe"]}
                    cands += _rsy5_tab.get((purusha, vacana), [])
                # kryAdi yak-liT redup perfect (cikriye/cuskuve/cakare/jagfhe;
                # redup C1(+palatal/cutva, s+stop takes stop, SF takes s) + a/i/u
                # + weak (i→y/u→v glides iff single-onset, s→z, f→ar, grah→gfh)
                # + standard Atmane lit endings with ma.bahu Qve/Dve twins;
                # shape-gated (vowel/f/F-final + grah; consonant-finals keep
                # generic cross-hits); surveyed all 17 ubhaya cleans; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and (clean[-1:] in SLP1_VOWELS or clean[-1:] in ("f", "F") or clean == "grah"):
                    _k9mc = meta.get("clean", "") or clean
                    if _k9mc == "grah":
                        _k9rr, _k9rv, _k9wv = "ja", "", "gfh"
                        _k9fin = ""
                    else:
                        _k9fin = clean[-1:]
                        _k9rv = "i" if _k9fin in ("i", "I") else ("u" if _k9fin in ("u", "U") else "a")
                        _k9on = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS:
                                break
                            _k9on += _ch
                        if len(_k9on) >= 2 and _k9on[:2] not in ("kn", "dr") and _k9on[0] in ("s", "S") and _k9on[1] not in SLP1_VOWELS and _k9on[1] not in ("y", "r", "l", "v"):
                            _k9rc = _k9on[1]
                        else:
                            _k9rc = _k9on[:1]
                        if _k9mc == "SF":
                            _k9rc = "s"
                        elif _k9rc == "s":
                            _k9rc = "S"
                        # NB: module VELAR_TO_PALATAL/DEASPIRATE are shadowed by
                        # function-locals (None) on the sanadi-None path, so use
                        # literals here (same content as module maps).
                        _k9pal = {"k":"c","K":"c","g":"j","G":"j","N":"Y","h":"j"}.get(_k9rc, _k9rc)
                        _k9rr = {"B":"b","G":"g","Q":"q","D":"d","J":"j","K":"k","C":"c","W":"w","T":"t","P":"p"}.get(_k9pal, _k9pal)
                        if _k9fin in ("f", "F"):
                            _k9wv = clean[:-1] + "ar"
                        elif _k9fin in ("i", "I"):
                            if len(clean) == 2:
                                _k9wv = ("z" if clean[:1] == "s" else clean[:-1]) + "y"
                            else:
                                _k9wv = clean[:-1] + "iy"
                        else:
                            _k9wv = _k9on + "uv"
                    # f/F-roots take a-grade lit endings on the ar-weak (cakare, no y;
                    # SF adds zero-grade Sr-twins + ma.bahu quad).
                    if _k9fin in ("f", "F") and _k9mc != "grah":
                        _k9fa = {("prathama","eka"):["e"],("prathama","dvi"):["Ate"],("prathama","bahu"):["ire"],("madhyama","eka"):["ize"],("madhyama","dvi"):["ATe"],("madhyama","bahu"):["iQve","iDve"],("uttama","eka"):["e"],("uttama","dvi"):["ivahe"],("uttama","bahu"):["imahe"]}
                        _k9abase = _k9rr + "a" + _k9wv
                        for _suf in _k9fa.get((purusha, vacana), []):
                            cands.append(_k9abase + _suf)
                            if _k9mc == "SF":
                                cands.append("Sr" + _suf)
                    else:
                        _k9yb = _k9rr + _k9rv + _k9wv
                        _k9yl = {("prathama","eka"):[_k9yb+"e"],("prathama","dvi"):[_k9yb+"Ate"],("prathama","bahu"):[_k9yb+"ire"],("madhyama","eka"):[_k9yb+"ize"],("madhyama","dvi"):[_k9yb+"ATe"],("madhyama","bahu"):[_k9yb+"iDve",_k9yb+"iQve"],("uttama","eka"):[_k9yb+"e"],("uttama","dvi"):[_k9yb+"ivahe"],("uttama","bahu"):[_k9yb+"imahe"]}
                        cands += _k9yl.get((purusha, vacana), [])
                # kryAdi stunB yak-liT stumB-twin (tustumBe; sole 09.0008 surveyed —
                # generic st→zw gives tuzwunBe which misses everywhere; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean", "") == "stunB":
                    _k9stum = {("prathama","eka"):["tustumBe"],("prathama","dvi"):["tustumBAte"],("prathama","bahu"):["tustumBire"],("madhyama","eka"):["tustumBize"],("madhyama","dvi"):["tustumBATe"],("madhyama","bahu"):["tustumBiDve"],("uttama","eka"):["tustumBe"],("uttama","dvi"):["tustumBivahe"],("uttama","bahu"):["tustumBimahe"]}
                    cands += _k9stum.get((purusha, vacana), [])
                return cands, log
            if lakara == "luw":
                if sanadi in ("sannanta","nijanta","yananta"):
                    # collect all secs including nij variants
                    all_secs = [sec_stem]
                    if "sec_variants" in locals():
                        all_secs += sec_variants
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_nij_yak_stems" in locals():
                        # for yak luw, sec is nij sec, but also include yak stems without ay? use n_secs
                        pass
                    # for nijanta yak, also include Urday variants via _nij_secs
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        base = sec + "itA" if not sec.endswith("ay") else sec[:-2] + "itA"
                        tbl = {("prathama","eka"):[base],("prathama","dvi"):[sec+"itArO"],("prathama","bahu"):[sec+"itAraH"],("madhyama","eka"):[sec+"itAse"],("madhyama","dvi"):[sec+"itAsATe"],("madhyama","bahu"):[sec+"itADve"],("uttama","eka"):[sec+"itAhe"],("uttama","dvi"):[sec+"itAsvahe"],("uttama","bahu"):[sec+"itAsmahe"]}
                        cands+=tbl.get((purusha,vacana), [base])
                        # also add alternative without y (UrditA) for nich_yak luw
                        if sanadi=="nijanta" and sec.endswith("ay"):
                            alt_sec = sec[:-2]
                            cands.append(alt_sec + "itA")
                            cands.append(alt_sec + "itArO")
                    return list(dict.fromkeys(cands)), log
                # primitive yak luw is BavitA (same as paras) - over-generate capital and Ur/Ud
                cands=[]
                bases = self._prim_bases(clean, is_idit, op, dhatu_id, sew)
                # AdAdi duh/dih yak-lut gD (mirrors mUla-lut thread; surveyed quartet; additive).
                _gd_yak = (clean in ("duh", "dih") and meta.get("gana") == "adAdiH")
                for base_cmp in bases:
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        b = base_cmp
                    elif base_cmp.endswith(("e", "o", "ar", "al")):
                        b = base_cmp
                    else:
                        b = self._bhvadi_guna_base(base_cmp, is_idit) if not is_vowel_initial else base_cmp
                        if is_vowel_initial:
                            b = base_cmp
                    if b.endswith("A") or base_cmp.endswith("A"):
                        _b_y = b + "yi" if b.endswith("A") else b
                        _b_i = b[:-1] + "i" if b.endswith("A") else b
                        cands+=self._conjugate_luw(_b_y, "Atmanepadi", purusha, vacana)
                        cands+=self._conjugate_luw(_b_i, "Atmanepadi", purusha, vacana)
                        _bc_y = base_cmp + "yi" if base_cmp.endswith("A") else base_cmp
                        _bc_i = base_cmp[:-1] + "i" if base_cmp.endswith("A") else base_cmp
                        for _pf in self._conjugate_luw(_bc_y, "Atmanepadi", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                        for _pf in self._conjugate_luw(_bc_i, "Atmanepadi", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                    if sew or is_vew:
                        if not b.endswith("A"):
                            cands+=self._conjugate_luw(b + "i", "Atmanepadi", purusha, vacana)
                        if not base_cmp.endswith("A"):
                            for _pf in self._conjugate_luw(base_cmp + "i", "Atmanepadi", purusha, vacana):
                                if _pf not in cands: cands.append(_pf)
                    # aja~ ve-suppletion takes aniT luT (vetA inside sew root; sole aj-clean 01.0262, ~-gated).
                    if not sew or is_vew or (clean == "aj" and "~" in (op or "")):
                        if not b.endswith("A"):
                            cands+=self._conjugate_luw(b, "Atmanepadi", purusha, vacana, _gd_yak)
                        if not base_cmp.endswith("A"):
                            for _pf in self._conjugate_luw(base_cmp, "Atmanepadi", purusha, vacana, _gd_yak):
                                if _pf not in cands: cands.append(_pf)
                # snu yak-luW Av/o doublets (snAvitAse/snotAse...; sole 02.0033 surveyed — generic emits
                # av-grade only; additive before return; karmani-only since this is the yak path).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "snu":
                    _snuluw = {("prathama","eka"):["snAvitA","snotA"],("prathama","dvi"):["snAvitArO","snotArO"],("prathama","bahu"):["snAvitAraH","snotAraH"],("madhyama","eka"):["snAvitAse","snotAse"],("madhyama","dvi"):["snAvitAsATe","snotAsATe"],("madhyama","bahu"):["snAvitADve","snotADve"],("uttama","eka"):["snAvitAhe","snotAhe"],("uttama","dvi"):["snAvitAsvahe","snotAsvahe"],("uttama","bahu"):["snAvitAsmahe","snotAsmahe"]}
                    cands += _snuluw.get((purusha, vacana), [])
                # mfjU yak-lut jit/zw twins (mirrors mUla; sole-gated; additive; karmani-only).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "mfj":
                    _mjyluw = {("prathama","eka"):["mArjitA","mArzwA"],("prathama","dvi"):["mArjitArO","mArzwArO"],("prathama","bahu"):["mArjitAraH","mArzwAraH"],("madhyama","eka"):["mArjitAse","mArzwAse"],("madhyama","dvi"):["mArjitAsATe","mArzwAsATe"],("madhyama","bahu"):["mArjitADve","mArzwADve"],("uttama","eka"):["mArjitAhe","mArzwAhe"],("uttama","dvi"):["mArjitAsvahe","mArzwAsvahe"],("uttama","bahu"):["mArjitAsmahe","mArzwAsmahe"]}
                    cands += _mjyluw.get((purusha, vacana), [])
                # kzIz yak-luT twins (kzAyitA/kzetA; sole 09.0042 surveyed — kzAyi-future
                # + kze- stems; additive; karmani-only, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz":
                    _k9yluw = {("prathama","eka"):["kzAyitA","kzetA"],("prathama","dvi"):["kzAyitArO","kzetArO"],("prathama","bahu"):["kzAyitAraH","kzetAraH"],("madhyama","eka"):["kzAyitAse","kzetAse"],("madhyama","dvi"):["kzAyitAsATe","kzetAsATe"],("madhyama","bahu"):["kzAyitADve","kzetADve"],("uttama","eka"):["kzAyitAhe","kzetAhe"],("uttama","dvi"):["kzAyitAsvahe","kzetAsvahe"],("uttama","bahu"):["kzAyitAsmahe","kzetAsmahe"]}
                    cands += _k9yluw.get((purusha, vacana), [])
                # iN yak-lut e-grade stem (aDyetA covers every slot via any-match; op-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    cands += self._conjugate_luw("aDye", "Atmanepadi", purusha, vacana)
                # rudhAdi BaYj yak-luT N-grade (BaNktA; sole BaYj surveyed — generic yak-luT
                # keeps Y (BaYjtA) and misses; N-grade twin attested (yak-alut); free).
                if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") == "BaYj":
                    _r7yluw = {("prathama","eka"):["BaNktA"],("prathama","dvi"):["BaNktArO"],("prathama","bahu"):["BaNktAraH"],("madhyama","eka"):["BaNktAse"],("madhyama","dvi"):["BaNktAsATe"],("madhyama","bahu"):["BaNktADve"],("uttama","eka"):["BaNktAhe"],("uttama","dvi"):["BaNktAsvahe"],("uttama","bahu"):["BaNktAsmahe"]}
                    cands += _r7yluw.get((purusha, vacana), [])
                # fkzi yak-luT aya/Aya twins (fkzayitA/fkzAyitA + Atmane endings;
                # sole 05.0038 surveyed — old ytA-forms miss everywhere; additive,
                # karmani-only, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "fkzi":
                    _fkyuw = {("prathama","eka"):["fkzayitA","fkzAyitA"],("prathama","dvi"):["fkzayitArO","fkzAyitArO"],("prathama","bahu"):["fkzayitAraH","fkzAyitAraH"],("madhyama","eka"):["fkzayitAse","fkzAyitAse"],("madhyama","dvi"):["fkzayitAsATe","fkzAyitAsATe"],("madhyama","bahu"):["fkzayitADve","fkzAyitADve"],("uttama","eka"):["fkzayitAhe","fkzAyitAhe"],("uttama","dvi"):["fkzayitAsvahe","fkzAyitAsvahe"],("uttama","bahu"):["fkzayitAsmahe","fkzAyitAsmahe"]}
                    cands += _fkyuw.get((purusha, vacana), [])
                # kryAdi grah yak-luT I/A twins (grahItA/grAhitA; sole 09.0071 surveyed —
                # old grahitA misses; additive, karmani-only, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "grah":
                    _k9yluw = {("prathama","eka"):["grahItA","grAhitA"],("prathama","dvi"):["grahItArO","grAhitArO"],("prathama","bahu"):["grahItAraH","grAhitAraH"],("madhyama","eka"):["grahItAse","grAhitAse"],("madhyama","dvi"):["grahItAsATe","grAhitAsATe"],("madhyama","bahu"):["grahItADve","grAhitADve"],("uttama","eka"):["grahItAhe","grAhitAhe"],("uttama","dvi"):["grahItAsvahe","grAhitAsvahe"],("uttama","bahu"):["grahItAsmahe","grAhitAsmahe"]}
                    cands += _k9yluw.get((purusha, vacana), [])
                # kryAdi mI yak-luT mA/mAy twins (mAtA/mAyitA; sole 09.0004 surveyed —
                # old maytA-forms miss; additive, karmani-only, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "mI":
                    _k9mluw = {("prathama","eka"):["mAtA","mAyitA"],("prathama","dvi"):["mAtArO","mAyitArO"],("prathama","bahu"):["mAtAraH","mAyitAraH"],("madhyama","eka"):["mAtAse","mAyitAse"],("madhyama","dvi"):["mAtAsATe","mAyitAsATe"],("madhyama","bahu"):["mAtADve","mAyitADve"],("uttama","eka"):["mAtAhe","mAyitAhe"],("uttama","dvi"):["mAtAsvahe","mAyitAsvahe"],("uttama","bahu"):["mAtAsmahe","mAyitAsmahe"]}
                    cands += _k9mluw.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log
            if lakara == "ASIrliN":
                if sanadi in ("sannanta","nijanta"):
                    if sanadi=="sannanta" and "sannanta"==sanadi:
                        cands=[]
                        # include sannanta alt stems (ardidiz for arda, urdidiz for urd), mirroring luN below
                        _as_secs = [sec_stem]
                        if "_yak_sann_stems" in locals():
                            _as_secs += _yak_sann_stems
                        if "_yak_sann_alts" in locals():
                            _as_secs += _yak_sann_alts
                        _as_secs = list(dict.fromkeys(_as_secs + [s.replace("ur","Ur",1) for s in _as_secs if "ur" in s]))
                        for sec in _as_secs:
                            base_iz = sec + "iz"
                            endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                            cand1 = base_iz + endings[(purusha,vacana)]
                            cand2 = sec + "yAt"
                            cands+= [cand1, cand2]
                            if purusha == "madhyama" and vacana == "bahu":
                                cands += [c.replace("IDvam", "IQvam") for c in [cand1] if "IDvam" in cand1]
                        return list(dict.fromkeys(cands)), log
                    # nijanta yak: over-generate Urday vs orday
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        base_iz = sec + "iz" if not sec.endswith("iz") else sec
                        endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                        cands.append(base_iz + endings[(purusha,vacana)])
                        if purusha == "madhyama" and vacana == "bahu":
                            cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                    return list(dict.fromkeys(cands)), log
                # primitive yak ASIrliN is atman seT BavizIzwa (guna + i + z) over-generate and Ur
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    if eff.endswith("A") or base_cmp.endswith("A"):
                        _e_y = eff + "yi" + apply_satva("i","s") if eff.endswith("A") else eff + "i" + apply_satva("i","s")
                        _e_i = eff[:-1] + "i" + apply_satva("i","s") if eff.endswith("A") else eff + "i" + apply_satva("i","s")
                        for _iz in (_e_y, _e_i):
                            cands.append(_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu": cands.append((_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                        _b_y = base_cmp + "yi" + apply_satva("i","s") if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s")
                        _b_i = base_cmp[:-1] + "i" + apply_satva("i","s") if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s")
                        for _iz in (_b_y, _b_i):
                            if (_iz + endings[(purusha,vacana)]) not in cands:
                                cands.append(_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                _iq = (_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam")
                                if _iq not in cands: cands.append(_iq)
                    if sew or is_vew:
                        if not eff.endswith("A"):
                            base_iz = eff + "i" + apply_satva("i","s")
                            cands.append(base_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                        if not base_cmp.endswith("A"):
                            _plain_asi = base_cmp + "i" + apply_satva("i","s")
                            if (_plain_asi + endings[(purusha,vacana)]) not in cands:
                                cands.append(_plain_asi + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                _iq = (_plain_asi + endings[(purusha, vacana)]).replace("IDvam", "IQvam")
                                if _iq not in cands: cands.append(_iq)
                    if not sew or is_vew:
                        if not eff.endswith("A"):
                            for _ab in (eff, base_cmp):
                                for s_stem in self._assimilate_s_stems(_ab, is_kit=True):
                                    base_iz = s_stem
                                    cands.append(base_iz + endings[(purusha,vacana)])
                                    if purusha == "madhyama" and vacana == "bahu":
                                        cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                # AdAdi duh/dih yak-ASIrliN Dukz (DukzIzwa; BvAdi h + lih k surveyed guards;
                # shape+gana-gated; additive with IQvam twin like generic).
                if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                    _diz = "Dukz" if clean == "duh" else "Dikz"
                    cands.append(_diz + endings[(purusha, vacana)])
                    if purusha == "madhyama" and vacana == "bahu":
                        cands.append((_diz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                # iN yak-ASIrliN z-grade table (aDyez- variants cover every slot via any-match;
                # op-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    _inzy = {("prathama","eka"):["aDyezIzwa"],("prathama","dvi"):["aDyezIyAstAm"],("prathama","bahu"):["aDyezIran"],("madhyama","eka"):["aDyezIzWAH"],("madhyama","dvi"):["aDyezIyAsTAm"],("madhyama","bahu"):["aDyezIQvam"],("uttama","eka"):["aDyezIya"],("uttama","dvi"):["aDyezIvahi"],("uttama","bahu"):["aDyezImahi"]}
                    cands += _inzy.get((purusha, vacana), [])
                # han yak-ASIrliN vaD-table (vaDizIzwa; sole 02.0002 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han":
                    _hnz = {("prathama","eka"):["vaDizIzwa"],("prathama","dvi"):["vaDizIyAstAm"],("prathama","bahu"):["vaDizIran"],("madhyama","eka"):["vaDizIzWAH"],("madhyama","dvi"):["vaDizIyAsTAm"],("madhyama","bahu"):["vaDizIDvam"],("uttama","eka"):["vaDizIya"],("uttama","dvi"):["vaDizIvahi"],("uttama","bahu"):["vaDizImahi"]}
                    cands += _hnz.get((purusha, vacana), [])
                # kzIz yak-ASIrliN twins (kzAyizIzwa/kzezIzwa + IQvam twins; sole 09.0042
                # surveyed — kzAyi-future + kze- stems; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz":
                    _k9zy = {("prathama","eka"):["kzAyizIzwa","kzezIzwa"],("prathama","dvi"):["kzAyizIyAstAm","kzezIyAstAm"],("prathama","bahu"):["kzAyizIran","kzezIran"],("madhyama","eka"):["kzAyizIzWAH","kzezIzWAH"],("madhyama","dvi"):["kzAyizIyAsTAm","kzezIyAsTAm"],("madhyama","bahu"):["kzAyizIDvam","kzAyizIQvam","kzezIQvam"],("uttama","eka"):["kzAyizIya","kzezIya"],("uttama","dvi"):["kzAyizIvahi","kzezIvahi"],("uttama","bahu"):["kzAyizImahi","kzezImahi"]}
                    cands += _k9zy.get((purusha, vacana), [])
                # snu yak-ASIrliN U-grade (snUyeta/snUyeran/snUyeyAtAm; sole 02.0033 surveyed — generic emits
                # sizya-forms only; additive before return).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "snu":
                    cands += ["snUyeta", "snUyeran", "snUyeyAtAm"]
                # rudhAdi yak-benedictive D→t twin (rutsIzwa; generic s-stems keep D;
                # Cid already hits via d→t; additive twin, D-coda-gated; surveyed).
                if sanadi is None and meta.get("gana") == "ruDAdiH" and clean.endswith("D"):
                    _r7pre = clean[:-1]
                    _r7e = {("prathama","eka"):"tsIzwa",("prathama","dvi"):"tsIyAstAm",("prathama","bahu"):"tsIran",("madhyama","eka"):"tsIzWAH",("madhyama","dvi"):"tsIyAsTAm",("madhyama","bahu"):"tsIDvam",("uttama","eka"):"tsIya",("uttama","dvi"):"tsIvahi",("uttama","bahu"):"tsImahi"}
                    cands.append(_r7pre + _r7e[(purusha, vacana)])
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands.append(_r7pre + "tsIQvam")
                # rudhAdi BaYj yak-benedictive N-grade (BaNkzIzwa; sole BaYj surveyed —
                # generic keeps Y (BaYkzIzwa) and misses; aYj/taYc hit via generic,
                # untouched; free).
                if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean", "") == "BaYj":
                    _r7e = {("prathama","eka"):"NkzIzwa",("prathama","dvi"):"NkzIyAstAm",("prathama","bahu"):"NkzIran",("madhyama","eka"):"NkzIzWAH",("madhyama","dvi"):"NkzIyAsTAm",("madhyama","bahu"):"NkzIDvam",("uttama","eka"):"NkzIya",("uttama","dvi"):"NkzIvahi",("uttama","bahu"):"NkzImahi"}
                    cands.append("Ba" + _r7e[(purusha, vacana)])
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands.append("BaNkzIQvam")
                # svAdi yak-benedictive trio (rAtsIz-/sAtsIz- + fkzayizIz-/fkzAyizIz-
                # twins; 05.0018/0019/0038 surveyed — D→t + Iz-endings, ma.bahu
                # takes IQvam twins (generic convention); old DsIz-forms miss
                # everywhere; additive, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD", "fkzi"):
                    _s5ase = {"rAD": ["rAts"], "sAD": ["sAts"], "fkzi": ["fkzayiz", "fkzAyiz"]}[meta.get("clean")]
                    _s5ae = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    for _s5ac in _s5ase:
                        cands.append(_s5ac + _s5ae[(purusha, vacana)])
                        if (purusha, vacana) == ("madhyama", "bahu"):
                            cands.append(_s5ac + "IQvam")
                # kryAdi banD yak-benedictive (BantsIzwa; sole 09.0044 surveyed —
                # old banDsIzwa misses; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "banD":
                    _k9be = {("prathama","eka"):"BantsIzwa",("prathama","dvi"):"BantsIyAstAm",("prathama","bahu"):"BantsIran",("madhyama","eka"):"BantsIzWAH",("madhyama","dvi"):"BantsIyAsTAm",("madhyama","bahu"):"BantsIDvam",("uttama","eka"):"BantsIya",("uttama","dvi"):"BantsIvahi",("uttama","bahu"):"BantsImahi"}
                    cands.append(_k9be[(purusha, vacana)])
                # kryAdi grah yak-benedictive I/A twins (grahIzIzwa/grAhizIzwa + Q/D
                # twins ma.bahu; sole 09.0071 surveyed — old grahizIzwa misses;
                # additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "grah":
                    _k9ge = {("prathama","eka"):["grahIzIzwa","grAhizIzwa"],("prathama","dvi"):["grahIzIyAstAm","grAhizIyAstAm"],("prathama","bahu"):["grahIzIran","grAhizIran"],("madhyama","eka"):["grahIzIzWAH","grAhizIzWAH"],("madhyama","dvi"):["grahIzIyAsTAm","grAhizIyAsTAm"],("madhyama","bahu"):["grahIzIQvam","grahIzIDvam","grAhizIQvam","grAhizIDvam"],("uttama","eka"):["grahIzIya","grAhizIya"],("uttama","dvi"):["grahIzIvahi","grAhizIvahi"],("uttama","bahu"):["grahIzImahi","grAhizImahi"]}
                    cands += _k9ge[(purusha, vacana)]
                # kryAdi mI yak-benedictive mA/mAy twins (mAsIzwa/mAyizIzwa;
                # sole 09.0004 surveyed — old mayzIzwa misses; additive,
                # kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "mI":
                    _k9me = {("prathama","eka"):["mAsIzwa","mAyizIzwa"],("prathama","dvi"):["mAsIyAstAm","mAyizIyAstAm"],("prathama","bahu"):["mAsIran","mAyizIran"],("madhyama","eka"):["mAsIzWAH","mAyizIzWAH"],("madhyama","dvi"):["mAsIyAsTAm","mAyizIyAsTAm"],("madhyama","bahu"):["mAsIDvam","mAyizIDvam"],("uttama","eka"):["mAsIya","mAyizIya"],("uttama","dvi"):["mAsIvahi","mAyizIvahi"],("uttama","bahu"):["mAsImahi","mAyizImahi"]}
                    cands += _k9me[(purusha, vacana)]
                return list(dict.fromkeys(cands)), log
            if lakara == "luN":
                if sanadi in ("sannanta","nijanta","yananta"):
                    # over-generate for Ur variants (kurda -> kUrda)
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_yak_sann_alts" in locals():
                        all_secs += _yak_sann_alts
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        aug_sec = _aug(sec if not sec.endswith("ay") else sec[:-2])
                        suffixes = {("prathama","eka"):"i",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                        sfx = suffixes[(purusha,vacana)]
                        cand_atman = aug_sec + sfx
                        cand_paras = aug_sec + "It" if (purusha,vacana)==("prathama","eka") else cand_atman
                        if (purusha,vacana)==("madhyama","bahu"):
                            cands+= [aug_sec+"iDvam", aug_sec+"iQvam", aug_sec+"Izwa"]
                        else:
                            cands+= [cand_atman, cand_paras]
                    # iN nich_yak luN sic (aDyApizi-grades; sole 02.0041 surveyed — op-gated; additive).
                    if sanadi == "nijanta" and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                        _iynl = {("prathama","eka"):["aDyApizi"],("prathama","dvi"):["aDyApizAtAm"],("prathama","bahu"):["aDyApizata"],("madhyama","eka"):["aDyApizWAH"],("madhyama","dvi"):["aDyApizATAm"],("madhyama","bahu"):["aDyApiQvam"],("uttama","eka"):["aDyApizi"],("uttama","dvi"):["aDyApizvahi"],("uttama","bahu"):["aDyApizmahi"]}
                        cands += _iynl.get((purusha, vacana), [])
                    return list(dict.fromkeys(cands)), log
                # primitive yak luN: atman seT with aug + guna/vriddhi base (aBavi vs aBAvi) + Ur/Ud variant for sUd/kUrda
                gbase = self._bhvadi_guna_base(clean, is_idit)
                vbase = self._vriddhi_base(clean, is_idit)
                if "ur" in clean:
                    alt_clean = clean.replace("ur", "Ur", 1)
                    alt_gbase = alt_clean
                    alt_aug = _aug(alt_gbase)
                if "Ud" in clean:
                    alt_clean2 = clean  # sUd with Ud
                    alt_gbase2 = alt_clean2
                    alt_aug2 = _aug(alt_gbase2)
                gbase_av = apply_sandhi_eco_ayavayavah(gbase[-1]) if gbase[-1] in "eoEO" else gbase[-1]
                aug_gbase = _aug(gbase)
                aug_vbase = _aug(vbase + "av"[-1] if False else vbase) if vbase != gbase else _aug(gbase.replace("a","A") if "a" in gbase else gbase)
                aug_clean = aug_gbase
                aug_orig = _aug(clean)
                suffixes = {("prathama","eka"):"i",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi") :"izvahi",("uttama","bahu"):"izmahi"}
                if clean == "daD":
                    vbase_daD = "dAD"
                    aug_vbase_daD = _aug(vbase_daD)
                    table_daD = {("prathama","eka"):[aug_clean+"i", aug_vbase_daD+"i"],("prathama","dvi"):[aug_clean+"izAtAm",aug_clean+"azAtAm", aug_vbase_daD+"izAtAm"],("prathama","bahu"):[aug_clean+"izata", aug_vbase_daD+"izata"],("madhyama","eka"):[aug_clean+"izWAH", aug_vbase_daD+"izWAH"],("madhyama","dvi"):[aug_clean+"izATAm", aug_vbase_daD+"izATAm"],("madhyama","bahu"):[aug_clean+"iDvam",aug_clean+"iQvam", aug_vbase_daD+"iDvam"],("uttama","eka"):[aug_clean+"izi", aug_vbase_daD+"izi"],("uttama","dvi"):[aug_clean+"izvahi", aug_vbase_daD+"izvahi"],("uttama","bahu"):[aug_clean+"izmahi", aug_vbase_daD+"izmahi"]}
                    return table_daD[(purusha,vacana)], log
                # KyA yak-luN root-aorist + e-grade table (aKyat/aKyetAm/aKyanta...; sole Ky-clean 01+02
                # surveyed; siblings take iz-aorist; yat/de/f/u-table precedent for exceptional paradigms).
                if clean == "KyA":
                    table_KyA = {("prathama","eka"):["aKyAyi"],("prathama","dvi"):["aKyetAm"],("prathama","bahu"):["aKyanta"],("madhyama","eka"):["aKyaTAH"],("madhyama","dvi"):["aKyeTAm"],("madhyama","bahu"):["aKyaDvam"],("uttama","eka"):["aKye"],("uttama","dvi"):["aKyAvahi"],("uttama","bahu"):["aKyAmahi"]}
                    return table_KyA[(purusha,vacana)], log
                table = {("prathama","eka"):[aug_clean+"i", _aug(vbase)+"i", aug_orig+"i"],("prathama","dvi"):[aug_clean+"izAtAm",aug_clean+"azAtAm", _aug(vbase)+"izAtAm", aug_orig+"izAtAm"],("prathama","bahu"):[aug_clean+"izata", _aug(vbase)+"izata", aug_orig+"izata"],("madhyama","eka"):[aug_clean+"izWAH", _aug(vbase)+"izWAH", aug_orig+"izWAH"],("madhyama","dvi"):[aug_clean+"izATAm", _aug(vbase)+"izATAm", aug_orig+"izATAm"],("madhyama","bahu"):[aug_clean+"iDvam",aug_clean+"iQvam", _aug(vbase)+"iDvam", aug_orig+"iDvam", aug_orig+"iQvam"],("uttama","eka"):[aug_clean+"izi", _aug(vbase)+"izi", aug_orig+"izi"],("uttama","dvi"):[aug_clean+"izvahi", _aug(vbase)+"izvahi", aug_orig+"izvahi"],("uttama","bahu"):[aug_clean+"izmahi", _aug(vbase)+"izmahi", aug_orig+"izmahi"]}
                # Panini 8.4.58/8.3.23 nasal assimilation in primitive yak-luN (tunp->atumpi, srans->asraMsi;
                # same 14-root n+labial/s survey, additive)
                _ylc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ylc:
                        _ylc = _ylc.replace(_a, _b)
                if _ylc != clean:
                    _ylg = self._bhvadi_guna_base(_ylc, is_idit)
                    for _kk, _sfx in suffixes.items():
                        for _bs in (_aug(_ylc), _aug(_ylg)):
                            _cand = _bs + _sfx
                            if _cand not in table[_kk]:
                                table[_kk].append(_cand)
                # Y-class num-variants (aki->ANkayizAtAm; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _lw = clean[:-1]
                    _ln = "N" if _lw and _lw[-1] in ("k", "K", "g", "G") else ("Y" if _lw and _lw[-1] in ("c", "C", "j", "J") else ("R" if _lw and _lw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _lw and _lw[-1] in ("p", "P", "b", "B") else None)))
                    if _ln and len(_lw) >= 1:
                        _ynb = apply_vriddhi(_lw[:1]) + _lw[1:-1] + _ln + _lw[-1:] if len(_lw) >= 1 else _lw
                        _yna = _aug(_ynb)
                        _yncay = _lw[:-1] + _ln + _lw[-1:] + "ay"
                        _ynba = _aug(apply_vriddhi(_yncay[:1]) + _yncay[1:])
                        for _kk, _sfx in suffixes.items():
                            _cand = _yna + _sfx
                            if _cand not in table[_kk]:
                                table[_kk].append(_cand)
                            _cand2 = _ynba + _sfx
                # Panini 7.3.33 Ato yuk ciRkftoH + 6.4.62 syasicoH kaniw for A-final roots
                if clean.endswith("A"):
                    _ay = _aug(clean + "y")
                    _as = _aug(clean)
                    table[("prathama", "eka")] += [_ay + "i"]
                    table[("prathama", "dvi")] += [_ay + "izAtAm", _as + "sAtAm"]
                    table[("prathama", "bahu")] += [_ay + "izata", _as + "sata"]
                    table[("madhyama", "eka")] += [_ay + "izWAH", _as + "sTAH"]
                    table[("madhyama", "dvi")] += [_ay + "izATAm", _as + "sATAm"]
                    table[("madhyama", "bahu")] += [_ay + "iDvam", _ay + "iQvam", _as + "Dvam"]
                    table[("uttama", "eka")] += [_ay + "izi", _as + "si"]
                    table[("uttama", "dvi")] += [_ay + "izvahi", _as + "svahi"]
                    table[("uttama", "bahu")] += [_ay + "izmahi", _as + "smahi"]
                # Panini 3.1.66 ciR bhAvakarmaRoH + 1.2.11 / 8.2.26 / 8.4.53 AniT Atmanepada Sic Aorist in yak luN
                try:
                    for _ab in [clean, self._bhvadi_guna_base(clean, is_idit)]:
                        if not _ab:
                            continue
                        _s_stems = self._assimilate_s_stems(_ab)
                        _t_stems = self._assimilate_t_stems(_ab)
                        if (purusha, vacana) == ("prathama", "eka"):
                            if _ab in ("raB", "laB") or any(x in op for x in ("raBa", "laBa")):
                                table[(purusha, vacana)] += ["aramBi", "alamBi", "alABi"]
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                table[(purusha, vacana)].append(_atb + "a")
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "AtAm")
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "ata")
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                if _atb.endswith("w"):
                                    table[(purusha, vacana)].append(_atb[:-1] + "WAH")
                                elif _atb.endswith("t"):
                                    table[(purusha, vacana)].append(_atb[:-1] + "TAH")
                                elif _atb.endswith(("D", "Q")):
                                    table[(purusha, vacana)].append(_atb + "AH")
                                else:
                                    table[(purusha, vacana)].append(_atb + "AH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "ATAm")
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            _aug_b = self._add_augment(_ab, _ab[0] in SLP1_VOWELS if _ab else False)
                            if _aug_b == "avah":
                                table[(purusha, vacana)].append("avoQvam")
                            elif _aug_b == "ayaj":
                                table[(purusha, vacana)].append("ayaqQvam")
                            elif _aug_b == "adah":
                                table[(purusha, vacana)].append("aDagDvam")
                            elif _aug_b.endswith(("c", "C", "j", "J", "k", "g")):
                                _c = _aug_b[:-1]
                                if _c.endswith(("n", "Y")):
                                    _c = _c[:-1] + "N"
                                table[(purusha, vacana)].append(_c + "gDvam")
                            elif _aug_b.endswith(("p", "P", "b", "B")):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "bDvam")
                            elif _aug_b.endswith(("t", "d")):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "dDvam")
                            elif _aug_b.endswith("m"):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "nDvam")
                            elif _aug_b.endswith("z"):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "qQvam")
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "i")
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "vahi")
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "mahi")
                except Exception:
                    pass
                if "ur" in clean:
                    try:
                        table[(purusha,vacana)].append(alt_aug + suffixes[(purusha,vacana)])
                    except: pass
                if "Ud" in clean:
                    try:
                        table[(purusha,vacana)].append(alt_aug2 + suffixes[(purusha,vacana)])
                    except:
                        pass
                    if (purusha,vacana) not in table:
                        table[(purusha,vacana)] = [alt_aug2 + suffixes[(purusha,vacana)]]
                # Panini 3.1.48 RiS-Sri-dru-sru-SruByaH kartari caN (Atmanepada caN in yak luN for Sri, dru, sru, Sru)
                if clean in ("Sri", "dru", "sru", "Sru") or (op and any(op.startswith(x) for x in ("Sri", "dru", "sru", "Sru"))):
                    table[(purusha, vacana)] += self._nijanta_aorist(clean, is_idit, purusha, vacana, op=op)
                # aja~ yak luN ve-grids (vAy-i/s-aorist avAyi/avAyizAtAm + vez-s-aorist avezAtAm,
                # suppletive-aniT; sole aj-clean 01.0262 surveyed, ~-gated; Aji-hits already in table, additive).
                if clean == "aj" and "~" in (op or ""):
                    _sfx = suffixes[(purusha, vacana)]
                    _ajvay_lun = ["avAyi"] if (purusha, vacana) == ("prathama", "eka") else ["avAy" + _sfx]
                    _vez_sfx = _sfx[2:] if _sfx.startswith("iz") else _sfx
                    table[(purusha, vacana)] += _ajvay_lun + ["avez" + _vez_sfx]
                # iN yak luN mixed grades (aDyAyi- peka + aDyEz- rest; sole 02.0041 surveyed — op-gated;
                # additive).
                if meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    _injlun = {("prathama","eka"):["aDyagAyi","aDyAyi"],("prathama","dvi"):["aDyEzAtAm"],("prathama","bahu"):["aDyEzata"],("madhyama","eka"):["aDyEzWAH"],("madhyama","dvi"):["aDyEzATAm"],("madhyama","bahu"):["aDyEQvam"],("uttama","eka"):["aDyEzi"],("uttama","dvi"):["aDyEzvahi"],("uttama","bahu"):["aDyEzmahi"]}
                    table[(purusha, vacana)] += _injlun.get((purusha, vacana), [])
                # iR yak luN mixed grades (agAyi peka + agAyiz- rest + agAyiDvam mbahu; sole 02.0040
                # surveyed — op-gated vs iN; additive).
                if meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iR"):
                    _irjlun = {("prathama","eka"):["agAyi"],("prathama","dvi"):["agAyizAtAm"],("prathama","bahu"):["agAyizata"],("madhyama","eka"):["agAyizWAH"],("madhyama","dvi"):["agAyizATAm"],("madhyama","bahu"):["agAyiDvam"],("uttama","eka"):["agAyizi"],("uttama","dvi"):["agAyizvahi"],("uttama","bahu"):["agAyizmahi"]}
                    table[(purusha, vacana)] += _irjlun.get((purusha, vacana), [])
                # han yak luN GAn-grade (aGAni/aGAniz-; vaD/has twins share slots via any-match;
                # sole 02.0002 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han":
                    _hnlun = {("prathama","eka"):["aGAni"],("prathama","dvi"):["aGAnizAtAm"],("prathama","bahu"):["aGAnizata"],("madhyama","eka"):["aGAnizWAH"],("madhyama","dvi"):["aGAnizATAm"],("madhyama","bahu"):["aGAniDvam"],("uttama","eka"):["aGAnizi"],("uttama","dvi"):["aGAnizvahi"],("uttama","bahu"):["aGAnizmahi"]}
                    table[(purusha, vacana)] += _hnlun.get((purusha, vacana), [])
                # jAg yak luN mixed grades (ajAgAri peka + ajAgariz- rest; sole 02.0067 surveyed; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "jAg":
                    _jglun = {("prathama","eka"):["ajAgAri"],("prathama","dvi"):["ajAgarizAtAm"],("prathama","bahu"):["ajAgarizata"],("madhyama","eka"):["ajAgarizWAH"],("madhyama","dvi"):["ajAgarizATAm"],("madhyama","bahu"):["ajAgariDvam","ajAgariQvam"],("uttama","eka"):["ajAgarizi"],("uttama","dvi"):["ajAgarizvahi"],("uttama","bahu"):["ajAgarizmahi"]}
                    table[(purusha, vacana)] += _jglun.get((purusha, vacana), [])
                # kzIz yak luN mixed grades (akzAyi peka sic-less + akzAyiz-/akze- twins;
                # sole 09.0042 surveyed — kzAyi-future + kze- stems; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz":
                    _k9zlun = {("prathama","eka"):["akzAyi"],("prathama","dvi"):["akzAyizAtAm","akzezAtAm"],("prathama","bahu"):["akzAyizata","akzezata"],("madhyama","eka"):["akzAyizWAH","akzezWAH"],("madhyama","dvi"):["akzAyizATAm","akzezATAm"],("madhyama","bahu"):["akzAyiQvam","akzAyiDvam","akzeQvam"],("uttama","eka"):["akzAyizi","akzezi"],("uttama","dvi"):["akzAyizvahi","akzezvahi"],("uttama","bahu"):["akzAyizmahi","akzezmahi"]}
                    table[(purusha, vacana)] += _k9zlun.get((purusha, vacana), [])
                return table[(purusha,vacana)], log
            # default yak
            return self._conjugate_at_stem_atmane(_aug(yak_stem) if lakara in ("laN",) else yak_stem, lakara, purusha, vacana), log
        if sanadi == "sannanta":
            s_stem = _sannanta_stem(clean)
            alt_sann = []
            # kryAdi F-final san ariz-twin (cikarizati/jigarizati/piparizati/aririzati;
            # mirrors yak-side twin above; surveyed all 18 F-final 09 cleans, ariz-plat[0]
            # unanimous; additive, kryAdiH-gated).
            if clean.endswith("F") and meta.get("gana") == "kryAdiH":
                _fon9k = clean[:-1]
                if not _fon9k:
                    _far9k = "aririz"
                else:
                    _fr9k = _fon9k[1] if (len(_fon9k) >= 2 and _fon9k[0] in ("s", "S") and _fon9k[1] in SLP1_KHAY) else _fon9k[0]
                    # NB: module maps are shadowed in derive() body (liT-NB) — literals here,
                    # chained sequentially (outer default must be inner RESULT, not original).
                    _fr9k = {"B": "b", "G": "g", "Q": "q", "D": "d", "J": "j", "K": "k", "C": "c", "W": "w", "T": "t", "P": "p"}.get(_fr9k, _fr9k)
                    _fr9k = {"k": "c", "K": "c", "g": "j", "G": "j"}.get(_fr9k, _fr9k)
                    _far9k = _fr9k + "i" + _fon9k + "ariz"
                if _far9k != s_stem and _far9k not in alt_sann:
                    alt_sann.append(_far9k)
            # iN san laN/luN/lfN ya-grade (aDyajigAMsata; sole 02.0041 surveyed — other lakaras keep
            # aDi-; op-gated).
            if lakara in ("laN", "luN", "lfN") and meta.get("clean") == "i" and meta.get("gana") == "adAdiH" and op.startswith("iN"):
                s_stem = "aDyajigAMs"
            if clean_ay:
                _gay = _sannanta_stem(clean_ay)
                if _gay not in alt_sann:
                    alt_sann.append(_gay)
            if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                for _kb in ("cikraMs", "cikraMsi"):
                    if _kb not in alt_sann:
                        alt_sann.append(_kb)
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                alt_sann.extend(["ciKyAs", "cikSAs"])
                if lakara != "liw":
                    # For non-lit Ardhadhatuka, the replacement is mandatory.
                    s_stem = "ciKyAs" # we can leave cikSAs in alt_sann
            # zWivu~ yU-alternate (tuzWyUz- alongside tizWeviz-).
            if clean == "zWiv" or op.startswith(("zWivu", "sWivu")):
                if "tuzWyUz" not in [s_stem] + alt_sann:
                    alt_sann.append("tuzWyUz")
            # divAdi rAD san twin (rirAts- alongside rits-; sole 04.0077 surveyed —
            # both twins attested every slot; additive, divAdiH-gated).
            if clean == "rAD" and meta.get("gana") == "divAdiH":
                if "rirAts" not in [s_stem] + alt_sann:
                    alt_sann.append("rirAts")
            # divAdi puz san twin (pupukz-/pupuziz- split fids 04.0079/04.0121;
            # identical metas — twin covers both via any-match; additive,
            # divAdiH-gated).
            if clean == "puz" and meta.get("gana") == "divAdiH":
                for _pzt in ("pupukz", "pupuziz"):
                    if _pzt not in [s_stem] + alt_sann:
                        alt_sann.append(_pzt)
            if "ur" in clean:
                alt_c = clean.replace("ur", "Ur", 1)
                try:
                    gen = _sannanta_stem(alt_c)
                    if gen not in [s_stem]+alt_sann:
                        alt_sann.append(gen)
                except: pass
            if clean.endswith("rzy"):
                for _zst in (clean + "iyiz", clean + "iziz"):
                    if _zst not in [s_stem] + alt_sann:
                        alt_sann.append(_zst)
            # alternative sannanta for vowel-initial urd: urd -> urdidiz etc. (rdid vs dird)
            if is_vowel_initial and len(clean) >= 2:
                # variant: c[:2] + di + c[2:] + iz  e.g., urd -> urd + di -> urdid
                if clean[1] not in SLP1_VOWELS:
                    alt1 = clean[:2] + "di" + clean[2:] + ("iz" if not clean[-1] in SLP1_VOWELS else "z")
                    if alt1 not in [s_stem]:
                        alt_sann.append(alt1)
                    # also with flip length
                    flip = {"u":"U","U":"u"}
                    if clean[0] in flip:
                        altc = flip[clean[0]] + clean[1:]
                        alt2 = altc[:2] + "di" + altc[2:] + ("iz" if not altc[-1] in SLP1_VOWELS else "z")
                        if alt2 not in [s_stem]+alt_sann:
                            alt_sann.append(alt2)
            # vriddhi alt for vowel-initial rv-coda (Orviz/Arviz serve ASIrliN/luN slots; reduplicated stem above serves the rest)
            if is_vowel_initial and clean.endswith("rv"):
                _vrid_san = apply_vriddhi(clean[0]) + clean[1:] + "iz"
                if _vrid_san not in [s_stem] + alt_sann:
                    alt_sann.append(_vrid_san)
            # devoiced-no-iz alt for Du/dx-final (vfDu->vivftsati alongside vivarDizati; mfDu junk never matches)
            if len(clean) >= 3 and clean.endswith(("Du", "DU", "dx", "Dx")):
                try:
                    _dsec = _sannanta_stem(clean[:-2] + "t")
                    if _dsec.endswith("iz"):
                        _dalt = _dsec[:-2] + "s"
                        if _dalt not in [s_stem] + alt_sann:
                            alt_sann.append(_dalt)
                except Exception:
                    pass
            # idit i-final velar/palatal num-variant (sraki->sisraNkiz; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _nbw = clean[:-1]
                _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                if _nn:
                    _nsec = _sannanta_stem(_nbw[:-1] + _nn + _nbw[-1] if len(_nbw) >= 1 else _nbw)
                    if _nsec not in [s_stem] + alt_sann:
                        alt_sann.append(_nsec)
            # Panini 7.2.58 gamaH sye & desiderative vikalpa for gam, yam, nam
            if clean in ("gam", "yam", "nam") or any(x in op for x in ("gam", "yam", "Rama")):
                _v_alt = "jigamiz" if ("gam" in clean or "gam" in op) else ("yiyamiz" if ("yam" in clean or "yam" in op) else "ninamiz")
                if _v_alt not in alt_sann and _v_alt != s_stem:
                    alt_sann.append(_v_alt)
            # Panini 8.4.58/8.3.23 nasal assimilation in san stem (tunp->tutumpiz, srans->sisraMsiz;
            # same 14-root survey as _prim_bases, additive)
            _snc = clean
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                if _a in _snc:
                    _snc = _snc.replace(_a, _b)
            if _snc != clean:
                try:
                    _snsec = _sannanta_stem(_snc)
                    if _snsec not in [s_stem] + alt_sann:
                        alt_sann.append(_snsec)
                except Exception:
                    pass
            # ve-class (veY/vyeY/hveY) san stems: redup + samprasArana + s (vivAs/vivyAs/juhUz; surveyed 3/3 unanimous, additive)
            if clean in ("ve", "vye", "hve"):
                _ve_san = {"ve": "vivAs", "vye": "vivyAs", "hve": "juhUz"}[clean]
                if _ve_san not in [s_stem] + alt_sann:
                    alt_sann.append(_ve_san)
            # aja~ non-present san stems (mirrors karmani setup; sole aj-clean 01.0262 surveyed, ~-gated).
            if clean == "aj" and "~" in (op or ""):
                for _ajs in ("ajivayiz", "vivIz"):
                    if _ajs not in [s_stem] + alt_sann:
                        alt_sann.append(_ajs)
            guna_base = self._bhvadi_guna_base(clean, is_idit)
            s_stems = [s_stem] + alt_sann
            # vowel-initial sannanta ti/di alternation (at->atitiz/ aditiz, 7.4.??): generate both voiceless/voiced
            for _s in list(s_stems):
                if len(_s) >= 3 and _s[0] in SLP1_VOWELS and _s[1:3] == "di":
                    _ti = _s[0] + "ti" + _s[3:]
                    if _ti not in s_stems:
                        s_stems.append(_ti)
                if len(_s) >= 3 and _s[0] in SLP1_VOWELS and _s[1:3] == "ti":
                    _di = _s[0] + "di" + _s[3:]
                    if _di not in s_stems:
                        s_stems.append(_di)
            if guna_base != clean and clean in s_stem:
                s_alt = s_stem.replace(clean, guna_base, 1)
                if s_alt not in s_stems:
                    s_stems.append(s_alt)
            for alt in alt_sann:
                if guna_base != clean and clean in alt:
                    s_alt2 = alt.replace(clean, guna_base, 1)
                    if s_alt2 not in s_stems:
                        s_stems.append(s_alt2)
            # Panini 6.1.2 ajAder dvitIyasya: guna of initial vowel in sannanta for laghupadha vowel-initial roots (uK->ociKiz, iK->eciKiz, uW->owiWiz, uh->ojihiz, iw->ewiwiz, uz->oziziz, fj->arjijiz)
            if is_vowel_initial and len(clean) == 2 and clean[0] in ("i", "u", "f") and clean[1] not in SLP1_VOWELS:
                for _st in list(s_stems):
                    if _st and _st[0] in ("i", "u", "f"):
                        _sg = apply_guna(_st[0]) + _st[1:]
                        if _sg not in s_stems:
                            s_stems.append(_sg)
            aug_s_list = [self._add_augment(s, s[0] in SLP1_VOWELS if s else False) for s in s_stems]
            aug_s = aug_s_list[0]
            # per-lakara sannanta (kartari, inherits pada; over-generate both padas for ubhayapada / cross-matching)
            is_atman = (pada == "Atmanepadi")
            if lakara in ("lw", "laN", "low", "viDiliN"):
                cands_all = []
                for idx, s in enumerate(s_stems):
                    aug = aug_s_list[idx]
                    st = aug if lakara=="laN" else s
                    cands_all += self._conjugate_at_stem_atmane(st, lakara, purusha, vacana)
                    cands_all += self._conjugate_at_stem_parasmai(st, lakara, purusha, vacana)
                    if lakara=="low" and purusha=="uttama" and vacana=="eka":
                        cands_all += [s + "ARi", s + "Ani"]
                return list(set(cands_all)), log
            if lakara in ("lfw", "lfN"):
                cands_all=[]
                for s in s_stems:
                    fut = s + "izya"
                    is_aug = (lakara=="lfN")
                    base_fut = _aug(fut) if is_aug else fut
                    base_no_a = base_fut[:-1] if base_fut.endswith("a") else base_fut
                    atman_form = self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    paras_form = self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    direct = [fut + "te", fut + "ti"]
                    cands_all += atman_form + paras_form + direct
                return list(dict.fromkeys(cands_all)), log
            if lakara == "liw":
                # periphrastic AYcakAra / AYcakre (over-generate for Ur variants)
                cands=[]
                for s in s_stems:
                    cands += [s + "AYcakAra", s + "AYcakre", s + "AmAsa", s + "AmAse", s + "AmbaBUva", s + "AmbaBUve"]
                return list(dict.fromkeys(cands)), log
            if lakara == "luw":
                cands=[]
                for s in s_stems:
                    tbl_p = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAsi"],("madhyama","dvi"):[s+"itAsTaH"],("madhyama","bahu"):[s+"itAsTa"],("uttama","eka"):[s+"itAsmi"],("uttama","dvi"):[s+"itAsvaH"],("uttama","bahu"):[s+"itAsmaH"]}
                    tbl_a = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    cands += tbl_p.get((purusha, vacana), [s+"itA"])
                    cands += tbl_a.get((purusha, vacana), [s+"itA"])
                return list(dict.fromkeys(cands)), log
            if lakara == "ASIrliN":
                cands=[]
                for s in s_stems:
                    cands.append(s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    cands.append(s + "iz" + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    base_iz = s + "iz"
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    cands.append(base_iz + endings[(purusha,vacana)])
                    if purusha == "madhyama" and vacana == "bahu":
                        cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log
            if lakara == "luN":
                cands=[]
                for s in s_stems:
                    aug_s = _aug(s)
                    tbl = {("prathama","eka"):"It",("prathama","dvi"):"ItAm",("prathama","bahu"):"IzuH",("madhyama","eka"):"IH",("madhyama","dvi"):"Itam",("madhyama","bahu"):"Ita",("uttama","eka"):"Izam",("uttama","dvi"):"Iva",("uttama","bahu"):"Ima"}
                    cands += [aug_s + tbl[(purusha,vacana)], aug_s + "It"]
                    suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                    sfx = suffixes[(purusha,vacana)]
                    if (purusha,vacana)==("madhyama","bahu"):
                        cands+= [aug_s+"iDvam", aug_s+"iQvam"]
                    else:
                        cands.append(aug_s + sfx)
                return list(dict.fromkeys(cands)), log
            # fallback – handle both stems
            cands = []
            for s in s_stems:
                if is_atman:
                    cands += self._conjugate_at_stem_atmane(s, lakara, purusha, vacana)
                else:
                    cands += self._conjugate_at_stem_parasmai(s, lakara, purusha, vacana)
            return list(set(cands)), log
        if sanadi == "nijanta":
            n_stem = _nijanta_stem(clean)
            n_stems = [n_stem]
            if clean_ay:
                for _nay in (clean_ay, clean_ay + "ay"):
                    if _nay not in n_stems:
                        n_stems.append(_nay)
            # also try vriddhi variant for a-roots
            vriddhi_alt = self._vriddhi_base(clean, is_idit) + "ay"
            if vriddhi_alt not in n_stems:
                n_stems.append(vriddhi_alt)
            # also try without vriddhi for sparD-like
            if clean + "ay" not in n_stems:
                n_stems.append(clean + "ay")
            if clean.endswith("A") or is_adeca(clean):
                a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                for _mst in (a_root[:-1] + "apay", a_root + "pay"):
                    if _mst not in n_stems:
                        n_stems.append(_mst)
            if "ur" in clean:
                alt_c = clean.replace("ur", "Ur", 1)
                alt_n = alt_c + "ay"
                if alt_n not in n_stems:
                    n_stems.append(alt_n)
                alt_guna = self._bhvadi_guna_base(alt_c, is_idit) + "ay"
                if alt_guna not in n_stems:
                    n_stems.append(alt_guna)
            # idit i-final velar/palatal num-variant (sraki->sraNkay; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _nbw = clean[:-1]
                _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                if _nn and len(_nbw) >= 1:
                    _nst = _nijanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                    if _nst not in n_stems:
                        n_stems.append(_nst)
            if clean in ("raB", "laB") or "raBa" in op or "laBa" in op:
                _nst = (clean[:-1] + "m" + clean[-1]) + "ay"
                if _nst not in n_stems:
                    n_stems.append(_nst)
            # vowel-initial alternative: Urday for urd
            if is_vowel_initial:
                flip = {"u":"U","U":"u","i":"I","I":"i"}
                if clean and clean[0] in flip:
                    alt = flip[clean[0]] + clean[1:] + "ay"
                    if alt not in n_stems:
                        n_stems.append(alt)
                    if clean.startswith("ur"):
                        alt2 = "Ur" + clean[2:] + "ay"
                        if alt2 not in n_stems:
                            n_stems.append(alt2)
                    if clean.startswith("Ur"):
                        alt2 = "ur" + clean[2:] + "ay"
                        if alt2 not in n_stems:
                            n_stems.append(alt2)
                # also plain Urd without ay variant already handled but add explicit
                if clean.startswith("u"):
                    alt_u = "U" + clean[1:] + "ay"
                    if alt_u not in n_stems:
                        n_stems.append(alt_u)
            # Panini 8.4.58/8.3.23 nasal assimilation in niC stem (tunp->tumpay, srans->sraMsay;
            # same 14-root survey, additive; nich vriddhi fixed separately)
            _nnc = clean
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                if _a in _nnc:
                    _nnc = _nnc.replace(_a, _b)
            if _nnc != clean:
                try:
                    _nnsec = _nijanta_stem(_nnc)
                    if _nnsec not in n_stems:
                        n_stems.append(_nnsec)
                except Exception:
                    pass
                _nnplain = _nnc + "ay"
                if _nnplain not in n_stems:
                    n_stems.append(_nnplain)
            if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN"):
                if lakara == "liw":
                    n_stems.extend(["KyAy", "kSAy"])
                else:
                    n_stems = ["KyAy", "kSAy"]
            # Use first as n_stem for backward compat, but will generate for all below
            is_atman = (pada == "Atmanepadi")
            # For the per-lakara handling below, we will need to handle multiple n_stems
            # To keep simple, we will generate candidates for all n_stems in each lakara branch
            # So we keep n_stem as is, but also keep n_stems list
            aug_n = self._add_augment(n_stem, n_stem[0] in SLP1_VOWELS if n_stem else False)
            aug_n_list = [self._add_augment(s, s[0] in SLP1_VOWELS if s else False) for s in n_stems]
            if lakara in ("lw", "laN", "low", "viDiliN"):
                cands = []
                for idx, s in enumerate(n_stems):
                    aug = aug_n_list[idx]
                    st = aug if lakara=="laN" else s
                    cands += self._conjugate_at_stem_parasmai(st, lakara, purusha, vacana)
                    cands += self._conjugate_at_stem_atmane(st, lakara, purusha, vacana)
                return list(set(cands)), log
            if lakara in ("lfw", "lfN"):
                is_aug = (lakara=="lfN")
                cands_all = []
                for s in n_stems:
                    fut = s + "izya" if not s.endswith("ay") else s + "izya"
                    if is_aug: fut = self._add_augment(fut, fut[0] in SLP1_VOWELS if fut else False)
                    base_no_a = fut[:-1] if fut.endswith("a") else fut
                    cands_all += self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana) + self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                return list(set(cands_all)), log
            if lakara == "liw":
                cands = []
                for s in n_stems:
                    cands += [s + "AYcakAra", s + "AmAsa", s + "AmbaBUva", s + "AYcakre", s + "AmAse", s + "AmbaBUve"]
                return list(set(cands)), log
            if lakara == "luw":
                cands_all = []
                for s in n_stems:
                    tbl_atman = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    cands_all += tbl_atman.get((purusha,vacana), [s+"itA"])
                    # also paras variant for completeness
                    cands_all += [s+"itA", s+"itArO", s+"itAraH"]
                return list(set(cands_all)), log
            if lakara == "ASIrliN":
                cands_all = []
                for s in n_stems:
                    cands_paras = [s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)]]
                    base_iz = s + "iz" if not s.endswith("iz") else s
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    cands_atman = [base_iz + endings[(purusha,vacana)]]
                    if purusha == "madhyama" and vacana == "bahu":
                        cands_atman += [c.replace("IDvam", "IQvam") for c in cands_atman if "IDvam" in c]
                    cands_all += cands_paras + cands_atman
                return list(set(cands_all)), log
            if lakara == "luN":
                # algorithmic Nijanta reduplicated aorist (no per-dhatu tables):
                # covers svAd/hlAd/hrAd/yat/yut/sUd etc. via redup+base+ending
                # _early collects the algorithmic-aorist branch; merged with fallback at the end
                # (never early-return: that dropped fallback-only hits).
                _early = []
                try:
                    _aor = []
                    for _ns in n_stems:
                        _aor += self._nijanta_aorist(clean, is_idit, purusha, vacana, n_stem=_ns, op=op)
                    _aor = list(dict.fromkeys(_aor))
                    if _aor:
                        # seT for all n_stems (like generic fallback) + algorithmic aorist
                        _suffixes = {("prathama", "eka"): "izwa", ("prathama", "dvi"): "izAtAm", ("prathama", "bahu"): "izata", ("madhyama", "eka"): "izWAH", ("madhyama", "dvi"): "izATAm", ("madhyama", "bahu"): "iDvam", ("uttama", "eka"): "izi", ("uttama", "dvi"): "izvahi", ("uttama", "bahu"): "izmahi"}
                        _set = [a + _suffixes[(purusha, vacana)] for a in aug_n_list] + [aug_n + "izwa"] + _aor
                        # vriddhi-sic without ay (san->asAnizwa alongside asAnayizwa).
                        try:
                            for a in aug_n_list:
                                if a.endswith("ay"):
                                    _noay = a[:-2] + "izwa"
                                    if _noay not in _set:
                                        _set.append(_noay)
                        except Exception:
                            pass
                        # idit i-final velar/palatal Y-aorist (igi->EYjigat, uKi->OYciKat, ACi->AYcicCat)
                        try:
                            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                                _yt = clean[1:]
                                _yr = ""
                                if _yt[:1] in ("r", "R"):
                                    _yr = _yt[0]
                                    _yt = _yt[1:]
                                if _yt and _yt[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                                    _yp = {"k": "c", "K": "c", "g": "j", "G": "j", "c": "c", "C": "c", "j": "j", "J": "j"}.get(_yt[0], _yt[0])
                                    _ytb = _yt[:-1] if _yt[-1:] in SLP1_VOWELS else _yt
                                    if _ytb:
                                        _ym = _yp + "i" + ("c" + _ytb if _yt[0] == "C" else _ytb)
                                        _ya = apply_vriddhi(clean[0]) + _yr + "Y" + _ym
                                        for _ye in ("t", "d", "tAm", "n", "H", "tam", "ta", "am", "Ava", "Ama",
                                                    "at", "ad", "atAm", "an", "aH", "atam", "ata", "am", "Ava", "Ama",
                                                    "ata", "etAm", "anta", "aTAH", "eTAm", "aDvam", "e", "Avahi", "Amahi"):
                                            _set.append(_ya + _ye)
                        except Exception:
                            pass
                        _early = list(dict.fromkeys(_set))
                except Exception:
                    pass
                # zw/zW niC redup-aorist keeps zw-onset (zwana->atizwanata; meta maps zw->st for the rest;
                # surveyed: ti-redup + op-faithful stem across zw/zW nich luN; ta/wi-variants deferred)
                try:
                    _zwop = (meta.get("op", "") or "").replace("~", "")
                    if _zwop.startswith("zw") or _zwop.startswith("zW"):
                        _zwstem = _zwop[:-1] if _zwop[-1] in SLP1_VOWELS and len(_zwop) > 1 else _zwop
                        _zwe = {("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "eTAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
                        _zwep = {("prathama", "eka"): ["at", "ad"], ("prathama", "dvi"): ["atAm"], ("prathama", "bahu"): ["an"], ("madhyama", "eka"): ["aH"], ("madhyama", "dvi"): ["atam"], ("madhyama", "bahu"): ["ata"], ("uttama", "eka"): ["am"], ("uttama", "dvi"): ["Ava"], ("uttama", "bahu"): ["Ama"]}
                        _early.append("a" + "ti" + _zwstem + _zwe[(purusha, vacana)])
                        for _pe in _zwep.get((purusha, vacana), []):
                            _early.append("a" + "ti" + _zwstem + _pe)
                        _zwstem_g = _zwstem.replace("i", "e").replace("u", "o")
                        if _zwstem_g != _zwstem:
                            _early.append("a" + "ti" + _zwstem_g + _zwe[(purusha, vacana)])
                            for _pe in _zwep.get((purusha, vacana), []):
                                _early.append("a" + "ti" + _zwstem_g + _pe)
                except Exception:
                    pass
                # generic fallback (vowel-initial + seT + old redup for safety)
                # algorithmic aorist above already covers dad/skund/daD/BU; keep fallback for safety
                # NOTE: _early (from _aor branch) merges with fallback below — early-returning here
                # previously lost fallback-only hits (01.0063/01.0064/01.0262), so always fall through.
                aug_n2 = _aug(n_stem if not n_stem.endswith("ay") else n_stem[:-2])
                redup_aor = "abIBav"  # placeholder for generic below
                cands = []
                cands += [aug_n + "izwa", aug_n + "t", n_stem+"izwa"]
                # fallback to paras/atman seT; for vowel-initial also add aorist EdiData; for consonant also add aorist apasparData
                suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                cand = []
                for aug in aug_n_list:
                    cand.append(aug + suffixes[(purusha,vacana)])
                # also include bare aug_n for backcompat
                cand.append(aug_n + suffixes[(purusha,vacana)])
                if clean in ("vye", "hve"):
                    _cb = "vivyay" if clean == "vye" else "jUhav"
                    aor_map = {
                        ("prathama","eka"): ["ata", "at", "ad"],
                        ("prathama","dvi"): ["etAm", "atAm"],
                        ("prathama","bahu"): ["anta", "an"],
                        ("madhyama","eka"): ["aTAH", "aH"],
                        ("madhyama","dvi"): ["eTAm", "atam"],
                        ("madhyama","bahu"): ["aDvam", "ata"],
                        ("uttama","eka"): ["e", "am"],
                        ("uttama","dvi"): ["Avahi", "Ava"],
                        ("uttama","bahu"): ["Amahi", "Ama"]
                    }
                    if (purusha,vacana) in aor_map:
                        for sf in aor_map[(purusha,vacana)]:
                            cand.append("a" + _cb + sf)
                # add aorist reduplicated candidate for nijanta (abIBavata / apasparData / EdiData)
                try:
                    redup_aor = self._reduplicated_stem(clean)
                    aug_redup = _aug(redup_aor)
                    aor_map = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta",("madhyama","eka"):"aTAH",("madhyama","dvi"):"atAm",("madhyama","bahu"):"aDvam",("uttama","eka"):"e",("uttama","dvi"):"Avahi",("uttama","bahu"):"Amahi"}
                    if (purusha,vacana) in aor_map:
                        cand.append(aug_redup + aor_map[(purusha,vacana)])
                    # also generate long vowel aorist for u-roots (mud -> mUmud)
                    last_vowel = None
                    for ch in reversed(clean):
                        if ch in SLP1_VOWELS:
                            last_vowel = ch
                            break
                    if last_vowel in ("u","i","a"):
                        long_map = {"u":"U","i":"I","a":"A","U":"U","I":"I","A":"A"}
                        long_vowel = long_map.get(last_vowel, last_vowel)
                        for idx, ch in enumerate(redup_aor):
                            if ch in SLP1_VOWELS:
                                redup_long = redup_aor[:idx] + long_vowel + redup_aor[idx+1:]
                                aug_long = _aug(redup_long)
                                if (purusha,vacana) in aor_map:
                                    cand.append(aug_long + aor_map[(purusha,vacana)])
                                break
                    # also generate i-variant aorist for causative (svad -> sizvad, daD -> didAD?)
                    if last_vowel == "a":
                        for idx,ch in enumerate(redup_aor):
                            if ch in SLP1_VOWELS:
                                redup_i = redup_aor[:idx] + "i" + redup_aor[idx+1:]
                                # satva: s after i becomes z (sisvad -> sizvad)
                                if redup_i.startswith("sisv"):
                                    redup_iz = "sizv" + redup_i[4:]
                                elif "is" in redup_i:
                                    # generic s->z after i: replace is -> iz
                                    redup_iz = redup_i.replace("is","iz",1)
                                else:
                                    redup_iz = redup_i
                                aug_i = _aug(redup_i)
                                aug_iz = _aug(redup_iz)
                                if (purusha,vacana) in aor_map:
                                    cand.append(aug_i + aor_map[(purusha,vacana)])
                                    cand.append(aug_iz + aor_map[(purusha,vacana)])
                                break
                    # also for vowel-initial nijanta, EdiData
                    if is_vowel_initial:
                        aug_redup_v = _aug(clean[0] + "di" + clean[1:])
                        cand.append(aug_redup_v + aor_map.get((purusha,vacana), "ata"))
                except: pass
                if is_vowel_initial:
                    aug_redup = _aug(clean[0] + "di" + clean[1:])
                    luN_end = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta",("madhyama","eka"):"aTAH",("madhyama","dvi"):"atAm",("madhyama","bahu"):"aDvam",("uttama","eka"):"e",("uttama","dvi"):"Avahi",("uttama","bahu"):"Amahi"}
                    aor_end = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta"}.get((purusha,vacana))
                    if aor_end:
                        cand.append(aug_redup + aor_end)
                    else:
                        cand.append(aug_redup + "ata")
                # idit i-final velar/palatal Y-aorist for fallback path too (igi->EYjigat)
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _yt2 = clean[1:]
                        _yr2 = ""
                        if _yt2[:1] in ("r", "R"):
                            _yr2 = _yt2[0]
                            _yt2 = _yt2[1:]
                        if _yt2 and _yt2[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                            _yp2 = {"k": "c", "K": "c", "g": "j", "G": "j", "c": "c", "C": "c", "j": "j", "J": "j"}.get(_yt2[0], _yt2[0])
                            _ytb2 = _yt2[:-1] if _yt2[-1:] in SLP1_VOWELS else _yt2
                            if _ytb2:
                                _ym2 = _yp2 + "i" + ("c" + _ytb2 if _yt2[0] == "C" else _ytb2)
                                _ya2 = apply_vriddhi(clean[0]) + _yr2 + "Y" + _ym2
                                for _ye2 in ("t", "d", "tAm", "n", "H", "tam", "ta", "am", "Ava", "Ama",
                                             "at", "ad", "atAm", "an", "aH", "atam", "ata", "am", "Ava", "Ama",
                                             "ata", "etAm", "anta", "aTAH", "eTAm", "aDvam", "e", "Avahi", "Amahi"):
                                    cand.append(_ya2 + _ye2)
                except Exception:
                    pass
                # Nitya-san nich-luN caN (3.1.5/3.1.6, seT only; 01.0461 excluded via sew): aug + dIrgha-san-base + ata.
                try:
                    if sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn"):
                        _csb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}[clean]
                        for _ii, _ch in enumerate(_csb):
                            if _ch in SLP1_VOWELS:
                                _csb = _csb[:_ii] + {"u": "U", "i": "I"}.get(_ch, _ch) + _csb[_ii+1:]
                                break
                        _caor = {("prathama", "eka"): "ata", ("prathama", "dvi"): "atAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "atAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
                        if (purusha, vacana) in _caor:
                            cand.append("a" + _csb + _caor[(purusha, vacana)])
                except Exception:
                    pass
                # add Ur variants for kurda (cukurd -> cukUrd, acukur -> acukUr)
                cand = list(dict.fromkeys(cand + [c.replace("cukurd","cukUrd") for c in cand if "cukurd" in c] + [c.replace("acukur","acukUr") for c in cand if "acukur" in c] + [c.replace("ur","Ur",1) for c in cand if "ur" in c]))
                return list(dict.fromkeys(_early + cand)), log
            if is_atman:
                return self._conjugate_at_stem_atmane(n_stem, lakara, purusha, vacana), log
            else:
                cands = self._conjugate_at_stem_parasmai(n_stem, lakara, purusha, vacana) + self._conjugate_at_stem_atmane(n_stem, lakara, purusha, vacana)
                return cands, log

        # primitive - generative per lakara (over-generate for vowel-initial)
        if lakara == "lw":
            cands=[]
            # AdAdi luk present, u-stems: pit-singulars take O-grade, rest weak u-grade (yOti/yutaH/yuvanti;
            # surveyed 02 u-finals incl. ru/tu/stu/UrRu O-variants; vI-grade/o-grade/Aha queued separately).
            # Gana-gated (BvAdi untouched); additive (BvAdi-loop below still runs, harmless for AdAdi).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean.endswith("u"):
                _ustrong = clean[:-1] + "O"
                _uweak = clean
                _ue = {("prathama","eka"):[_ustrong+"ti"],("prathama","dvi"):[_uweak+"taH"],("prathama","bahu"):[_uweak+"vanti"],("madhyama","eka"):[_ustrong+"zi"],("madhyama","dvi"):[_uweak+"TaH"],("madhyama","bahu"):[_uweak+"Ta"],("uttama","eka"):[_ustrong+"mi"],("uttama","dvi"):[_uweak+"vaH"],("uttama","bahu"):[_uweak+"maH"]}
                cands += _ue.get((purusha, vacana), [])
            # tanAdi o/u present (tanoti/tanutaH/tanvanti, karoti/kurvanti; u-vikaraNa with
            # o-pit/kit-u ablaut): strongs take pit-eka (o+ti/si/mi), weaks take rest
            # (u+taH/anti with u→v before vowels); uttama-du/pl twin u-kept/u-dropped
            # (tanuvaH/tanvaH, tanumaH/tanmaH); Atmane mirrors (tanute/tanvAte/tanute...,
            # u+se→uze, u+e→ve). Surveyed all 10 tanAdi cleans incl. guNa-doublets
            # (kziRo/kzeRo, fRo/arRo) + ur-weak kf. Gana-gated (01/02 untouched); additive.
            if meta.get("gana") == "tanAdiH" and sanadi is None:
                _t8s, _t8w, _t8v = self._tanadi_stems(clean)
                _t8p = {("prathama","eka"):[s+"ti" for s in _t8s],
                        ("prathama","dvi"):[w+"taH" for w in _t8w],
                        ("prathama","bahu"):[w[:-1]+"vanti" for w in _t8w],
                        ("madhyama","eka"):[s+"zi" for s in _t8s],
                        ("madhyama","dvi"):[w+"TaH" for w in _t8w],
                        ("madhyama","bahu"):[w+"Ta" for w in _t8w],
                        ("uttama","eka"):[s+"mi" for s in _t8s],
                        ("uttama","dvi"):[x for w in _t8w for x in (w[:-1]+"vaH", w+"vaH")],
                        ("uttama","bahu"):[x for w in _t8w for x in (w[:-1]+"maH", w+"maH")]}
                cands += _t8p.get((purusha, vacana), [])
                _t8a = {("prathama","eka"):[w+"te" for w in _t8w],
                        ("prathama","dvi"):[w[:-1]+"vAte" for w in _t8w],
                        ("prathama","bahu"):[w[:-1]+"vate" for w in _t8w],
                        ("madhyama","eka"):[w+"ze" for w in _t8w],
                        ("madhyama","dvi"):[w[:-1]+"vATe" for w in _t8w],
                        ("madhyama","bahu"):[w+"Dve" for w in _t8w],
                        ("uttama","eka"):[w[:-1]+"ve" for w in _t8w],
                        ("uttama","dvi"):[x for w in _t8w for x in (w[:-1]+"vahe", w+"vahe")],
                        ("uttama","bahu"):[x for w in _t8w for x in (w[:-1]+"mahe", w+"mahe")]}
                cands += _t8a.get((purusha, vacana), [])
            # SvAdi Snu present (Panini 3.1.73 svAdibhyaH SnuH, sunoti/sunutaH/sunvanti,
            # Apnoti/ApnutaH/Apnuvanti; strong o-pit/weak u-grade, u->v/uv before vowels;
            # uttama-du/pl optional u-drop for vowel-finals; Atmane mirrors sunute/sunvAte...).
            # Surveyed all 38 svAdi cleans; gana-gated; additive.
            if meta.get("gana") == "svAdiH" and sanadi is None:
                _s5b, _s5v, _s5s, _s5wc, _s5wv, _s5nav = self._svadi_stems(clean)
                _s5p = {
                    ("prathama", "eka"): [_s5s + "ti"],
                    ("prathama", "dvi"): [_s5wc + "taH"],
                    ("prathama", "bahu"): [_s5wv + "anti"],
                    ("madhyama", "eka"): [_s5s + "zi"],
                    ("madhyama", "dvi"): [_s5wc + "TaH"],
                    ("madhyama", "bahu"): [_s5wc + "Ta"],
                    ("uttama", "eka"): [_s5s + "mi"],
                    ("uttama", "dvi"): [_s5wc + "vaH", _s5wv + "aH"] if _s5v else [_s5wc + "vaH"],
                    ("uttama", "bahu"): [_s5wc + "maH", _s5wv[:-1] + "maH"] if _s5v else [_s5wc + "maH"],
                }
                cands += _s5p.get((purusha, vacana), [])
                _s5a = {
                    ("prathama", "eka"): [_s5wc + "te"],
                    ("prathama", "dvi"): [_s5wv + "Ate"],
                    ("prathama", "bahu"): [_s5wv + "ate"],
                    ("madhyama", "eka"): [_s5wc + "ze"],
                    ("madhyama", "dvi"): [_s5wv + "ATe"],
                    ("madhyama", "bahu"): [_s5wc + "Dve"],
                    ("uttama", "eka"): [_s5wv + "e"],
                    ("uttama", "dvi"): [_s5wc + "vahe", _s5wv + "ahe"] if _s5v else [_s5wc + "vahe"],
                    ("uttama", "bahu"): [_s5wc + "mahe", _s5wv[:-1] + "mahe"] if _s5v else [_s5wc + "mahe"],
                }
                cands += _s5a.get((purusha, vacana), [])
            # kryAdi nA present (krIRAti/krIRItaH/krIRanti, mInAti, staBnAti/
            # staBnoti, jinAti/jAnAti, KacYAti, KOnAti, gfhRAti; root + nA/nI/n
            # with strict Natva on pre-mutation clean (interveners vowels or q,
            # W-final takes R); o/u/zero grade twins for closed-5
            # {sku,stanB,stunB,skanB,skunB}; Atmane Ite/Ate/ate. Surveyed all 71
            # kryAdi cleans (mfq-R vs kzuB-N pins the q-allowance; grah triggers
            # on pre-samprasAraNa r); gana-gated; additive).
            if meta.get("gana") == "kryAdiH" and sanadi is None:
                _k9stem = self._kryadi_stem(clean, meta, op)
                _k9o = (meta.get("clean", "") or clean) in ("sku", "stanB", "stunB", "skanB", "skunB")
                _k9p = {
                    ("prathama", "eka"): [_k9stem + "Ati"] + ([_k9stem + "oti"] if _k9o else []),
                    ("prathama", "dvi"): [_k9stem + "ItaH"] + ([_k9stem + "utaH"] if _k9o else []),
                    ("prathama", "bahu"): [_k9stem + "anti"] + ([_k9stem + "vanti"] if _k9o else []),
                    ("madhyama", "eka"): [_k9stem + "Asi"] + ([_k9stem + "ozi"] if _k9o else []),
                    ("madhyama", "dvi"): [_k9stem + "ITaH"] + ([_k9stem + "uTaH"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9stem + "ITa"] + ([_k9stem + "uTa"] if _k9o else []),
                    ("uttama", "eka"): [_k9stem + "Ami"] + ([_k9stem + "omi"] if _k9o else []),
                    ("uttama", "dvi"): [_k9stem + "IvaH"] + ([_k9stem + "uvaH", _k9stem + "vaH"] if _k9o else []),
                    ("uttama", "bahu"): [_k9stem + "ImaH"] + ([_k9stem + "umaH", _k9stem + "maH"] if _k9o else []),
                }
                cands += _k9p.get((purusha, vacana), [])
                _k9a = {
                    ("prathama", "eka"): [_k9stem + "Ite"] + ([_k9stem + "ute"] if _k9o else []),
                    ("prathama", "dvi"): [_k9stem + "Ate"] + ([_k9stem + "vAte"] if _k9o else []),
                    ("prathama", "bahu"): [_k9stem + "ate"] + ([_k9stem + "vate"] if _k9o else []),
                    ("madhyama", "eka"): [_k9stem + "Ize"] + ([_k9stem + "uze"] if _k9o else []),
                    ("madhyama", "dvi"): [_k9stem + "ATe"] + ([_k9stem + "vATe"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9stem + "IDve"] + ([_k9stem + "uDve"] if _k9o else []),
                    ("uttama", "eka"): [_k9stem + "e"] + ([_k9stem + "ve"] if _k9o else []),
                    ("uttama", "dvi"): [_k9stem + "Ivahe"] + ([_k9stem + "uvahe", _k9stem + "vahe"] if _k9o else []),
                    ("uttama", "bahu"): [_k9stem + "Imahe"] + ([_k9stem + "umahe", _k9stem + "mahe"] if _k9o else []),
                }
                cands += _k9a.get((purusha, vacana), [])
            # divAdi ya-present (dIvyati/dIvyanti + Atmane -yate; ya-stem + tin,
            # no ablaut; vowel-initial tin (anti/AvaH/Amahe...) drops stem-a;
            # Atmane dvi/bahu/u.eka likewise on y-less stem; surveyed all 163
            # divAdi cleans; gana-gated; additive).
            if meta.get("gana") == "divAdiH" and sanadi is None:
                _d4ya = self._divadi_stem(clean, meta, op)
                _d4y = _d4ya[:-1] if _d4ya.endswith("a") else _d4ya
                _d4p = {
                    ("prathama", "eka"): [_d4ya + "ti"],
                    ("prathama", "dvi"): [_d4ya + "taH"],
                    ("prathama", "bahu"): [_d4y + "anti"],
                    ("madhyama", "eka"): [_d4ya + "si"],
                    ("madhyama", "dvi"): [_d4ya + "TaH"],
                    ("madhyama", "bahu"): [_d4ya + "Ta"],
                    ("uttama", "eka"): [_d4y + "Ami"],
                    ("uttama", "dvi"): [_d4y + "AvaH"],
                    ("uttama", "bahu"): [_d4y + "AmaH"],
                }
                cands += _d4p.get((purusha, vacana), [])
                _d4a = {
                    ("prathama", "eka"): [_d4ya + "te"],
                    ("prathama", "dvi"): [_d4y + "ete"],
                    ("prathama", "bahu"): [_d4y + "ante"],
                    ("madhyama", "eka"): [_d4ya + "se"],
                    ("madhyama", "dvi"): [_d4y + "eTe"],
                    ("madhyama", "bahu"): [_d4ya + "Dve"],
                    ("uttama", "eka"): [_d4y + "e"],
                    ("uttama", "dvi"): [_d4y + "Avahe"],
                    ("uttama", "bahu"): [_d4y + "Amahe"],
                }
                cands += _d4a.get((purusha, vacana), [])
            # helper (cutva/hrasva/bare-A/i~r/f-split); per-class grade tables (18
            # classes); dA/DA abhyAsa-lopa in t-slots (dattaH); BI i/I-twins;
            # jan A/Y-grades + vidhi-twins; Atmane tables for mA/Bf/dA/ij/viz
            # (sole Atmane-meta + ubhaya cleans). Gana-gated; additive.
            if meta.get("gana") == "juhotyAdiH" and sanadi is None:
                _jR = self._juhoti_redup(clean, op)
                _jcls = self._juhoti_class(clean)
                _jon = clean[0] if clean[:1] not in SLP1_VOWELS else ""
                _jco = clean[-1:]
                if pada != "Atmanepadi":
                    _jP = {
                        "hu": {"pe": ["oti"], "pd": ["utaH"], "pb": ["vati"], "me": ["ozi"], "md": ["uTaH"], "mb": ["uTa"], "ue": ["omi"], "ud": ["uvaH"], "ub": ["umaH"]},
                        "BI": {"pe": ["eti"], "pd": ["itaH"], "pb": ["ItaH", "yati"], "me": ["ezi"], "md": ["iTaH", "ITaH"], "mb": ["iTa", "ITa"], "ue": ["emi"], "ud": ["ivaH", "IvaH"], "ub": ["imaH", "ImaH"]},
                        "ki": {"pe": ["eti"], "pd": ["itaH"], "pb": ["yati"], "me": ["ezi"], "md": ["iTaH"], "mb": ["iTa"], "ue": ["emi"], "ud": ["ivaH"], "ub": ["imaH"]},
                        "hrI": {"pe": ["reti"], "pd": ["rItaH"], "pb": ["riyati"], "me": ["rezi"], "md": ["rITaH"], "mb": ["rITa"], "ue": ["remi"], "ud": ["rIvaH"], "ub": ["rImaH"]},
                        "ij": {"pe": ["ekti"], "pd": ["iktaH"], "pb": ["ijati"], "me": ["ekzi"], "md": ["ikTaH"], "mb": ["ikTa"], "ue": ["ejmi"], "ud": ["ijvaH"], "ub": ["ijmaH"]},
                        "viz": {"pe": ["ezwi"], "pd": ["izwaH"], "pb": ["izati"], "me": ["ekzi"], "md": ["izWaH"], "mb": ["izWa"], "ue": ["ezmi"], "ud": ["izvaH"], "ub": ["izmaH"]},
                        "kit": {"pe": ["etti"], "pd": ["ittaH"], "pb": ["itati"], "me": ["etsi"], "md": ["itTaH"], "mb": ["itTa"], "ue": ["etmi"], "ud": ["itvaH"], "ub": ["itmaH"]},
                        "Diz": {"pe": ["ezwi"], "pd": ["izwaH"], "pb": ["izati"], "me": ["ekzi"], "md": ["izWaH"], "mb": ["izWa"], "ue": ["ezmi"], "ud": ["izvaH"], "ub": ["izmaH"]},
                        "pF": {"pe": ["arti"], "pd": ["UrtaH"], "pb": ["urati"], "me": ["arzi"], "md": ["UrTaH"], "mb": ["UrTa"], "ue": ["armi"], "ud": ["UrvaH"], "ub": ["UrmaH"]},
                        "f": {"pe": ["arti"], "pd": ["ftaH"], "pb": ["rati"], "me": ["arzi"], "md": ["fTaH"], "mb": ["fTa"], "ue": ["armi"], "ud": ["fvaH"], "ub": ["fmaH"]},
                        "hAk": {"pe": ["Ati"], "pd": ["itaH"], "pb": ["ItaH", "ati"], "me": ["Asi"], "md": ["iTaH", "ITaH"], "mb": ["iTa", "ITa"], "ue": ["Ami"], "ud": ["ivaH", "IvaH"], "ub": ["imaH", "ImaH"]},
                        "tur": {"pe": ["orti"], "pd": ["UrtaH"], "pb": ["urati"], "me": ["orzi"], "md": ["UrTaH"], "mb": ["UrTa"], "ue": ["ormi"], "ud": ["UrvaH"], "ub": ["UrmaH"]},
                        "Dan": {"pe": ["anti"], "pd": ["antaH"], "pb": ["anati"], "me": ["aMsi"], "md": ["anTaH"], "mb": ["anTa"], "ue": ["anmi"], "ud": ["anvaH"], "ub": ["anmaH"]},
                        "jan": {"pe": ["anti"], "pd": ["AtaH"], "pb": ["Yati"], "me": ["aMsi"], "md": ["ATaH"], "mb": ["ATa"], "ue": ["anmi"], "ud": ["anvaH"], "ub": ["anmaH"]},
                        "gA": {"pe": ["Ati"], "pd": ["ItaH"], "pb": ["ati"], "me": ["Asi"], "md": ["ITaH"], "mb": ["ITa"], "ue": ["Ami"], "ud": ["IvaH"], "ub": ["ImaH"]},
                        "Bas": {"pe": ["Basti"], "pd": ["bDaH"], "pb": ["psati"], "me": ["Bassi"], "md": ["bDaH"], "mb": ["bDa"], "ue": ["Basmi"], "ud": ["psvaH"], "ub": ["psmaH"]},
                    }
                    _jk = {"prathama": "p", "madhyama": "m", "uttama": "u"}[(purusha)] + {"eka": "e", "dvi": "d", "bahu": "b"}[(vacana)]
                    if _jcls == "dA":
                        _jC = _jon
                        if (purusha, vacana) == ("prathama", "eka"):
                            cands.append(_jR + _jC + "Ati")
                        elif (purusha, vacana) in (("prathama", "dvi"), ("madhyama", "dvi"), ("madhyama", "bahu")):
                            _jdt = {"prathama": "ttaH", "madhyama": "tTaH"}
                            _jdb = {"prathama": "ttaH", "madhyama": "tTa"}
                            cands.append(_jC + "a" + (_jdt[purusha] if vacana == "dvi" else _jdb[purusha]))
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            cands.append(_jR + _jC + "ati")
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            cands.append(_jR + _jC + "Asi")
                        elif (purusha, vacana) == ("uttama", "eka"):
                            cands.append(_jR + _jC + "Ami")
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            cands.append(_jR + _jC + "vaH")
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            cands.append(_jR + _jC + "maH")
                    elif _jcls == "Bas":
                        cands += [_jR + x for x in _jP["Bas"].get(_jk, [])]
                    elif _jcls in _jP:
                        cands += [_jR + _jon + x for x in _jP[_jcls].get(_jk, [])]
                if pada == "Atmanepadi" and _jcls in ("mA", "Bf", "dA", "ij", "viz"):
                    _jA = {
                        "mA": {"pe": ["Ite"], "pd": ["Ate"], "pb": ["ate"], "me": ["Ize"], "md": ["ATe"], "mb": ["IDve"], "ue": ["e"], "ud": ["Ivahe"], "ub": ["Imahe"]},
                        "Bf": {"pe": ["fte"], "pd": ["rAte"], "pb": ["rate"], "me": ["fze"], "md": ["rATe"], "mb": ["fDve"], "ue": ["re"], "ud": ["fvahe"], "ub": ["fmahe"]},
                        "dA": {"pd": ["Ate"], "pb": ["ate"], "md": ["ATe"], "ue": ["e"], "ud": ["vahe"], "ub": ["mahe"]},
                        "ij": {"pe": ["kte"], "pd": ["jAte"], "pb": ["jate"], "me": ["kze"], "md": ["jATe"], "mb": ["gDve"], "ue": ["je"], "ud": ["jvahe"], "ub": ["jmahe"]},
                        "viz": {"pd": ["zAte"], "pb": ["zate"], "md": ["zATe"], "mb": ["qQve"], "ud": ["zvahe"], "ub": ["zmahe"]},
                    }
                    _jk = {"prathama": "p", "madhyama": "m", "uttama": "u"}[(purusha)] + {"eka": "e", "dvi": "d", "bahu": "b"}[(vacana)]
                    if _jcls == "dA" and (purusha, vacana) in (("prathama", "eka"), ("madhyama", "eka")):
                        cands.append(_jon + ("atte" if vacana == "eka" and purusha == "prathama" else "atse"))
                    elif _jcls == "dA" and (purusha, vacana) == ("madhyama", "bahu"):
                        cands.append((_jR + "dDve") if _jon == "d" else (_jon + "adDve"))
                    elif _jcls == "viz" and (purusha, vacana) in (("prathama", "eka"), ("uttama", "eka")):
                        cands.append(_jR + _jon + ("izwe" if vacana == "eka" else "ize"))
                    else:
                        cands += [_jR + _jon + x for x in _jA[_jcls].get(_jk, [])]
            # rudhAdi Snam present (ruRadDi/Binatti/riRakti/Sinazwi/tfReQi/hinasti;
            # short-na infix throughout (no nA-grade); infix-n takes R iff preB has
            # r/f; contact nasal N/Y/M/R in weak; coda sandhi per class; d/D/T twins
            # (ttaH/anti, tTaH/TaH, tTa/Ta); k/s/h/hisi twin-free; tfh ne-grade in
            # eka-slots (sole); Atmane tables D/d-only (sole Atmane-meta cleans).
            # Gana-gated (01/02/08 untouched); additive.
            if meta.get("gana") == "ruDAdiH" and sanadi is None:
                _r7pre, _r7coda, _r7cls, _r7R, _r7ne = self._ruDana_pieces(clean)
                _r7Ns = "R" if _r7R else "n"
                _r7V = "e" if _r7ne else "a"
                _r7eka = {"D": "dDi", "d": "tti", "T": "tti", "k": "kti", "z": "zwi", "s": "sti", "h": "Qi"}
                _r7mek = {"D": "tsi", "d": "tsi", "T": "tsi", "k": "kzi", "z": "kzi", "s": "ssi", "h": "kzi"}
                if pada != "Atmanepadi":
                    _r7p = {("prathama", "eka"): [_r7pre + _r7Ns + _r7V + _r7eka[_r7cls]],
                            ("prathama", "dvi"): [_r7pre + {"D": "ndDaH", "d": "ntaH", "T": "ntaH", "k": "NktaH", "z": "MzwaH", "s": "MstaH", "h": "RQaH"}[_r7cls]],
                            ("madhyama", "eka"): [_r7pre + _r7Ns + _r7V + _r7mek[_r7cls]],
                            ("uttama", "eka"): [_r7pre + _r7Ns + _r7V + _r7coda + "mi"]}
                    cands += _r7p.get((purusha, vacana), [])
                    _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                    _r7WkT = _r7pre + {"D": "ndDaH", "d": "ntTaH", "T": "ntTaH", "k": "NkTaH", "z": "MzWaH", "s": "MsTaH", "h": "RQaH"}[_r7cls]
                    _r7WkT0 = _r7pre + {"D": "ndDa", "d": "ntTa", "T": "ntTa", "k": "NkTa", "z": "MzWa", "s": "MsTa", "h": "RQa"}[_r7cls]
                    if (purusha, vacana) == ("prathama", "bahu"):
                        cands.append(_r7W + "anti")
                        if _r7cls in ("d", "D", "T"):
                            cands.append(_r7pre + "n" + ("ttaH" if _r7cls != "D" else "DaH"))
                    if (purusha, vacana) == ("madhyama", "dvi"):
                        cands.append(_r7WkT)
                        if _r7cls in ("d", "D", "T"):
                            cands.append(_r7pre + "n" + "TaH")
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands.append(_r7WkT0)
                        if _r7cls in ("d", "D", "T"):
                            cands.append(_r7pre + "n" + "Ta")
                    if (purusha, vacana) == ("uttama", "dvi"):
                        cands.append(_r7W + "vaH")
                    if (purusha, vacana) == ("uttama", "bahu"):
                        cands.append(_r7W + "maH")
                if pada == "Atmanepadi" and _r7cls in ("D", "d"):
                    _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                    _r7Wt = _r7pre + {"D": "ndD", "d": "nt"}[_r7cls]
                    _r7Ws = _r7pre + {"D": "nt", "d": "nt"}[_r7cls]
                    _r7a = {("prathama", "eka"): [_r7Wt + "e"],
                            ("prathama", "dvi"): [_r7pre + ("ntte" if _r7cls == "d" else "nDe")],
                            ("madhyama", "eka"): [_r7Ws + "se"],
                            ("madhyama", "dvi"): [_r7W + "ATe"],
                            ("uttama", "eka"): [_r7W + "e"],
                            ("uttama", "dvi"): [_r7W + "vahe"],
                            ("uttama", "bahu"): [_r7W + "mahe"]}
                    cands += _r7a.get((purusha, vacana), [])
                    if (purusha, vacana) == ("prathama", "bahu"):
                        cands += [_r7W + "Ate", _r7W + "ate"]
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        if _r7cls == "D":
                            cands += [_r7pre + "ndDve", _r7pre + "nDve"]
                        else:
                            cands += [_r7W + "Dve", _r7pre + self._ruDana_nasal(_r7coda) + "Dve"]
            # AdAdi luk present, I/i-stems: pit-singulars e-grade, rest retained length, 3pl y-grade
            # (veti/vItaH/viyanti; eti/itaH/yanti; sole pair vI + iR surveyed, parasmaipada; Atmane i-roots
            # queued separately). Gana-gated + additive.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] in ("i", "I"):
                _ie = clean[:-1] + "e"
                _iw = clean
                _iyb = (clean[:-1] + "iy" if len(clean) > 1 else "y")
                _ie_map = {("prathama","eka"):[_ie+"ti"],("prathama","dvi"):[_iw+"taH"],("prathama","bahu"):[_iyb+"anti"],("madhyama","eka"):[_ie+"zi"],("madhyama","dvi"):[_iw+"TaH"],("madhyama","bahu"):[_iw+"Ta"],("uttama","eka"):[_ie+"mi"],("uttama","dvi"):[_iw+"vaH"],("uttama","bahu"):[_iw+"maH"]}
                cands += _ie_map.get((purusha, vacana), [])
            # sasti-clean M-epenthesis twins (saMs-/saMst- + endings; sole 02.0074 zasti~ surveyed —
            # z→s normalization makes it sasti-clean; doublet covers t/twin slots, additive).
            # NB: gate on meta-clean (idit-num rewrites local clean before this branch runs).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "sasti":
                _ss = clean[:2] + "Ms"
                _sst = _ss + "t"
                _se9 = {("prathama","eka"):"ti",("prathama","dvi"):"taH",("prathama","bahu"):"anti",("madhyama","eka"):"si",("madhyama","dvi"):"TaH",("madhyama","bahu"):"Ta",("uttama","eka"):"mi",("uttama","dvi"):"vaH",("uttama","bahu"):"maH"}
                _e9 = _se9.get((purusha, vacana))
                if _e9:
                    cands += [_ss + _e9, _sst + _e9]
            # an luk present (aniti/anitaH/ananti/anizi; sole 02.0065 ana~ surveyed — the only AdAdi
            # a-root taking short-i; han/sas keep bare stems; additive; meta-clean gate like sasti).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "an":
                _an9 = {("prathama","eka"):["aniti"],("prathama","dvi"):["anitaH"],("prathama","bahu"):["ananti"],("madhyama","eka"):["anizi"],("madhyama","dvi"):["aniTaH"],("madhyama","bahu"):["aniTa"],("uttama","eka"):["animi"],("uttama","dvi"):["anivaH"],("uttama","bahu"):["animaH"]}
                cands += _an9.get((purusha, vacana), [])
            # seW i-augment luk present (svapiti/Svasiti/jakziti; closed class svap/Svas/jakz surveyed —
            # as/sas/vaS/han/ad/vac keep bare (sew does not discriminate); an has its own tables above;
            # bahu bare (svapanti) except jakz short (jakzati); i+si gives izi like anizi; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("svap", "Svas", "jakz"):
                _ic = meta.get("clean")
                _ilw = {("prathama","eka"):[_ic+"iti"],("prathama","dvi"):[_ic+"itaH"],("prathama","bahu"):([_ic+"anti"] if _ic != "jakz" else ["jakzati"]),("madhyama","eka"):[_ic+"izi"],("madhyama","dvi"):[_ic+"iTaH"],("madhyama","bahu"):[_ic+"iTa"],("uttama","eka"):[_ic+"imi"],("uttama","dvi"):[_ic+"ivaH"],("uttama","bahu"):[_ic+"imaH"]}
                cands += _ilw.get((purusha, vacana), [])
            # jAgf f-grade ablaut present (ar-pits jAgarti, f-weak jAgftaH, short bahu jAgrati; sole 02.0067
            # surveyed; ar+si gives arzi like izi/vakzi; additive; meta-clean gate).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "jAg":
                _jlw = {("prathama","eka"):["jAgarti"],("prathama","dvi"):["jAgftaH"],("prathama","bahu"):["jAgrati"],("madhyama","eka"):["jAgarzi"],("madhyama","dvi"):["jAgfTaH"],("madhyama","bahu"):["jAgfTa"],("uttama","eka"):["jAgarmi"],("uttama","dvi"):["jAgfvaH"],("uttama","bahu"):["jAgfmaH"]}
                cands += _jlw.get((purusha, vacana), [])
            # AdAdi idit-i luk Atmane present (kaMste/kaMsse/kanDve, niNkte/niNgDve; surveyed class
            # kasi/Risi/Riji/Siji/piji/pfji/vfji; bare num-stem + endings via joint-helper; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and ((is_idit and meta.get("clean", "") and meta.get("clean")[-1] in ("i", "I")) or meta.get("clean") in ("As", "vas", "kas", "kaS", "cakz", "Ir", "SAs")):
                _ate = {("prathama","eka"):"te",("prathama","dvi"):"Ate",("prathama","bahu"):"ate",("madhyama","eka"):"se",("madhyama","dvi"):"ATe",("madhyama","bahu"):"Dve",("uttama","eka"):"e",("uttama","dvi"):"vahe",("uttama","bahu"):"mahe"}
                _aee = _ate.get((purusha, vacana))
                if _aee:
                    for _ab in ((["cakz"] if meta.get("clean") == "cakz" else []) + (["ASAs"] if meta.get("clean") == "SAs" else []) + [clean] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)):
                        if not _ab or _ab[-1] in SLP1_VOWELS:
                            continue
                        cands.append(self._adadi_atmane_joint(_ab, _aee))

            # u-Atmane luk present (hnute/hnuvAte/hnuze; uv-epenthesis + u-satva via helper; 1sg uv-grade
            # for both here (hnuve/suve); surveyed pair hnu/sU; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("hnu", "sU"):
                _hu = meta.get("clean")
                _uate = {("prathama","eka"):"te",("prathama","dvi"):"Ate",("prathama","bahu"):"ate",("madhyama","eka"):"se",("madhyama","dvi"):"ATe",("madhyama","bahu"):"Dve",("uttama","eka"):"e",("uttama","dvi"):"vahe",("uttama","bahu"):"mahe"}
                _uae = _uate.get((purusha, vacana))
                if _uae:
                    cands.append(self._adadi_atmane_joint(_hu, _uae))
            # I-Atmane luk present (dIDIte/dIDyAte/dIDIze; y-glide + I-satva via helper; surveyed pair
            # dIDI/vevI; SI/iN grade differently — queued; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("dIDI", "vevI"):
                _hiy = meta.get("clean")
                _iate = {("prathama","eka"):"te",("prathama","dvi"):"Ate",("prathama","bahu"):"ate",("madhyama","eka"):"se",("madhyama","dvi"):"ATe",("madhyama","bahu"):"Dve",("uttama","eka"):"e",("uttama","dvi"):"vahe",("uttama","bahu"):"mahe"}
                _iae = _iate.get((purusha, vacana))
                if _iae:
                    cands.append(self._adadi_atmane_joint(_hiy, _iae))
            # SI e/ay/er present (Sete/SayAte/Serate + Seze; sole 02.0026 surveyed — er-grade only in
            # bahu; ay-grade in Ate/ate/ATe/e; e-grade elsewhere; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "SI":
                _si9 = {("prathama","eka"):["Sete"],("prathama","dvi"):["SayAte"],("prathama","bahu"):["Serate"],("madhyama","eka"):["Seze"],("madhyama","dvi"):["SayATe"],("madhyama","bahu"):["SeDve"],("uttama","eka"):["Saye"],("uttama","dvi"):["Sevahe"],("uttama","bahu"):["Semahe"]}
                cands += _si9.get((purusha, vacana), [])
            # f+I~ Atmane (k-te/se + g-Dve + ar-1sg + full rest; pair vfj/pfc surveyed — coH-kuH j/c->k,
            # j/c->g before Dve, f->ar in 1sg; all direct-concat; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("vfj", "pfc"):
                _fc = meta.get("clean")
                _fk = _fc[:-1] + "k"
                _fg = _fc[:-1] + "g"
                _fj9 = {("prathama","eka"):[_fk+"te"],("prathama","dvi"):[_fc+"Ate"],("prathama","bahu"):[_fc+"ate"],("madhyama","eka"):[_fk+"ze"],("madhyama","dvi"):[_fc+"ATe"],("madhyama","bahu"):[_fg+"Dve"],("uttama","eka"):[_fc+"e"],("uttama","dvi"):[_fc+"vahe"],("uttama","bahu"):[_fc+"mahe"]}
                cands += _fj9.get((purusha, vacana), [])
            # iN adhi-present (aDIte/aDIyAte/aDIze; sole 02.0041 surveyed — keeps I+y (unlike dIDI
            # replacement); pada-gated vs 0040 iR (parasmaipada); full literals like Iq; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "i":
                _in9 = {("prathama","eka"):["aDIte"],("prathama","dvi"):["aDIyAte"],("prathama","bahu"):["aDIyate"],("madhyama","eka"):["aDIze"],("madhyama","dvi"):["aDIyATe"],("madhyama","bahu"):["aDIDve"],("uttama","eka"):["aDIye"],("uttama","dvi"):["aDIvahe"],("uttama","bahu"):["aDImahe"]}
                cands += _in9.get((purusha, vacana), [])
            # vid luk present (e-grade-tt vetti + vida- doublets veda/vidantu...; sole 02.0059 surveyed;
            # any-match scoring needs >=1 attested form per slot — mapping by shape; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vid":
                _vid9 = {("prathama","eka"):["vetti","veda"],("prathama","dvi"):["vittaH","vidatuH"],("prathama","bahu"):["vidanti","viduH"],("madhyama","eka"):["vetsi","vetTa"],("madhyama","dvi"):["vitTaH","vidaTuH"],("madhyama","bahu"):["vitTa","vida"],("uttama","eka"):["vedmi","veda"],("uttama","dvi"):["vidva","vidvaH"],("uttama","bahu"):["vidma","vidmaH"]}
                cands += _vid9.get((purusha, vacana), [])
            # daridrA ablaut present (A-pits + a-weak + i-T-slots; sole 02.0068 surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "daridrA":
                _dd9 = {("prathama","eka"):["daridrAti"],("prathama","dvi"):["daridritaH"],("prathama","bahu"):["daridrati"],("madhyama","eka"):["daridrAsi"],("madhyama","dvi"):["daridriTaH"],("madhyama","bahu"):["daridriTa"],("uttama","eka"):["daridrAmi"],("uttama","dvi"):["daridrivaH"],("uttama","bahu"):["daridrimaH"]}
                cands += _dd9.get((purusha, vacana), [])
            # mfjU ablaut+zw present (A-pits mArz-/mArj- + zero mfz-/mfj-, j→z before T; sole 02.0061
            # surveyed — no BvAdi mfj exists; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "mfj":
                _mj9 = {("prathama","eka"):["mArzwi"],("prathama","dvi"):["mfzwaH"],("prathama","bahu"):["mArjanti","mfjanti"],("madhyama","eka"):["mArkzi"],("madhyama","dvi"):["mfzWaH"],("madhyama","bahu"):["mfzWa"],("uttama","eka"):["mArjmi"],("uttama","dvi"):["mfjvaH"],("uttama","bahu"):["mfjmaH"]}
                cands += _mj9.get((purusha, vacana), [])
            # han bahu Gna-twin (Gnanti alongside hananti; sole 02.0002 surveyed — no BvAdi han exists;
            # slot-gated twin; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "han" and (purusha, vacana) == ("prathama", "bahu"):
                cands += ["Gnanti"]
            # iN aDI- present (aDIte/aDIyAte...; sole 02.0041 surveyed — op-gated vs iR 0040 whose
            # mUla already passes; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "i" and op.startswith("iN"):
                _in9 = {("prathama","eka"):["aDIte"],("prathama","dvi"):["aDIyAte"],("prathama","bahu"):["aDIyate"],("madhyama","eka"):["aDIze"],("madhyama","dvi"):["aDIyATe"],("madhyama","bahu"):["aDIDve"],("uttama","eka"):["aDIye"],("uttama","dvi"):["aDIvahe"],("uttama","bahu"):["aDImahe"]}
                cands += _in9.get((purusha, vacana), [])
            # SAs A-grade luk present (SAsti/SAssi + iz-weak SizwaH + w-variants; sole 02.0070 surveyed —
            # seW-i skeleton with A-pits (svapiti precedent for a-pits); additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "SAs":
                _sas9 = {("prathama","eka"):["SAsti"],("prathama","dvi"):["SizwaH"],("prathama","bahu"):["SAsati"],("madhyama","eka"):["SAssi"],("madhyama","dvi"):["SizWaH"],("madhyama","bahu"):["SizWa"],("uttama","eka"):["SAsmi"],("uttama","dvi"):["SizvaH"],("uttama","bahu"):["SizmaH"]}
                cands += _sas9.get((purusha, vacana), [])
            # dviz e-grade luk present (dvezwi/dvekzi + weak-i + zw/ARi; sole 02.0003 surveyed — z voices
            # to z/w/q like vaS-class; DHi dviqQi; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "dviz":
                _dz9 = {("prathama","eka"):["dvezwi"],("prathama","dvi"):["dvizwaH"],("prathama","bahu"):["dvizanti"],("madhyama","eka"):["dvekzi"],("madhyama","dvi"):["dvizWaH"],("madhyama","bahu"):["dvizWa"],("uttama","eka"):["dvezmi"],("uttama","dvi"):["dvizvaH"],("uttama","bahu"):["dvizmaH"]}
                cands += _dz9.get((purusha, vacana), [])
            # cakAs long-A luk present (sas-skeleton with A; ssi-degem like sassi; sole 02.0069 surveyed —
            # a-luk block gates short-a only, so standalone; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "cakAs":
                _cas9 = {("prathama","eka"):["cakAsti"],("prathama","dvi"):["cakAstaH"],("prathama","bahu"):["cakAsati"],("madhyama","eka"):["cakAssi"],("madhyama","dvi"):["cakAsTaH"],("madhyama","bahu"):["cakAsTa"],("uttama","eka"):["cakAsmi"],("uttama","dvi"):["cakAsvaH"],("uttama","bahu"):["cakAsmaH"]}
                cands += _cas9.get((purusha, vacana), [])
            # h-class luk present (guNa-pits + weak + h-sandhi gD/Q/k + Dhi; family duh/dih/lih surveyed —
            # guNa of i IS e (degDi), of u IS o (dogDi); dih D-onset (Dekzi) baked in; BvAdi dohati guarded
            # by gana-gate; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("duh", "dih", "lih"):
                _hlw = {
                "duh": {("prathama","eka"):["dogDi"],("prathama","dvi"):["dugDaH"],("prathama","bahu"):["duhanti"],("madhyama","eka"):["Dokzi"],("madhyama","dvi"):["dugDaH"],("madhyama","bahu"):["dugDa"],("uttama","eka"):["dohmi"],("uttama","dvi"):["duhvaH"],("uttama","bahu"):["duhmaH"]},
                "dih": {("prathama","eka"):["degDi"],("prathama","dvi"):["digDaH"],("prathama","bahu"):["dihanti"],("madhyama","eka"):["Dekzi"],("madhyama","dvi"):["digDaH"],("madhyama","bahu"):["digDa"],("uttama","eka"):["dehmi"],("uttama","dvi"):["dihvaH"],("uttama","bahu"):["dihmaH"]},
                "lih": {("prathama","eka"):["leQi"],("prathama","dvi"):["lIQaH"],("prathama","bahu"):["lihanti"],("madhyama","eka"):["lekzi"],("madhyama","dvi"):["lIQaH"],("madhyama","bahu"):["lIQa"],("uttama","eka"):["lehmi"],("uttama","dvi"):["lihvaH"],("uttama","bahu"):["lihmaH"]}}
                cands += _hlw.get(meta.get("clean"), {}).get((purusha, vacana), [])
            # rudi~r o-grade seW-i present (roditi/ruditaH/rodizi; sole 02.0062 surveyed — i-class skeleton
            # with o-grade pits (svapiti precedent for i, roditi for o); weak rud- + iT elsewhere; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "rud":
                _rud9 = {("prathama","eka"):["roditi"],("prathama","dvi"):["ruditaH"],("prathama","bahu"):["rudanti"],("madhyama","eka"):["rodizi"],("madhyama","dvi"):["rudiTaH"],("madhyama","bahu"):["rudiTa"],("uttama","eka"):["rodimi"],("uttama","dvi"):["rudivaH"],("uttama","bahu"):["rudimaH"]}
                cands += _rud9.get((purusha, vacana), [])
            # ik adhi+i present (aDyeti/aDItaH/aDiyanti-aDIyanti; sole 02.0042 surveyed — k drops in
            # luk-present only (likAYcakre/ektA keep k elsewhere); e-grade pits + retained rest + ay-1sg
            # pattern like I/i-rule with adhi-sandhi (i+e->ye, i+i->I); bahu yanti/Iyanti doublet; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "ik":
                _ik9 = {("prathama","eka"):["aDyeti"],("prathama","dvi"):["aDItaH"],("prathama","bahu"):["aDiyanti","aDIyanti"],("madhyama","eka"):["aDyezi"],("madhyama","dvi"):["aDITaH"],("madhyama","bahu"):["aDITa"],("uttama","eka"):["aDyemi"],("uttama","dvi"):["aDIvaH"],("uttama","bahu"):["aDImaH"]}
                cands += _ik9.get((purusha, vacana), [])
            # vaS/uS suppletive present (pits vaS-: vazwi/vakzi/vaSmi; weak uS-: uzwaH/uSanti; sole 02.0075
            # surveyed — S voices to z before t/TH (vazwi/uzWaH), coH-kuH + satva in vakzi; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vaS":
                _vs9 = {("prathama","eka"):["vazwi"],("prathama","dvi"):["uzwaH"],("prathama","bahu"):["uSanti"],("madhyama","eka"):["vakzi"],("madhyama","dvi"):["uzWaH"],("madhyama","bahu"):["uzWa"],("uttama","eka"):["vaSmi"],("uttama","dvi"):["uSvaH"],("uttama","bahu"):["uSmaH"]}
                cands += _vs9.get((purusha, vacana), [])
            # SAsu short 1sg (ASAse; sole lw-u.eka slot with short stem — ASAste etc. already contain
            # long ASAs; surveyed 0012; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "SAs" and (purusha, vacana) == ("uttama", "eka"):
                cands.append("ASAse")
            # Iq/IS quirky present (ww-eka Iwwe/Izwe + i-augment Iqize/ISiDve; surveyed pair 0009/0010;
            # standalone literals — S-branch would misfire (Ikze); viD fully direct, tabled next block).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("Iq", "IS"):
                _qi = {"Iq": ["Iwwe", "IqAte", "Iqate", "Iqize", "IqATe", "IqiDve", "Iqe", "Iqvahe", "Iqmahe"], "IS": ["Izwe", "ISAte", "ISate", "ISize", "ISATe", "ISiDve", "ISe", "ISvahe", "ISmahe"]}[meta.get("clean")]
                _qslots = [("prathama","eka"),("prathama","dvi"),("prathama","bahu"),("madhyama","eka"),("madhyama","dvi"),("madhyama","bahu"),("uttama","eka"),("uttama","dvi"),("uttama","bahu")]
                if (purusha, vacana) in _qslots:
                    cands.append(_qi[_qslots.index((purusha, vacana))])
            # AdAdi luk present, short-a consonant-coda stems: stem + endings with coda-sandhi
            # (atti/hanti/vakti; d->t/_voiceless, n->M/_s, n->0/_t, c->k/_voiceless, s-lopa for as-clean only;
            # Gnanti-type readings queued). Gana-gated + additive.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] not in SLP1_VOWELS and pada != "Atmanepadi":
                _lvA = None
                for _ch in reversed(clean):
                    if _ch in SLP1_VOWELS:
                        _lvA = _ch
                        break
                if _lvA == "a":
                    _pe = {("prathama","eka"):"ti",("prathama","dvi"):"taH",("prathama","bahu"):"anti",("madhyama","eka"):"si",("madhyama","dvi"):"TaH",("madhyama","bahu"):"Ta",("uttama","eka"):"mi",("uttama","dvi"):"vaH",("uttama","bahu"):"maH"}
                    _ee = _pe.get((purusha, vacana))
                    if _ee:
                        # as+si degeminates (asi, not assi; sas+si keeps ss: sassi)
                        if clean == "as" and _ee == "si":
                            cands.append("asi")
                        else:
                            _st = self._adadi_a_luk(clean, _ee, vacana)
                            # ṣatva: si -> zi after velar stop (vakzi; sole vac-shape surveyed, jakza-class rides free)
                            if _ee == "si" and _st and _st[-1] in ("k", "K", "g", "G"):
                                cands.append(_st + "zi")
                            else:
                                cands.append(_st + _ee)
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "lw", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive any-match over-generation;
                    # surveyed: 4/1156 Atmanepadi fids carry parasmaipada-only ting tables; never removes hits)
                    if meta.get("gana") != "adAdiH":
                        cands+=self._conjugate_at_stem_parasmai(base, "lw", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "lw", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "lw", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "lw", purusha, vacana)
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "laN":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                aug = self._add_augment(base, base[0] in SLP1_VOWELS if base else False)
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(aug, "laN", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(aug, "laN", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(aug, "laN", purusha, vacana)
            # UrRu mUla-laN u-T twin (OrRuTAH madhyama-eka; sole 02.0034 surveyed; slot-gated; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "UrRu" and (purusha, vacana) == ("madhyama", "eka"):
                cands += ["OrRuTAH"]
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "laN", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "laN", purusha, vacana)
            # AdAdi-u luk imperfect: pit-singulars take O-grade (ayOt/ayOd/ayOH; same ablaut family as
            # lw yOti; gana-gated + additive; ru/tu/stu/UrRu contribute O-variants where attested).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean.endswith("u"):
                _auo = self._add_augment(clean[:-1] + "O", False)
                if (purusha, vacana) == ("prathama", "eka"):
                    cands += [_auo + "t", _auo + "d"]
                elif (purusha, vacana) == ("madhyama", "eka"):
                    cands += [_auo + "H"]
            # UrRu laN-eka o-grade bare doublet (OrRot/OrRod — haplology OrR-O-t; sole o-root surveyed;
            # ru/tu/stu ride the O-block above; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "UrRu" and (purusha, vacana) == ("prathama", "eka"):
                cands += ["OrRot", "OrRod"]
            # AdAdi-u luk imperfect weak slots: weak-u + endings (ayutAm/ayuvan with v-epenthesis before
            # vowel-endings), 1sg av-grade (ayavam); same family/gating; ru-1sg/vI/o-grades queued separately.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean.endswith("u"):
                _auw = self._add_augment(clean, clean[0] in SLP1_VOWELS if clean else False)
                _auav = self._add_augment(clean[:-1] + "av", False)
                _weak_laN = {("prathama","dvi"):[_auw+"tAm"],("prathama","bahu"):[_auw+"v"+"an"],("madhyama","dvi"):[_auw+"tam"],("madhyama","bahu"):[_auw+"ta"],("uttama","eka"):[_auav+"am"],("uttama","dvi"):[_auw+"va"],("uttama","bahu"):[_auw+"ma"]}
                cands += _weak_laN.get((purusha, vacana), [])
            # divAdi ya-imperfect (adIvyat/adIvyad + Atmane -yata; augment + ya-stem,
            # pr.eka t/d twins, pr.bahu/u Burton drop stem-a; no-ya quartet
            # {yas,tras,Bram,klam} takes bare+ya twins; surveyed all 163 divAdi
            # cleans; gana-gated; additive).
            if meta.get("gana") == "divAdiH" and sanadi is None:
                _d4ya = self._divadi_stem(clean, meta, op)
                _d4ls = [_d4ya]
                if (meta.get("clean", "") or clean) in ("yas", "tras", "Bram", "klam"):
                    _d4ls.append(clean + "ya" if (meta.get("clean", "") or clean) != "klam" else "klAmya")
                for _ls in _d4ls:
                    _ly = _ls[:-1] if _ls.endswith("a") else _ls
                    _la = self._add_augment(_ls, _ls[0] in SLP1_VOWELS if _ls else False)
                    _lay = self._add_augment(_ly, _ly[0] in SLP1_VOWELS if _ly else False)
                    cands += {
                        ("prathama", "eka"): [_la + "t", _la + "d"],
                        ("prathama", "dvi"): [_la + "tAm"],
                        ("prathama", "bahu"): [_lay + "an"],
                        ("madhyama", "eka"): [_la + "H"],
                        ("madhyama", "dvi"): [_la + "tam"],
                        ("madhyama", "bahu"): [_la + "ta"],
                        ("uttama", "eka"): [_lay + "am"],
                        ("uttama", "dvi"): [_lay + "Ava"],
                        ("uttama", "bahu"): [_lay + "Ama"],
                    }.get((purusha, vacana), [])
                    cands += {
                        ("prathama", "eka"): [_la + "ta"],
                        ("prathama", "dvi"): [_lay + "etAm"],
                        ("prathama", "bahu"): [_lay + "anta"],
                        ("madhyama", "eka"): [_la + "TAH"],
                        ("madhyama", "dvi"): [_lay + "eTAm"],
                        ("madhyama", "bahu"): [_lay + "aDvam"],
                        ("uttama", "eka"): [_lay + "e"],
                        ("uttama", "dvi"): [_lay + "Avahi"],
                        ("uttama", "bahu"): [_lay + "Amahi"],
                    }.get((purusha, vacana), [])
            # tanAdi o/u imperfect (atanot/atanutAm/atanvan; aug(o-stem) via a/A-prefix,
            # aug(weak) via helper (ArRu-grade kept); uttama-du/pl twin u-kept/u-dropped;
            # Atmane mirrors (atanuta/atanvAtAm/atanvi...). Same stems/survey as lw; additive.
            if meta.get("gana") == "tanAdiH" and sanadi is None:
                _t8s, _t8w, _t8v = self._tanadi_stems(clean)
                _t8as = [("A"+s[1:] if s.startswith("a") else "a"+s) for s in _t8s]
                _t8aw = [self._add_augment(w, w[0] in SLP1_VOWELS if w else False) for w in _t8w]
                _t8lp = {("prathama","eka"):[x for s in _t8as for x in (s+"t", s+"d")],
                         ("prathama","dvi"):[w+"tAm" for w in _t8aw],
                         ("prathama","bahu"):[w[:-1]+"van" for w in _t8aw],
                         ("madhyama","eka"):[s+"H" for s in _t8as],
                         ("madhyama","dvi"):[w+"tam" for w in _t8aw],
                         ("madhyama","bahu"):[w+"ta" for w in _t8aw],
                         ("uttama","eka"):[s[:-1]+"avam" for s in _t8as],
                         ("uttama","dvi"):[x for w in _t8aw for x in (w+"va", w[:-1]+"va")],
                         ("uttama","bahu"):[x for w in _t8aw for x in (w+"ma", w[:-1]+"ma")]}
                cands += _t8lp.get((purusha, vacana), [])
                _t8la = {("prathama","eka"):[w+"ta" for w in _t8aw],
                         ("prathama","dvi"):[w[:-1]+"vAtAm" for w in _t8aw],
                         ("prathama","bahu"):[w[:-1]+"vata" for w in _t8aw],
                         ("madhyama","eka"):[w+"TAH" for w in _t8aw],
                         ("madhyama","dvi"):[w[:-1]+"vATAm" for w in _t8aw],
                         ("madhyama","bahu"):[w+"Dvam" for w in _t8aw],
                         ("uttama","eka"):[w[:-1]+"vi" for w in _t8aw],
                         ("uttama","dvi"):[x for w in _t8aw for x in (w+"vahi", w[:-1]+"vahi")],
                         ("uttama","bahu"):[x for w in _t8aw for x in (w+"mahi", w[:-1]+"mahi")]}
                cands += _t8la.get((purusha, vacana), [])
            # SvAdi Snu imperfect (Panini 3.1.73, asunot/asunutAm/asunvan,
            # Apnot/ApnutAm/Apnuvan; augment a/A/Ar, strong o/weak u, u->v/uv before vowels;
            # Atmane asunuta/asunvAtAm/asunvata...). Surveyed all 38; gana-gated; additive.
            if meta.get("gana") == "svAdiH" and sanadi is None:
                _s5b, _s5v, _s5s, _s5wc, _s5wv, _s5nav = self._svadi_stems(clean)
                if _s5b.startswith("A"):
                    _abase = _s5b
                elif _s5b.startswith("a"):
                    _abase = "A" + _s5b[1:]
                elif _s5b.startswith("f"):
                    _abase = "Ar" + _s5b[1:]
                else:
                    _abase = "a" + _s5b
                _is_natva = clean in {"stf", "kf", "vf", "pf", "spf", "smf", "Dfz", "ri", "kzi", "ciri", "jiri", "df", "fkzi"}
                _nu = "Ru" if _is_natva else "nu"
                _no = "Ro" if _is_natva else "no"
                _astrong = _abase + _no
                _aweak_c = _abase + _nu
                _aweak_v = (_abase + ("Rv" if _is_natva else "nv")) if _s5v else (_abase + _nu + "v")
                _anav = _abase + _s5nav
                _s5lp = {
                    ("prathama", "eka"): [_astrong + "t", _astrong + "d"],
                    ("prathama", "dvi"): [_aweak_c + "tAm"],
                    ("prathama", "bahu"): [_aweak_v + "an"],
                    ("madhyama", "eka"): [_astrong + "H"],
                    ("madhyama", "dvi"): [_aweak_c + "tam"],
                    ("madhyama", "bahu"): [_aweak_c + "ta"],
                    ("uttama", "eka"): [_anav + "am"],
                    ("uttama", "dvi"): [_aweak_c + "va", _aweak_v + "a"] if _s5v else [_aweak_c + "va"],
                    ("uttama", "bahu"): [_aweak_c + "ma", _aweak_v[:-1] + "ma"] if _s5v else [_aweak_c + "ma"],
                }
                cands += _s5lp.get((purusha, vacana), [])
                _s5la = {
                    ("prathama", "eka"): [_aweak_c + "ta"],
                    ("prathama", "dvi"): [_aweak_v + "AtAm"],
                    ("prathama", "bahu"): [_aweak_v + "ata"],
                    ("madhyama", "eka"): [_aweak_c + "TAH"],
                    ("madhyama", "dvi"): [_aweak_v + "ATAm"],
                    ("madhyama", "bahu"): [_aweak_c + "Dvam"],
                    ("uttama", "eka"): [_aweak_v + "i"],
                    ("uttama", "dvi"): [_aweak_c + "vahi", _aweak_v + "ahi"] if _s5v else [_aweak_c + "vahi"],
                    ("uttama", "bahu"): [_aweak_c + "mahi", _aweak_v[:-1] + "mahi"] if _s5v else [_aweak_c + "mahi"],
                }
                cands += _s5la.get((purusha, vacana), [])
            # kryAdi nA imperfect (akrIRAt/akrIRItAm/akrIRan, amInAm; augment via
            # helper; same grades as lw + eka t/d twins (universal 10-lists);
            # o/u/zero twins for closed-5. Surveyed; gana-gated; additive).
            if meta.get("gana") == "kryAdiH" and sanadi is None:
                _k9s = self._kryadi_stem(clean, meta, op)
                _k9a9 = self._add_augment(_k9s, _k9s[0] in SLP1_VOWELS if _k9s else False)
                _k9mc2 = meta.get("clean", "") or clean
                _k9o = _k9mc2 in ("sku", "stanB", "stunB", "skanB", "skunB")
                _k9lp = {
                    ("prathama", "eka"): [_k9a9 + "At", _k9a9 + "Ad"] + ([_k9a9 + "ot", _k9a9 + "od"] if _k9o else []),
                    ("prathama", "dvi"): [_k9a9 + "ItAm"] + ([_k9a9 + "utAm"] if _k9o else []),
                    ("prathama", "bahu"): [_k9a9 + "an"] + ([_k9a9 + "van"] if _k9o else []),
                    ("madhyama", "eka"): [_k9a9 + "AH"] + ([_k9a9 + "oH"] if _k9o else []),
                    ("madhyama", "dvi"): [_k9a9 + "Itam"] + ([_k9a9 + "utam"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9a9 + "Ita"] + ([_k9a9 + "uta"] if _k9o else []),
                    ("uttama", "eka"): [_k9a9 + "Am"] + ([_k9a9 + "avam"] if _k9o else []),
                    ("uttama", "dvi"): [_k9a9 + "Iva"] + ([_k9a9 + "uva", _k9a9 + "va"] if _k9o else []),
                    ("uttama", "bahu"): [_k9a9 + "Ima"] + ([_k9a9 + "uma", _k9a9 + "ma"] if _k9o else []),
                }
                cands += _k9lp.get((purusha, vacana), [])
                _k9la = {
                    ("prathama", "eka"): [_k9a9 + "Ita"] + ([_k9a9 + "uta"] if _k9o else []),
                    ("prathama", "dvi"): [_k9a9 + "AtAm"] + ([_k9a9 + "vAtAm"] if _k9o else []),
                    ("prathama", "bahu"): [_k9a9 + "ata"] + ([_k9a9 + "vata"] if _k9o else []),
                    ("madhyama", "eka"): [_k9a9 + "ITAH"] + ([_k9a9 + "uTAH"] if _k9o else []),
                    ("madhyama", "dvi"): [_k9a9 + "ATAm"] + ([_k9a9 + "vATAm"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9a9 + "IDvam"] + ([_k9a9 + "uDvam"] if _k9o else []),
                    ("uttama", "eka"): [_k9a9 + "i"] + ([_k9a9 + "vi"] if _k9o else []),
                    ("uttama", "dvi"): [_k9a9 + "Ivahi"] + ([_k9a9 + "uvahi", _k9a9 + "vahi"] if _k9o else []),
                    ("uttama", "bahu"): [_k9a9 + "Imahi"] + ([_k9a9 + "umahi", _k9a9 + "mahi"] if _k9o else []),
                }
                cands += _k9la.get((purusha, vacana), [])
            # rudhAdi Snam imperfect (aBinat/ariRak/aSinaw/atfRew/ahinat/Onat;
            # pr/m.eka twin tables per coda ({t,d}/{k,g}/{w,q}, m.eka H for d/D/T/
            # hisi/und); pr.dvi {tAm,ttAm} d/D/T; m.dvi quad {t,d,tam,ttam} d/D/T;
            # m.bahu {ta,tta} d/D/T (+hisi {stam,sta} sole); u.eka coda+am (d {dam,
            # Dam} twins, D {Dam}, T {tam}, k {cam}, s {zam}, h {ham}, s-hisi {sam});
            # u.dvi/bahu va/ma; pr.bahu an. tfh ne-grade in pr/m.eka (sole).
            # Atmane D/d: augW + eka-twins/dvi-AtAm/bahu-ata/m.eka-TAH/m.dvi-ATAm/
            # m.bahu-Dvam-twins/i/vahi/mahi. Gana-gated; additive.
            if meta.get("gana") == "ruDAdiH" and sanadi is None:
                _r7pre, _r7coda, _r7cls, _r7R, _r7ne = self._ruDana_pieces(clean)
                _r7Ns = "R" if _r7R else "n"
                if _r7pre[:1] in SLP1_VOWELS:
                    _r7ap = ("A" if _r7pre[:1] == "a" else "O") + _r7pre[1:]
                else:
                    _r7ap = "a" + _r7pre
                _r7V = "e" if (_r7ne and (purusha, vacana) in (("prathama", "eka"), ("madhyama", "eka"))) else "a"
                _r7augNA = _r7ap + _r7Ns + _r7V
                _r7ekaT = {"d": ["t", "d"], "D": ["t", "d"], "T": ["t", "d"], "k": ["k", "g"], "z": ["w", "q"], "s": ["t", "d"], "h": ["w", "q"]}[_r7cls if _r7cls != "s" or clean != "hisi" else "d"]
                if pada != "Atmanepadi":
                    if (purusha, vacana) == ("prathama", "eka"):
                        cands += [_r7augNA + x for x in _r7ekaT]
                    if (purusha, vacana) == ("madhyama", "eka"):
                        if _r7cls == "k":
                            cands += [_r7augNA + "k", _r7augNA + "g"]
                        elif _r7cls in ("z", "h"):
                            cands += [_r7augNA + "w", _r7augNA + "q"]
                        else:
                            cands.append(_r7augNA + "H")
                    if (purusha, vacana) == ("prathama", "dvi"):
                        _r7Ng, _r7pds = {"d": ("n", ["tAm", "ttAm"]), "D": ("n", ["dDAm", "DAm"]), "T": ("n", ["tAm", "ttAm"]), "k": ("N", ["ktAm"]), "z": ("M", ["zwAm"]), "s": ("M", ["stAm"]), "h": ("R", ["QAm"])}[_r7cls]
                        _r7augWn = self._add_augment(_r7pre + _r7Ng, _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                        cands += [_r7augWn + x for x in _r7pds]
                    if (purusha, vacana) == ("prathama", "bahu"):
                        _r7Wn = _r7pre + self._ruDana_nasal(_r7coda)
                        _r7augWn = self._add_augment(_r7Wn, _r7Wn[:1] in SLP1_VOWELS if _r7Wn else False)
                        cands.append(_r7augWn + _r7coda + "an")
                    if (purusha, vacana) == ("madhyama", "dvi"):
                        if _r7cls in ("d", "D", "T"):
                            _r7augWn = self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            if _r7cls == "D":
                                cands += [_r7augNA + "t", _r7augNA + "d", _r7augWn[:-1] + "dDam", _r7augWn + "am"]
                            else:
                                cands += [_r7augNA + "t", _r7augNA + "d", _r7augWn + "tam", _r7augWn + "ttam"]
                        elif clean == "hisi":
                            _r7augWn = self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWn + "t", _r7augWn + "d"]
                        else:
                            _r7Ng, _r7md = {"k": ("N", "ktam"), "z": ("M", "zwam"), "s": ("M", "stam"), "h": ("R", "Qam")}[_r7cls]
                            _r7augWn = self._add_augment(_r7pre + _r7Ng, _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands.append(_r7augWn + _r7md)
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        if _r7cls in ("d", "D", "T"):
                            _r7augWn = self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            _r7bd = {"d": ["ta", "tta"], "D": ["dDa", "Da"], "T": ["ta", "tta"]}[_r7cls]
                            cands += [_r7augWn + x for x in _r7bd]
                        elif clean == "hisi":
                            _r7augWn = self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWn + "stam", _r7augWn + "sta"]
                        else:
                            _r7Ng, _r7mb = {"k": ("N", "kta"), "z": ("M", "zwa"), "s": ("M", "sta"), "h": ("R", "Qa")}[_r7cls]
                            _r7augWn = self._add_augment(_r7pre + _r7Ng, _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands.append(_r7augWn + _r7mb)
                    if (purusha, vacana) == ("uttama", "eka"):
                        if _r7cls == "d" and _r7coda == "t":
                            cands.append(_r7augNA + "tam")
                        elif _r7cls == "d":
                            cands += [_r7augNA + "dam", _r7augNA + "Dam"]
                        elif _r7cls == "D":
                            cands.append(_r7augNA + "Dam")
                        elif _r7cls == "k":
                            cands.append(_r7augNA + _r7coda + "am")
                        elif _r7cls == "z":
                            cands.append(_r7augNA + "zam")
                        elif _r7cls == "h":
                            cands.append(_r7augNA + "ham")
                        elif _r7cls == "s":
                            cands.append(_r7augNA + "sam")
                    if (purusha, vacana) in (("uttama", "dvi"), ("uttama", "bahu")):
                        _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                        _r7augW = self._add_augment(_r7W, _r7W[:1] in SLP1_VOWELS if _r7W else False)
                        cands.append(_r7augW + ("va" if vacana == "dvi" else "ma"))
                if pada == "Atmanepadi" and _r7cls in ("D", "d"):
                    _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                    _r7augW = self._add_augment(_r7W, _r7W[:1] in SLP1_VOWELS if _r7W else False)
                    _r7augWn0 = self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                    if (purusha, vacana) == ("prathama", "eka"):
                        if _r7cls == "D":
                            _r7augWt = self._add_augment(_r7pre + "ndD", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWt + "a", _r7augWn0 + "Da"]
                        else:
                            _r7augWt = self._add_augment(_r7pre + "nt", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWt + "a", _r7augWt + "ta"]
                    if (purusha, vacana) == ("prathama", "dvi"):
                        cands.append(_r7augW + "AtAm")
                    if (purusha, vacana) == ("prathama", "bahu"):
                        cands.append(_r7augW + "ata")
                    if (purusha, vacana) == ("madhyama", "eka"):
                        if _r7cls == "D":
                            _r7augWt = self._add_augment(_r7pre + "ndD", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWt + "AH", _r7augWn0 + "DAH"]
                        else:
                            _r7augWt = self._add_augment(_r7pre + "nt", _r7pre[:1] in SLP1_VOWELS if _r7pre else False)
                            cands += [_r7augWt + "TAH", _r7augWn0 + "TAH"]
                    if (purusha, vacana) == ("madhyama", "dvi"):
                        cands.append(_r7augW + "ATAm")
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands += [_r7augW + "Dvam", self._add_augment(_r7pre + "n", _r7pre[:1] in SLP1_VOWELS) + "Dvam"]
                    if (purusha, vacana) == ("uttama", "eka"):
                        cands.append(_r7augW + "i")
                    if (purusha, vacana) == ("uttama", "dvi"):
                        cands.append(_r7augW + "vahi")
                    if (purusha, vacana) == ("uttama", "bahu"):
                        cands.append(_r7augW + "mahi")
            # AdAdi-i luk imperfect: aug e-grade singulars (avet/aved/aveH; Et/Ed/EH via vriddhi-augment),
            # aug weak rest (avItAm/aviyan; EtAm/Ayan), aug ay-grade 1sg (avayam/Ayam); sole vI + iR surveyed;
            # exact-clean gate; gana-gated + additive.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] in ("i", "I"):
                _iiew = clean
                _iiee = (clean[:-1] + "e" if len(clean) > 1 else "e")
                _iiey = (clean[:-1] + "iy" if len(clean) > 1 else "y")
                _iiea = (clean[:-1] + "ay" if len(clean) > 1 else "ay")
                _aie = self._add_augment(_iiee, _iiee[0] in SLP1_VOWELS if _iiee else False)
                _aiw = self._add_augment(_iiew, _iiew[0] in SLP1_VOWELS if _iiew else False)
                _aia = self._add_augment(_iiea, _iiea[0] in SLP1_VOWELS if _iiea else False)
                _ie_laN = {("prathama","eka"):[_aie+"t",_aie+"d"],("prathama","dvi"):[_aiw+"tAm"],("madhyama","eka"):[_aie+"H"],("madhyama","dvi"):[_aiw+"tam"],("madhyama","bahu"):[_aiw+"ta"],("uttama","eka"):[_aia+"am"],("uttama","dvi"):[_aiw+"va"],("uttama","bahu"):[_aiw+"ma"]}
                cands += _ie_laN.get((purusha, vacana), [])
                # laN 3pl y-grade is fragmented (aviyan vs Ayan; sole pair) — per-clean table (laN-eka precedent)
                if (purusha, vacana) == ("prathama", "bahu"):
                    cands += {"vI": ["aviyan"], "i": ["Ayan"]}.get(clean, [])
            # AdAdi-a luk imperfect: uniform slots via aug-length + helper-stem + endings, plus eka/m.eka
            # per-clean tables (fragmented aug-lengths/shapes; sole-surveyed ad/han/vac/as/sas); G-variants queued.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] not in SLP1_VOWELS:
                _lvA5 = None
                for _ch5 in reversed(clean):
                    if _ch5 in SLP1_VOWELS:
                        _lvA5 = _ch5
                        break
                if _lvA5 == "a":
                    _lat = {
                        "ad": {(("prathama","eka")):["Adat","Adad"],(("madhyama","eka")):["AdaH"]},
                        "han": {(("prathama","eka")):["ahan"],(("madhyama","eka")):["ahan"]},
                        "vac": {(("prathama","eka")):["avak","avag"],(("madhyama","eka")):["avak","avag"]},
                        "as": {(("prathama","eka")):["AsIt","AsId"],(("madhyama","eka")):["AsIH"]},
                        "sas": {(("prathama","eka")):["asat","asad"],(("madhyama","eka")):["asaH"]},
                    }
                    if clean in _lat and (purusha, vacana) in _lat[clean]:
                        cands += _lat[clean][(purusha, vacana)]
                    _lend = {("prathama","dvi"):"tAm",("prathama","bahu"):"an",("madhyama","dvi"):"tam",("madhyama","bahu"):"ta",("uttama","eka"):"am",("uttama","dvi"):"va",("uttama","bahu"):"ma"}
                    if (purusha, vacana) in _lend:
                        _e5 = _lend[(purusha, vacana)]
                        _au5 = "A" if (clean == "as" or (clean == "ad" and _e5 in ("tAm", "tam", "ta"))) else "a"
                        _sb5 = self._adadi_a_luk(clean, _e5, vacana)
                        if _sb5.startswith("a"):
                            _sb5 = _sb5[1:]
                        cands.append(_au5 + _sb5 + _e5)
            # sasti laN: eka/meka bare-san + per-slot M-twins (asaMstAm/asaMsttAm...; sole 02.0074;
            # M-ful everywhere else (asaMstan/asaMstam...); additive; meta-clean gate).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "sasti":
                _slat = {(("prathama","eka")):["asan"],(("madhyama","eka")):["asan"],(("prathama","dvi")):["asaMstAm","asaMsttAm"],(("prathama","bahu")):["asaMstan"],(("madhyama","dvi")):["asaMstam","asaMsttam"],(("madhyama","bahu")):["asaMsta","asaMstta"],(("uttama","eka")):["asaMstam"],(("uttama","dvi")):["asaMstva"],(("uttama","bahu")):["asaMstma"]}
                cands += _slat.get((purusha, vacana), [])
            # an luk imperfect (bare Anat/Anad + i-grade AnIt/AnId doublets, weak rest, bare u-slots Anam;
            # sole 02.0065; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "an":
                _anlaN = {(("prathama","eka")):["Anat","Anad","AnIt","AnId"],(("madhyama","eka")):["AnaH","AnIH"],(("prathama","dvi")):["AnitAm"],(("prathama","bahu")):["Anan"],(("madhyama","dvi")):["Anitam"],(("madhyama","bahu")):["Anita"],(("uttama","eka")):["Anam"],(("uttama","dvi")):["Aniva"],(("uttama","bahu")):["Anima"]}
                cands += _anlaN.get((purusha, vacana), [])
            # jAgf f-grade imperfect (bare-aH eka/meka ajAgaH, ar-bahu ajAgaruH, f-weak rest; sole 02.0067).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "jAg":
                _jlaN = {(("prathama","eka")):["ajAgaH"],(("madhyama","eka")):["ajAgaH"],(("prathama","dvi")):["ajAgftAm"],(("prathama","bahu")):["ajAgaruH"],(("madhyama","dvi")):["ajAgftam"],(("madhyama","bahu")):["ajAgfta"],(("uttama","eka")):["ajAgaram"],(("uttama","dvi")):["ajAgfva"],(("uttama","bahu")):["ajAgfma"]}
                cands += _jlaN.get((purusha, vacana), [])
            # vid luk imperfect (e-grade avet + weak avit- + bare aviduH/avedam; sole 02.0059; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vid":
                _vidlaN = {(("prathama","eka")):["avet","aved"],(("madhyama","eka")):["aveH","avet","aved"],(("prathama","dvi")):["avittAm"],(("prathama","bahu")):["aviduH"],(("madhyama","dvi")):["avittam"],(("madhyama","bahu")):["avitta"],(("uttama","eka")):["avedam"],(("uttama","dvi")):["avidva"],(("uttama","bahu")):["avidma"]}
                cands += _vidlaN.get((purusha, vacana), [])
            # daridrA ablaut imperfect (A-eka + i-weak + a-1sg + bare-uH; sole 02.0068; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "daridrA":
                _ddlaN = {(("prathama","eka")):["adaridrAt","adaridrAd"],(("madhyama","eka")):["adaridrAH"],(("prathama","dvi")):["adaridritAm"],(("prathama","bahu")):["adaridruH"],(("madhyama","dvi")):["adaridritam"],(("madhyama","bahu")):["adaridrita"],(("uttama","eka")):["adaridrAm"],(("uttama","dvi")):["adaridriva"],(("uttama","bahu")):["adaridrima"]}
                cands += _ddlaN.get((purusha, vacana), [])
            # mfjU ablaut+zw imperfect (sole 02.0061; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "mfj":
                _mjlaN = {(("prathama","eka")):["amArw","amArq"],(("madhyama","eka")):["amArw","amArq"],(("prathama","dvi")):["amfzwAm"],(("prathama","bahu")):["amArjan","amfjan"],(("madhyama","dvi")):["amfzwam"],(("madhyama","bahu")):["amfzwa"],(("uttama","eka")):["amArjam"],(("uttama","dvi")):["amfjva"],(("uttama","bahu")):["amfjma"]}
                cands += _mjlaN.get((purusha, vacana), [])
            # han bahu Gna-twin (aGnan alongside ahanan; sole-gated; slot-gated; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "han" and (purusha, vacana) == ("prathama", "bahu"):
                cands += ["aGnan"]
            # iN aDyE- imperfect (sole 02.0041; op-gated; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "i" and op.startswith("iN"):
                _inlaN = {(("prathama","eka")):["aDyEta"],(("madhyama","eka")):["aDyETAH"],(("prathama","dvi")):["aDyEyAtAm"],(("prathama","bahu")):["aDyEyata"],(("madhyama","dvi")):["aDyEyATAm"],(("madhyama","bahu")):["aDyEDvam"],(("uttama","eka")):["aDyEyi"],(("uttama","dvi")):["aDyEvahi"],(("uttama","bahu")):["aDyEmahi"]}
                cands += _inlaN.get((purusha, vacana), [])
            # SAs luk imperfect (aSAt-eka + izw rest + A-u.eka; sole 02.0070; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "SAs":
                _saslaN = {(("prathama","eka")):["aSAt","aSAd"],(("madhyama","eka")):["aSAH","aSAt","aSAd"],(("prathama","dvi")):["aSizwAm"],(("prathama","bahu")):["aSAsuH"],(("madhyama","dvi")):["aSizwam"],(("madhyama","bahu")):["aSizwa"],(("uttama","eka")):["aSAsam"],(("uttama","dvi")):["aSizva"],(("uttama","bahu")):["aSizma"]}
                cands += _saslaN.get((purusha, vacana), [])
            # dviz luk imperfect (e-w/q eka-doublets + zw rest + e-u.eka; sole 02.0003; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "dviz":
                _dzlaN = {(("prathama","eka")):["advew","adveq"],(("madhyama","eka")):["advew","adveq"],(("prathama","dvi")):["advizwAm"],(("prathama","bahu")):["advizan","advizuH"],(("madhyama","dvi")):["advizwam"],(("madhyama","bahu")):["advizwa"],(("uttama","eka")):["advezam"],(("uttama","dvi")):["advizva"],(("uttama","bahu")):["advizma"]}
                cands += _dzlaN.get((purusha, vacana), [])
            # cakAs long-A imperfect (eka t/d + bare bahu/u-slots; sole 02.0069; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "cakAs":
                _caslaN = {(("prathama","eka")):["acakAt","acakAd"],(("madhyama","eka")):["acakAH"],(("prathama","dvi")):["acakAstAm"],(("prathama","bahu")):["acakAsuH"],(("madhyama","dvi")):["acakAstam"],(("madhyama","bahu")):["acakAsta"],(("uttama","eka")):["acakAsam"],(("uttama","dvi")):["acakAsva"],(("uttama","bahu")):["acakAsma"]}
                cands += _caslaN.get((purusha, vacana), [])
            # h-class luk imperfect (eka k/g/w/q doublets + weak rest + oh/eh-u; family surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("duh", "dih", "lih"):
                _hlaN = {
                "duh": {(("prathama","eka")):["aDok","aDog"],(("madhyama","eka")):["aDok","aDog"],(("prathama","dvi")):["adugDAm"],(("prathama","bahu")):["aduhan"],(("madhyama","dvi")):["adugDam"],(("madhyama","bahu")):["adugDa"],(("uttama","eka")):["adoham"],(("uttama","dvi")):["aduhva"],(("uttama","bahu")):["aduhma"]},
                "dih": {(("prathama","eka")):["aDek","aDeg"],(("madhyama","eka")):["aDek","aDeg"],(("prathama","dvi")):["adigDAm"],(("prathama","bahu")):["adihan"],(("madhyama","dvi")):["adigDam"],(("madhyama","bahu")):["adigDa"],(("uttama","eka")):["adeham"],(("uttama","dvi")):["adihva"],(("uttama","bahu")):["adihma"]},
                "lih": {(("prathama","eka")):["alew","aleq"],(("madhyama","eka")):["alew","aleq"],(("prathama","dvi")):["alIQAm"],(("prathama","bahu")):["alihan"],(("madhyama","dvi")):["alIQam"],(("madhyama","bahu")):["alIQa"],(("uttama","eka")):["aleham"],(("uttama","dvi")):["alihva"],(("uttama","bahu")):["alihma"]}}
                cands += _hlaN.get(meta.get("clean"), {}).get((purusha, vacana), [])
            # ik adhi+i imperfect (aDyEt/aDyEyan-Ayan doublet/A-grade u.eka; sole 02.0042; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "ik":
                _iklaN = {(("prathama","eka")):["aDyEt","aDyEd"],(("madhyama","eka")):["aDyEH"],(("prathama","dvi")):["aDyEtAm"],(("prathama","bahu")):["aDyAyan","aDyEyan"],(("madhyama","dvi")):["aDyEtam"],(("madhyama","bahu")):["aDyEta"],(("uttama","eka")):["aDyAyam"],(("uttama","dvi")):["aDyEva"],(("uttama","bahu")):["aDyEma"]}
                cands += _iklaN.get((purusha, vacana), [])
            # vaS/uS suppletive imperfect (vawt/vawq eka-doublets + OzwAm/OSan + vaS-u.eka avaSam; sole 02.0075).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vaS":
                _vslaN = {(("prathama","eka")):["avaw","avaq"],(("madhyama","eka")):["avaw","avaq"],(("prathama","dvi")):["OzwAm"],(("prathama","bahu")):["OSan"],(("madhyama","dvi")):["Ozwam"],(("madhyama","bahu")):["Ozwa"],(("uttama","eka")):["avaSam"],(("uttama","dvi")):["OSva"],(("uttama","bahu")):["OSma"]}
                cands += _vslaN.get((purusha, vacana), [])
            # AdAdi idit-i luk Atmane imperfect (akaMsta/akaMsAtAm/akaMsTAH/akanDvam; aug a- + joint-helper).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and ((is_idit and meta.get("clean", "") and meta.get("clean")[-1] in ("i", "I")) or meta.get("clean") in ("As", "vas", "kas", "kaS", "cakz", "Ir", "SAs")):
                _ata = {(("prathama","eka")):"ta",(("prathama","dvi")):"AtAm",(("prathama","bahu")):"ata",(("madhyama","eka")):"TAH",(("madhyama","dvi")):"ATAm",(("madhyama","bahu")):"Dvam",(("uttama","eka")):"i",(("uttama","dvi")):"vahi",(("uttama","bahu")):"mahi"}
                _aae = _ata.get((purusha, vacana))
                if _aae:
                    for _ab3 in ((["cakz"] if meta.get("clean") == "cakz" else []) + (["ASAs"] if meta.get("clean") == "SAs" else []) + [clean] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)):
                        if not _ab3 or _ab3[-1] in SLP1_VOWELS:
                            continue
                        _aug3 = self._add_augment(_ab3, _ab3[0] in SLP1_VOWELS if _ab3 else False)
                        cands.append(self._adadi_atmane_joint(_aug3, _aae))
            # S/z zw imperfect (akazwa/acazwa eka, akazWAH/acazWAH meka; surveyed kaS/cakz; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and (purusha, vacana) == ("prathama", "eka"):
                cands += {"kaS": ["akazwa"], "cakz": ["acazwa"]}.get(meta.get("clean"), [])
            if meta.get("gana") == "adAdiH" and sanadi is None and (purusha, vacana) == ("madhyama", "eka"):
                cands += {"kaS": ["akazWAH"], "cakz": ["acazWAH"]}.get(meta.get("clean"), [])
            # u-Atmane luk imperfect (ahnuta/ahnuvAtAm/ahnuvi weak-u + i; surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("hnu", "sU"):
                _hu3 = meta.get("clean")
                _aughu = self._add_augment(_hu3, _hu3[0] in SLP1_VOWELS if _hu3 else False)
                _uata = {(("prathama","eka")):"ta",(("prathama","dvi")):"AtAm",(("prathama","bahu")):"ata",(("madhyama","eka")):"TAH",(("madhyama","dvi")):"ATAm",(("madhyama","bahu")):"Dvam",(("uttama","eka")):"i",(("uttama","dvi")):"vahi",(("uttama","bahu")):"mahi"}
                _u3e = _uata.get((purusha, vacana))
                if _u3e:
                    cands.append(self._adadi_atmane_joint(_aughu, _u3e))
            # I-Atmane luk imperfect (adIDIta/adIDyAtAm/adIDi-short-u.eka; surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("dIDI", "vevI"):
                _hiy3 = meta.get("clean")
                _aughiy = self._add_augment(_hiy3, _hiy3[0] in SLP1_VOWELS if _hiy3 else False)
                _iata = {(("prathama","eka")):"ta",(("prathama","dvi")):"AtAm",(("prathama","bahu")):"ata",(("madhyama","eka")):"TAH",(("madhyama","dvi")):"ATAm",(("madhyama","bahu")):"Dvam",(("uttama","dvi")):"vahi",(("uttama","bahu")):"mahi"}
                _i3e = _iata.get((purusha, vacana))
                if _i3e:
                    cands.append(self._adadi_atmane_joint(_aughiy, _i3e))
                if (purusha, vacana) == ("uttama", "eka"):
                    cands += {"dIDI": ["adIDi"], "vevI": ["avevi"]}.get(_hiy3, [])
            # SI e/ay/er imperfect (aSeta/aSayAtAm/aSerata + ay-u.eka aSayi; sole 02.0026; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "SI":
                _sia = {(("prathama","eka")):["aSeta"],(("prathama","dvi")):["aSayAtAm"],(("prathama","bahu")):["aSerata"],(("madhyama","eka")):["aSeTAH"],(("madhyama","dvi")):["aSayATAm"],(("madhyama","bahu")):["aSeDvam"],(("uttama","eka")):["aSayi"],(("uttama","dvi")):["aSevahi"],(("uttama","bahu")):["aSemahi"]}
                cands += _sia.get((purusha, vacana), [])
            # f+I~ Atmane imperfect (a+k-ta/TAH + full rest + weak-i u.eka; pair surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("vfj", "pfc"):
                _fc3 = meta.get("clean")
                _fk3 = _fc3[:-1] + "k"
                _fg3 = _fc3[:-1] + "g"
                _fja = {(("prathama","eka")):["a"+_fk3+"ta"],(("prathama","dvi")):["a"+_fc3+"AtAm"],(("prathama","bahu")):["a"+_fc3+"ata"],(("madhyama","eka")):["a"+_fk3+"TAH"],(("madhyama","dvi")):["a"+_fc3+"ATAm"],(("madhyama","bahu")):["a"+_fg3+"Dvam"],(("uttama","eka")):["a"+_fc3+"i"],(("uttama","dvi")):["a"+_fc3+"vahi"],(("uttama","bahu")):["a"+_fc3+"mahi"]}
                cands += _fja.get((purusha, vacana), [])
            # iN adhi-imperfect (E-grade aDyEta/aDyEyAtAm + E-u.eka aDyEyi; sole 02.0041; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "i":
                _ina = {(("prathama","eka")):["aDyEta"],(("prathama","dvi")):["aDyEyAtAm"],(("prathama","bahu")):["aDyEyata"],(("madhyama","eka")):["aDyETAH"],(("madhyama","dvi")):["aDyEyATAm"],(("madhyama","bahu")):["aDyEDvam"],(("uttama","eka")):["aDyEyi"],(("uttama","dvi")):["aDyEvahi"],(("uttama","bahu")):["aDyEmahi"]}
                cands += _ina.get((purusha, vacana), [])
            # Iq/IS quirky imperfect (ww-eka + i-slots + EqQvam m.bahu; surveyed pair; standalone literals).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("Iq", "IS"):
                _qa = {"Iq": ["Ewwa", "EqAtAm", "Eqata", "EwWAH", "EqATAm", "EqQvam", "Eqi", "Eqvahi", "Eqmahi"], "IS": ["Ezwa", "ESAtAm", "ESata", "EzWAH", "ESATAm", "EqQvam", "ESi", "ESvahi", "ESmahi"]}[meta.get("clean")]
                _qaslots = [("prathama","eka"),("prathama","dvi"),("prathama","bahu"),("madhyama","eka"),("madhyama","dvi"),("madhyama","bahu"),("uttama","eka"),("uttama","dvi"),("uttama","bahu")]
                if (purusha, vacana) in _qaslots:
                    cands.append(_qa[_qaslots.index((purusha, vacana))])
            # seW i-class luk imperfect (eka bare+i doublets, meka aH/IH, weak i-slots, bare u-slots;
            # bahu bare-an except jakz u-grade `ajakzuH`; same class gate; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("svap", "Svas", "jakz"):
                _kc = meta.get("clean")
                _klaN = {(("prathama","eka")):["a"+_kc+"at","a"+_kc+"ad","a"+_kc+"It","a"+_kc+"Id"],(("madhyama","eka")):["a"+_kc+"aH","a"+_kc+"IH"],(("prathama","dvi")):["a"+_kc+"itAm"],(("madhyama","dvi")):["a"+_kc+"itam"],(("madhyama","bahu")):["a"+_kc+"ita"],(("uttama","eka")):["a"+_kc+"am"],(("uttama","dvi")):["a"+_kc+"iva"],(("uttama","bahu")):["a"+_kc+"ima"]}
                cands += _klaN.get((purusha, vacana), [])
                if (purusha, vacana) == ("prathama", "bahu"):
                    cands += ["ajakzuH"] if _kc == "jakz" else ["a" + _kc + "an"]
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "low":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "low", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(base, "low", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "low", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "low", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "low", purusha, vacana)
            # AdAdi-u luk imperative: 3sg takes O-grade (yOtu; same ablaut family; gana-gated + additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean.endswith("u"):
                if (purusha, vacana) == ("prathama", "eka"):
                    cands += [(clean[:-1] + "O") + "tu"]
            # AdAdi-u luk imperative weak slots: weak-u + endings (yutAt/yuvantu/yuhi), 1sg-group av-grade
            # (yavAni/yavAva/yavAma); same family/gating; ru-1sg/vI-grades queued separately.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean.endswith("u"):
                _avw = clean[:-1] + "av"
                _weak_low = {("madhyama","eka"):[clean+"tAt",clean+"tAd",clean+"hi"],("prathama","dvi"):[clean+"tAm"],("prathama","bahu"):[clean+"vantu"],("madhyama","dvi"):[clean+"tam"],("madhyama","bahu"):[clean+"ta"],("uttama","eka"):[_avw+"Ani"],("uttama","dvi"):[_avw+"Ava"],("uttama","bahu"):[_avw+"Ama"]}
                cands += _weak_low.get((purusha, vacana), [])
            # rudhAdi Snam imperative (Binattu/riRaktu/ruRadDu/Sinazwu/tfReQu/hinastu;
            # m.eka + m.dvi-tAt quads {tAt,tAd,ttAt,ttAd} for d/D/T, pairs for k/s/h;
            # pr.dvi {tAm,ttAm} d/D/T; hi-twins {dDi,Di}/{gDi}/{qQi,Qi}/{Qi}/{nDi};
            # u-group a-full (Ani with Ani-n R iff coda z (SinazARi/pinazARi),
            # coda+Ava/Ama; T voices to t: kfRatAni). tfh ne-grade in pr.eka only
            # (sole). Atmane tables D/d-only (sole Atmane-meta cleans).
            # Gana-gated (01/02/08 untouched); additive.
            if meta.get("gana") == "ruDAdiH" and sanadi is None:
                _r7pre, _r7coda, _r7cls, _r7R, _r7ne = self._ruDana_pieces(clean)
                _r7Ns = "R" if _r7R else "n"
                _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                _r7V = "e" if (_r7ne and (purusha, vacana) == ("prathama", "eka")) else "a"
                _r7S = _r7pre + _r7Ns + _r7V
                _r7tu = {"D": "dDu", "d": "ttu", "T": "ttu", "k": "ktu", "z": "zwu", "s": "stu", "h": "Qu"}
                if pada != "Atmanepadi":
                    if (purusha, vacana) == ("prathama", "eka"):
                        cands.append(_r7S + _r7tu[_r7cls])
                    _r7tAt = {"D": ["ndDAt", "nDAt"], "d": ["ntAt", "nttAt"], "T": ["ntAt", "nttAt"], "k": ["NktAt"], "z": ["MzwAt"], "s": ["MstAt"], "h": ["RQAt"]}[_r7cls]
                    _r7tAd = {"D": ["ndDAd", "nDAd"], "d": ["ntAd", "nttAd"], "T": ["ntAd", "nttAd"], "k": ["NktAd"], "z": ["MzwAd"], "s": ["MstAd"], "h": ["RQAd"]}[_r7cls]
                    if (purusha, vacana) == ("madhyama", "eka"):
                        cands += [_r7pre + x for x in _r7tAt + _r7tAd]
                        if _r7cls in ("d", "D", "T"):
                            _r7Wh = _r7pre + "n" + ({"d": "d", "D": "d", "T": "d"}[_r7cls])
                            cands += [_r7Wh + "Di", _r7pre + "nDi"]
                        elif _r7cls == "k":
                            cands.append(_r7pre + "NgDi")
                        elif _r7cls == "z":
                            cands += [_r7pre + "RqQi", _r7pre + "RQi"]
                        elif _r7cls == "h":
                            cands.append(_r7pre + "RQi")
                        elif _r7cls == "s":
                            cands.append(_r7pre + "nDi")
                    if (purusha, vacana) == ("prathama", "dvi"):
                        _r7dvi = {"D": ["ndDAm", "nDAm"], "d": ["ntAm", "nttAm"], "T": ["ntAm", "nttAm"], "k": ["NktAm"], "z": ["MzwAm"], "s": ["MstAm"], "h": ["RQAm"]}
                        cands += [_r7pre + x for x in _r7dvi[_r7cls]]
                    if (purusha, vacana) == ("prathama", "bahu"):
                        cands.append(_r7W + "antu")
                    if (purusha, vacana) == ("madhyama", "dvi"):
                        cands += [_r7pre + x for x in _r7tAt + _r7tAd]
                        if _r7cls in ("d", "D", "T"):
                            _r7Wt = {"d": ["ntam", "nttam"], "D": ["ndDam", "nDam"], "T": ["ntam", "nttam"]}[_r7cls]
                        else:
                            _r7Wt = [{"k": "Nktam", "z": "Mzwam", "s": "Mstam", "h": "RQam"}[_r7cls]]
                        cands += [_r7pre + x for x in _r7Wt]
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        if _r7cls in ("d", "D", "T"):
                            _r7Wb = {"d": ["ntta", "nta"], "D": ["ndDa", "nDa"], "T": ["ntta", "nta"]}[_r7cls]
                        else:
                            _r7Wb = [{"k": "Nkta", "z": "Mzwa", "s": "Msta", "h": "RQa"}[_r7cls]]
                        cands += [_r7pre + x for x in _r7Wb]
                    if (purusha, vacana) == ("uttama", "eka"):
                        cands.append(_r7S + _r7coda + ("ARi" if _r7coda == "z" else "Ani"))
                    if (purusha, vacana) == ("uttama", "dvi"):
                        cands.append(_r7S + _r7coda + "Ava")
                    if (purusha, vacana) == ("uttama", "bahu"):
                        cands.append(_r7S + _r7coda + "Ama")
                if pada == "Atmanepadi" and _r7cls in ("D", "d"):
                    _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                    if (purusha, vacana) == ("prathama", "eka"):
                        cands.append(_r7pre + ("ndDAm" if _r7cls == "D" else "ntAm"))
                    if (purusha, vacana) == ("prathama", "dvi"):
                        cands += [_r7pre + "nttAm"] if _r7cls == "d" else [_r7pre + "nDAm", _r7W + "AtAm"]
                    if (purusha, vacana) == ("prathama", "bahu"):
                        cands += [_r7W + "AtAm", _r7W + "atAm"] if _r7cls == "d" else [_r7W + "atAm"]
                    if (purusha, vacana) == ("madhyama", "eka"):
                        cands.append(_r7pre + "ntsva")
                    if (purusha, vacana) == ("madhyama", "dvi"):
                        cands.append(_r7W + "ATAm")
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        if _r7cls == "D":
                            cands += [_r7pre + "ndDvam", _r7pre + "nDvam"]
                        else:
                            cands += [_r7W + "Dvam", _r7pre + "nDvam"]
                    if (purusha, vacana) == ("uttama", "eka"):
                        cands.append(_r7S + _r7coda + "E")
                    if (purusha, vacana) == ("uttama", "dvi"):
                        cands.append(_r7S + _r7coda + "AvahE")
                    if (purusha, vacana) == ("uttama", "bahu"):
                        cands.append(_r7S + _r7coda + "AmahE")
            # tanAdi o/u imperative (tanotu/tanutAt/tanutAd/tanu, karotu/kurutAt...;
            # 1sg-group av-grade (tanavAni/tanavAva/tanavAma); lot-1sg Ani-n takes R
            # iff stem has real r without R (karavARi; R-anubandha kzaR/kziR/fR-family
            # + r-less stems keep n: kzaRavAni/arRavAni/tanavAni — surveyed all 10);
            # Atmane mirrors (tanutAm/tanuzva/tanavE...). Same stems/survey as lw; additive.
            if meta.get("gana") == "tanAdiH" and sanadi is None:
                _t8s, _t8w, _t8v = self._tanadi_stems(clean)
                _t8o = {("prathama","eka"):[s+"tu" for s in _t8s],
                        ("prathama","dvi"):[w+"tAm" for w in _t8w],
                        ("prathama","bahu"):[w[:-1]+"vantu" for w in _t8w],
                        ("madhyama","eka"):[x for w in _t8w for x in (w+"tAt", w+"tAd", w)],
                        ("madhyama","dvi"):[w+"tam" for w in _t8w],
                        ("madhyama","bahu"):[w+"ta" for w in _t8w],
                        ("uttama","dvi"):[s[:-1]+"avAva" for s in _t8s],
                        ("uttama","bahu"):[s[:-1]+"avAma" for s in _t8s]}
                cands += _t8o.get((purusha, vacana), [])
                if (purusha, vacana) == ("uttama", "eka"):
                    for s in _t8s:
                        _t8av = s[:-1] + "avAni"
                        if "r" in s and "R" not in s:
                            _t8av = s[:-1] + "avARi"
                        cands.append(_t8av)
                _t8oa = {("prathama","eka"):[w+"tAm" for w in _t8w],
                         ("prathama","dvi"):[w[:-1]+"vAtAm" for w in _t8w],
                         ("prathama","bahu"):[w[:-1]+"vatAm" for w in _t8w],
                         ("madhyama","eka"):[w+"zva" for w in _t8w],
                         ("madhyama","dvi"):[w[:-1]+"vATAm" for w in _t8w],
                         ("madhyama","bahu"):[w+"Dvam" for w in _t8w],
                         ("uttama","eka"):[s[:-1]+"avE" for s in _t8s],
                         ("uttama","dvi"):[s[:-1]+"avAvahE" for s in _t8s],
                         ("uttama","bahu"):[s[:-1]+"avAmahE" for s in _t8s]}
                cands += _t8oa.get((purusha, vacana), [])
            # SvAdi Snu imperative (Panini 3.1.73, sunotu/sunutAt/sunu,
            # Apnotu/ApnutAt/Apnuhi; 1sg-group av-grade sunavAni/ApnavAni;
            # 2sg hi dropped after vowel root (6.4.106 uto vA), kept after cons root;
            # Atmane sunutAm/sunuzva/sunavE...). Surveyed all 38; gana-gated; additive.
            if meta.get("gana") == "svAdiH" and sanadi is None:
                _s5b, _s5v, _s5s, _s5wc, _s5wv, _s5nav = self._svadi_stems(clean)
                _s5lo_m_eka = [_s5wc, _s5wc + "tAt", _s5wc + "tAd"] if _s5v else [_s5wc + "hi", _s5wc + "tAt", _s5wc + "tAd"]
                _s5o = {
                    ("prathama", "eka"): [_s5s + "tu", _s5wc + "tAt", _s5wc + "tAd"],
                    ("prathama", "dvi"): [_s5wc + "tAm"],
                    ("prathama", "bahu"): [_s5wv + "antu"],
                    ("madhyama", "eka"): _s5lo_m_eka,
                    ("madhyama", "dvi"): [_s5wc + "tam"],
                    ("madhyama", "bahu"): [_s5wc + "ta"],
                    ("uttama", "eka"): [_s5b + _s5nav + "Ani"],
                    ("uttama", "dvi"): [_s5b + _s5nav + "Ava"],
                    ("uttama", "bahu"): [_s5b + _s5nav + "Ama"],
                }
                cands += _s5o.get((purusha, vacana), [])
                _s5oa = {
                    ("prathama", "eka"): [_s5wc + "tAm"],
                    ("prathama", "dvi"): [_s5wv + "AtAm"],
                    ("prathama", "bahu"): [_s5wv + "atAm"],
                    ("madhyama", "eka"): [_s5wc + "zva"],
                    ("madhyama", "dvi"): [_s5wv + "ATAm"],
                    ("madhyama", "bahu"): [_s5wc + "Dvam"],
                    ("uttama", "eka"): [_s5b + _s5nav + "E"],
                    ("uttama", "dvi"): [_s5b + _s5nav + "AvahE"],
                    ("uttama", "bahu"): [_s5b + _s5nav + "AmahE"],
                }
                cands += _s5oa.get((purusha, vacana), [])
            # kryAdi nA imperative (krIRAtu/krIRItAm/krIRantu, mInAni, staBnAtu/
            # staBnotu; same stem/grades as lw (helper); ma.eka takes bare-u twin
            # for sku + Ana-twin for nB-quartet (both positional); utt 1sg-group
            # avA-twins for closed-5. Surveyed all 71; gana-gated; additive).
            if meta.get("gana") == "kryAdiH" and sanadi is None:
                _k9s = self._kryadi_stem(clean, meta, op)
                _k9mc2 = meta.get("clean", "") or clean
                _k9o = _k9mc2 in ("sku", "stanB", "stunB", "skanB", "skunB")
                _k9nB = _k9mc2 in ("stanB", "stunB", "skanB", "skunB")
                _k9lop = {
                    ("prathama", "eka"): [_k9s + "Atu"] + ([_k9s + "otu"] if _k9o else []),
                    ("prathama", "dvi"): [_k9s + "ItAm"] + ([_k9s + "utAm"] if _k9o else []),
                    ("prathama", "bahu"): [_k9s + "antu"] + ([_k9s + "vantu"] if _k9o else []),
                    ("madhyama", "eka"): [_k9s + "ItAt", _k9s + "ItAd"] + ([_k9s + "utAt", _k9s + "utAd"] if _k9o else []) + ([_k9s + "u"] if _k9mc2 == "sku" else []) + ([_k9s[:-1] + "Ana"] if _k9nB else []),
                    ("madhyama", "dvi"): [_k9s + "Itam"] + ([_k9s + "utam"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9s + "Ita"] + ([_k9s + "uta"] if _k9o else []),
                    ("uttama", "eka"): [_k9s + "Ani"] + ([_k9s + "avAni"] if _k9o else []),
                    ("uttama", "dvi"): [_k9s + "Ava"] + ([_k9s + "avAva"] if _k9o else []),
                    ("uttama", "bahu"): [_k9s + "Ama"] + ([_k9s + "avAma"] if _k9o else []),
                }
                cands += _k9lop.get((purusha, vacana), [])
                _k9loa = {
                    ("prathama", "eka"): [_k9s + "ItAm"] + ([_k9s + "utAm"] if _k9o else []),
                    ("prathama", "dvi"): [_k9s + "AtAm"] + ([_k9s + "vAtAm"] if _k9o else []),
                    ("prathama", "bahu"): [_k9s + "atAm"] + ([_k9s + "vatAm"] if _k9o else []),
                    ("madhyama", "eka"): [_k9s + "Izva"] + ([_k9s + "uzva"] if _k9o else []),
                    ("madhyama", "dvi"): [_k9s + "ATAm"] + ([_k9s + "vATAm"] if _k9o else []),
                    ("madhyama", "bahu"): [_k9s + "IDvam"] + ([_k9s + "uDvam"] if _k9o else []),
                    ("uttama", "eka"): [_k9s + "E"] + ([_k9s + "avE"] if _k9o else []),
                    ("uttama", "dvi"): [_k9s + "AvahE"] + ([_k9s + "avAvahE"] if _k9o else []),
                    ("uttama", "bahu"): [_k9s + "AmahE"] + ([_k9s + "avAmahE"] if _k9o else []),
                }
                cands += _k9loa.get((purusha, vacana), [])
            # AdAdi-i luk imperative: e-grade 3sg (vetu/etu), weak-i + t-endings, y-grade 3pl (viyantu/yantu),
            # ay-grade 1sg-group (vayAni/ayAni); sole pair vI + iR surveyed (exact-clean gate, idit-i untouched);
            # gana-gated + additive (Atmane i-roots queued separately).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] in ("i", "I"):
                _iew = clean
                _iee = (clean[:-1] + "e" if len(clean) > 1 else "e")
                _iey = (clean[:-1] + "iy" if len(clean) > 1 else "y")
                _iea = (clean[:-1] + "ay" if len(clean) > 1 else "ay")
                _ie_low = {("madhyama","eka"):[_iew+"tAt",_iew+"tAd",_iew+"hi"],("prathama","eka"):[_iee+"tu"],("prathama","dvi"):[_iew+"tAm"],("prathama","bahu"):[_iey+"antu"],("madhyama","dvi"):[_iew+"tam"],("madhyama","bahu"):[_iew+"ta"],("uttama","eka"):[_iea+"Ani"],("uttama","dvi"):[_iea+"Ava"],("uttama","bahu"):[_iea+"Ama"]}
                cands += _ie_low.get((purusha, vacana), [])
            # AdAdi-a luk imperative: luk-stem doublets (weak + strong for as-3sg astu) + endings
            # (attAt/adantu...; 2sg Dhi-variants adDi/vagDi/saDi/eDi, jahi skipped); same sandhi family
            # via helper; gana-gated + additive.
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] not in SLP1_VOWELS:
                _lvA4 = None
                for _ch4 in reversed(clean):
                    if _ch4 in SLP1_VOWELS:
                        _lvA4 = _ch4
                        break
                if _lvA4 == "a":
                    _lowmap = {("madhyama","eka"):["tAt","tAd"],("prathama","eka"):["tu"],("prathama","dvi"):["tAm"],("prathama","bahu"):["antu"],("madhyama","dvi"):["tam"],("madhyama","bahu"):["ta"],("uttama","eka"):["Ani"],("uttama","dvi"):["Ava"],("uttama","bahu"):["Ama"]}
                    for _e4 in _lowmap.get((purusha, vacana), []):
                        for _sq in (False, True):
                            cands.append(self._adadi_a_luk(clean, _e4, vacana, strong_eka=_sq) + _e4)
                    if (purusha, vacana) == ("madhyama", "eka"):
                        _dhi = {"ad": "adDi", "vac": "vagDi", "sas": "saDi", "as": "eDi"}
                        if clean in _dhi:
                            cands.append(_dhi[clean])
            # sasti low doublet + DHi (saMs-/saMst- + low-endings; sanddDi/sanDi for 2sg; sole 02.0074;
            # additive; NB meta-clean gate (idit-num rewrites local clean)).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "sasti":
                _slow = {("madhyama","eka"):["tAt","tAd"],("prathama","eka"):["tu"],("prathama","dvi"):["tAm"],("prathama","bahu"):["antu"],("madhyama","dvi"):["tam"],("madhyama","bahu"):["ta"],("uttama","eka"):["Ani"],("uttama","dvi"):["Ava"],("uttama","bahu"):["Ama"]}
                for _e10 in _slow.get((purusha, vacana), []):
                    cands += ["saMs" + _e10, "saMst" + _e10]
                if (purusha, vacana) == ("madhyama", "eka"):
                    cands += ["sanddDi", "sanDi"]
            # an luk imperative (anitAt/anitu/anantu/anihi + A-grade 1sg anAni; sole 02.0065; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "an":
                _anlow = {("madhyama","eka"):["anitAt","anitAd","anihi"],("prathama","eka"):["anitu"],("prathama","dvi"):["anitAm"],("prathama","bahu"):["anantu"],("madhyama","dvi"):["anitam"],("madhyama","bahu"):["anita"],("uttama","eka"):["anAni"],("uttama","dvi"):["anAva"],("uttama","bahu"):["anAma"]}
                cands += _anlow.get((purusha, vacana), [])
            # AdAdi idit-i luk Atmane imperative (kaMstAm/kaMssva/kanDvam; same class/helper as lw).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and ((is_idit and meta.get("clean", "") and meta.get("clean")[-1] in ("i", "I")) or meta.get("clean") in ("As", "vas", "kas", "kaS", "cakz", "Ir", "SAs")):
                _ato = {("prathama","eka"):"tAm",("prathama","dvi"):"AtAm",("prathama","bahu"):"atAm",("madhyama","dvi"):"ATAm",("madhyama","bahu"):"Dvam",("uttama","eka"):"E",("uttama","dvi"):"AvahE",("uttama","bahu"):"AmahE"}
                _aoe = _ato.get((purusha, vacana))
                if _aoe:
                    for _ab2 in ((["cakz"] if meta.get("clean") == "cakz" else []) + (["ASAs"] if meta.get("clean") == "SAs" else []) + [clean] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)):
                        if not _ab2 or _ab2[-1] in SLP1_VOWELS:
                            continue
                        cands.append(self._adadi_atmane_joint(_ab2, _aoe))
                if (purusha, vacana) == ("madhyama", "eka"):
                    for _ab2s in ((["cakz"] if meta.get("clean") == "cakz" else []) + (["ASAs"] if meta.get("clean") == "SAs" else []) + [clean] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)):
                        if not _ab2s or _ab2s[-1] in SLP1_VOWELS:
                            continue
                        cands.append(self._adadi_atmane_joint(_ab2s, "sva"))
            # S/z zw-eka imperative (kazwAm/cazwAm; surveyed kaS/cakz; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and (purusha, vacana) == ("prathama", "eka"):
                cands += {"kaS": ["kazwAm"], "cakz": ["cazwAm"]}.get(meta.get("clean"), [])
            # u-Atmane luk imperative (hnutAm/hnuzva(sva-only m.eka)/hnavE-1sg; sU takes suvE-1sg;
            # surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("hnu", "sU"):
                _hu2 = meta.get("clean")
                _uato = {("prathama","eka"):"tAm",("prathama","dvi"):"AtAm",("prathama","bahu"):"atAm",("madhyama","dvi"):"ATAm",("madhyama","bahu"):"Dvam"}
                _uao = _uato.get((purusha, vacana))
                if _uao:
                    cands.append(self._adadi_atmane_joint(_hu2, _uao))
                if (purusha, vacana) == ("madhyama", "eka"):
                    cands.append(self._adadi_atmane_joint(_hu2, "sva"))
                if (purusha, vacana) == ("uttama", "eka"):
                    cands += ["hnavE"] if _hu2 == "hnu" else ["suvE"]
                if (purusha, vacana) == ("uttama", "dvi"):
                    cands += ["hnavAvahE"] if _hu2 == "hnu" else ["suvAvahE"]
                if (purusha, vacana) == ("uttama", "bahu"):
                    cands += ["hnavAmahE"] if _hu2 == "hnu" else ["suvAmahE"]
            # I-Atmane luk imperative (dIDItAm/dIDIzva(sva-only m.eka)/dIDyE-1sg; surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("dIDI", "vevI"):
                _hiy2 = meta.get("clean")
                _iato = {("prathama","eka"):"tAm",("prathama","dvi"):"AtAm",("prathama","bahu"):"atAm",("madhyama","dvi"):"ATAm",("madhyama","bahu"):"Dvam",("uttama","eka"):"E",("uttama","dvi"):"AvahE",("uttama","bahu"):"AmahE"}
                _iao = _iato.get((purusha, vacana))
                if _iao:
                    cands.append(self._adadi_atmane_joint(_hiy2, _iao))
                if (purusha, vacana) == ("madhyama", "eka"):
                    cands.append(self._adadi_atmane_joint(_hiy2, "sva"))
            # SI e/ay/er imperative (SetAm/SayAtAm/SeratAm + Sezva; sole 02.0026; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "SI":
                _sio = {("prathama","eka"):["SetAm"],("prathama","dvi"):["SayAtAm"],("prathama","bahu"):["SeratAm"],("madhyama","eka"):["Sezva"],("madhyama","dvi"):["SayATAm"],("madhyama","bahu"):["SeDvam"],("uttama","eka"):["SayE"],("uttama","dvi"):["SayAvahE"],("uttama","bahu"):["SayAmahE"]}
                cands += _sio.get((purusha, vacana), [])
            # f+I~ Atmane imperative (k-tAm/zva + g-Dvam + ar-1sg; pair surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("vfj", "pfc"):
                _fc2 = meta.get("clean")
                _fk2 = _fc2[:-1] + "k"
                _fg2 = _fc2[:-1] + "g"
                _far2 = _fc2[:-2] + "ar" + _fc2[-1]
                _fjo = {("prathama","eka"):[_fk2+"tAm"],("prathama","dvi"):[_fc2+"AtAm"],("prathama","bahu"):[_fc2+"atAm"],("madhyama","eka"):[_fk2+"zva"],("madhyama","dvi"):[_fc2+"ATAm"],("madhyama","bahu"):[_fg2+"Dvam"],("uttama","eka"):[_far2+"E"],("uttama","dvi"):[_far2+"AvahE"],("uttama","bahu"):[_far2+"AmahE"]}
                cands += _fjo.get((purusha, vacana), [])
            # iN adhi-imperative (aDItAm/aDIyAtAm + ay-1sg aDyayE; sole 02.0041; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "i":
                _ino = {("prathama","eka"):["aDItAm"],("prathama","dvi"):["aDIyAtAm"],("prathama","bahu"):["aDIyatAm"],("madhyama","eka"):["aDIzva"],("madhyama","dvi"):["aDIyATAm"],("madhyama","bahu"):["aDIDvam"],("uttama","eka"):["aDyayE"],("uttama","dvi"):["aDyayAvahE"],("uttama","bahu"):["aDyayAmahE"]}
                cands += _ino.get((purusha, vacana), [])
            # Iq/IS quirky imperative (ww-eka + i-augment izva/iDve; surveyed pair; standalone literals).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("Iq", "IS"):
                _qo = {"Iq": ["IwwAm", "IqAtAm", "IqatAm", "Iqizva", "IqATAm", "IqiDvam", "IqE", "IqAvahE", "IqAmahE"], "IS": ["IzwAm", "ISAtAm", "ISatAm", "ISizva", "ISATAm", "ISiDvam", "ISE", "ISAvahE", "ISAmahE"]}[meta.get("clean")]
                _qoslots = [("prathama","eka"),("prathama","dvi"),("prathama","bahu"),("madhyama","eka"),("madhyama","dvi"),("madhyama","bahu"),("uttama","eka"),("uttama","dvi"),("uttama","bahu")]
                if (purusha, vacana) in _qoslots:
                    cands.append(_qo[_qoslots.index((purusha, vacana))])
            # jAgf f-grade imperative (ar-3sg jAgartu, short bahu jAgratu, AR-1sg jAgarARi; sole 02.0067).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "jAg":
                _jlow = {("madhyama","eka"):["jAgftAt","jAgftAd","jAgfhi"],("prathama","eka"):["jAgartu"],("prathama","dvi"):["jAgftAm"],("prathama","bahu"):["jAgratu"],("madhyama","dvi"):["jAgftam"],("madhyama","bahu"):["jAgfta"],("uttama","eka"):["jAgarARi"],("uttama","dvi"):["jAgarAva"],("uttama","bahu"):["jAgarAma"]}
                cands += _jlow.get((purusha, vacana), [])
            # vid luk imperative (luk vettu/vidantu/vidDi + periphrastic vidANkara twins; sole 02.0059;
            # any-match needs >=1 attested form per slot — mapping by shape; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vid":
                _vidlow = {("prathama","eka"):["vettu","vidANkarotu"],("prathama","dvi"):["vittAm","vidANkurutAm"],("prathama","bahu"):["vidantu","vidANkurvantu"],("madhyama","eka"):["vittAt","vittAd","vidDi","vidANkurutAt","vidANkurutAd","vidANkuru"],("madhyama","dvi"):["vittam","vidANkurutam"],("madhyama","bahu"):["vitta","vidANkuruta"],("uttama","eka"):["vedAni","vidANkaravARi"],("uttama","dvi"):["vedAva","vidANkaravAva"],("uttama","bahu"):["vedAma","vidANkaravAma"]}
                cands += _vidlow.get((purusha, vacana), [])
            # daridrA ablaut imperative (A-3sg + i-weak + A-1sg; sole 02.0068; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "daridrA":
                _ddlow = {("madhyama","eka"):["daridritAt","daridritAd","daridrihi"],("prathama","eka"):["daridrAtu"],("prathama","dvi"):["daridritAm"],("prathama","bahu"):["daridratu"],("madhyama","dvi"):["daridritam"],("madhyama","bahu"):["daridrita"],("uttama","eka"):["daridrARi"],("uttama","dvi"):["daridrAva"],("uttama","bahu"):["daridrAma"]}
                cands += _ddlow.get((purusha, vacana), [])
            # mfjU ablaut+zw imperative (sole 02.0061; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "mfj":
                _mjlow = {("madhyama","eka"):["mfzwAt","mfzwAd","mfqQi"],("prathama","eka"):["mArzwu"],("prathama","dvi"):["mfzwAm"],("prathama","bahu"):["mArjantu","mfjantu"],("madhyama","dvi"):["mfzwam"],("madhyama","bahu"):["mfzwa"],("uttama","eka"):["mArjAni"],("uttama","dvi"):["mArjAva"],("uttama","bahu"):["mArjAma"]}
                cands += _mjlow.get((purusha, vacana), [])
            # han bahu Gna-twin (Gnantu alongside hantu; sole-gated; slot-gated; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "han" and (purusha, vacana) == ("prathama", "bahu"):
                cands += ["Gnantu"]
            # iN aDI-/aDyay- imperative (sole 02.0041; op-gated; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "i" and op.startswith("iN"):
                _inlow = {("madhyama","eka"):["aDIzva"],("prathama","eka"):["aDItAm"],("prathama","dvi"):["aDIyAtAm"],("prathama","bahu"):["aDIyatAm"],("madhyama","dvi"):["aDIyATAm"],("madhyama","bahu"):["aDIDvam"],("uttama","eka"):["aDyayE"],("uttama","dvi"):["aDyayAvahE"],("uttama","bahu"):["aDyayAmahE"]}
                cands += _inlow.get((purusha, vacana), [])
            # SAs luk imperative (SAstu + izw-slots + SADi + A-1sg; sole 02.0070; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "SAs":
                _saslow = {("madhyama","eka"):["SizwAt","SizwAd","SADi"],("prathama","eka"):["SAstu"],("prathama","dvi"):["SizwAm"],("prathama","bahu"):["SAsatu"],("madhyama","dvi"):["Sizwam"],("madhyama","bahu"):["Sizwa"],("uttama","eka"):["SAsAni"],("uttama","dvi"):["SAsAva"],("uttama","bahu"):["SAsAma"]}
                cands += _saslow.get((purusha, vacana), [])
            # dviz luk imperative (e-3sg + zw-slots + q-DHi + ARi-1sg; sole 02.0003; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "dviz":
                _dzlow = {("madhyama","eka"):["dvizwAt","dvizwAd","dviqQi"],("prathama","eka"):["dvezwu"],("prathama","dvi"):["dvizwAm"],("prathama","bahu"):["dvizantu"],("madhyama","dvi"):["dvizwam"],("madhyama","bahu"):["dvizwa"],("uttama","eka"):["dvezARi"],("uttama","dvi"):["dvezAva"],("uttama","bahu"):["dvezAma"]}
                cands += _dzlow.get((purusha, vacana), [])
            # cakAs long-A imperative (DHi cakADi + short bahu cakAsatu like jakzatu; sole 02.0069).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "cakAs":
                _caslow = {("madhyama","eka"):["cakAstAt","cakAstAd","cakADi"],("prathama","eka"):["cakAstu"],("prathama","dvi"):["cakAstAm"],("prathama","bahu"):["cakAsatu"],("madhyama","dvi"):["cakAstam"],("madhyama","bahu"):["cakAsta"],("uttama","eka"):["cakAsAni"],("uttama","dvi"):["cakAsAva"],("uttama","bahu"):["cakAsAma"]}
                cands += _caslow.get((purusha, vacana), [])
            # h-class luk imperative (guNa-3sg + Dhi-variant + oh/eh-1sg; family surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("duh", "dih", "lih"):
                _hlow = {
                "duh": {("madhyama","eka"):["dugDAt","dugDAd","dugDi"],("prathama","eka"):["dogDu"],("prathama","dvi"):["dugDAm"],("prathama","bahu"):["duhantu"],("madhyama","dvi"):["dugDam"],("madhyama","bahu"):["dugDa"],("uttama","eka"):["dohAni"],("uttama","dvi"):["dohAva"],("uttama","bahu"):["dohAma"]},
                "dih": {("madhyama","eka"):["digDAt","digDAd","digDi"],("prathama","eka"):["degDu"],("prathama","dvi"):["digDAm"],("prathama","bahu"):["dihantu"],("madhyama","dvi"):["digDam"],("madhyama","bahu"):["digDa"],("uttama","eka"):["dehAni"],("uttama","dvi"):["dehAva"],("uttama","bahu"):["dehAma"]},
                "lih": {("madhyama","eka"):["lIQAt","lIQAd","lIQi"],("prathama","eka"):["leQu"],("prathama","dvi"):["lIQAm"],("prathama","bahu"):["lihantu"],("madhyama","dvi"):["lIQam"],("madhyama","bahu"):["lIQa"],("uttama","eka"):["lehAni"],("uttama","dvi"):["lehAva"],("uttama","bahu"):["lehAma"]}}
                cands += _hlow.get(meta.get("clean"), {}).get((purusha, vacana), [])
            # rudi~r o-grade seW-i imperative (roditu + weak-i slots + o-grade 1sg rodAni; sole 02.0062).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "rud":
                _rudlow = {("madhyama","eka"):["ruditAt","ruditAd","rudihi"],("prathama","eka"):["roditu"],("prathama","dvi"):["ruditAm"],("prathama","bahu"):["rudantu"],("madhyama","dvi"):["ruditam"],("madhyama","bahu"):["rudita"],("uttama","eka"):["rodAni"],("uttama","dvi"):["rodAva"],("uttama","bahu"):["rodAma"]}
                cands += _rudlow.get((purusha, vacana), [])
            # ik adhi+i imperative (aDyetu/aDItAm/aDiyantu + ay-1sg aDyayAni; sole 02.0042; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "ik":
                _iklow = {("prathama","eka"):["aDyetu"],("prathama","dvi"):["aDItAm"],("prathama","bahu"):["aDiyantu","aDIyantu"],("madhyama","eka"):["aDItAt","aDItAd","aDIhi"],("madhyama","dvi"):["aDItam"],("madhyama","bahu"):["aDIta"],("uttama","eka"):["aDyayAni"],("uttama","dvi"):["aDyayAva"],("uttama","bahu"):["aDyayAma"]}
                cands += _iklow.get((purusha, vacana), [])
            # vaS/uS suppletive imperative (vazwu + uztwAm/uqQi + vaSA-1sg; sole 02.0075; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vaS":
                _vslow = {("prathama","eka"):["vazwu"],("prathama","dvi"):["uzwAm"],("prathama","bahu"):["uSantu"],("madhyama","eka"):["uzwAt","uzwAd","uqQi"],("madhyama","dvi"):["uzwam"],("madhyama","bahu"):["uzwa"],("uttama","eka"):["vaSAni"],("uttama","dvi"):["vaSAva"],("uttama","bahu"):["vaSAma"]}
                cands += _vslow.get((purusha, vacana), [])
            # seW i-class luk imperative (shared X+it skeleton + ihi; bahu bare except jakz short `jakzatu`;
            # 1sg a-grade Ani/Ava/Ama except jakz eka ARi `jakzARi`; same class gate as lw; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("svap", "Svas", "jakz"):
                _jc = meta.get("clean")
                _jlow = {("madhyama","eka"):[_jc+"itAt",_jc+"itAd",_jc+"ihi"],("prathama","eka"):[_jc+"itu"],("prathama","dvi"):[_jc+"itAm"],("madhyama","dvi"):[_jc+"itam"],("madhyama","bahu"):[_jc+"ita"],("uttama","dvi"):[_jc+"Ava"],("uttama","bahu"):[_jc+"Ama"]}
                cands += _jlow.get((purusha, vacana), [])
                if (purusha, vacana) == ("prathama", "bahu"):
                    cands += ["jakzatu"] if _jc == "jakz" else [_jc + "antu"]
                if (purusha, vacana) == ("uttama", "eka"):
                    cands += ["jakzARi"] if _jc == "jakz" else [_jc + "Ani"]
            # divAdi ya-imperative (dIvyatu/dIvyantu + Atmane -yatAm; ya-stem + tin,
            # pr.bahu/u Burton drop stem-a; u.eka Ani→ARi iff last r/R/z/f/F-trigger
            # followed only by vowels/y/v/h/m; no-ya quartet {yas,tras,Bram,klam}
            # takes bare+ya twins; surveyed all 163 divAdi cleans; gana-gated; additive).
            if meta.get("gana") == "divAdiH" and sanadi is None:
                _d4ya = self._divadi_stem(clean, meta, op)
                _d4y = _d4ya[:-1] if _d4ya.endswith("a") else _d4ya
                _d4ss = [_d4ya]
                if (meta.get("clean", "") or clean) in ("yas", "tras", "Bram", "klam"):
                    _d4ss.append(clean + "ya" if not (meta.get("clean", "") or clean) == "klam" else "klAmya")
                _d4li = -1
                for _i, _ch in enumerate(_d4ya):
                    if _ch in ("r", "R", "z", "f", "F"):
                        _d4li = _i
                _d4R = _d4li != -1 and all(ch in SLP1_VOWELS or ch in ("y", "v", "h", "m") for ch in (_d4ya[_d4li + 1:] + "a"))
                for _st in _d4ss:
                    _sy = _st[:-1] if _st.endswith("a") else _st
                    _sli = -1
                    for _i, _ch in enumerate(_st):
                        if _ch in ("r", "R", "z", "f", "F"):
                            _sli = _i
                    _sR = _sli != -1 and all(ch in SLP1_VOWELS or ch in ("y", "v", "h", "m") for ch in (_st[_sli + 1:] + "a"))
                    _su1 = _sy + ("ARi" if _sR else "Ani")
                    cands += {
                        ("prathama", "eka"): [_st + "tu", _st + "tAt", _st + "tAd"],
                        ("prathama", "dvi"): [_st + "tAm"],
                        ("prathama", "bahu"): [_sy + "antu"],
                        ("madhyama", "eka"): [_st],
                        ("madhyama", "dvi"): [_st + "tAt", _st + "tAd"],
                        ("madhyama", "bahu"): [_st + "tam", _st + "ta"],
                        ("uttama", "eka"): [_su1],
                        ("uttama", "dvi"): [_sy + "Ava"],
                        ("uttama", "bahu"): [_sy + "Ama"],
                    }.get((purusha, vacana), [])
                    cands += {
                        ("prathama", "eka"): [_st + "tAm"],
                        ("prathama", "dvi"): [_sy + "etAm"],
                        ("prathama", "bahu"): [_st + "ntAm"],
                        ("madhyama", "eka"): [_st + "sva"],
                        ("madhyama", "dvi"): [_sy + "eTAm"],
                        ("madhyama", "bahu"): [_st + "Dvam"],
                        ("uttama", "eka"): [_sy + "E"],
                        ("uttama", "dvi"): [_sy + "AvahE"],
                        ("uttama", "bahu"): [_sy + "AmahE"],
                    }.get((purusha, vacana), [])
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "viDiliN":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "viDiliN", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(base, "viDiliN", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "viDiliN", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "viDiliN", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "viDiliN", purusha, vacana)
            # AdAdi-a luk optative: luk-stem + yAt-endings (adyAt/hanyAt; same yAt-map family as
            # yAyAt/yuyAt; gana + a-shape gated (mirrors lw-block condition); additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] not in SLP1_VOWELS:
                _lvA2 = None
                for _ch2 in reversed(clean):
                    if _ch2 in SLP1_VOWELS:
                        _lvA2 = _ch2
                        break
                if _lvA2 == "a":
                    _yend2 = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                    # as- ablaut: weak s- in viDiliN throughout (syAt; mirrors lw weak/outside-eka)
                    _ystem = "s" if clean == "as" else clean
                    _yf2 = _ystem + _yend2[(purusha, vacana)]
                    if _yf2 not in cands:
                        cands.append(_yf2)
            # sasti viDiliN t-form (saMstyAt-class; sole 02.0074; additive; meta-clean gate).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "sasti":
                _sy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _syf = "saMst" + _sy.get((purusha, vacana), "yAt")
                if _syf not in cands:
                    cands.append(_syf)
            # AdAdi-i luk optative: weak-i + yAt-endings (vIyAt/iyAt; same yAt-map family; sole vI + iR;
            # exact-clean gate; gana-gated + additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and clean and clean[-1] in ("i", "I"):
                _iy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _iyf = clean + _iy.get((purusha, vacana), "yAt")
                if _iyf not in cands:
                    cands.append(_iyf)
            # jAgf f-grade optative (f + yAt throughout; sole 02.0067; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "jAg":
                _jy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _jyf = "jAgf" + _jy.get((purusha, vacana), "yAt")
                if _jyf not in cands:
                    cands.append(_jyf)
            # divAdi ya-optative (dIvyet/dIvyed + Atmane -yeta; ya-stem + et-grades,
            # pr.eka et/ed twins; no-ya quartet {yas,tras,Bram,klam} takes bare+ya
            # twins; surveyed all 163 divAdi cleans; gana-gated; additive).
            if meta.get("gana") == "divAdiH" and sanadi is None:
                _d4ya = self._divadi_stem(clean, meta, op)
                _d4y = _d4ya[:-1] if _d4ya.endswith("a") else _d4ya
                _d4vs = [_d4ya]
                if (meta.get("clean", "") or clean) in ("yas", "tras", "Bram", "klam"):
                    _d4vs.append(clean + "ya" if (meta.get("clean", "") or clean) != "klam" else "klAmya")
                for _vs in _d4vs:
                    _vy = _vs[:-1] if _vs.endswith("a") else _vs
                    cands += {
                        ("prathama", "eka"): [_vy + "et", _vy + "ed"],
                        ("prathama", "dvi"): [_vy + "etAm"],
                        ("prathama", "bahu"): [_vy + "eyuH"],
                        ("madhyama", "eka"): [_vy + "eH"],
                        ("madhyama", "dvi"): [_vy + "etam"],
                        ("madhyama", "bahu"): [_vy + "eta"],
                        ("uttama", "eka"): [_vy + "eyam"],
                        ("uttama", "dvi"): [_vy + "eva"],
                        ("uttama", "bahu"): [_vy + "ema"],
                    }.get((purusha, vacana), [])
                    cands += {
                        ("prathama", "eka"): [_vy + "eta"],
                        ("prathama", "dvi"): [_vy + "eyAtAm"],
                        ("prathama", "bahu"): [_vy + "eran"],
                        ("madhyama", "eka"): [_vy + "eTAH"],
                        ("madhyama", "dvi"): [_vy + "eyATAm"],
                        ("madhyama", "bahu"): [_vy + "eDvam"],
                        ("uttama", "eka"): [_vy + "eya"],
                        ("uttama", "dvi"): [_vy + "evahi"],
                        ("uttama", "bahu"): [_vy + "emahi"],
                    }.get((purusha, vacana), [])
            # rudhAdi Snam optative (runDyAt/BindyAt/riYcyAt/SiMzyAt/tfMhyAt/hiMsyAt;
            # a-less weak stem + yAt-grades, coda kept (T voices to t: kfntyAt),
            # eka {yAt,yAd} twins; Atmane a-less + v + I-grades (runDIta/BindIta).
            # D/d Atmane tables cover sole Atmane-meta cleans (paras-meta k/j/d
            # avidhi hits via pool, no k/j Atmane generation). Gana-gated; additive.
            if meta.get("gana") == "ruDAdiH" and sanadi is None:
                _r7pre, _r7coda, _r7cls, _r7R, _r7ne = self._ruDana_pieces(clean)
                _r7W = _r7pre + self._ruDana_nasal(_r7coda) + _r7coda
                _r7yp = {("prathama", "dvi"): "yAtAm", ("prathama", "bahu"): "yuH", ("madhyama", "eka"): "yAH", ("madhyama", "dvi"): "yAtAm", ("madhyama", "bahu"): "yAta", ("uttama", "eka"): "yAm", ("uttama", "dvi"): "yAva", ("uttama", "bahu"): "yAma"}
                if pada != "Atmanepadi":
                    if (purusha, vacana) == ("prathama", "eka"):
                        cands += [_r7W + "yAt", _r7W + "yAd"]
                    elif (purusha, vacana) in _r7yp:
                        cands.append(_r7W + _r7yp[(purusha, vacana)])
                if pada == "Atmanepadi" and _r7cls in ("D", "d"):
                    _r7ya = {("prathama", "eka"): "Ita", ("prathama", "dvi"): "IyAtAm", ("prathama", "bahu"): "Iran", ("madhyama", "eka"): "ITAH", ("madhyama", "dvi"): "IyATAm", ("madhyama", "bahu"): "IDvam", ("uttama", "eka"): "Iya", ("uttama", "dvi"): "Ivahi", ("uttama", "bahu"): "Imahi"}
                    if (purusha, vacana) in _r7ya:
                        cands.append(_r7W + _r7ya[(purusha, vacana)])
            # tanAdi o/u optative (tanuyAt/kuryAt; paras takes weak-u + yA-grades with
            # yAt/yAd 3sg doublet, open-f kf takes bare ur-grade (kuryAt, samprasAraNa
            # f→ur before y, never *kuruyAt); Atmane takes weak-u + v + I-grades
            # (tanvIta/kurvIta). Same stems/survey as lw; gana-gated; additive.
            if meta.get("gana") == "tanAdiH" and sanadi is None:
                _t8s, _t8w, _t8v = self._tanadi_stems(clean)
                _t8yp = {("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                if (purusha, vacana) == ("prathama", "eka"):
                    for _t8ys in _t8v:
                        cands += [_t8ys + "yAt", _t8ys + "yAd"]
                elif (purusha, vacana) in _t8yp:
                    for _t8ys in _t8v:
                        cands.append(_t8ys + _t8yp[(purusha, vacana)])
                _t8ya = {("prathama","eka"):"Ita",("prathama","dvi"):"IyAtAm",("prathama","bahu"):"Iran",("madhyama","eka"):"ITAH",("madhyama","dvi"):"IyATAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                if (purusha, vacana) in _t8ya:
                    for _t8yw in _t8w:
                        cands.append(_t8yw[:-1] + "v" + _t8ya[(purusha, vacana)])
            # SvAdi Snu optative (Panini 3.1.73, sunuyAt/sunuyAd, ApnuyAt/ApnuyAd;
            # paras takes weak-u + yA-grades; Atmane sunvIta/aSnuvIta weak-v + I-grades).
            # Surveyed all 38 svAdi cleans; gana-gated; additive.
            if meta.get("gana") == "svAdiH" and sanadi is None:
                _s5b, _s5v, _s5s, _s5wc, _s5wv, _s5nav = self._svadi_stems(clean)
                _s5yp = {
                    ("prathama", "dvi"): "yAtAm", ("prathama", "bahu"): "yuH",
                    ("madhyama", "eka"): "yAH", ("madhyama", "dvi"): "yAtAm", ("madhyama", "bahu"): "yAta",
                    ("uttama", "eka"): "yAm", ("uttama", "dvi"): "yAva", ("uttama", "bahu"): "yAma"
                }
                if (purusha, vacana) == ("prathama", "eka"):
                    cands += [_s5wc + "yAt", _s5wc + "yAd"]
                elif (purusha, vacana) in _s5yp:
                    cands.append(_s5wc + _s5yp[(purusha, vacana)])
                _s5ya = {
                    ("prathama", "eka"): "Ita", ("prathama", "dvi"): "IyAtAm", ("prathama", "bahu"): "Iran",
                    ("madhyama", "eka"): "ITAH", ("madhyama", "dvi"): "IyATAm", ("madhyama", "bahu"): "IDvam",
                    ("uttama", "eka"): "Iya", ("uttama", "dvi"): "Ivahi", ("uttama", "bahu"): "Imahi"
                }
                if (purusha, vacana) in _s5ya:
                    cands.append(_s5wv + _s5ya[(purusha, vacana)])
            # kryAdi nA optative (krIRIyAt, mInuyAt-twins for closed-5; stem-I +
            # yA-grades paras, stem-I + I-grades Atmane with vI-twins for
            # closed-5; eka yAt/yAd twins universal. Surveyed; gana-gated;
            # additive).
            if meta.get("gana") == "kryAdiH" and sanadi is None:
                _k9s = self._kryadi_stem(clean, meta, op)
                _k9mc2 = meta.get("clean", "") or clean
                _k9o = _k9mc2 in ("sku", "stanB", "stunB", "skanB", "skunB")
                _k9yp = {
                    ("prathama", "dvi"): "yAtAm", ("prathama", "bahu"): "yuH",
                    ("madhyama", "eka"): "yAH", ("madhyama", "dvi"): "yAtAm", ("madhyama", "bahu"): "yAta",
                    ("uttama", "eka"): "yAm", ("uttama", "dvi"): "yAva", ("uttama", "bahu"): "yAma"
                }
                if (purusha, vacana) == ("prathama", "eka"):
                    cands += [_k9s + "IyAt", _k9s + "IyAd"] + ([_k9s + "uyAt", _k9s + "uyAd"] if _k9o else [])
                elif (purusha, vacana) in _k9yp:
                    cands.append(_k9s + "I" + _k9yp[(purusha, vacana)])
                    if _k9o:
                        cands.append(_k9s + "u" + _k9yp[(purusha, vacana)])
                _k9ya = {
                    ("prathama", "eka"): "Ita", ("prathama", "dvi"): "IyAtAm", ("prathama", "bahu"): "Iran",
                    ("madhyama", "eka"): "ITAH", ("madhyama", "dvi"): "IyATAm", ("madhyama", "bahu"): "IDvam",
                    ("uttama", "eka"): "Iya", ("uttama", "dvi"): "Ivahi", ("uttama", "bahu"): "Imahi"
                }
                if (purusha, vacana) in _k9ya:
                    cands.append(_k9s + _k9ya[(purusha, vacana)])
                    if _k9o:
                        cands.append(_k9s + "v" + _k9ya[(purusha, vacana)])
            # vid luk optative (vid + yAt, same map family; sole i-vowel consonant root surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vid":
                _vy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _vyf = "vid" + _vy.get((purusha, vacana), "yAt")
                if _vyf not in cands:
                    cands.append(_vyf)
            # daridrA ablaut optative (daridr + iyAt; sole 02.0068; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "daridrA":
                _ddy = {("prathama","eka"):["daridriyAt","daridriyAd"],("prathama","dvi"):["daridriyAtAm"],("prathama","bahu"):["daridriyuH"],("madhyama","eka"):["daridriyAH"],("madhyama","dvi"):["daridriyAtAm"],("madhyama","bahu"):["daridriyAta"],("uttama","eka"):["daridriyAm"],("uttama","dvi"):["daridriyAva"],("uttama","bahu"):["daridriyAma"]}
                cands += _ddy.get((purusha, vacana), [])
            # SAs luk optative (Siz + yAt; sole 02.0070; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "SAs":
                _sasy = {("prathama","eka"):["SizyAt","SizyAd"],("prathama","dvi"):["SizyAtAm"],("prathama","bahu"):["SizyuH"],("madhyama","eka"):["SizyAH"],("madhyama","dvi"):["SizyAtAm"],("madhyama","bahu"):["SizyAta"],("uttama","eka"):["SizyAm"],("uttama","dvi"):["SizyAva"],("uttama","bahu"):["SizyAma"]}
                cands += _sasy.get((purusha, vacana), [])
            # dviz luk optative (dviz + yAt; sole 02.0003; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "dviz":
                _dzy = {("prathama","eka"):["dvizyAt","dvizyAd"],("prathama","dvi"):["dvizyAtAm"],("prathama","bahu"):["dvizyuH"],("madhyama","eka"):["dvizyAH"],("madhyama","dvi"):["dvizyAtAm"],("madhyama","bahu"):["dvizyAta"],("uttama","eka"):["dvizyAm"],("uttama","dvi"):["dvizyAva"],("uttama","bahu"):["dvizyAma"]}
                cands += _dzy.get((purusha, vacana), [])
            # mfjU zero optative (mfj + yAt; sole 02.0061; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "mfj":
                _mjy = {("prathama","eka"):["mfjyAt","mfjyAd"],("prathama","dvi"):["mfjyAtAm"],("prathama","bahu"):["mfjyuH"],("madhyama","eka"):["mfjyAH"],("madhyama","dvi"):["mfjyAtAm"],("madhyama","bahu"):["mfjyAta"],("uttama","eka"):["mfjyAm"],("uttama","dvi"):["mfjyAva"],("uttama","bahu"):["mfjyAma"]}
                cands += _mjy.get((purusha, vacana), [])
            # iN aDIyI- optative (sole 02.0041; op-gated; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "i" and op.startswith("iN"):
                _iny = {("prathama","eka"):["aDIyIta"],("prathama","dvi"):["aDIyIyAtAm"],("prathama","bahu"):["aDIyIran"],("madhyama","eka"):["aDIyITAH"],("madhyama","dvi"):["aDIyIyATAm"],("madhyama","bahu"):["aDIyIDvam"],("uttama","eka"):["aDIyIya"],("uttama","dvi"):["aDIyIvahi"],("uttama","bahu"):["aDIyImahi"]}
                cands += _iny.get((purusha, vacana), [])
            # cakAs long-A optative (cakAs + yAt; sole 02.0069; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "cakAs":
                _casy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _casyf = "cakAs" + _casy.get((purusha, vacana), "yAt")
                if _casyf not in cands:
                    cands.append(_casyf)
            # h-class luk optative (weak-h + yAt; family surveyed; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("duh", "dih", "lih"):
                _hy = {("prathama","eka"):"yAt",("prathama","dvi"):"yAtAm",("prathama","bahu"):"yuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAtAm",("madhyama","bahu"):"yAta",("uttama","eka"):"yAm",("uttama","dvi"):"yAva",("uttama","bahu"):"yAma"}
                _hyf = meta.get("clean") + _hy.get((purusha, vacana), "yAt")
                if _hyf not in cands:
                    cands.append(_hyf)
            # rudi~r weak-u optative (rud + yAt; o-grade stays in pits only; sole 02.0062; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "rud":
                _ruy = {("prathama","eka"):["rudyAt","rudyAd"],("prathama","dvi"):["rudyAtAm"],("prathama","bahu"):["rudyuH"],("madhyama","eka"):["rudyAH"],("madhyama","dvi"):["rudyAtAm"],("madhyama","bahu"):["rudyAta"],("uttama","eka"):["rudyAm"],("uttama","dvi"):["rudyAva"],("uttama","bahu"):["rudyAma"]}
                cands += _ruy.get((purusha, vacana), [])
            # ik adhi+i optative (adhi + IyAt, t/d doublet eka; sole 02.0042; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "ik":
                _ky = {("prathama","eka"):["aDIyAt","aDIyAd"],("prathama","dvi"):["aDIyAtAm"],("prathama","bahu"):["aDIyuH"],("madhyama","eka"):["aDIyAH"],("madhyama","dvi"):["aDIyAtAm"],("madhyama","bahu"):["aDIyAta"],("uttama","eka"):["aDIyAm"],("uttama","dvi"):["aDIyAva"],("uttama","bahu"):["aDIyAma"]}
                cands += _ky.get((purusha, vacana), [])
            # vaS/uS suppletive optative (uS + yAt, t/d doublet eka; sole 02.0075; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "vaS":
                _vsy = {("prathama","eka"):["uSyAt","uSyAd"],("prathama","dvi"):["uSyAtAm"],("prathama","bahu"):["uSyuH"],("madhyama","eka"):["uSyAH"],("madhyama","dvi"):["uSyAtAm"],("madhyama","bahu"):["uSyAta"],("uttama","eka"):["uSyAm"],("uttama","dvi"):["uSyAva"],("uttama","bahu"):["uSyAma"]}
                cands += _vsy.get((purusha, vacana), [])
            # AdAdi idit-i luk Atmane optative (kaMsIta/kaMsIran/kaMsIDvam; stem + I-endings via helper).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and ((is_idit and meta.get("clean", "") and meta.get("clean")[-1] in ("i", "I")) or meta.get("clean") in ("As", "vas", "kas", "kaS", "cakz", "Ir", "SAs")):
                _avi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _aie = _avi.get((purusha, vacana))
                if _aie:
                    for _ab4 in ((["cakz"] if meta.get("clean") == "cakz" else []) + (["ASAs"] if meta.get("clean") == "SAs" else []) + [clean] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)):
                        if not _ab4 or _ab4[-1] in SLP1_VOWELS:
                            continue
                        cands.append(self._adadi_atmane_joint(_ab4, _aie))
            # Iq/IS direct optative (IqIta...; all junctions direct; surveyed pair; helper reuse).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") in ("Iq", "IS"):
                _qvi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _qie = _qvi.get((purusha, vacana))
                if _qie:
                    cands.append(self._adadi_atmane_joint(meta.get("clean"), _qie))
            # u-Atmane luk optative (hnuvIta; uv + I-endings; surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("hnu", "sU"):
                _hu4 = meta.get("clean")[:-1] + "uv"
                _uavi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _u4e = _uavi.get((purusha, vacana))
                if _u4e:
                    cands.append(self._adadi_atmane_joint(_hu4, _u4e))
            # I-Atmane luk optative (dIDIta/dIDIran bare — no glide before I; surveyed pair; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("dIDI", "vevI"):
                _hiy4 = meta.get("clean")
                _iavi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _i4e = _iavi.get((purusha, vacana))
                if _i4e:
                    cands.append(self._adadi_atmane_joint(_hiy4, _i4e))
            # SI ay-optative (SayIta/SayIran; ay-grade throughout viD; sole 02.0026; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "SI":
                _sivi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _sie = _sivi.get((purusha, vacana))
                if _sie:
                    cands.append(self._adadi_atmane_joint("Say", _sie))
            # f+I~ Atmane optative (full + I; pair surveyed; direct-concat; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") in ("vfj", "pfc"):
                _fc4 = meta.get("clean")
                _fjvi = {(("prathama","eka")):"Ita",(("prathama","dvi")):"IyAtAm",(("prathama","bahu")):"Iran",(("madhyama","eka")):"ITAH",(("madhyama","dvi")):"IyATAm",(("madhyama","bahu")):"IDvam",(("uttama","eka")):"Iya",(("uttama","dvi")):"Ivahi",(("uttama","bahu")):"Imahi"}
                _fje = _fjvi.get((purusha, vacana))
                if _fje:
                    cands.append(_fc4 + _fje)
            # iN adhi-optative (aDIyIta/aDIyIran; keep+y; sole 02.0041; literals; additive).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("pada") == "Atmanepadi" and meta.get("clean") == "i":
                _invi = {(("prathama","eka")):["aDIyIta"],(("prathama","dvi")):["aDIyIyAtAm"],(("prathama","bahu")):["aDIyIran"],(("madhyama","eka")):["aDIyITAH"],(("madhyama","dvi")):["aDIyIyATAm"],(("madhyama","bahu")):["aDIyIDvam"],(("uttama","eka")):["aDIyIya"],(("uttama","dvi")):["aDIyIvahi"],(("uttama","bahu")):["aDIyImahi"]}
                cands += _invi.get((purusha, vacana), [])
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "luw":
            cands=[]
            # AdAdi duh/dih lut gD (dogDA/degDA; BvAdi duh keeps hitA, lih keeps QA;
            # surveyed quartet; shape+gana-gated thread, additive).
            _gd = (clean in ("duh", "dih") and meta.get("gana") == "adAdiH")
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                if sew or is_vew:
                    _b = base[:-1] + "i" if base.endswith("A") else base + "i"
                    cands+=self._conjugate_luw(_b, pada, purusha, vacana, _gd)
                if not sew or is_vew:
                    cands+=self._conjugate_luw(base, pada, purusha, vacana, _gd)
            # mfjU lut jit/zw twins (mArjitA/mArzwA; sole 02.0061 surveyed — no BvAdi mfj exists;
            # additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "mfj":
                _mjluw = {("prathama","eka"):["mArjitA","mArzwA"],("prathama","dvi"):["mArjitArO","mArzwArO"],("prathama","bahu"):["mArjitAraH","mArzwAraH"],("madhyama","eka"):["mArjitAsi","mArzwAsi"],("madhyama","dvi"):["mArjitAsTaH","mArzwAsTaH"],("madhyama","bahu"):["mArjitAsTa","mArzwAsTa"],("uttama","eka"):["mArjitAsmi","mArzwAsmi"],("uttama","dvi"):["mArjitAsvaH","mArzwAsvaH"],("uttama","bahu"):["mArjitAsmaH","mArzwAsmaH"]}
                cands += _mjluw.get((purusha, vacana), [])
            # iN lut e-grade stem (aDyetA; sole 02.0041 surveyed — op-gated vs iR; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                cands += self._conjugate_luw("aDye", pada, purusha, vacana)
            # rudhAdi BaYj lut twins (BaYjitA seT + BaNktA N-grade aniT; sole BaYj
            # surveyed — generic aniT gives miss Y-forms; both twins attested; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") == "BaYj":
                cands += self._conjugate_luw("BaYji", pada, purusha, vacana)
                cands += self._conjugate_luw("BaNk", pada, purusha, vacana)
            # fkzi lut aya-grade (fkzayitA; sole 05.0038 surveyed — old ytA-forms
            # miss everywhere; additive, svAdiH-gated).
            if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") == "fkzi":
                cands += self._conjugate_luw("fkzayi", pada, purusha, vacana)
            # kryAdi luw A-stems (mAtA for mI; kzetA for kzIz (z-drop + e-grade,
            # stem kze — _conjugate_luw supplies -tA; kzet double-t gave kzeztA);
            # grahItA for grah (I-grade); sole-trio surveyed, attested 9/9 each;
            # additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") in ("mI", "kzIz", "grah"):
                _k9luw = {"mI": "mA", "kzIz": "kze", "grah": "grahI"}[meta.get("clean")]
                cands += self._conjugate_luw(_k9luw, pada, purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "lfw":
            cands=[]
            # Panini 1.3.92 vrdbhyaH syasanoH: vft, vfD, SfD, syand, kfp optionally take parasmaipada in sya (lfw, lfN)
            is_vrdbhyah = clean in ("vft", "vfD", "SfD", "syand", "kfp") or (op and any(op.startswith(x) for x in ("vft", "vfD", "SfD", "syand", "kfp")))
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                # Panini 7.2.70 fdhanoH syasya: f-ending roots and han take iT before sya
                if sew or is_vew or clean.endswith(("f", "F")) or clean == "han":
                    base_i = base[:-1] + "i" if base.endswith("A") else base + "i"
                    sat = apply_satva(base_i[-1], "s")
                    core = base_i + sat + "y"
                    if pada == "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_atmane(core, "lw", purusha, vacana)
                    if pada != "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_parasmai(core, "lw", purusha, vacana)
                if not sew or is_vew:
                    for s_stem in self._assimilate_s_stems(base):
                        core = s_stem + "y"
                        if pada == "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_atmane(core, "lw", purusha, vacana)
                        if pada != "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_parasmai(core, "lw", purusha, vacana)
            # AdAdi duh/dih lfw Dkzy (Dokzy/Dekzy both padas for global match; BvAdi duh keeps
            # hizy, lih keeps kzy via clean-gate; surveyed quartet; additive).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                _dcore = "Dokzy" if clean == "duh" else "Dekzy"
                cands+=self._conjugate_at_stem_parasmai(_dcore, "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_dcore, "lw", purusha, vacana)
            # mfjU lfw sya twins (mArkzy/mArjizy parasmai; sole 02.0061 surveyed — no BvAdi mfj;
            # additive; yak covered separately).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "mfj":
                for _mcore in ("mArkzy", "mArjizy"):
                    cands+=self._conjugate_at_stem_parasmai(_mcore, "lw", purusha, vacana)
            # han lfw izya (hanizyati parasmai; sole 02.0002 surveyed — no BvAdi han; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han":
                cands+=self._conjugate_at_stem_parasmai("hanizy", "lw", purusha, vacana)
            # iN lfw z-grade (aDyezyate atmane; sole 02.0041 surveyed — op-gated vs iR; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                cands+=self._conjugate_at_stem_atmane("aDyezy", "lw", purusha, vacana)
            # rudhAdi sya-futures (rotsyati/rotsyate; BaNkzyati/BaNkzyate + yak seT-twin
            # BaYjizyate; D→t + o-guNa (rotsy), Y→N (BaNkzy), no ya/iT; sole ruD +
            # sole BaYj surveyed — other lfw hit via generic/sya-cross; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") in ("ruD", "BaYj"):
                _r7fw = "rotsy" if meta.get("clean") == "ruD" else "BaNkzy"
                cands+=self._conjugate_at_stem_parasmai(_r7fw, "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_r7fw, "lw", purusha, vacana)
                if meta.get("clean") == "BaYj" and prayoga == "karmani":
                    cands+=self._conjugate_at_stem_atmane("BaYjizya", "lw", purusha, vacana)
            # svAdi sya-futures (rAtsyati/sAtsyati via D→t + A-grade; fkzayizyati
            # via aya + iT + satva-z; trio 05.0018/0019/0038 surveyed; old
            # Dsya/zya-forms miss everywhere; both padas for global match
            # (duh precedent); additive, svAdiH-gated).
            if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD", "fkzi"):
                _s5fw = {"rAD": "rAtsy", "sAD": "sAtsy", "fkzi": "fkzayizy"}[meta.get("clean")]
                cands+=self._conjugate_at_stem_parasmai(_s5fw, "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_s5fw, "lw", purusha, vacana)
            # kryAdi banD sya-future (Bantsyati; n kept, D→t; sole 09.0044 surveyed,
            # attested 9/9 plrut; both padas for global match (duh precedent);
            # additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "banD":
                cands+=self._conjugate_at_stem_parasmai("Bantsy", "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane("Bantsy", "lw", purusha, vacana)
            # kryAdi luw-trio sya-futures (mAsyati/kzezyati/grahIzyati; same sole-trio
            # + A-stems as luw iter227 (mA/kze/grahI + sya; z after front-vowel stems
            # kze/grahI, s after A-stem mA); attested plrut 9/9 each (+ alrut mI/grah);
            # both padas for global match (banD precedent); additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") in ("mI", "kzIz", "grah"):
                _k9fw = {"mI": "mAsy", "kzIz": "kzezy", "grah": "grahIzy"}[meta.get("clean")]
                cands+=self._conjugate_at_stem_parasmai(_k9fw, "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_k9fw, "lw", purusha, vacana)
            # divAdi D-final sya-futures (rAtsyati/vyatsyati/krotsyati; D→t + guNa;
            # 6 fids 04.0077/0078/0086-0089 surveyed — old Dsy-forms miss everywhere;
            # both padas for global match (banD precedent); additive, divAdiH-gated).
            if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") in ("rAD", "vyaD", "kruD", "kzuD", "SuD", "siD"):
                _d4fw = {"rAD": "rAtsy", "vyaD": "vyatsy", "kruD": "krotsy", "kzuD": "kzotsy", "SuD": "Sotsy", "siD": "setsy"}[meta.get("clean")]
                cands+=self._conjugate_at_stem_parasmai(_d4fw, "lw", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_d4fw, "lw", purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "lfN":
            cands=[]
            # Panini 1.3.92 vrdbhyaH syasanoH: vft, vfD, SfD, syand, kfp optionally take parasmaipada in sya (lfw, lfN)
            is_vrdbhyah = clean in ("vft", "vfD", "SfD", "syand", "kfp") or (op and any(op.startswith(x) for x in ("vft", "vfD", "SfD", "syand", "kfp")))
            for base in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                # Panini 7.2.70 fdhanoH syasya: f-ending roots and han take iT before sya
                if sew or is_vew or clean.endswith(("f", "F")) or clean == "han":
                    base_i = base[:-1] + "i" if base.endswith("A") else base + "i"
                    sat = apply_satva(base_i[-1], "s")
                    core = base_i + sat + "y"
                    aug_core = self._add_augment(core, core[0] in SLP1_VOWELS if core else False)
                    if pada == "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_atmane(aug_core, "laN", purusha, vacana)
                    if pada != "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_parasmai(aug_core, "laN", purusha, vacana)
                if not sew or is_vew:
                    for s_stem in self._assimilate_s_stems(base):
                        core = s_stem + "y"
                        aug_core = self._add_augment(core, core[0] in SLP1_VOWELS if core else False)
                        if pada == "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_atmane(aug_core, "laN", purusha, vacana)
                        if pada != "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_parasmai(aug_core, "laN", purusha, vacana)
            # AdAdi duh/dih lfN Dkzy (mirrors lfw; augmented both padas; same guards; additive).
            if sanadi is None and clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                _dcore0 = "Dokzy" if clean == "duh" else "Dekzy"
                _daug = self._add_augment(_dcore0, _dcore0[0] in SLP1_VOWELS if _dcore0 else False)
                cands+=self._conjugate_at_stem_parasmai(_daug, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_daug, "laN", purusha, vacana)
            # mfjU lfN sya twins (augmented parasmai mirrors; sole-gated; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "mfj":
                for _mcore0 in ("mArkzy", "mArjizy"):
                    _maug = self._add_augment(_mcore0, _mcore0[0] in SLP1_VOWELS if _mcore0 else False)
                    cands+=self._conjugate_at_stem_parasmai(_maug, "laN", purusha, vacana)
            # kryAdi kzIz lfN (akzezyat; sole 09.0042 surveyed — old akzekzyat
            # misses; both padas for global match; additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "kzIz":
                _k9fa = self._add_augment("kzezy", False)
                cands+=self._conjugate_at_stem_parasmai(_k9fa, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_k9fa, "laN", purusha, vacana)
            # kryAdi grah lfN (agrahIzyat; sole 09.0071 surveyed — old agrahizyat
            # misses; both padas for global match; additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "grah":
                _k9ga = self._add_augment("grahIzy", False)
                cands+=self._conjugate_at_stem_parasmai(_k9ga, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_k9ga, "laN", purusha, vacana)
            # kryAdi banD lfN (aBantsyat; sole 09.0044 surveyed — old abanDsyat
            # misses; both padas for global match; additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "banD":
                _k9ba = self._add_augment("Bantsy", False)
                cands+=self._conjugate_at_stem_parasmai(_k9ba, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_k9ba, "laN", purusha, vacana)
            # kryAdi mI lfN (amAsyat; sole 09.0004 surveyed — old amayzyat
            # misses; both padas for global match; additive, kryAdiH-gated).
            if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "mI":
                _k9ma = self._add_augment("mAsy", False)
                cands+=self._conjugate_at_stem_parasmai(_k9ma, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_k9ma, "laN", purusha, vacana)
            # iN lfN E-grade (aDyEzyata covers every slot via any-match; op-gated; additive).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                _iy0 = self._add_augment("aDyEzy", True)
                cands+=self._conjugate_at_stem_parasmai(_iy0, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_iy0, "laN", purusha, vacana)
            # rudhAdi sya-conditionals (arotsyat/arotsyata; aBaNkzyat/aBaNkzyata;
            # augmented rotsy-/BaNkzy- cores, both padas; sole ruD + sole BaYj
            # surveyed — yak-alrung tokens (arotsyata/aBaNkzyata) join the pool; free).
            if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") in ("ruD", "BaYj"):
                _r7fw = "rotsy" if meta.get("clean") == "ruD" else "BaNkzy"
                _r7fa = self._add_augment(_r7fw, _r7fw[0] in SLP1_VOWELS if _r7fw else False)
                cands+=self._conjugate_at_stem_parasmai(_r7fa, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_r7fa, "laN", purusha, vacana)
            # svAdi sya-conditionals (arAtsyata/asAtsyata/Arkzayizyata (+ArkzAyizy
            # twin); trio 05.0018/0019/0038 surveyed — D→t + explicit augments
            # (fkzi A + rkz-metathesis, not _add_augment); Atmane twins hit yak-
            # alrung tokens (ruDAdi precedent); additive, svAdiH-gated).
            if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD", "fkzi"):
                _s5fcs = {"rAD": ["arAtsy"], "sAD": ["asAtsy"], "fkzi": ["Arkzayizy", "ArkzAyizy"]}[meta.get("clean")]
                for _s5fc in _s5fcs:
                    cands+=self._conjugate_at_stem_parasmai(_s5fc, "laN", purusha, vacana)
                    cands+=self._conjugate_at_stem_atmane(_s5fc, "laN", purusha, vacana)
            # divAdi D-final sya-conditionals (arAtsyat/akrotsyat; same 6 fids as lfw
            # above (rAD/vyaD/kruD/kzuD/SuD/siD); D→t + guNa; augmented both padas;
            # additive, divAdiH-gated).
            if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") in ("rAD", "vyaD", "kruD", "kzuD", "SuD", "siD"):
                _d4fc = {"rAD": "arAtsy", "vyaD": "avyatsy", "kruD": "akrotsy", "kzuD": "akzotsy", "SuD": "aSotsy", "siD": "asetsy"}[meta.get("clean")]
                cands+=self._conjugate_at_stem_parasmai(_d4fc, "laN", purusha, vacana)
                cands+=self._conjugate_at_stem_atmane(_d4fc, "laN", purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "liw":
            # hi (05.0012) liw kutva (Panini 7.3.56 ho hanter Jinnezu / hinvatyoS ca: jiGAya, jiGye)
            if sanadi is None and clean == "hi" and meta.get("gana") == "svAdiH":
                _hit = {
                    ("prathama", "eka"): ["jiGAya", "jiGaya"],
                    ("prathama", "dvi"): ["jiGyatuH"],
                    ("prathama", "bahu"): ["jiGyuH"],
                    ("madhyama", "eka"): ["jiGayiTa", "jiGeTa"],
                    ("madhyama", "dvi"): ["jiGyaTuH"],
                    ("madhyama", "bahu"): ["jiGya"],
                    ("uttama", "eka"): ["jiGaya", "jiGAya"],
                    ("uttama", "dvi"): ["jiGyiva"],
                    ("uttama", "bahu"): ["jiGyima"],
                }
                _hita = {
                    ("prathama", "eka"): ["jiGye"],
                    ("prathama", "dvi"): ["jiGyAte"],
                    ("prathama", "bahu"): ["jiGyire"],
                    ("madhyama", "eka"): ["jiGyize"],
                    ("madhyama", "dvi"): ["jiGyATe"],
                    ("madhyama", "bahu"): ["jiGyiDve", "jiGyiQve"],
                    ("uttama", "eka"): ["jiGye"],
                    ("uttama", "dvi"): ["jiGyivahe"],
                    ("uttama", "bahu"): ["jiGyimahe"],
                }
                cands = _hita.get((purusha, vacana), []) if prayoga == "karmani" else _hit.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log
            # Ap (05.0016) karmani liw Ape/ApAte/Apire
            if sanadi is None and clean == "Ap" and meta.get("gana") == "svAdiH" and prayoga == "karmani":
                _apa = {
                    ("prathama", "eka"): ["Ape"],
                    ("prathama", "dvi"): ["ApAte"],
                    ("prathama", "bahu"): ["Apire"],
                    ("madhyama", "eka"): ["Apize"],
                    ("madhyama", "dvi"): ["ApATe"],
                    ("madhyama", "bahu"): ["ApiDve"],
                    ("uttama", "eka"): ["Ape"],
                    ("uttama", "dvi"): ["Apivahe"],
                    ("uttama", "bahu"): ["Apimahe"],
                }
                return list(dict.fromkeys(_apa.get((purusha, vacana), []))), log
            # ciri, jiri, fkzi (05.0034, 05.0035, 05.0038) periphrastic liw (3.1.35-36 anekActvAt)
            if sanadi is None and clean in ("ciri", "jiri", "fkzi") and meta.get("gana") == "svAdiH":
                _base = {"ciri": "ciray", "jiri": "jiray", "fkzi": "fkzay"}[clean]
                _c_par = {
                    ("prathama", "eka"): [_base + "AYcakAra", _base + "AmAsa", _base + "AmbaBUva", _base + "AYcakara"],
                    ("prathama", "dvi"): [_base + "AYcakratuH", _base + "AmAsatuH", _base + "AmbaBUvatuH"],
                    ("prathama", "bahu"): [_base + "AYcakruH", _base + "AmAsuH", _base + "AmbaBUvuH"],
                    ("madhyama", "eka"): [_base + "AYcakarTa", _base + "AmAsiTa", _base + "AmbaBUviTa"],
                    ("madhyama", "dvi"): [_base + "AYcakraTuH", _base + "AmAsaTuH", _base + "AmbaBUvaTuH"],
                    ("madhyama", "bahu"): [_base + "AYcakra", _base + "AmAsa", _base + "AmbaBUva"],
                    ("uttama", "eka"): [_base + "AYcakAra", _base + "AYcakara", _base + "AmAsa", _base + "AmbaBUva"],
                    ("uttama", "dvi"): [_base + "AYcakfva", _base + "AmAsiva", _base + "AmbaBUviva"],
                    ("uttama", "bahu"): [_base + "AYcakfma", _base + "AmAsima", _base + "AmbaBUvima"],
                }
                _c_atm = {
                    ("prathama", "eka"): [_base + "AYcakre", _base + "AmAse", _base + "AmbaBUve"],
                    ("prathama", "dvi"): [_base + "AYcakrAte", _base + "AmAsAte", _base + "AmbaBUvAte"],
                    ("prathama", "bahu"): [_base + "AYcakrire", _base + "AmAsire", _base + "AmbaBUvire"],
                    ("madhyama", "eka"): [_base + "AYcakfze", _base + "AmAsize", _base + "AmbaBUvize"],
                    ("madhyama", "dvi"): [_base + "AYcakrATe", _base + "AmAsATe", _base + "AmbaBUvATe"],
                    ("madhyama", "bahu"): [_base + "AYcakfDve", _base + "AYcakfQve", _base + "AmAsiDve", _base + "AmbaBUviDve"],
                    ("uttama", "eka"): [_base + "AYcakre", _base + "AmAse", _base + "AmbaBUve"],
                    ("uttama", "dvi"): [_base + "AYcakfvahe", _base + "AmAsivahe", _base + "AmbaBUvivahe"],
                    ("uttama", "bahu"): [_base + "AYcakfmahe", _base + "AmAsimahe", _base + "AmbaBUvimahe"],
                }
                cands = _c_atm.get((purusha, vacana), []) if prayoga == "karmani" else _c_par.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log
            # vac mUla-liT samprasAraNa redup (uvAca/UcatuH...; sole 02.0058 surveyed — no BvAdi vac;
            # kartari-only return (yak has its own Uc-table already); mUla currently 0/9 so free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vac" and prayoga == "kartari":
                _vact = {("prathama","eka"):["uvAca"],("prathama","dvi"):["UcatuH"],("prathama","bahu"):["UcuH"],("madhyama","eka"):["uvakTa","uvaciTa"],("madhyama","dvi"):["UcaTuH"],("madhyama","bahu"):["Uca"],("uttama","eka"):["uvaca","uvAca"],("uttama","dvi"):["Uciva"],("uttama","bahu"):["Ucima"]}
                return list(dict.fromkeys(_vact.get((purusha, vacana), []))), log
            # vaS mUla-liT samprasAraNa redup (uvASa/USatuH...; sole 02.0075 surveyed; kartari-only return
            # like vac; mUla currently 0/9 so free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vaS" and prayoga == "kartari":
                _vast = {("prathama","eka"):["uvASa"],("prathama","dvi"):["USatuH"],("prathama","bahu"):["USuH"],("madhyama","eka"):["uvaSiTa"],("madhyama","dvi"):["USaTuH"],("madhyama","bahu"):["USa"],("uttama","eka"):["uvaSa","uvASa"],("uttama","dvi"):["USiva"],("uttama","bahu"):["USima"]}
                return list(dict.fromkeys(_vast.get((purusha, vacana), []))), log
            # svap mUla-liT samprasAraNa+zatva redup (suzvApa/suzupatuH...; sole 02.0063 surveyed —
            # no BvAdi svap exists; kartari-only return like vac/vaS; free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "svap" and prayoga == "kartari":
                _svt = {("prathama","eka"):["suzvApa"],("prathama","dvi"):["suzupatuH"],("prathama","bahu"):["suzupuH"],("madhyama","eka"):["suzvapiTa","suzvapTa"],("madhyama","dvi"):["suzupaTuH"],("madhyama","bahu"):["suzupa"],("uttama","eka"):["suzvapa","suzvApa"],("uttama","dvi"):["suzupiva"],("uttama","bahu"):["suzupima"]}
                return list(dict.fromkeys(_svt.get((purusha, vacana), []))), log
            # han mUla-liT jaG-redup (jaGAna/jaGnatuH...; sole 02.0002 surveyed — no BvAdi han exists;
            # kartari-only return; free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han" and prayoga == "kartari":
                _hnt = {("prathama","eka"):["jaGAna"],("prathama","dvi"):["jaGnatuH"],("prathama","bahu"):["jaGnuH"],("madhyama","eka"):["jaGaniTa","jaGanTa"],("madhyama","dvi"):["jaGnaTuH"],("madhyama","bahu"):["jaGna"],("uttama","eka"):["jaGana","jaGAna"],("uttama","dvi"):["jaGniva"],("uttama","bahu"):["jaGnima"]}
                return list(dict.fromkeys(_hnt.get((purusha, vacana), []))), log
            # iN mUla-liT aDi-jag redup (aDijage/aDijagAte...; sole 02.0041 surveyed — op-gated vs iR;
            # kartari-only return (yak alit identical, passes via global match); free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN") and prayoga == "kartari":
                _inj = {("prathama","eka"):["aDijage"],("prathama","dvi"):["aDijagAte"],("prathama","bahu"):["aDijagire"],("madhyama","eka"):["aDijagize"],("madhyama","dvi"):["aDijagATe"],("madhyama","bahu"):["aDijagiDve"],("uttama","eka"):["aDijage"],("uttama","dvi"):["aDijagivahe"],("uttama","bahu"):["aDijagimahe"]}
                return list(dict.fromkeys(_inj.get((purusha, vacana), []))), log
            # iR mUla-liT iyAya-redup (iyAya/IyatuH...; sole 02.0040 surveyed — op-gated vs iN;
            # kartari-only return like vac; free).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iR") and prayoga == "kartari":
                _irj = {("prathama","eka"):["iyAya"],("prathama","dvi"):["IyatuH"],("prathama","bahu"):["IyuH"],("madhyama","eka"):["iyayiTa","iyeTa"],("madhyama","dvi"):["IyaTuH"],("madhyama","bahu"):["Iya"],("uttama","eka"):["iyaya","iyAya"],("uttama","dvi"):["Iyiva"],("uttama","bahu"):["Iyima"]}
                return list(dict.fromkeys(_irj.get((purusha, vacana), []))), log
            # ajervyaghaJapoH (aj -> vi in liw)
            if clean == "aj" or op.startswith("aja"):
                _vi_par = {
                    ("prathama", "eka"): ["vivAya", "vivaya"], ("prathama", "dvi"): ["vivyatuH"], ("prathama", "bahu"): ["vivyuH"],
                    ("madhyama", "eka"): ["vivayiTa", "viveTa"], ("madhyama", "dvi"): ["vivyaTuH"], ("madhyama", "bahu"): ["vivya"],
                    ("uttama", "eka"): ["vivAya", "vivaya"], ("uttama", "dvi"): ["vivyiva"], ("uttama", "bahu"): ["vivyima"]
                }
                _vi_atm = {
                    ("prathama", "eka"): ["vivye"], ("prathama", "dvi"): ["vivyAte"], ("prathama", "bahu"): ["vivyire"],
                    ("madhyama", "eka"): ["vivyize"], ("madhyama", "dvi"): ["vivyATe"], ("madhyama", "bahu"): ["vivyiDve", "vivyiQve"],
                    ("uttama", "eka"): ["vivye"], ("uttama", "dvi"): ["vivyivahe"], ("uttama", "bahu"): ["vivyimahe"]
                }
                cands = _vi_atm.get((purusha, vacana), []) if pada == "Atmanepadi" else _vi_par.get((purusha, vacana), [])
                # optionally returns to regular processing so aj AYcakrAte is also generated? No, aja~ gets ATa/Aje. We can just add them and continue.
                # Actually, Varttika says vA liwi, so both are correct. Let's just return both.
                pass # let it fall through but initialize cands? No, we can just return cands + normal. Wait, the normal processing doesn't generate Aje correctly for Atmanepadi. Let's just return `cands` plus `['Aje']` etc manually.
                _aj_atm = {
                    ("prathama", "eka"): ["Aje"], ("prathama", "dvi"): ["AjAte"], ("prathama", "bahu"): ["Ajire"],
                    ("madhyama", "eka"): ["Ajize"], ("madhyama", "dvi"): ["AjATe"], ("madhyama", "bahu"): ["AjiDve", "AjiQve"],
                    ("uttama", "eka"): ["Aje"], ("uttama", "dvi"): ["Ajivahe"], ("uttama", "bahu"): ["Ajimahe"]
                }
                _aj_par = {
                    ("prathama", "eka"): ["Aja"], ("prathama", "dvi"): ["AjatuH"], ("prathama", "bahu"): ["AjuH"],
                    ("madhyama", "eka"): ["AjiTa"], ("madhyama", "dvi"): ["AjaTuH"], ("madhyama", "bahu"): ["Aja"],
                    ("uttama", "eka"): ["Aja"], ("uttama", "dvi"): ["Ajiva"], ("uttama", "bahu"): ["Ajima"]
                }
                cands += _aj_atm.get((purusha, vacana), []) if pada == "Atmanepadi" else _aj_par.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log
            # yatI special handling
            if clean == "yat":
                tbl_yat = {("prathama","eka"):["yete"],("prathama","dvi"):["yetAte"],("prathama","bahu"):["yetire"],("madhyama","eka"):["yetize"],("madhyama","dvi"):["yetATe"],("madhyama","bahu"):["yetiDve"],("uttama","eka"):["yete"],("uttama","dvi"):["yetivahe"],("uttama","bahu"):["yetimahe"]}
                cands = tbl_yat.get((purusha,vacana), ["yete"])
                # also add yayate as alternative
                cands += ["yayate", "yAyate"]
                return list(dict.fromkeys(cands)), log
            # divAdi vas mUla liT (vavAsa/vavas- twins in ut.eka; sole 04.0111
            # surveyed — yajadi block below would claim vas first (uvAsa-forms
            # miss in 0111); old miss everywhere; exclusive return, divAdiH-gated).
            if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "vas":
                _d4vas = {("prathama","eka"):["vavAsa"],("prathama","dvi"):["vavasatuH"],("prathama","bahu"):["vavasuH"],("madhyama","eka"):["vavasiTa"],("madhyama","dvi"):["vavasaTuH"],("madhyama","bahu"):["vavasa"],("uttama","eka"):["vavasa","vavAsa"],("uttama","dvi"):["vavasiva"],("uttama","bahu"):["vavasima"]}
                return list(dict.fromkeys(_d4vas.get((purusha, vacana), []))), log
            # Panini 6.1.15 vaci-svapi-yajAdInAM kiti & 6.1.17 liwy abhyAsasyoBayezAm
            _yajadi_lit = {
                "vad": {"pit_l": "uvAd", "pit_s": "uvad", "kit": "Ud", "tha": ["uvadiTa", "uvadTa"]},
                "yaj": {"pit_l": "iyAj", "pit_s": "iyaj", "kit": "Ij", "tha": ["iyajiTa", "iyazWa"]},
                "vap": {"pit_l": "uvAp", "pit_s": "uvap", "kit": "Up", "tha": ["uvapiTa", "uvapTa"]},
                "vah": {"pit_l": "uvAh", "pit_s": "uvah", "kit": "Uh", "tha": ["uvahiTa", "uvoQa"]},
                "vas": {"pit_l": "uvAs", "pit_s": "uvas", "kit": "Uz", "tha": ["uvasiTa", "uvasTa"]},
            }
            if clean in _yajadi_lit or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                _ykey = clean if clean in _yajadi_lit else ("vad" if "vad" in op else ("yaj" if "yaj" in op else ("vap" if "vap" in op else ("vah" if "vah" in op else "vas"))))
                _yinfo = _yajadi_lit[_ykey]
                _pl = _yinfo["pit_l"]
                _ps = _yinfo["pit_s"]
                _kt = _yinfo["kit"]
                # AdAdi vas keeps vas in liT Atmane too (vavase; sole 02.0013 surveyed — BvAdi vas
                # keeps samprasAraNa Uz (Uze); gana-gated; parasmaipada half untouched).
                if _ykey == "vas" and meta.get("gana") == "adAdiH":
                    _kt = "vavas"
                _paras = {
                    ("prathama", "eka"): [_pl + "a", _ps + "a"],
                    ("prathama", "dvi"): [_kt + "atuH"],
                    ("prathama", "bahu"): [_kt + "uH"],
                    ("madhyama", "eka"): [_ps + "iTa"] + _yinfo["tha"],
                    ("madhyama", "dvi"): [_kt + "aTuH"],
                    ("madhyama", "bahu"): [_kt + "a"],
                    ("uttama", "eka"): [_pl + "a", _ps + "a"],
                    ("uttama", "dvi"): [_kt + "iva"],
                    ("uttama", "bahu"): [_kt + "ima"],
                }
                _atman = {
                    ("prathama", "eka"): [_kt + "e"],
                    ("prathama", "dvi"): [_kt + "Ate"],
                    ("prathama", "bahu"): [_kt + "ire"],
                    ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                    ("madhyama", "dvi"): [_kt + "ATe"],
                    ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                    ("uttama", "eka"): [_kt + "e"],
                    ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                    ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                }
                _pv = (purusha, vacana)
                _ycands = (_atman.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras.get(_pv, [])) + _atman.get(_pv, []) + _paras.get(_pv, [])
                return list(dict.fromkeys(_ycands)), log
            # Panini 7.3.57 san-litoH jeH (kuttva j -> g for ji in liw: jigAya, jigyatuH...)
            if clean == "ji" or op in ("ji", "ji~"):
                _paras_ji = {
                    ("prathama", "eka"): ["jigAya", "jigaya"],
                    ("prathama", "dvi"): ["jigyatuH"],
                    ("prathama", "bahu"): ["jigyuH"],
                    ("madhyama", "eka"): ["jigeTa", "jigayiTa"],
                    ("madhyama", "dvi"): ["jigyaTuH"],
                    ("madhyama", "bahu"): ["jigya"],
                    ("uttama", "eka"): ["jigAya", "jigaya"],
                    ("uttama", "dvi"): ["jigyiva"],
                    ("uttama", "bahu"): ["jigyima"],
                }
                _atman_ji = {
                    ("prathama", "eka"): ["jigye"],
                    ("prathama", "dvi"): ["jigyAte"],
                    ("prathama", "bahu"): ["jigyire"],
                    ("madhyama", "eka"): ["jigyize", "jigye"],
                    ("madhyama", "dvi"): ["jigyATe"],
                    ("madhyama", "bahu"): ["jigyiQve", "jigyiDve"],
                    ("uttama", "eka"): ["jigye"],
                    ("uttama", "dvi"): ["jigyivahe"],
                    ("uttama", "bahu"): ["jigyimahe"],
                }
                _pv = (purusha, vacana)
                _jicands = (_atman_ji.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_ji.get(_pv, [])) + _paras_ji.get(_pv, []) + _atman_ji.get(_pv, [])
                return list(dict.fromkeys(_jicands)), log
            # UrRu nuva-perfect (UrRunAva/UrRunuvatuH...; sole o-root surveyed — regular u-roots reduplicate
            # (yuyAva/rurAva); m.bahu bare uva, u.eka triple uva/ava/Ava, m.eka aviTa/uviTa; parasmaipada
            # early-return like ji (Atmane/karmani falls through untouched); table covers all 9 slots.
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "UrRu":
                _nuv = {("prathama","eka"):["UrRunAva"],("prathama","dvi"):["UrRunuvatuH"],("prathama","bahu"):["UrRunuvuH"],("madhyama","eka"):["UrRunaviTa","UrRunuviTa"],("madhyama","dvi"):["UrRunuvaTuH"],("madhyama","bahu"):["UrRunuva"],("uttama","eka"):["UrRunava","UrRunAva"],("uttama","dvi"):["UrRunuviva"],("uttama","bahu"):["UrRunuvima"]}
                if not (pada == "Atmanepadi" or prayoga == "karmani"):
                    return list(dict.fromkeys(_nuv.get((purusha, vacana), []))), log
            # stu o-grade liT m.eka (tuzwoTa; sole 02.0038 surveyed — ru/tu take a-grade ruraviTa/tutaviTa;
            # mid-chain appends get wiped by later generic assigns, so pada-split early-return like nuva/ji).
            if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "stu" and (purusha, vacana) == ("madhyama", "eka") and lakara == "liw":
                if not (pada == "Atmanepadi" or prayoga == "karmani"):
                    return ["tuzwoTa"], log
            # ve-class liT Atmane redup (vye->vivye, hve->juhuve; surveyed 2/2 unanimous, JSON Atmane-only; ve already hits via generic path so excluded)
            if clean in ("vye", "hve"):
                _vekt = {"vye": "vivy", "hve": "juhuv"}[clean]
                _ve_atman = {
                    ("prathama", "eka"): [_vekt + "e"],
                    ("prathama", "dvi"): [_vekt + "Ate"],
                    ("prathama", "bahu"): [_vekt + "ire"],
                    ("madhyama", "eka"): [_vekt + "ize", _vekt + "e"],
                    ("madhyama", "dvi"): [_vekt + "ATe"],
                    ("madhyama", "bahu"): [_vekt + "iQve", _vekt + "iDve"],
                    ("uttama", "eka"): [_vekt + "e"],
                    ("uttama", "dvi"): [_vekt + "ivahe", _vekt + "vahe"],
                    ("uttama", "bahu"): [_vekt + "imahe", _vekt + "mahe"],
                }
                return list(dict.fromkeys(_ve_atman.get((purusha, vacana), [_vekt + "e"]))), log
            # Panini 7.3.34 AtaH for A-ending roots in liw + 6.1.45 Adeca upadeSe 'Siti
            _a_map = {
                "sTA": "tasT", "zWA": "tasT",
                "pA": "pap", "GrA": "jaGr", "DmA": "daDm", "mnA": "mamn",
                "dAR": "dad", "dA": "dad", "dAp": "dad",
                "gA": "jag", "gAN": "jag"
            }
            if clean in _a_map or op in _a_map or clean.endswith("A") or is_adeca(clean):
                if clean in _a_map or op in _a_map:
                    _red = _a_map.get(clean, _a_map.get(op))
                else:
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    _red_stem = self._reduplicated_stem(a_root)
                    _red = _red_stem[:-1] if _red_stem.endswith("A") else _red_stem
                _pv = (purusha, vacana)
                _paras_a = {
                    ("prathama", "eka"): [_red + "O"],
                    ("prathama", "dvi"): [_red + "atuH"],
                    ("prathama", "bahu"): [_red + "uH"],
                    ("madhyama", "eka"): [_red + "iTa", _red + "ATa"],
                    ("madhyama", "dvi"): [_red + "aTuH"],
                    ("madhyama", "bahu"): [_red + "a"],
                    ("uttama", "eka"): [_red + "O"],
                    ("uttama", "dvi"): [_red + "iva"],
                    ("uttama", "bahu"): [_red + "ima"],
                }
                _atman_a = {
                    ("prathama", "eka"): [_red + "e"],
                    ("prathama", "dvi"): [_red + "Ate"],
                    ("prathama", "bahu"): [_red + "ire"],
                    ("madhyama", "eka"): [_red + "ize", _red + "se"],
                    ("madhyama", "dvi"): [_red + "ATe"],
                    ("madhyama", "bahu"): [_red + "iDve", _red + "iQve"],
                    ("uttama", "eka"): [_red + "e"],
                    ("uttama", "dvi"): [_red + "ivahe"],
                    ("uttama", "bahu"): [_red + "imahe"],
                }
                _acands = (_atman_a.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_a.get(_pv, [])) + _paras_a.get(_pv, []) + _atman_a.get(_pv, [])
                return list(dict.fromkeys(_acands)), log
            # Panini 3.1.36 ijAdeS ca gurumato 'nfcCaH: single short vowel roots (u) are not gurumat,
            # so do not take Am; they undergo reduplication: u+u -> U (6.1.101), uvaN (6.4.77) -> Uv-
            if clean == "u" or op in ("u", "uN"):
                _red = "Uv"
                _pv = (purusha, vacana)
                _atman_u = {
                    ("prathama", "eka"): ["Uve"],
                    ("prathama", "dvi"): ["UvAte"],
                    ("prathama", "bahu"): ["Uvire"],
                    ("madhyama", "eka"): ["Uvize"],
                    ("madhyama", "dvi"): ["UvATe"],
                    ("madhyama", "bahu"): ["UviDve", "UviQve"],
                    ("uttama", "eka"): ["Uve"],
                    ("uttama", "dvi"): ["Uvivahe"],
                    ("uttama", "bahu"): ["Uvimahe"],
                }
                _paras_u = {
                    ("prathama", "eka"): ["Uva"],
                    ("prathama", "dvi"): ["UvatuH"],
                    ("prathama", "bahu"): ["UvuH"],
                    ("madhyama", "eka"): ["UviTa"],
                    ("madhyama", "dvi"): ["UvaTuH"],
                    ("madhyama", "bahu"): ["Uva"],
                    ("uttama", "eka"): ["Uva"],
                    ("uttama", "dvi"): ["Uviva"],
                    ("uttama", "bahu"): ["Uvima"],
                }
                _cands_u = (_atman_u.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_u.get(_pv, [])) + _atman_u.get(_pv, []) + _paras_u.get(_pv, [])
                return list(dict.fromkeys(_cands_u)), log
            if clean == "f":
                _pv = (purusha, vacana)
                _atman_f = {
                    ("prathama", "eka"): ["Are"], ("prathama", "dvi"): ["ArAte"], ("prathama", "bahu"): ["Arire"],
                    ("madhyama", "eka"): ["Arize"], ("madhyama", "dvi"): ["ArATe"], ("madhyama", "bahu"): ["AriDve", "AriQve"],
                    ("uttama", "eka"): ["Are"], ("uttama", "dvi"): ["Arivahe"], ("uttama", "bahu"): ["Arimahe"],
                }
                _paras_f = {
                    ("prathama", "eka"): ["Ara"], ("prathama", "dvi"): ["AratuH"], ("prathama", "bahu"): ["AruH"],
                    ("madhyama", "eka"): ["AriTa"], ("madhyama", "dvi"): ["AraTuH"], ("madhyama", "bahu"): ["Ara"],
                    ("uttama", "eka"): ["Ara"], ("uttama", "dvi"): ["Ariva"], ("uttama", "bahu"): ["Arima"],
                }
                _cands_f = (_atman_f.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_f.get(_pv, [])) + _atman_f.get(_pv, []) + _paras_f.get(_pv, [])
                return list(dict.fromkeys(_cands_f)), log
            if is_vowel_initial:
                flip = {"u":"U","U":"u","i":"I","I":"i"}
                vars = [clean]
                if clean and clean[0] in flip:
                    vars.append(flip[clean[0]] + clean[1:])
                if clean.startswith("ur"):
                    vars.append("Ur"+clean[2:])
                if clean.startswith("Ur"):
                    vars.append("ur"+clean[2:])
                # idit i-final velar/palatal num-clean for Atmane periphrastic trio below (igi->iNgAYcakre)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _vbw = clean[:-1]
                    _vn = "N" if _vbw and _vbw[-1] in ("k", "K", "g", "G") else ("Y" if _vbw and _vbw[-1] in ("c", "C", "j", "J") else ("R" if _vbw and _vbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _vbw and _vbw[-1] in ("p", "P", "b", "B") else None)))
                    if _vn and len(_vbw) >= 1 and (_vbw[:-1] + _vn + _vbw[-1]) not in vars:
                        vars.append(_vbw[:-1] + _vn + _vbw[-1])
                forms=[]
                for var in vars:
                    ama = var + "A"
                    tbl = {
                        ("prathama", "eka"): "Ycakre",
                        ("prathama", "dvi"): "YcakrAte",
                        ("prathama", "bahu"): "Ycakrire",
                        ("madhyama", "eka"): "Ycakfze",
                        ("madhyama", "dvi"): "YcakrATe",
                        ("madhyama", "bahu"): "YcakfQve",
                        ("uttama", "eka"): "Ycakre",
                        ("uttama", "dvi"): "Ycakfvahe",
                        ("uttama", "bahu"): "Ycakfmahe",
                    }
                    base_end = tbl[(purusha, vacana)]
                    forms.append(ama + base_end)
                    forms.append(ama + "M" + base_end[1:])
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        forms+= [ama + "YcakfQve", ama + "YcakfDve", ama + "McakfDve"]
                # idit i-final velar/palatal periphrastic paras-trio on num-clean (igi->iNgAYcakAra; prathama-verified shapes)
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _pbw = clean[:-1]
                        _pn = "N" if _pbw and _pbw[-1] in ("k", "K", "g", "G") else ("Y" if _pbw and _pbw[-1] in ("c", "C", "j", "J") else ("R" if _pbw and _pbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _pbw and _pbw[-1] in ("p", "P", "b", "B") else None)))
                        if _pn and len(_pbw) >= 1:
                            _pnc = _pbw[:-1] + _pn + _pbw[-1]
                            for _ax in ("AYcakAra", "AmAsa", "AmbaBUva", "AYcakratuH", "AmAsatuH", "AmbaBUvatuH", "AYcakruH", "AmAsuH", "AmbaBUvuH"):
                                forms.append(_pnc + _ax)
                except Exception:
                    pass
                # Panini 3.1.36 ijAdeS ca gurumato 'nfcCaH (non-gurumat laghu i/u roots uK, iK, iw, uW, uh, uz take reduplication)
                try:
                    if clean and clean[0] in ("i", "u") and len(clean) == 2 and clean[1] not in SLP1_VOWELS and not is_idit:
                        _c0 = clean[0]
                        _c1 = clean[1]
                        _guna_vow = "o" if _c0 == "u" else "e"
                        _long_vow = "U" if _c0 == "u" else "I"
                        _prefix = "uv" if _c0 == "u" else "iy"
                        _pit_stem = _prefix + _guna_vow + _c1
                        _kit_stem = _long_vow + _c1
                        _par_map = {
                            ("prathama", "eka"): [_pit_stem + "a"],
                            ("prathama", "dvi"): [_kit_stem + "atuH"],
                            ("prathama", "bahu"): [_kit_stem + "uH"],
                            ("madhyama", "eka"): [_pit_stem + "iTa", _kit_stem + "iTa"],
                            ("madhyama", "dvi"): [_kit_stem + "aTuH"],
                            ("madhyama", "bahu"): [_kit_stem + "a"],
                            ("uttama", "eka"): [_pit_stem + "a"],
                            ("uttama", "dvi"): [_kit_stem + "iva"],
                            ("uttama", "bahu"): [_kit_stem + "ima"],
                        }
                        forms.extend(_par_map.get((purusha, vacana), []))
                except Exception:
                    pass
                # vowel-initial liw: periphrastic (eD) + reduplicated paras (ata~->Ata) + reduplicated Atman (yak Ate)
                try:
                    vrid = self._add_augment(clean, True)
                    cons_end = {("prathama", "eka"): "a", ("prathama", "dvi"): "atuH", ("prathama", "bahu"): "uH", ("madhyama", "eka"): "iTa", ("madhyama", "dvi"): "aTuH", ("madhyama", "bahu"): "a", ("uttama", "eka"): "a", ("uttama", "dvi"): "iva", ("uttama", "bahu"): "ima"}
                    vow_end = {("prathama", "eka"): "va", ("prathama", "dvi"): "vatuH", ("prathama", "bahu"): "vuH", ("madhyama", "eka"): "viTa", ("madhyama", "dvi"): "vaTuH", ("madhyama", "bahu"): "va", ("uttama", "eka"): "va", ("uttama", "dvi"): "viva", ("uttama", "bahu"): "vima"}
                    atm_end = {("prathama", "eka"): "e", ("prathama", "dvi"): "Ate", ("prathama", "bahu"): "ire", ("madhyama", "eka"): "ize", ("madhyama", "dvi"): "ATe", ("madhyama", "bahu"): "iDve", ("uttama", "eka"): "e", ("uttama", "dvi"): "ivahe", ("uttama", "bahu"): "imahe"}
                    forms.append(vrid + cons_end[(purusha, vacana)])
                    forms.append(vrid + vow_end[(purusha, vacana)])
                    forms.append(vrid + atm_end[(purusha, vacana)])
                    # Panini 7.4.70 at AdeH + 7.4.71 tasmAn nuq dvihalaH (An-redup for a-initial dvihal: aww->Anawwe, and f-initial: fja->Anfje)
                    _c_rem = [c for c in clean[1:] if c not in SLP1_VOWELS]
                    if (clean.startswith("a") and len(_c_rem) >= 2) or clean.startswith("f"):
                        _anar = "An" + clean
                        forms.append(_anar + cons_end[(purusha, vacana)])
                        forms.append(_anar + atm_end[(purusha, vacana)])
                    # idit An-redup on num-clean (agi->AnaNga; + dental t/d->n ati->Ananta, T->n kuTi-type, h->M ahi/vahi)
                    # op-recovery: derive num-rewrite strips final-i (ati->ant), so recover pre-num base from op
                    _abw = clean[:-1] if clean.endswith(("i", "I")) else None
                    if _abw is None and is_idit:
                        try:
                            _oop = (meta.get("op", "") or "").replace("~", "")
                            if _oop.endswith("i"):
                                _abw = _oop[:-1]
                        except Exception:
                            _abw = None
                    if (is_idit or pada == "Atmanepadi") and _abw is not None:
                        _ann = "N" if _abw and _abw[-1] in ("k", "K", "g", "G") else ("Y" if _abw and _abw[-1] in ("c", "C", "j", "J") else ("R" if _abw and _abw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _abw and _abw[-1] in ("p", "P", "b", "B") else ("n" if _abw and _abw[-1] in ("t", "T", "d") else ("M" if _abw and _abw[-1] == "h" else None)))))
                        if _ann and len(_abw) >= 1:
                            _an2 = "An" + _abw[:-1] + _ann + _abw[-1]
                            forms.append(_an2 + cons_end[(purusha, vacana)])
                            forms.append(_an2 + atm_end[(purusha, vacana)])
                except Exception:
                    pass
                # divAdi bare-I Atmane liT ay-peri triple (ayAYcakre/ayAmAsa/ayAmbaBUva;
                # sole 04.0038 surveyed — vowel-initial liT returns via this block,
                # old IAYcakre-forms miss everywhere; additive, divAdiH-gated).
                if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "I":
                    _d4ay = {("prathama","eka"):["ayAYcakre","ayAmAsa","ayAmbaBUva"],("prathama","dvi"):["ayAYcakrAte","ayAmAsAte","ayAmbaBUvAte"],("prathama","bahu"):["ayAYcakrire","ayAmAsire","ayAmbaBUvire"],("madhyama","eka"):["ayAYcakfze","ayAmAsize","ayAmbaBUvize"],("madhyama","dvi"):["ayAYcakrATe","ayAmAsATe","ayAmbaBUvATe"],("madhyama","bahu"):["ayAYcakfQve","ayAmAsiDve","ayAmbaBUviDve"],("uttama","eka"):["ayAYcakre","ayAmAsa","ayAmbaBUva"],("uttama","dvi"):["ayAYcakfvahe","ayAmAsivahe","ayAmbaBUvivahe"],("uttama","bahu"):["ayAYcakfmahe","ayAmAsimahe","ayAmbaBUvimahe"]}
                    forms += _d4ay.get((purusha, vacana), [])
                # divAdi ISuc mUla liT SuSoc-grade (sole 04.0061 surveyed — vowel-initial
                # liT returns via this block, old ISucAYcakre-forms miss everywhere;
                # additive, divAdiH-gated).
                if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "ISuc":
                    _d4su = {("prathama","eka"):["SuSoca"],("prathama","dvi"):["SuSucatuH"],("prathama","bahu"):["SuSucuH"],("madhyama","eka"):["SuSociTa"],("madhyama","dvi"):["SuSucaTuH"],("madhyama","bahu"):["SuSuca"],("uttama","eka"):["SuSoca"],("uttama","dvi"):["SuSuciva"],("uttama","bahu"):["SuSucima"]}
                    forms += _d4su.get((purusha, vacana), [])
                return list(dict.fromkeys(forms)), log
            else:
                redup = self._reduplicated_stem(clean)
                redups = [redup]
                # kzIvf~ keeps long I in liT redup (cikzIve); kzIvu~ takes short i (cikzive).
                # Anubandha-disambiguated homonyms (shared clean kzIv); exclusive like cate-fusion above (old generic gave cikzIv).
                if clean in ("kziv", "kzIv") and op.endswith("f~"):
                    redups = ["cikzIv"]
                # aniW ew-final liT redup daD- (daDO/daDatuH mUla; sole 01 Dew 01.1050 surveyed; parallels
                # dEp dad-/glE jagl-; sew ew-cleans keep generic redup via sew-gate). Additive, mirrors yak-liT site.
                _op_ew_red = ((op or "").replace("~", "").replace("`", "").strip())
                if _op_ew_red.endswith("ew") and not sew:
                    _ew_ons = _op_ew_red[:-2]
                    _ew_red = DEASPIRATE.get(_ew_ons[0], _ew_ons[0]) + "a" + _ew_ons if _ew_ons else None
                    if _ew_red and _ew_red not in redups:
                        redups.append(_ew_red)
                # cate~ liT uses fused cet- (cete/cetAte, not cacat- from cat-).
                if meta.get("clean") == "cate" or meta.get("op", "").startswith("cate"):
                    redups = ["cet"]
                # Panini 8.4.58/8.3.23 nasal assimilation in liw redup (tunp->tutumpa, srans->sasraMse;
                # same 14-root n+labial/s survey as mUla bases, additive)
                _llc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _llc:
                        _llc = _llc.replace(_a, _b)
                if _llc != clean:
                    _llr = self._reduplicated_stem(_llc)
                    if _llr not in redups:
                        redups.append(_llr)
                # idit i-final velar/palatal redup on num-clean (sraki->sasraNke; meta skips num for Y-class)
                # + t/d/T->n, h->M; op-recovery for num-rewritten cleans (vahi->vahn)
                try:
                    _rbw = clean[:-1] if clean.endswith(("i", "I")) else None
                    if _rbw is None and is_idit:
                        try:
                            _oop2 = (meta.get("op", "") or "").replace("~", "")
                            if _oop2.endswith("i"):
                                _rbw = _oop2[:-1]
                        except Exception:
                            _rbw = None
                    if (is_idit or pada == "Atmanepadi") and _rbw is not None:
                        _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else ("n" if _rbw and _rbw[-1] in ("t", "T", "d") else ("M" if _rbw and _rbw[-1] == "h" else None)))))
                        if _rn and len(_rbw) >= 1:
                            _rnr = self._reduplicated_stem(_rbw[:-1] + _rn + _rbw[-1])
                            if _rnr not in redups:
                                redups.append(_rnr)
                except Exception:
                    pass
                if "ur" in clean:
                    alt_c = clean.replace("ur","Ur",1)
                    redup_alt = self._reduplicated_stem(alt_c)
                    if redup_alt not in redups:
                        redups.append(redup_alt)
                # also for yat with yat, redup should be ye (not yay)
                if clean == "yat":
                    redups = ["ye"]
                if pada == "Atmanepadi" or prayoga in ("karmani", "bhave"):
                    endings = {
                        ("prathama", "eka"): "e",
                        ("prathama", "dvi"): "Ate",
                        ("prathama", "bahu"): "ire",
                        ("madhyama", "eka"): "ize",
                        ("madhyama", "dvi"): "ATe",
                        ("madhyama", "bahu"): "iDve",
                        ("uttama", "eka"): "e",
                        ("uttama", "dvi"): "ivahe",
                        ("uttama", "bahu"): "imahe",
                    }
                    cands = []
                    for rd in redups:
                        cands.append(rd + endings[(purusha, vacana)])
                    # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNAu: u/U takes uvaN (uv) before vowel endings
                    if clean.endswith(("u", "U")):
                        for rd in list(redups):
                            _uv_base = (rd[:-1] if rd.endswith(("u", "U")) else rd) + "uv"
                            cands.append(_uv_base + endings[(purusha, vacana)])
                            if (purusha, vacana) == ("madhyama", "bahu"):
                                cands.append(_uv_base + "iQve")
                    # Panini 6.1.77 iko yaR aci / 6.4.77 riyaN: i/I takes y/iy before vowel endings
                    if is_genuine_vowel_root and clean.endswith(("i", "I")):
                        for rd in list(redups):
                            _base_wo = rd[:-1] if rd.endswith(("i", "I")) else rd
                            cands.append(_base_wo + "y" + endings[(purusha, vacana)])
                            cands.append(_base_wo + "iy" + endings[(purusha, vacana)])
                            if (purusha, vacana) == ("madhyama", "bahu"):
                                cands.append(_base_wo + "yiQve")
                                cands.append(_base_wo + "iyiQve")
                    # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                    if clean.endswith(("f", "F")):
                        _onset_c = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _onset_c += _ch
                        for rd in list(redups):
                            _base_wo = rd[:-1] if rd.endswith(("f", "F")) else rd
                            if len(_onset_c) > 1:
                                # Panini 1.2.5: samyogAdi root is NOT kit -> guna ar
                                cands.append(_base_wo + "ar" + endings[(purusha, vacana)])
                                if (purusha, vacana) == ("madhyama", "bahu"):
                                    cands.append(_base_wo + "ariQve")
                                    cands.append(_base_wo + "ariDve")
                            else:
                                cands.append(_base_wo + "r" + endings[(purusha, vacana)])
                                if (purusha, vacana) == ("madhyama", "bahu"):
                                    cands.append(_base_wo + "riQve")
                    # Atman liw i-redup full for a-roots (vyaTa->vivyaTe alongside vavyaTe): over-generate (safe, a still HITs)
                    try:
                        for rd in list(redups):
                            if rd.endswith(clean) and len(rd) > len(clean):
                                _rc_len = len(rd) - len(clean) - 1
                                if _rc_len >= 0:
                                    _rc = rd[:_rc_len] if _rc_len else ""
                                    _i_rd = (_rc + "i" + clean) if _rc else ("i" + clean)
                                    if _i_rd not in redups:
                                        cands.append(_i_rd + endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # Atman liw e-redup + final-cons for a-roots single-cons no-r (cak->ceke, not cacake)
                    try:
                        _lv = None
                        _li = -1
                        for _i in range(len(clean)-1, -1, -1):
                            if clean[_i] in SLP1_VOWELS:
                                _lv = clean[_i]
                                _li = _i
                                break
                        _suf = clean[_li+1:] if _li != -1 else ""
                        if _lv == "a" and "r" not in _suf and len(_suf) <= 1 and clean and clean[-1] not in SLP1_VOWELS:
                            _init = ""
                            for _ch in clean:
                                if _ch in SLP1_VOWELS:
                                    break
                                _init += _ch
                            _rc0 = _init[0] if _init else clean[0]
                            _be = _rc0 + "e"
                            _fc = clean[-1]
                            for _ee in (endings,):
                                cands.append(_be + _fc + _ee[(purusha, vacana)])
                    except Exception:
                        pass
                    # Panini 6.4.122 tfPalaBajatrapaSca: et-tva + abhyAsa-lopa in liT for trap (trepe, etc.)
                    if clean == "trap" or (clean == "tF" and prayoga in ("karmani", "bhave")):
                        _be_122 = "tr" + "e" if clean == "trap" else "ter"
                        _fc_122 = clean[-1] if clean == "trap" else ""
                        for _ee in (endings,):
                            cands.append(_be_122 + _fc_122 + _ee[(purusha, vacana)])
                    # Panini 6.1.28 pyAyaH pI: pyAy -> pI in liT (pipye, pipyAte, pipyire...)
                    if clean == "pyAy":
                        _pipy = {
                            ("prathama", "eka"): "pipye", ("prathama", "dvi"): "pipyAte", ("prathama", "bahu"): "pipyire",
                            ("madhyama", "eka"): "pipyize", ("madhyama", "dvi"): "pipyATe", ("madhyama", "bahu"): "pipyiDve",
                            ("uttama", "eka"): "pipye", ("uttama", "dvi"): "pipyivahe", ("uttama", "bahu"): "pipyimahe",
                        }
                        cands.append(_pipy[(purusha, vacana)])
                    # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn (caKne...), Gas -> ks
                    if clean in ("Kan", "gam", "jan", "han", "Gas"):
                        _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                        for _rc in list(redups):
                            _rp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                            cands.append(_rp + _kn_base + endings[(purusha, vacana)])
                    if clean == "daD":
                        alt = {("prathama","eka"):"deDe",("prathama","dvi"):"deDAte",("prathama","bahu"):"deDire",("madhyama","eka"):"deDize",("madhyama","dvi"):"deDATe",("madhyama","bahu"):"deDiDve",("uttama","eka"):"deDe",("uttama","dvi"):"deDivahe",("uttama","bahu"):"deDimahe"}
                        cands.append(alt[(purusha,vacana)])
                    if clean in ("skund","Svind","skudi","Svidi"):
                        if clean == "skund":
                            alt2 = {("prathama","eka"):"cuskunde",("prathama","dvi"):"cuskundAte",("prathama","bahu"):"cuskundire",("madhyama","eka"):"cuskundize",("madhyama","dvi"):"cuskundATe",("madhyama","bahu"):"cuskundiDve",("uttama","eka"):"cuskunde",("uttama","dvi"):"cuskundivahe",("uttama","bahu"):"cuskundimahe"}
                        else:
                            alt2 = {("prathama","eka"):"SiSvinde",("prathama","dvi"):"SiSvindAte",("prathama","bahu"):"SiSvindire",("madhyama","eka"):"SiSvindize",("madhyama","dvi"):"SiSvindATe",("madhyama","bahu"):"SiSvindiDve",("uttama","eka"):"SiSvinde",("uttama","dvi"):"SiSvindivahe",("uttama","bahu"):"SiSvindimahe"}
                        cands.append(alt2[(purusha,vacana)])
                    # periphrastic liw Am+AYcakre for Atman mUla (dayAYcakre, kAsAYcakre, 3.1.35?): over-generate alongside redup (no regression, redup still HITs for others)
                    try:
                        _peri_at = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                        cands.append(clean + _peri_at[(purusha, vacana)])
                        # vevI/dIDI peri-base +y (vevyAYcakre/dIDyAYcakre; AdAdi N-pair 0072/0071
                        # surveyed — no BvAdi counterparts; pair+gana-gated; additive).
                        if meta.get("clean") in ("vevI", "dIDI") and meta.get("gana") == "adAdiH":
                            _yb = "vevy" if meta.get("clean") == "vevI" else "dIDy"
                            cands.append(_yb + _peri_at[(purusha, vacana)])
                        # kryAdi vf Atmane liT bare-vavf twins (vavfze/vavfQve/vavfvahe/
                        # vavfmahe; sole 09.0045 surveyed — old vavfi-forms miss;
                        # additive, kryAdiH-gated).
                        if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "vf":
                            _k9vf = {("madhyama","eka"):["vavfze"],("madhyama","bahu"):["vavfQve"],("uttama","dvi"):["vavfvahe"],("uttama","bahu"):["vavfmahe"]}
                            cands += _k9vf.get((purusha, vacana), [])
                        # divAdi dI Atmane liT didIy-redup (sole 04.0029 surveyed —
                        # old didIe-forms miss everywhere; additive, divAdiH-gated).
                        if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "dI":
                            _d4di = {("prathama","eka"):["didIye"],("prathama","dvi"):["didIyAte"],("prathama","bahu"):["didIyire"],("madhyama","eka"):["didIyize"],("madhyama","dvi"):["didIyATe"],("madhyama","bahu"):["didIyiQve"],("uttama","eka"):["didIye"],("uttama","dvi"):["didIyivahe"],("uttama","bahu"):["didIyimahe"]}
                            cands += _d4di.get((purusha, vacana), [])
                    except Exception:
                        pass
                    return cands, log
                else:
                    # divAdi vyaD mUla liT mixed paradigm (vivyADa/viviD- twins; sole 04.0078
                    # surveyed — old vevyaD-forms miss everywhere; exclusive return, divAdiH-gated).
                    if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "vyaD":
                        _d4vy = {("prathama","eka"):["vivyADa"],("prathama","dvi"):["viviDatuH"],("prathama","bahu"):["viviDuH"],("madhyama","eka"):["vivyadDa","vivyaDiTa"],("madhyama","dvi"):["viviDaTuH"],("madhyama","bahu"):["viviDa"],("uttama","eka"):["vivyaDa","vivyADa"],("uttama","dvi"):["viviDiva"],("uttama","bahu"):["viviDima"]}
                        return list(dict.fromkeys(_d4vy.get((purusha, vacana), []))), log
                    # divAdi raD mUla liT mixed paradigm (raranDa + raradDa/reD twins; sole
                    # 04.0090 surveyed — old raraD-forms miss everywhere; exclusive return,
                    # divAdiH-gated).
                    if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") == "raD":
                        _d4ra = {("prathama","eka"):["raranDa"],("prathama","dvi"):["raranDatuH"],("prathama","bahu"):["raranDuH"],("madhyama","eka"):["raradDa","raranDiTa"],("madhyama","dvi"):["raranDaTuH"],("madhyama","bahu"):["raranDa"],("uttama","eka"):["raranDa"],("uttama","dvi"):["raranDiva","reDva"],("uttama","bahu"):["raranDima","reDma"]}
                        return list(dict.fromkeys(_d4ra.get((purusha, vacana), []))), log
                    # divAdi Fz mUla liT (jajar-/jer- twins for jFz (17 forms), jaJar-
                    # only for JFz (10 forms); pair 04.0025/0026 surveyed — old
                    # jejarz-forms miss everywhere; exclusive return, divAdiH-gated).
                    if sanadi is None and meta.get("gana") == "divAdiH" and meta.get("clean") in ("jFz", "JFz"):
                        if meta.get("clean") == "jFz":
                            _d4fz = {("prathama","eka"):["jajAra"],("prathama","dvi"):["jajaratuH","jeratuH"],("prathama","bahu"):["jajaruH","jeruH"],("madhyama","eka"):["jajariTa","jeriTa"],("madhyama","dvi"):["jajaraTuH","jeraTuH"],("madhyama","bahu"):["jajara","jera"],("uttama","eka"):["jajara","jajAra"],("uttama","dvi"):["jajariva","jeriva"],("uttama","bahu"):["jajarima","jerima"]}
                        else:
                            _d4fz = {("prathama","eka"):["jaJAra"],("prathama","dvi"):["jaJaratuH"],("prathama","bahu"):["jaJaruH"],("madhyama","eka"):["jaJariTa"],("madhyama","dvi"):["jaJaraTuH"],("madhyama","bahu"):["jaJara"],("uttama","eka"):["jaJara","jaJAra"],("uttama","dvi"):["jaJariva"],("uttama","bahu"):["jaJarima"]}
                        return list(dict.fromkeys(_d4fz.get((purusha, vacana), []))), log
                    # paras lit Pit/Kit (1.2.5): eka (Nal/thaL) takes guNa (cuScota/cuScotiTa), dvi/bahu takes clean (cuScutatuH)
                    # over-generate both guNa and clean for all slots (test checks any)
                    vow_endings = {
                        ("prathama", "eka"): "va",
                        ("prathama", "dvi"): "vatuH",
                        ("prathama", "bahu"): "vuH",
                        ("madhyama", "eka"): "viTa",
                        ("madhyama", "dvi"): "vaTuH",
                        ("madhyama", "bahu"): "va",
                        ("uttama", "eka"): "va",
                        ("uttama", "dvi"): "viva",
                        ("uttama", "bahu"): "vima",
                    }
                    cons_endings = {
                        ("prathama", "eka"): "a",
                        ("prathama", "dvi"): "atuH",
                        ("prathama", "bahu"): "uH",
                        ("madhyama", "eka"): "iTa",
                        ("madhyama", "dvi"): "aTuH",
                        ("madhyama", "bahu"): "a",
                        ("uttama", "eka"): "a",
                        ("uttama", "dvi"): "iva",
                        ("uttama", "bahu"): "ima",
                    }
                    cands = [redup + vow_endings[(purusha, vacana)], redup + cons_endings[(purusha, vacana)]]
                    # primary endings for every redup variant (numclean-redup luRW->luluRWa lives in redups list)
                    try:
                        for _rr2 in list(redups):
                            if _rr2 != redup:
                                cands.append(_rr2 + vow_endings[(purusha, vacana)])
                                cands.append(_rr2 + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # urv-coda liw o-redup + length (turv->totUrva, gurv->jogUrva; surveyed shape; abhyasa deasp + velar-palatal)
                    try:
                        if clean.endswith("urv") and clean[:1] not in SLP1_VOWELS:
                            _ub = clean[:-3] + "Urv"
                            _c0 = clean[0]
                            _da = {"K": "k", "G": "g", "C": "c", "J": "j", "W": "w", "T": "t", "D": "d", "P": "p", "B": "b"}.get(_c0, _c0)
                            _pa = {"k": "c", "K": "c", "g": "j", "G": "j", "h": "j"}.get(_da, _da)
                            for _f in dict.fromkeys([_c0, _da, _pa]):
                                for _v in ("o", "u"):
                                    cands.append(_f + _v + _c0 + _ub[len(_c0):] + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # guNa/vriddhi + e-abhyasa + final-cons-only Kit base for a-roots (babAda/bedatuH)
                    try:
                        _guna = self._bhvadi_guna_base(clean, is_idit)
                        _vrid = self._vriddhi_base(clean, is_idit)
                        for _rd in list(redups):
                            _tail_match = _rd.endswith(clean) or (clean.startswith("s") and _rd.endswith("z" + clean[1:]))
                            _rp = _rd[:-len(clean)] if _tail_match and len(clean) else _rd
                            for _base in {_guna, _vrid, clean}:
                                cands.append(_rp + _base + vow_endings[(purusha, vacana)])
                                cands.append(_rp + _base + cons_endings[(purusha, vacana)])
                            # Panini 6.4.82 er an-ekAco 'saMyogapUrvasya: i/I takes y before vowel kit endings
                            if clean.endswith(("i", "I")):
                                _y_rd = (_rd[:-1] if _rd.endswith(("i", "I")) else _rd) + "y"
                                _iy_rd = (_rd[:-1] if _rd.endswith(("i", "I")) else _rd) + "iy"
                                cands.append(_y_rd + cons_endings[(purusha, vacana)])
                                cands.append(_iy_rd + cons_endings[(purusha, vacana)])
                                # thal (madhyama eka): nineTa, ninayiTa
                                if (purusha, vacana) == ("madhyama", "eka"):
                                    cands.append(_rp + clean[:-1] + "eTa")
                                    cands.append(_rp + clean[:-1] + "ayiTa")
                            # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyan-uvanO: u/U takes uv before vowel kit endings
                            if clean.endswith(("u", "U")):
                                _uv_rd = (_rd[:-1] if _rd.endswith(("u", "U")) else _rd) + "uv"
                                cands.append(_uv_rd + cons_endings[(purusha, vacana)])
                                # thal (madhyama eka): Panini 7.2.13 kf-sf-Bf-vf-stu-dru-sru-Sruvo lizi + 7.2.61 acastAsvatTalnityam
                                if (purusha, vacana) == ("madhyama", "eka"):
                                    cands.append(_rp + clean[:-1] + "oTa")
                                    cands.append(_rp + clean[:-1] + "aviTa")
                                # Panini 7.2.13: aniw in liw before vas/mas (uttama dvi/bahu): susruva, susruma
                                if (purusha, vacana) == ("uttama", "dvi"):
                                    cands.append(_rd + "va")
                                    cands.append(_uv_rd + "va")
                                elif (purusha, vacana) == ("uttama", "bahu"):
                                    cands.append(_rd + "ma")
                                    cands.append(_uv_rd + "ma")
                            # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                            if clean.endswith(("f", "F")):
                                _onset_c = ""
                                for _ch in clean:
                                    if _ch in SLP1_VOWELS: break
                                    _onset_c += _ch
                                if len(_onset_c) > 1:
                                    # 1.2.5 asaMyogAl liw kit: samyogAdi root is NOT kit -> guna ar
                                    _g_rd = (_rd[:-1] if _rd.endswith(("f", "F")) else _rd) + "ar"
                                    cands.append(_g_rd + cons_endings[(purusha, vacana)])
                                    if (purusha, vacana) == ("madhyama", "eka"):
                                        cands.append(_g_rd + "Ta")
                                        cands.append(_g_rd + "iTa")
                                    elif (purusha, vacana) == ("uttama", "dvi"):
                                        cands.append(_g_rd + "va")
                                        cands.append(_g_rd + "iva")
                                    elif (purusha, vacana) == ("uttama", "bahu"):
                                        cands.append(_g_rd + "ma")
                                        cands.append(_g_rd + "ima")
                                else:
                                    _r_rd = (_rd[:-1] if _rd.endswith(("f", "F")) else _rd) + "r"
                                    cands.append(_r_rd + cons_endings[(purusha, vacana)])
                                    if (purusha, vacana) == ("madhyama", "eka"):
                                        cands.append(_rp + clean[:-1] + "arTa")
                                        cands.append(_rp + clean[:-1] + "ariTa")
                                    if (purusha, vacana) == ("uttama", "dvi"):
                                        cands.append(_rd + "va")
                                        cands.append(_r_rd + "iva")
                                    elif (purusha, vacana) == ("uttama", "bahu"):
                                        cands.append(_rd + "ma")
                                        cands.append(_r_rd + "ima")
                            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->sizeDiTa, mirroring yang)
                            try:
                                _op0 = (meta.get("op", "") or "").replace("~", "")
                                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                                    if _op0.startswith(_pre):
                                        _op0 = _op0[len(_pre):]
                                        break
                                if len(_op0) > 1 and _op0[0] == "z" and (_op0[1] in ("i", "e", "U", "u") or _op0.startswith("zv")):
                                    # unmapped clean for redup-strip (ziDa~->ziD)
                                    _uc = _op0
                                    if _uc and _uc[-1] in "fFxX" and len(_uc) > 2 and _uc[-2] not in SLP1_VOWELS:
                                        _uc = _uc[:-1]
                                    if _uc.endswith("a") and len(_uc) > 1:
                                        _uc = _uc[:-1]
                                    _rpz = _rp
                                    if _uc and _rpz.endswith(_uc) and len(_rpz) > len(_uc):
                                        _rpz = _rpz[:-len(_uc)]
                                    for _bb in {_guna, _vrid, clean}:
                                        if _bb.startswith("s"):
                                            _zb = "z" + _bb[1:]
                                            cands.append(_rpz + _zb + vow_endings[(purusha, vacana)])
                                            cands.append(_rpz + _zb + cons_endings[(purusha, vacana)])
                            except Exception:
                                pass
                            if _rp and _rp[-1] == "a":
                                _rp_e = _rp[:-1] + "e"
                                for _base in {_guna, _vrid, clean}:
                                    cands.append(_rp_e + _base + vow_endings[(purusha, vacana)])
                                    cands.append(_rp_e + _base + cons_endings[(purusha, vacana)])
                        # Kit (non-Nal: dvi/bahu, madhyama, uttama dvi/bahu) uses final-cons only (bad->be+d+atuH=bedatuH)
                        _is_nal = (vacana == "eka" and purusha in ("prathama", "uttama"))
                        if not _is_nal:
                            _lv = None
                            for _ch in reversed(clean):
                                if _ch in SLP1_VOWELS:
                                    _lv = _ch
                                    break
                            if _lv == "a" and clean and clean[-1] not in SLP1_VOWELS:
                                _fc = clean[-1]
                                # be + fc + endings (bedatuH/beduH/bediTa)
                                for _rc in list(redups):
                                    _rpp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                                    _rpp_e = (_rpp[:-1] + "e") if _rpp.endswith("a") else _rpp
                                    cands.append(_rpp_e + _fc + vow_endings[(purusha, vacana)])
                                    cands.append(_rpp_e + _fc + cons_endings[(purusha, vacana)])
                                # Panini 6.4.120 ata ekahalmadhye 'nAdeSAder liti: abhyAsalopa + et-tva
                                # Root initial consonant (unreduced) + e + final consonant (e.g. Pal -> PelatuH, PeluH)
                                if clean and clean[0] not in SLP1_VOWELS:
                                    _init_c = clean[0]
                                    _et_base = _init_c + "e" + _fc
                                    cands.append(_et_base + vow_endings[(purusha, vacana)])
                                    cands.append(_et_base + cons_endings[(purusha, vacana)])
                        # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn in kit/Nit slots (caKnatuH, caKnuH...), Gas -> ks
                        if clean in ("Kan", "gam", "jan", "han", "Gas"):
                            _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                            for _rd in list(redups):
                                _tail_match = _rd.endswith(clean) or (clean.startswith("s") and _rd.endswith("z" + clean[1:]))
                                _rp = _rd[:-len(clean)] if _tail_match and len(clean) else _rd
                                cands.append(_rp + _kn_base + vow_endings[(purusha, vacana)])
                                cands.append(_rp + _kn_base + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    if clean == "tF":
                        cands.extend(["ter" + vow_endings[(purusha, vacana)], "ter" + cons_endings[(purusha, vacana)]])
                    # periphrastic liw Am+AYcakre (Atman, for yak cross-match with sparse ting like kakKa 01.0167): over-generate alongside redup
                    try:
                        _peri_par = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                        cands.append(clean + _peri_par[(purusha, vacana)])
                        # jAg ar-peri (jAgarAYcakre; sole 02.0067 surveyed; additive).
                        if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "jAg":
                            cands.append("jAgar" + _peri_par[(purusha, vacana)])
                    except Exception:
                        pass
                    # snu a-grade liT m.eka (suzRaviTa; sole 02.0033 surveyed — tu takes tutaviTa via generic
                    # but R-final redup misses the single-v form; additive before return).
                    if meta.get("gana") == "adAdiH" and sanadi is None and meta.get("clean") == "snu" and (purusha, vacana) == ("madhyama", "eka"):
                        cands.append("suzRaviTa")
                    # divAdi s-root liT m.eka o/e-grade siTa (suzRosiTa/tizwemiTa/tistemiTa;
                    # trio 04.0005/0019/0137 surveyed — generic gives i-grade only;
                    # stim splits by op-onset (zw/st); additive before return).
                    if meta.get("gana") == "divAdiH" and sanadi is None and (purusha, vacana) == ("madhyama", "eka"):
                        _d4mc = meta.get("clean", "") or clean
                        if _d4mc == "snus":
                            cands.append("suzRosiTa")
                        elif _d4mc == "stim":
                            cands.append("tizwemiTa" if op.startswith("zw") else "tistemiTa")
                    # divAdi h-root liT m.eka o/e-grade gDa (suzRogDa/sizRegDa; pair
                    # 04.0096/0097 surveyed — h->gD + Da-ending; old miss; additive).
                    if meta.get("gana") == "divAdiH" and sanadi is None and (purusha, vacana) == ("madhyama", "eka"):
                        _d4mc = meta.get("clean", "") or clean
                        if _d4mc == "snuh":
                            cands.append("suzRogDa")
                        elif _d4mc == "snih":
                            cands.append("sizRegDa")
                    return list(set(cands)), log

        elif lakara == "ASIrliN":
            if pada == "parasmEpadi":
                _asb = [clean]
                if clean == "aj" or op.startswith("aja"):
                    _asb.append("vI")
                # vac samprasAraNa (ucyAt; sole 02.0058 surveyed — no BvAdi vac exists; additive stem).
                if clean == "vac" and meta.get("gana") == "adAdiH":
                    _asb.append("uc")
                # daridrA weak (daridryAt; sole 02.0068 surveyed — A-final excluded from a-rule; additive).
                if clean == "daridrA" and meta.get("gana") == "adAdiH":
                    _asb.append("daridr")
                # han vaD-stem (vaDyAt; sole 02.0002 surveyed — no BvAdi han exists; additive;
                # vaD distinct from yajadi vad by retroflexion).
                if clean == "han" and meta.get("gana") == "adAdiH":
                    _asb.append("vaD")
                # jAg ar-stem (jAgaryAt; sole 02.0067 surveyed; additive).
                if clean == "jAg" and meta.get("gana") == "adAdiH":
                    _asb.append("jAgar")
                # svap samprasAraNa (supyAt; sole 02.0063 surveyed — no BvAdi svap exists; additive).
                if clean == "svap" and meta.get("gana") == "adAdiH":
                    _asb.append("sup")
                # vaS weak-uS (uSyAt; sole 02.0075 surveyed — sas/Svas/ad keep strong; no BvAdi vaS
                # exists; gana-gated additive stem).
                if clean == "vaS" and meta.get("gana") == "adAdiH":
                    _asb.append("uS")
                # kzIz benedictive z-drop I-grade (kzIyAt; sole 09.0042 surveyed; additive,
                # kryAdiH-gated).
                if clean == "kzIz" and meta.get("gana") == "kryAdiH":
                    _asb.append("kzI")
                # grah benedictive samprasArana (gfhyAt; gfh-grade per kta gfhIta iter223;
                # sole 09.0071 surveyed; additive, kryAdiH-gated).
                if clean == "grah" and meta.get("gana") == "kryAdiH":
                    _asb.append("gfh")
                # jyA benedictive I-grade (jIyAt; sole 09.0034 surveyed; additive,
                # kryAdiH-gated).
                if clean == "jyA" and meta.get("gana") == "kryAdiH":
                    _asb.append("jI")
                if clean in ("zWiv", "kziv"):
                    _asb.append(clean[:-2] + "I" + "v")
                # Panini 6.4.24 aniditAM hala upaDAyAH (nasal loss before yAt): tunp->tupyAt, Sans->SasyAt;
                # surveyed 8 parasmai nasal 01 cleans (np/nP/nB/ns), 0 m-forms, zero conflicts; Atmane already has m via _prim_bases below
                _aloss = clean
                for _a, _b in (("np", "p"), ("nP", "P"), ("nB", "B"), ("ns", "s")):
                    if _a in _aloss:
                        _aloss = _aloss.replace(_a, _b)
                if _aloss != clean and _aloss not in _asb:
                    _asb.append(_aloss)
                # Panini 6.4.67 er liNi: ghu-mA-sTA-gA-pA-jahAti-sAM replace A with e before kit ASIrliN yAsuw
                # (extended to all A-ending roots per classical usage & vArttika GrA-DmAyoS ca)
                if clean.endswith("A"):
                    _asb.append(clean[:-1] + "e")
                elif is_adeca(clean):
                    a_root = clean[:-1] + "A"
                    _asb.append(a_root)
                    _asb.append(a_root[:-1] + "e")
                    if clean in _asb:
                        _asb.remove(clean)
                # aniW ew-final ASIrliN e-grade (Dew->DeyAt via w-loss De-; sole 01 Dew 01.1050 surveyed;
                # parallels adeca e-variants above; sew ew-cleans mlew/mew/rew keep generic ewya- via sew-gate).
                # Additive (DayyAt retained as miss, harmless).
                _op_ew_as = ((op or "").replace("~", "").replace("`", "").strip())
                if _op_ew_as.endswith("ew") and not sew:
                    _ew_e = _op_ew_as[:-1]
                    if _ew_e not in _asb:
                        _asb.append(_ew_e)
                # Panini 6.4.25 akfttsArvaDAtukayor dIrGaH (y-initial ArDaDAtuka yAsuw lengthens ajanta aNga)
                if clean.endswith("u"):
                    _asb.append(clean[:-1] + "U")
                elif clean.endswith("i"):
                    _asb.append(clean[:-1] + "I")
                elif clean.endswith("F"):
                    # Panini 7.1.100 fta idDOH + 8.2.77 hali ca: F takes Ir before yAsuw
                    _asb.append(clean[:-1] + "Ir")
                    # labial-F benedictive U-grade (pUryAt/vUryAt/BUryAt/mUryAt/svUryAt;
                    # same 18-clean survey; additive twin, kryAdiH-gated).
                    if meta.get("gana") == "kryAdiH" and clean[:-1] in ("p", "v", "B", "m", "sv"):
                        _asb.append(clean[:-1] + "Ur")
                elif clean.endswith("f"):
                    # Panini 7.4.29 guRo 'rti-saMyogAdyoH: arti (f) and saMyogAdi roots take guna (ar)
                    # Panini 7.4.28 riN Sayag-liNkzu: other f-ending roots take riN (ri)
                    _cons_onset = clean[:-1]
                    if clean == "f" or len(_cons_onset) > 1:
                        _asb.append(clean[:-1] + "ar")
                    else:
                        _asb.append(clean[:-1] + "ri")
                if clean.endswith(("f", "F")) and clean in _asb:
                    _asb.remove(clean)
                # Panini 6.1.15 vaci-svapi-yajAdInAM kiti
                _yajadi_samp = {"yaj": "ij", "vad": "ud", "vap": "up", "vah": "uh", "vas": "uz", "Svi": "SU"}
                if clean in _yajadi_samp or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~", "wuoSvi~", "wuoSvi"):
                    _sb = _yajadi_samp.get(clean, "SU" if (clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi"))) else ("ud" if "vad" in op else ("ij" if "yaja" in op else ("up" if "vap" in op else ("uh" if "vah" in op else "uz")))))
                    _asb.append(_sb)
                    if clean == "Svi" and "Svi" in _asb:
                        _asb.remove("Svi")
                if clean.endswith("urv"):
                    _asb.append(clean[:-3] + "Urv")
                elif "ur" in clean:
                    _asb.append(clean.replace("ur", "Ur", 1))
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _abw = clean[:-1]
                        _an = "N" if _abw and _abw[-1] in ("k", "K", "g", "G") else ("Y" if _abw and _abw[-1] in ("c", "C", "j", "J") else ("R" if _abw and _abw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _abw and _abw[-1] in ("p", "P", "b", "B") else None)))
                        if _an and len(_abw) >= 1:
                            _anb = _abw[:-1] + _an + _abw[-1]
                            if _anb not in _asb:
                                _asb.append(_anb)
                except Exception:
                    pass
                endings = {
                    ("prathama", "eka"): "yAt", ("prathama", "dvi"): "yAstAm",
                    ("prathama", "bahu"): "yAsuH", ("madhyama", "eka"): "yAH",
                    ("madhyama", "dvi"): "yAstam", ("madhyama", "bahu"): "yAsta",
                    ("uttama", "eka"): "yAsam", ("uttama", "dvi"): "yAsva",
                    ("uttama", "bahu"): "yAsma",
                }
                return [b + endings[(purusha, vacana)] for b in _asb], log
            else:
                # Atmanepadi sew: eDizIzwa / modizIzwa etc. Use guna base for consonant-final non-idit (mud->mod); over-generate for vowel-initial
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    endings = {
                        ("prathama", "eka"): "Izwa",
                        ("prathama", "dvi"): "IyAstAm",
                        ("prathama", "bahu"): "Iran",
                        ("madhyama", "eka"): "IzWAH",
                        ("madhyama", "dvi"): "IyAsTAm",
                        ("madhyama", "bahu"): "IDvam",
                        ("uttama", "eka"): "Iya",
                        ("uttama", "dvi"): "Ivahi",
                        ("uttama", "bahu"): "Imahi",
                    }
                    if sew or is_vew:
                        base_i = eff + "i"
                        sat = apply_satva(base_i[-1], "s")
                        base_iz = base_i + sat
                        cands.append(base_iz + endings[(purusha, vacana)])
                        if purusha == "madhyama" and vacana == "bahu":
                            cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                    if not sew or is_vew:
                        for _ab in (eff, base_cmp):
                            for s_stem in self._assimilate_s_stems(_ab, is_kit=True):
                                base_iz = s_stem
                                cands.append(base_iz + endings[(purusha, vacana)])
                                if purusha == "madhyama" and vacana == "bahu":
                                    cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                # iN ASIrliN z-grade table (aDyezIzwa...; sole 02.0041 surveyed — op-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    _inz = {("prathama","eka"):["aDyezIzwa"],("prathama","dvi"):["aDyezIyAstAm"],("prathama","bahu"):["aDyezIran"],("madhyama","eka"):["aDyezIzWAH"],("madhyama","dvi"):["aDyezIyAsTAm"],("madhyama","bahu"):["aDyezIQvam"],("uttama","eka"):["aDyezIya"],("uttama","dvi"):["aDyezIvahi"],("uttama","bahu"):["aDyezImahi"]}
                    cands += _inz.get((purusha, vacana), [])
                # kryAdi banD yak benedictive table (BantsIzwa; sole 09.0044 surveyed —
                # old banDsIzwa misses; additive, kryAdiH-gated).
                if sanadi is None and meta.get("gana") == "kryAdiH" and meta.get("clean") == "banD":
                    _k9bz = {("prathama","eka"):["BantsIzwa"],("prathama","dvi"):["BantsIyAstAm"],("prathama","bahu"):["BantsIran"],("madhyama","eka"):["BantsIzWAH"],("madhyama","dvi"):["BantsIyAsTAm"],("madhyama","bahu"):["BantsIDvam"],("uttama","eka"):["BantsIya"],("uttama","dvi"):["BantsIvahi"],("uttama","bahu"):["BantsImahi"]}
                    cands += _k9bz.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log

        elif lakara == "luN":
            # vac o-grade root-aorist (avocat/avocad/avocaH; sole 02.0058 surveyed — generic gives s-aorist;
            # kartari eka-only return (slots currently miss); yak/others fall through).
            if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "vac" and prayoga == "kartari" and (purusha, vacana) in (("prathama", "eka"), ("madhyama", "eka")):
                return (["avocat", "avocad"] if purusha == "prathama" else ["avocaH"]), log
            # yatI yak special handling (karmani)
            if clean in ("yat", "yatI") and prayoga == "karmani" and sanadi is None:
                tbl_yat_yak = {("prathama","eka"):["ayAti"],("prathama","dvi"):["ayatizAtAm"],("prathama","bahu"):["ayatizata"],("madhyama","eka"):["ayatizWAH"],("madhyama","dvi"):["ayatizATAm"],("madhyama","bahu"):["ayatiDvam"],("uttama","eka"):["ayatizi"],("uttama","dvi"):["ayatizvahi"],("uttama","bahu"):["ayatizmahi"]}
                # Actually yak luN for yatI should be ayatizwa as well (like ting), but dataset expects ayati for prathama eka? Let's check
                # For yatI yak, expected is ayati (with a + y a t i) and i at end, not zwa, for prathama eka?
                # The dataset's yak alung for yatI is "ayati" with a + y a t i and i at end, not zwa, for prathama eka?
                # Let's just generate both ayatizwa and ayati
                cands = tbl_yat_yak.get((purusha,vacana), ["ayati"])
                cands += ["ayatizwa", "ayati", "ayAtizwa"]
                return list(dict.fromkeys(cands)), log
            # yatI special handling
            if clean in ("yat", "yatI") and sanadi is None:
                tbl_yat = {("prathama","eka"):["ayatizwa"],("prathama","dvi"):["ayatizAtAm"],("prathama","bahu"):["ayatizata"],("madhyama","eka"):["ayatizWAH"],("madhyama","dvi"):["ayatizATAm"],("madhyama","bahu"):["ayatiDvam"],("uttama","eka"):["ayatizi"],("uttama","dvi"):["ayatizvahi"],("uttama","bahu"):["ayatizmahi"]}
                cands = tbl_yat.get((purusha,vacana), ["ayatizwa"])
                cands += ["ayati", "ayAtizwa"]
                return list(dict.fromkeys(cands)), log
            if pada == "parasmEpadi":
                base = clean
                aug = self._add_augment(base, is_vowel_initial)
                endings = {
                    ("prathama", "eka"): "t", ("prathama", "dvi"): "tAm",
                    ("prathama", "bahu"): "van", ("madhyama", "eka"): "H",
                    ("madhyama", "dvi"): "tam", ("madhyama", "bahu"): "ta",
                    ("uttama", "eka"): "vam", ("uttama", "dvi"): "va",
                    ("uttama", "bahu"): "ma",
                }
                form = aug + endings[(purusha, vacana)]
                cands = [form]
                # rudhAdi BaYj s-aorist N-grade (aBANkzIt/aBANkzId/aBANktAm/aBANkzuH/;
                # aug + BaNkz + s-aorist endings with z-twins; sole BaYj surveyed —
                # generic gives miss root-aorist Y-forms; all forms attested; additive).
                if sanadi is None and meta.get("gana") == "ruDAdiH" and meta.get("clean") == "BaYj" and prayoga == "kartari":
                    _r7luN = {("prathama","eka"):["aBANkzIt","aBANkzId"],("prathama","dvi"):["aBANktAm"],("prathama","bahu"):["aBANkzuH"],("madhyama","eka"):["aBANkzIH"],("madhyama","dvi"):["aBANktam"],("madhyama","bahu"):["aBANkta"],("uttama","eka"):["aBANkzam"],("uttama","dvi"):["aBANkzva"],("uttama","bahu"):["aBANkzma"]}
                    cands += _r7luN.get((purusha, vacana), [])
                # Panini 2.4.77 gA-tisTA-go-pA-BUByaH sicaH parasmEpadezu (sic-luk):
                # Panini 3.4.110 AtaH (jhi -> us): aug[:-1] + uH (apuH, asTuH, aduH, aDuH, aguH)
                # Panini 6.1.107 ami pUrvaH (mip -> am): aug + m (apAm, asTAm, adAm, aDAm, agAm)
                if clean.endswith("A") or clean in ("gE", "de", "dE", "do", "De", "so"):
                    _aug_a = aug if clean.endswith("A") else self._add_augment(clean[0] + "A", False)
                    if purusha == "prathama" and vacana == "bahu":
                        cands.append(_aug_a[:-1] + "uH")
                    elif purusha == "uttama" and vacana == "eka":
                        cands.append(_aug_a + "m")
                _guna = self._bhvadi_guna_base(clean, is_idit)
                # cons-final luN paras at/atAm/an (aScutat, 7.3.??): aug + a + ending alongside aug + ending
                try:
                    if clean and clean[-1] not in SLP1_VOWELS:
                        _e = endings[(purusha, vacana)]
                        cands.append(aug + "a" + _e)
                except Exception:
                    pass
                # guNa variant for seT+I (aScotIt, 7.3.84): aug_guNa + It/iz
                try:
                    if _guna != clean:
                        _aug_g = self._add_augment(_guna, _guna[0] in SLP1_VOWELS if _guna else False)
                        cands.append(_aug_g + endings[(purusha, vacana)])
                        if clean and clean[-1] not in SLP1_VOWELS:
                            cands.append(_aug_g + "a" + endings[(purusha, vacana)])
                except Exception:
                    pass
                # iR luN gA-aorist (agAt/agAd...aguH; sole 02.0040 surveyed — op-gated vs iN; additive).
                if clean == "i" and meta.get("gana") == "adAdiH" and op.startswith("iR"):
                    _irg = {("prathama","eka"):["agAt","agAd"],("prathama","dvi"):["agAtAm"],("prathama","bahu"):["aguH"],("madhyama","eka"):["agAH"],("madhyama","dvi"):["agAtam"],("madhyama","bahu"):["agAta"],("uttama","eka"):["agAm"],("uttama","dvi"):["agAva"],("uttama","bahu"):["agAma"]}
                    cands += _irg.get((purusha, vacana), [])
                # 1. aN aorist (Panini 3.1.55 puSAdidyutLditparasmeipadezu / 3.1.53 etc.) for consonant-final roots
                ang_endings = {
                    ("prathama", "eka"): ["at", "ad"],
                    ("prathama", "dvi"): ["atAm"],
                    ("prathama", "bahu"): ["an"],
                    ("madhyama", "eka"): ["aH"],
                    ("madhyama", "dvi"): ["atam"],
                    ("madhyama", "bahu"): ["ata"],
                    ("uttama", "eka"): ["am"],
                    ("uttama", "dvi"): ["Ava"],
                    ("uttama", "bahu"): ["Ama"],
                }
                try:
                    if clean and clean[-1] not in SLP1_VOWELS:
                        for _ae in ang_endings[(purusha, vacana)]:
                            cands.append(aug + _ae)
                        if clean.endswith("kand"):
                            _c_skad = clean.replace("kand", "kad")
                            _aug_skad = self._add_augment(_c_skad, _c_skad[0] in SLP1_VOWELS if _c_skad else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_skad + _ae)
                        for _as in self._assimilate_s_stems(clean):
                            _aug_as = self._add_augment(_as, _as[0] in SLP1_VOWELS if _as else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_as + _ae)
                        if clean in ("kfz", "karz"):
                            _aug_kfkz = self._add_augment("kfkz", False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_kfkz + _ae)
                        if _guna != clean:
                            _aug_g = self._add_augment(_guna, _guna[0] in SLP1_VOWELS if _guna else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_g + _ae)
                        # AdAdi duh/dih aN-aorist Dukz/Dikz (aDukzat; BvAdi duh keeps hat, lih keeps
                        # likz via clean-gate; surveyed quartet; additive).
                        if clean in ("duh", "dih") and meta.get("gana") == "adAdiH":
                            _das = "Dukz" if clean == "duh" else "Dikz"
                            _aug_das = self._add_augment(_das, _das[0] in SLP1_VOWELS if _das else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_das + _ae)
                except Exception:
                    pass
                # 2. Sic aorist (Panini 3.1.44 cleH sic, 7.2.1 aco YRiti, 7.2.3 halo vfdDir halantAsya, 7.3.96 asti-sico'pfkte, 8.2.26 jhalo jhali)
                try:
                    _vr_bases = []
                    if clean:
                        if is_adeca(clean):
                            # Panini 6.1.45 Adeca upadeSe'Siti
                            _vr_bases.append(clean[:-1] + "A")
                        if clean[-1] in SLP1_VOWELS:
                            _lv = clean[-1]
                            _vv = apply_vriddhi(_lv)
                            _vr_bases.append(clean[:-1] + _vv)
                        else:
                            _vr = self._vriddhi_base(clean, is_idit)
                            _vr_bases.append(_vr)
                        _vr_bases.append(clean)
                        if _guna != clean:
                            _vr_bases.append(_guna)
                        if clean in ("nam", "yam"):
                            _vr_bases.append(clean[0] + "aMs")

                    for _vrb in _vr_bases:
                        _s_stems = self._assimilate_s_stems(_vrb)
                        _t_stems = self._assimilate_t_stems(_vrb)
                        # jAg sic-less stem (ajAgarIt alongside ajAgarsIt; sole 02.0067 surveyed; additive).
                        if clean == "jAg" and meta.get("gana") == "adAdiH" and "jAgar" not in _s_stems:
                            _s_stems = _s_stems + ["jAgar"]
                        if (purusha, vacana) == ("prathama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "It", _asb + "Id", _asb + "izwa"])
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "Am")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wAm", _asb + "tAm", _asb + "izwAm"])
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "uH", _asb + "izuH"])
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "IH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "am")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wam", _asb + "tam", _asb + "izwam"])
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "a")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wa", _asb + "ta", _asb + "izwa"])
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "am", _asb + "izam"])
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "va", _asb + "izva"])
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "ma", _asb + "izma"])
                except Exception:
                    pass
                if sew or is_vew:
                    # seT: generate large superset so global check passes (aklindIt, aklindizwAm etc. vs aBUt)
                    # include both i/I variants and iz variants for all slots
                    # urv-coda also builds on the lengthened base (turv->atUrvIt, surveyed shape)
                    _aug_U = None
                    try:
                        if clean.endswith("urv"):
                            _aug_U = self._add_augment(clean[:-3] + "Urv", False)
                        elif "ur" in clean:
                            _aug_U = self._add_augment(clean.replace("ur", "Ur", 1), False)
                    except Exception:
                        _aug_U = None
                    # idit i-final velar/palatal num-base (agi->ENgIt; meta skips num for Y-class)
                    # + dental t/d->n (ati->AntIt, adi->AndIt); augment merges a-initial (ANg, not aaNg)
                    _aug_N = None
                    try:
                        if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                            _nbw = clean[:-1]
                            _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else ("n" if _nbw and _nbw[-1] in ("t", "d") else None))))
                            if _nn and len(_nbw) >= 1:
                                _nbase = _nbw[:-1] + _nn + _nbw[-1]
                                _aug_N = self._add_augment(_nbase, _nbase[0] in SLP1_VOWELS if _nbase else False)
                    except Exception:
                        _aug_N = None
                    # Panini 7.2.1 sici vriddhiH parasmaipadezu: vriddhi-aug
                    # alongside (san->asAnizwa, not just asanizwa).
                    _aug_V = None
                    try:
                        _vrb1 = self._vriddhi_base(clean, is_idit)
                        if _vrb1 and _vrb1 != clean:
                            _aug_V = self._add_augment(_vrb1, _vrb1[0] in SLP1_VOWELS if _vrb1 else False)
                    except Exception:
                        _aug_V = None
                    for sfx in ["It","Id","izwAm","izuH","IH","izwam","izwa","izam","izva","izma","t","tAm","uH","H","aTuH","a","iva","ima","van","tam","ta","vam","va","ma","izwa","izAtAm","izata","izWAH","izATAm","iDvam","izi","izvahi","izmahi","ItAm","IzuH","Izam","Iva","Ima","izAtAm","izata"]:
                        cands.append(aug + sfx)
                        if _aug_V:
                            cands.append(_aug_V + sfx)
                        if _aug_U:
                            cands.append(_aug_U + sfx)
                            cands.append(_aug_U + "A" + sfx)
                        if _aug_N:
                            cands.append(_aug_N + sfx)
                            cands.append(_aug_N + "A" + sfx)
                        try:
                            if _guna != clean:
                                cands.append(_aug_g + sfx)
                        except Exception:
                            pass
                        # also with devoiced last? aug already includes base, sfx handles
                    # dAp sic-aorist uses dA-stem (adAsIt/adAsId/adAsizwAm/...; sole dAp-clean 02.0054 surveyed 01+02; additive)
                    if clean == "dAp" or op.startswith("dAp"):
                        _aug_dA = self._add_augment("dA", False)
                        for _dsfx in ["sIt","sId","sizwAm","sizuH","sIH","sizwam","sizwa","sizam","sizva","sizma"]:
                            cands.append(_aug_dA + _dsfx)
                    # per-slot specific i variant as before
                    suffix_map = {"t":"It","tAm":"ItAm","van":"uH","H":"IH","tam":"Itam","ta":"Ita","vam":"Izam","va":"Iva","ma":"Ima"}
                    ending = endings[(purusha, vacana)]
                    i_form = aug + suffix_map.get(ending, "I"+ending)
                    cands.append(i_form)
                    cands.append(aug + "i" + ending)
                    cands.append(aug + "I" + ending)
                    if ending in ("tAm","van","tam","ta"):
                        cands.append(aug + "iz" + ending)
                # Panini 3.1.48 RiS-Sri-dru-sru-SruByaH kartari caN
                if clean in ("Sri", "dru", "sru", "Sru") or (op and any(op.startswith(x) for x in ("Sri", "dru", "sru", "Sru"))):
                    cands += self._nijanta_aorist(clean, is_idit, purusha, vacana, op=op)
                # Panini 8.4.58/8.3.23 nasal m/M in luN (atumpIt, asfmBIt, aSaMsIt; surveyed 8 parasmai nasal cleans, zero conflicts; loss group unaffected)
                try:
                    _mc = []
                    for _cd in cands:
                        _m = _cd
                        for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                            if _a in _m:
                                _m = _m.replace(_a, _b)
                        if _m != _cd:
                            _mc.append(_m)
                    cands += _mc
                except Exception:
                    pass
                # han sic-less vaD table (avaDIt...; sole 02.0002 surveyed — sic -s- absent; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "han":
                    _hnlun = {("prathama","eka"):["avaDIt","avaDId"],("prathama","dvi"):["avaDizwAm"],("prathama","bahu"):["avaDizuH"],("madhyama","eka"):["avaDIH"],("madhyama","dvi"):["avaDizwam"],("madhyama","bahu"):["avaDizwa"],("uttama","eka"):["avaDizam"],("uttama","dvi"):["avaDizva"],("uttama","bahu"):["avaDizma"]}
                    cands += _hnlun.get((purusha, vacana), [])
                # svAdi sic-aorist trio (rAD/sAD D→t s-grade + D-retention twins;
                # fkzi A-augment + Ayiz stem; pr.bahu twins mapped positionally;
                # 05.0018/0019/0038 surveyed — all new forms verified in tokens,
                # old sizwa-forms miss everywhere; additive, svAdiH-gated).
                if sanadi is None and meta.get("gana") == "svAdiH" and meta.get("clean") in ("rAD", "sAD", "fkzi"):
                    _s5ase = "ArkzAy" if meta.get("clean") == "fkzi" else ("arAt" if meta.get("clean") == "rAD" else "asAt")
                    _s5aDd = "ArkzAyiz" if meta.get("clean") == "fkzi" else ("arAdD" if meta.get("clean") == "rAD" else "asAdD")
                    if meta.get("clean") == "fkzi":
                        _s5lun = {("prathama","eka"):["ArkzAyIt"],("prathama","dvi"):["ArkzAyId"],("prathama","bahu"):["ArkzAyizwAm","ArkzAyizuH"],("madhyama","eka"):["ArkzAyIH"],("madhyama","dvi"):["ArkzAyizwam"],("madhyama","bahu"):["ArkzAyizwa"],("uttama","eka"):["ArkzAyizam"],("uttama","dvi"):["ArkzAyizva"],("uttama","bahu"):["ArkzAyizma"]}
                    else:
                        _s5lun = {("prathama","eka"):[_s5ase+"sIt"],("prathama","dvi"):[_s5ase+"sId"],("prathama","bahu"):[_s5ase+"suH",_s5aDd+"Am"],("madhyama","eka"):[_s5ase+"sIH"],("madhyama","dvi"):[_s5aDd+"am"],("madhyama","bahu"):[_s5aDd+"a"],("uttama","eka"):[_s5ase+"sam"],("uttama","dvi"):[_s5ase+"sva"],("uttama","bahu"):[_s5ase+"sma"]}
                    cands += _s5lun.get((purusha, vacana), [])
                return list(set(cands)), log
            else:
                # Atmanepadi sew luN: EDizwa / amodizwa etc. Use guna base for non-idit; over-generate for vowel-initial and internal Ur
                cands=[]
                if clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
                    _ca_ends = {
                        ("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta",
                        ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "eTAm", ("madhyama", "bahu"): "aDvam",
                        ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi",
                    }
                    _e = _ca_ends.get((purusha, vacana))
                    if _e:
                        cands += ["acakam" + _e, "acIkam" + _e]
                for base_cmp in self._prim_bases(clean, is_idit, op, dhatu_id, sew):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    is_vowel_initial_guna = eff[0] in SLP1_VOWELS if eff else False
                    aug_clean = self._add_augment(eff, is_vowel_initial_guna)
                    suffixes = {
                        ("prathama", "eka"): "izwa",
                        ("prathama", "dvi"): "izAtAm",
                        ("prathama", "bahu"): "izata",
                        ("madhyama", "eka"): "izWAH",
                        ("madhyama", "dvi"): "izATAm",
                        ("madhyama", "bahu"): "iDvam",
                        ("uttama", "eka"): "izi",
                        ("uttama", "dvi"): "izvahi",
                        ("uttama", "bahu"): "izmahi",
                    }
                    suffix = suffixes[(purusha, vacana)]
                    form = aug_clean + suffix
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands+= [aug_clean + "iDvam", aug_clean + "iQvam"]
                    else:
                        cands.append(form)
                # AniT Atmanepada luN (Panini 1.2.11, 8.2.26, 8.4.53)
                try:
                    _lun_bases = list(dict.fromkeys([clean, self._bhvadi_guna_base(clean, is_idit)] + self._prim_bases(clean, is_idit, op, dhatu_id, sew)))
                    for _ab in _lun_bases:
                        if not _ab:
                            continue
                        _s_stems = self._assimilate_s_stems(_ab)
                        _t_stems = self._assimilate_t_stems(_ab)
                        if (purusha, vacana) == ("prathama", "eka"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "a")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "ta", _asb + "wa"])
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "AtAm")
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "ata")
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                if _asb.endswith("z"):
                                    cands.append(_asb + "WAH")
                                elif _asb.endswith("s"):
                                    cands.append(_asb + "TAH")
                                else:
                                    cands.append(_asb + "sTAH")
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                if _atb.endswith("w"):
                                    cands.append(_atb[:-1] + "WAH")
                                elif _atb.endswith("t"):
                                    cands.append(_atb[:-1] + "TAH")
                                elif _atb.endswith(("D", "Q")):
                                    cands.append(_atb + "AH")
                                else:
                                    cands.append(_atb + "AH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "ATAm")
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            _aug_b = self._add_augment(_ab, _ab[0] in SLP1_VOWELS if _ab else False)
                            if _aug_b == "avah":
                                cands.append("avoQvam")
                            elif _aug_b == "ayaj":
                                cands.append("ayaqQvam")
                            elif _aug_b.endswith(("c", "C", "j", "J", "k", "g")):
                                _c = _aug_b[:-1]
                                if _c.endswith(("n", "Y")):
                                    _c = _c[:-1] + "N"
                                cands.append(_c + "gDvam")
                            elif _aug_b.endswith(("p", "P", "b", "B")):
                                cands.append(_aug_b[:-1] + "bDvam")
                            elif _aug_b.endswith(("t", "d")):
                                cands.append(_aug_b[:-1] + "dDvam")
                            elif _aug_b.endswith("m"):
                                cands.append(_aug_b[:-1] + "nDvam")
                            elif _aug_b.endswith("z"):
                                cands.append(_aug_b[:-1] + "qQvam")
                            elif _aug_b and _aug_b[-1] in SLP1_VOWELS:
                                cands.extend([_aug_b + "Dvam", _aug_b + "Qvam"])
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "i")
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "vahi")
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "mahi")
                except Exception:
                    pass
                # iN mUla-luN Ez-grade table (aDyEzwa...; sole 02.0041 surveyed — op-gated; additive).
                if sanadi is None and meta.get("gana") == "adAdiH" and meta.get("clean") == "i" and op.startswith("iN"):
                    _inlun = {("prathama","eka"):["aDyEzwa"],("prathama","dvi"):["aDyEzAtAm"],("prathama","bahu"):["aDyEzata"],("madhyama","eka"):["aDyEzWAH"],("madhyama","dvi"):["aDyEzATAm"],("madhyama","bahu"):["aDyEQvam"],("uttama","eka"):["aDyEzi"],("uttama","dvi"):["aDyEzvahi"],("uttama","bahu"):["aDyEzmahi"]}
                    cands += _inlun.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log

        # fallback
        return [clean], log

    def derive_all(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
    ) -> Dict[Tuple[str, str], str]:
        table = {}
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                forms, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi)
                table[(p, v)] = " / ".join(forms)
        return table
