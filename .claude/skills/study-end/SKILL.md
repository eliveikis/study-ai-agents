---
name: study-end
description: Close a study session — ask what was done, log it in study_plan.md, tick only checkboxes with evidence, update the phase's status and the next-session entry, and commit the plan. Use at the end of a study session.
---

# Study end

Close a study session. Read `study_plan.md`, and `specs/architecture.md` for the progress log's format, the phase statuses and where exercises live. In the plan, write only the progress log, its checkboxes, the phase statuses and the next-session entry: the rest is the human's.

## 1. Ask

In one message, ask for:

- the minutes spent, as the human counts them
- what was done, by activity
- mistakes and open questions
- whether Claude wrote or fixed any code, and which part

Wait for the answers.

## 2. Log

From the answers, append one row for each phase worked on, in the log's format. The first row replaces the log's blank placeholder row.

## 3. Checkboxes

For each unticked checkbox the session's work bears on, tick it only when it has evidence as `.claude/rules/tutoring.md` defines it, and name that evidence in the row. Ask about the rest: say what evidence is missing, and offer to review the human's explanation or story now when the item is one they show.

## 4. Status and budget

- Update the phase's status as `specs/architecture.md` › Progress log defines it.
- Add up the minutes in the phase's rows. Once they pass the phase's budget, ask whether to stop the phase. If the human stops it, the phase is finished: record its unfinished work in the row's next priority, and make that work the next-session entry's first action only when the human says it blocks the next step.

## 5. Next session

Rewrite the next-session entry with the same fields: current phase, first action, timebox, resume references and known blockers. The first action is usually the next unticked activity in the plan.

## 6. Exercise READMEs

Point out any exercise README whose time spent or assistance used is empty or still the template's placeholder.

## 7. Commit

If the current branch (`git branch --show-current`) is `main`, commit `study_plan.md`. List any other uncommitted files (`git status --porcelain`), and commit only those the human confirms, in the same commit, with the subject `Log study session <YYYY-MM-DD>`. On any other branch, say so and leave the commit to the human.
