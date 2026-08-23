---
name: diagnose-first
description: >-
  Use whenever the user wants to reduce a cost, speed something up, fix a recurring problem,
  decide between options, or figure out where to focus — a gated problem-solving procedure
  that forces diagnosis before action. Trigger on "our cloud bill is too high", "the app
  feels slow", "왜 자꾸 깨지는 거야", "which of these should we build first", "how do we make
  onboarding cheaper" — even when the user hasn't named a method and seems about to jump to
  a solution before locating the real cause. The whole point is to stop the reflex of acting
  on a guess: first locate where the cost/slowness/failure actually lives, verify the cause
  with objective criteria, then act on the part that matters. Do NOT use for pure execution
  tasks where the cause is already known and agreed, for creative/subjective work, or for
  outward-looking market, demand, and competitor questions (use market-recon — the external
  companion to this inward-looking skill).
---

# Diagnose First

## First: does this even need the procedure?

Two quick checks before you engage, because misapplying this skill wastes the user's time as surely as skipping diagnosis does:

- **Is the cause already confirmed and agreed?** If the user has correctly identified the cause and is asking you to *act* — "the regex rejects valid emails, fix it," "rename these files," "the query is missing an index, add it" — then just do the task. Do not read the reference files, do not run the stages, do not open with a diagnostic lecture. At most, add a one-line sanity check or flag a directly-related bug you notice. The whole value of diagnosis is locating an *unknown* cause; when the cause is known, diagnosis is theater.
- **Is this creative, subjective, or purely conversational?** Not this skill's job. Move on.

Everything below applies when the cause is genuinely unknown and the stakes justify finding it.

## What this skill is actually for

Acting on a guess is the expensive mistake — renegotiating a contract that's 3% of spend, rewriting a module that's 5% of latency. Amdahl's law makes it literal: fixing a part that's 5% of the whole caps your gain at 5%, however hard you work.

Here's the thing, though: you already know to diagnose before acting. On an open "should I do X?" question you'll naturally say "let's find where the problem is first" without any prompting. So this skill's job is **not** to make you deliver that generic sermon — you'd do that anyway, and if every answer opens with "stop, don't jump to solutions," it reads as a tic. Its job is to supply the part you tend to *skip*: the specific, named rigor that turns a vague "let's diagnose" into a decision someone can act on and check. Concretely, that's —

- **Quantifying the share** (Amdahl): not just "find the bottleneck" but "this candidate is what % of the total, so fixing it moves the whole by at most X" — the number that tells you whether it's even worth it.
- **Signal vs. noise**: is this swing real, or is it a small-sample wobble / a measurement artifact (a tracking change, seasonality) you'd be foolish to chase?
- **Reversibility**: is this a cheap-to-undo decision you should just test small, or a one-way door that earns real analysis?
- **Analysis vs. experiment**: some questions (market pricing, org-culture) can't be analyzed to an answer — recognizing that and switching to experiments is a judgment the default response misses.
- **Metric integrity** (Goodhart) and **sunk-cost exclusion**: the traps that quietly corrupt otherwise-good reasoning.

So lead with the *specific* diagnostic move for this problem and the rigor above, woven in naturally. The gates below are where that rigor lives.

**Opening rule (follow literally).** Your first sentence must do one of these two things: (a) acknowledge that the user's proposed option might genuinely be the right answer ("광고를 더 돌리는 게 답일 수도 있지만…"), or (b) state a specific, concrete fact about *their* problem (what the tool they named actually fixes, which funnel stage matters, what the number splits into). Never open by characterizing the user's thinking — no "잠깐만요", no "그건 결론이지 진단이 아니에요", no "지금 하려는 일은 추측에 근거한 결정입니다", no "you're jumping to a solution", and no lecture about expensive mistakes before you've said anything specific. The user should feel a sharp colleague picking up their problem, not a methodology being recited at them. The diagnosis-first substance stays; the sermon goes.

## The one rule that carries the most weight

**No improvement talk before measurement.** If you catch yourself (or the user) settling on what to fix before there's a baseline showing where the problem lives, get the measurement first. Deming's funnel experiment proved that adjusting a stable process on individual results makes variation *worse* — premature intervention isn't just wasteful, it can harm.

## Match the weight of your response to the weight of the problem

A factory delivery crisis and a "should I try Pomodoro?" question do not deserve the same ceremony. The gates are the same underlying logic, but a personal or low-stakes question should get a light, conversational pass — one or two sharp diagnostic questions and the single most relevant rigor check — not a six-stage essay. A high-stakes, expensive, or irreversible problem earns the full treatment. When unsure, err toward lighter: a crisp response that lands the one insight that matters beats a thorough one the user won't finish.

## Evidence grade

