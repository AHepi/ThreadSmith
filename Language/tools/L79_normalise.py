#!/usr/bin/env python3
"""L79 normaliser: the instrument for expectation A1 of plan L79 (second version).

Reads a rig-1 report and returns its FINDINGS as canonical tuples, plus a list of
EXTRAS: blocks the second driver adds, each classified into a kind the plan lists,
or UNLISTED. A1 is met on a ledger when every finding of the old report is among
the findings of the new report (same kind, same line ids, same verdict word, same
world) and every extra of the new report is of a listed kind.

Usage: L79_normalise.py OLD_REPORT NEW_REPORT      -> prints the comparison, exit 0 if A1 holds
       L79_normalise.py REPORT                     -> prints the findings and extras of one report
Frozen with the plan; not edited after. Written from the old driver's report strings
(run_check.py) and the wordings fixed in plan L79 second version, sections D1 to D8.
"""
import re, sys

# The heads the OLD driver prints, in the order it prints them, with a regex that
# captures the line ids the head names and the verdict word that follows.
HEADS = [
    ("CONTRADICTION", r"^CONTRADICTION about (?P<fact>.+?)\.$", "CONTRADICTION"),
    ("BECAUSE", r'^BECAUSE-claim on line (?P<line>\S+?)(?: \[[^\]]*\])?: "', None),
    ("SINCE", r'^SINCE-claim on line (?P<line>\S+?)(?: \[[^\]]*\])?: "', None),
    ("CHAIN", r"^THE CHAIN, step by step:", None),
    ("FINAL", r"^THE FINAL CONCLUSION", None),
    ("PLAN", r'^PLAN on line (?P<line>\S+?)(?: \[[^\]]*\])?: "', None),
    ("DEPARTURE", r"^DEPARTURE FROM THE USUAL", "DEPARTURE"),
    ("EXCEPTION", r"^UNEXPLAINED EXCEPTION: line (?P<line>\S+)", "UNEXPLAINED EXCEPTION"),
    ("LIKENESS", r"^LIKENESS|^THESE TWO EVENTS", "LIKENESS"),
    ("TWO USUALLY", r"^TWO 'USUALLY' LINES PULL OPPOSITE WAYS about (?P<fact>.+?)\.", "PULL OPPOSITE"),
    ("EXEMPTION", r"^EXEMPTION FROM AN 'ALWAYS' LINE", "EXEMPTION"),
    ("ADDED LINES", r"^ADDED LINES ALONE GIVE THE CONCLUSION (?P<fact>\S+)", "ADDED LINES"),
    ("WHAT-IF", r'^WHAT-IF \[(?P<whose>[^\]]*)\](?: \(line [^)]*\))?: "', None),
    ("DENIED", r'^DENIED BECAUSE on line (?P<line>\S+?)(?: \[[^\]]*\])?: "', None),
    ("WORLD", r"^(?:INSIDE|UNDER THE SUPPOSITION) '(?P<world>[^']+)'", None),
    ("TIMEOUT", r"^RAN OUT OF TIME on the question: (?P<q>.+)$", "RAN OUT OF TIME"),
]
VERDICTS = ["FOLLOWS ONLY IF THE CAUSE IS GRANTED", "FOLLOWS", "JUMP", "CIRCLE", "NO CONNECTION",
            "KIND MISTAKE", "CANNOT TELL", "CANNOT WORK", "ACTS ON A CIRCLE", "HOLDS", "FAILS",
            "CANNOT BE RUN", "YOU DENY A CAUSE", "Fine.", "no contradiction", "no new contradiction",
            "CONTRADICTION", "DOES NOT STAND", "STANDS"]
