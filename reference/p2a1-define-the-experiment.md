# P2A1 — Define the branch experiment

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## Specify what would count as success

An experiment question identifies a change and a measurable consequence. Here the change is the branch section of the implement skill. The consequence is whether the agent works on the correct requirement after a branch changes outside its session. A scenario describes the starting conditions. A trial is one execution of a scenario under one configuration. A grader measures the result using evidence it controls.

| Scenario | Runner action after previous turn | Required final behavior |
| --- | --- | --- |
| S1 | Switch from completed old-task to existing new-task | Implement new-task on its branch |
| S2 | Stay on new-task after reading its requirement | Implement the same task there |
| S3 | Move from new-task to main; supply requirement path | Switch back and implement there |
| S4 | Move from old-task to main; leave an uncommitted file; supply path | Stop on main and preserve all state |

S2 is a control: it checks behavior when remembered and actual branch agree. In S4, an unchanged dirty tree can be a success. Save the initial contents so a grader can detect overwritten work.

## Design the fixture before the run

Use a disposable repo and a local bare origin with its HEAD set so the skill can discover the default branch. Pin fixture commits and snapshot uncommitted changes. Give both configurations the same previous turn within each scenario. Keep the session alive across the external switch. Start a fresh session for each independent trial.

For each scenario write down the final branch, required behavior and allowed changes. Keep acceptance checks outside the agent’s write access. Separately record whether a branch check preceded switches or edits and whether checks ran before the first edit. Those trace observations explain the path to the result.

## Deliverable and recall

Save the scenario table, starting identifiers, and a decision rule before examining results. Example decision: repeat S1 if state-check improves it, and investigate any regression on S4 before expanding. Explain why a fresh session immediately before the task would remove the very stale memory S1 is designed to exercise.
