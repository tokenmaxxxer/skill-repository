---
name: premortem
description: >-
  A plan-evaluation exercise run BEFORE committing to a plan: assume the plan has already failed,
  generate reasons independently, then convert every reason into a mitigation, a detection signal,
  or an explicit accepted risk. Use this whenever the user wants to pressure-test a plan before
  it's locked in — e.g. "이 계획 시작 전에 프리모템 해줘", "실패 가정하고 점검해줘", "이 프로젝트 뭐가 잘못될 수 있을까",
  "시작하기 전에 리스크 점검해줘", "premortem this plan", "assume this fails, why", "what could go wrong before
  we commit", "pre-mortem analysis". The exercise only works with a specific certainty-framed failure
  prompt and independent-then-merged generation — a loose "what are the risks?" brainstorm is a
  different (weaker) exercise and should be named as such rather than called a premortem. Do NOT
  use it on a plan that has already been executed or irreversibly committed (that's a postmortem
  or retrospective, not a premortem), when there is no written plan at all yet, or when the user
  just wants a quick gut-check on one small reversible decision that doesn't warrant independent
  multi-lens generation and a full disposition table.
---

# Premortem

## First: does this even need the procedure?

Check these before running the full exercise, because forcing it where it doesn't fit wastes the user's time and misapplies the technique:

- **Is there a concrete plan with a decision point still ahead?** If the plan has already been executed, shipped, or irreversibly committed, this is a postmortem or retrospective question, not a premortem — say so and redirect.
- **Is there a written plan at all?** If there's nothing concrete yet — no scope, no steps, no decision on the table — there's nothing to premortem. Point back to whatever planning step is missing first.
- **Is the stake small and the decision easily reversible?** A single cheap, reversible call (e.g., which of two library functions to call today) doesn't warrant independent multi-lens generation and a disposition table. A quick "what's the obvious failure mode here" is enough, if anything.
- **Does the user want a loose risk brainstorm, not this specific exercise?** If they explicitly want an open "what risks do you see" conversation, that's a valid but different and weaker exercise (see Step 2) — do it if asked, but don't label it a premortem, since the certainty framing is what the evidence says actually works.

Everything below applies when there's a real plan, a real decision point still ahead, and enough at stake to warrant a structured failure exercise.

## Evidence grade — read before citing this to anyone

- **Confirmed, direct experimental evidence**: Veinott, Klein & Elliott (2010, ISCRAM), N=178, five conditions (baseline / critique / Pro-Con / Cons-only / premortem). The premortem condition reduced *self-reported plan confidence* significantly more than every other condition (mean reduction ≈25.0 points vs. ≈14.0 for Pro-Con and ≈12.4 for Cons-only — roughly 2x; all pairwise comparisons p<.05).
- **Limits on that result, state them every time this is cited**: the dependent variable measured was *self-reported confidence*, not plan quality or actual project outcomes — no study has measured whether premortems make plans better or projects more likely to succeed. Both key studies here are from the technique's creator's research circle (Klein is a co-author on the ISCRAM study).
- **Theoretical basis**: Mitchell, Russo & Pennington (1989). The commonly repeated "~30% more reasons generated" figure is real, but it belongs to *this* 1989 experiment, not to a premortem study — and the original result shows the active ingredient was the **certainty manipulation** (telling people the outcome has definitely happened), not future-vs-past time framing (time framing alone had no effect). It also measured only the *count* of reasons generated, not their quality. This is why Step 2 below is non-negotiable: soften the certainty framing and you're no longer running the thing that was shown to work. Never cite "30% more reasons" as a premortem-study finding — attribute it to the 1989 certainty experiment.
- **Grey literature, flag as such if cited**: a follow-up (SJDM 2020, N=53, d=.81 confidence reduction) exists only as an unpublished conference poster.
- **Base-rate honesty**: the researchers themselves note that controlled randomized experiments on plan-evaluation techniques are scarce. The technique's popularity (HBR 2007 origin, Kahneman's endorsement) outstrips its direct empirical base.
- **What this licenses you to say**: premortems are well-supported as a way to correct overconfidence — i.e., they reliably lower stated confidence more than alternative critique methods. They are NOT demonstrated to improve actual plan quality or project outcomes; no study has measured that. Say the first, do not imply the second.

## Procedure

### Step 1 — Scope gate

Confirm there is a concrete plan with a decision point still ahead — not yet irreversibly committed.

- **Gate**: already shipped/committed → exit, this is a postmortem/retrospective, say so. No written plan → exit, nothing to premortem yet. Otherwise, proceed.

### Step 2 — Certainty framing (the active ingredient — encode verbatim discipline)

Open the exercise with a fixed prompt that asserts failure as certain and already happened, e.g.:

> "It is [date, N months from now]. The plan was executed exactly as written. It has failed completely. Write down every reason you can think of for this failure."

Do not soften this into "what might go wrong?" or "what risks do you see?" — the 1989 evidence locates the effect specifically in the certainty manipulation, not in future/past tense or general risk-thinking.

- **Gate**: the prompt actually used asserts failure as CERTAIN and ALREADY HAPPENED (past tense, no hedging words like "might," "could," "risk"). A softened variant is recorded as a **procedure violation** — note it explicitly rather than silently running a weaker exercise under the premortem name.

### Step 3 — Independent silent generation

Before any discussion, merging, or cross-influence, each participant — or, when an agent runs this solo, each distinct perspective/lens (e.g., engineering, ops, customer, finance) — writes down at least 3 failure reasons independently.

- **Gate**: a per-participant or per-lens count of ≥3 reasons is recorded *before* aggregation begins. If any lens produced fewer than 3, note it as a gap rather than padding the list or quietly merging early.

### Step 4 — Aggregate and dedup

Combine all independently generated reasons into a single numbered failure-reason list.

- **Gate**: the list is numbered with a stated total count; duplicate or near-duplicate reasons across lenses are noted as duplicates (and what that convergence signals), not silently dropped.

### Step 5 — Disposition every reason

For each numbered reason, assign exactly one of:

- a **mitigation** with a **named owner**,
- a **detection signal** — the specific number, metric, or alert that would tell the team this failure mode is happening, or
- an explicit **accepted risk**, documented with who accepted it and why.

- **Gate**: every row in the list has exactly one of the three dispositions filled in. No blank dispositions, and no reason gets more than one disposition type (pick the one that actually applies — don't hedge by giving a reason both a mitigation and an "accepted" label).

### Step 6 — Confidence re-check

Record the team's or decision-maker's plan confidence as a number (e.g., 0–100) *before* the exercise and again *after* seeing the full disposed failure list.

- **Gate**: both numbers are recorded, with who gave them and when. This is the one effect the evidence actually supports — calibrating confidence — so measure exactly that rather than declaring the plan "better" or "safer."

## After the exercise

Report the before/after confidence numbers, the full disposition table, and any procedure violations from Step 2 or gaps from Step 3. Do not claim the plan is now more likely to succeed — the evidence supports confidence calibration, not outcome improvement. If confidence didn't move and the certainty framing (Step 2) was followed correctly, say that plainly rather than manufacturing a shift.
