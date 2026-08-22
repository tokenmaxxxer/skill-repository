---
status: proposed
files:
  - docs/issue-74/reports/ux-engineering/survey.md
  - docs/issue-74/proposals/service-design-skill-family.md
---

# Service-design skill family (phase 1: research + proposal)

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): the current-state survey required by
the survey-before-proposal norm already exists on disk at
`docs/issue-74/reports/ux-engineering/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic `docs/issue-74/reports/
implementation/survey.md` path, since this role writes only its own
record area under `docs/issue-74/reports/ux-engineering/` and never
another role's `reports/implementation/` tree. No design decision
remains open beyond what that survey and this proposal already resolve
(the three-skill split below) — there is nothing a second survey copy
at the implementation path would add.

## Request

Issue #74 (professional-discipline gap #2 of 5): research-first,
primary-sourced (Shostack/Bitner blueprinting lineage, NN/g service-
blueprint and touchpoint-mapping guidance, frontstage/backstage/
support-process separation, ISO 9241-210 where it actually bears)
survey of service-design methodology, then propose a
`ux-engineering-service-design-*` skill family of >=3 skills (service-
blueprint construction, touchpoint/channel mapping, frontstage-
backstage-and-support-process separation), each with a condition-
matched "Use when" trigger, per-rule `source:` citations, and
resolving `Related-skills` links to `design-artifact-user-flow`,
`user-discovery`, and the existing `ux-engineering-*` family. Phase 1
(survey + proposal) only; authoring the actual
`skills/ux-engineering-service-design-*/SKILL.md` files is phase 2,
gated on approval.

## Constraints

- Every rule proposed below must trace to a primary source with a live
  URL, verified in `survey.md` (issue acceptance criterion).
- >=3 skills, axis-split, no content overlap between them or with
  `design-artifact-user-flow`/`design-artifact-user-scenario`/
  `user-discovery`/`ux-engineering-*` (MECE across and against the
  existing families).
- Each skill's `description` must carry a distinct "Use when..."
  trigger.
- `Related-skills` cross-references must resolve to real, existing
  skill directory names.
- `scripts/check_skill_conformance.py` must stay green once phase 2
  authors the actual SKILL.md files.

## Rationale

Two structural alternatives were considered for *how* to split the
family, given what the survey found:

1. **One single `ux-engineering-service-blueprint` skill covering
   construction, touchpoint mapping, and frontstage/backstage
   placement together, since all three are steps of building one
   artifact.** Rejected: the survey's Angle 2 and Angle 3 findings show
   these are separable decisions with separable trigger conditions —
   touchpoint/channel mapping is itself a standalone NN/g-named
   activity that fires whenever a journey is omnichannel, independent
   of whether a full five-layer blueprint is ever built (a team might
   map touchpoints for a journey audit without constructing a
   blueprint at all); and frontstage/backstage/support-process
   placement is a recurring classification judgment applied repeatedly
   *within* an already-scoped blueprint, not a one-time construction
   step. Collapsing them into one skill would force every invocation
   to load all three rule sets and break this repo's own
   axis-triggered dispatch convention (confirmed across
   `ux-engineering-*`'s 5 existing skills and `business-model-design-*`'s
   4).
2. **Fold frontstage/backstage/support-process separation into the
   existing `ux-engineering-surface-contrast` or `ux-engineering-
   navigation-depth` skills as an added rule, instead of a new skill,
   since both already live in the `ux-engineering-*` family.**
   Rejected: `surface-contrast` governs visual elevation/scrim
   treatment for a single active editing surface, and `navigation-depth`
   governs where an action sits in a navigation hierarchy — both are
   within-screen or within-app decisions for a single product surface.
   Frontstage/backstage/support-process separation is a cross-actor,
   cross-department classification (which employee, system, or process
   is customer-visible) that has no natural home in either sibling's
   axis and would silently widen their existing triggers past what
   their own `description` fields promise, breaking their own MECE
   boundary rather than this new family's.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
primary-source findings across all four scouted angles, with the
honest note that ISO 9241-210 supplies general HCD-process framing
here, not a blueprint- or touchpoint-specific clause. This proposal
specifies the three skills to author in phase 2.

### Proposed family: `ux-engineering-service-design-*` (3 skills)

1. **`ux-engineering-service-design-blueprint-construction`**
   - Axis: service-blueprint construction (five-layer structure, three
     dividing lines, scoping and construction-process sequencing).
   - Use when: building a service blueprint for an omnichannel or
     cross-functional service — laying out Physical Evidence, Customer
     Actions, Onstage, Backstage, and Support Processes layers,
     placing the Line of Interaction/Visibility/Internal Interaction,
     or scoping which journey/segment a blueprint should cover before
     starting.
   - Rule seeds (from survey Angles 1-2): five-layer structure
     (Shostack's original two-layer form extended by Bitner/Ostrom/
     Morgan 2008 to five); three dividing lines and their placement
     order (Interaction -> Visibility -> Internal Interaction);
     blueprinting-vs-flow/journey-mapping selection rule (omnichannel/
     multi-touchpoint/cross-functional triggers blueprinting; a
     single-channel, single-department interaction does not — routes
     to `design-artifact-user-flow` instead); the 5-step construction
     process (find support, define goal, gather customer research,
     gather internal research via >=2 observation methods, layer
     evidence); Customer Actions as a slimmed-down representation, not
     a full transcript (a named over-detailing failure mode); explicit
     experience/scope selection as its own step, not an afterthought.
   - Related-skills: `design-artifact-user-flow` (single-product,
     single-channel step sequences route there instead of triggering a
     full blueprint), `user-discovery` (the customer-research and
     internal-research gathering steps of blueprint construction are
     generative interviews/observation this skill hands off to).

2. **`ux-engineering-service-design-touchpoint-channel-mapping`**
   - Axis: touchpoint/channel mapping across a journey (distinct from
     full blueprint construction — mapping touchpoints and channels
     for a journey stands alone even when no blueprint is built).
   - Use when: identifying and sequencing the touchpoints (people,
     props, processes tied to a customer interaction moment) a
     customer encounters across channels for one journey, or judging
     whether a journey's channel set is omnichannel/cross-functional
     enough to warrant escalating to a full blueprint.
   - Rule seeds (from survey Angle 2): touchpoint definition (people +
     props/physical-or-digital-evidence + processes tied to one
     interaction moment); omnichannel/multi-touchpoint/cross-
     functional trigger test for when touchpoint mapping should
     escalate into full blueprinting vs. stand alone as its own
     artifact; scoping-before-mapping rule (choose which experience/
     segment/journey to map before enumerating touchpoints, per NN/g's
     named "choose what experience to visualize" step).
   - Related-skills:
     `ux-engineering-service-design-blueprint-construction` (touchpoint
     mapping is the narrower, standalone activity; that skill is the
     fuller artifact this one escalates into when the omnichannel/
     cross-functional trigger fires), `design-artifact-user-scenario`
     (cross-channel emotional/narrative journey content that
     `design-artifact-user-flow` explicitly excludes lives there,
     alongside touchpoint sequencing for the same journey).

3. **`ux-engineering-service-design-frontstage-backstage-separation`**
   - Axis: frontstage/backstage/support-process classification (what
     belongs where, by visibility/perceptibility test, not
     organizational location).
   - Use when: deciding whether a service action, system, or actor
     belongs frontstage (customer-visible), backstage (invisible
     support for an onstage moment, possibly performed by the same
     frontstage employee), or a support process (infrastructural,
     never customer-facing) inside an already-scoped blueprint or
     touchpoint map.
   - Rule seeds (from survey Angle 3): the perceptibility test itself
     (would the customer notice if this action failed or were
     delayed?) as the deciding criterion, not who performs it or which
     department owns it; backstage-by-the-same-employee case (a
     frontstage employee acting invisibly is still backstage, not
     frontstage, for that action); support-process vs. backstage
     distinction by staff role (never customer-facing) and function
     (infrastructural/enabling systems vs. in-the-moment task
     execution); named failure mode of placing work backstage purely
     because it is "internal," bypassing the perceptibility test.
   - Related-skills: `ux-engineering-service-design-blueprint-
     construction` (this skill classifies individual actions once a
     blueprint's layers already exist), `ux-engineering-surface-
     contrast` (that skill's elevation/chrome-treatment axis is a
     visually-analogous but distinct within-screen decision; this
     skill's frontstage/backstage line is a cross-actor visibility
     classification, not a visual-elevation one — cited to mark the
     boundary explicitly, not to merge them, per this proposal's own
     Rationale alternative 2).

### Cross-reference resolution

- `design-artifact-user-flow`, `design-artifact-user-scenario`,
  `user-discovery` — all confirmed present under `skills/` (`ls skills
  | grep -E "^design-artifact-user-(flow|scenario)$|^user-discovery$"`,
  see `survey.md`).
- `ux-engineering-surface-contrast` — confirmed present under
  `skills/` (mounted in this session's own skill list).

## Out of scope

- Authoring the actual
  `skills/ux-engineering-service-design-*/SKILL.md` files, their full
  numbered rule sections, and running
  `scripts/check_skill_conformance.py` — phase-2 work, gated on
  approval per contract v3 s19.
- Any change to `design-artifact-*`, `user-discovery`, or existing
  `ux-engineering-*` skills themselves beyond the new
  `Related-skills` links added *into* the new family's files in
  phase 2 (their own files are not touched).
- Deeper ISO 9241-210 clause-by-clause mapping — the survey found the
  standard bears on service design only through its general
  human-centred-design process principles, not a blueprint- or
  touchpoint-specific clause; phase 2 will cite it honestly at that
  level of generality where used, not manufacture a more specific
  citation than the standard supports.

## How you'll know it worked

- `docs/issue-74/reports/ux-engineering/survey.md` exists, covers all
  four scouted angles, and every external claim cites a live source
  URL.
- This proposal names exactly 3 skills with a distinct axis and "Use
  when" trigger each, MECE against each other and against
  `design-artifact-*`/`user-discovery`/existing `ux-engineering-*`.
- Each skill's rule seeds trace to a primary source captured in
  `survey.md`.
- `Related-skills` cross-references above name only skill directories
  confirmed to exist.
- PR against `main` from `issue-74/ux-engineering` references `#74`
  (no `Closes`/`Fixes`/`Resolves` trailer — phase-1 proposal PR).
