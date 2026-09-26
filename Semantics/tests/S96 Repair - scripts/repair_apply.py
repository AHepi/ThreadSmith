#!/usr/bin/env python3
"""S96 Repair: build the repaired copy of the scrubbed text by program.

Copies the approach of tests/S95 Scrub - scripts/scrub_apply.py. Reads the scrubbed
copy of draft 5 (refuses unless its md5 is 2517ef4ec1f274e8de2bfb7e6661ef94) and
replacements.json beside this script. Each entry names a line, an exact old span on
that line, an exact new span, a group and a reason. Every old span must occur exactly
once in the original line (refuses if missing or ambiguous), and spans on one line
must not overlap. One line of the scrubbed copy gives one line of the repaired copy,
so the two compare line by line. "replace_lines" replaces a whole line (the dated
note, l. 2) and refuses if that line also has an entry.

--scan runs the S95 residue scan (the FAMILIES and scan() of the S95 script,
imported unchanged) over the repaired copy, with the S95 BORDERLINE notes and the
S96 ones in replacements.json, and reports unexplained hits and stale notes.
--physical lists every remaining mention of physic*, admit*, adopt*, carrier*,
instantiat*, possib*/impossib* and task* with the reason it stays, and reports any
line with a mention and no reason.

Stage 2 (after the two checks, results/S96 Check of the repaired copy - *.md): the
stage-1 text above must have md5 c1eecbd1587e5aec91fd0ba7d46e1469 (refuses otherwise);
replacements_stage2.json, made by replacements_stage2_source.py, is then applied to it
by the same rules (spans exact, once on their line, not overlapping, no line added or
removed), and the result is written to OUT. --stage1-only writes the stage-1 text
instead, to reproduce the text the two readers read.

Stage 3 (log S97, after the outside cross-examination was read, results/S96 Reading of
the replies.md, and the owner's words of decision S28): --stage3 rebuilds stages 1 and
2 in memory, refuses unless the stage-2 text has md5 8bb4d19d5aad53de2492b2193fd23ff1
(the S96 final), applies replacements_stage3.json (made by
replacements_stage3_source.py) by the same span rules, and writes the result to OUT3,
a new file. With --stage3 nothing is written to OUT or to any other existing file.
--scan and --physical then run on the stage-3 text, with the notes of all three stages.
"""
import collections, hashlib, importlib.util, json, re, sys

SRC = ("/home/user/ThreadSmith/Semantics/tests/"
       "Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md")
MD5 = "2517ef4ec1f274e8de2bfb7e6661ef94"
REP = "/home/user/ThreadSmith/Semantics/tests/S96 Repair - scripts/replacements.json"
REP2 = "/home/user/ThreadSmith/Semantics/tests/S96 Repair - scripts/replacements_stage2.json"
STAGE1_MD5 = "c1eecbd1587e5aec91fd0ba7d46e1469"
OUT = ("/home/user/ThreadSmith/Semantics/tests/"
       "Revision 2 - scrubbed copy, repaired (S96), theory text.md")
S95_DIR = "/home/user/ThreadSmith/Semantics/tests/S95 Scrub - scripts/"
REP3 = "/home/user/ThreadSmith/Semantics/tests/S96 Repair - scripts/replacements_stage3.json"
STAGE2_MD5 = "8bb4d19d5aad53de2492b2193fd23ff1"
OUT3 = ("/home/user/ThreadSmith/Semantics/tests/"
        "Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md")
PHYS = re.compile(r"\b(physic\w*|admit\w*|adopt\w*|carrier\w*|instantiat\w*|possib\w*|impossib\w*|tasks?)\b", re.I)


def die(msg):
    sys.exit("REFUSED: " + msg)


def apply_spans(lines, entries, label):
    """Apply span entries to lines by the stage rules; return the new lines."""
    by_line = collections.defaultdict(list)
    for i, e in enumerate(entries):
        for k in ("line", "old", "new", "category", "reason"):
            if k not in e:
                die("%s entry %d lacks %r" % (label, i, k))
        by_line[e["line"]].append((i, e))
    out = list(lines)
    for n, es in sorted(by_line.items()):
        if not 1 <= n <= len(lines):
            die("%s entry line %d out of range" % (label, n))
        orig = lines[n - 1]
        spans = []
        for i, e in es:
            c = orig.count(e["old"])
            if c == 0:
                die("%s entry %d, line %d: old span missing: %r" % (label, i, n, e["old"]))
            if c > 1:
                die("%s entry %d, line %d: old span ambiguous (%d times): %r" % (label, i, n, c, e["old"]))
            p = orig.index(e["old"])
            spans.append((p, p + len(e["old"]), e["new"], i))
        spans.sort()
        for a, b in zip(spans, spans[1:]):
            if a[1] > b[0]:
                die("%s line %d: entries %d and %d overlap" % (label, n, a[3], b[3]))
        s = orig
        for p, q, new, i in reversed(spans):
            s = s[:p] + new + s[q:]
        if "\n" in s:
            die("%s line %d: a new span contains a line break" % (label, n))
        out[n - 1] = s
    return out


