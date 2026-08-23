---
name: architecture-coupling-classification
description: >-
  Use when classifying the type and severity of coupling between two components — shared data or
  global state, control flags, struct passing, internal reach-through, timing/deploy ordering,
  import cycles, or chatty call chains — and deciding whether to leave, weaken, or remove it.
  Trigger on requests like "이 모듈들 결합도 좀 봐줘", "classify this coupling", "shared database between
  services, how bad is it", "instability metric says split — should we". Do NOT use for deciding
  which way a dependency arrow should point (use architecture-dependency-direction).
metadata:
  axis: coupling-classification
  rule_count_floor: 12
---

# Coupling Classification — Operational Decision Rules

Scope: how to identify and classify coupling between components (afferent/efferent,
temporal, data, control coupling, connascence) and what corrective action to take.
Sources span three layers: practitioner writeups, named methodology (Constantine &
Yourdon structured design, Robert Martin's instability metric, Page-Jones/Weirich
connascence), and academic/theory (Stevens, Myers & Constantine 1974).

## Trigger

Apply this skill when reviewing or designing a dependency between two
components and you need to name the coupling type at play — a shared
global/database table, a control flag steering callee behavior, a
struct/DTO passed for one field, direct reach-through into another
module's internals, hand-coordinated deploy ordering, an unstable
dependency below a stable one, a shared magic literal, implicit
startup/shutdown timing, a god config object, an import cycle, or a
chatty synchronous call chain — and decide whether to leave it, weaken
it, or remove it.

## Procedure

1. Classify the coupling by its concrete shape: shared mutable
   global/database table (rule 1), a shared physical database across
   microservices (rule 2), hand-coordinated deploy/release timing
   (rule 3), a control/mode flag steering callee behavior (rule 4), a
   whole struct passed for one field (rule 5), direct reach into
   another module's private internals (rule 6), a magic shared literal
   with no enforcing symbol (rule 9), implicit startup/shutdown timing
   (rule 10), a god config object threaded through many modules
   (rule 11), an import/dependency cycle (rule 12), or a chatty
   synchronous cross-service call chain (rule 13).
2. Before trusting Robert Martin's instability metric (I = Ce/(Ca+Ce))
   alone, use it only as a triage signal, then classify the actual
   dependency by connascence strength/Constantine coupling type before
   judging severity (rule 1 of Cross-source conflicts).
3. For a component with high afferent coupling that also changes often,
   flag a Stable Dependencies Principle violation and freeze its
   interface (rule 7); for a component that depends on something less
   stable than itself, insert an abstraction/dependency inversion
   instead (rule 8).
4. For a stable-but-concrete package accumulating dependents, extract
   an abstract interface package (this rule is shared with the
   dependency-direction axis; see rule 13 there) — within this axis,
   apply rules 7/8 for the stability-direction judgment itself.
5. Once classified, apply the paired corrective action: REMOVAL rules
   (1, 2, 4, 6, 11, 12) delete or restructure the coupling; non-REMOVAL
   rules (3, 5, 7, 8, 9, 10, 13) narrow, invert, or make the coupling
   explicit instead of deleting it.
6. Never gate a design review purely on a coupling/cohesion metric
   threshold — pair the metric with a human classification of coupling
   type before deciding to act (rule 14).
7. When structural severity and observed change cost diverge — a
   moderate-ranked component is co-edited constantly, or a severe one
   is frozen — reprioritize remediation by observed co-change frequency
   from commit history, not by structural ranking alone (rule 15).

## Output shape

A coupling classification: the coupling type (common, control, stamp,
content, temporal, or connascence variant), the rule number(s) applied,
and the corrective action — REMOVAL, narrowing, or explicit
documentation — with its rationale.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **Instability metric vs. dependency quality.** Robert Martin's `I = Ce/(Ca+Ce)` ranks components purely by dependency *count*. coupling.dev's critique notes a component…
- 1.2 — **"Reduce coupling" vs. "coupling is unavoidable."** Fowler's structured-design lineage and connascence both agree coupling cannot be eliminated, only shaped: Weirich's…
- 1.3 — **Microservice writeups vs. classical structured-design vocabulary.** Modern distributed-monolith/shared-database writeups use different words (service coupling, chatty…
- 1 — Two modules share a mutable global or a shared database table/schema → Classify as **common coupling** (Constantine/Yourdon). Assign single ownership of the data to one component; all others must access it only…
- 2 — Microservices share one physical database → Split the schema so each service owns its own tables; replace direct cross-service queries with an API call or an event the owning service…
- 3 — Deploy order or release timing between two services is coordinated by hand → Classify as **temporal coupling**. Introduce a versioned/backward-compatible contract (e.g. additive schema changes, consumer-driven contra…
- 4 — One function takes a boolean/enum "mode" flag that changes callee behavior → Classify as **control coupling** (Constantine/Yourdon). Split the function into separate functions per behavior, or invert control so the c…
- 5 — A function passes a whole record/struct when it only uses one field → Classify as **stamp coupling**. Narrow the parameter to just the field(s) used, or if the structure is a legitimate shared concept, keep st…
- 6 — Module directly reaches into another module's internals (private fields, patched code) → Classify as **content coupling**, the worst type in the 1974 taxonomy. Refactor to go only through the module's declared public interface;…
- 7 — A component has very high afferent coupling (Ca) and also changes often → Flag as an instability violation — per Robert Martin's Stable Dependencies Principle, high-Ca components should be the most stable (I near…
- 8 — A component depends on something less stable than itself → This violates Martin's Stable Dependencies Principle. Insert an abstraction (interface/port) that X depends on instead, with Y implementing…
- 9 — Two classes reference each other only by a shared literal (magic string/number/name) → Classify as connascence of Name/Meaning (or worse, connascence of Position if order-dependent). Replace the duplicated literal with a singl…
- 10 — Two services rely on identical startup/shutdown ordering or shared runtime timing → Classify as connascence of Timing / temporal coupling. Replace implicit ordering with an explicit readiness check, event, or queue-based ha…
- 11 — A shared "god" configuration object is threaded through many unrelated modules → Classify as stamp coupling at architectural scale. Split the object into per-consumer config slices owned by the modules that actually need…
- 12 — A circular import/dependency exists between two modules or services → Classify as a violation of Martin's Acyclic Dependencies Principle (a degenerate, maximal form of control/common coupling). Break the cycle…
- 13 — Chatty synchronous call chains across service boundaries → Classify as efferent coupling concentrated in one orchestrating service plus temporal coupling across the chain. Either consolidate the cha…
- 14 — Cohesion/coupling metrics used as the sole gate for a design review → Do not gate on the metric alone — academic research found difficulties using cohesion and coupling metrics as standalone quality indicators…
- 15 — Structural coupling severity and actual change cost diverge → Reprioritize remediation order by pairing the structural classification (rules 1-14) with observed co-change frequency from commit history;…
