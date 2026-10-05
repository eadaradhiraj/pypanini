import re

# 1. tinanta.py wrapper
with open("pypanini/tinanta.py", "r") as f:
    t = f.read()

t = t.replace(
"""        if upasarga:
            cands = [apply_upasargas(upasarga, c) for c in cands]""",
"""        if upasarga and not _force_pada:
            from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass
        
        cands, log = self._derive_inner(
            dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path,
            _force_pada, _cakz_bypass
        )
        if upasarga:
            cands = [apply_upasargas(upasarga, c) for c in cands]""")

# 2. tinanta.py nasal bug
t = t.replace('pada == "Atmanepadi")', '(pada == "Atmanepadi" and _force_pada is None))')
t = t.replace('pada == "Atmanepadi" or', '(pada == "Atmanepadi" and _force_pada is None) or')

with open("pypanini/tinanta.py", "w") as f: f.write(t)


# 3. krdanta.py wrapper
with open("pypanini/krdanta.py", "r") as f:
    k = f.read()

k = k.replace(
"""    def derive_krdanta(
        self, dhatu: str = "BU", pratyaya: str = "kta", sanadi: Optional[str] = None, upasarga: Optional[str] = None, dhatu_id: Optional[str] = None,
        _force_pada: Optional[str] = None
    ) -> Union[str, Dict[str, Union[str, List[str]]]]:
        v = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, dhatu_id, _force_pada)""",
"""    def derive_krdanta(
        self, dhatu: str = "BU", pratyaya: str = "kta", sanadi: Optional[str] = None, upasarga: Optional[str] = None, dhatu_id: Optional[str] = None,
        _force_pada: Optional[str] = None
    ) -> Union[str, Dict[str, Union[str, List[str]]]]:
        if upasarga and not _force_pada:
            from .pada_rules import PADA_MAP_ID, PADA_MAP_CLEAN
            if dhatu_id and dhatu_id in PADA_MAP_ID and upasarga in PADA_MAP_ID[dhatu_id]:
                _force_pada = PADA_MAP_ID[dhatu_id][upasarga]
            else:
                try:
                    meta = self._get_meta(dhatu, dhatu_id)
                    cl = meta.get("clean")
                    if cl and cl in PADA_MAP_CLEAN and upasarga in PADA_MAP_CLEAN[cl]:
                        _force_pada = PADA_MAP_CLEAN[cl][upasarga]
                except Exception: pass
        v = self._derive_krdanta_inner(dhatu, pratyaya, sanadi, dhatu_id, _force_pada)""")

# 4. krdanta.py pada override inside _derive_krdanta_inner
k = k.replace(
"""        if "pada" in meta:
            pada = meta["pada"]""",
"""        if "pada" in meta:
            pada = _force_pada or meta["pada"]""")

# 5. krdanta.py nasal bug
k = k.replace('pada == "Atmanepadi")', '(pada == "Atmanepadi" and _force_pada is None))')
k = k.replace('pada == "Atmanepadi" or', '(pada == "Atmanepadi" and _force_pada is None) or')

# 6. krdanta.py nijanta SAnac bug
old_yamAna = """                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    # curAdi nich SAnac mUla-delegation (mUla grades + base + ay-twin; additive)."""

new_yamAna = """                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    
                    _ay_base = sec + "amAna"
                    if (_natva_applies(orig_clean) or _natva_applies(sec)) and _ay_base.endswith("amAna"):
                        _ay_base = _ay_base[:-5] + "amARa"
                        
                    _ay_m = _ay_base + "H"
                    _ay_f = _ay_base[:-1]+"A" if _ay_base.endswith("a") else _ay_base+"A"
                    _ay_n = _ay_base + "m"
                    
                    m = [m, _ay_m]
                    f = [f, _ay_f]
                    n = [n, _ay_n]
                    
                    # curAdi nich SAnac mUla-delegation (mUla grades + base + ay-twin; additive)."""

k = k.replace(old_yamAna, new_yamAna)

with open("pypanini/krdanta.py", "w") as f: f.write(k)
print("Restored!")
