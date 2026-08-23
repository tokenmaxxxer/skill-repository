---
name: flow-metrics
description: >-
  Use whenever the user wants to understand, measure, or diagnose work flow. A
  flow-measurement diagnostic that defines WIP, throughput, and lead time over one
  consistent boundary and applies Little's law (L = λW) correctly, with its actual stated
  conditions — then reports honestly what the evidence does and does not support about WIP
  limits (in the one quantitative case study available, neither direction is a controlled
  result). Trigger on "왜 이렇게 오래 걸리지", "리드타임 계산해줘", "why is this taking so long", "should we
  set a WIP limit", "diagnose our kanban board". Do NOT use when there is no per-item
  entry/exit timestamp data (the first action is instrumenting start/finish events), when
  the question is about individual performance rather than a system's flow, or when the team
  has already decided to change a WIP limit (use hypothesis-testing).
---

# Flow Metrics

## First: does this even need the procedure?

Check these before computing anything, because forcing the procedure where it doesn't fit wastes the user's time:

- **Is there a recorded entry and exit timestamp for each item (or an equivalent event log)?** If work items have no logged "started" and "finished" events — just a board people eyeball — there is nothing to measure yet. Exit and say so plainly: the first action is instrumenting item start/finish, not computing a metric. Don't estimate WIP or lead time from memory or a screenshot of the board.
- **Is this actually a question about a person, not a system?** "Why is this ONE developer slow" is a performance-management question, not a flow-measurement question. This skill measures a system's flow — exit and redirect if the ask is really about an individual.
- **Has the WIP-limit decision already been made, and does the user just want to know if it worked?** That's an intervention evaluation, not a diagnosis. Point to `hypothesis-testing` for the before/after check with a pre-committed metric and threshold, rather than re-running this diagnostic to retroactively justify a decision already shipped.
- **Does the user just want the popular claim confirmed ("lowering WIP boosts productivity, right?")?** Don't just agree. The evidence base for this skill exists specifically because that claim is not supported — say so up front rather than after being asked to compute something.

Everything below applies when there's real event-log data (or a real willingness to start collecting it) and an actual flow question on the table.

## Evidence grade — read before citing this to anyone

Grade honestly, and lead with the strongest fact, not the weakest:

- **Little's law is a mathematical theorem** — the strongest evidence grade in this registry, proved rather than surveyed. John D.C. Little proved it in 1961 ("A proof for the queuing formula: L = λW", *Operations Research* 9(3), pp. 383–387). It comes with explicitly stated conditions (below) and a **general form that holds under nonstationary conditions and independent of queue discipline** — the theorem itself is not in question.
- **The software-practice evidence is far weaker.** The first quantitative case study of WIP effects on kanban team performance examined data on more than 8,000 work items developed over four years by five teams **in one software company**. It found:
  - lower WIP correlates with shorter lead times — consistent with what Little's-law-style reasoning would predict.
  - WIP **also** correlates with productivity, but in a direction **inconsistent** with the kanban literature's claim that a low (but above-threshold) WIP improves productivity. The case-study evidence does **not** support "lower WIP → better productivity"; it supports "lower WIP → shorter lead time" only.
- **Industry case-study data (non-experimental, before/after, not a controlled experiment):** BBC Worldwide reported lead time improved 37%, delivery consistency rose 47%, and customer-reported defects fell 24% after kanban/WIP-limit adoption. Useful as a data point, not as causal proof.
- **There is no controlled experiment showing WIP limits improve productivity.** Do not imply one exists.
- **This skill makes no historical claims about kanban's origin.** The commonly told origin story did not survive verification here, so it is deliberately omitted — don't reach for it to add color.
- **No column-by-column WIP-limit-setting formula is verified.** Never invent a recommended WIP number or a universal formula for "what your WIP limit should be."

## Procedure

### Step 1 — Scope gate

Confirm the work stream has recorded per-item entry and exit timestamps (or an equivalent event log covering the same items).

**Gate:** either you can point to the actual log/data source with entry and exit events, or you cannot. If you cannot, stop here and tell the user the first action is instrumenting item start/finish — do not proceed to compute a metric from partial or eyeballed data. Also stop here (redirect instead) if the question is really about one person's performance, not the system's flow.

