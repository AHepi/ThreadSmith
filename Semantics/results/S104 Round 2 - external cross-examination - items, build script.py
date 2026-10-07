# S104 round 2: the external cross-examination the owner supplied, as items E01-E22.
# Run from the repository root:  python3 "Semantics/results/S104 Round 2 - external cross-examination - items, build script.py"
# It compares the md5 of the text under review and of the saved document, compares every quotation of
# the text with the line it names (each fragment, " … " joining fragments of one line, must stand in
# that line) and every quotation of the document with the document (and with the lines of it the item
# names), does the same for the quotations in the two maths addenda, and writes
#   Semantics/results/S104 Round 2 - external cross-examination - items.md and .json
# It refuses on any mismatch. Standard library only; it reads nothing in the returns folder.
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEM = os.path.join(ROOT, "Semantics")
TEXT = os.path.join(SEM, "tests", "103 The semantics, standing alone, after round 1.md")
TEXT_MD5 = "f31ebb1f050783f1a84f6136cec20fcd"
DOC = os.path.join(SEM, "results", "S104 Round 2 - external cross-examination supplied by the owner.txt")
DOC_MD5 = "3aeed4029848cc8ad375f314123eaf66"
OUT_MD = os.path.join(SEM, "results", "S104 Round 2 - external cross-examination - items.md")
OUT_JSON = os.path.join(SEM, "results", "S104 Round 2 - external cross-examination - items.json")
MATHS = os.path.join(SEM, "results", "S104 Round 2 - maths")
ADDENDA = [os.path.join(MATHS, "formal claims - addendum for the external examples.md"),
           os.path.join(MATHS, "inventions register - addendum for the external examples.md")]

YES = "yes"
DOUBT = "in doubt: goes to a checker (reading rule, rule 5)"
NO = "no: no line challenged"
SCOPE = "a finding about scope (section 3): no line challenged"

