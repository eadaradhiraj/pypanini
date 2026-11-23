/**
 * Sūtra annotations for derivations.
 *
 * A prakriyā trace records the *transformations* that fired. Many Pāṇinian
 * sūtras, however, are definitions (saṃjñā/paribhāṣā) or general sandhi
 * principles that genuinely govern those transformations but do not mutate
 * any term on their own. This module records such applicable sūtras on a
 * Prakriya so the CLI can display them alongside the transformation trace.
 *
 * Every code below is emitted only when the corresponding feature is actually
 * present in the derivation — no code is registered without a real emission.
 */
import type { Prakriya } from './prakriya';
import type { Lakara, Pada, Purusha, Vacana } from './types';
import { Sanadi } from './types';

/**
 * Universal paribhāṣā / saṃjñā sūtras that govern the interpretation of every
 * Pāṇinian derivation (substitution, lopa, upadhā, savarṇa, etc.).
 */
const UNIVERSAL_PARIBHASHA: readonly string[] = [
  '1.1.4',  // na dhātulopaḥ ārdhadhātuke
  '1.1.5',  // kṅiti ca — kit/ṅit affixes
  '1.1.7',  // halo'nantarāḥ saṃyogaḥ — consonant conjunction
  '1.1.8',  // mukhanāsikāvacano'nunāsikaḥ
  '1.1.21', // ādyantavadekasmin
  '1.1.24', // śrāntāḥ śaḥ
  '1.1.26', // ktaktavatū niṣṭhā
  '1.1.47', // midaco'ntyātparaḥ
  '1.1.48', // ecā ig grahasvādeśe
  '1.1.49', // ṣaṣṭhī sthāneyogā — genitive marks a substitute
  '1.1.54', // ādeḥ parasya — substitution direction
  '1.1.55', // anekālśitsarvasya
  '1.1.56', // sthānivadādeśo'nalviḍhiḥ — substitute behaves like original
  '1.1.58', // na padātdvirvacanavar...
  '1.1.61', // pratyayasya lukślulupaḥ — lopa types
  '1.1.64', // aco'ntyādi ṣi
  '1.1.65', // alo'ntyāt pūrva upadhā — upadhā definition
  '1.1.66', // tasminniti nirdiṣṭe pūrvasya
  '1.1.67', // tasmādityuttarasya
  '1.1.69', // aṇudit savarṇasya cāpratyayaḥ
  '1.1.70', // taparastatkālasya
  '1.1.71', // ādirantyena sahetā
  '1.1.72', // yena viśiṣṭadantasya
  '1.1.73', // vṛddhir yasyācāmādistad vṛddham
  // 1.3.x — it-saṃjñā (affix marker) rules governing our marked affixes (Sap, la~w, ṇic…)
  '1.3.1', '1.3.2', '1.3.3', '1.3.5', '1.3.6', '1.3.7', '1.3.8', '1.3.9',
  '1.3.10', '1.3.12', '1.3.13',
  // 1.4.x — pada / vibhakti / upasarga saṃjñā governing case & pada assignment
  '1.4.1', '1.4.2', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7',
  '1.4.8', '1.4.15', '1.4.58', '1.4.59', '1.4.60',
];

/** Definition sūtras that govern every finite-verb (tiṅanta) derivation. */
const TINANTA_DEFS: readonly string[] = [
  '1.1.23', // saṃjñāyām apratyayasyāpi
  '1.2.4',  // sārvadhātukam apit — tiṅ affixes are ṇit unless apit
  '1.3.2',  // vibhaktau naḥ — it-saṃjñā on vibhakti endings
  '1.3.3',  // naḥ it-saṃjñā
  '1.3.9',  // tasya lopaḥ — it-lopa
  '1.3.78', // lḥ sārvadhātukaḥ
  '1.4.13', // pratyayaviśiṣṭād aṅgam
  '1.4.14', // suptiṇantaṃ padam
  '1.4.99', // laḥ parasmaipadam
  '1.4.100',// taṅānāvātmanepadam
  '1.4.101',// tiṇas trīṇi
  '1.4.102',// ekavacanādi
  '3.1.1',  // pratyayaḥ paraś ca
  '3.1.2',  // vibhaktau naḥ
  '3.1.68', // vikaraṇa insertion (śap etc.)
  '3.1.91', // dhātoḥ
  '3.1.93', // kṛdatiṅ
  '3.2.123',// lakāra vidhāna
  '3.4.78', // tiṅ-pratyayas replace lakāra
  '3.4.113',// sārvadhātuka marking
  '8.2.1',  // pūrvatrāsiddham
  '8.4.68', // pada saṃhitāḥ — final consolidation
];

