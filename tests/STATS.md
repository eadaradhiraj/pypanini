# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-24
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1101/1156 100%** (95.2%, raw 1101/1166). Fails: 55 scored (65 with 10 skipped). Net matched tokens +5370 across 6 roots (0 worsened).
New 100% passes (6 roots unlocked in milestone 1101):
- `01.0760 kAkzi~` (0 -> 895/895, 100.0%, +895)
- `01.0761 vAkzi~` (0 -> 895/895, 100.0%, +895)
- `01.0762 mAkzi~` (0 -> 895/895, 100.0%, +895)
- `01.0763 drAkzi~` (0 -> 895/895, 100.0%, +895)
- `01.0764 DrAkzi~` (0 -> 895/895, 100.0%, +895)
- `01.0765 DvAkzi~` (0 -> 895/895, 100.0%, +895)

## Rules (general, pure generative)
- Panini 7.1.58 + 8.3.24 kz-num placement: idit `*Akzi~` with `base_wo_i` ending in `kz` inserts velar `N` before the `kz` cluster (`kAkz -> kANkz`), homorganic with `k` — not before final `z` (`kAkNz` was wrong). Surveyed all 7 `*kzi` dataset roots: 6 `*Akzi~` take `ANkz`, sole `01.0269 kzi` (no `~`, aniW) keeps `kzay-`; zero conflicts. Applied in `tinanta.py` mUla-num and mirrored in `krdanta.py`.

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 350 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 255 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 12 | 01.0648 san_krut/kta/M:cikzIvizitaH |
| nich_krut | 11 | 01.0920 nich_krut/Satf/M:dArayan |
| yak | 10 | 01.0921 yak/liw/prathama/eka:nanFe |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| nich | 5 | 01.0920 nich/lw/prathama/eka:dArayati |
| san | 5 | 01.1123 san/lw/prathama/eka:qiqayzati |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
