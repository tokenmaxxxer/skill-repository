---
name: devrel-program-subtraction
description: >-
  Use when deciding whether to add or cut a devrel program's content, channel, or program
  surface — evaluating a new content format against existing ones, retiring unused
  docs/samples/talks/channels, or consolidating instead of adding. Trigger on requests like
  "should we add a newsletter", "안 쓰는 샘플 정리해줘", "retire this conference talk", "too many
  community channels". Do NOT use for formatting or convention choices on content that stays
  (use devrel-channel-convention).
metadata:
  axis: program-subtraction
  rule_count_floor: 8
---

# Program subtraction (removal/omission decision rules)

## Trigger

Apply this skill when deciding whether to add to or cut from a devrel
program's content, channel, or program surface — evaluating a new
content format, reviewing docs/samples/talks/channels for retirement,
or choosing between consolidating existing surface and adding new
surface.

## Procedure

1. Before adding a new content format, first name which existing
   channel or format could be retired to hold total surface constant,
   and add only if nothing qualifies (rule 1).
2. Delete a docs page or sample with zero measured engagement over a
   defined review window rather than leaving it live (rule 2).
3. When a proposed new page could instead be answered by editing an
   existing page, edit the existing page instead of creating the new
   one (rule 3).
4. Retire a conference-talk topic delivered at more than 3 events with
   no content update, instead of resubmitting it (rule 4).
5. Cut optional onboarding-checklist steps out of the default path into
   an advanced appendix (rule 5).
6. Do not surface a feature used by a small minority of the target
   segment in the main path of a quickstart; defer it to a secondary
   view (rule 6).
7. Archive or merge community channels with no message activity over a
   defined window rather than letting them sit (rule 7).
8. Cut restated marketing framing from a changelog or release note and
   keep only what changed and the required developer action (rule 8).

## Output shape

An add/cut/consolidate decision for a devrel program surface (content
format, docs page, talk, onboarding step, feature exposure, community
channel, or changelog entry), attributed to the rule that drove it,
with total surface held constant by default unless the decision is to
add.

Research trail: layer 3 (academic — subtraction-neglect research) plus
layer 1/2 (practitioner minimalism and progressive-disclosure
convention).

## Rules

1. When evaluating whether to add a new content format (a video series,
   a newsletter, a new forum) to already-running channels, first name
   which existing channel or format could be retired to hold total
   program surface constant, and only add the new one if nothing
   qualifies — people systematically default to additive solutions and
   overlook subtractive ones even when subtracting scores equally well
   or better, so removal has to be made an explicit menu option or it
   gets skipped by default. source:
   https://www.nature.com/articles/s41586-021-03380-y

2. **REMOVAL**: when a docs page or sample has had zero measured
   engagement (page views, forks, stars) over a defined review window,
   delete it rather than leave it live — unused surface area is not
   free, it carries a hidden maintenance and search-noise cost that the
   additive-bias literature shows people systematically forget to count
   against it. source: https://www.nature.com/articles/s41586-021-03380-y

3. When a proposed new documentation page could instead be answered by
   editing an existing page to be more complete, edit the existing page
   and do not create the new one — this is the direct mechanical
   antidote the subtraction-neglect research names: forcing an explicit
   "could this be consolidated instead of added" check before defaulting
   to add. source: https://ideas.darden.virginia.edu/add-value-through-subtraction

4. **REMOVAL**: when a conference-talk backlog contains a topic that
   has been delivered at more than 3 events with no update to its
   content, retire it from the active rotation instead of resubmitting
   it again — a stale talk consumes a CFP slot and a rehearsal cycle
   that could go to a topic matching the product's current state, and
   "keep submitting what worked before" is exactly the additive default
   this research warns against. source:
   https://www.nature.com/articles/s41586-021-03380-y

5. When a developer-program onboarding checklist has accumulated
   optional steps beyond what's required for first success, cut the
   optional steps out of the default path and move them to an
   "advanced" appendix — minimalism in documentation practice holds
   that eliminating what isn't needed, not adding more explanation of
   it, is what best supports the reader's own sense-making. source:
   https://www.knowledgeowl.com/blog/posts/minimalism-documentation

6. When a console or SDK feature is used by a small minority of the
   target developer segment and is not part of the primary workflow, do
   not surface it in the main path of a devrel-authored quickstart —
   apply progressive disclosure and defer it to a secondary or advanced
   view so the default path stays uncluttered. source:
   https://www.nngroup.com/articles/progressive-disclosure/

7. **REMOVAL**: when a community Slack or Discord has channels with no
   message activity over a defined window, archive or merge them into
   an active channel instead of letting them sit — a dead channel is
   not neutral, it adds where-do-I-post noise for every new member, and
   leaving it is the same additive-default failure the subtraction
   research documents, applied to community structure instead of a
   single artifact. source: https://www.nature.com/articles/s41586-021-03380-y

8. When drafting a changelog or release-note entry, cut restated
   marketing framing and keep only what changed and what action the
   developer must take — the additive habit inflates changelogs with
   narrative the reader must now filter out to find the actionable
   delta, which is the same bias in miniature. source:
   https://www.nature.com/articles/s41586-021-03380-y
</content>
