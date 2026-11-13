# P3A1 — Timed coding and correction

Use 10–20 minutes to study the material below. The full activity has a 90-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Choose the mechanism you need to practice

Use your Phase 1 mistake log. If you repeatedly lost duplicate counts, pick a hash-map problem. If boundary indices caused failures, choose two pointers.

## The mechanisms

**Hash map.** A dictionary, or a set when you need only membership, answers "have I seen this?" in constant time on average. Trading O(n) memory for that lookup often turns an O(n²) pair of loops into one O(n) loop.

**Two pointers.** Two positions in a sequence, each advanced under a rule that shrinks the part still to search. A classic example checks whether a list reads the same both ways:

```python
def is_palindrome(items):
    left, right = 0, len(items) - 1
    while left < right:
        if items[left] != items[right]:
            return False
        left += 1
        right -= 1
    return True
```

Each step discards one position from each end, so the loop runs at most n/2 times: O(n) time and O(1) extra space. The loop condition is where bugs live. `left < right` stops when the pointers meet; `left <= right` would also compare the middle item with itself. Write down what's true at the top of every iteration, the **invariant**, and check that each move keeps it true.

**Stack.** Last in, first out: unfinished work waits on top. In Python, use a list: `stack.append(x)` and `stack.pop()`, both O(1).

**Queue.** First in, first out: the oldest entry goes first. Use `collections.deque`: `q.append(x)` and `q.popleft()`, both O(1). `list.pop(0)` works but costs O(n), because every remaining item shifts down.

**Sorting.** `sorted(items)` returns a new list; `items.sort()` sorts in place and returns `None`. Both accept `key=` and `reverse=`, and both cost O(n log n). Sorting first often makes a problem easier, because order lets you rule items out by comparing them with their neighbors.

## The timed prompt

Try this one if boundaries were difficult: given a sorted list of integers and a target, return two distinct indices whose values sum to the target, or report no pair. Clarify whether any valid pair suffices. Before coding, predict the result for each input:

| Values | Target |
| --- | ---: |
| `[]` | 5 |
| `[3]` | 6 |
| `[3, 3]` | 6 |
| `[-4, -1, 2, 7]` | 1 |
| `[1, 2, 4, 8]` | 6 |

Write the first attempt without assistance.

## Plan the session

Reserve 30 minutes for an independent attempt, 15 for tracing and tests, 25 for a second problem or variation and 20 for review and recall. Record elapsed time and the earliest failing input, and explain which invariant your fix restores. Retry from a blank file. Save the original attempt as evidence of what needs practice.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the timed prompt. Read on only once your attempt is frozen.

### Questions

1. What does your function return for each input in the table?
2. Trace target 6 on `[1, 2, 4, 8]` with two pointers. Why can each move discard a value for good?
3. Which invariant stops one element being used twice?
4. What are the time and space costs? What changes if the list isn't sorted?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. No pair; no pair, because one element can't be used twice; `(0, 1)`; `(1, 2)`, since -1 + 2 = 1; and `(1, 2)`, the values 2 and 4.
2. The extremes sum to 9. Even pairing 8 with the smallest value overshoots, so 8 can be discarded. Now the sum is 1 + 4 = 5. Pairing 1 with anything remaining cannot reach 6, so discard 1. The remaining pair is 2 and 4. This reasoning depends on sorted input.
3. Keep `left < right`: stop when the pointers meet, so the two indices are always distinct. That's why `[3]` with target 6 has no pair.
4. Each move eliminates a position, giving O(n) time and O(1) extra space. Unsorted, you can sort first in O(n log n), sorting (value, index) pairs to keep the original indices. Or keep a dictionary from each value seen so far to its index: O(n) time and O(n) space.
