---
status: proposed
files:
  - docs/issue-56/reports/market-analysis/survey.md
  - docs/issue-56/proposals/skill-ecosystem-benchmark.md
---

# Benchmark mature skill ecosystems and rank adoption candidates

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): this is a market-analysis role
deliverable, not an implementation role deliverable. The
current-state survey required by the survey-before-proposal norm
already exists on disk at
`docs/issue-56/reports/market-analysis/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic
`docs/issue-56/reports/implementation/survey.md` path, since this role
is barred from writing into another role's `reports/implementation/`
tree (board-gate). No design decision remains open beyond what that
survey and this proposal already resolve (the ranking below) — there
is nothing a second survey copy at the implementation path would add.

## Request

Issue #56 (operator direction 2026-08-22): survey mature, publicly
available skill/agent-instruction ecosystems that others already
operate at organization scale, and benchmark this repo (248 skills,
43 role families) against them. Sweep at minimum anthropics/skills,
top community Claude-skill collections, agents.md/.cursorrules, and
professional-discipline packs. Output a comparison report ranking
concrete adoption candidates (structural conventions, discipline
packs respecting licenses) with effort/benefit/license, plus gaps
where this repo is already ahead. Phase 1 (survey + proposal) only —
adoption itself is out of scope, deferred to follow-up issues.

## Constraints

- Every claim about an external repo must cite its URL (issue
  acceptance criterion) — enforced in `survey.md`.
- >=4 ecosystems surveyed with URLs — met: anthropics/skills, 4
  community collections, agents.md + .cursorrules, 4
  professional-discipline packs (11 external repos total across 4
  ecosystem categories).
- >=5 ranked adoption candidates each carrying effort, benefit, and
  license status — see below.
- Explicit list of areas where this repo is already ahead — see below.
- This phase produces no skill/script changes — adoption is follow-up
  issue work.

## Rationale

Two structural alternatives were considered for *how* to benchmark,
given what the survey found:

1. **Adopt AGENTS.md's single-file, schema-free convention** as the
   base format instead of our per-skill directory + fixed
   frontmatter/section schema. Rejected: AGENTS.md's own defining
   property is "no required schema, standard Markdown, any headings
   you like" (survey, Ecosystem 3) — adopting it would mean
   *discarding* the axis/trigger/citation formalism the issue asks us
   to benchmark other ecosystems against, not gaining anything; every
   surveyed ecosystem that has more structure than AGENTS.md (Cursor's
   `.mdc` glob-scoping, deanpeters' rich frontmatter) already exceeds
   it, so AGENTS.md is a floor, not a target.
2. **Treat deanpeters/Product-Manager-Skills' live evidence-discipline
   protocol (question-budget + Fact/Inference/Assumption labeling +
   "do-not-invent" lists, survey Ecosystem 4) as the adoption target
   in place of our static per-rule `source:` citation.** Rejected as a
   *replacement* — it answers a different problem (runtime analysis
   rigor during a live investigation) than our per-rule citation
   (auditable provenance of the rule itself, checkable without running
   an investigation). It is proposed below as an *addition* (candidate
   1), not a swap, because the two are complementary, not competing.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
current-state survey and comparison findings across all four
ecosystems with per-claim URLs. This proposal file adds the ranking,
adoption candidates, and already-ahead list the issue's acceptance
check requires.

### Structure/coverage/quality comparison table

| Ecosystem | Skill/rule count | Trigger convention | Rule format | Sourcing discipline | Validation tooling | Coverage vs. our 43 families | License |
|---|---|---|---|---|---|---|---|
| This repo | 248 skills / 43 families | `description` "Use when..." + `axis` field | Numbered Rules list, fixed Trigger/Procedure/Output-shape sections | **Every rule cites `source:`** | Not confirmed present (out of scope this survey) | baseline | n/a |
| anthropics/skills | 19 skills | free-text `description` only | unstructured prose | none found | none found | narrow (demo/product set) | mixed (Apache-2.0 / source-available per skill) |
| obra/superpowers | ~14 skills | one-line `description` | imperative prose | none | pre-commit on unrelated `evals/` dir only | narrow (SWE-process only) | MIT |
| ComposioHQ/awesome-claude-skills | ~28 hosted | one-paragraph `description` | ad hoc headers, capability lists | none | none | narrow-moderate (dev-tooling + light marketing) | Apache-2.0 |
| VoltAgent / karanb192 link-lists | 0 authored (index only) | n/a | n/a | n/a | link-liveness CI only | inherited from linked repos | MIT (list itself) |
| AGENTS.md | 1 file, no fixed count | none (always-on; path-nesting only) | free prose | none | none | engineering-ops only, not a discipline system | MIT / LF project terms |
| Cursor `.mdc` rules (awesome-cursorrules) | ~200+ packs | **glob + description + alwaysApply**, 4 activation modes | free prose per file | none | none (product parses frontmatter, no external schema check) | code/framework-only | CC0-1.0 (collection) |
| deanpeters/Product-Manager-Skills | 77 skills | `description` "Use when..." + `best_for`/`scenarios` | numbered Procedure + strict Output schema; live source-URL requirement per claim | **source-anchored at analysis time**, "do-not-invent" lists | `validate-skills.sh`, `check-skill-metadata.py`, `check-skill-triggers.py`, `check-library-drift.py` | broad within PM/strategy, not cross-functional | "Other/NOASSERTION" — verify before reuse |
| huntsyea/product-skills | 4 skills | keyword-list `description` | prose + references table | attribution at top, not per-claim | none | narrow (4 PM frameworks) | MIT |

### Ranked adoption candidates (>=5, effort/benefit/license)

1. **Repo-local skill-schema/citation validator** (adapt
   deanpeters' `validate-skills.sh` / `check-skill-metadata.py` /
   `check-skill-triggers.py` pattern to check frontmatter completeness,
   axis presence, and that every numbered rule has a trailing
   `source:` line). Effort: **medium** (new script(s) under
   `scripts/`, no external code copied — behavior re-implemented
   against our schema). Benefit: **high** — turns our citation
   discipline from a convention into a mechanically enforced gate,
   closing the one concrete tooling gap the survey found relative to
   our closest peer. License: n/a (re-implementation, not a port) —
   deanpeters' scripts themselves are under its "Other/NOASSERTION"
   license and were not copied.
2. **Cross-skill relative-link composition** for skills that
   naturally chain (e.g. `market-analysis-competitor-mapping` →
   `market-analysis-evidence-rigor`), following deanpeters' pattern of
   skills linking to `../other-skill/SKILL.md`. Effort: **low** (doc
   edits only, additive). Benefit: **medium** — reduces cases where an
   agent runs one axis skill without realizing a dependent axis skill
   also applies. License: n/a (a link is not content reuse).
3. **Live evidence-discipline layer** (question-budget cap,
   Fact/Inference/Assumption labeling, explicit "do-not-invent" list)
   as a *shared procedure section*, modeled on deanpeters'
   `autonomous-investigation` meta-skill, layered on top of (not
   replacing) our existing per-rule `source:` citation. Effort:
   **medium-high** — needs a new shared-protocol skill plus a
   `## Procedure` update across the market-analysis/product-discovery/
   growth-analytics families that benefit most. Benefit: **high** for
   research-shaped role families specifically — closes the gap-line
   item in `survey.md`. License: "Other/NOASSERTION" on the source
   repo — treat as inspiration for an independently-authored
   procedure, not a text port, until license terms are confirmed.
