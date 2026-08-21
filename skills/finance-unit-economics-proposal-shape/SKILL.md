---
name: finance-unit-economics-proposal-shape
description: Use when you need guidance on Proposal shape — decision rules. Applies to the proposal-shape axis.
axis: proposal-shape
rule_count_floor: 12
tier: moderate
---

# Proposal shape — decision rules

## Decision rules

- **ADDITION**: when a unit-economics proposal reaches a reader who
  will act on it under time pressure, apply progressive disclosure —
  headline metric first, supporting drivers behind a fold — rather than
  presenting every input at once, because well-structured, load-reduced
  presentation measurably speeds decisions. source:
  https://www.fegno.com/designing-enterprise-dashboards-with-cognitive-load-theory/
  (progressive disclosure reduces extraneous cognitive load; well
  designed dashboards improve decision speed by 58.7%).

- **ADDITION**: when a proposal presents more than one viable pricing or
  cost structure, cap the compared options at three (base/bull/bear or
  equivalent) rather than an open list — an unbounded option set induces
  decision fatigue and stalls the decision this proposal exists to
  produce. source:
  https://lifestyle.sustainability-directory.com/question/how-can-minimalism-reduce-decision-fatigue/
  (restricting options to essential choices hastens decisions; abundant
  options increase anxiety and postponement).

- **REMOVAL**: when a slide or section adds a metric, actively look for
  one metric already covered by it to cut in the same edit, rather than
  only adding — reviewers systematically fail to consider subtractive
  edits unless explicitly prompted to look for them, even when the
  subtractive edit is strictly better, so this check must be a
  deliberate proposal-shape step, not an assumed side effect of
  reviewing. source: https://www.nature.com/articles/s41586-021-03380-y
  (Adams, Converse, Hales & Klotz 2021 — participants across eight
  tasks systematically failed to identify available subtractive
  solutions, even when primed to look for them).

- **REMOVAL**: for a proposal whose glossary section defines terms with
  no attached condition or choice, cut that section entirely rather
  than let it stand in for decision rules — a definition-only block
  ("CAC is...") looks like guidance but gives a reader nothing to act
  on, which is exactly the shape this rulebook's own depth gate rejects.
  source: gates/playbook_depth_gate.py glossary-shape check (issue
  #1174 (c) check 4) — https://github.com/tokenmaxxxer/on-the-record
  gates/playbook_depth_gate.py.

## Notes

This axis is where the other five axes' outputs get assembled for a
reader; a proposal that cites cac-payback.md and ltv-cac-band.md but
skips evidence-chain.md's sourcing rule is incomplete.
