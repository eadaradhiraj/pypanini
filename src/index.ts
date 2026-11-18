/** Public library API for pypanini. All word forms are SLP1. */

export { Vyakarana } from './core/engine';
export { Prakriya } from './core/prakriya';
export type { Term, Step, PrakriyaSnapshot } from './core/prakriya';
export {
  Lakara,
  LAKARA_LABEL,
  Prayoga,
  Purusha,
  Vacana,
  Gana,
  Pada,
  Sanadi,
  Krt,
  Linga,
  Vibhakti,
} from './core/types';
export type {
  SLP1,
  Dhatu,
  TinantaArgs,
  KrdantaArgs,
  SubantaArgs,
} from './core/types';

export { deriveTinantas, deriveLatParadigm, getSuffixInfo } from './tinanta';
export {
  deriveParadigm,
  formatParadigm,
  PARADIGM_LAKARAS,
  PURUSHAS,
  VACANAS,
} from './paradigm';
export type { Paradigm, ParadigmCell } from './paradigm';
export { deriveAorist, derivePrecative, aoristKind, hasAorist } from './aorist';
export type { AoristKind, AoristArgs } from './aorist';
export { deriveKrdantas } from './krdanta';
export {
  deriveSubantas,
  deriveSubantaParadigm,
  aStemEnding,
  STEM_CLASSES,
  classFor,
} from './subanta';
export type { StemClass } from './subanta';
export { analyzeSubanta, describeAnalysis } from './analyze';
export type { SubantaAnalysis } from './analyze';
export {
  DHATUPATHA,
  findDhatu,
  findDhatus,
  searchDhatus,
  resolveDhatu,
} from './data/dhatupatha';
export { DHATUPATHA_FULL } from './data/dhatupatha.full';
export { SUTRAS } from './data/sutras';
export { IMPLEMENTED_CODES } from './data/implemented-codes';
export {
  buildCoverage,
  formatCoverage,
  topicOf,
  FOCUS_TOPICS,
} from './coverage';
export type { Topic, CoverageReport } from './coverage';
export * as aux from './data/aux';
export { deriveStri, striPratyayaFor, StriPratyaya } from './stri';
export type { StriArgs } from './stri';
export {
  UPASARGAS,
  isUpasarga,
  applyUpasargaSandhi,
  applyAyatiSandhi,
  needsSatva,
} from './upasarga';
export { deriveNamadhatus, NAMADHATU_INFO, NamadhatuPratyaya } from './namadhatu';
export type { NamadhatuArgs, NamadhatuInfo } from './namadhatu';
export {
  SANADI_INFO,
  reduplicate,
  heavyReduplicate,
  buildSanadiStem,
} from './sanadi';
export type { SanadiDerivation } from './sanadi';
export { toDevanagari, isSLP1, gunafy, vrddhify } from './core/slp1';

// Re-export rule primitives for advanced users who want to extend the engine.
export { RuleContext, Rule, SuffixStep, runTinantaPipeline } from './core/rules';
export {
  RuleScheduler,
  phaseFromCode,
  scheduled,
} from './core/scheduler';
export type {
  ScheduledRule,
  RulePhase,
  RuleStrength,
  ScheduleReport,
  SnapshotHooks,
} from './core/scheduler';
