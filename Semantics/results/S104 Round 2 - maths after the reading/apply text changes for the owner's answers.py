#!/usr/bin/env python3
"""S104 round 2, the owner's answers (decision S41): apply "text changes for the owner's answers.json" to
tests/104 by program. A companion of "apply text changes.py" (which builds tests/104 from tests/103 and is
left as it is); the same checks, on a new input and a new output.

Reads tests/104 (md5 checked) and writes a NEW file, line for line with 104:
  tests/104 The semantics, standing alone, after round 2, with the owner's answers.md
It never writes tests/104 or any earlier text. Kinds allowed: delete, formal, pointer (decision S40).
A change is refused when its kind is other, its old span is missing from its line or occurs there more
than once, or it overlaps another change on the same line (then neither is applied). Each applied change
is compared with its JSON entry byte for byte, and undoing the applied changes must give 104's line back.
Then the scans:
  S95 residue scan (FAMILIES of tests/S95 Scrub - scripts/scrub_apply.py): new hits per line, 104 -> new;
  S96 physical scan (PHYS of tests/S96 Repair - scripts/repair_apply.py): new hits per line;
  headings, defined terms (**bold**) and labelled formulas (\\tag) of 104 still present;
  words, and words outside formulas (\\( \\), \\[ \\] stripped), 104 -> new; the second must not grow.
Run: python3 -B "apply text changes for the owner's answers.py"   (standard library only)
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
SRC = SEM + "/tests/104 The semantics, standing alone, after round 2.md"
MD5 = "735ec1e8256cc6a251715a031944ea65"
OUT = SEM + "/tests/104 The semantics, standing alone, after round 2, with the owner's answers.md"
HERE = os.path.dirname(os.path.abspath(__file__))
CHANGES = os.path.join(HERE, "text changes for the owner's answers.json")
KINDS = {"delete", "formal", "pointer"}
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
    earlier = {"99 The semantics, standing alone.md", "103 The semantics, standing alone, after round 1.md",
               "104 The semantics, standing alone, after round 2.md"}
    if os.path.abspath(OUT) == os.path.abspath(SRC) or os.path.basename(OUT) in earlier:
        die("output would overwrite tests/104 or an earlier text")
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("tests/104 md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
    old = raw.decode("utf-8").split("\n")
    ch = [dict(e) for e in json.load(open(CHANGES, encoding="utf-8"))]
    ids = collections.Counter(e["id"] for e in ch)
    if any(v > 1 for v in ids.values()):
        die("duplicate ids: %s" % [k for k, v in ids.items() if v > 1])
    refused, ok = [], []
    for e in ch:
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
            die("L%d: undoing the applied changes does not give 104's line back" % ln)
    if len(new) != len(old):
        die("line count changed")
    text = "\n".join(new)
    p_old, p_new = len(prose("\n".join(old))), len(prose(text))
    if p_new > p_old:
        die("words outside formulas would grow: %d -> %d" % (p_old, p_new))
    open(OUT, "w", encoding="utf-8").write(text)
    md5n = hashlib.md5(text.encode("utf-8")).hexdigest()

    print("input md5 %s (as required); output %s" % (MD5, os.path.relpath(OUT, SEM)))
    print("changes read: %d from %s" % (len(ch), os.path.basename(CHANGES)))
    print("applied: %d on %d lines; refused: %d" % (len(applied), len(set(e["line"] for e in applied)), len(refused)))
    for e in sorted(applied, key=lambda e: (e["line"], e["span"][0])):
        print("  APPLIED  L%-4d %-9s answers %-4s %-7s prose words %+d" % (e["line"], e["id"], e["answers"], e["kind"], len(prose(e["new"])) - len(prose(e["old"]))))
    for e, why in refused:
        print("  REFUSED  L%-4d %s: %s" % (e["line"], e["id"], why))
    print("lines (newline count) 104: %d; new: %d; lines differing: %d" % (raw.count(b"\n"), text.count("\n"), sum(1 for a, b in zip(old, new) if a != b)))
    print("md5 new: %s" % md5n)

    # S95 residue scan: hits per line in the new text beyond those of the same line in 104
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
    print("S95 residue scan: hits 104 %d, new %d; new hits: %d; of them in S23's forbidden list: %d"
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
    print("S96 physical scan: physical-tie words 104 %d, new %d; new: %d" % (tp(old), tp(new), sum(c for _, _, c in ph)))
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
    print("kept: headings %d, defined terms %d, labelled formulas %d of 104; missing in the new text: %d" % (nh, nb, nt, len(miss)))
    for k, what, t in miss:
        print("  MISSING L%d %s: %s" % (k, what, t))

    w_old, w_new = len("\n".join(old).split()), len(text.split())
    print("words: 104 %d, new %d (%+d); words outside formulas: 104 %d, new %d (%+d)" % (w_old, w_new, w_new - w_old, p_old, p_new, p_new - p_old))
    print("prose check (new outside formulas <= 104): %s" % ("yes" if p_new <= p_old else "NO"))


if __name__ == "__main__":
    main()
