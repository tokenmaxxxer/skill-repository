# Survey: content-strategy skill family (issue-82)

## Scope surveyed

Current repo state relevant to a proposed `content-strategy-*` family
(editorial calendar/cadence, content audit/inventory, content
governance/ownership), and primary-source grounding for the three
candidate skills, per issue-82's named lineage: Halvorson/Rach
*Content Strategy for the Web*, the content-audit method (quantitative
inventory vs. qualitative audit), and content-governance/ownership
models (RACI, centralized/decentralized/hybrid).

## Repo state (empty-state check)

- `grep -ril "editorial\|content audit\|content governance\|cadence\|content strategy" skills/`
  returns 23 hits, all incidental (a `cadence` axis inside
  `risk-management-monitoring-review-cadence`,
  `release-engineering-release-cadence-and-toil`,
  `partnerships-bd-governance-cadence-and-kpi`, etc.) or the existing
  `content-design-operational-playbook` (copy-craft only — error
  messages, CTA labels, tone-of-voice at the sentence/string level; it
  has no rule about calendars, audits, or ownership).
- No `content-strategy-*` or `editorial-calendar-*` family exists.
  Confirms issue-82's stated empty state: content-design covers copy
  craft, not the planning/audit/governance layer above it.
- Nearest sibling families by shape: `devrel-*` (4 skills,
  channel/format/comprehensibility/subtraction axis split, resolving
  `Related-skills` links) and `market-analysis-*` (5 skills, MECE
  axis split). Both confirm this repo's convention: split by decision
  axis, one condition-matched "Use when" trigger per skill, no overlap
  between siblings.

## Angle 1 — Halvorson/Rach core discipline definition (family-boundary axis)

Kristina Halvorson and Melissa Rach, *Content Strategy for the Web*
(2nd ed., 2012) — the founding text of the discipline, also condensed
in Halvorson's 2008 A List Apart piece "The Discipline of Content
Strategy." Three converging working definitions, all load-bearing for
scoping this family against the existing `content-design-*` skill:

- "Content strategy guides the creation, delivery, and governance of
  useful, usable content."
- "Content strategy means getting the right content, to the right
  people, in the right place, at the right time."
- "Content strategy is an integrated set of user-centered, goal-driven
  choices about content throughout its lifecycle."

Halvorson decomposes the discipline into sub-disciplines, one of which
is **editorial strategy**: "defines the guidelines by which all
online content is governed: values, voice, tone, legal and regulatory
concerns, user-generated content... and also defines an organization's
online editorial calendar, including content life cycles." This is the
direct source for an `editorial-calendar-and-cadence` skill's scope
boundary — it is lifecycle/scheduling, explicitly distinct from the
sentence-level voice-and-tone rules `content-design-operational-
playbook` already owns.

Gap this closes: nothing in the repo currently distinguishes "what
content exists and when it runs" (planning layer) from "how a given
string reads" (craft layer, already covered). Halvorson's own
sub-discipline split is the axis boundary to build this family's first
skill against.