ITEMS = [
    dict(id="E01", section="1", title="What it finds stands", doc=(13, 21),
         place=[(245, "(F1) prevents an assembled match from hiding a decomposition in error. (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint."),
                (211, "A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails."),
                (407, "An inexplicit representation is not an absent one."),
                (409, "A system's realization can use a partial, distributed, or temporally extended representation."),
                (159, "a narrowing adopted after a failure is a new claim at a new index (Part VIII)"),
                (367, "A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim.")],
         check="Its descriptions (the three fidelities together; a representation of a theory in error against an erroneous representation; inexplicit, distributed and temporally extended representation; a narrower claim as a new index) match these lines of file 103.",
         finding="Requiring component, global and question fidelity together keeps an answer that matches the target's from vindicating a proposed mechanism; the text keeps a representation of a theory in error apart from a representation in error, admits inexplicit, distributed and temporally extended representation, and treats a narrowing after a failure as a new claim at a new index. These are strengths; they do not show that the class captures everything called explanatory creativity.",
         evidence="Its reading of the text's wording; no example.",
         repair=[],
         words=["The strongest part is the combination of component fidelity, global fidelity, and question fidelity. Requiring all three prevents a correct answer from automatically vindicating the proposed internal mechanism.",
                "These are substantive strengths. But they do not establish that the resulting class captures everything that deserves to be called explanatory creativity."],
         challenges=NO, note="What it says stands counts for nothing either way (addendum, point 5). Its closing sentence bears on L17 through E22.",
         fc=["FC19 ((F1) and (F2) do different work): holds on all models tried",
             "FC95 (a system can represent a theory in error): holds on all models tried",
             "FC99 (Argument 7: an account on C can fail on C'): holds on all models tried",
             "FC68 (a failed answer stays failed): holds on all models tried"],
         cex=[], inv=["I48", "I52", "I65"], chk=[], nf=["NF09 (L407)"], repro=None),

    dict(id="E02", section="2.1", title="The contribution test can make irrelevant material \u201cindispensable\u201d", doc=(25, 85),
         place=[(287, "Fix \\(\\mathcal E\\) and a declared restriction operation. For \\(W\\subseteq\\Gamma\\), let \\(E|W\\) retain the commitments in \\(W\\) with the named background fixed; the commitments of \\(E|W\\) are \\(W\\)."),
                (231, "those the candidate offers as doing the work, whether or not anyone has described their work"),
                (231, "for \\(E|W\\), \\(t'\\) is \\(t\\) with \\(\\lambda\\) restricted to the components of \\(E|W\\), and \\(\\Gamma'\\) is \\(W\\)."),
                (103, "A deleted component imposes the full relation on its ports."),
                (296, "\\operatorname{CriticalBlock}(B;W,p)\\iff W\\in\\mathsf S_{E,p}\\land W\\setminus B\\notin\\mathsf S_{E,p}. \\tag{B}"),
                (299, "Criticality is relative to the route \\(W\\) it is assessed in"),
                (305, "and \\(d\\) is **globally indispensable**, \\(\\Gamma\\setminus\\{d\\}\\notin\\mathsf S_{E,p}\\), exactly when \\(d\\in\\bigcap\\min\\mathsf S\\)"),
                (313, "**Commitments that do no work.** (E) has no condition that each commitment do work. … A commitment \\(d\\) of a candidate that has a route does no work by itself in it when every route stays a route after \\(d\\) is added to it and after \\(d\\) is removed from it")],
         check="Its descriptions (a route as a subset of commitments that still meets Account; a critical block as one whose deletion destroys that status; deletion keeping the ports; commitments that do no work) match L287\u2013L313 and L103 of file 103.",
         finding="A critical block (B), and with it \u201ccontributory\u201d, \u201cglobally indispensable\u201d and \u201cdoes no work by itself\u201d, is failure of Account after deletion, and Account's (F2) can fail for a reason the question does not turn on; so a commitment that plays no part in the answer can come out critical and globally indispensable. The definitions run together indispensability to the fidelity of the whole organization and contribution to explaining the question.",
         evidence="Its Boolean example: k: Y = X and d: V = U, identity transports, \u0393 = {k, d}, the baseline and every partial setting of X and U (nine edits), unset inputs zero. The full candidate meets the conditions; with d deleted, V is unconstrained, (F2) fails, and the answer about Y is unchanged at every pair, so CriticalBlock({d}; {k,d}, p) holds and d is globally indispensable. It weighs two defences: that d should not have been among the commitments (answered: L313's test is meant to find commitments that do no work, and asking for the relevance judgment first defeats it), and a restriction that removes the disconnected ports (answered: it needs a different restriction operation from the one with an unchanged identity projection).",
         repair=["Distinguish structural-fidelity criticality from question-relative explanatory contribution. The latter needs a relevance condition or an explicit question-preserving reduction, not merely failure of Account after deletion."],
         words=["The definition conflates indispensability to the fidelity of the whole represented organization with contribution to explaining this question.",
                "A demonstrated classification problem in the interpretation of explanatory contribution. It is not, by itself, a refutation of Account sufficiency: the full candidate still explains Y through k."],
         challenges=YES, note="It bears on L287\u2013L313 (and, through \u201cthe work\u201d, on L231); its own verdict is that it does not rule out sufficiency (L536).",
         fc=["FC37 (the finite monotone claim): holds on all models tried; the example leaves it as it is (FC-E1)",
             "FC41 (commitments that do no work): holds on all models tried, on set systems (I30), not on routes computed from a candidate",
             "FC38, FC39, FC40, FC42 (the route examples read as set systems, I30): hold on all models tried",
             "FC101 (Argument 9; uses I29): holds on all models tried"],
         cex=["none of the twelve falls on these lines"],
         inv=["I29 (the restriction operation: deletion, ports and π kept; its first other choice, removal, is made exact as I104 in the addendum)", "I30", "I15"],
         chk=["\u00a72b, I29's row: L231's wording and the register's choice (deletion keeps J_E whole, so \u03bb 'restricted to the components of E|W' restricts nothing)"],
         nf=[], repro="FC-E1: CONFIRMED on the text under review (resting on I29 and I103; variant (a\u2032), d in the named background, meets (E) with \u0393 = {k}; variant (b\u2032), the restriction of I104, removes the example and changes \u03c0, which L231's wording does not)"),

    dict(id="E03", section="2.2", title="Representation and construction appear to depend on each other", doc=(87, 121),
         place=[(208, "\\operatorname{Rep}_\\ell(o,c)\\iff\\exists t\\,[\\operatorname{Faithful}_C(t:\\operatorname{Org}_\\ell(o)\\to c)\\land(\\operatorname{Sel}(t)\\lor\\operatorname{Con}(t))]. \\tag{R}"),
                (197, "**Constructed.** There is an episode (Part X) whose construction trace prepares \\(t\\), and in which \\(t\\), or the organization it carries to, is available as a represented target."),
                (405, "\\(\\operatorname{Build}_{\\beta,\\ell}(s,c,h,e)\\) is met when an actual subhistory owned by \\(s\\) and delimited at \\(e\\) prepares a represented organization for explanatory use of \\(c\\)"),
                (405, "A construction trace identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation."),
                (526, "(R) depends on (F1)\u2013(F2) and physical provenance. … Build depends on histories, Ownership and (E). … The order has no cycle and no endless descent. A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order"),
                (520, "Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII).")],
         check="Its schematic 'Rep \u21d4 Faithful \u2227 (Sel \u2228 Con)' is (R) at L208; 'construction is described as preparing a represented organization, and its trace includes the resulting representation' matches L405; 'its stated dependency order omits the apparent dependence of Build on representation and then asserts that there is no cycle' matches L526, which lists Build under histories, Ownership and (E); the warning it credits is L526's last sentence.",
         finding="Read literally, (R) needs Sel or Con, Con needs a construction trace, and Build's trace prepares \u201ca represented organization\u201d and names \u201cthe resulting representation\u201d, so Rep \u2192 Con \u2192 Build \u2192 Rep; L526's order lists Build without (R) and says the order has no cycle. L526's warning names the risk and does not supply the missing construction.",
         evidence="The dependencies read from the wording of the definitions; a stripped-down instance ('This occurrence represents because it was constructed; it was constructed because the relevant physical process produced this representation'); no model.",
         repair=["Define a raw physical construction relation first. Its premises may refer to representations at strictly earlier stages; its output should initially be a carrier with specified structural properties. Then derive representation of that output. A ranked inductive definition would make the intended grounding explicit."],
         words=["Rep \u2192 Con \u2192 Build \u2192 Rep.",
                "\u201cConstruction trace\u201d is intended to be independently recognizable from physical processes, role bindings, and transformations, without applying Rep to its output.",
                "That could work. But it needs to be the actual definition.",
                "An unresolved foundational dependency, not a proof that no coherent version of the framework exists."],
         challenges=YES, note="It bears on L197, L405 and L526 (and on Argument 6 at L596, which rests on L526's order).",
         fc=["FC98 (Argument 6 and the dependence order): not tested (a property of the definitions' graph); its Look names the same loop, build \u2192 prov \u2192 rep",
             "FC78, FC81 (d), FC82, FC83: counterexamples on the same definitions (Con, Build), each resting on I56 with Prepares set by hand (I90); they bear on the exclusivity of the provenances, not on the loop"],
         cex=["FC78, FC81 (d), FC82, FC83 (above); none on the loop itself"],
         inv=["I56 (Prepares, BindingConstruction and TransferComposite as primitives: the formal core's way of keeping the loop open, D18.1)", "I52", "I53", "I48", "I90"],
         chk=["formal core D18.1: 'with \u201crepresented\u201d read through (R), Build, Con and Rep are defined together, as one fixed point, unless Con's trace is read without (R)'", "H05, T15 (Sel limited by L195; L201 and L411 left out)"],
         nf=[], repro="none: a matter of the order of the definitions, not of a model (FC98 was not tested for the same reason)"),

    dict(id="E04", section="2.3, first half", title="Functional determination does not uniquely identify outputs", doc=(123, 145),
         place=[(109, "No role assignment is supplied."),
                (109, "A port is an **output** of component \\(j\\) when its value is determined by \\(L_j\\) given the other ports of \\(V_j\\) across \\(B\\)."),
                (109, "The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read."),
                (103, "An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one."),
                (119, "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it"),
                (325, "Under \\(A\\) containing interventions on \\(H\\) and \\(\\theta\\), these ports are inputs and \\(L\\) is an output, by Part II.")],
         check="Its paraphrase of the output clause and of 'replacing the component that \u201cassigns\u201d the port' matches L109 and L103.",
         finding="L109's output criterion makes both ports of the relation {(0,0),(1,1)} outputs, so it does not tell Y := X from X := Y; the edits tell them apart only once it is said which component an intervention replaces, and \u201cthe component assigning that port\u201d is neither defined from the edits nor supplied with the data.",
         evidence="The relation {(0,0),(1,1)} on two two-valued ports, and 'A finite check'.",
         repair=["That assignment relation needs either an independent definition from the edit structure or explicit inclusion in the supplied data."],
         words=["Thus the literal criterion classes both ports as outputs. It does not distinguish the assignment Y := X from X := Y. A finite check confirms that directly.",
                "Repairable under-specification."],
         challenges=YES, note="It bears on L103, L109 and L119 (and on L325's 'by Part II').",
         fc=["FC02 (c): on the pole, H and \u03b8 are outputs of c_L as well as L, and the direction is carried by asg, not by output status: holds",
             "FC11 (roles relative to A, families relative to C; round-1 matter 5): holds", "FC06: holds"],
         cex=["none of the twelve falls on these lines"],
         inv=["I04 (the assigning component read off the setting edits; its other choice (b), the unique component of which v is an output, 'fails for relational components')", "I05", "I80", "I102"],
         chk=["H03, H04 (direction defined as (Input_A, asg), with no invention number)", "T13, R14 (the identity edit as a setting edit)", "R21 (output read at the identity edit)", "formal core \u00a72, the Vague note"],
         nf=[], repro="FC-E2: CONFIRMED on the text under review (resting on I05 and I105; the same under I106 (a); only under I106 (b) does output status follow the direction, and then through the setting edits that replace k)"),

    dict(id="E05", section="2.3, second half", title="The families of signatures do not give a sharp classification; kinds beyond the signatures", doc=(140, 145),
         place=[(121, "What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:"),
                (123, "- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;"),
                (124, "- a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;"),
                (125, "- a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule."),
                (127, "These are descriptions of patterns in (K), not additional data. … In particular, a part that reads or reports another part has a measurement's signature … Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."),
                (11, "at any level of detail, a *kind* is nothing over and above how a component responds to the changes that level admits."),
                (558, "The word \"kind\" is therefore eliminable from the definition of an account, and its elimination loses no case.")],
         check="Its 'proposed signatures of causal assignments, measurements, and rule applications' are L123\u2013L125 of file 103 (L123 as changed in round 1); 'the sharp semantic classification the surrounding prose suggests' points to L121 and L127.",
         finding="A causal assignment Y := X and a measuring component N := X both keep their relation under an upstream intervention on X, so the families of L123\u2013L125 cannot tell them apart by that; the patterns do not give the sharp classification the prose around them suggests. Argument 1 keeps the text's own signatures under (F1); it does not show that those signatures exhaust every important sense of kind.",
         evidence="Y := X against N := X under an intervention on X.",
         repair=[],
         words=["For a component Y := X, intervening upstream on X changes the solution but normally leaves the relation Y = X unchanged. A measuring component N := X has the same property. Their distinction cannot come merely from whether their own relation changes under that upstream intervention.",
                "This is not an argument that measurements cannot be causal processes; they can be. It is an argument that the listed patterns do not automatically provide the sharp semantic classification the surrounding prose suggests.",
                "Argument 1 establishes preservation of the document\u2019s defined signatures. It does not independently establish that those signatures exhaust every scientifically important sense of kind."],
         challenges=DOUBT, note="For L121\u2013L127: whether they say more than the patterns give. For L11 and L558: a question of scope, which bears on (Elim) at L540.",
         fc=["FC07 (under R-i a component that reads a port other than its output is a measurement and not causal on a contract that sets its output; the families differ between the readings on the pole's contract; round-1 change L123): holds",
             "FC08 (L127's gloss has a clause about solutions), FC09 (four names, three families; round-1 matter 4), FC10 (L57 against L123), FC12, FC13, FC14, FC17: hold",
             "FC18 (Argument 1's Consequence): counterexample under I94, a reading the text excludes (the check's T03)"],
         cex=["FC18 (above)"],
         inv=["I06 (the two readings of observation edits)", "I07", "I08", "I09", "I102"],
         chk=["H01 and R13 (a composite of settings is no setting edit)", "H02", "R01 (R-i against R-ii)"],
         nf=["NF04 (L540, (Elim))"], repro="FC-E3: CONFIRMED on the text under review (resting on I06 under both readings and I107; an edit that alters the reading's relation alone separates them)"),

    dict(id="E06", section="2.4", title="The proposed falsification tests are narrower than some of the claims", doc=(147, 173),
         place=[(17, "A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it; so would a candidate that meets (E) on its question and contract (Part V) when such an argument rules out the claim that it is an explanation there."),
                (61, "(Suff) sufficiency of the four conditions of Account; (Nec) their necessity"),
                (536, "A candidate meeting all four conditions of (E) on a contract of its question, with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks."),
                (538, "A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target."),
                (277, "(E) has no condition on how a mechanism came to be guessed")],
         check="Its 'Part XV asks for a candidate whose organization cannot be preserved by any transport under any contract on its target' matches L538; 'the sufficiency challenge adds a non-declared-provenance requirement' matches L536; 'explicitly does not depend on how the mechanism was guessed' matches L277.",
         finding="The denial of necessity on a question p is a candidate that explains p and fails Account on p's contract; L538 asks instead for a candidate whose organization no transport preserves under any contract on its target, a much stronger demand. L536 adds to sufficiency a transport whose provenance is not declared, though (E) takes no provenance. A critic can then defeat one claim while the text answers with a weaker one.",
         evidence="The two forms it writes out: 'Explains(E,p) \u21d2 Account(E,p)' on a specified question, against representability somewhere under some contract.",
         repair=["The statements of the central claims and their admissible refutations need to be aligned. Otherwise, a critic can defeat one claim while the document answers by defending a weaker one."],
         words=["But Part XV asks for a candidate whose organization cannot be preserved by any transport under any contract on its target. That is a much stronger demand on the critic.",
                "Likewise, the sufficiency challenge adds a non-declared-provenance requirement, although Account itself does not require that provenance and explicitly does not depend on how the mechanism was guessed."],
         challenges=YES, note="It bears on L17, L536 and L538 (and on L61's summary).",
         fc=["FC30 ((E) takes no assessor, history, provenance or wording): holds", "FC31 ('the four conditions', five conjuncts, L536): not tested"],
         cex=["none of the twelve falls on these lines"], inv=["I20", "I27", "I28", "I49"], chk=[],
         nf=["NF01 (L17)", "NF02 (L536)", "NF03 (L538)"], repro="none: it concerns how the claims and their refutations are stated"),

    dict(id="E07", section="3.1", title="Neural readout against causal mechanism: a successful test", doc=(187, 223),
         place=[(151, "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second."),
                (37, "A correlation has no component that responds to an intervention on its supposed input; a cause does."),
                (127, "Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."),
                (159, "Why the question asked is answered on this restriction and not on a wider one is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that decides it."),
                (606, "and \\(\\mathcal E\\) can meet (E) on \\(C\\) and fail it on \\(C'\\).")],
         check="No sentence of the text is described; the example is its own, worked with the text's conditions.",
         finding="On the memory system M := X, N := M, Y := M, the proposal Y := N meets the matching conditions on cue changes and fails (F1), (F2) and answer fidelity once the contract holds X = 1, do(N = 0); the text forces the distinction between a scoped dependence and a causal attribution. The formalism does not find which intervention isolates the readout, or whether a manipulation also changes the memory.",
         evidence="The memory example, with its values at X = 1, do(N = 0): target M = 1, N = 0, Y = 1; proposal Y = 0.",
         repair=[],
         words=["In the finite implementation, this intervention breaks F1, F2, and answer fidelity.",
                "This is a real success for the framework. It forces the distinction between an adequate scoped dependency and a stronger causal attribution.",
                "The formalism does not discover which neural intervention isolates the readout, or whether an experimental manipulation also changes memory. Those are substantive empirical assumptions."],
         challenges=SCOPE, note="What it credits counts for nothing either way (addendum, point 5).",
         fc=["FC99 (Argument 7): holds", "FC26, FC27, FC28 (the pole on the production and identification contracts): hold",
             "FC34, FC36: hold", "FC35 (L151's 'prediction' is outside L219's definition; round-1 matter 6): not tested", "FC101 (Argument 9): holds"],
         cex=["none of the twelve falls on these lines"], inv=["I51", "I65"], chk=["R09 (the identification contract's edits as boundary variations)", "R10"],
         nf=["NF08 (L151)"], repro="FC-E4: CONFIRMED on the text under review (resting on I108)"),

    dict(id="E08", section="3.2", title="Surprise: the clearest cognitive mismatch", doc=(225, 273),
         place=[(221, "- **surprise** is a violation of a selected transport at \\((a,b)\\notin H\\)."),
                (223, "a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise"),
                (584, "Surprise is not a feeling added to the semantics; it is the signature of a selected transport meeting a change outside its history."),
                (25, "a probability on claims")],
         check="Its 'surprise as a fidelity violation by a selected transport at an encountered pair outside its selection history' and 'a constructed transport can be violated, but its violation is explicitly not surprise' match L221 and L223.",
         finding="(A) A probabilistic model can be faithful and still meet an unexpected outcome (P(B) = 0.01, about 6.64 bits): unexpectedness does not need an unfaithful representation, so identifying surprise with fidelity failure leaves part of the phenomenon out. (B) Two agents with the same expectation and the same response differ only in how the expectation was acquired; the text calls one violation surprise and the other not, and a cognitive application needs an argument that this difference of history marks a difference in the process studied. It grants that the definition is consistent and that Argument 4 follows from it.",
         evidence="The probability example (\u2212log2 0.01 = log2 100 \u2248 6.644, arithmetic outside the S104 model, which has no probabilities; the text supplies none on claims, L25, L522); the two agents.",
         repair=["Distinguish statistical unexpectedness, subjective prediction discrepancy, recognized model inadequacy, and the provenance of the expectation. Those can interact without being defined as the same thing."],
         words=["Unexpectedness does not require an objectively unfaithful representation.",
                "That distinction may be useful for classifying histories. But a cognitive application needs an argument that this historical distinction identifies a relevant difference in the psychological process being studied.",
                "A strong coverage objection to a general cognitive application, not a counterexample to the definitional theorem."],
         challenges=SCOPE, note="Its point (B) meets FC81 (d): on the formal core, without L201 and L411 (H05), one transport can be selected and constructed on one history and be surprised.",
         fc=["FC81 (Argument 4): counterexample in part (d), resting on I52, I53, I56, I90",
             "FC82: counterexample (a transport the result of both responses)", "FC20 (violation in either extent): counterexample with non-injective value maps",
             "FC102 (a) (surprise in the worked case): not tested"],
         cex=["FC81 (d)", "FC82"], inv=["I50", "I51", "I52", "I53", "I56", "I90"], chk=["H05, R11 (Sel limited by L195)", "H07 (surprise with the selection parameters bound by 'for some')", "H08"],
         nf=[], repro="none in the S104 model (the probability example is arithmetic, checked by hand)"),

    dict(id="E09", section="3.3, first part", title="Infant exploration: representable, but not yet classified", doc=(275, 300),
         place=[(632, "This episode is a relative-consistency instance for the class. It is not a claim that any actual infant, animal, or program instantiates it."),
                (405, "Reconstruction by a learner is construction; relay is not."),
                (407, "None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format"),
                (409, "A construction trace may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it"),
                (429, "A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it.")],
         check="Its 'It explicitly says this is not an attribution to an actual infant, animal, or program' matches L632; 'The document allows tacit representations' matches L407\u2013L409.",
         finding="Behaviour after an expectation-violating event is compatible with the framework, but does not show that the learner represented a defect in its own account, or built a new binding rather than recruiting an existing capacity; allowing tacit representation does not show that the representations Build or a critical episode need were present. Representability succeeds while the empirical classification stays underdetermined.",
         evidence="Its two cross-examination questions; no example worked.",
         repair=[],
         words=["What evidence determines that the infant represented a defect in its own account, rather than changing attention or exploratory behavior after an unexpected event?",
                "The document allows tacit representations, so demanding verbal reports would be an unfair test. But allowing tacit representations does not establish that the particular representations required by Build or a critical episode were present.",
                "The empirical behavior is compatible with the framework. It does not identify the framework\u2019s proposed internal provenance or establish CreateEx."],
         challenges=SCOPE, note="",
         fc=["FC90 (the worked case's '(EX) is met' against (EX)'s conjuncts): not tested", "FC83, FC84 (only construction is originative; every creative attribution requires construction): FC83 a counterexample, FC84 holds"],
         cex=["FC83"], inv=["I55", "I56", "I60", "I68"], chk=["H15 (the four parts of a critical episode)"],
         nf=["NF09 (L407)", "NF10 (L429)"], repro="none"),

    dict(id="E10", section="3.3, second part", title="\u201cPredicts from occupancy\u201d does not fix a memoryless predictor", doc=(295, 295),
         place=[(620, "The sensory field is the occupancy of cells, which cells are filled, without which thing fills them."),
                (622, "\\(S_0\\) predicts occupancy from recent occupancy. It is faithful on \\(H_0\\)."),
                (624, "\\(S_0\\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity."),
                (626, "If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.")],
         check="Its 'the document's final example describes a selected occupancy predictor failing under occlusion' matches L620\u2013L626.",
         finding="A predictor from occupancy histories can carry information through an occlusion, so \u201cpredicts from occupancy\u201d does not by itself give a memoryless predictor; for no member of a selected population to survive the extended history, the population's state and memory restrictions have to be stated, not only its sensory input.",
         evidence="The remark; no model worked.",
         repair=["To establish the claimed impossibility for a selected population, one must specify its state and memory restrictions, not just describe its sensory input."],
         words=["There is also a technical caution about the occupancy example. \u201cPredicts from occupancy\u201d does not, by itself, establish a memoryless architecture. A predictor using occupancy histories may preserve information through occlusion."],
         challenges=YES + " (a finding of section 3 that bears on sentences of the text, L622 and L626; addendum, point 7)", note="The same point as the S104 counterexample to FC102 (b), which the reading rule already sends to a checker (rule 5, the twelve).",
         fc=["FC102 (b), second half: counterexample (computed: not as claimed): on I68's encoding with I100's occlusion, a window longer than the occlusion lets an occupancy predictor extrapolate, so the failure is not structural; with two things a window predictor can fail with no occlusion at all",
             "FC102 (b), first half (an occlusion that outlasts the window): computed as claimed; (a), (c): not tested"],
         cex=["FC102 (b), second half"], inv=["I68", "I100", "I52"], chk=["H17 (two things that may share a cell and pass through each other)", "R22"],
         nf=[], repro="none new: FC102 (b) is the S104 computation of the same point"),

    dict(id="E11", section="3.4", title="Model-based learning: no ready-made psychological distinction", doc=(302, 328),
         place=[(13, "Creativity lives in construction. Selection produces the raw material construction works on."),
                (225, "A **selection response** extends the history \\(H\\) of a selected transport and lets \\(\\mu\\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace."),
                (584, "The two responses, extend \\(H\\) and re-tune, or construct a new transport, are the difference between learning and creating")],
         check="No sentence of the text is described; it warns against a mapping the text does not make.",
         finding="Selection is not model-free learning and construction is not model-based learning: planning can use a learned model through a retained procedure with no new binding, and criticism can revise a simple value-based policy. The two distinctions concern different things, and trial-by-trial predictions come from supplied mechanisms, not from Account or provenance.",
         evidence="Reinforcement-learning research, named and not cited.",
         repair=["A cognitive application must measure both rather than substituting one for the other."],
         words=["In the present semantics, however, model-based planning need not automatically be construction. A system can use a learned transition model through a retained procedure without newly constructing a binding or criticizing a represented target during the relevant episode.",
                "Potentially useful descriptive structure, but not yet a psychological process theory."],
         challenges=SCOPE, note="",
         fc=["FC82, FC83 (the two responses; only construction originative): counterexamples resting on I52, I56, I90", "FC84: holds"],
         cex=["FC82", "FC83"], inv=["I52", "I53", "I56", "I90"], chk=["H05, H08, R11"], nf=[], repro="none"),

    dict(id="E12", section="3.5", title="Finding questions: recording the event is not explaining its occurrence", doc=(330, 347),
         place=[(15, "A question, meaning its target, its scope of admitted changes and what it asks, can be found as well as answered, and the semantics represents both (Part III, Argument 5)."),
                (588, "Hence an episode whose originative contribution is a new contract meets (G) and, where the other conjuncts are met, (EX)."),
                (592, "Finding a new question, by an owned construction (G), is a creative act, as answering one is."),
                (544, "A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture")],
         check="Its 'Treating questions as constructible contents' matches L15 and L588\u2013L592.",
         finding="The semantics can record that an agent changed a target, its admitted changes or its query, and supplies no mechanism that selects which change occurs; Argument 5 gives an encoding, not a theory of why particular questions are found. That is a problem only where representability is treated as the explanatory achievement itself.",
         evidence="Two questions a cognitive account would face.",
         repair=[],
         words=["The semantics can record changes in aims, hypotheses, and questions. What it does not yet supply is the mechanism selecting one of those changes.",
                "Argument 5 establishes an encoding possibility, not a theory of why particular questions are found."],
         challenges=SCOPE, note="",
         fc=["FC97 (Argument 5: a contract can be an organization and a content): holds"], cex=[], inv=["I01", "I48", "I67"], chk=[],
         nf=["NF06 (L544)"], repro="none"),

    dict(id="E13", section="4.1", title="Declared indices: objective, or merely conditional", doc=(351, 369),
         place=[(31, "Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them"),
                (43, "What is independent of the modeller lies in the target and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record."),
                (159, "the semantics records the restriction and supplies no rule that decides it"),
                (473, "Both are declared before the attribution, not chosen after it."),
                (522, "where the input is missing, the assessment is left open and the semantics says so rather than choosing the input from the assessment wanted."),
                (608, "Goalpost-moving is the act of passing off a claim at one index as a claim at another")],
         check="Its 'The document explicitly leaves the justification of a restricted scope as a substantive, criticizable input' matches L159.",
         finding="A fact can be objective relative to a contract, but the assessment turns on the target, grain, decomposition, counterparts, admitted changes and scope; recording them makes adjustment after the result visible and does not show that the question is the one a theory needed to answer. Without a procedure the framework risks becoming a precise language for whatever interpretation the investigator already favours.",
         evidence="Its argument; no example.",
         repair=["For cognitive-science applications, the protection should be procedural: specify the relevant grain, contrasts, component mappings, and admissible revisions before testing the decisive cases."],
         words=["How much of the desired classification can be obtained by choosing those inputs after seeing the result?",
                "Recording those choices makes retrospective adjustment visible. It does not establish that the resulting question is the one a scientific theory needed to answer."],
         challenges=DOUBT, note="The text asks for declaration before attribution for boundary and continuity (L473) and records scope (L159, L522); whether grain, counterparts and contrasts call for the same is the question. Its decisive question (section 7, E22) is the same point.",
         fc=["FC30, FC99: hold", "FC32 (L520 against L526's order): not tested", "FC50 (a narrowed contract leaves the problem on p): holds"], cex=[], inv=["I27", "I28", "I85"], chk=[], nf=[], repro="none"),

    dict(id="E14", section="4.2", title="Selection and construction: separate mechanisms, or separate labels on histories", doc=(371, 384),
         place=[(201, "Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both."),
                (47, "Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain"),
                (77, "Neither is reduced to the other."),
                (411, "Construction is not selection. A selected transport has no represented target in its history; a constructed one does."),
                (542, "a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics)")],
         check="Its 'The prohibition on represented targets in selected histories' matches L195, L201 and L411; 'The qualified underdetermination result in Argument 3' is L572\u2013L576.",
         finding="Argument 3's qualified underdetermination stands, with the population restriction doing the work, but it gives no general discontinuity between selection and construction: an evolutionary search with represented candidates, counterexamples and content-sensitive revision would count as construction, so \u201cselection\u201d here is narrower than variation and selection in general, and the ban on represented targets in selected histories gives a difference of classification, not of mechanism.",
         evidence="An evolutionary search procedure with represented candidates and revision.",
         repair=["Identify what a construction mechanism does that is not already captured by the independently specified physical processes, representations, memory, and feedback in its history."],
         words=["The qualified underdetermination result in Argument 3 is sound: if two transports survive the same history and differ elsewhere, survival on that history does not distinguish them there. The population restriction is doing important work.",
                "The prohibition on represented targets in selected histories guarantees a classificatory difference. It does not, by itself, establish a mechanistic irreducibility result."],
         challenges=DOUBT, note="Whether L47, L77, L201 and L542 claim more than a difference of classification.",
         fc=["FC78 (exactly one of three provenances): counterexample under D12.1, resting on H05 (L201 and L411 left out of Sel)", "FC80 (Argument 3): holds", "FC84: holds"],
         cex=["FC78"], inv=["I52", "I53", "I54", "I90"], chk=["H05, T15, R11"], nf=["NF05 (L542)", "NF07 (L201)"], repro="none"),

    dict(id="E15", section="4.3", title="Exact fidelity and explanatory idealization", doc=(386, 399),
         place=[(250, "\\operatorname{Ans}_E(\\tau(a),\\sigma(b))=\\operatorname{Ans}_p(a,b). \\tag{A}"),
                (242, "\\pi[\\operatorname{Sol}_D(a,b)]=\\operatorname{Sol}_E(\\tau(a),\\sigma(b))"),
                (277, "It does not exclude a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question"),
                (363, "An exact question is not silently replaced by an approximate one."),
                (538, "whose organization no transport can preserve under any contract on its target")],
         check="Its 'F1, F2, and answer fidelity are exact equalities' and 'an approximate transport bound' match L236\u2013L250 and L363.",
         finding="(F1), (F2) and (A) are exact equalities, and the approximate transport bound does not replace Account with an approximate account; a working model may capture a dependence while simplifying its realization, and the two answers the text has (an exact coarse-grained dependence, or a question about the approximation) do not show that every useful idealization is handled without changing what it was offered to explain.",
         evidence="Its argument; no worked idealization.",
         repair=["A substantive necessity question, not an immediate contradiction. A worked cognitive idealization is needed, with the coarse-graining and preserved dependence written out."],
         words=["The burden is to show that its exactness requirement tracks the intended scientific distinction rather than classifying most working explanations as merely candidates."],
         challenges=DOUBT, note="It bears on (Nec) at L538 and on L277 and L363.",
         fc=["FC66 ((T2)): holds", "FC104 (the two extents of 'fidelity'; round-1 matter 12): not tested", "FC19: holds"],
         cex=[], inv=["I28", "I49"], chk=[], nf=["NF03 (L538)"], repro="none"),

    dict(id="E16", section="4.4", title="Does the argument machinery explain reasoning?", doc=(401, 412),
         place=[(393, "or a premise \\(j\\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \\(j\\) holds an explanation of \\(d\\)"),
                (397, "A premise may be a claim taken as given: tentatively accepted, for whatever reason, even with no thought given to it, by someone who holds no explanation of it."),
                (429, "Closing an episode is a choice"),
                (8, "An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2).")],
         check="Its 'Usable records whether an agent admits the inference form, respects its scope, and retains its premises. It explicitly permits premises accepted without their explanations' matches L393 and L397.",
         finding="Usability records what an agent admits and retains and can model the consequences of its commitments, but does not explain why the agent adopts a premise, notices a conflict, drops an assumption or stops; the text calls these choices, which it says is no logical error, but in cognitive science they are among the phenomena to explain. Redescribing an argument for a conclusion as one against its denial does not by itself explain the operation or settle its status.",
         evidence="Its argument.",
         repair=[],
         words=["The document calls these choices. That is not a logical error. But in cognitive science, those choices are among the principal phenomena requiring explanation.",
                "Similarly, redescribing an argument for a conclusion as an argument against its denial does not by itself explain the psychological operation or settle its epistemic status.",
                "Useful bookkeeping for reasoning episodes; incomplete as a theory of reasoning dynamics."],
         challenges=NO, note="Its remark on L8 bears on the owner's decision S23 (argument as reasons why this and not that); a point against that reading is a question for the owner, and no ruling may change it (addendum, point 8).",
         fc=["FC56, FC69, FC70, FC72, FC73 (ruling out, (K2), premises taken as given): hold"], cex=[], inv=["I38", "I40", "I41"], chk=["R15"],
         nf=["NF13 (L8)", "NF14 (L397)"], repro="none"),

    dict(id="E17", section="4.5", title="The capability conditions and ordinary fallible performance", doc=(414, 424),
         place=[(466, "\\operatorname{RetReal}(\\pi,T,C;\\chi)\\iff\\forall z\\in C\\ \\forall i\\in\\operatorname{dom}T\\ \\forall\\eta\\in\\operatorname{Exec}(\\pi,z,i;\\chi),\\ \\eta\\text{ completes with }o\\in T[i]\\text{ and }z'\\in C. \\tag{CT1}"),
                (479, "\\(q\\in Q_\\Theta\\) is a tolerance of performance and \\(r\\in Q_\\Theta\\) a tolerance of retention"),
                (495, "An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable."),
                (509, "a finite performance record does not suffice for it.")],
         check="Its 'RetReal quantifies over every admitted execution: all must complete successfully and return to the retained constructor attribute' matches L466.",
         finding="(CT1) asks every admitted execution to complete and return, so a task with a small nonzero chance of failure, the failures in the execution family, fails it where ordinary usage would call the ability retained; the text has tolerances, but has to show whether a tolerance ranges over a distribution of executions or only over each output. \u201cNon-question-begging\u201d enabling conditions must exclude supplying the explanation being attributed while allowing teaching and scaffolding.",
         evidence="Its argument; no model.",
         repair=["But it needs to show explicitly how reliability is represented\u2014particularly whether tolerance applies to a distribution of executions rather than only to the quality of each output."],
         words=["Suppose a modeled cognitive task has a small but nonzero probability of failure, and those failures belong to the execution family. Then this condition fails, even when performance would ordinarily count as a retained ability.",
                "At the universal level, the existential enabling conditions need equally careful treatment. \u201cNon-question-begging\u201d must exclude supplying the very explanation or discovery being attributed, while still permitting genuine teaching and scaffolding."],
         challenges=YES, note="It bears on L466 and L479 (how reliability is represented) and on 'non-question-begging' at L495.",
         fc=["FC91 ((CT1) as C \u2286 F(C); round-1 matter 10), FC92 ((CT2); round-1 change L471), FC93 ((CT3), (CT4)): hold", "FC94 (recursion does not entail universality), FC110: not tested"],
         cex=[], inv=["I61", "I62", "I74", "I97", "I98"], chk=["T14"], nf=["NF11 (L495)", "NF12 (L497)"], repro="none"),

    dict(id="E18", section="5", title="Tables (set aside by the external reader)", doc=(430, 431),
         place=[(269, "A table that encodes an organization's response to every admitted change is not a table in that sense: it meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E)."),
                (536, "A table that encodes the response to every admitted change does not fail (F1)")],
         check="Its 'The document explicitly allows such a table when it preserves the required component structure' matches L269 and L536.",
         finding="\u201cA complete counterfactual lookup table cannot explain\u201d is no argument by itself: the text allows such a table when it keeps the required component structure and meets the other conditions, and repackaging a mechanism as a table gave no sufficiency counterexample.",
         evidence="None given.",
         repair=[],
         words=["The document explicitly allows such a table when it preserves the required component structure and meets the other conditions. Calling it a table is not an independent argument against explanation. I did not find a decisive sufficiency counterexample merely by repackaging a mechanism this way."],
         challenges=NO, note="The S104 search found what the external reader did not: FC25 (b), below, a case against L269's 'it meets (F1)'.",
         fc=["FC25 (tables): counterexample in part (b): an encoding table fails (F1) when a port of the target lies in no footprint, under I14 and I32; with \u03bb(k) read in the context of the whole target it meets (F1) (the check's R19)"],
         cex=["FC25 (b)"], inv=["I14", "I32"], chk=["R19"], nf=[], repro="none"),

    dict(id="E19", section="5", title="The transport could hide the answer (set aside as open)", doc=(433, 434),
         place=[(255, "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named \"law\" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements."),
                (273, "\"\\(p\\) because \\(p\\)\" fails non-circular dependence.")],
         check="Its 'the non-circularity clause' and 'structural answer-identity at the declared grain' match L255.",
         finding="The flexible translations make hiding the answer in the transport a serious line of attack; the non-circularity clause may exclude plain versions, but encoded variants need an exact account of structural answer-identity at the declared grain before they can be decided. An open obligation of formalization, not an exhibited counterexample.",
         evidence="None worked.",
         repair=["Encoded variants require a more exact account of structural answer-identity at the declared grain before they can be adjudicated."],
         words=["This is a serious attack surface because the translations are flexible. But the non-circularity clause may exclude straightforward versions."],
         challenges=YES, note="It names an obligation L255 leaves open (addendum, point 5).",
         fc=["FC23 ('p because p'): counterexample: it meets NC2 and fails non-circular dependence only through NC1, whose 'unanalysed', 'at the declared grain' and 'structural' are defined nowhere",
             "FC24, FC108: hold", "FC20: counterexample with non-injective value maps (I14, I81)"],
         cex=["FC23", "FC20"], inv=["I23", "I24", "I25", "I79", "I81", "I82", "I83"], chk=["R07, R08, R24", "formal core \u00a718, 'Where the text was vaguest', 2"], nf=[], repro="none"),

    dict(id="E20", section="5", title="Fixed port sets (set aside as repairable)", doc=(436, 437),
         place=[(425, "A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction."),
                (590, "and admitted edits (add or remove a change; alter \\(\\mathcal Q\\))."),
                (105, "Values of ports may be paths, functions, fields, mathematical structures or histories.")],
         check="No sentence is quoted; its 'the organizations have fixed port sets' is (O) at L87\u2013L100.",
         finding="Organizations have fixed port sets, so adding structure (a new question, a new component) needs dormant slots, structure-valued ports or a meta-organization; the value domains look broad enough that this is an encoding to make clear, not an impossibility.",
         evidence="None worked.",
         repair=["Some of the exact constructions need clearer encoding: adding structure requires dormant slots, structure-valued ports, or a meta-organization."],
         words=["But the allowed value domains are broad enough that this looks repairable. It is not a demonstrated expressive impossibility."],
         challenges=DOUBT, note="L425 and L590 speak of adding a port and adding a change; (O) fixes the port set and does not say how either is added.",
         fc=["FC97 (Argument 5): holds", "FC62 (the absent structure as a deleted counterpart): holds"], cex=[],
         inv=["I01", "I03 (ports and components the same under every edit; absence as the full relation)", "I67"], chk=[], nf=[], repro="none"),

    dict(id="E21", section="5", title="The finite monotone claim (set aside: no counterexample)", doc=(439, 440),
         place=[(305, "**Finite monotone claim.** If \\(\\Gamma\\) is finite, \\(\\mathsf S\\) is upward closed, and \\(\\Gamma\\in\\mathsf S\\), then \\(d\\in\\Gamma\\) is critical for some route (**contributory**) exactly when \\(d\\in\\bigcup\\min\\mathsf S\\)")],
         check="Matches L305.",
         finding="Every upward-closed route family containing the whole commitment set, for one to four commitments (193 families), gives no counterexample; the problem of 2.1 survives because the theorem can hold while its criticality predicate is read too strongly.",
         evidence="Its exhaustive check of 193 families.",
         repair=[],
         words=["I checked every upward-closed route family containing the full commitment set for one through four commitments: 193 families, with no counterexample."],
         challenges=NO, note="",
         fc=["FC37: holds on every family on |\u0393| \u2264 4 and on the 7,581 up-closures of antichains on five commitments"], cex=[], inv=["I30", "I77"], chk=[], nf=[],
         repro="FC-E5: CONFIRMED on the text under review (2, 5, 19 and 167 families for one to four commitments)"),

    dict(id="E22", section="opening, 5 (last paragraph), 6 and 7", title="The overall verdict, the revision priorities and the proposed benchmark", doc=(5, 494),
         place=[(3, "## A structural class of explanatory creativity, with selected and constructed correspondence"),
                (17, "The **constitutive conjecture** is this: explanatory creativity is fully characterized by"),
                (27, "It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes."),
                (546, "**A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1\u20133 under their stated assumptions.")],
         check="Its 'its strongest advertised achievement is a full characterization of explanatory creativity' points to L3 and L17; the text states the characterization as a conjecture (L17) and names what would rule it out (Part XV).",
         finding="The text's strongest shown achievement is an audit language for scoped explanatory structure, and its strongest advertised one a full characterization of explanatory creativity; the small mathematical results do much less than the conjecture, and their holding is no argument for it. Its priorities: explanatory relevance apart from whole-model fidelity (E02), construction grounded without its resulting representation (E03), surprise apart from fidelity failure (E08); then an operational account of component mappings, construction traces and scope choices (E13). Its benchmark: a known mechanism with hidden state, an editable measurement channel, an unrelated subsystem, and classifications fixed before the critical interventions are revealed.",
         evidence="Sections 1 to 5.",
         repair=["The highest-priority revisions are to separate explanatory relevance from whole-model fidelity, ground construction without presupposing its resulting representation, and separate surprise from objective fidelity failure."],
         words=["It is promising as a framework for auditing explanatory claims, but it has not established its stronger claim to fully characterize explanatory creativity.",
                "However, I did not find a decisive counterexample satisfying the document\u2019s full requirements for refuting the sufficiency of Account.",
                "The small mathematical results generally do much less than the central philosophical claim. Their correctness should not be mistaken for proof of the constitutive conjecture.",
                "Then fix the candidate classifications before revealing the critical interventions.",
                "What does the framework force us to conclude about a difficult case before we adjust its grain, contract, counterparts, and provenance description to fit the outcome?"],
         challenges=DOUBT, note="Whether L3 and L17 say more than the text's results; the text calls the characterization a conjecture. Its benchmark is a proposal for a test outside the text, and its priorities are proposals (addendum, point 6). The findings about scope (E07, E08, E09, E11, E12) and E16 bear on L17 through this item.",
         fc=["FC110 (the classes are defined; no membership is asserted): not tested", "FC109 ('A mathematical error': the named claims): holds"], cex=[], inv=["I74", "I75"], chk=[],
         nf=["NF01 (L17)"], repro="none"),
]


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def fail(msg):
    sys.exit("refused: " + msg)


