# Survey: service-design methodology (blueprinting / touchpoint mapping / frontstage-backstage)

Subject: issue-74. Scout stage used parallel fan-out (4 concurrent
`WebSearch` calls, one per angle: Shostack/Bitner blueprinting lineage,
NN/g service-blueprint guidance, frontstage/backstage/support-process
separation, ISO 9241-210 relevance), then one deepening round (2
further `WebSearch` calls narrowing on NN/g's 5-step process and the
5-layer blueprint definition) — saturation reached: a second round
would not change which skills to propose, only add redundant citations
to blueprint-layer facts already sourced from NN/g and the Shostack/
Bitner lineage.

## This repo's current write surface

- No `service-design-*` family exists (`ls skills | grep ^service-design`
  returns nothing) — matches issue #74's stated empty state.
- Closest existing families: `design-artifact-user-flow` (single-
  product, single-channel step sequence — explicitly excludes cross-
  channel/emotional content), `design-artifact-user-scenario` (likely
  the journey/emotion-narrative counterpart per user-flow's own
  Trigger section pointer), `user-discovery` (generative interview
  research, not service operations mapping), and the `ux-engineering-*`
  family (within-screen/within-flow decision rules: color, control
  choice, layout, navigation depth, surface contrast — none address
  cross-actor, frontstage/backstage, or multi-touchpoint service
  operations). None of these cover: (a) diagramming a service's
  frontstage/backstage/support-process structure across actors and
  time, (b) mapping touchpoints across channels for one journey, or
  (c) deciding what lives frontstage vs. backstage vs. support. This is
  the three-part gap issue #74 names.
- Fixed schema confirmed from `skills/ux-engineering-navigation-depth/
  SKILL.md` and `skills/design-artifact-user-flow/SKILL.md`:
  frontmatter `name`, `description` ("Use when..." trigger), `axis`,
  `rule_count_floor`; body `## Trigger`, `## Procedure`,
  `## Output shape`, `## Decision rules` (or `## Rules`) as a flat
  numbered list, each rule ending in a `source: <url>` citation line
  plus (per the `ux-engineering-navigation-depth` convention actually
  used in this repo) a `counter-example:` line. `scripts/
  check_skill_conformance.py` enforces frontmatter + per-rule
  `source:` mechanically; both flat-numbered-list and `### N.`
  sub-heading conventions pass its regex, and the `ux-engineering-*`
  family already uses the flat-list form — this family will match its
  own siblings and use the flat-list form too.
- `Related-skills` link convention confirmed from `skills/
  design-artifact-user-flow/SKILL.md` (prose pointer to sibling
  `design-artifact-user-scenario`) and `skills/business-model-design-*/
  SKILL.md` (an explicit `## Related skills` heading with bullet
  cross-references, both bare-name and `[name](../name/SKILL.md)`
  relative-link forms present across the repo) — this family uses the
  explicit `## Related skills` heading with relative links, matching
  the majority convention and issue #74's own "resolving Related-skills
  links" acceptance wording.

## Angle 1 — Shostack/Bitner blueprinting lineage (origin + line
structure)

- Service blueprinting originated with G. Lynn Shostack (Harvard
  Business Review, 1984), originally a two-layer model (frontstage/
  backstage); Bitner, Ostrom & Morgan (2008) extended it to the modern
  five-layer form: Physical Evidence, Customer Actions, Onstage
  (frontstage employee actions), Backstage (employee actions), Support
  Processes.
  Source: https://www.nngroup.com/articles/service-blueprinting-faq/ ,
  https://en.wikipedia.org/wiki/Service_blueprint
- Three horizontal dividing lines structure the diagram: the Line of
  Interaction separates Customer Actions from Onstage; the Line of
  Visibility separates Onstage from Backstage (the single most
  important line — it marks where customer perception ends and
  internal reality begins); the Line of Internal Interaction separates
  Backstage (customer-facing-adjacent staff) from Support Processes
  (staff who never interact with customers).
  Source: https://ixdf.org/literature/topics/frontstage-and-backstage ,
  https://www.nngroup.com/articles/service-blueprints-definition/
- Support Processes represent the foundation enabling both frontstage
  and backstage — payment systems, third-party logistics,
  infrastructure — and are staffed by people who do not regularly
  interact with customers, distinguishing them from Backstage staff who
  may still be customer-adjacent.
  Source: https://ixdf.org/literature/topics/frontstage-and-backstage ,
  https://www.nngroup.com/articles/service-blueprints-definition/

## Angle 2 — NN/g service-blueprint construction guidance

- Service blueprints are the right tool specifically for experiences
  that are omnichannel, involve multiple touchpoints, or require
  cross-functional coordination across departments — not for a
  single-channel, single-department interaction (that is user-flow/
  journey-map territory instead).
  Source: https://www.nngroup.com/articles/service-blueprinting-faq/
