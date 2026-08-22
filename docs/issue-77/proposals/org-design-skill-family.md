---
status: proposed
files:
  - docs/issue-77/reports/knowledge-management/survey.md
  - docs/issue-77/proposals/org-design-skill-family.md
---

# Organization/HR-design skill family (phase 1: research + proposal)

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): the current-state survey required by
the survey-before-proposal norm already exists on disk at
`docs/issue-77/reports/knowledge-management/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic
`docs/issue-77/reports/implementation/survey.md` path, since this role
writes only its own record area under
`docs/issue-77/reports/knowledge-management/` and never another role's
`reports/implementation/` tree. No design decision remains open beyond
what that survey and this proposal already resolve (the three-skill
split below) — there is nothing a second survey copy at the
implementation path would add.

## Request

Issue #77 (professional-discipline gap #3 of 5): research-first,
primary-sourced (Schmidt & Hunter structured-interview validity
evidence; McClelland/Boyatzis competency-definition practice; Skelton
& Pais's Team Topologies; Doran's SMART and Grove/Doerr's OKR
lineage) survey of organization/HR-design methodology, then propose an
`org-design-*` skill family of >=3 skills (hiring-rubric-and-structured-
interview design, role-and-competency definition, team-shape
selection), each with a condition-matched "Use when" trigger, per-rule
`source:` citations, and resolving `Related-skills` links to
`team-safety-measure` and `partnerships-bd-*` where they chain. Phase 1
(survey + proposal) only; authoring the actual
`skills/org-design-*/SKILL.md` files is phase 2, gated on approval.

## Constraints

- Every rule proposed below must trace to a primary source with a live
  URL, verified in `survey.md` (issue acceptance criterion).
- >=3 skills, axis-split, no content overlap between them or with
  `team-safety-measure`.
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

1. **Four skills, splitting OKR/SMART goal-setting into its own
   `org-design-goal-statement` skill, since Doran's SMART paper and
   Grove/Doerr's OKR lineage are named separately in the issue text.**
   Rejected: the survey's Angle 4 finding is that OKR/SMART supplies a
   *cross-cutting convention* (state a goal so it is falsifiable) used
   *inside* role/competency definitions and team charters — it has no
   standalone trigger condition of its own that isn't already "I'm
   writing a role's competencies" or "I'm defining what a team is
   accountable for." A free-standing fourth skill would either sit
   unused (nothing invokes "I need SMART goals" as its own task) or
   duplicate the trigger of whichever skill actually needed it,
   breaking this repo's own no-overlap convention (confirmed across
   `ux-engineering-service-design-*`'s and `partnerships-bd-*`'s
   axis-disjoint families). Folding the OKR/SMART rule into the
   role/competency-definition skill (as the rule for stating a
   competency's performance expectation in falsifiable form) keeps one
   trigger per decision.
2. **One single `org-design-hiring-and-role-design` skill covering both
   the structured-interview rubric and role/competency definition
   together, since both happen during the same hiring cycle.**
   Rejected: the survey's Angle 1 and Angle 2 findings show these are
   separable decisions with separable trigger conditions and separable
   failure modes — a rubric-design task fails by using unstructured,
   unanchored questions (Schmidt & Hunter's r=.51-vs-.38 gap), while a
   role-definition task fails by conflating threshold and
   differentiating competencies (Boyatzis). A team could define a
   role's competencies without ever writing an interview rubric (e.g.,
   for a promotion ladder, not a hiring loop), and could write an
   interview rubric for a role whose competency model already exists
   elsewhere. Collapsing them would force every invocation to load
   both rule sets and break this repo's own axis-triggered dispatch
   convention.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
primary-source findings across all four scouted angles. This proposal
specifies the three skills to author in phase 2.

### Proposed family: `org-design-*` (3 skills)

**1. `org-design-hiring-rubric-structured-interview`**
(axis: `interview-structure-vs-validity-tradeoff`)

- Use when: designing or reviewing a hiring interview rubric, or
  deciding whether an interview process is "structured enough" to
  trust its validity.
- Core rules (source-cited to Schmidt & Hunter 1998):
  - A structured format (fixed question set asked of every candidate +
    behaviorally anchored rating scale + systematic, not holistic,
    scoring) is required before a rubric can claim anything close to
    the r=.51 validity figure; an unstructured "conversation with
    notes" format tops out near r=.38 and must not borrow the higher
    number.
  - A structured interview is a strong complement, not a substitute,
    for a work-sample or general-ability measure where one is
    available (GMA+structured-interview combined validity r=.63) —
    the rubric should say so rather than implying the interview alone
    is sufficient signal.
- `Related-skills`: `team-safety-measure` (if the rubric author
  conflates "does this candidate feel safe disagreeing" with a
  competency question — route the measurement question there, not
  into the rubric).

**2. `org-design-role-competency-definition`**
(axis: `threshold-vs-differentiating-competency`)

- Use when: writing or reviewing a role's competency list, a job
  description's requirements section, or a promotion/leveling
  criterion.
- Core rules (source-cited to McClelland 1973 / Boyatzis 1982):
  - Every listed competency must be tagged threshold (necessary for
    minimally adequate performance) or differentiating (separates
    superior from average performers) — an untagged flat list is the
    most common authoring error the practice literature surfaces.
  - A competency statement should carry a falsifiable performance
    expectation (source-cited to Doran 1981's SMART criteria and
    Grove/Doerr's Objective+Key-Result split) rather than an
    unmeasurable trait adjective.
- `Related-skills`: `org-design-hiring-rubric-structured-interview`
  (a hiring rubric should draw its questions from an existing
  competency definition, not invent criteria ad hoc);
  `partnerships-bd-negotiation-positioning` (where a role's
  competency definition covers an externally-facing BD/partnerships
  seat, the two chain rather than duplicate).

**3. `org-design-team-shape-selection`**
(axis: `team-type-and-interaction-mode-by-cognitive-load`)

- Use when: deciding what kind of team a new or restructuring team
  should be, or what interaction mode two teams should use and for how
  long.
- Core rules (source-cited to Skelton & Pais, *Team Topologies*):
  - Classify against the four team types (stream-aligned, enabling,
    complicated-subsystem, platform) by what the team owns
    end-to-end and whose cognitive load it exists to reduce — not by
    org-chart convenience or pre-existing skill silo.
  - Classify the interaction between two teams as collaboration,
    X-as-a-service, or facilitating, and treat collaboration and
    facilitating modes as time-bounded by design — a facilitating
    relationship that never ends is a signal the receiving team's
    shape is wrong, not that facilitation should continue indefinitely.
- `Related-skills`: `team-safety-measure` (if the actual complaint is
  "this team doesn't feel safe," route to the measurement skill, not a
  reshape); `org-design-role-competency-definition` (once a team's
  type is chosen, the roles inside it should be defined against that
  type's accountabilities).

## Out of scope

- Authoring the actual `skills/org-design-*/SKILL.md` files (phase 2).
- Any intervention/prescription content ("how do we fix a broken
  team") beyond the selection/definition decision itself — consistent
  with `team-safety-measure`'s own measurement-only boundary.
- A fourth free-standing OKR/SMART skill (see Rationale, alternative 1).

## How you'll know it worked

- `docs/issue-77/reports/knowledge-management/survey.md` and this
  proposal exist on disk, phase-1 committed, PR opened against `main`
  referencing `#77` (no Closes/Fixes trailer at this phase).
- On approval (phase 2): three `skills/org-design-*/SKILL.md` files
  exist, each with a distinct "Use when" trigger, per-rule `source:`
  citations matching this survey, and `Related-skills` links that
  resolve to real directories; `scripts/check_skill_conformance.py`
  runs green over the full repo.
