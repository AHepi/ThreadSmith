#!/usr/bin/env python3
"""S103 Round 1: apply the final FIX and DROP rulings, by program, to a new copy.

Reads the text under review, tests/99 The semantics, standing alone.md, and refuses
unless its md5 is 74f4a4c7619345747f4fa976ddac9548. Applies each final FIX and DROP
ruling of round 1 (the rulings in results/S103 Round 1 - reading/rulings/, after the
critical review, which contested none) by exact span matching:

- each old span must occur exactly once on its line and exactly once in the whole
  text (refuses if missing or ambiguous);
- each old span and each new span must stand byte for byte in its ruling file
  (rule 13 of the reading rule: each applied change is compared with its ruling);
- rulings that touch the same line are combined only when their spans do not
  overlap; overlapping rulings on one sentence are a conflict, and neither is
  applied (reported);
- a DROP removes its span and applies the edits its ruling gives for each
  dependent (none this round: no ruling is DROP);
- one line of file 99 gives one line of the new copy, so the two compare line by
  line; no line is added or removed.

KEEP rulings apply nothing; each KEEP's span is checked to stand once, unchanged, in
both the old and the new text.

Writes tests/103 The semantics, standing alone, after round 1.md, a new file. It
refuses to write over an existing file whose content differs; file 99 is never
written; nothing is written into authority/.

Then scans the new text:
1. the S95 residue scan (the word families of tests/S95 Scrub - scripts/scrub_apply.py,
   imported unchanged): every hit of the new text is compared, line by line, with the
   hits of file 99; a hit the new text has and file 99 does not is a new forbidden
   word. The noted scan (the S95 and S96 BORDERLINE notes, as S96's repair_apply.py
   runs it) is also run on both texts and the unexplained hits compared.
2. the S96 physical scan (PHYS of tests/S96 Repair - scripts/repair_apply.py, imported
   unchanged): the same line-by-line comparison, and the noted run (the S96
   physical_mentions reasons) on both texts, comparing the lines with no reason.
3. structure: every heading, every bold (defined) term, every formula tag \\tag{..}
   and every parenthesised label such as (K), (CT2) of file 99 must still stand in the
   new text, as often as before, unless a DROP removed it.

Nothing is committed.
"""
import collections, hashlib, importlib.util, json, os, re, sys

sys.dont_write_bytecode = True          # importing the S95/S96 scripts writes nothing

ROOT = "/home/user/ThreadSmith/Semantics/"
SRC = ROOT + "tests/99 The semantics, standing alone.md"
MD5 = "74f4a4c7619345747f4fa976ddac9548"
OUT = ROOT + "tests/103 The semantics, standing alone, after round 1.md"
RULINGS = ROOT + "results/S103 Round 1 - reading/rulings/"
S95 = ROOT + "tests/S95 Scrub - scripts/"
S96 = ROOT + "tests/S96 Repair - scripts/"

# ---------------------------------------------------------------------------
# The final rulings of round 1 that change the text (FIX) or remove from it (DROP).
# Old and new are the rulings' own wordings, byte for byte.
FIXES = [
    {"id": "C07", "line": 123,
     "old": "- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;",
     "new": "- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;"},
    {"id": "C27", "line": 443,
     "old": "An explanatory aim requires an account, or the correction of a use through one, to be deployable.",
     "new": "An explanatory aim requires a deployable account, or the correction of a use through one."},
    {"id": "C28", "line": 471,
     "old": r"\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)",
     "new": r"\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)"},
    {"id": "C29", "line": 520,
     "old": "Account, from fidelity under change (E).",
     "new": "Account, from fidelity under change, non-circular dependence and non-vacuity (E)."},
]
# A DROP would be {"id", "line", "old", "dependents": [{"line", "old", "new", "why"}]}.
DROPS = []

