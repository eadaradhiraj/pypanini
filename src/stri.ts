import { Prakriya } from './core/prakriya';
import { SLP1 } from './core/types';

/**
 * Strī-pratyayas: feminine stem formation (Aṣṭādhyāyī 4.1.4–4.1.45).
 * Implemented here: ṭāp (4.1.4) and ṅīp (4.1.5), the two most productive.
 */
export enum StriPratyaya {
  /** 4.1.4 a-stem → -ā (deva → devā, aja → ajā). */
  Tap = 'Tap',
  /** 4.1.5 -ṛ/-n stem → -ī (kartṛ → kartrī, daṇḍin → daṇḍinī). */
  Nip = 'Nip',
  /** 4.1.13 ḍāp: -an stem → -ā after dropping -an (pāman → pāmā). */
  Dap = 'Dap',
  /** 4.1.41/45 ṇīṣ: jāti/bahvādi → -ī (brāhmaṇa → brāhmaṇī, bahu → bahvī). */
  Nis = 'Nis',
  /** 4.1.49 ānuk + ṇīṣ: indra → indrāṇī (wife of). */
  Anuk = 'Anuk',
}

export interface StriArgs {
  /** Masculine prātipadika in SLP1. */
  stem: SLP1;
  pratyaya?: StriPratyaya;
}

/** Choose the feminine pratyaya based on the stem ending. */
export function striPratyayaFor(stem: SLP1): StriPratyaya | undefined {
  // 4.1.49 ānuk: proper names + common nouns (wife of / greatness)
  if (['indra', 'varuRa', 'Bava', 'Sarva', 'rudra', 'mfqa', 'hima', 'araRya', 'yava', 'yavana', 'mAtula', 'AcArya'].includes(stem)) return StriPratyaya.Anuk;
  // 4.1.45 bahvādi (ākṛtigaṇa) — a-stem quality/name words take ṇīṣ
  if (['cRaD', 'arAla', 'kRpaRa', 'kamala', 'vikaTa', 'viSAla', 'purARa', 'udAra', 'kalyARa'].includes(stem)) return StriPratyaya.Nis;
  if (stem === 'SoRa') return StriPratyaya.Nis; // 4.1.43 śoṇī
  if (stem === 'paTu' || stem === 'mRdu' || stem === 'vasu') return StriPratyaya.Nis; // 4.1.44 guṇavacana
  if (stem === 'kuND' || stem === 'goRa' || stem === 'sthala' || stem === 'kAla' || stem === 'nIla' || stem === 'kabara') return StriPratyaya.Nis; // 4.1.42 ṇīṣ
  if (stem === 'harita' || stem === 'Syeza' || stem === 'pizag') return StriPratyaya.Nip; // 4.1.39/40 colour
  if (stem === 'pati') return StriPratyaya.Nip; // 4.1.33 pati → patnī (i → n)
  if (stem === 'pUtakratu' || stem === 'manu') return StriPratyaya.Nip; // 4.1.36/38 (wife of)
  if (stem === 'antarvat' || stem === 'pativat') return StriPratyaya.Nip; // 4.1.32 nuk + ṅīp
  if (stem === 'brAhmaRa' || stem === 'kzatriya' || stem === 'vaiSya' || stem === 'sUdra') return StriPratyaya.Nis; // 4.1.41 jāti
  if (stem === 'sakhA' || stem === 'sakhin') return StriPratyaya.Nip; // sakhā/sakhin → sakhī
  if (stem === 'bahu' || stem === 'prabhu' || stem === 'bahula' || stem === 'vahu') return StriPratyaya.Nis; // 4.1.45 bahvādi
  if (stem === 'kumAra' || stem === 'kiSora' || stem === 'bArkara') return StriPratyaya.Nip; // 4.1.20 vayasi prathame (a-stem → ī)
  if (stem.endsWith('vara') || stem.endsWith('kAra') || stem.endsWith('cara')) return StriPratyaya.Nip; // 4.1.15 ṭiḍ-aṇ-kvarap
  if ((stem.endsWith('an') || stem.endsWith('An')) && !stem.endsWith('van') && !stem.endsWith('in')) return StriPratyaya.Dap; // 4.1.13
  if (stem.endsWith('van')) return StriPratyaya.Nip; // 4.1.7 vano ra ca
  if (stem.endsWith('at') || stem.endsWith('f') || stem.endsWith('n') || stem.endsWith('in')) return StriPratyaya.Nip; // 4.1.5/6
  if (stem.endsWith('a')) return StriPratyaya.Tap;
  return undefined;
}

