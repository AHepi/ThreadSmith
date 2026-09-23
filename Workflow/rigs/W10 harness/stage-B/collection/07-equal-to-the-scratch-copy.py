"""07: the in-place collection (00b to 06 in this folder) against the scratch-copy run of the
same programs (stage-B/independent-check/checks/harness-programs-on-a-scratch-copy/).

  /home/user/.venvs/threadsmith/bin/python 07-equal-to-the-scratch-copy.py [SCRATCH_RUN_DIR]

SCRATCH_RUN_DIR is the scratch copy's own working folder (the `$S` of run.sh). Its two marks
files and its 96 run records were not committed; the committed folder kept only the logs and the
two count files. When the folder is given, this program first shows that its logs and count files
are byte-identical to the committed ones (so it is the same run), then compares its marks files
and run records too. Without it, only the committed counterparts are compared.

Reads only. Writes nothing (prints). Imports rig.py and record_adapter.py read-only, to learn the
adapter's default --record, with bytecode writing off.

What this check forbids, and what would show it blind:
- It classifies each difference as a timestamp (the keys made_at and adapted_at, both values of
  the form rig.stamp() writes), a path (a value or log line that becomes equal when the rig's
  absolute location is replaced by a placeholder, or the run record's from_the_record, which
  rig.py names relative to REPO, if both resolve to the same file), a log format difference (the
  two runners wrote their logs differently), or a FINDING (anything else). A difference of any
  other kind in any leaf or line is printed as a finding; nothing is dropped without a class.
- The canaries at the end run the same classifier on a perturbed copy of an in-place file: one
  mark value changed must come out a finding; only made_at changed must come out a timestamp and
  nothing else. If either canary fails, the comparison above it is not to be believed.
"""
import os, sys, re, json, copy
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", ".."))
REPO = os.path.normpath(os.path.join(RIG, "..", "..", ".."))
SC = os.path.join(RIG, "stage-B", "independent-check", "checks", "harness-programs-on-a-scratch-copy")
sys.path.insert(0, os.path.join(RIG, "code"))
import rig, record_adapter  # read only: the adapter's default --record

SCR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
SRIG = os.path.join(SCR, "W10 harness") if SCR else None
SREPO = os.path.normpath(os.path.join(SRIG, "..", "..", "..")) if SCR else None  # what rig.py computed there
STAMP = re.compile(r"^\d{4}-\d\d-\d\d \d\d:\d\d:\d\d$")
TIME_KEYS = {"made_at", "adapted_at"}
out = []
P = out.append