# The KEEP rulings: nothing is applied; each span is checked to stand unchanged.
KEEPS = [
    ("C01", 27, "It defines the classes."),
    ("C02", 41, "Survival is how the transport got there; fidelity is what it is."),
    ("C03", 47, "Construction is a separate provenance with a separate trace, and every creative attribution requires it."),
    ("C04", 113, r"Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III)."),
    ("C05", 113, r"The **signature** of component \(j\) on \(C\) is"),
    ("C06", 115, "\\[\n\\operatorname{sig}_C(j)=\\{(a,b,L_j(a,b)):(a,b)\\in C\\}. \\tag{K}\n\\]"),
    ("C08", 124, "- a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;"),
    ("C09", 125, "- a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule."),
    ("C10", 127, "These are descriptions of patterns in (K), not additional data."),
    ("C11", 127, 'The semantics never asks whether a component "is" a cause.'),
    ("C12", 127, "It asks what its signature is."),
    ("C13", 161, "A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements."),
    ("C14", 161, "Its formulation is still an event."),
    ("C15", 161, "Exposing the defect is another question with its own contract."),
    ("C16", 217, "For an edit\u2013boundary pair \\((a,b)\\in C\\) actually occurring:"),
    ("C17", 219, r"- the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);"),
    ("C18", 220, r"- a **violation** occurs when fidelity fails at \((a,b)\);"),
    ("C19", 225, "Two responses to a violation are distinguished."),
    ("C20", 225, "Only the second can be originative under Part X."),
    ("C21", 273, r'"\(p\) because \(p\)" fails non-circular dependence.'),
    ("C22", 311, "(B) records the collective contribution."),
    ("C23", 375, "An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts."),
    ("C24", 383, "A criticism occurrence can exist when (K1) fails."),
    ("C25", 385, "**Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route."),
    ("C26", 393, "Withdrawing a premise makes the step unusable; it does not rule the conclusion out."),
]


def die(msg):
    sys.exit("REFUSED: " + msg)


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)          # both scripts build nothing on import
    return m


# ---------------------------------------------------------------------------
def check_against_ruling(r):
    """Old and new must stand byte for byte in the ruling file."""
    path = RULINGS + "ruling %s.md" % r["id"]
    if not os.path.exists(path):
        die("%s: ruling file missing: %s" % (r["id"], path))
    t = open(path, encoding="utf-8").read()
    for k in ("old", "new"):
        if r[k] and r[k] not in t:
            die("%s: the %s wording does not stand byte for byte in %s" % (r["id"], k, path))
    return path


def locate(lines, text, r, label):
    n = r["line"]
    if not 1 <= n <= len(lines):
        die("%s %s: line %d out of range" % (label, r["id"], n))
    c_line = lines[n - 1].count(r["old"])
    c_all = text.count(r["old"])
    if c_line == 0:
        die("%s %s, line %d: old span missing: %r" % (label, r["id"], n, r["old"]))
    if c_line > 1 or c_all > 1:
        die("%s %s, line %d: old span ambiguous (%d on the line, %d in the text): %r"
            % (label, r["id"], n, c_line, c_all, r["old"]))
    p = lines[n - 1].index(r["old"])
    return (n, p, p + len(r["old"]))


def apply(lines, text):
    edits = []                           # (line, start, end, new, ruling id, kind)
    for r in FIXES:
        check_against_ruling(r)
        n, p, q = locate(lines, text, r, "FIX")
        if "\n" in r["new"]:
            die("FIX %s: the new span contains a line break" % r["id"])
        edits.append((n, p, q, r["new"], r["id"], "FIX"))
    for r in DROPS:
        check_against_ruling(r)
        n, p, q = locate(lines, text, r, "DROP")
        edits.append((n, p, q, "", r["id"], "DROP"))
        if "dependents" not in r:
            die("DROP %s: its ruling's handling of the dependents is not given" % r["id"])
        for d in r["dependents"]:
            dd = dict(d, id=r["id"] + " dependent")
            dn, dp, dq = locate(lines, text, dd, "DROP dependent")
            edits.append((dn, dp, dq, d["new"], r["id"] + " (dependent)", "DROP-dependent"))
    by_line = collections.defaultdict(list)
    for e in edits:
        by_line[e[0]].append(e)
    applied, not_applied = [], []
    conflicted = set()
    for n, es in by_line.items():
        es.sort(key=lambda e: e[1])
        for a, b in zip(es, es[1:]):
            if a[2] > b[1]:              # overlapping spans on one sentence: a conflict
                conflicted.add(a[4]); conflicted.add(b[4])
    out = list(lines)
    for n, es in sorted(by_line.items()):
        keep = [e for e in es if e[4] not in conflicted]
        s = lines[n - 1]
        for (_, p, q, new, rid, kind) in sorted(keep, key=lambda e: e[1], reverse=True):
            s = s[:p] + new + s[q:]
            applied.append((rid, kind, n))
        for e in es:
            if e[4] in conflicted:
                not_applied.append((e[4], e[5], n, "conflicts with another ruling on the same sentence"))
        out[n - 1] = s
    return out, sorted(applied), sorted(not_applied)


# ---------------------------------------------------------------------------
def hit_counter(regex, text):
    c = collections.Counter()
    for k, line in enumerate(text.split("\n"), 1):
        for m in regex.finditer(line):
            c[(k, m.group(0).lower())] += 1
    return c


