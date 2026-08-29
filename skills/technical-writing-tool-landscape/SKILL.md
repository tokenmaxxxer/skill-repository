---
name: technical-writing-tool-landscape
description: >-
  Use when applying a Claude Code plugin/skill-ecosystem tool learning to a
  diagram, redraw, or accuracy-review-evidence decision elsewhere in this
  family. Applies to the tool-landscape axis — adoption evidence backing diagram
  cap values, "what changed" ledgers for redrawn diagrams, deterministic
  doc-code drift checkers. Trigger on requests like "다이어그램 도구 근거 대줘", "redraw
  ledger", "doc-code drift checker", "editorial diagram constraints evidence".
  Do NOT use for the diagram judgment rules themselves, such as choosing a
  deliverable's quadrant or its diagram polish-vs-update-cheapness call (use
  technical-writing-doc-type-selection).
metadata:
  axis: tool-landscape
  rule_count_floor: 3
---

# Tool-landscape learnings (Claude Code plugin/skill ecosystem)

Survey scope (issue #1199, 2026-08-14 amendment): the Claude Code
plugin/skill ecosystem, not general domain tools (Vale/Mermaid/
Docusaurus, kept as secondary context only). Each entry names the
axis-file rule it upgrades so the learning is applied, not merely
catalogued.

## Trigger

Apply this skill when a diagram, redraw, or accuracy-review-evidence
decision elsewhere in this family (doc-type-selection,
minimalism-scoping, style-guide-compliance) needs the ecosystem's
adoption evidence to back its cap values or evidence-shape choice —
distinguishing it from the other 5 skills, which state the judgment
rules directly rather than surveying tool adoption for them.

## Procedure

1. For an editorial-diagram cap/constraint decision (doc-type-selection
   rule 11, minimalism-scoping rule 11), cite the token/grid-constrained
   generator adoption evidence rather than an unconstrained "draw me a
   diagram" default (rule 1).
2. For a redrawn/regenerated diagram, keep a visible "what changed"
   ledger, extending style-guide-compliance's accuracy-review-evidence
   expectation to diagram edits (rule 2).
3. For an accuracy claim spanning multiple artifacts (docs, code,
   tests, CI), prefer a read-only, deterministic drift checker over a
   manual doc-code sync pass (rule 3).

## Output shape

A named upgrade to the specific rule (doc-type-selection rule 11,
minimalism-scoping rule 11, or style-guide-compliance's
accuracy-review-evidence expectation) being applied, backed by the
cited adoption evidence — not a new judgment call.

1. When a deliverable needs an editorial (non-diagram-as-code) diagram,
   prefer a token/grid-constrained generator over an unconstrained
   "draw me a diagram" prompt — freeform generation drifts toward a
   generic rounded-box look with inconsistent color/type per diagram,
   the failure mode a 14k+-star practitioner tool was built specifically
   to close (brand-color extraction, 4px grid, one accent color, 1-2
   focal elements, three fixed font families, automatic WCAG AA
   contrast check). Upgrades: doc-type-selection.md rule 11 and
   minimalism-scoping.md rule 11 (diagram-cost/visual-discipline
   judgments) — this entry is the adoption evidence for those two
   rules' cap values (grid/accent/font constraints), not new judgment.
   adoption: 14,471 GitHub stars (cathrynlavery/diagram-design,
   checked 2026-08-14). source:
   https://github.com/cathrynlavery/diagram-design

2. When redrawing an imported diagram (draw.io/Mermaid) at a new
   fidelity or size, keep a visible "what changed" ledger rather than
   silently regenerating — a reviewer comparing before/after needs the
   delta named, not just the new artifact, because diagram regeneration
   is exactly the kind of edit where visual diffing is unreliable.
   Upgrades: style-guide-compliance.md's accuracy-review-evidence
   expectation — extends it to diagram edits, not only prose/command
   claims. adoption: same tool as entry 1 (14,471 stars). source:
   https://github.com/cathrynlavery/diagram-design

3. Prefer a read-only, deterministic drift checker over a manual
   doc-code sync pass when the deliverable's accuracy claim spans
   multiple artifacts (docs, code, tests, CI) — a fixed checklist of
   drift checks catches staleness a single-document read cannot, and
   staying read-only avoids the checker silently "fixing" prose it
   misread. Upgrades: technical-writing.md's accuracy-review-evidence
   requirement — the design move to borrow is the deterministic,
   enumerated-check shape, not the specific check list, since this
   skill's actual accuracy evidence is repo commands/reads already
   named per-record. adoption: content-consistency-validator skill,
   part of a 2,630-star Claude Code plugin marketplace (checked
   2026-08-14). source:
   https://github.com/jeremylongshore/claude-code-plugins-plus-skills
