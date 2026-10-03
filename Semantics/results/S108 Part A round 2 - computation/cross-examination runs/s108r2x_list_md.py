"""Writes 'S108 Part A round 2 - candidate definitions of explanation, after the cross-examination.md' from the list after round 2
(read, never written): each amendment a marked replacement ([X..] = the objection id in the settled file). Asserts every anchor.
  python3 -B s108r2x_list_md.py
"""
import hashlib

RES = "/home/user/ThreadSmith/Semantics/results/"
IN = RES + "S108 Part A round 2 - candidate definitions of explanation, after round 2.md"
OUT = RES + "S108 Part A round 2 - candidate definitions of explanation, after the cross-examination.md"
src = open(IN, encoding="utf-8").read()
md5 = hashlib.md5(src.encode("utf-8")).hexdigest()
t = src


def rep(old, new):
    global t
    assert t.count(old) == 1, ("anchor not unique or absent", old[:80])
    t = t.replace(old, new)


rep("# S108 Part A round 2 - candidate definitions of explanation, after round 2\n",
    "# S108 Part A round 2 - candidate definitions of explanation, after the cross-examination\n\n"
    "*A corrected copy of `S108 Part A round 2 - candidate definitions of explanation, after round 2.md` (md5 %s, kept as it was sent "
    "to the GLM cross-examination), amended under rule 4 of the cross-examination's reading rule for every objection that stands, each "
    "amendment marked with its objection id (settled in `S108 Part A round 2 - the GLM cross-examination, settled.md`). Built by "
    "`computation/cross-examination runs/s108r2x_list_md.py`. The map after it: `S108 Part A round 2 - the dependency map, after the "
    "cross-examination.md`. 29 September 2026, one Opus 5.5 agent (S56). Nothing applied; nothing ruled; no owner decision added.*\n\n"
    "## Original header (after round 2)\n" % md5)
rep("Status: complete, 29 September 2026, before the GLM cross-examination (S56).",
    "Status: complete, 29 September 2026, before the GLM cross-examination (S56). **After it** (this copy): the amendments are listed in §7, with the totals.")
rep("(the change as an edit or a boundary; D6.3's quantifier; whether a question's history is recorded)",
    "(the change as an edit or a boundary; D6.3's quantifier; whether a question's history is recorded; **[Xd1]** for the bridge, whether its history holds a criticized first design, with 'created' read as the program's CreateEx and the brief as the question)")
rep("recorded selected or constructed: nothing moves. The bridge: CreateEx 1 → 0 of 1,024 where its brief is declared |",
    "recorded selected or constructed: nothing moves. The bridge: CreateEx 1 → 0 of 1,024 where its brief is declared, **[Xd1]** on its history (a2) (a first design criticized), with 'created' read as CreateEx (Con and Build do not move) and p_c the brief (S108r2-1-I3); on (a1) (no criticism) CreateEx is 0 of 1,024 under every choice, so nothing moves |")
rep("and **S41 Q6** (\"Yes, it can\", read with S47) — each **on that reading**: only where the case's question is recorded as declared, or unrecorded and read as declared; with a found or worked-out question, none |",
    "and **S41 Q6** (\"Yes, it can\", read with S47) — each **on that reading**: only where the case's question is recorded as declared, or unrecorded and read as declared; with a found or worked-out question, none; **[Xd1]** S41 Q6 moreover only on the bridge's history (a2), with 'created' read as CreateEx and p_c the brief (which history the owner's case is, is the owner's: S47 writes it as an episode in which no question about the brief occurred, not one with no criticism) |")
rep("Correction O2: what V2.5 does to (Suff)'s defeat set was never computed (e2.14b) |",
    "Correction O2: what V2.5 does to (Suff)'s defeat set was never computed (e2.14b); **[rule 5 check, after the cross-examination]** now computed: on the 51 worked accounts with nothing tried, (Suff)'s defeat set (L536; L17 as S41 writes it) goes from 0 to 51 where an argument not using (E) rules the explanation out |")
rep("a fifth reading at the content (R2V4.3 (e)): 25 held relays of 3,208 chains drop (a relay inheriting a selection made where t was not held);",
    "a fifth reading at the content (R2V4.3 (e)): 25 held relays of 3,208 chains drop (a relay inheriting a selection made where t was not held), **[Xb1]** on S108r2-4-I3's reading of \"Sel at o\" (Sel's conditions staged at a holding of t); 4 with Sel read as the holding's inherited value; 0 with Sel at any holding (the reply's lemma then holds);")
rep("**S41 Q2**: the owner's question set a link \"simply declared\" against one \"found by trial or worked out\"; here a link found by trial counts as declared unless its construction is stated.",
    "**S41 Q2** (\"No, not if just declared\"; **[Xd2]** the question it answered, Claude's, set a link \"simply declared\" against one \"found by trial or worked out\"): here a link found by trial counts as declared unless its construction is stated.")
