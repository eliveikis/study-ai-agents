# First unique character

Use 10–20 minutes to study the material below. Questions and answers are at the end, behind a spoiler warning.

## Python you'll need

**Strings are sequences.** You can index a string (`s[0]`), measure it (`len(s)`), and loop over it. `for ch in s` gives each character; `for i, ch in enumerate(s)` gives each index with its character. `python-enumeration.md` has more loop forms.

**A dictionary maps keys to values.** Looking up, inserting and updating a key take constant time on average, however large the dictionary grows. To count, `counts[key] = counts.get(key, 0) + 1` starts a missing key at zero. `collections.Counter` counts a whole iterable at once: `Counter([3, 1, 3])` gives `Counter({3: 2, 1: 1})`, and a missing key reads as 0.

Since Python 3.7, a dictionary remembers the order in which keys were first inserted, and loops over them in that order.

## Estimating cost

Describe cost in terms of input size, such as n characters.

- One loop over n items doing constant work per item is O(n). Two such loops one after the other are still O(n).
- A loop inside a loop over the same input is O(n²). A call like `s.count(ch)` inside a loop hides the inner loop, because `count` scans the whole string.
- Sorting k items costs O(k log k).
- Space counts what you store beyond the input. A dictionary with one entry per distinct key uses space proportional to the number of keys.

## Edge cases to test

- **Empty input:** `""`. Decide what the function should return.
- **Duplicates:** repeated characters, including a repeated character before the answer.
- **Boundaries:** a single character, the answer at the very first or last position, and no valid answer at all.

## The exercise

Use the project's `practice/README.md` workflow. Before coding, state what the function accepts and returns, and predict the result by hand for `""`, `"x"`, `"aabb"` and `"swiss"`. Then write your own Python attempt.

**First unique character.** Return the zero-based index of the first character that occurs exactly once, or -1 if there is none.

Save the first attempt, a failing example, and the correction.

---

## ⚠️ SPOILERS: questions and answers

Prepare and attempt using only the text above this line. Everything below it answers the exercise. Read on only once your attempt is done.

### Questions

1. What does the function return for `""`, `"x"`, `"aabb"` and `"swiss"`?
2. In `"swiss"` you meet `s` first. Why can't it be the answer?
3. What are the function's time and space costs?
4. Where does the ordering in your answer come from?

**Stop here.** Answer every question aloud before you read on.

### Answers

1. `-1`, `0`, `-1` and `1`. In `"swiss"`, `w` at index 1 is the first character that occurs once; `i` occurs once too, but later.
2. "First" and "only once" are separate conditions. Seeing a character once *so far* says nothing about its later occurrences, and `s` appears three times. So count the whole string first, then scan it again in original order and return the first index whose character has a count of 1. Checking each character with `s.count(ch)` also works, but costs O(n²).
3. For a string of n characters with k distinct ones, the two passes take O(n) expected time and the counts take O(k) space.
4. From the string's own order: the second pass walks the string, so the index it returns is a position in the string. Looping over the counts dictionary instead finds the right *character*, because insertion order follows first occurrences, but its loop position counts distinct characters, not string positions. `"aab"` tells the two apart: the answer is 2, while the dictionary position of `b` is 1.
