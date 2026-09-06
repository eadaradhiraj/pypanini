# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-06T00:00:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **531/1166 100%**. Fails: 635. See tests/sweep_all.csv (grep).

## Rules (general, pure generative)
- Anubandha, redup 7.4.62, yan e/o, kta I~ (blocked unless r/R in stem: urvI~/turvI~-cluster takes iT -> tUrvita), Nic aorist, krdanta guna, Satf urv-coda lengthening (turv/tUrv->tUrvan), liw Pit/Kit+e+final-cons + urv o/u-redup + a+r n-redup + idit-i num redups (An on numclean, redup(numclean)), yak e+final + yak-liw vriddhi-Atmane finite (ata->Ate, a+single-C minus j, 12 roots surveyed), yak-ASIrliN sannanta alt stems, luN at/guNa + seT Urv-base (atUrvIt) + num-base (ENgIt), ASIrliN D/Q + urv-lengthening (tUrvyAt) + num-base (iNgyAt), yat vriddhi (kr-onset no-vriddhi krapya, kr+T blocks yat, ts/km/kz-onset blocks yat), yang_krut/yat palatal+Ay->Iy, Nic mit/GawAdi hrasva except kr+T + single-r allows vriddhi, liw satva blocked s+stop/final-k, liw periphrastic Am+AYcakre + on numclean/numay (igi->iNgAYcakAra, agi->aNgayAYcakre), liw i-redup, kta i-guna m+i+d, kta w-final w+ta->wwa, yat I~ except w-final, Natva `_natva_applies` (z-final always R; h-final R iff r/R; s/S-final never R; else R iff r/R + velar/labial/sonorant final; R-final blocked), loT ni->Ri (r/R + velar/labial/sonorant/h/z/S final, or z-final always; s-final always dental; R-final blocked), sannanta Ci-copy stem with velar/h palatalization in redup + i-final velar/palatal Y-insertion + mUla/yak/san/nich/yang/yanluganta assimilated-num, sannanta voicing ti/di + redup-vowel o/O->u (loka->lulokizati; e-roots keep i), krdanta nijanta vowel-initial gate, krdanta yanluganta Y-class sec, harness keeps "-" as token.

## Fails (635)
| anta | n | example |
|---|---|---|
| krut | 3846 | 01.0690 krut/SAnac/M:BikzamARaH |
| ting | 2500 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| yak | 350 | 01.0640 yak/liw/prathama/eka:cacare |
| yang_krut | 256 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 203 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| san | 37 | 01.0300 san/lw/prathama/eka:eWiWizate |
| san_krut | 118 | 01.0050 san_krut/kta/M:sisiDiztaH |
| nich_krut | 60 | 01.0050 nich_krut/kta/M:seDayitaH |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
| yangluk_krut | 12 | 01.0290 yangluk_krut/kta/M:lolupitaH |
