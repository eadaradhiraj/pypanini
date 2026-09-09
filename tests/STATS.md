# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-09T22:25:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **926/1156 100%** (raw 936/1166). Fails: 230 scored (240 with 10 skipped). See tests/sweep_all.csv (grep). Net +18,452 matched tokens across 92 improved roots (0 worsened). 7 new 100% passes (01.0663, 01.0720, 01.0721, 01.0740, 01.0833, 01.1132 had, 01.1151 pac).

## Rules (general, pure generative)
- Panini 1.3.3 *halantyam* & 1.3.12: Stripped `N` anubandha on all 25 Ātmanepada roots (`zmiN`, `guN`, `kuN`, `cyuN`, etc.) and `R` on `dAR` -> `dA` in `clean_dhatu_op` across both engines; fixed finite and non-finite forms across all these roots.
- Panini 8.3.24 *naś cāpadāntasya jhali*: Num assimilation for idit roots before sibilants (`s`, `S`, `z`) and `h` -> anusvāra `M` (`baMhita`, `vaMhita`, `GuMzita`, `SaMsita`); before `kz` -> `N` (`kANkzita`).
- Panini 3.1.5 *gup-tij-kidbhyaḥ san* & 3.1.6 *māna-badha-śān-dānbhyo dīrghaś ca*: Nitya-san participles in `_kta_stem` (`jugupsita`, `titikzita`, `cikitsita`, `mImAMsita`, `bIBatsita`, `dIdAMsita`, `SISAMsita`).
- Panini 6.1.15 *vaci-svapi-yajādīnāṁ kiti*: Samprasāraṇa added for `ve` -> `uta`, `vye` -> `vIta`, `hve` -> `hUta`, `Svi` -> `SUna` in `_kta_stem`.
- Panini 8.2.42 *radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ* & 8.2.52 *paco vaḥ*: Systematic `d` -> `nna` (`sanna`, `Sanna`, `hanna`, `bunna`, `matta` by 8.2.55); `pac` -> `pakva`.
- Panini 6.1.45 *ādeca upadeśe 'śiti* & 8.2.43 / 6.4.66 / 8.2.53: Full coverage for `Ec` -> `ā` roots (`gIta`, `kzAma`, `glAna`, `mlAna`, `drARa`, `DrARa`, `SrARa`, `srARa`, `SyAna`, `pyAna`, `trAta`/`trARa`, `vAna`, `DyAta`, `KAta`, etc.).
- Panini 7.4.54 *sani mīmāghūrābla...*: Sannanta stems for roots ending in `e`/`E`/`A` (`me` -> `mits`, `de` -> `dits`, `SyE` -> `SiSyAs`, `pyE` -> `pipyAs`, `trE` -> `titrAs`, `gA` -> `jigAs`) evaluated uniformly before the non-vowel-final check in both `tinanta._sannanta_stem` and `krdanta._sannanta_sec`.
- Panini 6.4.64 *āto lopaḥ* (dropping final `A` before kit/Nit vowel endings in liṭ: `jaGre`, `daDme`, `mamne`, `jaGrire`, `jaGrAte`, `jaGrize`), Panini 6.4.120 *ata ekahalmadhye 'nādeśa-der liti* (et-tva + abhyāsa-lopa for single-consonant initial, short-a upadhā, single-consonant final: `car` -> `cere`, `cerAte`, `cerire`), Panini 3.1.66 *ciṇ bhāvakarmaṇoḥ* + 1.2.11 / 8.2.26 / 8.4.53 Aniṭ Ātmanepada Sic aorist in yak luṅ (`aramBi`/`alamBi`/`alABi`, `araps-`/`alaps-`, `arabDvam`/`alabDvam`, `avoQvam` on `vah`, `aDagDvam` on `dah`), and Panini 7.3.33 *āto yuk ciṇkṛtoḥ* + 6.4.62 *syasicoḥ kaniṭ* for roots ending in `ā` in yak luṅ (`aGrAyi`/`aDmAyi`/`amnAyi`, `aGrAyizWAH`/`aGrAyizATAm`/`aGrAyiDvam`, `aGrAsTAH`/`aGrADvam`). Result: **ZERO `yak/` misses across all 1,166 roots in Gaṇa 01**; 17 improved (+183 matched tokens), 0 worsened, 1 new 100% pass (`01.1159 vaha~` 894->895 100.0%), passes 918->919/1156 (raw 929/1166). Pilots 100% OK.
- Panini 7.4.79 *sany ataḥ*, 8.2.30/36/41 palatal & sibilant coda sandhi (c, j, ś, ṣ, h -> kz: yiyakz-, vivakz-, pipakz-, titvikz-), 8.4.55 labial coda sandhi (p, b, bh -> ps: vivaps-, titaps-, SiSaps-), 8.4.55 / 7.4.49 dental coda sandhi (d, s -> ts: vivats-, titrats-), 8.3.24 nasal coda sandhi (m -> Ms: jigaMs-, ninaMs-, riraMs-), 8.2.37 ekāco baśo bhaṣ (dah -> diDakz-), 7.4.54 sani mīmāghūrāblabhaśakapatapadāṁ ca (raB -> rips-, laB -> lips-, meN -> mits-, deN -> dits-), 8.3.62 / 8.3.111 satva in abhyAsa (sad/zad -> sizats-), 6.1.45 ādeca upadeśe 'śiti (SyEN -> SiSyAs-, pyEN -> pipyAs-, trEN -> titrAs-, gAN -> jigAs-), 7.3.86 pugantalaghūpadha guṇa before seṭ iz (ṛ -> ar: Dfj -> diDarjiz-, pfz -> piparziz-), and 7.1.58 idito num dhātoḥ num-assimilation preservation in krdanta. 16 new 100% passes (01.0215, 01.0420, 01.0783, 01.0794, 01.0995, 01.0998, 01.1135, 01.1136, 01.1140, 01.1141, 01.1147, 01.1155, 01.1156, 01.1157, 01.1158, 01.1160), 74 improved (+12,740 matched tokens), 0 worsened, passes 902->918/1156. Pilots 100% OK.
## Fails (2712 capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 1273 | 01.0097 krut/SAnac/M:vfkamAnaH |
| ting | 998 | 01.0097 ting/liw/prathama/eka:vivfke |
| yang_krut | 186 | 01.0199 yang_krut/kta/M:tostucitaH |
| san_krut | 63 | 01.0588 san_krut/kta/M:IrzizyizitaH |
| yang | 54 | 01.0216 yang/lw/prathama/eka:vAvacyate |
| nich_krut | 54 | 01.0249 nich_krut/Satf/M:Dfjayan |
| san | 35 | 01.0588 san/lw/prathama/eka:Irdizyizati |
| nich | 30 | 01.0558 nich/lw/prathama/eka:knUyayate |
| yangluk_krut | 19 | 01.0989 yangluk_krut/ktvA:rAntvA |



