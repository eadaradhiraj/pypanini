import { Prakriya } from './core/prakriya';
import { runTinantaPipeline, RuleContext, SuffixStep } from './core/rules';
import {
  Gana,
  Lakara,
  LAKARA_LABEL,
  Pada,
  Prayoga,
  Purusha,
  Sanadi,
  TinantaArgs,
  Vacana,
} from './core/types';
import type { Dhatu, SLP1 } from './core/types';
import { resolveDhatu } from './data/dhatupatha';
import { buildSanadiStem } from './sanadi';
import {
  applyUpasargaSandhi,
  applyAyatiSandhi,
  isUpasarga,
  needsSatva,
} from './upasarga';
import { aoristKind, deriveAorist, hasAorist } from './aorist';
import { gunafy, applyAnusvara, initialNati, initialShatva } from './core/slp1';

/** A tiṅ pratyaya label plus the it-lopa steps that turn it into its surface form. */
interface SuffixInfo {
  label: string;
  steps: SuffixStep[];
}

function simple(label: string, surface: string, code = '1.3.9'): SuffixInfo {
  if (label === surface) return { label, steps: [] };
  return {
    label,
    steps: [
      { code: '1.3.3', from: label, to: label }, // it-saṃjñā (no surface change)
      { code, from: label, to: surface },
    ],
  };
}

function visarga(label: string): SuffixInfo {
  // final s → visarga (H), e.g. tas → taH
  return {
    label,
    steps: [
      { code: '1.3.3', from: label, to: label },
      { code: '8.3.15', from: label, to: label.slice(0, -1) + 'H' },
    ],
  };
}

/** Parasmaipada suffixes for lat (present). */
const PARASMAI_LAT: Record<Purusha, Record<Vacana, SuffixInfo>> = {
  [Purusha.Prathama]: {
    [Vacana.Eka]: simple('tip', 'ti'),
    [Vacana.Dvi]: visarga('tas'),
    [Vacana.Bahu]: simple('Jha', 'anti', '3.4.78 (Jha→anti)'),
  },
  [Purusha.Madhyama]: {
    [Vacana.Eka]: simple('sip', 'si'),
    [Vacana.Dvi]: visarga('thas'),
    [Vacana.Bahu]: simple('tha', 'tha'),
  },
  [Purusha.Uttama]: {
    [Vacana.Eka]: simple('mip', 'mi'),
    [Vacana.Dvi]: visarga('vas'),
    [Vacana.Bahu]: visarga('mas'),
  },
};

/** Ātmanepada suffixes for lat (present), keyed by puruṣa/vacana. */
const ATMANE_LAT: Record<Purusha, Record<Vacana, SuffixInfo>> = {
  [Purusha.Prathama]: {
    [Vacana.Eka]: simple('ta', 'te'),
    [Vacana.Dvi]: simple('tA', 'ete', '3.4.78 (tA→ete)'),
    [Vacana.Bahu]: simple('jha', 'ante', '3.4.78 (jha→ante)'),
  },
  [Purusha.Madhyama]: {
    [Vacana.Eka]: simple('tha', 'se', '3.4.78 (tha→se)'),
    [Vacana.Dvi]: simple('thA', 'ethe', '3.4.78 (thA→ethe)'),
    [Vacana.Bahu]: simple('Dve', 'Dve'),
  },
  [Purusha.Uttama]: {
    [Vacana.Eka]: simple('ma', 'e', '3.4.78 (ma→e)'),
    [Vacana.Dvi]: simple('vahi', 'vahe'), // bhavāvahe
    [Vacana.Bahu]: simple('mahe', 'mahe'), // bhavāmahe (dīrgha on the stem)
  },
};

/** vikaraṇa used by the active voice for bhvadi roots. */
const VIKARANA_KARTARI = { label: 'Sap', surface: 'a' };
/** vikaraṇa used by the passive (karmani) — yak → ya. */
const VIKARANA_KARMANI = { label: 'yak', surface: 'ya' };

/** A suffix whose label is already its surface form (no it-lopa step). */
function plain(surface: string): SuffixInfo {
  return { label: surface, steps: [] };
}

type SuffixTable = Record<Purusha, Record<Vacana, SuffixInfo>>;

function table(
  p1: [string, string, string], p2: [string, string, string], p3: [string, string, string],
): SuffixTable {
  const mk = (t: [string, string, string]): Record<Vacana, SuffixInfo> => ({
    [Vacana.Eka]: plain(t[0]), [Vacana.Dvi]: plain(t[1]), [Vacana.Bahu]: plain(t[2]),
  });
  return {
    [Purusha.Prathama]: mk(p1),
    [Purusha.Madhyama]: mk(p2),
    [Purusha.Uttama]: mk(p3),
  };
}

const PARASMAI_LOT = table(
  ['tu', 'tAm', 'antu'], ['', 'tam', 'ta'], ['Ani', 'AvaH', 'Ama'],
);
const ATMANE_LOT = table(
  ['tAm', 'AtAm', 'antAm'], ['sva', 'AvAm', 'Dvam'], ['E', 'Avahai', 'Amahe'], // 3.4.93 eta ai (1s)
);
const PARASMAI_LAN = table(
  ['t', 'tAm', 'an'], ['H', 'tam', 'ta'], ['m', 'vaH', 'maH'],
);
const ATMANE_LAN = table(
  ['ta', 'tAm', 'anta'], ['thAH', 'AvAm', 'Dvam'], ['e', 'vahi', 'mahe'],
);
const PARASMAI_LIT = table(
  ['a', 'atuH', 'uH'], ['iTa', 'athuH', 'a'], ['a', 'va', 'ma'],
);
const ATMANE_LIT = table(
  ['e', 'Ate', 'ire'], ['ise', 'Athe', 'aDve'], ['e', 'vahe', 'mahe'],
);
const PARASMAI_LIN = table(
  ['et', 'etAm', 'eyuH'], ['eH', 'etam', 'eta'], ['eyam', 'evaH', 'ema'],
);
const ATMANE_LIN = table(
  ['eta', 'eyAtAm', 'eran'], ['ethAH', 'eyAthAm', 'edhvam'], ['e', 'evahi', 'emahe'],
);
// luṭ (periphrastic future): -tṛ agent noun + auxiliary "as". 3rd person uses
// the noun's own nominative endings; 1st/2nd use the sg. noun + "as" endings.
// The endings begin at -tā (the -i belongs to the stem for roots like bhū).
const PARASMAI_LUT = table(
  ['A', 'Arau', 'AraH'], ['Asi', 'AsTaH', 'AsTa'], ['Asmi', 'AsvaH', 'AsmaH'],
);
const ATMANE_LUT = table(
  ['A', 'Arau', 'AraH'], ['Ase', 'AsAthe', 'Adhve'], ['Ahe', 'Avahe', 'Amahe'],
);

/** Periphrastic-future (luṭ) stems: -tṛ agent noun minus the nominative ending. */
const LUT_STEMS: Record<string, string> = {
  BU: 'Bavit',  // bhavitā
  dA: 'dAt',    // dātā (no -i-)
  kf: 'kart',   // kartā
  gam: 'gant',  // gantā (m → n before t)
  pac: 'pakt',  // paktā (c → k, 8.2.36)
  yaj: 'yaSt',  // yaṣṭā (j → ṣ, ṣṭ)
  ni: 'net',    // netā
  stu: 'stot',  // stotā
  han: 'hant',  // hantā
  nam: 'nant',  // nantā (m → n)
};
function lutStem(root: string): string {
  return LUT_STEMS[root] ?? gunafy(root).text + 'it'; // fallback: guṇa + i + t
}

/** Simple-future (lṛt) stems: root + (i) + sya/ṣya vikaraṇa, ready for tiṅ endings. */
const FUTURE_STEMS: Record<string, string> = {
  BU: 'Bavizya', // bhaviṣya-
  dA: 'dAsya',   // dā-sya- (no -i-)
  DA: 'DAsya',   // dhā-sya- (no -i-)
  yA: 'yAsya',   // yā-sya- (no -i-)
  kf: 'karizya', // kariṣya-
  gam: 'gamizya',// gamiṣya-
  pac: 'pakzya', // pak-ṣya- (c → k, 8.2.36 + ṣatva)
  yaj: 'yakzya', // yak-ṣya-
  ni: 'nezya',   // ne-ṣya-
  han: 'haMsya', // haṃsya- (8.3.23 mo'nusvāraḥ: n → ṃ before s; cf. 3s override below)
  vid: 'vedizya',// vediṣya-
  diS: 'dekzya', // dekṣya-
};
function futureStem(root: string): string {
  return FUTURE_STEMS[root] ?? gunafy(root).text + 'izya'; // fallback: guṇa + i + ṣya
}

/**
 * Explicit athematic present-system forms (classes 2/3/5 etc.), keyed
 * `root:lakara:pada:purusha:vacana`. Only verified common forms are listed;
 * everything else falls through to the thematic pipeline.
 */
