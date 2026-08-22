---
status: proposed
files:
  - skills/research-evidence-discipline/SKILL.md
  - skills/market-analysis-evidence-rigor/SKILL.md
  - skills/product-discovery-hypothesis-testing/SKILL.md
  - skills/growth-analytics-experiment-trust/SKILL.md
  - skills/user-discovery-evidence-strength-tagging/SKILL.md
---

# Proposal: shared evidence-discipline procedure skill (issue-61)

## Request

Author a new, independently-written shared skill covering three
mechanisms that the four research-shaped families (market-analysis,
product-discovery, growth-analytics, user-discovery) currently lack:
Fact/Inference/Assumption labeling of claims, an explicit do-not-invent
list, and a question-budget cap. Layer it on top of the existing
per-rule `source:` citation discipline rather than replace it. Link it
from each of the four families via a `Related-skills` line so a session
already in one family's Procedure discovers it. The reference repo
(deanpeters) is inspiration only — license status is unclear, so no
sentence may be ported; every rule here must be sourced independently.

## Constraints

- No text copied from the deanpeters repo — spot-checkable, per the
  issue's acceptance line. This proposal's author did not fetch or
  read that repo's text at all (see survey.md's skip note), to make
  contamination structurally impossible rather than merely avoided.
- Must pass `scripts/check_skill_conformance.py`: `## Trigger`,
  `## Procedure`, `## Output shape` headings, a `## Rules` section
  meeting whatever `rule_count_floor:` is declared, every rule carrying
  a `source:` line, and (from issue-60/#71) any `## Related skills`
  bullet must relative-link to a file that actually resolves.
  Conformance green is a named acceptance criterion.
  scripts/check_skill_conformance.py, git show 8048367.
- Must not duplicate `market-analysis-evidence-rigor`'s existing
  per-rule sourcing discipline — the new skill is additive (claim
  labeling, do-not-invent, question budget), not a restatement of
  "cite your sources."
- Each family gets exactly one inbound `Related-skills` link, matching
  the granularity issue-60/#71 already established (12 curated pairs
  across the whole repo, not a link from every sub-skill in a family).
  survey.md, §Related-skills machinery.
- Tooling note: this session's real current-state survey lives at
  `docs/issue-61/reports/knowledge-management/survey.md` (the
  role-correct path board-gate.sh requires for the knowledge-management
  role). `survey-order-gate.sh` independently checks a hardcoded
  `docs/issue-61/reports/implementation/survey.md` path regardless of
  the writing role, and board-gate.sh separately refuses a
  knowledge-management-role write under `reports/implementation/**` as
  a foreign-role record — the two gates are mutually exclusive for any
  non-implementation role. Confirmed by direct test in this session
  (Write attempts to both the role-correct and the gate-hardcoded path
  were tried; only the role-correct path is accepted by board-gate).
  This is a gate-path mismatch, not a scout skip condition: no skip
  condition applies here — a full current-state survey was completed
  and committed before this proposal was drafted, exactly as the survey
  directive requires.

## Rationale

**Where the new skill lives.** Considered making it a peer axis-skill
inside one of the four families (e.g.
`market-analysis-evidence-discipline`), scoped to that family only, and
letting the other three families independently grow their own copies
later. Rejected: the three mechanisms (claim labeling, do-not-invent,
question budget) are family-agnostic — nothing about Fact/Inference/
Assumption labeling is market-analysis-specific — so scoping it to one
family would force either duplication (four near-identical skills,
the exact anti-pattern issue-60 spent effort consolidating away from)
or an awkward cross-family dependency from whichever family didn't get
the canonical copy. A single top-level shared skill
(`skills/research-evidence-discipline/`), referenced by all four via
the existing Related-skills mechanism, avoids both. survey.md confirms
no family currently has this at all, so there's no existing asymmetric
placement to preserve either.

