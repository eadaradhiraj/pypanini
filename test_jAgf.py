from pypanini.krdanta import KrdantaEngine
KE = KrdantaEngine()
meta = KE._get_meta('jAgf', '02.0067')
clean = meta["clean"]
is_idit = meta.get("is_idit", False)
guna_base = KE._guna_base(clean, is_idit)
is_laghu_ik_init = (len(clean) == 1 and clean in ("i", "u", "f", "x")) or (len(clean) == 2 and clean[0] in ("i", "u", "f", "x") and clean[1] not in "aAiIuUfFxXeEoO")
print(f"{clean=} {guna_base=} {is_laghu_ik_init=}")
eff = guna_base if is_laghu_ik_init else (clean if (clean and clean[0] in "aAiIuUfFxXeEoO") or "Ur" in clean or "Ud" in clean else guna_base)
print(f"{eff=}")