- **Amdahl's law** (Amdahl 1967): ●●● — mathematically derived; the improvement-from-optimizing-a-fraction formula is exact given correct input shares.
- **Pareto principle / 80-20 rule** (Juran 1951, operationalized from Pareto 1896): ●●○ — observed across many domains but not a law; the specific 80-20 split is an empirical regularity, not a theorem.
- **Deming's funnel experiment** (Deming 1982, *Out of the Crisis*): ●●● — demonstrated that adjusting a stable process on individual measurements increases variance; the experiment is replicable.
- **Cynefin framework** (Kurtz & Snowden 2003, *IBM Systems Journal*): ●●○ — qualitative classification framework developed through action research; the four-domain distinction is analytically useful but has not been experimentally validated as improving decision outcomes.
- **Cynefin's retrospective coherence claim** (Snowden 2000): ●●○ — the argument that complex-domain cause is only knowable in hindsight is a theoretical claim supported by case evidence, not experimentally proven.
- **Five Rules of Causation** (Six Sigma / root-cause analysis practice): ●○○ — practitioner consensus codified in quality-management literature; individually the rules are definitional ("state the cause without vague words") rather than empirically validated.
- **SMART goals** (Doran 1981, *Management Review*): ●●○ — widely adopted management practice; the framework is definitional, not outcome-validated.
- **RICE / WSJF prioritization**: ●○○ — practitioner heuristics with no outcome-validated studies; they make prioritization transparent but do not guarantee better results.
- **Little's law** (Little 1961): ●●● — mathematically proven for stable queueing systems; the application to development queues assumes the stationarity condition holds, which is often violated in practice.
- **Goodhart's law**: ●●○ — widely observed (the Campbell law generalization in social science); the mechanism is well-documented but the threshold at which a metric becomes "gamed" is case-specific.

Full gate criteria with evidence chains: `references/gate-criteria.md`.

## Is this a diagnosable problem, or a complex one?

Not every problem yields to analysis, and forcing analysis on the wrong kind wastes time. Do a 30-second classification (this is the Cynefin distinction; Kurtz & Snowden 2003):

- **Obvious / known** — you've seen it many times, the fix is established. Just apply the known fix; don't run this procedure.
- **Complicated** — cause-and-effect exists and expert analysis can find it. **This is what the procedure below is for.** Cost, latency, and quality problems usually live here.
- **Complex** — cause is only knowable in hindsight, not before (market reactions, org-culture change, novel product bets). Analysis won't produce the answer; **switch to the experiment track** — form a hypothesis, run a small safe-to-fail experiment, observe, repeat. Measurement (Stage 1) still applies.
- **Chaotic** — it's actively on fire. Stop the bleeding first, stabilize, then re-classify.

The litmus test between "complicated" and "complex": *would an expert analyzing this reliably produce the answer?* If yes, analyze. If the honest answer is "we can only tell in retrospect," experiment instead. **Escape hatch:** if you run the analysis track and fail to narrow the cause after two honest attempts, re-classify as complex and switch to experiments.

## The procedure

Each stage has a question and a gate. Advance only when the gate is satisfied. But treat these as the *complete* toolkit to draw from proportionally (per the weight-matching note above), not a form to fill out top-to-bottom on every problem — on a lighter question you might spend one sentence on Stage 0, skip straight to the one rigor check that matters, and stop.

**Reference-file rule (follow literally).** Do not read `references/` by default. Read them only when BOTH are true: (1) the problem is high-stakes — an expensive or hard-to-reverse decision, a safety issue, or a formal analysis someone will act on — AND (2) you actually need the precise test or method steps, not just the concept. A conversational "what should I do?" question never needs the references; everything required for those is already on this page. `references/gate-criteria.md` has the objective gate tests with evidence strength; `references/methods.md` has method how-tos (running a Pareto, a USE check, a decision matrix).

### Stage 0 — Define the problem

**Question: are we solving the right problem?**

