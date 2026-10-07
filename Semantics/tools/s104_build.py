#!/usr/bin/env python3
"""s104_build.py: build the outside reading of round 2 of the review rounds of decision S35 (log S104, the maths round
of decision S36): the briefs that put the formal core, the formal claims, the inventions register, the counterexample
search and its two checks (results/S104 Round 2 - maths/) to the two outside readers, part by part, beside the sentences
of the text under review (tests/103 The semantics, standing alone, after round 1.md, md5
f31ebb1f050783f1a84f6136cec20fcd). Written 27 September 2026 by a Claude subagent for the orchestrator, on the model of
tools/s103_build.py.

  python3 Semantics/tools/s104_build.py            build the briefs and the two job lists; refuses to overwrite a file
                                                   whose content differs; prints the table for the reading rule
  python3 Semantics/tools/s104_build.py --check    rebuild in memory and compare with the files; writes nothing
  python3 Semantics/tools/s104_build.py --measure  print each part's size; writes nothing

What each part carries (the orchestrator's list): the owner's words of decisions S20, S21, S23, S25 to S28, S33, S34
and S36 (every quoted word unchanged; connecting words outside the quotation marks that name internal records replaced
by plain descriptions, REPLACE below); the formal definitions of its group beside the sentences they formalize (whole
sections of the formal core, and single definitions from other sections that its claims use); its claims, each with
its sentences quoted, its formal statement and its search result, counterexamples in full; the inventions its claims
rest on, from the register (in full where the part is the first to use them, or a counterexample of the part rests on
them; by title elsewhere); the choices not in the register that the two checks found (U1-U6 from the check of the
program, H01-H20 from the check of the formalization against the text), each in the part it bears on; the second
check's notes on each counterexample; the sentences of its group the maths could not write (NF); the round-1 matters
and round-1 changes that fall in its group; the task (a)-(e); the report form, ending "END OF REPORT".
Withheld: the formalization check's lists of inventions the text itself fixes and of readings that change a result
(its sections 2 and 3: the readers' own questions (c) and (a)); every model name; the books; the record's readings of
the decisions; decisions on how the work is run.
Checks, by program, before anything is written: every source's md5; every `> Lnnn | ...` line of every brief against
the text under review (each fragment, " ... " joining fragments of one line, must stand in the line it names); the
owner's words against the record; the frame (everything but the owner's words and the quoted lines) for the words
decision S23 scrubs, words near them, the readers' names and internal record labels; every part at most CAP words.
"""
import hashlib, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
TESTS = os.path.join(SEM, "tests")
MATHS = "results/S104 Round 2 - maths"
OUT_DIR = os.path.join(SEM, "results", "S104 Round 2 - returns")
JOBS_MIMO = os.path.join(HERE, "s104_jobs - round 2, Mimo.json")
JOBS_GLM = os.path.join(HERE, "s104_jobs - round 2, GLM.json")
READING_RULE = "results/S104 Round 2 - how the replies will be read, written before sending.md"
CAP = 7500   # words per brief, by the runner's count (the orchestrator's "at most about 7,500")

SRC = {
    "text": ("tests/103 The semantics, standing alone, after round 1.md", "f31ebb1f050783f1a84f6136cec20fcd"),
    "text99": ("tests/99 The semantics, standing alone.md", "74f4a4c7619345747f4fa976ddac9548"),
    "decisions": ("records/Semantics - Decisions.md", "1f1f5e40a60d8cdee4761b90a4dcd2aa"),
    "core": (MATHS + "/formal core.md", "3473b6d486a51a0630e24e0bb22d837b"),
    "claims": (MATHS + "/formal claims.json", "5974c7751fa1188f575e25f36e9a133a"),
    "register": (MATHS + "/inventions register.json", "15ea664ffa2f1bae4e0eaab35adb6693"),
    "search": (MATHS + "/search results.json", "27397fac2f7150fb00df6528e2ca88a2"),
    "checkprog": (MATHS + "/check - program and counterexamples.md", "6d01517686e674e5fac95905206b7a4d"),
    "checkform": (MATHS + "/check - formalization against the text.md", "ac165ce6d01ee6bd128c11841e6a5c01"),
    "review": ("results/S103 Round 1 - reading/critical review.md", "25911e0cb0a571851421399415d1d0df"),
}


def read(rel):
    with open(os.path.join(SEM, rel), encoding="utf-8") as f:
        return f.read()


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit("s104_build: " + msg)


def wc_words(s):
    """Runs of bytes that are not ASCII whitespace (the runner's count)."""
    return len(re.findall(rb"[^ \t\n\r\v\f]+", s.encode("utf-8")))


T = {}
for k, (rel, want) in SRC.items():
    T[k] = read(rel)
    need(md5(T[k]) == want, "%s: md5 %s, expected %s" % (rel, md5(T[k]), want))
TX = T["text"].split("\n")
if TX and TX[-1] == "":
    TX = TX[:-1]
TX99 = T["text99"].split("\n")[:len(TX)]
need(len(TX) == 632, "the text under review has %d lines, expected 632" % len(TX))
CLAIMS = {c["id"]: c for c in json.loads(T["claims"])["claims"]}
NF = {n["id"]: n for n in json.loads(T["claims"])["not_formalized"]}
REG = {i["id"]: i for i in json.loads(T["register"])["inventions"]}
SR = json.loads(T["search"])
RES = {r["id"]: r for r in SR["results"]}
NOT_TESTED = {}
for n in SR["not_tested"]:
    NOT_TESTED.setdefault(n["claim"], []).append(n)
need(len(CLAIMS) == 110 and len(REG) == 102 and len(RES) == 110, "claims, register or results not whole")

# ------------------------------------------------------------------ plain substitutions in the maths material
# Where the maths files use a word decision S23 scrubs, or name an internal record, the brief gives a plain substitute.
# Every substitution is listed here and in the reading rule; none touches a quotation of the text.
SUBST = [
    (r"The program reports this and keeps it; Roles\(exclude_identity=True\) gives the other reading\.",
     "The program reports this and keeps it, and can also run the other reading."),
    (r"\bset true\b", "set to hold"), (r"\bis False\b", "fails"), (r"\bis True\b", "holds"), (r"\bTrue\b", "yes"), (r"\bFalse\b", "no"),
    (r"\bis false\b", "fails"), (r"\bfalse\b", "failing"), (r"\btrue\b", "holding"),
    (r"truth-table inconsistency", "inconsistency under every two-valued assignment"),
    (r"\bderived ports\b", "computed ports"), (r"\bderived port\b", "computed port"),
    (r"\btruth values\b", "values, each 'holds' or 'fails'"), (r"\bderivations\b", "deductions"), (r"\bderivation\b", "deduction"),
    (r"\bthe wrong edit\b", "an edit other than the one required"), (r"\brank test\b", "linear-algebra test"),
    (r"\bthe loop read in S101\b", "the loop an earlier study read"), (r"\bS101\b", "an earlier study"),
    (r"`search results\.md`", "the search-results file"), (r"`formal core\.md`", "the formal core"),
    (r"`formal claims\.md`", "the formal claims"), (r"`inventions register\.md`", "the register"),
    (r"`model/core\.py`", "the program"), (r"`model/`", "the program"),
    (r"\bthe implementer's summary\b", "the search's summary"), (r"\bThis fits\b", "This matches"),
    (r"\[computed here\]", "[computed by the check]"), (r"; see §5\.$", "."),
]
SUBST_C = [(re.compile(a), b) for a, b in SUBST]


def plain(s):
    """The substitutions, applied outside quotation lines of the text (lines beginning '> L')."""
    out = []
    for ln in s.split("\n"):
        if re.match(r"^> L\d+ \| ", ln):
            out.append(ln)
            continue
        for rx, b in SUBST_C:
            ln = rx.sub(b, ln)
        out.append(ln)
    return "\n".join(out)


