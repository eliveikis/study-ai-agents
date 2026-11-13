# P5A3 — Repair the largest exposed gap

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## Select an observable failure

Read the two mock records. Prefer a recurring mistake that blocked a correct result or explanation. “Weak on Python” is hard to retest. “Counted duplicate deliveries as separate jobs” has a small counterexample and a clear success condition. If gaps appear equally important, choose the one for which a short exercise can supply fresh evidence.

## Run a repair cycle

1. **Recover the failure (10 min).** Re-run the smallest failing input or repeat the exact follow-up question without hints. Record your prediction and the observed discrepancy.
2. **Explain and correct it (20 min).** Identify the missing idea. For duplicate jobs, a job ID identifies logical work while an attempt ID identifies one execution. For a coding error, save the first red test and the corrected implementation. For an explanation, write the event sequence that was previously missing.
3. **Vary one condition (15 min).** For the job example, replay an older attempt after a newer attempt completed. Explain which identity and ownership checks prevent stale overwrites. For a string problem, change an input boundary or duplicate pattern.
4. **Retry cold (15 min).** Close the notes and start a new file or blank diagram. Repeat the original task and the variation. Record time, accuracy and assistance.

## Decide whether the repair transferred

Passing the original example shows that example is now handled. Correctly predicting the unfamiliar case supplies evidence that you understood the underlying rule. If the variation fails, keep the gap open and record the first point where the prediction went wrong. Save a before-and-after artifact and a one-sentence rule you can explain aloud.