def stage2(text1):
    if hashlib.md5(text1.encode("utf-8")).hexdigest() != STAGE1_MD5:
        die("stage-1 text md5 is %s, not %s" % (hashlib.md5(text1.encode("utf-8")).hexdigest(), STAGE1_MD5))
    R2 = json.load(open(REP2, encoding="utf-8"))
    out = apply_spans(text1.split("\n"), R2["entries"], "stage 2")
    return R2, "\n".join(out)


def stage3(text2):
    h = hashlib.md5(text2.encode("utf-8")).hexdigest()
    if h != STAGE2_MD5:
        die("stage-2 text md5 is %s, not %s" % (h, STAGE2_MD5))
    R3 = json.load(open(REP3, encoding="utf-8"))
    out = apply_spans(text2.split("\n"), R3["entries"], "stage 3")
    return R3, "\n".join(out)


def build(write=False):
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("scrubbed copy md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
    lines = raw.decode("utf-8").split("\n")
    R = json.load(open(REP, encoding="utf-8"))
    by_line = collections.defaultdict(list)
    for i, e in enumerate(R["entries"]):
        for k in ("line", "old", "new", "category", "reason"):
            if k not in e:
                die("entry %d lacks %r" % (i, k))
        by_line[e["line"]].append((i, e))
    out = list(lines)
    for n, es in sorted(by_line.items()):
        if not 1 <= n <= len(lines):
            die("entry line %d out of range" % n)
        orig = lines[n - 1]
        spans = []
        for i, e in es:
            c = orig.count(e["old"])
            if c == 0:
                die("entry %d, line %d: old span missing: %r" % (i, n, e["old"]))
            if c > 1:
                die("entry %d, line %d: old span ambiguous (%d times): %r" % (i, n, c, e["old"]))
            p = orig.index(e["old"])
            spans.append((p, p + len(e["old"]), e["new"], i))
        spans.sort()
        for a, b in zip(spans, spans[1:]):
            if a[1] > b[0]:
                die("line %d: entries %d and %d overlap" % (n, a[3], b[3]))
        s = orig
        for p, q, new, i in reversed(spans):
            s = s[:p] + new + s[q:]
        if "\n" in s:
            die("line %d: a new span contains a line break" % n)
        out[n - 1] = s
    for key, para in R.get("replace_lines", {}).items():
        n = int(key)
        if n in by_line:
            die("line %d has both an entry and a whole-line replacement" % n)
        if "\n" in para:
            die("replacement for line %d contains a line break" % n)
        out[n - 1] = para
    text = "\n".join(out)
    if write:
        open(OUT, "w", encoding="utf-8").write(text)
    return R, lines, text


def raw_nl():
    return open(SRC, encoding="utf-8").read().count("\n")


def s95_module():
    spec = importlib.util.spec_from_file_location("s95_scrub_apply", S95_DIR + "scrub_apply.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)          # defines FAMILIES, scan(); builds nothing on import
    return m


def run_scan(R, text, R2=None, R3=None):
    m = s95_module()
    s95 = json.load(open(S95_DIR + "replacements.json", encoding="utf-8"))
    notes = list(s95.get("borderline", [])) + list(R.get("borderline", []))
    if R2:
        notes += list(R2.get("borderline", []))
    if R3:
        notes += list(R3.get("borderline", []))
    hits, bl, res = m.scan({"borderline": notes}, text)
    print("residue scan (S95 families) hits:", len(hits), " BORDERLINE (noted):", len(bl),
          " unexplained:", len(res))
    print("borderline by family:", dict(collections.Counter(h[3] for h in bl)))
    for k, n5, w, lab in res:
        print("  UNEXPLAINED l.%d: %s [%s]" % (k, w, lab))
    c = collections.Counter((h[1], h[2].lower()) for h in hits)
    need = collections.Counter()
    for b in notes:
        need[(b["line"], b["word"].lower())] += b.get("count", 1)
    for key, n in sorted(need.items()):
        if c[key] < n:
            print("  STALE borderline note: line %d word %r (noted %d, found %d)" % (key[0], key[1], n, c[key]))
    return hits, bl, res


def run_physical(R, text, R2=None, R3=None):
    reasons = {int(k): v for k, v in R.get("physical_mentions", {}).items()}
    if R2:
        reasons.update({int(k): v for k, v in R2.get("physical_mentions", {}).items()})
    if R3:
        reasons.update({int(k): v for k, v in R3.get("physical_mentions", {}).items()})
    tot = 0
    missing = []
    fam = collections.Counter()
    for k, line in enumerate(text.split("\n"), 1):
        ms = [m.group(0) for m in PHYS.finditer(line)]
        if not ms:
            continue
        tot += len(ms)
        for w in ms:
            fam[w.lower()] += 1
        if k not in reasons:
            missing.append((k, ms))
    print("physical-tie words remaining:", tot, "on", sum(1 for l in text.split("\n") if PHYS.search(l)), "lines")
    print("by word:", dict(fam))
    for k, ms in missing:
        print("  NO REASON l.%d: %s" % (k, ms))
    for k in sorted(reasons):
        if not PHYS.search(text.split("\n")[k - 1]):
            print("  STALE reason for l.%d (no mention left)" % k)
    return tot, missing


def main_stage3():
    R, lines, text1 = build(write=False)
    R2, text2 = stage2(text1)                    # in memory only; OUT is not written
    R3, text3 = stage3(text2)
    open(OUT3, "w", encoding="utf-8").write(text3)
    print("stage 1 md5:", hashlib.md5(text1.encode("utf-8")).hexdigest())
    print("stage 2 md5:", hashlib.md5(text2.encode("utf-8")).hexdigest(), "(S96 final, checked; not written)")
    print("stage 3 entries applied:", len(R3["entries"]), " not applied:", len(R3.get("not_applied", [])))
    print("stage 3 by group:", dict(collections.Counter(e["group"] for e in R3["entries"])))
    print("stage 3 claim changed:", sum(1 for e in R3["entries"] if e.get("claim_changed")))
    print("stage 3 lines changed from stage 2:",
          sum(1 for a, b in zip(text2.split("\n"), text3.split("\n")) if a != b))
    print("lines (wc -l) stage 2:", text2.count("\n"), " stage 3:", text3.count("\n"))
    print("words stage 2:", len(text2.split()), " stage 3:", len(text3.split()))
    print("md5 stage 3 (written to OUT3):", hashlib.md5(text3.encode("utf-8")).hexdigest())
    if "--scan" in sys.argv:
        run_scan(R, text3, R2, R3)
    if "--physical" in sys.argv:
        run_physical(R, text3, R2, R3)


if __name__ == "__main__" and "--stage3" in sys.argv:
    main_stage3()
    sys.exit(0)

if __name__ == "__main__":
    R, lines, text1 = build(write="--stage1-only" in sys.argv)
    words0 = len(open(SRC, encoding="utf-8").read().split())
    print("stage 1 entries applied:", len(R["entries"]), " whole lines replaced:", len(R.get("replace_lines", {})))
    print("stage 1 by group:", dict(collections.Counter(e["group"] for e in R["entries"])))
    print("stage 1 claim changed:", sum(1 for e in R["entries"] if e.get("claim_changed")))
    print("md5 stage 1:", hashlib.md5(text1.encode("utf-8")).hexdigest())
    R2 = None
    text = text1
    if "--stage1-only" not in sys.argv:
        R2, text = stage2(text1)
        open(OUT, "w", encoding="utf-8").write(text)
        print("stage 2 entries applied:", len(R2["entries"]), " not applied:", len(R2.get("not_applied", [])))
        print("stage 2 by source:", dict(collections.Counter(e["group"] for e in R2["entries"])))
        print("stage 2 claim changed:", sum(1 for e in R2["entries"] if e.get("claim_changed")))
        print("stage 2 lines changed from stage 1:",
              sum(1 for a, b in zip(text1.split("\n"), text.split("\n")) if a != b))
    changed = sum(1 for a, b in zip(lines, text.split("\n")) if a != b)
    print("lines (wc -l) scrubbed copy:", raw_nl(), " written:", text.count("\n"), " lines differing from scrubbed copy:", changed)
    print("words scrubbed copy:", words0, " stage 1:", len(text1.split()), " written:", len(text.split()))
    print("md5 written:", hashlib.md5(text.encode("utf-8")).hexdigest())
    if "--scan" in sys.argv:
        run_scan(R, text, R2)
    if "--physical" in sys.argv:
        run_physical(R, text, R2)
