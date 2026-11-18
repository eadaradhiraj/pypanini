import { Prakriya } from './core/prakriya';
import { gunafy, vrddhify, applyNatva } from './core/slp1';
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
    pratyaya: 'anīyar', code: '3.1.95 (kṛtyāḥ), 3.1.96 (tavyattavyānīyaraḥ)',
  },
  [Krt.Tum]: {
    suffix: 'tum', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'tumun', code: '3.3.10 (tumun-ṇvulau)',
  },
  [Krt.Tavya]: {
    suffix: 'tavya', grade: 'guna', prayoga: Prayoga.Karmani,
    pratyaya: 'tavyat', code: '3.1.95 (kṛtyāḥ), 3.1.96 (tavyattavyānīyaraḥ), 7.2.10 (no iṭ for kṛ)',
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
    pratyaya: 'yat', code: '3.1.95 (kṛtyāḥ), 3.1.97 (aco yat)',
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
    suffix: 'a', grade: 'vrddhi', prayoga: Prayoga.Karmani,
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
    suffix: 'zRu', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kṣnu', code: '3.2.139 (glā-ji-sthaś ca kṣnuḥ)',
  },
  [Krt.izNuc]: {
    suffix: 'izRu', grade: 'guna', prayoga: Prayoga.Kartari,
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
  [Krt.aN]: {
    suffix: 'A', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'aṇ', code: '3.3.12 (aṇ karmaṇi ca), 3.3.105 (cinti-pūji-kathi-kumbi-carcaś ca)',
  },
  [Krt.gaNa]: {
    suffix: 'a', grade: 'vrddhi', prayoga: Prayoga.Karmani,
    pratyaya: 'ghañ', code: '3.3.18 (bhāve ghañ — action noun)',
  },
  [Krt.ap]: {
    suffix: 'a', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'ap', code: '3.3.61/62 (svana-hasor vā — ap)',
  },
  [Krt.kaN]: {
    suffix: 'za', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kañ', code: "3.2.60 (tyadādiṣu dṛśo 'nālocane kañ)",
  },
  [Krt.kvin]: {
    suffix: '', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'kvin', code: '3.2.59 (ṛtvig-dadhṛk-srag-dig-uṣṇig… kvin)',
  },
  [Krt.khuKN]: {
    suffix: 'uka', grade: 'guna', prayoga: Prayoga.Kartari,
    pratyaya: 'khukañ', code: '3.2.57 (kartari bhuvaḥ khiṣṇuc-khukañau)',
  },
  [Krt.khyun]: {
    suffix: 'aRa', grade: 'none', prayoga: Prayoga.Karmani,
    pratyaya: 'khyun', code: '3.2.56 (kṛñaḥ karaṇe khyun)',
  },
  [Krt.kiN]: {
    suffix: 'i', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ki/kin', code: '3.2.171 (ād-ṛ-gama-hana-janaḥ ki-kinau liṭ ca)',
  },
  [Krt.najiN]: {
    suffix: 'na', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'najiṅ', code: '3.2.172 (svapitṛṣornajiṅ)',
  },
  [Krt.ac]: {
    suffix: 'a', grade: 'none', prayoga: Prayoga.Bhave,
    pratyaya: 'ac', code: '3.3.56 (er ac — action noun after i/ī-final roots)',
  },
  [Krt.naN]: {
    suffix: 'na', grade: 'none', prayoga: Prayoga.Bhave,
    pratyaya: 'ṇa', code: '3.3.90 (yajayācayataviccha... ṇa)',
  },
  [Krt.Nvanip]: {
    suffix: 'van', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ṅvanip', code: '3.2.103 (suyajor ṅvanip)',
  },
  [Krt.atRn]: {
    suffix: 'at', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'atṛn', code: '3.2.104 (jīryater atṛn)',
  },
  [Krt.NyuT]: {
    suffix: 'ana', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ṇyuṭ', code: '3.1.147 (ṇyuṭ ca — gāyana)',
  },
  [Krt.thakan]: {
    suffix: 'Taka', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'thakan', code: '3.1.146 (gāḥ thakan — gāthaka)',
  },
  [Krt.Svun]: {
    suffix: 'aka', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ṣvun', code: '3.1.145 (śilpini ṣvun)',
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
  dfSir: 'dfk', // dṛś → dṛk (3.2.94 dṛśeḥ kvanip)
  sad: 'sat',   // sat (3.2.61 satsu kvip)
  vid: 'vit',   // vit (3.2.61)
  BAs: 'BAs',   // bhās → bhāḥ (3.2.177)
  BrAj: 'BrAj', // bhrāj → vibhrāj (3.2.177)
  dhurv: 'dhur', // dhūḥ (3.2.177)
  ppF: 'pUr',   // pūḥ (3.2.177)
  ju: 'jU',     // jūḥ (3.2.177)
};

