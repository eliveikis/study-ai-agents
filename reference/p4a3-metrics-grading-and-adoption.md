# P4A3 — Metrics, grading, and adoption

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## Choose what a positive verdict means

Suppose a review check flags a PR when it finds a defect. A true positive is a flagged real defect. A false positive consumes reviewer time on sound code. A false negative lets a real defect through. If your evaluation’s “positive” instead means a task passed, define that convention explicitly before interpreting its errors.

In a hypothetical audit, a reviewer confirms 6 of 10 flagged findings and discovers 3 additional missed defects. Precision is 6/10: the fraction of flags that were real. Recall is 6/9: the fraction of known real defects that were found. Merely counting flags cannot reveal missed defects. You need an independent reference or human audit.

## Evaluate the whole workflow

Track successful tasks per attempted task and report execution errors separately. Compare repeated trials on the same task to see consistency. Record severity, latency including slow cases, API cost, and human minutes spent reviewing or correcting output. State which denominators and measurements are available. A single overwritten uncommitted file can outweigh several minor gains.

Keep reference checks outside the agent-controlled workspace. Give a PR integration only the access its task requires. An advisory check posts information for a reviewer. A blocking check can prevent a merge, so false flags and service outages now affect delivery. Decide who owns appeals and how an outage is handled.

## Write a decision before expansion

Example pilot rule: keep the check advisory on a limited set of PRs; pause on any confirmed loss of unrelated work; consider expanding only after audited results meet agreed quality, reviewer-effort and latency bounds across representative PRs. Supply your own bounds with the team’s tolerances and name the observation window. State the rollback action and owner.

Teach back why an independent grader can itself have false positives. Give a specific test that could expose one, and explain what evidence would justify switching a check from advisory to blocking.
