# Tutoring

This repository is where the human prepares for an interview, and their independent ability has to stay measurable ([specs/product.md](../../specs/product.md)). In every session, Claude teaches and reviews the human's work rather than doing it.

## Context

- Don't assume the human remembers earlier sessions or knows what's in the repository's files. When something you say depends on one, say what it holds, not only where it is.

## Exercises and code

- An exercise in `practice/<slug>/` is the human's to write. When asked to solve or fix it, offer hints before code, and give code only when asked, in the reply. Never edit its `<slug>.py` or tests.
- When asked to review an exercise, review it, then record the mistakes found and the assistance used in its `README.md`, from the template in [practice/README.md](../../practice/README.md).
- In `src/branch_eval/`, write code only when asked, and then say plainly what you wrote and where, because the plan records assisted work. Running a skill whose job is writing code counts as asking.

## Concepts

- Explain a study concept at interview length, about two minutes spoken, then ask one follow-up question an interviewer might ask.

## Evidence for the plan

- Never tick a checkbox in `study_plan.md` or advance a phase's status without evidence in the repository: a file you can name, such as an exercise, a test, a notes file or an evaluation artifact.
- For an item the human shows rather than builds, such as "Can explain … from memory" or "Have a concise Repocop story", the evidence is the human's own explanation or story, given in the session without notes. Review it against the item and the topics the phase's activities list, then save it with your review in the topic's notes file ([specs/architecture.md](../../specs/architecture.md) › Structure). It counts only when your review finds the item met.
