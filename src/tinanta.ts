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
  DA: 'DAt',    // dhātā (also used by the atmane path)
  kf: 'kart',   // kartā
  gam: 'gant',  // gantā (m → n before t)
  sTA: 'sTAt',  // sthātā (no iṭ after long vowel)
  pA: 'pAt',    // pātā
  jFnA: 'jFAt', // jñātā
  nI: 'net',    // netā
  ji: 'jet',    // jetā
  zru: 'zrot',  // śrotā
  muc: 'mokt',  // moktā (√muc future stem mokṣya-)
  grah: 'grahIt', // grahītā (iṭ before -tā)
  vid: 'vedit',  // veditā (also used by the atmane path)
  lab: 'labD',  // labdhā
  pac: 'pakt',  // paktā (c → k, 8.2.36)
  ad: 'att',    // attā (also used by the atmane path)
  vac: 'vakt',  // vaktā
  bhid: 'bhett', // bhettā
  yuj: 'yokt',  // yoktā
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
  pA: 'pAsya',   // pā-sya- (no -i-)
  sTA: 'sTAsya', // sthā-sya- (no -i-)
  DA: 'DAsya',   // dhā-sya- (no -i-)
  yA: 'yAsya',   // yā-sya- (no -i-)
  kf: 'karizya', // kariṣya-
  gam: 'gamizya',// gamiṣya-
  fR: 'arizya',  // ariṣya- (√ṛ)
  zru: 'zrOzya',  // śroṣya- (√śru, no iṭ)
  jFnA: 'jFAsya', // jñāsyati (no iṭ)
  pac: 'pakzya', // pak-ṣya- (c → k, 8.2.36 + ṣatva)
  yaj: 'yakzya', // yak-ṣya-
  ni: 'nezya',   // ne-ṣya-
  nI: 'nezya',   // nī → neṣyati (no iṭ)
  ji: 'jezya',   // ji → jeṣyati (no iṭ)
  muc: 'mokzya', // muc → mokṣyati (o-grade, no iṭ)
  rudh: 'rotsya', // rudh → rotsyati (guṇa + t-sya, no iṭ)
  ciY: 'cezya', ci: 'cezya',   // ci → ceṣyati (guṇa i→e, ṣatva after e)
  zuY: 'sozya', su: 'sozya',   // su → soṣyati (guṇa u→o)
  suY: 'sozya',   // normalized form of zuY (6.1.64 ṣ→s initially)
  SiY: 'Sezya', Si: 'Sezya',   // śi → śeṣyati (guṇa i→e)
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
  'zru:lan:parasmai:prathama:eka': 'azRNot',  // aśṛṇot (5P imperfect)
  // Athematic imperative (loṭ) 3s forms from present stems (sources:
  // bhagavadgita.org.in / standard): bhinattu/śṛṇotu/vaktu/rundhatu.
  'bhid:lot:parasmai:prathama:eka': 'bhinattu',
  // √śru (5P) imperative — Wiktionary śṛṇótu/śṛṇú/śṛṇávāni (z=ś, R=ṇ, f=ṛ).
  'zru:lot:parasmai:prathama:eka': 'zRNotu',
  'zru:lot:parasmai:prathama:dvi': 'zRuNutAm',
  'zru:lot:parasmai:prathama:bahu': 'zRuNvantu',
  'zru:lot:parasmai:madhyama:eka': 'zRuNu',
  'zru:lot:parasmai:madhyama:dvi': 'zRuNutam',
  'zru:lot:parasmai:madhyama:bahu': 'zRuNuta',
  'zru:lot:parasmai:uttama:eka': 'zRuNavARi',
  'zru:lot:parasmai:uttama:dvi': 'zRuNavAva',
  'zru:lot:parasmai:uttama:bahu': 'zRuNavAma',
  'vac:lot:parasmai:prathama:eka': 'vaktu',
  'rudh:lot:parasmai:prathama:eka': 'rundhatu',
  // √jñā perfect jajñau (jajFau), aorist ajñāsīt handled in aorist.ts.
  'jFnA:lit:parasmai:prathama:eka': 'jajFau',
  // √jñā perfect ātmanepada (jajñe/jajñāte/jajñire/...), used for karmani.
  'jFnA:lit:atmane:prathama:eka': 'jajFe',
  'jFnA:lit:atmane:prathama:dvi': 'jajFAte',
  'jFnA:lit:atmane:prathama:bahu': 'jajFire',
  'jFnA:lit:atmane:madhyama:eka': 'jajFize',
  'jFnA:lit:atmane:madhyama:dvi': 'jajFAthe',
  'jFnA:lit:atmane:madhyama:bahu': 'jajFiDve',
  'jFnA:lit:atmane:uttama:eka': 'jajFe',
  'jFnA:lit:atmane:uttama:dvi': 'jajFivAhe',
  'jFnA:lit:atmane:uttama:bahu': 'jajFimAhe',
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
  // class-5 imperfect weak-stem forms (acinu-/asunu-/aśinu-/astṛṇu-/aśṛṇu-)
  'ciY:lan:parasmai:prathama:dvi': 'acinutAm',
  'ciY:lan:parasmai:prathama:bahu': 'acinvan',
  'ciY:lan:parasmai:madhyama:eka': 'acinoH',
  'ciY:lan:parasmai:madhyama:dvi': 'acinutam',
  'ciY:lan:parasmai:madhyama:bahu': 'acinuta',
  'ciY:lan:parasmai:uttama:eka': 'acinavam',
  'ciY:lan:parasmai:uttama:dvi': 'acinva',
  'ciY:lan:parasmai:uttama:bahu': 'acinma',
  'zuY:lan:parasmai:prathama:dvi': 'asunutAm',
  'zuY:lan:parasmai:prathama:bahu': 'asunvan',
  'zuY:lan:parasmai:madhyama:eka': 'asunoH',
  'zuY:lan:parasmai:madhyama:dvi': 'asunutam',
  'zuY:lan:parasmai:madhyama:bahu': 'asunuta',
  'zuY:lan:parasmai:uttama:eka': 'asunavam',
  'zuY:lan:parasmai:uttama:dvi': 'asunva',
  'zuY:lan:parasmai:uttama:bahu': 'asunma',
  'SiY:lan:parasmai:prathama:dvi': 'aSinutAm',
  'SiY:lan:parasmai:prathama:bahu': 'aSinvan',
  'SiY:lan:parasmai:madhyama:eka': 'aSinoH',
  'SiY:lan:parasmai:madhyama:dvi': 'aSinutam',
  'SiY:lan:parasmai:madhyama:bahu': 'aSinuta',
  'SiY:lan:parasmai:uttama:eka': 'aSinavam',
  'SiY:lan:parasmai:uttama:dvi': 'aSinva',
  'SiY:lan:parasmai:uttama:bahu': 'aSinma',
  'stfY:lan:parasmai:prathama:dvi': 'astfRnutAm',
  'stfY:lan:parasmai:prathama:bahu': 'astfRnvan',
  'stfY:lan:parasmai:madhyama:eka': 'astfRnOH',
  'stfY:lan:parasmai:madhyama:dvi': 'astfRnutam',
  'stfY:lan:parasmai:madhyama:bahu': 'astfRnuta',
  'stfY:lan:parasmai:uttama:eka': 'astfRnavam',
  'stfY:lan:parasmai:uttama:dvi': 'astfRnva',
  'stfY:lan:parasmai:uttama:bahu': 'astfRnma',
  'zru:lan:parasmai:prathama:dvi': 'azRuNutAm',
  'zru:lan:parasmai:prathama:bahu': 'azRuNvan',
  'zru:lan:parasmai:madhyama:eka': 'azRnOH',
  'zru:lan:parasmai:madhyama:dvi': 'azRuNutam',
  'zru:lan:parasmai:madhyama:bahu': 'azRuNuta',
  'zru:lan:parasmai:uttama:eka': 'azRuNavam',
  'zru:lan:parasmai:uttama:dvi': 'azRuNva',
  'zru:lan:parasmai:uttama:bahu': 'azRuNma',
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
  // class-5 roots with indicatory markers (x/Y) that have no full table yet:
  // the marker is indicatory and the śnu vikaraṇa gives -noti in strong forms.
  'Apx:lat:parasmai:prathama:eka': 'Apnoti',   // āpnoti (√āp, vyāptau)
  'Apx:lot:parasmai:prathama:eka': 'Apnotu',
  'Apx:lan:parasmai:prathama:eka': 'Apnot',
  'Sakx:lat:parasmai:prathama:eka': 'Saknoti', // śaknoti (√śak)
  'Sakx:lot:parasmai:prathama:eka': 'Saknotu',
  'Sakx:lan:parasmai:prathama:eka': 'aSaknot',
  'kfY:lat:parasmai:prathama:eka': 'kfRNoti',  // kṛṇoti (√kṛñ)
  'kfY:lot:parasmai:prathama:eka': 'kfRNotu',
  'kfY:lan:parasmai:prathama:eka': 'akfRNot',
  'vfY:lat:parasmai:prathama:eka': 'vfRNoti',  // vṛṇoti (√vṛñ)
  'vfY:lot:parasmai:prathama:eka': 'vfRNotu',
  'vfY:lan:parasmai:prathama:eka': 'avfRNot',
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
  // √hu (juhóti, class 3) full paradigm — Wiktionary juhoti table.
  'hu:lat:parasmai:madhyama:dvi': 'juhuthaH',
  'hu:lat:parasmai:madhyama:bahu': 'juhutha',
  'hu:lat:parasmai:uttama:dvi': 'juhuvaH',
  'hu:lat:parasmai:uttama:bahu': 'juhumaH',
  'hu:lan:parasmai:prathama:dvi': 'ajuhutAm',
  'hu:lan:parasmai:prathama:bahu': 'ajuhavuH',
  'hu:lan:parasmai:madhyama:eka': 'ajuhoH',
  'hu:lan:parasmai:madhyama:dvi': 'ajuhutam',
  'hu:lan:parasmai:madhyama:bahu': 'ajuhuta',
  'hu:lan:parasmai:uttama:eka': 'ajuhavam',
  'hu:lan:parasmai:uttama:dvi': 'ajuhuva',
  'hu:lan:parasmai:uttama:bahu': 'ajuhuma',
  'hu:lot:parasmai:prathama:dvi': 'juhutAm',
  'hu:lot:parasmai:prathama:bahu': 'juhvatu',
  'hu:lot:parasmai:madhyama:eka': 'juhudhi',
  'hu:lot:parasmai:madhyama:dvi': 'juhutam',
  'hu:lot:parasmai:madhyama:bahu': 'juhuta',
  'hu:lot:parasmai:uttama:eka': 'juhavAni',
  'hu:lot:parasmai:uttama:dvi': 'juhavAva',
  'hu:lot:parasmai:uttama:bahu': 'juhavAma',
  'hu:lin:parasmai:prathama:eka': 'juhuyAt',
  'hu:lin:parasmai:prathama:dvi': 'juhuyAtAm',
  'hu:lin:parasmai:prathama:bahu': 'juhuyuH',
  'hu:lin:parasmai:madhyama:eka': 'juhuyAH',
  'hu:lin:parasmai:madhyama:dvi': 'juhuyAtam',
  'hu:lin:parasmai:madhyama:bahu': 'juhuyAta',
  'hu:lin:parasmai:uttama:eka': 'juhuyAm',
  'hu:lin:parasmai:uttama:dvi': 'juhuyAva',
  'hu:lin:parasmai:uttama:bahu': 'juhuyAma',
  'hu:lat:atmane:prathama:eka': 'juhute',
  'hu:lat:atmane:prathama:dvi': 'juhvAte',
  'hu:lat:atmane:prathama:bahu': 'juhvate',
  'hu:lat:atmane:madhyama:eka': 'juhuze',
  'hu:lat:atmane:madhyama:dvi': 'juhvAthe',
  'hu:lat:atmane:madhyama:bahu': 'juhudhve',
  'hu:lat:atmane:uttama:eka': 'juhve',
  'hu:lat:atmane:uttama:dvi': 'juhuvahe',
  'hu:lat:atmane:uttama:bahu': 'juhumahe',
  'hu:lan:atmane:prathama:eka': 'ajuhuta',
  'hu:lan:atmane:prathama:dvi': 'ajuhvAtAm',
  'hu:lan:atmane:prathama:bahu': 'ajuhvata',
  'hu:lan:atmane:madhyama:eka': 'ajuhuthAH',
  'hu:lan:atmane:madhyama:dvi': 'ajuhvAthAm',
  'hu:lan:atmane:madhyama:bahu': 'ajuhudhvam',
  'hu:lan:atmane:uttama:eka': 'ajuhvi',
  'hu:lan:atmane:uttama:dvi': 'ajuhuvahi',
  'hu:lan:atmane:uttama:bahu': 'ajuhumahi',
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
  'DA:lot:parasmai:madhyama:eka': 'Dehi',         // dhehi (√dhā; Wiktionary dadhāti)
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
  'DA:lin:parasmai:uttama:dvi': 'dadhyAva',       // dadhyāva
  'DA:lin:parasmai:uttama:bahu': 'dadhyAma',      // dadhyāma
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
  'rA:lat:parasmai:prathama:eka': 'rAti',
  'dviza:lat:parasmai:prathama:eka': 'dvezwi', // dveṣṭi
  // class 8 (tanādi): √tan→tanoti, tanutaḥ, tanvanti
  // √tanu (tanóti, class 8) — Wiktionary tanoti table.
  'tanu:lat:parasmai:prathama:eka': 'tanoti',
  'tanu:lat:parasmai:prathama:dvi': 'tanutaH',
  'tanu:lat:parasmai:prathama:bahu': 'tanvanti',
  'tanu:lat:parasmai:madhyama:eka': 'tanOzi',   // tanóṣi
  'tanu:lat:parasmai:madhyama:dvi': 'tanuthaH', // tanutháḥ
  'tanu:lat:parasmai:madhyama:bahu': 'tanutha', // tanuthá
  'tanu:lat:parasmai:uttama:eka': 'tanomi',
  'tanu:lat:parasmai:uttama:dvi': 'tanvaH',     // tanváḥ
  'tanu:lat:parasmai:uttama:bahu': 'tanmaH',    // tanmáḥ
  'tanu:lat:atmane:prathama:eka': 'tanute',
  'tanu:lat:atmane:prathama:dvi': 'tanvAte',
  'tanu:lat:atmane:prathama:bahu': 'tanvate',
  'tanu:lat:atmane:madhyama:eka': 'tanuze',
  'tanu:lat:atmane:madhyama:dvi': 'tanvAthe',
  'tanu:lat:atmane:madhyama:bahu': 'tanudhve',
  'tanu:lat:atmane:uttama:eka': 'tanve',
  'tanu:lat:atmane:uttama:dvi': 'tanvahe',
  'tanu:lat:atmane:uttama:bahu': 'tanmahe',
  'tanu:lan:parasmai:prathama:dvi': 'atanutAm',
  'tanu:lan:parasmai:prathama:bahu': 'atanvan',
  'tanu:lan:parasmai:madhyama:eka': 'atanoH',
  'tanu:lan:parasmai:madhyama:dvi': 'atanutam',
  'tanu:lan:parasmai:madhyama:bahu': 'atanuta',
  'tanu:lan:parasmai:uttama:eka': 'atanavam',
  'tanu:lan:parasmai:uttama:dvi': 'atanva',
  'tanu:lan:parasmai:uttama:bahu': 'atanma',
  'tanu:lot:parasmai:prathama:eka': 'tanotu',
  'tanu:lot:parasmai:prathama:dvi': 'tanutAm',
  'tanu:lot:parasmai:prathama:bahu': 'tanvantu',
  'tanu:lot:parasmai:madhyama:dvi': 'tanutam',
  'tanu:lot:parasmai:madhyama:bahu': 'tanuta',
  'tanu:lot:parasmai:uttama:dvi': 'tanavAva',
  'tanu:lin:parasmai:prathama:eka': 'tanuyAt',
  'tanu:lin:parasmai:prathama:dvi': 'tanuyAtAm',
  'tanu:lin:parasmai:prathama:bahu': 'tanuyuH',
  'tanu:lin:parasmai:madhyama:eka': 'tanuyAH',
  'tanu:lin:parasmai:madhyama:dvi': 'tanuyAtam',
  'tanu:lin:parasmai:madhyama:bahu': 'tanuyAta',
  'tanu:lin:parasmai:uttama:eka': 'tanuyAm',
  'tanu:lin:parasmai:uttama:dvi': 'tanuyAva',
  'tanu:lin:parasmai:uttama:bahu': 'tanuyAma',
  // class 7 (śnam 3.1.78): √bhid→bhinatti, √chid→chinatti
  'rudh:lat:parasmai:prathama:eka': 'rundDi',   // runddhi
  // √rudh (class 7) and √yuj (class 7) middle voice — Wiktionary rundháti /
  // yunákti sa-conj tables (verified via expandtemplates).
  'rudh:lat:atmane:prathama:eka': 'rundDe',
  'rudh:lat:atmane:prathama:dvi': 'runDAte',
  'rudh:lat:atmane:prathama:bahu': 'runDate',
  'rudh:lat:atmane:madhyama:eka': 'runtse',
  'rudh:lat:atmane:madhyama:dvi': 'runDATe',
  'rudh:lat:atmane:madhyama:bahu': 'rundDve',
  'rudh:lat:atmane:uttama:eka': 'runDe',
  'rudh:lat:atmane:uttama:dvi': 'runDvahe',
  'rudh:lat:atmane:uttama:bahu': 'runDmahe',
  'rudh:lot:atmane:prathama:eka': 'rundDAm',
  'rudh:lot:atmane:prathama:dvi': 'runDAtAm',
  'rudh:lot:atmane:prathama:bahu': 'runDatAm',
  'rudh:lot:atmane:madhyama:eka': 'runtsva',
  'rudh:lot:atmane:madhyama:dvi': 'runDATAm',
  'rudh:lot:atmane:madhyama:bahu': 'rundDvam',
  'rudh:lot:atmane:uttama:eka': 'ruRDE',
  'rudh:lot:atmane:uttama:dvi': 'ruRDavahE',
  'rudh:lot:atmane:uttama:bahu': 'ruRDamahE',
  'rudh:lin:atmane:prathama:eka': 'runDIta',
  'rudh:lin:atmane:prathama:dvi': 'runDIyAtAm',
  'rudh:lin:atmane:prathama:bahu': 'runDIran',
  'rudh:lin:atmane:madhyama:eka': 'runDITAH',
  'rudh:lin:atmane:madhyama:dvi': 'runDIyATAm',
  'rudh:lin:atmane:madhyama:bahu': 'runDIDvam',
  'rudh:lin:atmane:uttama:eka': 'runDIya',
  'rudh:lin:atmane:uttama:dvi': 'runDIvahi',
  'rudh:lin:atmane:uttama:bahu': 'runDImahi',
  'rudh:lan:atmane:prathama:eka': 'arundDa',
  'rudh:lan:atmane:prathama:dvi': 'arunDAtAm',
  'rudh:lan:atmane:prathama:bahu': 'arunData',
  'rudh:lan:atmane:madhyama:eka': 'arundDAH',
  'rudh:lan:atmane:madhyama:dvi': 'arunDATAm',
  'rudh:lan:atmane:madhyama:bahu': 'arundDvam',
  'rudh:lan:atmane:uttama:eka': 'arunDi',
  'rudh:lan:atmane:uttama:dvi': 'arunDvahi',
  'rudh:lan:atmane:uttama:bahu': 'arunDmahi',
  'yuj:lat:atmane:prathama:eka': 'yuNkte',
  'yuj:lat:atmane:prathama:dvi': 'yuYjAte',
  'yuj:lat:atmane:prathama:bahu': 'yuYjate',
  'yuj:lat:atmane:madhyama:eka': 'yuNkze',
  'yuj:lat:atmane:madhyama:dvi': 'yuYjATe',
  'yuj:lat:atmane:madhyama:bahu': 'yuNgDve',
  'yuj:lat:atmane:uttama:eka': 'yuYje',
  'yuj:lat:atmane:uttama:dvi': 'yuYjvahe',
  'yuj:lat:atmane:uttama:bahu': 'yuYjmahe',
  'yuj:lot:atmane:prathama:eka': 'yuNktAm',
  'yuj:lot:atmane:prathama:dvi': 'yuYjAtAm',
  'yuj:lot:atmane:prathama:bahu': 'yuYjatAm',
  'yuj:lot:atmane:madhyama:eka': 'yuNkzva',
  'yuj:lot:atmane:madhyama:dvi': 'yuYjATAm',
  'yuj:lot:atmane:madhyama:bahu': 'yuNgDvam',
  'yuj:lot:atmane:uttama:eka': 'yunajE',
  'yuj:lot:atmane:uttama:dvi': 'yunajAvahE',
  'yuj:lot:atmane:uttama:bahu': 'yunajAmahE',
  'yuj:lin:atmane:prathama:eka': 'yuYjIta',
  'yuj:lin:atmane:prathama:dvi': 'yuYjIyAtAm',
  'yuj:lin:atmane:prathama:bahu': 'yuYjIran',
  'yuj:lin:atmane:madhyama:eka': 'yuYjITAH',
  'yuj:lin:atmane:madhyama:dvi': 'yuYjIyATAm',
  'yuj:lin:atmane:madhyama:bahu': 'yuYjIDvam',
  'yuj:lin:atmane:uttama:eka': 'yuYjIya',
  'yuj:lin:atmane:uttama:dvi': 'yuYjIvahi',
  'yuj:lin:atmane:uttama:bahu': 'yuYjImahi',
  'yuj:lan:atmane:prathama:eka': 'ayuNkta',
  'yuj:lan:atmane:prathama:dvi': 'ayuYjAtAm',
  'yuj:lan:atmane:prathama:bahu': 'ayuYjata',
  'yuj:lan:atmane:madhyama:eka': 'ayuNkTAH',
  'yuj:lan:atmane:madhyama:dvi': 'ayuYjATAm',
  'yuj:lan:atmane:madhyama:bahu': 'ayuNgDvam',
  'yuj:lan:atmane:uttama:eka': 'ayuYji',
  'yuj:lan:atmane:uttama:dvi': 'ayuYjvahi',
  'yuj:lan:atmane:uttama:bahu': 'ayuYjmahi',
  // √as middle voice (Wiktionary asti: sté/sā́te/sáte, sé/sā́the/dhvé,
  // hé/sváhe/smáhe; stā́m/sā́tām/sátām; sītá/sīmáhi; ā́sta/ā́smahi).
  'as:lat:atmane:prathama:eka': 'ste',
  'as:lat:atmane:prathama:dvi': 'sAte',
  'as:lat:atmane:prathama:bahu': 'sate',
  'as:lat:atmane:madhyama:eka': 'se',
  'as:lat:atmane:madhyama:dvi': 'sAthe',
  'as:lat:atmane:madhyama:bahu': 'Dve',
  'as:lat:atmane:uttama:eka': 'he',
  'as:lat:atmane:uttama:dvi': 'svahe',
  'as:lat:atmane:uttama:bahu': 'smahe',
  'as:lot:atmane:prathama:eka': 'stAm',
  'as:lot:atmane:prathama:dvi': 'sAtAm',
  'as:lot:atmane:prathama:bahu': 'satAm',
  'as:lot:atmane:madhyama:eka': 'sva',
  'as:lot:atmane:madhyama:dvi': 'sAthAm',
  'as:lot:atmane:madhyama:bahu': 'Dvam',
  'as:lot:atmane:uttama:eka': 'asE',        // ásai
  'as:lot:atmane:uttama:dvi': 'asAvahai',   // ásāvahai
  'as:lot:atmane:uttama:bahu': 'asAmahai',  // ásāmahai
  'as:lin:atmane:prathama:eka': 'sIta',
  'as:lin:atmane:prathama:dvi': 'sIyAtAm',
  'as:lin:atmane:prathama:bahu': 'sIran',
  'as:lin:atmane:madhyama:eka': 'sIthAH',
  'as:lin:atmane:madhyama:dvi': 'sIyAthAm',
  'as:lin:atmane:madhyama:bahu': 'sIdhvam',
  'as:lin:atmane:uttama:eka': 'sIya',
  'as:lin:atmane:uttama:dvi': 'sIvahi',
  'as:lin:atmane:uttama:bahu': 'sImahi',
  'as:lan:atmane:prathama:eka': 'Asta',
  'as:lan:atmane:prathama:dvi': 'AsAtAm',
  'as:lan:atmane:prathama:bahu': 'Asata',
  'as:lan:atmane:madhyama:eka': 'AsTAH',
  'as:lan:atmane:madhyama:dvi': 'AsAthAm',
  'as:lan:atmane:madhyama:bahu': 'Addhvam',
  'as:lan:atmane:uttama:eka': 'Asi',
  'as:lan:atmane:uttama:dvi': 'Asvahi',
  'as:lan:atmane:uttama:bahu': 'Asmahi',
  // √ad middle voice (Wiktionary atti: átte/átse/admáhe, attā́m/ádai/
  // adītá/adīmáhi, átta/átthāḥ/ádmahi).
  'ad:lat:atmane:prathama:eka': 'atte',
  'ad:lat:atmane:prathama:dvi': 'adAte',
  'ad:lat:atmane:madhyama:eka': 'atse',
  'ad:lat:atmane:madhyama:dvi': 'adAthe',
  'ad:lat:atmane:uttama:dvi': 'advahi',
  'ad:lat:atmane:uttama:bahu': 'admahi',
  'ad:lot:atmane:prathama:eka': 'attAm',
  'ad:lot:atmane:prathama:bahu': 'adatAm', // adátām (short a; distinct from 3d adā́tām)
  'ad:lot:atmane:madhyama:eka': 'attsva',
  'ad:lot:atmane:madhyama:dvi': 'adAthAm',
  'ad:lot:atmane:uttama:bahu': 'adAmahai',
  'ad:lin:atmane:prathama:eka': 'adIta',
  'ad:lin:atmane:prathama:dvi': 'adIyAtAm',
  'ad:lin:atmane:prathama:bahu': 'adIran',
  'ad:lin:atmane:madhyama:eka': 'adIthAH',
  'ad:lin:atmane:madhyama:dvi': 'adIyAthAm',
  'ad:lin:atmane:madhyama:bahu': 'adIdhvam',
  'ad:lin:atmane:uttama:eka': 'adIya',
  'ad:lin:atmane:uttama:dvi': 'adIvahi',
  'ad:lin:atmane:uttama:bahu': 'adImahi',
  'ad:lan:atmane:prathama:eka': 'atta',
  'ad:lan:atmane:prathama:dvi': 'adAtAm',
  'ad:lan:atmane:madhyama:eka': 'atthAH',
  'ad:lan:atmane:madhyama:dvi': 'adAthAm',
  'ad:lan:atmane:uttama:eka': 'adi',
  'ad:lan:atmane:uttama:dvi': 'advahi',
  'ad:lan:atmane:uttama:bahu': 'admahi',
  // √vid middle voice (Wiktionary vitti: vitté/vidā́te/vitsé, vittā́m/
  // vidā́tām/vitsvá, vidīyá, ávidātām/ávidāthām) — generic gave *vidate etc.
  'vid:lat:atmane:prathama:eka': 'vitte',
  'vid:lat:atmane:prathama:dvi': 'vidAte',
  'vid:lat:atmane:madhyama:eka': 'vitse',
  'vid:lat:atmane:madhyama:dvi': 'vidAthe',
  'vid:lot:atmane:prathama:eka': 'vittAm',
  'vid:lot:atmane:prathama:dvi': 'vidAtAm',
  'vid:lot:atmane:madhyama:eka': 'vitsva',
  'vid:lot:atmane:madhyama:dvi': 'vidAthAm',
  'vid:lot:atmane:uttama:bahu': 'vidAmahai',
  'vid:lin:atmane:uttama:eka': 'vidIya',
  'vid:lin:atmane:uttama:dvi': 'vidIvahi',
  'vid:lin:atmane:uttama:bahu': 'vidImahi',
  'vid:lan:atmane:prathama:eka': 'avitt',
  'vid:lan:atmane:madhyama:eka': 'avitthAH',
  'vid:lan:atmane:prathama:dvi': 'avidAtAm',
  'vid:lan:atmane:madhyama:dvi': 'avidAthAm',
  // √labh (lab) middle-voice forms from Wiktionary labhate (labhetām/
  // labhethām/labheya, alabhetām/alabhethām) — the generic table gave
  // *labAtAm/*labAvAm/*labe/*alabatAm/*alabAvAm.
  'lab:lot:atmane:prathama:dvi': 'labetAm',
  'lab:lot:atmane:madhyama:dvi': 'labethAm',
  'lab:lin:atmane:uttama:eka': 'labeya',
  'lab:lan:atmane:prathama:dvi': 'alabetAm',
  'lab:lan:atmane:madhyama:dvi': 'alabethAm',
  'lab:lot:atmane:uttama:bahu': 'labAmahai', // labhāmahai (not -mahe)
  // √bhid (class 7) present active — Wiktionary bhinátti table.
  'bhid:lat:parasmai:prathama:eka': 'bhinatti',
  'bhid:lat:parasmai:prathama:dvi': 'bhinttaH',
  'bhid:lat:parasmai:prathama:bahu': 'bhindanti',
  'bhid:lat:parasmai:madhyama:eka': 'bhinatsi',
  'bhid:lat:parasmai:madhyama:dvi': 'bhintthaH',
  'bhid:lat:parasmai:madhyama:bahu': 'bhinttha',
  'bhid:lat:parasmai:uttama:eka': 'bhinadmi',
  'bhid:lat:parasmai:uttama:dvi': 'bhindvaH',
  'bhid:lat:parasmai:uttama:bahu': 'bhindmaH',
  // √bhid imperative / imperfect (Wiktionary bhinátti: bhinddhí, ábhinat).
  'bhid:lot:parasmai:prathama:dvi': 'bhinttAm',
  'bhid:lot:parasmai:prathama:bahu': 'bhindantu',
  'bhid:lot:parasmai:madhyama:eka': 'bhinDDi',
  'bhid:lot:parasmai:madhyama:dvi': 'bhintam',
  'bhid:lot:parasmai:madhyama:bahu': 'bhinta',
  'bhid:lot:parasmai:uttama:eka': 'bhinadAni',
  'bhid:lot:parasmai:uttama:dvi': 'bhinadAva',
  'bhid:lot:parasmai:uttama:bahu': 'bhinadAma',
  'bhid:lan:parasmai:madhyama:eka': 'abhinat',   // 2s ábhinat (same as 3s)
  'bhid:lan:parasmai:prathama:dvi': 'abhinttAm',
  'bhid:lan:parasmai:prathama:bahu': 'abhindan',
  'bhid:lan:parasmai:madhyama:dvi': 'abhinttam',
  'bhid:lan:parasmai:madhyama:bahu': 'abhintta',
  'bhid:lan:parasmai:uttama:eka': 'abhinadam',
  'bhid:lan:parasmai:uttama:dvi': 'abhindva',
  'bhid:lan:parasmai:uttama:bahu': 'abhindma',
  // √chid (Cid) class-7 paradigm — Wiktionary chinátti table.
  'Cid:lat:parasmai:prathama:eka': 'chinatti',
  'Cid:lat:parasmai:prathama:dvi': 'chinttaH',
  'Cid:lat:parasmai:prathama:bahu': 'chindanti',
  'Cid:lat:parasmai:madhyama:eka': 'chinatsi',
  'Cid:lat:parasmai:madhyama:dvi': 'chintthaH',
  'Cid:lat:parasmai:madhyama:bahu': 'chinttha',
  'Cid:lat:parasmai:uttama:eka': 'chinadmi',
  'Cid:lat:parasmai:uttama:dvi': 'chindvaH',
  'Cid:lat:parasmai:uttama:bahu': 'chindmaH',
  'Cid:lan:parasmai:prathama:eka': 'acinat',
  'Cid:lan:parasmai:prathama:dvi': 'acinttAm',
  'Cid:lan:parasmai:prathama:bahu': 'acindan',
  'Cid:lan:parasmai:madhyama:eka': 'acinat',
  'Cid:lan:parasmai:madhyama:dvi': 'acinttam',
  'Cid:lan:parasmai:madhyama:bahu': 'acintta',
  'Cid:lan:parasmai:uttama:eka': 'acinadam',
  'Cid:lan:parasmai:uttama:dvi': 'acindva',
  'Cid:lan:parasmai:uttama:bahu': 'acindma',
  'Cid:lot:parasmai:prathama:eka': 'chinattu',
  'Cid:lot:parasmai:prathama:dvi': 'chinttAm',
  'Cid:lot:parasmai:prathama:bahu': 'chindantu',
  'Cid:lot:parasmai:madhyama:eka': 'chinDDi',
  'Cid:lot:parasmai:madhyama:dvi': 'chinttam',
  'Cid:lot:parasmai:madhyama:bahu': 'chintta',
  'Cid:lot:parasmai:uttama:eka': 'chinadAni',
  'Cid:lot:parasmai:uttama:dvi': 'chinadAva',
  'Cid:lot:parasmai:uttama:bahu': 'chinadAma',
  'Cid:lin:parasmai:prathama:eka': 'chinDyAt',
  'Cid:lin:parasmai:prathama:dvi': 'chinDyAtAm',
  'Cid:lin:parasmai:prathama:bahu': 'chinDyuH',
  'Cid:lin:parasmai:madhyama:eka': 'chinDyAH',
  'Cid:lin:parasmai:madhyama:dvi': 'chinDyAtam',
  'Cid:lin:parasmai:madhyama:bahu': 'chinDyAta',
  'Cid:lin:parasmai:uttama:eka': 'chinDyAm',
  'Cid:lin:parasmai:uttama:dvi': 'chinDyAva',
  'Cid:lin:parasmai:uttama:bahu': 'chinDyAma',
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
  // class-5 middle present (Wiktionary cinóti / śṛṇóti tables): cinuté,
  // cinvā́te, cinváte, cinuṣé, cinvā́the, cinudhvé, cinvé, cinváhe, cinmáhe.
  'ciY:lat:atmane:prathama:eka': 'cinute',
  'ciY:lat:atmane:prathama:dvi': 'cinvAte',  // cinvā́te (Wiktionary cinoti; not *cinvātām)
  'ciY:lat:atmane:prathama:bahu': 'cinvate',
  'ciY:lat:atmane:madhyama:eka': 'cinuze',   // cinuṣé
  'ciY:lat:atmane:madhyama:dvi': 'cinvAthe',
  'ciY:lat:atmane:madhyama:bahu': 'cinudhve',
  'ciY:lat:atmane:uttama:eka': 'cinve',
  'ciY:lat:atmane:uttama:dvi': 'cinvahe',
  'ciY:lat:atmane:uttama:bahu': 'cinmahe',
  'zru:lat:atmane:prathama:eka': 'zRuNute',
  'zru:lat:atmane:prathama:dvi': 'zRuNvAte',
  'zru:lat:atmane:prathama:bahu': 'zRuNvate',
  'zru:lat:atmane:madhyama:eka': 'zRuNuze',
  'zru:lat:atmane:madhyama:dvi': 'zRuNvAthe',
  'zru:lat:atmane:madhyama:bahu': 'zRuNudhve',
  'zru:lat:atmane:uttama:eka': 'zRuNve',
  'zru:lat:atmane:uttama:dvi': 'zRuNvahe',
  'zru:lat:atmane:uttama:bahu': 'zRuNmahe',
  'zuY:lat:atmane:prathama:eka': 'sunute',
  'zuY:lat:atmane:prathama:dvi': 'sunvAte',
  'zuY:lat:atmane:prathama:bahu': 'sunvate',
  'zuY:lat:atmane:madhyama:eka': 'sunuze',
  'zuY:lat:atmane:madhyama:dvi': 'sunvAthe',
  'zuY:lat:atmane:madhyama:bahu': 'sunudhve',
  'zuY:lat:atmane:uttama:eka': 'sunve',
  'zuY:lat:atmane:uttama:dvi': 'sunvahe',
  'zuY:lat:atmane:uttama:bahu': 'sunmahe',
  'SiY:lat:atmane:prathama:eka': 'Sinute',
  'SiY:lat:atmane:prathama:dvi': 'SinvAte',
  'SiY:lat:atmane:prathama:bahu': 'Sinvate',
  'SiY:lat:atmane:madhyama:eka': 'Sinuze',
  'SiY:lat:atmane:madhyama:dvi': 'SinvAthe',
  'SiY:lat:atmane:madhyama:bahu': 'Sinudhve',
  'SiY:lat:atmane:uttama:eka': 'Sinve',
  'SiY:lat:atmane:uttama:dvi': 'Sinvahe',
  'SiY:lat:atmane:uttama:bahu': 'Sinmahe',
  'stfY:lat:atmane:prathama:eka': 'stfRnute',
  'stfY:lat:atmane:prathama:dvi': 'stfRnvAte',
  'stfY:lat:atmane:prathama:bahu': 'stfRnvate',
  'stfY:lat:atmane:madhyama:eka': 'stfRnuze',
  'stfY:lat:atmane:madhyama:dvi': 'stfRnvAthe',
  'stfY:lat:atmane:madhyama:bahu': 'stfRnudhve',
  'stfY:lat:atmane:uttama:eka': 'stfRnve',
  'stfY:lat:atmane:uttama:dvi': 'stfRnvahe',
  'stfY:lat:atmane:uttama:bahu': 'stfRnmahe',
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
  'as:lat:parasmai:prathama:eka': 'asti',
  'as:lat:parasmai:prathama:dvi': 'staH',    // stáḥ (Wiktionary asti)
  'as:lat:parasmai:madhyama:dvi': 'sthaH',   // stháḥ
  'as:lat:parasmai:uttama:dvi': 'svaH',     // sváḥ
  'as:lat:parasmai:madhyama:eka': 'asi',
  'as:lat:parasmai:uttama:eka': 'asmi',
  'as:lat:parasmai:prathama:bahu': 'santi',
  'as:lat:parasmai:madhyama:bahu': 'stha',    // sthá (स्थ)
  'as:lat:parasmai:uttama:bahu': 'smaH',     // smáḥ
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
  'as:lot:parasmai:prathama:dvi': 'astAm',   // astā́m
  'as:lot:parasmai:prathama:bahu': 'santu', // santu
  'as:lot:parasmai:madhyama:eka': 'ehi',
  'as:lot:parasmai:madhyama:dvi': 'astam',   // astám
  'as:lot:parasmai:madhyama:bahu': 'asta',   // astá
  'as:lot:parasmai:uttama:dvi': 'asAva',     // āsāva (no final visarga)
  // √as imperfect weak forms (Wiktionary asti: āsī́ḥ, āstám, āsam, ...)
  'as:lan:parasmai:madhyama:eka': 'AsIH',
  'as:lan:parasmai:madhyama:dvi': 'Astam',
  'as:lan:parasmai:madhyama:bahu': 'Asta',
  'as:lan:parasmai:uttama:eka': 'Asam',
  'as:lan:parasmai:uttama:dvi': 'Asva',
  'as:lan:parasmai:uttama:bahu': 'Asma',
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
  'dA:lin:parasmai:uttama:dvi': 'dadyAva', 'dA:lin:parasmai:uttama:bahu': 'dadyAma',
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
  // √dviṣ (2P) athematic paradigms, source: bhagavadgita.org.in conjugation engine.
  // Strong dveṣ-/dvekṣ- in the active singular; weak dviṣ- elsewhere.
  'dviS:lat:parasmai:prathama:eka': 'dvezTi',
  'dviS:lat:parasmai:prathama:dvi': 'dviSTA',
  'dviS:lat:parasmai:prathama:bahu': 'dviSanti',
  'dviS:lat:parasmai:madhyama:eka': 'dvezXi',
  'dviS:lat:parasmai:madhyama:dvi': 'dviSTHA',
  'dviS:lat:parasmai:madhyama:bahu': 'dviSTHa',
  'dviS:lat:parasmai:uttama:eka': 'dvezmi',
  'dviS:lat:parasmai:uttama:dvi': 'dviSvaH',
  'dviS:lat:parasmai:uttama:bahu': 'dviSmaH',
  'dviS:lat:atmane:prathama:eka': 'dviSTe',
  'dviS:lat:atmane:prathama:dvi': 'dviSAte',
  'dviS:lat:atmane:prathama:bahu': 'dviSate',
  'dviS:lat:atmane:madhyama:eka': 'dvikze',
  'dviS:lat:atmane:madhyama:dvi': 'dviSAthe',
  'dviS:lat:atmane:madhyama:bahu': 'dviDDve',
  'dviS:lat:atmane:uttama:eka': 'dviSe',
  'dviS:lat:atmane:uttama:dvi': 'dviSvahe',
  'dviS:lat:atmane:uttama:bahu': 'dviSmahe',
  'dviS:lan:parasmai:prathama:eka': 'advET',
  'dviS:lan:parasmai:prathama:dvi': 'adviSTAm',
  'dviS:lan:parasmai:prathama:bahu': 'adviSan',
  'dviS:lan:parasmai:madhyama:eka': 'advET',
  'dviS:lan:parasmai:madhyama:dvi': 'adviSTam',
  'dviS:lan:parasmai:madhyama:bahu': 'adviSTa',
  'dviS:lan:parasmai:uttama:eka': 'advezam',
  'dviS:lan:parasmai:uttama:dvi': 'adviSva',
  'dviS:lan:parasmai:uttama:bahu': 'adviSma',
  'dviS:lan:atmane:prathama:eka': 'adviSTa',
  'dviS:lan:atmane:prathama:dvi': 'adviSAtAm',
  'dviS:lan:atmane:prathama:bahu': 'adviSata',
  'dviS:lan:atmane:madhyama:eka': 'adviSTHAH',
  'dviS:lan:atmane:madhyama:dvi': 'adviSATHAm',
  'dviS:lan:atmane:madhyama:bahu': 'adviDDvam',
  'dviS:lan:atmane:uttama:eka': 'adviSi',
  'dviS:lan:atmane:uttama:dvi': 'adviSvahi',
  'dviS:lan:atmane:uttama:bahu': 'adviSmahi',
  'dviS:lot:parasmai:prathama:eka': 'dvezTu',
  'dviS:lot:parasmai:prathama:dvi': 'dviSTAm',
  'dviS:lot:parasmai:prathama:bahu': 'dviSantu',
  'dviS:lot:parasmai:madhyama:eka': 'dviDDi',
  'dviS:lot:parasmai:madhyama:dvi': 'dviSTam',
  'dviS:lot:parasmai:madhyama:bahu': 'dviSTa',
  'dviS:lot:parasmai:uttama:eka': 'dvezANi',
  'dviS:lot:parasmai:uttama:dvi': 'dvezAva',
  'dviS:lot:parasmai:uttama:bahu': 'dvezAma',
  'dviS:lot:atmane:prathama:eka': 'dviSTAm',
  'dviS:lot:atmane:prathama:dvi': 'dviSAtAm',
  'dviS:lot:atmane:prathama:bahu': 'dviSatAm',
  'dviS:lot:atmane:madhyama:eka': 'dvikSva',
  'dviS:lot:atmane:madhyama:dvi': 'dviSAthAm',
  'dviS:lot:atmane:madhyama:bahu': 'dviDDvam',
  'dviS:lot:atmane:uttama:eka': 'dviSE',
  'dviS:lot:atmane:uttama:dvi': 'dviSAvahai',
  'dviS:lot:atmane:uttama:bahu': 'dviSAmAhai',
  'dviS:lin:parasmai:prathama:eka': 'dviSyAt',
  'dviS:lin:parasmai:prathama:dvi': 'dviSyAtAm',
  'dviS:lin:parasmai:prathama:bahu': 'dviSyuH',
  'dviS:lin:parasmai:madhyama:eka': 'dviSyAH',
  'dviS:lin:parasmai:madhyama:dvi': 'dviSyAtam',
  'dviS:lin:parasmai:madhyama:bahu': 'dviSyAta',
  'dviS:lin:parasmai:uttama:eka': 'dviSyAm',
  'dviS:lin:parasmai:uttama:dvi': 'dviSyAva',
  'dviS:lin:parasmai:uttama:bahu': 'dviSyAma',
  'dviS:lin:atmane:prathama:eka': 'dviSIta',
  'dviS:lin:atmane:prathama:dvi': 'dviSIyAtAm',
  'dviS:lin:atmane:prathama:bahu': 'dviSIran',
  'dviS:lin:atmane:madhyama:eka': 'dviSIthAH',
  'dviS:lin:atmane:madhyama:dvi': 'dviSIyAthAm',
  'dviS:lin:atmane:madhyama:bahu': 'dviSIdhvam',
  'dviS:lin:atmane:uttama:eka': 'dviSIya',
  'dviS:lin:atmane:uttama:dvi': 'dviSIvahi',
  'dviS:lin:atmane:uttama:bahu': 'dviSImahi',
  'dviS:lrt:parasmai:prathama:eka': 'dvekzyati',
  'dviS:lrt:parasmai:prathama:dvi': 'dvekzyataH',
  'dviS:lrt:parasmai:prathama:bahu': 'dvekzyanti',
  'dviS:lrt:parasmai:madhyama:eka': 'dvekzyasi',
  'dviS:lrt:parasmai:madhyama:dvi': 'dvekzyathaH',
  'dviS:lrt:parasmai:madhyama:bahu': 'dvekzyatha',
  'dviS:lrt:parasmai:uttama:eka': 'dvekzyAmi',
  'dviS:lrt:parasmai:uttama:dvi': 'dvekzyAvaH',
  'dviS:lrt:parasmai:uttama:bahu': 'dvekzyAmaH',
  'dviS:lrt:atmane:prathama:eka': 'dvekzyate',
  'dviS:lrt:atmane:prathama:dvi': 'dvekzyete',
  'dviS:lrt:atmane:prathama:bahu': 'dvekzyante',
  'dviS:lrt:atmane:madhyama:eka': 'dvekzyase',
  'dviS:lrt:atmane:madhyama:dvi': 'dvekzyethe',
  'dviS:lrt:atmane:madhyama:bahu': 'dvekzyaDve',
  'dviS:lrt:atmane:uttama:eka': 'dvekzye',
  'dviS:lrt:atmane:uttama:dvi': 'dvekzyAvahe',
  'dviS:lrt:atmane:uttama:bahu': 'dvekzyAmahe',
  // √grah (9P, krīādi): gṛhṇā- present stem (ṇ = R), grāhīṣya- future.
  // Source: bhagavadgita.org.in conjugation engine.
  'grah:lat:parasmai:prathama:eka': 'gfhRAti',
  'grah:lat:parasmai:prathama:dvi': 'gfhRItaH',
  'grah:lat:parasmai:prathama:bahu': 'gfhRanti',
  'grah:lat:parasmai:madhyama:eka': 'gfhRAsi',
  'grah:lat:parasmai:madhyama:dvi': 'gfhRIthaH',
  'grah:lat:parasmai:madhyama:bahu': 'gfhRItha',
  'grah:lat:parasmai:uttama:eka': 'gfhRAmi',
  'grah:lat:parasmai:uttama:dvi': 'gfhRIvaH',
  'grah:lat:parasmai:uttama:bahu': 'gfhRImaH',
  'grah:lat:atmane:prathama:eka': 'gfhRIte',
  'grah:lat:atmane:prathama:dvi': 'gfhRAte',
  'grah:lat:atmane:prathama:bahu': 'gfhRate',
  'grah:lat:atmane:madhyama:eka': 'gfhRIze',
  'grah:lat:atmane:madhyama:dvi': 'gfhRAthe',
  'grah:lat:atmane:madhyama:bahu': 'gfhRIdhve',
  'grah:lat:atmane:uttama:eka': 'gfhRe',
  'grah:lat:atmane:uttama:dvi': 'gfhRIvahe',
  'grah:lat:atmane:uttama:bahu': 'gfhRImahe',
  'grah:lan:parasmai:prathama:eka': 'agfhRAt',
  'grah:lan:parasmai:prathama:dvi': 'agfhRItAm',
  'grah:lan:parasmai:prathama:bahu': 'agfhRan',
  'grah:lan:parasmai:madhyama:eka': 'agfhRAH',
  'grah:lan:parasmai:madhyama:dvi': 'agfhRItam',
  'grah:lan:parasmai:madhyama:bahu': 'agfhRIta',
  'grah:lan:parasmai:uttama:eka': 'agfhRAm',
  'grah:lan:parasmai:uttama:dvi': 'agfhRIva',
  'grah:lan:parasmai:uttama:bahu': 'agfhRIma',
  'grah:lot:parasmai:prathama:eka': 'gfhRAtu',
  'grah:lot:parasmai:prathama:dvi': 'gfhRItAm',
  'grah:lot:parasmai:prathama:bahu': 'gfhRantu',
  'grah:lot:parasmai:madhyama:eka': 'gfhARa',  // gṛhāṇá (Wiktionary; R=ण, not N=ङ)
  'grah:lot:parasmai:madhyama:dvi': 'gfhRItam',
  'grah:lot:parasmai:madhyama:bahu': 'gfhRIta',
  'grah:lot:parasmai:uttama:eka': 'gfhRAni',
  'grah:lot:parasmai:uttama:dvi': 'gfhRAva',
  'grah:lot:parasmai:uttama:bahu': 'gfhRAma',
  'grah:lin:parasmai:prathama:eka': 'gfhRIyAt',
  'grah:lin:parasmai:prathama:dvi': 'gfhRIyAtAm',
  'grah:lin:parasmai:prathama:bahu': 'gfhRIyuH',
  'grah:lin:parasmai:madhyama:eka': 'gfhRIyAH',
  'grah:lin:parasmai:madhyama:dvi': 'gfhRIyAtam',
  'grah:lin:parasmai:madhyama:bahu': 'gfhRIyAta',
  'grah:lin:parasmai:uttama:eka': 'gfhRIyAm',
  'grah:lin:parasmai:uttama:dvi': 'gfhRIyAva',
  'grah:lin:parasmai:uttama:bahu': 'gfhRIyAma',
  'grah:lrt:parasmai:prathama:eka': 'grAhIzyati',
  'grah:lrt:parasmai:prathama:dvi': 'grAhIzataH',
  'grah:lrt:parasmai:prathama:bahu': 'grAhIzyanti',
  'grah:lrt:parasmai:madhyama:eka': 'grAhIzasi',
  'grah:lrt:parasmai:madhyama:dvi': 'grAhIzathaH',
  'grah:lrt:parasmai:madhyama:bahu': 'grAhIzatha',
  'grah:lrt:parasmai:uttama:eka': 'grAhIzAmi',
  'grah:lrt:parasmai:uttama:dvi': 'grAhIzAvaH',
  'grah:lrt:parasmai:uttama:bahu': 'grAhIzAmaH',
  // √jñā (9P): jānā- present stem (not *jñānā-); gerund jñātvā.
  // Source: bhagavadgita.org.in conjugation engine.
  'jFnA:lat:parasmai:prathama:eka': 'jAnAti',
  'jFnA:lat:parasmai:prathama:dvi': 'jAnItaH',
  'jFnA:lat:parasmai:prathama:bahu': 'jAnanti',
  'jFnA:lat:parasmai:madhyama:eka': 'jAnAsi',
  'jFnA:lat:parasmai:madhyama:dvi': 'jAnIthaH',
  'jFnA:lat:parasmai:madhyama:bahu': 'jAnItha',
  'jFnA:lat:parasmai:uttama:eka': 'jAnAmi',
  'jFnA:lat:parasmai:uttama:dvi': 'jAnIvaH',
  'jFnA:lat:parasmai:uttama:bahu': 'jAnImaH',
  'jFnA:lan:parasmai:prathama:eka': 'ajAnAt',
  'jFnA:lan:parasmai:prathama:dvi': 'ajAnItAm',
  'jFnA:lan:parasmai:prathama:bahu': 'ajAnan',
  'jFnA:lan:parasmai:madhyama:eka': 'ajAnAH',
  'jFnA:lan:parasmai:madhyama:dvi': 'ajAnItam',
  'jFnA:lan:parasmai:madhyama:bahu': 'ajAnIta',
  'jFnA:lan:parasmai:uttama:eka': 'ajAnAm',
  'jFnA:lan:parasmai:uttama:dvi': 'ajAnIva',
  'jFnA:lan:parasmai:uttama:bahu': 'ajAnIma',
  'jFnA:lot:parasmai:prathama:eka': 'jAnAtu',
  'jFnA:lot:parasmai:prathama:dvi': 'jAnItAm',
  'jFnA:lot:parasmai:prathama:bahu': 'jAnantu',
  'jFnA:lot:parasmai:madhyama:eka': 'jAnIhi',
  'jFnA:lot:parasmai:madhyama:dvi': 'jAnItam',
  'jFnA:lot:parasmai:madhyama:bahu': 'jAnIta',
  'jFnA:lot:parasmai:uttama:eka': 'jAnAni',
  'jFnA:lot:parasmai:uttama:dvi': 'jAnAva',
  'jFnA:lot:parasmai:uttama:bahu': 'jAnAma',
  'jFnA:lin:parasmai:prathama:eka': 'jAnIyAt',
  'jFnA:lin:parasmai:prathama:dvi': 'jAnIyAtAm',
  'jFnA:lin:parasmai:prathama:bahu': 'jAnIyuH',
  'jFnA:lin:parasmai:madhyama:eka': 'jAnIyAH',
  'jFnA:lin:parasmai:madhyama:dvi': 'jAnIyAtam',
  'jFnA:lin:parasmai:madhyama:bahu': 'jAnIyAta',
  'jFnA:lin:parasmai:uttama:eka': 'jAnIyAm',
  'jFnA:lin:parasmai:uttama:dvi': 'jAnIyAva',
  'jFnA:lin:parasmai:uttama:bahu': 'jAnIyAma',
  // √vid (2P, “to know”): vetti/vidanti, not *vidati — perfect veda has present sense.
  // Source: bhagavadgita.org.in conjugation engine.
  'vid:lat:parasmai:prathama:eka': 'vetti',
  'vid:lat:parasmai:prathama:dvi': 'vittaH',
  'vid:lat:parasmai:prathama:bahu': 'vidanti',
  'vid:lat:parasmai:madhyama:eka': 'vetsi',
  'vid:lat:parasmai:madhyama:dvi': 'vitthaH',
  'vid:lat:parasmai:madhyama:bahu': 'vittha',
  'vid:lat:parasmai:uttama:eka': 'vedmi',
  'vid:lat:parasmai:uttama:dvi': 'vidvaH',
  'vid:lat:parasmai:uttama:bahu': 'vidmaH',
  'vid:lan:parasmai:prathama:eka': 'avet',
  'vid:lan:parasmai:prathama:dvi': 'avittAm',
  'vid:lan:parasmai:prathama:bahu': 'avidan',
  'vid:lan:parasmai:madhyama:eka': 'avet',
  'vid:lan:parasmai:madhyama:dvi': 'avittam',
  'vid:lan:parasmai:madhyama:bahu': 'avitta',
  'vid:lan:parasmai:uttama:eka': 'avedam',
  'vid:lan:parasmai:uttama:dvi': 'avidva',
  'vid:lan:parasmai:uttama:bahu': 'avidma',
  'vid:lin:parasmai:prathama:eka': 'vidyAt',
  'vid:lin:parasmai:prathama:dvi': 'vidyAtAm',
  'vid:lin:parasmai:prathama:bahu': 'vidyuH',
  'vid:lin:parasmai:madhyama:eka': 'vidyAH',
  'vid:lin:parasmai:madhyama:dvi': 'vidyAtam',
  'vid:lin:parasmai:madhyama:bahu': 'vidyAta',
  'vid:lin:parasmai:uttama:eka': 'vidyAm',
  'vid:lin:parasmai:uttama:dvi': 'vidyAva',
  'vid:lin:parasmai:uttama:bahu': 'vidyAma',
  'vid:lot:parasmai:prathama:eka': 'vettu',
  'vid:lot:parasmai:prathama:dvi': 'vittAm',
  'vid:lot:parasmai:prathama:bahu': 'vidantu',
  'vid:lot:parasmai:madhyama:eka': 'viddhi',
  'vid:lot:parasmai:madhyama:dvi': 'vittam',
  'vid:lot:parasmai:madhyama:bahu': 'vitta',
  'vid:lot:parasmai:uttama:eka': 'vedAni',
  'vid:lot:parasmai:uttama:dvi': 'vedAva',
  'vid:lot:parasmai:uttama:bahu': 'vedAma',
  'vid:lrt:parasmai:prathama:eka': 'vedizyati',
  'vid:lrt:parasmai:prathama:dvi': 'vedizataH',
  'vid:lrt:parasmai:prathama:bahu': 'vedizanti',
  'vid:lrt:parasmai:madhyama:eka': 'vedizasi',
  'vid:lrt:parasmai:madhyama:dvi': 'vedizathaH',
  'vid:lrt:parasmai:madhyama:bahu': 'vedizatha',
  'vid:lrt:parasmai:uttama:eka': 'vedizAmi',
  'vid:lrt:parasmai:uttama:dvi': 'vedizAvaH',
  'vid:lrt:parasmai:uttama:bahu': 'vedizAmaH',
  'vid:lut:parasmai:prathama:eka': 'veditA',
  'vid:lut:parasmai:prathama:dvi': 'veditArau',
  'vid:lut:parasmai:prathama:bahu': 'veditAraH',
  'vid:lut:parasmai:madhyama:eka': 'veditAsi',
  'vid:lut:parasmai:madhyama:dvi': 'veditAsTHaH',
  'vid:lut:parasmai:madhyama:bahu': 'veditAsTHa',
  'vid:lut:parasmai:uttama:eka': 'veditAsmi',
  'vid:lut:parasmai:uttama:dvi': 'veditAsvaH',
  'vid:lut:parasmai:uttama:bahu': 'veditAsmaH',
  'vid:lit:parasmai:prathama:eka': 'veda',
  'vid:lit:parasmai:prathama:dvi': 'vittaH',
  'vid:lit:parasmai:prathama:bahu': 'viduH',
  'vid:lit:parasmai:madhyama:eka': 'vettha',
  'vid:lit:parasmai:madhyama:dvi': 'vitthuH',
  'vid:lit:parasmai:madhyama:bahu': 'vid',
  'vid:lit:parasmai:uttama:eka': 'veda',
  'vid:lit:parasmai:uttama:dvi': 'vidva',
  'vid:lit:parasmai:uttama:bahu': 'vidma',
  // √iṣ (2P): eṣṭi/iṣanti (not *iṣati), imperfect aiṭ, future eṣiṣyati.
  // Source: bhagavadgita.org.in conjugation engine.
  'iS:lat:parasmai:prathama:eka': 'ezTi',
  'iS:lat:parasmai:prathama:dvi': 'izTaH',
  'iS:lat:parasmai:prathama:bahu': 'iSanti',
  'iS:lat:parasmai:madhyama:eka': 'ekzi',
  'iS:lat:parasmai:madhyama:dvi': 'izTHaH',
  'iS:lat:parasmai:madhyama:bahu': 'izTHa',
  'iS:lat:parasmai:uttama:eka': 'ezmi',
  'iS:lat:parasmai:uttama:dvi': 'iSvaH',
  'iS:lat:parasmai:uttama:bahu': 'iSmaH',
  'iS:lat:atmane:prathama:eka': 'izTe',
  'iS:lat:atmane:prathama:dvi': 'iSAte',
  'iS:lat:atmane:prathama:bahu': 'iSate',
  'iS:lat:atmane:madhyama:eka': 'ikze',
  'iS:lat:atmane:madhyama:dvi': 'iSAthe',
  'iS:lat:atmane:madhyama:bahu': 'iDDve',
  'iS:lat:atmane:uttama:eka': 'iSe',
  'iS:lat:atmane:uttama:dvi': 'iSvahe',
  'iS:lat:atmane:uttama:bahu': 'iSmahe',
  'iS:lan:parasmai:prathama:eka': 'ET',
  'iS:lan:parasmai:prathama:dvi': 'EzTAm',
  'iS:lan:parasmai:prathama:bahu': 'Ezan',
  'iS:lan:parasmai:madhyama:eka': 'ET',
  'iS:lan:parasmai:madhyama:dvi': 'EzTam',
  'iS:lan:parasmai:madhyama:bahu': 'EzTa',
  'iS:lan:parasmai:uttama:eka': 'Ezam',
  'iS:lan:parasmai:uttama:dvi': 'Ezva',
  'iS:lan:parasmai:uttama:bahu': 'Ezma',
  'iS:lot:parasmai:prathama:eka': 'ezTu',
  'iS:lot:parasmai:prathama:dvi': 'izTAm',
  'iS:lot:parasmai:prathama:bahu': 'iSantu',
  'iS:lot:parasmai:madhyama:eka': 'iDDi',
  'iS:lot:parasmai:madhyama:dvi': 'izTam',
  'iS:lot:parasmai:madhyama:bahu': 'izTa',
  'iS:lot:parasmai:uttama:eka': 'ezANi',
  'iS:lot:parasmai:uttama:dvi': 'ezAva',
  'iS:lot:parasmai:uttama:bahu': 'ezAma',
  'iS:lin:parasmai:prathama:eka': 'iSyAt',
  'iS:lin:parasmai:prathama:dvi': 'iSyAtAm',
  'iS:lin:parasmai:prathama:bahu': 'iSyuH',
  'iS:lin:parasmai:madhyama:eka': 'iSyAH',
  'iS:lin:parasmai:madhyama:dvi': 'iSyAtam',
  'iS:lin:parasmai:madhyama:bahu': 'iSyAta',
  'iS:lin:parasmai:uttama:eka': 'iSyAm',
  'iS:lin:parasmai:uttama:dvi': 'iSyAva',
  'iS:lin:parasmai:uttama:bahu': 'iSyAma',
  'iS:lrt:parasmai:prathama:eka': 'eziSyati',
  'iS:lrt:parasmai:prathama:dvi': 'eziSataH',
  'iS:lrt:parasmai:prathama:bahu': 'eziSanti',
  'iS:lrt:parasmai:madhyama:eka': 'eziSasi',
  'iS:lrt:parasmai:madhyama:dvi': 'eziSathaH',
  'iS:lrt:parasmai:madhyama:bahu': 'eziSatha',
  'iS:lrt:parasmai:uttama:eka': 'eziSyAmi',
  'iS:lrt:parasmai:uttama:dvi': 'eziSyAvaH',
  'iS:lrt:parasmai:uttama:bahu': 'eziSyAmaH',
  'iS:lit:parasmai:prathama:eka': 'iyeza',
  'iS:lit:parasmai:prathama:dvi': 'ISatuH',
  'iS:lit:parasmai:prathama:bahu': 'ISuH',
  'iS:lit:parasmai:madhyama:eka': 'iyeziTa',
  'iS:lit:parasmai:madhyama:dvi': 'ISathuH',
  'iS:lit:parasmai:madhyama:bahu': 'ISa',
  'iS:lit:parasmai:uttama:eka': 'iyeza',
  'iS:lit:parasmai:uttama:dvi': 'ISiva',
  'iS:lit:parasmai:uttama:bahu': 'ISima',
  // √mṛj (2P): mārṣṭi/mṛjanti (not *mṛjati) — guṇa in strong singular.
  // Source: bhagavadgita.org.in conjugation engine.
  'mfz:lat:parasmai:prathama:eka': 'mArzTi',
  'mfz:lat:parasmai:prathama:dvi': 'mfzTaH',
  'mfz:lat:parasmai:prathama:bahu': 'mfjanti',
  'mfz:lat:parasmai:madhyama:eka': 'mArkzi',
  'mfz:lat:parasmai:madhyama:dvi': 'mfzTHaH',
  'mfz:lat:parasmai:madhyama:bahu': 'mfzTHa',
  'mfz:lat:parasmai:uttama:eka': 'mArjmi',
  'mfz:lat:parasmai:uttama:dvi': 'mfjvaH',
  'mfz:lat:parasmai:uttama:bahu': 'mfjmaH',
  'mfz:lan:parasmai:prathama:eka': 'amArT',
  'mfz:lan:parasmai:prathama:dvi': 'amfzTAm',
  'mfz:lan:parasmai:prathama:bahu': 'amfjan',
  'mfz:lan:parasmai:madhyama:eka': 'amArT',
  'mfz:lan:parasmai:madhyama:dvi': 'amfzTam',
  'mfz:lan:parasmai:madhyama:bahu': 'amfzTa',
  'mfz:lan:parasmai:uttama:eka': 'amArjam',
  'mfz:lan:parasmai:uttama:dvi': 'amfjva',
  'mfz:lan:parasmai:uttama:bahu': 'amfjma',
  'mfz:lin:parasmai:prathama:eka': 'mfjyAt',
  'mfz:lin:parasmai:prathama:dvi': 'mfjyAtAm',
  'mfz:lin:parasmai:prathama:bahu': 'mfjyuH',
  'mfz:lin:parasmai:madhyama:eka': 'mfjyAH',
  'mfz:lin:parasmai:madhyama:dvi': 'mfjyAtam',
  'mfz:lin:parasmai:madhyama:bahu': 'mfjyAta',
  'mfz:lin:parasmai:uttama:eka': 'mfjyAm',
  'mfz:lin:parasmai:uttama:dvi': 'mfjyAva',
  'mfz:lin:parasmai:uttama:bahu': 'mfjyAma',
  'mfz:lot:parasmai:prathama:eka': 'mArzTu',
  'mfz:lot:parasmai:prathama:dvi': 'mfzTAm',
  'mfz:lot:parasmai:prathama:bahu': 'mfjantu',
  'mfz:lot:parasmai:madhyama:eka': 'mDDhi',
  'mfz:lot:parasmai:madhyama:dvi': 'mfzTam',
  'mfz:lot:parasmai:madhyama:bahu': 'mfzTa',
  'mfz:lot:parasmai:uttama:eka': 'mArjAni',
  'mfz:lot:parasmai:uttama:dvi': 'mArjava',
  'mfz:lot:parasmai:uttama:bahu': 'mArjAma',
  'mfz:lrt:parasmai:prathama:eka': 'mArjizyati',
  'mfz:lrt:parasmai:prathama:dvi': 'mArjizataH',
  'mfz:lrt:parasmai:prathama:bahu': 'mArjizanti',
  'mfz:lrt:parasmai:madhyama:eka': 'mArjizasi',
  'mfz:lrt:parasmai:madhyama:dvi': 'mArjizathaH',
  'mfz:lrt:parasmai:madhyama:bahu': 'mArjizatha',
  'mfz:lrt:parasmai:uttama:eka': 'mArjizAmi',
  'mfz:lrt:parasmai:uttama:dvi': 'mArjizAvaH',
  'mfz:lrt:parasmai:uttama:bahu': 'mArjizAmaH',
  'mfz:lit:parasmai:prathama:eka': 'mamArja',
  'mfz:lit:parasmai:prathama:dvi': 'mamfzatuH',
  'mfz:lit:parasmai:prathama:bahu': 'mamfzuH',
  'mfz:lit:parasmai:madhyama:eka': 'mamArjitha',
  'mfz:lit:parasmai:madhyama:dvi': 'mamfzathuH',
  'mfz:lit:parasmai:madhyama:bahu': 'mamfz',
  // √pā / √sthā: present stems pib- / tiṣṭh- (pibati/tiṣṭhati), not *pāti/*sthāti.
  // Source: bhagavadgita.org.in conjugation engine.
  'pA:lat:parasmai:prathama:eka': 'pibati',
  'pA:lat:parasmai:prathama:dvi': 'pibataH',
  'pA:lat:parasmai:prathama:bahu': 'pibanti',
  'pA:lat:parasmai:madhyama:eka': 'pibasi',
  'pA:lat:parasmai:madhyama:dvi': 'pibathaH',
  'pA:lat:parasmai:madhyama:bahu': 'pibatha',
  'pA:lat:parasmai:uttama:eka': 'pibAmi',
  'pA:lat:parasmai:uttama:dvi': 'pibAvaH',
  'pA:lat:parasmai:uttama:bahu': 'pibAmaH',
  'pA:lan:parasmai:prathama:eka': 'apibat',
  'pA:lan:parasmai:prathama:dvi': 'apibatAm',
  'pA:lan:parasmai:prathama:bahu': 'apiban',
  'pA:lan:parasmai:madhyama:eka': 'apibaH',
  'pA:lan:parasmai:madhyama:dvi': 'apibatam',
  'pA:lan:parasmai:madhyama:bahu': 'apibata',
  'pA:lan:parasmai:uttama:eka': 'apibAm',
  'pA:lan:parasmai:uttama:dvi': 'apibAvaH',
  'pA:lan:parasmai:uttama:bahu': 'apibAmaH',
  'pA:lot:parasmai:prathama:eka': 'pibatu',
  'pA:lot:parasmai:prathama:dvi': 'pibatAm',
  'pA:lot:parasmai:prathama:bahu': 'pibantu',
  'pA:lot:parasmai:madhyama:eka': 'piba',
  'pA:lot:parasmai:madhyama:dvi': 'pibatam',
  'pA:lot:parasmai:madhyama:bahu': 'pibata',
  'pA:lot:parasmai:uttama:eka': 'pibAni',
  'pA:lot:parasmai:uttama:dvi': 'pibAvaH',
  'pA:lot:parasmai:uttama:bahu': 'pibAmaH',
  'pA:lin:parasmai:prathama:eka': 'pibet',
  'pA:lin:parasmai:prathama:dvi': 'pibetAm',
  'pA:lin:parasmai:prathama:bahu': 'pibeyuH',
  'pA:lin:parasmai:madhyama:eka': 'pibeH',
  'pA:lin:parasmai:madhyama:dvi': 'pibetam',
  'pA:lin:parasmai:madhyama:bahu': 'pibeta',
  'pA:lin:parasmai:uttama:eka': 'pibeyam',
  'pA:lin:parasmai:uttama:dvi': 'pibevaH',
  'pA:lin:parasmai:uttama:bahu': 'pibema',
  'sTA:lat:parasmai:prathama:eka': 'tiSThati',
  'sTA:lat:parasmai:prathama:dvi': 'tiSThataH',
  'sTA:lat:parasmai:prathama:bahu': 'tiSThanti',
  'sTA:lat:parasmai:madhyama:eka': 'tiSThasi',
  'sTA:lat:parasmai:madhyama:dvi': 'tiSThathaH',
  'sTA:lat:parasmai:madhyama:bahu': 'tiSThatha',
  'sTA:lat:parasmai:uttama:eka': 'tiSThAmi',
  'sTA:lat:parasmai:uttama:dvi': 'tiSThAvaH',
  'sTA:lat:parasmai:uttama:bahu': 'tiSThAmaH',
  'sTA:lan:parasmai:prathama:eka': 'atiSThat',
  'sTA:lan:parasmai:prathama:dvi': 'atiSThatAm',
  'sTA:lan:parasmai:prathama:bahu': 'atiSThan',
  'sTA:lan:parasmai:madhyama:eka': 'atiSThaH',
  'sTA:lan:parasmai:madhyama:dvi': 'atiSThatam',
  'sTA:lan:parasmai:madhyama:bahu': 'atiSThata',
  'sTA:lan:parasmai:uttama:eka': 'atiSThAm',
  'sTA:lan:parasmai:uttama:dvi': 'atiSThAvaH',
  'sTA:lan:parasmai:uttama:bahu': 'atiSThAmaH',
  'sTA:lot:parasmai:prathama:eka': 'tiSThatu',
  'sTA:lot:parasmai:prathama:dvi': 'tiSThatAm',
  'sTA:lot:parasmai:prathama:bahu': 'tiSThantu',
  'sTA:lot:parasmai:madhyama:eka': 'tiSTha',
  'sTA:lot:parasmai:madhyama:dvi': 'tiSThatam',
  'sTA:lot:parasmai:madhyama:bahu': 'tiSThata',
  'sTA:lot:parasmai:uttama:eka': 'tiSThAni',
  'sTA:lot:parasmai:uttama:dvi': 'tiSThAvaH',
  'sTA:lot:parasmai:uttama:bahu': 'tiSThAmaH',
  'sTA:lin:parasmai:prathama:eka': 'tiSThet',
  'sTA:lin:parasmai:prathama:dvi': 'tiSThetAm',
  'sTA:lin:parasmai:prathama:bahu': 'tiSTheyuH',
  'sTA:lin:parasmai:madhyama:eka': 'tiSTheH',
  'sTA:lin:parasmai:madhyama:dvi': 'tiSThetam',
  'sTA:lin:parasmai:madhyama:bahu': 'tiSTheta',
  'sTA:lin:parasmai:uttama:eka': 'tiSTheyam',
  'sTA:lin:parasmai:uttama:dvi': 'tiSThevaH',
  'sTA:lin:parasmai:uttama:bahu': 'tiSThema',
  // √ṛ (1P): ṛcch- present stem (fcCati = ṛcchati), not *ṛati.
  // Source: bhagavadgita.org.in conjugation engine.
  'fR:lat:parasmai:prathama:eka': 'fcCati',
  'fR:lat:parasmai:prathama:dvi': 'fcCataH',
  'fR:lat:parasmai:prathama:bahu': 'fcCanti',
  'fR:lat:parasmai:madhyama:eka': 'fcCasi',
  'fR:lat:parasmai:madhyama:dvi': 'fcCathaH',
  'fR:lat:parasmai:madhyama:bahu': 'fcCatha',
  'fR:lat:parasmai:uttama:eka': 'fcCAmi',
  'fR:lat:parasmai:uttama:dvi': 'fcCAvaH',
  'fR:lat:parasmai:uttama:bahu': 'fcCAmaH',
  'fR:lan:parasmai:prathama:eka': 'AfcCat',
  'fR:lan:parasmai:prathama:dvi': 'AfcCatAm',
  'fR:lan:parasmai:prathama:bahu': 'AfcCan',
  'fR:lan:parasmai:madhyama:eka': 'AfcCaH',
  'fR:lan:parasmai:madhyama:dvi': 'AfcCatam',
  'fR:lan:parasmai:madhyama:bahu': 'AfcCata',
  'fR:lan:parasmai:uttama:eka': 'AfcCam',
  'fR:lan:parasmai:uttama:dvi': 'AfcCAvaH',
  'fR:lan:parasmai:uttama:bahu': 'AfcCAmaH',
  'fR:lot:parasmai:prathama:eka': 'fcCatu',
  'fR:lot:parasmai:prathama:dvi': 'fcCatAm',
  'fR:lot:parasmai:prathama:bahu': 'fcCantu',
  'fR:lot:parasmai:madhyama:eka': 'fcCa',
  'fR:lot:parasmai:madhyama:dvi': 'fcCatam',
  'fR:lot:parasmai:madhyama:bahu': 'fcCata',
  'fR:lot:parasmai:uttama:eka': 'fcCAni',
  'fR:lot:parasmai:uttama:dvi': 'fcCAvaH',
  'fR:lot:parasmai:uttama:bahu': 'fcCAmaH',
  'fR:lin:parasmai:prathama:eka': 'fcCet',
  'fR:lin:parasmai:prathama:dvi': 'fcCetAm',
  'fR:lin:parasmai:prathama:bahu': 'fcCeyuH',
  'fR:lin:parasmai:madhyama:eka': 'fcCeH',
  'fR:lin:parasmai:madhyama:dvi': 'fcCetam',
  'fR:lin:parasmai:madhyama:bahu': 'fcCeta',
  'fR:lin:parasmai:uttama:eka': 'fcCeyam',
  'fR:lin:parasmai:uttama:dvi': 'fcCevaH',
  'fR:lin:parasmai:uttama:bahu': 'fcCema',
  // Athematic optatives (liṅ) from present stems — source: bhagavadgita.org.in / standard.
  // bhindyāt/rundhyāt/duhyāt/śṛṇuyāt (were thematic *bhidet etc.).
  'bhid:lin:parasmai:prathama:eka': 'bhinDyAt',
  'bhid:lin:parasmai:prathama:dvi': 'bhinDyAtAm',
  'bhid:lin:parasmai:prathama:bahu': 'bhinDyuH',
  'bhid:lin:parasmai:madhyama:eka': 'bhinDyAH',
  'bhid:lin:parasmai:madhyama:dvi': 'bhinDyAtam',
  'bhid:lin:parasmai:madhyama:bahu': 'bhinDyAta',
  'bhid:lin:parasmai:uttama:eka': 'bhinDyAm',
  'bhid:lin:parasmai:uttama:dvi': 'bhinDyAva',
  'bhid:lin:parasmai:uttama:bahu': 'bhinDyAma',
  'rudh:lin:parasmai:prathama:eka': 'runDyAt',
  'rudh:lin:parasmai:prathama:dvi': 'runDyAtAm',
  'rudh:lin:parasmai:prathama:bahu': 'runDyuH',
  'rudh:lin:parasmai:madhyama:eka': 'runDyAH',
  'rudh:lin:parasmai:madhyama:dvi': 'runDyAtam',
  'rudh:lin:parasmai:madhyama:bahu': 'runDyAta',
  'rudh:lin:parasmai:uttama:eka': 'runDyAm',
  'rudh:lin:parasmai:uttama:dvi': 'runDyAva',
  'rudh:lin:parasmai:uttama:bahu': 'runDyAma',
  'duh:lin:parasmai:prathama:eka': 'duhyAt',
  'duh:lin:parasmai:prathama:dvi': 'duhyAtAm',
  'duh:lin:parasmai:prathama:bahu': 'duhyuH',
  'duh:lin:parasmai:madhyama:eka': 'duhyAH',
  'duh:lin:parasmai:madhyama:dvi': 'duhyAtam',
  'duh:lin:parasmai:madhyama:bahu': 'duhyAta',
  'duh:lin:parasmai:uttama:eka': 'duhyAm',
  'duh:lin:parasmai:uttama:dvi': 'duhyAva',
  'duh:lin:parasmai:uttama:bahu': 'duhyAma',
  'zru:lin:parasmai:prathama:eka': 'zRuNuyAt',
  'zru:lin:parasmai:prathama:dvi': 'zRuNuyAtAm',
  'zru:lin:parasmai:prathama:bahu': 'zRuNuyuH',
  'zru:lin:parasmai:madhyama:eka': 'zRuNuyAH',
  'zru:lin:parasmai:madhyama:dvi': 'zRuNuyAtam',
  'zru:lin:parasmai:madhyama:bahu': 'zRuNuyAta',
  'zru:lin:parasmai:uttama:eka': 'zRuNuyAm',
  'zru:lin:parasmai:uttama:dvi': 'zRuNuyAva',
  'zru:lin:parasmai:uttama:bahu': 'zRuNuyAma',
  // Class-5 ñit roots: present-stem finite forms (Y marker never in surface).
  // class-5 (ci/sun/śi/stṛ) imperative — regular ₹ṇvantu/cinavāni pattern,
  // verified for the class-5 paradigm of √śru (Wiktionary śṛṇóti).
  'ciY:lot:parasmai:prathama:eka': 'cinotu',
  'ciY:lot:parasmai:prathama:dvi': 'cinutAm',
  'ciY:lot:parasmai:prathama:bahu': 'cinvantu',
  'ciY:lot:parasmai:madhyama:dvi': 'cinutam',
  'ciY:lot:parasmai:madhyama:bahu': 'cinuta',
  'ciY:lot:parasmai:uttama:eka': 'cinavARi',
  'ciY:lot:parasmai:uttama:dvi': 'cinavAva',
  'ciY:lot:parasmai:uttama:bahu': 'cinavAma',
  'zuY:lot:parasmai:prathama:dvi': 'sunutAm',
  'zuY:lot:parasmai:prathama:bahu': 'sunvantu',
  'zuY:lot:parasmai:madhyama:eka': 'sunu',
  'zuY:lot:parasmai:madhyama:dvi': 'sunutam',
  'zuY:lot:parasmai:madhyama:bahu': 'sunuta',
  'zuY:lot:parasmai:uttama:eka': 'sunavARi',
  'zuY:lot:parasmai:uttama:dvi': 'sunavAva',
  'zuY:lot:parasmai:uttama:bahu': 'sunavAma',
  'SiY:lot:parasmai:prathama:dvi': 'SinutAm',
  'SiY:lot:parasmai:prathama:bahu': 'SInvantu',
  'SiY:lot:parasmai:madhyama:eka': 'Sinu',
  'SiY:lot:parasmai:madhyama:dvi': 'Sinutam',
  'SiY:lot:parasmai:madhyama:bahu': 'Sinuta',
  'SiY:lot:parasmai:uttama:eka': 'SinavARi',
  'SiY:lot:parasmai:uttama:dvi': 'SinavAva',
  'SiY:lot:parasmai:uttama:bahu': 'SinavAma',
  'stfY:lot:parasmai:prathama:dvi': 'stfRnutAm',
  'stfY:lot:parasmai:prathama:bahu': 'stfRvantu',
  'stfY:lot:parasmai:madhyama:eka': 'stfRnu',
  'stfY:lot:parasmai:madhyama:dvi': 'stfRnutam',
  'stfY:lot:parasmai:madhyama:bahu': 'stfRnuta',
  'stfY:lot:parasmai:uttama:eka': 'stfRnavARi',
  'stfY:lot:parasmai:uttama:dvi': 'stfRnavAva',
  'stfY:lot:parasmai:uttama:bahu': 'stfRnavAma',
  // class-5 optative (cinuyāt / sunuyāt / śinuyāt / stṛṇuyāt), regular
  // paradigm verified by √śru (zRuNuyAt/zRuNuyAtAm/zRuNuyuH).
  'ciY:lin:parasmai:prathama:eka': 'cinuyAt',
  'ciY:lin:parasmai:prathama:dvi': 'cinuyAtAm',
  'ciY:lin:parasmai:prathama:bahu': 'cinuyuH',
  'ciY:lin:parasmai:madhyama:eka': 'cinuyAH',
  'ciY:lin:parasmai:madhyama:dvi': 'cinuyAtam',
  'ciY:lin:parasmai:madhyama:bahu': 'cinuyAta',
  'ciY:lin:parasmai:uttama:eka': 'cinuyAm',
  'ciY:lin:parasmai:uttama:dvi': 'cinuyAva',
  'ciY:lin:parasmai:uttama:bahu': 'cinuyAma',
  'zuY:lin:parasmai:prathama:dvi': 'sunuyAtAm',
  'zuY:lin:parasmai:prathama:bahu': 'sunuyuH',
  'zuY:lin:parasmai:madhyama:eka': 'sunuyAH',
  'zuY:lin:parasmai:madhyama:dvi': 'sunuyAtam',
  'zuY:lin:parasmai:madhyama:bahu': 'sunuyAta',
  'zuY:lin:parasmai:uttama:eka': 'sunuyAm',
  'zuY:lin:parasmai:uttama:dvi': 'sunuyAva',
  'zuY:lin:parasmai:uttama:bahu': 'sunuyAma',
  'SiY:lin:parasmai:prathama:dvi': 'SinuyAtAm',
  'SiY:lin:parasmai:prathama:bahu': 'SinuyuH',
  'SiY:lin:parasmai:madhyama:eka': 'SinuyAH',
  'SiY:lin:parasmai:madhyama:dvi': 'SinuyAtam',
  'SiY:lin:parasmai:madhyama:bahu': 'SinuyAta',
  'SiY:lin:parasmai:uttama:eka': 'SinuyAm',
  'SiY:lin:parasmai:uttama:dvi': 'SinuyAva',
  'SiY:lin:parasmai:uttama:bahu': 'SinuyAma',
  'stfY:lin:parasmai:prathama:dvi': 'stfRnuyAtAm',
  'stfY:lin:parasmai:prathama:bahu': 'stfRnuyuH',
  'stfY:lin:parasmai:madhyama:eka': 'stfRnuyAH',
  'stfY:lin:parasmai:madhyama:dvi': 'stfRnuyAtam',
  'stfY:lin:parasmai:madhyama:bahu': 'stfRnuyAta',
  'stfY:lin:parasmai:uttama:eka': 'stfRnuyAm',
  'stfY:lin:parasmai:uttama:dvi': 'stfRnuyAva',
  'stfY:lin:parasmai:uttama:bahu': 'stfRnuyAma',
  'ciY:lit:parasmai:prathama:eka': 'cikAya',
  'zuY:lan:parasmai:prathama:eka': 'asunot',
  'zuY:lin:parasmai:prathama:eka': 'sunuyAt',
  'zuY:lot:parasmai:prathama:eka': 'sunotu',
  'SiY:lan:parasmai:prathama:eka': 'aSinot',
  'SiY:lin:parasmai:prathama:eka': 'SinuyAt',
  'SiY:lot:parasmai:prathama:eka': 'Sinotu',
  'stfY:lan:parasmai:prathama:eka': 'astfRnot',
  'stfY:lin:parasmai:prathama:eka': 'stfRnuyAt',
  'stfY:lot:parasmai:prathama:eka': 'stfRnotu',
};
/** 6.1.101 akaḥ savarṇe dīrghaḥ for upasarga + athematic form. */
function coalesceUpasarga(upa: string, form: string): SLP1 {
  if (upa.endsWith('A') && form.startsWith('a')) return upa + form.slice(1); // 6.1.84: ā+a → ā
  if (upa.endsWith('a') && form.startsWith('A')) return upa.slice(0, -1) + 'A' + form.slice(1); // 6.1.84: a+ā → ā (pra+āda → prāda)
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
  fR: { strong: 'ar', weak: 'ar' },          // āra/āruḥ (perfect of √ṛ, no reduplication)
  dviS: { strong: 'didvez', weak: 'didviz' }, // didveṣa/didviṣuḥ (perfect of √dviṣ)
  grah: { strong: 'jagrAh', weak: 'jagf' },    // jagrāha/jagṛhuḥ (perfect of √grah)
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
  // ā-final roots (pā/sthā/glai) take the au (7.1.34 āta au ṇalaḥ) form only
  // in the strong 1s/3s *parasmai* forms. The ātmane-pada perfect uses the weak
  // stem throughout (dadhé, papé, tasthé, ...), so exclude it here; otherwise
  // we would derive *dadhaue / *papaue (SLP1 daDOe / papOe).
  const auRoots = ['pA', 'sTA', 'gAi', 'jYA', 'vI', 'DA', 'yA'];
  const auForm = auRoots.includes(root) && pada !== Pada.Atmane &&
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
  // Library callers may omit lakāra; normalise once so every lakāra-dependent
  // branch (present-system yak, lakāra labels, etc.) sees a concrete value.
  if (args.lakara === undefined) args = { ...args, lakara: Lakara.Lat };
  const dhatu = resolveDhatu(args.dhatu);
  // bhāve (impersonal passive) is always 3s ātmane, and its forms are
  // identical to the karmani 3s. Delegate to the ordinary karmani derivation
  // with prathama/eka forced so that lakāra-specific endings (aṣṭādhyāyī
  // present-system yak vs. future/perfect stems) are honoured instead of
  // emitting "*pacyate" for every lakāra.
  if (args.prayoga === Prayoga.Bhave) {
    return deriveTinantas({ ...args, prayoga: Prayoga.Karmani,
      purusha: Purusha.Prathama, vacana: Vacana.Eka });
  }
  // The aorist (luṅ) uses a separate formation system; dispatch to it.
  // Strip dhātupāṭha ñit marker Y (ciY → ci) for aorist lookup.
  const aoristRoot = initialShatva(initialNati(dhatu.text)).replace(/[Yx]$/, '');
  if ((args.lakara === Lakara.LatN || args.lakara === Lakara.Lang) &&
      hasAorist(aoristRoot)) {
    const passive = (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani;
    // Passive aorists take ātmane-pada (and, for the roots listed in the
    // passive-aorist table, the special -i/-ci 3s forms).
    const aoristPada = passive ? Pada.Atmane : args.pada ?? dhatu.pada;
    const p = deriveAorist({
      root: aoristRoot,
      pada: aoristPada,
      purusha: args.purusha,
      vacana: args.vacana,
      upasarga: args.upasarga,
      passive,
    });
    return p ? [p] : [];
  }
  // Athematic (non-Sap) forms for common roots. These bypass the thematic
  // vikaraṇa and use root-specific stems/endings. In the perfect (liṭ) the
  // karmani (passive) uses the same ātmane-pada forms as the middle voice, so
  // reuse those verified forms here (e.g. dā → dade, jñā → jajñe).
  const athematicPada = (args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani
    ? Pada.Atmane : args.pada ?? dhatu.pada;
  const athematic = (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    ((args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari ||
      ((args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani && args.lakara === Lakara.Lit))
    ? presentForm(dhatu.text, args.lakara, athematicPada,
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
  // Dhātupāṭha indicatory markers Y (ñit) and x are not phonemes. Strip them
  // before any vikaraṇa/sandhi is applied; otherwise x + a can surface as *-la-
  // (mucxati → *mucalati). Explicit athematic forms are keyed by dhatu.text.
  let rootText = /[Yx]$/.test(dhatu.text) ||
    (dhatu.gana === Gana.Divadi && /I$/.test(dhatu.text)) // class-4 indicatory ī
    ? dhatu.text.slice(0, -1) : dhatu.text;
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
  // drop the dhātupāṭha final -u/-I marker in the present system
  // (nftI → nṛtyati, trasI → trasyati, divu → dīvyati).
  const class4 = dhatu.gana === Gana.Divadi &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara);
  if (class4 && /[uI]$/.test(rootText)) rootText = rootText.slice(0, -1);
  // 3.1.134ff: Curādi (class-10) roots take ṇic, so their present stem is
  // guṇa(root) + ay (pūj + ay → pūjayati, cur → corayati).
  const class10 = dhatu.gana === Gana.Curadi &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    [Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.Lin].includes(args.lakara);
  if (class10) {
    const bare = /[ai]$/.test(rootText) ? rootText.slice(0, -1) : rootText;
    // Guṇa the root's last SHORT vowel (cur → cor, mid → med); long vowels
    // (pūj, kṣep) are already guṇa and stay unchanged.
    let g = bare;
    for (let i = bare.length - 1; i >= 0; i--) {
      const short = { i: 'e', u: 'o', f: 'ar', x: 'al' }[bare[i]];
      if (short) { g = bare.slice(0, i) + short + bare.slice(i + 1); break; }
      if ('aA`.'.includes(bare[i])) break; // stop at a/a-like vowel
    }
    rootText = g + 'ay';
  }
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
  // Saṇādi (causative/desiderative/intensive) stems are built from the bare
  // root: reduplication must see the root, not an upasarga (pra+jigamiṣati,
  // pra+bobhavīti). Prefix the upasarga onto the finished stem afterwards.
  const sanadiResult = upasargaArg && isUpasarga(upasargaArg) && sanadi !== Sanadi.None
    ? (() => {
        const bare = buildSanadiStem(shatvaText, sanadi);
        return { ...bare, root: coalesceUpasarga(upasargaArg!, bare.root) };
      })()
    : buildSanadiStem(rootText, sanadi);
  // karmāṇi (passive) always takes ātmane-pada endings.
  const pada = sanadiResult.pada ??
    ((args.prayoga ?? Prayoga.Kartari) === Prayoga.Karmani ? Pada.Atmane : args.pada ?? dhatu.pada);
  // Default to lat when the library caller omits lakāra (the CLI always passes
  // it), so every downstream lakāra-dependent check sees a concrete value.
  const lakara = args.lakara ?? Lakara.Lat;
  const config = LAKARA_CONFIG[lakara] ?? LAKARA_CONFIG[Lakara.Lat];
  const suffixTable = pada === Pada.Atmane ? config.atmane : config.parasmai;
  const suffix = suffixTable[args.purusha][args.vacana];

  // The passive `ya` vikaraṇa (3.1.67) belongs to the present system only;
  // in other lakāras the passive uses the ordinary lakāra vikaraṇa with
  // ātmanepada endings (bhaviṣyate, babhūve, ...).
  const passivePresent = [Lakara.Lat, Lakara.Lan, Lakara.Lot, Lakara.Lin].includes(args.lakara);
  const kartariVikarana =
    args.prayoga === Prayoga.Karmani && passivePresent ? VIKARANA_KARMANI
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
    jFnA: 'jFA', zru: 'zrU', grah: 'gfh', DA: 'dI', sTA: 'sTI', pA: 'pI', // dhā/sthā/pā passives (sthīyate, not *sthātyate)
  };
  // In non-present lakāras the yak-vikaraṇa does not apply, so the passive
  // uses the ordinary lakāra stem (futureStem/perfectStem/...) with ātmane-pada
  // endings. Restrict the yak-based PASSIVE_STEMS override to the present
  // system only; otherwise we would get *pacte /*Bavte instead of paksyate /
  // bhavisyate (cf. 3.1.67, which requires a sārvadhātuka affix).
  // In non-present lakāras the special stem (liṭ-reduplication, lut/future
  // stem) must be built from the bare root and only then have the upasarga
  // prefixed: pra + gam → prajagāma / pragantā / pragamiṣyati, never
  // *papragama / *pragamitā / *pragamiṣyati. The override tables are keyed by
  // bare roots, so deriving from the prefixed rootText would miss them.
  const upasargaStem = upasargaArg && isUpasarga(upasargaArg) && config.rootTransform &&
    (args.prayoga ?? Prayoga.Kartari) === Prayoga.Kartari &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None
    ? (bare: string) => {
        const base = args.lakara === Lakara.Lit
          ? (presentForm(bare, Lakara.Lit, pada, args.purusha, args.vacana) ??
             perfectStem(bare, args.purusha, args.vacana, pada))
          : config.rootTransform!(bare, args.purusha, args.vacana, pada);
        return coalesceUpasarga(upasargaArg!, base);
      }
    : undefined;
  const rootOverride = args.prayoga === Prayoga.Karmani && passivePresent
    ? (PASSIVE_STEMS[dhatu.text]
        ? (upasargaArg && isUpasarga(upasargaArg)
            ? coalesceUpasarga(upasargaArg, PASSIVE_STEMS[dhatu.text])
            : PASSIVE_STEMS[dhatu.text])
        : sanadiResult.root) // rootText already carries any upasarga
    : args.lakara === Lakara.Lin && dhatu.text === 'han' && (args.sanadi ?? Sanadi.None) === Sanadi.None
      ? 'vad' // 2.4.42 (hano vada liNi — vadet)
      : upasargaStem
        ? upasargaStem(shatvaText)
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
  // Dhātupāṭha indicatory markers Y (class-5 ñit) and x (e.g. Apx/Sakx/mucx)
  // are not phonemes — never let them leak into a derived surface form
  // (SiYati → Sati, Apxati → Apati).
  if (/[Yx]$/.test(dhatu.text)) {
    for (const term of result.terms) {
      if (/[Yx]/.test(term.text)) {
        term.text = term.text.replace(/[Yx]/g, '');
        result.collapse();
        break;
      }
    }
  }
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
