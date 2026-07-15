---
name: model-routing
description: >-
  Tiered orchestration policy (session model orchestrates / Opus reasoner /
  Sonnet executor): the session model decomposes, delegates, and synthesizes,
  pushing production work down to the executor tier. Use this
  skill on EVERY non-trivial task in any domain — development, design,
  architecture, data, docs, or multi-step orchestration — to decide what
  you do yourself, what goes to the reasoner subagent, and what goes to the
  executor subagent. Trigger even if the user never mentions cost, models,
  or delegation. Do not use for pure conversation or single trivial edits.
---

# Model Routing: orchestrate expensive, execute cheap

## The pattern

This encodes the community-standard split ("cheap fan-out, expensive
judgment"): the session model is the **orchestrator**, and two subagents
carry the load beside and below it.

| Role | Who | Owns |
|---|---|---|
| Orchestrator | YOU — whatever model the session runs on | understanding the user, decomposing work, writing delegation briefs, synthesizing results, final judgment calls, talking to the user |
| `core:reasoner` | subagent, `model: opus` | one hard bounded question at a time: architecture decisions, root-cause analysis of subtle bugs, security/design critique, trade-off arbitration, pre-commit review of risky diffs |
| `core:executor` | subagent, `model: sonnet` | producing things: implementing code and tests, refactors, docs, design tokens/assets, data scripts, bulk mechanical edits — and exploration/searching with `effort: low` briefs |

Pass these as `subagent_type` on the Agent tool. They are plugin agents, so
they carry the `core:` scope — a bare `reasoner` will not resolve.

The subagents pin their own tier, but the orchestrator is whatever `/model`
is set to — so how much delegation saves depends on the session. On Fable the
three tiers are distinct and every delegation is cheaper. On Opus the
orchestrator and the reasoner are the same model: executor briefs still cost
less, but a reasoner call buys you fresh-context judgment, not a discount. On
Sonnet it inverts — the executor is the session model itself, and a reasoner
call is an escalation upward. Don't reason about the savings from a fixed
multiplier; know which of those three you're in.

The routing below holds regardless. Behave like a tech lead, not a solo
engineer: decompose, brief, judge, integrate. Don't do mechanical work
yourself when an executor can — at worst it costs the same and keeps your
context clean for the judgment only you can make.

## Routing rules

Route by the nature of the STEP, not the domain of the task. The same
three roles cover development, design, architecture, and data work —
only the brief's content changes.

- **Production steps** (write code, write tests, write docs, build the
  CSS tokens, generate the migration script, apply a rename across 50
  files) → `core:executor`. Include in the brief: exact scope, files, the
  acceptance check it must run, and what to report back (summary, not
  logs).
- **Mechanical exploration** (find usages, map an unfamiliar area, run tests
  and summarize failures, analyze logs) → `core:executor` with an explicitly
  narrow question and instruction to return conclusions + file:line
  refs only. This tier replaces a dedicated cheap scout; keep these
  briefs small.
- **Exploration that has to judge what it finds** (trace each number to its
  primary source and flag the three reports that secretly share one; decide
  which of these sources is authoritative; separate what evidence shows from
  what it merely asserts) → `core:reasoner`. Retrieval and judgment look
  alike in a brief — the tell is whether the finder must *decide about* what
  it retrieves or merely report it. Route these by the deciding, not the
  fetching: an executor stops at the first plausible secondary source and
  hands it back as fact, and everything downstream inherits that.
- **Hard bounded questions** (which of these two architectures, why does
  this race only happen under load, is this auth diff safe to ship,
  critique this design against our system) → `core:reasoner`. One question
  per call, with the minimum context it needs and a demanded verdict
  format. For decisions that are expensive to reverse, ask the reasoner
  twice with opposing framings and synthesize yourself.
- **Judgment you keep** — do NOT delegate: interpreting what the user
  actually wants, decomposing the work, choosing what to delegate,
  integrating results, and anything requiring the full conversation
  context. Delegating orchestration itself defeats the pattern.

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
executor(scout brief) inventories call sites → you partition into
batches → parallel executors transform batches → executor runs the full
test suite → reasoner spot-reviews the riskiest diffs → you report.

## A delegate that delegates inherits your tier

Omitting `model` on an Agent call runs the child on the **caller's** model.
So a reasoner that fans out spawns reasoners, and each of those can spawn
more — the tier you chose once gets paid at every level below it. This is
the one way a correct top-level routing decision still blows the budget: a
single reasoner brief that quietly becomes four.

Before handing a brief to a reasoner, ask whether it will need scouts of its
own. If it will, either pass the cheaper tier down explicitly in the brief,
or keep the fan-out at your level and hand the reasoner only the collected
material to judge. Fan out wide at executor tier; converge to one reasoner.

## When NOT to delegate

Delegation has real overhead: each subagent starts cold and you must
write its brief and read its report. If a step takes fewer tool calls
than briefing would (one-file read, small edit, quick answer from
context), do it yourself — the pattern routes heavy steps, it does not
turn every action into bureaucracy. A rubber-stamp reasoner call on a
trivial diff is the most expensive form of waste in this system.

## Keeping it current

Role→model mapping lives ONLY in this plugin's `agents/reasoner.md` and
`agents/executor.md` frontmatter, as aliases (`opus`, `sonnet`) — never
pinned IDs. Agents must sit at the plugin root (`plugins/core/agents/`);
nested under a skill they are silently ignored. When a model generation
ships, re-run the team's golden tasks and adjust one line if a role can
move down a tier. If the org routes through a gateway with logical model
groups, point the agent files at those group names instead.