/** kvin (3.2.59): irregular zero-suffix agent nouns. */
const KVIN_FORMS: Record<string, string> = {
  ftu: 'ftvik',  // ṛtvik
  DFz: 'dadfzk', // dadhṛk
  sfj: 'srak',   // srak
  dfS: 'dik',    // dik (√diś)
  yuj: 'yuj',    // yuj
  spfS: 'spfk',  // spṛk (3.2.58 spṛśo'nudake kvin)
  dviS: 'dviT',  // dviṭ (3.2.61)
  druh: 'druk',  // druk (3.2.61)
  duh: 'duk',    // duk (3.2.61)
  Bid: 'Bit',    // bhit (3.2.61)
  Cid: 'Cit',    // chit (3.2.61)
};

/** ṣṭran (3.2.182) stems: the suffix is -tra on these roots (guṇa/vṛddhi varies). */
const STRAN_STEMS: Record<string, string> = {
  dA: 'dA',    // dātra (sickle)
  ni: 'ne',    // netra (eye)
  stu: 'sto',  // stotra (praise)
  yu: 'yo',    // yotra
  dhA: 'dA',   // dhātra (nurse, 3.2.181)
  hu: 'ho',    // hotra (oblation, 3.2.182)
};

/** Stem overrides for roots with an irregular kṛt formation (nipātana). */
/** iṣṇuc (3.2.136/138): per-root stems (guṇa/vṛddhi already applied). */
const IZNU_STEMS: Record<string, string> = {
  BU: 'Bav',    // bhaviṣṇu
  ruc: 'roc',   // rociṣṇu
  saha: 'sah',  // sahiṣṇu
  car: 'car',   // cariṣṇu
  vFt: 'vart',  // vartiṣṇu
  vid: 'ved',   // vediṣṇu
};