# ------------------------------------------------------------------ the formal core, in sections and units
def parse_core():
    core = T["core"]
    secs = {}
    for chunk in re.split(r"(?m)^(?=## §)", core)[1:]:
        m = re.match(r"## (§\d+) (.*)", chunk)
        key, title = m.group(1), m.group(2).strip()
        blocks = [b.strip("\n") for b in re.split(r"\n\s*\n", chunk.split("\n", 1)[1]) if b.strip()]
        secs[key] = dict(title=title, blocks=blocks)
    return secs


SECS = parse_core()
DROP_BLOCK = re.compile(r"^(\*Written |\*\*Counts\.\*\*)")


def units_of(sec):
    """Definition units of a section: the quotations before a D or E block, the block, and the prose after it."""
    units, pending, cur = [], [], None
    for b in SECS[sec]["blocks"]:
        if DROP_BLOCK.match(b):
            continue
        if b.startswith("> L"):
            pending.append(b)
            cur = None
        elif re.match(r"^\*\*[DE]\d", b):
            cur = dict(id=re.match(r"^\*\*([DE][\d.]+)", b).group(1).rstrip("."), blocks=pending + [b])
            units.append(cur)
            pending = []
        elif b.startswith("**Vague.**") or b.startswith("**Where the text was vaguest") or cur is None:
            units.append(dict(id=None, blocks=pending + [b]))
            pending, cur = [], None
        else:
            cur["blocks"].append(b)
    if pending:
        units.append(dict(id=None, blocks=pending))
    return units


UNITS = {s: units_of(s) for s in SECS}
DEF_UNIT = {u["id"]: (s, u) for s in UNITS for u in UNITS[s] if u["id"]}


def section_text(sec):
    return "\n\n".join(b for u in UNITS[sec] for b in u["blocks"])


def unit_text(uid, with_quotes=True):
    s, u = DEF_UNIT[uid]
    return "\n\n".join(b for b in u["blocks"] if with_quotes or not b.startswith("> L"))


# ------------------------------------------------------------------ the owner's words
dec = T["decisions"]
KEEP = [20, 21, 23, 25, 26, 27, 28, 33, 34, 36]
OWN = {}
for n in KEEP:
    m = re.search(r"(?m)^S%d\. \[Claude's reading: .*?\] (.*)$" % n, dec)
    need(m, "decision S%d not found" % n)
    OWN[n] = m.group(1)
REPLACE = [
    (21, "Answering file 93's choices (log S93): ", "Answering choices the drafters had put to the owner: "),
    (23, "Next step after log S94, in three paragraphs: ", "Next step, in three paragraphs: "),
    (25, "Claude's report that draft 5 ties", "Claude's report that an earlier draft ties"),
    (25, " (log S95): ", ": "),
    (26, " (log S95): ", ": "),
    (33, "After reading log S101 (file 101, what the tested strong candidates depend on), in three paragraphs: ",
     "After reading a study of what seven sentences of the text depend on, in three paragraphs: "),
    (34, "Then, after log S102 (file 102, every way hard to vary has been defined and used), in two paragraphs: ",
     "Then, after reading a summary of every way hard to vary had been defined and used, in two paragraphs: "),
    (36, "During the reading of round 1 (log S103): ", "During the reading of the first review round: "),
]
OWNER_TEXT = dict(OWN)
for n, old, new in REPLACE:
    s = OWNER_TEXT[n]
    need(s.count(old) == 1, "S%d: %r occurs %d times" % (n, old, s.count(old)))
    i = s.index(old)
    need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0, "S%d: %r lies inside a quotation" % (n, old))
    OWNER_TEXT[n] = s.replace(old, new)
for n in OWN:
    b = OWNER_TEXT[n]
    for _, old, new in [r for r in REPLACE if r[0] == n]:
        b = b.replace(new, old, 1)
    need(OWN[n] == b, "S%d: the owner's words changed" % n)
    need(not re.search(r"\blog S\d|\bfile \d{2,3}\b|\bdraft \d", OWNER_TEXT[n]), "S%d still names an internal record" % n)
need("if implementation forces invention, that needs to be recorded." in OWN[36], "S36 is not whole")
DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 23: "25 September 2026", 25: "26 September 2026",
         26: "26 September 2026", 27: "26 September 2026", 28: "26 September 2026", 33: "27 September 2026",
         34: "27 September 2026", 36: "27 September 2026"}
OWNER = "\n\n".join(
    ["## 2. The owner's words",
     "The theory's owner took the decisions below, in this order; the task in section 9 is set against them. Each is "
     "quoted from the project's record of decisions. Words inside quotation marks are the owner's, word for word, "
     "typos included, except where the connecting words say that a quoted phrase is Claude's (in S26 and S28). The "
     "few connecting words outside the quotation marks are the recorder's; where the record names internal files or "
     "logs there, a plain description stands in their place. The record's own reading of each decision is not given: "
     "the owner's words decide, and where section 9 is worded differently from them, the owner's words decide there "
     "too, and you should say so. Decisions on how the work is run are left out. In these words \"Claude\" is the "
     "drafters of the text and of the maths; \"your agents\" and \"your explanation\" in S27 are addressed to them."] +
    ["**S%d** (%s). %s" % (n, DATES[n], OWNER_TEXT[n]) +
     ("\n\n*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked for: holding "
      "an explanation in a carrier (ink, a brain, a file); copying or teaching it; testing between two rival "
      "explanations, where the test changes the thing explained; building from an explanation (a perpetual-motion "
      "machine, a bridge); and performing music. The examples are the drafters' words, not the owner's, and are not "
      "a decision. S27 is the owner's reply to them." if n == 26 else "")
     for n in KEEP])

# ------------------------------------------------------------------ the two checks
CF = T["checkform"]


def h_entries():
    sec = CF.split("## 1. Hidden inventions", 1)[1].split("## 2. Inventions the text fixes", 1)[0]
    out = {}
    for chunk in re.split(r"(?m)^(?=### H\d\d )", sec)[1:]:
        m = re.match(r"### (H\d\d) · (.*)", chunk)
        body = chunk.split("\n", 1)[1]
        quotes = [ln for ln in body.split("\n") if ln.startswith("> L")]
        body = "\n".join(ln for ln in body.split("\n") if not ln.startswith("> L")).strip()
        body = re.sub(r"\n{3,}", "\n\n", body)
        out[m.group(1)] = dict(title=m.group(2).strip(), quotes=quotes, body=body)
    return out


HENT = h_entries()
need(sorted(HENT) == ["H%02d" % i for i in range(1, 21)], "the hidden inventions H01-H20 were not all read")

