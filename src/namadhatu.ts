import { Prakriya } from './core/prakriya';
import { Lakara, Pada, Purusha, SLP1, Vacana } from './core/types';
import { SUTRAS } from './data/sutras';

/** Denominative (nāmādhatu) pratyayas from Aṣṭādhyāyī 3.1.8–3.1.21. */
export enum NamadhatuPratyaya {
  /** 3.1.8 sup ātmanaḥ kyac — "wishes X for oneself" (putrīyati). */
  Kyac = 'kyac',
  /** 3.1.9 kāmyacca — "desires X" (putrakāmyati). */
  Kamyac = 'kAmyac',
  /** 3.1.10 upamānād ācāre — "treats X as" (putrīyati). */
  KyacAcara = 'kyacAcara',
  /** 3.1.11 kartuḥ kyaṅ salopaś ca — "treats as X" (śyenāyate). */
  KyaN = 'kyaN',
  /** 3.1.21 muṇḍamiśra…bhyo ṇic — "makes X" (muṇḍayati). */
  Nic = 'Nic',
  /** 3.1.12 bhṛśādibhyo bhū-vyac-ver lopaś ca halaḥ — bhṛśāyate. */
  Buvyac = 'Buvyac',
  /** 3.1.13 lohitādibhyo kyaz — lohitāyate. */
  KyaS = 'kyaS',
  /** 3.1.14 kaṣṭāya kramaṇe — kaṣṭāyate. */
  KyaNKa = 'kyaNKa',
  /** 3.1.17 śabda-vaira-kalahā…bhyaḥ karaṇe — śabdāyate. */
  KyaNKara = 'kyaNKara',
  /** 3.1.18 sukhādibhyaḥ kartṛ-vedanāyām — sukhāyate. */
  KyaNSukha = 'kyaNSukha',
  /** 3.1.15 karmaṇo romanTatapoByAM varticaroH — romāyate. */
  Varticara = 'varticara',
  /** 3.1.16 bAzpozmaByAm udvamane — bāṣpāyate. */
  Udvamana = 'udvamana',
  /** 3.1.19 namo-varivaś-citraṇaḥ kyac — namasyati. */
  KyacNama = 'kyacNama',
  /** 3.1.20 puccha-bhāṇḍa-cīvarāṇ ṇiṅ — utpucchayate. */
  NiN = 'NiN',
  /** 3.1.27 kaṇḍvādibhyo yak — kaṇḍūyati. */
  Yak = 'yak',
  /** 3.1.28 gupū-dhūpa-vicchi-paṇi-panibhya āyaḥ — gopāyati. */
  Aya = 'Aya',
  /** 3.1.29 ṛter īyaṅ — ṛtīyate. */
  IyaN = 'IyaN',
  /** 3.1.30 kamer ṇiṅ — kāmayate. */
  KamerNiN = 'KamerNiN',
}

export interface NamadhatuInfo {
  pratyaya: NamadhatuPratyaya;
  sutra: string;
  meaning: string;
  pada: Pada;
  /** Surface material appended to the bare prātipadika. */
  stemSuffix: SLP1;
}

