"""S98 finishing fixes, part 1: corrections to collectors A to D, from the checks in
build/verification - fidelity.md (section 5) and their sources.

Each fix names the field, the value it expects before and the value after. A field already
holding the value after is left alone, so a rerun changes nothing; any other value stops the
script. Only the named fields of the named records change; every other byte stays.
Usage (from any folder): PYTHONDONTWRITEBYTECODE=1 python3 fix_collectors.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.dirname(os.path.dirname(HERE))
COLLECT = os.path.join(LEDGER, "collect")
ROOT = os.path.dirname(os.path.dirname(LEDGER))
TEXT = {
    "repaired": "tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md",
    "latest": "tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md",
    "scrubbed": "tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md",
}
TXT = {k: open(os.path.join(ROOT, p), encoding="utf-8").read() for k, p in TEXT.items()}

files = {}
recs = {}
for c in "ABCD":
    p = os.path.join(COLLECT, "collector %s.jsonl" % c)
    lines = open(p, encoding="utf-8").read().split("\n")
    assert lines[-1] == ""
    files[c] = [json.loads(l) for l in lines[:-1]]
    for r in files[c]:
        recs[r["rid"]] = r

LOG = []


def setf(rid, field, before, after):
    r = recs[rid]
    if r[field] == after:
        return
    if r[field] != before:
        sys.exit("fix_collectors.py: %s %s is %r, expected %r" % (rid, field, r[field], before))
    r[field] = after
    LOG.append((rid, field))


def expand(spec):
    out = []
    for part in spec.split(", "):
        if "…" in part:
            a, b = [int(x.strip().split("-")[1]) for x in part.split("…")]
            out += ["D-%d" % i for i in range(a, b + 1)]
        else:
            out.append(part.strip())
    return out


# 1. Stage-1 edits of S96 that stage 2 rewrote before the repaired copy (fidelity section 5, item 1).
STAGE1 = "D-301, D-302, D-307, D-309, D-312, D-316, D-322, D-326, D-327, D-328, D-354, D-362, D-365, D-368, D-378".split(", ")
STAGE1_AT = "stage-1 text of S96 (rebuilt in memory, not kept); stage 2 rewrote it before the repaired copy"
for rid in STAGE1:
    if recs[rid]["applied_in"] == "repaired copy":
        assert recs[rid]["new"] not in TXT["repaired"], rid
    setf(rid, "status", "applied", "superseded")
    setf(rid, "applied_in", "repaired copy", STAGE1_AT)

# 2. Recommendations taken in other words (item 2); D-857 is taken in part (item 11).
OTHER_REP = expand("D-718, D-719, D-721…D-725, D-728…D-735, D-737, D-738, D-740, D-741, D-744, D-745, D-747, "
                   "D-748, D-750, D-752…D-756, D-758, D-760, D-771, D-774, D-779, D-782, D-793, D-795, D-797, "
                   "D-800…D-804, D-809, D-813, D-816…D-820, D-822…D-824, D-828…D-830, D-833, D-838, D-847, "
                   "D-848, D-850…D-852, D-854, D-860, D-870…D-872")
OTHER_LAT = expand("D-876, D-883, D-885, D-892, D-916, D-920…D-922, D-924, D-930, D-931, D-935, D-943, D-944, "
                   "D-947, D-949, D-950, D-952")
for rid in OTHER_REP:
    if recs[rid]["applied_in"] == "repaired copy":
        assert recs[rid]["new"] not in TXT["repaired"], rid
    setf(rid, "applied_in", "repaired copy", "repaired copy, in other wording")
for rid in OTHER_LAT:
    if recs[rid]["applied_in"] == "latest text":
        assert recs[rid]["new"] not in TXT["latest"], rid
    setf(rid, "applied_in", "latest text", "latest text, in other wording")
D857_CLAUSE = "of the first kind where the pair is in \\(C\\) and of the second where it is not"
assert D857_CLAUSE in recs["D-857"]["new"] and D857_CLAUSE not in TXT["repaired"]
setf("D-857", "applied_in", "repaired copy",
     "repaired copy, in part and in other wording; not applied: \"%s\"" % D857_CLAUSE)

# 3. Insertions whose `new` was built as the old sentence plus the added sentence (item 3).
for rid in ["B-264", "B-267", "B-276", "B-280", "B-285"]:
    r = recs[rid]
    if r["old"] != "":
        assert r["new"] == r["old"] + " " + r["new_sentence"], rid
        setf(rid, "new", r["new"], r["new_sentence"])
        setf(rid, "old", r["old"], "")
B289_END = "; the commitments of \\(E|W\\) are \\(W\\), and \\((E|W)|W'=E|W'\\) for \\(W'\\subseteq W\\)."
setf("B-289", "new", "with the named background fixed" + B289_END, B289_END)
setf("B-289", "old", "with the named background fixed.", ".")

# 4. `new` built from the word the source offers plus old words (item 4).
setf("C-154", "old", "each component must anchor", "each component")
setf("C-154", "new", "each active component must anchor", "each active component")
setf("C-170", "old", "the exclusion ceases to be established", "the exclusion")
setf("C-170", "new", "the result ceases to be established", "the result")

# 5. C-145: the source's quoted wording has no full stop (item 5).
setf("C-145", "old", "Here selection is blind: its history holds no represented target (Parts 0 and IV).",
     "Here selection is blind: its history holds no represented target (Parts 0 and IV)")
setf("C-145", "new", "Here selection has no represented target in its history (Parts 0 and IV).",
     "Here selection has no represented target in its history (Parts 0 and IV)")

# 6. D-736: `old` with the text's markup, as D-798 has it (item 6).
setf("D-736", "old", "Here a route of the candidate is a member of S", recs["D-798"]["old"])
assert recs["D-736"]["old"] in TXT["scrubbed"]

# 7. Phrases from R2's reason paragraphs left out of the Stage B phrase cells, and C-181's purpose clause (item 8).
DROP = {
    "A-164": ["<u>share a working kind</u>", "<u>an irrelevant alteration elsewhere</u>"],
    "A-177": ["<u>a substantive account of content use</u>"],
    "A-180": ["<u>deliberate first construction</u>"],
    "A-188": ["<u>complete grounding of representation</u>"],
    "A-191": ["<u>genuinely redundant routes</u>"],
    "A-205": ["<u>a useful question</u>"],
    "A-210": ["<u>the normative problem</u>"],
    "A-214": ["<u>explanation-based leak repair</u>"],
}
for rid, drop in DROP.items():
    r = recs[rid]
    pieces = r["new"].split("; ")
    if any(d in pieces for d in drop):
        keep = [x for x in pieces if x not in drop]
        assert len(keep) == len(pieces) - len(drop), rid
        setf(rid, "new", r["new"], "; ".join(keep))
    setf(rid, "source_ref", r["source_ref"],
         r["source_ref"].replace("part of the cell is in R2 reason text", "the cell's phrases from R2 reason text are left out"))
setf("C-181", "new",
     "[no wording given] define (K2)'s Lic_j, Scope_j and Live_j (L390 only), so that Derivation 6 can be followed through receipts to the primitives",
     "[no wording given] define (K2)'s Lic_j, Scope_j and Live_j (L390 only)")

# 8. The same worklist item seen by collectors B and C (item 9): each names the other.
for b, c in [("B-208", "C-200"), ("B-294", "C-203"), ("B-296", "C-204"), ("B-302", "C-207"),
             ("B-303", "C-205"), ("B-306", "C-206")]:
    if c not in recs[b]["same_as"]:
        setf(b, "same_as", recs[b]["same_as"], recs[b]["same_as"] + [c])
    if b not in recs[c]["same_as"]:
        setf(c, "same_as", recs[c]["same_as"], recs[c]["same_as"] + [b])

for c in "ABCD":
    p = os.path.join(COLLECT, "collector %s.jsonl" % c)
    out = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in files[c])
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(out)
print("fix_collectors.py: %d fields changed in %d records" % (len(LOG), len({x[0] for x in LOG})))
