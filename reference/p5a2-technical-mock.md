# P5A2 — Technical mock

Use 10–20 minutes to set up. The full activity has a 60-minute timebox. The mock's questions, and what a strong answer covers, are at the end, behind a spoiler warning: in a mock, the questions are part of the test.

## What this mock draws on

No new material. The four rounds cover AI fundamentals (P1A2, P3A3), experiment design (P2A1, P3A2), failure diagnosis (P2A3) and systems (P4A2). Revisit those guides' teaching sections beforehand. If a partner runs the mock, they read the questions and you don't.

## Run four interview rounds

Use a timer or a partner. Take 12 minutes per round, then 12 minutes to score the session. Give a two-minute initial answer, draw or trace one example, and answer the follow-up without notes. Use your actual evaluation records for any claim about observed behavior.

Score each answer 0 if absent, 1 if you named the pieces, and 2 if you traced a concrete case and defended a tradeoff. Write down the first follow-up where you had to guess. Save that question, your answer and the evidence needed to improve it. This gives the repair session a more specific target than "study systems."

---

## ⚠️ SPOILERS: questions and answers

Everything below this line is the mock itself. Read on only when the timer starts, or let a partner read it to you.

### Questions

| Round | Opening question | Follow-up |
| --- | --- | --- |
| AI fundamentals | How does text become an agent action? | Where is the tool executed, and how does its result change the next prediction? |
| Experiment design | How would you test stale branch selection? | What must stay in the same session, and what must be reset between trials? |
| Failure diagnosis | The agent says it succeeded but the grader rejects it. What do you inspect? | How would you distinguish a wrong implementation from a broken acceptance check? |
| Systems | How do you complete 1,000 jobs overnight? | A worker submits its result after its lease expires. Which result is authoritative? |

**Stop here.** Answer every round aloud before you read on.

### Answers: the mechanisms to listen for

- **Round one:** trace tokenization, model output, harness dispatch, tool response and the next inference call.
- **Round two:** keep the previous turn and the external branch switch together inside a trial, while isolating different trials.
- **Round three:** compare the expected branch, observed tree, test output and grader version. Use known good and wrong states to check grading.
- **Round four:** explain a conditional final write keyed by the current lease, and how attempt IDs preserve history.