# The choices the check of the program found that are in no register entry (its section 4.4, and 4.2's last case).
UENT = {
    "U1": ("κ(⊥) := ⊥ in FC20", "FC20's test sets κ(⊥) := ⊥: a value map sends the undetermined answer to the "
           "undetermined answer. The part's statement says so; no register entry does, and the formal claim does not "
           "define κ at ⊥. FC20's counterexample exists only because of it.", ["FC20"]),
    "U2": ("An ill-formed λ(k) counts as a failure of (F1)", "When a port translation reads a port outside the "
           "subnetwork's ports V_N, the program scores the candidate as failing (F1). The other choice: such a tuple "
           "is no candidate at all. FC25 (b) uses it; under either choice 'E_enc meets (F1)' fails as stated.",
           ["FC25"]),
    "U3": ("'No other component constraining the answer ports', read by footprints", "FC23's premise is read by "
           "footprints: a component whose footprint misses the answer ports does not constrain them, even when its "
           "empty relation removes every valuation. The other choice: read by solutions, under which such a "
           "component does constrain them. FC23 (b)'s counterexample needs the footprint reading.", ["FC23"]),
    "U4": ("A third reading of 'the two relations stay equal' (L119)", "The register gives two readings (I93: under "
           "the bijection that witnesses the kind; under any bijection). A third: the edit leaves each of the two "
           "relations as it was at (1,b). The check searched it on 1,752 generated models meeting its premise: 82 "
           "were separated, and in every one of the 82 the pair (1,b) was not in C. So under this reading the sentence "
           "held whenever the baseline at that boundary is in the contract.", ["FC05"]),
    "U5": ("Under I102 a component can have the measurement signature for its own output port", "In a circuit where "
           "c_v copies u into v and no edit sets v, asg(v) is undefined, I102 counts v among the ports c_v does not "
           "assign, and Inv_C(c_v, Set_v) holds vacuously; so Meas(c_v, v) holds. The register records I102 but not "
           "this consequence.", ["FC07", "FC13"]),
    "U6": ("Inventions acting inside every computation of (E) and (F2) are not carried to the results",
           "The answer-slot test of NC1 (I83) runs inside every NC1, and the homomorphism test (I84) inside every "
           "(F2), yet the register ties I83 to FC23 and FC24 only and I84 to no claim. The recorded FC34 witness "
           "('a candidate can meet (E) on two questions about one target') rests on I83: its one commitment is the "
           "target's own component, which equals the answer slot wherever the answer is determined, and escapes NC1 "
           "only because one undetermined pair blocks the slot. Under I83's other choice the check found another "
           "witness, again a copy of the target (two components, each fixing the answer at one boundary). Whether the "
           "target itself counts as an explanation of the target, and under which reading of NC1, these models raise "
           "and do not settle. No status changed when the whole search was re-run with I83's, or I80's, other "
           "choice.", ["FC34", "FC23"]),
}

# The second check's notes on each counterexample (check of the program, section 2), in plain words.
CHECK = {
    "FC05": "The check re-ran it and worked it by hand: the swap of p0 and p1 carries L_c1(1,b0) to L_c0(1,b0), so "
            "c1 and c0 are of one kind on C; at (e1,b0) the two relations are equal under the identity bijection and "
            "not under the swap; on C ∪ {(e1,b0)} no one bijection serves both pairs. It rests on I93's reading (ii). "
            "FC05's own formal statement uses one bijection throughout, which is reading (i), and under reading (i) "
            "the claim held on every model tried: the counterexample is to one reading of L119, not to FC05 as "
            "written. For a third reading, see U4.",
    "FC18": "Worked by hand: D has one port p0 ∈ {0,1} and one component c0 with L_c0(1,b0) = {(1)}; E has p0 ∈ {1} "
            "and k0 with {(1)}; κ(0) = κ(1) = 1. (F1) holds; under I94 the counterpart is read untranslated, as {(1)} "
            "over {0,1}, while k0's relation is {(1)} over {1}; I10 asks equal domains, so no footprint bijection "
            "exists. The failure comes only from the two domains differing. It rests on I14's value maps, I94 and "
            "I10; under D4.4's reading the claim held on every model tried.",
    "FC20": "Worked by hand. By hand, wherever Ans_p(a,b) is determined (= y), the equation of (F2) makes the "
            "designated coordinate of Sol_E equal to {κ(y)}, so Ans_E = κ(Ans_p) for every κ, injective or not. The "
            "claim can fail only where Ans_p = ⊥ and κ merges the values Sol_D takes there. So 'only if κ is "
            "injective' is too strong: (F2) gives κ(Ans_p) wherever Ans_p is determined; where Ans_p = ⊥, E's answer "
            "is ⊥ only if κ does not merge the values Sol_D takes there. It also rests on U1 (κ(⊥) = ⊥).",
    "FC23": "Worked by hand: D has p0, p1 ∈ {0,1} and c0 on p0, with {(0)} at 1 and {(1)} at e1, so Ans_p is not "
            "constant on C; E_lk has the slot k on p0 and a background component bg on p1 with the empty relation at "
            "both pairs; Sol_E = ∅, Ans_E = ⊥ at both points, no pair gives a contrast, and NC2 fails. The model meets "
            "FC23's premise only under U3. It does not tell against L273: this lookup fails NC1 and NC2, so it still "
            "fails non-circular dependence; it bears only on FC23's 'through NC1 only'. With a satisfiable background "
            "the claim held on every model tried.",
    "FC25": "Worked by hand: D has p0, p1 ∈ {0} and one component h_p0 on p0, so p1 is in no footprint; E_enc "
            "records p1, and λ(tab) = (J_D, p1 ↦ p1); no θ can send p1 into V_{J_D} = {p0} (I14), and (F1) fails "
            "(also with two-valued domains). It also rests on U2. The substance: a port in no footprint, absent under "
            "I03, cannot be carried by any λ. On part (a): the smallest witness in the record uses [p0 = 0] where p0 "
            "is already 0, an edit that changes no relation; the check built one that does ([p0 = 1] replacing "
            "h_p0's relation, with the identity edit not counted as a setting edit), and a table on p1 alone still "
            "meets (F1): the finding against L269's 'under any contract containing one' stands without the "
            "degenerate case.",
    "FC63": "Worked by hand for (c-i): the sum component relates all 3⁶ tuples of GF(3) term values to their sum, while "
            "its counterpart projects only onto term tuples some matrix gives. The all-ones tuple is not realizable: "
            "for a 3×3 M each entry lies in exactly one even and one odd term, so t₀t₃t₄ = −t₁t₂t₅, and all ones "
            "would need 1 = −1 in GF(3). So (F1) fails for the sum component at every pair. Variant (c-ii), the sum "
            "restricted to term tuples some matrix gives, meets (E). Which of the two is 'the' Leibniz candidate is "
            "I99's choice; both need I81's computed ports, which I14 excludes, so under the formal core as written "
            "the candidate cannot be written at all.",
    "FC77": "Worked by hand: with τ([p0=0]) = 1, τ([alt]) = [alt] and τ([p0=0,alt]) = [p0=0], τ([p0=0])·τ([alt]) = "
            "[alt] ≠ τ([p0=0,alt]), so the homomorphism clause fails, and it is not relative to pairs (D5.7, I18); "
            "so Sel(t; {t}, id, ∅) fails, against 'fidelity on ∅ is vacuous'. FC77's point survives: (R) itself asks "
            "Faithful_C(t), which includes the homomorphism clause, so every t that can figure in (R) has the trivial "
            "witness Sel(t; {t}, id, ∅). Only its 'for every t' is too wide.",
    "FC78": "Worked by hand: the history is set by hand (I90); one occurrence represents t's codomain, Prepares holds, "
            "every pair of C occurs, and nothing represents t, H or the survival condition. D12.1 forbids only "
            "representations of t, H or the survival condition (L195), so Sel holds; D12.2 lets Con hold through "
            "'the organization it carries to' (L197), so Con holds too. I53's own gloss ('Sel has none') imports "
            "L201's clause, which D12.1 does not contain: the formal core is at odds with itself here. If the "
            "represented item is t itself rather than its codomain, Sel fails; everything turns on the codomain. "
            "FC81 (d) and FC82 use the same history and are one finding with FC78, not three. See H05.",
    "FC81": "One finding with FC78 (same history, with t replaced by a transport violated at (set(H=2), b1_45) ∉ H, "
            "so Sel, Viol, Surp and Con all hold). See FC78's note and H05.",
    "FC82": "One finding with FC78 (same history, t' = t). The recorded 'response' has t' = t and no violation; the "
            "check built a stronger case (population {t, t'}, μ(t) = {t'}, t violated at (set(H=2), b1_45) ∉ H, t' "
            "surviving on H with that pair added, the same history giving Con(t')): the two responses still have a "
            "common result. See H05 and H08.",
    "FC83": "Separate from FC78. Origin's three conjuncts are set to hold by hand (Attempt, New, and Build's "
            "primitives, I56); the selection response holds on the same history; nothing in D12.1, D12.8 or D13.3 "
            "ties Build's subhistory to the selection history. It shows what the definitions allow, not any physics "
            "(I52, I56, I90, I92).",
    "FC102": "Re-implemented from the register's description (six cells, reflection at the ends, cells 1..4 hidden "
             "for L steps, a window of w frames ending just before re-emergence): the same tables. One thing fails at "
             "(w, L) = (1,0), (2,1), (3,2), that is, at w = L + 1, and never once w ≥ L + 2: one visible frame gives "
             "position but not velocity. The printed two-thing example (w, L) = (1,0) fails for one thing too; "
             "(2,0) shows the missing identity (things at 0 and 1 standing still against things at 1 and 2 moving "
             "−1 give equal readings for two frames). See H17.",
}

