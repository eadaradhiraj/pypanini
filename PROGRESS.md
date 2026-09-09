# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-09T23:10:00Z
Sweep: 927/1156 100% (raw 937/1166)

## Done
- Panini 7.4.66 *uraḥ*: `abhyasa_vowel = "a"` for `f`/`F` roots in `tinanta._reduplicated_stem`, generating correct Pāṇinian reduplication (`vfk` -> `vavfke` not `vivfke`, `Bfj` -> `baBfje`, `Dfj` -> `daDarja`, `Bfz` -> `baBarza`, etc.) across 63+ dhātus.
- Panini 8.3.59 *ādeśapratyayayoḥ* + 8.4.41 *ṣṭunā ṣṭuḥ*: satva & ṣṭutva on reduplication of `st` clusters from `zw` upadeśa (`zwuc` -> `tuzwuce`, `zwuB` -> `tuzwuBe`, `zwip` -> `tizwipe`, `zwep` -> `tizwepe`).
- Panini 3.1.36 *ijādeś ca gurumato 'nṛcchaḥ*: non-gurumat laghu `i`/`u` roots (`uK`, `iK`, `iw`, `uW`, `uh`, `uz`) take classical reduplicated liṭ (pit: `uvoKa`, `iyeKa`, `iyewa`, `uvoWa`; kit: `UKatuH`, `IKatuH`).
- Panini 7.4.70 *at ādeḥ* + 7.4.71 *tasmān nuṭ dvihalaḥ*: An-reduplication for `ṛ`-initial roots in liṭ (`fja` -> `Anfje`, `AnfjAte`, `Anfjire`).
- Panini 6.4.120 *ata ekahalmadhye 'nādeśāder liti*: kit liṭ et-tva + abhyāsa-lopa in Parasmaipada with root's own unreduced initial consonant `_init_c + "e" + _fc` (`Pal` -> `PelatuH`, `PeluH`, `PeliTa`, etc.).
- Panini 7.3.57 *san-litoḥ jeḥ*: kuttva `j` -> `g` for root `ji` (`01.0642`, `01.1096`) in liṭ (`jigAya`, `jigaya`, `jigyatuH`, `jigyuH`, `jigeTa`, `jigayiTa`, `jigyaTuH`, `jigya`, `jigyiva`, `jigyima`, `jigye`, etc.).
- Full Sweep Results: **927/1156 100% passes** (raw 937/1166), 1 new 100% pass (`01.1153 vadI~`), **76 improved roots (+1,013 net tokens)**, **strictly 0 worsened roots**. All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) held at 100.0%. Ting misses dropped from 842 to 748 (-94 misses).
- Kartari Śānac (Panini 3.2.124 / 1.4.100) generative derivation: 445/445 (100.0%) roots matched in dataset. Passive yak+Śānac for Parasmaipada roots (preserving `clean + yamAna` with naṭva `yamARa`, plus 6.1.15 samprasāraṇa `vas` -> `uzyamARa`). Monosyllabic `i`/`I` root protection (`smi` 01.1099, `qI` 01.1123).

## Next
1. Target remaining `ting` misses (748 misses across remaining dhātus: e.g. `luw` periphrastic futures, `lw` class exceptions).
2. Target `krut` misses (1201 misses: e.g. `Satf` present active participles).
3. Push passes past 935 toward 950/1156.
