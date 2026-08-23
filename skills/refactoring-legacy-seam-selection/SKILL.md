---
name: refactoring-legacy-seam-selection
description: >-
  Use when choosing how to introduce new or changed behavior into legacy code
  without tests, deciding between Sprout/Wrap Method and a full object seam, or
  picking where in the call graph to place the seam. Trigger on requests like
  "seam 어디에 둬야 해", "sprout method or wrap method", "break this dependency for
  testing", "fake out this external call". Do NOT use for choosing Strangler Fig
  vs Branch by Abstraction for a whole-slice legacy migration and its cutover
  (use refactoring-legacy-strangler-fig-migration).
metadata:
  axis: seam-selection
  rule_count_floor: 5
---

# Seam selection

Research trail: Michael Feathers, *Working Effectively with Legacy Code* (seam taxonomy: preprocessing/link/object seams; Sprout Method, Sprout Class, Wrap Method), Martin Fowler's bliki "LegacySeam", and practitioner write-ups (Mike Bland; Codably's sprout/wrap/seam comparison) that restate the book's decision order in current terms. No independent academic layer was found specific to seam mechanics beyond Feathers' own text — this is a practitioner-canon axis, not a research-literature one, consistent with this role's sparse source tier.

## Trigger

Apply this skill when deciding how to introduce new or changed behavior
into untested legacy code, choosing between Sprout/Wrap Method and
instrumenting a full object seam, selecting which of several candidate
seam points to use, or scoping how much of a legacy method a seam
should enclose.

## Procedure

1. For behavior that changes at a single, clearly-localized point, use
   the Sprout Method rather than editing inline (rule 1).
2. For behavior that must run unconditionally before/after an existing
   method on every call, use the Wrap Method rather than editing inside
   it (rule 2).
3. To replace a hard external dependency with a fake, use an object
   seam rather than a preprocessor or link seam (rule 3).
4. Base the Sprout/Wrap-vs-full-seam choice on confidence and budget,
   not code aesthetics (rule 4).
5. When multiple call sites could serve as the seam, prefer the one
   closest to the point of actual behavioral difference (rule 5).
6. When only one responsibility of an entangled method needs testing,
   narrow the seam to the smallest enclosing scope rather than seaming
   the whole method (rule 6).
7. Before choosing a seam, read the surrounding legacy code for
   undocumented business rules the seam choice could otherwise miss
   (rule 7).

## Output shape

A minimal seam (Sprout Method, Wrap Method, or a scoped object seam)
placed at the point closest to the actual behavioral difference,
chosen by confidence/budget rather than aesthetics, informed by a read
of the surrounding legacy code for hidden rules.

## Rules

1. When behavior needs to change at a single, clearly-localized point inside an otherwise-clear legacy method, use the Sprout Method (write the new logic as a new, separately-testable method/function and call it from the one point) rather than editing inline — this ships new, fully-tested behavior without first earning the right to refactor the surrounding legacy code. source: https://codably.dev/code-quality/breaking-dependencies-in-legacy-code-sprout-wrap-seam-patterns

2. When new behavior must run unconditionally before or after an existing method's behavior on every call (e.g., logging, validation, an added side effect), use the Wrap Method rather than editing inside the legacy method — Wrap Method does not increase the size of the existing method and keeps the new logic's tests independent of the old logic's tests. source: https://codably.dev/code-quality/breaking-dependencies-in-legacy-code-sprout-wrap-seam-patterns

3. When the legacy code needs a hard external dependency (a network client, a clock, a global/static call) replaced with a fake before it can be brought under test at all, use an object seam (subclass-and-override, or extract-and-override the offending call) rather than reaching for the preprocessor or the linker — object seams are available in ordinary object-oriented code without a build-system change, whereas preprocessing and link seams require C/C++-style build machinery most modern codebases don't have. source: https://martinfowler.com/bliki/LegacySeam.html

4. When deciding between Sprout/Wrap and a full seam-based characterization pass, base the call on confidence and budget, not on code aesthetics: pick a minimal seam (sprout/wrap) when you are not confident the existing method's behavior is even correct and you cannot afford to touch the surrounding code yet, and only escalate to instrumenting a full object seam once you have the time and confidence to also characterize the untouched legacy path. source: https://gist.github.com/birdofpray70/8a42b05e2dd1a2f19922d0d92e9e4e06

5. When a seam is found but multiple call sites could serve as the enabling point, prefer the seam closest to the point of actual difference in behavior — the source's own guidance is to substitute a fake exactly where the dependency is invoked rather than at a higher call site, minimizing how much untested legacy code sits between the seam and the change. source: https://www.informit.com/articles/article.aspx?p=359417&seqNum=2

6. **REMOVAL**: When a legacy method has multiple entangled responsibilities and the change only needs one of them under test, do not introduce a seam for the whole method — narrow the seam to the smallest enclosing scope that isolates the dependency actually being changed, and leave the rest of the method's structure untouched until a later, separately-motivated step; enlarging the seam "while you're in there" is scope creep the seam taxonomy does not require. source: https://mike-bland.com/2023/08/23/legacy-code-seams-and-the-most-important-design-guideline.html

7. Before choosing a seam, read the surrounding legacy code specifically to surface undocumented business rules and load-bearing workarounds that no test currently covers, not only the dependency the seam needs to isolate — a seam chosen from the visible call graph alone can sit on the wrong side of a hidden rule, making the eventual characterization pass miss the exact behavior most likely to matter in production.
