"""Collector E (log S98): recommendations of wording never applied, from the records of logs S91, S93 and S94.

Writes collector E.jsonl beside this folder (refuses to overwrite a non-empty file unless --force is given,
which is only for rebuilding this collector's own file). Every "new" and "old" is taken from its source by
program or checked against it byte for byte; nothing is paraphrased except the "[no wording given]" descriptions.
No reason is copied: source_ref is the only pointer to the reasons.
"""
import json, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "collector E.jsonl")
FIELDS = ["rid", "round", "source_file", "source_ref", "kind", "status", "applied_in", "target_text",
          "target_line", "target_part", "old", "new", "old_sentence", "new_sentence", "scope", "same_as"]

# ---------------------------------------------------------------- sources
P_SF = "tests/Revision 2 - the owner's statement on choosing, against draft 5, 25 September.md"
P_RA = "tests/working files/S94 owner statement on choosing/reader A-text.md"
P_RB = "tests/working files/S94 owner statement on choosing/reader B-scope.md"
P_RC = "tests/working files/S94 owner statement on choosing/reader C-choices.md"
P_RD = "tests/working files/S94 owner statement on choosing/reader D-sources.md"
P_CL = "tests/Revision 2 - change list, draft of 23 September.md"
P_X03 = "results/S93 reading rulings/ruling S93 X03 W19.1.md"
P_ES = "tests/working files/errcorr/03 synthesis.md"
P_EG = "tests/Revision 2 - error correction and grading, analysis of 24 September.md"
P_CS = "tests/Revision 2 - does correction stick, the hard-to-vary lemma and its limit, analysis of 24 September.md"
P_RV = "tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md"
P_RE = "tests/working files/rivals/01 entries.md"
P_RM = "tests/working files/rivals/02 models.md"

SRC = {}
SRC_MD5 = {}
for p in [P_SF, P_RA, P_RB, P_RC, P_RD, P_CL, P_X03, P_ES, P_EG, P_CS, P_RV, P_RE, P_RM]:
    SRC[p], SRC_MD5[p] = read(p)

T = {n: load(n) for n in ["file 11", "draft 3", "draft 4", "draft 5", "latest text", "change list"]}
CL_LINES = T["change list"]

records = []


def has(p, s):
    """Assert s occurs verbatim in source p; return s."""
    if s not in SRC[p]:
        raise SystemExit("not verbatim in %s: %r" % (p, s[:100]))
    return s


def add(round_, src, ref, kind, status, target, line, old, new, *, scope, applied_in="none",
        old_sentence=None, new_sentence=None, anchor=None, same_as=(), part=None, check_old=True):
    """Build one record. target: a TEXTS name. anchor: for an insertion, the sentence after which the new
    words go (checked in the target line)."""
    lines = T[target]
    tl = TEXTS[target][2]
    if line is not None:
        ln = lines[line - 1]
        if check_old and old and "\n" not in old and old not in ln:
            raise SystemExit("old not on target line %s:%d: %r" % (target, line, old[:80]))
        if anchor is not None and anchor not in ln:
            raise SystemExit("anchor not on target line %s:%d: %r" % (target, line, anchor[:80]))
        if old_sentence is None:
            if old and "\n" not in old and check_old:
                if scope in ("sentence", "span", "term"):
                    old_sentence, ns = replaced_sentence(ln, old, new)
                    if new_sentence is None:
                        new_sentence = ns
                else:
                    old_sentence = sentence_of(ln, old)
            else:
                old_sentence = ""
        if new_sentence is None:
            new_sentence = new if (not old and scope in ("sentence", "paragraph")) else ""
        if new.startswith("[no wording given]"):
            new_sentence = ""
        tp = part if part is not None else part_at(lines, line)
    else:
        old_sentence = old_sentence or ""
        new_sentence = new_sentence or ""
        tp = part or ""
    rid = "E-%d" % (len(records) + 1)
    r = {"rid": rid, "round": round_, "source_file": src, "source_ref": ref, "kind": kind, "status": status,
         "applied_in": applied_in, "target_text": tl, "target_line": line, "target_part": tp, "old": old,
         "new": new, "old_sentence": old_sentence, "new_sentence": new_sentence, "scope": scope,
         "same_as": list(same_as)}
    records.append(r)
    return rid