const ATHEMATIC_FORMS: Record<string, SLP1> = {
  // √vac (2P, adādi): vakti/vakṣi/vacanti — 8.2.30 (coḥ kuḥ: c → k).
  // The 1d/1p and ātmanepada are defective/irregular; only attested forms are listed.
  'vac:lat:parasmai:prathama:eka': 'vakti',
  'vac:lat:parasmai:prathama:dvi': 'vaktaH',
  'vac:lat:parasmai:prathama:bahu': 'vacanti',
  'vac:lat:parasmai:madhyama:eka': 'vakzi',
  'vac:lat:parasmai:madhyama:dvi': 'vakthAH',
  'vac:lat:parasmai:madhyama:bahu': 'vaktha',
  'vac:lat:parasmai:uttama:eka': 'vacmi',
  'vach:lat:parasmai:prathama:eka': 'vakti',
  'vach:lat:parasmai:prathama:dvi': 'vaktaH',
  'vach:lat:parasmai:prathama:bahu': 'vacanti',
  'vach:lat:parasmai:madhyama:eka': 'vakzi',
  'vach:lat:parasmai:madhyama:dvi': 'vakthAH',
  'vach:lat:parasmai:madhyama:bahu': 'vaktha',
  'vach:lat:parasmai:uttama:eka': 'vacmi',
  // √gam present system: 7.3.77 (izugamiyamAM CaH) gam → gacch before śārvadhātuka.
  'gam:lat:parasmai:prathama:eka': 'gacchati',
  'gam:lat:parasmai:prathama:dvi': 'gacchataH',
  'gam:lat:parasmai:prathama:bahu': 'gacchanti',
  'gam:lat:parasmai:madhyama:eka': 'gacchasi',
  'gam:lat:parasmai:madhyama:dvi': 'gacchathaH',
  'gam:lat:parasmai:madhyama:bahu': 'gacchatha',
  'gam:lat:parasmai:uttama:eka': 'gacchAmi',
  'gam:lat:parasmai:uttama:dvi': 'gacchAvaH',
  'gam:lat:parasmai:uttama:bahu': 'gacchAmaH',
  'gam:lat:atmane:prathama:eka': 'gacchate',
  'gam:lat:atmane:prathama:dvi': 'gacchete',
  'gam:lat:atmane:prathama:bahu': 'gacchante',
  'gam:lat:atmane:madhyama:eka': 'gacchase',
  'gam:lat:atmane:madhyama:dvi': 'gacchethe',
  'gam:lat:atmane:madhyama:bahu': 'gacchaDve',
  'gam:lat:atmane:uttama:eka': 'gacche',
  'gam:lat:atmane:uttama:dvi': 'gacchAvahe',
  'gam:lat:atmane:uttama:bahu': 'gacchAmahe',
  // √gam present system: 7.3.77 (izugamiyamAM CaH) gam → gacch before śārvadhātuka.
  'gam:lan:parasmai:prathama:eka': 'agacchat',
  'gam:lan:parasmai:prathama:dvi': 'agacchatAm',
  'gam:lan:parasmai:prathama:bahu': 'agacchan',
  'gam:lan:parasmai:madhyama:eka': 'agacchaH',
  'gam:lan:parasmai:madhyama:dvi': 'agacchatam',
  'gam:lan:parasmai:madhyama:bahu': 'agacchata',
  'gam:lan:parasmai:uttama:eka': 'agacchAm',
  'gam:lan:parasmai:uttama:dvi': 'agacchAvaH',
  'gam:lan:parasmai:uttama:bahu': 'agacchAmaH',
  'gam:lan:atmane:prathama:eka': 'agacchata',
  'gam:lan:atmane:prathama:dvi': 'agacchatAm',
  'gam:lan:atmane:prathama:bahu': 'agacchanta',
  'gam:lan:atmane:madhyama:eka': 'agacchathAH',
  'gam:lan:atmane:madhyama:dvi': 'agacchAvAm',
  'gam:lan:atmane:madhyama:bahu': 'agacchaDvam',
  'gam:lan:atmane:uttama:eka': 'agacche',
  'gam:lan:atmane:uttama:dvi': 'agacchAvahi',
  'gam:lan:atmane:uttama:bahu': 'agacchAmahe',
  // √gam present system: 7.3.77 (izugamiyamAM CaH) gam → gacch before śārvadhātuka.
  'gam:lot:parasmai:prathama:eka': 'gacchatu',
  'gam:lot:parasmai:prathama:dvi': 'gacchatAm',
  'gam:lot:parasmai:prathama:bahu': 'gacchantu',
  'gam:lot:parasmai:madhyama:eka': 'gaccha',
  'gam:lot:parasmai:madhyama:dvi': 'gacchatam',
  'gam:lot:parasmai:madhyama:bahu': 'gacchata',
  'gam:lot:parasmai:uttama:eka': 'gacchAni',
  'gam:lot:parasmai:uttama:dvi': 'gacchAvaH',
  'gam:lot:parasmai:uttama:bahu': 'gacchAmaH',
  'gam:lot:atmane:prathama:eka': 'gacchatAm',
  'gam:lot:atmane:prathama:dvi': 'gacchetAm',
  'gam:lot:atmane:prathama:bahu': 'gacchantAm',
  'gam:lot:atmane:madhyama:eka': 'gacchasva',
  'gam:lot:atmane:madhyama:dvi': 'gacchethAm',
  'gam:lot:atmane:madhyama:bahu': 'gacchadvam',
  'gam:lot:atmane:uttama:eka': 'gacchE',
  'gam:lot:atmane:uttama:dvi': 'gacchAvahai',
  'gam:lot:atmane:uttama:bahu': 'gacchAmAhe',
  // √gam present system: 7.3.77 (izugamiyamAM CaH) gam → gacch before śārvadhātuka.
  'gam:lin:parasmai:prathama:eka': 'gacchet',
  'gam:lin:parasmai:prathama:dvi': 'gacchetAm',
  'gam:lin:parasmai:prathama:bahu': 'gaccheyuH',
  'gam:lin:parasmai:madhyama:eka': 'gaccheH',
  'gam:lin:parasmai:madhyama:dvi': 'gacchetam',
  'gam:lin:parasmai:madhyama:bahu': 'gaccheta',
  'gam:lin:parasmai:uttama:eka': 'gaccheyam',
  'gam:lin:parasmai:uttama:dvi': 'gachevaH',
  'gam:lin:parasmai:uttama:bahu': 'gacchema',
  'gam:lin:atmane:prathama:eka': 'gaccheta',
  'gam:lin:atmane:prathama:dvi': 'gaccheyAtAm',
  'gam:lin:atmane:prathama:bahu': 'gacheran',
  'gam:lin:atmane:madhyama:eka': 'gacchethAH',
  'gam:lin:atmane:madhyama:dvi': 'gaccheyAthAm',
  'gam:lin:atmane:madhyama:bahu': 'gacchedhvam',
  'gam:lin:atmane:uttama:eka': 'gacche',
  'gam:lin:atmane:uttama:dvi': 'gachevahi',
  'gam:lin:atmane:uttama:bahu': 'gacchemahe',
  // √as (2P) — asti, asi, asmi; optative syāt; imperative astu/ehi
  // class 9 (śnā 3.1.75): √mī→mināti, √pū→punāti, √lū→lunāti
  // imperative (loṭ) 2s of athematic presents
  'hi:lot:parasmai:madhyama:eka': 'hinu',
  'ciY:lot:parasmai:madhyama:eka': 'cinu',
  'pf:lot:parasmai:madhyama:eka': 'pfNu',
  'tanu:lot:parasmai:madhyama:eka': 'tanu',
  'dviza:lan:parasmai:prathama:eka': 'advezi',
  'dviza:lan:parasmai:prathama:bahu': 'adviSuH', // 3.4.112 jus
  // imperfect (laṅ) of athematic presents
  'hi:lan:parasmai:prathama:eka': 'ahinot',
  'ciY:lan:parasmai:prathama:eka': 'acinot',
  'pf:lan:parasmai:prathama:eka': 'apfNot',
  'tanu:lan:parasmai:prathama:eka': 'atanot',
  'mIY:lan:parasmai:prathama:eka': 'aminAt',
  'Asa:lat:atmane:prathama:eka': 'Aste', // āste (√ās 2Ā)
  // class 2 (adādi) u-final roots: 7.3.89 vṛddhi before pit sārvadhātuka
  'yu:lat:parasmai:prathama:eka': 'yOti',   // yauti
  'nu:lat:parasmai:prathama:eka': 'nOti',   // nauti
  'stu:lat:parasmai:prathama:eka': 'stOti', // stauti
  'ru:lat:parasmai:prathama:eka': 'rOti',   // rauti
  // class 3 (hu etc.): juhoti, jigāti
  'hu:lan:parasmai:prathama:eka': 'ajuhot',
  'hu:lot:parasmai:prathama:eka': 'juhotu',
  'hu:lat:parasmai:prathama:eka': 'juhoti',
  'hu:lat:parasmai:prathama:bahu': 'juhvanti',
  'gA:lat:parasmai:prathama:eka': 'jigAti',
  'gA:lat:parasmai:prathama:bahu': 'jiganti',
  'gA:lat:parasmai:prathama:dvi': 'jigAtuH',
  'gA:lat:parasmai:madhyama:eka': 'jigAsi',
  'gA:lat:parasmai:uttama:eka': 'jigAmi',
  'hu:lat:parasmai:prathama:dvi': 'juhutaH',
  'hu:lat:parasmai:madhyama:eka': 'juhOzi',
  'hu:lat:parasmai:uttama:eka': 'juhOmi',
  'SAsu:lat:parasmai:prathama:eka': 'SAsti', // śāsti
  // √āh (2P) — āha/āttha, 8.2.35 āhasthaḥ
  'AH:lat:parasmai:prathama:eka': 'Aha',
  'AH:lat:parasmai:madhyama:eka': 'AtTa',
  'AH:lat:parasmai:uttama:eka': 'Aha',
  // √dhā (3P, juhotyādi) — dadhāti/dhattaḥ; 8.2.38 dadhas ta-thoś ca
  'DA:lat:parasmai:prathama:eka': 'daDAti',
  'DA:lat:parasmai:prathama:dvi': 'dattaH',
  'DA:lat:parasmai:prathama:bahu': 'daDanti',
  'DA:lat:parasmai:madhyama:eka': 'daDAsi',
  'DA:lat:parasmai:madhyama:dvi': 'datTHaH',
  'DA:lat:parasmai:madhyama:bahu': 'daDAtha',
  'DA:lat:parasmai:uttama:eka': 'daDAmi',
  'DA:lat:parasmai:uttama:dvi': 'daDAvaH',
  'DA:lat:parasmai:uttama:bahu': 'daDAmaH',
  // √dhā imperfect/imperative/optative/future (juhoti class).
  'DA:lan:parasmai:prathama:eka': 'adadAt',      // adadhāt
  'DA:lan:parasmai:prathama:dvi': 'adadataH',     // adadhātām
  'DA:lan:parasmai:prathama:bahu': 'adadan',      // adadhān
  'DA:lan:parasmai:madhyama:eka': 'adadAH',       // adadhāḥ
  'DA:lan:parasmai:madhyama:dvi': 'adadAtam',     // adadhātam
  'DA:lan:parasmai:madhyama:bahu': 'adadAta',     // adadhāta
  'DA:lan:parasmai:uttama:eka': 'adadAm',         // adadhām
  'DA:lan:parasmai:uttama:dvi': 'adadAva',        // adadhāva
  'DA:lan:parasmai:uttama:bahu': 'adadAmaH',      // adadhāmaḥ
  'DA:lot:parasmai:prathama:eka': 'dadAtu',       // dadhātu
  'DA:lot:parasmai:prathama:dvi': 'dadAtAm',      // dadhātām
  'DA:lot:parasmai:prathama:bahu': 'dadAntu',     // dadhāntu
  'DA:lot:parasmai:madhyama:eka': 'dehi',         // dehi
  'DA:lot:parasmai:madhyama:dvi': 'dadAtam',      // dadhātam
  'DA:lot:parasmai:madhyama:bahu': 'dadAta',      // dadhāta
  'DA:lot:parasmai:uttama:eka': 'dadAmi',         // dadhāmi
  'DA:lot:parasmai:uttama:dvi': 'dadAva',         // dadhāva
  'DA:lot:parasmai:uttama:bahu': 'dadAma',        // dadhāma
  'DA:lin:parasmai:prathama:eka': 'dadhyAt',      // dadhyāt
  'DA:lin:parasmai:prathama:dvi': 'dadhyAtAm',    // dadhyātām
  'DA:lin:parasmai:prathama:bahu': 'dadhyuH',     // dadhyuḥ
  'DA:lin:parasmai:madhyama:eka': 'dadhyAH',      // dadhyāḥ
  'DA:lin:parasmai:madhyama:dvi': 'dadhyAtam',    // dadhyātam
  'DA:lin:parasmai:madhyama:bahu': 'dadhyata',    // dadhyata
  'DA:lin:parasmai:uttama:eka': 'dadhyAm',        // dadhyām
  'DA:lin:parasmai:uttama:bahu': 'dadhyema',      // dadhyema
  'DA:lut:parasmai:prathama:eka': 'DAtA',         // dhātā
  'DA:lut:parasmai:prathama:dvi': 'DAtArau',
  'DA:lut:parasmai:prathama:bahu': 'DAtAraH',
  'DA:lut:parasmai:madhyama:eka': 'DAtAsi',
  'DA:lut:parasmai:madhyama:dvi': 'DAtAsTaH',
  'DA:lut:parasmai:madhyama:bahu': 'DAtAsTa',
  'DA:lut:parasmai:uttama:eka': 'DAtAsmi',
  'DA:lut:parasmai:uttama:dvi': 'DAtAsvaH',
  'DA:lut:parasmai:uttama:bahu': 'DAtAsmaH',
  'DA:lrt:parasmai:prathama:eka': 'DAsyati',      // dhāsyati
  // class 2 (adādi): bravīti, brūte
  'brU:lat:parasmai:prathama:eka': 'bravIti',
  'brU:lat:parasmai:madhyama:eka': 'bravIZi', // bravīṣi
  'brU:lat:parasmai:uttama:eka': 'bravImi',
  'brU:lat:parasmai:prathama:bahu': 'bruvanti',
  'brU:lat:atmane:prathama:eka': 'brUte',
  // √brū imperfect (Whitney §632): abravīt / abruvan.
  'brU:lan:parasmai:prathama:eka': 'abravIt',
  'brU:lan:parasmai:prathama:bahu': 'abruvan',
  // class 2 (adādi): vāti, pāti, rāti, dveṣṭi
  'BA:lat:parasmai:prathama:eka': 'BAti',   // bhāti
  'mA:lat:parasmai:prathama:eka': 'mAti',   // māti
  'vA:lat:parasmai:prathama:eka': 'vAti',
  'pA:lat:parasmai:prathama:eka': 'pAti',
  'rA:lat:parasmai:prathama:eka': 'rAti',
  'dviza:lat:parasmai:prathama:eka': 'dvezwi', // dveṣṭi
  // class 8 (tanādi): √tan→tanoti, tanutaḥ, tanvanti
  'tanu:lat:parasmai:prathama:eka': 'tanoti',
  'tanu:lat:parasmai:prathama:dvi': 'tanutaH',
  'tanu:lat:parasmai:prathama:bahu': 'tanvanti',
  'tanu:lat:parasmai:uttama:eka': 'tanomi',
  // class 7 (śnam 3.1.78): √bhid→bhinatti, √chid→chinatti
  'rudh:lat:parasmai:prathama:eka': 'rundDi',   // runddhi
  'yuj:lat:atmane:prathama:eka': 'yuMkte',      // yuṅkte
  'bhid:lat:parasmai:prathama:eka': 'bhinatti',
  'bhid:lat:parasmai:prathama:bahu': 'bhindanti',
  'Cid:lat:parasmai:prathama:eka': 'chinatti',
  'Cid:lat:parasmai:prathama:bahu': 'chindanti',
  // class 5 (śnu 3.1.73): √su→sunoti, √śi→śinoti, √stṛ→stṛṇoti
  'zuY:lat:parasmai:prathama:eka': 'sunoti',
  'zuY:lat:parasmai:prathama:dvi': 'sunutaH',
  'zuY:lat:parasmai:prathama:bahu': 'sunvanti',
  'zuY:lat:parasmai:madhyama:eka': 'sunoZi',
  'zuY:lat:parasmai:uttama:eka': 'sunomi',
  'SiY:lat:parasmai:prathama:eka': 'Sinoti',
  'SiY:lat:parasmai:prathama:bahu': 'Sinvanti',
  'stfY:lat:parasmai:prathama:eka': 'stfRnoti',
  // class 5 (śnu 3.1.73): √ci→cinoti, √pṛ→pṛṇoti
  'ciY:lat:parasmai:prathama:eka': 'cinoti',
  // 3.1.60 (ciṇ te padaḥ): √ci takes ṇa before 3s ātmane te — cinute.
  'ciY:lat:atmane:prathama:eka': 'cinute',
  'ciY:lat:atmane:prathama:dvi': 'cinvAtAm',
  'ciY:lat:atmane:prathama:bahu': 'cinvate',
  'pf:lat:parasmai:prathama:eka': 'pfNoti',
  // √śru (5P, 3.1.74 śruvaḥ śṛ ca): śṛṇoti/śṛṇutaḥ/śṛṇvanti.
  'zru:lat:parasmai:prathama:eka': 'zRNoti',
  'zru:lat:parasmai:prathama:dvi': 'zRnutaH',
  'zru:lat:parasmai:prathama:bahu': 'zRnvanti',
  'zru:lat:parasmai:madhyama:eka': 'zRnozi',
  'zru:lat:parasmai:uttama:eka': 'zRnomi',
  // √jñā (9P, 3.1.81 kryādibhyaḥ śnā + 7.3.79 jñājanor jā): jānāti/jānanti.
  'jYA:lat:parasmai:prathama:eka': 'jAnAti',
  'jYA:lat:parasmai:prathama:dvi': 'jAnItaH',
  'jYA:lat:parasmai:prathama:bahu': 'jAnanti',
  'jYA:lat:parasmai:madhyama:eka': 'jAnAsi',
  'jYA:lat:parasmai:uttama:eka': 'jAnAmi',
  'mIY:lat:parasmai:prathama:eka': 'minAti',
  'mIY:lat:parasmai:prathama:bahu': 'minanti',
  'pUY:lat:parasmai:prathama:eka': 'punAti',
  'lUY:lat:parasmai:prathama:eka': 'lunAti',
  // √hi (5P, śnu vikaraṇa 3.1.73): hinoti, hinutaḥ, hinvanti
  'hi:lat:parasmai:prathama:eka': 'hinoti',
  'hi:lat:parasmai:prathama:dvi': 'hinutaH',
  'hi:lat:parasmai:prathama:bahu': 'hinvanti',
  'hi:lat:parasmai:madhyama:eka': 'hinozi',  // hinoṣi
  'hi:lat:parasmai:uttama:eka': 'hinomi',
  // √as imperfect (laṅ): āsīt, āstām, āsan (6.4.71 + 6.1.101)
  'as:lan:parasmai:prathama:eka': 'AsIt',
  'as:lan:parasmai:prathama:dvi': 'AstAm',
  'as:lan:parasmai:prathama:bahu': 'Asan',
  'as:lan:atmane:prathama:eka': 'Asata',
  'as:lat:parasmai:prathama:eka': 'asti',
  'as:lat:parasmai:prathama:dvi': 'astaH',   // staḥ
  'as:lat:parasmai:madhyama:dvi': 'asTHaH',  // sthaḥ
  'as:lat:parasmai:uttama:dvi': 'asvaH',     // svaḥ
  'as:lat:parasmai:madhyama:eka': 'asi',
  'as:lat:parasmai:uttama:eka': 'asmi',
  'as:lat:parasmai:prathama:bahu': 'santi',
  'as:lat:parasmai:madhyama:bahu': 'sTHa',    // stha (स्थ)
  'as:lat:parasmai:uttama:bahu': 'asmaH',     // asmaḥ
  'as:lin:parasmai:prathama:eka': 'syAt',   // syāt
  'as:lin:parasmai:madhyama:eka': 'syAH',   // syāḥ
  'as:lin:parasmai:uttama:eka': 'syAm',     // syām
  'as:lin:parasmai:prathama:bahu': 'syuH',  // syūḥ
  'as:lin:parasmai:prathama:dvi': 'syAtAm',  // syātām
  'as:lin:parasmai:madhyama:dvi': 'syAtam',  // syātam
  'as:lin:parasmai:madhyama:bahu': 'syAta',  // syāta
  'as:lin:parasmai:uttama:dvi': 'syAvaH',    // syāvaḥ
  'as:lin:parasmai:uttama:bahu': 'syAma',    // syāma
  // √as uses bhav- stem for the futures (bhūsuppletism).
  'as:lut:parasmai:prathama:eka': 'BavitA',
  'as:lut:parasmai:prathama:dvi': 'BavitArau',
  'as:lut:parasmai:prathama:bahu': 'BavitAraH',
  'as:lut:parasmai:madhyama:eka': 'BavitAsi',
  'as:lut:parasmai:madhyama:dvi': 'BavitAsTaH',
  'as:lut:parasmai:madhyama:bahu': 'BavitAsTa',
  'as:lut:parasmai:uttama:eka': 'BavitAsmi',
  'as:lut:parasmai:uttama:dvi': 'BavitAsvaH',
  'as:lut:parasmai:uttama:bahu': 'BavitAsmaH',
  'as:lrt:parasmai:prathama:eka': 'Bavizyati',
  'as:lrt:parasmai:prathama:dvi': 'BavizyataH',
  'as:lrt:parasmai:prathama:bahu': 'Bavizyanti',
  'as:lrt:parasmai:madhyama:eka': 'Bavizyasi',
  'as:lrt:parasmai:madhyama:dvi': 'BavizyathaH',
  'as:lrt:parasmai:madhyama:bahu': 'Bavizyatha',
  'as:lrt:parasmai:uttama:eka': 'BavizyAmi',
  'as:lrt:parasmai:uttama:dvi': 'BavizyAvaH',
  'as:lrt:parasmai:uttama:bahu': 'BavizyAmaH',
  'as:lot:parasmai:prathama:eka': 'astu',
  'as:lot:parasmai:prathama:bahu': 'santu', // santu
  'as:lot:parasmai:madhyama:eka': 'ehi',
  // 8.2.31 (ho ḍhaḥ): √vah/√sah future agent — voḍhā/soḍhā.
  'vah:lut:parasmai:prathama:eka': 'voDhA',
  'sah:lut:parasmai:prathama:eka': 'soDhA',
  // √han future: haṃsyati (8.4.22 ṇatva after upasarga, nasal here inherent).
  'han:lrt:parasmai:prathama:eka': 'haMsyati',
  // √dā (3P) — dadāti, dadāsi, dadāmi; dehi; dadātu
  'dA:lat:parasmai:prathama:eka': 'dadAti',
  'dA:lat:parasmai:prathama:dvi': 'dattaH',    // dattaḥ
  'dA:lat:parasmai:prathama:bahu': 'dadati',
  'dA:lat:parasmai:madhyama:eka': 'dadAsi',
  'dA:lat:parasmai:madhyama:dvi': 'datTaH',    // datthaḥ
  'dA:lat:parasmai:madhyama:bahu': 'datTa',
  'dA:lat:parasmai:uttama:eka': 'dadAmi',
  'dA:lat:parasmai:uttama:dvi': 'dadvaH',
  'dA:lat:parasmai:uttama:bahu': 'dadmaH',
  // √dā imperfect / optative full paradigms
  'dA:lan:parasmai:madhyama:dvi': 'adadAtam', 'dA:lan:parasmai:madhyama:bahu': 'adadAta',
  'dA:lan:parasmai:uttama:dvi': 'adadAvaH', 'dA:lan:parasmai:uttama:bahu': 'adadAmaH',
  'dA:lin:parasmai:madhyama:dvi': 'dadyAtam', 'dA:lin:parasmai:madhyama:bahu': 'dadyata',
  'dA:lin:parasmai:uttama:dvi': 'dadyAvaH', 'dA:lin:parasmai:uttama:bahu': 'dadyema',
  'dA:lat:atmane:prathama:eka': 'datte',
  'dA:lat:atmane:prathama:dvi': 'dadAte',
  'dA:lat:atmane:prathama:bahu': 'dadate',
  'dA:lat:atmane:madhyama:eka': 'datse',
  'dA:lat:atmane:madhyama:dvi': 'dadAthe',
  'dA:lat:atmane:madhyama:bahu': 'dadDve',
  'dA:lat:atmane:uttama:eka': 'dade',
  'dA:lat:atmane:uttama:dvi': 'dadvahe',
  'dA:lat:atmane:uttama:bahu': 'dadmahe',
  'dA:lot:parasmai:prathama:eka': 'dadAtu',
  'dA:lot:parasmai:prathama:dvi': 'dattAm',
  'dA:lot:parasmai:prathama:bahu': 'dadatu',
  'dA:lot:parasmai:madhyama:eka': 'dehi',
  'dA:lot:parasmai:madhyama:dvi': 'dattam',
  'dA:lot:parasmai:madhyama:bahu': 'datta',
  'dA:lot:parasmai:uttama:eka': 'dadAni',
  'dA:lot:parasmai:uttama:dvi': 'dadAva',
  'dA:lot:parasmai:uttama:bahu': 'dadAma',
  'dA:lin:parasmai:prathama:eka': 'dadyAt',
  'dA:lin:parasmai:prathama:dvi': 'dadyAtAm',
  'dA:lin:parasmai:prathama:bahu': 'dadyuH',
  'dA:lin:parasmai:madhyama:eka': 'dadyAH',
  'dA:lin:parasmai:uttama:eka': 'dadyAm',
  'dA:lan:parasmai:prathama:eka': 'adadAt',
  'dA:lan:parasmai:prathama:dvi': 'adattAm',
  'dA:lan:parasmai:prathama:bahu': 'adaduH',
  'dA:lan:parasmai:madhyama:eka': 'adadAH',
  'dA:lan:parasmai:uttama:eka': 'adadAm',
  'dA:lan:atmane:prathama:eka': 'adatta',
  'dA:lan:atmane:prathama:dvi': 'adadAtAm',
  'dA:lan:atmane:prathama:bahu': 'adadata',
  'dA:lan:atmane:madhyama:eka': 'adatTaH',  // adatthāḥ
  'dA:lan:atmane:madhyama:dvi': 'adadAthAm',
  'dA:lan:atmane:madhyama:bahu': 'adadDvam', // adaddhvam
  'dA:lan:atmane:uttama:eka': 'adade',
  'dA:lan:atmane:uttama:dvi': 'adadvahe',
  'dA:lan:atmane:uttama:bahu': 'adadmahe',
  // √dā perfect (dadau)
  'dA:lit:parasmai:prathama:eka': 'dadau',
  'dA:lit:parasmai:prathama:dvi': 'dadatuH',
  'dA:lit:parasmai:prathama:bahu': 'daduH',
  'dA:lit:parasmai:madhyama:eka': 'dadATa',  // dadātha
  'dA:lit:parasmai:madhyama:dvi': 'dadaTuH', // dadāthuḥ
  'dA:lit:parasmai:madhyama:bahu': 'dada',
  'dA:lit:parasmai:uttama:eka': 'dadau',
  'dA:lit:parasmai:uttama:dvi': 'dadiva',
  'dA:lit:parasmai:uttama:bahu': 'dadima',
  'dA:lit:atmane:prathama:eka': 'dade',
  'dA:lit:atmane:prathama:dvi': 'dadAte',
  'dA:lit:atmane:prathama:bahu': 'dadire',
  'dA:lit:atmane:madhyama:eka': 'dadize',   // dadiṣe
  'dA:lit:atmane:madhyama:dvi': 'dadATe',
  'dA:lit:atmane:madhyama:bahu': 'dadIDve', // dadidhve
  'dA:lit:atmane:uttama:eka': 'dade',
  'dA:lit:atmane:uttama:dvi': 'dadivahe',
  'dA:lit:atmane:uttama:bahu': 'dadimahe',
  // √kṛ (5P/8P) — karoti, karoṣi, karomi; kuru; karotu
  'kf:lat:parasmai:prathama:eka': 'karoti',
  'kf:lat:parasmai:prathama:dvi': 'kurutaH',    // kurutaḥ
  'kf:lat:parasmai:prathama:bahu': 'kurvanti',
  'kf:lat:parasmai:madhyama:eka': 'karozi',     // karoṣi
  'kf:lat:parasmai:madhyama:dvi': 'kuruTaH',    // kuruthaḥ
  'kf:lat:parasmai:madhyama:bahu': 'kuruTa',    // kurutha
  'kf:lat:parasmai:uttama:eka': 'karomi',
  'kf:lat:parasmai:uttama:dvi': 'kurvaH',       // kurvaḥ
  'kf:lat:parasmai:uttama:bahu': 'kurmaH',      // kurmaḥ
  'kf:lot:parasmai:prathama:eka': 'karotu',
  'kf:lot:parasmai:prathama:dvi': 'kurutAm',
  'kf:lot:parasmai:prathama:bahu': 'kurvantu',
  'kf:lot:parasmai:madhyama:eka': 'kuru',
  'kf:lot:parasmai:madhyama:dvi': 'kurutam',
  'kf:lot:parasmai:madhyama:bahu': 'kuruta',
  'kf:lot:parasmai:uttama:eka': 'karavARi',
  'kf:lot:parasmai:uttama:dvi': 'karavAva',
  'kf:lot:parasmai:uttama:bahu': 'karavAma',
  'kf:lin:parasmai:prathama:eka': 'kuryAt',     // kuryāt
  'kf:lin:parasmai:prathama:dvi': 'kuryAtAm',
  'kf:lin:parasmai:prathama:bahu': 'kuryuH',
  'kf:lin:parasmai:madhyama:eka': 'kuryAH',
  'kf:lin:parasmai:madhyama:dvi': 'kuryAtam',
  'kf:lin:parasmai:madhyama:bahu': 'kuryAta',
  'kf:lin:parasmai:uttama:eka': 'kuryAm',
  'kf:lin:parasmai:uttama:dvi': 'kuryAva',
  'kf:lin:parasmai:uttama:bahu': 'kuryAma',
  'kf:lan:parasmai:prathama:eka': 'aKarot',    // akarot
  'kf:lan:parasmai:prathama:dvi': 'akurutAm',
  'kf:lan:parasmai:prathama:bahu': 'akurvan',
  'kf:lan:parasmai:madhyama:eka': 'akaroH',
  'kf:lan:parasmai:madhyama:dvi': 'akurutam',
  'kf:lan:parasmai:madhyama:bahu': 'akuruta',
  'kf:lan:parasmai:uttama:eka': 'akaravam',
  'kf:lan:parasmai:uttama:dvi': 'akurva',
  'kf:lan:parasmai:uttama:bahu': 'akurma',
  // √han (2P) — hanti, haṃsi; jahi; hantu
  'han:lat:parasmai:prathama:eka': 'hanti',
  'han:lat:parasmai:prathama:bahu': 'ghnanti', // ghnanti — weak stem ghn- (3p)
  'han:lan:parasmai:prathama:bahu': 'aghnan',   // aghnan — weak stem ghn- (3p imperfect)
  'han:lot:parasmai:prathama:bahu': 'ghnantu',  // ghnantu — weak stem ghn- (3p imperative)
  'han:lat:parasmai:madhyama:eka': 'haMsi',  // haṃsi
  'han:lat:parasmai:uttama:eka': 'hanmi',
  'han:lot:parasmai:prathama:eka': 'hantu',
  'han:lot:parasmai:madhyama:eka': 'jahi',
  'SAsu:lot:parasmai:madhyama:eka': 'SAdhi', // 6.4.35 śā hau — śādhi
  // √kṛ (8P/5Ā) — ātmane kurute, kuruṣe, kurve
  'kf:lat:atmane:prathama:eka': 'kurute',
  'kf:lat:atmane:prathama:dvi': 'kurvAte',
  'kf:lat:atmane:prathama:bahu': 'kurvate',
  'kf:lat:atmane:madhyama:eka': 'kuruze',   // kuruṣe
  'kf:lat:atmane:madhyama:dvi': 'kurvATe',  // kurvāthe
  'kf:lat:atmane:madhyama:bahu': 'kuruDve', // kurudhve
  'kf:lat:atmane:uttama:eka': 'kurvE',      // kurve
  'kf:lat:atmane:uttama:dvi': 'kurvahe',
  'kf:lat:atmane:uttama:bahu': 'kurmahe',
  'kf:lot:atmane:prathama:eka': 'kurutAm',
  'kf:lot:atmane:prathama:dvi': 'kurvAtAm',
  'kf:lot:atmane:prathama:bahu': 'kurvatAm',
  'kf:lot:atmane:madhyama:eka': 'kuruzva',  // kuruṣva
  'kf:lot:atmane:madhyama:dvi': 'kurvAthAm',
  'kf:lot:atmane:madhyama:bahu': 'kuruDvam', // kurudhvam
  'kf:lot:atmane:uttama:eka': 'karavai',
  'kf:lin:atmane:prathama:eka': 'kurvIta',  // kurvīta
  'kf:lin:atmane:prathama:dvi': 'kurvIyAtAm',
  'kf:lin:atmane:prathama:bahu': 'kurvIran',
  'kf:lin:atmane:madhyama:eka': 'kurvITHaH', // kurvīthāḥ
  'kf:lin:atmane:uttama:eka': 'kurvIya',
  'kf:lan:atmane:prathama:eka': 'akuruta',
  'kf:lan:atmane:prathama:dvi': 'akurvAtAm',
  'kf:lan:atmane:prathama:bahu': 'akurvata',
  // √i (2P) — eti, eṣi, emi; etu/ehi
  'i:lat:parasmai:prathama:eka': 'eti',
  'i:lat:parasmai:madhyama:eka': 'ezi',    // eṣi
  'i:lat:parasmai:uttama:eka': 'emi',
  'i:lat:parasmai:prathama:bahu': 'yAnti', // yānti
  'i:lot:parasmai:prathama:eka': 'etu',
  'i:lot:parasmai:prathama:bahu': 'yAntu', // yāntu
  'i:lot:parasmai:madhyama:eka': 'ehi',
  // √i future: etā (etA), eṣyati (ezyati) — guṇa i→e, no iṭ.
  'i:lut:parasmai:prathama:eka': 'etA',
  'i:lut:parasmai:prathama:dvi': 'etArau',
  'i:lut:parasmai:prathama:bahu': 'etAraH',
  'i:lut:parasmai:madhyama:eka': 'etAsi',
  'i:lut:parasmai:madhyama:dvi': 'etAsTaH',
  'i:lut:parasmai:madhyama:bahu': 'etAsTa',
  'i:lut:parasmai:uttama:eka': 'etAsmi',
  'i:lut:parasmai:uttama:dvi': 'etAsvaH',
  'i:lut:parasmai:uttama:bahu': 'etAsmaH',
  'i:lrt:parasmai:prathama:eka': 'ezyati',
  'i:lrt:parasmai:prathama:dvi': 'ezyataH',
  'i:lrt:parasmai:prathama:bahu': 'ezyanti',
  'i:lrt:parasmai:madhyama:eka': 'ezyasi',
  'i:lrt:parasmai:madhyama:dvi': 'ezyathaH',
  'i:lrt:parasmai:madhyama:bahu': 'ezyatha',
  'i:lrt:parasmai:uttama:eka': 'ezyAmi',
  'i:lrt:parasmai:uttama:dvi': 'ezyAvaH',
  'i:lrt:parasmai:uttama:bahu': 'ezyAmaH',
  // √vac future: vaktā/vakṣyati (8.2.30 coḥ kuḥ).
  'vac:lut:parasmai:prathama:eka': 'vaktA',
  'vac:lrt:parasmai:prathama:eka': 'vakzyati',
  // √bhid (7P) future bhettā/bhetsyati; imperfect abhinat.
  'bhid:lan:parasmai:prathama:eka': 'abhinat',
  'bhid:lut:parasmai:prathama:eka': 'bhettA',
  'bhid:lrt:parasmai:prathama:eka': 'bhetsyati',
  // √yuj (7P) future yoktā/yokṣyati.
  'yuj:lut:parasmai:prathama:eka': 'yoktA',
  'yuj:lrt:parasmai:prathama:eka': 'yokzyati',
  // 8.2.18 (kṛpo ro laḥ): √kṛp → klṛp; guṇa gives kalp- in the present.
  'kfpa:lat:parasmai:prathama:eka': 'kalpati',
  'kfpa:lat:parasmai:prathama:bahu': 'kalpanti',
  'kfpa:lat:atmane:prathama:eka': 'kalpate',
  // √yā (2P) — yāti, yāsi, yāmi
  'yA:lat:parasmai:prathama:eka': 'yAti',
  'yA:lat:parasmai:madhyama:eka': 'yAsi',
  'yA:lat:parasmai:uttama:eka': 'yAmi',
  'yA:lat:parasmai:prathama:bahu': 'yAnti', // yānti (ā+a → ā)
  'yA:lot:parasmai:prathama:bahu': 'yAntu', // yāntu
  'yA:lot:parasmai:madhyama:eka': 'yAhi',
  // √yā optative/future paradigms (yāyāt/yātā/yāsyati).
  'yA:lin:parasmai:prathama:eka': 'yAyAt',
  'yA:lin:parasmai:prathama:dvi': 'yAyAtAm',
  'yA:lin:parasmai:prathama:bahu': 'yAyuH',
  'yA:lin:parasmai:madhyama:eka': 'yAyAH',
  'yA:lin:parasmai:uttama:eka': 'yAyAm',
  'yA:lut:parasmai:prathama:eka': 'yAtA',
  'yA:lrt:parasmai:prathama:eka': 'yAsyati',
  'yA:lrt:parasmai:prathama:bahu': 'yAsyanti',
  // √i (2P): additional athematic forms (weak stem i-/y-), source: bhagavadgita.org.in.
  // e.g. itaH/ithaH/ivaH (not *ayataH), Et (not *ayat), iyAt (not *ayet).
  'i:lat:parasmai:prathama:dvi': 'itaH',
  'i:lat:parasmai:madhyama:dvi': 'ithaH',
  'i:lat:parasmai:madhyama:bahu': 'itha',
  'i:lat:parasmai:uttama:dvi': 'ivaH',
  'i:lat:parasmai:uttama:bahu': 'imaH',
  'i:lat:atmane:prathama:eka': 'ite',
  'i:lat:atmane:prathama:dvi': 'iyAte',
  'i:lat:atmane:prathama:bahu': 'iyate',
  'i:lat:atmane:madhyama:eka': 'iSe',
  'i:lat:atmane:madhyama:dvi': 'iyAthe',
  'i:lat:atmane:madhyama:bahu': 'iDve',
  'i:lat:atmane:uttama:eka': 'iye',
  'i:lat:atmane:uttama:dvi': 'ivahe',
  'i:lat:atmane:uttama:bahu': 'imahe',
  'i:lan:parasmai:prathama:eka': 'Et',
  'i:lan:parasmai:prathama:dvi': 'EtAm',
  'i:lan:parasmai:prathama:bahu': 'Ayan',
  'i:lan:parasmai:madhyama:eka': 'EH',
  'i:lan:parasmai:madhyama:dvi': 'Eta',
  'i:lan:parasmai:madhyama:bahu': 'Eta',
  'i:lan:parasmai:uttama:eka': 'Ayam',
  'i:lan:parasmai:uttama:dvi': 'Eva',
  'i:lan:parasmai:uttama:bahu': 'Ema',
  'i:lan:atmane:prathama:eka': 'Eta',
  'i:lan:atmane:prathama:dvi': 'ayAtAm',
  'i:lan:atmane:prathama:bahu': 'Eyat',
  'i:lan:atmane:madhyama:eka': 'EthAH',
  'i:lan:atmane:madhyama:dvi': 'ayAthAm',
  'i:lan:atmane:madhyama:bahu': 'Edhvam',
  'i:lan:atmane:uttama:eka': 'Eyi',
  'i:lan:atmane:uttama:dvi': 'Evahi',
  'i:lan:atmane:uttama:bahu': 'Emahi',
  'i:lot:parasmai:prathama:dvi': 'itAm',
  'i:lot:parasmai:madhyama:dvi': 'itam',
  'i:lot:parasmai:madhyama:bahu': 'ita',
  'i:lot:parasmai:uttama:eka': 'ayAni',
  'i:lot:parasmai:uttama:dvi': 'ayAva',
  'i:lot:parasmai:uttama:bahu': 'ayAma',
  'i:lot:atmane:prathama:eka': 'itAm',
  'i:lot:atmane:prathama:dvi': 'yAtAm',
  'i:lot:atmane:prathama:bahu': 'yatAm',
  'i:lot:atmane:madhyama:eka': 'iSva',
  'i:lot:atmane:madhyama:dvi': 'yAthAm',
  'i:lot:atmane:madhyama:bahu': 'iDvam',
  'i:lot:atmane:uttama:eka': 'ayE',
  'i:lot:atmane:uttama:dvi': 'ayAvahai',
  'i:lot:atmane:uttama:bahu': 'ayAmAhai',
  'i:lin:parasmai:prathama:eka': 'iyAt',
  'i:lin:parasmai:prathama:dvi': 'iyAtAm',
  'i:lin:parasmai:prathama:bahu': 'iyuH',
  'i:lin:parasmai:madhyama:eka': 'iyAH',
  'i:lin:parasmai:madhyama:dvi': 'iyAtam',
  'i:lin:parasmai:madhyama:bahu': 'iyAta',
  'i:lin:parasmai:uttama:eka': 'iyAm',
  'i:lin:parasmai:uttama:dvi': 'iyAva',
  'i:lin:parasmai:uttama:bahu': 'iyAma',
  'i:lin:atmane:prathama:eka': 'iyIta',
  'i:lin:atmane:prathama:dvi': 'iyIyAtAm',
  'i:lin:atmane:prathama:bahu': 'iyIran',
  'i:lin:atmane:madhyama:eka': 'iyIthAH',
  'i:lin:atmane:madhyama:dvi': 'iyIyAthAm',
  'i:lin:atmane:madhyama:bahu': 'iyIdhvam',
  'i:lin:atmane:uttama:eka': 'iyIya',
  'i:lin:atmane:uttama:dvi': 'iyIvahi',
  'i:lin:atmane:uttama:bahu': 'iyImahi',
  'i:lrt:atmane:prathama:eka': 'ezyate',
  'i:lrt:atmane:prathama:dvi': 'ezyete',
  'i:lrt:atmane:prathama:bahu': 'ezyante',
  'i:lrt:atmane:madhyama:eka': 'ezyase',
  'i:lrt:atmane:madhyama:dvi': 'ezyethe',
  'i:lrt:atmane:madhyama:bahu': 'ezyaDve',
  'i:lrt:atmane:uttama:eka': 'ezye',
  'i:lrt:atmane:uttama:dvi': 'ezyAvahe',
  'i:lrt:atmane:uttama:bahu': 'ezyAmahe',
  'i:lng:parasmai:prathama:eka': 'Ezyat',
  'i:lng:parasmai:prathama:dvi': 'EzyatAm',
  'i:lng:parasmai:prathama:bahu': 'Ezyan',
  'i:lng:parasmai:madhyama:eka': 'EzyaH',
  'i:lng:parasmai:madhyama:dvi': 'Ezyatam',
  'i:lng:parasmai:madhyama:bahu': 'Ezyata',
  'i:lng:parasmai:uttama:eka': 'Ezyam',
  'i:lng:parasmai:uttama:dvi': 'EzyAva',
  'i:lng:parasmai:uttama:bahu': 'EzyAma',
  'i:lng:atmane:prathama:eka': 'Ezyata',
  'i:lng:atmane:prathama:dvi': 'EzyetAm',
  'i:lng:atmane:prathama:bahu': 'Ezyan',
  'i:lng:atmane:madhyama:eka': 'EzyathAH',
  'i:lng:atmane:madhyama:dvi': 'EzyethAm',
  'i:lng:atmane:madhyama:bahu': 'Ezyadhvam',
  'i:lng:atmane:uttama:eka': 'Ezye',
  'i:lng:atmane:uttama:dvi': 'EzyAvahi',
  'i:lng:atmane:uttama:bahu': 'EzyAmahi',
  'i:lut:atmane:prathama:eka': 'etA',
  'i:lut:atmane:prathama:dvi': 'etArau',
  'i:lut:atmane:prathama:bahu': 'etAraH',
  'i:lut:atmane:madhyama:eka': 'etAse',
  'i:lut:atmane:madhyama:dvi': 'etAsAthe',
  'i:lut:atmane:madhyama:bahu': 'etAdhve',
  'i:lut:atmane:uttama:eka': 'etAhe',
  'i:lut:atmane:uttama:dvi': 'etAvahe',
  'i:lut:atmane:uttama:bahu': 'etAmahe',
  'i:lit:parasmai:prathama:eka': 'iyAya',
  'i:lit:parasmai:prathama:dvi': 'IyatuH',
  'i:lit:parasmai:prathama:bahu': 'IyuH',
  'i:lit:parasmai:madhyama:eka': 'iyeTa',
  'i:lit:parasmai:madhyama:dvi': 'IyathuH',
  'i:lit:parasmai:madhyama:bahu': 'Iya',
  'i:lit:parasmai:uttama:eka': 'iyAya',
  'i:lit:parasmai:uttama:dvi': 'Iyiva',
  'i:lit:parasmai:uttama:bahu': 'Iyima',
  'i:lit:atmane:prathama:eka': 'Iye',
  'i:lit:atmane:prathama:dvi': 'IyAte',
  'i:lit:atmane:prathama:bahu': 'Iyire',
  'i:lit:atmane:madhyama:eka': 'IyiSe',
  'i:lit:atmane:madhyama:dvi': 'IyAthe',
  'i:lit:atmane:madhyama:bahu': 'Iyidhve',
  'i:lit:atmane:uttama:eka': 'Iye',
  'i:lit:atmane:uttama:dvi': 'Iyivahe',
  'i:lit:atmane:uttama:bahu': 'Iyimahe',
  // √ad (2P, adādi): attti/adanti, not *adati — source: bhagavadgita.org.in.
  // The a-aorist (aghasat) is supplied by aorist.ts.
  'ad:lat:parasmai:prathama:eka': 'atti',
  'ad:lat:parasmai:prathama:dvi': 'attaH',
  'ad:lat:parasmai:prathama:bahu': 'adanti',
  'ad:lat:parasmai:madhyama:eka': 'atsi',
  'ad:lat:parasmai:madhyama:dvi': 'atthaH',
  'ad:lat:parasmai:madhyama:bahu': 'attha',
  'ad:lat:parasmai:uttama:eka': 'admi',
  'ad:lat:parasmai:uttama:dvi': 'advaH',
  'ad:lat:parasmai:uttama:bahu': 'admaH',
  'ad:lan:parasmai:prathama:eka': 'Adat',
  'ad:lan:parasmai:prathama:dvi': 'AttAm',
  'ad:lan:parasmai:prathama:bahu': 'Adan',
  'ad:lan:parasmai:madhyama:eka': 'AdaH',
  'ad:lan:parasmai:madhyama:dvi': 'Attam',
  'ad:lan:parasmai:madhyama:bahu': 'Atta',
  'ad:lan:parasmai:uttama:eka': 'Adam',
  'ad:lan:parasmai:uttama:dvi': 'Adva',
  'ad:lan:parasmai:uttama:bahu': 'Adma',
  'ad:lin:parasmai:prathama:eka': 'adyAt',
  'ad:lin:parasmai:prathama:dvi': 'adyAtAm',
  'ad:lin:parasmai:prathama:bahu': 'adyuH',
  'ad:lin:parasmai:madhyama:eka': 'adyAH',
  'ad:lin:parasmai:madhyama:dvi': 'adyAtam',
  'ad:lin:parasmai:madhyama:bahu': 'adyAta',
  'ad:lin:parasmai:uttama:eka': 'adyAm',
  'ad:lin:parasmai:uttama:dvi': 'adyAva',
  'ad:lin:parasmai:uttama:bahu': 'adyAma',
  'ad:lot:parasmai:prathama:eka': 'attu',
  'ad:lot:parasmai:prathama:dvi': 'attAm',
  'ad:lot:parasmai:prathama:bahu': 'adantu',
  'ad:lot:parasmai:madhyama:eka': 'aDDi',
  'ad:lot:parasmai:madhyama:dvi': 'attam',
  'ad:lot:parasmai:madhyama:bahu': 'atta',
  'ad:lot:parasmai:uttama:eka': 'adAni',
  'ad:lot:parasmai:uttama:dvi': 'adAva',
  'ad:lot:parasmai:uttama:bahu': 'adAma',
  'ad:lrt:parasmai:prathama:eka': 'atsyati',
  'ad:lrt:parasmai:prathama:dvi': 'atsyataH',
  'ad:lrt:parasmai:prathama:bahu': 'atsyanti',
  'ad:lrt:parasmai:madhyama:eka': 'atsyasi',
  'ad:lrt:parasmai:madhyama:dvi': 'atsyathaH',
  'ad:lrt:parasmai:madhyama:bahu': 'atsyatha',
  'ad:lrt:parasmai:uttama:eka': 'atsyAmi',
  'ad:lrt:parasmai:uttama:dvi': 'atsyAvaH',
  'ad:lrt:parasmai:uttama:bahu': 'atsyAmaH',
  'ad:lut:parasmai:prathama:eka': 'attA',
  'ad:lut:parasmai:prathama:dvi': 'attArau',
  'ad:lut:parasmai:prathama:bahu': 'attAraH',
  'ad:lut:parasmai:madhyama:eka': 'attAsi',
  'ad:lut:parasmai:madhyama:dvi': 'attAsTHaH',
  'ad:lut:parasmai:madhyama:bahu': 'attAsTHa',
  'ad:lut:parasmai:uttama:eka': 'attAsmi',
  'ad:lut:parasmai:uttama:dvi': 'attAsvaH',
  'ad:lut:parasmai:uttama:bahu': 'attAsmaH',
  'ad:lit:parasmai:prathama:eka': 'Ad',
  'ad:lit:parasmai:prathama:dvi': 'AdatuH',
  'ad:lit:parasmai:prathama:bahu': 'AduH',
  'ad:lit:parasmai:madhyama:eka': 'AdiTa',
  'ad:lit:parasmai:madhyama:dvi': 'AdathuH',
  'ad:lit:parasmai:madhyama:bahu': 'Ad',
  'ad:lit:parasmai:uttama:eka': 'Ad',
  'ad:lit:parasmai:uttama:dvi': 'Adiva',
  'ad:lit:parasmai:uttama:bahu': 'Adima',
};
/** 6.1.101 akaḥ savarṇe dīrghaḥ for upasarga + athematic form. */
function coalesceUpasarga(upa: string, form: string): SLP1 {
  if (upa.endsWith('A') && form.startsWith('a')) return upa + form.slice(1); // 6.1.84: ā+a → ā
  if (upa.endsWith('a') && form.startsWith('a')) return upa.slice(0, -1) + 'A' + form.slice(1);
  // 6.1.89 (etyedhatyūṭhsu): a/ā + e (guṇa of √i) → ai (vṛddhi) — upa+eti → upaiti.
  if ((upa.endsWith('a') || upa.endsWith('A')) && form.startsWith('e')) {
    return upa.slice(0, -1) + 'E' + form.slice(1);
  }
  // 6.1.77 (iko yaṇ aci): i/u + vowel → y/v + vowel — anu+eti → anveti, vi+eti → vyeti.
  if (upa.endsWith('u') && /[aeiouAEIOUfFxX]/.test(form[0] ?? '')) {
    return upa.slice(0, -1) + 'v' + form;
  }
  if (upa.endsWith('i') && /[aeiouAEIOUfFxX]/.test(form[0] ?? '')) {
    return upa.slice(0, -1) + 'y' + form;
  }
  // 8.3.23 (mo'nusvāraḥ): m → anusvāra (M) before a consonant.
  return applyAnusvara(upa + form);
}
function presentForm(root: string, lakara: Lakara, pada: Pada,
  purusha: Purusha, vacana: Vacana): SLP1 | undefined {
  const key = `${root}:${lakara}:${pada}:${purusha}:${vacana}`;
  return ATHEMATIC_FORMS[key];
}

