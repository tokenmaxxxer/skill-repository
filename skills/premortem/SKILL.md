---
name: premortem
description: >-
  Use whenever the user wants to pressure-test a written plan BEFORE committing to it: assume the
  plan has already failed, gather reasons independently, then convert every reason into a
  mitigation, a detection signal, or an explicit accepted risk. Trigger on requests like "이 계획 시작
  전에 프리모템 해줘", "실패 가정하고 점검해줘", "premortem this plan", "assume this fails, why", "what could go
  wrong before we commit". The exercise only works with a specific certainty-framed failure prompt
  and independent-then-merged reason gathering — a loose "what are the risks?" brainstorm is a
  different exercise. Do NOT use on a plan already executed or irreversibly committed (use
  blameless-postmortem), when there is no written plan at all, or for a quick gut-check on a small
  reversible decision that doesn't warrant a full disposition table.
---

# Premortem

## First: does this even need the procedure?

Check these before running the full exercise, because forcing it where it doesn't fit wastes the user's time and misapplies the technique:

- **Is there a concrete plan with a decision point still ahead?** If the plan has already been executed, shipped, or irreversibly committed, this is a postmortem or retrospective question, not a premortem — say so and redirect.
- **Is there a written plan at all?** If there's nothing concrete yet — no scope, no steps, no decision on the table — there's nothing to premortem. Point back to whatever planning step is missing first.
- **Is the stake small and the decision easily reversible?** A single cheap, reversible call (e.g., which of two library functions to call today) doesn't warrant independent multi-lens generation and a disposition table. A quick "what's the obvious failure mode here" is enough, if anything.
- **Does the user want a loose risk brainstorm, not this specific exercise?** If they explicitly want an open "what risks do you see" conversation, that's a valid but different and weaker exercise (see Step 2) — do it if asked, but don't label it a premortem, since the certainty framing is what the evidence says actually works.

Everything below applies when there's a real plan, a real decision point still ahead, and enough at stake to warrant a structured failure exercise.

## Evidence grade

For full evidence grading — the ISCRAM 2010 experimental result, its limits, the 1989 certainty-manipulation basis, and what this technique does and does not license you to say — see [references/evidence.md](references/evidence.md). In short: premortems are well-supported for correcting overconfidence, not demonstrated to improve plan quality or project outcomes. Say the first, do not imply the second.

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

### Step 5 — Triage by impact × plausibility

Before writing dispositions, classify each failure reason from Step 4 on two axes:

- **Impact**: high (would materially compromise the plan's objective or cause user-visible harm) vs. low (inconvenience, delay, or contained cost).
- **Plausibility**: high (a concrete path from today's plan to this failure exists with no improbable leaps) vs. low (requires multiple unlikely events or a cascade this plan specifically guards against).

Assign each reason to one tier:

- **High tier** (high impact AND high plausibility): requires full disposition in Step 6 — mitigation with named owner, a specific detection signal, and the accepted-risk declaration if mitigation is impractical.
- **Medium tier** (high impact OR high plausibility, but not both): record a disposition label only — which of mitigation/detection/accepted-risk applies, with a one-line justification. No named owner or detailed signal required.
- **Low tier** (low impact AND low plausibility): do not individually disposition. Aggregate them as "N low-tier reasons noted (impact low, plausibility low), not individually dispositioned."

- **Gate**: every reason from Step 4 is classified into one of the three tiers before any disposition text is written. The tier assignment — not the disposition content — is the first gate output.

### Step 6 — Disposition (by tier)

For each high-tier reason, assign all three: a **mitigation** with a **named owner**, a **detection signal** (the specific number, metric, or alert that would tell the team this failure mode is happening), and an explicit **accepted risk** (documented with who accepted it and why) as the fallback.

For each medium-tier reason, assign a **disposition label** only — mitigation, detection signal, or accepted risk — with a one-line justification.

For low-tier reasons, output the aggregate count only (see Step 5).

- **Gate**: every high-tier reason has all three disposition elements (mitigation+owner, detection signal, accepted-risk fallback). Every medium-tier reason has a disposition label with one-line justification. Low-tier reasons are aggregated, not individually dispositioned. No reason spans more than one tier.

### Step 7 — Confidence re-check

Record the team's or decision-maker's plan confidence as a number (e.g., 0–100) *before* the exercise and again *after* seeing the full disposed failure list.

- **Gate**: both numbers are recorded, with who gave them and when. This is the one effect the evidence actually supports — calibrating confidence — so measure exactly that rather than declaring the plan "better" or "safer." For decisions where the confidence re-check triggers a go/kill/pivot/persist call, route to `hypothesis-testing` to pre-register the metric and threshold before acting on the revised confidence number.

## After the exercise

Report the before/after confidence numbers, the tiered disposition output (high-tier full dispositions, medium-tier labels, low-tier aggregate), and any procedure violations from Step 2 or gaps from Step 3. Do not claim the plan is now more likely to succeed — the evidence supports confidence calibration, not outcome improvement. If confidence didn't move and the certainty framing (Step 2) was followed correctly, say that plainly rather than manufacturing a shift.
