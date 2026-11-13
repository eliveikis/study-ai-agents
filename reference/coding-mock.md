# Coding mock

Use 10–20 minutes to set up. The worked solution is at the end, behind a spoiler warning.

## What this mock draws on

No new material: a mock tests what you can already do. This one uses dictionaries, counting and tests, from `results-reader.md`, `first-unique-character.md` and `group-anagrams.md`. Revisit those guides' teaching sections beforehand, not their answers.

## Set up an independent attempt

Choose the reference restrictions communicated for the interview. If they remain unknown, record an assumption and practice without AI or references. Set aside 5 minutes to clarify the problem, 30 to implement, 10 to test, 5 to explain complexity and 10 to review.

**Prompt.** A stream contains pairs of job ID and outcome in chronological order. Each new pair replaces that job's previous outcome. Return the number of distinct jobs currently in each outcome, omitting zero counts. Clarify how you will handle empty input, repeated identical events and invalid outcomes. Explain your approach aloud as you work.

Before coding, predict the result for `[(A, fail), (B, pass), (A, pass)]`, and what changes if `(A, pass)` is delivered again. Write down the smallest example that could distinguish counting jobs from counting attempts, and test it.

Save the independent code before applying corrections.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the mock. Read on only once time is up and your code is saved.

### Questions

1. What does `[(A, fail), (B, pass), (A, pass)]` return, and what changes if `(A, pass)` is delivered again?
2. What's the smallest example that distinguishes counting jobs from counting attempts?
3. Describe one approach and its time and space costs.
4. What changes if the caller needs the counts after every event?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Only pass, with count 2: A's fail was replaced. A repeated `(A, pass)` changes nothing.
2. `[(A, pass), (A, pass)]`: counting jobs gives pass 1, counting attempts gives pass 2.
3. Keep a dictionary of the latest outcome for each ID, then count its values. This uses expected O(n) time for n events and O(j) state for j distinct jobs, plus the output.
4. Update both maps incrementally, which changes the tradeoff. You must decrement the old outcome, handle repeated identical events, and remove empty buckets.

### Score yourself

Score four observable behaviors: clarified the contract, produced working code within time, tested a replacement, and gave a justified complexity bound. Record the time of the first working example and one exact input that exposed a mistake. Select a follow-up based on the weakest observed behavior.
