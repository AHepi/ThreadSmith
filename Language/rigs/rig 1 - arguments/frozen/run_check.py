# run_check.py
# What this file does: takes a ledger, runs the s(CASP) checker on it several times
# (taking lines out to see what changes), and writes a plain-prose report that points
# at the writer's own sentences. It never guesses: every sentence in the report is built
# from fixed templates plus the ledger's own wording.
import json, re, subprocess, sys, os, tempfile, time

SCASP = "/home/claude/sCASP/scasp"
RULES = open(os.path.join(os.path.dirname(__file__), "checker_rules.pl")).read()
TIME_LIMIT_SECONDS = 20

def run_query(ledger_text, query, removed_lines=()):
    """Run one question against the ledger with some lines taken out. Returns (list of answers, seconds, timed_out)."""
    kept = ledger_text
    for line_id in removed_lines:
        kept = re.sub(r"\bline\(%s\)\.\s*" % re.escape(str(line_id)), "", kept, count=1)
    program = RULES + "\n" + kept + "\n?- " + query + ".\n"
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as handle:
        handle.write(program); path = handle.name
    started = time.time()
    try:
        done = subprocess.run([SCASP, "--tree", "--human", "-s0", "--unknown=fail", path], stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, timeout=TIME_LIMIT_SECONDS,
                              env=dict(os.environ, LANG="C.UTF-8"))
        output = done.stdout + done.stderr
        timed_out = False
    except subprocess.TimeoutExpired:
        output, timed_out = "", True
    seconds = time.time() - started
    os.unlink(path)
    answers = []
    for block in re.split(r"%\s+Answer \d+.*\n", output)[1:]:
        tree = block.split("% Model")[0].replace("% Justification", "").strip("\n")
        lines_used = sorted(set(re.findall(r"line (\w+) is in the ledger", tree)), key=str)
        assumptions = sorted(set(a.strip().rstrip(",").replace(", and","").replace(", because","")
                                 for a in re.findall(r"there is no evidence that ([^\n]+)", tree)
                                 if "is in the ledger" not in a))
        bindings = dict((k, v.rstrip(",").strip()) for k, v in re.findall(r"^(\w+) = (.+?)\s*$", block.split("% Bindings")[-1], re.M)) if "% Bindings" in block else {}
        answers.append({"tree": tree, "lines": lines_used, "assumptions": assumptions, "bindings": bindings})
    return answers, seconds, timed_out, output

def describe_lines(meta, line_ids):
    parts = []
    for line_id in line_ids:
        info = meta["lines"][line_id]
        parts.append('  - line %s [%s, sentence %s]: %s' % (line_id, info["mark"], info["sentence"], info["text"]))
    return "\n".join(parts)

def guessed_lines(meta, line_ids):
    return [l for l in line_ids if meta["lines"][l]["mark"] != "said"]

def smallest_set(ledger_text, query, line_ids):
    """Take lines out one at a time. A line stays in the set only if taking it out makes the finding go away."""
    needed = []
    for line_id in line_ids:
        answers, _, _, _ = run_query(ledger_text, query, removed_lines=[line_id])
        if not answers:
            needed.append(line_id)
    return needed

