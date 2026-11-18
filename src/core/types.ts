/** Core grammatical value types. All textual values are SLP1. */

export type SLP1 = string;

export enum Lakara {
  Lat = 'lat', // present
  Lit = 'lit', // perfect
  Lut = 'lut', // future (1st)
  Lrt = 'lrt', // future (2nd)
  LatN = 'latN', // aorist (luN) — root/a/s/iṣ varieties via aorist.ts
  Lin = 'lin', // optative
  Lof = 'lof', // imperative (legacy alias)
  Lot = 'lot', // imperative (conventional)
  Lan = 'lan', // imperfect
  Lang = 'lang', // aorist
  LanN = 'lanN', // conditional (legacy alias)
  Lng = 'lng', // conditional (conventional)
}

/** Conventional ashtadhyayi.com-style SLP1 labels for the lakāras we support. */
export const LAKARA_LABEL: Partial<Record<Lakara, SLP1>> = {
  [Lakara.Lat]: 'la~w',
  [Lakara.Lit]: 'liw',
  [Lakara.Lut]: 'luw',
  [Lakara.Lrt]: 'lfw',
  [Lakara.Lin]: 'liN',
  [Lakara.Lof]: 'low',
  [Lakara.Lot]: 'low',
  [Lakara.Lan]: 'laN',
  [Lakara.Lang]: 'lfN',
  [Lakara.LanN]: 'lfN',
  [Lakara.Lng]: 'lfN',
};

export enum Prayoga {
  Kartari = 'kartari', // active
  Karmani = 'karmani', // passive
  Bhave = 'bhave', // impersonal
}

export enum Purusha {
  Prathama = 'prathama',
  Madhyama = 'madhyama',
  Uttama = 'uttama',
}

export enum Vacana {
  Eka = 'eka',
  Dvi = 'dvi',
  Bahu = 'bahu',
}

export enum Gana {
  Bhvadi = 1,
  Adadi = 2,
  Juhotyadi = 3,
  Divadi = 4,
  Svadi = 5,
  Tudadi = 6,
  Rudhadi = 7,
  Tanadi = 8,
  Kryadi = 9,
  Curadi = 10,
}

export enum Pada {
  Parasmai = 'parasmai',
  Atmane = 'atmane',
}

/** Saṇādi pratyayas attached to the dhātu before tiṅ/kṛt. */
export enum Sanadi {
  None = 'none',
  San = 'san', // desiderative (सन्)
  Nic = 'nic', // causative (णिच्)
  Yan = 'yan', // intensive (यङ्)
  Yang = 'yang', // याङ्
  YangLuk = 'yangLuk', // यङ्लुक्
}

/** A verb root from the Dhātupāṭha. */
export interface Dhatu {
  /** SLP1 form, e.g. "BU" (भू). */
  text: SLP1;
  gana: Gana;
  pada: Pada;
  /** Optional meaning gloss. */
  artha?: string;
  /** Optional Dhātupāṭha code (ashtadhyayi.com-style). */
  code?: string;
}

/** Arguments for deriving a finite verb (tiṅanta). */
export interface TinantaArgs {
  dhatu: Dhatu | string;
  lakara: Lakara;
  prayoga: Prayoga;
  purusha: Purusha;
  vacana: Vacana;
  pada?: Pada; // defaults to dhatu.pada
  sanadi?: Sanadi;
  /** Upasarga (prefix) from Pāṇini 1.4.58, e.g. "pra", "sam", "pari". */
  upasarga?: string;
}

