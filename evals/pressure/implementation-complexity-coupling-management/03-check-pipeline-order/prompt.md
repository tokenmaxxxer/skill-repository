---
name: implementation-complexity-coupling-management--check-pipeline-order
---
We are setting up a local pre-merge script for our Python monorepo. The
candidate checks, with rough timings on a typical change:

- `black --check` on touched files (~2s), formatting only
- `isort --check` on touched files (~2s), import order (black's profile
  already covers the same import-format violations via `ruff` below)
- `ruff` on touched files (~3s), lint incl. formatting + import-order rules
- `mypy` full-repo (~90s)
- full test suite (~4min)

A teammate proposes running them in the order mypy → tests → ruff →
black → isort, arguing "the expensive checks matter most so run them
first, and keeping all five tools is safest since more checks means more
coverage." Write the recommended pipeline (which tools, in what order)
and justify it.
