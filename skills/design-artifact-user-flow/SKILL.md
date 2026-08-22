---
name: design-artifact-user-flow
description: Use when diagramming the discrete step-by-step interaction path a user takes through one product task — screens/states and system responses, not emotions or cross-channel context.
axis: flow-micro-scope-vs-journey-macro-scope
rule_count_floor: 3
---

# Flow micro-scope vs. journey macro-scope

Decision rules for scoping and diagramming a user flow — the discrete,
single-product sequence of screens/states, actions, and system
responses a user moves through to complete one task — sourced from
NN/g's "User Journeys vs. User Flows"
(https://www.nngroup.com/articles/user-journeys-vs-user-flows/).

## Trigger

Apply this skill when diagramming the step-by-step interaction path a
user takes through one product task inside a single product — screens
or states connected by actions and system responses. Do not use it
for cross-channel, multi-touchpoint, or emotional/motivational
narrative about a user's experience over time; that is journey/
scenario territory — see the sibling skill design-artifact-user-scenario.

## Procedure

1. Identify the single task and single product/system the flow covers;
   exclude any other channel or touchpoint outside that product
   (rule 1).
2. For each step, diagram the screen or state, the user's action, and
   the system's response as the next screen/state — a flowchart or
   "wireflow" connecting wireframes with flow arrows (rule 2).
3. At every point where behavior diverges (error, validation failure,
   conditional branch), draw an explicit fork in the diagram rather
   than continuing a single happy-path line (rule 3).
4. REMOVAL: strip any emotional, motivational, or narrative annotation
   ("user feels frustrated here") from the flow diagram; if that
   content is needed, capture it in a user journey/scenario artifact
   instead (rule 4).

## Output shape

A flowchart or wireflow: screens or states connected by user actions
and system responses, scoped to one task within one product, with
decision branches (errors, conditional paths) shown as explicit forks
— and no emotional, motivational, or cross-channel narrative
annotation.

## Decision rules

1. When scoping a flow artifact, restrict it to the discrete steps a
   user takes within a single product to complete one task — screen,
   action, next screen/state — and exclude cross-channel context (e.g.
   a phone call, an in-store visit, an email received outside the
   product), because a flow is a micro-scope implementation artifact,
   not a record of the user's broader experience.
   source: NN/g, "User Journeys vs. User Flows"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/):
   describes user flows as depicting "the discrete steps a user takes
   to complete a task within a specific product or system," in
   contrast to journeys, which span "the entire experience... across
   multiple touchpoints and channels."
   counter-example: do not fold a customer-support phone call that
   happens mid-task into the flow diagram just because it's part of
   how some users actually complete the task — that cross-channel
   detour belongs in a journey map; the flow stays scoped to the
   product's own screens and states.

2. When two or more diverging outcomes are possible at a step (an
   error response, a validation failure, a conditional path based on
   account state), draw them as explicit separate branches/forks in
   the flow diagram, not as a single line that only shows the
   happy path, because a flow that omits real branches cannot serve
   as an implementation spec for what to build.
   source: NN/g, "User Journeys vs. User Flows"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/):
   notes that user flows are typically shown "as a flowchart," a
   diagram form whose purpose is to represent decision points and
   branching paths, and that flows are used to plan and evaluate the
   discrete steps and system responses of a task-specific interaction.
   counter-example: do not create a separate branch for a purely
   cosmetic variation (e.g. a screen that only differs in dark mode)
   — reserve forks for branches where the user's next required action
   or the system's next state actually differs.

3. REMOVAL: when a flow diagram has accumulated emotional or narrative
   annotations (e.g. "user feels anxious," "user is delighted"), strip
   that content out of the flow and, if it is needed, move it into a
   user-journey or scenario artifact instead, because a flow that is
   padded with journey-style emotional narrative stops functioning as
   a usable implementation spec for engineering.
   source: NN/g, "User Journeys vs. User Flows"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/):
   states that, unlike journeys, "user flows do not typically include
   information about the user's thoughts and feelings," and positions
   flows as a narrower, implementation-focused artifact distinct from
   the emotion/motivation content that belongs in a journey map.
   rationale: an engineer implementing a screen-to-screen transition
   needs to know the next state and system response, not how the user
   felt about it; mixing the two makes the flow slower to read as a
   spec and duplicates content the journey artifact already owns.

4. When a task's flow is being drafted and a stakeholder wants
   emotional or motivational context included "for completeness," cite
   design-artifact-user-scenario as the sibling artifact for that
   content rather than expanding the flow's scope to cover it, because
   keeping the two artifacts separate preserves the flow's usefulness
   as a precise, implementation-ready diagram.
   source: NN/g, "User Journeys vs. User Flows"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/):
   frames journeys and flows as complementary artifacts at different
   scopes — journey as macro/emotional, flow as micro/discrete-steps —
   rather than one artifact that does both jobs.
   counter-example: do not refuse to produce any journey-relevant
   content at all when a stakeholder asks — redirect it to the correct
   artifact rather than dropping the request; the point is separation
   of artifacts, not suppression of the information.
