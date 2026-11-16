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
5. `/implement specs/changes/todo/feature-a.md` is run on the agent.
6. The agent checks its current branch to see if feature-a branch is checkout out, changes it if not, and implements.
7. The Test checks the current branch and where files were added.
8. Success is determined by 5 runs all with the correct branch and files. Global success criteria should be graded as well, but these could potentially be layered in, including agent behavior trace review, human review, error log review.

## What would make me consider dropping the new skill changes

1. if I cannot easily reproduce the failure with the old behavior/skill.
2. if cost goes up tremendously in terms of token usage, time, github calls
3. if other negative effects are observed, e.g. new regressions