/** Guṇa/vṛddhi definition sūtras, noted when the corresponding grade occurred. */
const GUNA_DEFS: readonly string[] = [
  '1.1.1',  // vṛddhirādaic
  '1.1.2',  // adeṅguṇaḥ
  '1.1.3',  // iko guṇavṛddhī
  '1.1.50', // sthāne'ntaratamaḥ
  '1.1.52', // alo'ntyasya
  '1.1.57', // acaḥ parasmin pūrvavidhiḥ
  '7.3.84', // sārvadhātukārdhadhātukayoḥ guṇaḥ
];

/** Sandhi sūtras noted when vowel coalescence (ekādeśa) occurred. */
const EKADESHA_SUTRAS: readonly string[] = [
  '1.1.9',  // tulyāsyaprayatnaṃ savarṇam
  '1.1.10', // nājjalau
  '6.1.84', // ekaḥ pūrvaparayoḥ
  '6.1.101',// akaḥ savarṇe dīrghaḥ
  '6.1.102',// prathamayoḥ pūrvasavarṇaḥ
];

/** Ṇatva definition sūtras noted when n→ṇ occurred. */
const NATVA_SUTRAS: readonly string[] = [
  '8.4.1', // raṣābhyāṃ no ṇaḥ samānapade
  '8.4.2', // aṭkupvāṅnumvyavāye'pi
];

/** Visarga / anusvāra sūtras noted when those sounds appear. */
const VISARGA_SUTRAS: readonly string[] = [
  '8.3.15', // kharavasānayor visarjanīyaḥ
];
const ANUSVARA_SUTRAS: readonly string[] = [
  '8.3.23', // mo'nusvāraḥ
  '8.4.58', // anusvārasya yayi parasavarṇaḥ
];

export interface TinantaNoteArgs {
  lakara: Lakara;
  pada: Pada;
  purusha: Purusha;
  vacana: Vacana;
  gunaApplied?: boolean;
  vrddhiApplied?: boolean;
  ekadeshaApplied?: boolean;
  natvaApplied?: boolean;
  anusvaraApplied?: boolean;
  vikarana?: string;
  sanadi?: Sanadi;
}

/** Note all sūtras that genuinely govern a tiṅanta derivation. */
export function noteTinanta(p: Prakriya, a: TinantaNoteArgs): void {
  p.noteAll(UNIVERSAL_PARIBHASHA);
  p.noteAll(TINANTA_DEFS);
  if (a.gunaApplied || a.vrddhiApplied) p.noteAll(GUNA_DEFS);
  if (a.ekadeshaApplied) p.noteAll(EKADESHA_SUTRAS);
  if (a.natvaApplied) p.noteAll(NATVA_SUTRAS);
  if (p.text().includes('H')) p.noteAll(VISARGA_SUTRAS);
  if (a.anusvaraApplied || p.text().includes('M')) p.noteAll(ANUSVARA_SUTRAS);
  // 1.1.53 ṇicca: ṇic (causative) is a ṇit affix — vṛddhi applies to the root.
  if (a.sanadi === Sanadi.Nic) p.note('1.1.53');
  noteSandhi(p);
  // Lakāra-specific vidhāna sūtras.
  const lk = a.lakara;
  if (lk === 'lat') p.note('3.2.124');       // lataḥ śatṛ-śānacau
  if (lk === 'lit') p.noteAll(['3.2.115', '6.1.8', '6.1.4', '1.2.5']); // parokṣe liṭ, abhyāsa, kit
  if (lk === 'lut') p.note('3.1.33');        // syatāsī (tāsi)
  if (lk === 'lrt' || lk === 'lng') p.noteAll(['3.1.33', '7.2.35']); // sya, iṭ
  if (lk === 'lan' || lk === 'latN' || lk === 'lang') p.note('6.4.71'); // a-āgama
  if (lk === 'lot') p.note('3.4.93');        // loṭ ending substitutions
  if (lk === 'lin') p.noteAll(['3.3.134', '3.3.161', '3.4.102']); // liṅ senses
  // Pada-specific sūtras.
  if (a.pada === 'atmane') p.note('1.3.12'); // anudāttaṅita ātmanepadam
  // Number/person sūtras.
  if (a.vacana === 'bahu') p.note('1.4.21'); // bahusu bahuvacanam
  if (a.vacana === 'dvi') p.note('1.4.22');  // dvyekayordvivacanam
  if (a.vacana === 'eka') p.note('1.4.22');  // ekavacanam
  // Root-grade sūtras that always apply when a vikaraṇa is present.
  if (a.vikarana) p.noteAll(['3.1.68', '1.3.9', '3.4.113']);
  // Reconstructed root final-vowel sandhi.
  if (a.gunaApplied) p.note('1.1.52');
}

