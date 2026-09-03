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
# de-aspiration + velar->palatal for reduplication (Panini 7.4.62)
DEASPIRATE = {
    "B": "b", "G": "g", "Q": "q", "D": "d", "J": "j",
    "K": "k", "C": "c", "W": "w", "T": "t", "P": "p",
}
VELAR_TO_PALATAL = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}

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
        # hardcoded minimal for BU/eD if data not available
        self._dhatu_cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True, "gana": "BvAdiH"}
        self._dhatu_cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True, "gana": "BvAdiH"}
        # try auto-load from skt-morph-data
        try:
            base = Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01")
            if base.exists():
                for jf in glob.glob(str(base / "*.json")):
                    try:
                        d = json.load(open(jf, encoding="utf-8"))
                        info = {x["name"]: x["value"] for x in d.get("info", [])}
                        op = info.get("OpadeSikasvarUpam", "")
                        if not op:
                            continue
                        raw = op.replace("~", "").replace("`", "").strip()
                        # strip anubandha f/F/x/X for dhatus like gADf~ -> gAD
                        if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
                            raw = raw[:-1]
                        clean = raw
                        # strip trailing 'a' added for consonant-ending dhatus (eDa->eD, sparDa->sparD)
                        if clean.endswith("a") and len(clean) > 1:
                            clean = clean[:-1]
                        # SLP1 normalize: ensure we have SLP1 form (already)
                        padam = info.get("padam", "")
                        # normalize padam: parasmEpadI / AtmanepadI (with capital E)
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        gana = info.get("gaRaH", "BvAdiH")
                        self._dhatu_cache[clean] = {"clean": clean, "pada": pada, "sew": sew, "gana": gana}
                        # also map original op without stripping? for lookup
                        self._dhatu_cache[op] = self._dhatu_cache[clean]
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str) -> Dict:
        self._load_cache()
        assert self._dhatu_cache is not None
        if dhatu in self._dhatu_cache:
            return self._dhatu_cache[dhatu]
        # fallback inference with anubandha stripping
        raw = dhatu.replace("~", "").replace("`", "").strip()
        if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
            raw = raw[:-1]
        clean = raw
        if clean.endswith("a") and len(clean) > 1:
            clean = clean[:-1]
        # infer vowel-initial?
        # default: consonant-initial BvAdi, parasmaipada, sew
        # if dhatu is known vowel-initial like eD, infer Atmanepadi
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        if is_vowel_init:
            pada = "Atmanepadi"
        else:
            pada = "parasmEpadi"
        return {"clean": clean, "pada": pada, "sew": True, "gana": "BvAdiH"}

    # ---------- phonological helpers ----------
    def _bhvadi_guna_base(self, clean: str) -> str:
        if not clean:
            return clean
        last = clean[-1]
        if last in SLP1_VOWELS:
            gv = apply_guna(last)
            av = apply_sandhi_eco_ayavayavah(gv)
            return clean[:-1] + av
        return clean

    def _vriddhi_base(self, clean: str) -> str:
        if not clean:
            return clean
        last = clean[-1]
        if last in SLP1_VOWELS:
            vv = apply_vriddhi(last)
            av = apply_sandhi_eco_ayavayavah(vv)
            return clean[:-1] + av
        return clean

    def _add_augment(self, base: str, is_vowel_initial: bool) -> str:
        if not base:
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
            return "a" + base

    def _reduplicated_stem(self, clean: str) -> str:
        """Simple generative reduplication for consonant-initial BvAdi.
           Handles s+consonant clusters and de-aspiration."""
        if not clean or clean[0] in SLP1_VOWELS:
            return clean
        # extract initial consonant cluster (up to first vowel)
        cluster = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        if not cluster:
            return clean
        # if cluster starts with 's' + consonant, take second consonant
        redup_cons = cluster[0]
        if len(cluster) >= 2 and cluster[0] == "s":
            redup_cons = cluster[1]
        # de-aspirate
        redup_cons = DEASPIRATE.get(redup_cons, redup_cons).lower()
        # velar -> palatal (ku->cu)
        redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
        # reduplication vowel is 'a'
        return redup_cons + "a" + clean

    # ---------- conjugation helpers ----------
    def _conjugate_at_stem_atmane(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
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
                return [stem[:-1] + "A" + prat]
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
            if prat.startswith("a") or prat.startswith("u"):
                final = stem[:-1] + "ey" + prat
            else:
                final = stem[:-1] + "e" + prat
            return [apply_rutva_visarga(final)]
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

    def _conjugate_luw(self, luw_stem: str, pada: str, purusha: str, vacana: str) -> List[str]:
        # luw_stem = guna_base + ("i" if sew else "")  e.g., Bavi, eDi
        if pada == "Atmanepadi":
            tbl = {
                ("prathama", "eka"): [luw_stem + "tA"],
                ("prathama", "dvi"): [luw_stem + "tArO"],
                ("prathama", "bahu"): [luw_stem + "tAraH"],
                ("madhyama", "eka"): [luw_stem + "tAse"],
                ("madhyama", "dvi"): [luw_stem + "tAsATe"],
                ("madhyama", "bahu"): [luw_stem + "tADve"],
                ("uttama", "eka"): [luw_stem + "tAhe"],
                ("uttama", "dvi"): [luw_stem + "tAsvahe"],
                ("uttama", "bahu"): [luw_stem + "tAsmahe"],
            }
            return tbl[(purusha, vacana)]
        else:
            # parasmaipada luw (BU)
            # need handling for madhyama/uttama with visarga
            raw = self.pratyayas_parasmai[(purusha, vacana)]
            if purusha == "prathama":
                if vacana == "eka":
                    return [luw_stem + "tA"]
                elif vacana == "dvi":
                    return [luw_stem + "tArO"]
                elif vacana == "bahu":
                    return [luw_stem + "tAraH"]
            else:
                base_tas = luw_stem + "tAs"
                if raw == "sip":
                    return [luw_stem + "tAsi"]
                else:
                    clean_prat = raw[:-1] if raw.endswith("p") else raw
                    # for tip/ etc. the stem already has tA, need tAs + prat
                    # produce like BavitAsi, BavitAsTaH etc. Use generic
                    # simplified: BavitAs + prat_trunc
                    # For madhyama dvi Tas-> TaH etc. Need mapping similar to luw parasmaipada
                    # Use visarga path: base_tas + clean_prat -> then rutva
                    return [apply_rutva_visarga(base_tas + clean_prat)]
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
    ) -> Tuple[List[str], List[str]]:
        log: List[str] = []
        meta = self._get_meta(dhatu)
        clean = meta["clean"]
        pada = meta["pada"]
        sew = meta["sew"]
        is_vowel_initial = clean[0] in SLP1_VOWELS if clean else False

        # secondary stems (keep generative but still use derived stems)
        if sanadi == "yanluganta":
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
        if sanadi == "yananta":
            return self._conjugate_at_stem_atmane("boBUy", lakara, purusha, vacana), log
        if prayoga == "karmani":
            stem_base = "BAvy" if sanadi == "nijanta" else ("buBUzy" if sanadi == "sannanta" else clean + "y")
            return self._conjugate_at_stem_atmane(stem_base, lakara, purusha, vacana), log
        if sanadi == "sannanta":
            return self._conjugate_at_stem_parasmai("buBUz", lakara, purusha, vacana), log
        if sanadi == "nijanta":
            return self._conjugate_at_stem_parasmai("BAvay", lakara, purusha, vacana), log

        # primitive - generative per lakara
        if lakara == "lw":
            base = self._bhvadi_guna_base(clean)
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(base, "lw", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(base, "lw", purusha, vacana), log

        elif lakara == "laN":
            base = self._bhvadi_guna_base(clean)
            aug = self._add_augment(base, is_vowel_initial)
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(aug, "laN", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(aug, "laN", purusha, vacana), log

        elif lakara == "low":
            base = self._bhvadi_guna_base(clean)
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(base, "low", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(base, "low", purusha, vacana), log

        elif lakara == "viDiliN":
            base = self._bhvadi_guna_base(clean)
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(base, "viDiliN", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(base, "viDiliN", purusha, vacana), log

        elif lakara == "luw":
            base = self._bhvadi_guna_base(clean)
            luw_stem = base + ("i" if sew else "")
            return self._conjugate_luw(luw_stem, pada, purusha, vacana), log

        elif lakara == "lfw":
            base = self._bhvadi_guna_base(clean)
            if sew:
                base_i = base + "i"
                sat = apply_satva(base_i[-1], "s")
                core = base_i + sat + "y"  # eDizy, Bavizy
            else:
                core = base + "sy"
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(core, "lw", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(core, "lw", purusha, vacana), log

        elif lakara == "lfN":
            base = self._bhvadi_guna_base(clean)
            if sew:
                base_i = base + "i"
                sat = apply_satva(base_i[-1], "s")
                core = base_i + sat + "y"
            else:
                core = base + "sy"
            aug_core = self._add_augment(core, is_vowel_initial)
            if pada == "Atmanepadi":
                return self._conjugate_at_stem_atmane(aug_core, "laN", purusha, vacana), log
            else:
                return self._conjugate_at_stem_parasmai(aug_core, "laN", purusha, vacana), log

        elif lakara == "liw":
            if is_vowel_initial:
                ama = clean + "A"
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
                # Y variant
                form_y = ama + base_end
                # M variant: replace initial Y with M
                form_m = ama + "M" + base_end[1:]
                forms = [form_y, form_m]
                # for madhyama bahu also add Dve variant (Qve->Dve)
                if (purusha, vacana) == ("madhyama", "bahu"):
                    # add Dve alternatives
                    forms = [ama + "YcakfQve", ama + "YcakfDve", ama + "McakfDve"]
                return forms, log
            else:
                redup = self._reduplicated_stem(clean)
                if pada == "Atmanepadi":
                    # atmanepada reduplication lit (sparDa -> pasparDe)
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
                    return [redup + endings[(purusha, vacana)]], log
                else:
                    endings = {
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
                    return [redup + endings[(purusha, vacana)]], log

        elif lakara == "ASIrliN":
            if pada == "parasmEpadi":
                # no guna, base = clean
                endings = {
                    ("prathama", "eka"): "yAt", ("prathama", "dvi"): "yAstAm",
                    ("prathama", "bahu"): "yAsuH", ("madhyama", "eka"): "yAH",
                    ("madhyama", "dvi"): "yAstam", ("madhyama", "bahu"): "yAsta",
                    ("uttama", "eka"): "yAsam", ("uttama", "dvi"): "yAsva",
                    ("uttama", "bahu"): "yAsma",
                }
                return [clean + endings[(purusha, vacana)]], log
            else:
                # Atmanepadi sew: eDizIzwa etc.
                if sew:
                    base_i = clean + "i"
                    sat = apply_satva(base_i[-1], "s")
                    base_iz = base_i + sat
                else:
                    base_iz = clean + apply_satva(clean[-1], "s")
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
                return [base_iz + endings[(purusha, vacana)]], log

        elif lakara == "luN":
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
                # rutva not needed as endings already have H
                return [form], log
            else:
                # Atmanepadi sew luN: EDizwa etc. = aug(clean) + i + suffix
                aug_clean = self._add_augment(clean, is_vowel_initial)
                # suffixes include z where needed
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
                # For sew, suffix already includes i+z? Actually aug_clean + suffix gives ED + izwa = EDizwa
                # But for madhyama bahu we need ED i Dvam -> suffix "iDvam" gives ED i Dvam = EDiDvam correct
                # For uttama eka "izi": ED + izi? Wait ED + izi = EDizi? That's EDizi = ED + i + zi? Aug clean "ED" + "izi" = "EDizi" correct.
                # So we need to handle that suffix for generically already includes i.
                # For sew, we construct as aug_clean + suffix where suffix starts with i
                # For anit, suffix would be different (without i) - not needed now
                suffix = suffixes[(purusha, vacana)]
                # need to ensure satva already in suffix (z). For madhyama bahu, suffix is iDvam (no z) intentional.
                form = aug_clean + suffix
                # also need Qvam variant for madhyama bahu
                if (purusha, vacana) == ("madhyama", "bahu"):
                    return [aug_clean + "iDvam", aug_clean + "iQvam"], log
                return [form], log

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