def walk(a, b, path=""):
    """Every leaf where a and b differ: (path, a, b). Keys on one side only, types and list
    lengths are differences too."""
    if type(a) is not type(b):
        return [(path, a, b)]
    if isinstance(a, dict):
        d = []
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                d.append((f"{path}/{k}", a.get(k, "<absent>"), b.get(k, "<absent>")))
            else:
                d += walk(a[k], b[k], f"{path}/{k}")
        return d
    if isinstance(a, list):
        d = []
        if len(a) != len(b):
            d.append((f"{path}/len", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            d += walk(x, y, f"{path}[{i}]")
        return d
    return [] if a == b else [(path, a, b)]


def classify_json(path, a, b):
    key = path.rsplit("/", 1)[-1]
    if key in TIME_KEYS and isinstance(a, str) and isinstance(b, str) and STAMP.match(a) and STAMP.match(b):
        return "timestamp"
    if key == "from_the_record" and SCR and isinstance(a, str) and isinstance(b, str):
        if os.path.normpath(os.path.join(REPO, a)) == os.path.normpath(os.path.join(SREPO, b)):
            return "path (the same record file, named relative to REPO, which rig.py computes from where the rig sits)"
    if isinstance(a, str) and isinstance(b, str) and SCR and a.replace(RIG, "<RIG>") == b.replace(SRIG, "<RIG>"):
        return "path"
    return "FINDING"


def compare_json(label, pa, pb):
    ba, bb = open(pa, "rb").read(), open(pb, "rb").read()
    if ba == bb:
        return {"identical": True, "diffs": []}
    diffs = [(p, x, y, classify_json(p, x, y)) for p, x, y in walk(json.loads(ba), json.loads(bb))]
    return {"identical": False, "diffs": diffs}


def report_json(label, pa, pb, where):
    r = compare_json(label, pa, pb)
    if r["identical"]:
        P(f"  {label}: byte-identical ({where})")
    else:
        P(f"  {label}: {len(r['diffs'])} leaf difference(s) ({where})")
        for p, x, y, c in r["diffs"]:
            P(f"      {c}: {p}: in place {json.dumps(x, ensure_ascii=False)[:120]} | scratch {json.dumps(y, ensure_ascii=False)[:120]}")
    return r


def parse_inplace_log(p):
    t = open(p, encoding="utf-8").read().split("\n")
    m = re.match(r"^command \(run from (.*)/\): (.*)$", t[0]); assert m, p
    e = re.match(r"^exit code: (\d+)$", t[1]); assert e, p
    assert t[2] == "--- stdout ---", p
    i = t.index("--- stderr ---")
    so, se = t[3:i], [x for x in t[i + 1:] if x != ""]
    return {"dir": m.group(1), "command": m.group(2), "exit": int(e.group(1)), "lines": so + se, "stderr": se}


def parse_scratch_log(p, has_head=True):
    t = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    if not has_head:
        return {"command": None, "exit": None, "lines": t}
    m = re.match(r"^command: (.*)$", t[0]); assert m, p
    e = re.match(r"^exit code: (\d+)$", t[-1]); assert e, p
    return {"command": m.group(1), "exit": int(e.group(1)), "lines": t[1:-1]}


def classify_line(a, b):
    if a == b:
        return None
    if SCR and a.replace(RIG, "<RIG>") == b.replace(SRIG, "<RIG>"):
        return "path"
    return "FINDING"


def compare_log(label, pa, pb, has_head=True):
    A, B = parse_inplace_log(pa), parse_scratch_log(pb, has_head)
    d = []
    if not has_head:
        d.append(("log format", "the scratch runner wrote this log with no command line and no exit code "
                                "(run.sh redirected the adapter's output only)"))
    else:
        if A["command"] != B["command"]:
            if A["command"].replace('"', "") == B["command"]:
                d.append(("log format", "the command's quotes: the scratch runner echoed $*, which drops the "
                                        "quotes around ../stage-B; the argument the program received is the same"))
            else:
                d.append(("FINDING", f"command differs: in place {A['command']!r} | scratch {B['command']!r}"))
        if A["exit"] != B["exit"]:
            d.append(("FINDING", f"exit code: in place {A['exit']} | scratch {B['exit']}"))
    d.append(("log format", "the in-place log has the exit code at its head and stdout and stderr apart; "
                            "the scratch log put the exit code last and the two streams together"))
    if A["stderr"]:
        d.append(("note", f"in place, stderr had {len(A['stderr'])} line(s), compared after stdout"))
    if len(A["lines"]) != len(B["lines"]):
        d.append(("FINDING", f"output lines: in place {len(A['lines'])} | scratch {len(B['lines'])}"))
    for i, (x, y) in enumerate(zip(A["lines"], B["lines"])):
        c = classify_line(x, y)
        if c:
            d.append((c, f"line {i + 1}: in place {x!r} | scratch {y!r}"))
    return A, B, d


# ---------------------------------------------------------------------------------------------
P("07: the in-place collection against the scratch-copy run")
P(f"  in place: {RIG}")
P(f"  scratch copy, committed files: {os.path.relpath(SC, RIG)}")
P(f"  scratch copy, its working folder: {SCR or '(not given: marks files and run records not compared)'}")
P("")

# 0. is the working folder the same run as the committed files?
if SCR:
    P("0. The scratch working folder is the run whose files were committed (byte comparison of all nine)")
    same_run = True
    for f in sorted(os.listdir(SC)):
        if f == "run.sh":
            continue
        src = os.path.join(SCR, f) if f.endswith(".txt") else os.path.join(SRIG, "marking", f)
        ok = open(src, "rb").read() == open(os.path.join(SC, f), "rb").read()
        same_run &= ok
        P(f"  {f}: {'identical' if ok else 'DIFFERENT'}")
    P(f"  => {'the same run' if same_run else 'NOT the same run: the working folder is not to be used'}")
    if not same_run:
        SCR = None
    P("")

# 1. the adapter's input
P("1. The adapter's input: the in-place run used record_adapter.py's default --record; the scratch run passed it")
runsh = open(os.path.join(SC, "run.sh"), encoding="utf-8").read()
m = re.search(r'record_adapter\.py --record "([^"]+)"', runsh)
P(f"  default --record (record_adapter.RECORD): {record_adapter.RECORD}")
P(f"  --record in run.sh:                        {m.group(1) if m else '(not found)'}")
P(f"  => {'the same path' if m and m.group(1) == record_adapter.RECORD else 'FINDING: different'}")
P("")

findings = []
tally = {}


def note(label, diffs):
    for c, *_ in diffs:
        tally.setdefault(c, 0); tally[c] += 1
        if c == "FINDING":
            findings.append(label)


# 2. the output files under marking/
P("2. The output files the six commands wrote under marking/")
M = os.path.join(RIG, "marking")
for f in ("marks_first_record96.json", "marks_second_record96.json",
          "agreement_markers_record96.json", "stage_b_record96.json"):
    if os.path.exists(os.path.join(SC, f)):
        r = report_json(f, os.path.join(M, f), os.path.join(SC, f), "counterpart: the committed folder")
    elif SCR:
        r = report_json(f, os.path.join(M, f), os.path.join(SRIG, "marking", f),
                        "counterpart: the scratch working folder; not in the committed folder")
    else:
        P(f"  {f}: no counterpart in the committed folder; not compared"); continue
    note(f, [(c,) for *_, c in r["diffs"]])
mp = "secret_mapping_record96.json"
if SCR:
    report_json(mp + " (read, not written, by the six)", os.path.join(M, mp), os.path.join(SRIG, "marking", mp),
                "counterpart: the scratch working folder")
P("")

# 3. the run records the adapter wrote
if SCR:
    P("3. The 96 run records record_adapter.py wrote (runs/record96/, gitignored on both sides)")
    ia, sa = sorted(os.listdir(os.path.join(rig.RUNS, "record96"))), sorted(os.listdir(os.path.join(SRIG, "runs", "record96")))
    P(f"  files: in place {len(ia)}, scratch {len(sa)}; same names: {ia == sa}")
    if ia != sa:
        findings.append("run record names"); tally["FINDING"] = tally.get("FINDING", 0) + 1
    kinds = {}
    for f in sorted(set(ia) & set(sa)):
        r = compare_json(f, os.path.join(rig.RUNS, "record96", f), os.path.join(SRIG, "runs", "record96", f))
        for p, x, y, c in r["diffs"]:
            kinds.setdefault((p, c), []).append(f)
            if c == "FINDING":
                P(f"      FINDING {f} {p}: in place {x!r} | scratch {y!r}")
        note(f"runs/record96/{f}", [(c,) for *_, c in r["diffs"]])
    for (p, c), fs in sorted(kinds.items()):
        P(f"  {c}: {p} differs in {len(fs)} of {len(ia)} run records")
    ex = json.load(open(os.path.join(rig.RUNS, "record96", ia[0])))["from_the_record"]
    ey = json.load(open(os.path.join(SRIG, "runs", "record96", ia[0])))["from_the_record"]
    P(f"    for example {ia[0]}: in place {ex!r}; scratch {ey!r}")
    P("")

# 4. the logs
P("4. The logs, line by line (in place: this folder; scratch: the committed folder)")
C = HERE
pairs = [("00b-record-adapter.txt", "00-adapter.txt", False), ("01-first-collect.txt", "01-first-collect.txt", True),
         ("02-second-collect.txt", "02-second-collect.txt", True), ("03-validate-first.txt", "03-validate-first.txt", True),
         ("04-validate-second.txt", "04-validate-second.txt", True), ("05-compare.txt", "05-compare.txt", True),
         ("06-stage-b.txt", "06-stage-b.txt", True)]
for a, b, head in pairs:
    A, B, d = compare_log(a, os.path.join(C, a), os.path.join(SC, b), head)
    P(f"  {a} vs {b}: exit in place {A['exit']}, scratch {B['exit'] if B['exit'] is not None else '(not logged)'}; "
      f"output lines {len(A['lines'])} / {len(B['lines'])}")
    for c, t in d:
        P(f"      {c}: {t}")
    note(a, [(c,) for c, _ in d])
P("")

# 5. canaries: the classifier on the thing it must catch, and on its nearest innocent neighbour
P("5. Canaries (the classifier run on perturbed copies of an in-place file; nothing is written)")
first = json.load(open(os.path.join(M, "marks_first_record96.json")))
rid = sorted(first["marks"])[0]
fld = "test_remove"
orig = first["marks"][rid].get(fld)
bad = copy.deepcopy(first); bad["marks"][rid][fld] = "a value no marker wrote"
d1 = [(p, classify_json(p, x, y)) for p, x, y in walk(bad, first)]
ok1 = d1 == [(f"/marks/{rid}/{fld}", "FINDING")]
P(f"  one mark changed ({rid}.{fld}: {orig!r} -> 'a value no marker wrote'): {d1} -> {'caught' if ok1 else 'CANARY FAILED'}")
tim = copy.deepcopy(first); tim["made_at"] = "2000-01-01 00:00:00"
d2 = [(p, classify_json(p, x, y)) for p, x, y in walk(tim, first)]
ok2 = d2 == [("/made_at", "timestamp")]
P(f"  only made_at changed: {d2} -> {'timestamp only' if ok2 else 'CANARY FAILED'}")
lineA = "  test_remove                        within-step       94         2           0"
lineB = "  test_remove                        within-step       93         3           0"
ok3 = classify_line(lineB, lineA) == "FINDING"
P(f"  one count changed in a log line: {classify_line(lineB, lineA)} -> {'caught' if ok3 else 'CANARY FAILED'}")
ok4 = True
if SCR:
    wa = f"96 marked, 0 missing []; written {RIG}/marking/marks_second_record96.json."
    wb = f"95 marked, 1 missing []; written {SRIG}/marking/marks_second_record96.json."
    wc = f"96 marked, 0 missing []; written {SRIG}/marking/marks_second_record96.json."
    ok4 = classify_line(wa, wb) == "FINDING" and classify_line(wa, wc) == "path"
    P(f"  a log line differing by path and by a count: {classify_line(wa, wb)}; by path only: {classify_line(wa, wc)}"
      f" -> {'the path class hides nothing else' if ok4 else 'CANARY FAILED'}")
P("")

P("Result")
P(f"  differences by class: {json.dumps(tally)}")
P(f"  FINDINGS: {len(findings)}" + (f" -> {findings}" if findings else ""))
okc = ok1 and ok2 and ok3 and ok4
P(f"  canaries: {'all behaved' if okc else 'FAILED: do not believe the comparison'}")
print("\n".join(out))
sys.exit(0 if (not findings and okc) else 1)
