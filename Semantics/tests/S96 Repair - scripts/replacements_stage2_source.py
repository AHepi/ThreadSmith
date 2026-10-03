#!/usr/bin/env python3
"""S96 Repair, stage 2: the two readers' repairs to the repaired copy, written once, here.

The two readers read the stage-1 text (md5 c1eecbd1587e5aec91fd0ba7d46e1469):
  W = results/S96 Check of the repaired copy - whole text.md (items R-, P-, B-, O-)
  K = results/S96 Check of the repaired copy - cases.md (items named by case)
Each entry names a line of the stage-1 text (the line numbers are the scrubbed copy's,
the stage-1 text's and the final text's alike), an exact old span on it, a new span, the
reading it comes from (W or K), the reader's item, whether it is applied as worded or
adapted, and a reason. Repairs not applied are listed with the reason. Running this file
rebuilds the stage-1 text in memory (repair_apply.build), compares every old span with it
(present once on its line) and writes replacements_stage2.json beside it.
"""
import hashlib, importlib.util, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE1_MD5 = "c1eecbd1587e5aec91fd0ba7d46e1469"

E = []


def add(line, group, ref, how, old, new, reason, claim_changed=False):
    E.append(dict(line=line, group=group, ref=ref, how=how, old=old, new=new, reason=reason,
                  category=group, claim_changed=claim_changed))


# ------------------------------------------------------------------ l. 2, the dated note
add(2, "N", "the dated note", "Claude's",
    r"with the S96 repairs applied, made by program (`tests/S96 Repair - scripts/repair_apply.py`, from "
    r"`replacements.json` beside it),",
    r"with the S96 repairs applied in two stages, the second after two readings of the first "
    r"(`results/S96 Check of the repaired copy - whole text.md` and `- cases.md`), made by program "
    r"(`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` "
    r"beside it),",
    "The note says how the text was made; it now names the second stage and the two readings.")

# ------------------------------------------------------------------ l. 8
add(8, "W", "R-6", "adapted",
    r"and the claim's denial is not one of its premises (Part IX).",
    r"and the claim's denial is not among its premises, in the structural sense of Part IX.",
    "l. 8 and l. 397 said the denial block two ways; l. 8 now points to l. 397's structural reading. "
    "Worded without the reader's doubled '(Part IX)'.")

# ------------------------------------------------------------------ l. 49
add(49, "W", "B-5", "as worded",
    r"not on whether a candidate meets (E) at it.",
    r"not on whether a candidate meets (F1), (F2) and (A) there, or (E) on a contract that contains it.",
    "(E) is defined on a contract, not at an edit.")

# ------------------------------------------------------------------ l. 55
add(55, "W", "R-3", "as worded",
    r"Argument 7 rules out a conflict between them.",
    r"Argument 7 rules out a conflict between them, for whoever can use it.",
    "Ruling out is always for someone who can use the argument (l. 8, S23).")

# ------------------------------------------------------------------ l. 75
add(75, "W", "P-2", "adapted",
    r"as a candidate can conflict with a claim (Part VI).",
    r"as a candidate can conflict with a claim (Part VI). That an organization admits an edit is not a claim "
    r"that the edit can be carried out or can come about, so an attribution does not conflict with a physics "
    r"that excludes carrying out an edit the attributed organization admits (Parts II and III).",
    "Without this, an attribution to the Earth and Sun whose organization admits 'axis upright' would conflict "
    "with physics, and physical possibility would bound a physical target's range again, through the attribution "
    "(S25). The reader's '(Part III)' widened to Parts II and III: admitted edits are Part II's, contracts Part III's.",
    claim_changed=True)
add(75, "W", "O-1", "as worded",
    r"Physical possibility enters the semantics in two ways only: where a content is instantiated in a carrier "
    r"or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), "
    r"and as the content of claims that a candidate can conflict with (Part VI).",
    r"Physical possibility enters the semantics where a content is instantiated in a carrier or transformed, "
    r"as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and it also enters "
    r"as the content of claims that a candidate can conflict with (Part VI).",
    "'In two ways only' was Claude's: the owner wrote 'This is correct.' of the instantiation sentence (S26) and added the "
    "content of claims (S27), and closed no list. The list of ways stays, introduced by 'as when', as illustration.",
    claim_changed=True)

