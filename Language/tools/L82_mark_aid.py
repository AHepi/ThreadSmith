#!/usr/bin/env python3
"""L82_mark_aid.py OUT_DIR: a reading aid for marking Arm B (plan L82, eighth version). It is not an instrument the plan
freezes and it decides nothing: it lists, per ledger and per output, the fields the thirteen rows read, so the marker
reads them in one place and then reads the files themselves. Written 22 September 2026 beside the run; no earlier version."""
import os, re, sys, json

KINDS = ["JUMP", "NO CONNECTION", "CANNOT TELL", "YOU CLAIM AND DENY THE SAME CAUSE", "YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY",
         "FOLLOWS ONLY IF THE CAUSE IS GRANTED", "FOLLOWS", "CIRCLE", "TO BE EXPECTED", "KIND MISTAKE", "The action does touch", "CONTRADICTION", "Fine."]

def sections(report):
    """Split a new-driver report into the actual ledger's part and each world's part (by the INSIDE / UNDER headings)."""
    parts = {"actual": []}; cur = "actual"
    for line in report.splitlines():
        m = re.match(r"^(INSIDE|UNDER THE SUPPOSITION) '([^']+)'", line)
        if m: cur = m.group(2); parts.setdefault(cur, [])
        elif line.startswith("GAUGE:"): cur = "gauge"; parts.setdefault(cur, [])
        parts[cur].append(line)
    return {k: "\n".join(v) for k, v in parts.items()}

def kinds_in(text):
    found = []
    for k in KINDS:
        n = len(re.findall(r"(?m)^\s*%s" % re.escape(k), text)) if k not in ("The action does touch", "TO BE EXPECTED") else text.count(k)
        if n: found.append("%s x%d" % (k, n))
    return found

def heads(text):
    return re.findall(r"(?m)^\s*((?:BECAUSE|SINCE|PLAN|DENIED BECAUSE)-?[a-z]*(?:-claim)? on line \S+ \[[^\]]*\])", text)

def outcomes(text):
    m = re.search(r"OUTCOMES:\n((?:\s+.+\n?)+)", text)
    if not m: return {}
    d = {}
    for l in m.group(1).splitlines():
        if ":" in l: k, v = l.strip().split(":", 1); d[k.strip()] = v.strip()
    return d

