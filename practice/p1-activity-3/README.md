# Repocop story, first rehearsal

## Activity

Phase 1, "Rehearse a short Repocop story": in about 60 seconds, explain the problem, the architecture, one decision you made and one failure, and distinguish deterministic software from model decisions. It is evidence for the completion item "Have a 60-second Repocop story covering the problem, the architecture, one decision and one failure."

## Time spent

5 minutes.

## Review

Written on purpose as a casual opening, leaving the detail to the interviewer's follow-up questions.

What it covers:

- **The problem**, clearly: a small studio with several repositories, whose agent setup (the spec-driven workflow, skills, rules, hooks) changes constantly and applies to every project, so keeping the repositories in step by hand is slow and hard to standardize.
- **Scope**, stated honestly: built for this studio, not as an enterprise product.
- **What it does**: a dashboard that syncs the agent setup to the repositories and shows how far the spec work has got.
- **The architecture**, concretely: Python, SQLite, server-rendered Jinja HTML with htmx and no build step; modules grouped by page or concept; one git wrapper that does all the git work; templates, with one in use.

What's missing or weak:

- **No decision of your own.** The stack and the single git wrapper are decisions, but they're stated as facts, with no reason and no tradeoff.
- **No failure.**
- **No line between deterministic software and model decisions.** RepoCop's syncing and status reporting are deterministic. What an agent does with the synced skills is the model's decision.
- **"We" all the way through**, so a listener can't tell what you built yourself.
- **Length:** 228 words, about 90 seconds at a typical speaking pace. That's over the 60-second target before the decision and the failure go in.
- "Display the progress of specs work" assumes the listener knows what a spec's status is in your workflow. "The architecture is pretty basic" undersells a choice you made on purpose.

Verdict: **doesn't meet the item yet.** It has no decision, no failure and no line between deterministic software and model decisions, and it runs long. It does work as an opening: the problem is clear, the scope is honest and the stack is concrete.

## Assistance used

None: written from memory, with no notes, guide or AI.
