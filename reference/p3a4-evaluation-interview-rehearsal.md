# P3A4 — Evaluation interview rehearsal

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 45-minute timebox, including study.

## Answer the 16 versus 14 question

Two code-review agents review the same 20 pull requests. A succeeds on 16, B on 14. A has the higher observed success rate on these tasks (80% versus 70%). To decide which to use, ask how success was graded and which PRs each agent passed.

| Possible paired results | Both pass | Only A | Only B | Neither |
| --- | ---: | ---: | ---: | ---: |
| Pattern 1 | 14 | 2 | 0 | 4 |
| Pattern 2 | 10 | 6 | 4 | 0 |

Check the margins yourself. Both rows produce 16 and 14. Pattern 1 suggests inspecting two A-only wins. Pattern 2 exposes four regressions that an aggregate comparison conceals. Examine severity: a missed correctness defect and a stylistic comment may have different consequences.

## Practice follow-ups

- **Coverage.** Which languages, change sizes and defect types appear? Twenty near-identical PRs leave broad uncertainty about new workloads.
- **Consistency.** Repeat selected PRs under each configuration. Retain each attempt and grader output. Repeats help distinguish a stable difference from run-to-run variation.
- **Quality.** Inspect missed defects, incorrect comments and reviewer time spent verifying suggestions. Check whether the grader would recognize a valid alternative finding.
- **Cost and time.** Compare cost per attempted review, completion time and human effort alongside quality. A slower review can delay the entire PR even if the average score improves.

## Connect it to your experiment

Give a 90-second answer in four parts: observed difference, missing paired evidence, risks that matter, and the next test. Then do the same with actual S1–S4 outcomes. Save one answer to “What evidence would change your mind?” Identify a specific scenario and result. Avoid inventing repetitions or claiming statistical certainty from the totals.