def main():
    OUT = sys.argv[1]; rep = os.path.join(OUT, "reports")
    print("# L82 marking aid over", OUT)
    counts = open(os.path.join(OUT, "ledgers", "COUNTS.txt")).read() if os.path.exists(os.path.join(OUT, "ledgers", "COUNTS.txt")) else ""
    print("\n## COUNTS (B5)\n" + counts)
    print("## Reports, per ledger (B1, B2, B4, B8, B10, B11)")
    for f in sorted(os.listdir(rep)):
        if not (f.endswith(".new.txt") or f.endswith(".old.txt")): continue
        text = open(os.path.join(rep, f)).read()
        if not text.strip(): print("\n###", f, "EMPTY"); continue
        print("\n###", f)
        for name, part in sections(text).items():
            if name == "gauge":
                g = part.splitlines(); print("  gauge:", re.sub(r"\(not checked\): .*?\. Slowest", "(not checked). Slowest", g[0], flags=re.S)[:160]); [print("   ", l.strip()) for l in g[1:] if l.strip()]; continue
            k = kinds_in(part); h = heads(part); o = outcomes(part)
            print("  [%s] kinds: %s" % (name, ", ".join(k) or "none"))
            for x in h: print("    head:", x)
            if o: print("    outcomes: because=%s | since=%s | plans=%s | denied=%s | contradictions=%s" % (o.get("because claims"), o.get("since claims"), o.get("plans"), o.get("denied because"), o.get("contradictions")))
            if f.endswith(".old.txt") and re.search(r"(?m)^(BECAUSE-claim|SINCE-claim|PLAN|CANNOT TELL|JUMP|NO CONNECTION)", part): print("    OLD DRIVER prints a BECAUSE/SINCE/PLAN finding here (B8 reads this)")
    print("\n## Sameness within pairs and rewordings (B3, B12): ONLY and OPPOSITE lines with their sentence numbers")
    sd = os.path.join(OUT, "sameness")
    for f in sorted(os.listdir(sd)):
        text = open(os.path.join(sd, f)).read(); print("\n###", f)
        for bucket in ("ONLY THE FIRST SAYS", "ONLY THE SECOND SAYS", "OPPOSITE"):
            m = re.search(r"%s \((\d+)[^)]*\):\n((?:  .*\n?)*)" % re.escape(bucket), text)
            if not m: print("  %s: (heading not found)" % bucket); continue
            n = int(m.group(1)); lines = [l.strip() for l in m.group(2).splitlines() if l.strip()]
            sents = sorted(set(re.findall(r"sentence (\d+)", m.group(2))))
            print("  %s: %d; sentences %s" % (bucket, n, ", ".join(sents) or "-"))
            for l in lines[:12]: print("    ", l[:150])
        m = re.search(r"BIN ENTRIES: .*", text); print("  ", m.group(0) if m else "")
    print("\n## Reader (B6): parts 2 and 3 per report")
    rd = os.path.join(OUT, "reader"); key = json.load(open(os.path.join(rd, "KEY_report_names.json")))
    for code in sorted(key):
        e = key[code]; p = os.path.join(rd, code + ".response.txt"); ans = open(p).read() if os.path.exists(p) else "(no response)"
        m2 = re.search(r"(?s)\n\s*2\.(.*?)\n\s*3\.", ans); m3 = re.search(r"(?s)\n\s*3\.(.*?)\n\s*4\.", ans); m1 = re.search(r"(?s)\n\s*1\.(.*?)\n\s*2\.", ans)
        print("\n### %s = %s (worlds %s; still present %s)" % (code, e["report"], e.get("worlds"), e.get("name_still_present")))
        print("  part 1:", re.sub(r"\s+", " ", m1.group(1))[:500] if m1 else "(not parsed)")
        print("  part 2:", re.sub(r"\s+", " ", m2.group(1))[:300] if m2 else "(not parsed)")
        print("  part 3:", re.sub(r"\s+", " ", m3.group(1))[:300] if m3 else "(not parsed)")
    print("\n## Prose reader (B10, B11, B13): part 1 labels, part 2, part 3 per report")
    pd = os.path.join(OUT, "prose_reader")
    for f in sorted(x for x in os.listdir(pd) if x.endswith(".response.txt")):
        ans = open(os.path.join(pd, f)).read(); print("\n###", f)
        labels = {k: len(re.findall(k, ans)) for k in ("claimed as a fact in the passage", "hedged in the passage", "not made in the passage", "cannot tell from the report")}
        print("  labels:", labels)
        for l in ans.splitlines():
            if re.search(r"JUMP|NO CONNECTION|CANNOT TELL|CLAIM AND DENY|DENIED BECAUSE|BECAUSE-claim|SINCE-claim", l) and re.search(r"claimed as a fact|hedged|not made|cannot tell", l): print("   ", l.strip()[:220])
        m2 = re.search(r"(?s)\n\s*2\.(.*?)\n\s*3\.", ans); m3 = re.search(r"(?s)\n\s*3\.(.*?)\n\s*4\.", ans)
        print("  part 2:", re.sub(r"\s+", " ", m2.group(1))[:300] if m2 else "(not parsed)")
        print("  part 3:", re.sub(r"\s+", " ", m3.group(1))[:200] if m3 else "(not parsed)")
    for d in ("reader", "prose_reader"):
        for n in ("FAILED.txt", "SKIPPED.txt"):
            p = os.path.join(OUT, d, n); c = open(p).read().strip() if os.path.exists(p) else "(missing)"
            print("\n%s/%s: %s" % (d, n, c or "empty"))

if __name__ == "__main__": main()
