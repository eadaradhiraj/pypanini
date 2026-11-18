import type { SLP1 } from './types';

/** A single term in an in-progress derivation. */
export interface Term {
  text: SLP1;
  tags: Set<string>;
}

/** One recorded step: a sūtra code and the resulting terms. */
export interface Step {
  rule: string;
  /** Terms joined by " + ", e.g. "BU + a + ti". */
  result: string;
}

/**
 * A derivation in progress: an ordered list of terms plus a history of steps.
 * This is the central mutable object that rules operate on.
 */
export class Prakriya {
  readonly terms: Term[];
  readonly history: Step[] = [];

  constructor(initial: SLP1[] = []) {
    this.terms = initial.map((text) => ({ text, tags: new Set<string>() }));
  }

  static from(texts: SLP1[]): Prakriya {
    return new Prakriya(texts);
  }

  get length(): number {
    return this.terms.length;
  }

  at(i: number): Term {
    return this.terms[i];
  }

  textAt(i: number): SLP1 {
    return this.terms[i]?.text ?? '';
  }

  setText(i: number, text: SLP1): void {
    if (this.terms[i]) this.terms[i].text = text;
  }

  /** Transform the text of a term in place. */
  edit(i: number, fn: (text: SLP1) => SLP1): void {
    if (this.terms[i]) this.terms[i].text = fn(this.terms[i].text);
  }

  insert(i: number, text: SLP1, tags: string[] = []): void {
    this.terms.splice(i, 0, { text, tags: new Set(tags) });
  }

  remove(i: number): void {
    this.terms.splice(i, 1);
  }

  tag(i: number, ...tags: string[]): void {
    for (const t of tags) this.terms[i]?.tags.add(t);
  }

  hasTag(i: number, tag: string): boolean {
    return this.terms[i]?.tags.has(tag) ?? false;
  }

  findTag(tag: string): number {
    return this.terms.findIndex((t) => t.tags.has(tag));
  }

  /** Append a step to history using the current term state. */
  record(rule: string): void {
    this.history.push({ rule, result: this.render() });
  }

  /** Terms joined with " + " (the conventional prakriyā display). */
  render(): string {
    return this.terms
      .filter((t) => t.text.length > 0)
      .map((t) => t.text)
      .join(' + ');
  }

  /** Concatenated surface form (what becomes the final word). */
  text(): SLP1 {
    return this.terms.map((t) => t.text).join('');
  }

  /** Collapse all terms into one, keeping the concatenated text. */
  collapse(): void {
    const joined = this.text();
    this.terms.length = 0;
    this.terms.push({ text: joined, tags: new Set() });
  }

  /** Capture the full state (terms + history) for phase-entry snapshots. */
  snapshot(): PrakriyaSnapshot {
    return {
      terms: this.terms.map((t) => ({ text: t.text, tags: [...t.tags] })),
      history: this.history.map((s) => ({ ...s })),
    };
  }

  /** Restore a snapshot in place (keeps object identity for ctx.prakriya). */
  restore(snap: PrakriyaSnapshot): void {
    this.terms.length = 0;
    for (const t of snap.terms) this.terms.push({ text: t.text, tags: new Set(t.tags) });
    this.history.length = 0;
    for (const s of snap.history) this.history.push({ ...s });
  }
}

export interface PrakriyaSnapshot {
  terms: Array<{ text: SLP1; tags: string[] }>;
  history: Step[];
}
