# P3A2 — Repeat and compare configurations

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## Make one comparison interpretable

A configuration is the complete setup for a run. Here the intended difference is the branch text. For baseline, start from the current skill and restore only the branch wording from 54462fd. For state-check, use the branch wording in d3b9bf8. Both use the revised step 3. Replacing the whole baseline skill with an older version would confound the branch change with other instruction changes.

A paired comparison exposes both configurations to the same scenario. For S1 give each the same previous turn, fixture and external switch, in separate sessions. Match model, harness, tool permissions, time and token budgets. Reset between attempts. Repeats show whether the result persists when generation or execution varies.

## Record a small comparison

| Scenario | Baseline attempts and outcomes | State-check attempts and outcomes | Trace difference |
| --- | --- | --- | --- |
| S1 stale branch | Fill from records | Fill from records | Was branch checked before first edit or switch? |
| S2 unchanged branch | Fill from records | Fill from records | Did the control regress? |
| S3 explicit path | Fill from records | Fill from records | Was the required branch selected? |
| S4 dirty tree | Fill from records | Fill from records | Was unrelated work preserved? |

Repeat a selected subset under both configurations. Mark errors separately and preserve attempt IDs. Record whether either configuration ran checks before its first edit. Interleave run order if practical so a time-of-day effect is less likely to line up with one configuration.

## Defend your conclusion

Imagine S1 improves on one run but S4 loses an uncommitted edit. An aggregate pass count hides the difference in severity. Report those scenario outcomes individually, list uncontrolled conditions, and identify the next repeat that could change your recommendation. Explain aloud why three repeats on S1 add evidence about variability on S1 but do not add three new kinds of task.
