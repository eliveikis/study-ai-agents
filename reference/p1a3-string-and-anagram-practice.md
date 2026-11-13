# P1A3 — Two short coding exercises

Use 10–20 minutes to study the material below. The full activity has a 60-minute timebox, including study. Questions and answers are at the end, behind a spoiler warning.

## Python you'll need

**Strings are sequences.** You can index a string (`s[0]`), measure it (`len(s)`), and loop over it. `for ch in s` gives each character; `for i, ch in enumerate(s)` gives each index with its character. `python-enumeration.md` has more loop forms.

**A dictionary maps keys to values.** Looking up, inserting and updating a key take constant time on average, however large the dictionary grows. Two patterns come up constantly:

- *Counting.* `counts[key] = counts.get(key, 0) + 1` starts a missing key at zero. `collections.Counter` counts a whole iterable at once: `Counter([3, 1, 3])` gives `Counter({3: 2, 1: 1})`, and a missing key reads as 0.
- *Grouping.* `collections.defaultdict(list)` creates an empty list the first time a key is used, so you can append without checking first. Grouping numbers by whether they're even:

  ```python
  from collections import defaultdict

  groups = defaultdict(list)
  for n in [1, 2, 3, 4, 5]:
      groups[n % 2].append(n)
  list(groups.values())  # [[1, 3, 5], [2, 4]]
  ```

  The key is computed from each item, and items with equal keys land in the same list. Choosing the key is the whole design decision.

Since Python 3.7, a dictionary remembers the order in which keys were first inserted, and loops over them in that order.

**Only hashable values can be keys.** Immutable built-ins are hashable: `str`, `int`, `frozenset`, and a `tuple` whose items are hashable. Mutable ones aren't: `{[1, 2]: "x"}` raises `TypeError: unhashable type: 'list'`. Convert a list to a tuple or a string before using it as a key.

**`sorted()` accepts any iterable and returns a new list.** `sorted((3, 1, 2))` gives `[1, 2, 3]`. A string, a set or a dictionary's keys work the same way, and the result is always a list. `"".join(parts)` turns a list of strings back into one string: `"".join(["a", "b"])` gives `"ab"`.

**Sets forget repeats; counters don't.** `set([1, 1, 2])` is `{1, 2}`: it keeps only which items appeared. `Counter([1, 1, 2])` also keeps how many times.

## Estimating cost

Describe cost in terms of input size: n characters, or m words of at most L characters each.

- One loop over n items doing constant work per item is O(n). Two such loops one after the other are still O(n).
- A loop inside a loop over the same input is O(n²). A call like `s.count(ch)` inside a loop hides the inner loop, because `count` scans the whole string.
- Sorting k items costs O(k log k).
- Space counts what you store beyond the input. A dictionary with one entry per distinct key uses space proportional to the number of keys.

## Edge cases to test

- **Empty input:** `""` or `[]`. Decide what the function should return.
- **Duplicates:** repeated characters, or the same word twice in the list.
- **Boundaries:** a single character, the answer at the very first or last position, and no valid answer at all.

## The exercise

Use the project's `practice/README.md` workflow. Split the hour between the two prompts. Before coding each one, state what the function accepts and returns, and predict the outputs by hand for the inputs given. Then write your own Python attempt.

1. **First unique character.** Return the zero-based index of the first character that occurs exactly once, or -1 if there is none. Predict the result for `""`, `"x"`, `"aabb"` and `"swiss"`.
2. **Group anagrams.** Group a list of words into anagrams. Anagrams contain the same letters with the same multiplicities. Predict the groups for `["tea", "eat", "ate", "tan", "tea"]`. State how you treat upper and lower case, and whether the order of groups, or of words inside a group, matters.

Save the first attempt, a failing example, and the correction.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the exercise. Read on only once your attempt is frozen.

### Questions

1. What does the first function return for `""`, `"x"`, `"aabb"` and `"swiss"`?
2. What groups does the second function produce for `["tea", "eat", "ate", "tan", "tea"]`?
3. In `"swiss"` you meet `s` first. Why can't it be the answer?
4. Why is a set of letters the wrong key for grouping anagrams?
5. What are the time and space costs of each function?
6. Why does finding the first unique character need ordering, while an anagram key throws ordering away?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. `-1`, `0`, `-1` and `1`. In `"swiss"`, `w` at index 1 is the first character that occurs once; `i` occurs once too, but later.
2. Two groups: `["tea", "eat", "ate", "tea"]`, which keeps the duplicate, and `["tan"]`.
3. "First" and "only once" are separate conditions. Seeing a character once *so far* says nothing about its later occurrences, and `s` appears three times. So count the whole string first, then scan it again in original order and return the first index whose character has a count of 1. Checking each character with `s.count(ch)` also works, but costs O(n²).
4. A set loses multiplicity, so `"abb"` and `"aab"` both give `{"a", "b"}` and would wrongly share a group. A sorted spelling keeps every letter: `"".join(sorted("eat"))` is `"aet"`, the same as for `"tea"` and `"ate"`. A tuple of the sorted letters works too; a plain list doesn't, because it isn't hashable. Keep the original words, not the keys, in the output groups.
5. For a string of n characters with k distinct ones, the two passes take O(n) expected time and the counts take O(k) space. For m words of at most L characters, sorting each word costs O(L log L), so O(m · L log L) in total, and the keys and groups take O(m · L) space. A key built from letter counts instead of a sorted spelling brings the time down to O(m · L).
6. The first unique character is defined by position, so the final scan has to follow the original order. Anagrams are defined by which letters appear and how often, whatever their positions, so the key deliberately discards position.
