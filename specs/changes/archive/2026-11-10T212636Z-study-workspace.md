## Requirement

Set up this repository so the human can work through the five phases of [study_plan.md](../../../study_plan.md) without first deciding, each session, where work goes and how to record it. That means a Python project to write and check code in, a fixed place and template for each kind of study work, a tutor that teaches without doing the human's work, and two session routines that run the plan's own working rules: recall at the start of a session, and updating the progress log and next-session entry at the end. Today the repository holds only the plan and an empty spec workflow.

Study work (practice exercises, notes, the plan's log) is committed directly on the default branch. Only the evaluation harness, from Phase 2 on, is delivered as changes on their own branches. Code the human is meant to write is theirs to write: practice exercises and the `branch_eval` package, which starts in Phase 1 as the results reader and grows into the evaluation's grader and runner. Claude teaches and reviews that code, and writes it only when asked.

The plan requires that independent work and AI-assisted work stay distinguishable. That record lives with the work, in each exercise's README and in the session's progress-log row. It does not go in commits, which [.claude/rules/commits.md](../../../.claude/rules/commits.md) keeps free of AI credit.

Timings in the plan are targets. The human reports the time they spent; nothing in this change runs a timer.

## Acceptance Criteria

1. On a fresh clone, `uv sync` followed by `make check` passes. The check lints and tests all code except frozen first attempts, and it passes while no tests exist yet.
2. `uv run python -c "import branch_eval"` succeeds from the repository root, so later modules run as `uv run python -m branch_eval.<module>`.
3. `practice/README.md` gives the steps for an exercise: naming it as a folder `practice/<slug>/`, where the slug starts with the phase, such as `p1_two_sum`, and ends in `_2` for a repeat in the same phase, so no two exercises share a file name; writing the first attempt without AI (with the editor's inline AI completion turned off); freezing that attempt as `<slug>_attempt.py` the first time the human believes it works or is about to look something up or ask for help; then correcting it and running the check. It includes a README template to copy into each exercise, with headings for the problem, target time, time spent, approach and complexity, edge cases tested, mistakes, and assistance used. The assistance heading says what to write: none, which documentation, or what Claude did and for which part.
4. Exercises in two different practice folders, each with its own tests, both run under `make check` without clashing, even when both are the same problem.
5. `specs/product.md` states the project's purpose and audience, and these design pillars, ranked: independent ability stays measurable; `study_plan.md` is the only progress record, and what it claims has evidence; working code and recorded results come before infrastructure; a session takes little ceremony. It links to `study_plan.md` for the phases, budget and scope limits rather than restating them.
6. `specs/architecture.md` describes:
   - the repository layout: where exercises, notes, the `branch_eval` package and evaluation artifacts go
   - the trial record shared by Phase 1's results reader and Phase 2's runner: one JSON object per line, identifying the trial, scenario, configuration and attempt, with its outcome as pass, fail or error, any error message, and elapsed time. Readers ignore fields they don't know, so Phase 2's runner can add its own.
   - the flow of a study session
   - the trial-isolation decision: trial workspaces live outside this repository, because Claude Code loads `CLAUDE.md` files from a working directory's parents, which would put this repository's `CLAUDE.md` and `AGENTS.md` into every trial
   - a `_TBD_` for how far user-level configuration and state, such as `~/.claude/CLAUDE.md`, user skills and auto memory, can be kept out of trials on a subscription login, where `--bare` is unavailable
7. `AGENTS.md` names the stack and the setup and check commands, and points to `specs/architecture.md` for the layout.
8. In a session in this repository, Claude:
   - gives a hint or asks for the human's attempt, not code, when asked to solve or fix an exercise whose first attempt isn't frozen yet (its `<slug>_attempt.py` doesn't exist)
   - after the freeze, offers hints before code, writes code only when asked, and never edits the frozen attempt
   - writes code in `branch_eval` only when asked, and says so, so the session's log row can record it
   - explains a study concept at interview length (about two minutes spoken) first, then asks a follow-up question
   - never ticks a plan checkbox or advances a phase's status without evidence in the repository: a file it can name, such as an exercise, a test, a notes file or an evaluation artifact. For an item the human shows rather than builds, such as "Can explain … from memory" or "Have a concise Repocop story", the evidence is the human's own explanation or story, given in the session without notes. Claude reviews it against the item and the topics the phase's activities list, then saves it with that review in a notes file. It counts only when the review finds the item met.
9. `/study-start`:
   - Opens with recall, asking before revealing each answer. In a phase's first session (the phase has no log row yet), that's about five minutes on the previous phase, drawn from its notes and recorded mistakes. In a later session, it's a brief recall of the previous session's work. The plan's very first session has none.
   - Then states the current phase, the first action and its target time, taken from the plan's next-session entry and latest log row.
   - When the human says the activity is timed, notes the start time so it can report the elapsed time when they say they're done.
10. `/study-end`:
    - Asks for the minutes spent (self-reported), what was done, mistakes and open questions, and whether Claude wrote or fixed any code.
    - Appends one progress-log row for each phase worked on in the session, with those answers, including any code Claude wrote. The date is `YYYY-MM-DD`, the phase/activity is `Phase N — <activity titles as the plan names them>`, and the minutes are a whole number. The first row replaces the log's blank placeholder row.
    - Ticks only checkboxes that have evidence as criterion 8 defines it, names that evidence in the row, and asks about the rest.
    - Sets the phase's status to `In progress` at its first logged session and to `Done` when the human confirms the phase is finished, and rewrites the next-session entry.
    - Once the phase's logged minutes pass its budget, asks whether to stop the phase. If the human stops, it records the unfinished work in the row's next priority, and makes it the next-session entry's first action only when the human says it blocks the next step.
    - Points out any exercise README that lacks its time spent or assistance used.
    - Commits the updated plan when on `main`. On any other branch, it says so and leaves the commit to the human.

## Out of scope

- The evaluation harness: fixture, scenarios, configurations, grader and runner. These are Phase 2 changes.
- A mock-interview skill, which is planned for Phase 3.
- Study material itself: the results reader, exercises, notes and stories.
- Changing the content of `study_plan.md`. Its phases, checklists and log belong to the human; `/study-end` writes to the log, phase status, evidenced checkboxes and next-session entry only when run.
- CI.
- Removing `eval/workspaces/` from [.gitignore](../../../.gitignore). It's no longer needed, but stays in case trials later run on an API key.

## Implementation Notes

- A uv project on Python 3.12 with `branch_eval` in a `src/` layout, plus pytest and ruff as dev dependencies. Ruff selects at least `E`, `F` and `B` (bugbear flags mutable default arguments, a Phase 1 topic) and excludes `*_attempt.py`.
- Exercise modules and tests are named after the slug (`<slug>.py`, `test_<slug>.py`), never generically (`solution.py`). By default, pytest puts each test's folder on `sys.path`, so same-named modules in different folders collide. That's why a slug carries the phase and a repeat number.
- pytest exits with status 5 when it collects nothing. The check treats that as a pass.
- The tutoring rule goes in `.claude/rules/` with no `paths`, so it loads in every session.
- The skills follow [.claude/rules/skills.md](../../../.claude/rules/skills.md): neither names the other.
- The timed start is just the clock read in the session (for example `date`). It needs no timer or state file.
- `/study-end` commits `study_plan.md`. It lists any other uncommitted files from the session and commits only those the human confirms.
- Check criterion 4 and the two skills in a throwaway clone, with sample exercises and plan entries, and commit none of them: study material and the plan's log stay out of this change.
