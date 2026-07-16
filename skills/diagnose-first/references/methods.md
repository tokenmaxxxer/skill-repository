# Method Details — how to actually run each tool

The procedure names methods; this file is the how-to. Read the entry you need when you reach the stage that uses it. Methods are grouped by stage.

## Stage 0 — Framing

**Problem reframing.** Four questions on the problem statement: (1) What's the hidden assumption? (2) What's missing from this description? (3) When does the problem *not* occur (positive exceptions)? (4) Is the problem type mis-identified? Classic case: tenants complained the elevator was slow; the real problem was perceived wait time, and the fix was mirrors, not a new motor — an order of magnitude cheaper.

## Stage 1 — Instrumentation

**Software speed:**
- **Profiling / tracing** — flame graphs to find the code paths eating CPU time; distributed tracing to find latency across services (look for spans >100ms, error-flagged spans, N+1 repeated calls).
- **USE method** (per resource — CPU, memory, disk, network): check **U**tilization, **S**aturation (queued excess work), **E**rrors. Finds ~80% of infra problems with a short checklist. Start from "which resource is the problem?" not "what does my tool show?"
- **RED method** (per request-based service): **R**ate, **E**rrors, **D**uration. USE is machine-side; RED is user-side.
- **Golden Signals** (Google SRE): Latency, Traffic, Errors, Saturation.

**Cost:**
- **Cost-driver analysis / Activity-Based Costing** — attribute cost to the activities that actually consume resources, by causal driver, instead of spreading overhead evenly.
- **FinOps** — Inform → Optimize → Operate. The first step is *visibility*: real-time cost dashboards and strict tagging. "Waiting for the monthly report is a prescription for financial disaster" — make cost visible before optimizing.

**Quality:** defect-type counts; validate the measurement system (DMAIC's Measure).

**Process:** go and observe directly (genchi genbutsu); value-stream map; measure lead time and wait time.

## Stage 2 — Bottleneck / root cause

**Pareto (narrow).** Collect frequency (or cost/loss) per cause, sort descending, plot bars + cumulative % line, identify the vital few up to ~80% cumulative, concentrate there. 80/20 is an approximation, not a law.

**Issue tree / MECE (structure).** Break the problem into branches that are Mutually Exclusive and Collectively Exhaustive. E.g. profit = revenue (price × volume) − cost (fixed + variable); subdivide each branch.

**Fishbone / 6 Ms (structure).** Categories: Materials, Machinery, Methods, Measurement, Manpower, Mother-nature (+ Money). Brainstorm causes under each, then push the strong ones down with 5 Whys.

**5 Whys (depth).** Ask "why?" repeatedly down the causal chain to the *process* layer (why was there no guard against this?), not the symptom layer. Limits: the 5th answer isn't guaranteed to be the root; you can't find causes outside your own knowledge; different investigators reach different answers. It's a starting point, not a verdict — always pair with evidence verification.

**IS / IS-NOT (elimination).** Lay out what/where/when/extent the problem IS vs IS-NOT (situations where it could have occurred but didn't), derive the distinctions, and test each hypothesis against both columns. A cause that can't explain the IS-NOT is rejected.

**Theory of Constraints (system framing).** Every system has one throughput-limiting constraint; improving anywhere else is waste. Five steps: Identify the constraint → Exploit it (max it out with current resources) → Subordinate everything else to it → Elevate (add capacity) only if still needed → repeat, and beware inertia when the constraint moves. Same idea as Liebig's law of the minimum: growth is set by the scarcest input; a chain is only as strong as its weakest link.

## Stage 3 — Decision

**First-principles thinking.** Decompose to irreducible facts, separating what's truly known from assumed. Musk's battery example: instead of "battery packs are expensive," he priced the raw materials and found material cost was ~$80/kWh vs the ~$600 going rate — the gap was manufacturing inefficiency, not physics.

**Inversion.** Instead of "how do we succeed?", ask "what would reliably make this worse?" and avoid that.

**Expected value / decision tree.** For each option: EV = Σ(outcome × probability) − cost. A higher-cost option can have the best EV — judging by visible cost alone misleads.

**Weighted decision matrix (Pugh).** Criteria with weights on one axis, options on the other; score each option × weight, sum. The top score is a leading candidate, not an automatic verdict.

**Sunk cost / opportunity cost / marginal analysis.** Only future costs and benefits count; ignore money already spent. Compare options by what you'd give up (opportunity cost) and the added cost/benefit of one more unit (marginal).

**Type 1 vs Type 2 decisions (Bezos).** One-way door (hard/costly to reverse) → deep analysis. Two-way door (cheap to reverse) → skip the analysis, just experiment. The criterion is reversal cost, not absolute reversibility.

**Pre-mortem.** Assume the decision failed six months out; each person independently lists why; fold the risks into the plan. Bypasses the org pressure against voicing doubts.

## Stage 4 — Prioritization

**RICE:** (Reach × Impact × Confidence) ÷ Effort. Quantifies total impact per unit of work.
**ICE:** Impact × Confidence × Ease (lighter than RICE, 1–10 each).
**WSJF:** Cost of Delay ÷ Job Size. Surfaces short, high-impact work; auto-ignores sunk cost.
**MoSCoW:** Must / Should / Could / Won't — a shared language for in/out of scope.
**Value vs Effort 2×2:** the high-value/low-effort quadrant is the quick wins.
Common trap: people overvalue impact and undervalue effort (planning fallacy). Scores reduce arguments; they aren't mechanical verdicts.

## Stage 5 — Standardize

**DMAIC's Control / PDCA's Act.** Lock the gain in: regression guards, poka-yoke (mistake-proofing), automation, updated standard operating procedure and docs, continued measurement. The constraint moves after you fix one — re-enter the loop rather than assuming the old bottleneck still binds.

**Little's law (leave slack).** L = λW. Queue time explodes as utilization approaches 100% — at 80%+ it degrades sharply and p99 blows up on small load increases. Plan for headroom, not full utilization.