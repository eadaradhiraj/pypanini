import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

injection = """        if clean == "de" and lakara == "luN" and prayoga == "kartari" and sanadi is None:
            _de_lun = {
                "prathama": {"eka": ["adita"], "dvi": ["adizAtAm"], "bahu": ["adizata"]},
                "madhyama": {"eka": ["adiTAH"], "dvi": ["adizATAm"], "bahu": ["adiQvam", "adiDvam"]},
                "uttama": {"eka": ["adizi"], "dvi": ["adizvahi"], "bahu": ["adizmahi"]},
            }
            return list(dict.fromkeys(_de_lun[purusha][vacana])), []
        # cakziN -> KyA/kSA in Ardhadhatuka (Panini 2.4.54/55)
        if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN") and sanadi is None and not kwargs.get("_cakz_bypass"):
            _cakz_cands = []
            if lakara == "liw":
                # optional in liw, so get base cakz forms too by bypassing this interception
                _cakz_cands, _ = self.derive("cakz", lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada=_force_pada, _cakz_bypass=True)
            # KyA/kSA are ubhayapadi, generate both
            _kya_p, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", json_path, _force_pada="parasmEpadi")
            _kya_a, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", json_path, _force_pada="Atmanepadi")
            _ksa_p = [c.replace("Ky", "kS") for c in _kya_p]
            _ksa_a = [c.replace("Ky", "kS") for c in _kya_a]
            cands = _cakz_cands + _kya_p + _kya_a + _ksa_p + _ksa_a
            return list(dict.fromkeys(cands)), []"""

old_block = """        if clean == "de" and lakara == "luN" and prayoga == "kartari" and sanadi is None:
            _de_lun = {
                "prathama": {"eka": ["adita"], "dvi": ["adizAtAm"], "bahu": ["adizata"]},
                "madhyama": {"eka": ["adiTAH"], "dvi": ["adizATAm"], "bahu": ["adiQvam", "adiDvam"]},
                "uttama": {"eka": ["adizi"], "dvi": ["adizvahi"], "bahu": ["adizmahi"]},
            }
            return list(dict.fromkeys(_de_lun[purusha][vacana])), []
        # cakziN -> KyA/kSA in Ardhadhatuka (Panini 2.4.54/55)
        if meta.get("op") == "cakziN" and lakara in ("liw", "luw", "lfw", "lfN", "ASIrliN", "luN") and sanadi is None:
            _cakz_cands = []
            if lakara == "liw":
                # optional in liw, so get base cakz forms too by bypassing this interception
                # we change op to bypass the interception
                _cakz_cands, _ = self.derive("cakz", lakara, purusha, vacana, prayoga, sanadi, "fake", json_path, _force_pada=_force_pada)
            # KyA/kSA are ubhayapadi, generate both
            _kya_p, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", json_path, _force_pada="parasmEpadi")
            _kya_a, _ = self.derive("KyA", lakara, purusha, vacana, prayoga, sanadi, "02.0055", json_path, _force_pada="Atmanepadi")
            _ksa_p = [c.replace("Ky", "kS") for c in _kya_p]
            _ksa_a = [c.replace("Ky", "kS") for c in _kya_a]
            cands = _cakz_cands + _kya_p + _kya_a + _ksa_p + _ksa_a
            return list(dict.fromkeys(cands)), []"""

if old_block in content:
    content = content.replace(old_block, injection)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find block")
