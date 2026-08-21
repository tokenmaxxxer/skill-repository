---
name: upstream-defect-report-convention
description: Use when preparing to file a defect against an upstream project and its issue template, required pre-submission steps, commit-linking convention, report channel, contributor tone, or duplicate-check surface haven't yet been matched to that project's actual current norms.
axis: convention
rule_count_floor: 5
role: upstream-defect-report
---

# Convention — matching the upstream project's own norms

Decision rules for conforming a defect report to the specific upstream
project's stated process, so the report enters triage through the
channel and shape that project's maintainers already expect.

## Trigger

Apply this skill before filing a defect report against an upstream
project, whenever the report's template conformance, required
pre-submission steps, cross-link format, channel, tone, or duplicate
check have not yet been checked against that specific project's own
current process.

## Procedure

1. If the repo ships an issue template (`.github/ISSUE_TEMPLATE/*` or a
   CONTRIBUTING.md-stated format), fill every field in that template's
   own order rather than free-writing (rule 1).
2. If CONTRIBUTING.md or the template states a required pre-submission
   step, perform it and state its result in the report, not just the
   symptom (rule 2).
3. If the project's commit/PR history shows a consistent linking
   convention for fix commits, use that project's own convention to
   reference the defect (rule 3).
4. If the project designates a specific channel for this report type
   (security disclosure address, discussion forum for usage questions),
   route to that channel instead of the general tracker (rule 4).
5. Check whether CONTRIBUTING.md is stale relative to the last 5-10
   merged/closed issues of the same type; if it is, pattern-match the
   convention actually in force instead of the stale written
   instructions (rule 5).
6. Check the reporter's habitual tone against the tone visible in past
   accepted issues from this project's contributor culture, and reduce
   demanding/impatient phrasing to a plain, patient statement if it
   doesn't match (rule 6).
7. Before concluding no duplicate exists, run a concrete title/body
   overlap comparison against both the open backlog and the last 15-20
   closed issues, not a single keyword search (rule 7).

## Output shape

A defect report routed to the correct channel, filled into the
project's own template/field order, carrying a stated pre-submission-
step result, using the project's own commit-linking convention, in a
tone matching the project's contributor culture, filed only after a
backlog-plus-closed-set duplicate check found no hit.

## Rules

1. **When** the upstream repository ships an issue template (`.github/
   ISSUE_TEMPLATE/*` or a CONTRIBUTING.md-stated format) — **choice**:
   fill every templated field in that template's own order rather than
   free-writing a report and pasting it in; a report whose sections
   don't match the template's headings is harder for maintainers to
   triage against their own tooling (labels, bots keyed to headings).
   source: nayafia, "contributing-template,"
   https://github.com/nayafia/contributing-template ; The Good Docs
   Project, "About the Contributing Guide Template,"
   https://www.thegooddocsproject.dev/template/contributing-guide

2. **When** CONTRIBUTING.md or the issue template states a required
   pre-submission step (search existing issues, confirm against latest
   release, run a specific diagnostic command) — **choice**: perform
   that step and state its result in the report (e.g. "searched, no
   duplicate found"; "reproduces on latest tag vX.Y.Z"), not just the
   symptom; skipping a stated required step gets a report closed
   unread on many projects. source: Ten Simple Rules for Reporting a
   Bug, rules 2–3, PLOS Comput Biol (2022),
   https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010540

3. **When** the project's own commit/PR history shows a consistent
   commit-message convention (e.g. Conventional Commits, a scoped
   prefix style) for linked fix commits — **choice**: reference the
   defect using that project's own linking convention (issue number
   format, keyword like "Fixes #N") rather than an ad hoc cross-link,
   so the project's own automation (changelog generators, auto-close
   bots) picks it up. source: tenthirtyam, "Writing Practical
   Contribution Guidelines for GitHub Repositories,"
   https://tenthirtyam.org/dispatches/2026/03/21/writing-practical-contribution-guidelines-for-github-repositories/

4. **When** the project designates a specific channel for the report
   type (e.g. security issues go to a private disclosure address, not
   the public tracker; usage questions go to a discussion forum, not
   the bug tracker) — **choice**: route to that channel instead of the
   general issue tracker even if the tracker is more visible; filing in
   the wrong channel is treated as a convention violation independent
   of report quality and gets redirected or ignored. source: Ten Simple
   Rules for Reporting a Bug, rule 4 (as above).

5. **When** a project's CONTRIBUTING.md is stale relative to its actual
   current workflow (a labeled path, a bot, or a template that no
   longer matches what maintainers actually ask for in recent closed
   issues) — **choice**: 생략 (drop) following the stale written
   instructions verbatim and instead pattern-match the last 5–10 merged/
   closed issues of the same type for the convention actually in
   force; treating a written-but-abandoned convention as authoritative
   produces a report that "obeys the rules" but still gets bounced.
   source: River, "CONTRIBUTING.md Template," discussion of stale
   contribution docs, https://rivereditor.com/blogs/write-contribution-guide-open-source-project

6. **When** the reporter's own habitual tone (demanding, impatient, or
   entitled phrasing) would not match the collaborative tone the
   project's own contributor culture visibly uses in past accepted
   issues — **choice**: 줄이다 (reduce) hostile or demanding phrasing to
   a plain, patient statement of the problem; tone mismatch with the
   receiving community's convention measurably reduces the odds of a
   maintainer engaging at all. source: Ten Simple Rules for Reporting a
   Bug, rule 1 (as above).

7. **When** checking whether a defect has already been reported —
   **choice**: run a concrete similarity comparison (title/body overlap)
   against both the open backlog and the last 15-20 closed issues, not
   a single free-text keyword search; a defect closed as duplicate or
   wontfix under different wording than the reporter's own phrasing is
   invisible to a plain keyword search but not to an overlap comparison
   against the closed set. Treat closed issues as part of the dedup
   surface, not only open ones — a re-report of something already
   resolved wastes the same maintainer attention as a live duplicate.
