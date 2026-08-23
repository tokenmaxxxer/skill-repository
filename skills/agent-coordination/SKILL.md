---
name: agent-coordination
description: >-
  Use when multiple agents are writing to the same repo concurrently — when an agent starts
  work on a shared repo or detects a write-set collision mid-task. In-flight coordination
  protocol for AI agents sharing a git repository: file-based claim registration, conflict
  detection, heartbeat monitoring, structured negotiation via the ".agents/" directory, and
  unilateral resolution on timeout — the operational bridge between parallel-decomposition
  (pre-flight cut) and merge-gates (landing checks). Trigger on "에이전트끼리 충돌 안 나게 조율해줘", "two
  agents are editing the same files", "claim this file set before working". Do NOT use for
  read-only research fan-out, for single-agent tasks, or to replace parallel-decomposition
  or merge-gates — this skill does not cut the work and does not design landing gates; it
  keeps agents from stepping on each other while they work.
---

# Agent Coordination

## First: does this even need the procedure?

- **Is there more than one agent writing to this repo?** If only one agent has write access, there is nobody to coordinate with. Exit.
- **Is the work already cut by `parallel-decomposition`?** If not, decomposition runs first — this skill assumes pieces exist and contracts are frozen.
- **Are the agents read-only?** Research sweeps and source gathering don't collide. This skill is only for agents that produce commits.

Everything below applies when 2+ agents are actively writing to one repo.

## Where this skill fits

This skill is the middle layer in a three-skill pipeline:

```
parallel-decomposition          agent-coordination           merge-gates
    (pre-flight)                   (in-flight)                (landing)
    cuts the work,                 claims, heartbeats,        designs the gate
    freezes contracts              conflict resolution,       that main requires
                                   self-merge
```

- **Before fan-out:** `parallel-decomposition` cuts the work and freezes shared identifiers. Every agent receives a write set and a contract.
- **During work:** this skill. Agents register claims, monitor for conflicts, negotiate resolutions, and merge themselves when done.
- **When landing:** `merge-gates` defines what must pass before a merge is accepted. The self-merge in Step 6 satisfies the combined-state requirement by rebasing before pushing. If the repo has additional gate infrastructure (CI, merge queue), those gates apply on top.

## When this skill says stop

- **Deadlock after 3 negotiation rounds** → escalate, don't spin.
- **Three conflicts on the same file in one session** → the decomposition is wrong. Stop, flag to orchestrator, re-cut with `parallel-decomposition`.
- **Heartbeat of every other agent is stale** → coordination bus may be the problem, not the agents. Check connectivity.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 2.1 — Read `.agents/claims.json`. If the file does not exist, create it with an empty `agents` object
- 2.2 — Add your entry: `agent-id` (unique per agent), `branch`, `status: "starting"`, `write_set` (files you will write, from the `parallel-decomposition` contract), `started`…
- 2.3 — Push this commit alone, on your branch, before any code change. If the push fails (someone else pushed first), pull, re-read claims, re-check for conflicts, re-push
- 2.1(2) — **Update heartbeat.** Set `heartbeat` to now. This is the signal that you are alive
- 2.2(2) — **Pull remote.** Get the latest `claims.json` and `conflicts/`
- 2.3(2) — **Scan claims.** For every other agent with `status: "in-progress"` or `status: "waiting"`: - Compare their `write_set` against yours. Any overlap? - If overlap exists A…
- 2.4 — **Scan conflicts.** Read every file in `conflicts/` where you are named as `other_agent`. If any have `status: "waiting"` → go to Step 3 (respond)
- 2.5 — **Do one unit of work.** One commit, one test run, one file edit. Then loop back to Step 1.1
- 2.1(3) — Create `.agents/conflicts/<id>.md` where `<id>` is `conflict-<your-agent-id>-<their-agent-id>-<filename-slug>`
- 2.2(3) — Write the conflict file:
- 2.3(3) — Set your own `status` in `claims.json` to `"waiting"`
- 2.4(2) — Commit the conflict file AND the claims.json update. Push
- 2.1(4) — Read the detector's `my_change` and `my_progress`
- 2.2(4) — Assess the collision: - **Different regions of the same file, no semantic conflict** → propose parallel work. Append to the conflict file: `resolution: parallel — edits…
- 2.3(4) — Commit the updated conflict file. Push
- S1 — The infrastructure → references/rules.md
- S2 — Standing rules → references/rules.md
- S3 — Evidence grade → references/rules.md