/** Perfect-tense (liṭ) reduplicated stems: strong (3s/3d/2s/1s) vs weak. */
const PERFECT_STEMS: Record<string, { strong: string; weak: string }> = {
  BU: { strong: 'baBUv', weak: 'baBUv' },   // babhūva (ū long by nature)
  pac: { strong: 'papAc', weak: 'papac' },  // papāca / papacuḥ
  kf: { strong: 'cakAr', weak: 'cakr' },    // cakāra / cakruḥ
  gam: { strong: 'jagAm', weak: 'jagm' },  // jagāma / jagmuḥ (2.4.49 gāṃ liwi)
  ni: { strong: 'ninAy', weak: 'niniy' },   // nināya / niniyuḥ
  ji: { strong: 'jijAy', weak: 'jijiy' },   // jijāya / jijiyuḥ
  yaj: { strong: 'yayAj', weak: 'yayaj' },  // yayāja / yayajuḥ
  vid: { strong: 'ved', weak: 'vid' },       // veda (perfect of √vid 'know')
  vac: { strong: 'uvAc', weak: 'uc' },      // uvāca/ūcuḥ (1.1.45 samprasāraṇam)
  DA: { strong: 'daDO', weak: 'dadh' },     // dadhau (√dhā; de-aspiration of reduplicate 8.4.54)
  yA: { strong: 'yayO', weak: 'yay' },      // yayau/yayuḥ (√yā)
  han: { strong: 'jaghAn', weak: 'jaghn' }, // jaghāna / jaghnuḥ (6.4.98)
  car: { strong: 'cacAr', weak: 'cacar' },   // cacāra / cacaruḥ
  as: { strong: 'As', weak: 'As' },          // āsa (perfect of √as)
  i: { strong: 'iyAy', weak: 'iy' },         // iyāya (perfect of √i 'go')
  pA: { strong: 'papO', weak: 'pap' },       // papau (7.1.34 āta au ṇalaḥ)
  sTA: { strong: 'tasTO', weak: 'tasth' },   // tasthau
  gAi: { strong: 'jaglO', weak: 'jagl' },    // jaglau
  jYA: { strong: 'jajYO', weak: 'jajY' },    // jajñau/jajñuḥ (7.1.34)
  vI: { strong: 'vavO', weak: 'vav' },       // vavau/vavuḥ (2.4.41 veñ vayiḥ)
};
function perfectStem(root: string, purusha: Purusha, vacana: Vacana, pada?: Pada): string {
  // Strong stem in 3s, 3d, 2s, 1s (parasmai); ātmane uses the weak stem throughout.
  const isStrong = pada !== Pada.Atmane &&
    ((purusha === Purusha.Prathama && vacana !== Vacana.Bahu) ||
    (purusha === Purusha.Madhyama && vacana === Vacana.Eka) ||
    (purusha === Purusha.Uttama && vacana === Vacana.Eka));
  const entry = PERFECT_STEMS[root];
  // 7.1.6ff: liṭ reduplication — vowel-initial roots lengthen the reduplicate.
  const redv = root[0] === 'a' ? 'A' : root[0];
  // gam takes the weak stem in the 3rd-person dual (jagmatuḥ, 2.4.49).
  // ā-final roots (pā/sthā/glai) take the au(au ṇal) form only in 1s/3s (7.1.34).
  const auRoots = ['pA', 'sTA', 'gAi', 'jYA', 'vI', 'DA', 'yA'];
  const auForm = auRoots.includes(root) &&
    ((purusha === Purusha.Prathama || purusha === Purusha.Uttama) && vacana === Vacana.Eka);
  // vac uses the samprasāraṇa weak stem in the 3d (ucatuḥ, not uvācatuḥ).
  const weakDual = ['gam', 'han', 'khan', 'vac', 'i', 'kf'].includes(root) && purusha === Purusha.Prathama && vacana === Vacana.Dvi;
  const strong = auRoots.includes(root) ? auForm : isStrong && !weakDual;
  const stem = entry ? (strong ? entry.strong : entry.weak) : redv + 'a' + root;
  // 1d endings begin with v (-va / -vahe); a stem already ending in -v drops it
  // (babhūv + va → babhūva, not *babhūvva).
  if (purusha === Purusha.Uttama && vacana === Vacana.Dvi && stem.endsWith('v')) {
    return stem.slice(0, -1);
  }
  return stem;
}