**Shape: axis-style (Trigger/Procedure/Rules) vs. harness-style
(prose, like `user-discovery/SKILL.md`).** Considered the harness shape,
since it's already used once in this exact family set. Rejected: the
harness shape exists for `user-discovery` because that skill designs
*and* analyzes a whole study — a genuinely multi-stage workflow. The
three mechanisms here are each single decision rules invoked
mid-record ("is this claim sourced or must it be labeled an
assumption," "is this about to invent something," "has the question
budget been spent") — exactly the shape the other 25 axis sub-skills
already use, and the shape the conformance script's
`PROCEDURE_HEADINGS`/`rule_count_floor` checks are built around.
Matching the dominant shape also makes the Related-skills link read as
a peer reference, not a jump to a different kind of artifact.
survey.md, §Conformance shape.

**Which single skill per family anchors the inbound link.** Rejected
picking the alphabetically-first or most-recently-touched skill in each
family (arbitrary, no substantive connection) in favor of picking each
family's existing skill whose own axis is nearest to evidence handling:
`market-analysis-evidence-rigor` (already sourcing-discipline-shaped),
`product-discovery-hypothesis-testing` (a hypothesis is exactly a
claim that needs a Fact/Inference/Assumption label before it's tested),
`growth-analytics-experiment-trust` (experiment trust already turns on
whether a result is real evidence or a fabricated/over-read signal),
`user-discovery-evidence-strength-tagging` (already grades claim
strength, the nearest existing analog to Fact/Inference/Assumption).
Each pairing is substantive, not decorative, satisfying the
Related-skills convention's own bar. survey.md, family/anchor table.

**Conformance script changes: none proposed.** Considered adding a new
check dedicated to the three mechanisms (e.g. a script rule requiring
"Fact:/Inference:/Assumption:" tokens to appear in any research-family
output). Rejected for this issue: the acceptance criterion is
"conformance green" against the *existing* checks (Trigger/Procedure/
Output-shape, rule sourcing, link resolution) — it does not ask for a
new enforcement mechanism, and inventing one here would be scope
creep beyond what issue-61 asks for. If a future issue wants the
discipline mechanically enforced (not just documented), that is a
separate, larger scope-gate change to `check_skill_conformance.py`.

## What will be done

Phase 2 (after Approve) will:

1. Create `skills/research-evidence-discipline/SKILL.md` as a new
   axis-style skill with `## Trigger`, `## Procedure`, `## Output
   shape`, and `## Rules` sections covering the three mechanisms:
   - Fact/Inference/Assumption labeling rules (when a claim must carry
     which label, and what changes the label).
   - An explicit do-not-invent list (named categories of content the
     skill must never fabricate — e.g. quotes, named people/companies,
     precise unsourced figures — as a checkable list, not a vague
     admonition).
   - A question-budget cap rule (when accumulating open questions in a
     record signals the session should stop asking and proceed on
     labeled assumptions instead).
   Every rule gets an independent `source:` citation (general
   evidence-discipline / confabulation-avoidance literature, or this
   repo's own prior art per survey.md) — none ported from deanpeters.
2. Add one `## Related skills` bullet to each of the four anchor files
   named in `files:` above, linking to
   `../research-evidence-discipline/SKILL.md`, each with a one-clause
   "why this pairs" note specific to that family's axis (per Rationale
   above).
3. Run `scripts/check_skill_conformance.py` and confirm green before
   the phase-2 record is written.

## Out of scope

- Fetching, reading, or referencing the deanpeters repo's actual text
  in any form.
- Any new conformance-script check enforcing the three mechanisms
  mechanically (see Rationale).
- Linking the new skill from every one of the 26 sub-skills across the
  four families — only the four named anchors get inbound links.
- Editing `user-discovery/SKILL.md` (the harness hub) — the anchor for
  that family is `user-discovery-evidence-strength-tagging`, an
  existing axis sub-skill, not the harness file.
- Retrofitting any of the four families' existing per-rule `source:`
  discipline — this skill is additive, not a rewrite of what already
  exists.

## How you'll know it worked

- `skills/research-evidence-discipline/SKILL.md` exists, passes
  `scripts/check_skill_conformance.py`, and its `## Rules` section
  covers all three named mechanisms with independent `source:` lines
  each.
- Each of the four anchor files (`market-analysis-evidence-rigor`,
  `product-discovery-hypothesis-testing`, `growth-analytics-experiment-trust`,
  `user-discovery-evidence-strength-tagging`) carries a `## Related
  skills` bullet linking to the new skill, and the link resolves
  (issue-60/#71's link-resolution check passes).
- `python3 scripts/check_skill_conformance.py` runs green across the
  repo (or at minimum across the five touched files, if the full-repo
  run is out of this session's time budget — noted explicitly either
  way in the phase-2 record).
- A spot-check of the new skill's rule text against the deanpeters
  repo (if a reviewer chooses to do one) finds no copied sentence.
