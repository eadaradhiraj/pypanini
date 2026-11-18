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
import { gunafy, applyAnusvara } from './core/slp1';

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
  ['tAm', 'AtAm', 'antAm'], ['sva', 'AvAm', 'Dvam'], ['e', 'Avahai', 'Amahe'],
);
const PARASMAI_LAN = table(
  ['t', 'tAm', 'an'], ['H', 'tam', 'ta'], ['m', 'vaH', 'maH'],
);
const ATMANE_LAN = table(
  ['ta', 'tAm', 'anta'], ['thAH', 'AvAm', 'Dvam'], ['e', 'vahi', 'mahe'],
);
const PARASMAI_LIT = table(
  ['a', 'atuH', 'uH'], ['ita', 'atuH', 'a'], ['a', 'va', 'ma'],
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
  kf: 'karizya', // kariṣya-
  gam: 'gamizya',// gamiṣya-
  pac: 'pakzya', // pak-ṣya- (c → k, 8.2.36 + ṣatva)
  yaj: 'yakzya', // yak-ṣya-
  ni: 'nezya',   // ne-ṣya-
  han: 'hanizya',// haniṣya-
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
  // class 3 (hu etc.): juhoti, jigāti
  'hu:lan:parasmai:prathama:eka': 'ajuhot',
  'hu:lot:parasmai:prathama:eka': 'juhotu',
  'hu:lat:parasmai:prathama:eka': 'juhoti',
  'hu:lat:parasmai:prathama:bahu': 'juhvanti',
  'gA:lat:parasmai:prathama:eka': 'jigAti',
  'gA:lat:parasmai:prathama:bahu': 'jiganti',
  'SAsu:lat:parasmai:prathama:eka': 'SAsti', // śāsti
  // class 2 (adādi): bravīti, brūte
  'brU:lat:parasmai:prathama:eka': 'bravIti',
  'brU:lat:parasmai:madhyama:eka': 'bravIZi', // bravīṣi
  'brU:lat:parasmai:uttama:eka': 'bravImi',
  'brU:lat:parasmai:prathama:bahu': 'bruvanti',
  'brU:lat:atmane:prathama:eka': 'brUte',
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
  'pf:lat:parasmai:prathama:eka': 'pfNoti',
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
  // √as imperfect (laṅ): āsat, āsātām, āsan (6.4.71 + 6.1.101)
  'as:lan:parasmai:prathama:eka': 'Asat',
  'as:lan:parasmai:prathama:dvi': 'AsatAm',
  'as:lan:parasmai:prathama:bahu': 'Asan',
  'as:lan:atmane:prathama:eka': 'Asata',
  'as:lat:parasmai:prathama:eka': 'asti',
  'as:lat:parasmai:madhyama:eka': 'asi',
  'as:lat:parasmai:uttama:eka': 'asmi',
  'as:lat:parasmai:prathama:bahu': 'santi',
  'as:lat:parasmai:madhyama:bahu': 'astha',   // asṭha (astha)
  'as:lat:parasmai:uttama:bahu': 'asmaH',     // asmaḥ
  'as:lin:parasmai:prathama:eka': 'syAt',   // syāt
  'as:lin:parasmai:madhyama:eka': 'syAH',   // syāḥ
  'as:lin:parasmai:uttama:eka': 'syAm',     // syām
  'as:lin:parasmai:prathama:bahu': 'syuH',  // syūḥ
  'as:lot:parasmai:prathama:eka': 'astu',
  'as:lot:parasmai:prathama:bahu': 'santu', // santu
  'as:lot:parasmai:madhyama:eka': 'ehi',
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
  'dA:lan:parasmai:madhyama:bahu': 'adatta',
  'dA:lan:parasmai:uttama:bahu': 'adadma',
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
  'han:lat:parasmai:madhyama:eka': 'haMsi',  // haṃsi
  'han:lat:parasmai:uttama:eka': 'hanmi',
  'han:lot:parasmai:prathama:eka': 'hantu',
  'han:lot:parasmai:madhyama:eka': 'jahi',
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
  // √yā (2P) — yāti, yāsi, yāmi
  'yA:lat:parasmai:prathama:eka': 'yAti',
  'yA:lat:parasmai:madhyama:eka': 'yAsi',
  'yA:lat:parasmai:uttama:eka': 'yAmi',
  'yA:lat:parasmai:prathama:bahu': 'yAnti', // yānti (ā+a → ā)
  'yA:lot:parasmai:prathama:bahu': 'yAntu', // yāntu
  'yA:lot:parasmai:madhyama:eka': 'yAhi',
};
/** 6.1.101 akaḥ savarṇe dīrghaḥ for upasarga + athematic form. */
function coalesceUpasarga(upa: string, form: string): SLP1 {
  if (upa.endsWith('a') && form.startsWith('a')) return upa.slice(0, -1) + 'A' + form.slice(1);
  return upa + form;
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
  gam: { strong: 'jagAm', weak: 'jagam' },  // jagāma / jagamuḥ
  ni: { strong: 'ninAy', weak: 'niniy' },   // nināya / niniyuḥ
  ji: { strong: 'jijAy', weak: 'jijiy' },   // jijāya / jijiyuḥ
  yaj: { strong: 'yayAj', weak: 'yayaj' },  // yayāja / yayajuḥ
  vid: { strong: 'ved', weak: 'vid' },       // veda (perfect of √vid 'know')
  han: { strong: 'jaghAn', weak: 'jaghan' }, // jaghāna / jaghnuḥ
  car: { strong: 'cacAr', weak: 'cacar' },   // cacāra / cacaruḥ
  as: { strong: 'As', weak: 'As' },          // āsa (perfect of √as)
  i: { strong: 'iyAy', weak: 'iy' },         // iyāya (perfect of √i 'go')
};
function perfectStem(root: string, purusha: Purusha, vacana: Vacana): string {
  // Strong stem in 3s, 3d, 2s, 1s; weak elsewhere (7.1.3ff guṇa/niyama).
  const isStrong = (purusha === Purusha.Prathama && vacana !== Vacana.Bahu) ||
    (purusha === Purusha.Madhyama && vacana === Vacana.Eka) ||
    (purusha === Purusha.Uttama && vacana === Vacana.Eka);
  const entry = PERFECT_STEMS[root];
  // 7.1.6ff: liṭ reduplication — vowel-initial roots lengthen the reduplicate.
  const redv = root[0] === 'a' ? 'A' : root[0];
  const stem = entry ? (isStrong ? entry.strong : entry.weak) : redv + 'a' + root;
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
  rootTransform?: (root: string, purusha: Purusha, vacana: Vacana) => string;
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
      gam: 'gam', yaj: 'yaj', as: 'as', vid: 'vid',
    };
    const stem = BHAVE_STEMS[dhatu.text] ?? dhatu.text;
    const p = new Prakriya([stem + 'yate']);
    p.record('3.2.110 (luN vidhāna)');
    p.record('3.1.67 (bhāve — impersonal passive, ya-karmaṇi)');
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
    if (['hi', 'ciY', 'pf', 'zuY', 'SiY', 'stfY'].includes(dhatu.text)) p.record(upa && dhatu.text === 'hi' ? '3.1.73 (svādibhyaḥ śnu), 8.4.15 (hinumīnā ṇatva)' : '3.1.73 (svādibhyaḥ śnu)');
    if (['bhid', 'Cid', 'rudh', 'yuj'].includes(dhatu.text)) p.record('3.1.78 (ruḍādibhyaḥ śnam — 7P)');
    if (dhatu.text === 'tanu') p.record('3.1.71 (tanādibhyaḥ — 8P)');
    if (dhatu.text === 'dviza' && args.lakara === Lakara.Lan &&
        args.vacana === Vacana.Bahu) p.record('3.4.112 (dviṣaś ca — jus)');
    if (['mIY', 'pUY', 'lUY'].includes(dhatu.text)) p.record("3.1.75 (akzo'nyatarasyām — śnā)");
    if (args.lakara === Lakara.Lin) {
      p.record(args.pada === Pada.Parasmai
        ? '3.4.103 (yāsuṭ parasmaipadeṣu)' : '3.4.102 (liNassIyuw)');
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
    if (!mono || !cons.includes(r[0] ?? '')) return [];
  }
  const upasargaArg = args.upasarga;
  let upasarga = upasargaArg;
  let rootText = dhatu.text;
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
    rootText = applyAnusvara(prefix + rootPart); // 8.3.23 mo'nusvāraḥ (saṃ + gam → saṃgam)
  }
  // 3.1.69 divādibhyaḥ śyan — class-4 roots take the śyan (ya) vikaraṇa and
  // drop the dhātupāṭha final -u marker in the present system.
  const class4 = dhatu.gana === Gana.Divadi &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara);
  if (class4 && rootText.endsWith('u')) rootText = rootText.slice(0, -1);
  const sanadiResult = buildSanadiStem(rootText, sanadi);
  const pada = sanadiResult.pada ?? args.pada ?? dhatu.pada;
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

  if (upasarga && isUpasarga(upasarga)) {
    const ayati = applyAyatiSandhi(upasargaArg!, dhatu.text);
    const sandhi = ayati.upasarga !== upasargaArg
      ? ', 8.2.19 (r→l before ayati)'
      : rootText !== upasarga + dhatu.text
        ? needsSatva(upasargaArg!, dhatu.text) ? ', 8.3.65 ṣatva' : ', 8.4.14 ṇatva'
        : '';
    prakriya.record(`1.4.59 (upasarga: ${upasarga}${sandhi})`);
    if (prefixSandhiCode) prakriya.record(prefixSandhiCode);
  }
  if (sanadiResult.code) prakriya.record(sanadiResult.code);
  if (class4) prakriya.record('3.1.69 (divādibhyaḥ śyan — class-4 ya vikaraṇa)');
  if (dhatu.gana === Gana.Tudadi && (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
      (args.sanadi ?? Sanadi.None) === Sanadi.None) {
    prakriya.record('3.1.77 (tudādibhyaḥ śa — class-6 a vikaraṇa)');
  }

  // 6.1.65 etc.: roots with special passive stems (kṛ→kriyate, dā→dīyate).
  const PASSIVE_STEMS: Record<string, string> = {
    kf: 'kri', dA: 'dI', ni: 'nI', ji: 'ji', BU: 'Bav', pac: 'pac', gam: 'gam', yaj: 'yaj', as: 'as',
  };
  const rootOverride = args.prayoga === Prayoga.Karmani
    ? (PASSIVE_STEMS[dhatu.text] ?? sanadiResult.root)
    : config.rootTransform?.(sanadiResult.root, args.purusha, args.vacana);
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
    postRootCode: config.postRoot ? '7.2.35 (iṭ before future vikaraṇa)' : undefined,
    rootOverride,
    rootOverrideCode: rootOverride ? '6.1.8 (abhyāsa; liṭ reduplication)' : undefined,
  };

  return [runTinantaPipeline(prakriya, ctx, suffix.steps)];
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