D5 = "draft 5"
L = T[D5]
DECL_TEXT = "the note of file 13, its list of changes of claim (declarations; proposed for a change against file 13 draft 5, never entered)"


def as_declaration(rid, change_no, line):
    """Declarations go to the revision record, not to the theory text (as collector C records them)."""
    r = next(x for x in records if x["rid"] == rid)
    r["target_text"] = DECL_TEXT
    r["target_line"] = None
    r["target_part"] = "Front matter (before Part 0) / the note of file 13, the declaration of change %d of the owner's statement file (draft 5 L%d, %s)" % (change_no, line, part_at(L, line))
    r["scope"] = "paragraph"
SF, RA, RB, RC, RD = SRC[P_SF], SRC[P_RA], SRC[P_RB], SRC[P_RC], SRC[P_RD]

# anchors in draft 5
A317 = "Nothing here counts rivals, grades a candidate or ranks candidates."
AFITS = "A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing a condition of (E)."
ANOONE = "a candidate that nobody has offered is no one's rival."
A429 = "Closing an episode is a decision, not a proof."
A159 = "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one."

# ================================================================ S94: the statement file, section 8
sf_ref = "the owner's statement file (log S94), section 8.%d, change %d%s"

c1 = has(P_SF, between(SF, "Nothing here says which of two rivals anyone is to choose, keep or drop",
                       "for that assessor the problem for \\(p\\) stands."))
E_c1 = add("S94", P_SF, sf_ref % (1, 1, " (Part VI, \"Problems\"), wording; placed after \"" + A317 + "\" (L317); marked recommended; proposed only, never entered in the change list"),
           "recommendation", "not applied", D5, 317, "", c1, scope="sentence", anchor=A317)
d1 = has(P_SF, between(SF, "Part VI now says outright that it prescribes nothing", "no verdict changes."))
as_declaration(add("S94", P_SF, sf_ref % (1, 1, ", declaration (proposed wording for the revision record, layer 2)"),
    "recommendation", "not applied", D5, 317, "", d1, scope="sentence", new_sentence=d1, part=part_at(L, 317) + " (declaration)"), 1, 317)

c2a_old = has(P_SF, quoted_after(SF, "L299: delete the final clause "))
E_c2a = add("S94", P_SF, sf_ref % (2, 2, " (remove Boundary (D)), edit 1 of 3: L299, delete the final clause; marked recommended; proposed only"),
            "recommendation", "not applied", D5, 299, c2a_old, "", scope="span", new_sentence="")
disp = "\n".join(L[300:303])
assert disp.startswith("\\[") and "Boundary" in disp and disp.endswith("\\]")
E_c2b = add("S94", P_SF, sf_ref % (2, 2, " (remove Boundary (D)), edit 2 of 3: L301-L303, delete the display that defines Boundary_{E,p}, tag (D), with the blank line after it (L304), so that \"**Finite monotone theorem.**\" (L305) follows the paragraph; marked recommended; proposed only"),
            "recommendation", "not applied", D5, 301, disp, "", scope="paragraph", old_sentence=disp, new_sentence="")
c2c_old = has(P_SF, "(S), (B), (D) depend on (E).")
c2c_new = has(P_SF, "(S), (B) depend on (E).")
E_c2c = add("S94", P_SF, sf_ref % (2, 2, " (remove Boundary (D)), edit 3 of 3: L526; marked recommended; proposed only"),
            "recommendation", "not applied", D5, 526, c2c_old, c2c_new, scope="sentence")
d2 = has(P_SF, between(SF, "Part VI no longer defines \\(\\operatorname{Boundary}_{E,p}\\) (D) or the family",
                       "no verdict, derivation or other definition used them."))
as_declaration(add("S94", P_SF, sf_ref % (2, 2, ", declaration (proposed wording for the revision record, layer 2)"),
    "recommendation", "not applied", D5, 302, "", d2, scope="sentence", new_sentence=d2, part=part_at(L, 302) + " (declaration)"), 2, 302)

c3_old = has(P_SF, "an answer it refutes stays refuted on \\(p\\) (Part VIII)")
c3_new = has(P_SF, "an answer it refutes stays refuted on \\(p\\) for as long as the test's result stays established (Part VIII)")
E_c3 = add("S94", P_SF, sf_ref % (3, 3, " (Part VI, \"Problems\", kind (i)), wording; marked optional, low priority; proposed only"),
           "recommendation", "not applied", D5, 317, c3_old, c3_new, scope="span")

