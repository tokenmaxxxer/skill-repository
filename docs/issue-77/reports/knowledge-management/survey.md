# Survey: organization/HR-design skill family (issue-77)

## Scope surveyed

Current repo state relevant to the proposed `org-design-*` family, and
primary-source grounding for its three candidate skills (hiring rubric
+ structured interview, role/competency definition, team-shape
selection), per issue-77's named lineages: Schmidt & Hunter
structured-interview validity evidence, competency-definition practice,
Team Topologies, and OKR/SMART primary sources.

## Repo state (empty-state check)

- `grep -ril "interview\|competency\|team.topolog\|OKR\|SMART goal" skills/`
  returns no `org-design-*` or `hr-design-*` family. The only adjacent
  skill is `skills/team-safety-measure` (Edmondson psychological-safety
  *measurement*, explicitly not a hiring/role/team-shape skill — it
  routes intervention asks to `hypothesis-testing`).
- `skills/partnerships-bd-*` (5 skills) exists as the nearest sibling
  family in structure (axis-split, `Related-skills` cross-refs) but is
  deal-negotiation-scoped, not hiring/org-design-scoped — confirms the
  issue's stated empty state is accurate.
- Confirms issue #77's acceptance-criteria premise: no skill currently
  covers hiring rubrics, role/competency definition, or team-shape
  selection.

## Angle 1 — Schmidt & Hunter structured-interview validity (hiring rubric axis)

Schmidt & Hunter (1998), *Psychological Bulletin*, "The Validity and
Utility of Selection Methods in Personnel Psychology," meta-analyzed
85 years of selection-method research (n across studies in the
hundreds of thousands). Key numbers this skill must cite correctly:

- Structured interviews: mean operational validity **r = .51**.
- Unstructured interviews: mean operational validity **r = .38**.
- Highest incremental-validity *combinations*: GMA + work-sample test
  (r = .63), GMA + integrity test (r = .65), GMA + structured interview
  (r = .63) — i.e., a structured interview is a strong *complement* to,
  not a full substitute for, a work-sample/ability measure.
- "Structured" in this literature means: standardized questions asked
  of every candidate, behaviorally anchored rating scales, and
  systematic (not holistic/gut-feel) scoring — this is the load-bearing
  definition a hiring-rubric skill must operationalize, not just cite
  the headline r-value.

