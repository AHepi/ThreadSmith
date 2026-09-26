#!/usr/bin/env python3
"""make_blocks.py - build the six draft-4 entry blocks (W34.1, W33.1, W59.1, W60.1, W38.1, W36.1) from the
drafted entries (rivals/01 entries.md) and the repository change list, applying every FIX of the two attacks
(03a, 03b) as the orchestrator resolved them, and splice them into a copy of the change list.

Every replacement asserts that its old text occurs exactly once. Output: final/blocks/*.md and
final/cl_final.md (the change list with the six blocks; the frame is edited separately).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RIV = HERE.parent
REPO = pathlib.Path('/home/user/ThreadSmith')
CL = REPO / 'Semantics/tests/Revision 2 - change list, draft of 23 September.md'
E01 = (RIV / '01 entries.md').read_text(encoding='utf-8')
REQ = ("Drafted 25 September on the owner's position (rivals and problems); model-tested and attacked; "
       "not yet cross-examined by Atria or Mimo")


def one(text, old, new, what):
    n = text.count(old)
    if n != 1:
        sys.exit('replacement %s: old text occurs %d times' % (what, n))
    return text.replace(old, new)


def block(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


# ============================================================================================== W34.1
w34 = block(E01, '### W34.1 —', '### W33.1 —').rstrip('\n') + '\n'
w34 = one(w34, [l for l in w34.split('\n') if l.startswith('- **CHECK:**')][0] + '\n',
          "- **CHECK:** check 2, SOUND, on the text before 25 September. W34.1 was contested by neither S90 reply.\n"
          "  - **25 September:** " + REQ + ". OLD widened and NEW replaced under that position (see REASON). OLD occurs "
          "once in file 11, starts and ends on L315, and ends one space before W33.1's OLD begins, so the two do not "
          "overlap. The text attack upheld the entry in substance and corrected one REASON sentence, the N4 row and the "
          "GAIN, which had claimed that the variation family leaves the theory; it stays as the domain of (D). The model "
          "attack confirmed by grep that the new theory text has no Pres, no \"job\" and no \"Hard-to-vary\", and that the "
          "counts the REASON cites are the correction-sticks analysis's. W34.1 as edited, W33.1 as edited, W59.1, W60.1 and "
          "the companion edit to W36.1 stand or fall together under plan 1.5's cap (the group-H unit); if the unit is "
          "dropped, W34.1, W33.1 and W36.1 revert to their text of 24 September.\n", 'W34 check')
w34 = one(w34, "Its one clause that a verdict used, that standing is fixed by the candidate and the world and not by what "
               "anyone has checked (N4), is kept in W59.1, stated for questions.",
          "Its one clause that a verdict used, that standing is fixed by the candidate and the world and not by what "
          "anyone has checked (N4), is kept in W59.1, stated for questions: whether a candidate is an account of a "
          "question is fixed by the candidate, the question and the world, not by when anyone first asks the question or "
          "by whether anyone has checked the candidate against it. (The drafted \"whether or not anyone has asked the "
          "question\" was corrected: non-vacuity asks for a stated scope, which a question has only once it is posed.)",
          'W34 reach')
w34 = one(w34, '"The variation family is not a declared input": closed in substance.',
          '"The variation family is not a declared input": narrowed, not closed.', 'W34 gap')
w34 = one(w34, "No claim about a candidate or a pair of edits turns on which family is declared, and no case or other "
               "definition uses (D).",
          "No claim about a candidate or a pair of edits turns on which family is declared, and no case or other "
          "definition uses (D). It is still not among Part XIV's declared inputs (carried forward).", 'W34 gap2')
w34 = one(w34, "It stays toward through W59.1's sentence: whether a candidate is an account of a question is fixed by the "
               "candidate and the world, whether or not anyone has asked the question.",
          "It stays toward through W59.1's sentence: whether a candidate is an account of a question is fixed by the "
          "candidate, the question and the world, not by when anyone first asks the question or by whether anyone has "
          "checked the candidate against it.", 'W34 N4')
w34 = one(w34, "- **GAIN:** Part VI no longer carries a count over a family nobody declares, on jobs nobody defines. Both "
               "undefined inputs leave with it.",
          "- **GAIN:** Part VI no longer carries a count over a family nobody declares, on jobs nobody defines. \"Job\" "
          "leaves the theory. The family \\(\\mathcal V\\) stays only as the domain of (D), where no verdict turns on it, "
          "and it is still not among Part XIV's declared inputs.", 'W34 gain')

# ============================================================================================== W33.1
w33 = block(E01, '### W33.1 —', '### W59.1 —').rstrip('\n') + '\n'
w33 = one(w33, "and keeps the three on commitments that do no work, byte for byte.",
          "and keeps the three on commitments that do no work, the second now scoped to a candidate that has a support "
          "(the model attack's one fix to them); the first and third are byte for byte.", 'W33 where')
old_25 = [l for l in w33.split('\n') if l.startswith('  - **25 September:** NEW and the declaration edited')][0]
w33 = one(w33, old_25,
          "  - **25 September:** " + REQ + ". NEW and the declaration edited under that position. Two sentences are "
          "removed: file 11's \"More reach constrains variation; the containment need not be strict; counting jobs is "
          "not a warrant.\", which NEW had kept, and NEW's last sentence, \"How hard an account is to vary is a separate "
          "matter, shown by \\(\\operatorname{Pres}\\), and it grades nothing.\" The REASON WORD moves from clarification "
          "to change of claim, because a file-11 sentence is now withdrawn. The text attack upheld the entry in substance "
          "and struck O2's \"This derives L275 s2's rule.\", as check 2 had ruled. The model attack found one defect in "
          "the kept sentences: in a candidate with no support at all, every commitment passes the two-halved test "
          "vacuously, so E0's only component, the one that is wrong, would be said to \"do no work by itself\" (03b, "
          "A3 (a)). The definition is now scoped to \"a commitment \\(d\\) of a candidate that has a support\". R24's "
          "KEEP was ruled on the unscoped sentence; the scoping adds a condition and removes nothing it said of a "
          "candidate with a support. One unit with W34.1 as edited, W59.1, W60.1 and the W36.1 companion edit (see W34.1).",
          'W33 check')
old_new = ("A commitment \\(d\\) does no work by itself in the candidate when every support stays a support")
w33 = one(w33, "````text\n(E) has no condition that each commitment do work. " + old_new,
          "````text\n(E) has no condition that each commitment do work. A commitment \\(d\\) of a candidate that has a "
          "support does no work by itself in it when every support stays a support", 'W33 NEW')
w33 = one(w33, "it now says that (E) has no condition that each commitment do work; that a commitment such that every "
               "support stays a support when it is added and when it is removed does no work by itself in the candidate,",
          "it now says that (E) has no condition that each commitment do work; that a commitment of a candidate that has "
          "a support, such that every support stays a support when it is added and when it is removed, does no work by "
          "itself in the candidate,", 'W33 decl')
w33 = one(w33, "W36.1's \"how hard an account is to vary is a separate matter (Part VI)\" still lands, on W59.1's \"easy to "
               "vary\".",
          "W36.1's pointer to Part VI now lands on W59.1's \"easy to vary\". Its words \"how hard an account is to vary\" ask "
          "for a degree that Part VI no longer states, so they become \"whether an account is easy to vary\" (the "
          "companion edit to W36.1). The scoping \"of a candidate that has a support\" keeps the label off a commitment "
          "of a candidate that no subset of its commitments makes an account: there every commitment passes both halves "
          "vacuously, and calling E0's wrong component idle would misdescribe it (03b, A3 (a)). With a support, both "
          "halves say what they said before.", 'W33 reason')
w33 = one(w33, "  - O2 holds. The bell part does no work for the tide question. The candidate meets (E) with it exactly when "
               "it meets (E) without it, and without it the almanac restates the answer (L275), so it fails either way. "
               "This derives L275 s2's rule.",
          "  - O2 holds. The bell part does nothing for the tide question, and without it the almanac restates the answer "
          "(L275), so the candidate fails either way. After 25 September the candidate has no support, so the test's "
          "label does not apply to the bell; the verdict rests on L275, as before.", 'W33 O2')
w33 = one(w33, "  - **25 September.** No row rested on the two removed sentences.",
          "  - **25 September.** No row rested on the two removed sentences, or on the vacuous case the scoping removes.",
          'W33 cases')

# ============================================================================================== W59.1
W59_NEW = r"""**Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it. Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target that the adopted physics admits (Part I) and no such relations let both, as when two of their active components with one anchor have different relations there. A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\), but what its organization and transport give there can conflict with what another's give. Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, conflict at no pair (Part VIII, Recoding; Derivation 8), and nor do two candidates, however differently they are cut, that some such relations of the target would let both meet (F1), (F2) and (A) at each admitted pair both translate; neither pair is a pair of rivals. A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result that tells against a candidate tells against it only together with the background and instruments of the test that yields it. A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing a condition of (E). No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival. Nor are rivals a selection population: whether a selected transport is underdetermined at an unseen pair is fixed by its population (Derivation 3), whatever rivals anyone offers.

