---
name: product-discovery-opportunity-solution-tree
description: >-
  Use this skill whenever opportunity/outcome framing work recurs — i.e. whenever
  opportunity/outcome framing is drafted or re-affirmed with the user — to update the living
  Opportunity Solution Tree in product/opportunity-tree.md. Trigger on requests like "기회 트리
  업데이트해줘", "add this interview finding to the opportunity tree", "refresh the OST this
  week", "hang this solution under its opportunity". It is cross-cutting, runs on its own
  cadence independent of any hypothesis's state, and its artifact is never the product-cycle
  state file (no gate). Do NOT use for the axis-level rules on layer placement,
  prioritization, or pruning branches (use
  product-discovery-opportunity-solution-tree-branching).
---

# Opportunity Solution Tree maintenance

**Cadence:** cross-cutting; recurs with each scoping re-affirmation (not a
one-time step of any single state). Teresa Torres's practice treats this as
continuous, weekly-cadence maintenance, not a phase that starts and ends —
see `docs/reports/research/2026-07-27-role-practice/product.md`.

**What it asks the user for:** which opportunity or solution the tree
should be updated with this cycle, sourced back to specific customer
interview evidence where available.

**What it produces:** the Opportunity Solution Tree, four layers, top to
bottom:

1. **Desired outcome** — one node, a business metric.
2. **Opportunities** — customer needs/pains/desires (can nest).
3. **Candidate solutions** — per opportunity.
4. **Assumption tests** — per solution, at the leaves.

**Where it is written:** `product/opportunity-tree.md`.

**This artifact is explicitly outside the gate.** It is not
`docs/issue-<n>/reports/product-discovery.md` —
the record gate does not check writes to this file at all. Update it as
often as new interview evidence arrives; do not wait for a state
transition to justify writing to it.

## Trigger

Apply this skill whenever the `scoping to scoping` self-loop fires —
i.e. whenever opportunity/outcome framing is drafted or re-affirmed
with the user — to update the living Opportunity Solution Tree. This is
cross-cutting and runs on its own cadence, independent of any single
hypothesis's state; do not use it to register a hypothesis or to gate
any transition — it has no gate.

## Procedure

1. When the scoping re-affirmation moment comes up, ask which
   opportunity or solution should be added or updated this cycle (see
   `## How to run the conversation`).
2. Confirm which desired-outcome node it hangs under, creating one if
   none exists yet (see `## How to run the conversation`).
3. Ask whether new interview evidence supports it and record the
   evidence source alongside the node, never a stakeholder's unsourced
   opinion as if it were customer evidence (see `## How to run the
   conversation`).
4. Write or update `product/opportunity-tree.md` with the four-layer
   structure, outside the record gate entirely (see `## Where it is
   written`).

## Output shape

`product/opportunity-tree.md`, four layers top to bottom (desired
outcome, opportunities, candidate solutions, assumption tests), each
opportunity/solution node sourced to interview evidence where
available, maintained continuously outside the gated state file.

## How to run the conversation

1. When the scoping re-affirmation moment comes up, ask the user
   which opportunity or solution should be added or updated in the tree
   this cycle.
2. Confirm which desired outcome node it hangs under (create one if none
   exists yet).
3. Ask whether new interview evidence supports it, and if so, record the
   evidence source (which customer conversation) alongside the
   opportunity/solution node — per the interaction research's rule that a
   vague, unsourced claim should not be written into the tree as if it
   were evidence.
4. Write/update `product/opportunity-tree.md` with the four-layer
   structure above.

## Common mistakes this skill exists to prevent

- Treating this as a one-time artifact instead of a living document
  updated on an ongoing cadence.
- Recording a stakeholder's unsourced opinion as if it were customer
  evidence in the tree.
- Gating any state transition on this file — it has none; it stays
  outside `docs/issue-<n>/reports/product-discovery.md` and outside the record gate entirely.