# ------------------------------------------------------------------ round 1: the matters and the changes
REVIEW_MATTERS = {}
for m in re.finditer(r"(?m)^(\d+)\. \*\*(.*)$", T["review"].split("## Matters the checkers recorded outside", 1)[1]
                     .split("## Small points", 1)[0]):
    REVIEW_MATTERS[int(m.group(1))] = m.group(2)
need(sorted(REVIEW_MATTERS) == list(range(1, 15)), "the fourteen round-1 matters were not read")
# Each matter as the brief states it: the review's words, with the round-1 candidate numbers and ruling labels that
# say where it was noticed left out (the readers do not have them). The build checks that each keeps the line
# numbers the review gives.
MATTERS = {
    1: "(K) applied beyond components of D. Argument 1 reads (K) on τ[C], a set of E's pairs, and whether τ[C] is a "
       "contract of E in L141's sense is a question for L554–L556 and L119. L556 writes \"By (K)\" of a subnetwork "
       "λ(k), while (K) is stated for a component. The bridge is supplied at L119 and L233.",
    2: "\"event\" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere; \"occurrence\" is defined at "
       "L169; the text does not say how they are related (to be read with L596's claim).",
    3: "\"signature\" in the everyday sense at L584 (\"the signature of a selected transport meeting a change outside "
       "its history\"), beside the defined term.",
    4: "L121 names four things and gives three bullets; by L347 the rule-application bullet covers \"a rule\" and "
       "\"a constitutive status\".",
    5: "L109 gives roles \"under A\" while (K) builds a signature on a contract C.",
    6: "L151's \"prediction\" is used of a transport not said to be to the simulation layer, while L219 defines the "
       "term for transports to S only.",
    7: "L273's second sentence says an account fails non-circular dependence, where L269 and L277 use \"account\" "
       "strictly.",
    8: "L311's first sentence does not say in words that each d_n does no work by itself, which L313's \"such "
       "commitments\" needs; one step shows it.",
    9: "A premise live twice over (a leaf that is also a usable step's conclusion): withdrawing it leaves the step "
       "usable by the first disjunct of Live, so L393's \"Withdrawing a premise makes the step unusable\", read "
       "without restriction, says more than (K2) gives in that narrow configuration.",
    10: "\"complete\" in L471's first sentence must be read as (CT1)'s \"completes with o∈T[i]\" for clause 2 of (CT2) "
        "to be (CT1).",
    11: "\"operative result\", \"applicable relations\" (L375), \"deliberative\", \"structural map\" (L385) occur only "
        "there and are defined nowhere; round 1 read them as plain words.",
    12: "The two extents of \"fidelity\": L189 and L245 give (F1) and (F2); L247's heading (\"Question fidelity\") "
        "and L520 reach (A); L630 keeps \"the fidelity and the answers\" apart.",
    13: "\"contribution\" in Part VI and Part XI (L305; L435, L441), each sense fixed where it stands.",
    14: "L27 gives no pointer to Part XIV where L23 and L25 give theirs.",
}
for n, s in MATTERS.items():
    for ln in re.findall(r"L(\d+)", REVIEW_MATTERS[n]):
        if n != 12:
            need("L" + ln in s, "matter %d: line L%s of the review is not kept" % (n, ln))
R1CHANGES = {}
for ln in (123, 443, 471, 520):
    need(TX99[ln - 1] != TX[ln - 1], "line %d did not change in round 1" % ln)
    R1CHANGES[ln] = (TX99[ln - 1], TX[ln - 1])
need([i + 1 for i in range(len(TX)) if TX[i] != TX99[i]] == [123, 443, 471, 520], "round 1 changed other lines")

# the claims' round-1 field, in plain words (the round-1 candidate numbers are not given to the readers)
ROUND1_PLAIN = {
    "what the L123 change may have disturbed: the asymmetry the critical review gives between C07 and C08/C09":
        "what the round-1 change at L123 may have disturbed: round 1's reason for dropping L123's replacement clause "
        "while keeping the second clauses of L124 and L125 (an invariance clause is met vacuously by a component the "
        "contract never edits; a change clause is not)",
    "what the L123 change may have disturbed: the C07 / C08–C09 asymmetry":
        "what the round-1 change at L123 may have disturbed: the asymmetry between L123's change clause and the "
        "invariance clauses of L124 and L125",
}


def round1_line(c):
    out = []
    for s in c["round1"]:
        s = ROUND1_PLAIN.get(s, s)
        s = re.sub(r"^round-1 change (L\d+)$", r"the round-1 change at \1 (section 8)", s)
        s = re.sub(r"^matter (\d+): ", r"round-1 matter \1 (section 8): ", s)
        s = re.sub(r"^what the (L\d+) change may have disturbed: ", r"what the round-1 change at \1 may have "
                   r"disturbed: ", s)
        s = s.replace("(the C18 ruling's argument)", "(round 1's argument)")
        need(not re.search(r"\bC\d\d\b|ruling|critical review", s), "%s: round-1 field not plain: %r" % (c["id"], s))
        out.append(s)
    return "; ".join(out)


# ------------------------------------------------------------------ rendering
TYPE_PLAIN = {"definition-consequence": "follows from the definitions as written",
              "stated result": "a result the text states",
              "strong candidate": "a sentence that stood unchanged through every revision"}
SHOW_PROSE = {"counterexample found", "computed: not as claimed", "look: not as expected", "look: as expected",
              "witness found", "no witness found"}
MODEL_WORDS = 120   # a counterexample's model is printed when it is at most this long


def prose_and_model(s):
    lines = s.split("\n")
    return lines[0].strip(), "\n".join(lines[1:]).strip()


def render_part_result(p, cid):
    st = p["status"]
    lab = p["label"]
    head = "- *%s* (%s): **%s**" % (lab, p["kind"], st)
    if p.get("models_tried") and st in ("holds on all models tried", "counterexample found", "witness found",
                                        "no witness found"):
        head += " (%s models)" % format(p["models_tried"], ",")
    out = [head + "."]
    if st in SHOW_PROSE or st == "not tested":
        if p.get("statement") and st != "not tested":
            out.append("  Searched: %s" % p["statement"])
        body = p.get("counterexample") or p.get("result") or p.get("witness") or ""
        if st == "not tested":
            why = p.get("why") or "; ".join(n["why"] for n in NOT_TESTED.get(cid, []) if n["part"] in lab or
                                            lab in n["part"]) or "; ".join(n["why"] for n in NOT_TESTED.get(cid, []))
            out.append("  Why not: %s" % why)
        elif body:
            pr, model = prose_and_model(body)
            if pr:
                out.append("  " + pr)
            if model and st == "counterexample found" and len(model.split()) <= MODEL_WORDS:
                out.append("  ```\n" + "\n".join("  " + ln for ln in model.split("\n")) + "\n  ```")
            elif model and st in ("counterexample found", "computed: not as claimed"):
                out.append("  [The program's printout of the model, %d words, is not given here; the sentence above "
                           "states what it shows.]" % len(model.split()))
    return "\n".join(out)


def src_quotes(c):
    return "\n\n".join("> L%d | %s" % (s["line"], s["quote"]) for s in c["source"])


