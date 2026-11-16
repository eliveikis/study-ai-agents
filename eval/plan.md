# Q

Your question: one sentence saying what you want to find out from S1.

The starting setup: exactly what the test repository looks like before each run, precisely enough to rebuild it identically every time. Which branches exist, what's on each, which requirement files are where, and which branch is checked out.

What a correct agent does: the right behavior in S1, taken from the RepoCop requirement that defined it.

How you'll judge pass or fail: by inspecting the repository afterwards, never by trusting what the agent says it did. That's what "independent success check" means.

What would change your mind: decided before you run anything. What results would make you keep the new wording, go back to the old one, or say you need more runs?

# A

## This particular test case repo setup would be:

Branches:
    - main
        - repocop template synced
        - specs/changes/todo/
            - feature-a.md

## Requirements

feature-a.md
    - a simple requirement that says to create a file in the repository, for testing purposes
    - a single AC, that a file feature-a.out is present in the root

## Correct agent

1. Agent starts in main branch.
2. Agent is told to create and checkout the feature-a branch to prepare for work there.
3. At this point, the agent should think it is in feature-a branch.
4. Test checks out main in CLI, does not notify agent.
5. `/implement` is run on the agent.
6. The agent checks its current branch to see if feature-a branch is checkout out, changes it if not, and implements.
7. The Test checks the current branch and where files were added.
8. Success is determined by 5 runs all with the correct branch and files. Global success criteria should be graded as well, but these could potentially be layered in, including agent behavior trace review, human review, error log review.

## What would make me consider dropping the new skill changes

1. if I cannot easily reproduce the failure with the old behavior/skill.
2. if cost goes up tremendously in terms of token usage, time, github calls
3. if other negative effects are observed, e.g. new regressions

---

# S1 experiment, revised

Your plan with the five review changes applied. Claude wrote this version.

**What S1 is.** The study plan names four test situations, S1 to S4, in its Evaluation project scope section. S1 recreates the bug you hit. The agent finishes work on one branch, you switch branches by hand without telling it, and then you run `/implement` without naming a requirement. The bug was that it assumed it was still on the old branch. The experiment runs S1 under two versions of the `implement` skill: `baseline`, the old wording, and `state-check`, the new wording that makes checking the branch the agent's first command.

## Question

After a turn on `old-task` and a switch to `new-task` outside the session, does `/implement` with no path implement `new-task` under `state-check`, where it doesn't under `baseline`?

## Starting setup

A fixture script builds a fresh repository outside this one, the same way every time. Outside, so this repository's `CLAUDE.md` doesn't load into the trial.

- `main`: the RepoCop template at a recorded commit, with the configuration's `implement` skill (`baseline` or `state-check`), and two requirements in `specs/changes/todo/`:
  - `old-task.md`: create `old-task.out` in the root.
  - `new-task.md`: create `new-task.out` in the root.
- `old-task`: off `main`, with a commit adding `old-task.out`, so it's done.
- `new-task`: off `main`, with nothing added yet.
- `origin`: a local bare repository, with its HEAD set to `main`.
- Checked out: `old-task`.

The script prints each branch's commit SHA. Save them with the trial.

## Trial steps

The runner's part, the same for both configurations:

1. Run the fixture script for the configuration, and save the SHAs.
2. Start a new agent session in the fixture.
3. Previous turn, word for word: "Run the checks and confirm old-task is done."
4. Outside the session, without telling the agent: `git switch new-task`.
5. Task turn: `/implement`, with no path.
6. Run the grader. Save the transcript, the elapsed time and the token count where shown.

## What a correct agent does

It implements `new-task.md` on `new-task`: it commits `new-task.out` there and changes no other branch.

The failure this tests for: it assumes it's still on `old-task`, reports that as done, and asks what's next.

## Success check

A Python grader reads the fixture's repository after the trial, and the agent can't edit the grader. The trial passes when all three hold:

1. The current branch is `new-task`.
2. `new-task` has new commits on top of its saved SHA, and `new-task.out` is in its root.
3. `main` and `old-task` are still at their saved SHAs.

Otherwise it fails. If the trial couldn't run or be graded, record an error instead.

Not graded, but noted from the transcript: whether the agent checked the branch before its first switch or edit, and whether it ran `make check` before its first edit.

## Decision rule

Decided before running:

- **Keep** `state-check` if it passes and `baseline` fails.
- **Revert** if `state-check` fails, or costs over twice `baseline`'s tokens or time.
- **Unsure** if both pass or both fail. Both passing means the failure didn't reproduce: repeat the runs, or make the scenario harder.

This is a pilot, with one run per configuration, so a result is a signal to investigate, not proof. Repeats come in Phase 6. Regressions are checked in Phase 5 by S2, the same steps with no branch switch, where both versions should pass.
