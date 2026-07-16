---
name: parallel-decomposition
description: >-
  A gate for cutting build work into pieces several agents can produce at once without colliding:
  classify pieces by collision risk, enumerate write sets and list shared identifiers at depth
  proportional to risk, freeze those as a contract before fan-out, and refuse the fan-out when
  discovered by doing the work. This is the upstream half of parallel work — it decides the cut
  before any agent is spawned; `merge-gates` decides what must be true before a branch lands. Use
  before spawning more than one agent to BUILD — e.g. "이 작업 병렬로 쪼개서 시켜줘", "에이전트 여러 개로 나눠서
  돌려", "split this across agents", "fan this out in parallel", "can these run concurrently",
  "parallelize this". Trigger whenever someone is about to fan out production work on a shared
  codebase. Do NOT use for merge/landing questions (`merge-gates`), for research fan-out where
  agents share no artifact (`market-recon`, `tech-feasibility`), for model-tier routing
  (`model-routing`), or for work small enough that briefing costs more than doing it.
---

# Parallel Decomposition

## First: is there anything here to decompose?

- **Are the agents producing a shared artifact?** If each is reading the world and returning findings
  — search sweeps, candidate surveys, source gathering — nothing collides and this skill has no work
  to do. `market-recon` and `tech-feasibility` carry the fan-out discipline for that shape.
- **Is the question about landing, not cutting?** "What must pass before this merges" is
  `merge-gates`. This skill runs earlier and answers a different question: whether and where to cut
  at all. The two compose — cut here, land there.
- **Is there more than one piece?** One agent, one brief, no seams. Exit.
- **Is the whole job smaller than the briefing?** A one-file edit, a rename in three places. Do it
  yourself — `model-routing` draws that line and this skill does not move it.

Everything below applies when two or more agents will write to one codebase.

**A note on the word "Gate" here.** `merge-gates` defines the corpus's strict sense — binary,
machine-evaluable, fail-closed, evaluated on the combined state. The gates below are procedural
checkpoints in the looser sense `fmea` and `launch-readiness` use: each one names a written artifact
that must exist before the next step. Step 4 is the only one a machine could evaluate. Do not
present these as merge-gates-grade enforcement.

## Evidence grade

Full evidence grades with source-by-source detail in `references/evidence.md`. Summary: all studies are pre-2013 observational human-organization data; none measured agents and none was an experiment. The premise that the discipline pays off on agent fleets is untested.

## The reading that drives the procedure

Conway's constraint, pointed at a fleet, says something specific. Agents working in parallel
exchange nothing directly while they work — they share a repo and a common brief, but no channel
carries a decision from one to another mid-flight. An organization shaped like that can apply a
decomposition; it cannot discover one.

That gives the failure mode its shape. Fan out a change whose pieces must *agree* on something — a
type, a signature, a schema, an invariant — and each agent makes a locally plausible decision about
it. Every piece passes its own check. The disagreement is only visible in the union. The fix is not
more agents or better briefs: freeze the thing they would have had to agree on **before** any of
them starts, which turns a cross-cutting change into a module-shaped one.

Whether defects actually concentrate there is, per the evidence grade, an untested implication.
What is not in doubt is the mechanism: two agents that never exchange a message cannot converge on
an unstated convention except by luck.

## Procedure

### Classification — Triage by collision risk before enumerating

Classify each proposed piece into one of three tiers before any per-piece enumeration:

- **High risk**: pieces that share identifiers or write to overlapping paths. Full per-identifier enumeration required; every shared identifier frozen as contract.
- **Medium risk**: pieces in the same module but disjoint files. Named write sets required; identifier list optional.
- **Low risk**: completely isolated pieces in separate directories with no shared identifiers. Stated as "N isolated pieces, no shared identifiers" — skip per-identifier enumeration.

The classification drives depth: High runs the full procedure; Medium skips the per-identifier contract (Step 3 optional); Low skips Steps 2–3 and proceeds to Step 4.

### Step 1 — Enumerate write sets

For every proposed piece, write down the exact set of files it will **write to**. Reading is not
writing; a file two pieces only read is not shared for this purpose.

