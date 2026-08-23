---
name: model-routing--reasoner-fanout-tier
---
You are the session orchestrator on a mid-tier model, deciding how to answer:
"Which of these 12 candidate open-source libraries is safe to adopt for our
PDF pipeline?" Your tooling spawns subagents that, by default, run on the
caller's model; per-subagent model selection is NOT supported. Your plan
draft: send one brief to a top-tier reasoner subagent saying "investigate all
12 libraries — search advisories, fetch maintainer activity, read changelogs,
then rank them," letting it spawn whatever scout subagents it needs.

A colleague says this is efficient because "it's a single expensive call —
one reasoner, one brief." Evaluate the plan: what is wrong with it cost-wise,
and how do you restructure the delegation?