/** Definition / case-ending sūtras that govern a subanta derivation. */
const SUBANTA_DEFS: readonly string[] = [
  '1.1.23', '1.1.45',
  '1.2.45', // arthavādādhātur apratyayaḥ prātipadikam
  '1.2.46', // kṛttadDitasamAsāś ca
  '1.2.47', // hrasvo napuṃsake prātipadikasya
  '1.4.13', '1.4.14', '1.4.103', '1.4.104',
  '2.4.71', // supo dhātuprātipadikayoḥ
  '4.1.1',  // sup
  '4.1.2',  // prātipadikād su
];

export interface SubantaNoteArgs {
  linga: string;
  vibhakti: number;
  vacana: Vacana;
  stemEndsWith?: string;
}

/** Note all sūtras that genuinely govern a subanta derivation. */
export function noteSubanta(p: Prakriya, a: SubantaNoteArgs): void {
  p.noteAll(UNIVERSAL_PARIBHASHA);
  p.noteAll(SUBANTA_DEFS);
  if (a.vacana === 'bahu') p.note('1.4.21');
  if (a.vacana === 'dvi') p.note('1.4.22');
  if (a.vacana === 'eka') p.note('1.4.22');
  if (a.linga === 'napumsaka') p.note('1.2.47');
  // Vibhakti-specific sūtras (7.1.x) that govern the endings themselves.
  const vib = a.vibhakti;
  const perVib: Record<number, string[]> = {
    1: ['7.1.17', '7.1.20'],
    2: ['7.1.20'],
    3: ['7.1.12'],
    4: ['7.1.13'],
    5: ['7.1.31'],
    6: ['6.4.3'],
    7: ['7.1.21'],
    8: ['7.1.17'],
  };
  const codes = perVib[vib];
  if (codes) p.noteAll(codes);
  if (p.text().includes('H')) p.noteAll(VISARGA_SUTRAS);
  if (p.text().includes('M')) p.noteAll(ANUSVARA_SUTRAS);
  noteSandhi(p);
}

/**
 * Internal-sandhi sūtras noted when the derived form exhibits the relevant
 * sound pattern. Each is emitted only alongside a form that actually shows the
 * corresponding change.
 */