interface LakaraConfig {
  parasmai: SuffixTable;
  atmane: SuffixTable;
  vikarana: { label: string; surface: string };
  prefix?: string;
  postRoot?: string;
  rootTransform?: (root: string, purusha: Purusha, vacana: Vacana, pada?: Pada) => string;
  doGuna: boolean;
  doOAtoAv: boolean;
  doDirgha: boolean;
}

const LAKARA_CONFIG: Record<Lakara, LakaraConfig> = {
  [Lakara.Lat]: {
    parasmai: PARASMAI_LAT, atmane: ATMANE_LAT, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: true,
  },
  [Lakara.Lrt]: {
    parasmai: PARASMAI_LAT, atmane: ATMANE_LAT, vikarana: { label: '', surface: '' },
    rootTransform: futureStem, doGuna: false, doOAtoAv: false, doDirgha: false,
  },
  [Lakara.Lof]: {
    parasmai: PARASMAI_LOT, atmane: ATMANE_LOT, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: false,
  },
  [Lakara.Lot]: {
    parasmai: PARASMAI_LOT, atmane: ATMANE_LOT, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: false,
  },
  [Lakara.Lan]: {
    parasmai: PARASMAI_LAN, atmane: ATMANE_LAN, vikarana: VIKARANA_KARTARI,
    prefix: 'a', doGuna: true, doOAtoAv: true, doDirgha: true,
  },
  [Lakara.Lang]: {
    parasmai: PARASMAI_LAN, atmane: ATMANE_LAN, vikarana: { label: 'sya', surface: 'izya' },
    prefix: 'a', doGuna: true, doOAtoAv: true, doDirgha: true,
  },
  [Lakara.Lng]: {
    parasmai: PARASMAI_LAN, atmane: ATMANE_LAN, vikarana: { label: '', surface: '' },
    prefix: 'a', rootTransform: futureStem, doGuna: false, doOAtoAv: false, doDirgha: true,
  },
  [Lakara.Lit]: {
    parasmai: PARASMAI_LIT, atmane: ATMANE_LIT, vikarana: { label: '', surface: '' },
    rootTransform: perfectStem,
    doGuna: false, doOAtoAv: false, doDirgha: false,
  },
  [Lakara.Lut]: {
    parasmai: PARASMAI_LUT, atmane: ATMANE_LUT, vikarana: { label: '', surface: '' },
    rootTransform: lutStem, doGuna: false, doOAtoAv: false, doDirgha: false,
  },
  [Lakara.Lin]: {
    parasmai: PARASMAI_LIN, atmane: ATMANE_LIN, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: false,
  },
  // Legacy labels retained in the enum.
  [Lakara.LatN]: {
    parasmai: PARASMAI_LAT, atmane: ATMANE_LAT, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: true,
  },
  [Lakara.LanN]: {
    parasmai: PARASMAI_LAT, atmane: ATMANE_LAT, vikarana: VIKARANA_KARTARI,
    doGuna: true, doOAtoAv: true, doDirgha: true,
  },
};

