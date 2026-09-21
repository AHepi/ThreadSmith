# run_check.py
# What this file does: takes a ledger, runs the s(CASP) checker on it several times
# (taking lines out to see what changes), and writes a plain-prose report that points
# at the writer's own sentences. It never guesses: every sentence in the report is built
# from fixed templates plus the ledger's own wording.
import json, re, subprocess, sys, os, tempfile, time

SCASP = "/home/claude/sCASP/scasp"
RULES = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "checker_rules.pl")).read()
TIME_LIMIT_SECONDS = 20

def run_query(ledger_text, query, removed_lines=(), extra=""):
    """Run one question against the ledger with some lines taken out. Returns (list of answers, seconds, timed_out)."""
    kept = ledger_text
    for line_id in removed_lines:
        kept = re.sub(r"\bline\(%s\)\.\s*" % re.escape(str(line_id)), "", kept, count=1)
    program = RULES + "\n" + kept + "\n" + extra + "\n?- " + query + ".\n"
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
    def ask(query, removed=(), extra=""):
        nonlocal slowest
        answers, seconds, timed_out, raw = run_query(ledger_text, query, removed, extra)
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

    # ---- check 2: "because" claims (PATCHED: patches 1, 2, 3) ----
    circle_causes, observed_claims = set(), []
    for claim in ask("claim_because(N, E, C)"):
        n, effect, cause = claim["bindings"]["N"], claim["bindings"]["E"], claim["bindings"]["C"]
        head = 'BECAUSE-claim on line %s: "%s".' % (n, meta["lines"][n]["text"])
        direct = sorted({r["lines"][0] for r in ask("holds(%s)" % effect) if len(r["lines"]) == 1})   # lines that simply state the effect
        routes = ask("produced(%s)" % effect, removed=direct)
        cause_routes = ask("holds(%s)" % cause)
        cause_lines = sorted({l for r in cause_routes for l in r["lines"]})
        if routes:
            route = routes[0]
            text = head + "\nFOLLOWS, using:\n" + describe_lines(meta, route["lines"])
            if route["assumptions"]:
                text += "\nBUT ONLY ON ASSUMPTIONS NOBODY STATED:\n" + "\n".join("  - there is no evidence that " + a for a in route["assumptions"])
            if ask("produced(%s)" % effect, removed=direct + cause_lines): text += "\nIDLE CAUSE: with the stated cause taken out (%s), it is still produced. The cause is doing no work." % ", ".join(cause_lines)
            else: text += "\nThe stated cause does work: with it taken out (%s), this is no longer produced." % ", ".join(cause_lines)
            bad = [l for l in route["lines"] if l in lines_in_contradiction]
            if bad: text += "\nCANNOT BE LEANED ON YET: it uses line(s) %s, which are part of a contradiction above." % ", ".join(bad)
            if guessed_lines(meta, route["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, route["lines"]))
            if direct: observed_claims.append((n, route["lines"]))
            report.append(text); continue
        # PATCH 2: is the only support for the cause the effect itself?
        if cause_routes and not ask("holds(%s)" % cause, removed=direct):
            circle_causes.add(cause)
            report.append(head + "\nCIRCLE. The only reason the ledger gives for %s is %s, and the only thing said to produce %s is %s. Take out the line(s) that simply state the effect (%s) and both fall together. Lines in the circle:\n%s" % (
                cause, effect, effect, cause, ", ".join(direct), describe_lines(meta, sorted(set(cause_lines) | {n}))))
            continue
        # suppose the cause is true, and see whether the effect is then produced
        supposed = "" if cause_routes else "holds(%s).\n" % cause
        if ask("produced(%s)" % effect, removed=direct, extra=supposed):
            report.append(head + "\nFOLLOWS ONLY IF THE CAUSE IS GRANTED. Nothing else in the ledger supports: %s." % cause); continue
        text = head + "\nJUMP. Even granting the stated cause, nothing in the ledger produces %s." % effect
        # name the missing line: let the checker assume lines nobody wrote, and report which ones it needed
        abduce = supposed + "#abducible missing(X).\nholds(X) :- missing(X).\n"
        candidates = sorted({m for r in ask("produced(%s)" % effect, removed=direct, extra=abduce)
                               for m in re.findall(r"would be needed: (\w+\((?:[^()]|\([^()]*\))*\)|\w+)", r["tree"])})
        good, rejected = [], []
        for candidate in candidates:
            if re.search(r"\b[A-Z_]\w*", candidate): continue                     # not a definite line (still has a blank in it)
            if ask("denied(%s)" % candidate): rejected.append(candidate); continue    # limit on filling in: must not contradict the ledger
            if ask("produced(%s)" % effect, removed=direct, extra=supposed + "holds(%s).\n" % candidate): good.append(candidate)
        if good: text += "\nA single line that would close the jump, which nobody wrote: " + "; or: ".join(good)
        if rejected: text += "\nLines that would also close it but are ruled out, because the ledger denies them: " + "; ".join(rejected)
        report.append(text)

    # ---- check 2b (PATCH 6, forced by the owner's Markus paragraph): SINCE. A reason to EXPECT something, not a cause of it.
    # Tested on what follows by ANY route (what SHOWS as well as what MAKES), and reported with its unstated assumptions.
    supports = []
    for claim in ask("claim_since(N, E, C)"):
        n, expected, reason = claim["bindings"]["N"], claim["bindings"]["E"], claim["bindings"]["C"]
        head = 'SINCE-claim on line %s: "%s". (A reason to expect, not a cause.)' % (n, meta["lines"][n]["text"])
        direct = sorted({r["lines"][0] for r in ask("holds(%s)" % expected) if len(r["lines"]) == 1})
        reason_lines = sorted({l for r in ask("holds(%s)" % reason) for l in r["lines"] if len(r["lines"]) <= 2})
        routes = [r for r in ask("holds(%s)" % expected, removed=direct) if set(reason_lines) & set(r["lines"])]
        if routes:
            route = min(routes, key=lambda r: len(r["lines"]))
            text = head + "\nTO BE EXPECTED, using:\n" + describe_lines(meta, route["lines"])
            if route["assumptions"]: text += "\nBUT ONLY ON ASSUMPTIONS NOBODY STATED:\n" + "\n".join("  - there is no evidence that " + a for a in route["assumptions"])
            text += "\nA habit or a pattern tells you about the occasions it was drawn from. Whether this occasion is like them is for you to judge."
            if guessed_lines(meta, route["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, route["lines"]))
            supports.append((n, expected, reason, True, direct, route["lines"]))
        else:
            text = head + "\nNO CONNECTION. Nothing in the ledger leads from the reason to what is expected."
            abduce = "#abducible missing(X).\nholds(X) :- missing(X).\n"
            cands = sorted({m for r in ask("holds(%s)" % expected, removed=direct + [l for l in meta["lines"] if l not in reason_lines and meta["lines"][l].get("habit")], extra=abduce)
                            for m in re.findall(r"would be needed: (\w+\((?:[^()]|\([^()]*\))*\)|\w+)", r["tree"])})
            text += "\nIt would take a line nobody wrote, of this kind: a general line saying that someone who %s does %s." % (reason, expected)
            supports.append((n, expected, reason, False, direct, []))
        report.append(text)
    # PATCH 7 (forced by the owner's Mondays paragraph; corrected after it broke the Markus report): a CHAIN of reasons.
    # The final conclusion is the one argued for last. A conclusion stands if ANY step for it holds (two routes to one job).
    # A step that connects, but only by leaning on the bare statement of an earlier conclusion that failed, inherits the break.
    if supports:
        ordered = sorted(supports, key=lambda s: int(s[0]) if s[0].isdigit() else 0)
        final = ordered[-1][1]
        stands, failed_direct, rows, first_break, held = {}, set(), [], None, 0
        for n, e, c, ok, direct, route_lines in ordered:
            if not ok: state = "NO CONNECTION"
            elif set(route_lines) & failed_direct: state = "connects, BUT ONLY BY LEANING ON A CONCLUSION THAT ALREADY FAILED (line %s)" % ", ".join(sorted(set(route_lines) & failed_direct))
            else: state = "holds"
            if state == "holds": held += 1; stands[e] = True
            else:
                stands.setdefault(e, False)
                if first_break is None: first_break = n
            rows.append("  line %s: %s  ->  %s" % (n, meta["lines"][n]["text"], state))
            if not stands[e]: failed_direct |= set(direct)
            else: failed_direct -= set(direct)
        text = "THE CHAIN, step by step:\n" + "\n".join(rows)
        text += "\nTHE FINAL CONCLUSION, the one argued for last: %s.\n%d of %d steps hold. " % (final, held, len(ordered))
        if first_break: text += "The first step that fails is line %s. " % first_break
        text += "The final conclusion %s." % ("STANDS" if stands.get(final) else "DOES NOT STAND on this chain")
        spare = [n for n, e, _, ok, _, _ in ordered if e == final and not ok]
        if stands.get(final) and spare: text += "\n  Line(s) %s offer a reason that does not connect. Take it out and the conclusion stands exactly as before. It may be true, and it may matter to you, but it is doing no work in this argument." % ", ".join(spare)
        report.append(text)

    # ---- check 3: plans ----
    for claim in ask("claim_plan(N, A, F)"):
        n, action, fact = claim["bindings"]["N"], claim["bindings"]["A"], claim["bindings"]["F"]
        head = 'PLAN on line %s: "%s".' % (n, meta["lines"][n]["text"])
        works = ask("achieves(%s, %s)" % (action, fact))
        if works:
            text = head + "\nThe action does touch something the goal depends on, using:\n" + describe_lines(meta, works[0]["lines"])
            touched = {c["bindings"]["X"] for c in ask("changes(%s, X)" % action)}
            if touched & circle_causes: text += "\nBUT the plan acts on %s, whose only support is the CIRCLE found above." % ", ".join(sorted(touched & circle_causes))
            if guessed_lines(meta, works[0]["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, works[0]["lines"]))
            report.append(text)
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
    shortest = {}
    for found in ask("exception(N, X)"):                                   # keep one answer per exception: the one using fewest lines
        key = (found["bindings"]["N"], found["bindings"]["X"])
        if key not in shortest or len(found["lines"]) < len(shortest[key]["lines"]): shortest[key] = found
    for found in shortest.values():
        n, thing = found["bindings"]["N"], found["bindings"]["X"]
        explains_something_observed = any(n in lines for _, lines in observed_claims)
        has_reason = bool(ask("exception_reason(%s, %s, R)" % (n, thing)))
        if meta["lines"][n]["mark"] == "usual case" and not has_reason:
            # PATCH 4 (forced by paragraph F): the writer's own sentence goes against what usually happens
            said = [l for l in found["lines"] if meta["lines"][l]["mark"] == "said"]
            report.append('DEPARTURE FROM THE USUAL, NO REASON GIVEN. You said:\n%s\nThis goes against usual-case line %s ("%s"), and nothing in the ledger says why it happened here. In a story this may be exactly what you intend. If so, ignore it.\nNOTE: line %s is a usual-case line you did not write. If it is wrong, ignore this.' % (describe_lines(meta, said), n, meta["lines"][n]["text"], n))
        elif explains_something_observed and not has_reason:
            report.append('UNEXPLAINED EXCEPTION: line %s ("%s") is a "usually" line, and %s is an exception to it, but the ledger gives no reason why. Until there is a reason, nothing tells %s apart from the other cases line %s is used for.' % (n, meta["lines"][n]["text"], thing, thing, n))

    # ---- check 5 (PATCH 5, forced by paragraph F, fitted to that one paragraph): likeness between two events ----
    for claim in ask("claim_like(N, A, B)"):
        n, first, second = claim["bindings"]["N"], claim["bindings"]["A"], claim["bindings"]["B"]
        kinds_found = {first: set(), second: set()}
        for item in report:
            kind_of_finding = re.match(r"[A-Z][A-Z ,\-]+", item)
            if not kind_of_finding or item.startswith(("BECAUSE", "PLAN", "LIKENESS")): continue
            for line_id in re.findall(r"line (\w+)", item):
                event = meta["lines"].get(line_id, {}).get("event")
                if event in kinds_found: kinds_found[event].add(kind_of_finding.group(0).strip(" ,"))
        shared = kinds_found[first] & kinds_found[second]
        text = 'LIKENESS claimed on line %s: "%s". You do not say what the two have in common.\n' % (n, meta["lines"][n]["text"])
        if shared: text += "What the checker finds in both: " + "; ".join(sorted(shared)) + ".\nIf that is the likeness you mean, the paragraph never says so. If you mean something else, the ledger cannot see it."
        else: text += "The checker finds nothing the two have in common."
        report.append(text)

    # ---- the gauge ----
    marks = [v["mark"] for v in meta["lines"].values()]
    gauge = "GAUGE: %d lines said, %d filled in, %d usual case; %d of %d sentences went to the leftover bin (not checked)%s. Slowest question: %.2f seconds." % (
        marks.count("said"), marks.count("filled in"), marks.count("usual case"), len(meta["leftover"]), len(meta["sentences"]),
        (": " + "; ".join(meta["leftover"])) if meta["leftover"] else "", slowest)
    if not any(k in r for r in report for k in ("CONTRADICTION", "JUMP", "KIND MISTAKE", "IDLE", "CIRCLE", "UNEXPLAINED", "DEPARTURE", "NO CONNECTION")):
        report.insert(0, "NO FAULT FOUND in the lines that were checked.")
    return "REPORT for paragraph %s\n\n" % meta["paragraph"] + "\n\n".join(report) + "\n\n" + gauge + "\n"

if __name__ == "__main__":
    with open(sys.argv[2], "a") as log:
        print(check(sys.argv[1], log))
