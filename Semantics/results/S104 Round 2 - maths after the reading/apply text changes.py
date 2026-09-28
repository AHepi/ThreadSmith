#!/usr/bin/env python3
"""S104 round 2, integration: apply the three areas' text changes to tests/103 by program.

Writes tests/104 (line for line with 103). Kinds allowed: delete, formal, pointer (decision S40).
A change is refused when its kind is other, its old span is missing from its line or occurs there
more than once, or it overlaps another change on the same line (then neither is applied).
A change an area marked as waiting on an owner question is held (JSON key in HOLD_KEYS, or listed in HELD).
Each applied change is compared with its JSON entry byte for byte. Then the scans:
  S95 residue scan (FAMILIES of tests/S95 Scrub - scripts/scrub_apply.py): new hits per line, 103 -> 104;
  S96 physical scan (PHYS of tests/S96 Repair - scripts/repair_apply.py): new hits per line;
  headings, defined terms (**bold**) and labelled formulas (\\tag) of 103 still present in 104;
  words, and words outside formulas (\\( \\), \\[ \\] stripped), 103 -> 104.
Run: python3 -B "apply text changes.py"   (standard library only; writes only tests/104)
"""
import collections
import hashlib
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True
SEM = "/home/user/ThreadSmith/Semantics"
SRC = SEM + "/tests/103 The semantics, standing alone, after round 1.md"
MD5 = "f31ebb1f050783f1a84f6136cec20fcd"
OUT = SEM + "/tests/104 The semantics, standing alone, after round 2.md"
HERE = os.path.dirname(os.path.abspath(__file__))
AREAS = [(n, os.path.join(HERE, "area %d - text changes.json" % n)) for n in (1, 2, 3)]
KINDS = {"delete", "formal", "pointer"}
HOLD_KEYS = ("waiting", "owner_question", "held", "blocked_by", "hold")
# Marked waiting in the area files with no JSON entry (nothing to apply): area 3, E03 / D18.1 / OQ1,
# "the cut is OQ1 (A3-02); no text change until chosen" (L405 'represented organization', L526 'no cycle').
HELD = []
S95 = SEM + "/tests/S95 Scrub - scripts/scrub_apply.py"
S96 = SEM + "/tests/S96 Repair - scripts/repair_apply.py"
MATH = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.S)
BOLD = re.compile(r"\*\*(.+?)\*\*")
TAG = re.compile(r"\\tag\{[^}]*\}")


def die(msg):
    sys.exit("REFUSED: " + msg)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)  # constants and functions only; both files build nothing on import
    return m


def prose(s):
    return MATH.sub(" ", s).split()


