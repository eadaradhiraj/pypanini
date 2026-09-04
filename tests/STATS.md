# Generative Validation Stats (compact)

Engine: wholly generative (tinanta/krdanta from pada/sew/gana/vowel-initial, NO per-dhatu, NO JSON import).
Cross-check: skt-morph-data read-only.
Date: 2026-09-04T19:57:31Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **288/1166 100%**. Fails: 878. See table + tests/sweep_all.csv (grep, do not dump).

## How to validate
- Single: python tests/test_dhatu.py 01.0038
- Batch: sweep_gana --from/--to
- GRAND = tinanta + krdanta.
- Workflow: fix generally -> test -> unittest -> update STATS+PROGRESS -> commit & push.

## Algorithmic rules (general, do NOT re-add per-dhatu)
- Anubandha ~r/U~/I~/i~, s/S+stop, abhyasa e->i, yan e/o, kta I~, Nic aorist+vriddhi single-cons, krdanta guna, liw Pit/Kit, luN at/guNa, ASIrliN IDvam/IQvam, yat vriddhi single-cons no-r.

Passes table: see tests/sweep_all.csv pct==100 (too long for context, query via grep).

## Fails (878) by anta
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 3242 | 01.0049 ting/liw/madhyama/eka:siziDviTa |
| nich_krut | 757 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 268 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| san | 208 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang_krut | 199 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 137 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayate |

### Easiest next (>=97%)
- 01.1023 892/895 99.7% | yang_krut/yat/M:cAcAyyaH | yang_krut/yat/F:cAcAyyA | yang_krut/yat/N:cAcAyyam
- 01.0053 880/895 98.3% | ting/liw/prathama/dvi:babadvatuH | ting/liw/prathama/bahu:babadvuH | ting/liw/madhyama/eka:babadviTa | ting/liw/madhyama/dvi:babadvaTuH | ting/liw/utt
- 01.0055 880/895 98.3% | ting/liw/prathama/dvi:raradvatuH | ting/liw/prathama/bahu:raraduH | ting/liw/madhyama/eka:raradiTa | ting/liw/madhyama/dvi:raradaTuH | ting/liw/uttama
- 01.0124 880/895 98.3% | ting/liw/prathama/dvi:tatakvatuH | ting/liw/prathama/bahu:tatakvuH | ting/liw/madhyama/eka:tatakiTa | ting/liw/madhyama/dvi:tatakvaTuH | ting/liw/utta
- 01.0140 880/895 98.3% | ting/liw/prathama/dvi:mamaKvatuH | ting/liw/prathama/bahu:mamaKvuH | ting/liw/madhyama/eka:mamaKviTa | ting/liw/madhyama/dvi:mamaKvaTuH | ting/liw/utt
- 01.0146 880/895 98.3% | ting/liw/prathama/dvi:lalaKvatuH | ting/liw/prathama/bahu:lalaKvuH | ting/liw/madhyama/eka:lalaKviTa | ting/liw/madhyama/dvi:lalaKaTuH | ting/liw/utta
- 01.0185 880/895 98.3% | ting/liw/prathama/dvi:mamajatuH | ting/liw/prathama/bahu:mamajvuH | ting/liw/madhyama/eka:mamajviTa | ting/liw/madhyama/dvi:mamajaTuH | ting/liw/uttam
- 01.0253 880/895 98.3% | ting/liw/prathama/dvi:sasalatuH | ting/liw/prathama/bahu:sasaluH | ting/liw/madhyama/eka:sasaliTa | ting/liw/madhyama/dvi:sasalaTuH | ting/liw/uttama/
- 01.0271 880/895 98.3% | ting/liw/prathama/dvi:lalajvatuH | ting/liw/prathama/bahu:lalajuH | ting/liw/madhyama/eka:lalajiTa | ting/liw/madhyama/dvi:lalajvaTuH | ting/liw/uttam
- 01.0275 880/895 98.3% | ting/liw/prathama/dvi:jajajatuH | ting/liw/prathama/bahu:jajajuH | ting/liw/madhyama/eka:jajajviTa | ting/liw/madhyama/dvi:jajajaTuH | ting/liw/uttama
- 01.0333 880/895 98.3% | ting/liw/prathama/dvi:papawatuH | ting/liw/prathama/bahu:papawuH | ting/liw/madhyama/eka:papawiTa | ting/liw/madhyama/dvi:papawaTuH | ting/liw/uttama/
- 01.0334 880/895 98.3% | ting/liw/prathama/dvi:rarawvatuH | ting/liw/prathama/bahu:rarawuH | ting/liw/madhyama/eka:rarawiTa | ting/liw/madhyama/dvi:rarawvaTuH | ting/liw/uttam
- 01.0335 880/895 98.3% | ting/liw/prathama/dvi:lalawvatuH | ting/liw/prathama/bahu:lalawvuH | ting/liw/madhyama/eka:lalawviTa | ting/liw/madhyama/dvi:lalawvaTuH | ting/liw/utt
- 01.0336 880/895 98.3% | ting/liw/prathama/dvi:SaSawatuH | ting/liw/prathama/bahu:SaSawuH | ting/liw/madhyama/eka:SaSawviTa | ting/liw/madhyama/dvi:SaSawvaTuH | ting/liw/uttam
- 01.0342 880/895 98.3% | ting/liw/prathama/dvi:jajawvatuH | ting/liw/prathama/bahu:jajawuH | ting/liw/madhyama/eka:jajawiTa | ting/liw/madhyama/dvi:jajawvaTuH | ting/liw/uttam
