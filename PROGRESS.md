# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T04:45:00Z
Sweep: 947/1156 100% (raw 947/1166)

## Done
- Panini 6.4.92 *mitāṁ hrasvaḥ* & 1.1.48 *eca igghrasvādeśe*: In ṇi (ṇijanta), `mit` roots shorten the vowel. For roots with penultimate `ec` (`e`), `ik` (`i`) is substituted, shortening `heq` -> `hiqay-` across sārvadhātuka and ārdhadhātuka lakāras and kṛdantas (`hiqayati`, `hiqayate`, `hiqyate`, `hiqayitavya`, `hiqitA`, `hiqayan`...).
- Panini 7.3.36 *arti-hrī-vlī-rī-knūyī-kṣmāyyāṁ puṅ ṇau*: Roots `knUy` (`01.0558`) and `kzmAy` (`01.0559`) take `puk` (`puṅ`) augment before `ṇi`, yielding `knopay-` (by 7.3.86 laghūpadha guṇa) and `kzmApay-` across all tinanta and kṛdanta formations (`knopayati`, `knopayate`, `knopyate`, `kzmApayati`, `kzmApayate`, `kzmApyate`, `knopayitavya`, `kzmApayitavya`...).
- Panini 6.1.22 *sphāyaḥ spho vā* / Vārttika on 7.3.39 *sphāyo vuk*: Root `sPAy` (`01.0560`) takes `vuk` augment before `ṇi`, generating `sPAvay-` (`sPAvayati`, `sPAvayate`, `sPAvyate`, `sPAvayitavya`, `prasPAvya`...).
- Panini 7.4.1 *ṇau caṅy upadhāyā hrasvaḥ*, 7.4.61 *śarpūrvāḥ khayaḥ*, 7.4.62 *kuhoś cuḥ*, 7.4.93 *sanval laghuni*, 7.4.94 *dīrgho laghoḥ*: Algorithmic Caṅ Reduplicated Aorist accepts `n_stem` with shortened penultimate vowel in `bases` (`knop` -> `knup`, `kzmAp` -> `kzmap`, `sPAv` -> `sPav`, `hiq` -> `hiq`) and produces both Parasmaipada (`at`, `atAm`, `an`...) and Ātmanepada (`ata`, `etAm`, `anta`...) caṅ aorist forms (`ajIhiqat`, `ajIhiqata`, `acuknupat`, `acuknupata`, `acikzmapat`, `acikzmapata`, `apisPavat`, `apisPavata`).
- Full Sweep Results: **947/1156 100% passes** (raw 947/1166, 10 skipped), **4 new 100% passes**, **6 improved roots (+532 tokens)**:
  - `01.0887 heqa~`: 767 -> **895/895 (100.0%)** (+128 tokens) [NEW 100% PASS]
  - `01.0558 knUyI~`: 749 -> **883/883 (100.0%)** (+134 tokens) [NEW 100% PASS]
  - `01.0559 kzmAyI~`: 749 -> **883/883 (100.0%)** (+134 tokens) [NEW 100% PASS]
  - `01.0560 sPAyI~`: 749 -> **883/883 (100.0%)** (+134 tokens) [NEW 100% PASS]
  - `01.1129 rABa~`: 694 -> 695/883 (78.7%) (+1 token)
  - `01.1130 qulaBa~z`: 696 -> 697/883 (78.9%) (+1 token)
- **STRICTLY 0 worsened roots** (`worsened == 0`).
- All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) held at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.1122 mUN` (735/883, gap=148)
   - `01.1130 qulaBa~z` (697/883, gap=186)
   - `01.1129 rABa~` (695/883, gap=188)
   - `01.0200 fja~` (439/627, gap=188)
   - `01.1134 zkanda~r` (668/895, gap=227)
2. Target `krut/tavya` and `krut/anIyar` (1,101 misses across Gaṇa 01).
3. Target remaining `ting` misses (726 misses, e.g. `ting/luw`, `ting/lw` nasal suppletion/drops).
4. Push passes beyond 950 toward 960/1156.
