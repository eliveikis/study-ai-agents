# AI Tools Interview Study Plan

## Purpose and constraints

Prepare for a Senior AI Engineer, AI tools role.

Budget approximately 20 hours or less. Work in phases of up to four hours. Each phase builds on the previous work and leaves a usable result if preparation stops there. Phases 1–4 cover every topic once and end in mock interviews. Phases 5–7 each take the topics one layer deeper, so a budget that runs out cuts depth rather than topics. The timings are targets, not requirements to finish every exercise.

The interview format and date are unconfirmed. This plan assumes live coding is plausible and prioritizes independent Python fluency, AI fundamentals, and a small evaluation, built in RepoCop, that can be defended in discussion. Adjust the balance if the recruiter provides specific guidance.

## Starting assessment

| Area                 | Evidence from the diagnostic                                 | Preparation need                                             |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Software engineering | 15+ years of C++, five years of Go, developer tooling and API experience | Translate experience into concrete, concise examples         |
| Python               | Prior professional experience, currently rusty; extensive documentation needed | Practice writing, testing, and debugging without AI, including timed exercises |
| Agent workflows      | Built Repocop to synchronize agent development templates and expose spec workflow status | Explain personal design decisions, failures, and verified outcomes |
| AI fundamentals      | Gaps in tokenization, decoding, embeddings, fine-tuning, tool calling, and MCP | Build accurate explanations and connect them to workflow behavior |
| Evaluations          | Sensible reasoning about representativeness, quality, cost, and comparisons; no formal implementation experience | Add a small reproducible eval to RepoCop, with independent grading and failure analysis |
| Systems and adoption | Relevant rate-limiter experience and broad engineering judgment | Practice durable job execution, CI tradeoffs, and explicit adoption criteria |

Coding fluency and project implementation details have not been independently assessed. This is a preparation guide, not a prediction of interview success.

## Working rules

- Timebox phases. When an activity overruns, cut its depth, not the topic: record what's left as unfinished, for that topic's next layer, and promote it only when it blocks an important next step.
- End each phase by updating the progress log and next-session entry. Reserve time within the final activity.
- Write the first attempt at coding exercises without AI. Use documentation during learning exercises, then practice selected exercises without references.
- Explain the approach, edge cases, and time/space complexity aloud during timed coding.
- Keep explanations short enough for an interview, then practice follow-up questions.
- Prefer working code, recorded results, and corrected mistakes over extensive reading or polished infrastructure.
- Keep a record of assistance used so independent ability and AI-assisted work remain clear.

## Phase overview

| Phase | Focus                                                              | Main result                                          | Status      |
| ----- | ------------------------------------------------------------------ | ---------------------------------------------------- | ----------- |
| 1     | Python baseline, coding basics, inference and agent loop           | Working results reader and an initial skill baseline | Done        |
| 2     | A first layer of every other topic                                 | A first answer for every interview topic             | Done        |
| 3     | Explaining RepoCop's eval, timed coding                            | An explanation of RepoCop's eval, from memory        | Not started |
| 4     | Mock interviews and repair                                         | Evidence of performance under interview conditions   | Not started |
| 5     | Second layer: more eval tasks, reliability, retrieval, context     | RepoCop's eval on several tasks under both versions  | Not started |
| 6     | Third layer: eval repeats, crash recovery, the reader over HTTP    | Repeated eval runs and a crash-safe service design   | Not started |
| 7     | Metrics, recommendation, Repocop with evidence                     | One-page recommendation                              | Not started |
| 8     | Final rehearsal, just before the interview                         | Final mock results and prioritized remaining gaps    | Not started |

## Phase 1 — Establish the foundation

**Budget: four hours**

