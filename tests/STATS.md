# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-05T07:30:00Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **391/1166 100%**. Fails: 775. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi, yang_krut/yat palatal+Ay->Iy (cAy->cekIyya, 7.3.52), Nic mit/GawAdi hrasva (valaya) except kr+T (kraTa), liw satva blocked s+stop/final-k (siseke), liw periphrastic Am+AYcakre over-gen (day/kAs/kakKa), liw i-redup over-gen (vivyaTe), kta i-guna m+i+d (mid->medita, shape-based), kta w-final w+ta->wwa (kaw->kawwa, shape-based), yat I~ blocks except w-final to cross-match Ryat (kaw->kAwya, shape-based), Natva r/R+velar-final -> n->R for SAnac/anIyar/lyuw in mUla+nijanta+yananta (Srek->SrekamARa, shape-based), loT uttama eka ni->Ri for r/R+velar-final (rAK->rAKARi, shape-based, single-form).

## Fails (775)
| anta | n | example |
|---|---|---|
| krut | 4687 | 01.0038 krut/yat/M:atyaH |
| ting | 2783 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| nich_krut | 422 | 01.0050 nich_krut/kta/M:seDayitaH |
| san_krut | 361 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| yang_krut | 242 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| san | 215 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 197 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
| yangluk_krut | 6 | 01.0290 yangluk_krut/kta/M:lolupitaH |