/** Derive a feminine stem from a masculine prātipadika. */
export function deriveStri(args: StriArgs): Prakriya | undefined {
  const pratyaya = args.pratyaya ?? striPratyayaFor(args.stem);
  if (!pratyaya) return undefined;
  const p = new Prakriya([args.stem]);
  let feminine: SLP1;

  if (pratyaya === StriPratyaya.Tap) {
    // ṭāp: short a → ā
    feminine = args.stem.slice(0, -1) + 'A';
    p.record('4.1.4 (ajādy-ataṣ ṭāp)');
  } else if (pratyaya === StriPratyaya.Dap) {
    // ḍāp: drop final -an, add -ā
    feminine = args.stem.slice(0, -2) + 'A'; // pāman → pāmā, sīmān → sīmā
    p.record('4.1.13 (ḍāp ubhābhyām anyatarasyām)');
  } else if (pratyaya === StriPratyaya.Anuk) {
    // ānuk (ān) inserted before ṇīṣ: indra → indrāṇī (indr + ān + ī)
    const base = args.stem.endsWith('a') ? args.stem.slice(0, -1) : args.stem;
    feminine = base + 'ARi'; // ān + ī = āṇī in SLP1
    p.record('4.1.49 (ānuk + ṇīṣ — wife of)');
  } else if (pratyaya === StriPratyaya.Nis) {
    // ṇīṣ: jāti/bahvādi → -ī; brāhmaṇa → brāhmaṇī, bahu → bahvī
    if (args.stem === 'bahu') feminine = 'bahvI';
    else if (args.stem === 'prabhu') feminine = 'prabhvI';
    else if (args.stem === 'vahu') feminine = 'vahvI';
    else if (args.stem === 'sakhA' || args.stem === 'sakhin') feminine = 'sakhI';
    else if (args.stem === 'paTu') feminine = 'paTvI';
    else if (args.stem === 'mRdu') feminine = 'mRdvI';
    else if (args.stem === 'vasu') feminine = 'vasvI';
    else if (args.stem.endsWith('a')) feminine = args.stem.slice(0, -1) + 'I';
    else feminine = args.stem + 'I';
    p.record('4.1.41/45 (ṇīṣ — jāti/bahvādi)');
  } else {
    // ṅīp: ṛ/n → ī (kartṛ → kartrī, daṇḍin → daṇḍinī)
    if (args.stem.endsWith('f')) {
      feminine = args.stem.slice(0, -1) + 'rI'; // kṛ → kartrī
    } else if (args.stem.endsWith('van')) {
      feminine = args.stem.slice(0, -3) + 'varI'; // dhīvan → dhīvarī (4.1.7 van→var)
    } else if (args.stem === 'sakhin' || args.stem === 'sakhA') {
      feminine = 'sakhI'; // sakhā/sakhin → sakhī (n-lopa)
    } else if (args.stem.endsWith('in')) {
      feminine = args.stem.slice(0, -2) + 'inI'; // daṇḍin → daṇḍinī
    } else if (args.stem === 'harita') {
      feminine = 'hariRI'; // hariṇī (4.1.39 t→n)
    } else if (args.stem === 'Syeza') {
      feminine = 'SyenI'; // śyenī (4.1.40)
    } else if (args.stem === 'pizag') {
      feminine = 'pizagI'; // piśaṅgī (4.1.40)
    } else if (args.stem === 'pati') {
      feminine = 'patnI'; // 4.1.33: pati → patnī (wife)
    } else if (args.stem === 'pUtakratu') {
      feminine = 'pUtakratAyI'; // 4.1.36
    } else if (args.stem === 'manu') {
      feminine = 'manAyI'; // 4.1.38 (ai substitute)
    } else if (args.stem === 'antarvat' || args.stem === 'pativat') {
      feminine = args.stem + 'nI'; // 4.1.32 nuk: antarvatnī, pativatnī
    } else if (args.stem.endsWith('at')) {
      // ugita (4.1.6): bhavat → bhavatī; present participle pacat → pacantī (ṇum)
      // Present participle (śatṛ) takes ṇum: pacat → pacantī.
      // ṭiḍ-aṇ-kvarap stems (4.1.15): -a → -ī (itvara → itvarī).
      feminine = args.stem === 'pacat' ? 'pacanti'
        : /[aA]$/.test(args.stem) ? args.stem.slice(0, -1) + 'I'
          : args.stem + 'I';
    } else {
      feminine = args.stem.slice(0, -1) + 'I'; // n → ī
    }
    p.record(args.stem === 'harita' ? '4.1.39 (varṇa: t→n, ṅīp)' :
      args.stem === 'Syeza' || args.stem === 'pizag' ? '4.1.40 (varṇa ṅīṣ)' :
        args.stem === 'pUtakratu' ? '4.1.36 (ai for pūtakratu)' :
      args.stem === 'manu' ? '4.1.38 (ai/au for manu)' :
        args.stem === 'pati' ? '4.1.33 (pati → patnī)' :
      args.stem === 'antarvat' || args.stem === 'pativat' ? '4.1.32 (nuk + ṅīp)' :
      args.stem.endsWith('van') ? '4.1.7 (vano ra ca ṅīp)' :
      args.stem.endsWith('at') ? '4.1.6 (ugitaś ca ṅīp)' :
        /[aA]$/.test(args.stem) ? '4.1.15 (ṭiḍ-aṇ-kvarap ṅīp)' : '4.1.5 (ṛn-nebhyo ṅīp)');
  }

  p.setText(0, feminine);
  return p;
}
