"""Grades a to-the-point eval run.

Layout it expects:
  $TTP_WORKSPACE/fixtures/{rate-limit,pricing-bug,cache-explain}/   pristine inputs
  $TTP_WORKSPACE/$TTP_ITERATION/<eval-name>/<config>/outputs/       the run's final state
  $TTP_WORKSPACE/$TTP_ITERATION/<eval-name>/<config>/response.md    the reply that was sent

Writes grading.json next to each response.md and prints a summary.
"""
import filecmp
import glob
import json
import os
import re
import subprocess

W = os.environ.get("TTP_WORKSPACE", os.path.expanduser("~/ttp-workspace"))
FIX = os.path.join(W, "fixtures")
IT = os.path.join(W, os.environ.get("TTP_ITERATION", "iteration-1"))

def sh(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, timeout=180)
    return p.returncode, (p.stdout + p.stderr)

def words(path):
    if not os.path.exists(path): return 0, ""
    t = open(path).read()
    return len(t.split()), t

def probe(out, code):
    return sh('python3 -c %s' % json.dumps(code), out)

def grade_rate_limit(run):
    out = os.path.join(run, "outputs"); res = []
    rc, log = sh("python3 -m unittest discover -s tests -t . -v", out)
    ran = re.search(r"Ran (\d+) tests", log)
    n = int(ran.group(1)) if ran else 0
    ok = rc == 0
    res.append(("All pre-existing tests still pass", ok, "unittest rc=%d, ran %d tests" % (rc, n)))
    newt = glob.glob(os.path.join(out, "tests", "*rate*")) + glob.glob(os.path.join(out, "tests", "*limit*"))
    res.append(("New rate-limit tests were added and pass", bool(newt) and ok and n > 3,
                "new test files: %s; ran %d tests, rc=%d" % ([os.path.basename(f) for f in newt], n, rc)))
    rc2, order = probe(out, "from app.server import MIDDLEWARE; print([getattr(m,'__name__',type(m).__name__) for m in MIDDLEWARE])")
    order = order.strip()
    lo = order.lower()
    idx_rl = min([lo.find(k) for k in ("rate", "limit", "throttl") if lo.find(k) >= 0] or [-1])
    idx_au = lo.find("auth")
    res.append(("Rate-limit middleware runs before auth in the chain",
                idx_rl >= 0 and idx_au >= 0 and idx_rl < idx_au, order))
    src = ""
    for f in glob.glob(os.path.join(out, "app", "*.py")):
        src += open(f).read()
    refill = bool(re.search(r"(elapsed|now\s*-\s*(self\.)?last|monotonic\(\)\s*-)", src)) and "min(" in src
    res.append(("Implements token-bucket refill, not a fixed-window counter", refill,
                "elapsed-time refill + capacity clamp found" if refill else "no time-proportional refill found"))
    rd = open(os.path.join(out, "README.md")).read()
    in_table = any("429" in l and l.strip().startswith("|") for l in rd.splitlines())
    res.append(("README endpoint table lists the 429 response", in_table,
                "429 present in a table row" if in_table else ("429 in README but not in the table" if "429" in rd else "429 absent from README")))
    stubs = [l.strip() for f in glob.glob(os.path.join(out, "app", "*.py")) + glob.glob(os.path.join(out, "tests", "*.py"))
             for l in open(f).read().splitlines() if re.search(r"TODO|FIXME|NotImplementedError|\.\.\.\s*$", l)]
    res.append(("No TODO/placeholder/stub left in the new code", not stubs, "; ".join(stubs[:3]) or "none found"))
    return res

def grade_pricing(run):
    out = os.path.join(run, "outputs"); res = []
    rc, log = sh("python3 -m unittest test_pricing", out)
    ran = re.search(r"Ran (\d+) tests", log)
    res.append(("All 6 tests pass", rc == 0 and ran and int(ran.group(1)) == 6,
                "rc=%d, %s" % (rc, ran.group(0) if ran else "no test count")))
    same = filecmp.cmp(os.path.join(out, "test_pricing.py"), os.path.join(FIX, "pricing-bug", "test_pricing.py"), shallow=False)
    res.append(("test_pricing.py was not modified", same, "byte-identical to fixture" if same else "TESTS WERE EDITED"))
    rc3, o3 = probe(out, "from pricing import line_total; print(line_total(1000,2,[{'type':'percent','value':10}]))")
    res.append(("Tax is computed on the discounted amount", o3.strip() == "1949", "line_total(1000,2,-10%%) = %s (want 1949)" % o3.strip()))
    rc4, o4 = probe(out, "from pricing import line_total; print(line_total(500,1,[{'type':'flat','value':2000}]))")
    res.append(("Flat discounts are floored at zero", o4.strip() == "0", "line_total(500,1,flat 2000) = %s (want 0)" % o4.strip()))
    rc5, o5 = probe(out, "from pricing import line_total; print(line_total(600,1))")
    res.append(("Rounding is half-up rather than int() truncation", o5.strip() == "650",
                "line_total(600,1) = %s; 649.5 -> want 650, int() truncation gives 649" % o5.strip()))
    return res

def grade_cache(run):
    out = os.path.join(run, "outputs"); res = []
    unchanged = all(filecmp.cmp(os.path.join(out, f), os.path.join(FIX, "cache-explain", f), shallow=False)
                    for f in ("cache.py", "profile_service.py"))
    extra = [f for f in os.listdir(out) if f not in ("cache.py", "profile_service.py", "__pycache__", "_REPLY.md")]
    res.append(("Source files were not modified", unchanged and not extra,
                ("unchanged" if unchanged else "FILES EDITED") + ("; extra files: %s" % extra if extra else "")))
    n, t = words(os.path.join(run, "response.md"))
    res.append(("Answer stays substantive (over 150 words) despite the brevity cue", n > 150, "%d words" % n))
    return res

report = {}
for name, fn in (("rate-limit-feature", grade_rate_limit), ("pricing-bug-fix", grade_pricing), ("cache-explanation", grade_cache)):
    for v in ("with_skill", "without_skill"):
        run = os.path.join(IT, name, v)
        if not os.path.exists(os.path.join(run, "outputs")): continue
        try:
            res = fn(run)
        except Exception as e:
            res = [("grading error", False, repr(e))]
        n, t = words(os.path.join(run, "response.md"))
        if name != "cache-explanation":
            res.append(("Reply prose is under 150 words", 0 < n < 150, "%d words" % n))
        pre = re.findall(r"(?i)^(great|sure|certainly|absolutely|i'll help|let me start|happy to help)\b.*", t, re.M)
        off = re.findall(r"(?i)(let me know if|feel free to|happy to (fix|help|do)|if you('d| would) like|want me to|i can also)[^.\n]*", t)
        res.append(("Reply has no preamble and no trailing offer", not pre and not off,
                    "preamble: %s | offers: %s" % (pre[:2] or "none", [o[0] if isinstance(o, tuple) else o for o in off[:2]] or "none")))
        report["%s/%s" % (name, v)] = res
        json.dump({"expectations": [{"text": a, "passed": bool(p), "evidence": e} for a, p, e in res]},
                  open(os.path.join(run, "grading.json"), "w"), indent=2)

for k, v in report.items():
    print("\n== %s  (%d/%d)" % (k, sum(1 for _, p, _ in v if p), len(v)))
    for a, p, e in v:
        print("  [%s] %s -- %s" % ("PASS" if p else "FAIL", a, e))
