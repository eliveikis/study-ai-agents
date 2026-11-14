# Group anagrams

## Problem

Given a list of words, return them grouped so that each group holds words that are anagrams of each other. From `study_plan.md`, Phase 2, *Group anagrams*.

## Target time

30 minutes.

## Time spent

About 20 minutes in total: the session's 40, split evenly between the two exercises.

## Approach and complexity

Key each word by its sorted letters, inside buckets by word length, and collect the words of each key into a group. Since 2026-11-14, a word already in its group isn't added again: the problem didn't define duplicates, and the human chose to drop them.

Complexity, from Claude's review on 2026-11-14, for m words of at most L letters: sorting each word costs O(m · L log L) in total. The duplicate check `val in group` scans the group's list, so when most words fall into one group it adds up to O(m² · L) in the worst case, which dominates. Space is O(m · L) for the keys and groups. Not yet stated by the human.

## Edge cases tested

Empty list; a single word; two anagrams; anagrams plus a word of the same length; anagrams plus a word of a different length; a duplicated word (`["dog", "dog"]`, added 2026-11-14).

## Mistakes

From Claude's review on 2026-11-13. The output is correct, duplicates included, as far as traced.

- The length buckets are redundant: words with the same sorted letters always have the same length, so one dictionary keyed by the sorted letters is enough.
- `group = group.append(val)` sets `group` to `None`, since `list.append` returns `None`. Harmless here, but misleading.
- The tests assert one particular order of groups, so a correct solution ordering them differently would fail. The order isn't stated as part of the contract.
- The parameter name `input` shadows a built-in.

From Claude's review on 2026-11-14, of the duplicate handling:

- `not val in group` fails `make check`: ruff's E713 wants `val not in group`.
- Membership in a list is a linear scan, which makes the worst case quadratic in the number of words. A set of the words already seen keeps each check O(L) on average.
- Group order isn't first appearance: groups come out by word length first, so `["dog", "fish", "cat"]` gives `dog`, `cat`, `fish`.
- Minor: `enumerate` with an unused index, `.items()` with an unused key where `.values()` would do, and `.get(key, None)`, where `None` is already the default.

## Assistance used

None for the first working version. Claude reviewed it twice, and the second time gave the complexity analysis above. No code.