def main():
    if md5(TEXT) != TEXT_MD5:
        fail("text md5 %s" % md5(TEXT))
    if md5(DOC) != DOC_MD5:
        fail("document md5 %s" % md5(DOC))
    text = open(TEXT, encoding="utf-8").read().split("\n")
    doc_lines = open(DOC, encoding="utf-8").read().split("\n")
    doc = "\n".join(doc_lines)
    n_q = 0
    n_w = 0
    for it in ITEMS:
        for (ln, q) in it["place"]:
            for frag in q.split(" \u2026 "):
                if frag not in text[ln - 1]:
                    fail("%s: not in L%d: %r" % (it["id"], ln, frag))
            n_q += 1
        a, b = it["doc"]
        span = "\n".join(doc_lines[a - 1:b])
        for w in it["repair"] + it["words"]:
            if w not in doc:
                fail("%s: not in the document: %r" % (it["id"], w))
            if w not in span:
                fail("%s: not in the document's lines %d-%d: %r" % (it["id"], a, b, w))
            n_w += 1
    # the quotations of the text in the two maths addenda
    n_a = 0
    for path in ADDENDA:
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^> L(\d+) \| (.*)$", line.rstrip("\n"))
            if m:
                ln, q = int(m.group(1)), m.group(2)
                for frag in q.split(" \u2026 "):
                    if frag not in text[ln - 1]:
                        fail("%s: not in L%d: %r" % (os.path.basename(path), ln, frag))
                n_a += 1
            m = re.match(r'^\*\*The external reader \([^)]*\)\.\*\* "(.*)"$', line.rstrip("\n"))
            if m and m.group(1) not in doc:
                fail("%s: not in the document: %r" % (os.path.basename(path), m.group(1)))
    counts = {}
    for it in ITEMS:
        key = it["challenges"].split(" ")[0].rstrip(":")
        counts[key] = counts.get(key, 0) + 1
    write_md(counts)
    write_json()
    print("items %d; quotations of the text %d; of the document %d; in the addenda %d; all compared" % (len(ITEMS), n_q, n_w, n_a))
    print("challenges: %s" % counts)


