"""S98 finishing fixes, part 2: collect/collector F.jsonl, the records the completeness check
(build/verification - completeness.md, section 1) found missing, taken from their sources.

Every `new` with wording and every `old` is checked verbatim against its source or its target
text; target_part is read from the target text's headings; status and applied_in for wording
are set by searching the texts in order. Usage: PYTHONDONTWRITEBYTECODE=1 python3 build_F.py
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(os.path.dirname(LEDGER))
COLLECT = os.path.join(LEDGER, "collect")

F00 = "authority/00 FW5 JUMP from FW2+FW3+FW4 - Explanatory construction (predecessor, 8 September 2026).md"
F10 = "authority/10 Claude Fable Semantics - standalone theory.md"
F11 = "authority/11 Claude Fable Semantics - standalone theory, revision 1.md"
F11_LABEL = "file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md)"
D5 = "tests/Revision 2 - file 13 draft 5, theory text.md"
VERS = [  # the texts after file 11, in order, with the labels collector C uses
    ("tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md", "file 13 draft 1 (as sent)"),
    ("tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md", "file 13 draft 2 (as sent)"),
    ("tests/Revision 2 - file 13 draft 3, theory text.md", "file 13 draft 3"),
    ("tests/Revision 2 - file 13 draft 4, theory text.md", "file 13 draft 4"),
    (D5, "file 13 draft 5"),
    ("tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md", "scrubbed copy"),
    ("tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md", "repaired copy"),
    ("tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md", "latest text"),
]
CL = "tests/Revision 2 - change list, draft of 23 September.md"
PLAN = "tests/Revision 2 - plan and test round, draft of 23 September.md"
WL = "tests/Revision 2 - worklist, draft of 23 September.md"
SCEPTIC = "tests/S95 Scrub - vocabulary, sceptic's rulings.md"
MIMO = "results/S88 Cross-examination - three defects - returns/Mimo in three parts/"
PH = "[no wording given] "


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def line(p, n):
    return read(p).split("\n")[n - 1]


def part_at(p, n):
    """'Part … — title / section' from the headings above line n (file 11 style: '# Part', '## section')."""
    part, sec = None, None
    for i, l in enumerate(read(p).split("\n")[:n], 1):
        if l.startswith("# Part"):
            part, sec = l[2:], None
        elif l.startswith("## ") and part:
            sec = l[3:]
        elif l.startswith("# ") and not l.startswith("# Part"):
            part, sec = None, None
    if part is None:
        return "Front matter (before Part 0)"
    return part + (" / " + sec if sec else "")


def carried(words):
    """Collector C's applied_in form: every later text that holds the words, or None."""
    hit = [lab for p, lab in VERS if words in read(p)]
    return "; ".join(hit) if hit else None


def cell(p, n, col):
    """Column col of the table row at line n, as written (markdown's \\| read as |)."""
    l = line(p, n)
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", l)[1:-1]]
    return cells[col]


RECS = []


def rec(**k):
    base = dict(rid=None, round=None, source_file=None, source_ref=None, kind="recommendation", status=None,
                applied_in=None, target_text=None, target_line=None, target_part=None, old="", new="",
                old_sentence="", new_sentence="", scope="span", same_as=[])
    base.update(k)
    RECS.append(base)


# ---------------------------------------------------------------- 1. the change list's fixes before draft 1
# "What the checks changed", "Fixed: 19 entries" (lines 111-133). W37.1 and W58(ii).1 change only the
# expected ruling, so they have no record here. Rows: (entry, file line, file-11 line, old, new or None).
FIXES = [
    ("W22.1", 116, "account", "the explanatory candidate (Part V) that the criticism offers for \\(p_\\delta\\)"),
    ("W22.2", 117, "", "as grounds for an alleged defect in a target"),
    ("W30.1", 118, "", None),
    ("W39.1", 119, "", "identity of that assertion with the target's answer"),
    ("W7.3", 120, "", None),
    ("W57.1 + W32(b).1", 122, "", "does not certify the restriction as appropriate"),
    ("W17.2", 123, "realizable transports", "candidate transports"),
    ("W12.1", 124, "", None),
    ("W23.1", 125, "", None),
    ("W36.1", 126, "a separate measure", "a separate matter"),
    ("W45.1", 127, "kind of carrier", "physical medium"),
    ("W35.2", 128, "", "is violated, and the failure is not surprise"),
    ("W33.1", 129, "", None),
    ("W40.1", 130, "", None),
    ("W41.1", 131, "", None),
    ("W1.1", 132, "", None),
    ("W38.1", 133, "", None),
]
CREC = {}
for l in open(os.path.join(COLLECT, "collector C.jsonl"), encoding="utf-8"):
    r = json.loads(l)
    m = re.match(r"change list draft 5, entry (W[^ ]+) ", r["source_ref"])
    if m:
        CREC[m.group(1)] = r