**Problems.** Two rivals that both fit what is established for an assessor pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that what the assessor has established has not settled. It is of one of two kinds. (i) The rivals conflict at some \((a,b)\in C\). Whatever the target does there, at most one of them is an account of \(p\), whether or not anyone can establish what it does; establishing it, the target's relations as well as its answer where their answers there agree, is a **test** that solves the problem whatever it shows, since afterwards at most one of them fits; an answer it refutes stays refuted on \(p\) (Part VIII). (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no established answer holds one of them to account without the other; a test inside \(C\) can refute one of them without the other only for a failure of its own; and where both meet (E) on \(C\) both are accounts of \(p\). A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind; the rival is then easy to vary too, and the term says nothing about which of them is right. A criticism that a candidate is easy to vary must supply such a rival (Part IX). Two rivals that are both accounts on \(C\) conflict only outside it, and a claim that one is right and the other wrong is a claim that some admitted change outside \(C\) separates them, and must supply it, as a claim that one assignment of anchors is "really" right must (Derivation 2, Consequence). A finer contract that contains a change at which two rivals conflict makes a new question (Part III), on which, offered for it, they pose a problem of the first kind while both fit; whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and V). A contract narrowed to leave out the pairs at which two rivals conflict also makes a different question; it solves nothing on \(p\), and the problem for \(p\) stands until what is established leaves at most one of them fitting. Nothing here counts rivals, grades a candidate or ranks candidates. A problem that a system represents can be a recognized difficulty (Part X), as when choosing one of two rivals meets a claimed obligation only by dropping the other, which fits as well, where keeping every rival that fits is among the protected obligations (Part XI)."""

W59_DECL = ("Part VI now defines rivals for a question: two candidates, one of which has been offered as an answer in place "
            "of the other, that conflict at some admitted pair both translate, in the contract or outside it. Two "
            "candidates conflict at a pair when their answers there differ, or when each could meet (F1), (F2) and (A) "
            "there under some relations of the target that the adopted physics admits and no such relations let both. "
            "Two candidates that differ only in how they are written, or that some such relations would let both meet "
            "those conditions at each admitted pair, are not rivals. It defines when a result is established for an "
            "assessor (a usable receipt, with (K3)'s caveat) and when a candidate fits what is established. It says that "
            "no list of all rivals is supposed, that a candidate nobody has offered is no one's rival, and that rivals "
            "are not a selection population, of which Derivation 3 speaks. It says that two rivals that "
            "both fit pose, for that assessor, a problem for the question. Where they conflict at a pair of the "
            "contract, at most one of them is an account whatever the target does there, and establishing what the "
            "target does there, its relations as well as its answer, is a test that solves the problem whatever it "
            "shows. Where they conflict only outside the contract, their answers agree on it, no established answer "
            "holds one to account without the other, a test inside it refutes one without the other only for a failure "
            "of its own, and both are accounts where both meet (E). A candidate is easy to vary when it and a rival pose "
            "a problem of that second kind; the rival is then easy to vary too, and the term says nothing about which is "
            "right. A criticism that a candidate is easy to vary must supply such a rival. Two rivals that are both "
            "accounts conflict only outside the contract, and a claim that one is right must supply an admitted change "
            "outside it that separates them; a finer contract containing a change at which they conflict is a new "
            "question, on which they pose a problem of the first kind. Whether a candidate is an account of a question "
            "is fixed by the candidate, the question and the world, not by when the question is first asked or whether "
            "anyone has checked. A contract narrowed to leave out the pairs at which two rivals conflict makes a "
            "different question and solves nothing on the original, whose problem stands until what is established "
            "leaves at most one of them fitting. Nothing here counts, grades or ranks, and a represented problem can be "
            "a recognized difficulty where keeping every rival that fits is among the protected obligations.")