# ------------------------------------------------------------------ l. 159
add(159, "W", "P-2", "adapted",
    r"For a physical target they are changes in what the target itself is and does;",
    r"For a physical target they are changes in what the target itself is and does, as its attributed "
    r"organization admits them (Part II), and admitting a change is not a claim that it can be carried out "
    r"or come about;",
    "Same gap as at l. 75, closed where the range is defined: the target's own admitted edits, not the edits "
    "physics lets anyone carry out. '(Part I)' in the reader's wording changed to Part II, where admitted edits are defined.",
    claim_changed=True)

# ------------------------------------------------------------------ l. 275
add(275, "W", "B-6", "as worded",
    r"An account whose only substantive contrast",
    r"A candidate whose only substantive contrast",
    "An account meets (E) by definition, so 'an account ... fails' contradicted itself.")

# ------------------------------------------------------------------ l. 315
add(315, "W", "R-1", "as worded",
    r"an argument that the candidate gives there what \(\chi\) excludes (Part IX).",
    r"an argument that rules out, for whoever can use it, that what the candidate gives there is something "
    r"\(\chi\) allows (Part IX).",
    "'An argument that X' is a reasons-for form (S23); an argument rules out.")
add(315, "W", "B-1", "as worded",
    r"and so for whom \(\chi\) is a live premise (K2)",
    r"and so who tentatively accepts \(\chi\) (K2)",
    "Goes with the new reading of Live_j at l. 393: a premise is live for j only if j has taken it up.")
add(315, "W", "B-7 and P-1", "B-7 as worded; P-1 adapted",
    r"outside \(C\) it rules out what the candidate's organization gives there, not its meeting (E) on \(p\).",
    r"outside \(C\) it rules out that the target gives there what the candidate's organization gives, not the "
    r"candidate's meeting (E) on \(p\). Either way the argument needs the premise that \(\chi\) speaks of the "
    r"target under that pair's edit. Where the edit is itself one that \(\chi\) excludes, as when a question asks "
    r"what a pendulum does with its friction component deleted, the target so edited may itself give a motion "
    r"that never stops, and without that premise the argument rules out no candidate there; the candidate still "
    r"conflicts with \(\chi\).",
    "B-7: what the candidate gives is a matter of the candidate; what is ruled out is that the target gives it. "
    "P-1: without the premise, 'perpetual motion is impossible' would rule out every candidate for a question "
    "about an edit no one could carry out, which S25 forbids. Adapted: the reader also narrowed the definition "
    "of conflict with a claim; that part is not applied (see not applied), and the missing premise is named "
    "where the ruling out is, so the owner's 'that's a conflict' stands.",
    claim_changed=True)
add(315, "W", "O-6", "adapted",
    r"and \(\chi\) alone does not say where the candidate is in error.",
    r"and \(\chi\) alone does not say where the candidate is in error. A conflict with a claim that a system "
    r"represents can be a recognized difficulty (Part X), as when keeping the candidate meets a claimed aim only "
    r"by dropping the claim, where keeping the claim is among the protected aims (Part XI).",
    "The owner: a bare claim is 'enough to trigger a conflict', and an agent 'uses it to identify flaws'. "
    "Without this, a represented conflict with a claim could not be a recognized difficulty (l. 429 names aims "
    "only). Worded like the last sentence of l. 317 rather than the reader's 'keeping both'. Recognizing a "
    "difficulty is not yet a response, so 'not enough ... to do anything about it' stands.",
    claim_changed=True)
add(315, "W", "R-1 and B-2", "R-1 as worded; B-2 adapted",
    r"conflict there given \(\chi\): the argument that they conflict uses \(\chi\) as a premise and lapses with it.",
    r"conflict there given \(\chi\): an argument that rules out their both meeting (F1), (F2) and (A) there uses "
    r"\(\chi\) as a premise and lapses with it. Two candidates offered one in place of the other that conflict at "
    r"a pair given \(\chi\) are **rivals given \(\chi\)**: for an assessor who tentatively accepts \(\chi\) they "
    r"pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.",
    "R-1: the second reasons-for form. B-2: 'conflict given chi' was defined and used nowhere; now two such "
    "candidates pose a problem for an assessor who tentatively accepts chi. The reader's clause on which kind of "
    "problem is left out: the kinds follow from where the rivals conflict (l. 317), and the clause was in error when "
    "they conflict given chi both inside and outside C.",
    claim_changed=True)