const STEM_OVERRIDE: Partial<Record<Krt, Record<string, string>>> = {
  [Krt.Satr]: { kf: 'kurv', nI: 'nay' }, // kṛ → kurvat, nī → nayat
  [Krt.SanaC]: { kf: 'kurv', nI: 'nay' }, // kṛ → kurvāṇa, nī → nayamāna
  [Krt.Sanan]: { pU: 'pav', yaj: 'yaj', BU: 'Bav', kf: 'kurv' }, // kṛ→kurvāṇa, bhū→bhavamāna, pū→pavamāna
  [Krt.STran]: STRAN_STEMS, // dātra, netra, stotra, yotra
  [Krt.TRn]: { hu: 'ho', ni: 'neS', tviz: 'tvaS', gam: 'gan', vid: 'vet' }, // hotṛ, neṣṭṛ, tvaṣṭṛ, gantṛ, vettṛ
  [Krt.Kyap]: { vid: 'vid', man: 'man', i: 'it', zi: 'zay' }, // vidyā, manyā, ityā, śayyā
  [Krt.Sa]: { kf: 'kriy', iz: 'icC' }, // kriyā (3.3.100), icchā (3.3.101)
  [Krt.Nini]: { pac: 'pAc', yaj: 'yAj', gam: 'gAm', BU: 'BAv', vid: 'ved', diS: 'dez', car: 'cAr', nI: 'nAy' }, // ṇini vṛddhi
  [Krt.Nvul]: { pac: 'pAc', yaj: 'yAj', dA: 'dAy', vaha: 'vAh', nI: 'nAy' }, // pācaka, yājaka, dāyaka, vāhaka, nāyaka
  [Krt.ac]: { ci: 'cay', i: 'ay', ji: 'jay', kzi: 'kzay', sf: 'sar', nI: 'nay' }, // caya, aya, jaya, kṣaya, naya (3.3.56)
  [Krt.naN]: { yaj: 'yajY', yAc: 'yAcY' }, // yajña, yācñā (jñ/ñ)
  [Krt.kSnu]: { vid: 'ved' }, // vediṣṇu (guṇa before ṣṇu)
  [Krt.Nvanip]: { su: 'sut', yaj: 'yaj' }, // sutvan, yajvan (ṭuk 6.1.71)
  [Krt.atRn]: { jF: 'jar', jf: 'jar' },    // jarant (3.2.104)
  [Krt.NyuT]: { gAI: 'gAy' },              // gāyana (3.1.147)
  [Krt.thakan]: { gAI: 'gA' },             // gāthaka (3.1.146)
  [Krt.Svun]: { nft: 'nart', khan: 'khan', raYj: 'raj' }, // nartaka/khanaka/rajaka
  [Krt.Ani]: { ni: 'nay', nI: 'nay', dviza: 'dvez', vid: 'ved' },  // vedanīya
  [Krt.Ktin]: { av: 'U', yu: 'yU', ju: 'jU', san: 'sA', han: 'he', gam: 'ga', yuj: 'yuk', rudh: 'rudD', bhid: 'bhitT', Cid: 'CitT', vid: 'vit' }, // yukti/ruddhi/bhitti/chitti/vitti
  [Krt.KtvA]: { gam: 'ga', dA: 'dat', bhid: 'bhit', Cid: 'Cit', rudh: 'rudD', yuj: 'yuk', vid: 'vit', ciY: 'city', mIY: 'mI', gA: 'gIt' }, // vittvā, citytvā, mītvā, gītvā
  [Krt.LyuT]: { vid: 'ved', diS: 'dez', nI: 'nay', dviza: 'dvez' }, // dveṣaṇa
  [Krt.Tum]: { gam: 'gan', bhid: 'bhet', Cid: 'Chet', rudh: 'roDD', yuj: 'yok', vid: 'vet' }, // vettum
  [Krt.Tfc]: { gam: 'gan', mfj: 'mArz', hu: 'ho', vid: 'vet', bhid: 'bhet', Cid: 'Chet', rudh: 'roDD', yuj: 'yok' }, // bhettṛ, chettṛ, roddhṛ, yoktṛ
  [Krt.Tac]: { gam: 'ga', dA: 'dat', mid: 'minn', bhid: 'bhin', Cid: 'chin', rudh: 'rudD', yuj: 'yuk', dviza: 'dviz', gA: 'gIt', duha: 'dugD' },  // dugdha
  [Krt.Tavya]: { gam: 'gan', bhid: 'bhet', Cid: 'Chet', yuj: 'yok', vid: 'vet' },// vettavya
  [Krt.Ktavatu]: { gam: 'gan', dA: 'dat', bhid: 'bhet', Cid: 'Chet', yuj: 'yok', vid: 'vet', rudh: 'roDD' },// roddhavān
  [Krt.uH]: { Bikz: 'Bikz', AzaMs: 'AzaMs', iz: 'icC' }, // bhikṣu, āśaṃsu (3.2.168), icchu (3.2.169)
  [Krt.ghaH]: { CAd: 'Cad', pac: 'pAk', tyj: 'tyAj', raj: 'rAj', tyaj: 'tyAg', rAj: 'rAg', yuj: 'yoj', BU: 'BAv', car: 'cAr', ji: 'jay', vid: 'ved', nam: 'nAm', nI: 'nay' }, // pāka, tyāga, rāga, yoga, bhāva, cāra, jaya, veda, nāma, naya
  [Krt.raH]: { nam: 'nam', dIp: 'dIp', kamp: 'kamp', smi: 'sme', hiMs: 'hiMs' }, // namra, dīpra…
  [Krt.kru]: { Bi: 'Bi' }, // bhīru (3.2.174)
  [Krt.AruH]: { vand: 'vand', sF: 'sar' }, // vandāru, śarāru (3.2.173)
  [Krt.varac]: { sTA: 'sTA', IS: 'IS' }, // sthāvara, īśvara (3.2.175)
  [Krt.Du]: { viBU: 'viB', praBU: 'praB', samBU: 'samB' }, // vibhu/prabhu/sambhu (3.2.180)
  [Krt.knu]: { tras: 'tras', gFDi: 'gFd', DFzi: 'DFz', kzip: 'kziN' }, // trasnu/gṛdhnu/dhṛṣṇu/kṣiṇṇu
  [Krt.izNuc]: IZNU_STEMS, // bhaviṣṇu/rociṣṇu/sahiṣṇu/… (3.2.136/138)
  [Krt.yuc]: { cal: 'cal', Sabd: 'Sabd', rav: 'rav', COP: 'Cop', kruD: 'kroD', maND: 'maND', As: 'As', vid: 'ved' }, // +ana → calana/krodhana/āsanā/vedanā
  [Krt.ruH2]: { dA: 'dA', si: 'sa', sad: 'sad', saD: 'saD' }, // +ru → dāru/saru/sadru
  [Krt.kurac]: { vid: 'vid', Bid: 'Bid', cid: 'cid', vyD: 'viD' }, // +ura → vidura/bhidura/chidura/vidhura
  [Krt.ghurac]: { baNj: 'baNg', BAs: 'BAs', mid: 'med' }, // +ura → bhaṅgura/bhāsura/medura
  [Krt.kvarap]: { iR: 'it', i: 'it', naS: 'naS', ji: 'jit', sf: 'sf' }, // +vara → itvara/naśvara/jitvara/sṛvara (6.1.71 ṭuk)
  [Krt.ghinuN]: {
    vikaS: 'vikAS', vilas: 'vilAs', pralap: 'pralAp', pradru: 'pradrAv', pravas: 'pravAs',
    duz: 'doz', dviS: 'dvez', yuj: 'yog', tyaj: 'tyAg', raj: 'rAg', Baj: 'BAG',
    Sram: 'SrAm', Bram: 'BrAm', klam: 'klAm',ksam: 'kzAm', tyag: 'tyAg',
  }, // +I → vikāṣī/vilāsī/doṣī/dveṣī/yogī/tyāgī/…
  [Krt.cAnaS]: { buJ: 'buJj', biF: 'bibR', muND: 'muND', Buz: 'BuZ' }, // +Ana → bhuñjāna/bibhrāṇa
  [Krt.aN]: { cint: 'cint', pUj: 'pUj', kath: 'kath', kumb: 'kumb', carc: 'carc', bhid: 'bhed' }, // cintā/pūjā; bheda (3.3.104)
  [Krt.gaNa]: { pac: 'pAk', tyaj: 'tyAg', rAj: 'rAg', bId: 'bEd', bif: 'bEd', yuj: 'yoj', BU: 'BAv', car: 'cAr', ji: 'jay', vid: 'ved', nam: 'nAm', nI: 'nay' }, // ghañ vṛddhi
  [Krt.ap]: { svan: 'svAn', has: 'hAs', kf: 'kar', gF: 'gar', sf: 'sar', yu: 'yav', lU: 'lav', pU: 'pav' }, // 3.3.57 kara/śara/yava/lava/pava
  [Krt.kaN]: { tad: 'tAdf', yad: 'yAdf', sa: 'sadf', anya: 'anyAdf' }, // +za → tādṛśa/yādṛśa/sadṛśa
  [Krt.khuKN]: { BU: 'bAv' }, // +uka → bhāvuka
  [Krt.khyun]: { kf: 'kar', BU: 'Bav' }, // karaRa (karaṇa), BavaRa (bhavaṇa)
  [Krt.kiN]: { dA: 'dad', kf: 'cakr', sf: 'sasr', gam: 'jagm', nam: 'nem' }, // +i → dadiH/cakriH/…
  [Krt.najiN]: { svap: 'svap', tfza: 'tfz', Dfza: 'Dfz' }, // +na → svapna / tṛṣṇa / dhṛṣṇa
};