c4 = has(P_SF, between(SF, "Nothing here requires an episode to be completed or closed, and a problem",
                       "that a system leaves unsolved stands (Part VI)."))
E_c4 = add("S94", P_SF, sf_ref % (4, 4, " (Part X, \"Episodes\"), wording; placed after \"" + A429 + "\" (L429); an alternative to change 1, not an addition; proposed only"),
           "recommendation", "not applied", D5, 429, "", c4, scope="sentence", anchor=A429)
d4 = has(P_SF, between(SF, "Part X now says outright that no episode is required", "and that a problem left unsolved stands."))
as_declaration(add("S94", P_SF, sf_ref % (4, 4, ", declaration (proposed wording for the revision record, layer 2)"),
    "recommendation", "not applied", D5, 429, "", d4, scope="sentence", new_sentence=d4, part=part_at(L, 429) + " (declaration)"), 4, 429)

c5a_old = has(P_SF, "of the test that yields it")
c5a_new = has(P_SF, "of the test or examination that yields it")
E_c5a = add("S94", P_SF, sf_ref % (5, 5, ", edit 1 of 2 (reader B's sketch B3; conditional on a \"yes\" to the first choice of file 93); \"Not proposed now\""),
            "recommendation", "not applied", D5, 315, c5a_old, c5a_new, scope="span")
c5b = has(P_SF, between(SF, "Such a result may come from examining the candidate as well as from a test of the target",
                        "are live (K2)."))
E_c5b = add("S94", P_SF, sf_ref % (5, 5, ", edit 2 of 2: inserted after L315's \"fits\" sentence (conditional on a \"yes\" to the first choice); \"Not proposed now\""),
            "recommendation", "not applied", D5, 315, "", c5b, scope="sentence", anchor=AFITS)

c6a_old = has(P_SF, "when one of them has been offered as an answer to \\(p\\) in place of the other and they conflict")
c6a_new = has(P_SF, "when each has been offered as an answer to \\(p\\), by anyone, the assessor included, and they conflict")
E_c6a = add("S94", P_SF, sf_ref % (6, 6, ", edit 1 of 3 (conditional on the owner's answer to the second choice of file 93); \"Not proposed now\""),
            "recommendation", "open for the owner", D5, 315, c6a_old, c6a_new, scope="span")
c6b = has(P_SF, "An assessor who forms a candidate as an answer to \\(p\\) has offered it, to that assessor.")
E_c6b = add("S94", P_SF, sf_ref % (6, 6, ", edit 2 of 3: added after \"" + ANOONE + "\" (L315); conditional on the second choice; \"Not proposed now\""),
            "recommendation", "open for the owner", D5, 315, "", c6b, scope="sentence", anchor=ANOONE)
c6c_old = has(P_SF, "rivals on conflict and on the offer of one in place of the other")
c6c_new = has(P_SF, "rivals on conflict and on the offer of each as an answer to \\(p\\)")
E_c6c = add("S94", P_SF, sf_ref % (6, 6, ", edit 3 of 3: L526; conditional on the second choice; \"Not proposed now\""),
            "recommendation", "open for the owner", D5, 526, c6c_old, c6c_new, scope="span")

# section 9 of the statement file
b2 = has(P_SF, between(SF, "Where the target is not a physical system, as a proof's is not (Part VII)",
                       "can bear the organization so edited (Part I)."))
E_b2 = add("S94", P_SF, "the owner's statement file (log S94), section 9, \"Noticed along the way\" (reader B, finding B2): clarification placed after L159's first sentence; kind WORDING if that reading is the intended one; \"for a checker\", not counted as something the statement adds",
           "recommendation", "not applied", D5, 159, "", b2, scope="sentence", anchor=A159)
a4_old = has(P_SF, "Losses outside \\(P\\) must be exposed.")
a4_new = has(P_SF, "A repair claim exposes its losses outside \\(P\\).")
E_a4 = add("S94", P_SF, "the owner's statement file (log S94), section 9, \"Not proposed\", first item (reader A, finding A4), and section 10.5 (A4): the L441 rewording is dropped",
           "recommendation", "declined", D5, 441, a4_old, a4_new, scope="sentence")

