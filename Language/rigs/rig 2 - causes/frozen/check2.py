# check2.py
# What this file does: runs a second-form ledger against the laws in s(CASP) and writes a plain report.
# For every movement the writer states, it asks whether the laws allow it, and if not, WHICH SLOT failed.
# It also handles what-if sentences (by changing the ledger and asking again) and proposes an abstraction from two events.
import json, re, subprocess, sys, os, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__))
LAWS = open(os.path.join(HERE, "laws.pl")).read()
SCASP = "/home/claude/sCASP/scasp"
WORDS = {"toward": "toward the %s", "away_from": "away from the %s"}
def say_direction(d):
    m = re.match(r"(toward|away_from)\((\w+)\)", d)
    return WORDS[m.group(1)] % m.group(2) if m else {"across": "sideways", "down": "down", "up": "up"}.get(d, d)
CLASS_WORDS = {"light_loose": "a light loose thing", "heavy_loose": "a heavy loose thing", "heavy_standing": "a heavy standing thing", "fixed": "a fixed thing"}

def ask(ledger, query, log, remove=(), swap=None):
    text = ledger
    for line_id in remove: text = re.sub(r"\bline\(%s\)\.\s*" % re.escape(str(line_id)), "", text, count=1)
    if swap: assert swap[0] in text, swap; text = text.replace(swap[0], swap[1])
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as f: f.write(LAWS + "\n" + text + "\n?- " + query + ".\n"); path = f.name
    start = time.time()
    try:
        out = subprocess.run([SCASP, "--tree", "--human", "-s0", "--unknown=fail", path], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=20, env=dict(os.environ, LANG="C.UTF-8"))
        raw, timed_out = out.stdout + out.stderr, False
    except subprocess.TimeoutExpired: raw, timed_out = "", True
    os.unlink(path); seconds = time.time() - start
    log.write("\n=== query: %s | removed: %s | swap: %s | %.2fs | timed out: %s ===\n%s\n" % (query, list(remove), swap, seconds, timed_out, raw))
    answers = []
    for block in re.split(r"%\s+Answer \d+.*\n", raw)[1:]:
        tree = block.split("% Model")[0]
        bind = dict((k, v.rstrip(",").strip()) for k, v in re.findall(r"^(\w+) = (.+?)\s*$", block.split("% Bindings")[-1], re.M)) if "% Bindings" in block else {}
        answers.append({"lines": sorted(set(re.findall(r"line (\w+) is in the ledger", tree))), "bind": bind})
    ask.slowest = max(getattr(ask, "slowest", 0), seconds); ask.timed_out = getattr(ask, "timed_out", False) or timed_out
    return answers

def name(meta, thing): return meta.get("names", {}).get(thing, "the " + thing)
def lines_text(meta, ids): return "\n".join("  - line %s [%s]: %s" % (i, meta["lines"][i]["mark"], meta["lines"][i]["text"]) for i in ids)
def guessed(meta, ids): return [i for i in ids if meta["lines"][i]["mark"] != "said"]

def findings_for(ledger, meta, log, remove=(), swap=None):
    """Returns a list of (pattern id, kind of finding, report text)."""
    found = []
    seen = set()
    for a in ask(ledger, "said_moves(E, T, D)", log, remove, swap):
        e, thing, d = a["bind"]["E"], a["bind"]["T"], a["bind"]["D"]
        if (e, thing, d) in seen: continue
        seen.add((e, thing, d)); said = a["lines"]
        ok = ask(ledger, "can_move(%s, %s, Why)" % (thing, d), log, remove, swap)
        head = "You said (line %s): %s." % (", ".join(said), "; ".join(meta["lines"][i]["text"] for i in said))
        if ok:
            found.append((e, "fine", head + "\n  FINE. The laws allow it (%s)." % ok[0]["bind"].get("Why", ""))); continue
        weak = ask(ledger, "press_on(%s, %s, Size, Src)" % (thing, d), log, remove, swap)
        freed = ask(ledger, "releases(E2, I, %s)" % thing, log, remove, swap)
        other = ask(ledger, "press_on(%s, D2, Size, Src)" % thing, log, remove, swap)
        if weak:
            res = ask(ledger, "resistance(%s, R)" % thing, log, remove, swap)[0]["bind"]["R"]
            used = sorted(set(weak[0]["lines"]) | set(said))
            text = head + "\n  THE STRENGTH SLOT FAILS. Something does press %s %s (%s), but that press is %s and %s resists with %s. A press is never bigger than what the pressed thing resists, so it is far too small to do this.\n  Lines used:\n%s" % (
                name(meta, thing), say_direction(d), weak[0]["bind"]["Src"], weak[0]["bind"]["Size"], name(meta, thing), res, lines_text(meta, used))
            kind = "strength"
        elif freed:
            tend = ask(ledger, "tendency(%s, D3)" % thing, log, remove, swap)
            used = sorted(set(freed[0]["lines"]) | set(said))
            text = head + "\n  A LETTING PRODUCED SOMETHING NEW. %s was let go. Letting go can only produce what the thing was already heading for, which is %s. Nothing presses it %s.\n  Lines used:\n%s" % (
                name(meta, thing).capitalize() if name(meta, thing).startswith('the') else name(meta, thing), say_direction(tend[0]["bind"]["D3"]) if tend else "nothing", say_direction(d), lines_text(meta, used))
            kind = "letting"
        elif other:
            used = sorted(set(other[0]["lines"]) | set(said))
            text = head + "\n  THE DIRECTION SLOT FAILS. %s is pressed %s, and nothing presses it %s.\n  Lines used:\n%s" % (name(meta, thing).capitalize() if name(meta, thing).startswith("the") else name(meta, thing), say_direction(other[0]["bind"]["D2"]), say_direction(d), lines_text(meta, used))
            kind = "direction"
        else:
            used = said
            text = head + "\n  A CHANGE FROM NOTHING. Nothing in the ledger presses the %s or lets it go.\n  Lines used:\n%s" % (thing, lines_text(meta, used))
            kind = "from nothing"
        if guessed(meta, used): text += "\n  NOTE: leans on lines you did not write: %s. If they are wrong, ignore this." % ", ".join(guessed(meta, used))
        found.append((e, kind, text))
    for a in ask(ledger, "said_stays(E, T)", log, remove, swap):
        e, thing = a["bind"]["E"], a["bind"]["T"]
        forced = ask(ledger, "must_move(%s, D, Why)" % thing, log, remove, swap)
        head = "You said (line %s): %s." % (", ".join(a["lines"]), "; ".join(meta["lines"][i]["text"] for i in a["lines"]))
        if forced: found.append((e, "must move", head + "\n  IT COULD NOT HAVE STAYED. The laws say the %s must move %s." % (thing, say_direction(forced[0]["bind"]["D"]))))
        else: found.append((e, "fine", head + "\n  FINE. Nothing forces it to move."))
    for a in ask(ledger, "social(E, W, I, T, R)", log, remove, swap):
        e, word = a["bind"]["E"], a["bind"]["W"]
        head = "You said (line %s): %s." % (", ".join(a["lines"]), "; ".join(meta["lines"][i]["text"] for i in a["lines"]))
        if ask(ledger, "word_misfit(%s, %s)" % (e, word), log, remove, swap):
            found.append((e, "word misfit", head + "\n  THE WORD DOES NOT FIT THE SLOTS. '%s' needs %s, and the text says the opposite." % (word.upper(), "the thing to have been heading that way already" if word != "makes" else "the thing NOT to have been heading that way")))
        elif not ask(ledger, "tendency_stated(%s)" % e, log, remove, swap):
            found.append((e, "note", head + "\n  FINE, BUT IT RESTS ON SOMETHING NOBODY STATED: '%s' only fits if %s." % (word.upper(), "they were already heading that way" if word != "makes" else "they were not already heading that way")))
        else: found.append((e, "fine", head + "\n  FINE. The word fits the slots."))
    return found

