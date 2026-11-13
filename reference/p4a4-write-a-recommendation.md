# P4A4 — Write a one-page recommendation

Use 10–20 minutes to study the material below. The full activity has a 45-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

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

Use a concrete sentence frame for evidence: "On [scenario], [configuration] passed [x] of [n] attempts. In [attempt ID], the final branch was [observed] while the requirement specified [expected]." Fill it only from saved records.

## Alternative explanations

An alternative explanation is another cause that would produce the same observations. The usual suspects are chance, meaning run-to-run variation; a change in the setup during the runs, such as the fixture, the grader or the model version; and a difference between configurations you didn't intend. A good page names the most plausible one and the test that would tell it apart from yours.

Evidence also has limits of its own. A final repository state shows *what* happened. A trace can suggest *why*. Without a trace, say which of the two you have.

## Read it back

Read the page aloud in two minutes. Save the recommendation with references to the records and update the phase log.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. Under state-check, a branch check appears before a successful edit. What does that support, and what's an alternative explanation?
2. How would you test that alternative?
3. The fixture or grader changed partway through the runs. What do you do before interpreting the comparison?
4. With no trace available, what can you still claim about a failure?
5. After hearing the page, what three things should the reader be able to say?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. It's consistent with the instruction helping. One success could also reflect ordinary run-to-run variation.
2. Repeat both configurations on the same starting state.
3. Check the revisions, and compare only trials run against the same fixture and grader.
4. A final-state difference can still establish the failure, while leaving its cause unresolved.
5. What to do next, what would reverse that decision, and which result supports it. If the sample is incomplete, the next decision is about collecting the missing evidence.
