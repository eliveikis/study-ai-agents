# P4A4 — Write a one-page recommendation

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 45-minute timebox, including study.

## Start with the decision someone needs to make

Your reader knows engineering but may never have used RepoCop. Introduce the task in one sentence: an agent implementing a requirement must identify the current branch after a developer switches branches outside the conversation. Then state the decision your pilot can inform, such as whether to retain the state-check wording for a larger trial.

## Draft the page

| Paragraph | Material to supply |
| --- | --- |
| Question and recommendation | Exact change tested and the next action you recommend |
| Method | Four scenarios, previous turn, external change, two configurations, fixed settings and independent acceptance checks |
| Results | Counts by scenario and configuration, repeats, errors and unavailable data |
| Failure example | One attempt ID, expected behavior, observed state and first relevant trace event |
| Limits and next step | Alternative explanation, follow-up that could distinguish it, and stop condition |

Use a concrete sentence frame for evidence: “On [scenario], [configuration] passed [x] of [n] attempts. In [attempt ID], the final branch was [observed] while the requirement specified [expected].” Fill it only from saved records. If a trace is unavailable, a final-state difference can still establish failure while leaving its cause unresolved.

## Challenge your interpretation

A branch check that appears before a successful edit is consistent with the instruction helping. One success could also reflect ordinary run-to-run variation. Repeating both configurations on the same starting state probes that explanation. A fixture or grader change calls for checking revisions before interpreting the comparison.

Read the page aloud in two minutes. Can the reader identify what to do next, what would reverse that decision, and which result supports it? Save the recommendation with references to the records and update the phase log. If the sample is incomplete, make the next decision about collecting missing evidence.
