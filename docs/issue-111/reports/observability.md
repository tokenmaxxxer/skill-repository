---
issue: 111
role: observability
kind: review-record
type: audit
code_under_review: scripts/check_*.py (skill-repository's own SKILL.md/eval-corpus gates), scripts/rank_skill_invocation.py
breaking: false
loop_state: reported
upstream:
  - path: docs/issue-111/reports/observability.md
    sha: same-commit
signal_type: n/a
attribute_name: n/a
attribute_type: n/a
verdict: pass
---

# issue-111 — observability record

## What was done

Silent-failure sweep of this repo (skill-repository) per the audit lens in
issue #111 / on-the-record#2295 — "for every mechanism: when this fails,
what does it say, where, and to whom, and can that be swallowed?" Scope for
this pass: the repo's own corpus-lint mechanisms (`scripts/check_*.py`, 7
scripts / 1794 lines, the machinery that is supposed to catch broken
SKILL.md triggers/guidance before they land) and one measurement mechanism
(`scripts/rank_skill_invocation.py`) that gates which skills get eval
coverage. Not a manual read of all 273 SKILL.md files' prose — the audit
targets the *mechanisms* whose silent failure would make a manual read
unreliable in the first place, per the issue's own framing ("grep-level
suspicion alone is not a finding — run the real code path").

Five findings below, each demonstrated by running the actual code path and
pasting the actual output. Two areas were swept and found clean, stated
explicitly per the issue's "empty state" requirement rather than omitted.

## Why

The issue names the lens explicitly and asks for inventory, not fixes:
"the inventory then becomes fix issues, batched by mechanism." This record
is that inventory. I chose to spend the session's depth on the check
scripts rather than skill-by-skill prose review because (a) the scripts are
the actual enforcement surface — a prose defect the scripts don't catch
will recur indefinitely regardless of how many times one session reads it
by eye, and (b) the scripts self-report pass/fail, which is exactly the
"wrong signal" failure class the issue is hunting: a script that prints
"OK" or "N skills checked" is a report a human trusts without re-deriving,
so a gap between what it prints and what it actually checked is the
highest-leverage silent failure in this repo.

## Upstream basis

- Issue #111 / on-the-record#2295 (program directive, audit lens, failure
  classes, acceptance criteria).
- This repo's own `scripts/check_*.py`, `scripts/rank_skill_invocation.py`,
  `docs/issue-102/ranking.md`, and 20+ landed `docs/issue-*/reports/*.md`
  files, read and executed live during this session (paths and commands
  cited per finding below).

## Findings

### F1 — `check_skill_conformance.py`'s two opt-in checks have never been invoked with their flags in this repo's history; live run finds a real violation they'd have caught (HIGH — silent acceptance + wrong signal)

`scripts/check_skill_conformance.py` ships two additive, opt-in checks,
each gated behind a flag and a manifest file that already exists in the
repo:

- `--manifest scripts/procedure_authored_skills.txt` (199 skill names) —
  requires `## Trigger` / `## Procedure` / `## Output shape` headings.
- `--require-use-when-and-source scripts/issue_1996_use_when_source_manifest.txt`
  (9 skill names) — requires a literal "use when" clause and a `source:`
  citation.

Every landed report in this repo's history that cites this gate as
evidence — issues #58, #60, #61, #62, #63, #66, #74, #77, #82, #87, #90,
#93, #96 (grep across `docs/issue-*/`, 70+ matching lines) — cites the
**bare** invocation:

```
$ grep -rn "check_skill_conformance.py" docs/ | grep -v test/
# every hit across #58..#96 is: python3 scripts/check_skill_conformance.py
# (no --manifest, no --require-use-when-and-source, anywhere in landed history)
```

Running the bare command today, exactly as every prior session did:

```
$ python3 scripts/check_skill_conformance.py
273 skills checked
```

Pass-shaped, exit 0 — this is the signal 13+ landed sessions relied on as
"conformance verified." Running the identical script against the manifests
that already ship two directories over, which nothing in this repo's
history has ever done:

