# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T14:20:00+05:30
Sweep: 956/1156 100% (raw 956/1166)

## Done
- Panini 6.1.2 *ajāder dvitīyasya*, 6.1.3 *na ndrāḥ saṁyogādayaḥ*, 7.4.60 *halādiḥ śeṣaḥ*, 7.4.62 *kuhocuḥ*, 8.4.54 *abhyāse carca*, 8.4.58 *anusvārasya yayi parasavarṇaḥ*, & 7.4.79 *sany ataḥ*: Generative sannanta reduplication for vowel-initial roots:
  - Nasal-preceded conjuncts retain nasal in the base while the following consonant reduplicates; before palatal `j` (*kuhocuḥ* for `h`), anusvāra assimilates to `Y` (*parasavarṇaḥ* 8.4.58), yielding `aYjihiz-` (`01.0722 ahi~`, 627/627, 100.0%, +209 tokens) and `inviviz-` (`01.0670 ivi~`, 636/636, 100.0%, +212 tokens).
  - Aspirate consonants in abhyāsa deaspirate by 8.4.54 *abhyāse carca* (`B` -> `b`), yielding `abiBriz-` (`01.0637 aBra~`, 636/636, 100.0%, +212 tokens).
  - Roots ending in `rzy` (`01.0588 Irzya~`, 636/636, 100.0%, +212 tokens) reduplicate the sibilant/semivowel cluster as `Irzyiyiz-` and `Irzyiziz-`.
  - Laghūpadha ṛ-initial roots take initial guṇa `ar` (7.3.86) + *ajāder dvitīyasya* reduplication `ji` of the following consonant `j` (*na ndrāḥ* 6.1.3 blocks `r`), yielding `arjijiz-` across kartari, karmani (san_yak), and kṛdanta (`01.0200 fja~`, 627/627, 100.0%, +188 tokens).
- Panini 7.3.86 *pug-anta-laghūpadhasya ca*: Added `f`, `F` to laghūpadha guṇa in ṇijanta across `tinanta.py` and `krdanta.py`, generating `arjay-` for `01.0200 fja~` (`arjayati`, `arjayate`, `arjayitA`, `arjayitavyaH`...) and unlocking +133 to +145 tokens each across 24 ṛ-roots.
- Full Sweep Results: **956/1156 100% passes** (raw 956/1166, 10 skipped), **5 new 100% passes**, **29 improved roots (+4,432 net matched tokens)**:
  - `01.0670 ivi~`: 424 -> **636/636 (100.0%)** (+212 tokens) [NEW 100% PASS]
  - `01.0637 aBra~`: 424 -> **636/636 (100.0%)** (+212 tokens) [NEW 100% PASS]
  - `01.0588 Irzya~`: 424 -> **636/636 (100.0%)** (+212 tokens) [NEW 100% PASS]
  - `01.0722 ahi~`: 418 -> **627/627 (100.0%)** (+209 tokens) [NEW 100% PASS]
  - `01.0200 fja~`: 439 -> **627/627 (100.0%)** (+188 tokens) [NEW 100% PASS]
  - 12 roots (`01.0255`, `01.0496`, `01.0802`-`01.0806`, `01.1014`, `01.1015`, `01.1138`, `01.1143`, `01.1145`): +145 tokens each.
  - 5 roots (`01.0202`, `01.0737`, `01.0862`-`01.0864`): +142 tokens each.
  - 6 roots (`01.0249`, `01.0281`, `01.0834`, `01.0836`, `01.0852`, `01.0942`): +136 tokens each.
  - 1 root (`01.0097`): +133 tokens.
- **STRICTLY 0 worsened roots** (`worsened == 0`).
- All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) and previous milestone roots (`01.1049 nI`, `01.1122`, `01.1129`, `01.1130`) held strictly at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.1121 pUN` (674/883, gap=209): Panini 7.4.79 *sany ataḥ* & 7.4.80 *pvoḥ yan-sanoḥ* (`pipavizate`, `pipavizitA`, `apipavizata`).
   - `01.0199 zwuca~` (656/883, gap=227): 8.3.59 *ādeśapratyayayoḥ* after $iṇ$ abhyāsa -> `tozwucyate`.
   - `01.0463 japa~` (668/895, gap=227): 7.4.86 *japa-jabha-daha...* nuk -> `jaYjapyate`.
   - `01.1146 daha~` (668/895, gap=227): 7.4.86 nuk -> `daMdahyate` / `dandahyate`.
   - `01.0979 pata~` (668/895, gap=227): 7.4.87 nīk -> `panIpatyate`.
2. Target Yaṅ *nuk* / yaṅanta cluster (23 roots with identical gap=227).
3. Advance passes toward 960+/1156.
