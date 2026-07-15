---
name: premature-scaling
description: >-
  A stage-alignment diagnostic that detects premature scaling: acting (hiring, spending,
  building) ahead of what validated traction actually supports. Use this whenever the user is
  weighing whether to scale up — e.g. "지금 확장해도 될까", "팀 늘려도 되나", "스케일업 시점 점검", "이 시점에
  채용해도 될까", "펀딩 받은 김에 마케팅 늘려도 될까", "should we scale now", "is it too early to hire/spend/build
  this much", "are we scaling too fast", "premature scaling check". The diagnosis is a set of
  numeric comparisons between measured traction and measured action across five controllable
  dimensions — not a vibes-based "does this feel too early" judgment call. Do NOT use it when
  there is no traction data at all yet and no willingness to produce any (that's a discovery
  problem, not a scaling problem — point to user-discovery instead), when the user has already
  validated traction and is just asking for execution help (just do the task), or for a single
  small, cheap, reversible action that doesn't warrant a five-dimension audit.
---

# Premature Scaling

## First: does this even need the procedure?

Check these before running the full comparison, because forcing it where it doesn't fit wastes the user's time:

- **Is there any traction data at all, even rough?** If the product hasn't launched or has zero users and the user isn't willing to produce any numbers, this isn't a scaling question yet — it's a discovery or validation question. Say so and point to `user-discovery` or `diagnose-first` rather than running a comparison against nothing.
- **Has traction already been validated and the user is just asking you to execute?** "We hit 40% W1 retention and are past our committed threshold, help me write the hiring plan" — just do the task. Don't re-run the diagnostic on a decision that's already been made with evidence.
- **Is the action tiny, cheap, and reversible?** One contractor for a month, a $500 ad test. A full five-dimension audit is overkill; a single quick comparison on the one relevant dimension is enough, if any.
- **Is the user asking for a feelings check, not a numbers check?** If they want "does this feel too early" with no numbers offered or obtainable, say plainly that this skill can't answer that — the entire value of the procedure is that it reduces to numeric comparisons. Ask for the numbers or decline to guess.

Everything below applies when there's a real scale-up decision on the table, real stakes, and at least some traction data can be measured or is worth measuring.

## The hard rule

Every diagnosis in this skill reduces to a comparison between two measured columns: the ACTUAL stage (traction) and the ACTION stage (what's being done or planned). No dimension gets a flag based on impression. If a number can't be produced, the dimension is recorded as **"unmeasured"** — and unmeasured is not a free pass. It blocks a confident scaling decision on that dimension exactly as surely as a bad number would; the honest output is "we don't know yet," not "probably fine."

## Evidence grade — read before citing this to anyone

The empirical base for this procedure is the **Startup Genome report (2011)**, a study of roughly 3,200 high-growth internet startups. It found that about 70% of these startups scaled prematurely on at least one of five dimensions, and the report attributes 74% of startup failures to premature scaling.

Grade this correctly:

- This is a **non-peer-reviewed industry report** with self-reported survey data, documented survivorship-bias critique, and a commercial interest (the authors sell a scaling-diagnostic product). Treat it as **industry-adoption evidence, not academic validation** — on the same footing as a vendor benchmark, not a replicated experiment.
- The behavioral signatures the report measured (e.g., markedly more code written during the discovery stage, larger teams at the same stage compared to well-scaled peers) survived independent verification only at **medium confidence**. Present them as **indicative patterns worth noticing**, never as fixed numeric thresholds ("3x more code" is not a rule to enforce).
- **Never present the 74% failure-attribution figure or similar headline percentages as causal proof** that premature scaling causes failure at that rate. They are a single non-peer-reviewed report's own attribution, not an independently established causal estimate.
- The actual value this skill delivers is **the comparison structure** — actual-stage numbers vs. action-stage numbers, dimension by dimension, with a pre-committed re-test threshold. That structure is checkable and useful regardless of whether the report's exact percentages replicate. Lead with that, not with the percentages.

## Procedure

### Step 1 — Measure the ACTUAL stage (traction)

Get or compute each of the following as a **number with a measurement date**:

- **Active users** (count, over what window, as of what date)
- **Activation rate** (% of signups reaching the defined "activated" action)
- **Retention**, as a cohort figure (e.g., W1/W4 retention %, or a specific cohort's Day-30 return rate) — not a vague "people seem to stick around"
- **Revenue / MRR** (current number, trend)
- **Product-market-fit signal** — a measured proxy, e.g. Sean Ellis "very disappointed" %, organic/referral share of growth, or an equivalent number the user already tracks

If any metric has no number behind it, write **"unmeasured"** next to it rather than estimating or skipping it. Note the date of measurement for everything — traction six months old is not current traction.

### Step 2 — Measure the ACTION stage (five controllable dimensions)

Using the Startup Genome framing, get a number for each:

| Dimension | What to measure |
|---|---|
| Customer acquisition | Paid CAC spend — $ committed or spent per month on paid acquisition |
| Product | Feature/code volume vs. validated demand — e.g., number of major features shipped or planned vs. number of user problems actually validated |
| Team | Headcount now, headcount planned, and hiring timeline |
| Business model | Monetization commitments — contracts signed, pricing commitments made, revenue guarantees given to anyone |
| Financials | Burn rate ($/month) and raise size (raised or being raised) |

Same rule as Step 1: no number, no vibes-based fill-in — record "unmeasured."

### Step 3 — Compare, dimension by dimension

For each of the five dimensions, ask: **is this action level justified by the Step 1 numbers?** Output one flag per dimension:

- **ALIGNED** — the action level matches what the traction numbers support.
- **AHEAD** — action outruns traction. This flag is only valid if you can name *which specific traction number is missing, unmeasured, or too low* to justify the action. "Feels aggressive" is not a valid AHEAD justification; "W4 retention is unmeasured, so committing to 10 new sales hires has no traction backing it" is.
- **BEHIND** — traction supports more action than is currently being taken (worth noting, though it's not the failure mode this skill targets).

Do not average the five flags into one score. A single AHEAD dimension is not cancelled out by four ALIGNED ones — each dimension has its own consequence (over-hiring doesn't get fixed by good retention).

### Step 4 — Verdict

For every dimension flagged AHEAD:

1. State what to **freeze or defer** on that dimension specifically (e.g., "pause the next 3 planned hires," "cut paid CAC spend by X until...").
2. State the **traction threshold that unlocks it** — a specific number the user commits to *in advance*, not after the fact ("resume hiring once W4 retention is measured and clears 25%," not "once things feel more stable"). This pre-committed number is the objective re-test criterion — write it down now, so the re-test later isn't quietly re-negotiated in the moment.

If every dimension is ALIGNED or BEHIND, say so plainly — this skill's job is also to *not* manufacture a problem where the numbers don't support one.