for entry, ln, old, new in FIXES:
    row = line(CL, ln)
    assert row.startswith("| " + entry + " |"), (entry, row)
    fline = int(cell(CL, ln, 1))
    what = cell(CL, ln, 3)
    c = CREC[entry.split(" + ")[0]]
    assert c["target_line"] == fline, entry
    check = cell(CL, ln, 2)
    common = dict(round="S90", source_file=CL,
                  source_ref="section 'What the checks changed', table 'Fixed: 19 entries', row %s (file line %d), check %s; "
                             "the entry as first drafted, before the checks, is not held" % (entry, ln, check),
                  target_text=c["target_text"] + ", as change list entry %s first proposed to change it, before the two checks" % entry,
                  target_line=fline, target_part=c["target_part"],
                  same_as=[CL + "#" + entry])
    if new is None:
        rec(status="applied", applied_in=c["applied_in"], new=PH + what, scope="sentence", **common)
    else:
        assert new in what and (old == "" or old in what), entry
        at = carried(new)
        rec(status="applied" if at else "superseded", applied_in=at or "none (later drafts of entry %s changed it)" % entry,
            old=old, new=new, **common)

# ---------------------------------------------------------------- 2. S88: Mimo's own wordings
f3 = read(MIMO + "s88_xexam_mimo_F3.response.txt").split("\n")
p7 = f3[14]
assert p7.startswith("**7. My wording, if repairing.**")
s3 = re.search(r'S3 becomes: "(.*?)" To line 246 add', p7).group(1)
add246 = re.search(r'To line 246 add: "(.*?)" To line 522', p7).group(1)
B = {json.loads(l)["rid"]: json.loads(l) for l in open(os.path.join(COLLECT, "collector B.jsonl"), encoding="utf-8")}
b269, b285, b282 = B["B-269"], B["B-285"], B["B-282"]
rec(round="S88", source_file=MIMO + "s88_xexam_mimo_F3.response.txt",
    source_ref="point 7, 'My wording, if repairing', S3 (file line 15); settled positions, F3: \"Mimo's own S3 wording is not adopted\" "
               "(results/S88 Reading of Mimo's reply in three parts, and the settled positions.md, line 402)",
    status="declined", applied_in="none", target_text=b269["target_text"], target_line=b269["target_line"],
    target_part=b269["target_part"], old=b269["old"], new=s3, old_sentence=b269["old_sentence"], scope="sentence")
rec(round="S88", source_file=MIMO + "s88_xexam_mimo_F3.response.txt",
    source_ref="point 7, 'My wording, if repairing', the sentences for line 246 (file 10 numbering; file 11 line 233) (file line 15); "
               "settled positions, F3 (line 310 and the typing sentence of change 3)",
    status="declined", applied_in="none", target_text=b285["target_text"], target_line=b285["target_line"],
    target_part=b285["target_part"], old="", new=add246, old_sentence=b285["old_sentence"], scope="sentence")
f2 = read(MIMO + "s88_xexam_mimo_F2.response.txt").split("\n")[12]
assert f2.startswith("> **Approximate transport.**")
rec(round="S88", source_file=MIMO + "s88_xexam_mimo_F2.response.txt",
    source_ref="point 4, the wording offered for Approximate transport (file line 13); settled positions, F2, "
               "'The final repair wording' takes parts of it in other words",
    status="superseded", applied_in="none", target_text=b282["target_text"], target_line=b282["target_line"],
    target_part=b282["target_part"], old=b282["old"], new=f2[2:], scope="paragraph")

# ---------------------------------------------------------------- 3. the plan's own 'Take' wordings
# (item, file line, file-11 line, old, new or None for the cell as a description, prefix of the Take text)
PLAN_ROWS = [
    ("W7", 97, 33, "", None),
    ("W11", 101, 271, "", "is not excluded by (F1), and is an account when it meets the other conditions of (E)"),
    ("W11", 101, 528, "", PH + "L528 s3 changed in step"),
    ("W22", 112, 373, "", PH + "restore 00:620"),
    ("W22", 112, 373, "", "the question whether z has \\(\\delta\\) in respect of p"),
    ("W22", 112, 373, "represents how it bears", "represents its alleged connection"),
    ("W33", 123, 315, "", "(E) is fidelity: a commitment that does no work passes (E), and (B) reports it as critical in no support; "
                          "how hard an account is to vary is a separate measure and grades nothing"),
    ("W35", 125, 217, "", None),
    ("W41", 131, 401, "", PH + "restore the first two paragraphs of 00:855–861 after Build"),
    ("W41", 131, 401, "", "a witness may identify a binding by its use (reason use, Part IX); a carrier that delivers content it does "
                          "not use that way has relayed it, and relay is not construction"),
    ("W57", 143, 161, "", "where the claim states the ground of its restriction, the verdict is given with that ground; where it "
                          "states none, the ground is a missing declared input (Part XIV)"),
    ("W58", 144, 301, "", "the supports assessed are subsets of the written Γ, not a support someone could write in its place"),
    ("W58", 144, 33, "appears anywhere", "is defined or presupposed (Derivation 6)"),
]
ENTRIES = {}
for e in CREC:
    ENTRIES.setdefault(re.match(r"(W\d+)", e).group(1), []).append(e)
