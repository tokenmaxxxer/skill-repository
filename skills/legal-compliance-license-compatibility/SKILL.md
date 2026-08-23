---
name: legal-compliance-license-compatibility
description: Use when adding, auditing, or replacing an open-source dependency and its license must be checked for compatibility with the project's own license.
metadata:
  axis: oss-license-compatibility
  rule_count_floor: 2
---

# Open-source license compatibility

Decision rules for whether a dependency's license can be combined into
the product being reviewed, sourced live during issue #1174's
legal-compliance research pass (2026-08-13).

## Trigger

Apply this skill when a new dependency, vendored asset, or bundled
component is being added or audited and its license's compatibility
with the project's own license is the open question — distinguishing it
from the other legal-compliance axes, which govern personal-data
handling rather than dependency licensing.

## Procedure

1. If the dependency is permissive (MIT/Apache-2.0) and the project is
   not GPL-only, allow it (rule 1).
2. If any GPL dependency is added, treat the whole distributed combined
   work as GPL from that point (rule 2).
3. For an Apache-2.0 dependency entering a strict GPLv2 project, pick a
   different dependency or upgrade the project's license first (rule 3).
4. If two GPL components at incompatible major versions are both
   required, remove one or replace it with a dual-licensed/"or-later"
   alternative (rule 4).
5. For any vendored third-party code or bundled asset, check its
   license individually rather than assuming the top-level LICENSE
   covers it (rule 5).

## Output shape

A per-dependency compatibility verdict (allow / block / replace) citing
the triggering rule, and — when rule 5 applies — a per-component license
list distinct from the top-level LICENSE file.

## Decision rules

1. When a dependency is licensed MIT or Apache-2.0 (permissive) and the
   project it's entering is not itself GPL-licensed, pick it freely —
   permissive licenses can be combined into almost any project without
   forcing a license change on the whole work.
   source: Milvus OSS license-compatibility explainer (fetched
   2026-08-13, https://milvus.io/ai-quick-reference/what-are-license-compatibility-issues-in-open-source):
   "MIT and Apache-2.0 are permissive licenses and can generally be
   combined with many other licenses without any problems."
   counter-example: an Apache-2.0 dependency entering a GPLv2-only
   project is the one common exception — GPLv2 rejects Apache-2.0's
   patent clause, so this specific pair needs rule 3 below, not this
   default-permissive rule.

2. When any GPL-licensed dependency (GPLv2 or GPLv3) is added to a
   project, treat the entire distributed combined work as GPL from that
   point forward — do not assume the GPL scope stays contained to just
   that one dependency's own files.
   source: credativ GPL/MIT/Apache comparison (fetched 2026-08-13,
   https://www.credativ.de/en/blog/credativ-inside/understanding-open-source-licenses-gpl-mit-apache-compared/):
   "GPL licenses are copyleft, meaning that as soon as GPL code is
   combined, the entirety must be distributed under GPL."
   counter-example: a GPL tool invoked only as a separate out-of-process
   CLI (not linked/combined into the distributed binary) does not
   propagate copyleft to the calling project under the standard
   "mere aggregation" reading — verify the actual linkage/distribution
   boundary before applying this rule, not just co-presence in the repo.

3. When considering an Apache-2.0 dependency for a GPLv2 project
   specifically, pick a different (non-Apache) dependency or upgrade the
   project's own license to "GPLv2-or-later"/GPLv3 first — do not add
   the Apache-2.0 dependency to a strict GPLv2-only project as-is.
   source: Mend Apache License FAQ (fetched 2026-08-13,
   https://www.mend.io/blog/top-10-apache-license-questions-answered/),
   corroborated by credativ (https://www.credativ.de/en/blog/credativ-inside/understanding-open-source-licenses-gpl-mit-apache-compared/):
   "Apache-2.0 is compatible with GPLv3, but not with GPLv2, as GPLv2
   does not accept the Apache-2.0 patent clause."
   counter-example: if the GPLv2 project's own license text already
   includes the "or (at your option) any later version" clause, treat
   it as GPLv3-eligible and the Apache-2.0 dependency becomes
   compatible under that later-version option.

4. When a dependency audit finds two GPL-licensed components at
   different major versions (GPLv2-only and GPLv3-only) both required in
   the same distributed work, remove one of them (or replace it with a
   dual-licensed / "or-later" alternative) rather than shipping both —
   GPLv2 and GPLv3 are not mutually combinable without the "or later"
   escape hatch.
   source: credativ (fetched 2026-08-13,
   https://www.credativ.de/en/blog/credativ-inside/understanding-open-source-licenses-gpl-mit-apache-compared/):
   "GPLv2 and GPLv3 are not mutually compatible, unless a project uses
   the 'v2 or later' option."
   counter-example: none — this is a hard incompatibility per the same
   source outside the "or later" escape hatch; there is no safe way to
   ship both GPLv2-only and GPLv3-only code combined in one work.

5. When a repository bundles vendored third-party code, embedded fonts,
   or other assets distinct from the project's own source, check each
   bundled component's license individually — do not assume a single
   top-level LICENSE file covers everything actually shipped in the
   distribution.
   source: REUSE specification summary (fetched 2026-08-13,
   https://reuse.software/): compliance is achieved "using
   industry-standard System Package Data Exchange (SPDX) tags" applied
   per file, "each file needs just two tags, one for copyright and one
   for licensing" — a per-component model, not a single repo-wide
   declaration.
   counter-example: a monorepo where every file was authored under one
   license and no third-party code is vendored in has no divergent
   component to check — the single top-level LICENSE file is accurate
   in that case, and this rule adds no work.
