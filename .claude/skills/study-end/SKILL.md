---
name: study-end
description: Close a study session — log what was done in study_plan.md, from the human's answers or what the session shows, tick only checkboxes with evidence, update the phase's status and the next-session entry, and commit the plan. Use at the end of a study session.
---

# Study end

Close a study session. Read `study_plan.md`, and `specs/architecture.md` for what a session may write in the plan, the progress log's format, the phase statuses and where exercises live.

## 1. Ask

Fill in each of these from what the session shows:

- the minutes spent, as the human counts them
- what was done, by activity
- mistakes and open questions
- whether Claude wrote or fixed any code, and which part

In one message, show them and ask the human to correct or complete them, with section 4's question if the phase is over budget. Ask once. If the reply doesn't answer, or the human moves on, go on with what you have. For minutes, use what the human reported during the session, or your estimate, and say in the row which it is.

## 2. Log

From the answers, or what the session shows where there are none, append one row for each phase worked on, in the log's format. The first row replaces the log's blank placeholder row.

## 3. Checkboxes

For each unticked checkbox the session's work bears on, tick it only when it has evidence as `.claude/rules/tutoring.md` defines it, and name that evidence in the row. For the rest, say in your closing message what evidence is missing, and offer to review the human's explanation or story when the item is one they show. Don't wait on it.

## 4. Status and budget

- Update the phase's status as `specs/architecture.md` › Progress log defines it.
- Add up the minutes in the phase's rows. Once they pass the phase's budget, ask whether to stop the phase, in section 1's message. Without an answer, the phase stays open. If the human stops it, the phase is finished: record its unfinished work in the row's next priority, and make that work the next-session entry's first action only when the human says it blocks the next step.

## 5. Next session

Rewrite the next-session entry with the same fields: current phase, first action, timebox, resume references and known blockers. The first action names one activity by its title as the plan gives it, usually the next unticked one, with at most a note on where to resume within it. Don't restate the activity's text: the plan holds it.

## 6. Exercise READMEs

Point out any exercise README whose time spent or assistance used is empty or still the template's placeholder.

## 7. Commit

If the current branch (`git branch --show-current`) is `main`, commit `study_plan.md`. Commit, in the same commit, the files this session's work produced or changed, with the subject `Log study session <YYYY-MM-DD>`. List any other uncommitted files (`git status --porcelain`) without committing them. On any other branch, say so and leave the commit to the human.
