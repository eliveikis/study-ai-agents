# AI Tools Interview Study Plan

## Purpose and constraints

Prepare for a Senior AI Engineer, AI tools role.

Budget approximately 20 hours or less. Work in phases of up to four hours. Each phase builds on the previous work and leaves a usable result if preparation stops there. The timings are targets, not requirements to finish every exercise.

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

- Timebox phases. Record unfinished work and promote it only when it blocks an important next step.
- Begin each phase with five minutes of recall from the previous phase. Include this within the phase budget.
- End each phase by updating the progress log and next-session entry. Reserve time within the final activity.
- Write the first attempt at coding exercises without AI. Use documentation during learning exercises, then practice selected exercises without references.
- Explain the approach, edge cases, and time/space complexity aloud during timed coding.
- Keep explanations short enough for an interview, then practice follow-up questions.
- Prefer working code, recorded results, and corrected mistakes over extensive reading or polished infrastructure.
- Keep a record of assistance used so independent ability and AI-assisted work remain clear.

## Phase overview

| Phase | Focus                                                      | Main result                                          | Status      |
| ----- | ---------------------------------------------------------- | ---------------------------------------------------- | ----------- |
| 1     | Python baseline, coding basics, inference and agent loop   | Working results reader and an initial skill baseline | Not started |
| 2     | Small evaluation, independent grading, RAG and fine-tuning | First complete evaluation run                        | Not started |
| 3     | Timed coding, controlled comparison, context and MCP       | Repeated trials and stronger interview explanations  | Not started |
| 4     | Reliability, evaluation decisions, targeted coding         | One-page recommendation and service design           | Not started |
| 5     | Mock interviews and targeted repair                        | Evidence of performance under interview conditions   | Not started |

## Phase 1 — Establish the foundation

**Budget: four hours**