for item, ln, fl, old, new in PLAN_ROWS:
    row = line(PLAN, ln)
    assert ("| " + item + " ") in row or ("| **" + item + "**") in row, (item, row[:40])
    take = cell(PLAN, ln, 1)
    take = re.sub(r"^\*\*Take[^*]*\*\*:?\s*", "", take)
    es = sorted(ENTRIES[item])
    carry = "none (the change list's entries %s carry the item)" % ", ".join(es)
    if new is None:
        new = PH + take
    elif not new.startswith(PH):
        assert new in row and (old == "" or old in row), (item, new)
    at = None if new.startswith(PH) else carried(new)
    kind_of = "Take (b′)" if item == "W35" else "Take"
    rec(round="S90", source_file=PLAN,
        source_ref="table of the worklist items, row %s (file line %d), '%s'" % (item, ln, kind_of),
        status="applied" if at else "superseded", applied_in=at or carry,
        target_text=F11_LABEL, target_line=fl, target_part=part_at(F11, fl), old=old, new=new,
        scope="sentence" if (new.startswith(PH) or len(new) > 120) else "span")
# the F3 rider (lines 204-205)
r204, r205 = line(PLAN, 204), line(PLAN, 205)
old_r = "in \\(E|(\\Gamma\\setminus G)\\), with the named background fixed"
new_r = "in \\(E\\) with the components of \\(G\\) deleted (Part II: a deleted component imposes the full relation on its ports)"
assert old_r in r204 and new_r in r204
add_r = "\\(\\Gamma\\) is a set of components of \\(E\\): those the candidate offers as doing the work"
assert add_r in r205
for ln, old, new, tl, tp, os_, scope in [
        (204, old_r, new_r, b269["target_line"], b269["target_part"], "", "span"),
        (205, "", add_r, b285["target_line"], b285["target_part"], b285["old_sentence"], "sentence")]:
    at = carried(new)
    rec(round="S90", source_file=PLAN,
        source_ref="F3, 'Rider proposed here, not yet examined by S88' (file line %d); the rider applies to option B's S3" % ln,
        status="applied" if at else "superseded", applied_in=at or "none (the settled F3 wording of S88 carries it in other words)",
        target_text=F11_LABEL + (", as option B's S3 would read" if ln == 204 else ""), target_line=tl, target_part=tp,
        old=old, new=new, old_sentence=os_, scope=scope)

# ---------------------------------------------------------------- 4. worklist items with no record
for item, ln_head, fl, text, tpath, tlabel in [
        ("W49", 985, 335, "new constructions for Part VII from file 12: causation by absence (12:341–343), prevention and double "
                          "prevention (12:345–347), and absence and prevention added to attack B (12:548)", F11, F11_LABEL),
        ("W50", 997, 391, "a clarification from file 12 (12:411): An intervention whose prediction fails refutes the conjunction "
                          "that includes \"the intervention realized the intended edit\".", F11, F11_LABEL),
        ("W2", 150, 574, "carry Derivation 3's qualification (O48) into file 10: L38 (grievance 3), L74 (attack D), L539 (Part XV), "
                         "L567–573 (Derivation 3)", F10, "file 10 (authority/10 Claude Fable Semantics - standalone theory.md)")]:
    assert line(WL, ln_head).startswith("### " + item + "."), item
    rec(round="S90", source_file=WL,
        source_ref="worklist item %s (L%d); the plan leaves it out (plan, line %d)" % (item, ln_head, 137 if item != "W2" else 146),
        status="declined", applied_in="none", target_text=tlabel, target_line=fl if item != "W2" else 567,
        target_part=part_at(tpath, fl if item != "W2" else 567), new=PH + text, scope="sentence")

