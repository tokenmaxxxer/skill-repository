---
status: proposed
files:
  - docs/issue-82/reports/content-design/survey.md
  - docs/issue-82/proposals/content-strategy-skill-family.md
---

# Content-strategy skill family (phase 1: research + proposal)

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): the current-state survey required by
the survey-before-proposal norm already exists on disk at
`docs/issue-82/reports/content-design/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic
`docs/issue-82/reports/implementation/survey.md` path, since this role
writes only its own record area under
`docs/issue-82/reports/content-design/` and never another role's
`reports/implementation/` tree. No design decision remains open beyond
what that survey and this proposal already resolve (the three-skill
split below) — there is nothing a second survey copy at the
implementation path would add.

## Request

Issue #82 (professional-discipline gap #4 of 5): research-first,
primary-sourced (Halvorson/Rach *Content Strategy for the Web* lineage;
the content-audit method — quantitative inventory vs. qualitative
audit; content-governance/ownership models — RACI, centralized/
decentralized/hybrid) survey of the content-strategy discipline, then
propose a `content-strategy-*` skill family of >=3 skills
(`editorial-calendar-and-cadence`, `content-audit-and-inventory`,
`content-governance-ownership`), each with a condition-matched "Use
when" trigger, per-rule `source:` citations, and resolving
`Related-skills` links to `content-design-operational-playbook`,
`devrel-*`, and `marketing-*` where they chain. Phase 1 (survey +
proposal) only; authoring the actual `skills/content-strategy-*/
SKILL.md` files is phase 2, gated on approval.

## Constraints

- Every rule proposed below must trace to a primary source with a live
  URL, verified in `survey.md` (issue acceptance criterion).
- >=3 skills, axis-split, no content overlap between them or with
  `content-design-operational-playbook`.
- Each skill's `description` must carry a distinct "Use when..."
  trigger.
- `Related-skills` cross-references must resolve to real, existing
  skill directory names.
- `scripts/check_skill_conformance.py` must stay green once phase 2
  authors the actual SKILL.md files.
- Sources must appear in the PR body (issue acceptance criterion).

## Rationale

Two structural alternatives were considered, given what the survey
found.

1. **Two skills, folding governance/ownership into the audit skill,
   since a content audit is often what surfaces the governance gap in
   the first place (an audit finds orphaned content with no owner).**
   Rejected: the survey's Angle 2 and Angle 3 findings show these are
   separable decisions with separable trigger conditions. An audit
   task fails by skipping the quantitative-inventory step before
   qualitative judgment (Halvorson & Rach's "robot-free zone"
   distinction); a governance task fails by having no single
   Accountable owner or by picking the wrong centralized/decentralized/
   hybrid model for the org's scale (Content Strategy Inc.'s RACI
   rules). A team could run a content audit on a domain that already
   has clear ownership (nothing to fix there), or set up a governance
   model for content that has never been audited (a net-new content
   type). Collapsing them would force every audit invocation to also
   load ownership-model rules it may not need, breaking this repo's
   axis-triggered dispatch convention (confirmed against `devrel-*`
   and `market-analysis-*`'s own axis-disjoint splits).
2. **Fold editorial-calendar-and-cadence into
   `content-design-operational-playbook` as a new axis, since both are
   "content" skills and the existing skill already has a working
   Trigger/Procedure/Sources shape.** Rejected: the survey's Angle 1
   finding is that Halvorson's own sub-discipline split places
   editorial strategy (calendar, cadence, content lifecycle) and
   content-design/UX-writing craft (sentence-level wording, covered by
   the existing skill) in different sub-disciplines with different
   failure modes — a calendar/cadence task fails by publishing
   content with no lifecycle plan (nothing retires stale content, no
   cadence commitment), while the existing skill's failure modes are
   wording-level (jargon, missing plain-language pass). The existing
   skill's own description is scoped to "user-facing copy... tone-of-
   voice, copy-inventory reuse" at the string level; a calendar/cadence
   trigger ("is this editorial calendar covering the right cadence")
   never fires that condition. Keeping them separate matches this
   repo's convention that a family's internal skills split by decision
   axis, not by shared subject-matter label.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
primary-source findings across all four scouted angles. This proposal
specifies the three skills to author in phase 2.

### Proposed family: `content-strategy-*` (3 skills)

**1. `content-strategy-editorial-calendar-and-cadence`**
(axis: `lifecycle-and-cadence-planning`)

- Use when: planning or reviewing an editorial calendar, committing to
  a publishing cadence, or deciding a content asset's lifecycle stage
  (create, update, retire).
- Core rules (source-cited to Halvorson, "The Discipline of Content
  Strategy," and Halvorson & Rach, *Content Strategy for the Web*):
  - Editorial strategy governs values, voice, tone, legal/regulatory
    concerns, and the organization's editorial calendar including
    content life cycles — a calendar entry with no retirement/review
    date is an incomplete lifecycle plan, not just a scheduling gap.
  - Route sentence-level wording, tone-of-voice-per-string, and
    plain-language decisions to `content-design-operational-playbook`
    rather than re-deciding them inside calendar planning — the
    calendar owns *when and whether*, not *how it reads*.
- `Related-skills`: `content-design-operational-playbook` (wording/
  tone-of-voice decisions once a calendar slot is confirmed);
  `marketing-channel-selection` (channel choice for a calendar entry
  spanning marketing content); `content-strategy-content-governance-
  ownership` (when a calendar has no owner committed to the cadence).

**2. `content-strategy-content-audit-and-inventory`**
(axis: `enumeration-vs-judgment-task-type`)

- Use when: starting a content audit, building a content inventory, or
  deciding whether a content-assessment task needs quantitative
  enumeration, qualitative judgment, or both in sequence.
- Core rules (source-cited to Halvorson & Rach's quantitative-
  inventory/qualitative-audit distinction):
  - Classify the task first: a content inventory is quantitative
    (accounting of every asset — URL/type/owner/last-updated, no
    judgment calls); a content audit is qualitative (quality,
    structure, voice/tone fit, usefulness — requires human judgment).
    "The key distinction... is human judgement" — do not let a
    quantitative crawl stand in for a qualitative quality assessment.
  - Run the quantitative inventory before the qualitative audit, never
    the reverse — a qualitative judgment on an unenumerated asset set
    is ungrounded (you cannot assess "is this complete" without first
    knowing what exists).
- `Related-skills`: `content-strategy-content-governance-ownership`
  (an audit that surfaces an unowned or orphaned asset routes the
  ownership question there, not into the audit's own scoring);
  `devrel-content-comprehensibility` (when the audited asset is
  developer-facing content, comprehensibility scoring routes there).

**3. `content-strategy-content-governance-ownership`**
(axis: `accountability-and-decision-rights`)

- Use when: assigning ownership for a content domain, resolving who
  has final sign-off on a content decision, or choosing between a
  centralized, decentralized, or hybrid governance model for content
  across teams.
- Core rules (source-cited to Content Strategy Inc.'s RACI-for-content
  guidance and the converged centralized/decentralized/hybrid
  taxonomy):
  - Assign exactly one Accountable owner per content domain — final
    sign-off authority must not be split across more than one person;
    where an audit or calendar surfaces a domain with zero or multiple
    A's, that is the governance defect to fix before anything else.
  - Choose the governance model by organizational scale and update
    frequency, not default inertia: centralized when one team can
    still keep up with volume without becoming a bottleneck,
    decentralized when domains are independent enough to not need
    cross-team consistency, hybrid (central standards, team-level
    execution) as the default fit for a growing organization that
    needs both consistency and throughput.
- `Related-skills`: `content-strategy-editorial-calendar-and-cadence`
  (an ownerless calendar entry routes back here before scheduling);
  `content-strategy-content-audit-and-inventory` (an audit's orphaned-
  asset findings route here for an ownership decision);
  `partnerships-bd-governance-cadence-and-kpi` (where a content domain
  is jointly owned with an external partner, the two chain rather than
  duplicate).

## Out of scope

- Authoring the actual `skills/content-strategy-*/SKILL.md` files
  (phase 2).
- Sentence-level wording, tone-of-voice-per-string, or plain-language
  rules — already owned by `content-design-operational-playbook` (see
  Rationale, alternative 2).
- Channel/format selection for devrel or marketing content — already
  owned by `devrel-channel-convention` and `marketing-channel-
  selection`; this family only supplies the calendar/audit/governance
  layer above those choices.

## How you'll know it worked

- `docs/issue-82/reports/content-design/survey.md` and this proposal
  exist on disk, phase-1 committed, PR opened against `main`
  referencing `#82` (no Closes/Fixes trailer at this phase).
- On approval (phase 2): three `skills/content-strategy-*/SKILL.md`
  files exist, each with a distinct "Use when" trigger, per-rule
  `source:` citations matching this survey, and `Related-skills` links
  that resolve to real directories; `scripts/check_skill_conformance.py`
  runs green over the full repo.