Write the problem in one sentence with no solution and no blame in it. "The app is slow" — not "we need caching." Then challenge the frame, because a reframed problem can be an order of magnitude cheaper to solve: What's the hidden assumption? (slow = the machine is slow, or the *wait feels* long?) What's missing from this description? When does the problem *not* happen? Is this really the type of problem it looks like (a "communication problem" that's actually an incentive problem)?

Restate the goal in observable terms: **"move [metric] from [current] to [target] by [when], under [constraints]."**

**Gate G0:** the statement contains no solution/cause/blame; success is judged by a criterion a third party could check; stakeholders agree on the sentence. (Six Sigma problem-statement rules, SMART.)

### Stage 1 — Instrument and get a baseline

**Question: can we state the current situation in numbers?**

Pick the measurement that fits: profiling / tracing / USE or RED metrics for software speed; cost-driver analysis, activity-based costing, or FinOps dashboards for cost; defect-type counts for quality; direct observation and lead-time measurement for process. If the data doesn't exist, **install the instrumentation first** — diagnosing without data is just guessing with extra steps. Record the baseline; it's what you'll prove improvement against later. Keep a note of things that resist quantification (trust, morale) rather than dropping them.

**Gate G1:** the problem is reproduced/confirmed in data, and the baseline is written down. If measurement doesn't show the problem, go back to Stage 0 — the definition is probably wrong. (For software, beware coordinated omission and report p95/p99, not averages — see gate-criteria.)

### Stage 2 — Locate the bottleneck / root cause

**Question: which few causes drive the whole, and is there evidence?**

Three moves in order — **narrow, dig, verify.**

1. **Narrow (Pareto):** sort causes by their share of the total; take the vital few up to ~80% cumulative.
2. **Dig (structure + depth):** lay out candidate causes with an issue tree (MECE) or fishbone (the 6 Ms), then follow the strong branches down with 5 Whys until you reach the process layer. If the cause is murky, use an IS / IS-NOT contrast to eliminate.
3. **Verify (evidence):** brainstorming only produces hypotheses. Confirm each candidate against the four causal axes — did the cause precede the effect (temporality); does removing it make the problem vanish and reintroducing it bring it back (intervention / counterfactual — the strongest test); does one hypothesis explain both where it happens and where it *doesn't* (IS/IS-NOT); is the cause stated without vague words like "poor" or "inadequate" (Five Rules of Causation)?

Then the **Amdahl check:** what share of the whole does this cause carry, and how much can fixing it move the total? A 5%-share cause caps your gain at 5% — go find a bigger one.

**Gate G2:** the root cause is backed by evidence, not opinion; you can state quantitatively that removing it fixes/shrinks the problem; if multiple causes, each one's contribution is estimated. Note honestly that complex failures rarely have a single root cause — the real target is often "a set of jointly-sufficient necessary causes." Before attributing a cause to a swing in the numbers, confirm the swing is a real signal, not noise (control-chart 3-sigma / special-cause rules — see gate-criteria).

### Stage 3 — Generate and choose options

**Question: is this decision reversible, and which option has the best expected value?**

Generate options widely; if convention blocks you, decompose to first principles (what's the material cost floor?) and try inversion (what would reliably make this *worse*? — then avoid that). Then classify the decision's weight:

- **Reversible (two-way door):** stop analyzing and just try it, small, and read the data. Bringing a heavy decision matrix here *is* the analysis paralysis.
- **Irreversible (one-way door):** compare options by expected value (Σ outcome×probability − cost), or a weighted decision matrix for multiple criteria. **Exclude sunk costs**; count only future costs and opportunity cost. Run a pre-mortem ("it's six months later and this failed — why?"). Write the rollback plan.

**Gate G3:** the decision is classified one-way vs two-way and the rigor matches its weight; the rationale is documented so it can be reviewed later; sunk cost does not appear in the argument ("we've come this far" is a gate violation). Decide *when* to stop analyzing with value-of-information: only gather more if the expected value of that information exceeds its cost.

### Stage 4 — Prioritize and execute

**Question: what first, with how much resource?**

If there are several actions, score them — RICE (reach×impact×confidence÷effort) or WSJF (cost of delay ÷ size) — so short, high-impact work naturally rises. Do the quick wins (high value, low effort) first for early trust and learning. Apply the Theory-of-Constraints discipline: **don't spend resources anywhere but the bottleneck.** Exploit it with what you have before you invest in enlarging it. Bake the re-measurement point and owner into the plan — "fix it and move on" isn't in this procedure. Expect to overvalue impact and undervalue effort (planning fallacy); buffer estimates accordingly.

### Stage 5 — Re-measure and loop

**Question: did it actually improve, and where's the next bottleneck?**

Re-measure with the *same metric and method* as the baseline. Then branch: **target met** → lock the gain in as a standard (regression guard, automation, docs) and record what you learned; **improved but short** → the constraint has probably moved, go back to Stage 1 and find the new one (Theory of Constraints: beware inertia — don't assume last time's bottleneck is still the bottleneck); **no improvement** → the Stage 2 cause was wrong, widen the candidates and redo it. Leave slack in the system — targeting 100% utilization makes queue time explode (Little's law).

## The five standing disciplines

These apply at every stage, not just one:

1. **No improvement before measurement.** Baseline-free improvement talk gets stopped.
2. **Sunk cost is never an argument.** "We've already spent so much" is banned reasoning.
3. **Check the share first.** For any proposed fix, ask "what percent of the whole is that?" before anything else.
4. **Manage what you can't measure, too.** Trust, morale, long-term strategy don't show up in the dashboard — track them qualitatively. The moment someone games a metric to hit a target while harming the goal, the procedure has failed (Goodhart's law).
5. **Write it down.** Problem statement, baseline, cause evidence, decision rationale, re-measurement — these five make the next problem faster to solve. One A3 page is enough.

## An honest caveat about the criteria

The gate criteria in `references/gate-criteria.md` are graded by evidence strength (●●● peer-reviewed + quantitative, down to ●○○ management folklore). Two things to keep in mind. First, the strengths differ — causal inference, statistical process control, and value-of-information are solid; some decision heuristics are just well-traveled sayings. Second, even the most rigorous criteria explicitly refuse mechanical application (the measurement-systems manual and the American Statistical Association both warn against judging by a single number). So these criteria don't replace judgment — they make judgment transparent and reviewable. Record *which* criterion you used and how confident it is, so that when a call turns out wrong, the procedure can learn. That reviewability is the real product.