# Phase 3: Phonological Rules (Natva & Satva)

## Goal
Implement rules where the prefix triggers phonological shifts inside the root.

## Tasks
Add a phonological post-processor step in the engine that handles:

### 1. Natva (ṇ-tva)
Prefixes containing `r` or `ṛ` (such as `pra`, `parā`, `nir`, `antar`) cause a root-initial `n` to become `ṇ`.
- **Example:** `pra + namati` $\rightarrow$ `praṇamati`.
- **Example:** `pra + nayate` $\rightarrow$ `praṇayate`.

### 2. Satva (ṣ-tva)
Prefixes ending in `i` or `u` (such as `vi`, `ni`, `su`, `abhi`, `pari`) often trigger retroflexion of a root-initial `s` into `ṣ`.
- **Example:** `vi + sīdati` $\rightarrow$ `viṣīdati`.
- **Example:** `abhi + siñcati` $\rightarrow$ `abhiṣiñcati`.

*Note: There are specific exceptions in Pāṇini for both Natva and Satva (e.g., roots that inherently resist it), which should be gated via dictionary lookups or root conditions.*
