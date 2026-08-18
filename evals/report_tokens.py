"""Prints the token / time / reply-length comparison for one iteration.

Usage: TTP_WORKSPACE=... TTP_ITERATION=iteration-3 python3 evals/report_tokens.py
"""
import json
import os

W = os.environ.get("TTP_WORKSPACE", os.path.expanduser("~/ttp-workspace"))
IT = os.path.join(W, os.environ.get("TTP_ITERATION", "iteration-1"))


def load(run, name, default=0):
    p = os.path.join(run, name)
    return json.load(open(p)) if os.path.exists(p) else default


print("%-22s %-10s %10s %8s %8s" % ("eval", "config", "tokens", "secs", "words"))
totals = {}
for evl in sorted(os.listdir(IT)):
    for cfg in ("with_skill", "without_skill"):
        run = os.path.join(IT, evl, cfg)
        t = load(run, "timing.json", {})
        if not t:
            continue
        rp = os.path.join(run, "response.md")
        w = len(open(rp).read().split()) if os.path.exists(rp) else 0
        tok = t.get("total_tokens", 0)
        totals.setdefault(cfg, [0, 0, 0])
        totals[cfg][0] += tok
        totals[cfg][1] += t.get("total_duration_seconds", 0)
        totals[cfg][2] += w
        print("%-22s %-10s %10d %8.1f %8d" % (evl, cfg, tok, t.get("total_duration_seconds", 0), w))

print()
for cfg, (tok, sec, w) in totals.items():
    print("%-10s TOTAL  tokens=%d  time=%.1fs  words=%d" % (cfg, tok, sec, w))
if len(totals) == 2:
    a, b = totals["with_skill"], totals["without_skill"]
    for i, label in enumerate(("tokens", "time", "words")):
        if b[i]:
            print("%s delta: %+.1f%%" % (label, (a[i] - b[i]) / b[i] * 100))
