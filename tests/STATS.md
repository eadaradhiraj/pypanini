# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-09T22:55:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **926/1156 100%** (raw 936/1166). Fails: 230 scored (240 with 10 skipped). Net +903 matched tokens across 73 improved roots (0 worsened). Monosyllabic `smi` (01.1099, 0 -> 288 tokens, +288) and `qI` (01.1123, 143 -> 357 tokens, +214) restored from destructive num-stripping.

## Rules (general, pure generative)
- Panini 3.2.124 *laṭaḥ śatṛ-śānacāv aprathamā-samānādhikaraṇe* & 1.4.100 *taṅānāv ātmanepadam*: Kartari Śānac derivation for all Ātmanepada and Ubhayapada roots and suppletions (`sTA`/`zWA` -> `tizWa`, `Sad` -> `SIya`, `kfp` -> `kalpa`, `guh` -> `gUha`, `BrAS`/`BlAS`/`laz` -> `ya`, `jaB`/`jfBi` -> `jamB`/`jfmB` gated to `is_idit`, `svanj`/`ranj` -> `svaja`/`raja`, `cate` -> `cata`, `ubund` -> `bunda`, `ftu`/`fti` -> `ftIya`, nitya-san `jugups`/`titikz`/`cikits`/`mImAMs`/`bIBats`/`dIdAMs`/`SISAMs`, with stem guṇa and keep-shape). 445/445 (100.0%) roots with Śānac in data matched!
- Present Passive Participle (yak + Śānac, e.g. `clean + yamAna` with natva `yamARa`, and 6.1.15 samprasāraṇa `vas` -> `uzyamARa`) for Parasmaipada roots.
- Monosyllabic `i`/`I` root protection: `clean.endswith(("i","I")) and (is_idit or pada == "Atmanepadi") and any(c in SLP1_VOWELS for c in clean[:-1])` in both `tinanta.py` and `krdanta.py`, safeguarding `01.1099 smi` and `01.1123 qI`.
- Panini 1.3.3 *halantyam* & 1.3.12: Stripped `N` anubandha on all 25 Ātmanepada roots (`zmiN`, `guN`, `kuN`, `cyuN`, etc.) and `R` on `dAR` -> `dA` in `clean_dhatu_op` across both engines; fixed finite and non-finite forms across all these roots.
- Panini 8.3.24 *naś cāpadāntasya jhali*: Num assimilation for idit roots before sibilants (`s`, `S`, `z`) and `h` -> anusvāra `M` (`baMhita`, `vaMhita`, `GuMzita`, `SaMsita`); before `kz` -> `N` (`kANkzita`).
- Panini 3.1.5 *gup-tij-kidbhyaḥ san* & 3.1.6 *māna-badha-śān-dānbhyo dīrghaś ca*: Nitya-san participles in `_kta_stem` (`jugupsita`, `titikzita`, `cikitsita`, `mImAMsita`, `bIBatsita`, `dIdAMsita`, `SISAMsita`).
- Panini 6.1.15 *vaci-svapi-yajādīnāṁ kiti*: Samprasāraṇa added for `ve` -> `uta`, `vye` -> `vIta`, `hve` -> `hUta`, `Svi` -> `SUna` in `_kta_stem`.
- Panini 8.2.42 *radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ* & 8.2.52 *paco vaḥ*: Systematic `d` -> `nna` (`sanna`, `Sanna`, `hanna`, `bunna`, `matta` by 8.2.55); `pac` -> `pakva`.
- Panini 6.1.45 *ādeca upadeśe 'śiti* & 8.2.43 / 6.4.66 / 8.2.53: Full coverage for `Ec` -> `ā` roots (`gIta`, `kzAma`, `glAna`, `mlAna`, `drARa`, `DrARa`, `SrARa`, `srARa`, `SyAna`, `pyAna`, `trAta`/`trARa`, `vAna`, `DyAta`, `KAta`, etc.).
- Panini 7.4.54 *sani mīmāghūrābla...*: Sannanta stems for roots ending in `e`/`E`/`A` (`me` -> `mits`, `de` -> `dits`, `SyE` -> `SiSyAs`, `pyE` -> `pipyAs`, `trE` -> `titrAs`, `gA` -> `jigAs`) evaluated uniformly before the non-vowel-final check in both `tinanta._sannanta_stem` and `krdanta._sannanta_sec`.
- Panini 6.4.64 *āto lopaḥ* (dropping final `A` before kit/Nit vowel endings in liṭ: `jaGre`, `daDme`, `mamne`, `jaGrire`, `jaGrAte`, `jaGrize`), Panini 6.4.120 *ata ekahalmadhye 'nādeśa-der liti* (et-tva + abhyāsa-lopa for single-consonant initial, short-a upadhā, single-consonant final: `car` -> `cere`, `cerAte`, `cerire`), Panini 3.1.66 *ciṇ bhāvakarmaṇoḥ* + 1.2.11 / 8.2.26 / 8.4.53 Aniṭ Ātmanepada Sic aorist in yak luṅ (`aramBi`/`alamBi`/`alABi`, `araps-`/`alaps-`, `arabDvam`/`alabDvam`, `avoQvam` on `vah`, `aDagDvam` on `dah`), and Panini 7.3.33 *āto yuk ciṇkṛtoḥ* + 6.4.62 *syasicoḥ kaniṭ* for roots ending in `ā` in yak luṅ (`aGrAyi`/`aDmAyi`/`amnAyi`, `aGrAyizWAH`/`aGrAyizATAm`/`aGrAyiDvam`, `aGrAsTAH`/`aGrADvam`). Result: **ZERO `yak/` misses across all 1,166 roots in Gaṇa 01**.
## Fails (2712 capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 1201 | 01.1048 krut/SAnac/M:sUrkzyyamARaH |
| ting | 998 | 01.0097 ting/liw/prathama/eka:vivfke |
| yang_krut | 224 | 01.0199 yang_krut/kta/M:tostucitaH |
| nich_krut | 79 | 01.0249 nich_krut/Satf/M:Dfjayan |
| san_krut | 72 | 01.0588 san_krut/kta/M:IrzizyizitaH |
| yang | 54 | 01.0216 yang/lw/prathama/eka:vAvacyate |
| san | 35 | 01.0588 san/lw/prathama/eka:Irdizyizati |
| nich | 30 | 01.0558 nich/lw/prathama/eka:knUyayate |
| yangluk_krut | 19 | 01.0989 yangluk_krut/ktvA:rAntvA |



