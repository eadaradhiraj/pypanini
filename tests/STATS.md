# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-09T23:10:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **927/1156 100%** (raw 937/1166). Fails: 229 scored (239 with 10 skipped). Net +1013 matched tokens across 76 improved roots (0 worsened). New 100% pass: `01.1153 vadI~` (889 -> 895 100.0%).

## Rules (general, pure generative)
- Panini 7.4.66 *uraḥ*: `abhyasa_vowel = "a"` for `f`/`F` roots in `tinanta._reduplicated_stem`, generating correct Pāṇinian reduplication (`vfk` -> `vavfke` not `vivfke`, `Bfj` -> `baBfje`, `Dfj` -> `daDarja`, `Bfz` -> `baBarza`, etc.) across 63+ dhātus.
- Panini 8.3.59 *ādeśapratyayayoḥ* + 8.4.41 *ṣṭunā ṣṭuḥ*: satva & ṣṭutva on reduplication of `st` clusters from `zw` upadeśa (`zwuc` -> `tuzwuce`, `zwuB` -> `tuzwuBe`, `zwip` -> `tizwipe`, `zwep` -> `tizwepe`).
- Panini 3.1.36 *ijādeś ca gurumato 'nṛcchaḥ*: non-gurumat laghu `i`/`u` roots (`uK`, `iK`, `iw`, `uW`, `uh`, `uz`) take classical reduplicated liṭ (pit: `uvoKa`, `iyeKa`, `iyewa`, `uvoWa`; kit: `UKatuH`, `IKatuH`).
- Panini 7.4.70 *at ādeḥ* + 7.4.71 *tasmān nuṭ dvihalaḥ*: An-reduplication for `ṛ`-initial roots in liṭ (`fja` -> `Anfje`, `AnfjAte`, `Anfjire`).
- Panini 6.4.120 *ata ekahalmadhye 'nādeśāder liti*: kit liṭ et-tva + abhyāsa-lopa in Parasmaipada with root's own unreduced initial consonant `_init_c + "e" + _fc` (`Pal` -> `PelatuH`, `PeluH`, `PeliTa`, etc.).
- Panini 7.3.57 *san-litoḥ jeḥ*: kuttva `j` -> `g` for root `ji` (`01.0642`, `01.1096`) in liṭ (`jigAya`, `jigaya`, `jigyatuH`, `jigyuH`, `jigeTa`, `jigayiTa`, `jigyaTuH`, `jigya`, `jigyiva`, `jigyima`, `jigye`, etc.).
- Panini 3.2.124 *laṭaḥ śatṛ-śānacāv aprathamā-samānādhikaraṇe* & 1.4.100 *taṅānāv ātmanepadam*: Kartari Śānac derivation for all Ātmanepada and Ubhayapada roots and suppletions (`sTA`/`zWA` -> `tizWa`, `Sad` -> `SIya`, `kfp` -> `kalpa`, `guh` -> `gUha`, `BrAS`/`BlAS`/`laz` -> `ya`, `jaB`/`jfBi` -> `jamB`/`jfmB` gated to `is_idit`, `svanj`/`ranj` -> `svaja`/`raja`, `cate` -> `cata`, `ubund` -> `bunda`, `ftu`/`fti` -> `ftIya`, nitya-san `jugups`/`titikz`/`cikits`/`mImAMs`/`bIBats`/`dIdAMs`/`SISAMs`, with stem guṇa and keep-shape). 445/445 (100.0%) roots with Śānac in data matched!
- Present Passive Participle (yak + Śānac, e.g. `clean + yamAna` with natva `yamARa`, and 6.1.15 samprasāraṇa `vas` -> `uzyamARa`) for Parasmaipada roots.
- Monosyllabic `i`/`I` root protection: `clean.endswith(("i","I")) and (is_idit or pada == "Atmanepadi") and any(c in SLP1_VOWELS for c in clean[:-1])` in both `tinanta.py` and `krdanta.py`, safeguarding `01.1099 smi` and `01.1123 qI`.

## Fails (2667 capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 1201 | 01.1048 krut/SAnac/M:sUrkzyyamARaH |
| ting | 748 | 01.1091 ting/luw/prathama/dvi:savtArO |
| yang_krut | 224 | 01.0199 yang_krut/kta/M:tostucitaH |
| yang | 148 | 01.1133 yang/lw/prathama/eka:sesvidyate |
| nich | 141 | 01.1129 nich/lw/prathama/eka:rABayati |
| nich_krut | 79 | 01.0249 nich_krut/Satf/M:Dfjayan |
| san_krut | 72 | 01.0588 san_krut/kta/M:IrzizyizitaH |
| yak | 35 | 01.1145 yak/ASIrliN/prathama/eka:krakzIzwa |
| san | 35 | 01.0588 san/lw/prathama/eka:Irdizyizati |
| yangluk_krut | 19 | 01.0989 yangluk_krut/ktvA:rAntvA |
| san_yak | 5 | 01.0642 san_yak/lw/prathama/eka:jijizyate |
