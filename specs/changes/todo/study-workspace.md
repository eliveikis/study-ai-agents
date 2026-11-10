## Requirement

Set up this repository so the human can work through the five phases of [study_plan.md](../../../study_plan.md) without first deciding, each session, where work goes and how to record it. That means a Python project to write and check code in, a fixed place and template for each kind of study work, a tutor that teaches without doing the human's work, and two session routines that run the plan's own working rules: recall at the start of a session, and updating the progress log and next-session entry at the end. Today the repository holds only the plan and an empty spec workflow.

Study work (practice exercises, notes, the plan's log) is committed directly on the default branch. Only the evaluation harness, from Phase 2 on, is delivered as changes on their own branches. Code the human is meant to write is theirs to write: practice exercises and the `branch_eval` package, which starts in Phase 1 as the results reader and grows into the evaluation's grader and runner. Claude teaches and reviews that code, and writes it only when asked.

The plan requires that independent work and AI-assisted work stay distinguishable. That record lives with the work, in each exercise's README and in the session's progress-log row. It does not go in commits, which [.claude/rules/commits.md](../../../.claude/rules/commits.md) keeps free of AI credit.

Timings in the plan are targets. The human reports the time they spent; nothing in this change runs a timer.

## Acceptance Criteria

1. On a fresh clone, `uv sync` followed by `make check` passes. The check lints and tests all code except frozen first attempts, and it passes while no tests exist yet.
2. `uv run python -c "import branch_eval"` succeeds from the repository root, so later modules run as `uv run python -m branch_eval.<module>`.
3. `practice/README.md` gives the steps for an exercise: how to name its folder, writing the first attempt without AI (with the editor's inline AI completion turned off), freezing that attempt as `<slug>_attempt.py` the first time the human believes it works or is about to look something up or ask for help, then correcting it and running the check. It includes a README template to copy into each exercise, with headings for the problem, target time, time spent, approach and complexity, edge cases tested, mistakes, and assistance used. The assistance heading says what to write: none, which documentation, or what Claude did and for which part.
4. Exercises in two different practice folders, each with its own tests, both run under `make check` without clashing.
5. `specs/product.md` states the project's purpose, audience and design pillars. It links to `study_plan.md` for the phases, budget and scope limits rather than restating them, and names `study_plan.md` as the project's only progress record.
6. `specs/architecture.md` describes:
   - the repository layout: where exercises, notes, the `branch_eval` package and evaluation artifacts go
   - the trial record shared by Phase 1's results reader and Phase 2's runner: one JSON object per line, identifying the trial, scenario, configuration and attempt, with its outcome as pass, fail or error, any error message, and elapsed time
   - the flow of a study session
   - the trial-isolation decision: trial workspaces live outside this repository, because Claude Code loads `CLAUDE.md` files from a working directory's parents, which would put this repository's `CLAUDE.md` and `AGENTS.md` into every trial
   - a `_TBD_` for how far user-level configuration, such as `~/.claude/CLAUDE.md`, can be kept out of trials on a subscription login, where `--bare` is unavailable
7. `AGENTS.md` names the stack and the setup and check commands, and points to `specs/architecture.md` for the layout.
8. In a session in this repository, Claude:
   - gives a hint or asks for the human's attempt, not code, when asked to solve or fix an exercise whose first attempt isn't frozen yet
   - after the freeze, offers hints before code, and writes code only when asked
   - writes code in `branch_eval` only when asked, and says so, so the session's log row can record it
   - explains a concept at interview length first, then asks a follow-up question
   - never ticks a plan checkbox or advances a phase's status without evidence in the repository
9. `/study-start`:
   - At the start of a phase after the first, runs about five minutes of recall on the previous phase, drawn from its notes and recorded mistakes, and asks before revealing each answer.
   - Then states the current phase, the first action and its target time, taken from the plan's next-session entry and latest log row.
   - When the human says the activity is timed, notes the start time so it can report the elapsed time when they say they're done.
10. `/study-end`:
    - Asks for the minutes spent (self-reported), what was done, mistakes and open questions, and whether Claude wrote or fixed any code.
    - Appends a progress-log row with those answers, including any code Claude wrote.
    - Ticks only checkboxes whose evidence is in the repository, and asks about the rest.
    - Updates the phase's status and rewrites the next-session entry.
    - Asks whether to stop and record unfinished work once the phase's logged minutes pass its budget.
    - Points out any exercise README touched this session that lacks its time spent or assistance used.
    - Commits the updated plan.
11. When `/study-start` is run in sessions after the first one of a phase, given that the plan only asks for recall at the start of each phase, it will still output brief recall of the previous session's material.

## Out of scope

- The evaluation harness: fixture, scenarios, configurations, grader and runner. These are Phase 2 changes.
- A mock-interview skill, which is planned for Phase 3.
- Study material itself: the results reader, exercises, notes and stories.
- Changing the content of `study_plan.md`. Its phases, checklists and log belong to the human; `/study-end` writes to the log, phase status and next-session entry only when run.
- CI.
- [.gitignore](../../../.gitignore) ignores `eval/workspaces/`, which is no longer needed but left for the future in case we end up using these with api subscriptions.

## Implementation Notes

- A uv project on Python 3.12 with `branch_eval` in a `src/` layout, plus pytest and ruff as dev dependencies. Ruff selects at least `E`, `F` and `B` (bugbear flags mutable default arguments, a Phase 1 topic) and excludes `*_attempt.py`.
- Name exercise modules and tests after the exercise slug (`<slug>.py`, `test_<slug>.py`), never generically (`solution.py`). By default, pytest puts each test's folder on `sys.path`, so same-named modules in different folders collide.
- pytest exits with status 5 when it collects nothing. The check treats that as a pass.
- The tutoring rule goes in `.claude/rules/` with no `paths`, so it loads in every session.
- The skills follow [.claude/rules/skills.md](../../../.claude/rules/skills.md): neither names the other.
- The timed start is just the clock read in the session (for example `date`). It needs no timer or state file.
- `/study-end` commits `study_plan.md`. It lists any other uncommitted files from the session and commits only those the human confirms.
