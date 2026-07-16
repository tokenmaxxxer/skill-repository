---
name: work-in-english
description: >-
  Token-saving language policy for Korean-speaking teams: do all internal and
  repository-bound work in English, and write only the final user-facing
  summary in Korean. Use this skill on EVERY coding task in this project —
  writing code, fixing bugs, refactoring, committing, opening PRs, writing
  docs, or long agentic runs — whenever the user communicates in Korean.
  It governs the language of commit messages, PR titles/bodies, branch names,
  code comments, docstrings, READMEs and design docs, intermediate progress
  updates, and internal reasoning. It does NOT translate or alter the user's
  code or data. Trigger even if the user never mentions language or tokens.
---

# Work in English, Report in Korean

Korean costs ~1.9x the tokens of equivalent English on LLM tokenizers, and
models reason more accurately in English. Engineering exhaust — commits,
comments, progress notes, reasoning — is never read closely by the user, so
writing it in Korean pays that tax for nothing. Route each output by who
reads it: exhaust to English, everything the user reads to natural Korean.

## The rule

Write in **English**: internal reasoning and planning; commit messages, branch
names, PR titles and bodies, issue text; code comments, docstrings, log and
error messages; READMEs, design docs, changelogs — anything that lives in the
repo; intermediate progress updates (one short line each); todo items; test
names.

Write in **Korean**: the final summary at the end of a task — what you did,
what changed, what to check or decide; direct answers to questions the user
asks mid-task; anything the user must read to make a decision (options,
clarifications, blockers); warnings about destructive or irreversible actions.

If in doubt whether the user will read it, use Korean.

## Guards

- **Never announce the policy.** No "코드 주석은 정책에 따라 영어로
  작성했습니다", no unprompted offers to translate docs. Repeated across every
  task, those sentences are themselves the waste this skill removes, and they
  make a routine convention sound like a decision needing approval. The only
  thing that earns a mention is a real project-convention conflict (below) —
  and then exactly one sentence. Never explain your own defaults.
- **Never translate what already exists.** The user's code, comments, data,
  and documents stay as they are unless asked. Match surrounding style when
  editing next to existing Korean — one edit shouldn't leave a file
  half-and-half.
- **Quote, don't translate.** Korean you quote inside English text — a UI
  label you added, a commit you wrote to repo convention, the user's own
  words — stays verbatim.
- **Never thin the Korean report.** The savings come from the English
  internals, not from a shorter deliverable. Make it complete and natural, not
  a translation stub.

## Edge cases

- **User writes in English** — mirror them, reply in English. The Korean
  report only applies when the user works in Korean.
- **Project convention conflicts** — follow the project. If CONTRIBUTING.md or
  the existing git history uses Korean commit messages, write Korean commits
  and flag the conflict in exactly one sentence of the final summary so the
  team can decide.
- **Product content is not engineering exhaust** — UI copy and API errors
  shown to end users follow the product's language, not this policy.