# ------------------------------------------------------------------ l. 317
add(317, "W", "O-4", "adapted",
    r"(conflict with a claim, above; Part IX).",
    r"(conflict with a claim, above; Part IX). Solving a problem so rules one rival out for that assessor while "
    r"the claim stays live for that assessor; it is not a response to the conflict with the claim, which does not "
    r"say where the rival is in error, and what the person goes on with stays the person's choice (conflict with "
    r"a claim, above).",
    "Reading 'not enough ... to do anything about it' as 'does not say where or how to repair' is Claude's; the "
    "text now says what solving here is and is not. Cross-reference changed from 'Part VI' to 'above', since "
    "l. 317 is in Part VI.")
add(317, "W", "R-5", "adapted",
    r"or by whether anyone has tested the candidate on it (Parts I and V).",
    r"or by whether anyone has tested the candidate on it (Parts I and V) [whether this relation, which names "
    r"no assessor, stays in the theory is the owner's open question (S95, hard case 1)].",
    "The assessor-free relation does the work 'true' did; S26 and S27 do not answer hard case 1, so it is marked "
    "open, not closed.")

# ------------------------------------------------------------------ l. 393
add(393, "W", "B-1", "adapted",
    r"\(\operatorname{Live}_j(d;u)\): \(j\) has not withdrawn \(d\), whether or not \(j\) holds an explanation "
    r"of \(d\) [Claude's readings].",
    r"\(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is "
    r"usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not "
    r"withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not "
    r"live for \(j\) [Claude's readings].",
    "Most serious break found: with 'j has not withdrawn d', a premise j never took up was live, so any "
    "contingent claim and its denial were ruled out for every assessor, and 'not ruled out', problems and S21's "
    "choice became empty. 'The same argument' made 'the same argument as u', since u is a step.",
    claim_changed=True)

# ------------------------------------------------------------------ l. 397
add(397, "W", "O-2", "as worded",
    r"rules the candidate out for whoever can use it, on a question about the world as on any other.",
    r"rules the candidate out for whoever can use it, on a question about the world as on any other [Claude's "
    r"reading: the owner's words (S27) speak of a conflict; that a candidate found by examination to assume its "
    r"own answer is ruled out in the same way is read from the owner's definition of argument (S23)].",
    "Carrying S27 over from conflict to circularity is Claude's step, and is now marked so.")
add(397, "W", "O-3", "as worded",
    r"""Using a claim so is, in the owner's words, "a costly gamble for all creative agents"; without it, """
    r""""error correction could become impossibly costly to perform".""",
    r"""That a person can use a claim so, without containing its explanation, is, in the owner's words, "a costly """
    r"""gamble for all creative agents"; and "If this weren't possible, then error correction could become """
    r"""impossibly costly to perform.""" '"',
    "The owner calls 'that property', being able to use an explanation to find errors without containing it, "
    "the gamble; the text had moved the subject to the using. The second quotation is now whole.")
add(397, "W", "R-4", "as worded",
    r"The semantics records the gamble and puts no measure on it.",
    r"The semantics names the gamble and puts no measure on it.",
    "'Records' suggested a ledger; S20 calls a record redundant.")
add(397, "W", "B-3", "as worded",
    r"""Such an argument's conclusion is among its premises, as in "\(p\) because \(p\)", and it rules nothing """
    r"""out for anyone.""",
    r"""Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because """
    r"""\(p\)", and does not rule that claim out for anyone.""",
    "The definition blocks only that one claim; 'rules nothing out for anyone' said more.")
