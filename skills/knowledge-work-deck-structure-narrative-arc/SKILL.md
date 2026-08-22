---
name: knowledge-work-deck-structure-narrative-arc
description: Use when outlining or sequencing a slide deck's content before or while drafting individual slides. Applies to the deck-narrative-arc axis.
axis: deck-narrative-arc
rule_count_floor: 3
---

# Deck structure / narrative arc

Decision rules for sequencing a deck's content, sourced from documented
presentation-structure and signposting guidance fetched during issue
#53's ux-engineering research pass (2026-08-22).

## Trigger

Apply this skill when outlining or sequencing a deck's content — before
or while drafting slides — deciding what comes first, how sections are
announced and closed, and what argument order the deck follows.
Distinguish it from deck-toolchain-selection (which tool to author with,
decided before content exists) and slide-density-and-layout (per-slide
content limits, checked once content exists).

## Procedure

1. Decide the deck's argument order first: lead with the conclusion/
   recommendation (pyramid-style) when the audience is time-constrained
   or decision-making, or lead with situation/complication/question
   before the answer (SCQA-style) when the audience needs to be brought
   to the problem before the solution will land (rule 1).
2. Open with an agenda signpost naming the sections to come (rule 2).
3. Mark every section transition with an explicit transition signpost,
   not a silent slide change (rule 3).
4. Close with a summary signpost restating the key takeaways, not a new
   final point introduced only at the end (rule 4).
5. REMOVAL: when a deck's agenda slide lists sections that the deck body
   does not actually signpost transitions between, either add the
   missing transition signposts or cut the unused agenda entries —
   don't leave the agenda promising structure the deck doesn't deliver.

## Output shape

A section-by-section outline (agenda → body sections with transition
signposts → summary), plus the chosen argument order (pyramid vs. SCQA)
and the one reason it fits this audience.

## Decision rules

1. When the audience is time-constrained or primarily needs to make a
   decision, state the recommendation or conclusion first, then use the
   remaining slides to support it with evidence — do not build up to
   the conclusion at the end.
   source: McKinsey-style Pyramid Principle presentation framework
   (fetched 2026-08-22,
   https://a1slides.com/mckinsey-presentation-framework/): the Pyramid
   Principle leads with the recommendation and spends the rest of the
   deck proving it, rather than building an argument toward a
   conclusion revealed only at the end.

2. When the audience needs to first understand why the topic matters
   before a recommendation will make sense, sequence the deck as
   Situation, Complication, Question, then Answer, rather than leading
   with the answer.
   source: SCQA framework (fetched 2026-08-22,
   https://a1slides.com/mckinsey-presentation-framework/): SCQA is
   described as a consulting-industry-standard structure for building a
   narrative around a main idea by first establishing situation and
   complication before stating the answer.

3. Open a deck with an agenda signpost that outlines the major themes or
   sections the audience should expect, rather than starting directly
   with content and no roadmap.
   source: Antoni Lacinai, "Signposts in Speech" (fetched 2026-08-22,
   https://www.antonilacinai.com/news/signposts-in-speech/): agenda
   signposts "outline the major themes or format of the speech,"
   distinct from introduction, transition, and summary signposts.

4. Mark every move from one section to the next with an explicit
   transition signpost (e.g. "moving on to," "now let's consider")
   rather than changing topic silently between slides.
   source: Antoni Lacinai, "Signposts in Speech" (fetched 2026-08-22,
   https://www.antonilacinai.com/news/signposts-in-speech/): transition
   signposts are used "to smoothly guide listeners between ideas,"
   named as a distinct signpost category from agenda or summary.

5. Close the deck with a summary signpost that restates the key
   takeaways using explicit summary language, rather than ending on a
   new point introduced for the first time on the final slide.
   source: Antoni Lacinai, "Signposts in Speech" (fetched 2026-08-22,
   https://www.antonilacinai.com/news/signposts-in-speech/): summary
   signposts "communicate key takeaways" using language such as "in
   summary," helping audiences retain the deck's essential points.
