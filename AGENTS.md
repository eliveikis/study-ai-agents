This project's goal is to define, teach, and record progress against a study plan to improve python and ai agent tool skills.

The study plan is found in: /study_plan.md.

## Stack and commands

Python 3.12 as a [uv](https://docs.astral.sh/uv/) project, with pytest for tests and ruff for lint. It needs `uv` and `make` installed.

- Setup: `uv sync`
- Check: `make check`, which lints, then runs the tests

Where exercises, notes, the `branch_eval` package and evaluation artifacts go: [specs/architecture.md](specs/architecture.md) › Structure.

## Specifications

`/specs` is the authoritative source for product and system behavior.

Do not load `/specs` wholesale.

For tasks that may affect specified behavior:
1. Read `/specs/index.md`.
2. Identify only the relevant specs.
3. Read those specs and any documents they explicitly reference.
4. Treat applicable specs as authoritative over inferred behavior.

Do not load `/specs/changes/archive` at all.