# Kinds of addition the plan lists (D2 to D8). Each is a regex on a block's first line.
EXTRA_KINDS = [
    ("D2 world finding", None),  # assigned by position: any finding inside a world section
    ("D3 tie block", r"^\s*Set aside: line \S+ \[[^\]]*\] \(tied by line "),
    ("D3 not-written note", r"^\s*NOTE: leans on lines you did not write"),
    ("D4 described lines", r"^\s*- (?:line \S+ \[[^\]]*\]:|\(no line supports)"),
    ("D4 searched lines", r"^\s*(?:Lines searched|Cause's lines|Reason's lines|Effect's direct lines|Expected's direct lines|Plan line|Claim line):"),
    ("D5 outcomes block", r"^\s*OUTCOMES:|^\s*[a-z' ]+: (?:asked, |not asked, no line of that kind|ran out of time)"),
    ("D2 outside count", r"^\s*\d+ findings? inside '[^']+' would not stand"),
    ("D7 gauge counts", r"^\s*(?:bin sentences|sentences with no line(?: and no bin entry)?|filled in against said|bin entries):"),
    ("D8 claim and deny", r"^YOU CLAIM AND DENY THE SAME CAUSE"),
    ("D6 world verdict", r"^\s*Every line needed is inside the world\.$"),
    ("D2 world no-finding", r"^\s*no contradiction\.$"),
    ("blank", r"^\s*$"),
]

def strip_tokens(line):
    """Remove the tokens D4 adds inside old strings: ' [mark, sentence N]' after a line id, '(line j, sentence N)' in a what-if head."""
    line = re.sub(r"(line \S+) \[[^\]]*\]", r"\1", line)
    line = re.sub(r"(WHAT-IF \[[^\]]*\]) \(line [^)]*\)", r"\1", line)
    return line

def normalise_world_heading(line):
    """D6: the told-world contradiction heading. Both wordings map to one canonical form."""
    m = re.match(r"^(?:INSIDE|UNDER THE SUPPOSITION) '([^']+)'(?: \(a told world, looked at alone\))?: (.*)$", line)
    if not m: return line
    world, rest = m.group(1), m.group(2)
    rest = rest.replace(", which arises only once the supposed lines are added", "").replace(", which the world's own lines give", "")
    return "WORLD '%s': %s" % (world, rest)

def parse(text):
    """Return (findings, extras). A finding is (world, kind, line-or-fact, verdict)."""
    findings, extras = [], []
    world = ""
    lines = text.splitlines()
    i = 0
    current = None
    while i < len(lines):
        raw = lines[i]; line = strip_tokens(raw)
        if line.startswith("REPORT for paragraph") or line.startswith("GAUGE:") and False:
            i += 1; continue
        if line.startswith("GAUGE:"):
            # D7: only the marks part of the gauge is a finding; the rest is text
            world = ""   # the gauge ends any world section
            m = re.match(r"^GAUGE: (\d+) lines said, (\d+) filled in, (\d+) usual case", line)
            findings.append(("", "GAUGE", m.group(0) if m else line[:60], ""))
            i += 1; continue
        if line.startswith("NO FAULT FOUND"):
            # D5 removes this line in the new driver; it is exempt on both sides
            i += 1; continue
        if raw and not raw.startswith(" ") and not re.match(r"^(?:INSIDE|UNDER THE SUPPOSITION) '", raw):
            world = ""  # a non-indented line that is not a world head closes any world section
        wm = re.match(r"^(?:INSIDE|UNDER THE SUPPOSITION) '([^']+)'", line)
        if wm:
            canon = normalise_world_heading(line)
            verdict = next((v for v in VERDICTS if v in canon), "")
            fm = re.search(r"CONTRADICTION about (.+?)(?:, which |\.$|$)", canon)
            if verdict: findings.append((wm.group(1), "WORLD", fm.group(1) if fm else "", verdict))  # the old one-liner, or the D6 contradiction heading, with its fact
            world = wm.group(1)  # D2: the indented lines that follow belong to this world
            i += 1; continue
        if line.startswith("OUTCOMES:") or re.match(r"^\s*OUTCOMES", line):
            extras.append(("D5 outcomes block", line.strip()))
            i += 1
            while i < len(lines) and re.match(r"^\s+\S", lines[i]) and not lines[i].startswith("GAUGE"):
                extras.append(("D5 outcomes block", lines[i].strip())); i += 1
            continue
        matched = False
        for kind, pat, verdict in HEADS:
            m = re.match(pat, line.strip() if world else line)
            if m:
                matched = True
                ident = m.groupdict().get("line") or m.groupdict().get("fact") or m.groupdict().get("q") or ""
                # the verdict is on the head line or the next non-description line
                v = verdict or ""
                j = i + (0 if verdict else 1)
                while not v and j < len(lines):
                    cand = strip_tokens(lines[j]).strip()
                    if (cand.startswith("- ") or cand.startswith("Set aside") or cand.startswith("NOTE:") or cand == ""
                            or cand.startswith("The change made:") or cand.startswith("Claim line:") or cand.startswith("Cause's lines:")
                            or cand.startswith("Effect's direct lines:") or cand.startswith("Reason's lines:") or cand.startswith("Expected's direct lines:")
                            or cand.startswith("Plan line:") or cand.startswith("(no line")):
                        j += 1; continue
                    v = next((x for x in VERDICTS if x in cand), "")
                    if not v: v = "(no verdict word: %s)" % cand[:40]
                if kind == "CHAIN":
                    # chain rows: each row is a finding (line -> verdict)
                    j = i + 1
                    while j < len(lines) and strip_tokens(lines[j]).strip().startswith("line "):
                        row = strip_tokens(lines[j]).strip()
                        rm = re.match(r"^line (\S+):.*->\s+(.*)$", row)
                        if rm: findings.append((world, "CHAIN ROW", rm.group(1), rm.group(2).strip()))
                        j += 1
                    i = j; break
                if kind == "WORLD":
                    i += 1; break
                findings.append((world, kind, ident, v))
                i += 1
                break
        if matched: continue
        # anything else: a description line, a set-aside line, a note, a sentence of report prose
        s = raw.rstrip()
        kind = next((k for k, pat in EXTRA_KINDS if pat and re.match(pat, s)), None)
        if kind and kind != "blank":
            extras.append((kind, s.strip()))
        elif kind == "blank":
            pass
        else:
            extras.append(("D2 world finding" if world else "text", s.strip()))
        i += 1
    return findings, extras

