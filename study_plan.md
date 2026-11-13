# AI Tools Interview Study Plan

## Purpose and constraints

Prepare for a Senior AI Engineer, AI tools role.

Budget approximately 20 hours or less. Work in phases of up to four hours. Each phase builds on the previous work and leaves a usable result if preparation stops there. Phases 1–4 cover every topic once and end in mock interviews. Phases 5–7 each take the topics one layer deeper, so a budget that runs out cuts depth rather than topics. The timings are targets, not requirements to finish every exercise.

The interview format and date are unconfirmed. This plan assumes live coding is plausible and prioritizes independent Python fluency, AI fundamentals, and a small evaluation that can be defended in discussion. Adjust the balance if the recruiter provides specific guidance.

## Starting assessment

| Area                 | Evidence from the diagnostic                                 | Preparation need                                             |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Software engineering | 15+ years of C++, five years of Go, developer tooling and API experience | Translate experience into concrete, concise examples         |
| Python               | Prior professional experience, currently rusty; extensive documentation needed | Practice writing, testing, and debugging without AI, including timed exercises |
| Agent workflows      | Built Repocop to synchronize agent development templates and expose spec workflow status | Explain personal design decisions, failures, and verified outcomes |
| AI fundamentals      | Gaps in tokenization, decoding, embeddings, fine-tuning, tool calling, and MCP | Build accurate explanations and connect them to workflow behavior |
| Evaluations          | Sensible reasoning about representativeness, quality, cost, and comparisons; no formal implementation experience | Complete a small reproducible experiment with independent grading and failure analysis |
| Systems and adoption | Relevant rate-limiter experience and broad engineering judgment | Practice durable job execution, CI tradeoffs, and explicit adoption criteria |

Coding fluency and project implementation details have not been independently assessed. This is a preparation guide, not a prediction of interview success.

## Working rules

- Timebox phases. When an activity overruns, cut its depth, not the topic: record what's left as unfinished, for that topic's next layer, and promote it only when it blocks an important next step.
- Begin each phase with five minutes of recall from the previous phase. Include this within the phase budget.
- End each phase by updating the progress log and next-session entry. Reserve time within the final activity.
- Write the first attempt at coding exercises without AI. Use documentation during learning exercises, then practice selected exercises without references.
- Explain the approach, edge cases, and time/space complexity aloud during timed coding.
- Keep explanations short enough for an interview, then practice follow-up questions.
- Prefer working code, recorded results, and corrected mistakes over extensive reading or polished infrastructure.
- Keep a record of assistance used so independent ability and AI-assisted work remain clear.

## Phase overview

| Phase | Focus                                                              | Main result                                          | Status      |
| ----- | ------------------------------------------------------------------ | ---------------------------------------------------- | ----------- |
| 1     | Python baseline, coding basics, inference and agent loop           | Working results reader and an initial skill baseline | In progress |
| 2     | A first layer of every other topic                                 | A first answer for every interview topic             | In progress |
| 3     | The smallest real evaluation, timed coding                         | S1 graded under both configurations                  | Not started |
| 4     | Mock interviews and repair                                         | Evidence of performance under interview conditions   | Not started |
| 5     | Second layer: remaining scenarios, reliability, retrieval, context | All four scenarios under both configurations         | Not started |
| 6     | Third layer: repeats, crash recovery, the reader over HTTP         | Repeated trials and a crash-safe service design      | Not started |
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

## Phase 3 — Run the smallest real evaluation

**Budget: three hours**

