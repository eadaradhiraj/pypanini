import { Pada, Sanadi, SLP1 } from './core/types';

/** Metadata for the saṇādi pratyayas the user requested. */
export const SANADI_INFO: Record<Exclude<Sanadi, Sanadi.None>, {
  label: SLP1;
  devanagari: string;
  meaning: string;
  implemented: boolean;
}> = {
  [Sanadi.San]: {
    label: 'san',
    devanagari: 'सन्',
    meaning: 'desiderative (3.1.7)',
    implemented: true,
  },
  [Sanadi.Nic]: {
    label: 'Nic',
    devanagari: 'णिच्',
    meaning: 'causative',
    implemented: true,
  },
  [Sanadi.Yan]: {
    label: 'yaN',
    devanagari: 'यङ्',
    meaning: 'intensive, thematic (-ya-, ātmanepada)',
    implemented: true,
  },
  [Sanadi.Yang]: {
    label: 'yaN',
    devanagari: 'यङ्',
    meaning: 'alias of Yan (thematic intensive)',
    implemented: true,
  },
  [Sanadi.YangLuk]: {
    label: 'yaNluk',
    devanagari: 'यङ्लुक्',
    meaning: 'intensive, athematic (ya elided, parasmaipada)',
    implemented: true,
  },
};

export interface SanadiDerivation {
  /** The derived (reduplicated / strengthened) root. */
  root: SLP1;
  /** Extra SLP1 terms placed immediately after the root (e.g. "ay", "I"). */
  extra: SLP1[];
  /** Overrides the pada chosen from the dhātu. */
  pada?: Pada;
  /** Overrides the vikaraṇa. An empty surface means "no vikaraṇa". */
  vikarana?: { label: SLP1; surface: SLP1 };
  /** Whether 7.3.84 guṇa should apply to the root. */
  doGuna?: boolean;
  /** Whether o+a → av+a should apply at the root/vikaraṇa boundary. */
  doOAtoAv?: boolean;
  /** Primary sūtra code recorded in the trace. */
  code?: string;
}

const VOWELS = 'aAiIuUfFxXeEoO';
const CONSONANTS = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL';

/**
 * Heavy reduplication (abhyāsa) for yaṅ/yaṅluk, per 6.1.9, 7.4.82 and 7.4.83:
 *   - a/ā reduplicate as ā (dīrgha, 7.4.83)
 *   - i/ī → e, u/ū → o, ṛ/ṝ → ar (guṇa, 7.4.82)
 * Only consonant-initial, single-vowel roots are valid (3.1.22).
 */
export function heavyReduplicate(root: SLP1): SLP1 {
  const first = root[0];
  const vowel = root[1];
  if (!first || !CONSONANTS.includes(first) || !vowel || !VOWELS.includes(vowel)) {
    throw new Error(`saṇādi (yaṅ) requires a consonant-initial root with an initial vowel: ${root}`);
  }
  const numVowels = [...root].filter((c) => VOWELS.includes(c)).length;
  if (numVowels !== 1) {
    throw new Error(`saṇādi (yaṅ) requires a monosyllabic root: ${root}`);
  }
  const redVowel: Record<string, string> = {
    a: 'A', A: 'A', i: 'e', I: 'e', u: 'o', U: 'o', f: 'ar', F: 'ar',
  };
  return first + (redVowel[vowel] ?? vowel) + root;
}

/**
 * Desiderative (san, 3.1.7) stem: heavy reduplication (6.1.9) followed by `sa`,
 * with the special reduplicate changes taught in 7.4.x:
 *   - final a of the reduplicate → i (7.4.79): pac → pi-pac-sa → pipacṣa
 *   - ṛ of the reduplicate → ī (7.4.79 + 7.4.93): kf → ci-kīr-ṣa → cikīrṣa
 * The `sa` → `ṣa` after i/u/ṛ etc. is 8.2.36/8.2.41.
 */
