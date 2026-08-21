---
name: devrel-channel-convention
description: Use when you need guidance on Channel and format convention. Applies to the channel-convention axis.
axis: channel-convention
rule_count_floor: 8
---

# Channel and format convention

Decision rules for which content format, channel, and code-sample
convention a devrel deliverable should follow, so the same kind of
decision is made the same way across the program. Research trail:
layer 1 (practitioner CFP/community convention) plus layer 2 (named
API-style-guide and usability-heuristic convention).

## Rules

1. When authoring a code sample for public release, follow the
   formatting, commenting, and naming conventions already declared in
   the product's own API style guide rather than the individual
   author's personal style — code samples function as documentation,
   and an inconsistent sample forces every reader to relearn
   conventions per example instead of reusing what they already learned
   from the last one. source:
   https://docs.bump.sh/guides/technical-writing/incorporating-api-documentation-guidelines-into-your-api-style-guide/

2. When multiple sample snippets demonstrate the same operation across
   languages, keep parameter names, variable names, and comment
   placement consistent across every language variant — consistency
   across a whole surface is what lets a reader avoid re-asking "is
   this the same thing?" at each new sample, the exact cost Nielsen's
   consistency-and-standards heuristic names. source:
   https://heurilens.com/blog/nielsens-heuristics/nielsens-10-heuristics-real-website-examples

3. When submitting a conference proposal, match its stated topic to the
   conference's explicitly published themes rather than pitching an
   off-theme topic on the assumption content quality alone will carry
   it — reviewers preferentially select on-theme submissions, and an
   off-theme proposal needs exceptional independent value to clear that
   bar. source: https://www.freecodecamp.org/news/how-to-write-a-good-conference-talk-proposal/

4. When the same piece of information could become either a talk or a
   piece of written content, produce the written piece first and treat
   the talk as a derivative of it, not the other way around — CFP
   practitioner convention already treats an existing public writeup as
   a credibility prerequisite for the talk proposal, so the writeup has
   to exist before the talk is worth pursuing. source:
   https://medium.com/@KavishaMathur/how-to-write-a-cfp-that-gets-you-on-stage-at-major-tech-conferences-template-that-works-9563c5e780a6

5. When first entering a developer community (a forum, a Slack, a
   Discord) as a program representative, keep the first several
   interactions to answering existing questions and avoid any product
   promotion until then — community is the base pillar the rest of
   devrel rests on, and promoting before contributing breaks the trust
   that pillar depends on. source:
   https://chrisreddington.com/blog/devrel-four-pillars-authentic-foundation/

6. **REMOVAL**: when a sample-code convention guide has accumulated two
   accepted ways to do the same thing (e.g. two still-documented auth
   patterns), pick one as canonical and delete the other from new
   samples instead of keeping both "for compatibility" — API
   style-guide convention exists specifically to keep one way of doing
   a thing visible at a time, and two live conventions reintroduce the
   same-thing-or-not cost consistency is meant to remove. source:
   https://stoplight.io/api-style-guides-guidelines-and-best-practices

7. When naming a new SDK method or sample-repo file, match the existing
   repo's established naming pattern (verb-noun order, casing
   convention) rather than introducing a new pattern for the new
   addition alone — teams that hold to one style guide develop faster
   and ship more predictable APIs, and predictability is the direct
   developer-experience payoff of following the existing convention.
   source: https://stoplight.io/api-style-guides-guidelines-and-best-practices

8. **REMOVAL**: when a channel in the program's publishing list shows
   measurably declining or negligible developer presence, stop
   publishing new content there instead of maintaining parallel
   publishing across every channel the program has ever used —
   community-first convention favors concentrating effort where
   developers actually are over comprehensive channel coverage for its
   own sake. source: https://chrisreddington.com/blog/devrel-four-pillars-authentic-foundation/
