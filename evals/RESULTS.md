# Eval results

Four coding tasks, each run by an independent agent with the skill and without it.
Same prompts, same fixtures, same model. The question is not "is it shorter" but
**"is it shorter without the work getting worse"** — the failure mode most
conciseness prompts have.

## Headline

| Metric | With skill | Baseline |
|---|---|---|
| Assertions passed | **17/17** | 14/18 |
| Reply length, 3 shared tasks | **454 words** | 898 words |
| Work quality | identical | identical |

Every code assertion passes in **both** arms on every iteration. Both arms found
all three pricing bugs (including the latent rounding bug that only appears once
the first is fixed), ordered the middleware correctly, implemented real
token-bucket refill, updated the README table, and made the same surgical
one-file invoice fix. The skill has never cost a point of work quality — the
entire delta is prose.

## Reply length is not where the tokens are

Iterations 1-2 only measured prose. On tokens they showed 47,095 with the skill
against 46,731 baseline — i.e. **nothing**. Trimming a reply saves a few hundred
tokens out of fifty thousand.

Iteration 3 added `big-repo-bug` to measure spend instead: 52 files, 8.3k lines,
one shipping-on-refunded-lines bug. Reading the tree costs roughly 90k tokens;
grep finds it in one call, so exploration discipline dominates the result. The
token section was rewritten around the real cost model — context is re-sent every
turn, so spend ≈ context size × steps, and the levers are pulling in less and
taking fewer steps.

## Skill length is itself a recurring cost

The 123-line version was 2,636 tokens of context carried on every turn. Iteration
4 tested a 44-line rewrite (1,194 tokens, −55%) holding every behavioural rule.
Four replicates of each on `big-repo-bug`:

| | tokens (mean ± sd) | reply words (mean) | tests | files changed |
|---|---|---|---|---|
| 123-line skill | 49,055 ± 1,110 | 52 | 3/3 all runs | `aggregate.py` only |
| 44-line skill | 47,708 ± 2,901 | **29** | 3/3 all runs | `aggregate.py` only |
| no skill | 47,518 (n=1) | 165 | 3/3 | `aggregate.py` only |

**On tokens the difference is not significant** — 1,346 apart with a standard
error of 1,553 (t = 0.87). Run-to-run spread is larger than the effect, and four
replicates cannot resolve it. Do not read the 2.7% as a measured win.

**On everything else the short version is clearly better or equal**: replies are
~45% tighter (29 vs 52 words) and far more consistent (sd 2.1 vs 11.8), work
quality is identical across all eight runs, and its context cost is
deterministically 1,442 tokens smaller per turn. That is why it was adopted — not
because the token measurement proved anything.

## The control matters

`cache-explanation` is rigged against the skill: the user asks *why* something
happens and adds "keep it brief if you can". A naive brevity rule answers in two
lines and loses the diagnosis. With the skill the answer stayed 227-260 words and
kept the root cause (the stale-fallback path re-arms a full TTL) plus the
contributing factors. The "expand when it's the deliverable" rule doing its job.

## What each iteration caught

**Iteration 1** — on the 5-file feature the skilled run wrote 200 words, *longer*
than the 170-word baseline, padded with per-file implementation detail. Fixed by
the sizing budget: ~12 words per file touched, file lines say *what it does* not
*how*, a caveat earns its line only if it changes what the reader does next. That
run went to 110 words while raising its test count from 20 to 21.

**Iteration 3** — the skill was saving no tokens at all. Fixed by rewriting the
token section around context × steps.

**Iteration 4** — the skill's own length was the largest thing it controlled.
Fixed by cutting it 55%.

Three grader bugs were also found and fixed along the way: a name-based
middleware check that a closure factory defeated, a stub check that flagged an
ellipsis inside a comment, and a probe helper whose `json.dumps` quoting made
every multi-line probe fail as an assertion failure.

## Reproducing

```bash
export TTP_WORKSPACE=/path/to/workspace   # holds fixtures/ and iteration-N/
export TTP_ITERATION=iteration-1
python3 evals/grade.py
python3 evals/report_tokens.py
```

`evals/evals.json` holds the prompts, assertions, and the trap each task sets.
`evals/fixtures/` holds pristine inputs — copy them into a run directory before
each run, since agents mutate them in place.
