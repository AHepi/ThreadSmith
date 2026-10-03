#!/usr/bin/env python3
"""S96 Repair: write the plan from replacements.json and the two texts.

Every change listed in the plan is read from replacements.json (the file
repair_apply.py applies), so the plan and the build cannot drift apart. The prose
sections are below. Run after repair_apply.py.
"""
import collections, hashlib, importlib.util, json, re

T = "/home/user/ThreadSmith/Semantics/tests/"
SRC = T + "Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md"
OUT = T + "Revision 2 - scrubbed copy, repaired (S96), theory text.md"
REP = T + "S96 Repair - scripts/replacements.json"
PLAN = T + "S96 Repair of the scrubbed copy - plan.md"
S95 = T + "S95 Scrub - scripts/"
PHYS = re.compile(r"\b(physic\w*|admit\w*|adopt\w*|carrier\w*|instantiat\w*|possib\w*|impossib\w*|tasks?)\b", re.I)

R = json.load(open(REP, encoding="utf-8"))
old = open(SRC, encoding="utf-8").read().split("\n")
# The plan describes stage 1, the text the two readers read (md5 c1eecbd1587e5aec91fd0ba7d46e1469);
# it rebuilds that text in memory, since OUT now holds the final text after stage 2.
_spec = importlib.util.spec_from_file_location("repair_apply", T + "S96 Repair - scripts/repair_apply.py")
_ra = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ra)
new_text = _ra.build(write=False)[2]
new = new_text.split("\n")
E = R["entries"]


def fence(s):
    return "`` " + s.replace("``", "` `") + " ``"


def entries(group):
    out = []
    for k, e in enumerate(E):
        if e["group"] != group:
            continue
        cc = " **Claim changed.**" if e.get("claim_changed") else ""
        out.append("- **l. %d** (%s).%s %s\n  - old: %s\n  - new: %s" % (
            e["line"], e["ref"], cc, e["reason"], fence(e["old"]), fence(e["new"])))
    return "\n".join(out)


# ------------------------------------------------------------------ the P table (before)
p_by_line = collections.defaultdict(list)
for e in E:
    if e["group"] == "P":
        p_by_line[e["line"]].append(e)
reasons = {int(k): v for k, v in R["physical_mentions"].items()}
rows = []
for n, line in enumerate(old, 1):
    ws = [m.group(0) for m in PHYS.finditer(line)]
    if not ws:
        continue
    if n in p_by_line:
        what = "REWRITTEN (P): " + "; ".join(e["reason"].split(".")[0] for e in p_by_line[n])
        left = PHYS.findall(new[n - 1])
        if left:
            what += ". What stays: " + reasons.get(n, "NO REASON")
    elif n == 2:
        what = "the dated note, replaced whole (l. 2)"
    else:
        what = "KEPT: " + reasons.get(n, "NO REASON")
    rows.append("| %d | %s | %s |" % (n, ", ".join(ws), what.replace("|", "/")))
P_TABLE = "| line | words in the scrubbed copy | decision |\n| --- | --- | --- |\n" + "\n".join(rows)

# ------------------------------------------------------------------ remaining mentions (after)
rem = []
tot = 0
for n, line in enumerate(new, 1):
    ws = [m.group(0) for m in PHYS.finditer(line)]
    if ws:
        tot += len(ws)
        rem.append("| %d | %s | %s |" % (n, ", ".join(ws), reasons.get(n, "NO REASON")))
REM_TABLE = "| line | words in the repaired copy | why it stays |\n| --- | --- | --- |\n" + "\n".join(rem)
phys_only = [(n, [w for w in PHYS.findall(l) if re.match(r"(physic|admitted|adopted)", w, re.I)]) for n, l in enumerate(new, 1)]
phys_only = [(n, ws) for n, ws in phys_only if ws]

