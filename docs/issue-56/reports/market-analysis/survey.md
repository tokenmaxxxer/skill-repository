# Survey: current state vs. mature skill/agent-instruction ecosystems

Subject: issue-56. Scout stage used parallel fan-out (4 concurrent
`Agent` calls, one per ecosystem angle: anthropics/skills, community
collections, agents.md/.cursorrules, professional-discipline packs), one
round, all URLs verified live via WebSearch/WebFetch/`gh` on 2026-08-22.
Deepening was folded into each angle's own agent call rather than a
separate stage (saturation reached: no angle surfaced a new competing
structural convention worth a follow-up round).

## This repo's current state (write surface)

- 248 skills, one directory per skill, all under `skills/`, each
  `skills/<name>/SKILL.md`.
- Fixed frontmatter schema: `name`, `description` (mandatory
  `"Use when..."` trigger clause), `axis`, `rule_count_floor`.
- Fixed body schema, same section order in every file: `## Trigger`,
  `## Procedure`, `## Output shape`, `## Rules` (numbered list).
- **Every individual rule** carries a trailing `source: <url>` citing
  the external authority the rule is drawn from (verified in
  `skills/market-analysis-evidence-rigor/SKILL.md`).
- Organized into ~43 professional-discipline "role families" (e.g.
  `market-analysis-*`, `api-design-*`, `architecture-*`,
  `capacity-planning-*`), each split into fine-grained "axis" skills
  (one skill per decision axis within the discipline).
- No repo-local validation tooling for skill schema/citation
  completeness was found in this survey (out of scope to confirm
  exhaustively here; not contradicted by anything found externally).

## Ecosystem 1 — anthropics/skills (official)

