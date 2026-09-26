#!/usr/bin/env python3
"""S95 Scrub: build the scrubbed text of draft 5 by program.

Reads draft 5 (refuses unless its md5 is 7f1d8ad02adf96e27622593bd263252e) and
replacements.json beside this script. Each entry names a draft-5 line, an exact
old span on that line, an exact new span, a category and a reason. Every old span
must occur exactly once in the original line (refuses if missing or ambiguous),
and spans on one line must not overlap. One line of draft 5 gives one line of the
scrubbed text, so the two compare line by line.

Also runs the residue scan over the scrubbed text (--scan) with the register's
word families plus the families the sceptic found missing, and reports every hit
not covered by a BORDERLINE note in replacements.json.
"""
import hashlib, json, re, sys, collections

SRC = "/home/user/ThreadSmith/Semantics/tests/Revision 2 - file 13 draft 5, theory text.md"
MD5 = "7f1d8ad02adf96e27622593bd263252e"
REP = "/home/user/ThreadSmith/Semantics/tests/S95 Scrub - scripts/replacements.json"
OUT = ("/home/user/ThreadSmith/Semantics/tests/"
       "Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md")

# Residue families: the register's (register.py, list F) and the sceptic's missed words.
FAMILIES = [
 ("reason to believe/reject", r"reason to believe|reason to reject"),
 ("better/worse than", r"better than|worse than"),
 ("not true / more true", r"not true|more true"),
 ("rests on", r"rests? on|resting on"),
 ("well-founded", r"well[ -]founded"),
 ("more/less + adjective", r"less elegant|more admitted"),
 ("tells/counts against", r"tells? against|counts? against|counts? for"),
 ("fit", r"fit|fits|fitted|fitting"),
 ("support", r"support\w*"),
 ("verify", r"verif\w*"),
 ("corroborate", r"corroborat\w*"),
 ("disprove", r"disprov\w*|disproof\w*"),
 ("prove/proof", r"prove|proves|proved|proven|proving|provable|proofs?"),
 ("true/truth", r"true|truth\w*|truly|untrue"),
 ("establish", r"establish\w*"),
 ("authority", r"authorit\w*"),
 ("foundation", r"foundation\w*"),
 ("derive", r"deriv\w*"),
 ("belief", r"believ\w*|belief\w*"),
 ("credence/confidence", r"credenc\w*|confiden\w*|credib\w*"),
 ("justify", r"justif\w*"),
 ("warrant/trust/certain/sure/doubt", r"warrant\w*|trust\w*|certain\w*|sure|surely|doubt\w*"),
 ("know/knowledge", r"know|knows|known|knowing|knowledge"),
 ("evidence", r"evidence\w*|evidential\w*"),
 ("confirm/valid", r"confirm\w*|validat\w*|valid|validity|invalid"),
 ("epistemic", r"epistemic\w*"),
 ("expectation", r"expect\w*"),
 ("reliable", r"reliab\w*"),
 ("certify", r"certif\w*"),
 ("false/falsify", r"false\w*|falsi\w*"),
 ("correct", r"correct\w*|incorrect\w*"),
 ("fact", r"facts?|factual"),
 ("real/reality", r"real|reality|realities|really|realism|realist\w*"),
 ("ground/basis", r"ground\w*|basis|basic\w*"),
 ("primitive/axiom", r"primitive\w*|axiom\w*"),
 ("secure/guarantee/sound", r"secur\w*|guarante\w*|sound\w*"),
 ("refute", r"refut\w*"),
 ("theorem/corollary/demonstration", r"theorem\w*|lemma\w*|corollar\w*|demonstrat\w*"),
 ("show", r"show|shows|shown|showing"),
 ("anchor", r"anchor\w*"),
 ("standing", r"standing"),
 ("license", r"licen[cs]\w*|Lic"),
 ("normative", r"normativ\w*"),
 ("obligation", r"obligation\w*"),
 ("settle", r"settle\w*|unsettled"),
 ("genuine/objective/legitimate", r"genuine\w*|objectiv\w*|legitima\w*"),
 ("witness", r"witness\w*"),
 ("right/wrong", r"wrong\w*|right"),
 ("accurate", r"accura\w*"),
 ("better/worse/best", r"better|worse|best|worst|superior\w*|inferior\w*"),
 ("merit/worth/grade/rank/success/adequate/perfection",
  r"merit\w*|worth\w*|grade\w*|rank\w*|good|bad|prefer\w*|success\w*|adequa\w*|perfect\w*"),
 ("progress/advance/elegant/appropriate", r"progress\w*|advanc\w*|elegan\w*|appropriate\w*"),
 ("accept", r"accept\w*"),
 ("adopt", r"adopt\w*"),
 ("hold", r"hold|holds|held"),
 ("logical joint", r"entail\w*|implies|imply|follows|yields?"),
 # families the sceptic found that the register's scan missed
 ("check", r"check\w*"),
 ("verdict", r"verdicts?"),
 ("credit", r"credit\w*"),
 ("load-bearing", r"load-bearing"),
 ("footing", r"footing"),
 ("relies on", r"reli(?:es|ed|ance)|rely"),
 ("reject", r"reject\w*"),
 ("plainly/obviously", r"plain(?:ly)?|obvious\w*"),
 ("permit", r"permi(?:t|ts|tted|ssion|ssible)"),
 ("satisfy", r"satisf\w*"),
 ("understand", r"understand\w*|understood"),
 ("surprise", r"surpris\w*"),
 ("warranted/vindicated", r"vindicat\w*|well-founded"),
]
BIG = re.compile(r"\b(" + "|".join("(?:%s)" % rx for _, rx in FAMILIES) + r")\b", re.I)


