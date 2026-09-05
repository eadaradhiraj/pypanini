# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-05T05:42:59Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **374/1166 100%**. Fails: 792. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi, yang_krut/yat palatal+Ay->Iy (cAy->cekIyya, 7.3.52), Nic mit/GawAdi hrasva (valaya) except kr+T (kraTa), liw satva blocked s+stop/final-k (siseke), liw periphrastic Am+AYcakre over-gen (day/kAs/kakKa), liw i-redup full over-gen for a-roots (vyaTa->vivyaTe alongside vavyaTe).

## Fails (792)
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 2790 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| nich_krut | 499 | 01.1006 krut/kta/M:miditaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| yang_krut | 242 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| san | 215 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 197 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayate |

### Next >=97%
- 01.1006 877/895 98.0% | krut/kta/M:miditaH | krut/kta/F:miditA | krut/kta/N:miditam | krut/ktavatu/M:miditavAn | krut/ktavatu/F:miditavatI | krut/ktavatu/N:miditavat | nich_krut/kta/M:miditaH |
- 01.0359 871/895 97.3% | krut/kta/M:kawtaH | krut/kta/F:kawtA | krut/kta/N:kawtam | krut/ktavatu/M:kawtavAn | krut/ktavatu/F:kawtavatI | krut/ktavatu/N:kawtavat | krut/yat/M:kawyaH | krut/yat/F:k