add(397, "W", "B-3 and B-4", "as worded",
    r"it finds that the candidate gives what the premise excludes.",
    r"it finds that the candidate gives what the premise excludes. The block catches only a premise that is the "
    r"claim's denial, read structurally; a premise from which a step leads to the denial, as one does from "
    r"""\(r\) and "if \(r\), this candidate fails (E)", is a premise taken as given, and using it is the gamble """
    r"above, not a circular argument. Where the premises \(j\) tentatively accepts are inconsistent, arguments "
    r"from them can rule out, for \(j\), a claim and its denial alike; the semantics then says only that \(j\)'s "
    r"premises conflict, and which of them \(j\) drops, if any, is \(j\)'s choice (Part 0).",
    "B-3: 'cannot stand in for the steps' said more than the block catches; the text now says what it catches. "
    "B-4: premises taken 'without any thought whatsoever' (S27) make inconsistent premises a case to reckon with; the "
    "text now says what follows, and leaves the dropping to the person (S21).",
    claim_changed=True)

# ------------------------------------------------------------------ l. 429
add(429, "W", "O-5", "adapted",
    r"Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes "
    r"the choice.",
    r"""Closing an episode is a choice: an argument can rule out some ways of closing it for the person choosing, """
    r"""and where it leaves one way not ruled out, the person, in the owner's words, "sees no option" but that one, """
    r"""which is not to say the person "has no option" [the owner said this of non-scientific theories (S21); """
    r"""using it for every episode is Claude's reading]; no argument makes the choice.""",
    "S21: 'sees no option', not 'has no option'. The text never said what a ruling out is for the person "
    "choosing. Worded for the case the owner describes (one way left), not 'one not ruled out' in general. The owner's "
    "words were said 'In the case of non scientific theories'; the bracket marks their use for every episode as Claude's.")

# ------------------------------------------------------------------ l. 461
add(461, "W", "O-1", "as worded",
    r"the only other way it enters is as the content of claims a candidate can conflict with (Part VI).",
    r"it also enters as the content of claims a candidate can conflict with (Part VI).",
    "As at l. 75: the list is not closed at two.",
    claim_changed=True)

# ------------------------------------------------------------------ l. 497
add(497, "W", "P-3", "as worded",
    r"With \(\mathfrak E_\Theta\) the explanatory contents and",
    r"With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module "
    r"(whether a content is explanatory on its question is fixed by (E), Part V; \(\Theta\) says only which of "
    r"them a carrier can hold) and",
    "The index Theta read as if the physical module fixed which contents are explanatory; it belongs to holding "
    "a content (instantiation, S26).")

# ------------------------------------------------------------------ l. 522
add(522, "W", "B-1", "as worded",
    r"the premises \(j\) has not withdrawn",
    r"the premises \(j\) tentatively accepts and has not withdrawn",
    "Goes with l. 393.")

# ------------------------------------------------------------------ l. 526
add(526, "W", "B-2", "as worded",
    r"rivals on conflict and on the offer of one in place of the other,",
    r"rivals on conflict and on the offer of one in place of the other, rivals given a claim on conflict given "
    r"that claim and on the same offer,",
    "Goes with l. 315: the new relation gets its place in the order.")
add(526, "K", "O37", "as worded",
    r"and a separate definition that would supply it is part of the account only when the account uses it",
    r"and a separate definition that would supply it, or a separate argument that rules out the denial of the "
    r"result it is defined through without using it, is part of the account only when the account uses it",
    "Case O37: read strictly, 'a separate definition' left the case's fixed answer ('The textbook proof would break the circle') unreachable; this keeps "
    "O49's reading and restores O37's.")

# ------------------------------------------------------------------ l. 540
add(540, "W", "R-2", "as worded",
    r"Such a case would rule out the Claim of Argument 1 and make correspondence an import again.",
    r"An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it, and "
    r"make correspondence an import again.",
    "A case does not rule out; an argument does, for whoever can use it (l. 17, l. 495).")

