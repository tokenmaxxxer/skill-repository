---
name: architecture-module-boundary-definition
description: >-
  Use when deciding where to draw a module/component/service boundary — what belongs together by
  cohesion, when to stop splitting, when to merge things back, and how to keep a C4-level
  boundary diagram reviewable as the decision evolves. Trigger on requests like "모듈 경계 어디에 그을까",
  "does this belong in the same component", "bounded context 나눠줘", "is this module too big to
  stay one module". Do NOT use for the system-wide split/keep/merge-back decision on service
  count (use architecture-decomposition-strategy).
metadata:
  axis: module-boundary-definition
  rule_count_floor: 12
---

# Module Boundary Definition

Operational decision rules for where to draw a module/component/service boundary:
cohesion criteria, what belongs together, and — just as important — when to stop
splitting and merge things back. Sourced from practitioner writeups (layer 1),
named methodologies (layer 2), and academic/theoretical grounding (layer 3).

Where sources conflict — most sharply "always favor small, single-purpose
services" (microservices advocacy) vs. "avoid premature decomposition, start
monolith-first" (Fowler, and the growing body of monolith-reversion case
studies) — the conflict is called out explicitly in the affected rules rather
than silently picking a side.

## Trigger

Apply this skill when placing or auditing a module/component/service
boundary: deciding what belongs together, whether a proposed split
should happen at all, whether an existing split should be merged back,
or whether a boundary diagram is trustworthy enough to review against.

## Procedure

1. Draw the boundary so a likely-to-change design decision is hidden
   entirely inside one module (rule 1); never decompose purely by
   processing step/technical layer — keep those steps together unless a
   real hidden-decision boundary separates them (rule 2); organize by
   domain concept, not technical role (rule 3).
2. Require every cross-component interaction to go through an explicit
   public interface, treating direct data reach-through as a violation
   to fix (rule 4); use bounded contexts — where the ubiquitous language
   changes — as the seam, not database schemas (rule 5).
3. When decomposing a newly identified bounded context, model it as one
   service first and only split further once a concrete need
   (independent scaling, ownership, deploy cadence) appears (rule 6);
   for a new system, build a monolith first and defer service
   boundaries until real usage reveals the seams (rule 7).
4. Merge over-decomposed services back together when each is thin and
   mostly passes calls through (rule 8); merge two services back into
   one when their boundary no longer hides an independent design
   decision (rule 9); redraw the boundary to match a single team's
   ownership, or restructure teams via reverse-Conway, rather than
   leaving a boundary that forces permanent cross-team coordination
   (rule 10).
5. Split a module along the seam where cohesion changes from
   functional/sequential to coincidental/logical — never solely because
   line count crossed a threshold (rule 11); conversely, leave a large
   but low-coupling, internally-cohesive module as one module rather
   than splitting to satisfy a size guideline (rule 12).
6. When a boundary discussion conflates deployable-unit and
   internal-code-organization questions, separate them: pick container
   boundaries from ownership/scaling/deploy-cadence needs first, then
   component boundaries from cohesion inside each container (rule 13).
7. When two boundary placements both seem plausible, prefer the one
   that isolates the assumption most likely to change, not the one that
   merely looks tidier (rule 14).
8. When a C4-level boundary diagram exists only as a pasted image,
   produce it instead from a single text-based model checked into the
   record's write scope so it diffs like code (rule 15).

## Output shape

A boundary decision: keep-together / split / merge-back, the rule
number(s) applied, the cohesion or bounded-context justification, and
— where a REMOVAL rule fires (8, 9, 12) — what gets merged or left
unsplit.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1 — Hide a design decision likely to change → pick the module boundary so that decision is hidden entirely inside one module, exposing only a stable interface
- 2 — Do not decompose by processing step / technical layer → keep those steps in one module unless a real hidden-decision boundary separates them; do not split purely by flowchart phase
- 3 — Organize components by domain concept, not technical role → split components along real-world business concepts (orders, shipping, inventory, billing), each owning its own data, instead of along MVC-…
- 4 — Give every component exactly one public interface and forbid direct data reach-through → require the interaction go through an explicit public API; treat any cross-component association or direct data access as a boundary violat…
- 5 — Use bounded contexts, not database schemas, as the seam → identify bounded contexts by where the ubiquitous language changes (the same word means a different thing to different teams), and place th…
- 6 — Model the whole bounded context as one service first (REMOVAL applies at finer grain) → keep the whole bounded context as a single service initially; only split it further into smaller services around aggregates later, and only…
- 7 — Do not decompose into services before the domain model is understood → build it as a monolith first; defer service-boundary decomposition until real usage has revealed where the seams actually are
- 8 — CONFLICT — reconcile "many small services" advice against "avoid premature decomposition" **REMOVAL** → merge over-decomposed services back into fewer, coarser-grained ones until each surviving boundary corresponds to an independently-changing…
- 9 — Merge a service back when its boundary no longer hides anything **REMOVAL** → merge them into one module/service and delete the network boundary between them
- 10 — Let team communication boundaries and reverse-Conway maneuvers set the boundary, not vice versa → either redraw the module boundary to match a single team's ownership, or restructure the teams to match the desired architecture (reverse-C…
- 11 — Split a module when its cohesion type is coincidental or logical, not when it merely feels "big" → split the module along the seam where cohesion changes from functional/sequential to coincidental/logical; do not split solely because line…
- 12 — Don't split further just because a module is large — check coupling first **REMOVAL** → leave it as one module; do not split it merely to satisfy a size guideline
- 13 — Use C4 container/component levels to decide which granularity a "boundary" question is even about → separate the two: pick container boundaries (independently deployable units — services, databases) first from ownership/scaling/deploy-cade…
- 14 — Draw the boundary where a difficult-to-predict change is most likely to land → prefer the placement that isolates the assumption most likely to change (data source, third-party API, regulatory rule) inside a single mod…
- 15 — A C4-level boundary diagram exists only as a pasted image, not as a versioned model → produce the diagram from a single text-based model (one DSL/model file that generates the context/container/component views), and check tha…
