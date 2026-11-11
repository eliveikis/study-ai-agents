# study-ai-agents

Interview prep for a Senior AI Engineer (AI tools) role. The plan is [study_plan.md](study_plan.md): five phases of about four hours each, with Claude Code as your tutor.

## Do a phase

A phase is one or more sessions. In each session:

1. Run `/study-start`. Answer its recall questions, and it tells you the phase, your first action and its target time. Say the activity is timed if you want it to track the minutes.
2. Do that action:
   - **Coding exercise:** follow [practice/README.md](practice/README.md).
   - **Concept or story** ("Can explain …", the Repocop story): explain it to Claude without notes. Claude reviews it and saves it in `notes/`, which is the evidence that ticks the box.
   - **Evaluation harness** (Phase 2 on): build it as a change, as [specs/changes/README.md](specs/changes/README.md) describes.
3. Run `/study-end` and answer its questions. It logs the session, ticks the boxes you have evidence for, sets up the next session and commits.

Keep going until the phase's boxes are ticked or its budget runs out. Once you're over budget, `/study-end` asks whether to stop. After you stop, the next `/study-start` moves you on to the next phase.

## Repeat a phase

Do a phase again and keep what you've already earned.

1. At `/study-end`, say the next session is Phase N again.
2. Run sessions as in [Do a phase](#do-a-phase). Name repeated exercises with `_2`, like `p1_two_sum_2`.
3. When `/study-end` says you're over budget, say you're not stopping. The phase's old minutes still count toward its budget.
4. When you're done, tell `/study-end` which phase comes next.

## Restart a phase

Start a phase over from scratch.

1. In [study_plan.md](study_plan.md), for that phase: untick its boxes, set its status to `In progress`, and set the next-session entry to that phase and its first activity.
2. Leave its log rows and `*_attempt.py` files alone. They record your first try.
3. Follow [Repeat a phase](#repeat-a-phase) from step 2.
