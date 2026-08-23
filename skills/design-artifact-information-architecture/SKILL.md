---
name: design-artifact-information-architecture
description: >-
  Use when structuring or labeling a site or app's content hierarchy — organizing categories,
  choosing depth vs. breadth, and naming labels for findability. Trigger on requests like
  "sitemap structure", "category depth vs breadth", "label naming for findability", "IA 구조
  잡아줘". Do NOT use for the step-by-step path a user takes through one task (use
  design-artifact-user-flow).
metadata:
  axis: ia-findability-vs-depth
  rule_count_floor: 3
---

# IA findability vs. depth

Decision rules for structuring a site or app's content hierarchy around
how users actually seek information rather than internal org structure,
sourced from NN/g's IA study guide and IA topic report.

## Trigger

Apply this skill when organizing a site or app's content into
categories, choosing between a deep narrow tree and a shallow broad
one, or naming the labels users will click through to find content —
distinguishing it from ux-engineering-navigation-depth, which governs
where an already-defined action sits in a nav menu rather than how the
underlying content taxonomy itself is structured and labeled.

## Procedure

1. Gather evidence of users' own mental models and vocabulary for the
   content (e.g. via card sorting) before drafting category structure
   (rule 1).
2. Draft category labels that carry clear information scent — a user
   should be able to predict what's behind a label before clicking
   (rule 2).
3. Do not impose an artificial maximum-click-depth constraint on the
   tree; let scent quality, not click count, determine acceptable depth
   (rule 3, REMOVAL).
4. For an item that genuinely belongs under more than one category,
   place it under both (a polyhierarchy) rather than forcing a single
   parent (rule 4).

## Output shape

A content hierarchy/tree with labeled categories, each label chosen
for information scent rather than internal terminology, annotated with
which depth/breadth tradeoff was made and why, plus any polyhierarchy
exceptions noted (item, the multiple parent categories it lives under,
and why a single parent would have misrepresented it).

## Decision rules

1. When drafting a site or app's category structure, base it on how
   users actually seek and describe the content (their own mental
   models and vocabulary), not on the organization's internal org-chart
   structure or department names — structure that mirrors internal
   teams routinely fails to match how visitors go looking for things.
   source: NN/g, "Information Architecture Study Guide"
   (https://www.nngroup.com/articles/ia-study-guide/): frames IA as
   organizing and labeling content "in a way that supports usability
   and findability," built from user research into how people actually
   search, rather than from internal structure.
   counter-example: do not preserve a department-driven category (e.g.
   "Enterprise Solutions Division") just because it maps cleanly to an
   internal team — if user research shows visitors look for that
   content under a task-based label (e.g. "For large teams"), use the
   task-based label instead.

2. When naming a category or navigation label, choose wording that
   gives users a clear prediction of what they'll find behind it
   (strong "information scent"), and treat that scent quality — not
   click-count — as what determines whether depth is acceptable.
   source: NN/g IA topic report
   (https://www.nngroup.com/reports/topic/information-architecture/):
   NN/g's IA research repeatedly ties findability to labels carrying
   accurate information scent, so users can judge, before clicking,
   whether a link leads where they want.
   counter-example: do not flatten a deep-but-well-scented tree into a
   shallower one with vaguer labels just to reduce nominal depth — a
   vague top-level label ("Resources") with no scent can force more
   backtracking than a well-labeled path three levels deep.

3. REMOVAL: when a stakeholder proposes restructuring the IA to force
   every page within 3 clicks of the homepage, remove that constraint —
   the "3-click rule" is a myth NN/g explicitly refutes; depth on its
   own does not predict abandonment or findability failure, so do not
   flatten a tree, merge unrelated categories, or compress genuinely
   distinct content levels solely to satisfy a click-count ceiling.
   source: NN/g, "Information Architecture Study Guide"
   (https://www.nngroup.com/articles/ia-study-guide/): NN/g's IA
   guidance explicitly refutes the 3-click rule, holding that depth is
   acceptable as long as labels carry clear information scent letting
   users predict what's behind a link, and that users tolerate more
   clicks when each step confirms they're on the right path.
   counter-example: if a category truly has grown unnecessarily deep
   for reasons unrelated to content complexity (e.g. accreted
   single-child parents), address that as its own structural problem —
   but justify the fix by scent/complexity evidence, not by a bare
   click-count target.

4. When an item genuinely fits more than one category equally well
   (a real outlier, not a mis-sorted item), model it as a
   polyhierarchy — surfaced under each relevant parent — rather than
   forcing a single "best-fit" parent and hiding the other valid path.
   source: NN/g IA topic report
   (https://www.nngroup.com/reports/topic/information-architecture/) and
   card-sort evidence per NN/g's IA study guide
   (https://www.nngroup.com/articles/ia-study-guide/), which cites card
   sorting as an input for surfacing exactly these cross-category
   placements when a meaningful share of sorters split an item across
   groups.
   counter-example: do not default every ambiguous item to a
   polyhierarchy — if card-sort or other evidence shows most users
   expect the item under one clear parent and only a small minority
   split it, single-parent placement with a cross-link is usually
   enough; reserve true polyhierarchy for items that recur as outliers
   across the evidence, not for every mildly ambiguous case.
