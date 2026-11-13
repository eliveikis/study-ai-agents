# Product — study-ai-agents

Root design file. It covers *why* this repository exists and for whom; *how* it's put together is in [architecture.md](architecture.md).

## Purpose

A workspace for working through [study_plan.md](../study_plan.md), the preparation plan for a Senior AI Engineer (AI tools) interview, without deciding each session where work goes or how to record it. It gives each kind of study work a fixed place, a Python project to write and check code in, a tutor that teaches without doing the work, and routines that open and close each session by the plan's own working rules.

## Audience

One learner: an experienced engineer whose Python is rusty, working through the plan in sessions of an hour or a few, with Claude Code as tutor and reviewer.

## Design pillars

Ranked: when two conflict, the higher one wins.

1. **Independent ability stays measurable.** First attempts are written without AI before any review, and each exercise and session records the assistance used.
2. **`study_plan.md` is the only progress record, and what it claims has evidence.** A checkbox is ticked, or a phase's status advanced, only on evidence in the repository.
3. **Working code and recorded results come before infrastructure.**
4. **A session takes little ceremony.** Opening and closing a session is one command each.

## Scope

The phases, budget, completion evidence and the evaluation project's scope limits are in [study_plan.md](../study_plan.md).
