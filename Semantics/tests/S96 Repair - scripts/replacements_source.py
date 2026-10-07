#!/usr/bin/env python3
"""S96 Repair: the changes to the scrubbed copy of draft 5, written once, here.

Each entry names a line of the scrubbed copy (md5 2517ef4ec1f274e8de2bfb7e6661ef94),
an exact old span on that line, an exact new span, the group it belongs to
(P physical ties, C conflict with a claim, G premises taken as given, F the first
choice, R an S95 repair), the S95 item it applies or supersedes, and a reason.
Running this file compares every old span with the scrubbed copy (present once
on its line) and writes replacements.json beside it; repair_apply.py applies it.
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = ("/home/user/ThreadSmith/Semantics/tests/"
       "Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md")
MD5 = "2517ef4ec1f274e8de2bfb7e6661ef94"

E = []


def add(line, group, ref, old, new, reason, claim_changed=False, whole_line=False):
    E.append(dict(line=line, group=group, ref=ref, old=old, new=new, reason=reason,
                  category=group, claim_changed=claim_changed, whole_line=whole_line))


# ---------------------------------------------------------------- the dated note
NOTE = ("*Experiment, 26 September 2026 (log S96, on decisions S23 to S27). This is the scrubbed "
        "copy of draft 5 (log S95, md5 2517ef4ec1f274e8de2bfb7e6661ef94) with the S96 repairs applied, "
        "made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` beside it), "
        "one line of the scrubbed copy to one line here, so the two compare line by line. The repairs take "
        "physical possibility out of what defines a question, its range of changes, an account and a conflict, "
        "and keep it where a content is instantiated or transformed and as the content of claims a candidate "
        "can conflict with (decisions S25 to S27); they add conflict with a claim, found by argument with no "
        "test, and premises taken as given; and they apply the S95 repairs. Every change, with its reason, is in "
        "`tests/S96 Repair of the scrubbed copy - plan.md`. It is an experiment, not yet a draft of file 13: "
        "draft 5 stays the current draft. The words, and why each was chosen, are in "
        "`tests/S95 Scrub - vocabulary, as used.md`. Some names here are provisional and say so (Part XI).*")

# ---------------------------------------------------------------- P: physical ties
add(75, "P", "S25-S27; supersedes nothing",
    "Every attribution of an organization to a physical system must be possible under the adopted physics; here and throughout, to adopt something is to take it tentatively, open to replacement. Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are fixed by the adopted physics, and substrate independence reaches as far as that physics lets contents pass between media.",
    "Every attribution of an organization to a physical system is a claim that the system instantiates it, and whether a system can is a matter of physics; here and throughout, to adopt something is to take it tentatively, open to replacement, and an attribution that the adopted physics excludes conflicts with it, as a candidate can conflict with a claim (Part VI). Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are matters of physics as well, and substrate independence reaches as far as contents can pass between media.",
    "Instantiation stays physical (S25, S26), but 'must be possible under the adopted physics' and 'fixed by the adopted physics' made a tentatively adopted theory the last word; the adopted physics is now a claim an attribution can conflict with (S26 'not strictly nothing', S27).",
    claim_changed=True)
add(75, "P", "S25-S27 (the one statement of where physics enters)",
    "a barrier in the sense of Part XIII.",
    "a barrier in the sense of Part XIII. Physical possibility enters the semantics in two ways only: where a content is instantiated in a carrier or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and as the content of claims that a candidate can conflict with (Part VI). It does not define a question, its range of changes, an account or a conflict between candidates (Parts III, V, VI).",
    "States S25 as refined by S26 and S27 once, in the Commitments, so every later place can point here.",
    claim_changed=True)
add(43, "P", "S25; supersedes S95 R7",
    "The physical theory fixes which changes are possible at all. A contract is a declared subset of those.",
    "A contract is a declared subset of the changes its target admits (Part II), which are changes in whatever the target is, a garden, a mathematical structure or a melody, and not only those anyone could carry out.",
    "Draft 5 answered grievance 4 by making the contract a subset of the physically possible changes, which S25 takes out of explanation. R7 only renamed 'the physical theory' to 'the adopted physical theory' and is superseded.",
    claim_changed=True)
add(43, "P", "S25",
    "A contract that quietly excludes physically possible changes to protect an account",
    "A contract that quietly excludes changes its target admits to protect an account",
    "Same universe as the new first sentence: the target's changes, not the physically possible ones.")
add(43, "P", "S25; supersedes S95 R7",
    "What is independent of the modeller lies in the physics and in fidelity;",
    "What is independent of the modeller lies in the target and in fidelity;",
    "Point 1 of the reading: whether a candidate meets the requirements is fixed by the thing explained itself. R7's 'the world the adopted physics describes' is superseded.")
add(41, "P", "point 1",
    "turns on the transport and the world alone",
    "turns on the transport and the target alone",
    "'The world' presumes a physical target; the target is whatever is explained (point 1).")
add(49, "P", "S25, point 1",
    "A mathematical argument explains, relative to a question, when its components respond to those edits as the target structure does (Part VII).",
    "A mathematical argument explains, relative to a question, when its components respond to those edits as the target structure does (Part VII). The same goes for a melody, where changing a note or a chord is an edit, and for a philosophical claim, where dropping a premise or a distinction is one. Whether anyone could carry an edit out in a physical system bears on testing and building (Part XII), not on whether a candidate meets (E) at it.",
    "The task asks that a melody or a philosophical claim could be a target; this grievance is where the text already says an admitted change need not be physical.")
add(51, "P", "one word, one thing",
    "get three distinct carriers",
    "get three distinct relations",
    "'Carrier' is a physically located occurrence (Part IV); here it meant a relation, which the next sentence and Part XI call them.")
add(159, "P", "S25; B-scope finding B2 (L159)",
    "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one.",
    "A contract is a declared subset of the changes its target admits (Part II), and a stated scope is what makes it one. Those are the changes the question asks about, in whatever the target is: a garden, a mathematical structure, a melody or a philosophical claim. For a physical target they are changes in what the target itself is and does; whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII), which bears on testing and building and does not by itself put a change in a contract or keep it out.",
    "The definition of a question's range. It keeps what the theory needed from the old 'adopted physics' (for a physical target, what the target itself does) without letting physical possibility define the range (point 1).",
    claim_changed=True)
add(223, "P", "S25",
    "Surprise requires an incomplete selection history: the world must admit changes the system's correspondence was never shaped against (Argument 4).",
    "Surprise requires an incomplete selection history: the contract must contain changes the system's correspondence was never shaped against, and one of them must occur (Argument 4).",
    "'The world must admit' tied the contract to what the world allows; surprise needs only a contract larger than the history and an occurring pair outside it, as its definition at l. 221 says.")
add(257, "P", "S25; B-scope finding B2 (L257)",
    "The contract \\(C\\) is a declared subset of the physically admitted edits, and every physically admitted edit excluded from \\(C\\) is excluded by a stated scope, not silently.",
    "The contract \\(C\\) is a declared subset of the edits the target admits, and every edit the target admits that is excluded from \\(C\\) is excluded by a stated scope, not silently.",
    "Non-vacuity defined through physically admitted edits; now through the target's own admitted edits (Part II's A).",
    claim_changed=True)
add(275, "P", "S25; B-scope finding B2 (L275)",
    "An account whose only substantive contrast is one that no physically admitted edit realizes fails non-vacuity by having a silently narrowed contract.",
    "An account whose only substantive contrast is one that no edit the target admits realizes has no pair of \\(C\\) at which the contrast appears, and fails non-circular dependence. A contrast that no one could produce, or that could not come about, is still a contrast of its question when the target admits the edit that realizes it; whether it can be produced bears on testing (Part XII), not on (E).",
    "Draft 5 made a contrast no physical edit realizes a failure of (E). A clash can stand where no test can reach it (S26 context, example 3); what fails is only a contrast outside the target's own edits, and then non-circular dependence, which needs a pair of C with the contrast, is what fails.",
    claim_changed=True, whole_line=True)
add(315, "P", "S25; B-scope finding B2 (L315); feeds C",
    "or when each of them could meet (F1), (F2) and (A) there under some relations of the target that the adopted physics admits (Part I) and no such relations let both, as none do when two of their active components with one counterpart have different relations there.",
    "or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both, as none do when two of their active components with one counterpart have different relations there. Whether two candidates conflict is fixed by their organizations and transports and by the target's ports and components; it is found by argument, with no test, and it does not turn on what any physics admits (Part I).",
    "Conflict read through 'the relations the adopted physics admits' failed the worked example (l. 343) and made physics define conflict. It now ranges over relations on the target's footprints; what a physics excludes comes in as a claim (conflict with a claim, C).",
    claim_changed=True)
add(317, "P", "point 1",
    "fixed by the candidate, the question and the world,",
    "fixed by the candidate, the question and its target,",
    "Point 1: fixed by the thing explained itself, of whatever kind.")
add(343, "P", "S25; B-scope finding B2 (L343, the worked example)",
    "Non-vacuity is met: any nonzero odd skew matrix is an instance.",
    "Non-vacuity is met: any nonzero odd skew matrix is an instance, and the edits the target admits outside the contract, to the field arithmetic and to the link between determinant and invertibility, are left out by the stated scope. No edit here is a physical one, and none needs to be: the contract is a set of changes to the mathematical target (Part III).",
    "Makes the worked example come out an account on the new wording, with both clauses of non-vacuity read.")
add(461, "P", "S25-S27, Part XII's role",
    "The physical module adopts a task-based formulation of physics for this purpose.",
    "The physical module adopts a task-based formulation of physics for this purpose. It is where physical possibility enters the semantics as instantiation and transformation; the only other way it enters is as the content of claims a candidate can conflict with (Part VI). The module says which organizations a carrier can instantiate, and which transformations of a content, such as holding, copying, teaching, testing, building or performing it, can be carried out. It does not define a question, an account or a conflict between candidates (Parts III, V, VI).",
    "Marks Part XII as the place S25 names, and says what it does not do.")
add(526, "P", "S25; B-scope finding B2 (L526, dependence order)",
    "In Part VI, conflict depends on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict",
    "In Part VI, conflict depends on (F1), (F2), (A) and the target's ports and components (Part II), conflict with a claim on those and on the claim, rivals on conflict",
    "Dependence order follows the new conflict definition and adds conflict with a claim.",
    claim_changed=True)
add(536, "P", "S25; with B6",
    "**(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that nonetheless explains nothing.",
    "**(A) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks.",
    "Part XV's 'physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8).",
    claim_changed=True)
add(538, "P", "S25; with B6",
    "**(B) Necessity.** An explanation, argued to be one and not a non-explanation by an argument that does not use (E), whose organization no transport can preserve under any physically admitted contract.",
    "**(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any contract on its target.",
    "'Physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8), which drops the argued-FOR form.",
    claim_changed=True)
add(580, "P", "S25",
    "strictly smaller than the contract \\(C\\) of changes the world admits.",
    "strictly smaller than its contract \\(C\\).",
    "Argument 4 needs only H strictly inside C; 'changes the world admits' tied C to what the world allows.")
add(211, "P", "point 1",
    "the content's transport to the world fails",
    "the content's transport to its target fails",
    "A theory in error need not be about the physical world (a mathematical structure, a melody).")

# ---------------------------------------------------------------- C: conflict with a claim
add(315, "C", "S27 first footnote; points 2(ii) and 3",
    "whatever rivals anyone offers.",
    "whatever rivals anyone offers. **Conflict with a claim.** A candidate can conflict with a claim as well as with a rival. A candidate **conflicts with** a claim \\(\\chi\\) at an admitted pair of the target that its transport translates, in \\(C\\) or outside it, when \\(\\chi\\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there. \\(\\chi\\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion. Such a conflict is found by argument, with no test against the target: an argument that the candidate gives there what \\(\\chi\\) excludes (Part IX). Where the pair is in \\(C\\), that argument rules out that the candidate meets (E) for any assessor \\(j\\) who can use it, and so for whom \\(\\chi\\) is a live premise (K2); outside \\(C\\) it rules out what the candidate's organization gives there, not its meeting (E) on \\(p\\). The conflict does not by itself say which to drop, the candidate, \\(\\chi\\) or another premise of the argument: which one the person goes on with is the person's choice (Part 0), and using \\(\\chi\\) as a premise gives \\(\\chi\\) nothing. Nor is the conflict enough to do anything about it: a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI), and \\(\\chi\\) alone does not say where the candidate is in error. Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \\(\\chi\\) excludes every such relation, conflict there given \\(\\chi\\): the argument that they conflict uses \\(\\chi\\) as a premise and lapses with it.",
    "Point 3: explanations conflict at the level of explanation, found by argument, with no test; a bare claim is enough to trigger a conflict and not enough to do anything about it. Placed where rivals and conflict are defined; the rivals definition is kept. The last sentence keeps what draft 5's 'relations the adopted physics admits' did, as a conflict relative to a claim.",
    claim_changed=True)
add(317, "C", "S95 R15 (B4), widened for C",
    "Nothing here counts rivals or orders candidates: of one candidate, the only thing said is whether it is ruled out for an assessor; of two, whether they conflict.",
    "Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict.",
    "Applies R15 (the old sentence did not agree with its own paragraph) and adds the new relation so the sentence stays exhaustive.")

# ---------------------------------------------------------------- F: the first choice
add(317, "F", "S27; files 93-94 first choice; point 5",
    "and where both meet (E) on \\(C\\) both are accounts of \\(p\\).",
    "and where both meet (E) on \\(C\\) both are accounts of \\(p\\). Either kind of problem can also be solved with no test, by an argument usable by that assessor that rules out that one of the rivals meets (E) on \\(C\\): one that finds, by examining it, that it assumes its own answer, or that at a pair of \\(C\\) it gives what a claim the assessor tentatively accepts excludes (conflict with a claim, above; Part IX).",
    "A failure found by argument, not by looking at the world, counts, for questions about the world as for others (S27; answers file 93's (c2) and file 94's first question).",
    claim_changed=True)
add(8, "F", "S27; points 4 and 5 (pointer from the definition of argument)",
    "and the semantics never defines accepting by the arguments someone holds.",
    "and the semantics never defines accepting by the arguments someone holds. A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX).",
    "Points the owner's definition of argument at the two S27 points, where it is defined.")

# ---------------------------------------------------------------- G and F and B1/B12 at Part IX
OLD397 = ("**Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions. For \\(\\psi\\), \\(R_j(\\psi)\\) is the set of arguments usable by \\(j\\) that rule out \\(\\psi\\). Where no argument usable by \\(j\\) rules out \\(\\phi\\), that absence rules out nothing, neither \\(\\phi\\) nor \\(\\neg\\phi\\). A record reconstructed from a claim does not rule out that claim's denial.")
NEW397 = ("**Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions. "
          "Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\\(\\operatorname{Form}_j\\)), while that form stays admitted. An argument is usable by \\(j\\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below). "
          "For \\(\\psi\\), \\(X_j(\\psi)\\) is the set of arguments usable by \\(j\\) that rule out \\(\\psi\\). Where no argument usable by \\(j\\) rules out \\(\\phi\\), that absence rules out nothing, neither \\(\\phi\\) nor \\(\\neg\\phi\\). "
          "An argument need not cite a test: one with no record leaf that finds, by examining a candidate, that it assumes its own answer, or that it gives what a claim excludes (Part VI, conflict with a claim), rules the candidate out for whoever can use it, on a question about the world as on any other. "
          "**Premises taken as given.** A premise may be a claim taken as given: tentatively accepted, for whatever reason, even with no thought given to it, by someone who holds no explanation of it. As to its premises, (K2) asks only that they be live for the person using the step; neither it nor anything else in the semantics asks that the person represent (R) a premise's explanation, or any part of it, before using the premise to find an error. Using a claim so is, in the owner's words, \"a costly gamble for all creative agents\"; without it, \"error correction could become impossibly costly to perform\". The semantics records the gamble and puts no measure on it. A system can be designed that must hold the whole explanation of a premise before using it; that is a detail outside the process the semantics describes, and the semantics does not require it. "
          "**A premise that is the denial.** What a stated premise cannot do is stand in for the steps. An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by \"and\", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial. Such an argument's conclusion is among its premises, as in \"\\(p\\) because \\(p\\)\", and it rules nothing out for anyone. A person may still drop the claim, for whatever reason (Part 0): that is the person's choice, not a ruling out, and it leaves the claim not ruled out and any problem it poses as it was (Part VI). A premise taken as given differs from such a premise in that the argument has steps from it to what it rules out: it finds that the candidate gives what the premise excludes.")
add(397, "G", "S27 second footnote (point 4); S95 B1 (range 2 repair 12), B12 (range 2 B4, repair 13) reconsidered; F; rename R_j to X_j",
    OLD397, NEW397,
    "B1: what a whole argument rules out is defined (results file wording). Rename R_j to X_j, R being the repertoire. F: an argument with no record leaf counts, on a question about the world too, and B12's owner marker is dropped because S27 answers it. G: premises taken as given, not contained, not required; the gamble noted, not measured; the fuller system is outside the process. B12 reconsidered: a premise taken as given is distinguished from a premise that is the very denial; the latter rules nothing out, and the person's choice to drop the claim stays the person's (S21). The watch on 'A record ... does not rule out' (O16) is met by saying 'an argument whose record leaf was made from a claim'.",
    claim_changed=True, whole_line=True)
add(393, "G", "S95 B7 (optional readings) and B1 (tentative admitting); G pointer",
    "[Claude's reading; draft 5 names this predicate and does not define it].",
    "[Claude's reading; draft 5 names this predicate and does not define it]. \\(\\operatorname{Scope}_j(u)\\): \\(u\\) is applied within the contract, grain and boundary \\(j\\) has declared for it; \\(\\operatorname{Live}_j(d;u)\\): \\(j\\) has not withdrawn \\(d\\), whether or not \\(j\\) holds an explanation of \\(d\\) [Claude's readings]. Admitting a form, like accepting a claim, is tentative (Part 0).",
    "B7's optional readings of Scope_j and Live_j, applied; Live_j is read so that a premise taken as given is live (G); admitting a form is declared tentative (R1's point, stated where Form_j is).")

# ---------------------------------------------------------------- R: the S95 repairs
R1_OLD = ("Each of its steps rules out the case in which the step's premises are met and its conclusion fails (Part IX). An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2); a claim that no argument rules out is only not ruled out, and gets nothing from that.")
R1_NEW = ("Each of its steps is of an inference form that the person using it admits (\\(\\operatorname{Form}_j\\), Part IX), and admitting a form, like accepting a claim, is tentative; for that person, while the form stays admitted, the step rules out the case in which its premises are met and its conclusion fails. An argument rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not one of its premises (Part IX). An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2). A claim that no argument rules out is only not ruled out, and gets nothing from that; a claim whose denial an argument rules out gets nothing more than that ruling out.")
add(8, "R", "B1 (R1)", R1_OLD, R1_NEW,
    "B1: Part 0's step clause now points at a definition Part IX gives; admitting a form is tentative; a claim whose denial is ruled out gets nothing more. One clause added to R1 ('and the claim's denial is not one of its premises'), to agree with G at l. 397.")
add(17, "R", "B6 (results file wording; supersedes R2)",
    "An explanatory achievement that these four cannot represent would rule out the conjecture; so would a candidate that meets all four and explains nothing. Part XV lists what would rule it out.",
    "A candidate that an argument not using these four rules out as a non-explanation of its question, and that these four cannot represent, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract. An argument that exhibits either rules the conjecture out for whoever can use it, while it stays usable. Part XV lists what such an argument would have to exhibit.",
    "B6: the defeaters rested on the bare 'explains nothing', the predicate l. 31 refuses, and a case, not an argument, ruled out.",
    claim_changed=True)
add(25, "R", "R19",
    "It does not divide an achievement among contributors beyond what a history contains (Part XI).",
    "It does not attribute an achievement to contributors beyond what a history contains (Part XI).",
    "R19: 'attribution' is the vocabulary's word.")
add(31, "R", "B11",
    "No predicate that says \"explains\" without a question and a contract, or \"is a cause\", or \"is a created explanation\", is taken as an import, and no definition depends on one (Argument 6).",
    "No undefined predicate that says \"explains\" without a question and a contract, or \"is a cause\", is taken as an import, and no definition depends on one (Argument 6); (EX) is a defined relation of an episode, not such a predicate.",
    "B11: the refused predicate collided with the defined (EX).")
add(47, "R", "R3",
    "Nothing about construction is reduced to selection; Part IV forbids the reduction and Part XV names what would rule it out.",
    "Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out.",
    "R3: 'forbids', on the S95 residue list, and a rule-out with no argument.")
add(61, "R", "R3",
    "are stated exactly in Part XV together with what would rule out each.",
    "are stated exactly in Part XV together with what an argument would have to exhibit to rule out each.",
    "R3: only an argument rules out.")
add(151, "R", "B9 (R8)",
    "A measure that identifies an outcome, with a prediction from it that is faithful on the contract, answers the identification question;",
    "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question;",
    "B9: 'faithful' is defined for transports only.")
add(159, "R", "B10 (R9)",
    "Meeting the conditions of an account (Part V) on the restricted contract leaves open whether the restriction drops changes the question asked contains.",
    "Meeting the conditions of an account (Part V) on the restricted contract leaves open why the claim is made on this restriction and not on a wider one.",
    "B10: the old reading said nothing, the question asked having the restricted contract.")
add(161, "R", "R4",
    "What is prohibited is changing \\(C\\) or \\(\\mathcal Q\\) during an assessment without recording that the claim has changed.",
    "An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \\(C\\) or \\(\\mathcal Q\\) during it, left unrecorded, makes the record name a claim other than the one assessed.",
    "R4: 'prohibited' is on the S95 residue list.")
add(201, "R", "R10",
    "that is the usual arrangement, not a requirement.",
    "that is one arrangement, not a requirement.",
    "R10: an unargued claim about frequency.")
add(211, "R", "R5",
    "and a later record made from the carrier is not a second, independent trace of its history.",
    "and a later record made from the carrier carries that provenance, not a second, independent one.",
    "R5: an independent second trace, on the S95 residue list.")
add(221, "R", "R6 option B (owner question 3 still open)",
    "- **surprise** is a violation of a selected transport at \\((a,b)\\notin H\\).",
    "- **surprise** is a violation of a selected transport at \\((a,b)\\notin H\\) (the name is provisional; see the marker in Part XI).",
    "R6: option B, which marks and does not decide; option A (renaming) is the owner's call.",
    whole_line=True)
add(223, "R", "R6 option B",
    "a violation the system represents can be a recognized difficulty (Part X).",
    "a violation the system represents can be a recognized difficulty (Part X; the name is provisional, as in Part XI).",
    "R6 option B for 'recognized difficulty' at its first use.")
add(277, "R", "B5 (R11)",
    "(E) does not exclude a mechanism that meets (E) whatever led anyone to guess it; how it came to be taken up is assessed elsewhere (Part IX).",
    "(E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it, and how it came to be taken up is assessed elsewhere (Part IX).",
    "B5: the first sentence had an empty head.")
add(299, "R", "B8 (R12)",
    "Criticality is relative to the route \\(W\\) it is assessed in:",
    "Criticality is relative to the route \\(W\\) it is assessed in, a **route** of the candidate being a member of \\(\\mathsf S_{E,p}\\) (not an active route of a history, Part IX):",
    "B8: 'route' used before it is defined.")
add(305, "R", "range 1 optional clarity",
    "Deletion of \\(d\\) from \\(\\Gamma\\) leaves a route exactly when a minimal route omits \\(d\\).",
    "Deletion of \\(d\\) from \\(\\Gamma\\) leaves \\(\\Gamma\\setminus\\{d\\}\\) a route exactly when a minimal route omits \\(d\\).",
    "Optional clarity, no change of claim; applied.")
add(307, "R", "B8 (R12)",
    "Here a route of the candidate is a member of \\(\\mathsf S\\), and is a route whether or not any history runs it;",
    "A route of the candidate is a route whether or not any history runs it;",
    "B8: the definition now sits at l. 299.")
add(311, "R", "range 1 optional clarity",
    "no minimal route and no singleton instance exists",
    "no minimal route, and no route of one commitment, exists",
    "Optional clarity, no change of claim; applied.")
add(315, "R", "B2 (R13)",
    "A candidate is **ruled out** for an assessor \\(j\\) when an argument usable by \\(j\\) (Part IX) rules out that the candidate meets (E);",
    "A claim is **ruled out** for an assessor \\(j\\) when an argument usable by \\(j\\) (Part IX) rules it out, and a candidate is ruled out for \\(j\\) when the claim that it meets (E) is;",
    "B2: 'ruled out' defined for claims, so l. 369 can apply it to an answer.")
add(317, "R", "B3 (R14, kind i)",
    "is a **test** that solves the problem whatever it records, since an argument from what it records rules out at least one of them for as long as that argument stays usable; an answer it rules out stays ruled out on \\(p\\) for as long as the argument that rules it out stays usable (Part VIII).",
    "is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable; an answer that such an argument rules out stays ruled out on \\(p\\) for as long as the argument stays usable (Part VIII).",
    "B3: the test must solve the problem for that assessor.")
add(317, "R", "B3 (R14, kind ii)",
    "a test inside \\(C\\) can rule out one of them without the other only for a failure of its own;",
    "an argument from a test inside \\(C\\) can rule out one of them without the other only for a failure of its own;",
    "B3/residue: only an argument rules out, not a test.")
add(317, "R", "range 2 repair 22 (l. 317 side)",
    "as a claim that one assignment of counterparts, and not the other, is the target's must (Argument 2, Consequence).",
    "as a claim that the target pairs its components one way and not the other must (Argument 2, Consequence).",
    "The contrastive restatement no longer follows by definition (changed-claims list, l. 317 and 568).")
add(331, "R", "B9 (R16)",
    "it is circular, though its content might be faithful on the contract.",
    "it is circular, though the value it sets might be the target's.",
    "B9: 'faithful' outside its definition.")
add(335, "R", "R17",
    "permitting division changes the state space and does not rule out the scoped result.",
    "permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was.",
    "R17: 'rule out' with no argument.")
add(369, "R", "B2 (R18)",
    "Here \"ruled out\" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out \\(y\\) as the target's answer at \\((a,b)\\), and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses.",
    "Here \"ruled out\" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out the claim that \\(y\\) is the target's answer at \\((a,b)\\); joined to a candidate's own answer \\(y\\) there and to (A), it rules out that the candidate meets (E); and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses.",
    "B2: l. 315 and l. 369 agree, and the step from y to the candidates goes through (A).")
add(385, "R", "range 2 repair 19",
    "Using an objection gives it no bearing (K1) and makes no argument from it usable (K2).",
    "Using an objection does not give it bearing (K1) or make any argument from it usable (K2).",
    "Changed claim: 'gives it no bearing' read as taking bearing away.")
add(429, "R", "range 2 repair 20",
    "Closing an episode is a choice, not an argument.",
    "Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes the choice.",
    "Changed claim: read as saying arguments play no part, against S21.")
add(441, "R", "B13 (range 2 repair 11)",
    "it attributes the repair to each contribution the history contains, and where two sufficient contributions both ran,",
    "it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran,",
    "B13: widened attribution, against l. 307.")
add(443, "R", "R6 option B (the marker)",
    "as are \"understanding\" (Part X) and \"surprise\" (Part IV);",
    "as are \"understanding\" (Part X), \"surprise\" (Part IV) and \"recognized difficulty\" (Parts IV, X);",
    "R6: 'recognized' was marked nowhere.")
add(453, "R", "B15 (range 2 repair 17)",
    "A later narrowing of that contract to rescue its meeting (E)",
    "A later narrowing of that contract to rescue \\(c\\)'s meeting (E)",
    "B15: 'its' had no clear referent.")
add(461, "R", "residue (range 2 repair 7)",
    "a task a permitted input-to-output attribute transformation",
    "a task a specified input-to-output attribute transformation",
    "Residue ('permitted'); with 'specified' a task can be possible or impossible, as Admit and Poss require.")
add(479, "R", "B14 (range 2 repair 15)",
    "each admitting no performance the one before it excludes, and short of exact;",
    "in which \\(q\\) precedes \\(q'\\) when \\(q'\\) admits no performance \\(q\\) excludes, and none of them is exact;",
    "B14: the order presumed a chain.")
add(495, "R", "range 2 repair 1, extended",
    "A finite list of failures is not an argument that no bypass exists; one bypass rules out a proposed barrier.",
    "A finite list of failures does not rule out a bypass; an argument that exhibits one bypass rules out a proposed barrier for whoever can use it.",
    "Repair 1 kept 'one bypass rules out', a rule-out with no argument; extended so only an argument rules out (the vocabulary's one sense).")
add(518, "R", "residue (range 2 repair 5)",
    "It is taken as an input and never defined in terms of anything else;",
    "It is taken as an input and the semantics does not define it;",
    "Residue: the old wording said N cannot be defined.")
add(522, "R", "B7 (with 'admits', per B1)",
    "the system boundary and continuity of an attribution (Part XII);",
    "the system boundary and continuity of an attribution (Part XII); for an assessor \\(j\\), the inference forms \\(j\\) admits, the scope \\(j\\) declares and the premises \\(j\\) has not withdrawn (K2, Part IX);",
    "B7: the assessor's inputs are declared, closing the gap in Argument 6.")
add(526, "R", "B7",
    "(K1) depends on (E).",
    "(K1) depends on (E). (K2) depends on the assessor's declared inputs (Part XIV, above); (K3) on (K2).",
    "B7: (K2) and (K3) take their place in the order.")
add(526, "R", "B11 (range 2 repair 10)",
    "Nothing depends on a predicate that says \"explains\" without a question and a contract, or \"is a cause,\" or \"is a created explanation.\"",
    "Nothing depends on an undefined predicate that says \"explains\" without a question and a contract, or \"is a cause\"; (EX) is a defined relation of an episode, not such a predicate.",
    "B11.")
add(526, "R", "residue (range 2 repair 9)",
    "and a separate argument that would supply it is part of the account only when the account uses it.",
    "and a separate definition that would supply it is part of the account only when the account uses it.",
    "A definition's job is meant; 'an argument that X' was the reasons-FOR form.")
add(532, "R", "residue (range 2 repair 6)",
    "# Part XV — What defeats this class",
    "# Part XV — What would rule this class out",
    "The heading's 'defeats' is on the S95 residue list.",
    whole_line=True)
add(536, "R", "B6 (range 2 repair 8, end of (A))",
    "it is a counterexample only if it fails none of the four and still explains nothing.",
    "it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation.",
    "B6.")
add(540, "R", "B15 (range 2 repair 17)",
    "Such a case would rule out Argument 1 and make correspondence an import again.",
    "Such a case would rule out the Claim of Argument 1 and make correspondence an import again.",
    "B15: claims are ruled out, arguments are not.")
add(542, "R", "residue (range 2 repair 2)",
    "; an argument that every construction trace can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that the object layer of Part IV is not what explanation operates on.",
    "; a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.",
    "'An argument that X', the reasons-FOR form.")
add(544, "R", "residue (range 2 repair 3)",
    "**(E) Question-finding.** An argument that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, either trivializes creativity or fails to capture some case of finding a new question (against Argument 5).",
    "**(E) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5).",
    "'An argument that X', the reasons-FOR form.",
    whole_line=True)
add(568, "R", "range 2 repair 22",
    "a claim that one assignment, and not the other, is the target's is a claim that some admitted change separates them, and must supply it.",
    "a claim that the target pairs its components one way and not the other is a claim that some admitted change separates them, and must supply it.",
    "The contrastive restatement no longer follows by definition.")
add(592, "R", "range 2 repair 21",
    "Finding a new question is a creative act, as answering one is.",
    "Finding a new question, by an owned construction (G), is a creative act, as answering one is.",
    "'Finding' must mean owned construction, as (G) has it.")
add(598, "R", "B7",
    "following each definition back until it reaches the imports, the indices or the declared inputs.",
    "following each definition back until it reaches the imports, the indices, the declared inputs, or (O) and (Q), which depend on nothing.",
    "B7: the walk back never reached (O) and (Q).")
add(600, "R", "B11 (range 2 repair 10)",
    "There is no residual predicate meaning \"explains,\" \"represents,\" \"is a cause,\" or \"is a created explanation.\"",
    "There is no residual, undefined predicate meaning \"explains,\" \"represents,\" or \"is a cause\"; (EX) is defined (Part XI).",
    "B11.")
add(600, "R", "B15 (range 2 repair 17)",
    "Neither is a predicate about explanation taken as an import.",
    "Neither is a predicate about explanation.",
    "B15.")
add(620, "R", "B15 (range 2 repair 16)",
    "Stipulate a object layer",
    "Stipulate an object layer",
    "B15: article.")
add(630, "R", "B15 (range 2 repair 16)",
    "That is not a defect of \\(S_1\\); it is what the contract contains: identity, at this grain, is exhausted by trajectory.",
    "That is not a defect of \\(S_1\\): the contract contains no change that separates the two things except by their trajectories, so identity, at this grain, is exhausted by trajectory.",
    "B15: a category slip, a contract contains changes.")

# ---------------------------------------------------------------- not applied, with reasons
NOT_APPLIED = [
    ("R2 (l. 17)", "superseded by B6's l. 17 wording, which the results file chose (section 7, B6)."),
    ("R7 (l. 43)", "superseded by P at l. 43: the contract is no longer a subset of what any physics says is possible."),
    ("range 2 repair 4 (l. 393, Form_j as 'tentatively accepts')", "superseded by B1's choice of 'admits', declared tentative (results file, B1)."),
    ("range 2 repair 14 with 'tentatively accepts'", "applied with 'admits' instead, per B1."),
    ("B12's marker (the owner's open question on arguments with no record leaf)", "superseded by F: decision S27 answers it; l. 397 now says such an argument counts, on a question about the world as on any other."),
    ("range 2 repair 13 (l. 397, 'neither does a stated assumption of the claim, or of a claim that contains it')", "superseded by G: 'a claim that contains it' could catch a premise taken as given such as 'perpetual motion is impossible'; the new wording names the premise that is the denial, alone or joined by 'and', read structurally."),
    ("R6 option A (rename surprise and recognized difficulty)", "the owner's call (S95 question 3); option B, which marks and does not decide, is applied."),
    ("range 2 repair 18, optional (l. 403, 'a theory that is not an account of its question')", "not applied: l. 211 uses 'a theory in error' for the same idea, and one idea keeps one wording."),
    ("range 2 repair 23, optional (l. 455, worth)", "the owner's call (S95 question 4)."),
    ("hard case 1 (the assessor-free 'meets (E)')", "the owner's call (S95 question 1); the text keeps the relation, now said to be fixed by the candidate, the question and its target."),
]

# ---------------------------------------------------------------- borderline notes (S96 additions)
# Matched by line and word, as in S95 (scan() of the S95 script); S95's own notes are read from its json.
BORDERLINE = [
    dict(line=8, word="accepting", reason="'like accepting a claim': the person's tentative choice, as defined on this line (S23)."),
    dict(line=8, word="accepted", reason="'a claim tentatively accepted as given': tentative by the definition on this line (S23, S27)."),
    dict(line=75, word="held", reason="possession: a content held in a carrier (instantiation, S26)."),
    dict(line=317, word="accepts", reason="'a claim the assessor tentatively accepts': tentative (S23)."),
    dict(line=393, word="holds", reason="possession: whether j holds an explanation of d (S27)."),
    dict(line=393, word="accepting", reason="'like accepting a claim': tentative (S23)."),
    dict(line=397, word="accepted", reason="'tentatively accepted, for whatever reason': tentative (S23), the owner's 'accepted it as a given' (S27)."),
    dict(line=397, word="holds", reason="possession: someone who holds no explanation of the premise (S27)."),
    dict(line=397, word="hold", reason="possession: a system that must hold the whole explanation first (S27)."),
    dict(line=397, word="correction", reason="the owner's words quoted, 'error correction' (S27); a repair of error, not a test of anything."),
]

# ---------------------------------------------------------------- why each remaining physical-tie word stays
ORG = "organization sense: the edits an organization or its target admits (Part II's A), not physical possibility"
POP = "population sense: what a selection population contains (Argument 3), not physical possibility"
INST = "instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII"
CLAIM = "the content of a claim about what is possible or impossible (point 2(ii))"
WHERE = "the statement of where physical possibility enters and where it does not (S25-S27)"
FORM = "the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative)"
ADOPT = "'adopt' in the sense declared at l. 75, to take tentatively"
PHYS_REASONS = {
    2: "the dated note, saying what the repair did with physical possibility",
    8: FORM, 11: ORG, 15: ORG,
    17: ORG + "; and (iv) 'physical realization' of explanatory creativity: " + INST,
    21: INST, 31: INST + "; and 'the contract of admitted changes': " + ORG,
    39: ORG, 41: POP, 43: ORG, 45: INST,
    49: ORG + "; and " + WHERE, 53: INST, 57: ORG, 61: POP,
    75: INST + "; " + CLAIM + " (the adopted physics as a claim an attribution can conflict with); " + WHERE + "; " + ADOPT,
    91: ORG, 105: ORG, 109: ORG, 141: ORG,
    159: ORG + "; " + WHERE + " (for a physical target, what the target itself is and does); and 'a narrowing adopted': " + ADOPT,
    169: INST, 175: ORG, 177: ORG, 179: INST, 193: INST, 201: INST,
    205: INST + "; and 'admits a transport': the organization has one, not physical possibility",
    211: INST, 213: INST, 257: ORG, 269: ORG, 275: ORG,
    315: ORG + "; " + WHERE + " ('does not turn on what any physics admits'); " + CLAIM + " ('perpetual motion is impossible')",
    317: ORG, 325: ORG, 329: ORG,
    343: ORG + "; and " + WHERE + " ('No edit here is a physical one')",
    353: ORG, 365: INST, 375: INST, 393: FORM,
    397: FORM + "; and 'impossibly costly' is the owner's quoted words about cost, not physical possibility",
    403: INST, 405: INST, 407: INST, 409: INST, 411: INST, 425: ORG, 459: INST,
    461: INST + "; " + WHERE + "; and 'adopts': " + ADOPT,
    463: INST, 469: INST, 475: INST, 477: INST, 479: INST, 481: INST,
    487: INST, 492: INST, 495: INST, 517: INST,
    520: ORG + "; and 'physical history' of provenance: " + INST,
    522: FORM, 526: INST + " ('physical provenance' of (R))", 528: INST,
    536: ORG, 540: ORG, 542: POP, 568: ORG,
    572: INST + " (the selection population, a physical history)", 574: ORG,
    576: POP + "; and 'a physical relation' that may fix a selected value: " + INST,
    590: ORG, 608: "'an operation the semantics admits': the S95 word for draft 5's 'licensed', not physical possibility",
    612: INST, 620: ORG, 626: ORG, 630: ORG, 632: INST,
}

if __name__ == "__main__":
    raw = open(SRC, "rb").read()
    assert hashlib.md5(raw).hexdigest() == MD5, "scrubbed copy md5 changed"
    lines = raw.decode("utf-8").split("\n")
    problems = 0
    for i, e in enumerate(E):
        c = lines[e["line"] - 1].count(e["old"])
        if c != 1:
            problems += 1
            print("SPAN PROBLEM entry %d line %d count %d: %r" % (i, e["line"], c, e["old"][:90]))
        if e["whole_line"] and lines[e["line"] - 1] != e["old"]:
            print("NOTE entry %d line %d marked whole_line but is a span" % (i, e["line"]))
    out = {
        "about": "S96 Repair replacements for the scrubbed copy of draft 5 (md5 %s). Made by replacements_source.py; applied by repair_apply.py. Line numbers are the scrubbed copy's and the repaired copy's alike." % MD5,
        "groups": {"P": "physical ties (decisions S25-S27, points 1-2)",
                   "C": "conflict at the level of explanation (S27, point 3)",
                   "G": "premises taken as given (S27, point 4; S95 B12 reconsidered)",
                   "F": "the first choice of files 93-94 (S27, point 5)",
                   "R": "S95 break and residue repairs (results file sections 7-9, both S95 range readings)"},
        "replace_lines": {"2": NOTE},
        "entries": E,
        "not_applied": [{"item": a, "reason": b} for a, b in NOT_APPLIED],
        "borderline": BORDERLINE,
        "physical_mentions": {str(k): v for k, v in sorted(PHYS_REASONS.items())},
    }
    json.dump(out, open(os.path.join(HERE, "replacements.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("entries:", len(E), " span problems:", problems)
