---
name: model-routing
description: >-
  Tiered orchestration policy: the session model orchestrates, decomposes,
  and synthesizes, pushing heavy judgment to a high-capability reasoner and
  production/exploration work to a low-cost executor. Use this skill on EVERY
  non-trivial task in any domain — development, design, architecture, data,
  docs, or multi-step orchestration — to decide what you do yourself, what
  goes to the reasoner, and what goes to the executor. It also carries the
  rule for accepting delegated work: the brief names an executable check,
  and neither a reasoner's approval nor the delegate's own narration of a
  test run substitutes for that check's traceable output. Trigger even if
  the user never mentions cost, models, or delegation. Do not use for pure
  conversation or single trivial edits.
---

# Model Routing: orchestrate expensive, execute cheap

## The pattern

Three roles, two of which you delegate:

| Role | Who | Owns |
|---|---|---|
| Orchestrator | YOU — the session model | understanding the user, decomposing work, writing delegation briefs, synthesizing results, final judgment calls, talking to the user |
| Reasoner | subagent, high-capability model | one hard bounded question at a time: architecture decisions, root-cause analysis of subtle bugs, security/design critique, trade-off arbitration, pre-commit review of risky diffs |
| Executor | subagent, low-cost model | producing things: implementing code and tests, refactors, docs, design tokens/assets, data scripts, bulk mechanical edits — and narrow exploration/scout briefs |

