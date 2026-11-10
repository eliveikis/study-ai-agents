# Practice

One folder per coding exercise. The first attempt is yours alone, so the plan can tell your independent ability from AI-assisted work.

## Steps

1. **Name it.** Make a folder `practice/<slug>/`. The slug starts with the phase and names the problem in snake_case, such as `p1_two_sum`. A repeat of a problem in the same phase ends in `_2`: `p1_two_sum_2`. No two exercises share a slug, so their files never clash when the tests run. Name the files after the slug:
   - `<slug>.py`: your solution
   - `test_<slug>.py`: its tests, which `import <slug>`
   - `README.md`: copied from the template below
2. **Turn off inline AI completion** in your editor. In VS Code, set `editor.inlineSuggest.enabled` to `false`.
3. **Write the first attempt without AI** in `<slug>.py`, with its tests if you write them, against the target time.
4. **Freeze it** the first time you believe it works, or are about to look something up or ask for help, whichever comes first: copy `<slug>.py` to `<slug>_attempt.py` and commit it. Never change it after that. The check skips it.
5. **Correct it** in `<slug>.py`, with documentation or hints if you need them, and run `make check` until it passes.
6. **Fill in the README**, including the time spent, the mistakes and the assistance used, and commit. Where study work is committed: [specs/architecture.md](../specs/architecture.md) › Structure.

## README template

```markdown
# <Problem name>

## Problem

<The problem statement, or where it comes from.>

## Target time

<Minutes, from the plan.>

## Time spent

<Minutes to the frozen attempt, and in total.>

## Approach and complexity

<The idea in a few lines, and its time and space complexity.>

## Edge cases tested

<Empty input, duplicates, boundaries, and any others.>

## Mistakes

<What the frozen attempt got wrong, and what you had to look up.>

## Assistance used

<"None"; or which documentation, for which part; or what Claude did (a hint, a review, code) and for which part.>
```
