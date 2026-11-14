---
name: study-start
description: Open a study session — state the current phase, the first action and its target time from study_plan.md, and time the activity if asked. Use at the start of a study session, or when asked what to study next.
---

# Study start

Open a study session. Read `study_plan.md` (its phase overview, progress log and next-session entry), and `specs/architecture.md` for where notes and exercises live and the progress log's format. Change no files but `current_activity.md` (section 1).

## 1. What's next

State the current phase and the target time from the next-session entry. Name the first action as `p<phase>a<n>: <title>`, where n is its position in the phase's activity list, such as `p1a4: Rehearse a short Repocop story`. Then quote the plan's text for the activity it names word for word, sub-items included: don't reword or shorten it. Then give the content of each file or section the activity links to that the work depends on, such as an input format or a sample, so the human can start without opening another file. If the latest log row's next priority says something else, mention it too.

Write the same content to `current_activity.md` at the repository root, replacing any earlier one, so the human can reread it outside the session. In order: the date and that it comes from the plan's next-session entry, the phase and target time, the activity's text, without its checkbox, under a heading that names it the same way, then the linked content, saying so when there is none. If the human moves on to another activity later in the session, rewrite the file for that one.

## 2. Timing

When the human says the activity is timed, read the clock (`date`) and say the start time. When they say they're done, read it again and report the minutes elapsed.
