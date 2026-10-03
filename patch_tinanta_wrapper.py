with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

# We need to change `def derive(` to `def _derive_inner(`
# and add a new `def derive(` that calls `_derive_inner` and applies upasarga.

new_wrapper = """
    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        upasarga: Optional[str] = None,
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
        cands, log = self._derive_inner(dhatu, lakara, purusha, vacana, prayoga, upasarga, sanadi, dhatu_id, json_path, _force_pada, _cakz_bypass, _sad_c10_recurse)
        if upasarga:
            cands = [apply_upasargas(upasarga, c) for c in cands]
            return list(dict.fromkeys(cands)), log
        return cands, log

    def _derive_inner(
"""

content = content.replace("""
    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        upasarga: Optional[str] = None,
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        _force_pada: Optional[str] = None,
        _cakz_bypass: bool = False,
        _sad_c10_recurse: bool = False,
    ) -> Tuple[List[str], List[str]]:
""", new_wrapper)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Patched tinanta.py with derive wrapper")