W59 = r"""### W59.1 — Part VI: hard-to-vary stated through rivals and problems

- **STATUS:** applied
- **GROUP:** H
- **ITEM:** W59 (new: the owner's position of 24–25 September on hard-to-vary)
- **FILE-11 LINE:** 317–319
- **WHERE:** Part VI, after its last paragraph (L315, headed "Commitments that do no work" after W34.1) and before the rule at L317 that opens Part VII. Two paragraphs are inserted, "Rivals" and "Problems". The anchor is L317–L319 (the rule, the blank line and the Part VII heading), kept byte for byte, as W38.1 anchors on L7–L9. No other entry touches L316–L319.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** @@REQ@@. OLD occurs once in file 11 and overlaps no other OLD.
  - **The drafted wording (first form, 25 September)** defined rivals as candidates offered in place of each other that "are not one account on \(C\) in the sense of Derivation 2". Both attacks refuted that test, and it is replaced (REASON, "How the wording was reached"). The text attack (03a) ruled FIX and gave the conflict test; the model attack (03b) ruled the rivals clause REFUTED and gave a different repair, and asked for six fixes to the other sentences (the tense of "offered", the physics' quantifier, the assessor, kind (i)'s claim, the scope of the finer contract, the declared obligation). Every FIX of both is applied, the two repairs reconciled as the REASON says. Refuted and dropped: the rival test by "one account on \(C\)"; "each is offered" (present tense); "whatever the target's relations there" unrestricted; "the remedy is a finer contract" unscoped; the REASON's step "one answer at every pair, so they conflict at no pair of \(C\)"; 02's repairs 1 and 4, which 03b found insufficient.
  - **Model-tested.** The final wording was re-run (`final/f1_final_wording.py`) on every pair 02 built and every pair either attack used: 54 rows. Every claim the text makes about the kind found was checked on each row and holds. The final verdict agrees with 03b's repair on 47 of the 51 rows run under both; the four differences are recorded in REASON. It matches the expected verdict (the owner's, a case book's or an attack's) on every row but two kinds: rows whose expectation was the first form's own verdict, which the attacks refuted (02's degenerate kind (i); 02's kind (ii) for mechanism against rule, the door, and the dog against "self"); and the owner's example in the model that admits only place and half, where no change sets the mediating state and the two myths are not rivals. Once such a change is admitted they are kind (ii), as the owner expects (03a m2b; the seasons with shading).
  - One unit with W34.1 and W33.1 as edited, W60.1 and the W36.1 companion edit (see W34.1). No outside reader has seen this text.
- **OLD:**
````text
---

# Part VII — Exact constructions
````
- **NEW:**
````text
@@NEW@@

---

# Part VII — Exact constructions
````
- **DECLARATION:** @@DECL@@
- **REASON:**
  - **The owner's position (agreed in conversation, 24–25 September).** Hard-to-vary is not a count over a listed set of versions: no one can list all rivals, even in principle, and the set does not matter. A variation is a competitor, and two discovered rival explanations that both fit constitute a problem. Three refinements were agreed:
    1. Rivals must differ in what they claim, not only in wording, since a redescription is one explanation (Derivation 2).
    2. "Fit" means fit the whole question, every admitted change, tested or not. This splits problems into two kinds. Rivals that differ at some change the question covers are settled by a test there. Rivals that differ nowhere the question covers cannot be held to account by the question, and that is the mark of an easily varied explanation ("Demeter grieves" against "Persephone is underground").
    3. Deutsch's "easy to vary" judges an explanation before anyone offers a rival. On this view the criticism is the producing of the rival, and no grade or count is needed.
  - **What the theory already half-said.**
    - Revised Derivation 2's Consequence (D3:L562): two candidates with one answer profile; a claim that one is "really" right must supply a separating admitted change; "The remedy is a finer contract, which is a new question".
    - The recognized difficulty (W35; D3:L223, L423).
    - Grievance 4 (D3:L43): an exclusion is caught "by any criticism that supplies the excluded change". This is the model for "a criticism that a candidate is easy to vary must supply such a rival".
    - The error-correction analysis lists what the theory leaves open: "A choice between candidates the contract does not tell apart" (section 1, citing D3:L562).
  - **How the wording was reached.** The first form's test, "not one account on \(C\) in the sense of Derivation 2", failed both ways.
    - *Too narrow.* Kinds are judged on \(C\), so two candidates cut alike that differ only outside \(C\) were "one account" and not rivals: the good and bad rescue on the record question, the myth and its southern variant written with a place port, the tilt and the tilt patched where the Greeks never looked (02 M1(8), M2; 03b A1(3), A11). That is refinement (2)'s own kind of problem.
    - *Too wide.* A recoding, a duplicate, a coarsening, a compatible cut and an idle addition came out as kind-(ii) rivals, so "a conflict between ideas" was false of them and "the remedy is a finer contract" had no finer contract to point to (02 M3(b), M6; 03b A3 (b)–(e)).
    - *Blind to the background.* Two candidates with one active cut and one answer profile that differ in their named background conflict at every pair through (F2), and came out as one account (03b A3 (a)).
    - *Against Derivation 2.* It read the premise of Derivation 2 (ii), a sufficient condition for candidates that meet the three conditions, as a definition for candidates that need not ("Without the premise of (ii) nothing more follows", D3:L560; W19.2, LOSS).
    - Two repairs were tested. 03a: rivals conflict at some admitted pair. 03b: each claims something the other does not. On 51 rows run under both they agree on 47. They differ on the door (a spring against a slack cable, only pushes admitted: 03b rivals, the conflict test not, since the physics lets both be faithful at once) and on a myth tied to nothing against the tilt (03b not rivals, since the myth can never be faithful; the conflict test rivals of kind (ii) on the Greek question, since their answers differ in the far south). The conflict test is taken: a problem is a conflict between ideas (Deutsch p.17); two candidates that could both be faithful at once are compatible, and treating them as competitors would make a distinction that no admitted change supports do work, which Part 0 and attack (C) exclude; and answers that differ are claims that conflict, whether or not one candidate can ever be faithful.
    - From 03b the final wording also takes: the quantifier over what the adopted physics admits (A8: a splitter under a conservation law, where both rivals meet the conditions only with the law broken; over every relation the two are not even rivals, over what the physics admits they are kind (i)); "has been offered" and the narrowing sentence (A5: read as "currently offered", withdrawing both and narrowing made the problem vanish with nothing established); "at most one of them is an account of \(p\), whether or not anyone can establish what it does" (A1: a change nobody can perform); the scoping of the finer contract to one that contains a change at which they conflict (A3 (b)); and "for an assessor" (A7).
  - **Why it is stated this way.**
    - *Rivals by conflict.* The owner's "a variation is a competitor", and Deutsch's problem as a conflict between ideas (p.17), both need a conflict. "They differ in what they claim, not only in wording" (refinement (1)) is conflict at some admitted change, in \(C\) or outside it.
    - *Redescriptions and compatible candidates.* A structure-preserving bijection that takes the transport with it and leaves the answers as they are preserves (F1), (F2) and (A) pair by pair (Derivation 8), so a candidate and its rewriting conflict nowhere. Whether Part IV's port translation may carry a map of values, as such a recoding of \(E\) alone needs, is not said; it is carried forward (03b A3 (c)). The models run both forms: with the value map the recoding is no rival, and with a translation that only renames ports the recoded candidate can never be faithful, so it conflicts with nothing and is no rival either (f1). Two candidates that some admitted relations let both meet the conditions at each admitted pair conflict nowhere either, however they are cut: a fuller and a leaner account, a duplicate, an idle addition, a coarsening.
    - *Conflict.* Answers that differ cannot both meet (A), since \(\operatorname{Ans}_p(a,b)\) is one value by (Q). Otherwise each could meet the three conditions and no admitted relations let both, as with two components on one anchor with different relations, which cannot both meet (F1). A candidate that could not meet the conditions at a pair whatever the target does is excluded from the second route: its failure is its own, and it would otherwise conflict with its own relabelling (03a, r2).
    - *The physics.* Part I fixes which organizations a carrier can bear by the adopted physics, so the relations quantified over are those it admits (03b A8). The quantifier ranges over the target at one pair, not over rivals, and it is the same kind as Derivation 3's proof ("another admitted relation").
    - *Outside \(C\).* A candidate for \(p\) claims nothing outside \(C\) (D3:L43, L159), but its organization and transport give something there. Derivation 2's Consequence already speaks of "some admitted change" that separates candidates the contract does not. "That both their transports translate" keeps the definition to pairs where both give something.
    - *Established and fits*, with the assessor named, since a usable receipt is indexed to one (D3:L384). What is established is read through Part IX's usable receipts, so the semantics gains no new input.
    - *Not a population.* A differing survivor (Derivation 3) is a member of \(\mathcal T\) whether or not anyone has conjectured it. A rival is offered whether or not \(\mathcal T\) contains it. The sentence keeps O48 and D3-T from being read through rivals.
    - *Problem for \(p\).* The bold term is "problem for \(p\)", not "problem". The bare word keeps the passing sense it has at D3:L397 ("problem-directed activity") and D3:L399 ("an available problem").
  - **What each sentence rests on (checked in draft 3 and on the models).**
    - *Kind (i).* At a pair of \(C\) where they conflict, no admitted relations let both meet (F1), (F2) and (A), so whatever the target does at most one does, and at most one is an account of \(p\). Once the target's relations there (or, where the answers differ, its answer) are established, at most one fits. "An answer it refutes stays refuted on \(p\)": W60.1.
    - *Kind (ii).* At each pair of \(C\) there is no conflict, so the answers agree. Equal answers stand or fall together under (A). A relation test there refutes one of them without the other only for a failure of its own. Where both meet (E) on \(C\) both are accounts: (E) itself.
    - *Both accounts.* If both are accounts on \(C\), both meet the three conditions at every pair of \(C\) under the actual relations, which the physics admits, so they conflict at no pair of \(C\). Their rivalry lies outside \(C\), and a claim that one is right must supply that change (Derivation 2, Consequence). A finer contract containing a pair at which they conflict makes the conflict one inside the new contract, which is kind (i).
    - *Narrowing.* A contract that omits the conflict pairs is a different question (D3:L151, L159); nothing is established at the omitted pairs, so on \(p\) both still fit. This is W60.1's narrowing clause applied to a problem.
    - *Not by when the question is asked.* (E) uses neither \(O_p\) nor \(\rho_p\), and nothing in it is dated. Non-vacuity's stated scope belongs to the question whenever it is asked, so the drafted "whether or not anyone has asked the question" was false of a question nobody has posed (03a §1.5). This is W34.1's reach clause, kept and stated for questions.
    - *The recognized difficulty.* The last sentence is an instance of W35.3's second clause (D3:L423), with the obligation marked as declared (D3:L435, L516). It says "can be", as D3:L223 does for a violation.
  - **The model results** (`final/f1_output.txt`). On all 54 rows the checks hold: at every conflict pair of \(C\), whatever the physics lets the target do, at most one rival meets the three conditions, and establishing the relations there (the answer, where the answers differ) solves the problem whatever it shows; on every kind-(ii) row the answers agree on \(C\), and a finer contract with one outside conflict pair gives kind (i); where both are accounts on \(C\) they conflict nowhere in \(C\). The verdicts: the good and bad rescue are kind (i) on every kind of spring and kind (ii) on the record question; "wet spring" against "windy spring" kind (ii); the myth against its southern variant kind (ii) on both writings; grief against "sorrow", Persephone against Freyr, dog against turtle, a renamed or value-recoded candidate, a duplicate, an idle, route or unfaithful sun god, a coarsening: not rivals; D3-T's discarded design: no problem; a conjectured third design: kind (i) until the population is established.
  - **The owner's example.** "Demeter grieves" and "Persephone is underground" (as the cause, with no grief) give one answer at every pair of the Greek question.
    - With grief tied to the warmth received, a change that sets the warmth received on its own, such as a veil of dust, is physically admitted and lies outside that contract; there the grieving goddess makes the cold and Persephone's absence alone does not. So they conflict outside \(C\) and nowhere inside it: rivals of kind (ii) (03a m2b: 12 conflicting pairs, none in the Greek contract; f1).
    - Where no such change is admitted, they conflict nowhere and are not rivals. Their difference is then idle, as the difference between Persephone and Freyr is (Deutsch p.21).
    - Tied to nothing in the target, a god's component can meet (F1) nowhere; such a myth is not a rival of its own relabelling, but its answers still conflict with the tilt's in the far south.
  - **Labels do not make rivals.** Two tellings that differ only in labels, a dog or a turtle (N25), conflict at no admitted change, so they are not rivals. Deutsch reduces the Persephone and Freyr myths to one core explanation, though he says they assert incompatible things (p.21); here an incompatibility carried by no anchor and no admitted change is one of labels, and the sources note records the departure.
  - **The easy-to-vary sentence is a definition, not a grade.** It needs an offered rival, which is refinement (3). It is relative to \(p\) and to what is established. It is symmetric between the two rivals, and the text now says so. It counts nothing and ranks nothing.
  - **The correction-sticks analysis supports this form.** It found that no Pres statement can separate a good rescue from a bad one on the symmetric record (1:1, 4:4, 6:6). Only "a job holding a pair where they differ" can, and "it is (E) on that job, not a count" (§1(2); §2, limit (iii)). That job is kind (i)'s test.
- **CASES AT RISK:**
  - **O24 (the unused joint setting): toward.** The two arrangements conflict at the joint setting. It is reachable by hand, so it is physically admitted, and by non-vacuity it is in \(C\) unless a stated scope excludes it. Then the problem is kind (i), and "One reachable setting is enough" is the test that solves it. If a stated scope excludes the setting, the problem is kind (ii), and the finer question makes it kind (i). Read as selection, the case rests on Derivation 3 (W19.2, W17.3), which the new sentence keeps apart.
  - **O36 (a premise both routes use): toward on the reason; no mark moves.** "A candidate that nobody has offered is no one's rival" is O36's "a fact about a candidate nobody has written". Pres, which counted such candidates, goes (W34.1). P's criticality rests on (B) and D3:L299.
  - **O45 (the spring nobody mentioned): holds.** No candidate is offered in place of the two-spring account. A one-spring candidate offered in its place would conflict with it where the first spring is deleted: a test there if that deletion is in \(C\).
  - **O46 (the cable that used to be a spring): holds.** The cable account anchors a different subnetwork. Offered in the spring account's place, it is a rival only where an admitted change separates the two; its success is its own (D3:L307).
  - **O48 (the forbidden wire): holds; the watch is lifted.** A conjectured arrangement with the forbidden wire is at most a rival, not a member of the population, and the text now says that rivals do not make a population (Derivation 3). If the devices are established to lack the wire, the arrangement does not fit.
  - **D3-T (O76): holds.** The discarded design failed a tried setting, so it does not fit and poses no problem (02 M4; f1). "No such pair exists" is Derivation 3's fact about the population, which the new sentence keeps a conjectured design from overturning.
  - **N1 (O53): holds; toward on the reason.** An idle sun god conflicts with Tomas's account at no admitted pair, so it is not a rival even if someone offers the struck version in its place: some admitted relations let both meet the conditions at every pair (f1, M6). The same holds on the route reading. On the unfaithful reading it is not a rival either: the answers are the same, and its failure is its own, which is W33.1's interference.
  - **N2 (O54): holds (No); toward on the reason, on either writing of the myth.** Before the sailor's report, the southern variant conflicts with the myth only at the southern pairs, which lie outside the Greek question: kind (ii) (f1, M2 and S+). The report is a pair of the world question, where the two conflict: kind (i) there. The "No" rests on (E): (F1), and non-circular dependence as W20.2 words it.
  - **N3 (O55): holds on both questions.** Some of its details, those whose swap changes what the story gives at an admitted change (why grief brings cold, not which gods), give rivals of kind (ii); a swap of labels gives no rival (f1: grief against "sorrow", Persephone against Freyr). Watched: a reader may take "no rival" for name swaps as calling the myth hard to vary. The "No" rests on non-circular dependence and the "only in form" on W36.1.
  - **N4 (O56): Q1 toward** through the corrected sentence (not by when the question is first asked). Q2 rests on Deploy and Attempt, unchanged.
  - **N5 (O57): toward.** The rule's two readings conflict at the southern change, outside the home question: kind (ii) at home. The finer question makes it kind (i), and a trial in the south solves it. "The rule itself cannot tell him which reading to trust … he needs what the rule leaves out … or else trial" says the same. It agrees with W17.2's Derivation-3 reading, in which both readings are population members that survive the home history, because the two are kept apart.
  - **N7 (O59): holds; the watch is narrowed.** A leaner account that some admitted relations let meet the conditions wherever the fuller one does conflicts with it nowhere, so the two are not rivals even if offered in place of each other. Watched only if Maya's candidate gives something outside her range that conflicts with Bea's there.
  - **N17 (O67):** no pull. Answers A and B conflict nowhere.
  - **N24 (O74): holds.** Asha's weak reading and Bram's claim use different queries, so they answer different questions and are not candidates for one \(p\) (D3:L151).
  - **N25 (O75): Q1 holds; Q2 toward.** Dog and turtle conflict at no admitted change, on either anchoring (f1, M5). "As explanations they make the same empty claim … the difference between them is idle" is this.
  - **Others.** O1: its second half stays SILENT, since nothing here reads a series; for its first half see W60.1. O27: holds; "the one test that would separate them" is a kind-(i) test, and the robot's move is (K3)'s caveat. O2, O8 and O47 hold.
- **GAIN:** The theory says what hard-to-vary comes to without a count, a family or a grade. Two candidates are rivals when they conflict somewhere the physics admits a change. An easily varied candidate has a rival that fits as well and conflicts with it only where the question does not reach. A finer question is where a test can solve the problem, and the criticism is the rival. Kind (i) states the crucial test, O24's case, directly. Redescriptions, compatible accounts and idle additions are not rivals, and a narrowed question solves no problem on the old one.
- **LOSS:**
  - Two paragraphs, about @@WORDS@@ words, and seven bold terms.
  - "Easy to vary" is symmetric and relative to the question and to what an assessor has established. It gives no ground for preferring either rival. On a contract that omits an admitted change at which a candidate claims something, a variant patched there is a rival of the second kind, so any such candidate, the tilt on the Greek question included, is easy to vary there once the variant, or the myth, is offered (03b A11).
  - A candidate nobody has challenged with a rival is not called easy to vary, however loose it is (refinement (3)).
  - Variants that conflict at no admitted change, such as two myths that differ only in their gods, are not rivals at all, though Deutsch calls them incompatible (p.21).
  - A candidate with a kind-(ii) rival is still an account of its question if it meets (E). Deutsch would say it explains nothing (sources note).
  - Whether two candidates conflict outside \(C\) depends on what their transports translate there. A candidate whose transport translates nothing outside \(C\) has no kind-(ii) rival.
  - A problem ends only when what is established leaves at most one of its rivals fitting, not when a third candidate claims all that each claims. Two partial claims, each exact about a different link and both true inside \(C\), can conflict at a change outside it where both are false; the finer question's test then refutes both, and neither is right there (03b A3 (f)).
"""

