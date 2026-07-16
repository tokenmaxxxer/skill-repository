---
name: prose-modes
description: >-
  Routes a writing task to the right style regime before writing, on two axes — document type
  (tutorial / how-to / reference / explanation / decision record / book chapter) and the reader's
  assumed background knowledge — then applies only the rules that regime licenses. The reader axis
  is load-bearing and evidenced: raising cohesion helps low-knowledge readers and HURTS
  high-knowledge readers on deep-comprehension measures, so a single universal style is wrong by
  construction. Use when writing or revising prose a human will read — explanation, report, book
  or article draft, teaching material, design/decision writeup, long review feedback — in Korean
  or English. Also use when an existing draft reads badly and you need to find out which rule it
  is breaking. Do NOT use for code, or for a document whose nature is a list (CLI flags, config
  keys, error codes) with no explanatory prose around it — routing those returns "reference" and
  most rules switch off, so invoking the skill buys nothing. Every rule here carries an evidence
  grade; NONE has passed an A/B test. It is a graded prescription, not a verified instrument.
---

# Prose Modes

## First: route, then write

Answer both before drafting. The regimes below are not stylistic preferences — one of them contains a rule that the others' evidence argues against.

**Axis 1 — document type.** Tutorial · how-to · reference · explanation · decision record · book chapter.

**Axis 2 — reader's background knowledge.** Novice · intermediate · expert *in this specific topic*, not in general.

If you cannot answer axis 2, ask. Do not default to novice — see rule R1's evidence, where that default is the thing that got refuted.

## Evidence grades — read before citing this skill to anyone

Grades used below:

- **[검증]** — passed 3-vote adversarial verification against a primary source with an effect size.
- **[카탈로그]** — named in a practitioner catalog (mostly Wikipedia's "Signs of AI Writing"). Real observations; nobody has run the study.
- **[가설]** — inferred from a validated mechanism, or collected from field correction. Not tested.
- **[현장]** — this user corrected it into existence. n=1, and irreplaceable — no literature recovers it.

**Nothing here is A/B verified.** The pre-registration (`docs/research/prose-skill-ab-preregistration.md`) exists, the 3-arm test is frozen and ready, and it has not run. Do not say this skill is "verified to improve writing." It is not verified to do anything.

**Ceiling — state this whenever the skill is cited.** A skill is a prompt, and prompting raises the floor, not the ceiling. 31 prompting strategies land on a near-identical length/accuracy curve (arXiv:2503.01141); multi-hop accuracy caps near 60% even when every single-hop fact is correct (arXiv:2506.02000). **This skill can move wording, structure, and format. It cannot make thinking deeper.** Any rule below that seems to promise depth is promising placement, not cognition.

## The reader axis (R1) — the one rule with teeth

**[검증]** "Raise cohesion and comprehension improves" was **rejected 0-3**. The real finding has a sign flip:

- **Low-knowledge readers**: high-cohesion text wins. Problem-solving 30% (low-cohesion) → 17% is the *wrong* direction for them; they need the connections spelled out (McNamara et al. 1996).
- **High-knowledge readers**: low-cohesion text wins — **61% problem-solving vs 46%** on high-cohesion (O'Reilly & McNamara 2007). The gap they fill themselves is what builds the situation model.
- **The effect is invisible on recall.** It shows up only on inference and problem-solving. A high-knowledge reader given spelled-out text *feels* fine and learns less.
- **Boundary**: strategic readers with high reading skill do better with high cohesion regardless. Cohesion is never a loss for them.

**So:** density and gap-leaving are set by axis 2, not by taste. For novices, connect everything. For experts, leave the one-step inference. Never both, and never neither.

**[검증]** Connective type is not a detail: causal and contrastive connectives ("때문에", "그러나") **raise** comprehension; additive ones ("또한", "추가로") **lower** it, and the effect grows with text difficulty (Kleijn, Pander Maat & Sanders 2019, n=794). Do not ban "또한" — that buys either unmarked juxtaposition or, likelier, a *mislabeled* causal marker, and a false "따라서" is a relation the reader tries to build and cannot. Fix the relation, then mark it truthfully.

**[검증]** Referential distance is span-bound: low-span readers lose pronoun–antecedent binding after 2–3 intervening sentences, high-span at 6–7 (Just & Carpenter 1992). Re-mention the referent before it decays. In Korean, subjects drop — the surrogate is "이는"/"그것"/지시관형사+명사, and it is a *different* construct with a different base rate. Do not port the English threshold.

## Per-mode regimes

| Mode | Bullets/tables | Gaps | Numbered cross-refs | Meta scope statement |
|---|---|---|---|---|
| Reference | **Correct** — the content *is* a list | No | Yes | Yes, if long |
| How-to | Steps: yes | No | Yes | Brief |
| Tutorial | Sparingly | Only for experts (axis 2) | Yes | Brief |
| Explanation | Prose (R2) | Per axis 2 | Resolve in place (R6) | No |
| Decision record | Comparison tables ok | No | Yes | Yes |
| Book chapter | Prose (R2) | Per axis 2 | Resolve in place (R6) | No |

**The mode taxonomy is [가설].** It is adapted from practitioner taxonomies (Diátaxis, DITA, Information Mapping) that were **not researched for this skill** — that round was cut for cost. Whether reference and explanation *empirically* need different rules is unverified. The reader axis above is evidenced; this table is inference. Treat it as a working split, not a finding.

## Rules

### R2 — Prose over bullets, in explanation and book-chapter modes only

**[검증] — the best-evidenced rule here.** Injecting **0.7%** format-biased data into reward-model training raises list-preference win-rate **51% → 77.5%**, and bold-preference **57.5% → 88.0%** (arXiv:2409.11704). Bullets are a trained reward artifact, not a reasoning aid: they let you omit the relation between items. Prose forces "그래서", "그런데", and that connective *is* the understanding.

**Switches off entirely in reference and how-to modes.** A `ls` flag list is a list. Bulleting it is correct, and a rule that suppressed it would be scoring a working router as a failure.

Note the asymmetry the evidence hands you: **bold had a larger effect than lists and has no rule.** Watch `**bold:**` headers substituting for paragraph development.

### R3 — Name the boundary condition (replaces "hedge when uncertain")

**[검증] on the symptom; [가설] on this rule as the fix.** Reward models penalize explicit uncertainty markers **on correct answers** (Fein et al. 2026). Downstream: GPT-4o emits strong confidence markers on **15%** of its wrong answers, Llama-8B on **49%**, and human over-reliance runs **65%** (COLM 2025).

**Do not write "hedge when uncertain."** A model cannot condition on its own uncertainty, so that instruction produces *global* hedge inflation — and flat hedging destroys the confidence gradient exactly as thoroughly as flat confidence does. It converts one symptom (과잉 확신) into another (헤징·거짓 균형).

**Write the boundary instead.** Not "아마 X일 것이다" but "X이며, **Y인 경우에는 성립하지 않는다**." This carries the uncertainty *structurally*, is checkable, and never asks the model to read its own confidence. **No design available to this project measures calibration** — this rule sidesteps the question rather than answering it.

### R4 — Name what you are giving up (아첨)

**[검증] at both symptom and cause — the strongest causal chain in the base.** Agreement with the user's stated view predicts human preference over correctness; optimizing against a real preference model raises sycophancy **monotonically** with pressure (Sharma et al., ICLR 2024, Anthropic). Under rebuttal, 58.19% of responses change stance (SycEval, n=15,345); Claude 1.3 withdraws **98%** of *correct* answers when asked "Are you sure?"

**In a decision record or design writeup, when the requester states the conclusion in the request, an honest document still names the specific costs.** "gRPC를 채택하기로 했어요, 왜 그런지 문서로 남겨줘" is a sycophancy trap by construction. The answer names grpc-web's browser gap, opaque payloads breaking curl/tcpdump, and codegen build coupling — or it is flattery with citations.

**Effect sizes do not transfer.** Those numbers measure multi-turn retraction under pushback. Single-turn document generation carries the *symptom class* (Sharma's free-form tasks are single-turn), not the numbers. Do not import them.

### R5 — Depth: mechanism → example → failure condition

**[검증] on the shape, [카탈로그] on the pattern.** Blind human raters score AI essays **3.85–4.67** where the auto-grader gives **4.45–5.32** (arXiv:2410.17439, 2,000 AI + 200 human GRE essays) — humans see the substance deficit, the automated grader does not. That asymmetry is *why* mention-and-move-on survives: what is easy to score is what gets optimized.

A concept you introduce descends to mechanism, one concrete instance, and **the condition under which it fails**. Two sentences per concept is the signature of coverage anxiety. Cut items to keep depth, and say which you cut.

**Honest limit:** the reasoning-depth benchmarks behind this are an **analogy** to prose shallowness, not a measurement of it. And per the ceiling, this rule places depth markers; it does not create depth.

### R6 — Resolve cross-references in place

**[카탈로그]** In explanation and book modes, "3장에서 본 X" outsources the explanation to the reader's memory. Half a clause fixes it: "앞서 본 자유간접화법, 곧 인물의 목소리가 서술에 스며드는 기법". In reference and how-to modes, numbered pointers are correct — that is what a reference is for.

### R7 — Definition before analogy

**[현장]** Define operationally first — what was measured, how. Analogy comes after, one per concept, never in the conclusion slot ("~인 셈이다"). Chained metaphors make the reader decode the metaphors' correspondences on top of the concept.

This rule has **no literature backing in this research base** — it exists because the user corrected it into being after a chain of "자기 채점 / 문제집 점수 / 판결문" analogies made a statistics passage *harder*. Field correction is thin evidence and it is real evidence. Do not delete it for lacking a citation; test it.

### R8 — No empty frames, no meta-announcements, no manufactured contrast

**[카탈로그] — all three.** "질문은 간단하다. ~인가." (announce-then-deliver), "이 글에서는 ~를 살펴본다" (structure narration), "단순히 X가 아니라 Y다" (strawman-then-knock-down).

Be honest about what this grade means: **nobody ran the study.** These are catalog entries and daily observation, not measurement. The cause is unknown — the evidence base grades the *cause attribution* [가설], which is a statement about mechanism, not about whether the symptom is real.

**Real exceptions:** a count that informs ("조건은 셋이다"), a scope statement at the top of a long reference, and negation-contrast where the misconception is genuinely widespread and you can show it. This document uses all three.

### R9 — Say it once

**[카탈로그], and in tension with a [검증] finding — read the test.** Word-swapped restating is padding. But the levels effect says superordinate propositions are recalled **2–3× better** *because they re-enter the working buffer*, not because they were labeled important (Kintsch & van Dijk 1978). Prior-knowledge advantage runs +50% on recall tasks and **+200%** on situation-model tasks (McNamara & Kintsch 1994).

**The test:** does the recurrence *do work* — is the claim used as a premise, applied to a new case, loaded with more? Then it is re-entry; keep it. Does it only restate? Then it is padding; cut it. R9 and re-entry are not opposites, and the skill does not resolve them for you.

## Rules deliberately not written

- **Length / verbosity.** Reward length bias is [검증] (length-only reward reproduces 51–64% of RLHF's win-rate gains, Singhal et al. 2024) — and the fix is refuted in advance: 31 prompting strategies all land on one length/accuracy curve, real prompts achieving 1.16–1.47× compression against 3.2–11.2× theoretical room (arXiv:2503.01141). **The published literature predicts a length rule would fail an ON-vs-placebo test before we run it.** Length interacts with every depth rule anyway — measure it as a covariate, never rule it.
- **Sentence-length variance (burstiness).** [검증] as a symptom (6 LLMs cluster at 10–30 tokens vs dispersed human, p<0.001; cross-model syntactic cosine 0.9996–0.9999 vs human-human 0.94–0.99). Not prompt-movable: model identity dominates style far more than decoding, and a "vary your sentence lengths" rule Goodharts its own metric — you get performed variance without the syntactic complexity it proxies.
- **Lexical bans (delve-class).** The most-replicated symptom in the base — ≥13.5% of 2024 PubMed abstracts, some subcorpora ~40% (Kobak et al., *Science Advances* 2025); three independent peer-reviewed corpora. Trivially enforceable, near-worthless: it costs context linear in list length, and **no Korean list exists** — all three studies are English biomedical, and this skill is Korean-first.
- **"제목에 개수를 넣지 마라."** Zero evidence anywhere in the base. It has a licit use ("SOLID의 다섯 원칙") and no false-alarm test. The pre-registration's own decision table returns: do not ship. It was a taste.

## Korean-specific: translationese

**[검증], and it cuts against the prescription.** Corpus measurement exists — 김혜영(2009), 100M-eojeol balanced corpus, finds translated Korean over-uses '-에 의하여' passive, syntactic passive '-아/어 지다', 2nd/3rd-person pronouns, and dependent nouns '것/거'·'때문' (medium grade: secondary summary via 김정우 2012; the dissertation is not publicly verifiable).

Three findings that should stop you from writing a translationese linter:

1. **최희경(2016) contradicts the prescription.** '~통하다' is **2× more frequent in NON-translated Korean**. The author reframes translationese as language contact, not a translation defect.
2. **'~에 의하여' is a Japanese calque of 依って**, per 법제처's own 「알기 쉬운 법령 정비기준」 — not an English passive. That document cites **zero** sources for its prescription.
3. **법제처 explicitly permits inanimate-subject passive**: "소멸시효가 **완성된** 때." The active form is also widespread in civil law. A regex that flags this is wrong at exactly the place the norm-setting body permits it.

**No experiment shows translationese harms readability** — within verified scope, and that scope is not complete (15 unverified claims remain on that angle). Do not upgrade this to "no such research exists."

Full evidence: `docs/research/korean-translationese-evidence.md`. Observed frequencies in AI-written Korean: `docs/research/translationese-candidates-observed.md`.

## What this skill is not verified to do

Written before there was any reason to want it softer:

- **Permitted:** "This skill applies rules R1–R9, graded as marked."
- **Forbidden:** "verified to improve prose quality", "A/B verified", "makes writing clearer/deeper". None of that has been measured. The test is frozen and has not run.
- **Rules whose evidence is [카탈로그] or [가설] or [현장] are prescriptions.** Say so when citing them. R1, R2, R3's symptom, R4, and the connective/reference findings are the only [검증] items.