export const NAMADHATU_INFO: Record<NamadhatuPratyaya, NamadhatuInfo> = {
  [NamadhatuPratyaya.Kyac]: {
    pratyaya: NamadhatuPratyaya.Kyac, sutra: '3.1.8',
    meaning: 'wishes (the stem) for oneself', pada: Pada.Parasmai, stemSuffix: 'Iya',
  },
  [NamadhatuPratyaya.Kamyac]: {
    pratyaya: NamadhatuPratyaya.Kamyac, sutra: '3.1.9',
    meaning: 'desires', pada: Pada.Parasmai, stemSuffix: 'kAmya',
  },
  [NamadhatuPratyaya.KyacAcara]: {
    pratyaya: NamadhatuPratyaya.KyacAcara, sutra: '3.1.10',
    meaning: 'treats as / behaves toward (upamāna)', pada: Pada.Parasmai, stemSuffix: 'Iya',
  },
  [NamadhatuPratyaya.KyaN]: {
    pratyaya: NamadhatuPratyaya.KyaN, sutra: '3.1.11',
    meaning: 'treats as / behaves like', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.Nic]: {
    pratyaya: NamadhatuPratyaya.Nic, sutra: '3.1.21',
    meaning: 'makes / renders', pada: Pada.Parasmai, stemSuffix: 'aya',
  },
  [NamadhatuPratyaya.Buvyac]: {
    pratyaya: NamadhatuPratyaya.Buvyac, sutra: '3.1.12',
    meaning: 'becomes / behaves like (bhṛśāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.KyaS]: {
    pratyaya: NamadhatuPratyaya.KyaS, sutra: '3.1.13',
    meaning: 'becomes red etc. (lohitāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.KyaNKa]: {
    pratyaya: NamadhatuPratyaya.KyaNKa, sutra: '3.1.14',
    meaning: 'strives for (kaṣṭāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.KyaNKara]: {
    pratyaya: NamadhatuPratyaya.KyaNKara, sutra: '3.1.17',
    meaning: 'makes a sound etc. (śabdāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.KyaNSukha]: {
    pratyaya: NamadhatuPratyaya.KyaNSukha, sutra: '3.1.18',
    meaning: 'feels happy etc. (sukhāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.Varticara]: {
    pratyaya: NamadhatuPratyaya.Varticara, sutra: '3.1.15',
    meaning: 'hair-raising etc. (romāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.Udvamana]: {
    pratyaya: NamadhatuPratyaya.Udvamana, sutra: '3.1.16',
    meaning: 'sheds tears / sweats (bāṣpāyate)', pada: Pada.Atmane, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.KyacNama]: {
    pratyaya: NamadhatuPratyaya.KyacNama, sutra: '3.1.19',
    meaning: 'honours (namasyati)', pada: Pada.Parasmai, stemSuffix: 'ya',
  },
  [NamadhatuPratyaya.NiN]: {
    pratyaya: NamadhatuPratyaya.NiN, sutra: '3.1.20',
    meaning: 'makes / handles (utpucchayate)', pada: Pada.Atmane, stemSuffix: 'aya',
  },
  [NamadhatuPratyaya.Yak]: {
    pratyaya: NamadhatuPratyaya.Yak, sutra: '3.1.27',
    meaning: 'itches / scratches (kaṇḍūyati)', pada: Pada.Parasmai, stemSuffix: 'Uya',
  },
  [NamadhatuPratyaya.Aya]: {
    pratyaya: NamadhatuPratyaya.Aya, sutra: '3.1.28',
    meaning: 'protects / heats (gopāyati)', pada: Pada.Parasmai, stemSuffix: 'Aya',
  },
  [NamadhatuPratyaya.IyaN]: {
    pratyaya: NamadhatuPratyaya.IyaN, sutra: '3.1.29',
    meaning: 'pities / reproaches (ṛtīyate)', pada: Pada.Atmane, stemSuffix: 'Iya',
  },
  [NamadhatuPratyaya.KamerNiN]: {
    pratyaya: NamadhatuPratyaya.KamerNiN, sutra: '3.1.30',
    meaning: 'desires (kāmayate)', pada: Pada.Atmane, stemSuffix: 'aya',
  },
};

export interface NamadhatuArgs {
  /** SLP1 prātipadika, e.g. "putra", "Syena". */
  pratipadika: SLP1;
  pratyaya: NamadhatuPratyaya;
  lakara?: Lakara;
  purusha?: Purusha;
  vacana?: Vacana;
  pada?: Pada;
}

const SUTRA_TEXT = new Map(SUTRAS.map(([code, text]) => [code, text]));

function suffixes(pada: Pada, purusha: Purusha, vacana: Vacana): string {
  const tables: Record<Pada, Record<Purusha, [string, string, string]>> = {
    [Pada.Parasmai]: {
      [Purusha.Prathama]: ['ti', 'taH', 'anti'],
      [Purusha.Madhyama]: ['si', 'thaH', 'tha'],
      [Purusha.Uttama]: ['mi', 'vaH', 'maH'],
    },
    [Pada.Atmane]: {
      [Purusha.Prathama]: ['te', 'ete', 'ante'],
      [Purusha.Madhyama]: ['se', 'ethe', 'Dve'],
      [Purusha.Uttama]: ['e', 'vAhe', 'mAhe'],
    },
  };
  const idx = vacana === Vacana.Eka ? 0 : vacana === Vacana.Dvi ? 1 : 2;
  return tables[pada][purusha][idx];
}