const KSNU_SUFFIX: Record<string, string> = {
  glA: 'snu', // glāsnu
  ji: 'zRu',  // jiṣṇu
  sTA: 'snu', // sthāsnu
  BU: 'zRu',  // bhūṣṇu
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
    p.record(dhatu.text === 'dfSir' ? '3.2.94 (dṛśeḥ kvanip — kvip)' :
      ['BAs', 'BrAj', 'dyut'].includes(dhatu.text)
        ? '3.2.177 (bhrājādiṣu kvip)'
        : "3.2.178 (anyebhyo 'pi dṛśyate — kvip)");
    if (form) p.insert(0, form, ['krt']);
    else p.insert(0, dhatu.text, ['krt']);
    p.collapse();
    return [p];
  }
  // kvin (3.2.59): irregular zero-suffix agent nouns.
  if (args.krt === Krt.kvin) {
    const form = KVIN_FORMS[dhatu.text] ?? dhatu.text;
    const p = new Prakriya([]);
    p.record('3.2.59 (kvin — irregular agent nouns)');
    p.insert(0, form, ['krt']);
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
  if (args.krt === Krt.naN && dhatu.text === 'yaj') spec.suffix = 'a'; // yajY + a → yajña
  if (args.krt === Krt.Tac && dhatu.text === 'mid') spec.suffix = 'a'; // minn + a → minna (3.2.187)
  if (args.krt === Krt.Tac && ['bhid', 'Cid'].includes(dhatu.text)) spec.suffix = 'na'; // bhin+na → bhinna
  if (args.krt === Krt.Tac && dhatu.text === 'rudh') spec.suffix = 'a'; // rudD+a → ruddha
  if (args.krt === Krt.Tum && dhatu.text === 'rudh') spec.suffix = 'um'; // roDD+um → roddhum
  if (args.krt === Krt.Tfc && dhatu.text === 'rudh') spec.suffix = 'f'; // roDD+f → roddhṛ
  if (args.krt === Krt.Ktavatu && dhatu.text === 'rudh') spec.suffix = 'avAn'; // roddhavān
  if (args.krt === Krt.Tac && dhatu.text === 'dviza') spec.suffix = 'wa'; // dviz+wa → dviṣṭa
  if (args.krt === Krt.KtvA && dhatu.text === 'rudh') spec.suffix = 'vA'; // rudD+vA → ruddhvā
  if (args.krt === Krt.Ktin && ['rudh', 'bhid', 'Cid'].includes(dhatu.text)) spec.suffix = 'i'; // ruddhi/bhitti/chitti
  if (args.krt === Krt.Tac && dhatu.text === 'gA') spec.suffix = 'a'; // gIt+a → gīta
  if (args.krt === Krt.KtvA && dhatu.text === 'gA') spec.suffix = 'vA'; // gIt+vA → gītvā
  if (args.krt === Krt.naN && dhatu.text === 'yAc') spec.suffix = 'A'; // yācñā (fem.)
  if (args.krt === Krt.aN && dhatu.text === 'bhid') { spec.suffix = 'a'; spec.code = '3.3.104 (śid-bhidādiṣv aṇ)'; } // bheda
  if (args.krt === Krt.Yat) spec.grade = rFinal ? 'vrddhi' : 'guna';
  if (args.krt === Krt.kSnu && KSNU_SUFFIX[dhatu.text]) spec.suffix = KSNU_SUFFIX[dhatu.text];
  if (args.krt === Krt.SanaC && rFinal) spec.suffix = 'ARa'; // kṛ → kurvāṇa
  if (args.krt === Krt.Sanan) spec.infix = 'a'; // pava/yaja + māna (thematic a)
  if (args.krt === Krt.Sanan && dhatu.text === 'kf') { spec.suffix = 'ARa'; spec.infix = ''; } // kṛ → kurvāṇa
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

  // 8.2.36 (vraśca-bhrasja-sṛja-mṛja-yaja-rāja-bhrāja-ccha-śāṃ ṣaḥ): these
  // roots (and any ś-final root) take ṣ before a jhal kṛt suffix, overriding
  // 8.2.30. Then 8.4.41 (ṣṭunā ṣṭuḥ) makes a following dental t → ṭ (ṣṭ).
  const SATVA_ROOTS = new Set(['vraSc', 'Brasz', 'sfj', 'mfj', 'mFj', 'mrf', 'yaj', 'rAj', 'BrAj', 'praC', 'liS', 'viS']);
  if (spec.suffix.length > 0 && /[kKgGcCjJYtTdDn pPbBm]/.test(spec.suffix[0])) {
    const lastIdx = p.length - 1;
    const tail = p.textAt(lastIdx); // the root is the last term (suffix not yet inserted)
    const c = tail.slice(-1);
    if (SATVA_ROOTS.has(tail) || c === 'S') {
      p.setText(lastIdx, tail.slice(0, -1) + 'z'); // → ṣ
      p.record('8.2.36 (j/ś → ṣ before jhal suffix)');
    } else {
      // 8.2.30 (coḥ kuḥ): a final palatal becomes its guttural before a jhal suffix.
      const palatalToGuttural: Record<string, string> = {
        c: 'k', j: 'g', C: 'K', J: 'G', Y: 'N',
      };
      if (palatalToGuttural[c]) {
        p.setText(lastIdx, tail.slice(0, -1) + palatalToGuttural[c]);
        p.record('8.2.30 (jhalo jhali: palatal → guttural)');
      }
    }
    // 8.4.41 ṣṭunā ṣṭuḥ: a dental t starting the suffix → ṭ (w) after ṣ
    if (p.textAt(lastIdx).endsWith('z') && spec.suffix.startsWith('t')) {
      spec.suffix = 'w' + spec.suffix.slice(1);
      p.record('8.4.41 (ṣṭunā ṣṭuḥ: t → ṭ after ṣ)');
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

  // 6.1.84 ekādeśa: ā + a → ā (dā + anīya → dānīya).
  if (p.textAt(p.length - 1).endsWith('A') && spec.suffix.startsWith('a')) {
    spec.suffix = spec.suffix.slice(1); // ā + a → ā (single long vowel)
    p.record('6.1.84 (ekādeśa: ā + a → ā)');
  }
  if (p.textAt(p.length - 1).endsWith('a') && spec.suffix.startsWith('a')) {
    spec.suffix = spec.suffix.slice(1); // a + a → a (6.1.84)
    p.record('6.1.84 (ekādeśa: a + a → a)');
  }
  p.insert(p.length, spec.suffix, ['krt']);
  p.record(spec.code);

  p.record(`kṛt-prayoga: ${args.prayoga ?? spec.prayoga} (kāraka-vivakṣā)`);
  p.collapse();
  // 6.1.84 ekādeśa for infix boundaries (e.g. eDa + a + mAna → eDamAna).
  const beforeEk = p.terms[0].text;
  while (/(aa|ii|uu|ee|oo|Aa|Ii|Uu)/.test(p.terms[0].text)) {
    p.terms[0].text = p.terms[0].text.replace(/(aa|ii|uu|ee|oo|Aa|Ii|Uu)/g,
      (m) => m[0]); // 6.1.84 ekādeśa: same/heterogeneous vowel pair → single
  }
  if (p.terms[0].text !== beforeEk) {
    p.record('6.1.84 (ekādeśa: vowel + same vowel → single)');
    p.collapse();
  }
  // ṇatva (8.4.1) must see the whole pada: tṛṣ + na → tṛṣṇa.
  const t = p.terms[0];
  const natva = applyNatva(t.text);
  if (natva !== t.text) { t.text = natva; p.record('8.4.1 (ṇatva: n → ṇ after r/ṣ/ṛ)'); }
  return [p];
}
