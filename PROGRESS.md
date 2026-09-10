# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T16:15:00+05:30
Sweep: 964/1156 100% (raw 964/1166)

## Done
- Panini 7.4.84 *nīg vañcu-sraṁsu-dhvaṁsu-bhraṁsu-kasa-pata-pada-skandām*:
  - In Yaṅ and Yaṅluk stems across `tinanta.py` and `krdanta.py`, roots `vañc`, `sraṁs`, `dhvaṁs`, `bhraṁs`, `kas`, `pat`, `pad`, `skand` take augment *nīk* in the abhyāsa (`yan_vowel = "anI"`).
  - Generative integration with Panini 6.4.24 *aniditāṁ hala upadhāyāḥ kṅiti*: penultimate nasals elide before kṅit affixes (`vanIvacya-`, `canIskadya-`, `sanIsrasya-`, `danIDvasya-`, `banIBrasya-`).
  - Generative Yaṅluk integration: by Panini 1.2.4 *sārvadhātukam apit*, pit endings (`tip`, `sip`, `mip`) are not ṅit and retain penultimate nasals (`vanIvaNkti`, `vanIvaYcIti`, `canIskanti`, `canIskandIti`), while apit endings are ṅit and elide them (`vanIvaktaH`, `canIskattaH`, `vanIvacvaH`, `canIskadvaH`).
- Full Sweep Results: **964/1156 100% passes** (raw 964/1166, 10 skipped):
  - `01.0979 pata~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0996 kasa~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0216 vañcu~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.1134 skandir~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - Major advances on sibling roots:
    - `01.0857 sransu~`: 46 -> **273/883 (30.9%)** (+227 tokens)
    - `01.0858 Dvansu~`: 46 -> **273/883 (30.9%)** (+227 tokens)
    - `01.0859 Bransu~`: 46 -> **273/883 (30.9%)** (+227 tokens)
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 17 Pilot/Milestone roots strictly held at 100.0%.

## Next
1. Target remaining top closest roots to 100%:
   - `01.0423 zwepf` (876/883, gap=7): yaṅ_krut SAnac/anIyar/lyuw natva adjustment.
   - `01.0460 zwuBu` (876/883, gap=7): yaṅ_krut natva.
   - `01.0422 zwipf` (875/883, gap=8): nich luN `astepayizwa` + yaṅ_krut natva.
2. Advance Gaṇa 01 passes from 964 to 967+/1156.
