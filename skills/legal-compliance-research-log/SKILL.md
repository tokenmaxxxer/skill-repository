---
name: legal-compliance-research-log
description: >-
  Use when you need to trace which source justifies a legal-compliance
  playbook rule, verify a rule's provenance, or extend the playbook's research
  to a new or amended axis. Trigger on requests like "where does this consent
  rule come from", "이 규칙 출처 추적해줘", "provenance of the SCC rule", "three-layer
  research audit". Do NOT use to apply the rules to a live compliance decision
  (use legal-compliance-lawful-basis-selection).
---

# Playbook research log — legal-compliance (issue #1174)

Evidence trail for `playbook/*.md`, recorded per the amendment-1
three-layer research protocol (practitioner knowledge / named
methodology-standard / academic theory). All sources listed here were
fetched live via WebSearch/WebFetch during this session on 2026-08-13,
not recalled from training. Tier: moderate (batch 7, per
`docs/issue-1174/proposals/operational-playbook-program.md` (b));
per-axis floor = max(8, axes x 2) = max(8, 12) = 12 total, per-axis
`rule_count_floor: 2`; 6 axes x 4 rules landed = 24 rule blocks across
the 6 files.

## Trigger

Apply this skill when a playbook rule's source/provenance needs tracing
back to its fetched citation, when auditing whether the three-layer
research protocol (practitioner / named-standard / academic) and the
removal-rule coverage requirement were actually satisfied, or when a new
or amended axis needs its research trail recorded — distinguishing it
from the other 6 legal-compliance skills, which apply already-sourced
rules rather than tracing or extending their provenance.

## Procedure

1. To trace a specific playbook rule's source, look up its owning axis
   section below (## Axis: lawful-basis-selection, ##
   Axis: retention-and-minimization, ## Axis:
   cross-border-transfer-mechanism, ## Axis: consent-mechanism-ux, ##
   Axis: vendor-dpa-requirements, or ## Axis: oss-license-compatibility)
   and match the rule number to its cited layer and URL.
2. To audit three-layer coverage for an axis, confirm its section cites
   at least one named-legal-standard/primary-text source (layer 1/2) and
   at least one practitioner-synthesis source (layer 1), per the
   per-axis entries below.
3. To audit removal-rule coverage, cross-check the target axis's file
   against the ## Removal-rule coverage check list, and against the
   academic-layer cognitive-bias citation grounding why an all-additive
   playbook is insufficient.
4. To extend the research trail for a new or amended axis, add a new
   `## Axis: <name> -> <path>` section following the same
   layer-tagged, live-fetched-source format used by the existing six.

## Output shape

For a trace request: the fetched URL(s) and quoted standard text backing
a named rule. For a coverage audit: a pass/fail per axis against the
three-layer requirement and the removal-rule coverage list. For an
extension: a new `## Axis:` section appended in the existing format.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — Axis: lawful-basis-selection -> `playbook/lawful-basis-selection.md` → references/rules.md
- S2 — Axis: retention-and-minimization -> `playbook/retention-minimization.md` → references/rules.md
- S3 — Axis: cross-border-transfer-mechanism -> `playbook/cross-border-transfer.md` → references/rules.md
- S4 — Axis: consent-mechanism-ux -> `playbook/consent-ux.md` → references/rules.md
- S5 — Axis: vendor-dpa-requirements -> `playbook/vendor-dpa.md` → references/rules.md
- S6 — Axis: oss-license-compatibility -> `playbook/license-compatibility.md` → references/rules.md
- S7 — Sources fetched but not used as a rule citation → references/rules.md
- S8 — Removal-rule coverage check (amendment 4) → references/rules.md