def compare(old_text, new_text):
    of, oe = parse(old_text); nf, ne = parse(new_text)
    old_set, new_set = set(of), set(nf)
    missing = [f for f in of if f not in new_set]
    added = [f for f in nf if f not in old_set]
    # additions of findings are allowed only inside a world (D2) or of kind D8 / GAUGE relabel
    bad_added = [f for f in added if not (f[0] or f[1] in ("CLAIM AND DENY",))]
    old_text_extras = set(e[1] for e in oe if e[0] == "text")
    unlisted = [e for e in ne if e[0] == "text" and e[1] not in old_text_extras]
    # A1 also promises the old line ids and the old text survive: every old extra that
    # must persist has to reappear. D6 replaces the supposition verdict, so it is exempt.
    D6_GONE = ("THE SUPPOSITION UNDOES ITSELF",)
    MUST_KEEP = ("text", "D4 described lines", "D3 not-written note")
    new_extra_set = set(ne)
    dropped = [e for e in oe if e[0] in MUST_KEEP and e not in new_extra_set
               and not any(g in e[1] for g in D6_GONE)]
    unlisted = unlisted + [("dropped from new", e[1]) for e in dropped]
    ok = not missing and not bad_added and not unlisted
    return ok, missing, bad_added, unlisted, (of, nf, ne)

def main():
    if len(sys.argv) == 2:
        f, e = parse(open(sys.argv[1]).read())
        print("FINDINGS:"); [print("  ", x) for x in f]
        print("EXTRAS:"); [print("  ", x) for x in e]
        return 0
    ok, missing, bad_added, unlisted, _ = compare(open(sys.argv[1]).read(), open(sys.argv[2]).read())
    print("A1 %s" % ("HOLDS" if ok else "FAILS"))
    for x in missing: print("  missing from new:", x)
    for x in bad_added: print("  added outside any world (not listed):", x)
    for x in unlisted: print("  unlisted text in new:", x)
    return 0 if ok else 1

if __name__ == "__main__": sys.exit(main())
