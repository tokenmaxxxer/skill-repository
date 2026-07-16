---
name: parallel-decomposition
description: >-
  A gate for cutting build work into pieces several agents can produce at once without colliding:
  enumerate each piece's write set, list every identifier two pieces would both have to agree on,
  freeze those as a contract before fan-out, and refuse the fan-out when the contract can only be
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

## Evidence grade — read before citing this to anyone

The caveat is load-bearing and comes first.

- **Nothing here was measured on agents. The transfer is an argument, not a result.** No
  agent-specific baseline exists — worktree-per-agent isolation, how agent PRs are gated in real
  teams, observed agent failure modes, and the substrate by which agents observe each other have no
  confirmed evidence behind any of them. State that gap in the right shape, because this repo stated
  it wrong once and corrected it: the round-7 agent claims were **never put to a vote**. The research
  harness verifies only the top 25 of 111 extracted claims, all 8 agent claims lost their slot on
  array position alone, and the synthesis stage then reported that truncation as absence of evidence.
  Re-verified separately at the same three-vote bar, 3 of the 8 survived, and none of them
  establishes a baseline for fan-out. So: the evidence is **missing, not refuted** — never say the
  agent claims were tested and failed. Every claim below was measured on human organizations in 2012
  or earlier, and applying it to a fleet is extrapolation. Say so rather than implying the evidence
  covers it. What the procedure delivers is engineering discipline whose *steps* are checkable; the
  *premise* that the discipline pays off on agents is untested.
- **None of these studies is an experiment.** MacCormack is matched-pair observational over
  organizational form; Nagappan is correlational; Rodriguez is headcount against productivity. They
  observe organizations that differ; they do not control anything. The transfer argument rests on
  what they observed pointing the same direction, not on any of them isolating a cause.
- **Conway's law** (Conway 1968, *Datamation*): "organizations which design systems are constrained
  to produce designs which are copies of the communication structures of these organizations." A
  stated observation and argument. The frame, not the proof.
- **Mirroring** (MacCormack, Baldwin & Rusnak; HBS WP 2008, *Research Policy* 2012): across 5 matched
  product pairs of comparable function, products built by loosely-coupled organizations were more
  modular in **every pair**, with propagation cost differing by **up to 8×**. Directional; N=5 pairs.
  **The widely-repeated "2011, 6×" citation is an error — do not use it.**
- **Organizational structure predicts defect-proneness** (Nagappan, Murphy & Basili, ICSE 2008):
  across **3,404 Windows Vista binaries**, eight organizational-structure metrics out-predicted code
  churn, complexity, dependencies, coverage, and pre-release bug counts (**precision 86.2%, recall
  84.0%**). One system, one company. **It says organizational structure carries defect signal at the
  binary level. It says nothing about where defects sit inside a change, and nothing about fan-out
  seams — do not attribute a seam-localization finding to it.** The prediction below that defects
  concentrate at frozen-contract seams is an untested implication of Conway's argument, not a result
  anyone reported.
- **Team size** (Rodriguez et al. 2012, *JSS*, ISBSG): teams averaging **more than 9 people** were
  significantly less productive (p=2.2e-16), from **199 projects**, with a single-submitting-
  organization risk the authors named themselves. **This does not transfer to a fleet-size limit and
  must not be cited as one.** Step 6 derives the ceiling from the work instead. Related caution:
  Gote et al. (EMSE) showed "larger teams are more productive" findings can be a Simpson's-paradox
  artifact of aggregating heterogeneous projects.
- **Team Topologies** builds on this evidence base but its own prescriptions are **unverified** in
  this repo's research. Do not cite it as support for anything here.

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

### Step 1 — Enumerate write sets

For every proposed piece, write down the exact set of files it will **write to**. Reading is not
writing; a file two pieces only read is not shared for this purpose.

**Gate:** every piece has an enumerated write set with the count stated ("4 pieces; write sets of
12/7/9/3 files"). "Roughly the auth module" does not pass. If you cannot enumerate them, you do not
yet know whether this decomposes — send a scout brief to inventory the call sites (`model-routing`\nroutes that to the executor), then come back.

### Step 2 — List the shared identifiers

Go piece by piece and name every **identifier** that appears in more than one piece's work as
something the piece must either produce or conform to: a type, a function signature, a schema field,
an endpoint shape, a config key, an error contract, an ordering invariant.

The list decides the classification, and it is an enumeration rather than a judgment:

- **Empty list → module-shaped.** The pieces are independently correct.
- **Non-empty list → cross-cutting.** The list **is** the contract that Step 3 freezes.

**Gate:** the list exists in writing, and every entry is a nameable identifier — `UserId`,
`POST /v2/sessions`, `Result<T, ApiError>`, `retry_after_ms`. An entry like "they need to be
consistent" is not an identifier and does not pass; either name the thing or you have not found it
yet. If producing the list requires reading code you have not read, that is a scout brief, not a
guess.

### Step 3 — Freeze the contract before fan-out

If Step 2's list is non-empty, every entry on it gets fixed **first, serially, by you or one agent**,
and written as text that goes into every brief verbatim.

Then re-classify: with the contract frozen, the work is "apply this fixed contract in N places," which
is module-shaped. That re-classification is the point of the step.

**Gate:** the contract text exists and is byte-identical in every brief. If two agents would each
have to decide the same entry independently, this gate **fails** — go back and freeze it.

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
