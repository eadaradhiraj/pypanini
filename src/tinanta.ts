import { Prakriya } from './core/prakriya';
import { runTinantaPipeline, RuleContext, SuffixStep } from './core/rules';
import {
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
import { gunafy } from './core/slp1';

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
  'as:lat:parasmai:prathama:eka': 'asti',
  'as:lat:parasmai:madhyama:eka': 'asi',
  'as:lat:parasmai:uttama:eka': 'asmi',
  'as:lat:parasmai:prathama:bahu': 'santi',
  'as:lin:parasmai:prathama:eka': 'syAt',   // syāt
  'as:lin:parasmai:madhyama:eka': 'syAH',   // syāḥ
  'as:lin:parasmai:uttama:eka': 'syAm',     // syām
  'as:lot:parasmai:prathama:eka': 'astu',
  'as:lot:parasmai:madhyama:eka': 'ehi',
  // √dā (3P) — dadāti, dadāsi, dadāmi; dehi; dadātu
  'dA:lat:parasmai:prathama:eka': 'dadAti',
  'dA:lat:parasmai:madhyama:eka': 'dadAsi',
  'dA:lat:parasmai:uttama:eka': 'dadAmi',
  'dA:lat:parasmai:prathama:bahu': 'dadati',
  'dA:lot:parasmai:prathama:eka': 'dadAtu',
  'dA:lot:parasmai:madhyama:eka': 'dehi',
  'dA:lot:parasmai:uttama:eka': 'dadAni',
  // √kṛ (5P/8P) — karoti, karoṣi, karomi; kuru; karotu
  'kf:lat:parasmai:prathama:eka': 'karoti',
  'kf:lat:parasmai:madhyama:eka': 'karozi',  // karoṣi
  'kf:lat:parasmai:uttama:eka': 'karomi',
  'kf:lat:parasmai:prathama:bahu': 'kurvanti',
  'kf:lot:parasmai:prathama:eka': 'karotu',
  'kf:lot:parasmai:madhyama:eka': 'kuru',
  'kf:lot:parasmai:uttama:eka': 'karavANi',
  // √han (2P) — hanti, haṃsi; jahi; hantu
  'han:lat:parasmai:prathama:eka': 'hanti',
  'han:lat:parasmai:madhyama:eka': 'haMsi',  // haṃsi
  'han:lat:parasmai:uttama:eka': 'hanmi',
  'han:lot:parasmai:prathama:eka': 'hantu',
  'han:lot:parasmai:madhyama:eka': 'jahi',
  // √kṛ (8P/5Ā) — ātmane kurute, kuruṣe, kurve
  'kf:lat:atmane:prathama:eka': 'kurute',
  'kf:lat:atmane:madhyama:eka': 'kuruze',  // kuruṣe
  'kf:lat:atmane:uttama:eka': 'kurvE',     // kurve
  'kf:lat:atmane:prathama:bahu': 'kurvate',
  'kf:lot:atmane:prathama:eka': 'kurutAm',
  'kf:lot:atmane:madhyama:eka': 'kuruzva', // kuruṣva
  'kf:lin:atmane:prathama:eka': 'kurvIta', // kurvīta
  // √i (2P) — eti, eṣi, emi; etu/ehi
  'i:lat:parasmai:prathama:eka': 'eti',
  'i:lat:parasmai:madhyama:eka': 'ezi',    // eṣi
  'i:lat:parasmai:uttama:eka': 'emi',
  'i:lat:parasmai:prathama:bahu': 'yAnti', // yānti
  'i:lot:parasmai:prathama:eka': 'etu',
  'i:lot:parasmai:madhyama:eka': 'ehi',
  // √yā (2P) — yāti, yāsi, yāmi
  'yA:lat:parasmai:prathama:eka': 'yAti',
  'yA:lat:parasmai:madhyama:eka': 'yAsi',
  'yA:lat:parasmai:uttama:eka': 'yAmi',
  'yA:lot:parasmai:madhyama:eka': 'yAhi',
};
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
};
function perfectStem(root: string, purusha: Purusha, vacana: Vacana): string {
  // Strong stem in 3s, 3d, 2s, 1s; weak elsewhere (7.1.3ff guṇa/niyama).
  const isStrong = (purusha === Purusha.Prathama && vacana !== Vacana.Bahu) ||
    (purusha === Purusha.Madhyama && vacana === Vacana.Eka) ||
    (purusha === Purusha.Uttama && vacana === Vacana.Eka);
  const entry = PERFECT_STEMS[root];
  const stem = entry ? (isStrong ? entry.strong : entry.weak) : root[0] + 'a' + root;
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
  const athematic = (args.sanadi ?? Sanadi.None) === Sanadi.None
    ? presentForm(dhatu.text, args.lakara, args.pada ?? dhatu.pada,
        args.purusha, args.vacana)
    : undefined;
  if (athematic) {
    const p = new Prakriya([athematic]);
    p.record(`3.2.123 (${LAKARA_LABEL[args.lakara] ?? 'la~w'} vidhāna)`);
    p.record('3.4.78 (athematic tiṅ)');
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
    rootText = prefix + rootPart;
  }
  const sanadiResult = buildSanadiStem(rootText, sanadi);
  const pada = sanadiResult.pada ?? args.pada ?? dhatu.pada;
  const config = LAKARA_CONFIG[args.lakara] ?? LAKARA_CONFIG[Lakara.Lat];
  const suffixTable = pada === Pada.Atmane ? config.atmane : config.parasmai;
  const suffix = suffixTable[args.purusha][args.vacana];

  const kartariVikarana =
    args.prayoga === Prayoga.Karmani ? VIKARANA_KARMANI : config.vikarana;
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

  const rootOverride = config.rootTransform?.(sanadiResult.root, args.purusha, args.vacana);
  const ctx: RuleContext = {
    prakriya,
    args: { ...args, dhatu },
    lakaraLabel: LAKARA_LABEL[args.lakara] ?? 'la~w',
    suffixLabel: suffix.label,
    vikaranaLabel: vikarana.label,
    vikaranaSurface: vikarana.surface,
    doGuna: sanadiResult.doGuna ?? config.doGuna,
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