**Gate:** every High and Medium piece has an enumerated write set with the count stated ("4 pieces; write sets of
12/7/9/3 files"). Low pieces may state the directory instead ("writes to `pkg/isolation/` only; no other piece touches this tree"). "Roughly the auth module" does not pass. If you cannot enumerate them, you do not
yet know whether this decomposes — send a scout brief to inventory the call sites (`model-routing`\nroutes that to the executor), then come back.

### Step 2 — List the shared identifiers

Go piece by piece and name every **identifier** that appears in more than one piece's work as
something the piece must either produce or conform to: a type, a function signature, a schema field,
an endpoint shape, a config key, an error contract, an ordering invariant.

The list decides the classification, and it is an enumeration rather than a judgment:

- **Empty list → module-shaped.** The pieces are independently correct.
- **Non-empty list → cross-cutting.** The list **is** the contract that Step 3 freezes.

**Gate:** per the Classification tier: **High** — the list exists in writing, and every entry is a nameable identifier — `UserId`,
`POST /v2/sessions`, `Result<T, ApiError>`, `retry_after_ms`. An entry like "they need to be
consistent" is not an identifier and does not pass. **Medium** — the list is optional; if provided, same requirement. **Low** — state "no shared identifiers" and skip Steps 2–3. If producing the list for High/Medium requires reading code you have not read, that is a scout brief, not a
guess.

### Step 3 — Freeze the contract before fan-out

Per the Classification tier: **High** — every shared identifier gets fixed **first, serially, by you or one agent**,
and written as text that goes into every brief verbatim. **Medium with identifiers listed** — freeze or document as accepted risk. **Low** — skip this step.

Then re-classify: with the contract frozen, the work is "apply this fixed contract in N places," which
is module-shaped. That re-classification is the point of the step.

**Gate:** per the Classification tier: **High** — the contract text exists and is byte-identical in every brief. If two agents would each
have to decide the same entry independently, this gate **fails** — go back and freeze it. **Medium with identifiers listed** — freeze or document as accepted risk. **Low** — this step is skipped.

**Exit condition:** if the contract cannot be written now, do not reach for a judgment about whether
it "genuinely" can't be — **name the unknown**. Write one sentence: which specific fact, discoverable
only by doing the work, would determine the contract's shape? If you can name it, **do not fan out**:
that is serial work, or one agent's job, until the unknown resolves. If you cannot name it, you have
not tried to write the contract yet — go write it.

A fleet cannot discover an interface. Pretending otherwise buys N mutually incompatible answers that
each look right.

### Step 4 — Prove disjointness

Compare the Step 1 write sets pairwise.

**Gate:** every pairwise intersection is empty. Where it is not, one of these holds before you
proceed:
- the shared file is assigned to **exactly one** piece and every other brief says explicitly not to
  touch it; or
- the shared file is edited or extracted **serially first**, and the fan-out starts after; or
- the pieces are **merged into one** and one agent does both.

"They'll probably not conflict" does not pass. Neither does "git will merge it" — a clean textual
merge is not semantic agreement, and `merge-gates` Step 5 carries the evidence for why that is the
wrong variable to gate on.

### Step 5 — Every brief names its own check

Each piece's brief must name the command that decides whether that piece is done and what its output
must show. `model-routing` carries the rule, the evidence that a reviewer's opinion does not fill
that slot, and the provenance requirement — an agent's narration of its own test run is not
acceptance evidence.

**Gate:** every brief names a check. A piece whose completion nothing executable can check is not
ready to delegate — that is a requirements gap (`requirements-quality`) or a bad cut (return to
Step 2), not something to hand out and hope for.

### Step 6 — The piece count is a ceiling, not a target

The number of disjoint pieces surviving Step 4 is the **maximum** useful fleet size. Fewer agents is
often right — one agent can take three disjoint pieces in sequence, and `model-routing` owns that
call on context and cost grounds. There is no verified agent-count threshold, the human team-size
finding does not transfer (see Evidence grade), and inventing one is not licensed.

**Gate:** the agent count does not exceed the disjoint-piece count, and no single piece is split
across two agents. If someone names a desired agent count first and asks for the work to be divided
into it, that is backwards — cut lines come from the code's structure, not from the parallelism
someone wants.

### Step 7 — Hand the union to merge-gates

Per-piece checks passing does not mean the union is correct, and per-piece checks cannot see the
disagreement Step 3 exists to prevent. The union is `merge-gates`' subject: its Step 3 requires the
combined state — trunk plus every change ahead — and names the mechanisms that produce it.

**Gate:** before fan-out, name the mechanism that will evaluate the combined state, or write
`merge-gates`' honest sentence instead: changes are gated individually and can break trunk in
combination. Do not invent a substitute here; that skill has the evidence and this one does not.

### Step 8 — Record the cut

Write down the pieces, the frozen contract, the disjointness argument, and the union result. If the
contract was an architectural decision, `decision-records` carries the trigger test for whether it
needs an ADR.

**Gate:** the record exists before the fleet is dismissed. A cut that worked and went unrecorded gets
re-derived, badly, by whoever fans out that area next.

## When the procedure says no

"Do not parallelize this" is an honest output, not a failure. A change whose contract can only be
discovered by doing the work, or whose write sets cannot be made disjoint, is serial work. Reporting
that costs one paragraph. The alternative costs N confident agents and a union nobody can untangle.
