# Upasarga (Prefix) Implementation Overview

## Context
The `pypanini` engine currently supports derivation of bare (unprefixed) roots for all 10 Pāṇinian gaṇas at 100% accuracy. The next major milestone is adding support for **Upasargas** (verbal prefixes like `pra`, `sam`, `vi`, `upa`).

In the validation data (`skt-morph-data/` JSON files), prefixed forms are located under the `"upasarga_forms"` key. The structure mirrors the root structure:
```json
"upasarga_forms": {
  "pra": {
    "conjugations": { "ting": { "plat": [...] }, ... },
    "participles": { ... }
  },
  "vi;ati": { ... }
}
```

## Challenge
Prefixes in Pāṇini do not just naively concatenate (e.g., `pra + bhavati`). They require:
1. **Saṃhitā (Sandhi):** Fusing the prefix to the root or to the augment (`aṬ`).
2. **Morphophonological changes:** Triggering `n -> ṇ` (natva) or `s -> ṣ` (satva) across the prefix-root boundary.
3. **Pada Shifts:** Overriding the voice (Parasmaipada vs Ātmanepada) of the root based on specific sutras.

## Plan Structure
This plan is broken into 5 phases to ensure test-driven development. If you are an LLM taking over this task, please execute these phases sequentially:
- `01_Phase_1_Test_Infrastructure.md`
- `02_Phase_2_Sandhi_Engine.md`
- `03_Phase_3_Phonological_Rules.md`
- `04_Phase_4_Morphological_Overrides.md`
- `05_Phase_5_API_Refactoring.md`
