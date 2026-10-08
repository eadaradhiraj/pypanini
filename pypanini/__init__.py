"""
PyPanini: Computational Sanskrit grammar engine based on Paninian rules (SLP1).
"""
from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import (
    apply_guna,
    apply_vriddhi,
    apply_sandhi_eco_ayavayavah,
    apply_satva,
    apply_rutva_visarga,
)
from .tinanta import TinantaDerivationEngine, clean_dhatu_op
from .krdanta import KrdantaEngine
from .subanta import (SubantaEngine, decline_all, ekaSeza, pumvatBAva,
                       avyaya_pada, saH_sulopa, satf_feminine, stri_pratipadika)
from .search import (analyze, analyze_tin_krd, best, subanta_search,
                      krdanta_search, tinanta_search)

__all__ = [
    "MaheshvaraSutrasSLP1",
    "apply_guna",
    "apply_vriddhi",
    "apply_sandhi_eco_ayavayavah",
    "apply_satva",
    "apply_rutva_visarga",
    "TinantaDerivationEngine",
    "KrdantaEngine",
    "SubantaEngine",
    "decline_all",
    "ekaSeza",
    "pumvatBAva",
    "avyaya_pada",
    "saH_sulopa",
    "satf_feminine",
    "stri_pratipadika",
    "analyze",
    "analyze_tin_krd",
    "best",
    "subanta_search",
    "krdanta_search",
    "tinanta_search",
    "clean_dhatu_op",
]