def family(w):
    for lab, rx in FAMILIES:
        if re.fullmatch(rx, w, re.I):
            return lab
    return "?"


def die(msg):
    sys.exit("REFUSED: " + msg)


def build():
    raw = open(SRC, "rb").read()
    if hashlib.md5(raw).hexdigest() != MD5:
        die("draft 5 md5 is %s, not %s" % (hashlib.md5(raw).hexdigest(), MD5))
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
    # Added paragraphs (the dated note, the two definitions) go on lines that are
    # blank in draft 5, so no line number moves. CommonMark lets a paragraph sit
    # between two ATX headings without blank lines.
    for key, para in sorted(R.get("fill_blank_lines", {}).items(), key=lambda kv: int(kv[0])):
        n = int(key)
        if lines[n - 1] != "":
            die("line %d of draft 5 is not blank" % n)
        if n in by_line:
            die("line %d has both an entry and an added paragraph" % n)
        if "\n" in para:
            die("added paragraph for line %d contains a line break" % n)
        out[n - 1] = para
    text = "\n".join(out)
    open(OUT, "w", encoding="utf-8").write(text)
    return R, lines, text


def scan(R, text):
    notes = R.get("borderline", [])
    # each borderline note: {"line": n (draft-5 line), "word": w, "reason": "..."}
    covered = collections.Counter()
    for b in notes:
        covered[(b["line"], b["word"].lower())] += b.get("count", 1)
    hits = []
    for k, line in enumerate(text.split("\n"), 1):
        for m in BIG.finditer(line):
            hits.append((k, k, m.group(0), family(m.group(0))))
    used = collections.Counter()
    residue, borderline = [], []
    for k, n5, w, lab in hits:
        key = (n5, w.lower())
        if used[key] < covered[key]:
            used[key] += 1
            borderline.append((k, n5, w, lab))
        else:
            residue.append((k, n5, w, lab))
    return hits, borderline, residue


if __name__ == "__main__":
    R, lines, text = build()
    words5 = len(open(SRC, encoding="utf-8").read().split())
    words = len(text.split())
    print("entries applied:", len(R["entries"]))
    print("categories:", dict(collections.Counter(e["category"] for e in R["entries"])))
    print("lines draft 5:", len(lines), " lines scrubbed:", len(text.split("\n")))
    print("words draft 5:", words5, " words scrubbed:", words)
    print("md5 scrubbed:", hashlib.md5(text.encode("utf-8")).hexdigest())
    if "--scan" in sys.argv:
        hits, bl, res = scan(R, text)
        print("residue scan hits:", len(hits), " BORDERLINE (noted):", len(bl),
              " unexplained:", len(res))
        print("borderline by family:", dict(collections.Counter(h[3] for h in bl)))
        for k, n5, w, lab in res:
            print("  UNEXPLAINED scrubbed l.%d (draft l.%d): %s [%s]" % (k, n5, w, lab))
        stale = []
        c = collections.Counter((h[1], h[2].lower()) for h in hits)
        for b in R.get("borderline", []):
            if c[(b["line"], b["word"].lower())] < b.get("count", 1):
                stale.append(b)
        for b in stale:
            print("  STALE borderline note:", b)
