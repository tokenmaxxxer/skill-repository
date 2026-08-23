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

## The infrastructure

Every shared repo carries an `.agents/` directory at its root. This is the coordination bus — no server, no queue, no API. Agents read and write markdown and JSON files.

```
.agents/
├── claims.json          # All active agents, their write sets, status, heartbeat
├── conflicts/            # Detected write-set collisions
│   └── <id>.md          # Negotiation thread per conflict
└── resolutions/          # Closed conflicts with verdict and rationale
```

All files in `.agents/` are committed to the repo. An agent that pulls reads the current coordination state from the same git history as the code. An agent that pushes writes its coordination state alongside its code changes.

## The work loop (applies to every agent)

Before starting any task, every agent must register. After registration, work proceeds in a monitoring loop that weaves coordination checks between units of productive work.

### Step 0 — Register

1. Read `.agents/claims.json`. If the file does not exist, create it with an empty `agents` object.
2. Add your entry: `agent-id` (unique per agent), `branch`, `status: "starting"`, `write_set` (files you will write, from the `parallel-decomposition` contract), `started` (ISO timestamp), `heartbeat` (ISO timestamp, same as `started` initially).
3. Push this commit alone, on your branch, before any code change. If the push fails (someone else pushed first), pull, re-read claims, re-check for conflicts, re-push.

**Gate:** your entry appears in `claims.json` on the remote. If you cannot register, do not start work — the coordination bus is unreachable.

### Step 1 — Enter the work loop

After every unit of productive work (one file edit, one test run, one commit — not every keystroke), run this loop:

1. **Update heartbeat.** Set `heartbeat` to now. This is the signal that you are alive.
2. **Pull remote.** Get the latest `claims.json` and `conflicts/`.
3. **Scan claims.** For every other agent with `status: "in-progress"` or `status: "waiting"`:
   - Compare their `write_set` against yours. Any overlap?
   - If overlap exists AND your change to the overlapping file is not yet committed → go to Step 2 (detect conflict).
   - If no overlap OR your change is already committed and you're done with that file → continue.
4. **Scan conflicts.** Read every file in `conflicts/` where you are named as `other_agent`. If any have `status: "waiting"` → go to Step 3 (respond).
5. **Do one unit of work.** One commit, one test run, one file edit. Then loop back to Step 1.1.

**Gate:** the heartbeat is never more than 15 minutes stale. A heartbeat older than 15 minutes signals a stalled or dead agent.

### Step 2 — Detect and report a conflict

When your scan finds a write-set overlap with another agent:

1. Create `.agents/conflicts/<id>.md` where `<id>` is `conflict-<your-agent-id>-<their-agent-id>-<filename-slug>`.
2. Write the conflict file:

```markdown
# conflict: <overlapping file>
- detector: <your-agent-id>
- other_agent: <their-agent-id>
- detected_at: <ISO timestamp>
- type: write-set-overlap
- my_change: "<one sentence describing what you need to change in this file>"
- my_progress: "<already committed | in progress, not committed | not started>"
- status: waiting
```

3. Set your own `status` in `claims.json` to `"waiting"`.
4. Commit the conflict file AND the claims.json update. Push.

**Gate:** the conflict file exists on the remote. Your status is `"waiting"`. You do not touch the overlapping file until this conflict is resolved.

### Step 3 — Respond to a conflict directed at you

When you find a conflict file naming you as `other_agent` with `status: "waiting"`:

1. Read the detector's `my_change` and `my_progress`.
2. Assess the collision:
   - **Different regions of the same file, no semantic conflict** → propose parallel work. Append to the conflict file: `resolution: parallel — edits are to different sections of <file>; both can proceed.` Set `status: resolved-parallel`.
   - **Same region, but your change is smaller/trivial** → yield. Append: `resolution: yield — <your-agent-id> will drop/pause <file>; rationale: <why yours is smaller>.` Set `status: resolved-yield`. Remove the file from your `write_set` in `claims.json`.
   - **Same region, both changes are significant** → negotiate. Append: `resolution: negotiate — <your-agent-id> proposes: <concrete proposal for how to sequence or split>.` Set `status: negotiating`.
   - **You haven't started that file yet** → yield preemptively. It costs nothing.
3. Commit the updated conflict file. Push.

**Rule for deciding who yields:** the agent whose change to the overlapping file requires fewer lines to implement (estimated) yields. This is the cheapest-to-revert heuristic — not a judgment about whose work is more important. If both changes are similar in size, the agent whose `started` timestamp is earlier keeps the file; the later agent yields.

**Gate:** the conflict file's `status` is no longer `"waiting"`. If the status changed to `resolved-*`, both agents resume their work loop. If `negotiating`, continue to Step 4.

### Step 4 — Negotiate

When a conflict is in `negotiating` status, both agents write proposals into the same conflict file. The file becomes a structured thread:

```markdown
## proposal: <agent-id> (timestamp)
<concrete proposal>

## counter: <other-agent-id> (timestamp)
<response to proposal>
```

Negotiation ends when one agent yields or a sequence is agreed:

- `resolution: serialize — <agent-A> will complete <file> first; <agent-B> waits and rebases.`
- `resolution: split — <file> will be split into <sub-file-A> and <sub-file-B>; each agent takes one.`
- `resolution: yield — <agent> drops the file.`

