---
name: ux-engineering-service-design-blueprint-construction
description: Use when building a service blueprint for an omnichannel or cross-functional service — laying out Physical Evidence, Customer Actions, Onstage, Backstage, and Support Processes layers, placing the Line of Interaction/Visibility/Internal Interaction, or scoping which journey/segment a blueprint should cover before starting.
axis: blueprint-construction-scope-and-layering
rule_count_floor: 5
---

# Service blueprint construction

Decision rules for scoping, structuring, and constructing a service
blueprint — sourced from G. Lynn Shostack's original blueprinting
concept (Harvard Business Review, 1984) as extended to the modern
five-layer form by Bitner, Ostrom & Morgan (2008), and NN/g's
service-blueprinting construction guidance, per issue #74's phase-1
survey (`docs/issue-74/reports/ux-engineering/survey.md`, 2026-08-22).

## Trigger

Apply this skill when building a service blueprint for an omnichannel,
multi-touchpoint, or cross-functional service — laying out its five
layers, placing its three dividing lines, or scoping which
journey/segment/experience the blueprint should cover before
construction starts. Do not use it for a single-channel,
single-department interaction (route to `design-artifact-user-flow`
instead) or for mapping touchpoints alone without constructing a full
blueprint (route to
`ux-engineering-service-design-touchpoint-channel-mapping` instead).

## Procedure

1. Before laying out any layer, confirm the interaction is
   omnichannel, multi-touchpoint, or cross-functional (rule 1); if not,
   stop and route to `design-artifact-user-flow`.
2. Scope the experience/segment/journey the blueprint covers as an
   explicit named step (rule 2).
3. Run the 5-step construction process — find support, define the
   goal, gather customer research, gather internal research via at
   least two observation methods, layer in evidence (rule 3).
4. Lay out the five layers in order — Physical Evidence, Customer
   Actions, Onstage, Backstage, Support Processes — separated by the
   Line of Interaction, Line of Visibility, and Line of Internal
   Interaction (rule 4).
5. Keep the Customer Actions layer a slimmed-down representation, not a
   full moment-by-moment transcript (rule 5).

## Output shape

A scoped service blueprint with its five layers and three dividing
lines placed, the construction-process step that produced each layer
noted, and — when the omnichannel/cross-functional trigger test fails —
a routing note to `design-artifact-user-flow` instead of a blueprint.

## Decision rules

1. Before starting construction, confirm the experience is
   omnichannel, involves multiple touchpoints, or requires
   cross-functional coordination across departments — a service
   blueprint is the right tool specifically for these cases, not for a
   single-channel, single-department interaction.
   source: https://www.nngroup.com/articles/service-blueprinting-faq/
   counter-example: do not build a full blueprint for a single-channel
   checkout-error-message flow inside one product — that is
   `design-artifact-user-flow` territory; reserve blueprinting for
   cases that actually cross channels or departments.

2. Choose and record which experience, segment, or journey the
   blueprint covers as its own explicit step before enumerating any
   layer content — scoping too broadly or too narrowly both degrade
   the blueprint's usefulness, so this decision is made deliberately,
   not left as a byproduct of wherever documentation happened to start.
   source: https://www.nngroup.com/articles/service-blueprints-choose-what-experience/
   counter-example: do not treat "we'll blueprint the whole customer
   lifecycle" as sufficiently scoped — that scope is too broad to
   layer evidence into usefully; narrow to one journey or segment
   first.

3. Run construction as a 5-step process in order: (1) find support —
   build a cross-disciplinary core team and stakeholder buy-in; (2)
   define the goal the blueprint initiative serves; (3) gather customer
   research establishing a baseline of customer actions/steps/choices;
   (4) gather internal research using at least two research methods
   that place the team in direct observation of employees, not customer
   research alone; (5) layer evidence at each customer-action step and
   assemble the visual blueprint.
   source: https://www.nngroup.com/articles/5-steps-service-blueprinting/
   counter-example: do not skip step 4's direct-observation requirement
   and substitute a second round of customer interviews instead —
   customer research alone cannot supply the Onstage/Backstage/Support
   layer content, which requires observing employees.

4. Lay out the five layers — Physical Evidence, Customer Actions,
   Onstage (frontstage employee actions), Backstage (employee actions),
   Support Processes — separated by three horizontal dividing lines in
   this order: the Line of Interaction (between Customer Actions and
   Onstage), the Line of Visibility (between Onstage and Backstage —
   the line marking where customer perception ends), and the Line of
   Internal Interaction (between Backstage and Support Processes).
   source: https://www.nngroup.com/articles/service-blueprinting-faq/ ,
   https://en.wikipedia.org/wiki/Service_blueprint ,
   https://ixdf.org/literature/topics/frontstage-and-backstage
   counter-example: do not collapse Backstage and Support Processes
   into one layer for convenience — the Line of Internal Interaction
   marks a real distinction (customer-adjacent staff vs. staff who
   never interact with customers) that a merged layer would erase; see
   `ux-engineering-service-design-frontstage-backstage-separation` for
   the placement test itself.

5. Keep the Customer Actions layer a "slimmed down" representation —
   the steps, choices, and activities a customer performs to reach one
   goal — rather than a full moment-by-moment transcript of everything
   the customer did or felt.
   source: https://www.nngroup.com/articles/service-blueprints-definition/
   counter-example: do not refuse to record a customer action's
   emotional weight anywhere — route that content to
   `design-artifact-user-scenario` instead of inflating the Customer
   Actions layer with it; the layer's job is the action sequence, not
   the narrative.

## Related skills

- [design-artifact-user-flow](../design-artifact-user-flow/SKILL.md) — routes here when an interaction is single-product/single-channel and does not meet this skill's omnichannel/cross-functional trigger test.
- [user-discovery](../user-discovery/SKILL.md) — supplies the generative-interview and observation methodology this skill's customer-research and internal-research construction steps hand off to.
- [ux-engineering-service-design-touchpoint-channel-mapping](../ux-engineering-service-design-touchpoint-channel-mapping/SKILL.md) — the narrower, standalone touchpoint-mapping activity that escalates into this skill's full blueprint when its own omnichannel/cross-functional trigger fires.
- [ux-engineering-service-design-frontstage-backstage-separation](../ux-engineering-service-design-frontstage-backstage-separation/SKILL.md) — classifies individual actions once this skill's layers already exist.