# ================================================================ S94: the four readers' working files
ra_ref = "S94 working file, reader A, finding %s"
a3 = has(P_RA, between(RA, "Nor does anything here say what an assessor must do with rivals or with a problem",
                       "does not by itself solve the problem."))
add("S94", P_RA, ra_ref % "A3, \"Proposed change\" (inserted after \"" + A317 + "\", L317); taken into change 1 of the statement file in other words (E-1)",
    "recommendation", "superseded", D5, 317, "", a3, scope="sentence", anchor=A317)
a3p = has(P_RA, "It does not say what anyone must do with the candidates, rivals and problems it describes (Part VI).")
add("S94", P_RA, ra_ref % "A3, \"Checks\": an optional pointer for Part 0 after L25, \"Only after the body sentence exists\"; not carried into the statement file",
    "recommendation", "not applied", D5, 25, "", a3p, scope="sentence")
a4r = has(P_RA, "A repair claim exposes its losses outside \\(P\\)")
add("S94", P_RA, ra_ref % "A4, \"Proposed change\": the optional L441 reading; dropped in the statement file (section 9 and 10.5)",
    "recommendation", "declined", D5, 441, a4_old, a4r, scope="sentence", same_as=[E_a4])
a6 = has(P_RA, between(RA, "Nothing here requires an episode to be completed or closed: a system may leave one",
                       "stands (Part VI)."))
add("S94", P_RA, ra_ref % "A6, \"Proposed change\" (\"If the owner wants it said\", after L429's \"" + A429 + "\"); taken into change 4 of the statement file in other words (E-8)",
    "recommendation", "superseded", D5, 429, "", a6, scope="sentence", anchor=A429)
a10_new = has(P_RA, "an answer it refutes stays refuted on \\(p\\) for as long as the result stays established (Part VIII)")
add("S94", P_RA, ra_ref % "A10, \"Proposed change\" (optional, wording only); taken into change 3 of the statement file in other words (E-7)",
    "recommendation", "superseded", D5, 317, has(P_RA, c3_old), a10_new, scope="span")

rb_ref = "S94 working file, reader B, %s"
b2r = has(P_RB, between(RB, "Where the target is not a physical system, as a proof's is not (Part VII)",
                        "can bear the organization so edited (Part I)."))
add("S94", P_RB, rb_ref % "finding B2, \"Proposed change (clarification on reading (a), for a checker)\": after L159's first sentence; recorded in the statement file's section 9 (E-15)",
    "recommendation", "not applied", D5, 159, "", b2r, scope="sentence", anchor=A159, same_as=[E_b2])
add("S94", P_RB, rb_ref % "section 2.7 (finding B3), \"Wording, if the owner confirms 'yes'\", first bullet; the statement file's change 5, edit 1 (E-10)",
    "recommendation", "not applied", D5, 315, has(P_RB, c5a_old), has(P_RB, c5a_new), scope="span", same_as=[E_c5a])
b3b = has(P_RB, between(RB, "Such a result may come from examining the candidate as well as from a test of the target",
                        "are live (K2)."))
add("S94", P_RB, rb_ref % "section 2.7 (finding B3), second bullet: inserted after L315's \"fits\" sentence; the statement file's change 5, edit 2 (E-11)",
    "recommendation", "not applied", D5, 315, "", b3b, scope="sentence", anchor=AFITS, same_as=[E_c5b])
b3c = has(P_RB, between(RB, "An assessor who holds a usable receipt that a criticism of a candidate bears on it (K1)",
                        "holds a result established against that candidate (Part VI)."))
add("S94", P_RB, rb_ref % "section 2.7 (finding B3), third bullet: \"Alternatively, or as well, in Part IX after (K1)\" (the display tagged (K1), L380); conditional on a \"yes\" to the first choice; not carried into the statement file",
    "recommendation", "not applied", D5, 380, "", b3c, scope="sentence")
b8 = has(P_RB, between(RB, "It is the physics adopted, and is itself conjectural", "is given with it."))
add("S94", P_RB, rb_ref % "finding B8, \"Proposed change (optional, for a checker)\": at L517, after the description of the physical module; the statement file's section 9, \"Not proposed\", second item",
    "recommendation", "declined", D5, 517, "", b8, scope="sentence")

