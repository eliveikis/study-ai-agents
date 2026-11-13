# P2A1 — Define the branch experiment

Use 10–20 minutes to study the material below. The full activity has a 60-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Specify what would count as success

An experiment question identifies a change and a measurable consequence. Here the change is the branch section of the implement skill. The consequence is whether the agent works on the correct requirement after a branch changes outside its session. A scenario describes the starting conditions. A trial is one execution of a scenario under one configuration. A grader measures the result using evidence it controls.

| Scenario | Runner action after previous turn | Required final behavior |
| --- | --- | --- |
| S1 | Switch from completed old-task to existing new-task | Implement new-task on its branch |
| S2 | Stay on new-task after reading its requirement | Implement the same task there |
| S3 | Move from new-task to main; supply requirement path | Switch back and implement there |
| S4 | Move from old-task to main; leave an uncommitted file; supply path | Stop on main and preserve all state |

A **control** is a condition where you expect no difference between configurations. If a difference shows up there, the change has a side effect, or the setup is wrong. S2 is the control here.

## Design the fixture before the run

Use a disposable repo and a local bare origin with its HEAD set so the skill can discover the default branch. Pin fixture commits and snapshot uncommitted changes. Give both configurations the same previous turn within each scenario. Keep the session alive across the external switch. Start a fresh session for each independent trial.

To show that something *didn't* change, you need a record of what it was before: a commit SHA for committed state, and a saved copy or hash of anything uncommitted. A grader can then compare the final state with that record.

For each scenario write down the final branch, required behavior and allowed changes. Keep acceptance checks outside the agent's write access. Separately record whether a branch check preceded switches or edits and whether checks ran before the first edit. Those trace observations explain the path to the result.

## Decide before you look

Write the decision rule before examining any results: which outcomes would make you keep, change or drop the new wording. A rule written after seeing the data tends to fit whatever the data happened to show.

Save the scenario table, starting identifiers, and a decision rule before examining results.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Why does each trial need a previous turn in the same session, instead of starting the task in a fresh session?
2. What does S2 tell you that S1 can't?
3. What counts as success in S4, and what must you save before the trial to check it?
4. Why must the acceptance checks sit outside the agent's write access?
5. Write an example decision rule for this experiment.

**Stop here.** Answer every question aloud before you read on.

### Answers

1. S1 tests whether the agent trusts a branch it remembers. A fresh session immediately before the task has no remembered branch, so nothing can mislead it: it would remove the very stale memory S1 is designed to exercise, and both configurations would likely pass.
2. Whether the new wording breaks the ordinary case, where the remembered and actual branch agree. If state-check helps S1 but hurts S2, it isn't simply better.
3. Stopping on `main` with nothing changed: an unchanged dirty tree is the success. Save the starting commit and the uncommitted file's initial contents, or a hash of them, so the grader can detect overwritten or lost work.
4. An agent that can edit the checks can change what counts as a pass, deliberately or by accident. The grade then no longer measures the task.
5. For example: repeat S1 if state-check improves it, and investigate any regression on S4 before expanding. Any rule will do if it's written down first and names the outcome that would change your mind.
