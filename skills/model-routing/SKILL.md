---
name: model-routing
description: >-
  Use this skill on EVERY non-trivial task in any domain — development, design, architecture,
  data, docs, or multi-step orchestration — to decide what you do yourself, what goes to a high-
  capability reasoner, and what goes to a low-cost executor. Tiered orchestration policy: the
  session model orchestrates, decomposes, and synthesizes, pushing heavy judgment to the reasoner
  and production/exploration work to the executor. It also carries the rule for accepting
  delegated work: the brief names an executable check, and neither a reasoner's approval nor the
  delegate's own narration of a test run substitutes for that check's traceable evidence. Trigger
  even if the user never mentions cost, models, or delegation — e.g. "이 작업 어느 모델한테 맡길까", "which
  model should handle this", "delegate this to a cheaper model", "opus vs haiku for this task". Do
  NOT use for pure conversation or single trivial edits, or for cutting work into non-colliding
  pieces (use parallel-decomposition).
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

## When NOT to delegate

Delegation has real overhead: each subagent starts cold and you must
write its brief and read its report. If a step takes fewer tool calls
than briefing would (one-file read, small edit, quick answer from
context), do it yourself — the pattern routes heavy steps, it does not
turn every action into bureaucracy. A rubber-stamp reasoner call on a
trivial diff is the most expensive form of waste in this system.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 4.1 — **Scope** (you — orchestration-adjacent): decompose the question into 5 deliberately disjoint search angles. Each angle gets a label, a query, and a rationale. Disjointn…
- 4.2 — **Search** (executor): one executor per angle runs web search. Returns top 4-6 results each with relevance rating
- 4.3 — **Fetch + Extract** (executor): URL-dedup across all searchers, then one executor per novel source fetches the page and extracts 2-5 falsifiable claims. Each claim carri…
- 4.4 — **Verify** (reasoner): 3-vote adversarial verification. Each claim gets 3 independent reasoner voters instructed to be skeptical and try to refute. ≥2 refutations kill t…
- 4.5 — **Synthesize** (you): merge semantic duplicates, group into coherent findings, assign confidence (high/medium/low by source count and vote unanimity), list caveats and o…
- 4.1(2) — Verify slots are allocated **round-robin across angles**, not by a global importance rank. A global top-N sort let one angle's claims fill every slot and starved another…
- 4.2(2) — Claims the verify cap cannot reach become a **deferred** list — a first-class output, not a silent drop. It travels on every exit path and the synthesis must account for…
- 4.3(2) — The report schema requires a **notChecked** field. A report physically cannot be produced without declaring the coverage gap. An empty notChecked is a claim that nothing…
- S1 — Routing rules → references/rules.md
- S2 — Evidence grade → references/rules.md
- S3 — Review is not the acceptance gate → references/rules.md
- S4 — A delegate that delegates inherits your tier → references/rules.md