- 5-step construction process: (1) find support — build a cross-
  disciplinary core team and stakeholder buy-in; (2) define the goal —
  scope and align on what the blueprint initiative is for; (3) gather
  customer research — establish a baseline of customer actions/steps/
  choices; (4) gather internal research — a minimum of two research
  methods placing the team in direct observation of employees (not
  customer research alone); (5) layer in evidence at each customer
  action step and assemble the visual blueprint.
  Source: https://www.nngroup.com/articles/5-steps-service-blueprinting/
- Customer Actions layer is a "slimmed down" representation — the
  steps/choices/activities a customer performs to reach one goal — not
  a full moment-by-moment transcript; over-detailing this layer is a
  named failure mode.
  Source: https://www.nngroup.com/articles/service-blueprints-definition/
- Choosing what experience/scope to visualize (which journey, which
  segment, how much of the service) is itself a distinct decision NN/g
  treats as a named step before blueprinting starts, not an
  afterthought — scoping too broadly or too narrowly both degrade the
  blueprint's usefulness.
  Source: https://www.nngroup.com/articles/service-blueprints-choose-what-experience/

## Angle 3 — frontstage/backstage/support-process separation (what goes
where)

- Frontstage = everything the customer directly perceives during a
  touchpoint (onstage employee actions plus physical/digital evidence);
  Backstage = internal actions supporting an onstage moment, which may
  be done by a dedicated backstage employee or by the SAME frontstage
  employee acting invisibly (e.g. a teller updating a database after
  a visible transaction) — backstage is defined by visibility to the
  customer, not by which employee/department performs it.
  Source: https://www.nngroup.com/articles/service-blueprints-definition/ ,
  https://ixdf.org/literature/topics/frontstage-and-backstage
- A common construction failure is placing an activity backstage
  purely because it is "internal work," when the real test is whether
  the customer would perceive it if it failed or were delayed — that
  perceptibility test, not organizational location, is what the Line
  of Visibility encodes.
  Source: https://www.nngroup.com/articles/service-blueprints-definition/ ,
  https://ixdf.org/literature/topics/frontstage-and-backstage
- Support Processes must be distinguished from Backstage by staff role
  (never customer-facing) and by function (infrastructural enabling
  systems — payment rails, logistics, IT platforms — rather than
  in-the-moment task execution); collapsing Support Processes into
  Backstage loses the distinction between "this team could fail
  silently for a long time before anyone downstream notices" (support)
  and "this action directly and immediately enables the current
  customer moment" (backstage).
  Source: https://ixdf.org/literature/topics/frontstage-and-backstage

## Angle 4 — ISO 9241-210 (bearing on service design)

- ISO 9241-210 defines human-centred design (HCD) principles for
  interactive systems generally (not service-design-specific): design
  based on explicit understanding of users/tasks/environment, user
  involvement throughout, iterative refinement driven by user-centred
  evaluation, and a multidisciplinary design team.
  Source: https://www.iso.org/standard/77520.html ,
  https://digital.nhs.uk/blog/design-matters/2022/how-a-20-year-old-standard-is-still-relevant-today
- Search found no ISO 9241-210 clause specific to touchpoints,
  channels, or service blueprinting by name — the standard's HCD
  process principles (iterative, evidence-based, multidisciplinary)
  are the load-bearing bridge to service design, not a blueprinting- or
  touchpoint-specific clause. This survey therefore does not force an
  ISO 9241-210 `source:` citation onto a rule that isn't actually
  ISO-sourced; where a proposed rule below draws on the HCD-process
  framing, it is cited to ISO 9241-210's general principles honestly,
  not over-claimed as blueprint-specific guidance.

## Gap line

Field must-bes this repo already meets structurally: axis-scoped
condition-matched triggers, fixed Trigger/Procedure/Output-shape/Rules
schema, per-rule `source:` citation discipline, `## Related skills`
cross-referencing (matches or exceeds every source surveyed — none of
Shostack/Bitner/NN/g/ISO ship a machine-checkable per-rule citation
format; that is this repo's own convention, applied here).

Field must-bes this repo is missing (the gap issue #74 names): no
skill covers constructing a service blueprint's five-layer structure
and three dividing lines (the Angle 1/2 gap); no skill covers mapping
touchpoints/channels across a multi-touchpoint or omnichannel journey,
distinct from `design-artifact-user-flow`'s deliberately single-
channel/single-product scope (the Angle 2 gap, NN/g's own omnichannel-
trigger framing); no skill covers deciding what belongs frontstage vs.
backstage vs. support process by the visibility/perceptibility test
rather than org-chart location (the Angle 3 gap). All three gaps trace
to primary sources found above (Shostack's original HBR framing via
NN/g and Wikipedia citing it, Bitner/Ostrom/Morgan 2008 via NN/g and
IxDF, NN/g's own construction-process articles) at this repo's citation
bar — proposal below routes each gap to one proposed skill, chaining to
`design-artifact-user-flow`, `user-discovery`, and the `ux-engineering-*`
family per issue #74's stated chaining requirement.
