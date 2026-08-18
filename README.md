# to-the-point

A Claude Code skill that makes responses terse without making the work shallow.

Most "be concise" instructions compress everything uniformly — so the model
trims the explanation *and* the implementation, and ships stubbed functions,
dropped error handling, and skipped files. This skill separates the two
channels: prose gets cut hard, the engineering work stays at full depth.

## Install

```bash
cp -r .claude/skills/to-the-point ~/.claude/skills/
```

Or use it only inside this repo — it is already at `.claude/skills/to-the-point/`.

## Trigger

Fires on "be concise", "less talking", "to the point", "stop explaining",
"token efficient", and similar, and stays on for the rest of the session.
Can also be invoked directly with `/to-the-point`.

## Evals

`evals/` holds the A/B harness: three coding tasks, each run with the skill and
with no skill, graded on 20 assertions covering both the code and the reply.
Current: **18/18 with the skill vs 16/20 baseline, at half the reply length.**
See `evals/RESULTS.md`.
