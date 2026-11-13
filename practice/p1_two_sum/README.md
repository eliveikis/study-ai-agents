# First unique character

## Problem

Given a string, return the index of its first character that appears only once, or -1 if there is none. From `study_plan.md`, Phase 1, *One short coding exercise*.

## Target time

30 minutes.

## Time spent

Not recorded.

## Approach and complexity

One pass over the string records, for each character, the index where it first appears and how many times it appears. A second pass over that dictionary, in insertion order, returns the stored index of the first character with a count of 1. The first attempt returned the loop position in the dictionary instead. Complexity not yet stated.

## Edge cases tested

Empty string; a single character; only a repeated character (`"aa"`); a unique character between repeats (`"aba"`); no unique character (`"abab"`). Added after the review: a repeated character before the unique one (`"aab"`).

## Mistakes

From Claude's review on 2026-11-13:

- The second loop returns the position among the dictionary's distinct characters, not the position in the string. `"aab"` returns 1 instead of 2. The tests pass only because, in `"aba"`, the two positions happen to coincide.
- `enumerate` in the counting loop is unused; `for char in text` is enough.

Corrected by hand: the dictionary now stores each character's first index alongside its count, and `"aab"` is tested. `make check` passes.

## Assistance used

None for the first working version. Claude reviewed it and gave the failing input `"aab"` with a hint to trace what the second loop's index counts. No code.