rc_ref = "S94 working file, reader C, %s"
add("S94", P_RC, rc_ref % "section 1.2 (finding C2), the possible wording \"If the owner answers yes to both halves\", first edit (L315); the statement file's change 6, edit 1 (E-12)",
    "recommendation", "open for the owner", D5, 315, has(P_RC, c6a_old), has(P_RC, c6a_new), scope="span", same_as=[E_c6a])
add("S94", P_RC, rc_ref % "section 1.2 (finding C2), second edit, added after \"" + ANOONE + "\" (L315); the statement file's change 6, edit 2 (E-13)",
    "recommendation", "open for the owner", D5, 315, "", has(P_RC, c6b), scope="sentence", anchor=ANOONE, same_as=[E_c6b])
c8v = has(P_RC, between(RC, "Nothing here says what anyone is to do with rivals or with a problem.",
                        "to stop inquiring is a decision (Part X).", after="### 2.6 What the statement adds on the chooser"))
add("S94", P_RC, rc_ref % "section 2.6 and finding C8, the variant placed after \"" + A317 + "\" (L317); taken into change 1 of the statement file in other words (E-1)",
    "recommendation", "superseded", D5, 317, "", c8v, scope="sentence", anchor=A317)
add("S94", P_RC, rc_ref % "section 3.8 \"Proposed change\" (finding C6), first bullet (L299); the statement file's change 2, edit 1 (E-3)",
    "recommendation", "not applied", D5, 299, has(P_RC, c2a_old), "", scope="span", new_sentence="", same_as=[E_c2a])
add("S94", P_RC, rc_ref % "section 3.8 \"Proposed change\" (finding C6), second bullet (L301-L303, the display with tag (D), and the blank line after it); the statement file's change 2, edit 2 (E-4)",
    "recommendation", "not applied", D5, 301, disp, "", scope="paragraph", old_sentence=disp, new_sentence="", same_as=[E_c2b])
add("S94", P_RC, rc_ref % "section 3.8 \"Proposed change\" (finding C6), third bullet (L526); the statement file's change 2, edit 3 (E-5)",
    "recommendation", "not applied", D5, 526, has(P_RC, c2c_old), has(P_RC, c2c_new), scope="sentence", same_as=[E_c2c])

# reader D: the note of sources and departures, in the change list's entry W38.1 (CL line numbers as reader D gives them)
CLN = "change list"
d4s = has(P_RD, between(RD, "For him, solving a problem means creating an explanation without the conflict (p.17).",
                        "and a recognized difficulty by a repair (Part XI)."))
ASP = "when the system represents it."
add("S94", P_RD, "S94 working file, reader D, finding D4, \"Proposed change (optional, note only, CL403)\": added after \"" + ASP + "\" in the note's *Surprise and problems* line; the statement file's section 9, \"Not proposed\", third item",
    "recommendation", "declined", CLN, 403, "", d4s, scope="sentence", anchor=ASP,
    part="Note of sources and departures / Departures / Surprise and problems")
d14_old = has(P_RD, "here it is shown only by offering the rival")
d14_new = has(P_RD, "here ease of variation is shown only by offering the rival")
E_d14 = add("S94", P_RD, "S94 working file, reader D, finding D14, \"Proposed change (CL399, a small wording change)\"; the statement file's section 9, \"Not proposed\", fourth item: \"It waits on that choice\" (the first choice of file 93)",
            "recommendation", "not applied", CLN, 399, d14_old, d14_new, scope="span",
            part="Note of sources and departures / Departures / Hard to vary")
d14b = has(P_RD, "A candidate that examination shows failing a condition of an account no longer fits, with no experiment (Part VI).")
add("S94", P_RD, "S94 working file, reader D, finding D14, the conditional second sentence (\"If the owner settles file 93's first choice for counting\", \"must not be added before it\"), after the *Hard to vary* sentence it rewords (CL399)",
    "recommendation", "not applied", CLN, 399, "", d14b, scope="sentence",
    anchor="here it is shown only by offering the rival, which is the criticism.",
    part="Note of sources and departures / Departures / Hard to vary")

# ================================================================ S93: carried forward, not held by collector C
has(P_CL, "**Classes across candidates.**")
add("S93", P_CL, "change list, \"Carried forward after S93\", \"Findings for later entries\", item \"Classes across candidates\"; ruling S93 X03 (W19.1), \"Findings for later entries\", finding 3",
    "recommendation", "not applied", "draft 4", 119, "",
    "[no wording given] if a later revision wants classes of components across candidates, state the relation's domain (components of candidates with transports from one \\(D\\), read on one \\(C\\)) and its transitivity, as a CLAIM",
    scope="sentence", check_old=False)
