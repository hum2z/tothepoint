# Eval results

Each task was run twice by an independent agent: once with `to-the-point` loaded,
once with no skill at all. Same prompt, same fixtures, same model. The question
being tested is not "is it shorter" — it is **"is it shorter without the work
getting worse"**, which is the failure mode most conciseness prompts have.

## Iteration 2 (current skill)

| Metric | With skill | Baseline |
|---|---|---|
| Assertions passed | **18/18 (100%)** | 16/20 (80%) |
| Reply length, all 3 tasks | **454 words** | 898 words |
| Wall clock | 87.9s ± 44.5s | 113.9s ± 44.9s |
| Tokens | 47,095 ± 5,501 | 46,731 ± 7,691 |

Per task, reply length in words (with skill → baseline):

| Task | With skill | Baseline | Change |
|---|---|---|---|
| Rate-limit feature (5 files) | 110 | 170 | −35% |
| Pricing bug fix | 117 | 295 | −60% |
| Cache explanation *(control)* | 227 | 433 | −48% |

**Every code assertion passed in both arms.** Both configurations found all
three pricing bugs — including the latent rounding bug that only surfaces once
the first fix is in — ordered the middleware correctly, implemented real
token-bucket refill, and updated the README table. The skill did not cost a
single point of work quality; the entire delta is prose.

## The control matters

`cache-explanation` is deliberately rigged against the skill: the user asks
*why* something happens and adds "keep it brief if you can". A naive brevity
instruction answers that in two lines and loses the diagnosis. With the skill
the answer stayed 227 words, kept the root cause (the stale-fallback path
re-arms a full TTL), and kept the contributing factors. That is the
"when to expand" rule doing its job — the explanation *is* the deliverable.

## What iteration 1 caught

Iteration 1 scored 95.8% vs 80.0%, with one genuine failure: on the 5-file
feature the skilled run wrote **200 words — longer than the 170-word
baseline.** The padding was per-file implementation detail ("lock-guarded,
injectable clock, sweeps idle buckets every 5 min") plus two long caveats.

Fix: the `Sizing it` section — an explicit word budget that scales with files
touched, a rule that each file line says *what it does now* rather than how,
and a test for whether a caveat earns its line (does it change what the reader
does next?). That run went 200 → 110 words in iteration 2 while *increasing*
its test count from 20 to 21 and keeping both real caveats, compressed.

## Reproducing

```bash
export TTP_WORKSPACE=/path/to/workspace   # holds fixtures/ and iteration-N/
export TTP_ITERATION=iteration-1
python3 evals/grade.py
```

`evals/evals.json` holds the prompts, the assertions, and the trap each task
sets. `evals/fixtures/` holds the pristine inputs — copy them into a run
directory before each run, since agents mutate them in place.
