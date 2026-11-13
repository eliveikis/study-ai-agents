# P1A3 — Two short coding exercises

Use 10–20 minutes to study the example and answer the recall questions. The full activity has a 60-minute timebox, including study.

## First independent attempt

Use the project’s `practice/README.md` workflow. Split the hour between the two prompts. Before reading the hints below, state what the function accepts, predict two outputs by hand, and write your own Python attempt.

1. Return the zero-based index of the first character that occurs exactly once. Try an empty string, `aabb`, and `swiss`. Expected values are −1, −1, and 1.
2. Group a list of words into anagrams. Anagrams contain the same letters with the same multiplicities. For `["tea", "eat", "ate", "tan", "tea"]`, one group contains all four three-letter rearrangements of “tea”, including its duplicate. The other contains “tan”. State how you treat case and whether group ordering matters.

## Hints after the attempt

“First” and “only once” are separate conditions. Seeing a letter once so far says nothing about its later occurrences. Count the whole string, then scan in original order. Trace why the opening s in “swiss” cannot win even though you encounter it first.

A dictionary key identifies a group. A sorted spelling gives all anagrams the same key. A set of letters loses multiplicity, so it would wrongly group “abb” with “aab”. Keep the original words in the output buckets.

## Explain your cost

For a string of length n with k distinct characters, two passes take O(n) expected time using a hash map and O(k) counts. For m words of maximum length L, sorting each costs up to O(m L log L); storing the group keys also consumes space. Describe your own implementation if it differs.

Save the first attempt, a failing example, and the correction. From memory, explain why finding the first unique character needs ordering while forming an anagram key discards ordering.
