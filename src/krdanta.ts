import { Prakriya } from './core/prakriya';
import { gunafy, vrddhify, applyNatva, initialNati, initialShatva } from './core/slp1';
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
  [Krt.ka]: {
    suffix: 'a', grade: 'none', prayoga: Prayoga.Kartari,
    pratyaya: 'ka', code: '3.1.135 (igupadhā-jñā-prī-kiraḥ kaḥ)',
  },
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
  dviS: 'dviT', // dviṭ (3.2.61)
  druh: 'druk', // druk (3.2.61)
  duh: 'duk',   // duk (3.2.61)
  Cid: 'Cit',   // chit (3.2.61)
  ji: 'jit',    // jit (3.2.61)
  rAj: 'rAT',   // rāṭ (3.2.61)
  nI: 'nI',     // nīḥ (3.2.61)
  BAs: 'BAs',   // bhās → bhāḥ (3.2.177)
  BrAj: 'BrAj', // bhrāj → vibhrāj (3.2.177)
  dhurv: 'dhur', // dhūḥ (3.2.177)
  ppF: 'pUr',   // pūḥ (3.2.177)
  ju: 'jU',     // jūḥ (3.2.177)
  Sam: 'SAn',  // praśān (8.2.64: mo no dhātoḥ)
  tam: 'tAn',  // pratān (8.2.64)
  dam: 'dAn',  // pradān (8.2.64)
  naS: 'nak',  // jīvanak (8.2.63 naśer vā)
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
  [Krt.Satr]: { kf: 'kurv', nI: 'nay', vid: 'vidvas', as: 'sat', SAsu: 'SAs', rudh: 'rundh', yuj: 'yuNY', bhid: 'bhinD', Cid: 'CinD', dA: 'dad', DA: 'daD', i: 'y' }, // śatṛ present participles (dadat/dadhat)
  [Krt.SanaC]: { kf: 'kurv', nI: 'nay' }, // kṛ → kurvāṇa, nī → nayamāna
  [Krt.Sanan]: { pU: 'pav', yaj: 'yaj', BU: 'Bav', kf: 'kurv' }, // kṛ→kurvāṇa, bhū→bhavamāna, pū→pavamāna
  [Krt.STran]: STRAN_STEMS, // dātra, netra, stotra, yotra
  [Krt.TRn]: { hu: 'ho', ni: 'neS', tviz: 'tvaS', gam: 'gan', vid: 'vet' }, // hotṛ, neṣṭṛ, tvaṣṭṛ, gantṛ, vettṛ
  [Krt.Kyap]: { vid: 'vid', man: 'man', i: 'it', zi: 'zay', vraja: 'vraj', yaja: 'yaj', khan: 'khe' }, // kheya (3.1.111)
  [Krt.Sa]: { kf: 'kriy', iz: 'icC' }, // kriyā (3.3.100), icchā (3.3.101)
  [Krt.Nini]: { pac: 'pAc', yaj: 'yAj', gam: 'gAm', BU: 'BAv', vid: 'ved', diS: 'dez', car: 'cAr', nI: 'nAy', grah: 'grAh', gfhm: 'grAh' }, // ṇini vṛddhi (3.1.134 grahādi)
  [Krt.Nvul]: { pac: 'pAc', yaj: 'yAj', dA: 'dAy', vaha: 'vAh', nI: 'nAy' }, // pācaka, yājaka, dāyaka, vāhaka, nāyaka
  [Krt.ac]: { ci: 'cay', i: 'ay', ji: 'jay', kzi: 'kzay', sf: 'sar', nI: 'nay' }, // caya, aya, jaya, kṣaya, naya (3.3.56)
  [Krt.naN]: { yaj: 'yajY', yAc: 'yAcY' }, // yajña, yācñā (jñ/ñ)
  [Krt.kSnu]: { vid: 'ved' }, // vediṣṇu (guṇa before ṣṇu)
  [Krt.Nvanip]: { su: 'sut', yaj: 'yaj' }, // sutvan, yajvan (ṭuk 6.1.71)
  [Krt.atRn]: { jF: 'jar', jf: 'jar' },    // jarant (3.2.104)
  [Krt.NyuT]: { gAI: 'gAy' },              // gāyana (3.1.147)
  [Krt.thakan]: { gAI: 'gA' },             // gāthaka (3.1.146)
  [Krt.Yat]: { gada: 'gad', mada: 'mad', cara: 'car', yama: 'yam', yam: 'yam', f: 'ar', i: 'it', stu: 'stut', SAsu: 'Siz', vR: 'vRt', juza: 'juz', fR: 'adfRt', dA: 'de', DA: 'dhe', hA: 'he', stA: 'ste', kzi: 'kzay', ji: 'jay', kri: 'kray' }, // kṣayya/jayya/krayya (6.1.81/82)
  [Krt.ka]: { jYA: 'jY', prIY: 'priy', kF: 'kir' }, // jña (6.4.64), priya (prī+ka 6.1.77), kira (kṝ→kir)
  [Krt.Svun]: { nft: 'nart', khan: 'khan', raYj: 'raj' }, // nartaka/khanaka/rajaka
  [Krt.Ani]: { ni: 'nay', nI: 'nay', dviza: 'dvez', vid: 'ved' },  // vedanīya
  [Krt.Ktin]: { av: 'U', yu: 'yU', ju: 'jU', san: 'sA', han: 'he', gam: 'ga', yuj: 'yuk', rudh: 'rudD', bhid: 'bhitT', Cid: 'CitT', vid: 'vit', muR: 'mUr', mUrcC: 'mUr', tUrva: 'tUr', Durva: 'dUr', man: 'ma', mana: 'ma', ram: 'ra', rama: 'ra', yam: 'ya', yama: 'ya', nam: 'na', tan: 'ta', van: 'va', kF: 'kIr' }, // mūrti/tūrti (6.4.21); mati/rati (6.4.37); kīrti (3.3.97)
  [Krt.KtvA]: { gam: 'ga', dA: 'dat', bhid: 'bhit', Cid: 'Cit', rudh: 'rudD', yuj: 'yuk', vid: 'vit', ciY: 'city', mIY: 'mI', gA: 'gIt', SAsu: 'Sizw', Brasz: 'Barz', brU: 'uk', cakz: 'AKyA', Sam: 'Sami', tam: 'tami', dam: 'dami', nah: 'nadD', laB: 'labD', vach: 'vak', vacha: 'vak', han: 'ha', car: 'cari', cara: 'cari', arh: 'arhi', arha: 'arhi', rama: 'ra', ram: 'ra', vasu: 'uSi', vas: 'uSi', Svap: 'sup', svapa: 'sup', vada: 'vadi' }, // vaktvā (8.2.30); hatvā (6.4.37); caritvā (7.2.35); arhitvā/ratvā/uṣitvā/suptvā
  [Krt.LyuT]: { vid: 'ved', diS: 'dez', nI: 'nay', dviza: 'dvez' }, // dveṣaṇa
  [Krt.Tum]: { gam: 'gan', bhid: 'bhet', Cid: 'Chet', rudh: 'roDD', yuj: 'yok', vid: 'vet', SAsu: 'SAs', Brasz: 'Barz', brU: 'vak', cakz: 'AKyA', as: 'Bavi', grah: 'grahI', vf: 'varI', nah: 'nadD', laB: 'labD', dah: 'dagD', vach: 'vak', vacha: 'vak', arh: 'arhi', arha: 'arhi', vada: 'vadi' }, // vaktum (8.2.30); arhitum (7.2.35)
  [Krt.Tfc]: { gam: 'gan', mfj: 'mArz', hu: 'ho', vid: 'vet', bhid: 'bhet', Cid: 'Chet', rudh: 'roDD', yuj: 'yok', Brasz: 'Barz', brU: 'vak', cakz: 'AKyA', as: 'Bavi', grah: 'grahI', vf: 'varI', laB: 'labD', iZ: 'ez', luB: 'lobD', ruS: 'roz', riS: 'rez', vach: 'vak', vacha: 'vak', arh: 'arhi', arha: 'arhi', vada: 'vadi' }, // vaktṛ (8.2.30); arhitṛ (7.2.35)
  [Krt.Tac]: { gam: 'ga', dA: 'dat', mid: 'minn', bhid: 'bhin', Cid: 'chin', rudh: 'rudD', yuj: 'yuk', dviza: 'dviz', gA: 'gIt', duha: 'dugD', lUY: 'lU', pUY: 'pU', jyA: 'jI', kF: 'kIr', gF: 'gIr', SF: 'SIr', sf: 'SIrR', stf: 'stIrR', gf: 'gIrR', pac: 'pakv', kzi: 'kzAm', vid: 'vitt', nud: 'nun', trA: 'trA', ghrA: 'ghrA', hrI: 'hrI', uza: 'un', pF: 'pUr', mUrcC: 'mUr', mada: 'mat', mad: 'mat', sraMs: 'sras', DvaMs: 'Dvas', SAsu: 'Siz', jan: 'jA', san: 'sA', khan: 'khA', Brasz: 'Barz', brU: 'uk', cakz: 'AKyA', kziBid: 'kzviR', buDa: 'budD', jYA: 'jYA', pUza: 'pUj', iza: 'iz', vaca: 'uk', svap: 'sup', yaj: 'iz', vap: 'up', vas: 'Uz', vada: 'ud', nah: 'nadD', laB: 'labD', dah: 'dagD', ama: 'ami', am: 'ami', ruza: 'ruzi', vach: 'vak', vacha: 'vak', mIY: 'mI', prIY: 'prI', SrIY: 'SrI', RIY: 'RI', qukrIY: 'qukrI', kfpa: 'klfp', kfp: 'klfp', han: 'ha', DA: 'hi', tana: 'ta', tanu: 'ta', tan: 'ta', vana: 'va', van: 'va', yama: 'ya', yam: 'ya', rama: 'ra', ram: 'ra', nama: 'na', nam: 'na', mana: 'ma', man: 'ma', arh: 'arhi', arha: 'arhi', cara: 'car', jIv: 'jIvi', jIva: 'jIvi', cint: 'cinti', pUj: 'pUji', sev: 'sevi', seva: 'sevi', BAs: 'BAsi' },  // vakta (8.2.30); mīna/prīṇa (8.2.45); klṛpta (8.2.18); hata (6.4.37); hita (√dhā); tanādi n-lopa (6.4.37); arhita/carita (7.2.35)
  [Krt.Tavya]: { gam: 'gan', bhid: 'bhet', Cid: 'Chet', yuj: 'yok', vid: 'vet', brU: 'vak', cakz: 'AKyA', as: 'Bavi', grah: 'grahI', vf: 'varI', nah: 'nadD', laB: 'labD', dah: 'dagD', vach: 'vak', vacha: 'vak', rudh: 'roDD', arh: 'arhi', arha: 'arhi', vada: 'vadi' },// vaktavyam (8.2.30); roddhavyam (√rudh); arhitavyam (7.2.35)
  [Krt.Ktavatu]: { gam: 'gan', dA: 'dat', bhid: 'bhet', Cid: 'Chet', yuj: 'yok', vid: 'vit', rudh: 'roDD', pac: 'pakv', sf: 'SIrR', stf: 'stIrR', gf: 'gIrR', kF: 'kIrR', gF: 'gIrR', SF: 'SIrR', nud: 'nunn', trA: 'trAR', ghrA: 'ghrAR', hrI: 'hIR', uza: 'unn', pF: 'pUr', mUrcC: 'mUr', mada: 'mat', mad: 'mat', grah: 'grahI', vf: 'varI', laB: 'labD', car: 'cari', cara: 'cari', han: 'ha', arh: 'arhi', arha: 'arhi', vada: 'vadi' },// labdhavān (8.4.53); caritavān/hatavān
  [Krt.uH]: { Bikz: 'Bikz', AzaMs: 'AzaMs', iz: 'icC' }, // bhikṣu, āśaṃsu (3.2.168), icchu (3.2.169)
  [Krt.ghaH]: { CAd: 'Cad', pac: 'pAk', tyj: 'tyAj', raj: 'rAj', tyaj: 'tyAg', rAj: 'rAg', yuj: 'yoj', BU: 'BAv', car: 'cAr', ji: 'jay', vid: 'ved', nam: 'nAm', nI: 'nay', likh: 'lek', viS: 'vez', mfj: 'mArg', ram: 'rAm', pad: 'pAd', ruj: 'rog', spfS: 'sparS', syand: 'syad', indh: 'eD', ad: 'GAs' }, // ghāsa (2.4.38 ghañ-apoś ca)
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
  [Krt.gaNa]: { pac: 'pAk', tyaj: 'tyAg', rAj: 'rAg', bId: 'bEd', bif: 'bEd', yuj: 'yoj', BU: 'BAv', car: 'cAr', ji: 'jay', vid: 'ved', nam: 'nAm', nI: 'nay', yaj: 'yAg' }, // yāga (3.3.18)
  [Krt.ap]: { svan: 'svAn', has: 'hAs', kf: 'kar', gF: 'gar', sf: 'sar', yu: 'yav', lU: 'lav', pU: 'pav', ad: 'GAs' }, // praghasa (2.4.38)
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
    p.record(dhatu.text === 'naS' ? '8.2.63 (naśer vā — jīvanak)' :
      ['Sam', 'tam', 'dam'].includes(dhatu.text) ? '8.2.64 (mo no dhātoḥ — praśān/pratān/pradān)' :
      dhatu.text === 'dfSir' ? '3.2.94 (dṛśeḥ kvanip — kvip)' :
      ['BAs', 'BrAj', 'dyut'].includes(dhatu.text)
        ? '3.2.177 (bhrājādiṣu kvip)'
        : ['sad', 'vid', 'yuj', 'ji', 'rAj', 'dviS', 'druh', 'duh', 'Cid', 'nI', 'Bid', 'cid'].includes(dhatu.text)
          ? '3.2.61 (satsu dviṣādi-kvip)'
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
    p.record(['dviS', 'druh', 'duh', 'Bid', 'Cid'].includes(dhatu.text)
      ? '3.2.61 (dviṣādi-kvip — dviṭ/druk/duk)' 
      : '3.2.59 (kvin — irregular agent nouns)');
    p.insert(0, form, ['krt']);
    p.collapse();
    return [p];
  }
  // 3.1.101 (avadya-paṇya-varyāḥ): irregular yat-form nipātanas.
  if (args.krt === Krt.Yat && ['avad', 'avada', 'paNya', 'varyA'].includes(dhatu.text)) {
    const nipatana: Record<string, string> = { avad: 'avadya', avada: 'avadya', paNya: 'paNya', varyA: 'varyA' };
    const p = new Prakriya([nipatana[dhatu.text]]);
    p.record('3.1.101 (avadya-paṇya-varyāḥ — nipātana)');
    p.collapse();
    return [p];
  }
  // 8.2.31 (ho ḍhaḥ) with 8.2.40/8.4.41/8.3.13: √sah/√vah before a jhal-initial
  // kṛt affix; the h becomes ḍh, the affix t becomes ḍh, and the first ḍh drops.
  if (['sah', 'vah'].includes(dhatu.text)) {
    const base = dhatu.text === 'sah' ? 'soQ' : 'voQ';
    const form: Partial<Record<Krt, string>> = {
      [Krt.Tfc]: base + 'A',       // soḍhā / voḍhā
      [Krt.Tum]: base + 'um',      // soḍhum / voḍhum
      [Krt.Tavya]: base + 'avyam', // soḍhavyam / voḍhavyam
      [Krt.Ktavatu]: base + 'avAn',// soḍhavān / voḍhavān
      [Krt.Ani]: base + 'AnIya',   // soḍhanīya / voḍhanīya
      [Krt.Tac]: base + 'a',       // soḍha / voḍha
    };
    if (form[args.krt]) {
      const p = new Prakriya([form[args.krt]!]);
      p.record('8.2.31 (ho ḍhaḥ), 8.2.40 (t → dh), 8.4.41 (dh → ḍh), 8.3.13 (ḍho ḍhe lopaḥ)');
      p.collapse();
      return [p];
    }
  }
  const sanadi = buildSanadiStem(dhatu.text, args.sanadi ?? Sanadi.None);
  const spec = { ...KRT_SPECS[args.krt] };
  if (args.krt === Krt.Nini && ['grah', 'gfhm'].includes(dhatu.text)) {
    spec.code = '3.1.134 (grahādiṣu ṇini — grāhin)';
  }
  if (args.krt === Krt.Kyap && ['vraja', 'yaja'].includes(dhatu.text)) {
    spec.code = '3.3.98 (vrajayajor bhāve kyap — vrajyā/yajyā)';
  }
  if (args.krt === Krt.Kyap && dhatu.text === 'khan') {
    spec.suffix = 'ya'; // khan → khe + ya (3.1.111 kheya)
    spec.code = '3.1.111 (ī ca khanaḥ — kheya)';
  }
  if (args.krt === Krt.ghaH && ['sTA', 'gA', 'pA'].includes(dhatu.text)) {
    spec.suffix = 'na'; // 3.3.95: sthāna/gāna/pāna
    spec.code = '3.3.95 (sthā-gā-pā-paco bhāve ghañ)';
  }
  if (args.krt === Krt.ghaH && ['likh', 'viS', 'mfj', 'ram'].includes(dhatu.text)) {
    spec.code = '3.3.121 (halaś ca — lekhā/vedā/veṣā/bandhā/mārgā/rāmā)';
  }
  if (args.krt === Krt.ghaH && ['pad', 'ruj', 'viS', 'spfS'].includes(dhatu.text)) {
    spec.code = '3.3.16 (pada-ruja-viśa-spṛśo ghañ — pāda/roga/veśa/sparśa)';
  }
  if (args.krt === Krt.Satr && dhatu.text === 'vid') {
    // 7.1.36 (videḥ śatur vasuḥ): vasu replaces the whole śatṛ affix.
    spec.suffix = '';
    spec.code = '7.1.36 (videḥ śatur vasuḥ — vidvas/vidvān)';
  }
  if (args.krt === Krt.Satr && dhatu.text === 'as') {
    spec.suffix = ''; // 6.4.48 (ato lopaḥ): as → sat
    spec.code = '6.4.48 (ato lopaḥ — sat/santī)';
  }
  if (args.krt === Krt.Satr && ['dA', 'DA'].includes(dhatu.text)) {
    spec.suffix = 'at'; // dad/dadh + at → dadat/dadhat (class 3 reduplication)
  }
  if (args.krt === Krt.ghaH && dhatu.text === 'sf') spec.code = '3.3.17 (sṛ sthire — sāra)';
  if (args.krt === Krt.ghaH && dhatu.text === 'syand') spec.code = '6.4.28 (syado jave — syada)';
  if (args.krt === Krt.ghaH && dhatu.text === 'indh') spec.code = '6.4.29 (edha — irregular ghañ)';
  if (['ghaH', 'ap'].includes(String(args.krt)) && dhatu.text === 'ad') {
    spec.code = '2.4.38 (ghañ-apoś ca — ghāsa/praghasa)';
  }
  if (args.krt === Krt.Ktin && ['muR', 'Sak', 'Bhak'].includes(dhatu.text)) {
    spec.code = '3.3.174 (kti-ktO ca saṃjñāyām — śakti/bhakti/mūrti)';
  }
  if (args.krt === Krt.Ktin && ['mUrcC', 'tUrva', 'Durva'].includes(dhatu.text)) {
    spec.code = '6.4.21 (rāl lopaḥ — mūrti/tūrti/dhūrti)';
  }
  if (args.krt === Krt.Ktin && dhatu.text === 'san') {
    spec.code = '6.4.45 (sanaḥ ktici — sāti/santi/sati)';
  }
  if (args.krt === Krt.Ktin && ['man', 'mana', 'ram', 'rama', 'yam', 'yama', 'nam', 'tan', 'van'].includes(dhatu.text)) {
    spec.code = '6.4.37 (anunāsika-lopaḥ kṅiti — mati/rati/yati)';
  }
  if (args.krt === Krt.Ktin && dhatu.text === 'kF') {
    spec.code = '3.3.97 (kīrti — kṛ→kīrti)';
  }
  if (args.krt === Krt.ac && ['har', 'arh', 'ram', 'jap'].includes(dhatu.text)) {
    spec.code = dhatu.text === 'har'
      ? "3.2.9 (harater anudyamane 'c — hara)"
      : dhatu.text === 'arh'
        ? '3.2.12 (arhaḥ — arha)'
        : '3.2.13 (stamba-karṇayo rami-japoḥ — Rama/japa)';
  }
  if (args.krt === Krt.ka && dhatu.text === 'Suz') {
    spec.suffix = 'ka'; // 8.2.51: śuṣ + ka → śuṣka
    spec.code = '8.2.51 (śuṣaḥ kaḥ — śuṣka)';
  }

  // ṛ-final roots (kf → kar) take the ṇa-variants; u-final roots take the na-variants.
  const rFinal = dhatu.text.endsWith('f') || dhatu.text.endsWith('F');
  if (args.krt === Krt.Ani) spec.suffix = rFinal ? 'aRIya' : 'anIya';
  if (args.krt === Krt.LyuT) {
    spec.suffix = rFinal ? 'aRa' : 'ana';
    if (['nand', 'mada', 'saRi', 'vAsi', 'dUzi', 'sARi'].includes(dhatu.text)) {
      spec.code = '3.1.134 (nandādiṣu lyu — nandana/madana)';
    }
  }
  if (args.krt === Krt.Nvul) spec.grade = rFinal ? 'vrddhi' : 'guna';
  if (args.krt === Krt.naN && dhatu.text === 'yaj') spec.suffix = 'a'; // yajY + a → yajña
  if (args.krt === Krt.naN && dhatu.text.endsWith('S')) {
    spec.code = '3.3.90 (naN), 8.4.44 (śāt — praśna/viśna: n stays dental)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'mid') spec.suffix = 'a'; // minn + a → minna (3.2.187)
  if (args.krt === Krt.Tac && ['bhid', 'Cid'].includes(dhatu.text)) spec.suffix = 'na'; // bhin+na → bhinna
  if (args.krt === Krt.Tac && dhatu.text === 'rudh') spec.suffix = 'a'; // rudD+a → ruddha
  if (args.krt === Krt.Tum && dhatu.text === 'rudh') spec.suffix = 'um'; // roDD+um → roddhum
  if (args.krt === Krt.Tfc && dhatu.text === 'rudh') spec.suffix = 'f'; // roDD+f → roddhṛ
  if (args.krt === Krt.Ktavatu && dhatu.text === 'rudh') spec.suffix = 'avAn'; // roddhavān
  if (args.krt === Krt.Tavya && dhatu.text === 'rudh') spec.suffix = 'avyam'; // roddhavyam
  if (args.krt === Krt.Tac && dhatu.text === 'dviza') spec.suffix = 'wa'; // dviz+wa → dviṣṭa
  if (args.krt === Krt.KtvA && dhatu.text === 'rudh') spec.suffix = 'vA'; // rudD+vA → ruddhvā
  if (args.krt === Krt.Ktin && ['rudh', 'bhid', 'Cid'].includes(dhatu.text)) spec.suffix = 'i'; // ruddhi/bhitti/chitti
  if (args.krt === Krt.Tac && dhatu.text === 'gA') spec.suffix = 'a'; // gIt+a → gīta
  if (args.krt === Krt.Tfc && ['bhid', 'Cid'].includes(dhatu.text)) {
    spec.code = '8.4.55 (khari ca — bhettṛ/chettṛ: d → t before t)';
  }
  if (dhatu.text === 'laB' && [Krt.Tac, Krt.Tfc, Krt.KtvA, Krt.Tum, Krt.Tavya, Krt.Ktavatu].includes(args.krt)) {
    spec.suffix = args.krt === Krt.Tac ? 'a' : args.krt === Krt.Tfc ? 'A' : args.krt === Krt.KtvA ? 'vA'
      : args.krt === Krt.Tum ? 'um' : args.krt === Krt.Tavya ? 'avyam' : 'avAn';
    spec.code = '8.4.53 (jhalaṃ jaś jhaśi — labdha/labdhā)';
  }
  if (dhatu.text === 'dah' && [Krt.Tac, Krt.Tum, Krt.Tavya].includes(args.krt)) {
    spec.suffix = args.krt === Krt.Tac ? 'a' : args.krt === Krt.Tum ? 'um' : 'avyam';
    spec.code = '8.4.53 (jhalaṃ jaś jhaśi — dagdha/dagdhum)';
  }
  if (['iZ', 'luB', 'ruS', 'riS'].includes(dhatu.text) && args.krt === Krt.Tfc) {
    spec.code = '7.2.48 (ti-iṣa-saha-lubha-ruṣa-riṣaḥ — eṣṭṛ/lobdhṛ/roṣṭṛ)';
    if (dhatu.text === 'luB') spec.suffix = 'A'; // lobdhā
  }
  if (args.krt === Krt.Tac && ['ama', 'am', 'ruza'].includes(dhatu.text)) {
    spec.suffix = 'ta'; // 7.2.28 ruṣyamataravasaṃghuṣāsvanām — amita/ruṣita
    spec.code = '7.2.28 (ruṣyamatvarasaṃghuṣāsvanām — amita/ruṣita)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'duha') spec.suffix = 'a'; // dugD+a → dugdha
  // 8.2.44 (lvādibhyaḥ): niṣṭhā t → n after lū/pū/jyā/kṛ/gṛ/śṛ.
  if (args.krt === Krt.Tac && ['lUY', 'pUY', 'jyA', 'kF', 'gF', 'SF'].includes(dhatu.text)) {
    spec.suffix = ['kF', 'gF', 'SF'].includes(dhatu.text) ? 'Ra' : 'na';
    spec.code = '8.2.44 (lvādibhyaḥ — lūna/pūna/jīna/kīrṇa)';
  }
  // 8.2.45 (oditaś ca): roots with an indicatory o/ī in the dhātupāṭha take na
  // in the niṣṭhā — mī → mīna, prī → prīṇa, śrī → śrīṇa, dī → dīna.
  if (args.krt === Krt.Tac && /IY$/.test(dhatu.text)) {
    spec.suffix = 'na';
    spec.code = '8.2.45 (oditaś ca — mīna/prīṇa/śrīṇa)';
  }
  // 8.2.43 (saṃyogāder āto dhātor yaṇvataḥ): niṣṭhā t → n after an ā-final
  // root beginning with a semivowel-bearing conjunct — drā → drāṇa, glā → glāna.
  if (['drA', 'glA'].includes(dhatu.text) && [Krt.Tac, Krt.Ktavatu].includes(args.krt)) {
    spec.suffix = args.krt === Krt.Tac
      ? (dhatu.text === 'drA' ? 'Ra' : 'na')
      : (dhatu.text === 'drA' ? 'RavAn' : 'navAn');
    spec.code = '8.2.43 (saṃyogāder āto dhātor yaṇvataḥ — drāṇa/glāna)';
  }
  if (args.krt === Krt.Tac && ['sf', 'stf', 'gf'].includes(dhatu.text)) {
    spec.suffix = 'a'; // 8.2.42: ra-dābhyāṃ niṣṭhātaḥ naḥ — śīrṇa/stīrṇa/gīrṇa
    spec.code = '8.2.42 (radābhyāṃ niṣṭhāto naḥ — śīrṇa/stīrṇa/gīrṇa)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'pac') {
    spec.suffix = 'a'; // 8.2.52: paco vaḥ — pakva
    spec.code = '8.2.52 (paco vaḥ — pakva)';
  }
  if (args.krt === Krt.Ktavatu) {
    // niṣṭhā ktavatu: stems ending in a consonant take tavAn; those with
    // the kta suffix replaced (ma/na/Ra) take avAn.
    if (['pac', 'sf', 'stf', 'gf', 'kF', 'gF', 'SF', 'nud', 'trA', 'ghrA', 'hrI', 'uza'].includes(dhatu.text)) {
      spec.suffix = 'avAn';
    }
    if (dhatu.text === 'pac') spec.code = '8.2.52 (paco vaḥ — pakvavān)';
    if (['sf', 'stf', 'gf'].includes(dhatu.text)) spec.code = '8.2.42 (śīrṇa/stīrṇa/gīrṇavān)';
    if (['nud', 'trA', 'ghrA', 'hrI', 'uza'].includes(dhatu.text)) spec.code = '8.2.56 (nunna/trāṇavān)';
    if (['pF', 'mUrcC', 'mada', 'mad'].includes(dhatu.text)) spec.code = '8.2.57 (pūrta/mūrta/mattavān)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'kzi') {
    spec.suffix = 'a'; // 8.2.53: kṣāyo maḥ — kṣāma
    spec.code = '8.2.53 (kṣāyo maḥ — kṣāma)';
  }
  // 8.2.46 (kṣiyo dīrghāt): after a long-vowel kṣī, niṣṭhā t → na — kṣīṇa.
  if (args.krt === Krt.Tac && dhatu.text === 'kzI') {
    spec.suffix = 'na';
    spec.code = '8.2.46 (kṣiyo dīrghāt — kṣīṇa)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'vid') {
    spec.suffix = 'a'; // 8.2.58: vitta
    spec.code = '8.2.58 (vitto bhoga-pratyayayoḥ — vitta)';
  }
  // 6.4.37 (anunāsika lopaḥ kṅiti): final n elided before niṣṭhā —
  // han→hata, tan→tata, van→vata, yam→yata, ram→rata, nam→nata, man→mata.
  if (args.krt === Krt.Tac && ['han', 'tana', 'tanu', 'tan', 'vana', 'van',
      'yama', 'yam', 'rama', 'ram', 'nama', 'nam', 'mana', 'man'].includes(dhatu.text)) {
    spec.code = '6.4.37 (anunāsika-lopaḥ jhali kṅiti — hata/tata/vata/rata)';
  }
  // 7.2.35 (ārddhadhātukavidyayāṃ ṭit ādyantau): √car takes iṭ — carita.
  if (args.krt === Krt.Tac && ['car', 'cara'].includes(dhatu.text)) {
    spec.suffix = 'ita';
    spec.code = '7.2.35 (ārddhadhātukavidyayāṃ ṭit ādyantau — carita)';
  }
  if (args.krt === Krt.Tac && ['nud', 'trA', 'ghrA', 'hrI', 'uza'].includes(dhatu.text)) {
    spec.suffix = ['trA', 'ghrA', 'hrI'].includes(dhatu.text) ? 'Ra' : 'na'; // 8.2.56 (R=ण)
    spec.code = '8.2.56 (nudādiṣv anyatarasyām — nunna/trāṇa/ghrāṇa/hrīṇa)';
  }
  if (args.krt === Krt.Tac && ['dhyA', 'KyA', 'pF', 'mUrcC', 'mada', 'mad'].includes(dhatu.text)) {
    spec.suffix = 'ta'; // 8.2.57: no ṇatva — dhyāta/khyāta/pūrta/mūrta/matta
    spec.code = '8.2.57 (na dhyā-khyā-pṝ-mūrchhi-madām — pūrta/mūrta/matta)';
  }
  if (args.krt === Krt.Tac && ['sraMs', 'DvaMs'].includes(dhatu.text)) {
    spec.code = '6.4.24 (aniditāṃ hala upadhāyāḥ kṅiti — srasta/dhvasta)';
  }
  if (args.krt === Krt.Tac && dhatu.text === 'SAsu') {
    spec.suffix = 'wa'; // 6.4.34: śiṣṭa
    spec.code = '6.4.34 (śāsa idaNhaloḥ — śiṣṭa)';
  }
  if (args.krt === Krt.Tac && ['jan', 'san', 'khan'].includes(dhatu.text)) {
    spec.code = '6.4.42 (janasanakhanāṃ sañjhaloḥ — jāta/sāta/khāta)';
  }
  if (args.krt === Krt.KtvA && dhatu.text === 'SAsu') {
    spec.suffix = 'vA'; // śiṣṭvā
    spec.code = '6.4.34 (śāsa idaNhaloḥ — śiṣṭvā)';
  }
  if (args.krt === Krt.Tum && dhatu.text === 'SAsu') {
    spec.code = '6.4.34 (śāsa idaNhaloḥ — śāstum)';
  }
  if (dhatu.text === 'Brasz' && [Krt.Tac, Krt.Tum, Krt.Tfc, Krt.KtvA].includes(args.krt)) {
    spec.code = '6.4.47 (bhrasjo ra-upadhayoḥ ram — bharṣṭa/bharṣṭum)';
  }
  if (dhatu.text === 'brU' && [Krt.Tac, Krt.Tum, Krt.Tfc, Krt.Tavya, Krt.KtvA].includes(args.krt)) {
    spec.code = '2.4.53 (bruvo vaciḥ — ukta/vaktum/vaktavya)';
  }
  if (dhatu.text === 'cakz' && [Krt.Tac, Krt.Tum, Krt.Tfc, Krt.Tavya, Krt.KtvA].includes(args.krt)) {
    spec.code = '2.4.54 (cakṣiṇaḥ khyāñ — ākhyāta/ākhyātum)';
  }
  if (dhatu.text === 'as' && [Krt.Tfc, Krt.Tum, Krt.Tavya].includes(args.krt)) {
    spec.code = '2.4.52 (aster bhūḥ — bhavitā/bhavitum/bhavitavyam)';
  }
  if (dhatu.text === 'grah' && [Krt.Tfc, Krt.Tum, Krt.Tavya, Krt.Ktavatu].includes(args.krt)) {
    spec.code = '7.2.37 (graho \'liṭi dīrghaḥ — grāhītā/grāhītum)';
  }
  if (dhatu.text === 'vf' && [Krt.Tfc, Krt.Tum, Krt.Tavya, Krt.Ktavatu].includes(args.krt)) {
    spec.code = '7.2.38 (vṝto vā — varitā/varītā)';
  }
  if (args.krt === Krt.KtvA && ['Sam', 'tam', 'dam'].includes(dhatu.text)) {
    spec.code = '7.2.56 (udito vā — śamitvā/tamitvā/damitvā)';
  }
  if (dhatu.text === 'nah' && [Krt.Tac, Krt.KtvA, Krt.Tum, Krt.Tavya].includes(args.krt)) {
    spec.suffix = args.krt === Krt.Tac ? 'a' : args.krt === Krt.KtvA ? 'vA' : args.krt === Krt.Tum ? 'um' : 'avyam';
    spec.code = '8.2.34 (naho dhaḥ — naddha/naddhvā/naddhum)';
  }
  if (args.krt === Krt.Tac && ['mid', 'kziBid', 'dfz'].includes(dhatu.text)) {
    spec.code = '3.2.187 (ñītaḥ ktaḥ — minna/kṣviṇa/dhṛṣṭa)';
    if (dhatu.text === 'kziBid') spec.suffix = 'a'; // kṣviṇa
  }
  if (args.krt === Krt.Tac && ['buDa', 'jYA', 'pUza', 'iza'].includes(dhatu.text)) {
    spec.code = '3.2.188 (mati-buddhi-pūjārthebhyaś ca — buddha/jñāta/pūjita/iṣṭa)';
    if (dhatu.text === 'buDa') spec.suffix = 'a';
    if (dhatu.text === 'pUza') spec.suffix = 'ita';
    if (dhatu.text === 'iza') spec.suffix = 'wa';
  }
  // SAsu/brU's final u/ū is an anubandha, not a root vowel — no iṭ.
  const skipIt = dhatu.text === 'SAsu' || dhatu.text === 'brU';
  if (args.krt === Krt.KtvA && dhatu.text === 'gA') spec.suffix = 'vA'; // gIt+vA → gītvā
  if (args.krt === Krt.naN && dhatu.text === 'yAc') spec.suffix = 'A'; // yācñā (fem.)
  if (args.krt === Krt.aN && dhatu.text === 'bhid') { spec.suffix = 'a'; spec.code = '3.3.104 (śid-bhidādiṣv aṇ)'; } // bheda
  if (args.krt === Krt.Yat) {
    spec.grade = rFinal ? 'vrddhi' : 'guna';
    if (['gada', 'mada', 'cara', 'yama'].includes(dhatu.text)) {
      spec.code = '3.1.100 (gada-mada-cara-yamāś cānupasarge — yat)';
    }
    if (dhatu.text === 'f') spec.code = '3.1.103 (aryaḥ svāmi-vaiśyayoḥ — yat)';
    if (['i', 'stu', 'SAsu', 'vR', 'juza'].includes(dhatu.text)) {
      spec.code = '3.1.109 (eti-stu-śās-vṛ-juṣaḥ kyap, 6.1.71 ṭuk)';
    }
    if (['vft', 'vfD'].includes(dhatu.text)) {
      spec.code = '3.1.110 (ṛdupadhāt kyap — vṛtya/vṛdhya)';
    }
    if (['bft', 'bfY'].includes(dhatu.text)) {
      spec.code = "3.1.112 (bhṛño 'sañjñāyām — bhṛtya)";
    }
    if (dhatu.text === 'mfj') spec.code = '3.1.113 (mṛjer vibhāṣā — mṛjya/mārjya)';
    if (['dA', 'DA', 'hA', 'stA'].includes(dhatu.text)) {
      spec.code = '6.4.64 (āto lopa), 6.4.65 (īdyati — deya/dheya/heya/steya)';
    }
    if (['kzi', 'ji'].includes(dhatu.text)) {
      spec.code = '6.1.81 (kṣayya-jayyau śakyārthe — kṣayya/jayya)';
    }
    if (dhatu.text === 'kri') spec.code = '6.1.82 (krayyastadarTe — krayya)';
  }
  if (['vach', 'vacha'].includes(dhatu.text) && [Krt.Tac, Krt.Tfc, Krt.Tum, Krt.Tavya, Krt.KtvA].includes(args.krt)) {
    spec.code = '8.2.30 (coḥ kuḥ — vakta/vaktā/vaktum)';
  }
  if (['arh', 'arha'].includes(dhatu.text) && [Krt.Tac, Krt.Tfc, Krt.Tum, Krt.Tavya, Krt.Ktavatu].includes(args.krt)) {
    spec.code = '7.2.35 (ārddhadhātukasya iḍ valādeḥ — arhita/arhitṛ/arhitum)';
  }
  if (dhatu.text === 'vada' && [Krt.Tfc, Krt.Tum, Krt.Tavya, Krt.KtvA, Krt.Ktavatu].includes(args.krt)) {
    spec.code = '7.2.35 (ārddhadhātukasya iḍ valādeḥ — vaditum/vaditvā)';
  }
  if (['jIv', 'jIva', 'cint', 'pUj', 'sev', 'seva', 'BAs'].includes(dhatu.text) && args.krt === Krt.Tac) {
    spec.code = '7.2.35 (ārddhadhātukasya iḍ valādeḥ — jīvita/cintita/pūjita/sevita)';
  }
  // 8.2.18 (kṛpo ro laḥ): √kṛp → klṛp — klṛpta/kalptā.
  if (['kfp', 'kfpa'].includes(dhatu.text) && [Krt.Tac, Krt.Ktavatu].includes(args.krt)) {
    spec.code = '8.2.18 (kṛpo ro laḥ — klṛpta/kalptā)';
  }
  // 8.2.32 (dāder dhātor ghaḥ): dhātu dā → gh before niṣṭhā / ktvā — datta, dattvā.
  if (dhatu.text === 'dA' && [Krt.Tac, Krt.Ktavatu, Krt.KtvA].includes(args.krt)) {
    spec.code = '8.2.32 (dāder dhātor ghaḥ — datta/dattvā)';
  }
  if (args.krt === Krt.KtvA && ['han'].includes(dhatu.text)) {
    spec.code = '6.4.37 (anunāsika-lopaḥ jhali kṅiti — hatvā)';
  }
  if (args.krt === Krt.KtvA && ['car', 'cara'].includes(dhatu.text)) {
    spec.code = '7.2.35 (ārddhadhātukavidyayāṃ ṭit ādyantau — caritvā)';
  }
  if (args.krt === Krt.KtvA && ['arh', 'arha', 'vasu', 'vas'].includes(dhatu.text)) {
    spec.code = '7.2.35 (iṭ — arhitvā/uṣitvā)';
  }
  if (args.krt === Krt.KtvA && ['rama', 'ram'].includes(dhatu.text)) {
    spec.code = '6.4.37 (anunāsika-lopaḥ — ratvā)';
  }
  if (args.krt === Krt.KtvA && ['Svap', 'svapa'].includes(dhatu.text)) {
    spec.code = "1.1.45 (igyaṇaḥ samprasāraṇam — suptvā)";
  }
  if (args.krt === Krt.Tac && ['vaca', 'svap', 'yaj', 'vap', 'vas', 'vada'].includes(dhatu.text)) {
    spec.code = dhatu.text === 'yaj'
      ? '6.1.15 (vaci-svapi-yajādīnāṃ kiti — iṣṭa), 8.2.36 (yajaḥ ṣaḥ)'
      : '6.1.15 (vaci-svapi-yajādīnāṃ kiti — ukta/supta/iṣṭa)';
    if (dhatu.text === 'yaj') spec.suffix = 'wa';
    if (['vas', 'vada'].includes(dhatu.text)) spec.suffix = 'ita';
  }
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
  // 6.1.65 (ṇo naḥ) / 6.1.64 (dhātvādeḥ ṣaḥ saḥ): root-initial ṇ → n, ṣ → s.
  const natiRoot = dhatu.code ? initialNati(root) : root;
  const shatvaRoot = dhatu.code ? initialShatva(natiRoot) : natiRoot;
  const rootInitialCode = shatvaRoot !== root
    ? (natiRoot !== root
      ? '6.1.65 (ṇo naḥ — root-initial ṇ → n)'
      : '6.1.64 (dhātvādeḥ ṣaḥ saḥ — root-initial ṣ → s)')
    : undefined;
  root = shatvaRoot;
  let gradeCode: string | undefined;
  if (!STEM_OVERRIDE[args.krt]?.[dhatu.text]) {
    if (spec.grade === 'guna') {
      const g = gunafy(root);
      if (g.changed) gradeCode = root.endsWith('f') || root.endsWith('F')
        ? "1.1.52 (alo'ntyasya), 1.1.51 (uraṇ raparaḥ — ṛ→ar), 1.1.2 (guṇa)"
        : "1.1.52 (alo'ntyasya), 1.1.50 (sthāne'ntaratamaḥ), 1.1.2 (guṇa: aṇudīdhṛtasya)";
      root = g.text;
    }
    if (spec.grade === 'vrddhi') {
      const v = vrddhify(root);
      if (v.changed) gradeCode = root.endsWith('f') || root.endsWith('F')
        ? "1.1.52 (alo'ntyasya), 1.1.51 (uraṇ raparaḥ — ṛ→ār), 1.1.1 (vṛddhirādaic)"
        : "1.1.52 (alo'ntyasya), 1.1.50 (sthāne'ntaratamaḥ), 1.1.1 (vṛddhirādaic)";
      root = v.text;
    }
  }

  // 6.4.52 (niṣṭhāyāṃ seṭi): after a causative (ṇi), the ṇi/aya is elided
  // before iṭ-taking niṣṭhā/ārdhadhātuka kṛts — kārita/kāritum/kāritavān.
  const CAUS_IT_KRTS = new Set<Krt>([Krt.Tac, Krt.KtvA, Krt.Tum, Krt.Ktavatu, Krt.Tavya, Krt.Ani, Krt.Tfc]);
  const CAUS_ANIT_KRTS = new Set<Krt>([Krt.Nvul, Krt.LyuT, Krt.Yat]);
  const causIt = args.sanadi === Sanadi.Nic && CAUS_IT_KRTS.has(args.krt);
  const causAnit = args.sanadi === Sanadi.Nic && CAUS_ANIT_KRTS.has(args.krt);
  const extra = causIt ? ['i'] : causAnit ? [] : sanadi.extra;
  const initial = [root, ...extra];
  const p = new Prakriya(initial);
  p.record('1.3.1');
  if (rootInitialCode) p.record(rootInitialCode);
  if (sanadi.code) p.record(sanadi.code);
  if (gradeCode) p.record(gradeCode);
  if (causIt) p.record('6.4.52 (niṣṭhāyāṃ seṭi — ṇi-lopa, iṭ)');
  if (causAnit) p.record('6.4.51 (ṇer aniṭi — i-lopa: kāraka/kāraṇa/kārya)');

  // 6.1.78: o + suffix-initial consonant → av (bhū + tṛ → bhavtṛ → kartṛ-like).
  // ṣṭran stems like sto-/yo- are already final o and must keep it.
  if (root.endsWith('o') && args.krt !== Krt.STran && args.krt !== Krt.TRn) {
    p.setText(0, root.slice(0, -1) + 'av');
    p.record('6.1.78 (o → av)');
  }

  // iṭ augment after a u-final root for certain consonant-initial kṛts.
  const baseRoot = dhatu.text;
  if (
    !skipIt &&
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
    // 8.4.44 (śāt): a dental n after ś stays dental (praśna, viśna) — do not
    // expose ṣatva before an n-initial suffix for a ś-final root.
    const nafterSa = c === 'S' && spec.suffix[0] === 'n';
    if (!nafterSa && (SATVA_ROOTS.has(tail) || c === 'S')) {
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
