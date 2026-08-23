---
name: architecture-interface-contract-shape
description: >-
  Use when choosing the shape of a boundary contract between services or modules — sync vs.
  async, saga orchestration vs. choreography, shared-kernel vs. published-language context
  mapping, anticorruption layers, or interface surface segregation — at the architecture level,
  not field-level API design. Trigger on requests like "sync 호출을 이벤트로 바꿀까", "orchestration vs
  choreography for this saga", "ACL을 둘까 Conformist로 갈까", "BFF split for web and mobile". Do NOT
  use for deciding where the module/service boundary itself sits (use
  architecture-module-boundary-definition).
metadata:
  axis: interface-contract-shape
  rule_count_floor: 12
---

# Interface Contract Shape

Operational decision rules for the architecture role on choosing the SHAPE of a
boundary contract: sync vs async, shared-kernel vs published-language,
orchestration vs choreography, and interface surface area. Scope is
architecture-level shape, not API field-level design.

Layers researched this turn: (1) practitioner writeups on sync/async and
orchestration/choreography, (2) named DDD context-mapping patterns (Eric
Evans) and the Saga pattern and Interface Segregation Principle, (3)
academic/theory sources on information hiding (Parnas) and
consistency/latency tradeoffs (CAP/PACELC) in distributed systems.

## Trigger

Apply this skill when choosing the shape of a boundary contract: sync
vs. async communication, orchestration vs. choreography for a
distributed transaction, context-mapping pattern (Conformist, ACL,
Open Host Service, Shared Kernel) between two bounded contexts,
interface breadth/segregation, or a BFF split for divergent client
types.

## Procedure

1. Use synchronous request-response only when the caller is waiting in
   real time on the critical path (rule 1); route long-running or
   non-critical chained workflows through asynchronous messaging
   instead (rule 2); if an existing sync chain cascades failures
   upward, remove the synchronous hop in favor of async publication
   (rule 2b).
2. For a distributed transaction needing central visibility, use Saga
   orchestration (rule 3); for numerous independently-evolving
   participants with no owner willing to run a coordinator, use Saga
   choreography (rule 4); if a choreography chain grows past the point
   anyone can trace it, reintroduce an orchestrator or a process
   tracker rather than adding more links (rule 5).
3. When a downstream context has no leverage over an upstream model,
   adopt Conformist (rule 6); when integrating with an incompatible
   external system whose model would otherwise leak inward, build an
   Anticorruption Layer (rule 7); when exposing functionality to
   unknown/many consumers, expose an Open Host Service with a
   Published Language rather than bespoke per-consumer contracts
   (rule 8).
4. Adopt a Shared Kernel between two teams only with explicit joint
   ownership and a bounded, small surface (rule 9); if that kernel has
   grown without coordination and both teams now fight over changes,
   remove it and replace it with a Published Language or
   Conformist/Customer-Supplier split instead (rule 9b).
5. When two contexts' models have converged to a pass-through or
   diverged to irrelevance, remove the integration — collapse the ACL
   into a shared type, or mark the contexts Separate Ways (rule 10).
6. Split a fat interface per Interface Segregation so consumers depend
   only on the methods they use (rule 11); when an audit shows exported
   interface methods have zero live callers, delete them rather than
   keeping them "just in case" (rule 11b); when carving a new module
   boundary, expose only the minimal contract needed and hide
   likely-to-change decisions behind it (rule 12).
7. When one general-purpose backend API is accumulating client-specific
   branching to satisfy divergent client types, split into a Backend
   for Frontend per client type (rule 13).
8. Under latency/consistency pressure across wide-area or
   partition-prone boundaries, prefer asynchronous, eventually
   consistent contracts, reserving synchronous strongly-consistent
   calls for single low-latency failure domains (rule 14).

## Output shape

An interface-contract-shape decision: the axis choice made (sync/async,
orchestration/choreography, or a named DDD context-mapping pattern),
the rule number(s) applied, and — where a REMOVAL rule fires (2b, 9b,
10, 11b) — the surface deleted.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1 — Downstream call sits on the critical path of a user-facing request → Use synchronous request-response (REST/gRPC) only for this real-time, client-facing case; do not default every internal call to sync
- 2 — Long-running or non-critical workflow chained across services (e.g. order fulfillment, notifications) → Route the workflow through asynchronous messaging (queue/event bus) instead of a synchronous call chain
- 2b — Existing synchronous call chain crosses multiple services and a downstream outage cascades upward → **REMOVAL** — Remove the synchronous hop between A and B/C in favor of publishing an event B/C can consume asynchronously; collapse the cha…
- 3 — Distributed transaction spans several services and needs a single coordinator's view of state → Use Saga orchestration with an explicit orchestrator service issuing commands and handling compensation
- 4 — Distributed transaction's participants are numerous, evolve independently, and no team wants to own a coordinator → Use Saga choreography — each service publishes/reacts to domain events with no central coordinator
- 5 — A choreography-based saga's event chain has grown past the point anyone can trace it end to end → Introduce an orchestrator to reclaim explicit flow ownership for that specific saga, or add a dedicated process tracker; do not keep adding…
- 6 — Two bounded contexts need to integrate and one team controls the domain model, the other must comply → Adopt the Conformist pattern — downstream fully adapts to the upstream model rather than building a translation layer it cannot sustain
- 7 — Downstream context's domain concepts would otherwise be corrupted by an external system's model → Build an Anticorruption Layer (ACL) that translates the external system's interface into the local domain's own terms
- 8 — A context wants to expose functionality to arbitrary, unknown consumers rather than one negotiated partner → Expose an Open Host Service with a documented Published Language (well-defined shared schema/protocol) instead of bespoke per-consumer cont…
- 9 — Two teams share a subset of code/model between two bounded contexts to avoid duplication → Adopt Shared Kernel only with explicit joint ownership, a change-review process between both teams, and a small, deliberately bounded surfa…
- 9b — Shared Kernel has been growing without coordination and both teams now fight over changes to it → **REMOVAL** — Remove the Shared Kernel; split it, or replace it with a Published Language contract each side owns independently (Customer-S…
- 10 — Two contexts have fully diverged in domain concepts and integration cost now exceeds its value → **REMOVAL** — If models converged, collapse the ACL and merge the contexts' integration into a plain Conformist/shared type; if models are…
- 11 — A module's interface exposes many fine-grained methods but each consumer only uses a handful → Split the fat interface into smaller, client-specific interfaces per the Interface Segregation Principle; expose only the operations a give…
- 11b — A public module interface carries methods with zero live callers after a feature removal or refactor → **REMOVAL** — Delete the unused method(s) from the interface rather than leaving them "just in case"; do not keep dead surface area on a pu…
- 12 — Designing a new module boundary and deciding what the interface should reveal → Hide design decisions that are likely to change or are difficult, and expose only the minimal contract needed for correct use (signature, m…
- 13 — A single general-purpose backend API serves multiple very different client types (web, mobile, partner) → Split into a Backend for Frontend (BFF) per client type, each with its own tailored contract aggregating downstream services
- 14 — Choosing sync vs async under latency/consistency pressure at scale → Prefer asynchronous, eventually-consistent contracts across wide-area or partition-prone boundaries; reserve synchronous strongly-consisten…
- S1 — Conflicts between sources and resolution → references/rules.md