const DESIDERATIVE_STEMS: Record<string, string> = {
  BU: 'buBUza',     // bhū → bubhūṣa-
  pac: 'pipakza',   // pac → pipakṣa-
  kf: 'cikIza',     // kṛ → cikīrṣa-
  gam: 'jigamiza',  // gam → jigamiṣa-
  ni: 'ninIza',     // nī → ninīṣa- (7.4.79 dīrgha of the abhyāsa)
  nI: 'ninIza',     // nī → ninīṣa-
  ji: 'jijIza',     // ji → jijīṣa- (dīrgha in the abhyāsa)
  vid: 'vividiza',  // vid → vividiṣa-
  zru: 'zuzrUza',   // śru → śuśrūṣa- (u in the abhyāsa, dīrgha of ū)
  yaj: 'yiyakza',   // yaj → yiyakṣa- (8.2.30/36 jhal+ṣatva)
  han: 'jighAmsa',  // han → jighāṃsa-
  viz: 'viviza',    // viṣ → viviṣa-
  diS: 'didiza',    // diś → didiṣa- (ś→ṣ, 8.2.36)
  iS: 'iziza',      // iṣ → iṣiṣa- (8.2.36 śatva before the san ṣ)
  dA: 'dIdAsa',     // dā → dīdāsa (3.1.6 dīrgha of abhyāsa)
  mA: 'mImAMsa',    // mā → mīmāṃsa (3.1.6)
  gup: 'jugupza',   // gup → jugupṣa (3.1.5)
  tij: 'titikza',   // tij → titikṣa (3.1.5)
  kit: 'cikitsa',   // kit → cikitsa (3.1.5)
  dviS: 'dviviza',  // dviṣ → dviviṣa (Wiktionary)
  vac: 'vivakza',   // vac → vivakṣa (Wiktionary)
  grah: 'jigfkza',  // grah → jighṛkṣa (conjugation source)
  jFnA: 'jijFAsa',  // jñā → jijñāsa
  sTA: 'tiSThAsa',  // sthā → tiṣṭhāsa
  fR: 'aririza',    // ṛ → ari(ri)ṣa
  mfz: 'mimArjiza', // mṛj → mimārjiṣa (Wiktionary)
  muc: 'mumukza',   // muc → mumukṣa (Wiktionary)
  lab: 'lipsa',     // labh → lipsa (Wiktionary)
  rudh: 'rurutsa',  // rudh → rurutsa (Wiktionary)
};

function desiderativeStem(root: SLP1): SLP1 {
  const known = DESIDERATIVE_STEMS[root];
  if (known) return known;
  // Generic fallback: reduplicate the initial consonant + vowel, set reduplicate
  // vowel to i, and append -sa (with ṣ after i/u/ṛ/f).
  const first = root[0];
  const redVowel = root[1] && VOWELS.includes(root[1]) ? 'i' : 'i';
  // 8.2.36/8.2.41: the san `sa` becomes `ṣa` after i/u/ṛ (and their long
  // counterparts I/U/F), so dīdāsa-type roots keep dental s but śuśrūṣa-type
  // roots take ṣ.
  const sibilant = /[iufFxXIUF]/.test(root.slice(-1)) ? 'z' : 's';
  return first + redVowel + root + sibilant + 'a';
}

/**
 * Irregular / nipātana intensive stems for roots whose ṛ does not follow the
 * regular guṇa pattern (traditional nipātana lists).
 */
const INTENSIVE_IRREGULAR: Record<string, { yan: string; yangLukRoot: string }> = {
  kf: { yan: 'cekrI', yangLukRoot: 'cakAr' }, // kṛ → cekrīya- / cakārti
};

