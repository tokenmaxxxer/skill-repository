---
name: upstream-defect-report-comprehensibility
description: >-
  Use when drafting or reviewing an upstream defect report and its
  expected/actual behavior, code/log/command snippets, environment facts,
  repro steps, or lead fact are not yet formatted for a stranger maintainer to
  parse on first read. Trigger on requests like "make this bug report
  readable", "split it into expected vs actual lines", "put the error message
  above the fold", "업스트림 버그 리포트 읽기 쉽게 다듬어줘". Do NOT use for deciding what
  content to cut from the report before filing (use
  upstream-defect-report-subtraction).
metadata:
  axis: comprehensibility
  rule_count_floor: 5
  role: upstream-defect-report

---

# Comprehensibility — making the report readable by a stranger

Decision rules for structuring a defect report so a maintainer who has
zero context on the reporter's system can understand the failure on
first read, without back-and-forth.

## Trigger

Apply this skill whenever a defect report is being drafted or reviewed
before filing upstream, and any of: the failure description is not yet
split into expected/actual; code, logs, commands, or paths appear as
plain prose; environment facts are unpinned and not yet labeled;
reproduction needs more than ~3 steps and isn't a numbered list; or the
single most decision-relevant fact is buried inside a longer dump.

## Procedure

1. Split the failure description into two separate, labeled lines —
   expected behavior and actual behavior (rule 1).
2. Wrap every code snippet, log excerpt, command, or file path in a
   fenced or inline code block (rule 2).
3. If the environment isn't already pinned by a lockfile the maintainer
   can read, state each relevant environment fact (OS, runtime/
   interpreter version, package version, hardware) as its own labeled
   line (rule 3).
4. If reproduction takes more than ~3 sequential steps, number them as
   an ordered list, one action per line (rule 4).
5. Identify the single most decision-relevant fact (exact error
   message, throwing line, regressed version) and quote it at the top
   of the report, above the fold; move any full log dump to a
   collapsed/linked attachment below it (rule 5).
6. Check the draft for the same failure description repeated across
   title, summary, and reproduction section in different phrasings;
   collapse to one canonical phrasing used in the title and referenced
   (not restated) elsewhere (rule 6).

## Output shape

A defect report body with: separate expected/actual lines; all
code/log/command/path content in code blocks; environment facts as
labeled lines; reproduction as a numbered list where warranted; the
single decision-relevant fact stated above the fold; and no
repeated-phrasing redundancy across sections.

## Rules

1. **When** describing the failure — **choice**: state expected
   behavior and actual behavior as two separate, labeled lines (not
   folded into one narrative sentence), so the gap between them is the
   first thing a reader parses, not something they must infer.
   source: Ten Simple Rules for Reporting a Bug, rule 5, PLOS Comput
   Biol (2022),
   https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010540

2. **When** the report includes code, logs, commands, or file paths —
   **choice**: wrap each in a fenced/inline code block rather than plain
   prose; unformatted code mixed into prose measurably slows comprehension
   because the reader must re-parse token boundaries the formatting would
   otherwise mark for free. source: Ten Simple Rules for Reporting a Bug,
   rule 8 (as above); GitHub Flavored Markdown spec conventions,
   https://github.github.com/gfm/

3. **When** the environment (OS, runtime/interpreter version, package
   version, hardware) is not already pinned by a lockfile the maintainer
   can read — **choice**: state each relevant environment fact as its
   own labeled line (`OS:`, `version:`), not folded into prose, since a
   maintainer scanning many reports needs to pattern-match this field
   without re-reading a paragraph. source: Ten Simple Rules for
   Reporting a Bug, rule 7 (as above).

4. **When** the reproduction requires more than ~3 sequential steps —
   **choice**: number the steps as an ordered list, one action per line,
   rather than a paragraph describing the sequence; sequence information
   folded into prose imposes avoidable extraneous cognitive load on a
   reader who must reconstruct the step boundaries themselves. source:
   J. Sweller, "Cognitive Load Theory," Psychology of Learning and
   Motivation (2011) — extraneous load is created by presentation format,
   not just content, and is minimized by matching structure (sequence) to
   presentation (ordered list).

5. **When** a report would otherwise bury the single most decision-
   relevant fact (the exact error message, the line that throws, the
   version that regressed) inside a long log dump — **choice**: quote
   that one fact at the top of the report, above the fold, and keep the
   full dump as a collapsed/linked attachment below it. A reader's first
   screen of text should already contain the fact that lets them route
   or dedupe the report. source: Ten Simple Rules for Reporting a Bug,
   rule 8 (as above).

6. **When** the report would otherwise repeat the same failure
   description in the title, the body summary, and the reproduction
   section in three different phrasings — **choice**: 줄이다 (cut) it to
   one canonical phrasing used in the title and referenced, not
   restated, elsewhere; restating in varied wording adds re-parsing
   cost per Sweller redundancy effect without adding information.
   source: J. Sweller, "Cognitive Load Theory" (2011), redundancy
   effect.