```
$ python3 scripts/check_skill_conformance.py \
    --manifest scripts/procedure_authored_skills.txt \
    --require-use-when-and-source scripts/issue_1996_use_when_source_manifest.txt
1 violation(s) found in 1 skill(s) (273 skills checked):
  skills/accessibility-aria-and-contrast-rules/SKILL.md:1: missing at least one 'source: <https?:// URL>' citation
```

`skills/accessibility-aria-and-contrast-rules` has been silently failing
the issue-#1996 use-when/source requirement through every one of those
13+ landed "green" reports, because the checker that would have caught it
only runs when a human remembers to type two flags nobody has ever typed.
The manifest files sitting in `scripts/` look like committed intent
("this needs checking") that never got wired to execution.

### F2 — `rank_skill_invocation.py`'s verdict source excludes this repo's own docs/, silently dropping 48 already-committed skill-verdict citations from the ranking that gates eval coverage (HIGH — silent loss)

`scripts/rank_skill_invocation.py` computes a skill-usage ranking from two
sources; source 2 is:

```python
patterns = [
    "/home/jwjung/tm-dicequest/docs/issue-*/reports/*.md",
    "/home/jwjung/.claude/plugins/marketplaces/tokenmaxxxer/docs/**/*.md",
]
```

Neither pattern matches this repo's own tree
(`/home/jwjung/.tokenmaxxxer/work/skill-repository-issue-111-observability`,
`docs/issue-*/reports/*.md`) — even though this repo's docs are the exact
shape (`docs/issue-<n>/reports/<role>.md`) the first pattern already
targets in a *different* repo. Live count of `skill-verdict:` lines
already committed in this repo's own `docs/`:

```
$ grep -rhoE "skill-verdict:\s*([a-z0-9-]+)" docs/ | sed -E 's/skill-verdict:\s*//' | sort | uniq -c | sort -rn
      8 knowledge-management-taxonomy-tagging
      8 knowledge-management-supersession-lifecycle
      8 knowledge-management-structure-findability
      8 knowledge-management-pattern-extraction
      8 knowledge-management-curation-pruning
      2 game-character-rendering-composition
      2 conformance-review-requirement-extraction
      1 technical-feasibility-build-vs-buy
      1 product-discovery-opportunity-solution-tree
      1 model-routing
      1 market-analysis-mece-proposal
      1 finance-unit-economics-ltv-cac-band
      1 defect-verification-reproduction-evidence-quality
```

48 lines, none reachable by the script's glob. Running the script live:

```
$ python3 scripts/rank_skill_invocation.py | head -20
sessions_measured	39
rank	skill	invoked	verdicts	mounted	score
1	implementation-performance-data-structure-choice	0	48	8	104
...
```

No `knowledge-management-*` skill appears anywhere in the ranking's
output, despite 40 of the 48 excluded lines belonging to exactly five
`knowledge-management-*` skills (8 each). This ranking is not academic:
`docs/issue-102/ranking.md` documents this exact script/method producing
the "top-20 most-invoked skills" that then received pressure-test eval
scenarios (commit 0de4154). `evals/pressure/` has exactly 20 skill
directories, and none of them is a `knowledge-management-*` skill:

```
$ ls evals/pressure | wc -l
20
$ ls evals/pressure | grep knowledge-management
(no output)
```

