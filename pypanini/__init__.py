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
from .subanta import SubantaEngine, decline_all

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
    "clean_dhatu_op",
]
