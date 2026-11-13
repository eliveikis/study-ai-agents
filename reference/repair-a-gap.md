# Repair the largest exposed gap

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Select an observable failure

Read the two mock records. Prefer a recurring mistake that blocked a correct result or explanation. "Weak on Python" is hard to retest. "Counted duplicate deliveries as separate jobs" has a small counterexample and a clear success condition. If gaps appear equally important, choose the one for which a short exercise can supply fresh evidence.

## Run a repair cycle

1. **Recover the failure (10 min).** Re-run the smallest failing input or repeat the exact follow-up question without hints. Record your prediction and the observed discrepancy.
2. **Explain and correct it (20 min).** Identify the missing idea. For duplicate jobs, a job ID identifies logical work while an attempt ID identifies one execution. For a coding error, save the first red test and the corrected implementation. For an explanation, write the event sequence that was previously missing.
3. **Vary one condition (15 min).** Change one thing about the original case. For the job example, replay an older attempt after a newer attempt completed. For a string problem, change an input boundary or duplicate pattern.
4. **Retry cold (15 min).** Close the notes and start a new file or blank diagram. Repeat the original task and the variation. Record time, accuracy and assistance.

## Decide whether the repair transferred

Passing the original example again shows only that this example is now handled; you may have remembered the fix. Predicting an unfamiliar variation correctly is evidence that you understood the rule behind it. If the variation fails, keep the gap open and record the first point where the prediction went wrong. Save a before-and-after artifact and a one-sentence rule you can explain aloud.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. What makes "counted duplicate deliveries as separate jobs" a better repair target than "weak on Python"?
2. You pass the original failing example after the repair. What does that show, and what doesn't it?
3. An older attempt is replayed after a newer attempt of the same job completed. Which identity and ownership checks prevent a stale overwrite?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. It has a small counterexample and a clear success condition, so you can retest it and see the result. "Weak on Python" can't be retested.
2. That this example is now handled. Not that you understood the rule: only a correct prediction on an unfamiliar variation shows that.
3. Identity: results are stored under the attempt ID, and the job ID ties them to one logical job. Ownership: the final write is conditional on the current lease, so a stale attempt can't finalize the job, though its diagnostics can still be kept.
