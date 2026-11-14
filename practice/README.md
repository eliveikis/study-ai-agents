# Practice

One folder per exercise: a coding problem, or an explanation or story that the plan asks you to give. The first attempt is yours alone, so the plan can tell your independent ability from AI-assisted work.

## Coding exercises

1. **Name it.** Make a folder `practice/<slug>/`. The slug is the activity's code, `p<phase>a<n>`, where n is the activity's position in its phase's list in `study_plan.md`, then a short name in snake_case: `p1a3_first_unique_char`. A repeat of the same activity ends in `_2`: `p1a3_first_unique_char_2`. No two exercises share a slug, so their files never clash when the tests run. Name the files after the slug:
   - `<slug>.py`: your solution
   - `test_<slug>.py`: its tests, which `import <slug>`
   - `README.md`: written by Claude at the review, from the template below
2. **Turn off inline AI completion** in your editor. In VS Code, set `editor.inlineSuggest.enabled` to `false`.
3. **Write the first attempt without AI** in `<slug>.py`, with its tests if you write them, against the target time.
4. **Ask Claude to review it** once you believe it works. Claude records the review's mistakes and the assistance used in the README.
5. **Correct it** in `<slug>.py` if you want to, with documentation or hints if you need them, and run `make check` until it passes. Commit. Where study work is committed: [specs/architecture.md](../specs/architecture.md) › Structure.

## README template

```markdown
# <Problem name>

## Problem

<The problem statement, or where it comes from.>

## Target time

<Minutes, from the plan.>

## Time spent

<Minutes to the first working version, and in total.>

## Approach and complexity

<The idea in a few lines, and its time and space complexity.>

## Edge cases tested

<Empty input, duplicates, boundaries, and any others.>

## Mistakes

<What the first working version got wrong, from the review, and what you had to look up.>

## Assistance used

<"None"; or which documentation, for which part; or what Claude did (a hint, a review, code) and for which part.>
```

## Explanations and stories

For an activity or completion item you show rather than build, such as "Can explain … from memory" or a Repocop story.

1. **Name it** as for a coding exercise: `practice/<slug>/`, such as `p1a4_repocop_story`. Its files:
   - `<slug>.md`: your explanation or story
   - `README.md`: written by Claude at the review, from the template below
2. **Write it from memory**, without notes or AI, as you'd say it in an interview. Read it aloud against the plan's length to check it.
3. **Ask Claude to review it.** Claude reviews it against the plan's item and records the review and the assistance used in the README.
4. **Revise it** in `<slug>.md` if you want to, and commit.

### README template

```markdown
# <Activity title>

## Activity

<The plan's activity or completion item it shows.>

## Time spent

<Minutes.>

## Review

<Claude's review against the item: what it covers, what's missing or wrong, and whether it meets the item.>

## Assistance used

<"None"; or what you looked up or asked while writing it.>
```
