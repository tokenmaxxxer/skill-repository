---
type: llm
criteria: >-
  Whether the response states that the Nature.com article was NOT directly fetched (it redirected to an idp.nature.com authentication wall) and that the phys.org research summary and ideas.repec.org bibliographic record were the actually-fetched substitutes, and lists all five axis removal rules.
target: last_message
---
Pass only if the response (a) says the Nature.com article page was not
accessible — it redirected to an authentication wall (idp.nature.com) —
and (b) names the actually-fetched substitutes: the phys.org research
summary (phys.org/news/2021-04-brains-opportunities.html) and the
ideas.repec.org bibliographic record, and lists the removal rule in each
of the five axis files (control-selection rule 7, layout-grouping rule 6,
surface-contrast rule 4, navigation-depth rule 5, color-visibility
rule 6). Fail if it claims the Nature.com page was fetched directly,
omits the auth-wall fact, or cannot name the substitute sources.
