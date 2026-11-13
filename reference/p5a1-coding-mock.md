# P5A1 — Coding mock

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## Set up an independent attempt

Choose the reference restrictions communicated for the interview. If they remain unknown, record an assumption and practice without AI or references. Set aside 5 minutes to clarify the problem, 30 to implement, 10 to test, 5 to explain complexity and 10 to review. Read the prompt and stop before the review section until the attempt ends.

**Prompt.** A stream contains pairs of job ID and outcome in chronological order. Each new pair replaces that job’s previous outcome. Return the number of distinct jobs currently in each outcome, omitting zero counts. Clarify how you will handle empty input, repeated identical events and invalid outcomes. Explain your approach aloud as you work.

For [(A, fail), (B, pass), (A, pass)] the result contains only pass with count 2. Predict what would happen if (A, pass) were delivered again. Test the smallest example that could distinguish counting jobs from counting attempts.

## Review after time expires

One approach keeps a dictionary of the latest outcome for each ID, then counts its values. This uses expected O(n) time for n events and O(j) state for j distinct jobs plus the output. If a caller needs counts after every event, updating both maps incrementally changes the tradeoff. You must decrement the old outcome, handle repeated identical events, and remove empty buckets.

Score four observable behaviors: clarified the contract, produced working code within time, tested a replacement and gave a justified complexity bound. Record the time of the first working example and one exact input that exposed a mistake. Save the independent code before applying corrections. Select a follow-up based on the weakest observed behavior.
