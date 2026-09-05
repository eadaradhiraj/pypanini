# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-05T08:30:00Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **412/1166 100%**. Fails: 754. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi, yang_krut/yat palatal+Ay->Iy (cAy->cekIyya, 7.3.52), Nic mit/GawAdi hrasva (valaya) except kr+T (kraTa), liw satva blocked s+stop/final-k (siseke), liw periphrastic Am+AYcakre over-gen (day/kAs/kakKa), liw i-redup over-gen (vivyaTe), kta i-guna m+i+d (mid->medita, shape-based), kta w-final w+ta->wwa (kaw->kawwa, shape-based), yat I~ blocks except w-final to cross-match Ryat (kaw->kAwya, shape-based), Natva r/R+velar/labial-final -> n->R for SAnac/anIyar/lyuw in mUla+nijanta+yananta (Srek/Garb, shape-based), loT uttama eka ni->Ri for r/R+velar/labial-final (rAK/Garb, shape-based), sannanta voicing ti/di for vowel-initial (atitiz vs aditiz, shape-based).

## Fails (754)
| anta | n | example |
|---|---|---|
| krut | 4515 | 01.0038 krut/yat/M:atyaH |
| ting | 2763 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| san_krut | 364 | 01.0038 san_krut/kta/M:aditizitaH |
| nich_krut | 338 | 01.0050 nich_krut/kta/M:seDayitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| yang_krut | 246 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| san | 215 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 198 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
| yangluk_krut | 9 | 01.0290 yangluk_krut/kta/M:lolupitaH |