def render_claim(cid, part_claims):
    c = CLAIMS[cid]
    r = RES[cid]
    types = "; ".join(TYPE_PLAIN[t] for t in c["type"])
    head = "### %s · %s" % (cid, c["title"])
    meta = "*%s.* Inventions it uses: %s." % (types, ", ".join(c["inventions"]) or "none")
    if c["round1"]:
        meta += " Bears on %s." % round1_line(c)
    out = [head, meta, src_quotes(c), "**Formal.** " + c["formal"]]
    if c.get("look") and any(p["kind"] == "look" or p["label"].startswith("(look)") for p in r["parts"]):
        out.append("**Look** (a first reading of where a counterexample might lie, written before the search). " +
                   c["look"])
    res = ["**Result: %s.**" % r["status"]]
    if r.get("note"):
        res.append(r["note"])
    out.append(" ".join(res))
    out.append("\n".join(render_part_result(p, cid) for p in r["parts"]))
    if cid in CHECK:
        out.append("**The second check.** " + CHECK[cid])
    out.append("**Rests on:** %s." % (", ".join(r["rests_on"]) or "no invention"))
    return plain("\n\n".join(out))


def render_inv(iid, part_claims):
    i = REG[iid]
    here = [c for c in i["claims"] if c in part_claims]
    other = [c for c in i["claims"] if c not in part_claims]
    out = ["### %s · %s" % (iid, i["title"]),
           "Fills in for:\n\n" + "\n\n".join("> L%d | %s" % (q["line"], q["quote"]) for q in i["fills_in_for"]),
           "**Invented.** " + i["invented"],
           "**Other choices.** " + " ".join("(%s) %s." % (chr(97 + k), re.sub(r"^\([a-z]\) ", "", o).rstrip("."))
                                            for k, o in enumerate(i["other_choices"]))]
    used = []
    if here:
        used.append("claims of this part: " + ", ".join(here))
    if other:
        used.append("%s other claim%s" % (len(other), "" if len(other) == 1 else "s"))
    cx = [x["claim"] for x in i["results"] if x["counterexample_parts"]]
    tail = "**Used by:** " + ("; ".join(used) or "no claim") + "."
    if cx:
        tail += " Counterexamples resting on it: " + ", ".join(cx) + "."
    out.append(tail)
    return plain("\n\n".join(out))


def render_h(hid):
    h = HENT[hid]
    return plain("### %s · %s\n\n%s\n\n%s" % (hid, h["title"], "\n\n".join(h["quotes"]), h["body"]))


def render_u(uid):
    t, body, claims = UENT[uid]
    return plain("### %s · %s\n\n%s Claims: %s." % (uid, t, body, ", ".join(claims)))


def render_nf(nid):
    n = NF[nid]
    return plain("**%s** (L%d). Why it was not formalized: %s\n\n> L%d | %s" % (nid, n["line"], n["why"], n["line"],
                                                                                n["quote"]))


# ------------------------------------------------------------------ the parts
# sections: printed whole (quotations, definitions, the Vague notes); extra: single definition units of other sections
# that the part's claims use, each with the quotations before it; claims, H and U entries, matters, round-1 changes
# and NF entries as named. Inventions: in full where this is the first part whose claims use them or whose sections
# mark them, or where a counterexample of the part rests on them; by title otherwise.
PARTS = [
    dict(key="1", title="Organizations, setting edits and roles",
         where="Part II of the text on organizations and roles (L83–L110), with the pole of L325 as the claims about "
               "direction use it",
         sections=["§1", "§2"], extra=["D4.5", "D4.6", "E1"],
         claims=["FC01", "FC02", "FC11"], H=["H03", "H04"], U=[], matters=[5], r1=[], nf=[]),
    dict(key="2", title="The three families of signatures",
         where="the families of signatures in Part II of the text (L121–L127), with the roles they use (L103, L109) "
               "and the round-1 change at L123",
         sections=[], extra=["D2.1", "D2.2", "D2.4", "D4.1", "D4.5", "D4.6", "E1"],
         claims=["FC06", "FC07", "FC08", "FC09", "FC10", "FC12", "FC13", "FC14"],
         H=["H01", "H02"], U=["U5"], matters=[4], r1=[123], nf=[]),
    dict(key="3", title="Kinds, and kinds read through a transport",
         where="kinds as edit-signatures in Part II of the text (L111–L119), and Argument 1 (L552–L558) on reading "
               "them through a transport",
         sections=["§4"], extra=["D5.1", "D5.2", "D5.4"],
         claims=["FC03", "FC04", "FC05", "FC15", "FC16", "FC17", "FC18"], H=[], U=["U4"], matters=[1], r1=[],
         nf=[]),
    dict(key="4", title="Questions and contracts",
         where="Part III of the text on questions, contracts, the respect of a question and a question in error "
               "(L131–L161)",
         sections=["§3"], extra=["D6.7", "D12.6"],
         claims=["FC34", "FC35", "FC36", "FC106", "FC107"], H=[], U=["U6"], matters=[6], r1=[], nf=["NF08"]),
    dict(key="5", title="Transports, fidelity and the transport results",
         where="transports (L181–L189), component and question fidelity in Part V (L231–L253), Argument 2 "
               "(L560–L568) and the transport results of Part VIII (L351–L365)",
         sections=["§5"], extra=["D4.3", "D6.7", "E7"],
         claims=["FC19", "FC20", "FC96", "FC104", "FC64", "FC65", "FC66", "FC67"], inv=["I84"],
         H=[], U=["U1"], matters=[12], r1=[], nf=[]),
    dict(key="6", title="Account: non-circular dependence and non-vacuity",
         where="Part V of the text on non-circular dependence, non-vacuity and (E) (L255–L283), with the dependence "
               "order of Part XIV (L520–L526)",
         sections=["§6"], extra=["D5.4", "D5.5", "D5.6"],
         claims=["FC22", "FC23", "FC24", "FC30", "FC31", "FC32", "FC33", "FC108"],
         H=[], U=["U3"], matters=[7], r1=[520], nf=[]),
    dict(key="7", title="What (E) excludes: relabelings, tables, and the pole and its shadow",
         where="what (E) excludes in Part V of the text (L257, L267–L277: relabelings, tables, a contrast no edit "
               "realizes) and the pole and its shadow in Part VII (L323–L325)",
         sections=[], extra=["D2.1", "D6.3", "D6.4", "D6.6", "D6.9", "D6.10", "E1"],
         claims=["FC21", "FC25", "FC29", "FC26", "FC27", "FC28"], H=[], U=["U2"], matters=[], r1=[], nf=[]),
    dict(key="8", title="Identification, obstruction, removed structure, skew-symmetric matrices",
         where="the exact constructions of Part VII of the text (L327–L349): identification, the two balances, "
               "obstruction, explanation that removes structure, odd-order skew-symmetric matrices",
         sections=[], extra=["D6.3", "D6.4", "E2", "E3", "E4", "E5", "E6"],
         claims=["FC57", "FC58", "FC59", "FC60", "FC61", "FC62", "FC63"], H=[], U=[], matters=[], r1=[], nf=[]),
    dict(key="9", title="Routes, and active routes in a history",
         where="routes, critical blocks and boundaries in Part VI of the text (L285–L313), and occurrences, "
               "histories and active routes (L167–L169, L375)",
         sections=["§7", "§11"], extra=[],
         claims=["FC37", "FC38", "FC39", "FC40", "FC41", "FC42", "FC75", "FC105"],
         H=["H11", "H19"], U=[], matters=[2, 8, 11, 13], r1=[], nf=["NF18"]),
    dict(key="10", title="Conflict and rivals",
         where="conflict, rivals and conflict with a claim in Part VI of the text (L315)",
         sections=["§8"], extra=[],
         claims=["FC43", "FC44", "FC45", "FC52", "FC53", "FC54"], H=[], U=[], matters=[], r1=[], nf=[]),
    dict(key="11", title="Problems, tests and easy to vary",
         where="problems, tests and the text's own 'easy to vary' in Part VI of the text (L317), with Argument 2's "
               "consequence (L568)",
         sections=["§10"], extra=["D8.1", "D8.2", "D8.3", "D9.8"],
         claims=["FC46", "FC47", "FC48", "FC49", "FC50", "FC51", "FC55"], H=["H10"], U=[], matters=[], r1=[],
         nf=[]),
    dict(key="12", title="Arguments, criticism and reason use",
         where="Part IX of the text on criticism, bearing, reason use, usable arguments and what a test rules out "
               "(L377–L399), with the failed answer of Part VIII (L369)",
         sections=["§9"], extra=[],
         claims=["FC56", "FC68", "FC69", "FC70", "FC71", "FC72", "FC73", "FC74", "FC76"],
         H=["H12"], U=[], matters=[9], r1=[], nf=["NF13", "NF14"]),
    dict(key="13", title="Selection, construction and representation",
         where="the three provenances and representation in Part IV of the text (L191–L213)",
         sections=["§12"], extra=[],
         claims=["FC77", "FC78", "FC79", "FC95"], H=["H05", "H09", "H13"], U=[], matters=[], r1=[], nf=[]),
    dict(key="14", title="Prediction, violation, surprise and the two responses",
         where="prediction, violation and surprise in Part IV of the text (L215–L225), with Arguments 3 and 4 "
               "(L570–L584)",
         sections=[], extra=["D12.1", "D12.2", "D12.6", "D12.7", "D12.8", "D13.3"],
         claims=["FC80", "FC81", "FC82", "FC83"], H=["H07", "H08"], U=[], matters=[3], r1=[], nf=[]),
    dict(key="15", title="Construction, newness, origin, repair and created explanation",
         where="Part X of the text on understanding, construction, newness and origin (L401–L431) and Part XI on "
               "repair, created explanation and appraisal (L433–L457)",
         sections=["§13", "§14"], extra=[],
         claims=["FC84", "FC85", "FC86", "FC87", "FC88", "FC89", "FC90"],
         H=["H06", "H14", "H15"], U=[], matters=[], r1=[443], nf=["NF07", "NF09", "NF10", "NF19"]),
    dict(key="16", title="The physical module, recursion, universality and the class collected",
         where="Part XII of the text (L459–L483), Part XIII (L485–L511) and Part XIV (L513–L530)",
         sections=["§15", "§16"], extra=[],
         claims=["FC91", "FC92", "FC93", "FC94", "FC110"], H=["H16"], U=[], matters=[10, 14], r1=[471],
         nf=["NF11", "NF12", "NF16", "NF17"]),
    dict(key="17", title="The Arguments of Part XVI, and what would rule the class out",
         where="the Arguments of Part XVI of the text (L550–L632), Part XV (L532–L548) and the dependence order "
               "(L526)",
         sections=["§18"], extra=["D0.1", "D0.2", "E8", "E9"],
         claims=["FC97", "FC98", "FC99", "FC100", "FC101", "FC102", "FC103", "FC109"],
         H=["H17", "H18", "H20"], U=[], matters=[], r1=[],
         nf=["NF01", "NF02", "NF03", "NF04", "NF05", "NF06", "NF15"]),
]
# Where an invention's full entry goes: the part named here; else the first part that prints whole the first
# section of the formal core (other than §0) that marks it; else the first part whose claims use it or whose printed
# definitions mark it. The parts named here are the natural homes of their subject where the rule would put them
# elsewhere.
HOME_OVERRIDE = {"I26": "7", "I06": "2", "I07": "2", "I08": "2", "I09": "2", "I14": "3", "I21": "6", "I48": "13", "I50": "14",
                 "I51": "4", "I56": "13", "I65": "7", "I81": "5", "I90": "13", "I92": "7"}
