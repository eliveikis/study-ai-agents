# P3A4 — Evaluation interview rehearsal

Use 10–20 minutes to study the material below. The full activity has a 45-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Totals hide which items changed

Suppose two students take the same 10-question quiz. A gets 8 right and B gets 7. Each question has one of four results: both right, only A right, only B right, or both wrong. The totals, 8 and 7, are only the margins of that four-way table, and very different tables produce the same totals. In one, A got right every question B did, plus one more. In another, each got right several questions the other missed. Results on the same items are **paired**, and the pairs tell you more than the totals.

## Small samples move in big steps

With 20 tasks, one task is 5 percentage points. Agent runs vary, so running the same agent twice on the same tasks can flip a task or two. A small gap between totals can come from that variation alone. Repeating runs on the same tasks shows how far the totals move by themselves.

## What a pass rate leaves out

- **Coverage:** which kinds of task the set contains. A narrow set says little about the others.
- **Severity:** a missed security defect and a missed style nit each count as one miss.
- **The grader:** it can wrongly accept or reject, and may score a valid alternative answer as a fail.
- **Cost and time:** price per run, time to finish, and the human effort to check the output.

## The rehearsal

The plan's practice question: two versions of a code-review agent each review the same 20 pull requests. One succeeds on 16, the other on 14. Is the first one better?

Give a 90-second answer in four parts: observed difference, missing paired evidence, risks that matter, and the next test. Then do the same with actual S1–S4 outcomes. Save one answer to "What evidence would change your mind?", naming a specific scenario and result. Avoid inventing repetitions or claiming statistical certainty from the totals.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Is the agent that succeeds on 16 of 20 better than the one at 14?
2. Give two paired tables that both produce 16 and 14, and say what each would lead you to do.
3. What follow-ups would you raise on coverage, consistency, quality, and cost and time?
4. What evidence would change your mind?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Not established yet. A has the higher observed success rate on these tasks, 80% against 70%. To decide which to use, ask how success was graded and which PRs each agent passed.
2. Check the margins yourself: both rows produce 16 and 14.

   | Possible paired results | Both pass | Only A | Only B | Neither |
   | --- | ---: | ---: | ---: | ---: |
   | Pattern 1 | 14 | 2 | 0 | 4 |
   | Pattern 2 | 10 | 6 | 4 | 0 |

   Pattern 1 suggests inspecting A's two extra wins. Pattern 2 exposes four regressions that an aggregate comparison conceals. Either way, examine severity: a missed correctness defect and a stylistic comment may have different consequences.
3. - **Coverage.** Which languages, change sizes and defect types appear? Twenty near-identical PRs leave broad uncertainty about new workloads.
   - **Consistency.** Repeat selected PRs under each configuration. Retain each attempt and grader output. Repeats help distinguish a stable difference from run-to-run variation.
   - **Quality.** Inspect missed defects, incorrect comments and reviewer time spent verifying suggestions. Check whether the grader would recognize a valid alternative finding.
   - **Cost and time.** Compare cost per attempted review, completion time and human effort alongside quality. A slower review can delay the entire PR even if the average score improves.
4. Any answer that names a specific result. For example: if rerunning both agents on the same 20 PRs reversed the order, the gap was run-to-run variation. Or if B's wins over A include correctness defects that A missed, A's extra wins may not be worth the regressions.