4. **Glob/path-scoped trigger option**, borrowed conceptually from
   Cursor's `.mdc` `globs` field, for skills whose trigger condition is
   naturally file-pattern-shaped (e.g. a skill that only applies when
   editing `**/*.sql` or `**/Dockerfile`) as a supplement to the
   existing prose "Use when..." trigger. Effort: **low-medium** (schema
   addition, opt-in field, no rewrite of existing skills required).
   Benefit: **medium** — sharpens trigger precision for the subset of
   skills where "Use when..." prose is inherently a file-pattern
   condition; most of our 248 skills are judgment-triggered, not
   path-triggered, so this helps a minority. License: n/a (a schema
   idea, not text) — Cursor's own format is proprietary product
   behavior; awesome-cursorrules content (CC0-1.0) was not proposed for
   copying, only its field convention.
5. **Adopt/port select deanpeters PM-strategy skills not yet covered**
   (e.g. `pestel-analysis`, `ansoff-matrix`, `battle-card-builder`,
   `customer-journey-mapping-workshop` — checked against this repo's
   existing `market-analysis-*`/`product-discovery-*`/
   `marketing-*` families, which do not currently name these
   specific frameworks) rewritten from scratch in our
   axis/Rules/`source:` schema. Effort: **medium per skill** (each
   needs independent primary-source research to populate `source:`
   citations per this repo's own evidence bar — deanpeters' skills
   cite live search results, not stable per-rule URLs, so content
   cannot be copied directly). Benefit: **medium-high** — fills named
   framework gaps in the strategy family with skills matching our
   existing quality bar. License: **blocking until clarified** —
   deanpeters/Product-Manager-Skills is licensed "Other/NOASSERTION"
   per GitHub; a rewrite-from-scratch avoids copying text, but the
   *framework selection itself* (which PESTEL/Ansoff variant, which
   procedure steps) still needs independent sourcing, not
   transcription, to stay clearly outside any license concern.