- [ ] **45 minutes — Define the experiment for S1.** Start from S1 in [Evaluation project scope](#evaluation-project-scope), below. Specify its starting repository state, expected branch behavior, and an independent success check. Record an experiment question and what evidence would support changing the workflow.
- [ ] **75 minutes — Run S1 under both configurations.** Build the disposable repository fixture and run S1 once under `baseline` and once under `state-check`, using an existing agent invocation method. Run the trials by hand if integration takes too long, and record the manual steps. Save actual outcomes, errors, elapsed time, and available traces.
- [ ] **30 minutes — Grade and inspect the result.** Write a small Python grader that checks the final branch from repository state. Check that it ran on both trials, and test it against a deliberately wrong result. Inspect a failure if one occurred, or a successful trace if not, and distinguish task failure from execution or grading errors.
- [ ] **30 minutes — Timed coding.** Solve one problem in Python against the clock, then repair mistakes. Prioritize strings, hash maps, sorting, two pointers, stacks/queues, or basic traversal according to earlier weaknesses. Explain complexity and test cases.

### Completion evidence

- [ ] A task definition, starting-state identifier, configuration, and outcome exist for each trial.
- [ ] Success is determined from repository state and acceptance checks, rather than the agent's completion message.
- [ ] A deliberately wrong outcome is rejected by the grader.
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
- [ ] **75 minutes — Run the remaining scenarios.** Define S2, S3 and S4 as you did S1, then run each once under both configurations, with the same fixture, grader, and settings. Save outcomes, errors, elapsed time, and available traces. If you automate the runs, fake the external invocation boundary in a test so runner behavior can be checked without paid calls.
- [ ] **40 minutes — Rate limits, retries, and timeouts.** Extend the job-service sketch with shared rate limits, a retry policy, timeouts, and the arithmetic for finishing overnight. Explain how to distinguish failed tasks from incomplete or broken executions.
- [ ] **30 minutes — The retrieval pipeline.** Explain embeddings, chunking, query retrieval, reranking, and generation using retrieved context. Diagnose a wrong answer stage by stage.
- [ ] **35 minutes — Context management.** Explain scoped context loading, compaction, and durable working state. Review one concrete context-related failure from your experience.

### Completion evidence

- [ ] All four scenarios have recorded results under both configurations.
- [ ] Can distinguish retrieval-pipeline tuning from model fine-tuning.
- [ ] Can describe how a change in context or tools could alter outcomes with the same model.

## Phase 6 — Go a third layer deeper

**Budget: two and a half hours**

- [ ] **60 minutes — Repeat and compare.** Compare the `baseline` and `state-check` configurations in [Evaluation project scope](#evaluation-project-scope): the original branch instruction and an explicit state-check instruction. Keep the model, tools, starting states, and budgets fixed where possible. Repeat selected scenarios under both configurations and report per-scenario outcomes.
- [ ] **45 minutes — Crash recovery and duplicate results.** Extend the job-service sketch with attempt IDs, duplicate-result handling, and persisted results. Trace a worker that crashes, and one that reports after its lease expired, and say which result is authoritative.
- [ ] **45 minutes — The results reader over HTTP.** Rehearse the Phase 1 results reader as an interview task, changed to fetch the JSONL from an HTTP API instead of a file, and test it through a fake client or mocked HTTP boundary so no test makes a network call. Include the reader work deferred in the progress log's 2026-11-12 row.

### Completion evidence

- [ ] Both configurations have recorded results on the same scenario set, with repeats on a subset.
- [ ] Can explain what was controlled and what still varies.
- [ ] Have a short result summary that states the small sample and remaining uncertainty.
- [ ] Can explain crash recovery without losing jobs or counting retries as independent successes.

## Phase 7 — Decide and explain

**Budget: three hours**

- [ ] **30 minutes — Timed coding on recurring mistakes.** Solve one timed problem on the most frequent mistakes so far, then repair them.
- [ ] **60 minutes — Metrics, grading, and adoption.** Review task success, consistency across trials, false positives/negatives, severity, latency, API cost, and human review effort. Discuss protected grading, PR review integration, permissions, advisory versus blocking checks, and explicit expansion/stop criteria.
- [ ] **45 minutes — Write a recommendation.** Summarize the experiment question, method, results, failure examples, limitations, and recommended next step in approximately one page. Include an alternative explanation for the findings. Then explain the experiment, its limitations, and the next experiment aloud, as in an interview.
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

## Evaluation project scope

### Initial question

When the branch changes outside the agent's session between tasks, does requiring the branch check as the agent's first command make `/implement` work on the current branch's requirement instead of the one it remembers?

### Origin

RepoCop's template `implement` skill gained its branch section in `54462fd` (Oct 30, requirement `implement-starts-its-branch`). `d3b9bf8` (Nov 2) revised it after two observed failures:

1. **Stale branch.** After a previous task on one branch, you switched branches by hand and ran `/implement` with no path. The agent assumed it was still on the previous branch, picked that branch's requirement, reported it already complete, and asked whether to start another. Checking the branch would have found the right requirement, still to do.
2. **Redundant check.** The agent ran `make check` before starting, though the checks had just run while completing the previous work.

The revision makes `git status --porcelain --branch` the first command, picks the branch from its output before reading or planning, requires the reply to open by naming the requirement and branch, and says not to run the check command before starting.

### Configurations

- `baseline`: the current skill with only its branch text reverted to the `54462fd` wording. Get the old text with `git -C ~/projects/repocop show 54462fd:templates/default-repo/.claude/skills/implement/SKILL.md`.
- `state-check`: the current skill (`d3b9bf8`).

Both keep the revised step 3, so the branch text is the only difference. Comparing step 3's two wordings is a separate follow-up experiment.

### Policy and scenarios

Derive the expected behavior from RepoCop's archived `implement-starts-its-branch` requirement, and define it before running trials.

A fresh session has no remembered branch, so it can't reproduce failure 1. Each trial therefore has three steps in one session:

1. A short previous turn, identical for both configurations and not using `/implement`.
2. The runner changes the repository outside the session, as you did by hand.
3. The task turn runs `/implement`.

| ID | Previous turn | Then the runner | Task turn | Expected |
| -- | ------------- | --------------- | --------- | -------- |
| S1 | On `old-task`: runs the checks and confirms old-task is done | Switches to the existing `new-task` | `/implement` (no path) | Implements `new-task.md` on `new-task` |
| S2 | On `new-task`: reads its requirement | Changes nothing | `/implement` (no path) | Same as S1 (control) |
| S3 | On `new-task` | Switches to `main` | `/implement` with the `new-task.md` path | Switches to `new-task` and implements there |
| S4 | On `old-task` | Switches to `main` and leaves an uncommitted file | `/implement` with the path | Stops, changes nothing |

Grade on the final repository state. Also record from each trace whether the agent checked the branch before its first switch or edit, and whether it ran `make check` before its first edit.

Use a disposable repository fixture with a tiny implementation task and a local bare repository as `origin` with its HEAD set, since the skill finds the default branch through `origin/HEAD`. Expand beyond these scenarios only if time remains.

### Minimal method

1. Save the specification, branch policy, task scenarios, and immutable starting-state identifiers.
2. Record agent/harness version, exact model identifier where available, instructions, permissions, and time/token limits.
3. Reset each trial to its designated starting state. Prevent one trial's edits, notes, or session history from influencing another.
4. Run the task and save the patch, final repository state, available trace, elapsed time, and token/cost information where exposed. Mark unavailable data explicitly.
5. Grade using evaluator-owned checks that the agent cannot edit. Verify final branch, required code behavior, and preservation of unrelated changes where relevant.
6. Check grading executed and report execution errors separately. Record scenario ID, configuration ID, and attempt ID.
7. Compare baseline and revised instructions on the same scenarios. Repeat a subset to investigate variability. Report counts and scenario-level differences.

This is a pilot evaluation of a narrow workflow behavior. A few tasks and repetitions support learning and diagnosis, with limited evidence for broader adoption claims.

### Scope limits

- Use an existing CLI or invocation path. Avoid building a new agent framework.
- If invocation integration consumes too much time, run trials manually and use Python to validate and summarize saved artifacts. Record the manual steps.
- Keep grading separate from the agent's workspace and control. Check what permissions the agent actually has.
- Use fakes to test the runner. Use real agent executions for conclusions about agent behavior.
- Add no dashboard, distributed runner, plugin system, or general benchmarking framework during this preparation cycle.

## Selected reference material

Use the sections that address a current exercise or knowledge gap. Reading the entire resource is optional.

- Python language and standard-library reference for the exercises. [Python documentation](https://docs.python.org/3/)
- Introductory LLM material for tokenization and model concepts. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1)
- Agent task design, grading, and evaluation practices. [Anthropic agent evaluation guide](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
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

## Next session

- **Current phase:** Phase 1
- **First action:** Rehearse a short Repocop story.
- **Timebox:** 20 minutes.
- **Resume references:** This plan, the latest progress-log entries and `reference/repocop-story.md`.
- **Known blockers:** Interview date and exact assessment format are unconfirmed.