- [ ] **90 minutes — Python through a useful program.** Write a command-line program that reads a JSONL file of evaluation results and prints how many results have each outcome. Practice file handling, dictionaries/lists, functions, exceptions, and simple tests. Review mutability, default arguments, and iteration as needed.
  - **Input:** one JSON object per line. Each is the result of one trial in the evaluation you build in Phase 2: one run of an AI agent on one test scenario. Its fields are in [specs/architecture.md › Trial record](specs/architecture.md#trial-record).
  - **Output:** one line per outcome with its count, such as `pass: 4`.
  - **Malformed input:** a line that isn't a valid trial record stops the program with an error that gives the line number and what's wrong.
  - **Samples:** [tests/data/results_sample.jsonl](tests/data/results_sample.jsonl) gives `pass: 4`, `fail: 1` and `error: 1`. [tests/data/results_malformed.jsonl](tests/data/results_malformed.jsonl) fails at line 3, which has no `outcome`.
  - **Where:** the program goes in `src/branch_eval/` and its tests in `tests/`. `make check` lints and runs the tests.
- [ ] **60 minutes — Inference and the agent loop.** Learn and explain tokens, context windows, next-token probabilities, sampling versus greedy decoding, and training versus inference. Draw the flow from model tool-call request to harness execution to returned result. Distinguish the model, harness, and tools.
- [ ] **60 minutes — Two short coding exercises.** Use Python for a string problem and a list/dictionary problem. Attempt each before checking a solution. Discuss complexity and test empty inputs, duplicates, and boundaries where applicable. Follow [practice/README.md](practice/README.md) for each.
  - **String:** given a string, return the index of its first character that appears only once, or -1 if there is none.
  - **List/dictionary:** given a list of words, return them grouped so that each group holds words that are anagrams of each other.
- [ ] **30 minutes — Record gaps and rehearse Repocop.** Explain the problem, architecture, your decisions, one failure, and how you know the tool helps. Distinguish deterministic software from model decisions. Record unresolved Python and AI concepts.

### Completion evidence

- [ ] Results reader runs on a small sample and reports errors visibly.
- [ ] At least one meaningful test covers parsing or aggregation behavior.
- [ ] Coding attempts and mistakes are saved.
- [ ] Can explain inference and a tool-use loop in roughly two minutes from memory.
- [ ] Have a concise Repocop story with honest limits on measured outcomes.

## Phase 2 — Complete a small evaluation

**Budget: four hours**

- [ ] **60 minutes — Define the experiment.** Start from the four scenarios in [Evaluation project scope](#evaluation-project-scope), below. Specify starting repository state, expected branch behavior, and independent success checks. Record an experiment question and what evidence would support changing the workflow.
- [ ] **90 minutes — Run real trials.** Implement a minimal Python runner or validator and execute trials using an existing agent invocation method. Save actual outcomes, errors, elapsed time, and available traces. Fake the external invocation boundary in a test so runner behavior can be checked without paid calls.
- [ ] **45 minutes — Inspect the results.** Check that grading ran, inspect at least one failure if any occur, and distinguish task failure from execution or grading errors. If every trial succeeds, inspect a successful trace and deliberately test the grader against a known incorrect result.
- [ ] **45 minutes — Retrieval and training.** Explain embeddings, chunking, query retrieval, reranking, and generation using retrieved context. Explain what fine-tuning changes. Discuss why retrieval is a plausible starting point for a private codebase that changes daily.

### Completion evidence

- [ ] A task definition, starting-state identifier, configuration, and outcome exist for each trial.
- [ ] Success is determined from repository state and acceptance checks, rather than the agent's completion message.
- [ ] A deliberately wrong outcome is rejected by the grader.
- [ ] Have a short result summary that states the small sample and remaining uncertainty.
- [ ] Can distinguish retrieval-pipeline tuning from model fine-tuning.

## Phase 3 — Strengthen interview execution

**Budget: four hours**

- [ ] **90 minutes — Timed coding and correction.** Solve one or two problems in Python, then repair mistakes. Prioritize strings, hash maps, sorting, two pointers, stacks/queues, or basic traversal according to Phase 1 weaknesses. Explain complexity and test cases.
- [ ] **60 minutes — Repeat and compare.** Compare the `baseline` and `state-check` configurations in [Evaluation project scope](#evaluation-project-scope): the original branch instruction and an explicit state-check instruction. Keep the model, tools, starting states, and budgets fixed where possible. Repeat selected scenarios under both configurations and report per-scenario outcomes.
- [ ] **45 minutes — Context, tool schemas, and MCP.** Explain scoped context loading, compaction, durable working state, tool descriptions/argument schemas, and MCP's role between host/client and server. Review one concrete context-related failure from your experience.
- [ ] **45 minutes — Evaluation interview rehearsal.** Explain your experiment, limitations, and next experiment. Practice this question: two versions of a code-review agent each review the same 20 pull requests, and one succeeds on 16 while the other succeeds on 14. Is the first one better? Cover task coverage, paired outcomes, repeated runs, quality, cost, and time.

### Completion evidence

- [ ] Have a timed coding result and a short list of recurring mistakes.
- [ ] Both configurations have recorded results on the same scenario set, with repeats on a subset.
- [ ] Can explain what was controlled and what still varies.
- [ ] Can describe how a change in context or tools could alter outcomes with the same model.

## Phase 4 — Add reliability and decision-making

**Budget: four hours**

- [ ] **75 minutes — Targeted coding practice.** Address the most frequent prior mistakes. Include an unfamiliar variation to check transfer rather than memorization. Rehearse the Phase 1 results reader as an interview task, changed to fetch the JSONL from an HTTP API instead of a file, and test it through a fake client or mocked HTTP boundary so no test makes a network call.
- [ ] **60 minutes — Evaluation-service design.** Sketch a service for 1,000 overnight jobs. Cover bounded concurrency, a durable queue, job leases, retry policy, shared rate limits, timeouts, attempt IDs, duplicate-result handling, and persisted results. Explain how to distinguish failed tasks from incomplete or broken executions.
- [ ] **60 minutes — Metrics, grading, and adoption.** Review task success, consistency across trials, false positives/negatives, severity, latency, API cost, and human review effort. Discuss protected grading, PR review integration, permissions, advisory versus blocking checks, and explicit expansion/stop criteria.
- [ ] **45 minutes — Write a recommendation.** Summarize the experiment question, method, results, failure examples, limitations, and recommended next step in approximately one page. Include an alternative explanation for the findings.

### Completion evidence

- [ ] Can explain crash recovery without losing jobs or counting retries as independent successes.
- [ ] Can distinguish a model error, harness error, and grading error, including ambiguous cases.
- [ ] Have a recommendation proportional to the evidence, without claiming production readiness or general model superiority.

## Phase 5 — Rehearse and repair

**Budget: four hours**

- [ ] **60 minutes — Coding mock.** Use a timed problem with no AI and the reference restrictions expected in the interview. Explain the approach, implement it, test edge cases, and discuss complexity.
- [ ] **60 minutes — Technical mock.** Cover AI fundamentals, experiment design, failure diagnosis, and evaluation-service design. Use follow-ups that probe mechanisms and tradeoffs.
- [ ] **60 minutes — Repair the largest exposed gap.** Choose based on the mock results. Produce a corrected implementation or explanation, then retry without notes.
- [ ] **60 minutes — Experience and final recall.** Rehearse Repocop, the LLM API rate limiter, a failure-analysis example, and one specific influence story. Clearly identify your contribution, evidence, tradeoffs, and outcomes. Review concise notes and update remaining risks.

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
|      |                |         |                      |                                   |               |

## Next session

- **Current phase:** Phase 1
- **First action:** Python through a useful program.
- **Timebox:** 90 minutes, including tests and correction.
- **Resume references:** This plan and the latest progress-log entry.
- **Known blockers:** Interview date and exact assessment format are unconfirmed.