6. **Contributor-facing "Skill Quality Standards" checklist**, modeled
   on VoltAgent/awesome-agent-skills' published bar (progressive
   disclosure under ~100 token metadata, <500 lines body, no absolute
   paths, scoped tool declarations) adapted into a short doc under
   `docs/handbooks/` for anyone authoring a new skill in this repo.
   Effort: **low** (single short doc, no code). Benefit: **low-medium**
   — mostly formalizes conventions this repo's schema already implies;
   useful as an explicit onboarding reference rather than a structural
   change. License: n/a (idea/checklist shape, not text) — the
   checklist's own list of criteria is generic practice, not
   copyrightable expression, and would be independently worded.

### Areas where this repo is already ahead

- **Per-rule source citation**: no surveyed ecosystem requires every
  individual rule (not just the overall skill/framework) to carry a
  `source: <url>`. deanpeters comes closest but sources at
  analysis-time, not as a pre-vetted, audit-checkable citation list.
- **Cross-functional breadth**: 43 professional-discipline role
  families is broader than any surveyed set — deanpeters' 77 skills
  (the largest external professional-discipline pack found) covers PM/
  strategy only; anthropics/skills and the community collections skew
  SWE-process/dev-tooling; AGENTS.md/.cursorrules aren't discipline
  systems at all.
- **Fixed body schema**: uniform Trigger/Procedure/Output-shape/Rules
  sectioning enforced across all 248 skills. Every other ecosystem
  surveyed uses free-form, per-author section headers.
- **Axis decomposition**: fine-grained per-decision-axis skills within
  a discipline (e.g. `market-analysis-evidence-rigor` vs.
  `market-analysis-five-forces` as separate skills) have no analogue
  in any surveyed ecosystem — the closest is Cursor's glob-scoping,
  which scopes by file pattern, not by decision axis within a
  discipline.
- **`rule_count_floor`**: a minimum rigor bar per skill; not found as
  a concept in any surveyed ecosystem.

## Out of scope

- Actually writing/porting any adopted skill, script, or doc from the
  candidates above — this proposal only ranks candidates; adoption is
  follow-up issue work per the issue's own scoping ("adoption lands as
  follow-up issues").
- Verifying the exact legal terms of deanpeters/Product-Manager-Skills'
  "Other/NOASSERTION" license beyond noting it blocks direct
  content-copying — full license review is part of whichever follow-up
  issue actually proposes a port.
- Auditing whether this repo currently has any skill-schema validation
  tooling — noted as "not confirmed present" in the survey; a full
  audit is candidate 1's own follow-up scope, not this phase's.

## How you'll know it worked

- `docs/issue-56/reports/market-analysis/survey.md` exists, names >=4
  surveyed ecosystems with URLs, and every external claim in it cites
  a source URL.
- This proposal's comparison table covers structure/coverage/quality
  for each surveyed ecosystem against this repo.
- >=5 ranked adoption candidates are listed above, each with an
  explicit effort, benefit, and license note.
- An explicit "areas where this repo is already ahead" list is present
  above.
- PR against `main` from `issue-56/market-analysis` references `#56`
  (no `Closes`/`Fixes`/`Resolves` trailer — phase-1 proposal PR).