Source: [The Discipline of Content Strategy – A List Apart](https://alistapart.com/article/thedisciplineofcontentstrategy/), [Kristina Halvorson — Wikipedia](https://en.wikipedia.org/wiki/Kristina_Halvorson), [Content Strategy for the Web, 2nd ed. — Content Strategy Knowledge Base literature review](https://www.contentstrategy.at/literature-reviews/content-strategy-for-the-web-2nd-edition-by-kristina-halvorson-and-melissa-rach)

## Angle 2 — content-audit method (quantitative inventory vs. qualitative audit)

Halvorson & Rach's own methodological split, restated across multiple
practitioner sources that all cite the same distinction: **a content
inventory is quantitative** (an accounting of every published content
asset — URL, type, owner, last-updated date, no judgment calls) and
**a content audit is qualitative** (assessment of quality, structure,
voice/tone fit, and usefulness — requires human judgment). Halvorson &
Rach's own framing, quoted directly: "The key distinction between
quantitative inventories and qualitative audits is human judgement.
Qualitative content audits are a robot-free zone." Sequencing rule
found across sources: the qualitative audit is normally run *after*
the quantitative inventory exists, not standalone — you cannot judge
quality of an asset set you have not first enumerated.

This is the direct source for a `content-audit-and-inventory` skill's
core rule: classify the task as inventory-shaped (enumerate, no
judgment) vs. audit-shaped (assess against quality/voice/usefulness
criteria) before starting, and never skip straight to a qualitative
pass without the inventory underneath it.

Gap this closes: no skill in the repo currently distinguishes an
enumeration task from a judgment task for content assets — the
distinction determines both process (spreadsheet crawl vs. rubric
scoring) and who should do it (can be delegated/tooled vs. requires a
content strategist's judgment).

Source: [The Content Inventory: Your Core Audit Tool — Peachpit (Halvorson)](https://www.peachpit.com/articles/article.aspx?p=1388961&seqNum=3), [Content audit — Wikipedia](https://en.wikipedia.org/wiki/Content_audit), [Content inventory — Wikipedia](https://en.wikipedia.org/wiki/Content_inventory)

## Angle 3 — content governance/ownership models (RACI, centralized/decentralized/hybrid)

Two converging findings:

1. **Strategy vs. governance boundary** (multiple sources converge):
   "Content strategy defines what to create and why. Content
   governance defines how to manage it. Strategy produces a content
   calendar and editorial plan. Governance produces style guides,
   approval workflows, and audit schedules." This boundary matters for
   this family's own internal axis split — editorial-calendar owns
   the "what/when," content-governance owns the "who decides."
2. **RACI as the operational ownership model** (Content Strategy Inc.,
   a practitioner source specializing in this discipline):
   Responsible (executes), Accountable (final sign-off — "make sure
   there is only one A for each role"), Consulted (subject-matter
   input sought before completion), Informed (notified after, cannot
   block). Concrete failure modes named: multiple A's break sign-off
   clarity; too many C's stall the process; too few C's produce
   quality gaps from missing expertise.
3. **Governance model taxonomy** (converges across sources): three
   named models — centralized (one team controls all content
   decisions), decentralized (each team/unit governs its own), hybrid
   (central standards, team-level execution) — with hybrid reported as
   the best fit for most growing organizations, because it keeps a
   single accountable standard-setter while not bottlenecking
   execution through one team.

This is the direct source for a `content-governance-ownership`
skill's two core rules: (a) apply RACI's single-Accountable-owner rule
when a content domain has no clear final approver, and (b) choose
centralized/decentralized/hybrid by organizational scale and update
frequency, not by default inertia.

Gap this closes: no skill in the repo currently supplies a decision
rule for "who has final say over this piece of content" or "should
this content decision be made centrally or locally" — both are
structurally distinct from the wording-level content-design rules and
from the calendar/cadence rules above.

Source: [How to use a RACI chart to define content roles and responsibilities — Content Strategy Inc.](https://contentstrategyinc.com/how-to-use-a-raci-chart-to-define-content-roles-and-responsibilities/), [Content Governance: Your Essential Matrix Checklist](https://www.crispycontent.de/en/blog/content-governance-checklist-matrix-organisations-accountability), [Content Governance (2026): Strategies, Tactics & Examples](https://thestacc.com/blog/content-governance-guide/)

## Angle 4 — chaining points to content-design, devrel, marketing

- `content-design-operational-playbook`: sentence/string-level craft
  (error messages, CTA labels, tone-of-voice per surface). The new
  family's editorial-calendar skill should route "what should this
  string actually say" questions there rather than duplicating
  wording rules; the new family owns planning/audit/governance, not
  craft.
- `devrel-channel-convention` / `devrel-content-comprehensibility`:
  format/channel decisions for developer-facing content, and
  cross-language sample consistency. A content audit that surfaces a
  devrel asset (sample repo, conference talk) should route
  channel/format questions there, not re-derive them.
- `marketing-channel-selection` / `marketing-scope-pruning`: channel
  choice and program-subtraction for marketing content. An editorial
  calendar spanning marketing content should route channel-selection
  and scope-pruning decisions there rather than re-deciding them
  inside the calendar skill.

## Judgment (saturation check)

Two search rounds (sweep + one snowball/deepening round on the ALA
article and the RACI primary source) converge on the same three-axis
split the issue text already names: calendar/cadence (Halvorson's
editorial-strategy sub-discipline), audit/inventory (Halvorson &
Rach's quantitative/qualitative split), and governance/ownership
(RACI + centralized/decentralized/hybrid). A third round would not
change the family boundary or the chaining points — stopping here.
Mode used: parallel fan-out (3 concurrent `WebSearch` calls in one
turn) for the sweep, batched-sequential (2 `WebFetch` calls in one
turn) for the deepening round.