`docs/issue-102/ranking.md`'s own Method section documents one bias
explicitly ("the work-log window covers recent sessions only... biased
toward the implementation/UX/conformance flows that ran recently — that
bias is the point") but says nothing about the second, larger, silent
bias: the ranking mechanism structurally cannot see usage evidence that
lives inside the very repo it is ranking skills for. A session invoking
`rank_skill_invocation.py` from this repo gets a clean-looking table with
no indication that its own repo's history was excluded from the count.

### F3 — `check_retrieval_sanity.py` is a single hardcoded historical regression pin, but its name and "PASS" banner read as a general retrieval-health gate (MEDIUM — wrong signal)

Source (`scripts/check_retrieval_sanity.py`) asserts exactly one fixed
task string against exactly two named skills outranking exactly one named
competitor — the issue-#99 regression it was built to pin. Live run:

```
$ python3 scripts/check_retrieval_sanity.py
...
Retrieval sanity: PASS
```

"Retrieval sanity: PASS" reads as "retrieval is sane" for the corpus. It
actually means "these 2 skills still beat this 1 skill on this 1 frozen
sentence." A new retrieval blind spot anywhere else in the other 271
skills, or a regression on any task text other than the one hardcoded
string, prints the identical reassuring banner. This is not wrong to
exist (regression pins are legitimate), but the name and single-line exit
banner overstate its coverage to anyone who hasn't read the source —
exactly the "wrong signal" class the issue names ("HEALTHY that means
only 'alive'").

### F4 — six of the seven `check_*.py` gates silently swallow `--help` and run the full corpus scan instead (LOW — caller-dependent visibility)

```
$ grep -n "argparse" scripts/check_*.py
scripts/check_skill_conformance.py:46:import argparse
```

Only `check_skill_conformance.py` parses arguments. The other six accept
none, so `--help`/`-h` is silently ignored as an unrecognized "no
arguments" case and the script runs its default full-corpus scan instead
of printing usage:

```
$ python3 scripts/check_progressive_disclosure.py --help
OK: 273 skills checked, all bodies <= 150 lines; 41 index<->references/rules.md bijections verified.
```

Exit 0, no usage text, no indication `--help` wasn't understood. Low
blast radius (the scripts still do something correct), but it's a caller-
dependent-visibility gap: a session or human typing `--help` to learn a
script's arguments gets a wall of "OK" instead, and has to read source to
find out `--help` was a no-op.

### F5 — none of the 7 corpus-lint gates are wired to run automatically; all enforcement is manual invocation (HIGH — root cause of F1)

```
$ find . -iname "*.yml" -o -iname "*.yaml" | grep -i workflow
(no output)
$ ls .github 2>&1
ls: cannot access '.github': No such file or directory
$ find . -iname ".pre-commit*" -o -iname "Makefile"
(no output)
```

No CI workflow directory, no pre-commit hook, no Makefile. The 1794 lines
of `scripts/check_*.py` validation logic — frontmatter shape, trigger
sentences, rule citations, progressive-disclosure bijections, retired
vocabulary, eval-scenario schema, rationalization tables — run only when
a human or session remembers the exact command. F1 is the demonstrated
consequence: even the humans who *do* remember to run the gate have only
ever run its bare, weaker form. A gate whose non-invocation produces no
signal at all is the umbrella version of every other finding here: the
failure to run is itself invisible, to every consumer, every time.

## Swept clean (stated explicitly, not omitted)

- **Dangling `(use X)` cross-references in SKILL.md frontmatter
  descriptions.** Every "Do NOT use ... (use X)" clause across all 273
  skills was checked against the actual `skills/` directory listing:

  ```
  0 dangling '(use X)' cross-references found among 273 skills
  ```

  Clean. (Method: extracted every `(use <name>)` parenthetical from each
  skill's frontmatter and confirmed `<name>` resolves to a real skill
  directory.)

- **`check_description_enrichment.py`'s hardcoded 44-prefix `FAMILY_PREFIXES`
  allowlist**, which decides which skills require a "Do NOT use" sibling
  clause. Computed actual skill-name clustering against the hardcoded list:
  235/273 skills fall inside a known family; the 38 outside it cluster into
  no missed multi-member family (one near-miss, `requirements-engineering-rules`
  vs. `requirements-quality`, checked and ruled out — they don't share a
  common family-prefix pattern under the script's own matching rule, so
  there is no live sibling-confusion gap today).

- **`check_rationalizations.py`'s hardcoded 3-prefix `FAMILY_PREFIXES`**
  (`conformance-review-`, `defect-verification-`, `implementation-`),
  which decides which skills must carry a Rationalizations table. Verified
  live: all 16 skills that actually carry a `## Rationalizations` section
  and a `references/rationalizations.md` file fall inside these 3
  prefixes today — 0 live gap. Flagged as a **latent** structural risk,
  not a current defect: the allowlist is hardcoded rather than derived
  from a metadata tag, so a future judgment-gate skill family landing
  outside these three prefixes would silently skip validation. Not
  claimed as a finding per the issue's own instruction against grep-level
  suspicion; recorded here so a later sweep doesn't have to rediscover it.

## What did not work

Nothing attempted was abandoned. One early hypothesis was checked and
ruled out rather than reported: that `check_rationalizations.py`'s
hardcoded family-prefix list currently misses a live judgment-gate skill
outside its 3 prefixes. Live enumeration showed 16/16 alignment, so it is
recorded under "swept clean" as a latent risk, not asserted as a finding.

## Open findings

| # | Finding | Resolution path |
|---|---|---|
| F1 | Opt-in manifest checks in `check_skill_conformance.py` never invoked; `accessibility-aria-and-contrast-rules` fails them today | Fix issue: make the two manifest flags non-optional (always-on) in `check_skill_conformance.py`'s default invocation, or fold their coverage into the unconditional per-skill checks; separately, fix `skills/accessibility-aria-and-contrast-rules/SKILL.md`'s missing source citation |
| F2 | `rank_skill_invocation.py` excludes this repo's own `docs/` from its skill-verdict glob, dropping 48 citations (40 for 5 `knowledge-management-*` skills) | Fix issue: add this repo's own `docs/issue-*/reports/*.md` to the glob patterns (or generalize to "the repo the script is run from"); re-run the issue-102-style ranking and reconsider `evals/pressure/` coverage for the skills whose evidence was previously invisible |
| F3 | `check_retrieval_sanity.py`'s name/banner overstate a single historical regression pin as general retrieval health | Fix issue: rename to reflect scope (e.g. `check_retrieval_regression_pins.py`) and/or change the exit banner to name the specific pin(s) checked rather than "Retrieval sanity: PASS" |
| F4 | `--help` silently swallowed by 6/7 gate scripts | Fix issue: add minimal argparse (or a manual `-h`/`--help` check) to the 6 scripts, matching `check_skill_conformance.py`'s existing pattern |
| F5 | No CI/pre-commit/Makefile wiring for any of the 7 gates | Fix issue: wire at least the unconditional checks into a pre-commit hook or CI workflow; note this repo's own commit-time trailer-gate.sh precedent as the existing enforcement pattern to extend |

## Next steps

`loop_state` is terminal (`reported`) for this review-record — the sweep
itself is complete and delivered as this inventory, per the issue's own
scope ("the inventory then becomes fix issues, batched by mechanism").
Next steps belong to those future fix issues, not this one:

- File fix issues for F1–F5, batched by mechanism as the program directive
  requests, each carrying the operator's frozen no-side-effects constraint.
- F1's live violation (`accessibility-aria-and-contrast-rules`) is small
  enough it could be folded into F1's fix issue rather than filed
  separately.

## Acceptance evidence

```
$ python3 -m pytest test/ -q
..........................................................               [100%]
58 passed in 1.18s
```

No test files were added or modified by this session (inventory-only
deliverable, per issue scope — no code/script changes made). All findings
above were demonstrated by direct execution, commands and real output
pasted inline per finding, per the issue's provenance requirement
("executed-live... paste real output per finding").

skill-verdict: observability-cardinality-budget — not-applicable: task is a meta-audit of skill trigger/gate integrity, not classification of a candidate metric label's cardinality risk
skill-verdict: observability-explorability — not-applicable: no dashboard/incident-investigation design was in scope
skill-verdict: observability-methodology-selection — not-applicable: no RED/USE/Golden methodology selection for a touched surface was in scope
skill-verdict: observability-phase-trace — not-applicable: no phase-2 signal-placement record was being checked against a phase-1 methodology choice
skill-verdict: observability-signal-golden — not-applicable: no service-rollup surface was being instrumented
skill-verdict: observability-signal-red — not-applicable: no request-driven surface was being instrumented
skill-verdict: observability-signal-use — not-applicable: no resource-bound surface was being instrumented
other mounted skills: not triggered