def s95_scan(old, new):
    m = load_module("s95_scrub_apply", S95 + "scrub_apply.py")
    co, cn = hit_counter(m.BIG, old), hit_counter(m.BIG, new)
    added = cn - co
    removed = co - cn
    notes = list(json.load(open(S95 + "replacements.json", encoding="utf-8")).get("borderline", []))
    for f in ("replacements.json", "replacements_stage2.json", "replacements_stage3.json"):
        notes += list(json.load(open(S96 + f, encoding="utf-8")).get("borderline", []))
    _, blo, reso = m.scan({"borderline": notes}, old)
    _, bln, resn = m.scan({"borderline": notes}, new)
    ro = collections.Counter((k, w.lower()) for k, _, w, _ in reso)
    rn = collections.Counter((k, w.lower()) for k, _, w, _ in resn)
    return {"hits_old": sum(co.values()), "hits_new": sum(cn.values()),
            "added": sorted(added.elements()), "removed": sorted(removed.elements()),
            "unexplained_old": sum(ro.values()), "unexplained_new": sum(rn.values()),
            "unexplained_added": sorted((rn - ro).elements()),
            "family": {w: m.family(w) for (_, w) in list(added) + list(removed)}}


def s96_physical(old, new):
    m = load_module("s96_repair_apply", S96 + "repair_apply.py")
    co, cn = hit_counter(m.PHYS, old), hit_counter(m.PHYS, new)
    reasons = {}
    for f in ("replacements.json", "replacements_stage2.json", "replacements_stage3.json"):
        reasons.update({int(k): v for k, v in
                        json.load(open(S96 + f, encoding="utf-8")).get("physical_mentions", {}).items()})
    def no_reason(t):
        return sorted(k for k, line in enumerate(t.split("\n"), 1)
                      if m.PHYS.search(line) and k not in reasons)
    nro, nrn = no_reason(old), no_reason(new)
    return {"hits_old": sum(co.values()), "hits_new": sum(cn.values()),
            "added": sorted((cn - co).elements()), "removed": sorted((co - cn).elements()),
            "no_reason_old": nro, "no_reason_new": nrn,
            "no_reason_added": sorted(set(nrn) - set(nro))}


HEAD = re.compile(r"^#{1,6} .*$", re.M)
BOLD = re.compile(r"\*\*([^*\n]+?)\*\*")
TAG = re.compile(r"\\tag\{([^}]*)\}")
# a label such as (K), (F1), (CT2), (EX): not LaTeX's \( and not a function's argument, F(C)
LABEL = re.compile(r"(?<![\\A-Za-z0-9_}])\(([A-Z][A-Za-z]{0,3}[0-9]{0,2})\)")


def structure(old, new, dropped_spans):
    rep = {}
    for name, rx in (("headings", HEAD), ("bold terms", BOLD), ("formula tags", TAG), ("labels", LABEL)):
        co = collections.Counter(m.group(0) if name == "headings" else m.group(1) for m in rx.finditer(old))
        cn = collections.Counter(m.group(0) if name == "headings" else m.group(1) for m in rx.finditer(new))
        lost = {k: (co[k], cn[k]) for k in co if cn[k] < co[k]}
        excused = {k: v for k, v in lost.items() if any(k in s for s in dropped_spans)}
        rep[name] = {"old": sum(co.values()), "distinct_old": len(co), "new": sum(cn.values()),
                     "distinct_new": len(cn),
                     "lost": {k: v for k, v in lost.items() if k not in excused},
                     "lost_by_drop": excused,
                     "gained": {k: (co[k], cn[k]) for k in cn if cn[k] > co[k]}}
    return rep