/** Build the saṇādi stem and its derivation overrides. */
export function buildSanadiStem(root: SLP1, sanadi: Sanadi): SanadiDerivation {
  // Dhātupāṭha indicatory markers Y (ñit on class-5 roots ciY/zuY/...) and x
  // (e.g. Apx/Sakx/mucx) are not phonemes — strip them before building
  // secondary stems so they cannot leak into causative/desiderative forms.
  if (/[Yx]$/.test(root)) root = root.slice(0, -1);
  switch (sanadi) {
    case Sanadi.None:
    default:
      return { root, extra: [] };

    case Sanadi.San: {
      // Desiderative: the stem is built with the sa/sa pratyaya (3.1.7) and
      // already ends in ṣ/s; the following tiṅ attaches with no extra vikaraṇa.
      return {
        root: desiderativeStem(root),
        extra: [],
        pada: ['gup', 'tij', 'kit'].includes(root) ? Pada.Atmane : Pada.Parasmai,
        vikarana: { label: '', surface: '' },
        doGuna: false,
        doOAtoAv: false,
        code: root === 'han'
          ? '2.4.47 (sani ca — han→vad, jighāṃsa), 6.4.16 (ajjhanagamāṃ sani — dīrgha)'
          : ['dA', 'mA'].includes(root)
            ? '3.1.6 (dā-mābhyāṃ san — dīdāsa/mīmāṃsa dīrgha), 6.4.16 (ajjhanagamāṃ sani)'
          : ['gup', 'tij', 'kit'].includes(root)
            ? '3.1.5 (gup-tij-kitbhyo san — jugupsā/titikṣā/cikitsā)'
          : ['lupa', 'sada', 'cara', 'japa', 'ja', 'badha', 'hada', 'sf'].includes(root)
            ? '3.1.24 (lupādi-bhyo bhāva-garhāyām san)'
          : ['zri', 'yu', 'bF', 'san', 'Brasz', 'fD', 'fR'].includes(root)
            ? '7.2.49 (sani ivant-ṛdha-bhrasja-dambhu-śri-svṛ-yu-ūrṇu-bhara-jñapi-sanām — iṭ vā)'
          : /[aiufxAEIOU]$/.test(root)
            ? '3.1.7 (san), 6.4.16 (ajjhanagamāṃ sani — dīrgha), 6.1.1 (abhyāsa), 6.1.9'
            : '3.1.7 (san), 6.1.1 (ekāco dve prathamasya), 6.1.9 (abhyāsa), 7.4.79 (reduplicate changes)',
      };
    }

    case Sanadi.Nic: {
      // कृ + णिच् → कारयati (vṛddhi); भू → भावयati (u/ū → Av); दा → दापयati (puk).
      const CAUSATIVE_STEMS: Record<string, string> = {
        pac: 'pAc', kf: 'kAr', yaj: 'yAj', ni: 'nAy', nI: 'nAy', vid: 'ved',
        dA: 'dAp', jFA: 'jFAp', han: 'GAt', car: 'cAr', kram: 'krAm',
        i: 'gam', // 2.4.46 (ṇau gamir abodhane — gamayati)
        duS: 'dUz', // 6.4.90 (doṣo ṇau — dūṣayati)
        bhid: 'bhed', rudh: 'rodh', yuj: 'yoj', svap: 'svAp', // 7.2.116 vṛddhi
        budh: 'bodh', duh: 'doh', ruh: 'roh', ruC: 'roC', // guṇa before ṇic (bodhayati/dohayati)
        vft: 'vart', gras: 'grAs', // vartayati/grāsayati (guṇa/vṛddhi)
        midi: 'med', // Curādi midí — avoid a second -ay when nic is explicit
        sah: 'sAh', vah: 'vAh', // vṛddhi a → ā (sāhayati/vāhayati)
        pf: 'pAr', stf: 'stAr', gf: 'gAr', // 7.2.115 acau ṇiti vṛddhiḥ (ṛ → ār)
        ad: 'Ad', dviS: 'dvez', diS: 'deS', vac: 'vAc', grah: 'grAh', // guṇa/vṛddhi before ṇic (deśayati)
        pA: 'pAy', sTA: 'sTAp', jFnA: 'jFAp', jYA: 'jYAp', fR: 'arp', // puk/dīrgha causatives (jñāpayati, Wiktionary)
        DA: 'DAp', muc: 'moc', iS: 'ez', mfz: 'mArj', lab: 'lamB', hi: 'hAy', // source-backed causatives (hāyayati, Wiktionary)
      };
      let r = CAUSATIVE_STEMS[root] ?? root;
      const c = r.slice(-1);
      if (!CAUSATIVE_STEMS[root] && (c === 'u' || c === 'U')) r = r.slice(0, -1) + 'Av';
      const NIC_25_ROOTS = ['satya', 'pApa', 'SarUpa', 'vIra', 'tUla', 'sloka', 'senA', 'loman', 'tvac', 'varman', 'varcas', 'curA'];
      return {
        root: r,
        extra: ['ay'],
        code: ['pf', 'stf', 'gf'].includes(root)
          ? '7.2.115 (acau ṇiti vṛddhiḥ — pārayati/stārayati/gārayati)'
          : root === 'i'
            ? '2.4.46 (ṇau gamir abodhane — gamayati)'
          : root === 'duS'
            ? '6.4.90 (doṣo ṇau — dūṣayati)'
            : ['gaT', 'jana', 'raj', 'Sam', 'tam', 'jFA'].includes(root)
            ? '6.4.92 (mitāṃ hrasvaḥ — ghaṭayati/janayati/śamayati)'
            : NIC_25_ROOTS.includes(root)
            ? '3.1.25 (satyādi-bhyo ṇic), 7.2.116 (vṛddhi)'
            : '3.1.26 (ṇic), 7.2.116 (vṛddhi)',
      };
    }

    case Sanadi.Yan:
    case Sanadi.Yang: {
      // भू → बोभूय- (boBUya-), पच् → पापच्य- (pApacya-), कृ → चेक्रीय- (cekrIya-).
      // -ya- is supplied by the vikaraṇa override (yak → ya), like karmani.
      return {
        root: INTENSIVE_IRREGULAR[root]?.yan ?? heavyReduplicate(root),
        extra: [],
        pada: Pada.Atmane,
        vikarana: { label: 'yak', surface: 'ya' },
        doGuna: false,
        doOAtoAv: false,
        code: root === 'tuj'
          ? '3.1.22 (yaṅ), 6.1.7 (tujādīnāṃ dīrgho\'bhyāsasya — totujyate)'
          : ['nij', 'vij', 'viz'].includes(root)
            ? '3.1.22 (yaṅ), 7.4.75 (ṇijāṃ trayāṇāṃ guṇaḥ ślau — nenijyate/vevijyate)'
            : '3.1.22 (yaṅ), 6.1.1 (ekāco dve prathamasya), 6.1.9 (abhyāsa), 7.4.82–83 (guṇa/dīrgha of abhyāsa)',
      };
    }

    case Sanadi.YangLuk: {
      // yaṅ with luk (2.4.74): no -ya-, parasmaipada, ī augment (7.3.94).
      // भू → बोभवीति (boBavIti), पच् → पापचीति (pApacIti), कृ → चकार्ति (cakArti).
      const irregular = INTENSIVE_IRREGULAR[root]?.yangLukRoot;
      let stem = irregular ?? heavyReduplicate(root);
      let extra = ['I'];
      if (irregular) {
        extra = []; // cakārti has no ī augment
      } else {
        const c = stem.slice(-1);
        if (c === 'u' || c === 'U') stem = stem.slice(0, -1) + 'av';
      }
      return {
        root: stem,
        extra,
        pada: Pada.Parasmai,
        vikarana: { label: '', surface: '' }, // ya is elided (luk)
        doGuna: false,
        doOAtoAv: false,
        code: '3.1.22, 2.4.74 (yaṅluk), 7.3.94 (iṭ/ī augment, optional)',
      };
    }
  }
}

/** Reduplicate a root (legacy helper kept for compatibility). */
export function reduplicate(root: SLP1): SLP1 {
  return heavyReduplicate(root);
}