- https://github.com/anthropics/skills — 170,935 stars, actively
  maintained (pushed 2026-08-21), no single repo-wide license (mixed:
  many skills Apache-2.0, document skills "source-available, not open
  source"; see `THIRD_PARTY_NOTICES.md`).
- Only **19 skills**, a curated demo/product set (docx, pdf, pptx, xlsx,
  brand-guidelines, canvas-design, frontend-design, mcp-builder,
  skill-creator, webapp-testing, internal-comms, academy-guide, etc.) —
  not a systematic discipline map.
- Frontmatter: only `name` + free-text `description`, no axis/trigger
  formalism, no `rule_count_floor`. Body: unstructured prose
  (Overview/Features/When-to-use, no fixed Trigger/Procedure/Output
  schema). No numbered rules, zero `source:` citations found in
  inspected skills (`brand-guidelines`, `internal-comms`). No CI/schema
  validation found (`.github/workflows` 404).
- A formal external spec exists at agentskills.io/specification
  (repo's own `spec/agent-skills-spec.md` redirects there) but it does
  not mandate sourcing or a rules schema.
- Sources: https://github.com/anthropics/skills,
  https://raw.githubusercontent.com/anthropics/skills/main/README.md,
  https://raw.githubusercontent.com/anthropics/skills/main/spec/agent-skills-spec.md,
  https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md,
  https://raw.githubusercontent.com/anthropics/skills/main/skills/internal-comms/SKILL.md

## Ecosystem 2 — community Claude-skill collections

Four collections surveyed: two actual skill packs, two curated
link-lists.

- **obra/superpowers** —
  https://github.com/obra/superpowers — 275,873 stars, MIT, updated
  daily. ~14 skills, purely SWE-process (TDD, code review, git
  worktrees, parallel-agent dispatch). Minimal frontmatter (`name` +
  one-line `description`), free-form prose body, imperative rules with
  zero external citations. `.pre-commit-config.yaml` only lints a
  Python `evals/` subdir, not skill files; no schema/citation CI.
- **ComposioHQ/awesome-claude-skills** —
  https://github.com/ComposioHQ/awesome-claude-skills — 73,001 stars,
  Apache-2.0, ~28 hosted skills (productivity/ops automation, light
  marketing/design), also markets Composio's MCP Gateway. Ad hoc
  section headers, no axis/citation formalism, no schema CI.
- **VoltAgent/awesome-agent-skills** —
  https://github.com/VoltAgent/awesome-agent-skills — 30,849 stars,
  MIT, pure link-index (no skill files of its own), aggregates vendor
  skills (Stripe, Cloudflare, Figma, etc.). Publishes a "Skill Quality
  Standards" checklist (progressive disclosure, keyword-matchable
  description, <500 lines) as contributor guidance, not enforced by
  tooling.
- **karanb192/awesome-claude-skills** —
  https://github.com/karanb192/awesome-claude-skills — 495 stars, MIT,
  link-index re-pointing mostly to obra/superpowers and
  anthropics/skills; only tooling found across all four is
  `validate-links.yml` (link liveness, not content quality).
- Cross-cutting: none of the four has an axis field, a
  `rule_count_floor`, a fixed Trigger/Procedure/Output schema, or
  per-rule `source:` citation. Coverage skews SWE-process and
  dev-tooling/productivity automation, not the ~43 cross-functional
  disciplines this repo covers.
- Sources: https://github.com/obra/superpowers,
  https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md,
  https://github.com/ComposioHQ/awesome-claude-skills,
  https://github.com/ComposioHQ/awesome-claude-skills/blob/main/mcp-builder/SKILL.md,
  https://github.com/VoltAgent/awesome-agent-skills,
  https://github.com/karanb192/awesome-claude-skills

## Ecosystem 3 — agents.md / .cursorrules

- **AGENTS.md** — https://agents.md/, reference repo
  https://github.com/openai/agents.md (MIT); donated Dec 2025 to the
  Linux Foundation's Agentic AI Foundation. >60,000 repos reportedly
  use it, 20+ agent tools support it. Single Markdown file at repo
  root (optionally nested per subdir), **no required schema**, no
  frontmatter, no trigger/scoping mechanism beyond path nesting, no
  citation discipline, no validation tooling. Flat, always-on
  project-config convention scoped to engineering ops knowledge
  (build/test/lint commands, code style) — not a discipline/skill
  system at all.
- **.cursorrules / Cursor Rules** — official docs at
  https://cursor.com/docs; legacy single-file `.cursorrules` deprecated
  ~v0.43 (late 2024) in favor of `.cursor/rules/*.mdc`. Largest
  community collection: https://github.com/PatrickJS/awesome-cursorrules
  — 40.6k stars, CC0-1.0, ~200+ technology-specific rule packs. Real
  structural discipline here: YAML frontmatter with `description`,
  `globs` (file-pattern scoping), `alwaysApply` — four activation modes
  (Always/Agent-judged/Glob-scoped/Manual), closest analogue to our
  axis-triggered dispatch among all ecosystems surveyed. Still: no
  per-rule sourcing requirement, no schema-validation/CI tooling found,
  and coverage is exclusively "how to write code in framework X," never
  cross-discipline professional guidance.
- Sources: https://agents.md/, https://github.com/openai/agents.md,
  https://github.com/PatrickJS/awesome-cursorrules,
  https://cursor.com/docs

## Ecosystem 4 — professional-discipline packs

- **deanpeters/Product-Manager-Skills** —
  https://github.com/deanpeters/Product-Manager-Skills — 6,587 stars,
  license "Other/NOASSERTION" (verify terms before reuse), actively
  maintained, 77 skills. **Closest peer in spirit to this repo.**
  Frontmatter is rich (`name`, `description` with "Use when...",
  `intent`, `type`, `theme`, `best_for`, `scenarios`,
  `estimated_time`); skills cross-reference each other and several
  defer to a shared `autonomous-investigation` meta-protocol for
  question-budget and Fact/Inference/Assumption labeling. Its
  `porters-five-forces` skill requires every force rating to be backed
  by "documented signals... each with URL + label" and explicitly bans
  invented data — source-anchored, but enforced at analysis-time
  (search-and-cite-as-you-go) rather than baked into a pre-vetted
  per-rule citation list; no axis/`rule_count_floor` formalism. Has
  real validation tooling: `validate-skills.sh`,
  `check-skill-metadata.py`, `check-skill-triggers.py`,
  `check-library-drift.py`, `test-a-skill.sh`. Coverage: strategy/PM
  frameworks (porters-five-forces, pestel-analysis, ansoff-matrix,
  jobs-to-be-done, opportunity-solution-tree, competitive-analysis,
  positioning, pricing-advisor, market-landscape-scan, etc.) —
  substantial overlap with this repo's market-analysis/product-discovery/
  marketing/pricing families.
  Source: https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/porters-five-forces/SKILL.md
- **huntsyea/product-skills** —
  https://github.com/huntsyea/product-skills — MIT, 7 stars, 4 skills
  (continuous-discovery, jobs-to-be-done, shape-up, story-mapping).
  Narrow, deep, single-framework-per-skill, attributed to named authors
  once at the top (not per-claim). No condition-matched rule table, no
  validation tooling.
  Source: https://github.com/huntsyea/product-skills/blob/main/skills/jobs-to-be-done/SKILL.md
- Other, shallower packs surfaced but not deep-dived: aakashg/pm-claude-skills
  (MIT, 102 stars, 5 skills),
  pratikshadake/claude-product-management-skills (MIT, 32 stars).
- anthropics/skills confirmed to carry **no** product-management,
  market-strategy, pricing, or business-discipline packs — the gap this
  repo fills relative to Anthropic's own reference set is real.
- Sources: https://github.com/deanpeters/Product-Manager-Skills,
  https://github.com/huntsyea/product-skills,
  https://github.com/aakashg/pm-claude-skills,
  https://github.com/pratikshadake/claude-product-management-skills

## Gap line

Field must-bes this repo already meets: axis-scoped conditional
triggers (closest external analogue: Cursor's glob/description-scoped
`.mdc` rules — narrower, code-only); cross-discipline breadth (no
surveyed ecosystem spans 43 professional-discipline role families —
deanpeters' 77 skills is the broadest non-SWE set found, still PM/
strategy-only); a fixed three-part body schema per skill.

Field must-bes this repo is missing relative to the strongest peer
(deanpeters/Product-Manager-Skills): (1) a shared cross-skill meta-
protocol for runtime evidence discipline (question-budget,
Fact/Inference/Assumption labeling, "do-not-invent" lists) layered on
top of static per-rule citations — ours cites the rule's origin but has
no equivalent live-analysis discipline; (2) repo-local validation
tooling that checks skill metadata/triggers/library-drift
mechanically — no such tooling was confirmed present in this repo
during this survey; (3) skills that cross-reference each other via
relative links to compose into multi-step workflows.