W59_words = len(W59_NEW.split())
W59 = W59.replace('@@NEW@@', W59_NEW).replace('@@DECL@@', W59_DECL).replace('@@REQ@@', REQ)
W59 = W59.replace('@@WORDS@@', '{:,}'.format(round(W59_words / 10) * 10))

# ============================================================================================== W60.1
w60 = block(E01, '### W60.1 —', '**W38.1: the lines of NEW that change.**').rstrip('\n') + '\n'
W60_NEW = r"""A new index is a new claim.

**A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and the same holds on every question with the same target and query whose contract contains \((a,b)\). Once it is established for an assessor that the target's answer at \((a,b)\) is not \(y\), this is established for that assessor of every such candidate alike, from the candidate's own answer there, with no record of which candidates failed before or of how any was changed. Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the background and instruments it relies on. If a premise about them ceases to be live, the receipt is not usable and the exclusion ceases to be established, for every such candidate alike; no candidate is thereby shown to be an account (K2). A contract that omits \((a,b)\), or a changed query, makes a different question (Part III): an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index)."""
i = w60.index("- **NEW:**\n````text\n")
j = w60.index("````\n", i + len("- **NEW:**\n````text\n"))
w60 = w60[:i] + "- **NEW:**\n````text\n" + W60_NEW + "\n" + w60[j:]
old_decl = [l for l in w60.split('\n') if l.startswith('- **DECLARATION:**')][0]
w60 = one(w60, old_decl,
          "- **DECLARATION:** Part VIII now states that on a question, a candidate whose answer at a pair of the contract "
          "differs from the target's is not an account of it, nor of any question with the same target and query whose "
          "contract contains that pair, whatever candidate it is. Once the target's answer there is established for an "
          "assessor, by a usable receipt, this is established for that assessor of every such candidate alike, from its "
          "own answer there, with no record of earlier failures or changes. By (K3) the exclusion is established only "
          "together with the background and instruments of the test; if a premise about them ceases to be live, it "
          "ceases to be established for every such candidate alike, without any candidate being shown to be an account. "
          "A contract omitting the pair, or a changed query, makes a different question, an account on which does not "
          "answer the original, whose failure stands.", 'W60 decl')