Source: [Schmidt & Hunter (1998) summary/citation trail](https://firstpersonnel.org/wp-content/uploads/2013/10/Summary-Schmidt-Hunter-1998.pdf), [Plum.io explainer with citation](https://www.plum.io/blog/schmidt-hunter-meta-analysis)

Gap this closes: no skill currently tells a rubric author *why*
structured beats unstructured (the r=.51 vs r=.38 gap) or what
"structured" operationally requires (anchors + fixed question set +
systematic scoring, not "ask everyone similar things").

## Angle 2 — competency definition practice (role/competency axis)

Two converging primary-source definitions, both traceable to named
authors and dates, not a vendor gloss:

- McClelland (1973), "Testing for Competence Rather Than for
  Intelligence," *American Psychologist* — founding argument that
  intelligence-test scores are poor predictors of job success and
  proposed competency-based assessment instead.
- Boyatzis (1982), *The Competent Manager* — defines a job competency
  as "an underlying characteristic of a person... causally related to
  effective and/or superior performance," and introduces the
  **threshold vs. differentiating** competency distinction: threshold
  competencies are necessary for minimally adequate performance;
  differentiating competencies separate superior from average
  performers. This threshold/differentiating split is the operational
  axis a role-definition skill needs — it is the difference between
  "must-have to do the job at all" and "what makes someone excellent
  at it," and conflating them is the most common competency-model
  authoring error found across the practice literature surveyed.

Source: [Literature survey citing McClelland 1973 and Boyatzis's threshold/differentiating distinction](http://www.iosrjournals.org/iosr-jbm/papers/Vol16-issue1/Version-1/C016111422.pdf)

Gap this closes: no skill currently distinguishes threshold from
differentiating competencies when defining a role, which is the axis
that prevents competency lists from becoming an undifferentiated
wish-list.

## Angle 3 — Team Topologies (team-shape-selection axis)

Skelton & Pais, *Team Topologies* (IT Revolution, 2019) — the primary
source for:

- **Four fundamental team types**: stream-aligned (owns end-to-end
  delivery for one business domain/product/customer need, minimal
  external dependencies), enabling (builds missing capability in other
  teams, aims at their autonomy), complicated-subsystem (isolates
  genuinely hard specialist work so it doesn't tax stream-aligned
  teams' cognitive load), platform (provides internal services so
  stream-aligned teams self-serve with reduced cognitive load).
- **Three interaction modes**: collaboration (close joint work on an
  evolving problem — intentionally short-lived, high-bandwidth),
  X-as-a-Service (one team consumes another's output with minimal
  communication overhead), facilitating (one team helps another
  overcome a gap, aiming at facilitation ending, not becoming
  permanent).
- The book's central selection principle: team shape and interaction
  mode should be chosen to minimize a team's **cognitive load**, not by
  org-chart convenience or skill-silo habit — this is the axis a
  team-shape-selection skill should trigger on (a team drowning in
  extraneous cognitive load is the signal to reshape or re-interact,
  not a generic "should we reorg" prompt).

Source: [Team Topologies key concepts (official site)](https://teamtopologies.com/key-concepts), [CALADE glossary summary](https://calade.de/en/glossary/what-are-team-topologies)

Gap this closes: no skill currently helps decide which of the four
team types a new or struggling team should be, or which interaction
mode two teams should use and when that mode should end.

## Angle 4 — OKR/SMART primary sources (goal-setting, cross-cutting into role/team skills)

- Doran, G.T. (1981), "There's a S.M.A.R.T. Way to Write Management's
  Goals and Objectives," *Management Review* — the primary source for
  the SMART acronym (Specific, Measurable, Assignable, Realistic,
  Time-related in Doran's original; later popularizations relabel two
  letters, which a skill must flag rather than silently adopt one
  variant as canonical).
- Drucker's Management by Objectives (1954) → Andy Grove's OKR at Intel
  (1970s, originally "iMbO") → Doerr, *Measure What Matters* (2018)
  popularizing OKRs at Google. Grove's throughline contribution:
  splitting a goal into an Objective (qualitative direction) and Key
  Results (quantitative, falsifiable measures of whether the objective
  was met) — this split is what a competency/role or team-shape skill
  should borrow when it needs a goal-setting rule, rather than
  reinventing one.

Source: [OKR origin story — Andy Grove/Intel](https://www.whatmatters.com/articles/the-origin-story), [History of SMART goals and OKRs](https://www.collective-genius.com/blog/the-history-of-smart-goals-and-okrs)

Gap this closes: role/competency definitions and team charters in this
repo currently have no primary-sourced convention for stating a goal
in falsifiable form; OKR/SMART is the cited lineage issue-77 names for
that convention.

## Judgment (saturation check)

The four angles are non-overlapping and each maps to one proposed
skill's axis (Angle 1 → hiring-rubric skill; Angle 2 → role/competency
skill; Angle 3 → team-shape skill; Angle 4 → a cross-cutting
goal-statement rule usable by the role/competency skill and optionally
the team-shape skill, not a fourth free-standing skill — see proposal
Rationale for why OKR/SMART is folded in rather than split out).
Another round would not change any build decision; stopping here
(1 sweep stage, no deepening stage needed — sources already reached
primary-author/primary-paper level on the first pass).

Mode used: parallel WebSearch calls in one message (true concurrent
fan-out, not batched-sequential).

## Sources consulted

- https://firstpersonnel.org/wp-content/uploads/2013/10/Summary-Schmidt-Hunter-1998.pdf
- https://www.plum.io/blog/schmidt-hunter-meta-analysis
- http://www.iosrjournals.org/iosr-jbm/papers/Vol16-issue1/Version-1/C016111422.pdf
- https://teamtopologies.com/key-concepts
- https://calade.de/en/glossary/what-are-team-topologies
- https://www.whatmatters.com/articles/the-origin-story
- https://www.collective-genius.com/blog/the-history-of-smart-goals-and-okrs
