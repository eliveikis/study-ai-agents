# Group anagrams

## Problem

Given a list of words, return them grouped so that each group holds words that are anagrams of each other. From `study_plan.md`, Phase 2, *Group anagrams*.

## Target time

30 minutes.

## Time spent

About 20 minutes in total: the session's 40, split evenly between the two exercises.

## Approach and complexity

Key each word by its sorted letters, inside buckets by word length, and collect the words of each key into a group. Complexity not yet stated.

## Edge cases tested

Empty list; a single word; two anagrams; anagrams plus a word of the same length; anagrams plus a word of a different length. Not tested: a duplicated word.

## Mistakes

From Claude's review on 2026-11-13. The output is correct, duplicates included, as far as traced.

- The length buckets are redundant: words with the same sorted letters always have the same length, so one dictionary keyed by the sorted letters is enough.
- `group = group.append(val)` sets `group` to `None`, since `list.append` returns `None`. Harmless here, but misleading.
- The tests assert one particular order of groups, so a correct solution ordering them differently would fail. The order isn't stated as part of the contract.
- The parameter name `input` shadows a built-in.

## Assistance used

None for the first working version. Claude reviewed it. No code.