old_check = [l for l in w60.split('\n') if l.startswith('- **CHECK:**')][0]
w60 = one(w60, old_check,
          "- **CHECK:** " + REQ + ". OLD occurs once in file 11. Each claim was checked against (A), D3:L151, D3:L159, "
          "D3:L363, (K2) and (K3) in draft 3 (see REASON).\n"
          "  - The text attack (03a) found it true under its hypotheses, including (K3)'s caveat, once three phrases were "
          "made exact: the assessor is named; \"alike\" is \"from the candidate's own answer there\"; what lapses under (K3) "
          "is the establishing, not the fact (K2). It also corrected the D3-T row. The model attack (03b) upheld every "
          "clause on the models (02 M1 (6); A6; A7: 67 of 67 candidates that fail only at the failed summer revive alike "
          "when the background premise is dropped, and no other candidate moves) and asked for one addition: a changed "
          "query, like a narrowed contract, makes a different question (A6 (4)). All four are applied.\n"
          "  - One unit with W34.1 and W33.1 as edited, W59.1 and the W36.1 companion edit: its \"established\" is Part "
          "VI's. No outside reader has seen this text.", 'W60 check')
w60 = one(w60, "    - For \"established\", a usable receipt (Part IX), with (K3)'s caveat. The first sentence is a fact of (A) "
               "and needs no receipt. Only its being established does.",
          "    - For \"established\", a usable receipt (Part IX), with (K3)'s caveat. The first sentence is a fact of (A) "
          "and needs no receipt. Only its being established does.\n"
          "    - \"Established\" is for one assessor. \"Alike\" means from each candidate's own answer, derived from its "
          "organization, over the same leaf.\n"
          "    - What lapses under (K3) is the establishing, not the fact: \"Withdrawing a premise removes a license; it "
          "does not make the conclusion false\" (D3:L387); \"The binding is by the world's answer, not by the recorded "
          "observation\" (correction-sticks analysis, Appendix A (b)).\n"
          "    - A changed query makes a different question as a narrowed contract does (D3:L151, L253: \"an account of a "
          "different query is not an account of this one\"). A coarser query that the same receipt settles by one more "
          "derivation step is not claimed (03b A6 (2)); it is a separate derivation over the same leaf.", 'W60 hyp')
