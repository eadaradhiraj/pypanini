# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T08:30:00Z
Sweep: 951/1156 100% (raw 951/1166)

## Done
- Panini 7.3.84 *sārvadhātukārdhadhātukayoḥ* & 6.1.78 *eco 'yavāyāvaḥ*: Fixed guṇa base for vowel-ending roots (`i`, `I`, `u`, `U`) before consonant-initial ārdhadhātuka affixes (`luw`, `lfw`, `lfN`, `ASIrliN`, `tavya`, `tumun`, `tfc`), ensuring `e` and `o` do not undergo *eco 'yavāyāvaḥ* (which applies strictly before vowels).
- Panini 3.1.97 *aco yat* & 6.1.79 *vānto yi pratyaye*: In `yat`, roots ending in `i`/`I` take guṇa `e` before `ya` without becoming `ay` (`neyaH`/`neyA`/`neyam`, `jeyaH`...).
- Panini 7.2.115 *aco ñṇiti*: In `GaY` (ñit), roots ending in a vowel take vṛddhi, yielding `nAyaH` for `nI` and `BAvaH` for `BU`.
- Panini 6.4.82 *er an-ekāco 'saṁyogapūrvasya*: Implemented `yaṇ` (`y`) for multi-syllabic `ik` stems in Liṭ before vowel-initial kit/ṅit endings across parasmaipada (`ninyatuH`, `ninyuH`...) and karmani/ātmanepada (`ninye`, `ninyAte`, `ninyire`...).
- Full Sweep Results: **951/1156 100% passes** (raw 951/1166, 10 skipped), **1 new 100% pass**, **59 improved roots (+2,241 net matched tokens)**:
  - `01.1049 RIY`: 798 -> **895/895 (100.0%)** (+97 tokens) [NEW 100% PASS]
  - `01.1097 jri`: 330 -> 425/895 (+95 tokens)
  - `01.1099 zmiN`: 288 -> 378/883 (+90 tokens)
  - `01.0269 kzi`: 330 -> 419/895 (+89 tokens)
  - 15 roots (`01.1100`, `01.1103`-`01.1114`): each improved by +84 tokens.
  - `01.0642 ji` & `01.1096 ji`: +79 tokens each.
  - 6 roots (`01.1090`-`01.1095`): each improved by +75 tokens.
  - `01.1102`: +58 tokens.
  - 18 additional roots improved by +2 to +20 tokens each.
- **STRICTLY 0 worsened roots** (`worsened == 0`).
- All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) and previous milestone roots (`01.1122`, `01.1129`, `01.1130`) held strictly at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.0200 fja~` (439/627, gap=188)
   - `01.0722 aMha~` (418/627, gap=209)
   - `01.1121 pUN` (674/883, gap=209)
   - `01.0588 Irzya~` (424/636, gap=212)
   - `01.0637 aBdi~` (424/636, gap=212)
   - `01.0670 idi~` (424/636, gap=212)
   - `01.0199 stuca~` (656/883, gap=227)
2. Target `krut` participles (down to 986 misses, down by 101!).
3. Advance passes toward 960/1156.
