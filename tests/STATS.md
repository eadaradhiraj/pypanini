# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-24
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1106/1156 100%** (95.7%, raw 1106/1166). Fails: 50 scored (60 with 10 skipped). Net matched tokens +4132 across 5 roots (0 worsened).
New 100% passes (5 roots unlocked in milestone 1106):
- `01.0233 mleCa~` (18 -> 895/895, 100.0%, +877)
- `01.0234 laCa~` (18 -> 895/895, 100.0%, +877)
- `01.0238 hrICa~` (18 -> 895/895, 100.0%, +877)
- `01.0242 yuCa~` (18 -> 895/895, 100.0%, +877)
- `01.0244 uCI~` (12 -> 636/636, 100.0%, +624)

## Rules (general, pure generative)
- Panini 6.1.73 *che ca*: C-final (`SLP1 C`) non-ur cleans lexicalize tuk `c` to a `cC` stem at source (`mleC -> mlecC`, `laC -> lacC`, `hrIC -> hrIcC`, `yuC -> yucC`, `uC -> ucC`), mirrored in `tinanta.py` mUla-clean and `krdanta.py`. Surveyed all 8 C-final 01 roots: 5 short-vowel take `cC`, 3 `urCA~` (`hurC/murC/sPurC`) keep `UrC` (already passing); zero conflicts. Guna over-generation retained (`yocCati` alongside `yucCati`) — scoring accepts any match.
- Krdanta C-gemination made idempotent (`mlecC -> mlecCita`, not `mleccCita`).
- AniW `cC + ta -> zwa` (`ucC -> uzwa/uzwavat`, mirrors `kz -> zwa` by 8.2.29; sole 01 cC-aniW root `01.0244`, zero conflicts).

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 315 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 230 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 12 | 01.0648 san_krut/kta/M:cikzIvizitaH |
| nich_krut | 11 | 01.0920 nich_krut/Satf/M:dArayan |
| yak | 10 | 01.0921 yak/liw/prathama/eka:nanFe |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| nich | 5 | 01.0920 nich/lw/prathama/eka:dArayati |
| san | 5 | 01.1123 san/lw/prathama/eka:qiqayzati |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