w60 = one(w60, "Part XV's list of results open to a counterexample is left unchanged: a counterexample to this one would be "
               "a counterexample to (A).",
          "Part XV's list is left unchanged. The first sentence follows from (A) and (Q) by definition, and the rest from "
          "Part IX's receipts, (K2) and (K3), so the paragraph adds no result open to a counterexample of its own.",
          'W60 place')
old_d3t = [l for l in w60.split('\n') if l.startswith('  - **D3-T (O76): holds, and moves toward on its reason.**')][0]
w60 = one(w60, old_d3t,
          "  - **D3-T (O76): holds; not moved.** The discarded design fails at a tried setting, which the case already "
          "says. Its reason, \"No such pair exists\", is about the population (Derivation 3), which this entry does not "
          "reach.", 'W60 d3t')
old_gain = [l for l in w60.split('\n') if l.startswith('- **GAIN:**')][0]
w60 = one(w60, old_gain,
          "- **GAIN:** The theory says in one paragraph why a correction sticks on its question with no record of which "
          "candidates failed or how any was changed. It needs only a usable receipt of the target's answer at the pair, "
          "which is a record of the world, not of the candidates. It says what \"established\" requires, and why blaming "
          "the test exempts no candidate.", 'W60 gain')
W60_words = len(W60_NEW.split()) - len('A new index is a new claim.'.split())
old_loss = [l for l in w60.split('\n') if l.startswith('- **LOSS:**')][0]
w60 = one(w60, old_loss,
          "- **LOSS:** About %d words. It does not reach pairs beyond the failed one, runs of saves, or grain changes: the "
          "limits the correction-sticks analysis found (§1(1); §4, losses). The same mistake at an untested neighbouring "
          "pair stays undetected until that pair is tested (03b A6 (1)), and on another target the failed answer can be "
          "right (A6 (3)), which the text rightly does not claim." % (round(W60_words / 10) * 10), 'W60 loss')

