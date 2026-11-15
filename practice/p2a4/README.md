# Compare two agents

## Activity

Phase 2, "Compare two agents": two versions of a code-review agent each review the same 20 pull requests, and one succeeds on 16 while the other succeeds on 14. Is the first one better? Cover task coverage, paired outcomes, repeated runs, quality, cost, and time. It is evidence for the completion item "Can answer the 16-versus-14 question without claiming more than the totals show."

## Time spent

Not reported.

## Review

What it gets right:

- **"Better" needs defining first:** on which tasks, at what cost, quality and time.
- **Task coverage, beyond "is it representative":** each task's importance and how often its kind of task comes up in practice, so that a minor but frequent task counts.
- **Paired outcomes:** focus on the PRs where the agents differ, and ask why one failed and the other didn't.
- **Repeated runs** of the same PR, to see whether results are consistent.
- **Quality, cost and time:** grading the work even when both pass, tokens and human effort, time per task.
- It claims nothing the totals don't show.

What's missing:

- **No answer to "Is the first one better?"** The completion item asks for exactly that. The answer is: not from these totals. With 20 PRs, each PR is 5 percentage points, and the gap is two PRs, which one rerun could erase. At most, it's a weak hint worth testing.
- **Why the disagreements matter isn't said.** PRs that both agents pass or both fail say nothing about which is better. Only the disagreements count, and how many there are sets how strong the evidence is: 2 against 0 is weak, and so is 4 against 2.
- **What "success" means isn't questioned.** For a code-review agent, did it find the real defect, and did it add false alarms? Who judged success, and would they judge it the same way again?
- **Sample size and representativeness are mixed together.** Whether the PRs are the right kind is coverage. Whether there are enough of them is statistical power. They're separate problems with separate fixes.
- **No next step.** The strongest close is the experiment you'd run: more PRs, several runs per PR for each agent, the paired disagreements counted, and quality and cost recorded.

Spoken, it works best in this order: the verdict first, then two or three reasons, then what you'd run to find out. The checklist suits writing, not speaking.

Verdict: **doesn't meet the item yet.** It covers all six topics well, but never answers the question or says why two PRs out of 20 is weak evidence. Two sentences would fix it.

## Assistance used

Before writing, Claude explained what "paired outcomes" means, with a 10-PR example of identical totals that hide different disagreements. Otherwise not reported.