# ------------------------------------------------------------------ residue scan (S95's)
spec = importlib.util.spec_from_file_location("s95", S95 + "scrub_apply.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
s95 = json.load(open(S95 + "replacements.json", encoding="utf-8"))
notes = list(s95.get("borderline", [])) + list(R.get("borderline", []))
hits, bl, res = m.scan({"borderline": notes}, new_text)
fam = dict(collections.Counter(h[3] for h in bl))
c = collections.Counter((h[1], h[2].lower()) for h in hits)
need = collections.Counter()
for b in notes:
    need[(b["line"], b["word"].lower())] += b.get("count", 1)
stale = ["l. %d %r" % (k[0], k[1]) for k, v in sorted(need.items()) if c[k] < v]

md5_new = hashlib.md5(new_text.encode("utf-8")).hexdigest()
OWNER_LIST = re.compile(r"\b(fit\w*|support\w*|verif\w*|corroborat\w*|prove[ns]?|proved|proof\w*|disprov\w*|reason to \w+|belie\w*|better|worse|true|truth\w*|establish\w*|authorit\w*|foundation\w*|deriv\w*)\b", re.I)
owner_hits = [(n, mm.group(0)) for n, l in enumerate(new, 1) for mm in OWNER_LIST.finditer(l)]
nl_wc = new_text.count("\n")
n_diff = sum(1 for a, b in zip(old, new) if a != b)
by_group = collections.Counter(e["group"] for e in E)
n_cc = sum(1 for e in E if e.get("claim_changed"))
words_old = len(open(SRC, encoding="utf-8").read().split())
words_new = len(new_text.split())

NA = "\n".join("- **%s**: %s" % (d["item"], d["reason"]) for d in R["not_applied"])

S95_MAP = """| S95 item | where | what happened here |
| --- | --- | --- |
| B1 (whole-argument rule-out undefined) | l. 8, l. 397 | applied: R1 at l. 8 (one clause added to agree with G); the results-file wording at l. 397; R_j renamed X_j |
| B2 (l. 315 and l. 369 disagree) | l. 315, l. 369 | applied: R13, R18 |
| B3 (test solves "for that assessor") | l. 317 | applied: R14 (i) and (ii) |
| B4 (l. 317 last sentence at odds with its paragraph) | l. 317 | applied: R15, widened by C with "of a candidate and a claim, whether they conflict" |
| B5 (l. 277 empty head) | l. 277 | applied: R11 |
| B6 (defeaters and Part XV (A)/(B)) | l. 17, l. 536, l. 538 | applied: the results-file wording (R2 superseded); "physically admitted contract" also removed by P |
| B7 (assessor inputs, Argument 6) | l. 393, l. 522, l. 526, l. 598 | applied, with "admits"; the optional readings of Scope_j and Live_j applied at l. 393, Live_j read for G |
| B8 (route used before defined) | l. 299, l. 307 | applied: R12 |
| B9 (faithful outside its definition) | l. 151, l. 331 | applied: R8, R16 |
| B10 (l. 159 said nothing) | l. 159 | applied: R9 |
| B11 (refused predicate against (EX)) | l. 31, l. 526, l. 600 | applied |
| B12 (stated-assumption leaves; the range 2 reader's B4) | l. 397 | reconsidered under G and F: the owner marker is dropped (S27 answers it); range 2 repair 13 superseded by the premise-that-is-the-denial wording |
| B13 (ProducedBy widened) | l. 441 | applied |
| B14 (tolerance order presumed a chain) | l. 479 | applied |
| B15 (small breaks) | l. 453, 540, 600, 620, 630 | applied |
| residue l. 47, l. 61 (R3) | l. 47, l. 61 | applied |
| residue l. 161 (R4) | l. 161 | applied |
| residue l. 211 (R5) | l. 211 | applied |
| residue: attitude words (R6) | l. 221, 223, 443 | option B applied (mark, not decide); option A is the owner's |
| borderline l. 43 (R7) | l. 43 | superseded by P |
| borderline l. 201 (R10) | l. 201 | applied |
| residue l. 335 (R17) | l. 335 | applied |
| residue l. 461 ("permitted") | l. 461 | applied ("specified") |
| residue l. 495 | l. 495 | applied, extended so that only an argument rules out |
| residue l. 518 (N indefinable) | l. 518 | applied |
| residue l. 526 ("a separate argument") | l. 526 | applied ("a separate definition") |
| residue l. 532 (heading) | l. 532 | applied |
| residue l. 542, l. 544 (reasons-FOR form) | l. 542, l. 544 | applied |
| changed claim l. 25 (R19) | l. 25 | applied |
| changed claim l. 385 | l. 385 | applied |
| changed claim l. 429 | l. 429 | applied |
| changed claim l. 568 and l. 317 (repair 22) | l. 568, l. 317 | applied at both |
| changed claim l. 592 (repair 21) | l. 592 | applied |
| optional clarity l. 305, l. 311 | l. 305, l. 311 | applied |
| optional l. 403 (repair 18) | l. 403 | not applied (see below) |
| optional l. 455 (repair 23, worth) | l. 455 | not applied: the owner's question 4 |
| watch l. 522 ("any function that orders explanations") | l. 522 | a watch, no repair proposed; unchanged |
| watch l. 526 ("defined only by its own construction") | l. 526 | a watch, no repair proposed; unchanged |
| watch l. 397 ("A record ... does not rule out", O16) | l. 397 | met: "an argument whose record leaf was made from a claim" |
| hard case 1 | l. 67, l. 317 | the owner's question 1; the relation is kept, now "fixed by the candidate, the question and its target" |"""

HEAD = """# S96 Repair of the scrubbed copy - plan

*Log S96, 26 September 2026. Agent 10 of the owner's 15 for this task (decisions S22, S24). Written by `tests/S96 Repair - scripts/plan_build.py` from `replacements.json` beside it, so every change listed here is the change the build applies. Not yet committed. Line numbers are the scrubbed copy's; the repaired copy keeps them, line for line.*

**Input.** `tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md` (log S95, md5 2517ef4ec1f274e8de2bfb7e6661ef94), unchanged. Draft 5 and the change list are unchanged.

**Output.** `tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md`, md5 %(md5)s, built by `tests/S96 Repair - scripts/repair_apply.py`, which refuses unless the input's md5 matches and refuses any span that is missing, occurs more than once on its line, or overlaps another.

**Decisions applied.** S20, S21, S23, S25, and S26 and S27 (recorded in commit da91472, 26 September 2026).

**Counts.** %(n)d entries (P %(P)d, C %(C)d, G %(G)d, F %(F)d, R %(R)d) and the dated note at l. 2 replaced whole; %(cc)d entries change what a sentence claims. %(nd)d lines differ from the scrubbed copy; both have %(nl)d lines (wc -l). Words: %(wo)d in the scrubbed copy, %(wn)d repaired. These counts describe the work; they put no order on anything (S20).

## 1. The reading, against the owner's words

The five points of the reading were compared with the owner's words (a), (b) and (d) in decisions S26 and S27. Where a point goes beyond them:

- **Point 1** (that the thing explained itself fixes whether a candidate meets the requirements, whether or not anyone knows it) is not in the owner's words. It follows from S25 ("It has nothing to do with explanation") as refined by S26, and it restates the relation of the S95 hard case 1, which is still the owner's question. The list of kinds of target in point 1 is Claude's.
- **Point 2(i)**: the owner said "This is correct" of the sentence "Physical possibility comes in only when something is instantiated or transformed", and asked for examples; the list of ways (held, copied, taught, tested, built, performed) comes from Claude's five examples, which the owner answered with footnotes "so your agents aren't led astray", not with a reading of each. **Point 2(ii)** joins "not strictly nothing" to the footnote's "'perpetual motion is impossible' is enough to trigger a conflict"; that these are the only two ways physical possibility enters is Claude's.
- **Point 3**: "responding needs more" and "creative work (Parts X-XI)" are Claude's; the owner says only that the bare claim "is not enough for a creative agent to do anything about it".
- **Point 4**: the owner says a system that must contain the whole explanation first can be designed ("nothing is stopping one") and that this is "a detail that exists outside the process". "The theory must not require it" reads that as: the process the theory describes leaves it out, and the theory does not forbid such a design either. The text says both.
- **Point 5**: the owner's example is a conflict (an explanation that implies perpetual motion), and it is about the world ("you don't have to compare your explanation directly to the world"). The files 93-94 first choice was about a failure found by examining a candidate, that it assumes its own answer. That case is not a conflict between explanations; carrying S27 over to it is Claude's step. It also follows from the owner's definition of argument (S23), which names no records.

## 2. What the repair does, in brief

- **(P)** Draft 5 and the scrubbed copy define a question's range as a subset of "the physically admitted changes" (l. 159, l. 257), fail an account whose contrast "no physically admitted edit realizes" (l. 275), and read conflict through "the relations the adopted physics admits" (l. 315, l. 526); Part XV speaks of a "physically admitted contract" (l. 536, l. 538). The repair puts **the changes the target admits** (Part II's set A of the target organization) where "physically admitted" was: those are the changes the question asks about, in whatever the target is. Conflict between candidates ranges over **relations of the target's components on their footprints**, not over relations a physics admits. Physical possibility stays where a content is instantiated in a carrier or transformed (Parts IV, X to XIII), and it comes back in as the content of claims a candidate can conflict with (C). One sentence at l. 75 says this for the whole text, and l. 461 says it for Part XII.
- **What is kept from the old "adopted physics".** For a physical target, what the target itself is and does still fixes whether a candidate meets (E) (l. 159, l. 317: "fixed by the candidate, the question and its target"). What a physics excludes still bears on two candidates: where a claim excludes every relation that would let both meet (F1), (F2) and (A), they "conflict there given" that claim (l. 315), and that argument lapses with the claim.
- **The worked example at l. 343** (odd-order skew-symmetric matrices) now comes out an account on the new wording, conjunct by conjunct: (F1), (F2) and (A) as before; non-circular dependence at the two contrasts; non-vacuity because Sol_D(1,b_0) is not empty and the target's edits outside the contract (the field arithmetic, the link between determinant and invertibility) are left out by the stated scope; and nothing asks that an edit be physical. Conflict, where a rival is offered, ranges over relations on the matrix organization's footprints, which exist for a mathematical target.
- **A melody or a philosophical claim** can be a target: l. 49 names the edits (a note or chord changed; a premise or a distinction dropped), l. 159 names the kinds of target, and l. 275 says a contrast no one could produce is still a contrast of its question when the target admits the edit.
- **(C)** At the end of the Rivals paragraph (l. 315), a new relation, **conflict with a claim**, beside conflict between rivals, which is kept as it was. A bare claim, including one about what is possible, is enough for a conflict; the conflict is found by argument, with no test; it rules the candidate out for an assessor who can use the argument (on a pair of C), and it does not say which to drop: that is the person's choice (S21), and responding is construction and repair (Parts X, XI).
- **(G)** In Part IX (l. 397), **premises taken as given**: a premise may be a claim tentatively accepted, even with no thought, by someone who holds no explanation of it; nothing in the semantics asks that the person represent the premise's explanation. The gamble is named in the owner's words and not measured. A system that must hold the whole explanation first can be designed; the semantics does not require it. Then **a premise that is the denial**: an argument whose premises include the very denial of what it would rule out rules nothing out; the person may still drop the claim, which is a choice, not a ruling out, and the claim stays not ruled out and any problem stays.
- **(F)** The text now says, at l. 8, l. 317 and l. 397, that an argument need not cite a test, and that a failure found by argument rules a candidate out for whoever can use the argument, on a question about the world as on any other.
- **(R)** Every S95 break, residue item and changed-claim repair is applied, superseded or left to the owner, item by item in section 8.

## 3. Words

The one-word-one-thing rule and the S95 vocabulary are kept. New terms: **conflict with a claim** (l. 315), **premise taken as given** and **a premise that is the denial** (l. 397), and \\(X_j(\\psi)\\) for the S95 \\(R_j(\\psi)\\), R being the repertoire. "Carrier" at l. 51 meant a relation and now says so. "World" as the thing a candidate answers to becomes "target" where it was a definition (l. 41, l. 211, l. 317), since a target need not be physical; l. 11, l. 57 and l. 608 keep "world" in passing. "Admit" keeps its S95 senses, each fixed by its subject: an organization or its target admits edits (Part II); a population admits a survivor (Argument 3); an assessor admits an inference form (Form_j, declared tentative); the semantics admits an operation (l. 608). "Physically admitted" is left only in Part XII, of constructions and variation operators. Every new sentence was run through the S95 residue scan (section 9).
"""

PSEC = """## 4. (P) The physical ties

**The scan.** A program listed every line of the scrubbed copy with physic*, admit*, adopt*, carrier*, instantiat*, possib*/impossib* or task*: 175 words on 81 lines. Most are "admitted" in the organization sense (Part II's admitted edits), which is not physical possibility. The table gives each line's decision: rewritten where physical possibility or an adopted physics defined a question, its range, non-vacuity, a conflict or Part XV's contracts; kept, with which kind, where it concerns instantiation or transformation, the content of a possibility claim, or a sense of "admit" that is not physical.

%(table)s

**The changes (P).**

%(entries)s
"""

CSEC = """## 5. (C) Conflict at the level of explanation

Placed at the end of the Rivals paragraph (l. 315), after "ruled out" and "not ruled out" are defined, since it uses them; the rivals definition is kept word for word except for the P change to its conflict clause and R13. l. 317's list of what the text says of candidates now includes it, and the dependence order (l. 526) gives it a place. What it says, in the theory's vocabulary:
- a candidate conflicts with a claim \\(\\chi\\) at a pair its transport translates when \\(\\chi\\) excludes the candidate's answer there, or every relation of the target's components under which it could meet (F1), (F2) and (A) there;
- \\(\\chi\\) need not be an explanation; a bare claim about what is possible, such as that perpetual motion is impossible, is enough for a conflict;
- the conflict is found by argument, with no test against the target;
- on a pair of \\(C\\), the argument rules out that the candidate meets (E) for any assessor who can use it (so for whom \\(\\chi\\) is live); outside \\(C\\) it rules out only what the organization gives there;
- it does not say which to drop: the candidate, \\(\\chi\\), or another premise; which one the person goes on with is the person's choice (Part 0, S21), and using \\(\\chi\\) gives \\(\\chi\\) nothing;
- it is not enough to do anything about it: a response is construction and repair (Parts X, XI), and \\(\\chi\\) alone does not say where the candidate is in error.

%(entries)s
"""

GSEC = """## 6. (G) Premises taken as given, and S95 B12 (the range 2 reader's B4) reconsidered

**Premises taken as given** (l. 397, and l. 393 for Live_j). An argument may use a claim tentatively accepted as given by someone who holds no explanation of it. (K2) asks of a premise only that it be live; Live_j is read as "j has not withdrawn d, whether or not j holds an explanation of d". The owner's "costly gamble" is quoted and not measured. A system that must hold the whole explanation first "can be designed", and "the semantics does not require it".

**B12 in this light.** S95 found that stated-assumption leaves let an assessor rule a candidate out by stating that it fails (E), which would dissolve "not ruled out", a problem for p, and S21's choice. The S95 repair ("neither does a stated assumption of the claim, or of a claim that contains it") could catch a premise taken as given, since "perpetual motion is impossible" can be read as containing the denial of a candidate that implies perpetual motion. The repair draws the line elsewhere:
- a **premise taken as given** is used through steps: the argument finds that the candidate gives what the premise excludes. It rules the candidate out for whoever can use it;
- **a premise that is the denial** (alone or joined by "and", read structurally, as non-circular dependence reads identity, not by logical equivalence alone) puts the conclusion among the premises, as "p because p" does. Such an argument rules nothing out for anyone. The same goes for an argument whose record leaf was made from the claim.

**What the theory does with the latter, without forbidding a choice.** It does not count it as ruling out. The person may still drop the claim, "for whatever reason" (Part 0): that is the person's choice (S21), not a ruling out, and the claim stays not ruled out, and a problem it poses stays a problem for that assessor (Part VI). Nothing forbids the choice; the text only declines to call it an argument.

**Arguments 1 to 10** remain arguments: their stated assumptions are hypotheses of conditional claims, and no claim's denial is among their premises.

%(entries)s
"""

FSEC = """## 7. (F) The first choice of files 93-94

The owner's footnote answers it for conflict: "you don't have to compare your explanation directly to the world". The text says so where it bears: in the definition of argument (l. 8, a pointer), in Problems (l. 317: either kind of problem can be solved with no test, by an argument that rules out that one rival meets (E) on C), and in Part IX (l. 397: an argument with no record leaf rules a candidate out for whoever can use it, "on a question about the world as on any other"). S95's provisional marker (B12) is therefore not added. The extension from conflict to a candidate that assumes its own answer is Claude's (section 1).

%(entries)s
"""

RSEC = """## 8. (R) The S95 repairs, item by item

%(map)s

**Not applied, or superseded, with the reason.**

%(na)s

**The changes (R).**

%(entries)s
"""

RES = """## 9. The build and the scans

- `python3 "tests/S96 Repair - scripts/replacements_source.py"` compares every span with the scrubbed copy and writes `replacements.json`; `python3 "tests/S96 Repair - scripts/repair_apply.py" --scan --physical` builds the repaired copy and runs both scans; this plan is written by `plan_build.py`.
- **md5** of the repaired copy: %(md5)s.
- **The S95 residue scan** (the families and `scan()` of `tests/S95 Scrub - scripts/scrub_apply.py`, imported unchanged), with S95's BORDERLINE notes and %(nb)d S96 notes: %(hits)d hits, %(bl)d noted BORDERLINE, **%(res)d unexplained**. By family: %(fam)s. The S96 notes cover a tentative "accept" (S23), "hold" as possession, and the owner's quoted "error correction". Stale S95 notes, for words the repair removed: %(stale)s.
- The owner's own list (fit, support, verif-, corroborat-, prove, proof, disprove, reason to, belief, better, worse, true, truth, establish, authority, foundation, derive, derivation) finds, by program, %(owner)s in the repaired copy.

**Every remaining physical-tie word, with why it stays** (%(tot)d words on %(nlines)d lines):

%(rem)s

**Every remaining physic*, admitted or adopted, in short:** %(short)s.
"""

OPEN = """## 10. Open points

1. **Point 1 and hard case 1.** The text keeps the assessor-free relation "a candidate meets (E) on C or fails it", now "fixed by the candidate, the question and its target". That is still the owner's question 1 of S95; S26 and S27 do not answer it.
2. **A premise that is the denial, taken as given.** If someone takes "this candidate is in error" as given, on another's say-so, the repair counts it as a choice to drop the candidate, not a ruling out, because no step leads from it to what it excludes. Whether the owner means S27's "accepted it as a given" to reach that far is open.
3. **Circularity found by examination** (a candidate that assumes its own answer) is carried over from S27's conflict case by Claude (section 1).
4. **"Only two ways in."** l. 75 and l. 461 say physical possibility enters in two ways only. The owner said "not strictly nothing" and gave the perpetual-motion claim; "only" is Claude's.
5. **Relations on footprints.** Conflict between candidates now ranges over every relation on the target's component footprints. Two candidates that only a physically excluded arrangement would let both meet the conditions no longer conflict outright; they conflict given the claim that excludes it. This is intended (S25), and it narrows outright conflict.
6. **R6 option A, worth, the critics' words, "knowledge"** (S95 questions 3 to 5) stay the owner's.
7. **Nothing here has been read by a second reader** or by Atria or Mimo; the repaired copy is an experiment, not yet a draft of file 13.
"""

vals = dict(md5=md5_new, n=len(E), P=by_group["P"], C=by_group["C"], G=by_group["G"], F=by_group["F"],
            R=by_group["R"], cc=n_cc, nd=n_diff, nl=nl_wc, wo=words_old, wn=words_new)
short = "; ".join("l. %d %s" % (n, ", ".join(ws)) for n, ws in phys_only)
doc = (HEAD % vals + "\n" + PSEC % dict(table=P_TABLE, entries=entries("P")) + "\n"
       + CSEC % dict(entries=entries("C")) + "\n" + GSEC % dict(entries=entries("G")) + "\n"
       + FSEC % dict(entries=entries("F")) + "\n"
       + RSEC % dict(map=S95_MAP, na=NA, entries=entries("R")) + "\n"
       + RES % dict(md5=md5_new, nb=len(R.get("borderline", [])), hits=len(hits), bl=len(bl), res=len(res),
                    fam=fam, stale=", ".join(stale) or "none", tot=tot, nlines=len(rem), rem=REM_TABLE,
                    short=short, owner=("nothing" if not owner_hits else "; ".join("l. %d %s" % h for h in owner_hits)))
       + "\n" + OPEN)
# ------------------------------------------------------------------ section 11: stage 2
REP2 = T + "S96 Repair - scripts/replacements_stage2.json"
R2, final_text = _ra.stage2(new_text)
final = final_text.split("\n")
md5_final = hashlib.md5(final_text.encode("utf-8")).hexdigest()
E2 = R2["entries"]
s2 = []
for e in E2:
    cc = " **Claim changed.**" if e.get("claim_changed") else ""
    s2.append("- **l. %d** (%s %s, %s).%s %s\n  - old: %s\n  - new: %s" % (
        e["line"], e["group"], e["ref"], e["how"], cc, e["reason"], fence(e["old"]), fence(e["new"])))
na2 = "\n".join("- **%s**: %s" % (d["item"], d["reason"]) for d in R2["not_applied"])
STAGE2 = """
## 11. Stage 2: the two readers' repairs

The two readings (`results/S96 Check of the repaired copy - whole text.md`, W, and `results/S96 Check of the repaired copy - cases.md`, K) read the stage-1 text described above (md5 c1eecbd1587e5aec91fd0ba7d46e1469). Their repairs are written once in `replacements_stage2_source.py`, which writes `replacements_stage2.json`; `repair_apply.py` applies them to the stage-1 text by the same rules and writes the final text. The Output line and section 8 above give the stage-1 figures; the final text's are here.

- **Final text:** `tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md`, md5 %(md5)s.
- **Stage 2:** %(n)d entries (W %(w)d, K %(k)d, the dated note %(nn)d); %(cc)d change what a sentence claims; %(nd)d lines differ from the stage-1 text, %(nd0)d from the scrubbed copy; 632 lines, none added or removed. Words: %(wn)d.
- **Not applied or not text:** %(nna)d items, below.

### Applied

%(entries)s

### Not applied, or no text proposed

%(na)s
""" % dict(md5=md5_final, n=len(E2), w=sum(1 for e in E2 if e["group"] == "W"),
           k=sum(1 for e in E2 if e["group"] == "K"), nn=sum(1 for e in E2 if e["group"] == "N"),
           cc=sum(1 for e in E2 if e.get("claim_changed")),
           nd=sum(1 for a, b in zip(new, final) if a != b), nd0=sum(1 for a, b in zip(old, final) if a != b),
           wn=len(final_text.split()), nna=len(R2["not_applied"]), entries="\n".join(s2), na=na2)
doc = doc + STAGE2
open(PLAN, "w", encoding="utf-8").write(doc)
print("plan written:", PLAN, len(doc.split()), "words; unexplained residue:", len(res))
