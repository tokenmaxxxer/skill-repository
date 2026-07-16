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

The reminder must never name individual skills. It is paid on every turn, and
a list here would be a second place to update on every skill added — one that
rots silently when someone forgets. Claude already has the descriptions; the
reminder only has to force the decision — check whether one fits, invoke it if
so — not re-list them. It frames that check as a mandatory step, not optional
encouragement, because "use them actively" reads as skippable next to a
concrete task; it also bars invoking a skill that does not fit, so the push
cannot degrade into rubber-stamp skill-loading on trivial work.

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

# Model-routing policy, injected alongside the skill reminder on every event.
# One constant, three surfaces: the main loop (every user turn), subagents
# (they start cold and route their own children), and Workflow calls (their
# agent() spawns bypass the Agent-tool guard entirely, so a pre-call reminder
# is the only lever). Deliberately restates the model-routing skill's rule
# instead of just naming it — a subagent deciding a tier mid-brief won't stop
# to load a skill, so the rule itself must be in front of it.
ROUTING = (
    "Model routing (see the model-routing skill): run each agent task on the "
    "tier that fits it — mechanical work (production briefs, search, "
    "fetch/extract, bulk edits) on `sonnet` (core:executor), hard bounded "
    "judgment on `opus` (core:reasoner); keep orchestration and synthesis "
    "at the session tier. Never let mechanical fan-out inherit an expensive "
    "tier."
)

REMINDER = (
    "The skill-registry (core) skills are active. Before answering, decide "
    "explicitly whether one fits THIS task — if so, invoke it with the Skill "
    "tool before answering rather than working from memory; if none genuinely "
    "fits, proceed. Make this check every turn, and never invoke a skill that "
    "does not fit. " + ROUTING
)

SUBAGENT_REMINDER = (
    "The skill-registry (core) skills are active. You are a subagent and "
    "inherit no conversation context, so nothing else will surface them. "
    "Before starting work, decide explicitly whether one fits your brief and "
    "state your choice in one line (the skill you will use, or 'none fits'); "
    "if one fits, invoke it with the Skill tool before proceeding. Never "
    "invoke a skill that does not fit your brief. " + ROUTING
)

WORKFLOW_REMINDER = (
    "Workflow skill + model routing. Skills: workflow agents are spawned by "
    "the script and may not receive the subagent skill reminder, so bake it "
    "into each agent() prompt — instruct every agent to first decide whether "
    "a registry skill fits its brief and invoke it before working. Model "
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