NOT_APPLIED = [
    ("W P-1, first part (l. 315): define conflict with a claim only 'when chi, as a claim about the target under "
     "that pair's edit and boundary, excludes' what the candidate gives",
     "The owner: 'If it can be shown that your explanation implies perpetual motion, then that's a conflict', with "
     "no restriction. Narrowing the definition would make the frictionless-pendulum candidate conflict with nothing. "
     "The gap the reader found is in the ruling out, not in the conflict, and the adapted second part names the "
     "missing premise there."),
    ("W B-2, the clause 'of the first kind where the pair is in C and of the second where it is not'",
     "The kinds follow from where the rivals conflict (l. 317); the clause was in error for two candidates that "
     "conflict given chi both inside and outside C. 'As rivals do' carries it."),
    ("W O-7 (point 1 of the reading goes beyond the owner's words)",
     "No text of its own: R-5 marks the assessor-free relation at l. 317 as the owner's open question."),
    ("K l. 317 (N5, O24): point the no-test sentence back to 'does not by itself say which to drop'",
     "Proposed as an owner question, not a text change. O-4 now says that solving a problem by a claim is not a "
     "response to the conflict with the claim; whether the owner's 'not enough ... to do anything about it' "
     "reaches a choice between rivals stays the owner's."),
    ("K l. 275 (N25)",
     "The reader proposed no text change: what a target such as 'the universe and what holds it up' admits is "
     "S95 hard case 1 in another form."),
]

BORDERLINE = [
    dict(line=2, word="Check", reason="a file name, `results/S96 Check of the repaired copy - whole text.md`, in the dated note."),
    dict(line=315, word="accepts", count=2, reason="'who tentatively accepts chi' and 'an assessor who tentatively accepts chi': tentative (S23)."),
    dict(line=393, word="accepts", reason="'a premise j tentatively accepts': tentative (S23)."),
    dict(line=397, word="accepts", reason="'the premises j tentatively accepts': tentative (S23)."),
    dict(line=522, word="accepts", reason="'the premises j tentatively accepts': tentative (S23)."),
    dict(line=497, word="hold", count=2, reason="possession: a content a carrier can hold (instantiation, S26)."),
]

PHYS_REASONS = {
    75: ("instantiation or transformation (point 2(i)); the content of a claim about what is possible or impossible "
         "(point 2(ii)): the adopted physics as a claim an attribution can conflict with, and admitting an edit is not "
         "a claim that it can be carried out; the statement of where physical possibility enters and where it does not "
         "(S25-S27), no longer closed at two; 'adopt' in the sense declared on this line, to take tentatively"),
    159: ("organization sense: the edits the target admits (Part II's A); the statement of where physical possibility "
          "enters (for a physical target, what the target itself is and does, as its attributed organization admits "
          "it, and admitting a change is not a claim that it can be carried out); 'a narrowing adopted': to take tentatively"),
    461: ("instantiation or transformation (point 2(i)): Part XII; the statement of where physical possibility enters, "
          "no longer closed at two; 'adopts': to take tentatively"),
    497: "instantiation (point 2(i)): which explanatory contents some carrier can hold under the physical module",
}

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("repair_apply", os.path.join(HERE, "repair_apply.py"))
    ra = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ra)
    _, _, text1 = ra.build(write=False)
    assert hashlib.md5(text1.encode("utf-8")).hexdigest() == STAGE1_MD5, "stage-1 text md5 changed"
    lines = text1.split("\n")
    problems = 0
    for i, e in enumerate(E):
        c = lines[e["line"] - 1].count(e["old"])
        if c != 1:
            problems += 1
            print("SPAN PROBLEM entry %d line %d count %d: %r" % (i, e["line"], c, e["old"][:90]))
    out = {
        "about": ("S96 Repair, stage 2: the two readers' repairs, applied by repair_apply.py to the stage-1 text "
                  "(md5 %s). Made by replacements_stage2_source.py. W = the whole-text reading, K = the cases "
                  "reading (results/S96 Check of the repaired copy - *.md)." % STAGE1_MD5),
        "groups": {"N": "the dated note at l. 2",
                   "W": "results/S96 Check of the repaired copy - whole text.md",
                   "K": "results/S96 Check of the repaired copy - cases.md"},
        "entries": E,
        "not_applied": [{"item": a, "reason": b} for a, b in NOT_APPLIED],
        "borderline": BORDERLINE,
        "physical_mentions": {str(k): v for k, v in sorted(PHYS_REASONS.items())},
    }
    json.dump(out, open(os.path.join(HERE, "replacements_stage2.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("stage 2 entries:", len(E), " not applied:", len(NOT_APPLIED), " span problems:", problems)
