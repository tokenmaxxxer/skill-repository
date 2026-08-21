---
name: ux-engineering-navigation-depth
description: Use when deciding where an action or item sits in a navigation hierarchy, top level vs. nested, and in what order. Applies to the nav-order-vs-usage-frequency axis.
axis: nav-order-vs-usage-frequency
rule_count_floor: 3
---

# Navigation order vs. usage frequency

Decision rules for placing frequent actions shallow and rare actions
deep, and ordering navigation by task sequence rather than alphabet or
org chart, sourced from Hick's Law / Fitts's Law and NN/g navigation
research actually fetched during issue #1174's ux-engineering research
pass (2026-08-13).

## Trigger

Apply this skill when deciding where an action or item sits in a
navigation hierarchy — top level vs. nested, and in what order —
distinguishing it from control-selection and layout-grouping, which
govern within-screen controls rather than cross-screen navigation
structure.

## Procedure

1. For an action used by most users in most sessions, place it at the
   top level, reachable in one tap/click (rule 1).
2. For a rarely used action, nest it inside a secondary/overflow menu
   rather than giving it top-level billing (rule 2).
3. When ordering a navigation list, order by task-flow sequence, not
   alphabetically or by org chart (rule 3).
4. When a component set exceeds roughly 7±2 top-level choices,
   consolidate related items under one parent (rule 4).
5. REMOVAL: when a navigation tree has a parent menu holding only one
   child item, delete that parent level and promote the child (rule
   5).
6. Judge navigation depth by a measured directness score — completion
   without backtracking — rather than a subjective read of tree depth
   alone (rule 6).

## Output shape

A navigation placement per action or item (top-level vs. nested, and
its position in list order), plus, where rule 5 fires, a flagged
single-child parent to flatten, and where rule 6 applies, a
directness-based verdict rather than a bare depth count.

## Decision rules

1. When an action is used by most users in most sessions (e.g. "save,"
   "send"), place it at the top level of navigation, reachable in one
   tap/click, not nested inside a secondary menu — every additional
   level a frequent action is nested behind multiplies the decision
   cost paid on every use.
   source: Hick's Law, Laws of UX (fetched 2026-08-13,
   https://lawsofux.com/hicks-law/): "the time it takes to make a
   decision increases with the number and complexity of choices" and
   the article's guidance to "minimize available choices when quick
   responses matter" and "emphasize preferred alternatives."
   counter-example: do not promote a frequent-but-destructive action
   (e.g. "delete all") to one-tap top-level placement just because
   usage frequency is high — some frequent actions still need
   deliberate friction; frequency alone doesn't override safety.

2. When an action is used rarely (e.g. "export audit log," "change
   workspace region"), nest it inside a secondary/overflow menu rather
   than giving it equal top-level billing with frequent actions —
   reserve the scarce top-level slots, and the low decision-time cost
   they carry, for what most sessions actually need.
   source: Hick's Law, Laws of UX (fetched 2026-08-13,
   https://lawsofux.com/hicks-law/): guidance to "fragment complicated
   processes into manageable stages" and progressively disclose lower-
   priority functions, citing Slack's staged feature exposure as an
   example of hiding infrequent capability behind initial simplicity.
   counter-example: do not bury a rarely used but safety-critical
   action (e.g. "revoke compromised API key") three menus deep just
   because it's rarely used — low frequency does not mean low urgency
   when it is needed; keep it reachable within two steps even if not
   one.

3. When ordering a navigation list, order items by the sequence users
   actually perform tasks in (task flow order), not alphabetically and
   not by internal org-chart/team structure — matching nav order to the
   task sequence reduces the physical/attentional distance between
   consecutively needed items.
   source: Fitts's Law, Laws of UX summary (fetched 2026-08-13, search
   result summarizing https://lawsofux.com/fittss-law/ and
   https://www.nngroup.com/articles/fitts-law/): "the time to acquire a
   target is a function of the distance to and size of the target" —
   applied to navigation order, placing the next task-sequence item
   near the current one minimizes that distance across a session,
   whereas alphabetical/org-chart order places task-adjacent items at
   arbitrary distances from each other.
   counter-example: do not force strict task-sequence order onto a
   navigation area that different user roles enter at different points
   in the sequence (e.g. an admin who only ever does step 4) —
   for a multi-role nav, group by task-sequence within each role's own
   entry point rather than imposing one global sequence order on
   everyone.

4. When a UI component set exceeds roughly 7±2 top-level choices,
   consolidate related items under one parent item rather than listing
   all of them flat — this keeps the top-level decision count within
   the range Hick's Law guidance treats as manageable before decision
   time degrades noticeably.
   source: Hick's Law, Laws of UX (fetched 2026-08-13,
   https://lawsofux.com/hicks-law/): "the time to make a decision
   increases with the number and complexity of choices," with guidance
   to fragment/stage complex option sets rather than presenting them
   flat.
   counter-example: do not consolidate a flat list of 9 items if those
   9 are all equally frequent, equally important peer categories with
   no natural parent grouping (e.g. 9 regional offices) — forcing an
   artificial parent category to hit a numeric target adds a spurious
   extra click for every one of those equally important choices.

5. REMOVAL: when a navigation tree has grown a parent menu that
   contains only one child item (a common result of nesting rare
   actions over time without periodic review), delete that
   single-child parent level and promote its one child directly — a
   menu layer that gates access to exactly one destination adds a step
   with no organizing benefit.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021) (fetched 2026-08-13
   via https://phys.org/news/2021-04-brains-opportunities.html summary)
   — applied to navigation trees that accrete extra nesting through
   additive edits (each new feature gets tucked under a parent for
   "consistency") without anyone later checking whether the parent
   layer still earns its place once it holds only one child.
   counter-example: do not flatten a single-child parent if that parent
   is a stable, named category users already rely on for orientation
   (e.g. "Settings" with currently one item, but known to be a stable
   landing spot for future settings) — the removal rule targets
   accidental single-child nesting, not an intentional category that is
   temporarily sparse.

6. Judge navigation depth by a measured directness score — can a user
   complete the target task without backtracking, and how many
   redundant hops does the path require — rather than a subjective
   "feels too deep" read of the tree structure alone.
   rationale: nesting depth counted on paper often disagrees with actual
   task difficulty — a shallow tree with poorly-named categories can
   force more backtracking than a deeper tree whose labels match users'
   own task vocabulary; the count is a proxy, the completion-without-
   backtracking behavior is the thing that actually matters.
   counter-example: do not flatten a deep-but-measurably-direct tree
   (one where users reliably reach their target on the first try despite
   several levels) just to reduce the nominal depth count — a
   structure that already scores well on directness does not need
   restructuring to satisfy a depth number.
