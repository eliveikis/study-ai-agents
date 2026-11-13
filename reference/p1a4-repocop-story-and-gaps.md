# P1A4 — Record gaps and rehearse Repocop

Use 10–20 minutes to study the material below. The full activity has a 30-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Build a story from one observed incident

Start with the developer's task. Someone finished work on one branch, switched branches manually, and asked the agent to implement the next requirement. The agent relied on the previous branch and reported the earlier task complete. Someone listening now knows what failed and why it mattered.

## Deterministic software and model decisions

Deterministic software gives the same output for the same input every time, so you can test it and rely on it. Git reporting the current branch is deterministic: `git status --branch` reads repository state. Copying template files into a repository is too. A model's next action isn't: it depends on everything in its context, and sampling can vary it between runs.

That gives three sources of information. Git can report the current branch from repository state. A template can instruct an agent when to request that information. The model still chooses its next action. An instruction to run a check and an application that enforces a check make different guarantees: the instruction makes the check likely, while enforcement makes it certain, because code outside the model runs it whatever the model decides.

## Kinds of evidence

A commit shows a change landed. A trace shows behavior on one run. A claim that a change helps needs a comparison: the same situation with and without the change, more than once. An adoption or reliability claim needs evidence at that level. When you don't have it, say what you would run to get it.

## Make a two-minute version

- **First 20 seconds:** Who used RepoCop and what repetitive work did it handle? Explain what template synchronization distributes.
- **Next 40 seconds:** Trace one template change from its source to a consuming repository. Name the component you personally changed and one decision you owned. Check those details against a real artifact.
- **Next 40 seconds:** Tell the stale-branch incident. Explain how checking live branch state before planning addresses the observed failure. Name a plausible remaining failure even with the revision.
- **Last 20 seconds:** State what evidence you have, and what it does and doesn't show.

Save the short story and two gaps in the progress log. For each gap, record a concrete next check, such as explaining token IDs from memory or writing a dictionary test unaided.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them. The story itself is yours; the answers give the points an interviewer listens for.

### Questions

1. Why put the branch check in the skill's instructions, as the agent's first command?
2. How would you know the revision helped?
3. What does an instruction give you that an enforced check doesn't, and the other way round?
4. Name a plausible failure that remains even with the revision.

**Stop here.** Answer every question aloud before you read on.

### Answers

1. The failure came from the model acting on what it remembered instead of what was true. The skill's instructions are in context at the moment the model decides where to work, and making the check the first command puts the live branch into context before any planning. The tradeoff: it's still an instruction, so the model can skip it.
2. Not from the commit, and not from one good run. You'd compare both wordings on the same scenarios, the stale-branch one included, with repeats, and grade the final repository state. Until you've run that in Phases 2 and 3, describe it as proposed work.
3. An instruction is cheap and flexible, and it can ask for judgement, such as choosing the requirement that matches the branch. Nothing makes the model follow it. An enforced check, such as a hook the harness runs, always runs, but it can only do what code can decide, and it's one more piece to maintain.
4. Any of these: the model skips or misreads the check; the branch changes again after the check, mid-task; the branch name matches no requirement; uncommitted work in the tree gets disturbed.