_all = [c for p in PARTS for c in p["claims"]]
need(sorted(_all) == sorted(CLAIMS) and len(_all) == len(set(_all)), "the parts do not hold each claim once: %s" % (
    sorted(set(CLAIMS) - set(_all)) or sorted({c for c in _all if _all.count(c) > 1})))
need(sorted(h for p in PARTS for h in p["H"]) == sorted(HENT), "the parts do not hold each H entry once")
need(sorted(u for p in PARTS for u in p["U"]) == sorted(UENT), "the parts do not hold each U entry once")
need(sorted(m for p in PARTS for m in p["matters"]) == list(range(1, 15)), "the parts do not hold each matter once")
need(sorted(n for p in PARTS for n in p["nf"]) == sorted(NF), "the parts do not hold each NF entry once")
for p in PARTS:
    for c in p["claims"]:
        for x in CLAIMS[c]["round1"]:
            for ln in re.findall(r"\bL(123|443|471|520)\b", x):
                if int(ln) not in p["r1"]:
                    p["r1"].append(int(ln))
    p["r1"].sort()
need(sorted({r for p in PARTS for r in p["r1"]}) == [123, 443, 471, 520], "the parts do not hold each round-1 change")
for p in PARTS:
    for u in p["extra"]:
        need(u in DEF_UNIT, "part %s: no definition unit %s" % (p["key"], u))
        need(DEF_UNIT[u][0] not in p["sections"], "part %s: %s is in a section printed whole" % (p["key"], u))


def invs_used(p):
    """Inventions the part's claims use or rest on, and those its printed definitions mark, in first-use order."""
    seen = []
    for c in p["claims"]:
        for i in CLAIMS[c]["inventions"] + RES[c]["rests_on"]:
            if i not in seen:
                seen.append(i)
    for i in p.get("inv", []):
        if i not in seen:
            seen.append(i)
    printed = "\n".join(section_text(s) for s in p["sections"]) + "\n".join(unit_text(u) for u in p["extra"])
    for i in re.findall(r"\bI\d\d\d?\b", printed):
        if i in REG and i not in seen:
            seen.append(i)
    return seen


def compute_home():
    HOME.clear()
    HOME.update(HOME_OVERRIDE)
    for i, e in REG.items():
        fcs = [x for x in e["formal_core_sections"] if x != "§0"]
        for p in PARTS:
            if fcs and fcs[0] in p["sections"]:
                HOME.setdefault(i, p["key"])
                break
    for p in PARTS:
        for i in invs_used(p):
            HOME.setdefault(i, p["key"])
    for i in REG:
        need(i in HOME, "invention %s is in no part" % i)


HOME = {}
compute_home()


def full_invs(p):
    """(in full: the part is the first to use them; what was invented only: a counterexample of the part rests on
    them and another part has them in full; by title: the rest)."""
    used = invs_used(p)
    cx = set()
    for c in p["claims"]:
        for x in SR["counterexamples"]:
            if x["claim"] == c:
                cx |= set(x["rests_on"])
    key = lambda x: int(x[1:])
    full = sorted([i for i in used if HOME[i] == p["key"]], key=key)
    mid = sorted([i for i in used if i not in full and i in cx and i not in ("I77", "I78")], key=key)
    brief = sorted([i for i in used if i not in full and i not in mid], key=key)
    return full, mid, brief


CONVENTIONS = """Notation (from the maths' conventions). A condition holds or fails; ⊥ is the undetermined answer, not the value of a condition. P(X) is the set of subsets of X; ∏ the cartesian product; z|U restricts a valuation to the ports U; f[S] is the image of S; R* is the reflexive-transitive closure of a relation; ⇀ marks a partial map. D is a target, E a candidate's organization; a subscript or superscript names the organization where needed (A_E, B_E, J_E, L^E_k). A pair (a,b) is an edit a and a boundary b; x := (τ(a),σ(b)) and x0 := (1,σ(b0)). Definitions are numbered D§.n by the maths' sections (§1–§18), encodings of the text's worked cases E1–E9. **[Inn]** marks the place where an invention is used."""