export function getSuffixInfo(
  lakara: Lakara,
  pada: Pada,
  purusha: Purusha,
  vacana: Vacana,
): SuffixInfo {
  const config = LAKARA_CONFIG[lakara] ?? LAKARA_CONFIG[Lakara.Lat];
  const suffixTable = pada === Pada.Atmane ? config.atmane : config.parasmai;
  return suffixTable[purusha][vacana];
}

export interface TinantaResult {
  prakriya: Prakriya;
  text: string;
}

/** Derive a finite-verb form matching `args`. */
export function deriveTinantas(args: TinantaArgs): Prakriya[] {
  const dhatu = resolveDhatu(args.dhatu);
  // bhāve (impersonal passive) = passive stem + 3s ātmane -te (3.1.67/3.2.110).
  if (args.prayoga === Prayoga.Bhave) {
    const BHAVE_STEMS: Record<string, string> = {
      kf: 'kri', dA: 'dI', ni: 'nI', ji: 'ji', BU: 'Bav', pac: 'pac',
      gam: 'gam', yaj: 'ij', as: 'as', vid: 'vid', vac: 'uc', // 1.1.45 samprasāraṇam
    };
    const rawStem = BHAVE_STEMS[dhatu.text] ?? dhatu.text;
    // 6.1.65 (ṇo naḥ) / 6.1.64 (dhātvādeḥ ṣaḥ saḥ): dhātupāṭha root-initial
    // ṇ → n, ṣ → s (ṭham/mi exceptions per the bhāṣya are handled centrally).
    // Both rules are "dhātvādeḥ": they apply only to roots enumerated in the
    // dhātupāṭha (which carry a `code`), not to ad-hoc fallback root strings.
    const natiStem = dhatu.code ? initialNati(rawStem) : rawStem;
    const stem = dhatu.code ? initialShatva(natiStem) : natiStem;
    const p = new Prakriya([stem + 'yate']);
    if (stem !== rawStem) p.record(dhatu.text.startsWith('R')
      ? '6.1.65 (ṇo naḥ — root-initial ṇ → n)'
      : '6.1.64 (dhātvādeḥ ṣaḥ saḥ — root-initial ṣ → s)');
    p.record('3.2.123 (lat vidhāna)');
    p.record('3.1.67 (sārvaDhātuke yak — bhāve/impersonal passive)');
    p.record('1.3.13 (bhāvakarmaṇoḥ — ātmane-pada in impersonal)');
    if (['yaj', 'vac'].includes(dhatu.text)) {
      p.record('1.1.45 (igyaṇaḥ samprasāraṇam — ijyate/ucyate)');
    }
    p.collapse();
    return [p];
  }
  // The aorist (luṅ) uses a separate formation system; dispatch to it.
  if ((args.lakara === Lakara.LatN || args.lakara === Lakara.Lang) &&
      hasAorist(dhatu.text)) {
    const aoristPada = args.pada ?? dhatu.pada;
    const p = deriveAorist({
      root: dhatu.text,
      pada: aoristPada,
      purusha: args.purusha,
      vacana: args.vacana,
    });
    return p ? [p] : [];
  }
  // Athematic (non-Sap) present-system forms for common roots. These bypass the
  // thematic vikaraṇa and use root-specific stems/endings.
  const athematic = (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari
    ? presentForm(dhatu.text, args.lakara, args.pada ?? dhatu.pada,
        args.purusha, args.vacana)
    : undefined;
  if (athematic) {
    const upa = args.upasarga && isUpasarga(args.upasarga) ? args.upasarga : '';
    const athemForm = !upa ? athematic
      : dhatu.text === 'hi' ? upa + athematic.replace(/n/g, 'R') // 8.4.15
      : coalesceUpasarga(upa, athematic); // 6.1.101 a+a → ā (prāsti)
    const p = new Prakriya([athemForm]);
    p.record(`3.2.123 (${LAKARA_LABEL[args.lakara] ?? 'la~w'} vidhāna)`);
    p.record('3.4.78 (athematic tiṅ)');
    p.record((args.pada ?? dhatu.pada) === Pada.Atmane
      ? '1.3.12 (anudāttaṅita ātmanepadam), 1.4.100 (taṅānāvātmanepadam)'
      : '1.4.99 (laḥ parasmaipadam)');
    if (upa && args.upasarga) {
      const satva = needsSatva(args.upasarga, dhatu.text);
      const anusvara = athemForm.includes('M') ? ', 8.3.23 (mo\'nusvāraḥ)' : '';
      p.record(`1.4.59 (upasarga: ${upa}${satva ? ', 8.3.65 ṣatva' : ''}${anusvara})`);
      if (/[iu]/.test(upa[upa.length - 1] ?? '') && /[aeiouAEIOU]/.test(athematic[0] ?? '')) {
        p.record(`6.1.77 (iko yaṇ aci — ${upa.slice(-1)} + vowel → ${upa.endsWith('i') ? 'y' : 'v'}, vyeti/anveti)`);
      }
    }
    if (['hi', 'ciY', 'pf', 'zuY', 'SiY', 'stfY'].includes(dhatu.text)) p.record(upa && dhatu.text === 'hi' ? '3.1.73 (svādibhyaḥ śnu), 8.4.15 (hinumīnā ṇatva)' : '3.1.73 (svādibhyaḥ śnu)');
    if (['vac', 'vach'].includes(dhatu.text) && args.lakara === Lakara.Lat) {
      p.record('8.2.30 (coḥ kuḥ — vac + ti → vakti)');
    }
    if (dhatu.text === 'han' && args.lakara === Lakara.Lat) {
      p.record('weak stem ghn- of √han in the 3rd-person plural (ghnanti)');
    }
    if (dhatu.text === 'gam' && [Lakara.Lat, Lakara.Lan, Lakara.Lot, Lakara.Lin].includes(args.lakara)) {
      p.record('7.3.77 (izugamiyamAM CaH — gam → gacch before śārvadhātuka)');
    }
    if (['bhid', 'Cid', 'rudh', 'yuj'].includes(dhatu.text)) p.record('3.1.78 (ruḍādibhyaḥ śnam — 7P)');
    if (dhatu.text === 'tanu') p.record('3.1.79 (tanādikṛdbhyo uḥ — 8P)');
    if (['vah', 'sah'].includes(dhatu.text) && args.lakara === Lakara.Lut) {
      p.record('8.2.31 (ho ḍhaḥ — voḍhā/soḍhā in the future)');
    }
    if (dhatu.text === 'zru') p.record('3.1.74 (śruvaḥ śṛ ca — śṛṇoti)');
    if (dhatu.text === 'kfpa') p.record('8.2.18 (kṛpo ro laḥ — kalpati)');
    if (dhatu.text === 'an' && upa && /[rfz]/.test(upa)) {
      p.record('8.4.19 (aniteḥ — prāṇiti/prāṇati: n → ṇ after upasarga)');
    }
    if (dhatu.text === 'i' && upa && upa.endsWith('a')) {
      p.record('6.1.89 (etyedhatyūṭhsu — upa+eti → upaiti)');
    }
    if (dhatu.text === 'vac' && [Lakara.Lut, Lakara.Lrt].includes(args.lakara)) {
      p.record('8.2.30 (coḥ kuḥ — vaktā/vakṣyati)');
    }
    if (dhatu.text === 'bhid' && [Lakara.Lut, Lakara.Lrt].includes(args.lakara)) {
      p.record('7.2.48 (bhidādiṣu iṭ — bhettā/bhetsyati)');
    }
    if (dhatu.text === 'yuj' && [Lakara.Lut, Lakara.Lrt].includes(args.lakara)) {
      p.record('8.4.55 (khari ca — yoktā/yokṣyati)');
    }
    if (dhatu.text === 'jYA' && (args.pada ?? dhatu.pada) === Pada.Parasmai) {
      p.record('3.1.81 (kryādibhyaḥ śnā — 9P), 7.3.79 (jñājanor jā — jānāti)');
    }
    if (dhatu.text === 'ciY' && (args.pada ?? dhatu.pada) === Pada.Atmane) {
      p.record('3.1.60 (ciṇ te padaḥ — cinute/cinvate)');
    }
    if (dhatu.text === 'brU' && args.vacana === Vacana.Eka) {
      p.record('7.3.93 (bruva īṭ — bravīti/bravīṣi/bravīmi)');
    }
    if (dhatu.text === 'han' && args.lakara === Lakara.Lot &&
        args.purusha === Purusha.Madhyama && args.vacana === Vacana.Eka) {
      p.record('6.4.36 (hanter jaḥ — jahi)');
    }
    if (dhatu.text === 'SAsu' && args.lakara === Lakara.Lot &&
        args.purusha === Purusha.Madhyama && args.vacana === Vacana.Eka) {
      p.record('6.4.35 (śā hau — śādhi)');
    }
    if (dhatu.text === 'AH' && args.purusha === Purusha.Madhyama && args.vacana === Vacana.Eka) {
      p.record('8.2.35 (āhasthaḥ — āttha)');
    }
    if (args.lakara === Lakara.Lot && args.pada === Pada.Atmane &&
        args.purusha === Purusha.Uttama && args.vacana === Vacana.Eka) {
      p.record('3.4.93 (eta ai — 1s ātmane -ai)');
    }
    if (dhatu.text === 'DA' && args.lakara === Lakara.Lat && ['dvi', 'bahu'].includes(String(args.vacana)) &&
        args.purusha !== Purusha.Uttama) {
      p.record('8.2.38 (dadhas ta-thoś ca — dhattaḥ/dhatthaḥ)');
    }
    if (dhatu.text === 'dviza' && args.lakara === Lakara.Lan &&
        args.vacana === Vacana.Bahu) p.record('3.4.112 (dviṣaś ca — jus)');
    if (['yu', 'nu', 'stu', 'ru'].includes(dhatu.text) && args.lakara === Lakara.Lat) {
      p.record('7.3.89 (uto vṛddhir luki hali — yauti/nauti/stauti)');
    }
    if (dhatu.text === 'i' && args.lakara === Lakara.Lat && args.vacana !== Vacana.Eka) {
      p.record('6.4.81 (iṇo yaṇ — yanti/yantu)');
    }
    if (['hu', 'zuY'].includes(dhatu.text) && args.lakara === Lakara.Lat && args.vacana === Vacana.Bahu) {
      p.record('6.4.87 (huśnuvoḥ sārvadhātuke — juhvanti/sunvanti)');
    }
    if (['mIY', 'pUY', 'lUY'].includes(dhatu.text)) {
      p.record('3.1.81 (kryādibhyaḥ śnā — 9P)');
      if (['pUY', 'lUY'].includes(dhatu.text)) {
        p.record('7.3.80 (pvādīnāṃ hrasvaḥ — punāti/lunāti)');
      }
    }
    if (args.lakara === Lakara.Lin) {
      p.record(args.pada === Pada.Parasmai
        ? '3.4.103 (yāsuṭ parasmaipadeṣu)' : '3.4.102 (liNassIyuw)');
      if (args.purusha === Purusha.Uttama && args.vacana === Vacana.Eka) {
        p.record('3.4.116 (liNAśi — 1s -am)');
      }
    }
    p.collapse();
    return [p];
  }

  const sanadi = args.sanadi ?? Sanadi.None;
  // Pāṇini 3.1.22: yaṅ requires a monosyllabic, consonant-initial root. Rather
  // than throwing on an invalid combination, return no forms (valid grammar
  // option not available for this root).
  if (sanadi === Sanadi.Yan || sanadi === Sanadi.Yang || sanadi === Sanadi.YangLuk) {
    const r = dhatu.text;
    const vowels = 'aAiIuUfFxXeEoO';
    const cons = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL';
    const mono = [...r].filter((c) => vowels.includes(c)).length === 1;
    // 3.1.22: yaṅ requires a consonant-initial root whose vowel is in the
    // second position (CVC shape); roots like √śri (zr-i) are excluded here
    // rather than throwing later in heavyReduplicate.
    const cvc = vowels.includes(r[1] ?? '');
    if (!mono || !cons.includes(r[0] ?? '') || !cvc) return [];
  }
  const upasargaArg = args.upasarga;
  let upasarga = upasargaArg;
  let rootText = dhatu.text;
  // 6.1.65 (ṇo naḥ): root-initial ṇ → n; 6.1.64 (dhātvādeḥ ṣaḥ saḥ): ṣ → s.
  const natiText = dhatu.code ? initialNati(rootText) : rootText;
  const shatvaText = dhatu.code ? initialShatva(natiText) : natiText;
  const rootInitialCode = shatvaText !== rootText
    ? (natiText !== rootText
      ? '6.1.65 (ṇo naḥ — root-initial ṇ → n)'
      : '6.1.64 (dhātvādeḥ ṣaḥ saḥ — root-initial ṣ → s)')
    : undefined;
  rootText = shatvaText;
  let prefixSandhiCode: string | undefined;
  if (upasarga && isUpasarga(upasarga)) {
    const ayati = applyAyatiSandhi(upasarga, rootText);
    upasarga = ayati.upasarga;
    const mutatedRoot = applyUpasargaSandhi(upasargaArg!, rootText);
    // prefix/root vowel coalescence (6.1.77 iko yaṇ aci, 6.1.84 ekādeśa)
    let prefix = upasarga;
    let rootPart = mutatedRoot;
    if (upasarga.endsWith('a') && mutatedRoot.startsWith('a')) {
      // 6.1.101 akaḥ savarṇe dīrghaḥ: a + a → ā (e.g. pla + ay → plāyati).
      prefix = upasarga.slice(0, -1);
      rootPart = 'A' + mutatedRoot.slice(1);
      prefixSandhiCode = '6.1.101 (a+a → ā)';
    } else if (upasarga.endsWith('A') && mutatedRoot.startsWith('a')) {
      rootPart = mutatedRoot.slice(1);
      prefixSandhiCode = '6.1.84 (A+a → A)';
    } else if (upasarga.endsWith('i') && mutatedRoot.startsWith('a')) {
      prefix = upasarga.slice(0, -1); // i → y (yaṇ)
      rootPart = 'y' + mutatedRoot;
      prefixSandhiCode = '6.1.77 (iko yaṇ aci: i+a → ya)';
    } else if (upasarga.endsWith('u') && mutatedRoot.startsWith('a')) {
      prefix = upasarga.slice(0, -1); // u → v (yaṇ)
      rootPart = 'v' + mutatedRoot;
      prefixSandhiCode = '6.1.77 (iko yaṇ aci: u+a → va)';
    }
    const anusvaraText = applyAnusvara(prefix + rootPart); // 8.3.23 mo'nusvāraḥ
    if (anusvaraText.includes('M') && !prefix.includes('M')) {
      prefixSandhiCode = `${prefixSandhiCode ?? ''} 8.3.23 (mo'nusvāraḥ: saṃ + gam → saṃgam)`;
    }
    rootText = anusvaraText;
  }
  // 3.1.69 divādibhyaḥ śyan — class-4 roots take the śyan (ya) vikaraṇa and
  // drop the dhātupāṭha final -u marker in the present system.
  const class4 = dhatu.gana === Gana.Divadi &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara);
  if (class4 && rootText.endsWith('u')) rootText = rootText.slice(0, -1);
  // 6.4.25 (daṃśa-sañja-svañjāṃ śapi): penultimate nasal elision in the
  // present system (daśati/sajati/svajati).
  const NASAL_LOPA_SAP: Record<string, string> = { daMs: 'das', saYj: 'saj', svaYj: 'svaj', raYj: 'raj' };
  const sapNasalLopa = (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara) &&
    NASAL_LOPA_SAP[dhatu.text];
  if (sapNasalLopa) rootText = sapNasalLopa;
  // 7.3.82 (mider guṇaḥ): mid → med before śit affixes in the present system.
  const midGuna = dhatu.text === 'mid' && (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara);
  if (midGuna) rootText = 'med';
  const sanadiResult = buildSanadiStem(rootText, sanadi);
  // karmāṇi (passive) always takes ātmane-pada endings.
  const pada = sanadiResult.pada ??
    ((args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani ? Pada.Atmane : args.pada ?? dhatu.pada);
  const config = LAKARA_CONFIG[args.lakara] ?? LAKARA_CONFIG[Lakara.Lat];
  const suffixTable = pada === Pada.Atmane ? config.atmane : config.parasmai;
  const suffix = suffixTable[args.purusha][args.vacana];

  const kartariVikarana =
    args.prayoga === Prayoga.Karmani ? VIKARANA_KARMANI
      : class4 ? { label: 'Syan', surface: 'ya' }
        : config.vikarana;
  const vikarana = sanadiResult.vikarana ?? kartariVikarana;

  const initial = [sanadiResult.root, ...sanadiResult.extra];
  const prakriya = new Prakriya(initial);

  if (upasargaArg && isUpasarga(upasargaArg)) {
    const ayati = applyAyatiSandhi(upasargaArg!, dhatu.text);
    const sandhi = ayati.upasarga !== upasargaArg
      ? ', 8.2.19 (r→l before ayati)'
      : rootText !== upasargaArg + dhatu.text
        ? needsSatva(upasargaArg!, dhatu.text) ? ', 8.3.65 ṣatva' : ', 8.4.14 ṇatva'
        : '';
    prakriya.record(`1.4.59 (upasarga: ${upasarga}${sandhi})`);
    if (dhatu.text === 'an' && /[rfz]/.test(upasargaArg!)) {
      prakriya.record('8.4.19 (aniteḥ — prāṇiti/prāṇati: n → ṇ after upasarga)');
    }
    if (prefixSandhiCode) prakriya.record(prefixSandhiCode);
    if (dhatu.text === 'sad' && /[iu]$/.test(upasargaArg) && upasargaArg !== 'prati') {
      prakriya.record('8.3.66 (sadir aprateḥ — viṣīdati)');
    }
    if (dhatu.text === 'han' && (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani) {
      prakriya.record('8.4.22 (hanter atpūrvasya — ṇatva after upasarga)');
    }
  }
  if (rootInitialCode) prakriya.record(rootInitialCode);
  if (sanadiResult.code) prakriya.record(sanadiResult.code);
  if (class4) prakriya.record('3.1.69 (divādibhyaḥ śyan — class-4 ya vikaraṇa)');
  if (dhatu.text === 'tanu' && (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani) {
    prakriya.record('6.4.44 (tanoteryaki — tāyate)');
  }
  if (['vac', 'yaj'].includes(dhatu.text) && (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani) {
    prakriya.record('1.1.45 (igyaṇaḥ samprasāraṇam — ucyate/ijyate)');
  }
  // 1.4.99 / 1.4.100: the lakāra affix takes parasmai / ātmane pada.
  const karmaBhave = (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani;
  prakriya.record(pada === Pada.Atmane
    ? karmaBhave
      ? '1.3.13 (bhāvakarmaṇoḥ — ātmane-pada in passive), 1.4.100 (taṅānāvātmanepadam), 1.4.101 (tiṇas trīṇi), 1.4.102 (ekavacanādi)'
      : '1.3.12 (anudāttaṅita ātmanepadam), 1.4.100 (taṅānāvātmanepadam), 1.4.101 (tiṇas trīṇi), 1.4.102 (ekavacanādi)'
    : '1.4.99 (laḥ parasmaipadam — parasmai-pada), 1.4.101 (tiṇas trīṇi), 1.4.102 (ekavacanādi)');
  if (sapNasalLopa) prakriya.record(dhatu.text === 'raYj'
    ? '6.4.26 (rañjeś ca — rajati)'
    : '6.4.25 (daṃśa-sañja-svañjāṃ śapi — daśati/sajati/svajati)');
  if (midGuna) prakriya.record('7.3.82 (mider guṇaḥ — medati)');
  // 7.2.58 (gamer iṭ parasmaipadeṣu): √gam takes iṭ before s-initial
  // ārdhadhātuka affixes (future/desiderative) in parasmaipada — gam-i-ṣyati.
  if (dhatu.text === 'gam' && pada === Pada.Parasmai &&
      (sanadi === Sanadi.San || [Lakara.Lrt, Lakara.Lng].includes(args.lakara))) {
    prakriya.record('7.2.58 (gamer iṭ parasmaipadeṣu — gamiṣyati/jigamiṣati)');
  }
  // 8.4.16 (āni loṭ): after a ṇatva-causing upasarga, the ṇ of the lot 1s
  // ending -āni remains ṇ (pravapāṇi, parivapāṇi).
  if (args.lakara === Lakara.Lot && args.pada !== Pada.Atmane &&
      args.purusha === Purusha.Uttama && args.vacana === Vacana.Eka &&
      upasargaArg && /[rfz]/.test(upasargaArg) &&
      suffix.label === 'Ani') {
    prakriya.record('8.4.16 (āni loṭ — ṇi in loṭ 1s after r/ṣ/ṛ upasarga)');
  }
  if (dhatu.gana === Gana.Tudadi && (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
      (args.sanadi ?? Sanadi.None) === Sanadi.None) {
    prakriya.record('3.1.77 (tudādibhyaḥ śa — class-6 a vikaraṇa)');
  }

  // 6.1.65 etc.: roots with special passive stems (kṛ→kriyate, dā→dīyate).
  const PASSIVE_STEMS: Record<string, string> = {
    kf: 'kri', dA: 'dI', ni: 'nI', ji: 'ji', BU: 'Bav', pac: 'pac', gam: 'gam', as: 'as',
    sraMs: 'sras', DvaMs: 'Dvas', // 6.4.24: penultimate nasal elision before yak
    tanu: 'tA', // 6.4.44 (tanoteryaki — tāyate)
    vac: 'uc', yaj: 'ij', // 1.1.45 (igyaṇaḥ samprasāraṇam — ucyate/ijyate)
  };
  const rootOverride = args.prayoga === Prayoga.Karmani
    ? (PASSIVE_STEMS[dhatu.text] ?? sanadiResult.root)
    : args.lakara === Lakara.Lin && dhatu.text === 'han' && (args.sanadi ?? Sanadi.None) === Sanadi.None
      ? 'vad' // 2.4.42 (hano vada liNi — vadet)
      : config.rootTransform?.(sanadiResult.root, args.purusha, args.vacana, pada);
  const ctx: RuleContext = {
    prakriya,
    args: { ...args, dhatu },
    lakaraLabel: LAKARA_LABEL[args.lakara] ?? 'la~w',
    suffixLabel: suffix.label,
    vikaranaLabel: vikarana.label,
    vikaranaSurface: vikarana.surface,
    doGuna: args.prayoga === Prayoga.Karmani ? false : (sanadiResult.doGuna ?? config.doGuna),
    doOAtoAv: sanadiResult.doOAtoAv ?? config.doOAtoAv,
    doDirgha: config.doDirgha,
    prefix: config.prefix,
    prefixCode: config.prefix ? '6.4.71 (a-āgama before laṅ/lṛṅ)' : undefined,
    postRoot: config.postRoot,
    postRootCode: config.postRoot ? '7.2.35 (iṭ before future vikaraṇa), 1.1.46 (ādyantau ṭakitau)' : undefined,
    rootOverride,
    rootOverrideCode: rootOverride
      ? dhatu.text === 'han' && args.lakara === Lakara.Lin
        ? '2.4.42 (hano vada liNi — vadet)'
        : dhatu.text === 'ad' && args.lakara === Lakara.Lit
          ? '2.4.40 (liṭy anyatarasyām — āda/jakṣatuḥ)'
          : dhatu.text === 'BU' && args.lakara === Lakara.Lit
            ? '7.4.73 (bhavater aḥ), 6.4.88 (bhuvo vug — babhūva)'
            : ['gam', 'han'].includes(dhatu.text) && args.lakara === Lakara.Lit &&
            args.vacana === Vacana.Bahu
          ? '6.4.98 (gamahanādīnāṃ lopaḥ — jagmuḥ/jaghnuḥ)'
          : dhatu.text === 'gam' && args.lakara === Lakara.Lit
            ? '2.4.49 (gāṃ liwi — jagāma/jagmuḥ)'
          : ['pA', 'sTA', 'gAi', 'jYA', 'vI'].includes(dhatu.text) && args.lakara === Lakara.Lit &&
            (args.purusha === Purusha.Prathama || args.purusha === Purusha.Uttama) && args.vacana === Vacana.Eka
            ? dhatu.text === 'vI'
              ? '2.4.41 (veño vayiḥ — vavau/vavuḥ)'
              : '7.1.34 (āta au ṇalaḥ — papau/tasthau/jaglau)'
            : args.lakara === Lakara.Lit
        ? dhatu.text === 'vac'
          ? '6.1.8 (abhyāsa), 6.1.4 (pūrvo \'bhyāsaḥ), 6.1.5 (ubhe abhyastam), 1.1.45 (igyaṇaḥ samprasāraṇam — uvāca/ūcuḥ)'
          : dhatu.text === 'kf' ? '6.1.8 (abhyāsa), 6.1.4 (pūrvo \'bhyāsaḥ), 6.1.5 (ubhe abhyastam), 7.4.62 (kuhoś cuḥ: ku → cu — cakāra)' : '6.1.8 (liṭi dhātor anabhyāsasya), 1.1.59 (dvirvacane_ci — reduplication), 6.1.4 (pūrvo \'bhyāsaḥ), 6.1.5 (ubhe abhyastam)'
        : [Lakara.Lrt, Lakara.Lng].includes(args.lakara)
          ? '3.1.33 (syatāsī lṛluṭoḥ — sya vikaraṇa), 1.1.46 (ādyantau ṭakitau — iṭ placement)'
          : args.lakara === Lakara.Lut
            ? '3.1.33 (syatāsī lṛluṭoḥ — tāsi vikaraṇa)'
            : '6.1.8 (abhyāsa), 6.1.4 (pūrvo \'bhyāsaḥ), 6.1.5 (ubhe abhyastam)'
      : undefined,
  };

  const result = runTinantaPipeline(prakriya, ctx, suffix.steps);
  const { noteTinanta } = require('./core/sutra-notes');
  noteTinanta(result, {
    lakara: args.lakara, pada, purusha: args.purusha, vacana: args.vacana,
    gunaApplied: ctx.doGuna && sanadi === Sanadi.None,
    vrddhiApplied: args.lakara === Lakara.Lut,
    ekadeshaApplied: suffix.steps.some((s) => s.code.includes('6.1.84')) ||
      prakriya.history.some((s) => s.rule.includes('6.1.84') || s.rule.includes('6.1.97') || s.rule.includes('6.1.88')),
    natvaApplied: prakriya.history.some((s) => s.rule.includes('8.4.1') || s.rule.includes('ṇatva')),
    anusvaraApplied: prakriya.history.some((s) => s.rule.includes('8.3.23')),
    vikarana: vikarana.label,
  });
  return [result];
}

/** Convenience: the nine parasmai lat forms of a dhātu, keyed by puruṣa/vacana. */
export function deriveLatParadigm(dhatu: string | TinantaArgs['dhatu']): Array<{
  purusha: Purusha;
  vacana: Vacana;
  text: string;
  prakriya: Prakriya;
}> {
  const out: Array<{
    purusha: Purusha;
    vacana: Vacana;
    text: string;
    prakriya: Prakriya;
  }> = [];
  for (const purusha of [Purusha.Prathama, Purusha.Madhyama, Purusha.Uttama]) {
    for (const vacana of [Vacana.Eka, Vacana.Dvi, Vacana.Bahu]) {
      const base: TinantaArgs =
        typeof dhatu === 'string'
          ? {
              dhatu,
              lakara: Lakara.Lat,
              prayoga: Prayoga.Kartari,
              purusha,
              vacana,
              pada: Pada.Parasmai,
            }
          : {
              dhatu: dhatu as Dhatu,
              lakara: Lakara.Lat,
              prayoga: Prayoga.Kartari,
              purusha,
              vacana,
              pada: (dhatu as Dhatu).pada,
            };
      const p = deriveTinantas(base)[0];
      out.push({ purusha, vacana, text: p.text(), prakriya: p });
    }
  }
  return out;
}
