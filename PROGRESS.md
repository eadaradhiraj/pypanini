# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T04:05:00Z
Sweep: 942/1156 100% (raw 942/1166)

## Done
- Panini 6.1.101 *akaḥ savarṇe dīrghaḥ* & 6.1.8 *liṭi dhātor anabhyāsasya*: In Ātmanepada / yak liṭ, short vowel-initial single-consonant roots take dīrgha reduplication (`iw` -> `Iwe`, `uz` -> `Uze`, `uK` -> `UKe`, `iK` -> `IKe`, `uW` -> `UWe`, `uh` -> `Uhe` / `UhiQve`).
- Panini 6.1.2 *ajāder dvitīyasya* & 7.3.86 *puganta-laghūpadhasya ca*: Laghūpadha vowel-initial roots take initial guṇa alongside second-syllable reduplication across sannanta tinanta (kartari & karmani) and krdanta (`uK` -> `ociKiz`, `iK` -> `eciKiz`, `uW` -> `owiWiz`, `uh` -> `ojihiz`, `iw` -> `ewiwiz`, `uz` -> `oziziz`).
- Panini 7.3.86 *puganta-laghūpadhasya ca*: Laghūpadha short `ik`-initial roots (`i`, `u`, `ṛ`, `ḷ` followed by single hal: `iw`, `uz`, `uK`, `iK`, `uW`, `uh`, `fj`) take guṇa before non-kit ārdhadhātuka affixes in `krdanta.py` (`tavya`, `anIyar`, `yat`/`Ryat`, `Rvul`, `tfc`, `lyuw`, `GaY`, `tumun`, and seṭ `ktvA` by 1.2.18 *na ktvā seṭ*).
- Panini 7.3.52 *cajoḥ ku ghiṇyatoḥ*: In `GaY`, final `j` becomes velar `g` (`fj` -> `argaH`).
- Panini 6.1.88 *vṛddhir eci*: In sannanta `lyap`, `pra` + initial guṇa vowel undergoes vṛddhi sandhi (`pra` + `ewiwizya` -> `prEwiwizya`, `pra` + `ozizizya` -> `prOzizizya`).
- Full Sweep Results: **942/1156 100% passes** (raw 942/1166, 10 skipped), **6 new 100% passes** (`01.0136 uKa~`, `01.0148 iKa~`, `01.0357 iwa~`, `01.0392 uWa~`, `01.0792 uza~`, `01.0840 uhi~r`), **35 improved roots (+1,048 tokens)**, **STRICTLY 0 worsened roots**.
- All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) held at 100.0%.

## Next
1. Target remaining closest roots: `01.0541 Camu~` (777/895, gap=118), `01.0887 heqa~` (767/895, gap=128), `01.0558-01.0560 knUyI/kzmAyI/sPAyI` (749/883, gap=134), `01.1122 mUN` (735/883, gap=148).
2. Target `krut/tavya` and `krut/anIyar` (1,102 misses across Gaṇa 01).
3. Target remaining `ting` misses (736 misses, e.g. `ting/luw`, `ting/lw` nasal suppletion/drops).
4. Push passes beyond 950 toward 960/1156.