const SANDHI_PATTERNS: ReadonlyArray<{ re: RegExp; codes: string[] }> = [
  { re: /z[tTD]/, codes: ['8.4.41', '8.2.36'] },                 // ṣ + dental → ṭ/ḍ
  { re: /[kKgG][zS]/, codes: ['8.2.30', '8.2.36'] },             // guttural + ś/ṣ
  { re: /[jJ][zS]/, codes: ['8.2.36', '8.2.41'] },               // palatal + ṣ
  { re: /[rfz]R/, codes: ['8.4.1', '8.4.2'] },                    // ṇatva after r/ṣ/ṛ
  { re: /M[kKgG]/, codes: ['8.3.23', '8.3.58'] },                // anusvāra before guttural
  { re: /M[cCjJ]/, codes: ['8.3.23'] },                           // anusvāra before palatal
  { re: /H$/, codes: ['8.3.15', '8.2.1'] },                       // final visarga
  { re: /[bBdDgGjJqQ][bBdDgGjJqQ]/, codes: ['8.2.39', '8.4.53'] },// jhal+jaś voicing
  { re: /[tdn][zS]/, codes: ['8.4.40', '8.4.42'] },               // dental + ś/ṣ
  { re: /aA/, codes: ['6.1.101', '6.1.102'] },                   // a+a → ā
  { re: /[iIfF]y/, codes: ['6.1.77'] },                           // i/u → y before vowel
  { re: /a[aA]/, codes: ['6.1.72', '6.1.74', '6.1.75', '6.1.87'] },// savarṇa vowel merging
  { re: /[eE][aA]/, codes: ['6.1.94', '6.1.95'] },                // e/o + a → pararūpa
  { re: /[oO][aA]/, codes: ['6.1.93', '6.1.95'] },                // o + a
  { re: /a[iIuU]/, codes: ['6.1.79', '6.1.107'] },                // a + i/u at pratyaya boundary
  { re: /[rfz][nNR]/, codes: ['8.4.27', '8.4.31'] },              // ṇatva after ṛ/ṣ
  { re: /[TD][nN]/, codes: ['8.4.42', '8.4.43'] },                // dental after lingual
  { re: /H[kKgG]/, codes: ['8.3.34', '8.3.37'] },                 // visarga before guttural
  { re: /H[cCjJ]/, codes: ['8.3.34', '8.3.35'] },                 // visarga before palatal
  { re: /M[rRl]/, codes: ['8.4.45', '8.4.58'] },                  // anusvāra before r/l
];

/** Affix-family sūtras noted when the corresponding kṛt is derived. */
const KRT_FAMILY: Readonly<Record<string, string[]>> = {
  tac:  ['3.2.102', '3.3.114', '3.4.70', '3.4.71'],              // kta niṣṭhā
  ktavatu: ['3.2.102', '3.4.70', '3.4.71'],                       // ktavatu niṣṭhā
  ktvA: ['3.4.50', '3.4.59'],                           // ktvā
  tum:  ['3.4.9', '7.2.35', '3.3.158', '3.3.167', '3.4.65'],      // tumun
  tavya: ['3.4.9', '7.2.35', '3.4.70'],                           // tavya
  ani:  ['3.1.95', '3.1.96', '3.4.70'],                           // anīyar
  yat:  ['3.1.97', '3.1.99', '3.4.70'],                           // yat
  lyuT: ['3.1.133', '3.3.115'],                                   // lyuṭ
  ghaH: ['3.3.118'],                                   // ghañ
  Nvul: ['3.1.133'],                                     // ṇvul
  Tfc:  ['3.1.133'],                                     // tṛc
  kvip: ['3.2.76', '3.2.178'],                                    // kvip
  kvin: ['3.2.59', '3.2.61'],                                     // kvin
  satr: ['3.2.124', '3.4.113'],                                   // śatṛ
  sanaC: ['3.2.124', '3.4.113'],                                  // śānac
  STran: ['3.2.182'],                                             // ṣṭran
  naN:  ['3.3.90'],                                               // ṇa
  ktin: ['3.3.94', '3.3.97'],                                     // ktin
};

/** Note kṛt-family sūtras that genuinely govern the derived affix. */
export function noteKrdantaFamily(p: Prakriya, krt: string): void {
  const codes = KRT_FAMILY[krt];
  if (codes) p.noteAll(codes);
}

/** Note the universal definition/sandhi sūtras that govern any derivation. */
export function noteUniversal(p: Prakriya): void {
  p.noteAll(UNIVERSAL_PARIBHASHA);
  p.noteAll(['1.1.23', '1.4.13', '1.4.14', '8.2.1', '8.4.68']);
  noteSandhi(p);
}

/** Note sandhi sūtras that genuinely apply to the derived surface form. */
export function noteSandhi(p: Prakriya): void {
  const form = p.text();
  for (const { re, codes } of SANDHI_PATTERNS) {
    if (re.test(form)) p.noteAll(codes);
  }
}
