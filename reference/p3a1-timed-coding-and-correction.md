# P3A1 — Timed coding and correction

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 90-minute timebox, including study.

## Choose the mechanism you need to practice

Use your Phase 1 mistake log. If you repeatedly lost duplicate counts, pick a hash-map problem. If boundary indices caused failures, choose two pointers. Two pointers are positions advanced under a rule that shrinks the remaining search space. A stack stores unfinished work in last-in, first-out order; a queue processes the oldest entry first.

Try this timed prompt if boundaries were difficult: given a sorted list of integers and a target, return two distinct indices whose values sum to the target, or report no pair. Clarify whether any valid pair suffices. Predict results for an empty input, a singleton, repeated values and negative values. Write the first attempt without assistance.

## Review after the timer

Trace target 6 on [1, 2, 4, 8]. The extremes sum to 9. Even pairing 8 with the smallest value overshoots, so 8 can be discarded. Now the sum is 5. Pairing 1 with anything remaining cannot reach 6, so discard 1. The remaining pair is 2 and 4. This reasoning depends on sorted input. Each move eliminates a position, giving linear time and constant auxiliary space.

## Spend the rest of the session on correction

Reserve 30 minutes for an independent attempt, 15 for tracing and tests, 25 for a second problem or variation and 20 for review and recall. Record elapsed time and the earliest failing input. Explain which invariant your fix restores. For example, stopping when the pointers meet prevents reusing one element twice. Retry from a blank file. Save the original attempt as evidence of what needs practice.
