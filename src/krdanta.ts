import { Prakriya } from './core/prakriya';
import { gunafy, vrddhify } from './core/slp1';
import { KrdantaArgs, Krt, Prayoga, Sanadi } from './core/types';
import { resolveDhatu } from './data/dhatupatha';
import { buildSanadiStem } from './sanadi';

interface KrtSpec {
  /** SLP1 suffix appended to the (possibly strengthened) root. */
  suffix: string;
  /** Root grading before the suffix. */
  grade: 'none' | 'guna' | 'vrddhi';
  /** Optional extra material inserted between root and suffix. */
  infix?: string;
  prayoga: Prayoga;
  /** Traditional label of the kṛt pratyaya. */
  pratyaya: string;
  /** Sūtra that introduces it (codes verified against the bundled Sūtrapaṭha). */
  code: string;
}

const KRT_SPECS: Record<Krt, KrtSpec> = {
  [Krt.Tac]: {
    suffix: 'ta', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'kta', code: '3.2.102 (niṣṭhā: kta)',
  },
  [Krt.Tfc]: {
    suffix: 'tf', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'tṛc', code: '3.2.135 (tṛc / tṛn)',
  },
  [Krt.Satr]: {
    suffix: 'at', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'śatṛ', code: '3.2.124 (lataḥ śatṛ-śānacau)',
  },
  [Krt.Ani]: {
    suffix: 'aRIya', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'anīyar', code: '3.1.96 (tavyattavyānīyaraḥ)',
  },
  [Krt.Tum]: {
    suffix: 'tum', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'tumun', code: '3.3.10 (tumun-ṇvulau)',
  },
  [Krt.Tavya]: {
    suffix: 'tavya', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'tavyat', code: '3.1.96 (tavyattavyānīyaraḥ), 7.2.10 (no iṭ for kṛ)',
  },
  [Krt.LyuT]: {
    suffix: 'aRa', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'lyuṭ', code: '3.3.115 (lyuṭ ca)',
  },
  [Krt.KtvA]: {
    suffix: 'tvA', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'ktvā', code: '3.4.18 (ktvā)',
  },
  [Krt.Nvul]: {
    suffix: 'aka', grade: 'vrddhi', prayoga: Prayoga.Kartari,
    pratyaya: 'ṇvul', code: '3.1.133 (ṇvul-tṛcau)',
  },
  [Krt.Ktavatu]: {
    suffix: 'tavAn', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ktavatu', code: '3.2.102 (niṣṭhā: ktavatu)',
  },
  [Krt.SanaC]: {
    suffix: 'amAna', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'śānac', code: '3.2.124 (lataḥ śatṛ-śānacau)',
  },
  [Krt.Yat]: {
    suffix: 'ya', grade: 'vrddhi', prayoga: Prayoga.Karmani,
    pratyaya: 'yat', code: '3.1.97 (aco yat)',
  },
  [Krt.Ktin]: {
    suffix: 'ti', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'ktin', code: '3.3.94 (striyāṃ ktin), 3.3.97 (ūti-yūti-jūti-sāti-heti-kīrti)',
  },
  [Krt.Nini]: {
    suffix: 'in', grade: 'vrddhi', prayoga: Prayoga.Kartari,
    pratyaya: 'ṇini', code: '3.3.170 (āvaśyakādhamarṇyayor ṇiniḥ)',
  },
  [Krt.Sanan]: {
    suffix: 'mAna', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'śānan', code: '3.2.128 (pūṅ yajoḥ śānan)',
  },
  [Krt.STran]: {
    suffix: 'tra', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'ṣṭran', code: '3.2.182 (dām-nī-stu… karaṇe ṣṭran)',
  },
  [Krt.TRn]: {
    suffix: 'tf', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'tṛn', code: '3.2.135 (tṛn — habitual agent)',
  },
  [Krt.Kyap]: {
    suffix: 'yA', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'kyap', code: '3.3.99 (sañjñāyāṃ … kyap)',
  },
  [Krt.Sa]: {
    suffix: 'A', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'śa', code: '3.3.100 (kṛñaḥ śa ca) / 3.3.101 (iccyā)',
  },
  [Krt.uH]: {
    suffix: 'u', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'uḥ', code: '3.2.168 (san-āśaṃsa-bhikṣa uḥ)',
  },
  [Krt.ghaH]: {
    suffix: 'a', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'ghaḥ', code: '3.3.118 (puṃsi sañjñāyāṃ ghaḥ)',
  },
  [Krt.raH]: {
    suffix: 'ra', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'raḥ', code: '3.2.167 (nami-kampi-… dīpo raḥ)',
  },
  [Krt.kru]: {
    suffix: 'ru', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kru', code: '3.2.174 (bhiyaḥ kru-klukanau)',
  },
  [Krt.AruH]: {
    suffix: 'Aru', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'āruḥ', code: '3.2.173 (śṝ-vandyor āruḥ)',
  },
  [Krt.varac]: {
    suffix: 'vara', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'varac', code: '3.2.175 (sthā-īśa-bhāsa-pisa-kaso varac)',
  },
  [Krt.kvip]: {
    suffix: '', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kvip', code: '3.2.178 (anyebhyo\'pi dṛśyate — kvip)',
  },
  [Krt.Du]: {
    suffix: 'u', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ḍu', code: '3.2.180 (vi-pra-sambhyo ḍu)',
  },
  [Krt.knu]: {
    suffix: 'nu', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'knu', code: '3.2.140 (trasi-gṛdhi-dhṛṣi-kṣipeḥ knuḥ)',
  },
  [Krt.kSnu]: {
    suffix: 'zNu', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kṣnu', code: '3.2.139 (glā-ji-sthaś ca kṣnuḥ)',
  },
  [Krt.izNuc]: {
    suffix: 'izNu', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'iṣṇuc', code: '3.2.138 (bhuvaś ca — iṣṇuc)',
  },
  [Krt.yuc]: {
    suffix: 'ana', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'yuc', code: '3.2.148 (calana-śabdārthād akarmakād yuc)',
  },
  [Krt.ruH2]: {
    suffix: 'ru', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ruḥ', code: '3.2.159 (dā-dheṭ-si-śada-sado ruḥ)',
  },
  [Krt.kurac]: {
    suffix: 'ura', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kurac', code: '3.2.162 (vidi-bhidi-cchideḥ kurac)',
  },
  [Krt.ghurac]: {
    suffix: 'ura', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ghurac', code: '3.2.161 (bhañja-bhāsa-mido ghurac)',
  },
  [Krt.kvarap]: {
    suffix: 'vara', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kvarap', code: '3.2.163 (iṇ-naś-ji-sartibhyaḥ kvarap, 6.1.71 ṭuk)',
  },
  [Krt.vuN]: {
    suffix: 'aka', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'vuñ', code: '3.2.146 (ninda-hiṃsā… vuñ)',
  },
  [Krt.ghinuN]: {
    suffix: 'I', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ghinuṇ', code: '3.2.143/145 (vau/pre ghinuṇ)',
  },
  [Krt.cAnaS]: {
    suffix: 'Ana', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'cānaś', code: '3.2.129 (tācchīlya-vayovacana-śaktiṣu cānaś)',
  },
};

/** kvip (3.2.178): zero-suffix agent nouns; final consonant adjusts per root. */
const KVIP_FORMS: Record<string, string> = {
  yuj: 'yuk',   // yuk (joining)
  cid: 'cit',   // chit (piercing)
  Bid: 'Bit',   // bhit (dividing)
  vac: 'vAk',   // vāk (voice)
  gam: 'jagat', // jagat (world — reduplicated)
  dyut: 'vidyut', // vidyut (lightning — reduplicated)
  zrI: 'zrI',   // śrī
};

/** ṣṭran (3.2.182) stems: the suffix is -tra on these roots (guṇa/vṛddhi varies). */
const STRAN_STEMS: Record<string, string> = {
  dA: 'dA',    // dātra (sickle)
  ni: 'ne',    // netra (eye)
  stu: 'sto',  // stotra (praise)
  yu: 'yo',    // yotra
  dhA: 'dA',   // dhātra (nurse, 3.2.181)
};

/** Stem overrides for roots with an irregular kṛt formation (nipātana). */
/** iṣṇuc (3.2.136/138): per-root stems (guṇa/vṛddhi already applied). */
const IZNU_STEMS: Record<string, string> = {
  BU: 'Bav',    // bhaviṣṇu
  ruc: 'roc',   // rociṣṇu
  saha: 'sah',  // sahiṣṇu
  car: 'car',   // cariṣṇu
  vFt: 'vart',  // vartiṣṇu
};

const STEM_OVERRIDE: Partial<Record<Krt, Record<string, string>>> = {
  [Krt.Satr]: { kf: 'kurv' }, // kṛ + śatṛ → kurvat
  [Krt.SanaC]: { kf: 'kurv' }, // kṛ + śānac → kurvāṇa
  [Krt.Sanan]: { pU: 'pav', yaj: 'yaj' }, // pū/pava + māna → pavamāna
  [Krt.STran]: STRAN_STEMS, // dātra, netra, stotra, yotra
  [Krt.TRn]: { hu: 'ho', ni: 'neS', tviz: 'tvaS' }, // hotṛ, neṣṭṛ, tvaṣṭṛ (with ṣuk/ṣ)
  [Krt.Kyap]: { vid: 'vid', man: 'man', i: 'it', zi: 'zay' }, // vidyā, manyā, ityā, śayyā
  [Krt.Sa]: { kf: 'kriy', iz: 'icC' }, // kriyā (3.3.100), icchā (3.3.101)
  [Krt.Ktin]: { av: 'U', yu: 'yU', ju: 'jU', san: 'sA', han: 'he' }, // ūti, yūti, jūti, sāti, heti (3.3.97); kṛ→kṛti regular
  [Krt.uH]: { Bikz: 'Bikz', AzaMs: 'AzaMs', iz: 'icC' }, // bhikṣu, āśaṃsu (3.2.168), icchu (3.2.169)
  [Krt.ghaH]: { CAd: 'Cad' }, // chada (3.3.118, lip)
  [Krt.raH]: { nam: 'nam', dIp: 'dIp', kamp: 'kamp', smi: 'sme', hiMs: 'hiMs' }, // namra, dīpra…
  [Krt.kru]: { Bi: 'Bi' }, // bhīru (3.2.174)
  [Krt.AruH]: { vand: 'vand', sF: 'sa' }, // vandāru, śarāru (3.2.173)
  [Krt.varac]: { sTA: 'sTA', IS: 'IS' }, // sthāvara, īśvara (3.2.175)
  [Krt.Du]: { viBU: 'viB', praBU: 'praB', samBU: 'samB' }, // vibhu/prabhu/sambhu (3.2.180)
  [Krt.knu]: { tras: 'tras', gFDi: 'gFd', DFzi: 'DFz', kzip: 'kziN' }, // trasnu/gṛdhnu/dhṛṣṇu/kṣiṇṇu
  [Krt.izNuc]: IZNU_STEMS, // bhaviṣṇu/rociṣṇu/sahiṣṇu/… (3.2.136/138)
  [Krt.yuc]: { cal: 'cal', Sabd: 'Sabd', rav: 'rav', COP: 'Cop', kruD: 'kroD', maND: 'maND' }, // +ana → calana/krodhana/maṇḍana
  [Krt.ruH2]: { dA: 'dA', si: 'sa', sad: 'sad', saD: 'saD' }, // +ru → dāru/saru/sadru
  [Krt.kurac]: { vid: 'vid', Bid: 'Bid', cid: 'cid', vyD: 'viD' }, // +ura → vidura/bhidura/chidura/vidhura
  [Krt.ghurac]: { baNj: 'baNg', BAs: 'BAs', mid: 'med' }, // +ura → bhaṅgura/bhāsura/medura
  [Krt.kvarap]: { i: 'it', naS: 'naS', ji: 'jit', sf: 'sf' }, // +vara → itvara/naśvara/jitvara/sṛvara
  [Krt.ghinuN]: {
    vikaS: 'vikAS', vilas: 'vilAs', pralap: 'pralAp', pradru: 'pradrAv', pravas: 'pravAs',
    duz: 'doz', dviS: 'dvez', yuj: 'yog', tyaj: 'tyAg', raj: 'rAg', Baj: 'BAG',
    Sram: 'SrAm', Bram: 'BrAm', klam: 'klAm',ksam: 'kzAm', tyag: 'tyAg',
  }, // +I → vikāṣī/vilāsī/doṣī/dveṣī/yogī/tyāgī/…
  [Krt.cAnaS]: { buJ: 'buJj', biF: 'bibR', muND: 'muND', Buz: 'BuZ' }, // +Ana → bhuñjāna/bibhrāṇa
};

const KSNU_SUFFIX: Record<string, string> = {
  glA: 'snu', // glāsnu
  ji: 'zNu',  // jiṣṇu
  sTA: 'snu', // sthāsnu
  BU: 'zNu',  // bhūṣṇu
};

/** Suffixes that take the iṭ augment after a u-final root (7.2.35). */
const IT_SUFFIXES = new Set<Krt>([Krt.Tum, Krt.Tavya, Krt.Tfc]);

/**
 * Derive kṛdantas. The kṛt suffix determines the prayoga in most cases; an
 * explicit `prayoga` argument is recorded but does not yet change the form.
 */
export function deriveKrdantas(args: KrdantaArgs): Prakriya[] {
  const dhatu = resolveDhatu(args.dhatu);
  // kvip (3.2.178): zero suffix with root-specific surface forms.
  if (args.krt === Krt.kvip) {
    const form = KVIP_FORMS[dhatu.text];
    const p = new Prakriya([]);
    p.record("3.2.178 (anyebhyo 'pi dṛśyate — kvip)");
    if (form) p.insert(0, form, ['krt']);
    else p.insert(0, dhatu.text, ['krt']);
    p.collapse();
    return [p];
  }
  const sanadi = buildSanadiStem(dhatu.text, args.sanadi ?? Sanadi.None);
  const spec = { ...KRT_SPECS[args.krt] };

  // ṛ-final roots (kf → kar) take the ṇa-variants; u-final roots take the na-variants.
  const rFinal = dhatu.text.endsWith('f') || dhatu.text.endsWith('F');
  if (args.krt === Krt.Ani) spec.suffix = rFinal ? 'aRIya' : 'anIya';
  if (args.krt === Krt.LyuT) spec.suffix = rFinal ? 'aRa' : 'ana';
  if (args.krt === Krt.Nvul) spec.grade = rFinal ? 'vrddhi' : 'guna';
  if (args.krt === Krt.Yat) spec.grade = rFinal ? 'vrddhi' : 'guna';
  if (args.krt === Krt.kSnu && KSNU_SUFFIX[dhatu.text]) spec.suffix = KSNU_SUFFIX[dhatu.text];
  if (args.krt === Krt.SanaC && rFinal) spec.suffix = 'ARa'; // kṛ → kurvāṇa
  if (args.krt === Krt.Sanan) spec.infix = 'a'; // pava/yaja + māna (thematic a)
  if (args.krt === Krt.TRn && (dhatu.text === 'ni' || dhatu.text === 'tviz')) {
    spec.suffix = 'Tf'; // ṣṭṛ / tvaṣṭṛ: retroflex ṭ after ṣ
  }

  // Grade the root. For u-final roots before consonant-initial suffixes, guṇa
  // yields o and 6.1.78 turns it into av (bhav-); handled after grading below.
  let root = STEM_OVERRIDE[args.krt]?.[dhatu.text] ?? sanadi.root;
  if (!STEM_OVERRIDE[args.krt]?.[dhatu.text]) {
    if (spec.grade === 'guna') root = gunafy(root).text;
    if (spec.grade === 'vrddhi') root = vrddhify(root).text;
  }

  const initial = [root, ...sanadi.extra];
  const p = new Prakriya(initial);
  p.record('1.3.1');
  if (sanadi.code) p.record(sanadi.code);

  // 6.1.78: o + suffix-initial consonant → av (bhū + tṛ → bhavtṛ → kartṛ-like).
  // ṣṭran stems like sto-/yo- are already final o and must keep it.
  if (root.endsWith('o') && args.krt !== Krt.STran && args.krt !== Krt.TRn) {
    p.setText(0, root.slice(0, -1) + 'av');
    p.record('6.1.78 (o → av)');
  }

  // iṭ augment after a u-final root for certain consonant-initial kṛts.
  const baseRoot = dhatu.text;
  if (
    (baseRoot.endsWith('u') || baseRoot.endsWith('U')) &&
    IT_SUFFIXES.has(args.krt) &&
    (args.sanadi ?? Sanadi.None) === Sanadi.None
  ) {
    p.insert(p.length, 'i', ['it']);
    p.record('7.2.35 (iṭ augment after u-final root)');
  }

  // Special infixes for specific pratyayas (e.g. anīyar → karaṇīya).
  if (spec.infix) p.insert(p.length, spec.infix, ['krt-infix']);

  // Thematic saṇādi (yaṅ) needs its -ya- vikaraṇa before the kṛt suffix.
  if (sanadi.vikarana?.surface) {
    p.insert(p.length, sanadi.vikarana.surface, ['vikarana']);
    p.record('3.1.68 (saṇādi vikaraṇa)');
  }

  // 8.2.30 (jhalo jhali): a final palatal of the root becomes a guttural before
  // a jhal (consonant-initial) kṛt suffix. c→k, j→g, C→K, J→G, Y→N.
  if (spec.suffix.length > 0 && /[kKgGcCjJYtTdDn pPbBm]/.test(spec.suffix[0])) {
    const palatalToGuttural: Record<string, string> = {
      c: 'k', j: 'g', C: 'K', J: 'G', Y: 'N',
    };
    const lastIdx = p.length - 1;
    const tail = p.textAt(lastIdx);
    const c = tail.slice(-1);
    if (palatalToGuttural[c]) {
      p.setText(lastIdx, tail.slice(0, -1) + palatalToGuttural[c]);
      p.record('8.2.30 (jhalo jhali: palatal → guttural)');
    }
  }

  // A + i → āyi: insert a y-glide after a long ā before an i-initial suffix
  // (e.g. dā + ṇini → dāyin).
  if (spec.suffix.startsWith('i') && p.length > 0) {
    const lastIdx = p.length - 1;
    const tail = p.textAt(lastIdx);
    if (tail.endsWith('A')) {
      p.setText(lastIdx, tail + 'y');
      p.record('6.1.77 (ā + i → āyi: y-glide)');
    }
  }

  p.insert(p.length, spec.suffix, ['krt']);
  p.record(spec.code);

  p.record(`kṛt-prayoga: ${args.prayoga ?? spec.prayoga} (kāraka-vivakṣā)`);
  p.collapse();
  return [p];
}