def check(ledger_path, log):
    ledger_text = open(ledger_path).read()
    meta = json.load(open(ledger_path.replace(".pl", ".json")))
    report, slowest = [], 0.0
    def ask(query, removed=()):
        nonlocal slowest
        answers, seconds, timed_out, raw = run_query(ledger_text, query, removed)
        slowest = max(slowest, seconds)
        log.write("\n=== %s | query: %s | removed: %s | %.2fs | timed out: %s ===\n%s\n" % (meta["paragraph"], query, list(removed), seconds, timed_out, raw))
        if timed_out: report.append("RAN OUT OF TIME on the question: " + query)
        return answers

    # ---- check 1: contradictions ----
    seen = set()
    for answer in ask("contradiction(F)"):
        fact = answer["bindings"].get("F", "?")
        if fact in seen: continue
        seen.add(fact)
        needed = smallest_set(ledger_text, "contradiction(%s)" % fact, answer["lines"])
        text = "CONTRADICTION about %s.\nThese lines cannot all hold (each one was taken out in turn; the contradiction went away every time):\n%s" % (fact, describe_lines(meta, needed))
        extra = [l for l in answer["lines"] if l not in needed]
        if extra: text += "\nAlso used, but the contradiction survives without them:\n" + describe_lines(meta, extra)
        if guessed_lines(meta, needed): text += "\nNOTE: this finding leans on lines you did not write: %s. If they are wrong, ignore it." % ", ".join(guessed_lines(meta, needed))
        report.append(text)
    lines_in_contradiction = set()
    for item in report:
        lines_in_contradiction |= set(re.findall(r"- line (\w+) \[", item.split("Also used")[0]))

    # ---- check 2: "because" claims ----
    for claim in ask("claim_because(N, E, C)"):
        n, effect, cause = claim["bindings"]["N"], claim["bindings"]["E"], claim["bindings"]["C"]
        head = 'BECAUSE-claim on line %s: "%s".' % (n, meta["lines"][n]["text"])
        all_routes = ask("holds(%s)" % effect)
        direct = [r["lines"][0] for r in all_routes if len(r["lines"]) == 1]      # lines that simply state the effect
        routes = ask("holds(%s)" % effect, removed=direct) if direct else all_routes
        cause_lines = sorted({l for r in ask("holds(%s)" % cause) for l in r["lines"]})
        if not routes:
            report.append(head + "\nJUMP. Leaving aside the line(s) that simply state it (%s), nothing in the ledger makes %s follow." % (", ".join(direct) or "none", effect))
            continue
        route = routes[0]
        text = head + "\nFOLLOWS, using:\n" + describe_lines(meta, route["lines"])
        if route["assumptions"]:
            text += "\nBUT ONLY ON ASSUMPTIONS NOBODY STATED:\n" + "\n".join("  - there is no evidence that " + a for a in route["assumptions"])
        without_cause = ask("holds(%s)" % effect, removed=direct + cause_lines)
        if without_cause: text += "\nIDLE CAUSE: with the stated cause taken out (%s), it still follows. The cause is doing no work." % ", ".join(cause_lines)
        else: text += "\nThe stated cause does work: with it taken out (%s), this no longer follows." % ", ".join(cause_lines)
        bad = [l for l in route["lines"] if l in lines_in_contradiction]
        if bad: text += "\nCANNOT BE LEANED ON YET: it uses line(s) %s, which are part of a contradiction above." % ", ".join(bad)
        if guessed_lines(meta, route["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, route["lines"]))
        report.append(text)

    # ---- check 3: plans ----
    for claim in ask("claim_plan(N, A, F)"):
        n, action, fact = claim["bindings"]["N"], claim["bindings"]["A"], claim["bindings"]["F"]
        head = 'PLAN on line %s: "%s".' % (n, meta["lines"][n]["text"])
        works = ask("achieves(%s, %s)" % (action, fact))
        if works:
            report.append(head + "\nThe action does touch something the goal depends on, using:\n" + describe_lines(meta, works[0]["lines"]))
        else:
            why = ask("not achieves(%s, %s)" % (action, fact))
            changed = ask("changes(%s, X)" % action)
            reaches = ask("depends_on(%s, X)" % fact)
            text = head + "\nKIND MISTAKE (the plan cannot work as written). "
            text += "Doing %s changes only: %s. " % (action, ", ".join(sorted({c["bindings"]["X"] for c in changed})) or "nothing the ledger knows of")
            text += "But %s depends only on: %s. These do not meet." % (fact, ", ".join(sorted({r["bindings"]["X"] for r in reaches})) or "nothing the ledger knows of")
            used = sorted({l for c in changed + reaches for l in c["lines"]})
            text += "\nLines used:\n" + describe_lines(meta, used)
            if guessed_lines(meta, used): text += "\nNOTE: leans on lines you did not write: %s. If they are wrong, ignore it." % ", ".join(guessed_lines(meta, used))
            text += "\n(The checker's own proof that the plan fails was %s.)" % ("found" if why else "NOT found")
            report.append(text)

    # ---- check 4: an exception to a "usually" line, with no reason given ----
    for found in ask("exception(N, X)"):
        n, thing = found["bindings"]["N"], found["bindings"]["X"]
        if not ask("exception_reason(%s, %s, R)" % (n, thing)):
            report.append('UNEXPLAINED EXCEPTION: line %s ("%s") is a "usually" line, and %s is an exception to it, but the ledger gives no reason why. Until there is a reason, nothing tells %s apart from the other cases line %s is used for.' % (n, meta["lines"][n]["text"], thing, thing, n))

    # ---- the gauge ----
    marks = [v["mark"] for v in meta["lines"].values()]
    gauge = "GAUGE: %d lines said, %d filled in, %d usual case; %d of %d sentences went to the leftover bin (not checked)%s. Slowest question: %.2f seconds." % (
        marks.count("said"), marks.count("filled in"), marks.count("usual case"), len(meta["leftover"]), len(meta["sentences"]),
        (": " + "; ".join(meta["leftover"])) if meta["leftover"] else "", slowest)
    if not any(k in r for r in report for k in ("CONTRADICTION", "JUMP", "KIND MISTAKE", "IDLE", "CIRCLE", "UNEXPLAINED")):
        report.insert(0, "NO FAULT FOUND in the lines that were checked.")
    return "REPORT for paragraph %s\n\n" % meta["paragraph"] + "\n\n".join(report) + "\n\n" + gauge + "\n"

if __name__ == "__main__":
    with open(sys.argv[2], "a") as log:
        print(check(sys.argv[1], log))