has(P_CL, "**The sources note's fallback for *Surprise and problems*.**")
add("S93", P_CL, "change list, \"Carried forward after S93\", \"Findings for later entries\", item \"The sources note's fallback for *Surprise and problems*\" (ruling S93 X18, ruling 3); the FALLBACKS field of entry W38.1",
    "recommendation", "not applied", CLN, 435, "",
    "[no wording given] if the FALLBACKS table's fallback for the *Surprise and problems* line (its text in draft 3 of the change list) is ever used, apply to it the same replacement as ruling X18's fix",
    scope="sentence", check_old=False, part="Change list entry W38.1 / FALLBACKS")

# ================================================================ S91: the error-correction analysis, option (b) and (c)
ES, EG = SRC[P_ES], SRC[P_EG]
D3 = "draft 3"
L3 = T[D3]


def blockline(src, start):
    """The whole line of src that starts with start (unique), blockquote marker removed."""
    ls = [l for l in src.split("\n") if l.startswith(start)]
    if len(ls) != 1:
        raise SystemExit("line start %r found %d times" % (start, len(ls)))
    return unquote_block(ls[0])


es_par = blockline(ES, "> **Absorbed failure.**")
eg_par = blockline(EG, "> **Absorbed failure.**")
es_p3 = quoted_after(ES, "- Part III, at the end of D3:L159: ")
es_p6 = quoted_after(ES, "- Part VI, at the end of D3:L313: ")
eg_p3 = quoted_after(EG, "- Part III, at the end of D3:L159: ")
eg_p6 = quoted_after(EG, "Part VI, at the end of D3:L313: ")
eg_p5 = quoted_after(EG, "Part V, at the end of the first sentence of D3:L277 ", occurrence=2)
A363 = "A new index is a new claim."
A159_3 = "the ground is a missing declared input (Part XIV)."
A313_3 = "and it grades nothing."
A277_3 = "assessed elsewhere (Part IX)"

eg_ref = "error-correction analysis of 24 September (log S91), section 4, option (b), %s; the owner's decision S20 (\"A record is redundant.\")"
E_egp = add("S91", P_EG, eg_ref % "\"Draft wording\", a new paragraph in Part VIII after \"Historical index\" (D3:L363)",
            "recommendation", "declined", D3, 363, "", eg_par, scope="paragraph", anchor=A363)
E_eg3 = add("S91", P_EG, eg_ref % "pointer sentence for Part III, at the end of D3:L159",
            "recommendation", "declined", D3, 159, "", eg_p3, scope="sentence", anchor=A159_3)
E_eg6 = add("S91", P_EG, eg_ref % "pointer sentence for Part VI, at the end of D3:L313 (marked CHANGED: restated for accounts)",
            "recommendation", "declined", D3, 313, "", eg_p6, scope="sentence", anchor=A313_3)
E_eg5 = add("S91", P_EG, eg_ref % "optional pointer for Part V, at the end of the first sentence of D3:L277 (after \"… assessed elsewhere (Part IX)\")",
            "recommendation", "declined", D3, 277, "", eg_p5, scope="span", anchor=A277_3,
            old_sentence=sentence_of(L3[276], A277_3),
            new_sentence=sentence_of(L3[276], A277_3).replace(A277_3, A277_3 + eg_p5.rstrip(".")) + "")
add("S91", P_EG, "error-correction analysis of 24 September (log S91), section 4, option (c), \"Full grading from Pres\", its definition; not recommended there; the owner's decision S20",
    "recommendation", "declined", D3, 313, "",
    "[no wording given] full grading from Pres: fix a declared family V of variations of E and a set of jobs F; for candidates that share V, order them by inclusion of Pres(F), the variants that stay accounts on every job in F (smaller means harder to vary); a number, or any comparison across different families, needs a measure on V",
    scope="paragraph", check_old=False)
es_ref = "error-correction working file 03 (synthesis before its check, 24 September; log S91), section 4, option (b), %s; replaced by the checked answer's wording (%s)"
add("S91", P_ES, es_ref % ("\"Draft wording\", a new paragraph in Part VIII after \"Historical index\" (D3:L363)", E_egp),
    "recommendation", "superseded", D3, 363, "", es_par, scope="paragraph", anchor=A363)
