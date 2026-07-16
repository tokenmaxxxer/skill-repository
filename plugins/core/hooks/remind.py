#!/usr/bin/env python3
"""Inject a standing reminder that this plugin's skills apply.

Skill descriptions are already always-on, so this adds pressure, not
information: the failure mode it targets is the model reading the task, not
thinking about skills, and answering directly. Two events cover the gap:

  UserPromptSubmit — every turn. SessionStart injects once and gets buried;
    repeating keeps the reminder adjacent to the request being judged.
  SubagentStart    — subagents start cold. They inherit no conversation and
    no earlier injection, so without this they never see the policy at all.
  PreToolUse(Workflow) — workflow scripts spawn agents outside the Agent
    tool, so the guard-agent-model deny path never fires for them; a
    reminder immediately before the Workflow call is the only lever.

The reminder must never list the dispatch catalog — the procedure skills a task
selects among (diagnose-first, fmea, market-recon, ...). It is paid on every
turn, and such a list would be a second place to update on every skill added —
one that rots silently when someone forgets. Claude already has the
descriptions; the reminder only has to force the decision — check whether one
fits, invoke it if so — not re-list them. It frames that check as a mandatory
step, not optional encouragement, because "use them actively" reads as
skippable next to a concrete task; it also bars invoking a skill that does not
fit, so the push cannot degrade into rubber-stamp skill-loading on trivial
work.

Standing policies are the exception to that bar and are inlined verbatim below
(ROUTING, LANGUAGE). They are not dispatch candidates: they govern how every
output is produced, not which procedure a task needs, so the fitness check
cannot surface them — "which skill fits this task?" never answers "write your
progress lines in English." Observed with only the fitness check in place: on a
repo-inspection turn no procedure fit, the check passed correctly, and
work-in-english was never a candidate, so half the turn came out in Korean. The
rot argument that bars the catalog does not reach them either — standing
policies are a fixed pair, not a growing list. Inlining is what makes them
stick: nobody stops mid-sentence to load a skill before choosing a tier or a
language, so the rule itself has to be in front of them.

Every turn is reminded, with no prefilter for greetings or short prompts.
A prefilter only pays off when something expensive (e.g. a subprocess
retrieval) runs behind the gate; this only echoes a constant, so there is
nothing to save. A
prefilter would also be actively wrong here: a bare "응" / "그래" / "네" is how
a Korean user approves work, and that turn is the last injection point before
a long stretch with no further prompts — exactly the one worth keeping.

SubagentStart accepts only the JSON hookSpecificOutput form — plain stdout
fires the hook but reaches nothing (verified empirically; not documented).
UserPromptSubmit accepts either; both use JSON here for one code path.

Dependency-free (Python 3.9+ stdlib). Always exits 0 — a broken reminder must
never block a turn.
"""
from __future__ import annotations

import json
import sys

# Standing policies, injected alongside the skill reminder on every event.
# Each restates its skill's rule instead of just naming it, for the reason in
# the module docstring: the decision they govern is made mid-work, and nobody
# pauses mid-sentence to load a skill.
#
# Model routing — one constant, three surfaces: the main loop (every user
# turn), subagents (they start cold and route their own children), and Workflow
# calls (their agent() spawns bypass the Agent-tool guard entirely, so a
# pre-call reminder is the only lever).
ROUTING = (
    "Model routing (see the model-routing skill): run each agent task on the "
    "tier that fits it — mechanical work (production briefs, search, "
    "fetch/extract, bulk edits) on `sonnet` (core:executor), hard bounded "
    "judgment on `opus` (core:reasoner); keep orchestration and synthesis "
    "at the session tier. Never let mechanical fan-out inherit an expensive "
    "tier."
)

# Language — split by who reads the output, so the two surfaces need different
# rules rather than one shared constant. In the main loop the user reads the
# final answer, so that much is Korean. A subagent's final message is a tool
# result read by the orchestrator, which makes it exhaust like everything else;
# telling a subagent to "report in the user's language" would buy a Korean
# report that no user ever sees, and that the orchestrator has to rewrite.
LANGUAGE = (
    "Language (see the work-in-english skill): write engineering exhaust in "
    "English — internal reasoning, progress lines, commit messages, branch "
    "names, code comments, and repo-bound docs. Write in the user's language "
    "only what the user reads: the final summary, direct answers, blockers, "
    "and warnings. Never announce the policy; never translate what already "
    "exists."
)

SUBAGENT_LANGUAGE = (
    "Language (see the work-in-english skill): work AND report in English. "
    "Your final message is a tool result read by the orchestrator, not by the "
    "user, so it is exhaust like the rest — do not close with a Korean "
    "summary; the orchestrator writes the user's Korean. The exception is "
    "content you are asked to author for a human reader: match the language "
    "of the target file or brief, and keep quoted Korean verbatim."
)

REMINDER = (
    "The skill-registry (core) skills are active. Before answering, decide "
    "explicitly whether one fits THIS task — if so, invoke it with the Skill "
    "tool before answering rather than working from memory; if none genuinely "
    "fits, proceed. Make this check every turn, and never invoke a skill that "
    "does not fit. " + ROUTING + " " + LANGUAGE
)

SUBAGENT_REMINDER = (
    "The skill-registry (core) skills are active. You are a subagent and "
    "inherit no conversation context, so nothing else will surface them. "
    "Before starting work, decide explicitly whether one fits your brief and "
    "state your choice in one line (the skill you will use, or 'none fits'); "
    "if one fits, invoke it with the Skill tool before proceeding. Never "
    "invoke a skill that does not fit your brief. " + ROUTING + " "
    + SUBAGENT_LANGUAGE
)

WORKFLOW_REMINDER = (
    "Workflow skills + model routing + language. Skills: workflow agents are "
    "spawned by the script and may not receive the subagent skill reminder, so "
    "bake it into each agent() prompt — instruct every agent to first decide "
    "whether a registry skill fits its brief and invoke it before working. "
    "Language: bake that in too — workflow agents return data to the script, "
    "never a report a user reads, so every agent() prompt, label, and schema "
    "description stays English, and so does whatever the agent returns. Model "
    "routing: agent() calls inside workflow scripts inherit the session model "
    "unless the script says otherwise, and the Agent-tool guard cannot see "
    "them. Before launching, confirm the script sets model: 'sonnet' (add "
    "effort: 'low' where it fits) on mechanical stages — search, "
    "fetch/extract, bulk transforms — and reserves the session tier for "
    "judgment stages (scope, verify, synthesize). If the script lacks these "
    "overrides, edit it first (e.g. use the deep-research-tiered variant "
    "instead of deep-research)."
)


def emit(event: str, context: str) -> None:
    json.dump(
        {"hookSpecificOutput": {"hookEventName": event,
                                "additionalContext": context}},
        sys.stdout,
        ensure_ascii=False,
    )


def main() -> int:
    if "--subagent" in sys.argv:
        emit("SubagentStart", SUBAGENT_REMINDER)
    elif "--workflow" in sys.argv:
        emit("PreToolUse", WORKFLOW_REMINDER)
    else:
        emit("UserPromptSubmit", REMINDER)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # never block a turn