# ============================================================================================== W38.1
w38 = block(E01, '### W38.1 — The note of sources and departures', '## 6. Verification').rstrip('\n') + '\n'
OLD_LINES = {
    'Explanation': [l for l in w38.split('\n') if l.startswith('- *Explanation.*')][0],
    'Idle': [l for l in w38.split('\n') if l.startswith('- *Idle parts.*')][0],
    'Hard': [l for l in w38.split('\n') if l.startswith('- *Hard to vary.*')][0],
    'Reach': [l for l in w38.split('\n') if l.startswith('- *Reach.*')][0],
}
NEW_LINES = {
    'Explanation': "- *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V). Part I's fallibility commitment uses \"explanation\" for an account on a contract, and whether an account is easy to vary is a separate matter (Part VI).",
    'Idle': "- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0, VI and XIV).",
    'Hard': "- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions, and so changed to make other predictions when they were needed (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); establishing what the target does at a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it only outside what the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Four departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation that could easily explain anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and a finer question is where a test can decide between the two. Here being easy to vary is relative to the question and symmetric between two rivals, and prefers neither: on the question of the seasons the Greeks knew, the axis-tilt theory, which he calls hard to vary (p.24), is easy to vary relative to the myth when the two are offered in place of each other, and relative to a variant that keeps its predictions where the Greeks looked and changes them elsewhere, which for him is no longer an explanation but a rule of thumb (pp.27–28). And variants that conflict at no admitted change, such as the Persephone and Freyr myths, which he finds assert incompatible things and yet reduce to one core explanation (p.21), are here not rivals at all (Part VI).",
    'Reach': "- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28), and an explanation already applies, when it is first thought of, where its creators never looked (p.29). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and VI).",
}
for k in OLD_LINES:
    w38 = one(w38, OLD_LINES[k] + '\n', NEW_LINES[k] + '\n', 'W38 line ' + k)
old_c = [l for l in w38.split('\n') if l.startswith('  - **25 September:** four lines of NEW changed')][0]
w38 = one(w38, old_c,
          "  - **25 September:** " + REQ + ". Five lines of NEW changed for W59.1 and the edits to W34.1, W33.1 and W36.1, "
          "and the fallback table with them. *Explanation* reads \"whether an account is easy to vary\", with W36.1's "
          "companion edit. *Idle parts* no longer says that how hard an account is to vary grades nothing, since Pres "
          "goes; it says that nothing grades a candidate for carrying a commitment that does no work (Parts 0, VI and "
          "XIV). A line *Hard to vary* is added after it. *Reach* no longer gives a definition by jobs, and cites p.29. "
          "*Surprise and problems* now names the problem for a question of Part VI and says that a problem in the wider "
          "sense \"can be\" a recognized difficulty, where it said \"is\", to agree with Part VI's \"can be\"; \"narrower\" "
          "is exact, because every problem for a question is a conflict. Every other line is byte for byte as before. The "
          "text attack (03a) had the *Hard to vary* line follow W59.1's fix and record a fourth departure (symmetry), the "
          "*Reach* line follow the corrected sentence, and the fallback table recut to the group-H unit. The model "
          "attack (03b) corrected three wording points against the pages (a pair is not a test; \"could easily explain "
          "anything\"; the two myths \"assert incompatible things\") and added the p.27 variant, which here is merged into "
          "the fourth departure. Every page cited was checked by page marker in the extracted text: pp.16, 17, 19, "
          "20–22, 24, 25, 27–28, 29 and 31. No outside reader has seen these lines.", 'W38 check')
old_r = [l for l in w38.split('\n') if l.startswith('  - **25 September: hard to vary.**')][0]
w38 = one(w38, old_r,
          "  - **25 September: hard to vary.** The owner's position of 24–25 September states hard-to-vary through rivals "
          "and problems (W59.1), and this note says so. The pages used, all in Deutsch, chapter 1: p.16, on experiment "
          "between two viable theories; p.17, on problems as conflicts; pp.20–22, on ease of variation (on p.21 the "
          "southern variant, and the Persephone and Freyr myths, which assert incompatible things yet have one core "
          "explanation; on p.22 an explanation that could easily explain anything); p.24, the axis tilt as hard to vary; "
          "p.25, rejection without experiment; pp.27–28, the variant that keeps the tilt's predictions in the known world "
          "and changes them elsewhere, which is no longer an explanation but a rule of thumb; p.29, an explanation that "
          "already applies where its creators never looked; p.31, the glossary. Each page was checked by page marker in "
          "the extracted text. The lines paraphrase; the longest run of the book's own words is the glossary's phrase "
          "\"while still accounting for what it purports to account for\" (p.31), within the 25-word limit. Four "
          "departures are recorded: judgement before a rival is offered; the name of explanation kept for an account "
          "with an easy rival; relativity and symmetry, which make the axis tilt easy to vary on the Greeks' question "
          "relative to the myth or to the p.27 variant; and variants that conflict at no admitted change, which are not "
          "rivals. The *Surprise and problems* line changes \"is\" to \"can be\" for the wider sense, since Part VI now "
          "says a represented problem for a question \"can be\" a recognized difficulty, and \"is\" would contradict it.",
          'W38 reason')
w38 = one(w38, "  - No book is quoted, so plan 1.3.6's 25-word limit is met trivially.",
          "  - No book is quoted at length: every quotation is within plan 1.3.6's 25-word limit.", 'W38 quote')