add("S91", P_ES, es_ref % ("pointer sentence for Part III, at the end of D3:L159; the same words stand in the checked answer", E_eg3),
    "recommendation", "superseded", D3, 159, "", es_p3, scope="sentence", anchor=A159_3,
    same_as=[E_eg3] if es_p3 == eg_p3 else [])
add("S91", P_ES, es_ref % ("pointer sentence for Part VI, at the end of D3:L313", E_eg6),
    "recommendation", "superseded", D3, 313, "", es_p6, scope="sentence", anchor=A313_3)

# ================================================================ S91: the correction-sticks analysis
CS = SRC[P_CS]
csC = CS[CS.index("## Appendix C — The proposal"):CS.index("## Appendix D — The text attack")]
cs2 = CS[CS.index("### 2. The checked wording"):CS.index("### 3. The three test situations and the named cases")]


def block_between(seg, start, stop):
    a = seg.index(start)
    b = seg.index(stop, a)
    return unquote_block(seg[a:b].rstrip("\n").rstrip())


A313a = "For explanatory jobs \\(F\\subseteq F'\\),"
A313b = "the containment need not be strict;"
has(P_CS, "Replace \"" + A313a + "\" with \"For explanatory jobs \\(F\\subseteq F'\\) (a job is a question, Part III),\"")
csC_a1 = "For explanatory jobs \\(F\\subseteq F'\\) (a job is a question, Part III),"
csC_a2 = unquote_block([l for l in csC.split("\n") if l.startswith("> the containment need not be strict, and")][0])
csC_b = block_between(csC, "> **Correction in a common family.**", "**(c) Optional pointer, end of D3:L363.**")
csC_c = quoted_after(csC, "**(c) Optional pointer, end of D3:L363.** ") if csC.count("**(c) Optional pointer, end of D3:L363.** ") == 1 else None
cs2_a = unquote_block([l for l in cs2.split("\n") if l.startswith("> the containment need not be strict, and")][0])
cs2_b = block_between(cs2, "> **Witness in a common family.**", "**(c) Optional pointer, at the end of D3:L363.**")
cs2_c = unquote_block([l for l in cs2.split("\n") if l.startswith("> A set of jobs that omits one")][0])
for s in (csC_a2, csC_b, csC_c, cs2_a, cs2_b, cs2_c):
    assert s and s in unquote_block(CS)

cs2_ref = "correction-sticks analysis of 24 September (log S91), section 2 \"The checked wording\", %s; the owner's decision S20 on the set of versions, and lesson S26"
E_cs2a = add("S91", P_CS, cs2_ref % "(a) edit in D3:L313 (\"Hard-to-vary\")",
             "recommendation", "declined", D3, 313, A313b, cs2_a.rstrip(), scope="span")
E_cs2b = add("S91", P_CS, cs2_ref % "(b) new paragraph after D3:L313, \"Witness in a common family\" (lemma (H*), its second-candidate bridge, the narrowing clause and limits (i)-(iv)); blockquote markers removed",
             "recommendation", "declined", D3, 313, "", cs2_b, scope="paragraph")
E_cs2c = add("S91", P_CS, cs2_ref % "(c) optional pointer, at the end of D3:L363 (\"Historical index\")",
             "recommendation", "declined", D3, 363, "", cs2_c, scope="sentence", anchor=A363)
csC_ref = "correction-sticks analysis of 24 September (log S91), Appendix C (working file 03, the proposal before the text and model attacks), section 2, %s; replaced by the checked wording of section 2 (%s)"
add("S91", P_CS, csC_ref % ("(a), first replacement in D3:L313", "which drops it"),
    "recommendation", "superseded", D3, 313, A313a, csC_a1, scope="span")
add("S91", P_CS, csC_ref % ("(a), second replacement in D3:L313", E_cs2a),
    "recommendation", "superseded", D3, 313, A313b, csC_a2.rstrip(), scope="span")
add("S91", P_CS, csC_ref % ("(b) new paragraph after D3:L313, \"Correction in a common family\" (lemma (H*), with the companion clause on CriticalBlock, the narrowing clause and limits (i)-(iv)); blockquote markers removed", E_cs2b),
    "recommendation", "superseded", D3, 313, "", csC_b, scope="paragraph")
