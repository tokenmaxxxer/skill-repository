---
name: technical-writing-tool-landscape
description: Use when you need guidance on Tool-landscape learnings (Claude Code plugin/skill ecosystem). Applies to the tool-landscape axis.
axis: tool-landscape
rule_count_floor: 3
---

# Tool-landscape learnings (Claude Code plugin/skill ecosystem)

Survey scope (issue #1199, 2026-08-14 amendment): the Claude Code
plugin/skill ecosystem, not general domain tools (Vale/Mermaid/
Docusaurus, kept as secondary context only). Each entry names the
axis-file rule it upgrades so the learning is applied, not merely
catalogued.

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
   role's actual accuracy evidence is repo commands/reads already
   named per-record. adoption: content-consistency-validator skill,
   part of a 2,630-star Claude Code plugin marketplace (checked
   2026-08-14). source:
   https://github.com/jeremylongshore/claude-code-plugins-plus-skills