# ---------------------------------------------------------------------------
def main():
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("file 99 md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
    old = raw.decode("utf-8")
    lines = old.split("\n")

    keep_not_verbatim = []
    for rid, n, span in KEEPS:
        c = old.count(span)
        if c != 1 or span.split("\n")[0] not in lines[n - 1]:
            die("KEEP %s: span not found once on line %d (found %d in the text)" % (rid, n, c))
        # a KEEP applies nothing; whether its ruling quotes the span verbatim is only reported
        if span not in open(RULINGS + "ruling %s.md" % rid, encoding="utf-8").read():
            keep_not_verbatim.append(rid)

    out, applied, not_applied = apply(lines, old)
    new = "\n".join(out)

    # one line to one line; only the lines of applied rulings differ
    if len(out) != len(lines):
        die("line count changed: %d -> %d" % (len(lines), len(out)))
    touched = {n for _, _, n in applied}
    diff = [k for k, (a, b) in enumerate(zip(lines, out), 1) if a != b]
    if set(diff) != touched:
        die("lines differing %s are not the lines ruled %s" % (diff, sorted(touched)))
    # each changed line is the old line with exactly its ruling's span replaced
    for r in FIXES:
        if (r["id"], "FIX", r["line"]) in applied:
            a, b = lines[r["line"] - 1], out[r["line"] - 1]
            if a.replace(r["old"], r["new"]) != b or b.count(r["new"]) != 1 or new.count(r["new"]) != 1:
                die("%s: the changed line does not match its ruling byte for byte" % r["id"])
    for rid, n, span in KEEPS:
        if new.count(span) != 1:
            die("KEEP %s: span no longer stands once in the new text" % rid)

    if os.path.exists(OUT):
        if open(OUT, encoding="utf-8").read() != new:
            die("%s exists and differs; not written over" % OUT)
        wrote = "already present, identical"
    else:
        open(OUT, "w", encoding="utf-8").write(new)
        wrote = "written"
    if hashlib.md5(open(SRC, "rb").read()).hexdigest() != MD5:
        die("file 99 changed while running")

    moves = sum(1 for _, k, _ in applied if k in ("FIX", "DROP"))
    print("input md5:", MD5, "(checked)")
    print("rulings: FIX %d, DROP %d, KEEP %d" % (len(FIXES), len(DROPS), len(KEEPS)))
    print("KEEP spans each found once on their line, and once, unchanged, in the new copy;"
          " rulings that do not quote the span verbatim (markup set aside there):",
          keep_not_verbatim or "none")
    per_line = collections.Counter(r["line"] for r in FIXES + DROPS)
    shared = sorted(n for n, c in per_line.items() if c > 1)
    print("lines touched by more than one FIX or DROP (combined only if the spans do not overlap):",
          shared or "none")
    for rid, kind, n in applied:
        print("  applied %s %s at line %d" % (kind, rid, n))
    for rid, kind, n, why in not_applied:
        print("  NOT applied %s %s at line %d: %s" % (kind, rid, n, why))
    print("moves (FIX + DROP applied):", moves)
    print("lines old/new:", len(lines), len(out), " lines differing:", diff)
    print("words old/new (split):", len(old.split()), len(new.split()))
    print("output:", OUT, "-", wrote)
    print("output md5:", md5(new))

    s = s95_scan(old, new)
    print("\nS95 residue scan (word families of scrub_apply.py):")
    print("  hits file 99: %d, new copy: %d" % (s["hits_old"], s["hits_new"]))
    print("  hits the new copy has and file 99 does not (new forbidden words):", s["added"] or "none")
    print("  hits removed:", [(k, w, s["family"][w]) for k, w in s["removed"]] or "none")
    print("  noted scan, unexplained: file 99 %d, new copy %d; added: %s"
          % (s["unexplained_old"], s["unexplained_new"], s["unexplained_added"] or "none"))

    p = s96_physical(old, new)
    print("\nS96 physical scan (PHYS of repair_apply.py):")
    print("  mentions file 99: %d, new copy: %d" % (p["hits_old"], p["hits_new"]))
    print("  mentions added:", p["added"] or "none", " removed:", p["removed"] or "none")
    print("  lines with a mention and no S96 reason: file 99 %d, new copy %d; added: %s"
          % (len(p["no_reason_old"]), len(p["no_reason_new"]), p["no_reason_added"] or "none"))

    dropped = [r["old"] for r in DROPS if (r["id"], "DROP", r["line"]) in applied]
    st = structure(old, new, dropped)
    print("\nStructure (every heading, bold term, formula tag and label of file 99 still present):")
    ok = True
    for name, v in st.items():
        print("  %s: file 99 %d (%d distinct), new copy %d (%d distinct); lost: %s; lost by a DROP: %s; gained: %s"
              % (name, v["old"], v["distinct_old"], v["new"], v["distinct_new"],
                 v["lost"] or "none", v["lost_by_drop"] or "none", v["gained"] or "none"))
        ok = ok and not v["lost"]

    fail = []
    if s["added"]:
        fail.append("S95 scan: new forbidden word")
    if s["unexplained_added"]:
        fail.append("S95 noted scan: new unexplained hit")
    if p["added"] or p["no_reason_added"]:
        fail.append("S96 physical scan: new mention")
    if not ok:
        fail.append("structure: something lost")
    print("\nRESULT:", "all scans pass" if not fail else "FAILED: " + "; ".join(fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