/** Kṛt pratyayas we model (SLP1 labels). */
export enum Krt {
  Tac = 'tac', // क्त → -ta (karmani participle)
  Tfc = 'tfc', // क्तृ → -tṛ (agent noun)
  Satr = 'satr', // शतृ → -at (present participle, kartari)
  Ani = 'ani', // अनीयर् → -anIya (gerundive/karmani)
  Tum = 'tum', // तुम् → -tum (infinitive)
  Tavya = 'tavya', // तव्यत् → -tavya (gerundive)
  LyuT = 'lyuT', // ल्युट् → -ana (action noun)
  KtvA = 'ktvA', // क्त्वा → -tvā (gerund)
  Nvul = 'nvul', // ण्वुल् → -aka (agent noun)
  Ktavatu = 'ktavatu', // क्तवतु → -tavān (kartari past participle)
  SanaC = 'sanaC', // शानच् → -amāna (ātmanepada present participle)
  Yat = 'yat', // यत् → -ya (karmani gerundive, 3.1.97)
  Ktin = 'ktin', // क्तिन् → -ti (feminine action noun, 3.3.94)
  Nini = 'Nini', // णिनि → -in (obligation agent, 3.3.170)
  Sanan = 'Sanan', // शानन् → -māna (pavamāna/yajamāna, 3.2.128)
  STran = 'STran', // ष्ट्रन् → -tra instrument noun (dātra/netra/stotra, 3.2.182)
  TRn = 'TRn', // तृन् → -tṛ habitual agent (kartṛ/hotṛ/neṣṭṛ, 3.2.135)
  Kyap = 'Kyap', // क्यप् → -yā feminine appellative (vidyā/manyā, 3.3.99)
  Sa = 'Sa', // श → -ā/-iyā feminine (kriyā, 3.3.100; icchā 3.3.101)
  uH = 'uH', // उः → -u habitual agent (bhikṣu, 3.2.168)
  ghaH = 'ghaH', // घः → -a instrument/location name (chada, 3.3.118)
  raH = 'raH', // रः → -ra habitual agent (namra/dīpra, 3.2.167)
  kru = 'kru', // क्रु → -ru (bhīru, 3.2.174)
  AruH = 'AruH', // आरुः → -āru (vandāru, 3.2.173)
  varac = 'varac', // वरच् → -vara (sthāvara/īśvara, 3.2.175)
  kvip = 'kvip', // क्विप् → zero suffix agent noun (yuk/vāk/jagat, 3.2.178)
  Du = 'Du', // डु → -u after vi/pra/sam+bhū (vibhu/prabhu, 3.2.180)
  knu = 'knu', // क्नु → -nu habitual agent (trasnu/gṛdhnu, 3.2.140)
  kSnu = 'kSnu', // क्ष्णु → -ṣṇu (jizṇu/sthāsnu/bhūṣṇu, 3.2.139)
  izNuc = 'izNuc', // इष्णुच् → -iṣṇu (bhaviṣṇu, 3.2.138)
  yuc = 'yuc', // युच् → -ana (calana/śabdana, 3.2.148)
  ruH2 = 'ruH2', // रुः → -ru (dāru/saru/sadru, 3.2.159)
  kurac = 'kurac', // कुरच् → -ura (vidura/bhidura/chidura, 3.2.162)
  ghurac = 'ghurac', // घुरच् → -ura (bhaṅgura/bhāsura/medura, 3.2.161)
  kvarap = 'kvarap', // क्वरप् → -vara with ṭuk (itvara/naśvara/jitvara, 3.2.163)
  vuN = 'vuN', // वुञ् → -aka (nindaka/hiṃsaka/khādaka, 3.2.146)
  ghinuN = 'ghinuN', // घिनुण् → -in (vikāṣī/vilāsī/pravāsī, 3.2.143/145)
  cAnaS = 'cAnaS', // चानश् → -āna (bhuñjāna/bibhrāṇa, 3.2.129)
  aN = 'aN', // अण् → -ā feminine action noun (cintā/pūjā/kathā, 3.3.105)
  gaNa = 'gaNa', // घञ् → -a action noun with vṛddhi (pāka/tyāga/rāga, 3.3.18)
  ap = 'ap', // अप् → -a action noun (svāna/hāsa, 3.3.61/62)
  kaN = 'kaN', // कञ् → -śa (tādṛśa/yādṛśa/sadṛśa, 3.2.60)
  kvin = 'kvin', // क्विन् → zero-suffix agent (ṛtvik/dadhṛk/srak/dik, 3.2.59)
  khuKN = 'khuKN', // खुकञ् → -uka (bhāvuka, 3.2.57)
  khyun = 'khyun', // ख्युन् → -ana instrument (karaṇa, 3.2.56)
  kiN = 'kiN', // कि/किन् → -i agent with reduplication (dadiḥ/cakriḥ, 3.2.171)
  najiN = 'najiN', // नजिङ् → -na habitual agent (svapna/tṛṣṇa/dhṛṣṇa, 3.2.172)
  ac = 'ac', // अच् → -a action noun after i/ī-final roots (caya/jaya/kṣaya, 3.3.56)
  naN = 'naN', // ण → -na noun (yajña/praśna, 3.3.90)
  Nvanip = 'Nvanip', // ङ्वनिप् → -van agent (sutvan/yajvan, 3.2.103)
}

export interface KrdantaArgs {
  dhatu: Dhatu | string;
  krt: Krt;
  prayoga?: Prayoga; // defaults kartari, except where krt implies karmani
  sanadi?: Sanadi;
}

export interface SubantaArgs {
  /** SLP1 prātipadika, e.g. "bala" (बल). */
  pratipadika: SLP1;
  linga: Linga;
  vibhakti: Vibhakti;
  vacana: Vacana;
}

export enum Linga {
  Pumsaka = 'pumsaka',
  Stri = 'stri',
  Napumsaka = 'napumsaka',
}

export enum Vibhakti {
  Prathama = 1,
  Dvitiya = 2,
  Trtiya = 3,
  Caturthi = 4,
  Pancami = 5,
  Sasti = 6,
  Saptami = 7,
  Sambodhana = 8,
}
