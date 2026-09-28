#!/usr/bin/env python3
"""S105 round 3, integration (rule 7 of "S105 Round 3 - how the replies will be read, written before sending.md"):
apply the three areas' permitted text changes to the text under review by program.

Reads  tests/104 The semantics, standing alone, after round 2, with the owner's answers.md  (md5 checked)
and    area 1, 2, 3 - text changes.json  (beside this program; read only).
Writes a NEW file, line for line with the input:
       tests/105 The semantics, standing alone, after round 3.md
It never writes the input or any earlier text. Kinds allowed: delete, formal, pointer (decision S40).
A change is refused when its kind is other; when its old span is missing from its line or occurs there more than
once; when a delete has a nonempty new span; when its line is held for an owner question (HELD_LINES); or when it
overlaps another change on the same line (then neither is applied). Two changes on one line are combined only when
their spans do not overlap. A delete whose span is the whole line leaves an empty line (the line count is kept).
Each applied change is compared with its JSON entry byte for byte, and undoing the applied changes must give the
input line back. Then the scans:
  S95 residue scan (FAMILIES of tests/S95 Scrub - scripts/scrub_apply.py): new hits per line; S23's forbidden list;
  S96 physical scan (PHYS of tests/S96 Repair - scripts/repair_apply.py): new hits per line;
  headings, defined terms (**bold**) and labelled formulas (\\tag) of the input still present, unless deleted on purpose;
  words, and words outside formulas (\\( \\), \\[ \\] stripped), input -> new; the second must not grow.
Run: python3 -B "apply text changes.py"   (standard library only)
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
SRC = SEM + "/tests/104 The semantics, standing alone, after round 2, with the owner's answers.md"
MD5 = "bc14045aae3139df710d8339a9c1c81b"
OUT = SEM + "/tests/105 The semantics, standing alone, after round 3.md"
HERE = os.path.dirname(os.path.abspath(__file__))
AREAS = [(n, os.path.join(HERE, "area %d - text changes.json" % n)) for n in (1, 2, 3)]
KINDS = {"delete", "formal", "pointer"}
# Lines held for an owner question (rule 12): L255, OQ-R3A2-1 (D6.3's quantifier, I136). No change proposes it.
HELD_LINES = {255: "OQ-R3A2-1 (area 2): L255 held until the owner answers"}
S95 = SEM + "/tests/S95 Scrub - scripts/scrub_apply.py"
S96 = SEM + "/tests/S96 Repair - scripts/repair_apply.py"
MATH = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.S)
BOLD = re.compile(r"\*\*(.+?)\*\*")
TAG = re.compile(r"\\tag\{[^}]*\}")
S23 = {"reason to believe/reject", "better/worse than", "not true / more true", "fit", "support", "verify", "corroborate",
       "disprove", "prove/proof", "true/truth", "establish", "authority", "foundation", "derive", "belief"}


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
               "104 The semantics, standing alone, after round 2.md",
               "104 The semantics, standing alone, after round 2, with the owner's answers.md"}
    if os.path.abspath(OUT) == os.path.abspath(SRC) or os.path.basename(OUT) in earlier:
        die("output would overwrite the input or an earlier text")
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("input md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
    old = raw.decode("utf-8").split("\n")
    ch = []
    for n, path in AREAS:
        for e in json.load(open(path, encoding="utf-8")):
            e = dict(e)
            e["area"] = n
            ch.append(e)
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
        if e["line"] in HELD_LINES:
            refused.append((e, "line held: %s" % HELD_LINES[e["line"]]))
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
    # byte-for-byte comparison of every applied change with its JSON entry; undoing gives the input line back
    for ln in sorted(set(e["line"] for e in applied)):
        es = sorted((e for e in applied if e["line"] == ln), key=lambda e: e["span"][0])
        got, back, pos = new[ln - 1], [], 0
        for e in es:
            seg = got[e["out_at"]:e["out_at"] + len(e["new"])]
            if seg.encode("utf-8") != e["new"].encode("utf-8"):
                die("%s: written span differs from its JSON entry" % e["id"])
            e["bytes_equal"] = True
            back.append(got[pos:e["out_at"]])
            back.append(e["old"])
            pos = e["out_at"] + len(e["new"])
        back.append(got[pos:])
        if "".join(back).encode("utf-8") != old[ln - 1].encode("utf-8"):
            die("L%d: undoing the applied changes does not give the input line back" % ln)
    if len(new) != len(old):
        die("line count changed")
    text = "\n".join(new)
    p_old, p_new = len(prose("\n".join(old))), len(prose(text))
    if p_new > p_old:
        die("words outside formulas would grow: %d -> %d" % (p_old, p_new))
    open(OUT, "w", encoding="utf-8").write(text)
    md5n = hashlib.md5(text.encode("utf-8")).hexdigest()

    print("input md5 %s (as required); output %s" % (MD5, os.path.relpath(OUT, SEM)))
    print("changes read: %d (area 1: %d, area 2: %d, area 3: %d)" % (len(ch), *[sum(1 for e in ch if e["area"] == n) for n in (1, 2, 3)]))
    print("applied: %d on %d lines; refused: %d" % (len(applied), len(set(e["line"] for e in applied)), len(refused)))
    for e in sorted(applied, key=lambda e: (e["line"], e["span"][0])):
        print("  APPLIED  L%-4d area %d %-8s %-7s bytes equal %s  prose words %+d  settles: %s" % (
            e["line"], e["area"], e["id"], e["kind"], "yes" if e.get("bytes_equal") else "NO",
            len(prose(e["new"])) - len(prose(e["old"])), "; ".join(e.get("settles") or []) or "-"))
    for e, why in refused:
        print("  REFUSED  L%-4d area %d %s: %s" % (e["line"], e["area"], e["id"], why))
    shared = sorted(ln for ln, es in byline.items() if len(es) > 1)
    print("lines with two or more changes, spans disjoint: %s" % (", ".join("L%d (%d)" % (ln, len(byline[ln])) for ln in shared) or "none"))
    print("held lines: %s" % "; ".join("L%d %s" % kv for kv in HELD_LINES.items()))
    print("lines (newline count) input: %d; new: %d; lines differing: %d; empty lines input %d, new %d" % (
        raw.count(b"\n"), text.count("\n"), sum(1 for a, b in zip(old, new) if a != b),
        sum(1 for l in old if l == ""), sum(1 for l in new if l == "")))
    print("md5 new: %s" % md5n)

    # S95 residue scan: hits per line in the new text beyond those of the same line in the input
    m95 = load(S95, "s95_scrub_apply")
    newhits = []
    for k, (a, b) in enumerate(zip(old, new), 1):
        ca = collections.Counter(x.group(0).lower() for x in m95.BIG.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m95.BIG.finditer(b))
        for w, c in (cb - ca).items():
            newhits.append((k, w, m95.family(w), c))
    tot = lambda ls: sum(1 for l in ls for _ in m95.BIG.finditer(l))
    s23_all = lambda ls: sum(1 for l in ls for x in m95.BIG.finditer(l) if m95.family(x.group(0)) in S23)
    print("S95 residue scan: hits input %d, new %d; new hits: %d; of them in S23's forbidden list: %d; S23-list hits in the whole text: input %d, new %d"
          % (tot(old), tot(new), sum(h[3] for h in newhits), sum(h[3] for h in newhits if h[2] in S23), s23_all(old), s23_all(new)))
    for k, w, lab, c in newhits:
        print("  new  L%d: %s x%d [%s]%s" % (k, w, c, lab, "  FORBIDDEN (S23)" if lab in S23 else ""))

    # S96 physical scan
    m96 = load(S96, "s96_repair_apply")
    ph = []
    for k, (a, b) in enumerate(zip(old, new), 1):
        ca = collections.Counter(x.group(0).lower() for x in m96.PHYS.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m96.PHYS.finditer(b))
        for w, c in (cb - ca).items():
            ph.append((k, w, c))
    tp = lambda ls: sum(1 for l in ls for _ in m96.PHYS.finditer(l))
    print("S96 physical scan: physical-tie words input %d, new %d; new: %d" % (tp(old), tp(new), sum(c for _, _, c in ph)))
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
    print("kept: headings %d, defined terms %d, labelled formulas %d of the input; missing in the new text: %d; deleted on purpose: %d"
          % (nh, nb, nt, len(miss), len(deleted)))
    for k, what, t in miss:
        print("  MISSING L%d %s: %s" % (k, what, t))

    w_old, w_new = len("\n".join(old).split()), len(text.split())
    print("words: input %d, new %d (%+d); words outside formulas: input %d, new %d (%+d)" % (w_old, w_new, w_new - w_old, p_old, p_new, p_new - p_old))
    print("prose check (new outside formulas <= input): %s" % ("yes" if p_new <= p_old else "NO"))


if __name__ == "__main__":
    main()
