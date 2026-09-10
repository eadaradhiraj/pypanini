# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-10T05:35:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **950/1156 100%** (raw 950/1166). Fails: 206 scored (216 with 10 skipped). Net +374 matched tokens across 2 improved roots (0 worsened). New 100% passes (2): `01.1129 rABa~` (695 -> 883/883, 100.0%, +188 tokens), `01.1130 qulaBa~z` (697 -> 883/883, 100.0%, +186 tokens).

## Rules (general, pure generative)
- Panini 7.1.63 *rabher a-śab-liṭoḥ* & 7.1.64 *labheś ca*: `raB` and `laB` take `num` augment (`ramB`, `lamB`) everywhere except before `śap` (kartari sārvadhātuka) and `liṭ`. Governs ṇijanta tinanta (`ramBayati`/`ramBayate`, `lamBayati`/`lamBayate`), karmaṇi ṇijanta (`ramByate`, `lamByate`), ṇijanta kṛdanta (`ramBayitA`, `ramBayitavya`...), and primitive kṛdantas (`ramBakaH`/`lamBakaH` in ṇvul, `ramBaRam`/`lamBanam` in lyuṭ, `ramBaRIyaH`/`lamBanIyaH` in anīyar).
- Panini 7.1.67 *upasargāt khal-ghañoḥ*: For `laB`, `num` augment in khal and ghañ is conditioned on an upasarga (*anupasarge tu na*). Therefore, simplex `laB` without upasarga in ghañ takes no num, undergoing regular vṛddhi by 7.2.116 *ata upadhāyāḥ* to `lABaH`, whereas `raB` takes num by 7.1.63 yielding `ramBaH`.
- Panini 3.1.98 *por adupadhāt*: Roots ending in pavarga with short `a` upadhā take `yat` affix (without vṛddhi) rather than `ṇyat`, generating `raByaH`/`raByA`/`raByam` and `laByaH`/`laByA`/`laByam`.
- Panini 6.4.77 *aci śnu-dhātu-bhruvāṁ yvo riyaṅ-uvaṅau*: In Ātmanepada Liṭ and Karmani Liṭ, roots ending in `u`/`U` take `uvaṅ` (`uv`) before vowel-initial endings (`e`, `Ate`, `ire`, `ize`, `ATe`, `iDve`, `e`, `ivahe`, `imahe`), producing `mumuve`, `mumuvAte`, `mumuvire`, `mumuvize`, `mumuvATe`, `mumuvvahe` / `mumuviQve` for `mU` and `pU`.
- Panini 6.4.48 *ato lopaḥ* & 6.4.49 *yaḥ sya halaḥ*: In ārdhadhātuka affixes for Yaṅanta, *ato lopaḥ* drops final `at` (`a`) leaving `y`. By 6.4.49 *halaḥ*, the `y` is deleted only after consonants (*hal*). Thus, genuine vowel roots (*ac-anta*) retain the `y` of Yaṅanta (`momUy-` -> `momUyitaH`, `momUyitavAn`, `momUyitavyaH`, `momUyanIyaH`, `momUyAYcakre`), whereas consonant roots (*hal-anta*, including idit roots `sraki~` and y-ending roots `vay`, `pay`) delete `y` (`sAsraNkitaH`, `vAvayitaH`, `vAvayAYcakre`).
- Panini 6.4.92 *mitāṁ hrasvaḥ* & 1.1.48 *eca igghrasvādeśe*: In ṇi (ṇijanta), `mit` roots shorten the vowel. For roots with penultimate `ec` (`e`), `ik` (`i`) is substituted, shortening `heq` -> `hiqay-` across sārvadhātuka and ārdhadhātuka lakāras and kṛdantas (`hiqayati`, `hiqayate`, `hiqyate`, `hiqayitavya`, `hiqitA`, `hiqayan`...).
- Panini 7.3.36 *arti-hrī-vlī-rī-knūyī-kṣmāyyāṁ puṅ ṇau*: Roots `knUy` (`01.0558`) and `kzmAy` (`01.0559`) take `puk` (`puṅ`) augment before `ṇi`, yielding `knopay-` (by 7.3.86 laghūpadha guṇa) and `kzmApay-` across all tinanta and kṛdanta formations (`knopayati`, `knopayate`, `knopyate`, `kzmApayati`, `kzmApayate`, `kzmApyate`, `knopayitavya`, `kzmApayitavya`...).
- Panini 6.1.22 *sphāyaḥ spho vā* / Vārttika on 7.3.39 *sphāyo vuk*: Root `sPAy` (`01.0560`) takes `vuk` augment before `ṇi`, generating `sPAvay-` (`sPAvayati`, `sPAvayate`, `sPAvyate`, `sPAvayitavya`, `prasPAvya`...).
- Panini 7.4.1 *ṇau caṅy upadhāyā hrasvaḥ*, 7.4.61 *śarpūrvāḥ khayaḥ*, 7.4.62 *kuhoś cuḥ*, 7.4.93 *sanval laghuni*, 7.4.94 *dīrgho laghoḥ*: Algorithmic Caṅ Reduplicated Aorist accepts `n_stem` with shortened penultimate vowel in `bases` (`knop` -> `knup`, `kzmAp` -> `kzmap`, `sPAv` -> `sPav`, `hiq` -> `hiq`) and produces both Parasmaipada (`at`, `atAm`, `an`...) and Ātmanepada (`ata`, `etAm`, `anta`...) caṅ aorist forms (`ajIhiqat`, `ajIhiqata`, `acuknupat`, `acuknupata`, `acikzmapat`, `acikzmapata`, `apisPavat`, `apisPavata`).
- Panini 6.1.73 *chē ca* & 8.4.40 *stoḥ ścunā ścuḥ*: Short vowel augment (`aṭ`) and short reduplication vowel (`abhyāsa` by 7.4.59 *hrasvaḥ*) before `ch` (`C`) take obligatory `tuk` augment (`t` -> `c`), generating `acC-` across all augmented lakāras (laṅ, luṅ, lṛṅ in ting, yak, and nich) and `cacC-` in liṭ (`acCamat`, `acCamyata`, `acCamIt`, `acCamizyat`, `acCAmayat`, `cacCAma`, `cacCama`, `cacCamatuH`, `cacCame`...). Also in `pra` prefix for lyap (`pracCamya`, `pracCamayya`).
- Panini 6.1.101 *akaḥ savarṇe dīrghaḥ* & 6.1.8 *liṭi dhātor anabhyāsasya*: In Ātmanepada / yak liṭ, short vowel-initial single-consonant roots take dīrgha reduplication (`iw` -> `Iwe`, `uz` -> `Uze`, `uK` -> `UKe`, `iK` -> `IKe`, `uW` -> `UWe`, `uh` -> `Uhe` / `UhiQve`).
- Panini 6.1.2 *ajāder dvitīyasya* & 7.3.86 *puganta-laghūpadhasya ca*: Laghūpadha vowel-initial roots take initial guṇa alongside second-syllable reduplication across sannanta tinanta (kartari & karmani) and krdanta (`uK` -> `ociKiz`, `iK` -> `eciKiz`, `uW` -> `owiWiz`, `uh` -> `ojihiz`, `iw` -> `ewiwiz`, `uz` -> `oziziz`).
- Panini 7.3.86 *puganta-laghūpadhasya ca*: Laghūpadha short `ik`-initial roots (`i`, `u`, `ṛ`, `ḷ` followed by single hal: `iw`, `uz`, `uK`, `iK`, `uW`, `uh`, `fj`) take guṇa before non-kit ārdhadhātuka affixes in `krdanta.py` (`tavya`, `anIyar`, `yat`/`Ryat`, `Rvul`, `tfc`, `lyuw`, `GaY`, `tumun`, and seṭ `ktvA` by 1.2.18 *na ktvā seṭ*).
- Panini 7.3.52 *cajoḥ ku ghiṇyatoḥ*: In `GaY`, final `j` becomes velar `g` (`fj` -> `argaH`).
- Panini 6.1.88 *vṛddhir eci*: In sannanta `lyap`, `pra` + initial guṇa vowel undergoes vṛddhi sandhi (`pra` + `ewiwizya` -> `prEwiwizya`, `pra` + `ozizizya` -> `prOzizizya`).
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

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 1087 | 01.1048 krut/SAnac/M:sUrkzyyamARaH |
| ting | 711 | 01.1091 ting/luw/prathama/dvi:savtArO |
| yang_krut | 212 | 01.0199 yang_krut/kta/M:tostucitaH |
| yang | 153 | 01.1133 yang/lw/prathama/eka:sesvidyate |
| nich | 111 | 01.0505 nich/lw/prathama/eka:vevayati |
| nich_krut | 78 | 01.0249 nich_krut/Satf/M:Dfjayan |
| san_krut | 65 | 01.0588 san_krut/kta/M:IrzizyizitaH |
| san | 40 | 01.0588 san/lw/prathama/eka:Irdizyizati |
| yak | 10 | 01.1145 yak/ASIrliN/prathama/eka:krakzIzwa |
| san_yak | 5 | 01.0642 san_yak/lw/prathama/eka:jijizyate |