rep("a customer just asks \"why is the sign red on Mondays?\", with no story of how the question arose; on the reading that such a question counts as laid down, nothing explains the sign, the weathervane, or what your engineer's bridge creates. Where the question's story is recorded as found or worked out, nothing changes.",
    "a customer just asks \"why is the sign red on Mondays?\", with no story of how the question arose; on the reading that such a question counts as laid down, nothing explains the sign or the weathervane. Your engineer's bridge is touched only on further readings: that the work included criticizing a first design, and that \"creating\" is taken in the program's narrow sense; then nothing counts as created there. Without a criticized first design, nothing counted as created there before either, so nothing changes. Where the question's story is recorded as found or worked out, nothing changes. [Xd1]")
rep("*Seems to go against* S41 Q2, which set a link \"simply declared\" against one \"found by trial or worked out\";",
    "*Seems to go against* S41 Q2: \"No, not if just declared\" (the question you answered set a link \"simply declared\" against one \"found by trial or worked out\") [Xd2];")
rep("- **Still computed one way only**: what V2.5 does to (Suff)'s defeat set (e2.14b); C16 and C21",
    "- **[Xd1] The bridge (C2, S41 Q6)**: its move needs three readings besides the question's history: a criticized first design in its history (a2), \"created\" as the program's CreateEx, and the brief as the question. Which history the owner's case is stays the owner's.\n"
    "- **[Xb1] C13's reading (e)**: computed under all three readings of \"Sel at o\" (25 / 4 / 0 of 3,208 chains); C13 is not flagged under any.\n"
    "- **Still computed one way only**: ~~what V2.5 does to (Suff)'s defeat set (e2.14b)~~ (computed after the cross-examination: 0 → 51); C16 and C21")
t = t.rstrip("\n") + """

## 7. After the GLM cross-examination: amendments and totals

| objection | amendment |
|---|---|
| Xd1 | C2: the bridge's move named with its three further readings (history (a2), CreateEx, p_c the brief); §0's readings, §4's plain version (no claim about which history the owner meant), §5 |
| Xd2 | C16: S41 Q2 quoted with the owner's answer; the question named as Claude's |
| Xb1 | C13: reading (e)'s 25 drops qualified (25 / 4 / 0 under three readings of "Sel at o"); C13 stays unflagged |
| rule 5 (no objection) | C7: e2.14b computed (V2.5 takes (Suff)'s defeat set from 0 to 51 worked accounts on the 'nothing tried' history) |
| Xa1 | no text change: every section-2 number the list quotes (C5, C6, C7, C11, C15) was reproduced by the rerun |

Not changing the list: Xa2, Xa3, Xa4, Xb2–Xb5, Xc1–Xc5 (the map's, or errata of the section files, or not standing). Xd1's claim that the owner's bridge is history (a1) was recorded, not applied (rule 6).

**Totals after the cross-examination**: **21 candidates** (C1–C13 from round 1, C14–C21 from round 2); **11 flagged**, with the decisions they may clash with:

| candidate | decisions it may clash with | in one plain sentence |
|---|---|---|
| C1 | S44 | each part of an explanation must match what its piece does inside the whole thing |
| C2 | S44, S41 Q15, S41 Q6, each on that reading (the question's history; for the bridge also its history, "created", the brief) | a question simply laid down, not found or worked out, has no answer |
| C5 | S41 Q15, S44, on that reading (change as a boundary) | a difference counts only when it comes with a change made to the thing |
| C6 | S45; S44 on that reading (D6.3's quantifier) | something whose answer is written into one of its parts is no explanation |
| C7 | S41 Q2 (in part) | a link counts as found by trial even when nothing was tried, if nothing earlier stood for the answer |
| C8 | S41 Q2, S41 Q15, on that reading (S108-3-I2) | a worked-out link counts only if what it leaned on passes the tests |
| C11 | S45; S44 on that reading (D6.3's quantifier) | an answer written into one part passes the tests but is no explanation |
| C12 | S41 Q2 | anything that passes the tests is an explanation, even with a declared link |
| C15 | S44, S41 Q15, at that grain (Desc) | a question counts only if what it describes could be built in just one way |
| C16 | S41 Q2; S44, S41 Q15 on a selection history | a link found by trying counts as declared unless the trying says what it was built from |
| C21 | S41 Q2, on the reply's reading | a link counts as found by trial even when the answer was already written in front of the chooser |

Each flagged candidate's everyday example is in §4 (C2 and C16 as amended). Nothing applied (rule 11).
"""
open(OUT, "w", encoding="utf-8").write(t)
assert hashlib.md5(open(IN, encoding="utf-8").read().encode("utf-8")).hexdigest() == md5
print("written", OUT, len(t))
