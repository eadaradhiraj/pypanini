# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T05:35:00Z
Sweep: 950/1156 100% (raw 950/1166)

## Done
- Panini 7.1.63 *rabher a-śab-liṭoḥ* & 7.1.64 *labheś ca*: Roots `raB` (`01.1129`) and `laB` (`01.1130`) take `num` augment (`ramB`, `lamB`) everywhere except before `śap` (kartari sārvadhātuka) and `liṭ`. Implemented generative num-augment across ṇijanta tinanta (`ramBayati`/`ramBayate`, `lamBayati`/`lamBayate`), karmaṇi ṇijanta (`ramByate`, `lamByate`), ṇijanta kṛdanta (`ramBayitA`, `ramBayitavya`...), and non-śab/liṭ primitive formations (`ramBakaH`/`lamBakaH` in ṇvul, `ramBaRam`/`lamBanam` in lyuṭ, `ramBaRIyaH`/`lamBanIyaH` in anīyar).
- Panini 7.1.67 *upasargāt khal-ghañoḥ*: In `GaY`, root `laB` only takes `num` following an upasarga (*anupasarge tu na*), so simplex `laB` without prefix undergoes regular vṛddhi by 7.2.116 *ata upadhāyāḥ* yielding `lABaH`, whereas `raB` takes num by 7.1.63 yielding `ramBaH`.
- Panini 3.1.98 *por adupadhāt*: Roots ending in pavarga with short `a` upadhā take `yat` affix (without vṛddhi) rather than `ṇyat`, generating `raByaH`/`raByA`/`raByam` and `laByaH`/`laByA`/`laByam`.
- Full Sweep Results: **950/1156 100% passes** (raw 950/1166, 10 skipped), **2 new 100% passes**, **+374 net matched tokens**:
  - `01.1129 rABa~`: 695 -> **883/883 (100.0%)** (+188 tokens) [NEW 100% PASS]
  - `01.1130 qulaBa~z`: 697 -> **883/883 (100.0%)** (+186 tokens) [NEW 100% PASS]
- **STRICTLY 0 worsened roots** (`worsened == 0`).
- All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) held strictly at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.1049 kzamU~` (798/895, gap=97)
   - `01.0200 fja~` (439/627, gap=188)
   - `01.0722 aMha~` (418/627, gap=209)
   - `01.1121 pUN` (674/883, gap=209)
   - `01.0588 Irzya~` (424/636, gap=212)
   - `01.0637 aBdi~` (424/636, gap=212)
   - `01.0670 idi~` (424/636, gap=212)
2. Target `krut` participles (1,087 misses across Gaṇa 01, down from 1,101).
3. Target `ting` misses (711 misses).
4. Advance passes toward 960/1156.