function coalesce(stem: SLP1, suffix: SLP1): SLP1 {
  const vowels = 'aAiIuUfFxXeEoO';
  if (stem.endsWith('a') && suffix.length && vowels.includes(suffix[0])) {
    return stem.slice(0, -1) + suffix; // a + vowel → long vowel (6.1.101)
  }
  if (stem.endsWith('A') && suffix.startsWith('a')) {
    return stem + suffix.slice(1); // ā + a → ā (6.1.84)
  }
  if (stem.endsWith('A') && suffix.startsWith('A')) {
    return stem + suffix.slice(1); // ā + ā → ā (ekādeśa)
  }
  return stem + suffix;
}

/** Derive a denominative finite verb (nāmādhatu) from a prātipadika. */
export function deriveNamadhatus(args: NamadhatuArgs): Prakriya[] {
  const info = NAMADHATU_INFO[args.pratyaya];
  const pada = args.pada ?? info.pada;
  const purusha = args.purusha ?? Purusha.Prathama;
  const vacana = args.vacana ?? Vacana.Eka;

  // Bare prātipadika + denominative suffix. After long ā, kyac takes -ya
  // (vidyā + ya → vidyāya), not the -īya used after short-a stems (putrīya).
  let effectiveSuffix = (info.pratyaya === NamadhatuPratyaya.Kyac ||
    info.pratyaya === NamadhatuPratyaya.KyacAcara) &&
    args.pratipadika.endsWith('A') ? 'ya' : info.stemSuffix;
  let base = args.pratipadika;
  // 3.1.27 yak: final u lengthens before the ya vikaraṇa (kaṇḍu → kaṇḍūya).
  if (info.pratyaya === NamadhatuPratyaya.Yak && base.endsWith('u')) {
    base = base.slice(0, -1) + 'U';
    effectiveSuffix = 'ya';
  }
  // 3.1.28 āya: drop the dhātupāṭha anubandha vowel, then guṇa a short u
  // before a final consonant (gupū → gup → gopāya); long vowels stay.
  if (info.pratyaya === NamadhatuPratyaya.Aya) {
    const vowels = 'aAiIuUfFxXeEoO';
    if (vowels.includes(base.slice(-1))) base = base.slice(0, -1);
    if (/u[^aAiIuUfFxXeEoO]$/.test(base)) {
      const i = base.lastIndexOf('u');
      base = base.slice(0, i) + 'o' + base.slice(i + 1);
    }
  }
  // 3.1.29 īyaṅ: final i of the prātipadika merges with ī (ṛti → ṛtīya).
  if (info.pratyaya === NamadhatuPratyaya.IyaN && base.endsWith('i')) {
    base = base.slice(0, -1);
  }
  // 3.1.30 ṇiṅ: drop anubandha, then vṛddhi the last vowel (kama → kam → kām).
  if (info.pratyaya === NamadhatuPratyaya.KamerNiN) {
    const vowels = 'aAiIuUfFxXeEoO';
    if (vowels.includes(base.slice(-1))) base = base.slice(0, -1);
    const vrddhi: Record<string, string> = { a: 'A', i: 'E', I: 'E', u: 'O', U: 'O', f: 'Ar', F: 'Ar' };
    for (let i = base.length - 1; i >= 0; i--) {
      if (vrddhi[base[i]]) { base = base.slice(0, i) + vrddhi[base[i]] + base.slice(i + 1); break; }
    }
  }
  const stem = coalesce(base, effectiveSuffix);
  const suffix = suffixes(pada, purusha, vacana);
  const surface = coalesce(stem, suffix);

  const p = new Prakriya([stem]);
  const text = SUTRA_TEXT.get(info.sutra) ?? '';
  p.record(`${info.sutra} ${text} (${info.pratyaya})`.trim());
  p.record('3.1.32 (sanādyantā dhātavaḥ — denominative stem is a dhātu)');
  p.record(`3.2.123 (${args.lakara ?? Lakara.Lat} vidhāna)`);
  p.record(`3.4.78 (tiṅ: ${suffix})`);
  p.setText(0, surface);
  if (surface !== stem + suffix) p.record('6.1.84 (ekādeśa)');
  p.record('8.2.1 (final consolidation)');
  p.collapse();
  return [p];
}
