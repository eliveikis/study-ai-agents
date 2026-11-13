# P2A3 — Inspect and calibrate the results

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 45-minute timebox, including study.

## Read one result backwards

Start with a reported outcome. Find the grader output that produced it, the final repository it inspected, and the starting state for that attempt. Confirm the grader actually ran and completed. An empty log or missing result cannot establish that the task passed.

| Observation | Interpretation to investigate |
| --- | --- |
| Grader ran correctly; final branch wrong | Task failure |
| Invocation timed out before final state was captured | Incomplete execution |
| Agent finished; acceptance test could not import its fixture | Grading error |
| Agent claimed success; grader found required behavior missing | Task failure if the grader and fixture are valid |

A trace is a chronological record of events. Locate the earliest event that separates the expected path from the observed one. In S1 that might be selecting the old requirement before querying Git. The trace can support that explanation even if it cannot reveal the model’s private reasoning.

## Challenge the grader

On a separate copy, deliberately create a known incorrect result. For example, implement the requested behavior on the wrong branch. A grader checking only the behavior could accept it. Predict which check should reject it, run the grader, and inspect its reason. Also try a known good result so a grader that rejects everything cannot appear successful.

## Summarize

Count passes, failures and errors by scenario and configuration. Include attempted trials and the denominator for any pass rate. Inspect a failure if one exists; otherwise walk through one successful trace and the deliberate negative control. Save a paragraph linking the evidence to one explanation and naming one uncertainty.

Recall question: if one of three attempts passes, one fails and one has a broken grader, what can you say? Two attempts have interpretable task outcomes, one of those passed, and grading failed on the third. Keep all three visible.