# ---------------------------------------------------------------- 5. the sceptic's rows for four words (S95)
d5 = read(D5)
scr = read(VERS[5][0])
SC = [
    (110, "\"unsettled\"", "\"left open\"", [25, 522], ["D-517"]),
    (111, "\"there is no objectivity\"; \"Objectivity lives in the physics and the fidelity facts; scope-honesty lives in the record\"",
     "Objection: \"and nothing is independent of anyone's say-so\"; reply: \"What is independent of any assessor lies in the physics "
     "and in whether transports are faithful; scope-honesty lies in the record\"", [43], []),
    (112, "\"verdict\"", "\"assessment\": \"an assessment of the restriction is made with that statement\"; \"an assessment that "
     "depends on one of these … is made given the input; where the input is missing, it is left open\"", [159, 522, 534], ["D-516"]),
    (113, "\"credit\", \"credits\", \"credited\"", "\"attribution\" / \"attributes\": \"ProducedBy attributes a repair to the "
     "contributions …\"; \"the history supplies no division of the attribution that it does not contain\"", [25, 307, 427, 441, 522], ["D-564"]),
]
D5L = d5.split("\n")


def d5_part(n):
    part = None
    for l in D5L[:n]:
        if l.startswith("# Part"):
            part = l[2:]
    return part or "Front matter (before Part 0)"


for ln, old, new, lines_, same in SC:
    row = line(SCEPTIC, ln)
    for q in re.findall(r'"([^"]+)"', old + " " + new):
        assert q in row, (ln, q)
        if old.find(q) >= 0:
            assert q in d5, (ln, q)
    quoted_new = re.findall(r'"([^"]+)"', new)
    found = [all(x.strip() in scr for x in q.split("…")) for q in quoted_new]
    at = "scrubbed copy" if all(found) else ("scrubbed copy, in other wording" if found[0] else None)
    parts = []
    for n in lines_:
        pt = d5_part(n)
        if pt not in parts:
            parts.append(pt)
    rec(round="S95", source_file=SCEPTIC,
        source_ref="section 3 (3. Occurrences the proposal does not cover), second table, row at file line %d; "
                   "the cells' bracketed grounds are left out" % ln,
        status="applied" if at else "not applied", applied_in=at or "none",
        target_text="draft 5", target_line=lines_[0] if len(lines_) == 1 else None,
        target_part=("several places: " if len(lines_) > 1 else "") + "; ".join(parts) + " (l. %s)" % ", ".join(map(str, lines_)),
        old=old, new=new, scope="term", same_as=same)

# ---------------------------------------------------------------- 6. whole texts made outside the lined-up chain
rec(round="file 10 (before log 25)", source_file=F10,
    source_ref="file 00 and file 10 as whole texts; log 56 (file 10 added to the repository as uploaded)",
    kind="edit", status="applied", applied_in="file 10",
    target_text="file 00 (" + F00 + ")", target_line=None, target_part="whole text",
    new=PH + "file 10, the first standalone theory, made as a new text from its predecessor, file 00 (FW5)", scope="whole text")
rec(round="S77", source_file="authority/12 Claude Fable Semantics - causality, standalone theory.md",
    source_ref="log S77 (records/Semantics - project story.md); decision S9",
    kind="edit", status="applied", applied_in="file 12",
    target_text=F11_LABEL, target_line=None, target_part="whole text",
    new=PH + "file 12, the whole theory rewritten from file 11 in terms of causality, with no mention of provenance, "
             "as a separate standalone text", scope="whole text")

# ---------------------------------------------------------------- checks and write
for i, r in enumerate(RECS, 1):
    r["rid"] = "F-%d" % i
    src = read(r["source_file"]).replace("\\|", "|")
    if not r["new"].startswith(PH) and r["source_file"] != SCEPTIC:
        assert r["new"] in src, r["rid"]
    for k in ("old", "new", "old_sentence", "new_sentence"):
        assert isinstance(r[k], str)
    if r["old_sentence"]:
        assert r["old_sentence"] in read(F11), r["rid"]
    if r["old"] and r["target_text"].startswith("file 11") and "first proposed" not in r["target_text"] \
            and "option B" not in r["target_text"]:
        assert r["old"] in read(F11), (r["rid"], r["old"])
ORDER = ["rid", "round", "source_file", "source_ref", "kind", "status", "applied_in", "target_text", "target_line",
         "target_part", "old", "new", "old_sentence", "new_sentence", "scope", "same_as"]
out = "".join(json.dumps({k: r[k] for k in ORDER}, ensure_ascii=False) + "\n" for r in RECS)
with open(os.path.join(COLLECT, "collector F.jsonl"), "w", encoding="utf-8", newline="") as f:
    f.write(out)
from collections import Counter
print("build_F.py: %d records; %s" % (len(RECS), dict(Counter((r["round"], r["status"]) for r in RECS))))