def frame_intro(p, full, mid, brief):
    n = len(PARTS)
    cl = p["claims"]
    return "\n\n".join([
        "# The maths against the words, part %s of %d: %s" % (p["key"], n, p["title"]),
        "## 1. What you are asked to do",
        "**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory "
        "creativity, 632 lines, which calls itself \"the semantics\". Its owner took the decisions in section 2, and "
        "asked for \"exploring the math a bit more\" since \"words are vague\", adding: \"if implementation forces "
        "invention, that needs to be recorded\" (S36).",
        "**The maths.** The text's definitions were written as mathematics beside the sentences they formalize "
        "(D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put "
        "to a program that searched small finite models for a counterexample. Every choice the maths or the program "
        "made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that "
        "were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read "
        "the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing "
        "invented is the text's own content.** A counterexample that rests on an invention tells against that way "
        "of writing the text, and against the text only where the text fixes what the invention fills in.",
        "**This part** covers %s: the definitions in section 3; %d claims (%s) with their results in section 4; the "
        "inventions they rest on in section 5 (%d in full); the unrecorded choices in section 6; sentences the maths "
        "could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in %d "
        "parts, each read on its own." % (p["where"], len(cl), ", ".join(cl), len(full), n),
        "**Your task, in one line:** say where the maths and the words part company and which should stand; whether "
        "each counterexample tells against the text or only against an invention, and what change to the text "
        "removes it; whether the text settles each invention, and if not what it should say; and try by hand to "
        "break the claims that held (section 9; the report, section 10). Try as hard as you can, against the texts "
        "given here alone. The maths is itself a conjecture about how the text can be written; so is the text.",
        "**The search.** Every port had a finite domain; the organizations searched had at most 3 ports of 2 or 3 "
        "values, 3 or 4 components, 2 boundaries and about 12 edits, in two generated families (I77, I78), tried "
        "smallest first. Statuses: *holds on all models tried* (and nothing beyond them); *counterexample found*; "
        "*witness found* or *no witness found* (for a claim that something exists); *computed: as claimed* or *not "
        "as claimed* (on an encoding of a worked case); *holds by construction* (so written in the program, not "
        "searched); *look* (a first reading, written before the search, of where a counterexample might lie, then "
        "computed); *not tested*, with the reason. The physical module was not computed: where a claim needs "
        "histories or provenance, they were set by hand (I90).",
        "**Who is who; citing.** \"The owner\" is the theory's owner; \"Claude\" is the drafters of the text and of "
        "the maths. Line numbers are those of the whole text, title as line 1. `> Lnnn | …` quotes line nnn exactly "
        "as it stands, formulas in the text's markup; \" … \" joins fragments of one line. The maths writes in its "
        "own notation. Quote the text exactly, with line numbers; where you rely on a line not given here, say so.",
    ])


TASK = """For the definitions, claims, counterexamples and inventions of this part:

**(a) Does each formal statement say what the sentence says?** For each definition in section 3 and each claim in section 4, compare the maths with the sentence or sentences it formalizes. Where they part company, say how, and which should stand, the maths or the words, with reasons why this and not that. Where the words should change, give the new wording.

**(b) Each counterexample** (a part marked *counterexample found* or *computed: not as claimed*, and a *look* that came out *not as expected*). Is it a counterexample to the text, or only to an invention or to the claim's own wording? If it tells against the text, give the exact change to the text that removes it; or say that it shows the text saying something it should not, and what.

**(c) Each invention given in full in section 5, and each unrecorded choice in section 6.** Does the text in fact settle it? If it does, quote the words that do. If not, give the exact wording the text should carry, or say why it should stay open. A proposal that writes an invention into the text says so, naming it.

**(d) Attack the claims that held.** A claim that held on every model tried held only on those small models, under the inventions named. Try by hand to find a counterexample, to the claim or to the sentence it formalizes: under another reading, without an invention, or beyond the bounds searched. Give the model in full and say what it rests on.

**(e) The round-1 matters and changes in section 8.** For each, does the text need a change? Give the exact wording, or the reasons why none.

**Rules.**

- Give the exact wording for every proposal: the whole sentence as it would stand, between fence lines, with the line it replaces.
- Do not list, count, grade or rank rivals, and do not argue from how many there are (decision S20).
- Say nothing about what must happen to a candidate (decision S21).
- An argument here means reasons why this and not that (decision S23). A wording you propose obeys decision S23 and keeps to what the owner's words in section 2 say.
- Physical possibility enters only where information or knowledge is instantiated or transformed, and as the content of a claim a candidate can conflict with (decisions S25–S27).
- Nothing is settled, and a ruling out by a claim taken as given is a choice the person made (decision S28); nothing you find settles anything.
- Do not propose anything about what hard to vary covers: the owner has parked that question (decisions S33, S34). The text's own 'easy to vary' (L317) is not that question.
- Where values are placed is the owner's question; do not propose to move them.
- Keep apart what the text forces and what a reader might take it to mean."""

REPORT = """- Five sections, (a) to (e), in that order. In each, one entry per item you have something to say about, headed by its id and line (for example `FC05 · L119`, `I93 · L119`, `H05`, `U4`, `matter 5 · L109`), with the exact wording of each proposal between fence lines. Items on which you have nothing to add are named together in one line at the end of the section.
- Keep the whole report under about 3,000 words. Depth where an item needs it counts for more than equal space for all.
- End the report with a line that reads exactly END OF REPORT."""


def dedupe(text, seen):
    """A quotation of the text already printed in this part, word for word, is replaced by a pointer to it."""
    out = []
    for ln in text.split("\n"):
        m = re.match(r"^> L(\d+) \| (.*)$", ln)
        if m:
            k = (m.group(1), m.group(2).strip())
            if k in seen:
                out.append("*(L%s, quoted above.)*" % m.group(1))
                continue
            seen.add(k)
        out.append(ln)
    return "\n".join(out)


def build_part(p):
    full, mid, brief = full_invs(p)
    s3 = ["## 3. The definitions, beside the sentences they formalize",
          "The maths' own sections are printed whole where this part's claims live in them; single definitions from "
          "other sections follow, each with the sentences before it. Under **Vague**, the maths names what the "
          "text leaves open there.", CONVENTIONS]
    for s in p["sections"]:
        s3.append("### %s %s" % (s, SECS[s]["title"]))
        s3.append(plain(section_text(s)))
    if p["extra"]:
        s3.append("### Definitions from other sections that these claims use")
        for u in p["extra"]:
            s3.append(plain(unit_text(u)))
    s4 = ["## 4. The claims, with their search results",
          "Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, "
          "part by part; for a counterexample, what it shows and, where short, the model; then the second check's "
          "note, and every invention the result rests on (the claim's own and the program's)."]
    s4 += [render_claim(c, p["claims"]) for c in p["claims"]]
    s5 = ["## 5. The inventions these rest on",
          "In full: each invention this part is the first of the parts to use. Then, for an invention given in full "
          "in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and "
          "I78, the bounds and families of the search, are described in section 1%s." % (
              "" if "I77" in full else " and given in full in another part")]
    s5 += [render_inv(i, p["claims"]) for i in full]
    s5 += [plain("### %s · %s\n\n**Invented** (given in full in another part). %s" % (i, REG[i]["title"],
                                                                                    REG[i]["invented"])) for i in mid]
    if brief:
        s5.append("Named by title only (given in full in another part): " + "; ".join(
            "%s, %s" % (i, plain(REG[i]["title"])) for i in brief) + ".")
    s6 = ["## 6. Choices no register entry records",
          "Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the "
          "check that read the maths against the text, in its wording."]
    items6 = [render_u(u) for u in p["U"]] + [render_h(h) for h in p["H"]]
    s6 += items6 if items6 else ["None bears on this part's claims."]
    s7 = ["## 7. Sentences of this group the maths could not write"]
    s7 += [render_nf(n) for n in p["nf"]] if p["nf"] else ["None beyond those named under the claims."]
    s8 = ["## 8. Round 1: matters noted and changes made",
          "In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed "
          "four lines and recorded fourteen matters outside the sentences examined, left for later rounds."]
    for ln in p["r1"]:
        old, new = R1CHANGES[ln]
        s8.append("**The round-1 change at L%d.** Before:\n\n> L%d (before round 1) | %s\n\nAfter, as the text now "
                  "stands:\n\n> L%d | %s" % (ln, ln, old, ln, new))
    for m in p["matters"]:
        s8.append("**Round-1 matter %d.** %s" % (m, MATTERS[m]))
    if not p["r1"] and not p["matters"]:
        s8.append("None falls in this part.")
    s9 = ["## 9. The task", TASK]
    s10 = ["## 10. The report", REPORT]
    seen = set()
    s3, s4, s5, s6, s7 = ([dedupe(x, seen) for x in blk] for blk in (s3, s4, s5, s6, s7))
    body = "\n\n".join([frame_intro(p, full, mid, brief), OWNER] + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10) + "\n"
    return body, full, mid, brief