def write_json():
    out = []
    for it in ITEMS:
        out.append(dict(id=it["id"], section=it["section"], title=it["title"], document_lines=list(it["doc"]),
                        place=[dict(line=ln, quote=q) for (ln, q) in it["place"]], its_description_of_the_text=it["check"],
                        finding=it["finding"], evidence=it["evidence"], repair_in_its_own_words=it["repair"],
                        other_words_of_its_own=it["words"], challenges_the_text=it["challenges"], note=it["note"],
                        s104=dict(formal_claims=it["fc"], counterexamples=it["cex"], inventions=it["inv"],
                                  check_of_the_formalization=it["chk"], not_formalized=it["nf"]),
                        reproduced=it["repro"]))
    meta = dict(text="tests/103 The semantics, standing alone, after round 1.md", text_md5=TEXT_MD5,
                document="results/S104 Round 2 - external cross-examination supplied by the owner.txt", document_md5=DOC_MD5,
                built_by="results/S104 Round 2 - external cross-examination - items, build script.py", date="2026-09-27")
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dict(meta=meta, items=out), f, ensure_ascii=False, indent=1)
        f.write("\n")


def lines_of(it):
    ls = sorted(set(ln for ln, _ in it["place"]))
    return ", ".join("L%d" % ln for ln in ls)


