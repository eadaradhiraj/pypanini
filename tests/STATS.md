# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-10T03:50:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **936/1156 100%** (raw 946/1166). Fails: 220 scored (230 with 10 skipped). Net +43 matched tokens across 2 improved roots (0 worsened). New 100% passes: `01.0812 Gasx~` (881 -> 895), `01.0991 Sadx~` (866 -> 892).

## Rules (general, pure generative)
- Panini 6.4.98 *gamahanajanakhanaghasāṁ lopaḥ kṅityanaṅi* & 8.4.55 *khari ca*: In kit liṭ and kit yaṅanta (kta/ktavatu), `Gas` drops upadhā `a` to `Gs`, devoiced to `ks` before khar `s` (`jaksatuH`, `jaksuH`, `jaksaTuH`, `jaksa`, `jaksiva`, `jaksima`; yak liṭ `jakse`, `jaksAte`...; yaṅanta `jAksitaH`, `jAksitavAn`).
- Panini 7.3.78 *śadāṁ śīyadāḥ* & 1.3.60 *śaḍaḥ śīyateḥ*: `Sad` takes `SIyad` before Śit sārvadhātuka affix and is exclusively Ātmanepada in Sārvadhātuka lakāras (`SIyate`, `SIyatAm`, `aSIyata`, `SIyeta`), and takes Śānac (`SIyamAnaH`) rather than Śatṛ in kartari mUla.
- Panini 7.1.78 *nābhyastācchaturguṇakṛtamanikartuśca*: Yaṅluk abhyasta `SASad` takes no num (`SASadat`, `SASadatI`, `SASadat`).
- Panini 8.4.2 *aṭkupvāṅnumvyavāye 'pi*: Dental `s` of `san` intervenes and blocks natva (`_nat = _natva_applies(sec)`), generating dental `riraMsamAnaH`, `riraMsanIyaH`, `riraMsanam` instead of retroflex `ṇ`.
- Panini 3.1.44 *cleḥ sic* & 8.2.26 *jhalo jhali*: Aniṭ Atmanepada luṅ prathama eka for roots where `s` of `sic` does not drop after non-jhal sounds (`_asb + "ta"` -> `araMsta`).
- Panini 6.4.37 *anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kniti* & 7.2.56 *uditto vā*: Anudātta roots `ram`, `yam`, `nam`, `gam` drop `m` before kit jhal `tvA` without dīrgha (`ratvA`, `ramitvA`; yaṅluk `raMratvA`, `raMramitvA`).
- Panini 7.3.77 *iṣu-gami-yamāṁ chaḥ* & 7.3.78 *pā-ghrā-dhmā-ṣṭhā-mnā-dāṇ-dṛśi-śṛ-ṣad-śadāṁ piba-jighra-dhama-tiṣṭha-mana-yaccha-paśya-ṛccha-dhau-śīyadāḥ*: Sārvadhātuka Śit suppletions for Śatṛ in kartari mUla (`gam` -> `gacCan`, `yam` -> `yacCan`, `pA` -> `piban`, `GrA` -> `jiGran`, `DmA` -> `Dam`, `sTA`/`zWA` -> `tizWan`, `mnA` -> `man`, `dAR`/`dA` -> `yacCan`, `dfS` -> `paSy`, `f` -> `fcCan`, `sad`/`zad` -> `sIdan`, `Sru` -> `SfRvan`/`SfRvatI`), 6.4.89 *guher dīrgho 'saṁpṛktasya* (`guh` -> `gUhan`), and 6.4.24 *aniditāṁ hala upadhāyāḥ kṅiti* nasal drop (`sanj` -> `sajan`, `ranj` -> `rajan`, `danS` -> `daSan`).
- Vārttika on 7.3.77 *yamir uparama eva cha-bhāva-bhāk* (SK 2353): Restricted `yam` -> `yacC` to non-Gaṭādi roots (`meta.get("antara") != "GawAdiH"`), preserving `01.0930 yama~ aparivezaRe` at 100.0% (`yaman`, `yamantI`, `yamat`).
- Panini 7.3.86 *puganta-laghūpadhasya ca* & 1.4.11 *saṁyoge guru*: In `kr-` onset roots for `yat`, laghūpadha guṇa applied before Ṇyat when vowel is followed by a single consonant (`kruS` -> `kroSyaH`, while cluster-guru `kruYc` stays `kruYcyaH` and `krap` stays `krapyaH`).
- Panini 7.4.66 *uraḥ*: `abhyasa_vowel = "a"` for `f`/`F` roots in `tinanta._reduplicated_stem` (`vfk` -> `vavfke` not `vivfke`, `Bfj` -> `baBfje`, `Dfj` -> `daDarja`, `Bfz` -> `baBarza`, etc.) across 63+ dhātus.
- Panini 8.3.59 *ādeśapratyayayoḥ* + 8.4.41 *ṣṭunā ṣṭuḥ*: satva & ṣṭutva on reduplication of `st` clusters from `zw` upadeśa (`zwuc` -> `tuzwuce`, `zwuB` -> `tuzwuBe`, `zwip` -> `tizwipe`, `zwep` -> `tizwepe`).
- Panini 3.1.36 *ijādeś ca gurumato 'nṛcchaḥ*: non-gurumat laghu `i`/`u` roots (`uK`, `iK`, `iw`, `uW`, `uh`, `uz`) take classical reduplicated liṭ (pit: `uvoKa`, `iyeKa`, `iyewa`, `uvoWa`; kit: `UKatuH`, `IKatuH`).
- Panini 7.4.70 *at ādeḥ* + 7.4.71 *tasmān nuṭ dvihalaḥ*: An-reduplication for `ṛ`-initial roots in liṭ (`fja` -> `Anfje`, `AnfjAte`, `Anfjire`).
- Panini 6.4.120 *ata ekahalmadhye 'nādeśāder liti*: kit liṭ et-tva + abhyāsa-lopa in Parasmaipada with root's own unreduced initial consonant `_init_c + "e" + _fc` (`Pal` -> `PelatuH`, `PeluH`, `PeliTa`, etc.).
- Panini 7.3.57 *san-litoḥ jeḥ*: kuttva `j` -> `g` for root `ji` (`01.0642`, `01.1096`) in liṭ (`jigAya`, `jigaya`, `jigyatuH`, `jigyuH`, `jigeTa`, `jigayiTa`, `jigyaTuH`, `jigya`, `jigyiva`, `jigyima`, `jigye`, etc.).

## Fails (2633 capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 1179 | 01.1048 krut/SAnac/M:sUrkzyyamARaH |
| ting | 736 | 01.1091 ting/luw/prathama/dvi:savtArO |
| yang_krut | 214 | 01.0199 yang_krut/kta/M:tostucitaH |
| yang | 148 | 01.1133 yang/lw/prathama/eka:sesvidyate |
| nich | 141 | 01.1129 nich/lw/prathama/eka:rABayati |
| nich_krut | 82 | 01.0249 nich_krut/Satf/M:Dfjayan |
| san_krut | 58 | 01.0588 san_krut/kta/M:IrzizyizitaH |
| yak | 35 | 01.1145 yak/ASIrliN/prathama/eka:krakzIzwa |
| san | 35 | 01.0588 san/lw/prathama/eka:Irdizyizati |
| san_yak | 5 | 01.0642 san_yak/lw/prathama/eka:jijizyate |
