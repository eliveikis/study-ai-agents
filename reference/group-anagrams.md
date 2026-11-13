# Group anagrams

Use 10–20 minutes to study the material below. The dictionary basics and cost rules in `first-unique-character.md` apply here too. Questions and answers are at the end, behind a spoiler warning.

## Python you'll need

**Grouping with a dictionary.** `collections.defaultdict(list)` creates an empty list the first time a key is used, so you can append without checking first. `d.setdefault(key, []).append(x)` does the same with a plain dictionary. Grouping numbers by whether they're even:

```python
from collections import defaultdict

groups = defaultdict(list)
for n in [1, 2, 3, 4, 5]:
    groups[n % 2].append(n)
list(groups.values())  # [[1, 3, 5], [2, 4]]
```

The key is computed from each item, and items with equal keys land in the same list. Choosing the key is the whole design decision.

**Only hashable values can be keys.** Immutable built-ins are hashable: `str`, `int`, `frozenset`, and a `tuple` whose items are hashable. Mutable ones aren't: `{[1, 2]: "x"}` raises `TypeError: unhashable type: 'list'`. Convert a list to a tuple or a string before using it as a key.

**`sorted()` accepts any iterable and returns a new list.** `sorted((3, 1, 2))` gives `[1, 2, 3]`. A string, a set or a dictionary's keys work the same way, and the result is always a list. `"".join(parts)` turns a list of strings back into one string: `"".join(["a", "b"])` gives `"ab"`.

**Sets forget repeats; counters don't.** `set([1, 1, 2])` is `{1, 2}`: it keeps only which items appeared. `Counter([1, 1, 2])` also keeps how many times.

**Methods that change a list return `None`.** `items.append(x)` and `items.sort()` change the list in place and return `None`, so `items = items.append(x)` loses the list.

**Testing output whose order doesn't matter.** If the order of groups isn't part of the contract, a test comparing exact lists fails a correct solution that orders them differently. Normalize both sides first, such as by sorting the words in each group and then sorting the groups.

## The exercise

Use the project's `practice/README.md` workflow. Before coding, state what the function accepts and returns, and predict the groups for `["tea", "eat", "ate", "tan", "tea"]`. State how you treat upper and lower case, and whether the order of groups, or of words inside a group, matters. Test an empty list, a duplicated word, and a word with no anagram.

**Group anagrams.** Group a list of words into anagrams. Anagrams contain the same letters with the same multiplicities.

Save the first attempt, a failing example, and the correction.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the exercise. Read on only once your attempt is done.

### Questions

1. What groups does the function produce for `["tea", "eat", "ate", "tan", "tea"]`?
2. Why is a set of letters the wrong key?
3. Do you need to group words by length before grouping them by letters?
4. What are the function's time and space costs?
5. Why does an anagram key throw ordering away?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. Two groups: `["tea", "eat", "ate", "tea"]`, which keeps the duplicate, and `["tan"]`.
2. A set loses multiplicity, so `"abb"` and `"aab"` both give `{"a", "b"}` and would wrongly share a group. A sorted spelling keeps every letter: `"".join(sorted("eat"))` is `"aet"`, the same as for `"tea"` and `"ate"`. A tuple of the sorted letters works too; a plain list doesn't, because it isn't hashable. Keep the original words, not the keys, in the output groups.
3. No. Two words with the same sorted spelling always have the same length, so one dictionary keyed by the sorted spelling already separates lengths.
4. For m words of at most L characters, sorting each word costs O(L log L), so O(m · L log L) in total, and the keys and groups take O(m · L) space. A key built from letter counts instead of a sorted spelling brings the time down to O(m · L).
5. Anagrams are defined by which letters appear and how often, whatever their positions, so the key deliberately discards position. The first unique character is the opposite: it's defined by position.
