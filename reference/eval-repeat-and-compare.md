# Repeat and compare configurations

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Make one comparison interpretable

A configuration is the complete setup for a run. Here the intended difference is the branch text. For baseline, start from the current skill and restore only the branch wording from 54462fd. For state-check, use the branch wording in d3b9bf8. Both use the revised step 3.

A **confound** is any second difference between the things you compare. If two configurations differ in more than the one thing you meant to change, a difference in outcomes can't be pinned on that thing.

A paired comparison exposes both configurations to the same scenario. For S1 give each the same previous turn, fixture and external switch, in separate sessions. Match model, harness, tool permissions, time and token budgets. Reset between attempts.

## Repeats and variation

Agent runs vary. Sampling, timing and tool output can differ, so the same inputs can pass once and fail the next time. Repeating a scenario under the same configuration shows how much its outcome moves by itself. Outside factors can drift during a session too, such as API load or a model update. Interleave the run order where practical, so such a drift is less likely to line up with one configuration.

Failures also differ in cost. A recoverable mistake and one that destroys work both count as one failure in a total.

## Record a small comparison

| Scenario | Baseline attempts and outcomes | State-check attempts and outcomes | Trace difference |
| --- | --- | --- | --- |
| S1 stale branch | Fill from records | Fill from records | Was branch checked before first edit or switch? |
| S2 unchanged branch | Fill from records | Fill from records | Did the control regress? |
| S3 explicit path | Fill from records | Fill from records | Was the required branch selected? |
| S4 dirty tree | Fill from records | Fill from records | Was unrelated work preserved? |

Repeat a selected subset under both configurations. Mark errors separately and preserve attempt IDs. Record whether either configuration ran checks before its first edit.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Why is the baseline the current skill with only its branch text reverted, rather than the whole skill from 54462fd?
2. What makes the S1 comparison paired, and what must match between the two configurations?
3. Why interleave the run order?
4. Under state-check, S1 improves on one run, but S4 loses an uncommitted edit. Why isn't a total pass count enough, and what do you report?
5. Why do three repeats on S1 add evidence about variability on S1, but not three new kinds of task?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Replacing the whole baseline skill with an older version would confound the branch change with every other instruction change since then. Any difference in outcomes couldn't be attributed to the branch text.
2. Both configurations run the same scenario: the same previous turn, fixture and external switch, in separate sessions. Model, harness, tool permissions, time and token budgets match, and each attempt starts from a reset.
3. So that a time-of-day effect, or any drift during the runs, is less likely to line up with one configuration.
4. An aggregate pass count hides the difference in severity: losing uncommitted work can outweigh a gain on S1, and the totals might even tie. Report each scenario's outcomes individually, list the uncontrolled conditions, and identify the next repeat that could change your recommendation.
5. Repeats sample the same task again. They show whether S1's outcome is stable, not how the agent handles situations S1 doesn't cover. Coverage comes only from different scenarios.
