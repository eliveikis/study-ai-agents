# Design an overnight evaluation service

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Building blocks

**Job and attempt.** A job is the logical task, such as running S1 under baseline for repetition 3. An attempt is one execution of that job. Planned repetitions are separate jobs, with their own IDs. A retry is a new attempt of the same job.

**Durable queue.** Stores pending work so it survives restarts. Most queues deliver *at least once*: a message stays until the consumer acknowledges it, and if the consumer dies first, the queue delivers it again. So the same job can arrive twice, and handling it twice must be harmless. An operation that's harmless to repeat is **idempotent**.

**Lease and heartbeat.** A lease is a worker's temporary claim on a job, expiring at a set time. A heartbeat renews it during legitimate work. If the worker disappears, the lease expires and another worker can claim the job.

**Bounded concurrency.** Only a fixed number of trials run at once, through a fixed pool of workers or a semaphore.

**Shared rate limit.** A limit on requests or tokens per unit of time, counted across all workers. Ten individually compliant workers can collectively exceed an account limit, so the budget must be shared, not per worker.

**Conditional update.** A write that succeeds only if the stored record still matches what the writer expects: "save this text, but only if the document is still at version 7." If someone else changed it first, the write fails and the writer finds out, instead of silently overwriting. Databases do this with a `WHERE` clause on the expected value, then check how many rows changed.

**Timeouts and retries.** A timeout bounds how long a call, or a whole attempt, may run. A transient failure, such as a dropped connection or an HTTP 503 or 429, may succeed if retried. A permanent one, such as a 404 or invalid input, won't. Retry transient failures only, with a limit, exponential backoff (a longer wait after each failure) and jitter (a random part of each wait, so workers don't retry in lockstep).

**Throughput arithmetic.** Total work is jobs × average duration. Workers needed is total work ÷ time window, before allowing for retries, queue delays and rate limits. Label any numbers as illustrative assumptions, and recalculate with observed throughput.

## The design task

Sketch the service the plan's activity describes, from the building blocks above, before reading further. For each block, say where it sits in the path of one job.

---

## ⚠️ SPOILERS: questions and answers

Prepare and sketch using only the text above this line. Everything below it answers the design task. Read on only once your sketch is done.

### Questions

1. Draw the path of one job from submission to a persisted result.
2. Worker A saves an artifact just before losing its lease, and worker B retries the job. How do you keep a late write from A from overwriting B's result?
3. When do you acknowledge the queue delivery? What happens if a crash comes just before the acknowledgement, and just after it?
4. Why does a retry get a new attempt ID but keep its job ID, while a planned repetition gets a new job ID?
5. The grader says the task failed. Should the service retry? What about a timeout, or a crashed grader?
6. Jobs average six minutes. How many concurrent workers do 1,000 jobs need in an eight-hour window?
7. Where in the design does each of these go: a duplicate delivery, a worker crash, a rate-limit response?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. ```mermaid
   flowchart LR
       A[Submit job and configuration] --> Q[Durable queue]
       Q --> W[Worker claims time-limited lease]
       W --> L[Acquire shared rate-limit budget]
       L --> R[Run isolated trial with timeout]
       R --> G[Grade captured final state]
       G --> P[Persist attempt and finalize job]
       W -. expired lease .-> Q
   ```
2. Store artifacts under distinct attempt IDs, and use a conditional database update to finalize the logical job only for its active lease. A late A can retain diagnostic evidence without overwriting B's result.
3. After durable finalization. A crash just before it: the queue delivers again, and the new delivery finds the job already completed and does nothing. A crash just after it: nothing is lost, because the result is already stored.
4. A retry recovers the same measurement, so it's the same job. A planned repetition is a new sample. Keeping them apart means reliability recovery can't inflate the experiment's sample size, and a retry's success never counts as an independent success.
5. No. A valid grader verdict that the task failed is a completed measurement, and re-running until it passes biases the study. A timeout is an incomplete execution and a crashed grader is a grading error: retry those within limits, and record them separately. Keep incomplete executions, grader errors and task failures as distinct outcomes.
6. 1,000 × 6 minutes is 6,000 minutes, or 100 worker-hours. Over 8 hours that's 12.5, so at least 13 concurrent workers, before retries, queue delays and rate limits.
7. A duplicate delivery hits the completed-job check, or the conditional finalize, and becomes a no-op. A worker crash stops its heartbeats; the lease expires and the job is claimed again under a new attempt ID. A rate-limit response is transient: back off with jitter and retry within the shared budget, without recording a task failure.
