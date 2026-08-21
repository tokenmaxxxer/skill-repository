---
name: observability-phase-trace
description: Use when you need guidance on Phase-1 to phase-2 methodology-consistency. Applies to the phase-trace axis.
axis: phase-trace
rule_count_floor: 3
---

# Phase-1 to phase-2 methodology-consistency

Decision rules for keeping the phase-2 record's implemented signals
consistent with the methodology phase-1 named for that surface, and for
handling deliberate deviation. Research trail: layer 2 (Google SRE
Workbook's SLI-definition-to-implementation traceability practice)
plus layer 1 (practitioner drift-detection patterns for design-vs-build
divergence).

## Rules

1. When phase-1 already named a methodology for a surface (RED, USE, or
   Golden Signals), phase-2's record must instrument exactly that
   methodology's signal set on that surface — the SRE Workbook's SLI
   practice treats the SLI definition chosen up front as the contract
   the implementation is measured against, and an implementation that
   silently substitutes a different signal set breaks that
   traceability even if the substitute is individually reasonable.
   source: https://one2n.io/blog/sre-math-percentiles-in-sre-why-averages-lie-about-latency

2. When phase-2 implementation reveals the phase-1 surface
   classification was wrong (e.g. what looked request-driven turns out
   to be resource-bound because it has no per-call boundary), the
   record must state the deviation and the corrected methodology
   explicitly rather than instrument the corrected methodology silently
   — an unstated deviation reads, to a later reviewer diffing phase-1
   against phase-2, as a bug rather than a deliberate correction; SLI/
   SLO traceability practice treats an unexplained target change as a
   red flag precisely because it is indistinguishable from drift.
   source: https://one2n.io/blog/sre-math-percentiles-in-sre-why-averages-lie-about-latency

3. **REMOVAL**: when a phase-2 record carries signals for a methodology
   phase-1 did NOT name (e.g. USE panels added to a surface phase-1
   classified request-driven and assigned RED) with no stated
   reclassification, remove the extra unstated signals from the record
   rather than leave them as an unexplained superset — an unexplained
   superset of signals is exactly as untraceable as an unexplained
   substitution (rule 2), because a reviewer cannot tell whether the
   extra signals reflect a considered decision or scope creep. source:
   https://one2n.io/blog/sre-math-percentiles-in-sre-why-averages-lie-about-latency