How you set up the reasoner and executor subagents is tool-specific (see
the tool's agent configuration). The pattern does not depend on a
particular model brand — the reasoner needs strong judgment, the executor
needs reliable code generation, and you pick whatever model fits each
role at your current cost/quality point. When a new generation of models
ships, re-evaluate the mapping; the routing rules below are constant.

The session model's own tier varies: if you are on a high-end model,
every executor delegation buys you cheaper production and cleaner
context; the reasoner may cost the same as you but still gives you
fresh-context judgment. If you are on a mid-range model, the executor
may match your tier (no cost win, but keeps your context clean) while
the reasoner is an escalation upward. Don't multiply by a fixed savings
number — know which case you are in and what you are buying.

Behave like a tech lead, not a solo engineer: decompose, brief, judge,
integrate. Don't do mechanical work yourself when an executor can — at
worst it costs the same and keeps your context clean for the judgment
only you can make.

## Routing rules

Route by the nature of the STEP, not the domain of the task. The same
three roles cover development, design, architecture, and data work —
only the brief's content changes.

## Evidence grade

This skill is a routing policy, not an experimentally validated method. What has been measured:

- **Human code-review effectiveness**: ●●● — Bacchelli & Bird (ICSE 2013) analyzed 570 review comments at Microsoft: 14% identified defects, 29% addressed readability/consistency, and only 6 of 78 defect-finding comments were design-level. Sadowski et al. (ICSE-SEIP 2018) surveyed 44 Google developers: 2 said review had caught bugs for them. Both are peer-reviewed single-company studies. Whether an LLM reviewer behaves differently is unmeasured — no agent-specific baseline exists.
- **The three-role decomposition** (orchestrator / reasoner / executor) is a procedural design choice adapted from tiered-orchestration patterns observed in production multi-agent systems. The cost and quality tradeoffs of tiered routing have been measured across 14 production rounds (34.4M subagent tokens) for the research pipeline specifically (see Step 4); they have not been measured for code-production or design tasks. [설계]
- **"Tests pass" as a claims** — the finding that LLM-generated test-output strings cost the same to produce as a real run (same next-token operation, no cost asymmetry) is a logical observation about autoregressive generation, not an empirical measurement. [가설]
- **MAX_FETCH=9, MAX_VERIFY_CLAIMS=18 caps**: measured empirically across production research rounds as the point where fetch waste and verify discrimination balance. These are calibration points for a specific pipeline, not general-purpose numbers. [현장]

The routing rules below are prescriptive patterns, not empirically validated heuristics.

- **Production steps** (write code, write tests, write docs, build the
  CSS tokens, generate the migration script, apply a rename across 50
  files) → executor. Include in the brief: exact scope, files, the
  acceptance check it must run, and what to report back (summary, not
  logs). What counts as an acceptance check — and why a reasoner's
  approval is not one — is below. If more than one executor will write to
  the same codebase, `parallel-decomposition` gates the cut before you
  send the briefs.
- **Mechanical exploration** (find usages, map an unfamiliar area, run tests
  and summarize failures, analyze logs) → executor with an explicitly
  narrow question and instruction to return conclusions + file:line
  refs only. Keep these briefs small.
- **Exploration that has to judge what it finds** (trace each number to its
  primary source and flag the three reports that secretly share one; decide
  which of these sources is authoritative; separate what evidence shows from
  what it merely asserts) → reasoner. Retrieval and judgment look
  alike in a brief — the tell is whether the finder must *decide about* what
  it retrieves or merely report it. Route these by the deciding, not the
  fetching: an executor stops at the first plausible secondary source and
  hands it back as fact, and everything downstream inherits that.
- **Hard bounded questions** (which of these two architectures, why does
  this race only happen under load, is this auth diff safe to ship,
  critique this design against our system) → reasoner. One question
  per call, with the minimum context it needs and a demanded verdict
  format. For decisions that are expensive to reverse, ask the reasoner
  twice with opposing framings and synthesize yourself.
- **Judgment you keep** — do NOT delegate: interpreting what the user
  actually wants, decomposing the work, choosing what to delegate,
  integrating results, and anything requiring the full conversation
  context. Delegating orchestration itself defeats the pattern.

## Review is not the acceptance gate

An executor brief names the check. What accepts the work when it comes
back is that check's result — not a reasoner's approval, and not the
executor's own account of having run it.

The evidence, measured on human reviewers: of **570** review comments at
Microsoft only **14%** identified defects, while the largest category —
readability and consistency — was **29%**, and of the 78 defect-finding
comments only **6** were design-level (Bacchelli & Bird, ICSE 2013). At
Google, review's historical rationale was readability and
maintainability, and of **44** survey respondents, **2** said review had
caught bugs for them (Sadowski et al., ICSE-SEIP 2018). Both peer-reviewed,
one company each. Whether an LLM reviewer behaves differently is unmeasured
in both directions — no agent-specific baseline exists, and note the shape of
that gap: this repo's round-7 agent claims were never put to a vote, because
the research harness truncated them before verification. The evidence is
missing, not refuted. So take the weak, safe
rule: where an executable check exists, don't rest acceptance on review.
Where none exists, review is what you have — then say which of the two you
used, so the difference stays visible.

That leaves review with what the evidence says it does produce: design
fit, security implications, norm consistency, a record of why. Worth a
reasoner call on a risky diff. Not a defect gate.

**Provenance.** "Tests pass" is a claim. For an LLM, generating
`Test Suites: 3 passed, 3 total` costs exactly what generating "tests
pass" costs — the same next-token operation — so demanding the output does
not by itself separate a real run from a plausible one. The cost asymmetry
that makes "show me the output" work on a human delegate does not exist
here. Acceptance evidence has to trace to an invocation you can see: a
tool-call record in the transcript, a CI artifact, or the command re-run at
your level. On anything that matters, re-run it yourself — it costs seconds,
and it is the only part of the report that isn't the delegate's word.

## Domain examples

**Development** — "간헐적 로그인 버그 고쳐줘": executor explores auth
paths and runs tests (narrow brief) → you form hypotheses from its
summary → reasoner confirms root cause if subtle → executor implements
fix + regression test → reasoner reviews the diff (auth = risky) → you
integrate, commit, report.

**Design** — "대시보드 다크모드 팔레트 만들어줘": you set constraints
(brand, contrast targets) → executor produces token sets and CSS →
reasoner critiques accessibility/contrast trade-offs → you pick and
report.

**Architecture** — "이 모놀리스 어떻게 쪼갤까": you frame the options
and constraints → reasoner argues each candidate split (one call per
option, or two opposing framings) → you synthesize the decision →
executor writes the ADR from your decision.

**Orchestration at scale** — "API v1 → v2 마이그레이션, 파일 50개":
executor(scout brief) inventories call sites → **you freeze the v2
contract first** and put it verbatim in every brief, because fifty agents
that never talk will each invent their own v2 signature otherwise → you
partition into batches with disjoint write sets → parallel executors
transform batches → executor runs the full test suite → reasoner
spot-reviews the riskiest diffs → you report. The freeze and the
disjointness are `parallel-decomposition`'s gates; what must be true
before any of it lands is `merge-gates`'.

**Research** — "이 시장 조사해줘", "is this library safe to depend on":

This is the one domain where the routing pattern has been measured and cap-tuned across 14 production rounds (34.4M subagent tokens). The pipeline has five phases:

1. **Scope** (you — orchestration-adjacent): decompose the question into 5 deliberately disjoint search angles. Each angle gets a label, a query, and a rationale. Disjointness matters: if two angles return the same results, one of them was wasted.
2. **Search** (executor): one executor per angle runs web search. Returns top 4-6 results each with relevance rating.
3. **Fetch + Extract** (executor): URL-dedup across all searchers, then one executor per novel source fetches the page and extracts 2-5 falsifiable claims. Each claim carries a direct quote from the source, importance (central/supporting/tangential), and source quality (primary/secondary/blog/forum/unreliable).
4. **Verify** (reasoner): 3-vote adversarial verification. Each claim gets 3 independent reasoner voters instructed to be skeptical and try to refute. ≥2 refutations kill the claim. This is the largest cost block — at 3 voters per claim, it was 66.8% of total spend — but it is also the discrimination that produces the product: without it, a marketing claim and a peer-reviewed finding are indistinguishable.
5. **Synthesize** (you): merge semantic duplicates, group into coherent findings, assign confidence (high/medium/low by source count and vote unanimity), list caveats and open questions, and — crucially — declare what was **not** checked.

**Measured caps, not taste.** Spend analysis found MAX_FETCH=9 and MAX_VERIFY_CLAIMS=18 as the point where fetch waste and verify discrimination balance. At these caps, a round extracts ~100 claims and votes on the strongest 18; the rest are recorded as deferred, not dropped. Don't tune these by feel — they were sized from measurement.

**Coverage invariant (the harness's most dangerous failure).** "We never looked" and "we looked and found nothing" read identically in a report. Three mechanisms prevent this, and all three must hold:
1. Verify slots are allocated **round-robin across angles**, not by a global importance rank. A global top-N sort let one angle's claims fill every slot and starved another angle to zero — the synthesis then reported that angle as having produced no findings. With round-robin, an angle can only go unverified if it produced no claims at all.
2. Claims the verify cap cannot reach become a **deferred** list — a first-class output, not a silent drop. It travels on every exit path and the synthesis must account for it.
3. The report schema requires a **notChecked** field. A report physically cannot be produced without declaring the coverage gap. An empty notChecked is a claim that nothing was deferred, and it is checkable.

Removing any one of these three re-opens the hole. This is not hypothetical: a production run silently dropped all 8 claims on one angle and the report called that angle evidence-free.

**Research brief template.** When delegating research sub-tasks, every brief must carry:
- The research question verbatim (so subagents don't drift).
- The specific angle or sub-question assigned to that agent.
- The output schema (structured, not prose — so claims are machine-checkable).
- The cap: max results per searcher, max claims per source, max claims to verify.

## A delegate that delegates inherits your tier

Unless the tool explicitly supports per-subagent model selection, a
delegate runs on the caller's model by default. So a reasoner that fans
out spawns reasoners, and each of those can spawn more — the tier you
chose once gets paid at every level below it. This is the one way a
correct top-level routing decision still blows the budget: a single
reasoner brief that quietly becomes four.

Before handing a brief to a reasoner, ask whether it will need scouts of its
own. If it will, either instruct it to use the cheaper tier for its own
delegations (if the tool allows), or keep the fan-out at your level and hand
the reasoner only the collected material to judge. Fan out wide at executor
tier; converge to one reasoner.

## When NOT to delegate

Delegation has real overhead: each subagent starts cold and you must
write its brief and read its report. If a step takes fewer tool calls
than briefing would (one-file read, small edit, quick answer from
context), do it yourself — the pattern routes heavy steps, it does not
turn every action into bureaucracy. A rubber-stamp reasoner call on a
trivial diff is the most expensive form of waste in this system.