# P1A4 — Record gaps and rehearse Repocop

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 30-minute timebox, including study.

## Build a story from one observed incident

Start with the developer’s task. Someone finished work on one branch, switched branches manually, and asked the agent to implement the next requirement. The agent relied on the previous branch and reported the earlier task complete. Someone listening now knows what failed and why it mattered.

Distinguish three sources of information. Git can report the current branch from repository state. A template can instruct an agent when to request that information. The model still chooses its next action. An instruction to run a check and an application that enforces a check make different guarantees.

## Make a two-minute version

- **First 20 seconds:** Who used RepoCop and what repetitive work did it handle? Explain what template synchronization distributes.
- **Next 40 seconds:** Trace one template change from its source to a consuming repository. Name the component you personally changed and one decision you owned. Check those details against a real artifact.
- **Next 40 seconds:** Tell the stale-branch incident. Explain how checking live branch state before planning addresses the observed failure. Name a plausible remaining failure even with the revision.
- **Last 20 seconds:** State what evidence you have. A commit shows a change landed. A trace shows behavior on one run. An adoption or reliability claim needs evidence at that level.

## Test your explanation

Answer “Why put the instruction there?” and “How would you know it helped?” aloud. If you lack before-and-after measurements, describe the paired branch experiment as proposed work. Save the short story and two gaps in the progress log. For each gap, record a concrete next check, such as explaining token IDs from memory or writing a dictionary test unaided.
