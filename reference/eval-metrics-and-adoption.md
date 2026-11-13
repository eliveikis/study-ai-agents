# Metrics, grading, and adoption

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Choose what a positive verdict means

Suppose a review check flags a PR when it finds a defect. A true positive is a flagged real defect. A false positive consumes reviewer time on sound code. A false negative lets a real defect through. If your evaluation's "positive" instead means a task passed, define that convention explicitly before interpreting its errors.

In a hypothetical audit, a reviewer confirms 6 of 10 flagged findings and discovers 3 additional missed defects. Precision is 6/10: the fraction of flags that were real. Recall is 6/9: the fraction of known real defects that were found. Merely counting flags cannot reveal missed defects. You need an independent reference or human audit.

## Evaluate the whole workflow

Track successful tasks per attempted task and report execution errors separately. Compare repeated trials on the same task to see consistency. Record severity, latency including slow cases, API cost, and human minutes spent reviewing or correcting output. State which denominators and measurements are available. A single overwritten uncommitted file can outweigh several minor gains.

Keep reference checks outside the agent-controlled workspace. A grader is software with its own assumptions, so it has false positives and negatives of its own. Give a PR integration only the access its task requires. An advisory check posts information for a reviewer. A blocking check can prevent a merge, so false flags and service outages now affect delivery. Decide who owns appeals and how an outage is handled.

## Write a decision before expansion

A pilot rule makes adoption a decision you can check, rather than a drift. It names:

- **Scope:** where the check runs, and whether it advises or blocks.
- **Stop condition:** an outcome that pauses the pilot at once.
- **Expansion condition:** the quality, reviewer-effort and latency bounds results must meet, over which PRs.
- **Observation window:** how long, or how many PRs, before deciding.
- **Rollback:** the action that undoes it, and who owns it.

Supply your own bounds from the team's tolerances.

---

## ⚠️ SPOILERS: questions and answers

Prepare using only the text above this line. Everything below it asks the questions and then answers them.

### Questions

1. A check flags 8 PRs. A reviewer confirms 6 as real defects and finds 4 more that it missed. What are its precision and recall?
2. Why can't counting flags tell you about missed defects?
3. What changes when a check moves from advisory to blocking?
4. Write a pilot rule for introducing an advisory review check.
5. Why can an independent grader itself have false positives? Give a specific test that could expose one.
6. What evidence would justify switching a check from advisory to blocking?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Precision is 6/8, or 75%: the fraction of flags that were real. Recall is 6/10, or 60%: 6 found out of the 6 + 4 known real defects.
2. A missed defect produces no flag at all. Only an independent reference or a human audit can find it.
3. False flags and outages now stop merges, not just inform a reviewer. Someone must own appeals, and the team must decide what happens when the check is down.
4. For example: keep the check advisory on a limited set of PRs; pause on any confirmed loss of unrelated work; consider expanding only after audited results meet agreed quality, reviewer-effort and latency bounds across representative PRs. Name the observation window, the rollback action and its owner.
5. A grader is code with assumptions. It might check the behavior but not the branch, or accept output that only looks right. Expose that with a negative control: a known-incorrect result, such as a correct implementation on the wrong branch, which it must reject. Pair it with a known-good result it must accept.
6. Audited results over an agreed window, on representative PRs: false flags rare enough that blocks are almost always right, quality, reviewer-effort and latency within bounds, and acceptable availability. Plus an override and appeal path with an owner, and a rollback plan.