def write_md(counts):
    L = []
    L.append("# S104 Round 2 \u2014 the external cross-examination: items")
    L.append("")
    L.append("*Log S104, review round 2 (the maths round), 27 September 2026. Written by a Claude subagent while the round's runs were going and before any round-2 reply was opened, under `results/S104 Round 2 - addendum to the reading rule, the external cross-examination, written before any reply was opened.md`. Built by `results/S104 Round 2 - external cross-examination - items, build script.py`, which compared the md5 of the text under review (`tests/103 The semantics, standing alone, after round 1.md`, f31ebb1f050783f1a84f6136cec20fcd) and of the saved document (3aeed4029848cc8ad375f314123eaf66), every quotation of the text with the line it names, and every quotation of the document with the document and with the lines the item names. No theory text was written. This file obeys decision S23 except where it quotes the text or the document.*")
    L.append("")
    L.append("**What this is.** The findings of the external cross-examination the owner supplied (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`; \"the external reader\"), as items E01 to E22 in the document's order. For each: the lines of the document it comes from; the place in the text it bears on, quoted; whether its description of the text matches file 103; the finding in one or two sentences and its evidence (Claude's words); its proposed repair and its other key sentences in its own words; whether it challenges the text; and the S104 formal claims, counterexamples, inventions, entries of the check of the formalization and claims not formalized that touch the same place. The extraction is Claude's; where it and the document differ, the document's words govern (addendum, point 2). The same items are in the `.json` file beside this one.")
    L.append("")
    L.append("**Challenges the text.** *yes*: it names a sentence of the text and a defect in it, and goes to a checker (addendum, point 4). *in doubt*: it may challenge a sentence, and goes to a checker (rule 5). *a finding about scope (section 3)*: recorded as a finding about scope, not as a defect (addendum, point 7). *no*: it names no line to change. An item that goes to no checker is still given as context to the checker of any group whose lines it names (addendum, point 4). Nothing here rules on an item.")
    L.append("")
    L.append("**Counts.** 22 items: %d *yes*, %d *in doubt*, %d *a finding about scope (section 3)*, %d *no*. Five examples reproduced on the S104 model as FC-E1 to FC-E5 (`results/S104 Round 2 - maths/formal claims - addendum for the external examples.md`), every one CONFIRMED on the text under review; their inventions are I103 to I108 (`results/S104 Round 2 - maths/inventions register - addendum for the external examples.md`)." % (
        counts.get("yes", 0), counts.get("in", 0), counts.get("a", 0), counts.get("no", 0)))
    L.append("")
    L.append("**Which copy the external reader examined** is not stated. Every description of the text it gives was compared with file 103 (below, item by item), and each matched; the four lines round 1 changed (L123, L443, L471, L520) are not quoted by it.")
    L.append("")
    L.append("## Index")
    L.append("")
    L.append("| id | its section | finding | lines of the text | challenges | S104 on the same place | reproduced |")
    L.append("| --- | --- | --- | --- | --- | --- | --- |")
    for it in ITEMS:
        ids = []
        for x in re.findall(r"FC\d+", " ".join(it["fc"])):
            if x not in ids:
                ids.append(x)
        s104 = ", ".join(ids[:7]) + (", \u2026" if len(ids) > 7 else "")
        rep = it["repro"].split(":")[0] if it["repro"] and it["repro"].startswith("FC-E") else "\u2014"
        ch = it["challenges"].split(":")[0].split(" (")[0]
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (it["id"], it["section"], it["title"], lines_of(it), ch, s104 or "\u2014", rep))
    L.append("")
    L.append("## Items")
    for it in ITEMS:
        L.append("")
        L.append("### %s \u00b7 %s \u00b7 %s" % (it["id"], it["section"], it["title"]))
        L.append("")
        a, b = it["doc"]
        L.append("**In the document.** Lines %d\u2013%d of the saved file." % (a, b) if a != b else "**In the document.** Line %d of the saved file." % a)
        L.append("")
        L.append("**The place in the text.**")
        L.append("")
        for (ln, q) in it["place"]:
            L.append("> L%d | %s" % (ln, q))
            L.append("")
        L.append("**Its description of the text.** %s" % it["check"])
        L.append("")
        L.append("**The finding.** %s" % it["finding"])
        L.append("")
        L.append("**Its evidence.** %s" % it["evidence"])
        L.append("")
        if it["repair"]:
            L.append("**Its repair, in its own words.**")
            L.append("")
            for w in it["repair"]:
                L.append("> %s" % w)
                L.append("")
        else:
            L.append("**Its repair, in its own words.** None offered.")
            L.append("")
        L.append("**Its other words.**")
        L.append("")
        for w in it["words"]:
            L.append("> %s" % w)
            L.append("")
        L.append("**Challenges the text.** %s.%s" % (it["challenges"], (" " + it["note"]) if it["note"] else ""))
        L.append("")
        L.append("**S104 on the same place.**")
        L.append("")
        L.append("- Formal claims: %s." % ("; ".join(it["fc"]) if it["fc"] else "none"))
        L.append("- Counterexamples (`search results.md`): %s." % ("; ".join(it["cex"]) if it["cex"] else "none"))
        L.append("- Inventions (`inventions register.md`): %s." % (", ".join(it["inv"]) if it["inv"] else "none"))
        if it["chk"]:
            L.append("- The check of the formalization, and the formal core: %s." % "; ".join(it["chk"]))
        if it["nf"]:
            L.append("- Claims of the text not formalized: %s." % ", ".join(it["nf"]))
        L.append("")
        L.append("**Reproduced.** %s." % it["repro"])
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    main()
