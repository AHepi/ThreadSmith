#!/usr/bin/env python3
"""S96 Repair, stage 3 (log S97): the FIX rulings of the reading of the outside
cross-examination (results/S96 Reading of the replies.md) and the owner's two points
of decision S28, as span entries on the S96 final text (md5
8bb4d19d5aad53de2492b2193fd23ff1). Writes replacements_stage3.json beside this file.
Applied by repair_apply.py --stage3, under the stage rules: each old span exact and
once on its line, spans on a line not overlapping, no line added or removed.

Each entry: line, ruling (the ids of the rulings it applies), group (X = a reply's
challenge taken up; O = the owner's words of S28; N = the dated note), old, new,
reason, claim_changed.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

E = []


def add(line, ruling, group, old, new, reason, claim_changed=False):
    E.append(dict(line=line, ruling=ruling, group=group, old=old, new=new,
                  reason=reason, category=group, claim_changed=claim_changed))


# ---- N: the dated note -------------------------------------------------------
add(2, "note", "N",
    "(log S96, on decisions S23 to S27)",
    "(logs S96 and S97, on decisions S23 to S28)",
    "The note names the log entries and decisions the text now answers to.")
add(2, "note", "N",
    "made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` beside it),",
    "made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` beside it), and a third stage after the outside cross-examination and the owner's words of 26 September (decision S28), from `replacements_stage3.json` (rulings in `results/S96 Reading of the replies.md`),",
    "The note says how the text was made; it now names the third stage and where its rulings are.")
add(2, "note", "N",
    "Every change, with its reason, is in `tests/S96 Repair of the scrubbed copy - plan.md`.",
    "Every change of the first two stages, with its reason, is in `tests/S96 Repair of the scrubbed copy - plan.md`, and of the third in the reading of the replies.",
    "The plan covers stages 1 and 2 only.")

# ---- O: decision S28 ----------------------------------------------------------
add(8, "S28 (i), S28 (ii)", "O",
    "A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX).",
    "A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX). Nothing in the semantics is settled: whether a candidate meets the conditions of an account depends on the candidate, its question and its target, not on anyone's view of them, and whatever anyone accepts about it is accepted tentatively (Part VI); in the owner's words, \"A theory is never settled.\" Where a claim taken as given is used to rule out a rival, that ruling out is a choice the person made, not something the claim does by itself; in the owner's words, \"That \"ruling out\" is a choice that was made.\"",
    "Decision S28, both points, stated once where the two words are defined; the owner's words quoted verbatim.",
    claim_changed=True)
add(315, "S28 (i)", "O",
    "Whether two candidates conflict is fixed by their organizations and transports and by the target's ports and components;",
    "Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them;",
    "S28 (i): no wording implying finality; 'depends on ... not on anyone's view' is the owner's point applied to conflict, next to the relation it pairs with.")
add(315, "S28 (ii)", "O",
    "Nor is the conflict enough to do anything about it: a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI), and \\(\\chi\\) alone does not say where the candidate is in error.",
    "Nor is the conflict enough to do anything about it (S27): ruling the candidate out by \\(\\chi\\) is already doing something about it, and is a choice the person made in taking \\(\\chi\\) as given, not something \\(\\chi\\) does by itself (S28); a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI); and \\(\\chi\\) alone does not say where the candidate is in error.",
    "S28 (ii): 'Also, yes. That \"ruling out\" is a choice that was made.' The bare claim is still not enough (S27); the ruling out that uses it is the person's choice.",
    claim_changed=True)
add(317, "S28 (ii)", "O",
    "Solving a problem so rules one rival out for that assessor while the claim stays live for that assessor; it is not a response to the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above).",
    "Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor. Where the argument uses a claim the assessor tentatively accepts, that ruling out is a choice the assessor made, in taking the claim as given and going on with it, and not something the claim does by itself; it is already something done about the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above).",
    "S28 (ii) reverses 'it is not a response to the conflict with the claim': the owner answered 'Also, yes.' 'While the argument stays usable' covers the circular case too, which has no claim.",
    claim_changed=True)
add(317, "mimo 2 2; S28 (ii)", "X",
    "is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable;",
    "is a **test**. Whatever it records, an argument from what it records rules out at least one of them for an assessor who can use it, that is, for whom its steps' forms are admitted, its scope is the one declared and its premises about the test's background and instruments are live (K2, K3), while it stays usable; taking those premises as given is that assessor's choice, and so is the ruling out that uses them, which the test does not make by itself (Part 0);",
    "Live premises alone do not make an argument usable (K2 asks forms and scope as well), and 'solves the problem whatever it records' stated an outcome (S21); the ruling out is the assessor's choice (S28).",
    claim_changed=True)
add(317, "S28 (i)", "O",
    "whether a candidate is an account of a question is fixed by the candidate, the question and its target, not by when anyone first asks the question or by whether anyone has tested the candidate on it (Parts I and V) [whether this relation, which names no assessor, stays in the theory is the owner's open question (S95, hard case 1)].",
    "whether a candidate is an account of a question depends on the candidate, the question and its target, and not on anyone's view of them, on when anyone first asks the question or on whether anyone has tested the candidate on it (Parts I and V); nothing about it is ever settled, and whatever anyone accepts about it, that a candidate is an account or that it is not, is accepted tentatively (Part 0) [the owner's words of 26 September (S28): \"A theory is never settled.\"; the owner called \"correct\" the reading that the thing explained is however it is and that everything anyone accepts about it stays tentative].",
    "S28 (i): 'fixed by' read as final; the owner's answer to hard case 1 replaces the open-question bracket.",
    claim_changed=True)
add(397, "S28 (ii)", "O",
    "is read from the owner's definition of argument (S23)].",
    "is read from the owner's definition of argument (S23)]. Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0; the owner's words, S28).",
    "S28 (ii), where Part IX says an argument with no record leaf rules a candidate out.",
    claim_changed=True)
add(369, "S28 (i)", "O",
    "and the failure on \\(p\\) stands (Historical index).",
    "and it leaves the failure on \\(p\\) as it was (Historical index).",
    "S28 (i): 'stands' can be read as final; the point is only that a new question does not change the old one.")
add(606, "S28 (i)", "O",
    "and whether \\(\\mathcal E\\) meets (E) on \\(C\\) is fixed at that index (Part VIII, historical index).",
    "and whether \\(\\mathcal E\\) meets (E) on \\(C\\) is a claim at that index (Part VIII, historical index).",
    "S28 (i): 'fixed' can be read as final; the argument needs only that the claim is indexed.")

# ---- X: challenges taken up ------------------------------------------------------
add(15, "mimo 1 8", "X",
    "and question-finding is at least half of creativity.",
    "and creativity includes finding questions, not only answering them.",
    "A proportion the semantics never measures and no word of the owner's gives (S20: no count).",
    claim_changed=True)
add(17, "mimo 1 1; mimo 4 F3 (ii)", "X",
    "and (iv) their physical realization. A candidate that an argument not using these four rules out as a non-explanation of its question, and that these four cannot represent, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract.",
    "and (iv) their physical realization, the instantiation and transformation of these contents in carriers (Part I). A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it; so would a candidate that meets (E) on its question and contract (Part V) when such an argument rules out the claim that it is an explanation there.",
    "'Rules out as a non-explanation' reads both ways; 'their' had no clear antecedent; 'meets all four' made physical realization a condition a candidate meets (against S25), and is aligned with Part XV's (Suff).",
    claim_changed=True)
add(31, "mimo 4 F1", "X",
    "Everything else is defined in terms of the two imports, the declared indices and the **declared inputs**,",
    "Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the **declared inputs**,",
    "Argument 6's reasons end at (O) and (Q) as well; the front matter says what the claim now says.")
add(43, "mimo 1 3", "X",
    "A contract is a declared subset of the changes its target admits (Part II)",
    "A contract is a stated subset of the changes its target admits (Part II)",
    "'Declared' is also one of three provenances (Part III); 'stated' removes the clash.")
add(47, "atria A 3", "X",
    "Selection appears once, at the bottom, to produce the object layer of persistent things that explanation operates on.",
    "Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, it produces the object layer of persistent things that explanation operates on.",
    "The front matter said flatly what Part IV (l. 201) calls one arrangement, not a requirement; l. 35 promises the front matter says nothing the body does not.")
add(49, "mimo 1 7", "X",
    "A mathematical argument explains, relative to a question,",
    "A piece of mathematics explains, relative to a question,",
    "'Argument' is defined in Part 0 as reasons why this and not that; a candidate explanation is another thing.")
add(53, "glm A 3", "X",
    "Whether it occurred is a claim about the physical module, fallible but testable in principle.",
    "Whether it occurred is a claim about the physical module, fallible as any claim about it is (Part XII).",
    "'Testable in principle', set against 'a kind-label is not a claim about anything', reads as a criterion of meaning by testability (S23); the contrast needs only the physical claim.")
add(61, "atria A 4; mimo 1 4", "X",
    "In short: (A) sufficiency of the four conditions of Account; (B) their necessity; (C) the eliminability of kinds; (D) the two provenances",
    "In short: (Suff) sufficiency of the four conditions of Account; (Nec) their necessity; (Elim) the eliminability of kinds; (Prov) the two provenances",
    "The labels (A) to (E) are also the tags of question fidelity, the account relation and others.")
add(61, "atria A 4; mimo 1 4", "X",
    "(E) the representability of question-finding.",
    "(QF) the representability of question-finding.",
    "As above.")
add(105, "mimo 1 7", "X",
    "mathematical arguments or histories.",
    "mathematical structures or histories.",
    "As at l. 49.")
add(109, "mimo 1 6", "X",
    "A port is an **observation** when \\(A\\) contains an edit that alters the relation reporting it without altering what it reports.",
    "A port is an **observation** when \\(A\\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).",
    "'Reporting' is a role word under a heading that supplies no roles; the pointer names the signature it comes from.")
add(119, "mimo 1 9 (b)", "X",
    "where \\(\\tau\\) translates edits,",
    "where \\(\\pi\\) translates valuations, \\(\\tau\\) translates edits,",
    "Four components introduced, three glossed.")
add(151, "mimo 1 5", "X",
    "An obstruction question has a \\(\\mathcal Q\\) that returns reachable or unreachable.",
    "An obstruction question has a \\(\\mathcal Q\\) that returns reachable or unreachable. The rule-status and purpose-achievement cases are given with constitutive rules (Part VII) and with achievement, (AR) (Part XI).",
    "Two of the five respects had no pointer; the fix points to where they are worked, and adds no claim.")
add(155, "mimo 1 3", "X",
    "A **declared** contract is stipulated by the modeller.",
    "A **declared** contract is stipulated by the modeller, with neither selection nor construction in its history; this is its provenance, and not the sense in which every contract, whatever its provenance, is a declared index of the claims made on it (Part XIV).",
    "Two senses of 'declared' named apart.")
add(159, "mimo 1 3", "X",
    "A contract is a declared subset of the changes its target admits (Part II), and a stated scope is what makes it one.",
    "A contract is a stated subset of the changes its target admits (Part II), and a stated scope is what makes it one.",
    "As at l. 43.")
add(193, "mimo 2 5", "X",
    "A transport \\(t\\) between organizations of a physical system has exactly one of three provenances,",
    "A transport \\(t\\) whose domain is an organization of a physical system has exactly one of three provenances,",
    "(R) gives a provenance to a transport from an occurrence's organization to a content, which need not be an organization of a physical system.")
add(197, "mimo 2 4", "X",
    "or the organization it targets,",
    "or the organization it carries to,",
    "'Target' is the question's target elsewhere; here it meant the transport's codomain.")
add(205, "mimo 2 5", "X",
    "when the organization that \\(o\\) instantiates under the physical module, at grain \\(\\ell\\), admits a transport to \\(c\\) that is faithful on \\(c\\)'s contract and whose provenance is selected or constructed:",
    "when there is a transport from the organization that \\(o\\) instantiates under the physical module, at grain \\(\\ell\\), to \\(c\\), faithful on \\(c\\)'s contract, whose provenance is selected or constructed; in (R), \\(\\operatorname{Sel}(t)\\) and \\(\\operatorname{Con}(t)\\) abbreviate \\(\\operatorname{Sel}(t;\\mathcal T,\\mu,H)\\) and \\(\\operatorname{Con}(t;h,e)\\) for some such parameters:",
    "'Admits' is the verb for edits (Part II); the parameters of Sel and Con were suppressed without a word.")
add(211, "mimo 2 4", "X",
    "while the content's transport to its target fails.",
    "while the transport from the content's target to the content fails.",
    "Transports run from the target to the candidate (l. 183, l. 231).")
add(231, "atria A 6; mimo 2 6", "X",
    "The pair \\(\\mathcal E=(E,p,t,\\Gamma)\\) meets \\(\\operatorname{Account}(\\mathcal E)\\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \\(C\\).",
    "The candidate together with its question, \\(\\mathcal E=(E,p,t,\\Gamma)\\), meets \\(\\operatorname{Account}(\\mathcal E)\\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \\(C\\). Where an organization \\(E'\\) is obtained from \\(E\\) by a declared operation (Part VI), \\(\\operatorname{Account}(E',p)\\) abbreviates \\(\\operatorname{Account}\\big((E',p,t',\\Gamma')\\big)\\), with \\(t'\\) the transport the operation carries \\(t\\) to and \\(\\Gamma'\\) the commitments it leaves; for \\(E|W\\), \\(t'\\) is \\(t\\) with \\(\\lambda\\) restricted to the components of \\(E|W\\), and \\(\\Gamma'\\) is \\(W\\).",
    "A quadruple was called a pair, and Account was used with two arguments (ll. 290, 302) with no word saying what they abbreviate.")
add(233, "glm A 1", "X",
    "the relation obtained by imposing the constraints of \\(\\lambda(k)\\) and projecting away its hidden ports equals the component relation of \\(k\\) under the translated edit:",
    "the relation obtained by imposing the constraints of \\(\\lambda(k)\\), projecting away its hidden ports and carrying what remains to \\(V_k\\) by the port translation of \\(\\lambda\\) (write \\(\\operatorname{proj}^{\\lambda}_{V_k}\\) for this projection) equals the component relation of \\(k\\) under the translated edit:",
    "V_k is a footprint of E and Sol of lambda(k) is over ports of D; the projection needs the port translation that l. 119 and Argument 1 name.")
add(236, "glm A 1", "X",
    "\\operatorname{proj}_{V_k}\\!\\big[",
    "\\operatorname{proj}^{\\lambda}_{V_k}\\!\\big[",
    "As at l. 233.")
add(245, "mimo 2 3", "X",
    "By (K), no component of \\(E\\) whose signature differs from its counterpart's meets (F1);",
    "By (K), no component of \\(E\\) whose signature on \\(C\\) differs from its counterpart's meets (F1);",
    "(F1) quantifies over C; l. 281 reads kinds on C.")
add(255, "mimo 2 1", "X",
    "such that the answer profile at \\((a,b)\\) differs from its value at \\((1,b_0)\\), or is not determined there in the claimed way,",
    "such that the answer of \\(E\\) at \\((\\tau(a),\\sigma(b))\\) differs from its answer at \\((1,\\sigma(b_0))\\), or is not determined at \\((\\tau(a),\\sigma(b))\\) in the claimed way,",
    "Whose answer and which 'there' were unstated; the loss clause is about E's answers at these two points, and by (A) the first disjunct is unchanged.")
add(257, "mimo 1 3", "X",
    "The contract \\(C\\) is a declared subset of the edits the target admits,",
    "The contract \\(C\\) is a stated subset of the edits the target admits,",
    "As at l. 43.")
add(257, "mimo 2 6", "X",
    "does not meet non-circular dependence and is therefore not a contract",
    "admits no candidate that meets non-circular dependence, and is therefore not a contract",
    "Non-circular dependence is a condition on a candidate, not on a contract.")
add(305, "mimo 2 7", "X",
    "then the critical singletons are exactly \\(\\bigcup\\min\\mathsf S\\) and the globally indispensable ones are exactly \\(\\bigcap\\min\\mathsf S\\).",
    "then \\(d\\in\\Gamma\\) is critical for some route (**contributory**) exactly when \\(d\\in\\bigcup\\min\\mathsf S\\), and \\(d\\) is **globally indispensable**, \\(\\Gamma\\setminus\\{d\\}\\notin\\mathsf S_{E,p}\\), exactly when \\(d\\in\\bigcap\\min\\mathsf S\\).",
    "Singletons were equated with commitments, and 'globally indispensable' (and l. 307's 'contributory') had no definition before use; the argument's reasons are unchanged and read as before.")
add(311, "mimo 2 8", "X",
    "\\(\\Gamma=\\{d_n:|x|\\le 1/n\\}\\): every unbounded index set determines \\(x=0\\);",
    "\\(\\Gamma=\\{d_n:n\\in\\mathbb N\\}\\), \\(d_n\\) the constraint \\(|x|\\le 1/n\\): every set of indices unbounded in \\(\\mathbb N\\) determines \\(x=0\\);",
    "The set-builder had its condition on x, not on n.")
add(325, "atria A 2", "X",
    "Stipulate \\(H:=U_H,\\ \\theta:=U_\\theta,\\ L:=H\\cot\\theta\\).",
    "Stipulate \\(H:=U_H,\\ \\theta:=U_\\theta,\\ L:=H\\cot\\theta\\), where \\(U_H\\) and \\(U_\\theta\\) are exogenous values setting the pole's height \\(H\\) and the sun's elevation \\(\\theta\\), and \\(L\\) is the length of the pole's shadow.",
    "U_H and U_theta occur only here; the gloss keeps the components the rest of the paragraph intervenes on.")
add(329, "atria A 1; glm A 2; mimo 3 5", "X",
    "For linear \\(A\\) and feature \\(c^\\top\\), identification is \\(\\ker A\\subseteq\\ker c^\\top\\). (I4)",
    "For linear \\(g\\) and linear feature \\(c^\\top\\), identification is \\(\\ker g\\subseteq\\ker c^\\top\\). (I3)",
    "A is the set of admitted edits (l. 91); the tag (I3) was missing since file 10, not dropped by the scrub or the repair (looked up in draft 5 and file 10); no line cites (I4).")
add(331, "atria A 1", "X",
    "For the two balances \\(\\begin{pmatrix}1&1&0\\\\1&0&1\\end{pmatrix}\\), the kernel",
    "For the two balances \\(\\begin{pmatrix}1&1&0\\\\1&0&1\\end{pmatrix}\\), reading an unknown mass \\(x\\) with biases \\(b_A,b_B\\), in that order, the kernel",
    "x, b_A and b_B were never introduced, and the kernel claim goes through only in that order.")
add(339, "mimo 3 6", "X",
    "whose relation is full by (O).",
    "whose relation is full (Part II).",
    "Fullness of a deleted component's relation is stated at l. 103, beside (O), not by (O).")
add(339, "atria A 4; mimo 1 4", "X",
    "is listed under attack (B) in Part XV",
    "is listed under attack (Nec) in Part XV",
    "The Part XV labels, renamed.")
add(343, "mimo 1 7", "X",
    "That a three-line mathematical argument is shorter",
    "That a three-line piece of mathematics is shorter",
    "As at l. 49.")
add(369, "mimo 3 3", "X",
    "the argument is not usable and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (K2).",
    "the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (E).",
    "The lapse is (K2)'s; becoming an account is (E)'s.")
add(375, "mimo 3 1", "X",
    "with an acyclic causal precedence \\(\\prec_h\\) and a physical",
    "with an acyclic causal precedence \\(\\prec_h\\) (write \\(\\preceq_h\\) for its reflexive closure) and a physical",
    "(EX) uses a relation never defined.")
add(377, "mimo 3 1", "X",
    "and \\(\\mathcal E_c\\) the criticism's connection from \\(g\\) to \\(\\delta\\), interpreted as an explanatory candidate (Part V) for \\(p_\\delta\\).",
    "and \\(\\mathcal E_c\\) the explanatory candidate (Part V) for \\(p_\\delta\\) whose organization is the criticism's connection from \\(g\\) to \\(\\delta\\), with its transport and its identified commitments.",
    "Account takes the whole candidate, question included (l. 231).")
add(380, "mimo 3 1", "X",
    "\\operatorname{Account}(\\mathcal E_c,p_\\delta)",
    "\\operatorname{Account}(\\mathcal E_c)",
    "As at l. 377.")
add(387, "mimo 3 1", "X",
    "with essential premises \\(\\operatorname{Prem}(u)\\):",
    "with essential premises \\(\\operatorname{Prem}(u)\\), the premises its inference form uses:",
    "'Essential' was never said.")
add(413, "mimo 3 2", "X",
    "The equivalence is structural at the stated grain, not string equality or similarity.",
    "The relation is structural at the stated grain, not string equality or similarity; it is read with \\(c\\) and its contract fixed, and (N) uses it only so, testing each \\(d\\) against \\(c\\).",
    "Faithful on c's contract makes the relation neither symmetric nor transitive in general; (N) needs neither.")
add(422, "mimo 3 1", "X",
    "\\iff\\operatorname{Attempt}\\land\\operatorname{New}\\land\\operatorname{Build}.",
    "\\iff\\operatorname{Attempt}(s,c,p,h,e)\\land\\operatorname{New}(s,c,h,e)\\land\\operatorname{Build}_{\\beta,\\ell}(s,c,h,e).",
    "The arguments, written out; no change of claim.")
add(447, "mimo 3 1", "X",
    "\\land\\operatorname{Repair}_{O,P}(\\xi,\\xi';\\Delta)\\\\",
    "\\land\\exists\\xi,\\xi'\\,\\bigl[\\operatorname{Repair}_{O,P}(\\xi,\\xi';\\Delta)\\\\",
    "xi and xi' were free in (EX).")
add(448, "mimo 3 1", "X",
    "\\exists c,p_c,e_c\\,[e_c\\preceq_h e\\land\\neg o(\\xi)\\land o(\\xi')\\land\\operatorname{Origin}(s,c,p_c,h,e_c)\\\\",
    "\\exists c,p_c,e_c,t_c,\\Gamma_c\\,[e_c\\preceq_h e\\land\\neg o(\\xi)\\land o(\\xi')\\land\\operatorname{Origin}_{\\beta,\\ell}(s,c,p_c,h,e_c)\\\\",
    "Account needs a transport and commitments for c.")
add(449, "mimo 3 1", "X",
    "\\land\\operatorname{Account}(c,p_c)\\land c\\in\\operatorname{Result}(\\Delta)\\land\\operatorname{Deploy}(s,c,\\xi';U_c)\\land\\operatorname{ProducesVia}(\\Delta,c,o;\\xi,\\xi')].",
    "\\land\\operatorname{Account}\\big((c,p_c,t_c,\\Gamma_c)\\big)\\land c\\in\\operatorname{Result}(\\Delta)\\land\\operatorname{Deploy}_{\\beta,\\ell}(s,c,\\xi';U_c)\\land\\operatorname{ProducesVia}(\\Delta,c,o;\\xi,\\xi')]\\bigr].",
    "As at l. 447 and l. 448.")
add(453, "mimo 3 1", "X",
    "The scope of \\(\\operatorname{Account}(c,p_c)\\) is the contract fixed at \\(e_c\\).",
    "In (EX), \\(t_c\\) and \\(\\Gamma_c\\) are the transport and the identified commitments that make \\(c\\), with \\(p_c\\), an explanatory candidate (Part V), and \\(U_c\\) is the declared use task for \\(c\\) (Deploy, Part X). The scope of \\(\\operatorname{Account}((c,p_c,t_c,\\Gamma_c))\\) is the contract fixed at \\(e_c\\).",
    "Glosses for the new bound variables and for U_c, which was free.")
add(455, "mimo 3 4", "X",
    "\\(\\mathcal R\\subseteq A\\times K\\times F\\); a purpose \\(G\\subseteq K\\times F\\);",
    "\\(\\mathcal R\\subseteq \\mathit{Act}\\times\\mathit{Occ}\\times\\mathit{Eff}\\); a purpose \\(G\\subseteq \\mathit{Occ}\\times\\mathit{Eff}\\);",
    "A, K and F already name edits, the signature tag and the feature space.")
add(455, "mimo 3 4", "X",
    "\\(\\mathcal N\\subseteq A\\times K\\times\\mathcal Rsn\\times\\mathcal V_A\\) taken as a substantive input when aesthetic value is claimed.",
    "\\(\\mathcal N\\subseteq \\mathit{Act}\\times\\mathit{Occ}\\times\\mathsf{Rsn}\\times\\mathcal V_A\\) taken as a substantive input when aesthetic value is claimed, where \\(\\mathit{Act}\\) is a set of actions, \\(\\mathit{Occ}\\) of occasions, \\(\\mathit{Eff}\\) of effects, \\(\\mathsf{Rsn}\\) of aesthetic reasons and \\(\\mathcal V_A\\) of aesthetic values, the last two not further specified here.",
    "Rsn and V_A were never glossed.")
add(495, "mimo 4 F5", "X",
    "enabling condition for \\(s\\) and the task \\(T\\).",
    "enabling condition for \\(s\\) and the task \\(T\\), in the sense of (CT1).",
    "Enable read as circular; 'enabling condition' is the chi of (CT1).")
add(497, "mimo 4 F5", "X",
    "both specified independently of the candidate,",
    "both specified independently of the candidate, with \\(\\operatorname{Can}\\), \\(\\operatorname{CanAdv}\\), \\(J_p\\) and \\(C_I\\) as in Part XII, \\(U_c\\) the declared use task for \\(c\\) (Deploy, Part X), \\(A_p\\) the task for \\(p\\) that \\(\\operatorname{CanAdv}\\) describes, and \\(\\xi_0\\) the index at which the claim is made,",
    "Symbols used in (U1) to (U3) with no gloss or pointer.")
add(506, "mimo 4 F5", "X",
    "\\mathsf{UECS}=\\{(M,s,\\Omega,\\beta):",
    "\\mathsf{UECS}=\\{(M,s,\\xi_0,\\Omega,\\beta):",
    "xi_0 was free in (U3).")
add(520, "mimo 4 F1", "X",
    "Everything else is defined in terms of the two imports, the declared indices and the declared inputs (below).",
    "Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below).",
    "As at l. 31.")
add(526, "mimo 4 F10", "X",
    "The order has no cycle and no endless descent: a representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in it, and a separate definition that would supply it, or a separate argument that rules out the denial of the result it is defined through without using it, is part of the account only when the account uses it.",
    "The order has no cycle and no endless descent. A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order; a separate definition that would supply that place, or a separate argument that rules out the denial of the result the definition goes through without using that result, is part of the account only when the account uses it.",
    "One sentence with four referents for 'it'; split, with each named.")
add(536, "atria A 4; mimo 1 4", "X",
    "**(A) Sufficiency.**",
    "**(Suff) Sufficiency.**",
    "The Part XV labels, renamed.")
add(536, "mimo 4 F3", "X",
    "with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks.",
    "with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.",
    "'Non-declared' could be read as a declared input; it is the provenance. 'Rules out as' made one-way.")
add(536, "mimo 4 F3", "X",
    "and such an argument rules it out as an explanation.",
    "and such an argument rules out the claim that it is an explanation.",
    "As above.")
add(538, "atria A 4; mimo 1 4; mimo 4 F3 (ii)", "X",
    "**(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation,",
    "**(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation,",
    "The Part XV label, renamed; 'rules out as a non-explanation' reads both ways.")
add(540, "atria A 4; mimo 1 4", "X",
    "**(C) Reinstatement of kinds.**",
    "**(Elim) Reinstatement of kinds.**",
    "The Part XV labels, renamed.")
add(540, "mimo 4 F9 (i)", "X",
    "would rule out the Claim of Argument 1,",
    "would rule out the Consequence of Argument 1,",
    "The kind-label case bears on the Consequence (the word 'kind' eliminable), not on the signature Claim.")
add(542, "atria A 4; mimo 1 4", "X",
    "**(D) Genesis.**",
    "**(Prov) Genesis.**",
    "The Part XV labels, renamed.")
add(544, "atria A 4; mimo 1 4", "X",
    "**(E) Question-finding.**",
    "**(QF) Question-finding.**",
    "The Part XV labels, renamed.")
add(556, "glm A 1", "X",
    "\\operatorname{proj}_{V_k}\\operatorname{Sol}_{\\lambda(k)}(a,b)",
    "\\operatorname{proj}^{\\lambda}_{V_k}\\operatorname{Sol}_{\\lambda(k)}(a,b)",
    "As at l. 233; Argument 1's reasons use the same projection.")
add(562, "mimo 4 F9 (ii)", "X",
    "with port translations onto the same ports of \\(D\\)",
    "with port translations that are bijections onto the same ports of \\(D\\)",
    "The argument's reasons compose one translation with the inverse of the other.",
    claim_changed=True)
add(568, "mimo 4 F2", "X",
    "and must supply it. The remedy is a finer contract, which is a new question.",
    "and must supply it. A finer contract that contains such a change is a new question (Part III); whether anyone asks it is that person's choice (Part 0).",
    "'The remedy is' names what must happen (S21); 'must supply it' is a condition on a claim and stays.")
add(582, "mimo 4 F4", "X",
    "Surprise is defined as a violation of a selected transport at \\((a,b)\\notin H\\). If there is no transport there is no prediction and hence no violation. If \\(H=C\\), every occurring \\((a,b)\\) is in \\(H\\), so no violation at \\((a,b)\\notin H\\) exists.",
    "Surprise is defined (Part IV) as a violation of a selected transport at an occurring \\((a,b)\\in C\\) with \\((a,b)\\notin H\\). If there is no transport there is no prediction and hence no violation. If \\(H=C\\), every such \\((a,b)\\) is in \\(H\\), so no violation at a pair of \\(C\\) outside \\(H\\) exists.",
    "Part IV (l. 217) defines surprise only at occurring pairs of C; the reasons now say so.")
add(588, "mimo 4 F7", "X",
    "**Claim.** A contract \\(C\\) is an organization (a set of edits with a query), and can be the content \\(c\\) in (G).",
    "**Claim.** A contract \\(C\\), taken with its edits and its query, can be given the structure of an organization in the sense of (O), and can be the content \\(c\\) in (G).",
    "The reasons build the organization; the claim now says what they give.",
    claim_changed=True)
add(590, "mimo 4 F7", "X",
    "components (the closure conditions), and admitted edits",
    "components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits",
    "(O) asks for a relation for each component.")
add(596, "mimo 4 F1", "X",
    "together with declared indices and declared inputs.",
    "together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.",
    "The reasons end at (O) and (Q) as well.")
add(600, "mimo 4 F11", "X",
    "a theory of reasons.",
    "a theory of appraisal.",
    "The second import is the appraisal relation (l. 31, l. 518).")
add(608, "mimo 4 F12", "X",
    "Goalpost-moving is the act of changing the index without recording the change, and it is a failure of the record, not an operation the semantics admits.",
    "Goalpost-moving is the act of passing off a claim at one index as a claim at another; it is not an operation the semantics admits, since every claim is relative to its declared index (Part XIV).",
    "The index does the work, not a record (S20: 'A record is redundant').")
add(612, "mimo 4 F8", "X",
    "Transporting all carriers, relations, transports, histories, and contracts along structure-preserving bijections preserves (E), (G), (P), (EX). *Why this and not its denial.* Each is a conjunction of equalities and existence claims over the transported data; bijections preserve them.",
    "Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX). *Why this and not its denial.* Each is a conjunction of equalities and existence claims over the transported data, the declared aims and occasions of (P) and (EX) among them; bijections preserve them.",
    "(P) and (EX) depend on the declared aims with their occasions (l. 526).",
    claim_changed=True)
add(622, "mimo 4 F4", "X",
    "A simulation layer \\(S_0\\) with a transport \\(t_0\\) selected on a history \\(H_0\\) containing displacements and velocity changes but no occlusions.",
    "A simulation layer \\(S_0\\) with a contract \\(C_0\\) containing the occlusion edit, and a transport \\(t_0\\) selected on a history \\(H_0\\subsetneq C_0\\) containing displacements and velocity changes but no occlusions.",
    "The example cites Argument 4 without stating the contract the occlusion lies in.")
add(626, "mimo 4 F6 (i)", "X",
    "They are objects because they respond as objects do to what the contract admits.",
    "On this contract the word adds nothing to the signatures they already have (Argument 1).",
    "The sentence brought back a kind-label and read as circular.")
add(630, "mimo 4 F6 (ii)", "X",
    "is a claim that some admitted change distinguishes them, and on this contract none does.",
    "is a claim that some admitted change separates the two pairings of persistence components to things, and on this contract none does.",
    "'Them' was the pairings here and the things in the next sentence.")

J = {
    "about": ("S96 Repair, stage 3 (log S97): the FIX rulings of the reading of the outside cross-examination "
              "(results/S96 Reading of the replies.md) and the owner's two points of decision S28, applied by "
              "repair_apply.py --stage3 to the S96 final text (md5 8bb4d19d5aad53de2492b2193fd23ff1). Made by "
              "replacements_stage3_source.py. Groups: X = a reply's challenge taken up; O = decision S28; N = the dated note."),
    "groups": {"X": "a reply's challenge taken up (ruling ids as in the reading)",
               "O": "decision S28 (i) and (ii)",
               "N": "the dated note at l. 2"},
    "entries": E,
    "not_applied": [],
    "borderline": [],
    "physical_mentions": {},
}

if __name__ == "__main__":
    extra = os.path.join(HERE, "replacements_stage3_extra.json")
    if os.path.exists(extra):
        X = json.load(open(extra, encoding="utf-8"))
        for k in ("not_applied", "borderline"):
            J[k] = X.get(k, [])
        J["physical_mentions"] = X.get("physical_mentions", {})
    json.dump(J, open(os.path.join(HERE, "replacements_stage3.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("stage 3 entries:", len(E), " claim changed:", sum(1 for e in E if e["claim_changed"]))