add("S91", P_CS, csC_ref % ("(c) optional pointer, end of D3:L363", E_cs2c),
    "recommendation", "superseded", D3, 363, "", csC_c, scope="sentence", anchor=A363)

# ================================================================ S91: rivals and problems, the first drafts of the entries
RE = SRC[P_RE]
CL4, CL4_MD5 = git_md5("3f7c3ab", P_CL)
F11 = "file 11"
C_LATER = {"W33.1": "C-80 superseded, C-28 applied", "W59.1": "C-81 superseded, C-29 applied",
           "W60.1": "C-34 applied", "W38.1": "C-69 superseded, C-2 applied"}
for eid in ["W33.1", "W59.1", "W60.1", "W38.1"]:
    a = entry_fields(RE, eid)
    b = entry_fields(CL4, eid)
    assert a["OLD"] == b["OLD"], eid
    if a["NEW"] == b["NEW"]:
        continue
    fl = a["FILE-11 LINE"].strip()
    line = int(fl.split("–")[0].split("-")[0])
    old = a["OLD"]
    if "\n" not in old:
        assert old in T[F11][line - 1] or old in "\n".join(T[F11]), eid
    else:
        assert old in "\n".join(T[F11]), eid
    kind_sc = {"W33.1": "sentence", "W59.1": "paragraph", "W60.1": "paragraph", "W38.1": "whole text"}[eid]
    part_x = {"W33.1": None,
              "W59.1": "Part VI — Work, support, and interference (new paragraphs \"Rivals\" and \"Problems\", before the rule that opens Part VII)",
              "W60.1": "Part VIII — Transport results (new paragraph \"A failed answer stays failed\", after \"Historical index\")",
              "W38.1": "Front matter (before Part 0) / the note of sources and departures"}[eid]
    add("S91", P_RE, "rivals working file 01 (the drafted change entries, 25 September, 01:39 UTC; log S91), entry %s (\"%s\"), FILE-11 LINE %s, OLD and NEW as first drafted; changed after the text attack (03a) and the model attack (03b) before draft 4 was committed (the note on rivals and problems, section 3); the entry's later forms: %s"
        % (eid, a["heading"].split(" — ", 1)[1], fl, C_LATER[eid]),
        "recommendation", "superseded", F11, line, old, a["NEW"], scope=kind_sc,
        old_sentence=old, new_sentence=a["NEW"], check_old=False,
        part=part_x)

RM = SRC[P_RM]
rep1 = has(P_RM, quoted_after(RM, "and not on \\(C\\) alone. For example, "))
add("S91", P_RM, "rivals working file 02 (the models), section 3, mismatch M1, \"Repair tested\" (02's repair 1), the example wording for the rivals sentence of the first-drafted W59.1; not used (the note on rivals and problems, section 3, table: \"02's repairs 1 ... and 4 ...\")",
    "recommendation", "declined", F11, 317, "", rep1, scope="span", check_old=False,
    part="Part VI — Work, support, and interference (new paragraph \"Rivals\", first-drafted W59.1)")
has(P_RM, "set aside every single commitment that does no work by itself (W33.1's test)")
add("S91", P_RM, "rivals working file 02 (the models), section 3, \"Repair tested\" (02's repair 4); not used (the note on rivals and problems, section 3, table)",
    "recommendation", "declined", F11, 317, "",
    "[no wording given] before asking whether two candidates are one account, set aside every single commitment that does no work by itself (W33.1's test); stated for single commitments",
    scope="sentence", check_old=False,
    part="Part VI — Work, support, and interference (new paragraph \"Rivals\", first-drafted W59.1)")

# ---------------------------------------------------------------- write
for r in records:
    assert list(r.keys()) == FIELDS
out = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records)
force = "--force" in sys.argv
if os.path.exists(OUT) and os.path.getsize(OUT) > 0 and not force:
    raise SystemExit("collector E.jsonl exists and is not empty; rerun with --force to rebuild this collector's own file")
open(OUT, "w", encoding="utf-8").write(out)
print(len(records), "records;", md5b(out.encode("utf-8")))
json.dump({"sources": {p: SRC_MD5[p] for p in SRC}, "change list draft 4 (git 3f7c3ab)": CL4_MD5,
           "targets": {n: TEXTS[n][1] for n in T}},
          open("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/E/build_md5s.json", "w"), indent=1)
