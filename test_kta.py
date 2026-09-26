from pypanini.krdanta import KrdantaEngine
KE = KrdantaEngine()
meta = KE._get_meta('SrE', '01.1067')
print(meta['clean'])
op_for_kta = meta.get("op", "")
print(op_for_kta)
sew = str(meta.get("sew_raw", "")).strip() == "sew"
print(sew)
stem = KE._kta_stem(meta['clean'], sew, op_for_kta, is_idit=meta.get("is_idit", False))
print(stem)
