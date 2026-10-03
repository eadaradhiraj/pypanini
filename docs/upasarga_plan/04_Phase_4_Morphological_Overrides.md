# Phase 4: Morphological Overrides (Pada Shifts)

## Goal
Handle Pāṇinian rules where an upasarga overrides the root's inherent voice (Parasmaipada vs Ātmanepada).

## Tasks
Implement a rule-interceptor inside `TinantaDerivationEngine.derive()` (in `pypanini/tinanta.py`). 

Before the engine assigns the tiṅ endings based on the root's anubandhas, it must check the `upasarga` + `dhatu` combination against voice-shifting sutras:

### Examples of Ātmanepada Shifts:
- **1.3.19 (viparābhyāṃ jeḥ):** `vi` or `parā` + `ji` (normally P) $\rightarrow$ Ātmanepada (`vijayate`, `parājayate`).
- **1.3.29 (samo gamyṛcchipracchisvaratyartiśruvidibhyaḥ):** `sam` + `gam` $\rightarrow$ Ātmanepada (`saṅgacchate`).

### Examples of Parasmaipada Shifts:
- **1.3.79 (anuparābhyāṃ kṛñaḥ):** `anu` or `parā` + `kṛ` (normally U) $\rightarrow$ strictly Parasmaipada (`anukaroti`).

### Implementation Strategy:
Create a mapping or evaluation function `get_pada_override(dhatu, upasargas) -> Optional[str]`. If it returns `"Atmanepada"` or `"parasmaipada"`, the engine forces that voice for the current derivation.
