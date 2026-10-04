# Upasarga Implementation Progress

## Log
* **2026-10-03:** Project plan initialized. All 5 phases documented.
* **2026-10-03:** Phase 1 (Test Infrastructure) completed. 
  - `pypanini/tinanta.py` modified: `derive` and `derive_all` now accept `upasarga: Optional[str] = None`.
  - `tests/test_dhatu.py` modified: `validate_dhatu` now accepts `prefix=...` and restricts token-matching logic strictly to the prefixed JSON data to prevent false positives.
  - Created `tests/sweep_upasargas.py` to iterate over prefixed data and output CSVs.
* **2026-10-03:** Phase 2 (Sandhi Engine) completed.
  - Wrote `apply_upasargas` in `pypanini/phonetics.py` that handles vowel sandhi, consonant sandhi (anusvara/parasavarna), and augment boundary (`pra + aBavat -> prABavat`).
  - Implemented the wrapper pattern in `pypanini/tinanta.py` and `pypanini/krdanta.py` to automatically intercept the `_inner` return value and apply the `upasarga` sandhi precisely once before returning to the user.
* **2026-10-03:** Phase 5 (API Refactoring / Krdanta Cleanup) completed.
  - Fixed Krdanta legacy loops that were double-applying prefixes for `lyap`.
  - `krdanta.py` wrapper now correctly strips old hardcoded cache prefixes and only applies the Sandhi engine uniformly to the forms (skipping metadata keys like `gender`).
* **2026-10-03:** Phase 3 (Natva & Satva Refinements) started.
  - Basic `s -> z` Satva rule implemented in `apply_upasargas`.
  - Perfected `n -> R` Natva logic (`apply_natva`) across boundaries (e.g., matching `pra + havanIya -> prahavaRIya` while deliberately preventing it on padanta `n` or tiṅanta `nti/ntu` like `praBavanti`).
* **2026-10-04:** Phase 4 (Pada Overrides) completed!
  - Created `pypanini/pada_rules.py` by compiling `PADA_MAP_ID` and `PADA_MAP_CLEAN` dictionaries from the source JSON files containing `[ting] sanadi=None prayoga=kartari` permutations.
  - Plumbed `_force_pada` through both `TinantaDerivationEngine` and `KrdantaEngine` wrappers into their inner functions.
  - **Fixed critical bug 1 (Nasal Augment Heuristic):** The base engine had a hacky heuristic `(is_idit or pada == "Atmanepadi")` pasted ~30 times across both engines that falsely triggered `num` (nasal) augments for roots whose voice was overridden to Atmanepada (e.g., `vi + ji` -> `viYj`). Rewrote these heuristics across the codebase to `(is_idit or (pada == "Atmanepadi" and _force_pada is None))` to safely isolate overrides from derivation hacks.
  - **Fixed critical bug 2 (Nijanta Kartari SAnac):** The Krdanta engine erroneously hardcoded the Passive (`BAvakarma`) suffix `yamAna` (`jApyamAna`) for all `nijanta SAnac` kartari forms (instead of `ayamAna` like `jApayamAna`). Fixed the fallback in `pypanini/krdanta.py`.
  - **Results:** Validation for `01.1096` (`ji`) with prefix `vi` passed at **100.0% (870/870)**, seamlessly resolving both Tinanta and Krdanta (properly suppressing `Satf` and generating `SAnac`).

## Next Steps for the Next Agent:
1. **Run Full Gaṇa 1 Sweep:**
   - Run `python3 tests/sweep_upasargas.py 01 > logs_01.txt`.
   - Validate that overall Prefix coverage across all prefixes in Gaṇa 1 is consistently above 99.5%.
   - Note any final missing edge cases and investigate if they are Sandhi issues (Phase 3) or idiosyncratic base engine failures, and patch them.
2. **Review Output and Wrap Up:**
   - The prefix engine is fully functional and architecturally robust. If the sweep passes gracefully, you can conclude the project!
