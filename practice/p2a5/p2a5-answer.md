# Q

Sketch a service for 1,000 overnight jobs at its simplest: jobs and attempts, a durable queue, job leases, and bounded concurrency. Explain what happens to a job when its worker crashes.

# A

I'll first discuss the product goals a bit to help plan.

## Requirement

A service must support running 1000 overnight jobs and the target is simple feature support, which could be extended later.

## Acceptance Criteria

1. The service has a test that runs 1000 jobs, targetted for ci/cd and local dev, so ideally the jobs finish quickly (e.g. entire test takes seconds).
2. A test confirms that job leases, failed jobs, and max concurrency works as expected.
3. If a single job exceeds a configurable timeout, the job is cancelled with an error.
4. If the entire 1000 job process exceeds a configurable timeout, any in-flight and remaining jobs are cancelled with an error.
5. Logs show service lifecycle and events like loading jobs, queing jobs, and running jobs, finishing jobs, and errors.
6. Jobs are run in a reasonably isolated manner for this "simple" service, e.g. in a docker container, to minimize the behavioral effects of a running job on other jobs and the overall service.
7. The service hosts and a simple HTTP rest api to add jobs.
8. Jobs are stored in a postgres db, for now it can just be in a local docker for the first version and to support local development and testing.
9. If the service goes down, it is able to reload its jobs from the db.
10. The service configuration allows jobs to be run in parallel, with a max concurrent count.
11. When a worker crashes, its docker image is automatically cleaned up. The job becomes available again after its lease times out.
12. TBD: etc final acceptance criteria to check for pending jobs, locking and applying a lease, handling concurrency, recovery, error handling & reporting/visibilty.

## Architecture

One approach would be a single long-running python job scheduler/dispatcher, with a postgres db in docker, which can run locally for dev or simple systems, or on a separate server/vps/etc. I'm assuming we want to schedule jobs dynmically so the service could have an HTTP api. The scheduler and dispatcher could be separated into isolated concerns/services. Exact design would depend on product research to see the scale, users, production needs, etc.

An existing solution like the Perfect docker job scheduler for Python could be evaluated and used if it meets the needs.

