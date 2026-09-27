def _adadi_atmane_joint(stem: str, ending: str) -> str:
    if not stem or not ending:
        return (stem or "") + (ending or "")
    _e0 = ending[0]
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
    return stem + ending

print(_adadi_atmane_joint('cakz', 'te'))
print(_adadi_atmane_joint('cakz', 'Ate'))
print(_adadi_atmane_joint('kaS', 'te'))
