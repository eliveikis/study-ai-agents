# Experience stories and final recall

Use 10–20 minutes to study the material below. Recall questions and answers are at the end, behind a spoiler warning.

## Build four evidence-backed stories

An interviewer needs to understand the situation, your individual decision, alternatives you considered, and what happened afterward. A shipped change, a measured outcome and a teammate's observation support different claims. Use the strongest evidence you actually have and name any missing measurement.

| Story | Recall prompt | Evidence to locate |
| --- | --- | --- |
| RepoCop | Why synchronize templates, and what failed when branch state changed outside the session? | A template change, archived requirement or real trace |
| LLM API rate limiter | What resource was limited, where was it measured, and how did concurrent callers coordinate? | Your design, implementation, logs or tests |
| Failure analysis | What was the first visible symptom and how did you distinguish competing explanations? | Reproduction, diagnostic record and verification after the fix |
| Influence | Who faced a decision, what concern did they raise, and what changed after your contribution? | Decision record, feedback or observable adoption |

## Concurrency limits and rate limits

A **concurrency limit** caps how many requests are in flight at once, typically with a semaphore of N permits. It says nothing about how many complete per minute. A **rate limit** caps how much is used per unit of time. A common design is the token bucket: a bucket refills at a fixed rate up to a capacity, each request takes from it, and a request waits or fails when it's empty, which allows short bursts. LLM APIs often limit both requests and tokens per minute, and output tokens are only known once the response arrives. Scope matters too: a limit can apply per process, per host, or across every caller through shared state.

## Rehearse with a follow-up

Spend eight minutes per story. Give a 90-second version, then answer one challenge: "What did you personally do?", "What did the alternative cost?", or "How do you know?" For the rate limiter, explain the unit and scope of your actual implementation. For influence, name a concrete interaction and outcome you can defend.

Use 15 minutes for closed-notes recall: the questions at the end, answered without notes, then checked against the answers and your records. Use the final 13 minutes to update the progress log with remaining risks, evidence and next priority.

## Finish with an honest handoff

Write one line each for what you can now do independently, what still requires notes and what remains untested. Include a concrete correction from the mocks. These lines make resuming preparation possible even if the interview format or date changes.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them. Your stories are your own and have no answers here.

### Questions

1. Draw the model–harness–tool loop.
2. Which scenario is the branch experiment's control, and why?
3. Trace a worker crash followed by a retry.
4. What's the difference between a concurrency limit and a rate limit?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. User → harness → model, with tool descriptions → model requests a tool with arguments → harness checks and invokes the tool → tool returns a result → harness adds the result to the context → the model's next call answers.
2. S2: the remembered and actual branch agree, so it checks that the new wording doesn't break the ordinary case.
3. The worker claims a lease and starts an attempt, then crashes. Its heartbeats stop and the lease expires. Another worker claims the job under a new attempt ID and the same job ID. The final write is conditional on the active lease, so a late write from the crashed attempt can't overwrite the result, and the job counts once.
4. A concurrency limit caps requests in flight at once; a rate limit caps requests or tokens per unit of time. Ten slow requests can respect a concurrency limit of 10 and still be well under a rate limit, while a hundred fast ones can respect it and exceed the rate limit.