**Gate:** every negotiation round moves the status or the content. Three rounds with no resolution → escalate to the orchestrator by writing `escalation: deadlock after 3 rounds` and setting `status: deadlocked`. Both agents halt work on the overlapping file and move to non-overlapping work if possible. Do not spin.

### Step 5 — Timeout and unilateral resolution

When you are blocked waiting on another agent (your status is `"waiting"`):

1. On each loop iteration, check their `heartbeat` in `claims.json`.
2. If their heartbeat is older than **30 minutes** from now:
   - They are presumed dead or disconnected.
   - You may resolve unilaterally.
3. Append to the conflict file: `resolution: timeout — <your-agent-id> resolves unilaterally; <their-agent-id> heartbeat is <N> minutes stale.`
4. Set `status: resolved-timeout`.
5. Set your own status back to `"in-progress"`.
6. Move the conflict file to `.agents/resolutions/<id>.md`.
7. Commit and push.

**Gate:** the timeout is measured, not guessed. The exact heartbeat age is written into the resolution. If the other agent later revives, the resolution file is the audit record for why you proceeded without them.

### Step 6 — Self-merge to main

When your task is complete — all intended changes committed, all your conflicts resolved — you merge your own branch to main. Do not wait for an orchestrator; that creates a central bottleneck that defeats the parallelism.

1. **Verify clean state.** No unresolved conflicts remain. Your status in `claims.json` is `"in-progress"` (not `"waiting"`).
2. **Pull and integrate.** `git fetch origin main && git rebase origin/main`. This brings in every other agent's work that landed on main while you were working.
3. **Resolve rebase conflicts.** If rebase surfaces conflicts:
   - These are landing-stage collisions, not in-flight ones — the other agent's work is already on main.
   - Resolve them yourself if the conflicts are trivial (your change and theirs don't interact semantically).
   - If the conflict is non-trivial, create an emergency conflict file in `.agents/conflicts/merge-<your-agent-id>.md`, set your status to `"merging"`, and negotiate per Steps 3–4. This is the one case where conflict resolution happens at landing time rather than in-flight — the other agent may already be done and unregistered.
4. **Push to main.** `git push origin main`. This is a fast-forward push — you just rebased, so your branch tip should be directly ahead of origin/main.
   - **If the push is rejected** (non-fast-forward): another agent pushed to main while you were rebasing. Pull, rebase again, retry. Each retry updates your heartbeat. Do not force-push to main — the rejection means someone else's work landed first and you must integrate it.
   - **If the push succeeds:** your work is on main.
5. **Mark complete.** Set `status: "complete"` in `claims.json`. Move any remaining conflict files to `.agents/resolutions/`. Update `heartbeat` one final time. Commit and push this final coordination update.
6. **Clean up.** Delete your feature branch locally and on the remote. Your work is done.

**Gate:** your `claims.json` entry shows `status: "complete"`. Your commits are on main. Your branch is deleted. Your conflict files are in `resolutions/`.

**Merge race protocol.** Two agents cannot fast-forward to main simultaneously — git rejects the second push. This is not a bug; it is the serialization point. The agent whose push was rejected must pull, rebase, and retry. The rejected agent owns the integration burden: they must reconcile their work with whatever landed while they were pushing. This is fair — the agent that finishes first gets the clean path; the agent that finishes second does the integration work. Do not negotiate who goes first; git decides.

## The coordination files as audit record

The `.agents/` directory is committed to the repo. Every claim, conflict, negotiation, and resolution is in git history. This serves three purposes:

1. **Debugging:** when the union breaks, the coordination trail shows which agent touched what, who yielded to whom, and why.
2. **Post-hoc review:** an orchestrator (human or AI) can replay the coordination timeline to understand what happened.
3. **Learning:** patterns of frequent conflicts on the same files signal that `parallel-decomposition`'s cut was wrong — those files should have been a single piece or the contract should have been frozen differently.

## Standing rules

- **The repo is the bus.** An agent that doesn't push doesn't exist to other agents. Push coordination changes frequently — at minimum, every heartbeat update.
- **Heartbeat is the liveness signal.** No heartbeat = dead. 30 minutes is the default; tune it by task granularity (shorter for fast tasks, longer for deep analysis work).
- **Work small, commit small.** Large commits that touch many files create broader write sets and more conflicts. Each commit should touch the fewest files possible.
- **Yield early.** The cheapest time to yield is before you've written any code. If you detect a conflict and haven't started the overlapping file, yield immediately — don't wait for negotiation.
- **Write the rationale.** Every resolution records why. "I yielded because" or "I proceeded because heartbeat stale." Future agents (and future you) need to understand the decision.
- **You merge yourself.** Each agent merges its own branch to main when done. No central merge master. The merge race (two agents pushing main simultaneously) is resolved by git itself: the second push is rejected, the rejected agent rebases and retries.
- **Rebase before merge, always.** The rebase in Step 6.2 is the combined-state requirement from `merge-gates` Step 3, applied operationally. An agent that pushes without rebasing first may break main if another agent's work landed in the meantime. The push rejection is the safety net, but the rebase is the first line of defense.

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

## Evidence grade

This skill draws on distributed systems primitives (lease-based liveness, file-based coordination, the "cheapest-to-revert" conflict heuristic from optimistic concurrency) but has no direct experimental evidence that AI agents following this protocol produce fewer defects or faster completion than uncoordinated agents. The premise that structured coordination beats ad-hoc conflict resolution is an engineering assumption, not a measured outcome. State this plainly when the protocol is introduced to a new repo.