# ------------------------------------------------------------------ checks: quotations and the frame
SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bfalse\b",
         r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*",
         r"\bvalid\w*", r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*",
         r"\bgrade[sd]?\b", r"\bwrong\b", r"\bprefer\w*",
         r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bFable\b", r"\bOpus\b", r"\bDeutsch\b", r"\bMarletto\b",
         r"\bPinker\b", r"\blog S\d", r"\bS(?:9\d|1\d\d)\b", r"\bC\d\d\b", r"\bCONFIRMED\b"]
ALLOWED_IN_FRAME = ["Do not list, count, grade or rank rivals"]   # the task's rule from decision S20
DECISIONS_NAMED = {20, 21, 23, 25, 26, 27, 28, 33, 34, 36}


def frame_of(text):
    f = re.sub(r"(?m)^> L\d+( \(before round 1\))? \| .*$", "", text)
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The definitions)", "", f)
    f = re.sub(r"(?s)```.*?```", "", f)      # the program's printout of a model: names of ports and edits
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    hits = sorted({m.group(0) for pat in SCRUB for m in re.finditer(pat, f, re.I)})
    for m in re.finditer(r"\bS(\d\d)\b", f):
        if int(m.group(1)) not in DECISIONS_NAMED:
            hits.append(m.group(0))
    return hits


def check_quotes(text, key):
    n = 0
    for m in re.finditer(r"(?m)^> L(\d+)( \(before round 1\))? \| (.*)$", text):
        ln, before, q = int(m.group(1)), m.group(2), m.group(3)
        src = (TX99 if before else TX)[ln - 1]
        for frag in q.split(" … "):
            frag = frag.strip()
            need(frag and frag in src, "part %s: a quotation of L%d is not in that line: %r" % (key, ln, frag[:80]))
        n += 1
    return n


def build():
    out, rows = {}, []
    for p in PARTS:
        text, full, mid, brief = build_part(p)
        hits = scan(text)
        need(not hits, "part %s: forbidden or withheld words in the frame: %s" % (p["key"], hits))
        nq = check_quotes(text, p["key"])
        for c in p["claims"]:
            need("### %s · " % c in text, "part %s: %s has no heading" % (p["key"], c))
        for n in KEEP:
            need(OWNER_TEXT[n] in text, "part %s: S%d is not whole" % (p["key"], n))
        fname = "S104 Round 2 - the maths against the words - part %02d, %s.md" % (int(p["key"]),
                                                                                 p["title"].replace(":", " -"))
        out[os.path.join(TESTS, fname)] = text
        rows.append((p, fname, text, full, mid, brief, nq))
    jobs, glm = [], []
    for p, fname, text, full, mid, brief, nq in rows:
        note = ("S104 round 2 (decisions S35, S36), part %s (%s): %s; read under '%s', together with the other "
                "reader's reply to the same part" % (p["key"], p["title"], ", ".join(p["claims"]), READING_RULE))
        jobs.append({"tag": "s104_maths_mimo_%s" % p["key"], "provider": "mimo", "brief": os.path.join(TESTS, fname),
                     "out": OUT_DIR, "effort": "medium", "ladder": [131072, 131072], "attempts": 6,
                     "max_rejects": 3, "max_pass": 3, "note": note})
        glm.append({"tag": "s104_maths_glm_%s" % p["key"], "part": p["key"], "brief": os.path.join(TESTS, fname),
                    "brief_md5": md5(text), "note": note})
    about = ("S104 round 2 of the review rounds of decision S35, the maths round of decision S36: the formal core, "
             "formal claims, inventions register, counterexample search and its two checks (%s/), put beside the "
             "text under review (%s, md5 %s) to Mimo and to GLM in the same %d parts, each part sent whole as the one "
             "user message at medium effort (decision S17), built by tools/s104_build.py. Up to three passes "
             "(max_pass 3), a later pass only for calls with no reply returned. Read under '%s'." % (
                 MATHS, SRC["text"][0], SRC["text"][1], len(PARTS), READING_RULE))
    out[JOBS_MIMO] = json.dumps({"purpose": "audit", "about": about, "jobs": jobs}, indent=1,
                                ensure_ascii=False) + "\n"
    out[JOBS_GLM] = json.dumps({"about": about, "rule": READING_RULE, "out": os.path.relpath(OUT_DIR, SEM),
                                "effort": "medium", "max_pass": 3, "jobs": [
                                    dict(j, brief=os.path.relpath(j["brief"], SEM)) for j in glm]},
                               indent=1, ensure_ascii=False) + "\n"
    return out, rows


def report(rows, out):
    print("| part | title | claims | inventions in full | what was invented only | by title | U, H | "
          "matters, round-1 changes | NF | quotations | words (runner / `wc -w`) | md5 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for p, fname, text, full, mid, brief, nq in rows:
        print("| %s | %s | %s | %s | %s | %d | %s | %s | %s | %d | %d / %d | %s |" % (
            p["key"], p["title"], ", ".join(p["claims"]), ", ".join(full), ", ".join(mid) or "none", len(brief),
            ", ".join(p["U"] + p["H"]) or "none",
            ", ".join(["matter %d" % m for m in p["matters"]] + ["L%d" % r for r in p["r1"]]) or "none",
            ", ".join(p["nf"]) or "none", nq, len(text.split()), wc_words(text), md5(text)))
    for path in (JOBS_MIMO, JOBS_GLM):
        print("job list %s, sha256 %s" % (os.path.relpath(path, SEM), hashlib.sha256(out[path].encode()).hexdigest()))


def main():
    args = sys.argv[1:]
    if "--measure" in args:
        for p in PARTS:
            text, full, mid, brief = build_part(p)
            print("part %s: %d words (%s); claims %d, inventions in full %d, invented only %d, by title %d; scan %s" % (
                p["key"], wc_words(text), p["title"], len(p["claims"]), len(full), len(mid), len(brief), scan(text)))
        return
    check = "--check" in args
    out, rows = build()
    for p, fname, text, full, mid, brief, nq in rows:
        need(wc_words(text) <= CAP and len(text.split()) <= CAP, "part %s is over %d words (%d)" % (
            p["key"], CAP, wc_words(text)))
    bad = []
    for path, text in out.items():
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                if f.read() != text:
                    bad.append(path)
        elif check:
            bad.append(path)
    if check:
        print("check: %d files, %d differ or are missing%s" % (len(out), len(bad), (": " + "; ".join(
            os.path.basename(b) for b in bad)) if bad else ""))
        sys.exit(1 if bad else 0)
    need(not [b for b in bad if os.path.exists(b)], "refusing to overwrite files whose content differs: %s" % bad)
    for path, text in out.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    report(rows, out)


if __name__ == "__main__":
    main()
