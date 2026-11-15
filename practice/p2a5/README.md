# Evaluation-service basics

## Activity

Phase 2, "Evaluation-service basics": sketch a service for 1,000 overnight jobs at its simplest: jobs and attempts, a durable queue, job leases, and bounded concurrency. Explain what happens to a job when its worker crashes.

## Time spent

Not reported.

## Review

Left partly unfinished on purpose, as a first pass in the right direction, so the human could move on.

What it gets right:

- **A durable queue:** jobs stored in Postgres, and reloaded from it if the service goes down.
- **Bounded concurrency:** a configured maximum of jobs running at once.
- **The crash case, in outline:** the job becomes available again once its lease times out.
- **Timeouts** for a single job and for the whole run, and jobs isolated from each other in containers.
- **Build or buy:** checking an existing scheduler before writing one. The Python orchestrator meant is probably Prefect.

What's missing:

- **Jobs and attempts aren't told apart**, though the activity names them first. A job is the work to do; an attempt is one try at it. A crash ends an attempt, not the job: the job gets a new attempt. Recording attempts shows the retries, lets you cap them and mark a job failed after N, and keeps a retried job from counting as two results.
- **No sketch of the mechanism.** The four building blocks get one criterion each, and claiming a job is left as TBD. At its simplest: a jobs table with a status, a lease owner and a lease expiry, and an attempts table. A worker claims one queued job, or one whose lease has expired, in a single atomic update, so two workers can't take the same job. In Postgres that's `SELECT … FOR UPDATE SKIP LOCKED`, or an `UPDATE … RETURNING`.
- **The crash isn't explained step by step.** The worker stops renewing its lease, the lease expires, another worker claims the job, and a new attempt starts. If the crashed attempt was only slow and reports later, its result is a duplicate, and the service has to decide which result counts.
- **Most of the words go on things outside "at its simplest":** the HTTP API, logging, containers and a CI test. "Exact design would depend on product research" hedges where an interview wants stated assumptions and a design.

Verdict: **doesn't meet the activity yet.** The direction is right, with a durable store, leases, bounded concurrency and recovery by lease expiry. But jobs and attempts are missing, the claim mechanism is left as TBD, and the crash gets one sentence.

## Assistance used

Before writing, Claude explained what a job lease is and how it differs from a lock. Otherwise not reported.
