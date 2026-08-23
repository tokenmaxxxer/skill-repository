---
name: architecture-dependency-direction
description: >-
  Use when deciding which way a dependency arrow should point between modules/layers/services —
  domain vs. infrastructure imports, adapter-to-port direction, breaking an import cycle,
  layer-skipping exceptions, or auditing whether a declared direction rule still holds against
  the real import graph. Trigger on requests like "domain이 infra를 import해도 돼?", "break this
  import cycle", "hexagonal ports and adapters wiring", "의존성 방향 점검해줘". Do NOT use for naming the
  coupling type between two components (use architecture-coupling-classification).
metadata:
  axis: dependency-direction
  rule_count_floor: 12
---

# Dependency Direction Playbook

Decision rules for which way a dependency arrow should point between modules, layers, or
components, and when a dependency is a violation to be corrected. Sourced from practitioner
writeups, named methodologies/standards, and academic/theory literature, each fetched or
searched this session.

## Trigger

Apply this skill when a dependency's direction is in question: domain
code wants to import infrastructure, a high-level module instantiates
a low-level one directly, an adapter and a core need wiring, an import
cycle exists, a layer-skip is proposed for performance, or a
previously-decided direction rule needs auditing against the real
import graph.

## Procedure

1. Block domain/use-case code from importing framework or
   infrastructure symbols directly; introduce a domain-owned interface
   and move the concrete import behind an adapter instead (rule 1).
2. When a high-level module calls a low-level one concretely, choose
   abstraction-via-interface so both sides depend on an abstraction the
   high-level module owns (rule 2); in a hexagonal design, define the
   port inside the core and require both driving and driven adapters to
   depend on it, never the reverse (rule 3).
3. Even when an infrastructure package looks "stable" by Martin's
   metric, keep the domain depending on interfaces it owns rather than
   the infrastructure package directly — layering takes precedence over
   the stability metric alone (rule 4); never let an inner (stable)
   layer import an outer (unstable) one — push the needed data/behavior
   down into the core instead (rule 5).
4. When two packages cycle and one owns a clear policy/implementation
   split, break the cycle by extracting an interface on the policy side
   (rule 6); when the cycle exists only because the two share a few
   common types, extract those types into a new shared lower-level
   package instead (rule 7).
5. Enforce the intended layering in CI with executable architecture
   tests so violations fail the build automatically (rule 8); if a
   layer-skip is proposed for performance, only allow it as an
   explicit, allowlisted exception in that test suite, never as an
   undocumented ad hoc import (rule 9).
6. Track whether disallowed edges are drifting upward over time with a
   scheduled dependency-drift fitness function, not just a one-time
   pass/fail check (rule 10); when an audit surfaces many flagged
   edges, build a Dependency Structure Matrix to separate genuine
   erosion from edges already contained within an accepted subsystem
   (rule 11).
7. When a facade/intermediary was added "for future flexibility" but
   only one implementation has ever existed, collapse it rather than
   keeping the indirection hop (rule 12); when a package accumulates
   many inbound dependents while staying concrete rather than abstract,
   extract an abstract interface package for its dependents to point at
   instead (rule 13).
8. When a direction rule was decided and documented but never verified
   against the actual codebase, generate the import graph from the real
   imports (not hand-drawn) and treat any edge crossing the declared
   boundary as a finding to fix or explicitly re-litigate (rule 14).

## Output shape

A dependency-direction decision: the violating or at-risk edge, the
rule number(s) applied, the corrective direction (introduce an
interface, invert via a shared package, collapse a facade, or confirm
via generated graph), and whether it's a REMOVAL or a redirection.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1 — Business/domain logic must not import framework or infrastructure code → Introduce an interface (port) owned by the domain module; move the concrete infrastructure import behind an adapter that implements that in…
- 2 — Choosing between abstraction-via-interface and abstraction-via-inheritance to invert a dependency → Have the high-level module depend only on an abstraction (interface/protocol) that it or its layer owns; make the low-level module implemen…
- 3 — Adapters must depend on ports defined by the core, never the reverse → Define the port (interface) inside the application core; require both driving and driven adapters to depend on that port. Never let the cor…
- 4 — Infrastructure that appears "stable" must still not pull dependencies outward → Keep the domain layer depending only on interfaces it owns; force the "stable" infrastructure package to implement those interfaces rather…
- 5 — Outer (unstable) layers must never be imported by inner (stable) layers → Push the needed data or behavior down into the core (as a value object, parameter, or port), and have the outer layer supply it through tha…
- 6 — Two same-level modules directly reference each other (import cycle) and one owns a clear abstraction boundary → Extract an interface for the capability the "implementation" side needs to expose, place it in the policy side, and have the implementation…
- 7 — Two packages depend on each other only because they share a few common types → Extract the shared types into a new, lower-level shared package that both A and B depend on; remove A's and B's direct dependency on each o…
- 8 — Enforcing a defined layered architecture in CI so violations aren't discovered by accident → Write executable architecture tests (e.g. ArchUnit's `layeredArchitecture()`) that assert each layer may only access the layers it's permit…
- 9 — A layer-skipping read dependency is proposed for performance reasons → Only allow the skip if it is declared as an explicit, named exception in the architecture test suite (e.g. an allowlisted rule) — do not al…
- 10 — Tracking whether a dependency direction is drifting toward disallowed edges over time → Add a dependency-drift fitness function that runs on a schedule/CI and reports the trend of disallowed-edge counts, not just a pass/fail sn…
- 11 — Diagnosing whether existing violations represent real architecture erosion before deciding to fix them → Build a Dependency Structure Matrix of the current codebase, visually cluster modules, and treat any flagged cell that falls outside the in…
- 12 — A facade or intermediary layer was added "for future flexibility" but never varies → Collapse the facade and let the caller depend directly on the single concrete module (or, if inversion is genuinely still needed, keep the…
- 13 — A module accumulates many inbound dependents while still being “abstract enough” only in theory → Extract the parts of that package that other packages actually need into an abstract interface package, and have both the original concrete…
- 14 — A layering/direction rule was decided and documented but nobody has generated the actual import graph to see if it currently holds → Generate the dependency graph directly from the codebase's actual imports (not hand-drawn) as part of closing the decision, and re-run it w…