# FALLBACKS table
ti = w38.index('  | line | rests on | fallback |')
tj = w38.index('\n\n', ti) if '\n\n' in w38[ti:] else len(w38)
table = w38[ti:tj]
rows = table.split('\n')
keep = {}
for r in rows:
    keep[r.strip().strip('|').split('|')[0].strip()] = r
new_rows = [rows[0], rows[1],
            keep['Inexplicit representation (parallels)'],
            keep["Part I's substrate independence (parallels)"],
            "  | Explanation | C W36.1, and its companion edit (group H) for \"whether an account is easy to vary\" | the "
            "fallback below if W36.1 is dropped: - *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, "
            "p.19). Here that is an explanatory candidate (Part V), and Part I's fallibility commitment uses \"explanation\" "
            "for what is not in error in the dependence alleged to do the work. If only the companion edit is dropped, the "
            "line keeps \"how hard an account is to vary is a separate matter (Part VI)\". |",
            "  | Idle parts | C W33.1 (the words 'does no work by itself'); the claim itself holds on file 11 and Parts 0 "
            "and XIV | - *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). "
            "Here a commitment that does no work does not stop a candidate from being an account; Part VI reports it. |",
            "  | Hard to vary, Reach, Surprise and problems (its sentence on a problem for a question), Idle parts (\"Parts 0, "
            "VI and XIV\") | the group-H unit: W34.1 and W33.1 as edited, W59.1, W60.1 and the W36.1 companion edit | if "
            "the unit is dropped: no *Hard to vary* line, and the lines *Idle parts*, *Reach* and *Surprise and problems* "
            "revert to their text in draft 3 of this list |",
            keep['Stated limits'],
            keep['Selection'],
            keep['Surprise and problems'],
            keep['Elimination']]
w38 = w38[:ti] + '\n'.join(new_rows) + w38[tj:]
w38 = one(w38, "The authority file grows by about 720 words.",
          "The authority file grows by about 1,190 words (the note as spliced in draft 4; about 720 before 25 September).",
          'W38 loss')
w38 = w38.rstrip('\n') + '\n'

# ============================================================================================== W36.1 (from the list)
import subprocess
# the base is draft 3 of the list, as committed (HEAD), not the working copy
CLT = subprocess.run(['git', 'show', 'HEAD:Semantics/tests/Revision 2 - change list, draft of 23 September.md'], cwd=str(REPO), capture_output=True, text=True, check=True).stdout
w36_old = block(CLT, '### W36.1 —', '### W45.1 —')
w36 = w36_old
w36 = one(w36, "- **GROUP:** C\n", "- **GROUP:** C; edited 25 September (group H)\n", 'W36 group')
w36 = one(w36, "  - S90 cross-examination: s90_xexam_atria_C, point 3 (R06 STANDS, naming a move toward on N3)",
          "  - S90 cross-examination: s90_xexam_atria_C, point 3 (R06 STANDS, naming a move toward on N3)", 'W36 s90')
s90_line = [l for l in w36.split('\n') if l.startswith('  - S90 cross-examination:')][0]
w36 = one(w36, s90_line + '\n',
          s90_line + '\n' + "  - **25 September:** " + REQ + ". The companion edit to W33.1 and W59.1, required by the "
          "text attack (03a, §2.7 and §3.6): Part VI no longer states a degree of variation, so \"how hard an account is to "
          "vary\" dangled. NEW and the declaration now read \"whether an account is easy to vary is a separate matter "
          "(Part VI)\", which lands on W59.1's defined term. The REASON's \"and W33.1 says that measure grades nothing\" is "
          "replaced, and the pointer \"(L313)\" in the S90 line above is dated with it; the pointer to Part VI now lands on W59.1. R06's "
          "KEEP was ruled on the old words; the edit changes the phrase that names the separate matter and nothing else. "
          "KIND stays CLAIM, and the counts do not change. One unit with W34.1 and W33.1 as edited, W59.1 and W60.1 (see "
          "W34.1).\n", 'W36 check')
w36 = one(w36, "which ordinary usage may still call an explanation, and how hard an account is to vary is a separate matter "
               "(Part VI).\n````",
          "which ordinary usage may still call an explanation, and whether an account is easy to vary is a separate "
          "matter (Part VI).\n````", 'W36 NEW')
w36 = one(w36, "which ordinary usage may still call an explanation, and that how hard an account is to vary is a separate "
               "matter (Part VI).",
          "which ordinary usage may still call an explanation, and that whether an account is easy to vary is a separate "
          "matter (Part VI).", 'W36 decl')
w36 = one(w36, "This places the source's \"good\" without naming it and without a grade, which L27 would forbid, and W33.1 "
               "says that measure grades nothing.",
          "This places the source's \"good\" without naming it and without a grade, which L27 would forbid, and Part VI "
          "states no degree of variation (W59.1). On 25 September the phrase became \"whether an account is easy to "
          "vary\", W59.1's term, since \"how hard\" asked for a degree Part VI no longer states.", 'W36 reason')

# ============================================================================================== write
out = HERE / 'blocks'
out.mkdir(exist_ok=True)
for name, text in (('W34.1', w34), ('W33.1', w33), ('W59.1', W59), ('W60.1', w60), ('W38.1', w38), ('W36.1', w36)):
    (out / (name + '.md')).write_text(text, encoding='utf-8')

# splice into a copy of the change list
cl = CLT
def replace_block(cl, start, end, new):
    i = cl.index(start)
    j = cl.index(end, i)
    return cl[:i] + new.rstrip('\n') + '\n\n' + cl[j:]
cl = replace_block(cl, '### W36.1 —', '### W45.1 —', w36)
cl = replace_block(cl, '### W38.1 —', '### W37.1 —', w38)
cl = replace_block(cl, '### W34.1 —', '### W33.1 —', w34)
cl = replace_block(cl, '### W33.1 —', '### W40.1 —', w33 + '\n' + W59)
cl = replace_block(cl, '### W22.1 —', '### W22.1 —', w60)   # insert W60.1 before W22.1 (after W31.1)
(HERE / 'cl_final.md').write_text(cl, encoding='utf-8')
print('blocks written; W59.1 NEW words: %d; W60.1 paragraph words: %d' % (W59_words, W60_words))
print('change list with blocks: %s (%d lines)' % (HERE / 'cl_final.md', cl.count('\n')))