def main():
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("tests/103 md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
    old = raw.decode("utf-8").split("\n")
    ch, seen = [], collections.Counter()
    for n, p in AREAS:
        for e in json.load(open(p, encoding="utf-8")):
            e = dict(e)
            e["area"] = n
            if "id" not in e:  # area 3's entries carry no id: A3-L<line>, with .1, .2 where a line has two
                seen[(n, e["line"])] += 1
                e["id"] = "A%d-L%d.%d" % (n, e["line"], seen[(n, e["line"])])
            ch.append(e)
    refused, held, ok = [], [], []
    for e in ch:
        if any(e.get(k) for k in HOLD_KEYS) or e["id"] in HELD:
            held.append((e, "marked waiting on an owner question"))
            continue
        if e.get("kind") not in KINDS:
            refused.append((e, "kind %r not delete/formal/pointer" % e.get("kind")))
            continue
        if not (1 <= e["line"] <= len(old)):
            refused.append((e, "no line %d" % e["line"]))
            continue
        k = len(re.findall("(?=%s)" % re.escape(e["old"]), old[e["line"] - 1])) if e["old"] else 0  # overlapping occurrences counted
        if k != 1:
            refused.append((e, "old span occurs %d times in L%d" % (k, e["line"])))
            continue
        if e["kind"] == "delete" and e.get("new", "") != "":
            refused.append((e, "delete with a nonempty new span"))
            continue
        s = old[e["line"] - 1].index(e["old"])
        e["span"] = (s, s + len(e["old"]))
        ok.append(e)
    byline = collections.defaultdict(list)
    for e in ok:
        byline[e["line"]].append(e)
    applied = []
    for ln, es in byline.items():
        bad = set()
        for i in range(len(es)):
            for j in range(i + 1, len(es)):
                a, b = es[i]["span"], es[j]["span"]
                if a[0] < b[1] and b[0] < a[1]:
                    bad |= {i, j}
        for i in sorted(bad):
            refused.append((es[i], "overlaps another change on L%d; neither applied" % ln))
        applied += [e for i, e in enumerate(es) if i not in bad]
    new = list(old)
    for ln in sorted(set(e["line"] for e in applied)):
        es = sorted((e for e in applied if e["line"] == ln), key=lambda e: e["span"][0])
        line, out, pos = old[ln - 1], [], 0
        for e in es:
            out.append(line[pos:e["span"][0]])
            e["out_at"] = sum(len(x) for x in out)
            out.append(e["new"])
            pos = e["span"][1]
        out.append(line[pos:])
        new[ln - 1] = "".join(out)
    # byte-for-byte comparison of every applied change with its JSON entry
    for ln in sorted(set(e["line"] for e in applied)):
        es = sorted((e for e in applied if e["line"] == ln), key=lambda e: e["span"][0])
        got, back, pos = new[ln - 1], [], 0
        for e in es:
            seg = got[e["out_at"]:e["out_at"] + len(e["new"])]
            if seg.encode("utf-8") != e["new"].encode("utf-8"):
                die("%s: written span differs from its JSON entry" % e["id"])
            back.append(got[pos:e["out_at"]])
            back.append(e["old"])
            pos = e["out_at"] + len(e["new"])
        back.append(got[pos:])
        if "".join(back).encode("utf-8") != old[ln - 1].encode("utf-8"):
            die("L%d: undoing the applied changes does not give 103's line back" % ln)
    if len(new) != len(old):
        die("line count changed")
    text = "\n".join(new)
    open(OUT, "w", encoding="utf-8").write(text)
    md5n = hashlib.md5(text.encode("utf-8")).hexdigest()

    print("input md5 %s (as required); output %s" % (MD5, os.path.relpath(OUT, SEM)))
    print("changes read: %d (area 1: %d, area 2: %d, area 3: %d)" % (len(ch), *[sum(1 for e in ch if e["area"] == n) for n in (1, 2, 3)]))
    print("applied: %d on %d lines; refused: %d; held: %d" % (len(applied), len(set(e["line"] for e in applied)), len(refused), len(held)))
    for e in sorted(applied, key=lambda e: (e["line"], e["span"][0])):
        print("  APPLIED  L%-4d area %d %-6s %-7s prose words %+d" % (e["line"], e["area"], e["id"], e["kind"], len(prose(e["new"])) - len(prose(e["old"]))))
    for e, why in refused:
        print("  REFUSED  L%-4d area %d %s: %s" % (e["line"], e["area"], e["id"], why))
    for e, why in held:
        print("  HELD     L%-4d area %d %s: %s" % (e["line"], e["area"], e["id"], why))
    print("  held with no JSON entry: area 3 OQ1 (E03, D18.1): the cut of 'represented' at L405 and L526's 'no cycle'; not written")
    print("lines (newline count) 103: %d; 104: %d; lines differing: %d" % (raw.count(b"\n"), text.count("\n"), sum(1 for a, b in zip(old, new) if a != b)))
    print("md5 104: %s" % md5n)

    # S95 residue scan: hits per line in 104 beyond those of the same line in 103
    m95 = load(S95, "s95_scrub_apply")
    s23 = {"reason to believe/reject", "better/worse than", "not true / more true", "fit", "support", "verify", "corroborate",
           "disprove", "prove/proof", "true/truth", "establish", "authority", "foundation", "derive", "belief"}
    newhits = []
    for k, (a, b) in enumerate(zip(old, new), 1):
        ca = collections.Counter(x.group(0).lower() for x in m95.BIG.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m95.BIG.finditer(b))
        for w, c in (cb - ca).items():
            newhits.append((k, w, m95.family(w), c))
    tot = lambda ls: sum(1 for l in ls for _ in m95.BIG.finditer(l))
    print("S95 residue scan: hits 103 %d, 104 %d; new hits in 104: %d; of them in S23's forbidden list: %d"
          % (tot(old), tot(new), sum(h[3] for h in newhits), sum(h[3] for h in newhits if h[2] in s23)))
    for k, w, lab, c in newhits:
        print("  new  L%d: %s x%d [%s]%s" % (k, w, c, lab, "  FORBIDDEN (S23)" if lab in s23 else ""))

    # S96 physical scan
    m96 = load(S96, "s96_repair_apply")
    ph = []
    for k, (a, b) in enumerate(zip(old, new), 1):
        ca = collections.Counter(x.group(0).lower() for x in m96.PHYS.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m96.PHYS.finditer(b))
        for w, c in (cb - ca).items():
            ph.append((k, w, c))
    tp = lambda ls: sum(1 for l in ls for _ in m96.PHYS.finditer(l))
    print("S96 physical scan: physical-tie words 103 %d, 104 %d; new in 104: %d" % (tp(old), tp(new), sum(c for _, _, c in ph)))
    for k, w, c in ph:
        print("  new  L%d: %s x%d" % (k, w, c))

    # headings, defined terms, labelled formulas
    deleted = {(e["line"], m.group(1)) for e in applied if e["kind"] == "delete" for m in BOLD.finditer(e["old"])}
    miss = []
    for k, (a, b) in enumerate(zip(old, new), 1):
        if a.startswith("#") and a != b:
            miss.append((k, "heading", a))
        for t, c in (collections.Counter(m.group(1) for m in BOLD.finditer(a)) - collections.Counter(m.group(1) for m in BOLD.finditer(b))).items():
            if (k, t) not in deleted:
                miss.append((k, "defined term", t))
        for t in (collections.Counter(TAG.findall(a)) - collections.Counter(TAG.findall(b))):
            miss.append((k, "labelled formula", t))
    nh = sum(1 for l in old if l.startswith("#"))
    nb = sum(len(BOLD.findall(l)) for l in old)
    nt = sum(len(TAG.findall(l)) for l in old)
    print("kept: headings %d, defined terms %d, labelled formulas %d of 103; missing in 104: %d" % (nh, nb, nt, len(miss)))
    for k, what, t in miss:
        print("  MISSING L%d %s: %s" % (k, what, t))

    w_old, w_new = len("\n".join(old).split()), len(text.split())
    p_old, p_new = len(prose("\n".join(old))), len(prose(text))
    print("words: 103 %d, 104 %d (%+d); words outside formulas: 103 %d, 104 %d (%+d)" % (w_old, w_new, w_new - w_old, p_old, p_new, p_new - p_old))
    print("prose check (104 outside formulas <= 103): %s" % ("yes" if p_new <= p_old else "NO"))


if __name__ == "__main__":
    main()