### Step 2 — Boundary and window definition

Write down, in one place, **one** system boundary (what event counts as entry, what event counts as exit) and **one** measurement window (start date to end date). Then define, using that single boundary and window:

- **WIP (L)** = mean number of items inside the boundary during the window.
- **λ** = the **arrival** rate — per Little's 1961 definitions, `1/λ` is the mean time between arrivals of two consecutive units, so λ counts items crossing the **entry** event per unit time. Throughput measured at the exit is a *substitute* for λ, valid only when arrivals ≈ departures over the window.
- **Lead time (W)** = mean time a unit spends inside the boundary. Averaging only over items that *exited* during the window is a distinct estimator that carries survivorship bias when the system is not in balance — long-running items still inside are excluded from it.

**Gate:** all three definitions cite the same boundary and the same window, in writing. Additionally, record the **entry count** and the **exit count** over the window, and state explicitly whether the "arrivals ≈ departures" assumption holds — using exit-side throughput as λ, or exiters-only averaging for W, is permitted only with that assumption written down and checked. If the counts diverge, say so and treat the λW cross-check in Step 3 as weakened, not as confirmation. If any of the three was actually computed over a different boundary or window (e.g., WIP from today's snapshot but lead time from last quarter's closed tickets), it must be recomputed or dropped — mixing scopes is the classic misuse this step exists to prevent.

### Step 3 — Compute and cross-check with Little's law

Write down a **reconciliation tolerance before computing** (e.g. "|L − λW| / L ≤ 10%"), then compute WIP (L), λ, and lead time (W) independently from the data and check L ≈ λW.

**Gate:** show the three measured numbers and the λW product side by side, with the discrepancy stated as a number or percentage. The gate is mechanical: **if |L − λW| / L exceeds the pre-stated tolerance, stop and investigate the data; if no tolerance was pre-stated before computing, the gate fails** — a tolerance chosen after seeing the discrepancy is not a check. A discrepancy is a **measurement signal, not a physics violation** — it means the boundary or window disagree somewhere (e.g., items counted at entry but some never logged an exit). Note the blind spot named in Step 2: if λ was taken from the exit side and W averaged over exiters only, an entry/exit logging asymmetry cancels out of both and this cross-check will not see it — only L is left exposed, so the entry/exit counts recorded in Step 2 are what catch that case.

### Step 4 — Conditions statement

State precisely which form of Little's law is being invoked:

- The **original 1961 proof** requires three conditions for L = λW: (1) the three means are finite, (2) the corresponding stochastic processes are strictly stationary, (3) the arrival process is metrically transitive with nonzero mean.
- The **general form** of the law holds under nonstationary conditions and independent of queue discipline. Its full condition set is *not characterized by this skill's evidence base* — do not assert conditions for it in either direction. The finiteness / strict-stationarity / metric-transitivity triple belongs to the 1961 proof and must be cited as such, not transplanted onto the general form.

**Gate:** the report names which form is being invoked and does not claim conditions this skill's evidence base did not verify (e.g., do not assert "Little's law requires a stable system" as a blanket rule, and do not assert "conditions never matter" either — both collapse the nuance).

### Step 5 — Diagnosis, evidence-bounded

Report the flow picture: WIP, throughput, lead time, and their trend across the window.

If asked whether to lower WIP, the answer this skill is licensed to give: the case-study evidence associates lower WIP with **shorter lead time**, and does **not** support the common claim that lower WIP improves **productivity** — that expectation was contradicted by the same case-study data.

**Gate:** any WIP recommendation names which outcome it targets (lead time vs. productivity) and carries the evidence grade for *that specific outcome*. A recommendation that promises productivity gains from lowering WIP fails this gate and must be rewritten or dropped.

### Step 6 — If the team wants to change WIP limits

Treat a WIP-limit change as an intervention with an expected effect, not a foregone conclusion. Route the before/after evaluation to `hypothesis-testing`: pre-register the target metric (e.g., lead time, not productivity, unless a productivity claim is separately and honestly justified) and its threshold before the change ships.

**Gate:** the target metric and its numeric threshold are written down and committed **before** the WIP change goes live. A post-hoc chart produced after the change, with no pre-committed threshold, does not satisfy this gate — it is not evidence of the change's effect, only a description of what happened.