def abstraction(ledger, meta, log, found):
    events = meta.get("events", {})
    if len(events) < 2: return None
    feats = {}
    for name, ids in events.items():
        f = set()
        for e in ids:
            for q, label in (("presses(%s, I, T, D)" % e, "presses"), ("releases(%s, I, T)" % e, "lets go of"), ("holds_back(%s, I, T)" % e, "holds")):
                for a in ask(ledger, q, log):
                    ci = ask(ledger, "body(%s, C)" % a["bind"]["I"], log); ct = ask(ledger, "body(%s, C)" % a["bind"]["T"], log)
                    is_doer = bool(ask(ledger, "doer(%s)" % a["bind"]["I"], log))
                    f.add("%s %s %s" % ("a doer" if is_doer else CLASS_WORDS.get(ci[0]["bind"]["C"], "something") if ci else "something", label, CLASS_WORDS.get(ct[0]["bind"]["C"], "something") if ct else "something"))
            for (pe, kind, _) in found:
                if pe == e and kind not in ("fine", "note"): f.add("a law is broken"); f.add("which slot: " + kind)
        feats[name] = f
    names = list(feats); shared = set.intersection(*feats.values())
    differ = {n: sorted(x for x in feats[n] - shared if x.startswith("which slot")) for n in names}
    text = "PROPOSED ABSTRACTION from %s (a question, not a finding; fitted to these %d cases only).\n  In all of them: %s.\n" % (" and ".join(names), len(names), "; ".join(sorted(shared)) or "nothing the checker can see")
    text += "  They differ in: " + "; ".join("%s -> %s" % (n, ", ".join(differ[n]) or "no broken slot") for n in names) + "."
    return text

def report(path, log):
    ledger = open(path).read(); meta = json.load(open(path.replace(".pl", ".json")))
    found = findings_for(ledger, meta, log)
    out = ["REPORT for %s  [whose case: %s]" % (meta["paragraph"], meta["whose"]), ""]
    out += [t + "\n" for (_, _, t) in found]
    for w in meta.get("whatifs", []):
        remove = [w["remove_line"]] if "remove_line" in w else []
        swap = tuple(w["swap"]) if "swap" in w else None
        if "ask" in w: result = bool(ask(ledger, w["ask"], log, remove, swap)); 
        else: result = not any(k == w["finding_gone"] for (_, k, _) in findings_for(ledger, meta, log, remove, swap))
        out.append("WHAT-IF [%s]: \"%s\"\n  The checker made the change, kept everything that led up to it, and recomputed what follows. Your what-if %s.\n" % (w["whose"], w["text"], "HOLDS" if result == w["claims"] else "FAILS"))
    ab = abstraction(ledger, meta, log, found)
    if ab: out.append(ab + "\n")
    marks = [v["mark"] for v in meta["lines"].values()]
    out.append("GAUGE: %d lines said, %d filled in, %d usual case. Left in the bin: %s. Slowest question %.2f seconds%s." % (marks.count("said"), marks.count("filled in"), marks.count("usual case"), "; ".join(meta["leftover"]) or "nothing", ask.slowest, "; SOMETHING RAN OUT OF TIME" if ask.timed_out else ""))
    return "\n".join(out)

if __name__ == "__main__":
    with open(sys.argv[2], "a") as log: print(report(sys.argv[1], log))
