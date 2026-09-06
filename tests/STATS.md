# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-06T00:00:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **466/1166 100%**. Fails: 700. See tests/sweep_all.csv (grep).

## Rules (general, pure generative)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi (kr-onset no-vriddhi krapya, kr+T blocks yat, ts/km/kz-onset blocks yat), yang_krut/yat palatal+Ay->Iy, Nic mit/GawAdi hrasva except kr+T + single-r allows vriddhi, liw satva blocked s+stop/final-k, liw periphrastic Am+AYcakre, liw i-redup, kta i-guna m+i+d, kta w-final w+ta->wwa, yat I~ except w-final, Natva `_natva_applies` (z-final always R; h-final R iff r/R; s/S-final never R; else R iff r/R + velar/labial/sonorant final; R-final blocked), loT ni->Ri r/R+velar/labial/r-final/sibilant + kz-final + B-onset+z-coda (R-final uppercase blocks Ri), sannanta voicing ti/di, harness keeps "-" as token.

## Fails (700)
| anta | n | example |
|---|---|---|
| krut | 3895 | 01.0690 krut/SAnac/M:BikzamARaH |
| ting | 2723 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| san_krut | 459 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 275 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| yang_krut | 253 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| san | 220 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 198 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| nich_krut | 47 | 01.0050 nich_krut/kta/M:seDayitaH |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
| yangluk_krut | 15 | 01.0290 yangluk_krut/kta/M:lolupitaH |