- [ ] **90 minutes — Python through a useful program.** Write a command-line program that reads a JSONL file of evaluation results and prints how many results have each outcome. Practice file handling, dictionaries/lists, functions, exceptions, and simple tests. Review mutability, default arguments, and iteration as needed.
  - **Input:** one JSON object per line. Each is the result of one trial in the evaluation you build from Phase 3: one run of an AI agent on one test scenario. Its fields are in [specs/architecture.md › Trial record](specs/architecture.md#trial-record).
  - **Output:** one line per outcome with its count, such as `pass: 4`.
  - **Malformed input:** a line that isn't a valid trial record stops the program with an error that gives the line number and what's wrong.
  - **Samples:** [tests/data/results_sample.jsonl](tests/data/results_sample.jsonl) gives `pass: 4`, `fail: 1` and `error: 1`. [tests/data/results_malformed.jsonl](tests/data/results_malformed.jsonl) fails at line 3, which has no `outcome`.
  - **Where:** the program goes in `src/branch_eval/` and its tests in `tests/`. `make check` lints and runs the tests.
- [ ] **60 minutes — Inference and the agent loop.** Learn and explain tokens, context windows, next-token probabilities, sampling versus greedy decoding, and training versus inference. Draw the flow from model tool-call request to harness execution to returned result. Distinguish the model, harness, and tools.
- [ ] **30 minutes — One short coding exercise.** Use Python for a string problem. Attempt it before checking a solution. Discuss complexity and test empty inputs, duplicates, and boundaries. Follow [practice/README.md](practice/README.md).
  - **String:** given a string, return the index of its first character that appears only once, or -1 if there is none.
- [ ] **20 minutes — Rehearse a short Repocop story.** In about 60 seconds, explain the problem, the architecture, one decision you made and one failure. Distinguish deterministic software from model decisions.

### Completion evidence

- [x] Results reader runs on a small sample and reports errors visibly.
- [x] At least one meaningful test covers parsing or aggregation behavior.
- [x] Coding attempts and mistakes are saved.
- [ ] Have a 60-second Repocop story covering the problem, the architecture, one decision and one failure.

## Phase 2 — Cover every topic once

**Budget: three hours**

- [ ] **30 minutes — Group anagrams.** Use Python for a list/dictionary problem: given a list of words, return them grouped so that each group holds words that are anagrams of each other. Attempt it before checking a solution. Discuss complexity and test empty inputs and duplicates. Follow [practice/README.md](practice/README.md).
- [ ] **30 minutes — Retrieval versus fine-tuning.** Explain what retrieval-augmented generation supplies at request time and what fine-tuning changes. Discuss why retrieval is a plausible starting point for a private codebase that changes daily.
- [ ] **30 minutes — Tool schemas and MCP.** Explain tool descriptions and argument schemas, and MCP's role between host/client and server.
- [ ] **30 minutes — Compare two agents.** Practice this question: two versions of a code-review agent each review the same 20 pull requests, and one succeeds on 16 while the other succeeds on 14. Is the first one better? Cover task coverage, paired outcomes, repeated runs, quality, cost, and time.
- [ ] **30 minutes — Evaluation-service basics.** Sketch a service for 1,000 overnight jobs at its simplest: jobs and attempts, a durable queue, job leases, and bounded concurrency. Explain what happens to a job when its worker crashes.
- [ ] **30 minutes — Mini-mock.** Without notes, answer one interview question on each topic covered so far: inference and the tool-use loop, retrieval versus fine-tuning, MCP, comparing two agents, and the job service. Record each question where you had to guess.

### Completion evidence

- [x] The anagram attempt and its mistakes are saved.
- [ ] Can explain inference and a tool-use loop in roughly two minutes from memory.
- [ ] Can say what retrieval and fine-tuning each change, and why retrieval suits a codebase that changes daily.
- [ ] Can answer the 16-versus-14 question without claiming more than the totals show.
- [ ] Mini-mock answers are recorded, with the questions where you had to guess.

## Phase 3 — Explain RepoCop's eval

**Budget: one hour**

- [ ] **30 minutes — Explain the eval.** Without notes, explain in about two minutes how RepoCop's eval works: what it tests, how it runs and grades each case, what it found, and what you'd do next. Tell task failures apart from execution and grading errors.
- [ ] **30 minutes — Timed coding.** Solve one problem in Python against the clock, then repair mistakes. Prioritize strings, hash maps, sorting, two pointers, stacks/queues, or basic traversal according to earlier weaknesses. Explain complexity and test cases.

### Completion evidence

- [ ] Can explain the eval in two minutes without notes.
- [ ] Have a timed coding result and a short list of recurring mistakes.

## Phase 4 — Rehearse under interview conditions

**Budget: three hours**

- [ ] **45 minutes — Coding mock.** Use a timed problem with no AI and the reference restrictions expected in the interview. Explain the approach, implement it, test edge cases, and discuss complexity.
- [ ] **45 minutes — Technical mock.** Cover AI fundamentals, experiment design, failure diagnosis, and evaluation-service design at the depth covered so far. Use follow-ups that probe mechanisms and tradeoffs.
- [ ] **45 minutes — Repair the largest exposed gap.** Choose based on the mock results. Produce a corrected implementation or explanation, then retry without notes.
- [ ] **45 minutes — Repocop and the rate limiter.** Rehearse the Repocop story and the LLM API rate limiter. Clearly identify your contribution, evidence, tradeoffs, and outcomes.

### Completion evidence

- [ ] Mock results include concrete mistakes and corrections.
- [ ] Have specific Repocop and rate-limiter stories rather than general statements about working style.

## Phase 5 — Go a layer deeper

**Budget: three and a half hours**

- [ ] **30 minutes — Timed coding on the mock's mistakes.** Solve one timed problem chosen from the mock's mistakes, then repair them. Explain complexity and test cases.
- [ ] **75 minutes — More eval tasks.** In RepoCop, add tasks around the stale-branch one, and run each under both versions: a control, where nothing changes and both versions should pass, and a task where the agent should stop and change nothing, such as when uncommitted work is in the way. If you automate the runs, test the runner with a fake agent, so its tests make no paid calls.
- [ ] **40 minutes — Rate limits, retries, and timeouts.** Extend the job-service sketch with shared rate limits, a retry policy, timeouts, and the arithmetic for finishing overnight. Explain how to distinguish failed tasks from incomplete or broken executions.
- [ ] **30 minutes — The retrieval pipeline.** Explain embeddings, chunking, query retrieval, reranking, and generation using retrieved context. Diagnose a wrong answer stage by stage.
- [ ] **35 minutes — Context management.** Explain scoped context loading, compaction, and durable working state. Review one concrete context-related failure from your experience.

### Completion evidence

- [ ] RepoCop's eval has a control task and a should-stop task, with results under both versions.
- [ ] Can distinguish retrieval-pipeline tuning from model fine-tuning.
- [ ] Can describe how a change in context or tools could alter outcomes with the same model.

## Phase 6 — Go a third layer deeper

**Budget: two and a half hours**

- [ ] **60 minutes — Repeat and compare.** In RepoCop, run each eval task several times under each version of the skill, keeping everything but its branch wording fixed, and compare the versions task by task.
- [ ] **45 minutes — Crash recovery and duplicate results.** Extend the job-service sketch with attempt IDs, duplicate-result handling, and persisted results. Trace a worker that crashes, and one that reports after its lease expired, and say which result is authoritative.
- [ ] **45 minutes — The results reader over HTTP.** Rehearse the Phase 1 results reader as an interview task, changed to fetch the JSONL from an HTTP API instead of a file, and test it through a fake client or mocked HTTP boundary so no test makes a network call. Include the reader work deferred in the progress log's 2026-11-12 row.

### Completion evidence

- [ ] RepoCop's eval has repeated results for both versions on every task, compared task by task.
- [ ] Can explain what was controlled and what still varies.
- [ ] Have a short result summary that states the small sample and remaining uncertainty.
- [ ] Can explain crash recovery without losing jobs or counting retries as independent successes.

## Phase 7 — Decide and explain

**Budget: three hours**

- [ ] **30 minutes — Timed coding on recurring mistakes.** Solve one timed problem on the most frequent mistakes so far, then repair them.
- [ ] **60 minutes — Metrics, grading, and adoption.** Review task success, consistency across trials, false positives/negatives, severity, latency, API cost, and human review effort. Discuss protected grading, PR review integration, permissions, advisory versus blocking checks, and explicit expansion/stop criteria.
- [ ] **45 minutes — Write a recommendation.** Decide whether RepoCop keeps the revised skill. Summarize the question, method, results, failure examples, limitations, and recommended next step in approximately one page. Include an alternative explanation for the findings. Then explain the experiment, its limitations, and the next experiment aloud, as in an interview.
- [ ] **45 minutes — Repocop with evidence.** Rehearse the Repocop story with what your evaluation measured: the problem, architecture, your decisions, one failure, and how you know the change helps.

### Completion evidence

- [ ] Can distinguish a model error, harness error, and grading error, including ambiguous cases.
- [ ] Have a recommendation proportional to the evidence, without claiming production readiness or general model superiority.
- [ ] Have a concise Repocop story with honest limits on measured outcomes.

## Phase 8 — Final rehearsal

**Budget: two and a half hours.** Run this phase just before the interview, whatever phase you've reached.

- [ ] **45 minutes — Coding mock with a variation.** Use a timed problem with no AI and the reference restrictions expected in the interview, then an unfamiliar variation of it, to check transfer rather than memorization. Explain the approach, implement it, test edge cases, and discuss complexity.
- [ ] **45 minutes — Technical mock.** Cover AI fundamentals, experiment design, failure diagnosis, and evaluation-service design at the depth reached. Use follow-ups that probe mechanisms and tradeoffs.
- [ ] **30 minutes — Failure-analysis and influence stories.** Rehearse a failure-analysis example and one specific influence story. Clearly identify your contribution, evidence, tradeoffs, and outcomes.
- [ ] **30 minutes — Final recall.** Review concise notes and update remaining risks.

### Completion evidence

- [ ] Mock results include concrete mistakes and corrections.
- [ ] Can discuss the evaluation project without relying on the written report.
- [ ] Have specific experience stories rather than general statements about working style.
- [ ] Remaining gaps are recorded honestly and prioritized.

## Evaluation project

You add evals to RepoCop as real work in that repository, so they're yours to put on your resume and discuss in the interview. This plan sets only the goal and the requirements: how you build the eval is up to you. This repository is where you learn the concepts and rehearse explaining the work.

### Why RepoCop needs one

On Nov 2, RepoCop's `implement` skill was revised (`d3b9bf8`) after a failure you saw. After working on one branch, you switched branches by hand and ran `/implement` without naming a requirement. The agent assumed it was still on the old branch, reported that branch's work as already done, and asked what to do next. The revision makes checking the branch the agent's first command. Nothing yet shows that it fixes the failure.

### Goal

Show, with evidence, whether the revised skill makes the agent work on the branch it's actually on rather than the one it remembers, and be able to explain how you know.

### Requirements

The finished eval meets all of these. Phases 3, 5 and 6 build up to them.

1. The old wording fails: the eval reproduces the stale-branch failure at least once.
2. Every run starts from the same repository, built fresh by a script.
3. A script grades each run from the repository afterwards: which branch it ended on, and what was committed where. The agent can't change that script.
4. The two versions differ only in the skill's branch wording. The old wording is in `54462fd`.
5. Each version runs several times on each task.
6. The keep-or-revert rule is written down before any run.
7. Each run records its result, time and tokens, and keeps its transcript.

### Scope limits

- Run the agent with an existing CLI. Don't build an agent framework.
- Running trials by hand is fine if automating them takes too long, as long as you record the steps.
- No dashboard, distributed runner or general benchmarking framework.

## Selected reference material

Use the sections that address a current exercise or knowledge gap. Reading the entire resource is optional.

- Python language and standard-library reference for the exercises. [Python documentation](https://docs.python.org/3/)
- Introductory LLM material for tokenization and model concepts. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1)
- Agent task design, grading, and evaluation practices. [Anthropic agent evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Process-level and end-to-end agent evaluation. Treat this as technical reading, not an interview syllabus. [NVIDIA agent evaluation article](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/)

## Recruiter questions

- Does the coding assessment emphasize algorithms/data structures, practical Python automation, or both?
- Is Python required, or may I use Go or C++ for algorithmic questions?
- Which documentation and other references are permitted?
- What rounds are planned, and which focus on AI fundamentals, evaluation design, systems, or past experience?

## Progress log

| Date | Phase/activity | Minutes | Evidence or artifact | Mistakes and unresolved questions | Next priority |
| ---- | -------------- | ------- | -------------------- | --------------------------------- | ------------- |
| 2026-11-12 | Phase 1 — Python through a useful program | 360 | `src/branch_eval/parse.py` (the results reader) and `tests/test_results.py`; `make check` passes. Ticked "Results reader runs on a small sample and reports errors visibly": the sample prints `pass: 4`, `fail: 1`, `error: 1`, and the malformed file stops at line 3, naming the missing `outcome`. Ticked "At least one meaningful test covers parsing or aggregation behavior": `test_valid_jsonl` asserts the exact counts and `test_invalid_jsonl` asserts a `ValueError` at line 3. Code written by hand, after a full Python refresh using tutorials and ChatGPT; corrections followed Claude's review and hints. Claude wrote no code. | From Claude's review, not yet reviewed by the human: passed the type `dict` instead of `result`, so the required-field check never fired; tests ran the code without asserting its results; a bare `except`; printed instead of returning, so it was hard to test; errors without a line number; raised a generic `Exception`, so `pytest.raises` couldn't target it. The minutes include a full Python refresh after six years away, so they don't represent the activity. | Inference and the agent loop. Phase 1 continues past its 240-minute budget, the overrun being the refresh. The activity's checkbox stays unticked: field types aren't checked yet. Deferred to Phase 4's rehearsal of the reader: type checks, blank lines, CLI errors through `sys.exit` or `argparse`, test paths relative to the test file, a test for a missing field other than `outcome`, naming. |
| 2026-11-13 | Phase 1 — Inference and the agent loop | 60 | Studied `reference/inference-and-agent-loop.md`, from a new `reference/` folder with a study guide for every activity, written by ChatGPT. Answered the guide's teach-back questions aloud and checked them against its answers. No explanation, notes or flow drawing saved. Nothing ticked: the activity and "Can explain inference and a tool-use loop in roughly two minutes from memory" need an explanation given in a session, reviewed and saved in a notes file, and the human moved on without one. Claude wrote no code. | None reported. | Two short coding exercises. Phase 1 continues past its 240-minute budget, with 420 minutes logged. The inference activity and its explain-from-memory check stay unticked until an explanation is reviewed. |
| 2026-11-13 | Phase 1 — One short coding exercise | 20 | `practice/p1_two_sum/`: `p1_two_sum.py`, its tests and `README.md`; `make check` passes. Ticked "Coding attempts and mistakes are saved": the README records the mistake Claude's review found and the correction. The activity stays unticked: its complexity hasn't been discussed. Code written by hand; Claude reviewed it and gave a failing input, `"aab"`, with a hint, and wrote no code. Minutes: the human reported 40 for both exercises, split evenly. The plan was reshaped this session into eight phases that take each topic in layers, with the second coding exercise moved to Phase 2; the freeze step for exercises was dropped; and Claude rewrote the `reference/` guides with spoiler sections and new teaching text, and renamed them by topic. | The second loop returned the position among the dictionary's distinct characters, not the position in the string, so `"aab"` gave 1 instead of 2; no test had a repeated character before the unique one. Fixed by storing each character's first index with its count. Open: the time and space complexity, and why the dictionary's insertion order gives the *first* unique character. | Rehearse a short Repocop story. Phase 1 continues past its 240-minute budget, with 440 minutes logged. The coding activity ticks once its complexity is discussed. |
| 2026-11-13 | Phase 2 — Group anagrams | 20 | `practice/p1_two_sum_2/`: `p1_two_sum_2.py`, its tests and `README.md`; `make check` passes. Done ahead of the plan, before Phase 1 finished. Ticked "The anagram attempt and its mistakes are saved": the README records Claude's review. The activity stays unticked: no test has a duplicated word, and the complexity hasn't been discussed. Code written by hand; Claude reviewed it and wrote no code. | From Claude's review: length buckets are redundant, since equal sorted letters imply equal length; `group = group.append(val)` sets `group` to `None`; the tests fix one order of groups, which the contract doesn't state; the parameter `input` shadows a built-in. Open: the complexity. | Retrieval versus fine-tuning, once Phase 1 is done. A duplicated-word test and the complexity discussion tick the activity. |
| 2026-11-14 | Phase 1 — Rehearse a short Repocop story | 5 | `practice/p1-activity-3/p1a3.md`, the story, and its `README.md` with Claude's review. Written as a casual opening that leaves the detail to follow-up questions. Nothing ticked: Claude's review found the story doesn't yet meet "Have a 60-second Repocop story covering the problem, the architecture, one decision and one failure", and the human moved on without revising it. Claude wrote no code. | From Claude's review, not yet reviewed by the human: no decision named as the human's, with its reason and tradeoff; no failure; no line between deterministic software and model decisions; "we" throughout, so the human's own part isn't clear; 228 words, about 90 seconds spoken. Open: why put the branch check in the skill's instructions rather than enforce it in code. | Retrieval versus fine-tuning. Phase 1 stopped at 445 minutes against its 240-minute budget, the overrun mostly the Python refresh. Unfinished, none blocking the next step: the results reader's field-type checks, with the rest of the 2026-11-12 row's deferred work, for Phase 6's results reader over HTTP; a saved explanation of inference and the agent loop, which Phase 2's explain-from-memory item asks for; the first-unique-character exercise's complexity discussion; a Repocop story with a decision, a failure and the line between deterministic software and model decisions, for Phase 4's Repocop rehearsal. |
| 2026-11-14 | Phase 2 — Retrieval versus fine-tuning | 10 | `practice/p2-a2/p2-a2-answer.md`, the explanation, and its `README.md` with Claude's review. Nothing ticked: the review found the explanation doesn't yet meet "Can say what retrieval and fine-tuning each change, and why retrieval suits a codebase that changes daily", and it hasn't been revised. After the review, Claude explained fine-tuning, listed the retrieval pipeline's settings and asked two follow-ups; the human answered one. Minutes: the human reported 5–10 for the answer; the rest of the session wasn't counted. Also this session: recall removed from `/study-start`, its flow in `specs/architecture.md`, the README and the plan's working rules; `reference/_index.md` added, listing each activity's guides and, for concept activities, one outside source whose link Claude checked; the opening line on time and spoilers removed from 21 guides. Claude wrote no code. | From Claude's review, not yet reviewed by the human: read "fine-tuning" as tuning the RAG pipeline, so what fine-tuning changes was left out; RAG described as supplying links rather than text the model generates its answer from; the case for retrieval with daily changes made without comparing it to fine-tuning; no mention that the query is embedded too, of exact-text search, or of why reranking is a second step. On the follow-up, split the review format (behavior) from yesterday's API change (knowledge) correctly, but reached for fine-tuning before trying the prompt. Open: when to search the live files with grep instead of an embedding index. | Tool schemas and MCP: the human moved on from p2a2. Left in p2a2: revising the explanation from memory to cover what fine-tuning changes, and the open follow-up. |
| 2026-11-15 | Phase 2 — Tool schemas and MCP | 15 | `practice/p2a3/p2a3-answer.md`, the explanation, and its `README.md` with Claude's review. Nothing ticked: the review found the activity not yet met, as the answer lists what tool descriptions and schemas contain without saying that the model chooses tools from the descriptions and writes arguments to fit the schema. The human chose to leave MCP's basics, such as host versus client and why MCP exists, to follow-up questions, which the review accepts at interview length. Minutes: Claude's estimate; the human didn't report a time. Claude wrote no code. | From Claude's review, not yet reviewed by the human: descriptions and schemas explained as protocol fields rather than as what the model reads to choose and call tools; clarifying questions before and after the answer read as hedging. Open: what to look at and change when an agent calls `search_code` instead of `read_file` on a path it already has. | Compare two agents. Left in p2a3: one sentence in the answer saying the model chooses tools from the descriptions and fills arguments from the schema, and the open follow-up. |
| 2026-11-15 | Phase 2 — Compare two agents | 20 | `practice/p2a4/p2a4-answer.md`, the answer, and its `README.md` with Claude's review. Nothing ticked: the review found "Can answer the 16-versus-14 question without claiming more than the totals show" not yet met, as the answer covers all six topics without answering whether the first agent is better. Before the answer was written, Claude explained "paired outcomes" with a 10-PR example. Minutes: Claude's estimate; the human didn't report a time. Claude wrote no code. | From Claude's review, not yet reviewed by the human: no verdict on whether the first agent is better, nor why two PRs out of 20 is weak evidence; not saying why only the PRs where the agents disagree count; what counts as success not questioned; sample size and representativeness treated as one point; no next experiment. Open: what to tell a manager, and run next, when the agents disagree on 6 PRs, 4 against 2. | Evaluation-service basics. Left in p2a4: a verdict up front and why two PRs out of 20 is weak evidence, and the open follow-up. |
| 2026-11-15 | Phase 2 — Evaluation-service basics | 25 | `practice/p2a5/p2a5-answer.md`, the sketch, left partly unfinished on purpose, and its `README.md` with Claude's review. Nothing ticked: the review found the activity not yet met. Before the sketch was written, Claude explained what a job lease is. Minutes: Claude's estimate; the human didn't report a time. Claude wrote no code. | From Claude's review, not yet reviewed by the human: jobs and attempts not told apart; how a worker claims a job left as TBD; the crash explained in one sentence; most of the answer on things outside "at its simplest". Open: how long a lease should be, and what goes wrong if it's too short or too long; what the records show for a job whose worker crashed and whose retry succeeded, and how many results it counts as. | Mini-mock. Left in p2a5: jobs and attempts, the claim mechanism, and the crash step by step. |
| 2026-11-15 | Phase 2 — Mini-mock | 0 | Skipped at the human's choice: the topics had just been studied, and they wanted to move on to new material. Nothing ticked: "Mini-mock answers are recorded, with the questions where you had to guess" has no answers. Phase 2 stopped at 90 of its 180 minutes, the human moving on to the next phase. Claude wrote no code. | None reported. | Define the experiment for S1. Unfinished in Phase 2, none blocking: none of its six activities is ticked. Its open completion items are the two-minute explanation of inference and a tool-use loop, what retrieval and fine-tuning each change, the 16-versus-14 verdict, and the mini-mock. p2a2 to p2a5 each have a short fix recorded in their rows and READMEs. Phase 4's mocks take these topics again. |

## Next session

- **Current phase:** Phase 3
- **First action:** Explain the eval.
- **Timebox:** 30 minutes.
- **Resume references:** This plan, including its Evaluation project, the latest progress-log entries, and the guides listed for p3a1 in `reference/_index.md`.
- **Known blockers:** Interview date and exact assessment format are unconfirmed.