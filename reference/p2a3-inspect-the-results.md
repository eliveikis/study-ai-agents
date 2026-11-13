# P2A3 — Inspect and calibrate the results

Use 10–20 minutes to study the material below. The full activity has a 45-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Read one result backwards

Start with a reported outcome. Find the grader output that produced it, the final repository it inspected, and the starting state for that attempt. Confirm the grader actually ran and completed. An empty log or missing result cannot establish that the task passed.

| Observation | Interpretation to investigate |
| --- | --- |
| Grader ran correctly; final branch wrong | Task failure |
| Invocation timed out before final state was captured | Incomplete execution |
| Agent finished; acceptance test could not import its fixture | Grading error |
| Agent claimed success; grader found required behavior missing | Task failure if the grader and fixture are valid |

A trace is a chronological record of events. Locate the earliest event that separates the expected path from the observed one. The trace can support an explanation of what went wrong even though it cannot reveal the model's private reasoning.

## Check the grader with controls

A grader is software, and it can be wrong. Test it the way you'd test any check:

- A **negative control** is a result you know is wrong. The grader must reject it. Choose one that a careless grader would accept: one that looks right on the dimension the grader checks most obviously, and is wrong on another.
- A **positive control** is a result you know is right. The grader must accept it, so a grader that rejects everything can't pass for a strict one.

Build each control on a separate copy, predict which check should fire, run the grader, and read its reason.

## Summarize

Count passes, failures and errors by scenario and configuration. Include attempted trials and the denominator for any pass rate. Inspect a failure if one exists; otherwise walk through one successful trace and the deliberate negative control. Save a paragraph linking the evidence to one explanation and naming one uncertainty.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Of three attempts, one passes, one fails and one has a broken grader. What can you say?
2. Classify each: (a) the agent stopped on an API rate-limit error before finishing; (b) the grader ran, the branch is right, but the required function is missing; (c) the grader crashed while loading the fixture; (d) the agent says it's done, and the grader never ran.
3. Design a known-incorrect result for S1 that a grader checking only behavior would accept.
4. Why also run a known-good result through the grader?
5. In S1, what might the earliest diverging trace event be?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Two attempts have interpretable task outcomes, and one of those passed. Grading failed on the third, which tells you nothing about the task. Keep all three visible, with the denominator.
2. (a) Incomplete execution, so an error, not a task failure. (b) Task failure. (c) Grading error. (d) Not a pass: with no grade it's an error until grading runs.
3. Implement the requested behavior on the wrong branch, such as `old-task` or `main`. The final-branch check should reject it.
4. A grader that rejects everything also rejects the negative control, and looks strict. Only a known-good result shows it can pass anything.
5. Selecting the old requirement before querying Git.
