"""Full 24-form paradigm audit — SLP1 golden tables.

Each golden dict covers (vibhakti 1..8 x vacana) with exact expected lists.
Twins (vibhAzA) are lists with 2 entries. Empty list = impossible number
(dvi-only / bahu-only stems).
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini.subanta import SubantaEngine

GOLDENS = {
    ("rAma", "puM"): {
        (1, "eka"): ["rAmaH"], (1, "dvi"): ["rAmO"], (1, "bahu"): ["rAmAH"],
        (2, "eka"): ["rAmam"], (2, "dvi"): ["rAmO"], (2, "bahu"): ["rAmAn"],
        (3, "eka"): ["rAmeRa"], (3, "dvi"): ["rAmAByAm"], (3, "bahu"): ["rAmEH"],
        (4, "eka"): ["rAmAya"], (4, "dvi"): ["rAmAByAm"], (4, "bahu"): ["rAmeByaH"],
        (5, "eka"): ["rAmAt"], (5, "dvi"): ["rAmAByAm"], (5, "bahu"): ["rAmeByaH"],
        (6, "eka"): ["rAmasya"], (6, "dvi"): ["rAmayoH"], (6, "bahu"): ["rAmARAm"],
        (7, "eka"): ["rAme"], (7, "dvi"): ["rAmayoH"], (7, "bahu"): ["rAmezu"],
        (8, "eka"): ["rAma"], (8, "dvi"): ["rAmO"], (8, "bahu"): ["rAmAH"],
    },
    ("sItA", "strI"): {
        (1, "eka"): ["sItA"], (1, "dvi"): ["sIte"], (1, "bahu"): ["sItAH"],
        (2, "eka"): ["sItAm"], (2, "dvi"): ["sIte"], (2, "bahu"): ["sItAH"],
        (3, "eka"): ["sItayA"], (3, "dvi"): ["sItAByAm"], (3, "bahu"): ["sItABiH"],
        (4, "eka"): ["sItAyE"], (4, "dvi"): ["sItAByAm"], (4, "bahu"): ["sItAByaH"],
        (5, "eka"): ["sItAyAH"], (5, "dvi"): ["sItAByAm"], (5, "bahu"): ["sItAByaH"],
        (6, "eka"): ["sItAyAH"], (6, "dvi"): ["sItayoH"], (6, "bahu"): ["sItAnAm"],
        (7, "eka"): ["sItAyAm"], (7, "dvi"): ["sItayoH"], (7, "bahu"): ["sItAsu"],
        (8, "eka"): ["sIte"], (8, "dvi"): ["sIte"], (8, "bahu"): ["sItAH"],
    },
    ("hari", "puM"): {
        (1, "eka"): ["hariH"], (1, "dvi"): ["haryO"], (1, "bahu"): ["harayaH"],
        (2, "eka"): ["harim"], (2, "dvi"): ["haryO"], (2, "bahu"): ["harIn"],
        (3, "eka"): ["haryA"], (3, "dvi"): ["hariByAm"], (3, "bahu"): ["hariBiH"],
        (4, "eka"): ["haraye"], (4, "dvi"): ["hariByAm"], (4, "bahu"): ["hariByaH"],
        (5, "eka"): ["hareH"], (5, "dvi"): ["hariByAm"], (5, "bahu"): ["hariByaH"],
        (6, "eka"): ["hareH"], (6, "dvi"): ["haryoH"], (6, "bahu"): ["harIRAm"],
        (7, "eka"): ["harO"], (7, "dvi"): ["haryoH"], (7, "bahu"): ["harizu"],
        (8, "eka"): ["hare"], (8, "dvi"): ["haryO"], (8, "bahu"): ["harayaH"],
    },
    ("nadI", "strI"): {
        (1, "eka"): ["nadIH"], (1, "dvi"): ["nadyO"], (1, "bahu"): ["nadyaH"],
        (2, "eka"): ["nadIm"], (2, "dvi"): ["nadyO"], (2, "bahu"): ["nadIH"],
        (3, "eka"): ["nadyA"], (3, "dvi"): ["nadIByAm"], (3, "bahu"): ["nadIBiH"],
        (4, "eka"): ["nadyE"], (4, "dvi"): ["nadIByAm"], (4, "bahu"): ["nadIByaH"],
        (5, "eka"): ["nadyAH"], (5, "dvi"): ["nadIByAm"], (5, "bahu"): ["nadIByaH"],
        (6, "eka"): ["nadyAH"], (6, "dvi"): ["nadyoH"], (6, "bahu"): ["nadInAm"],
        (7, "eka"): ["nadyAm"], (7, "dvi"): ["nadyoH"], (7, "bahu"): ["nadIzu"],
        (8, "eka"): ["nadi"], (8, "dvi"): ["nadyO"], (8, "bahu"): ["nadyaH"],
    },
    ("vAri", "napuMsaka"): {
        (1, "eka"): ["vAri"], (1, "dvi"): ["vAriRI"], (1, "bahu"): ["vArIRi"],
        (2, "eka"): ["vAri"], (2, "dvi"): ["vAriRI"], (2, "bahu"): ["vArIRi"],
        (3, "eka"): ["vAriRA"], (3, "dvi"): ["vAriByAm"], (3, "bahu"): ["vAriBiH"],
        (4, "eka"): ["vAriRe"], (4, "dvi"): ["vAriByAm"], (4, "bahu"): ["vAriByaH"],
        (5, "eka"): ["vAriRaH"], (5, "dvi"): ["vAriByAm"], (5, "bahu"): ["vAriByaH"],
        (6, "eka"): ["vAriRaH"], (6, "dvi"): ["vAriRoH"], (6, "bahu"): ["vArIRAm"],
        (7, "eka"): ["vAriRi"], (7, "dvi"): ["vAriRoH"], (7, "bahu"): ["vArizu"],
        (8, "eka"): ["vAri"], (8, "dvi"): ["vAriRI"], (8, "bahu"): ["vArIRi"],
    },
    ("kartf", "puM"): {
        (1, "eka"): ["kartA"], (1, "dvi"): ["kartArO"], (1, "bahu"): ["kartAraH"],
        (2, "eka"): ["kartAram"], (2, "dvi"): ["kartArO"], (2, "bahu"): ["kartFRaH"],
        (3, "eka"): ["kartrA"], (3, "dvi"): ["kartfByAm"], (3, "bahu"): ["kartfBiH"],
        (4, "eka"): ["kartre"], (4, "dvi"): ["kartfByAm"], (4, "bahu"): ["kartfByaH"],
        (5, "eka"): ["kartuH"], (5, "dvi"): ["kartfByAm"], (5, "bahu"): ["kartfByaH"],
        (6, "eka"): ["kartuH"], (6, "dvi"): ["kartroH"], (6, "bahu"): ["kartrARAm"],
        (7, "eka"): ["kartari"], (7, "dvi"): ["kartroH"], (7, "bahu"): ["kartfzu"],
        (8, "eka"): ["kartar"], (8, "dvi"): ["kartArO"], (8, "bahu"): ["kartAraH"],
    },
    ("rAjan", "puM"): {
        (1, "eka"): ["rAjA"], (1, "dvi"): ["rAjAnO"], (1, "bahu"): ["rAjAnaH"],
        (2, "eka"): ["rAjAnam"], (2, "dvi"): ["rAjAnO"], (2, "bahu"): ["rAjYaH"],
        (3, "eka"): ["rAjYA"], (3, "dvi"): ["rAjaByAm"], (3, "bahu"): ["rAjaBiH"],
        (4, "eka"): ["rAjYe"], (4, "dvi"): ["rAjaByAm"], (4, "bahu"): ["rAjaByaH"],
        (5, "eka"): ["rAjYaH"], (5, "dvi"): ["rAjaByAm"], (5, "bahu"): ["rAjaByaH"],
        (6, "eka"): ["rAjYaH"], (6, "dvi"): ["rAjYoH"], (6, "bahu"): ["rAjYAm"],
        (7, "eka"): ["rAjYi"], (7, "dvi"): ["rAjYoH"], (7, "bahu"): ["rAjasu"],
        (8, "eka"): ["rAjA"], (8, "dvi"): ["rAjAnO"], (8, "bahu"): ["rAjAnaH"],
    },
    ("manas", "napuMsaka"): {
        (1, "eka"): ["manaH"], (1, "dvi"): ["manasI"], (1, "bahu"): ["manAMsi"],
        (2, "eka"): ["manaH"], (2, "dvi"): ["manasI"], (2, "bahu"): ["manAMsi"],
        (3, "eka"): ["manasA"], (3, "dvi"): ["manoByAm"], (3, "bahu"): ["manoBiH"],
        (4, "eka"): ["manase"], (4, "dvi"): ["manoByAm"], (4, "bahu"): ["manoByaH"],
        (5, "eka"): ["manasaH"], (5, "dvi"): ["manoByAm"], (5, "bahu"): ["manoByaH"],
        (6, "eka"): ["manasaH"], (6, "dvi"): ["manasoH"], (6, "bahu"): ["manasAm"],
        (7, "eka"): ["manasi"], (7, "dvi"): ["manasoH"], (7, "bahu"): ["manaHsu"],
        (8, "eka"): ["manaH"], (8, "dvi"): ["manasI"], (8, "bahu"): ["manAMsi"],
    },
    ("vAc", "strI"): {
        (1, "eka"): ["vAk"], (1, "dvi"): ["vAcO"], (1, "bahu"): ["vAcaH"],
        (2, "eka"): ["vAcam"], (2, "dvi"): ["vAcO"], (2, "bahu"): ["vAcaH"],
        (3, "eka"): ["vAcA"], (3, "dvi"): ["vAgByAm"], (3, "bahu"): ["vAgBiH"],
        (4, "eka"): ["vAce"], (4, "dvi"): ["vAgByAm"], (4, "bahu"): ["vAgByaH"],
        (5, "eka"): ["vAcaH"], (5, "dvi"): ["vAgByAm"], (5, "bahu"): ["vAgByaH"],
        (6, "eka"): ["vAcaH"], (6, "dvi"): ["vAcoH"], (6, "bahu"): ["vAcAm"],
        (7, "eka"): ["vAci"], (7, "dvi"): ["vAcoH"], (7, "bahu"): ["vAkzu"],
        (8, "eka"): ["vAk"], (8, "dvi"): ["vAcO"], (8, "bahu"): ["vAcaH"],
    },
    ("go", "puM"): {
        (1, "eka"): ["gOH"], (1, "dvi"): ["gAvO"], (1, "bahu"): ["gAvaH"],
        (2, "eka"): ["gAm"], (2, "dvi"): ["gAvO"], (2, "bahu"): ["gAH"],
        (3, "eka"): ["gavA"], (3, "dvi"): ["goByAm"], (3, "bahu"): ["goBiH"],
        (4, "eka"): ["gave"], (4, "dvi"): ["goByAm"], (4, "bahu"): ["goByaH"],
        (5, "eka"): ["goH"], (5, "dvi"): ["goByAm"], (5, "bahu"): ["goByaH"],
        (6, "eka"): ["goH"], (6, "dvi"): ["gavoH"], (6, "bahu"): ["gavAm"],
        (7, "eka"): ["gavi"], (7, "dvi"): ["gavoH"], (7, "bahu"): ["gozu"],
        (8, "eka"): ["gOH"], (8, "dvi"): ["gAvO"], (8, "bahu"): ["gAvaH"],
    },
    ("tad", "puM"): {
        (1, "eka"): ["saH"], (1, "dvi"): ["tO"], (1, "bahu"): ["te"],
        (2, "eka"): ["tam"], (2, "dvi"): ["tO"], (2, "bahu"): ["tAn"],
        (3, "eka"): ["tena"], (3, "dvi"): ["tAByAm"], (3, "bahu"): ["tEH"],
        (4, "eka"): ["tasmE"], (4, "dvi"): ["tAByAm"], (4, "bahu"): ["teByaH"],
        (5, "eka"): ["tasmAt"], (5, "dvi"): ["tAByAm"], (5, "bahu"): ["teByaH"],
        (6, "eka"): ["tasya"], (6, "dvi"): ["tayoH"], (6, "bahu"): ["tezAm"],
        (7, "eka"): ["tasmin"], (7, "dvi"): ["tayoH"], (7, "bahu"): ["tezu"],
        (8, "eka"): ["saH"], (8, "dvi"): ["tO"], (8, "bahu"): ["te"],
    },
    ("tad", "napuMsaka"): {
        (1, "eka"): ["tat"], (1, "dvi"): ["te"], (1, "bahu"): ["tAni"],
        (2, "eka"): ["tat"], (2, "dvi"): ["te"], (2, "bahu"): ["tAni"],
        (3, "eka"): ["tena"], (3, "dvi"): ["tAByAm"], (3, "bahu"): ["tEH"],
        (4, "eka"): ["tasmE"], (4, "dvi"): ["tAByAm"], (4, "bahu"): ["teByaH"],
        (5, "eka"): ["tasmAt"], (5, "dvi"): ["tAByAm"], (5, "bahu"): ["teByaH"],
        (6, "eka"): ["tasya"], (6, "dvi"): ["tayoH"], (6, "bahu"): ["tezAm"],
        (7, "eka"): ["tasmin"], (7, "dvi"): ["tayoH"], (7, "bahu"): ["tezu"],
        (8, "eka"): ["tat"], (8, "dvi"): ["te"], (8, "bahu"): ["tAni"],
    },
}

GOLDENS2 = {
    ("saKi", "puM"): {
        (1, "eka"): ["saKA"], (1, "dvi"): ["saKAyO"], (1, "bahu"): ["saKAyaH"],
        (2, "eka"): ["saKAyam"], (2, "dvi"): ["saKAyO"], (2, "bahu"): ["saKyIn"],
        (3, "eka"): ["saKyA"], (3, "dvi"): ["saKiByAm"], (3, "bahu"): ["saKiBiH"],
        (4, "eka"): ["saKye"], (4, "dvi"): ["saKiByAm"], (4, "bahu"): ["saKiByaH"],
        (5, "eka"): ["saKyuH"], (5, "dvi"): ["saKiByAm"], (5, "bahu"): ["saKiByaH"],
        (6, "eka"): ["saKyuH"], (6, "dvi"): ["saKyoH"], (6, "bahu"): ["saKInAm"],
        (7, "eka"): ["saKyO"], (7, "dvi"): ["saKyoH"], (7, "bahu"): ["saKizu"],
        (8, "eka"): ["saKe"], (8, "dvi"): ["saKAyO"], (8, "bahu"): ["saKAyaH"],
    },
    ("asTi", "napuMsaka"): {
        (1, "eka"): ["asTi"], (1, "dvi"): ["asTinI"], (1, "bahu"): ["asTini"],
        (2, "eka"): ["asTi"], (2, "dvi"): ["asTinI"], (2, "bahu"): ["asTini"],
        (3, "eka"): ["asTnA"], (3, "dvi"): ["asTiByAm"], (3, "bahu"): ["asTiBiH"],
        (4, "eka"): ["asTne"], (4, "dvi"): ["asTiByAm"], (4, "bahu"): ["asTiByaH"],
        (5, "eka"): ["asTnaH"], (5, "dvi"): ["asTiByAm"], (5, "bahu"): ["asTiByaH"],
        (6, "eka"): ["asTnaH"], (6, "dvi"): ["asTnoH"], (6, "bahu"): ["asTnAm"],
        (7, "eka"): ["asTni"], (7, "dvi"): ["asTnoH"], (7, "bahu"): ["asTizu"],
        (8, "eka"): ["asTi"], (8, "dvi"): ["asTinI"], (8, "bahu"): ["asTini"],
    },
    ("sarva", "puM"): {
        (1, "eka"): ["sarvaH"], (1, "dvi"): ["sarvO"], (1, "bahu"): ["sarve"],
        (2, "eka"): ["sarvam"], (2, "dvi"): ["sarvO"], (2, "bahu"): ["sarvAn"],
        (3, "eka"): ["sarveRa"], (3, "dvi"): ["sarvAByAm"], (3, "bahu"): ["sarvEH"],
        (4, "eka"): ["sarvasmE"], (4, "dvi"): ["sarvAByAm"], (4, "bahu"): ["sarveByaH"],
        (5, "eka"): ["sarvasmAt"], (5, "dvi"): ["sarvAByAm"], (5, "bahu"): ["sarveByaH"],
        (6, "eka"): ["sarvasya"], (6, "dvi"): ["sarvayoH"], (6, "bahu"): ["sarvezAm"],
        (7, "eka"): ["sarvasmin"], (7, "dvi"): ["sarvayoH"], (7, "bahu"): ["sarvezu"],
        (8, "eka"): ["sarva"], (8, "dvi"): ["sarvO"], (8, "bahu"): ["sarve"],
    },
    ("adas", "puM"): {
        (1, "eka"): ["asO"], (1, "dvi"): ["amU"], (1, "bahu"): ["amI"],
        (2, "eka"): ["amum"], (2, "dvi"): ["amU"], (2, "bahu"): ["amUn"],
        (3, "eka"): ["amunA"], (3, "dvi"): ["amUByAm"], (3, "bahu"): ["amIBiH"],
        (4, "eka"): ["amuzmE"], (4, "dvi"): ["amUByAm"], (4, "bahu"): ["amIByaH"],
        (5, "eka"): ["amuzmAt"], (5, "dvi"): ["amUByAm"], (5, "bahu"): ["amIByaH"],
        (6, "eka"): ["amuzya"], (6, "dvi"): ["amuyoH"], (6, "bahu"): ["amIzAm"],
        (7, "eka"): ["amuzmin"], (7, "dvi"): ["amuyoH"], (7, "bahu"): ["amIzu"],
        (8, "eka"): ["asO"], (8, "dvi"): ["amU"], (8, "bahu"): ["amI"],
    },
    ("SrI", "strI"): {
        (1, "eka"): ["SrIH"], (1, "dvi"): ["SriyO"], (1, "bahu"): ["SriyaH"],
        (2, "eka"): ["Sriyam"], (2, "dvi"): ["SriyO"], (2, "bahu"): ["SriyaH"],
        (3, "eka"): ["SriyA"], (3, "dvi"): ["SrIByAm"], (3, "bahu"): ["SrIBiH"],
        (4, "eka"): ["SriyE"], (4, "dvi"): ["SrIByAm"], (4, "bahu"): ["SrIByaH"],
        (5, "eka"): ["SriyaH"], (5, "dvi"): ["SrIByAm"], (5, "bahu"): ["SrIByaH"],
        (6, "eka"): ["SriyaH"], (6, "dvi"): ["SriyoH"], (6, "bahu"): ["SriyAm"],
        (7, "eka"): ["Sriyam"], (7, "dvi"): ["SriyoH"], (7, "bahu"): ["SrIzu"],
        (8, "eka"): ["SrI"], (8, "dvi"): ["SriyO"], (8, "bahu"): ["SriyaH"],
    },
    ("pratyaYc", "puM"): {
        (1, "eka"): ["pratyaN"], (1, "dvi"): ["pratyaYcO"], (1, "bahu"): ["pratyaYcaH"],
        (2, "eka"): ["pratyaYcam"], (2, "dvi"): ["pratyaYcO"], (2, "bahu"): ["pratIcaH"],
        (3, "eka"): ["pratIcA"], (3, "dvi"): ["pratyagByAm"], (3, "bahu"): ["pratyagBiH"],
        (4, "eka"): ["pratIce"], (4, "dvi"): ["pratyagByAm"], (4, "bahu"): ["pratyagByaH"],
        (5, "eka"): ["pratIcaH"], (5, "dvi"): ["pratyagByAm"], (5, "bahu"): ["pratyagByaH"],
        (6, "eka"): ["pratIcaH"], (6, "dvi"): ["pratIcoH"], (6, "bahu"): ["pratIcAm"],
        (7, "eka"): ["pratIci"], (7, "dvi"): ["pratIcoH"], (7, "bahu"): ["pratyakzu"],
        (8, "eka"): ["pratyaN"], (8, "dvi"): ["pratyaYcO"], (8, "bahu"): ["pratyaYcaH"],
    },
    ("Sreyas", "puM"): {
        (1, "eka"): ["SreyAn"], (1, "dvi"): ["SreyAMsO"], (1, "bahu"): ["SreyAMsaH"],
        (2, "eka"): ["SreyAMsam"], (2, "dvi"): ["SreyAMsO"], (2, "bahu"): ["SreyasaH"],
        (3, "eka"): ["SreyasA"], (3, "dvi"): ["SreyoByAm"], (3, "bahu"): ["SreyoBiH"],
        (4, "eka"): ["Sreyase"], (4, "dvi"): ["SreyoByAm"], (4, "bahu"): ["SreyoByaH"],
        (5, "eka"): ["SreyasaH"], (5, "dvi"): ["SreyoByAm"], (5, "bahu"): ["SreyoByaH"],
        (6, "eka"): ["SreyasaH"], (6, "dvi"): ["SreyasoH"], (6, "bahu"): ["SreyasAm"],
        (7, "eka"): ["Sreyasi"], (7, "dvi"): ["SreyasoH"], (7, "bahu"): ["SreyaHsu"],
        (8, "eka"): ["Sreyan"], (8, "dvi"): ["SreyAMsO"], (8, "bahu"): ["SreyAMsaH"],
    },
    ("Bavat", "puM"): {
        (1, "eka"): ["BavAn"], (1, "dvi"): ["BavAntO"], (1, "bahu"): ["BavAntaH"],
        (2, "eka"): ["BavAntam"], (2, "dvi"): ["BavAntO"], (2, "bahu"): ["BavataH"],
        (3, "eka"): ["BavatA"], (3, "dvi"): ["BavadByAm"], (3, "bahu"): ["BavadBiH"],
        (4, "eka"): ["Bavate"], (4, "dvi"): ["BavadByAm"], (4, "bahu"): ["BavadByaH"],
        (5, "eka"): ["BavataH"], (5, "dvi"): ["BavadByAm"], (5, "bahu"): ["BavadByaH"],
        (6, "eka"): ["BavataH"], (6, "dvi"): ["BavatoH"], (6, "bahu"): ["BavatAm"],
        (7, "eka"): ["Bavati"], (7, "dvi"): ["BavatoH"], (7, "bahu"): ["Bavatsu"],
        (8, "eka"): ["BavAn"], (8, "dvi"): ["BavAntO"], (8, "bahu"): ["BavAntaH"],
    },
    ("gacCat", "puM"): {
        (1, "eka"): ["gacCan"], (1, "dvi"): ["gacCantO"], (1, "bahu"): ["gacCantaH"],
        (2, "eka"): ["gacCantam"], (2, "dvi"): ["gacCantO"], (2, "bahu"): ["gacCataH"],
        (3, "eka"): ["gacCatA"], (3, "dvi"): ["gacCadByAm"], (3, "bahu"): ["gacCadBiH"],
        (4, "eka"): ["gacCate"], (4, "dvi"): ["gacCadByAm"], (4, "bahu"): ["gacCadByaH"],
        (5, "eka"): ["gacCataH"], (5, "dvi"): ["gacCadByAm"], (5, "bahu"): ["gacCadByaH"],
        (6, "eka"): ["gacCataH"], (6, "dvi"): ["gacCatoH"], (6, "bahu"): ["gacCatAm"],
        (7, "eka"): ["gacCati"], (7, "dvi"): ["gacCatoH"], (7, "bahu"): ["gacCatsu"],
        (8, "eka"): ["gacCan"], (8, "dvi"): ["gacCantO"], (8, "bahu"): ["gacCantaH"],
    },
    ("cakfvas", "puM"): {
        (1, "eka"): ["cakfvAn"], (1, "dvi"): ["cakfvAMsO"], (1, "bahu"): ["cakfvAMsaH"],
        (2, "eka"): ["cakfvAMsam"], (2, "dvi"): ["cakfvAMsO"], (2, "bahu"): ["cakfuzaH"],
        (3, "eka"): ["cakfuzA"], (3, "dvi"): ["cakfvadByAm"], (3, "bahu"): ["cakfvadBiH"],
        (4, "eka"): ["cakfuze"], (4, "dvi"): ["cakfvadByAm"], (4, "bahu"): ["cakfvadByaH"],
        (5, "eka"): ["cakfuzaH"], (5, "dvi"): ["cakfvadByAm"], (5, "bahu"): ["cakfvadByaH"],
        (6, "eka"): ["cakfuzaH"], (6, "dvi"): ["cakfuzoH"], (6, "bahu"): ["cakfuzAm"],
        (7, "eka"): ["cakfuzi"], (7, "dvi"): ["cakfuzoH"], (7, "bahu"): ["cakfvatsu"],
        (8, "eka"): ["cakfvAn"], (8, "dvi"): ["cakfvAMsO"], (8, "bahu"): ["cakfvAMsaH"],
    },
    ("kftavat", "puM"): {
        (1, "eka"): ["kftavAn"], (1, "dvi"): ["kftavAntO"], (1, "bahu"): ["kftavAntaH"],
        (2, "eka"): ["kftavAntam"], (2, "dvi"): ["kftavAntO"], (2, "bahu"): ["kftavataH"],
        (3, "eka"): ["kftavatA"], (3, "dvi"): ["kftavadByAm"], (3, "bahu"): ["kftavadBiH"],
        (4, "eka"): ["kftavate"], (4, "dvi"): ["kftavadByAm"], (4, "bahu"): ["kftavadByaH"],
        (5, "eka"): ["kftavataH"], (5, "dvi"): ["kftavadByAm"], (5, "bahu"): ["kftavadByaH"],
        (6, "eka"): ["kftavataH"], (6, "dvi"): ["kftavatoH"], (6, "bahu"): ["kftavatAm"],
        (7, "eka"): ["kftavati"], (7, "dvi"): ["kftavatoH"], (7, "bahu"): ["kftavatsu"],
        (8, "eka"): ["kftavAn"], (8, "dvi"): ["kftavAntO"], (8, "bahu"): ["kftavAntaH"],
    },
}


class TestSubantaFullAudit(unittest.TestCase):
    def test_full_tables(self):
        e = SubantaEngine()
        total = 0
        misses = []
        for (stem, linga), golden in {**GOLDENS, **GOLDENS2}.items():
            got = e.decline(stem, linga)
            for key, exp_list in golden.items():
                total += 1
                got_list = got.get(key, [])
                for exp in exp_list:
                    if exp not in got_list:
                        misses.append(f"{stem}/{linga} {key}: want {exp} got {got_list}")
        self.assertEqual(misses, [], f"{len(misses)}/{total} misses:\n" + "\n".join(misses[:20]))


if __name__ == "__main__":
    unittest.main()
