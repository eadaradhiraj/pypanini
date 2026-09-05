# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-05T09:40:00Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **420/1166 100%**. Fails: 746. See tests/sweep_all.csv (grep).

## Rules (general, pure generative)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi (kr-onset no-vriddhi krapya, kr+T blocks yat), yang_krut/yat palatal+Ay->Iy, Nic mit/GawAdi hrasva except kr+T + single-r allows vriddhi (tsar->tsAraya), liw satva blocked s+stop/final-k, liw periphrastic Am+AYcakre, liw i-redup, kta i-guna m+i+d, kta w-final w+ta->wwa, yat I~ except w-final, Natva r/R+velar/labial/r-final, loT ni->Ri r/R+velar/labial/r-final, sannanta voicing ti/di.

## Fails (746)
| anta | n | example |
|---|---|---|
| krut | 4539 | 01.0635 krut/yat/M:tsaryaH |
| ting | 2767 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| san_krut | 369 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| nich_krut | 270 | 01.0050 nich_krut/kta/M:seDayitaH |
| san | 215 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 180 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| yang_krut | 141 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yangluk_krut | 33 | 01.0290 yangluk_krut/kta/M:lolupitaH |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
