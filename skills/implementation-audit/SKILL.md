---
name: implementation-audit
description: >-
  A two-session audit protocol: the builder session extracts falsifiable claims from the
  specification, then a structurally independent evaluator session (spawned via
  adversarial-review) classifies each claim against the implementation as Present, Surface,
  Absent, Incorrect, or Unverifiable — with no access to the builder's intent or context.
  Use after AI completes a task and you need to know "did it genuinely deliver what I asked for"
  without the builder grading its own homework — e.g. "AI가 구현한 거 검증해줘", "이 코드가 요구사항
  제대로 구현했는지 확인해줘", "did the agent actually build what the spec says", "check if this
  implementation matches the requirements", "요구사항 대비 구현 감사". Do NOT use for code style
  (linter), to evaluate requirements themselves (requirements-quality), or to decide what tests
  to write (test-derivation). This skill answers exactly one question: "for each thing asked,
  is there a real implementation or just a surface imitation?" — and it answers it in a session
  that has no stake in the answer.
---

# Implementation Audit

## The self-review problem — read this first

An AI that built something cannot honestly audit whether it built the right thing. This is not a trust issue — it's a structural one. The builder's context window already contains the chain of reasoning that produced the output, and asking the same model mid-session to now declare those outputs flawed is asking it to contradict its own probability distribution. Telling it "be critical" or "be honest" doesn't fix this — the prior tokens are already committed, and each subsequent token is conditioned on them.

This skill therefore does not have the builder audit itself. It describes a **two-session protocol**:

```
[Session A: Builder (or User)]            [Session B: Evaluator (independent)]

  1. Extract falsifiable claims             3. Receive claims + implementation
     from the specification                    (no spec, no builder context)

  2. Collect implementation files            4. For each claim:
                                                - Search for evidence
                                                - Classify (P/S/A/I/U)
                                                - Depth-check Present claims

                                             5. Output structured gap report
                                                (User reads report, decides action)
```

Session B is set up using the `adversarial-review` skill. It receives claims and implementation, but not the original specification, the builder's prompt, or any statement of what the builder intended. Its system prompt frames finding flaws as success.

**If you are the builder agent reading this skill**: your job is Steps 1 and 2 only. Do not classify, do not evaluate, do not produce the audit report. Extract claims from the spec, collect the implementation files, and hand them to the user — then stop. The user (or an orchestrator) spawns the evaluator session.

**If you are the user or an orchestrator**: you run both sessions. Steps 1-2 in the builder's session (or by hand), then Steps 3-5 in a fresh evaluator session using the adversarial-review protocol.

## First: does this even need the procedure?

- **Is there a written specification or requirement set?** If the user gave the AI a one-line prompt with no recorded requirements, there is nothing to audit against — suggest capturing the requirements first, then running the audit.
- **Is this about code style, formatting, or conventions?** That's a linter's job. Skip.
- **Is the implementation trivially verifiable by eye?** A one-line config change, a single regex fix — just check it directly.
- **Is the builder also the one asking for audit?** If the same session is being asked to audit itself, stop. This is the exact situation the two-session protocol exists to prevent. Tell the user: "This needs a separate evaluator session — I can extract the claims and prepare the files, but the audit itself must run in a fresh session with no knowledge of my reasoning."

## Evidence grade

- **Session separation as a debiasing mechanism** — see adversarial-review for the full evidence grade on this claim. [가설]
- **The reverse-generation technique** (extracting claims from code and comparing to originals) has a published benchmark — Sun et al. (arXiv 2502.07835). [검증]
- **The classification taxonomy (P/S/A/I/U) is a procedural design choice**, not empirically validated. [가설]
- **The surface-pattern catalog** is compiled from practitioner reports. [현장]

## The two-session protocol

### Session A — Extract claims and prepare files

This happens in the builder's session (or by the user manually). The builder does NOT evaluate — it only prepares inputs for the evaluator.

#### Step A1 — Extract falsifiable claims

Take the original specification and produce a numbered list of claims, each:

1. **Falsifiable**: a third party can look at the code and say "yes" or "no."
2. **Atomic**: one claim = one observable behavior. "The login page works" → "form accepts email+password," "invalid credentials show error," "success redirects to /dashboard."

Implied claims (obvious from context but unstated) are allowed only if labeled "[implied]." Do not invent claims.

**Gate**: numbered list with count. Every claim is falsifiable and atomic. Implied claims are labeled.

#### Step A2 — Collect implementation files

Gather every file the builder produced or modified. Include the full content, not summaries. Do not include:
- The original specification (the evaluator doesn't get this — it gets claims, which are the specification translated into checkable form)
- The builder's prompt
- Any commentary on what the builder intended

**Gate**: a file bundle exists containing the implementation and nothing else.

#### Handoff

The builder's output is: (1) the claims list, (2) the implementation files. These are handed to the user, who feeds them to Session B.

The builder stops here. It does not classify, audit, or report.

### Session B — Evaluate (independent, via adversarial-review)

This is a fresh session with no access to the builder's context. Set it up using the `adversarial-review` skill's Step 2 evaluator prompt, then add the implementation-audit-specific instructions below.

#### Evaluator prompt (append to the adversarial-review base prompt)

```
You are evaluating whether an implementation satisfies a set of claims.

You will receive:
1. A numbered list of claims — each is a specific, falsifiable statement about
   what the implementation should do.
2. The implementation files.

You do NOT receive the original specification or any statement of what the
builder intended. Judge only what the code actually does against what each
claim says it should do.

For each claim, search the implementation for concrete evidence and classify:

PRESENT (P): Concrete code exists that implements the claimed behavior. Cite
the file:line where the logic lives. A function whose body is just a stub,
a TODO, or a constant return is NOT Present even if it's named correctly.

SURFACE (S): Something exists that appears to address the claim but is
structurally insufficient. This includes:
- A function body that is a stub (pass, return null, throw NotImplemented)
- A TODO comment where implementation should be
- A function that always returns a constant regardless of input
- An empty catch block (catches errors but does nothing)
- A component that renders only static placeholder content
- A handler that covers only the happy path with no error/edge handling
See the full surface-pattern catalog for more patterns.
When in doubt between P and S, classify as S and explain why.

ABSENT (A): No evidence found. State where you searched.

INCORRECT (I): Code exists but does the wrong thing — inverted condition,
wrong endpoint, conflicting rule.

UNVERIFIABLE (U): The claim can't be checked by code inspection alone
("responds within 200ms"). Suggest what method would verify it.

For every claim you classify as PRESENT, also check:
- Are edge cases handled (empty input, boundary values, null, etc.)?
- Are error states handled (what if the operation fails)?
If a Present claim fails these depth checks, reclassify it as SURFACE.

Output: a table with claim number, classification, file:line of evidence
(or search locations for Absent), and one-sentence diagnosis. Then a summary:
X/Y claims Present, with counts for each classification.
```

#### Run the evaluator

Feed the claims list and implementation files to the evaluator session. The evaluator produces the classification table and summary. The user reads the output.

### After the audit — route findings

Based on the evaluator's output:

- **Mostly Present**: implementation is genuine. Route to test-derivation.
- **Mostly Surface**: the builder produced mock-like code. The spec was likely too vague — route to requirements-quality, tighten, and re-build.
- **Mostly Absent**: the builder missed requirements. The task was likely too large — break into smaller tasks, submit individually, re-audit.
- **Mixed**: inconsistent work. Break into claim-level tasks, audit incrementally.
