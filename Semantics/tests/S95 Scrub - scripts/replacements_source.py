#!/usr/bin/env python3
"""S95 Scrub: the source of replacements.json.

Each E(...) is one replacement on one line of draft 5: exact old span, exact new
span, category, reason. kind="rewording" marks a span that needed new wording, not
a word swap; claim=... marks a place where what the sentence claims changed.
AUTO(...) rules generate one entry per occurrence of a mechanical swap (for example
"Derivation 3" -> "Argument 3") outside the spans of hand entries; each generated
entry carries the smallest context that makes its old span unique on its line.
Run it to write replacements.json; scrub_apply.py then applies that file.
"""
import json, re, collections

SRC = "/home/user/ThreadSmith/Semantics/tests/Revision 2 - file 13 draft 5, theory text.md"
OUT = "/home/user/ThreadSmith/Semantics/tests/S95 Scrub - scripts/replacements.json"
L = open(SRC, encoding="utf-8").read().split("\n")

ENTRIES, AUTOS, BORDER = [], [], []
FILL = {}


def E(line, old, new, cat, reason, kind="swap", claim=None, owner=False):
    e = dict(line=line, old=old, new=new, category=cat, reason=reason, kind=kind)
    if claim:
        e["claim_changed"] = claim
    if owner:
        e["owner"] = "provisional term; the owner decides (sceptic's OWNER ruling on 'knowledge')"
    ENTRIES.append(e)


def AUTO(pattern, repl, cat, reason, skip_lines=()):
    AUTOS.append((re.compile(pattern), repl, cat, reason, set(skip_lines)))


def B(line, word, reason, count=1):
    BORDER.append(dict(line=line, word=word, reason=reason, count=count))


# ---------------------------------------------------------------- header, definitions
FILL["2"] = (
    "*Experiment, 25 September 2026 (log S95, on decision S23). This is draft 5 of revision 2 "
    "with the words the owner forbade that day replaced, made by program "
    "(`tests/S95 Scrub - scripts/scrub_apply.py`, from `replacements.json` beside it) out of draft 5, "
    "md5 7f1d8ad02adf96e27622593bd263252e, one line of draft 5 to one line here, so the two compare "
    "line by line. It does not take the place of draft 5, which stays the current draft; it is the "
    "step the owner asked for next, to see what of the semantics is left in these words. The words, and "
    "why each was chosen, are in `tests/S95 Scrub - vocabulary, as used.md`. One name here is "
    "provisional and says so (Part XI).*")
FILL["8"] = (
    "**Two words, as used here.** An **argument** is, in the owner's words, \"reasons why this and not "
    "that\": \"something that can be strung together into a coherent structure to decide why this and "
    "not another.\" Each of its steps rules out the case in which the step's premises are met and its "
    "conclusion fails (Part IX). An argument is never a reason *for* a claim: what it does is rule out "
    "a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2); a "
    "claim that no argument rules out is only not ruled out, and gets nothing from that. To "
    "**tentatively accept** a claim is a person's choice to go on with it, made, in the owner's words, "
    "\"for whatever reason\"; whatever is accepted is accepted tentatively, open to being dropped, and "
    "the semantics never defines accepting by the arguments someone holds.")

# ---------------------------------------------------------------- mechanical swaps
AUTO(r"\bDerivations(?= \d)", "Arguments", "LISTED",
     "derived: Part XVI's items are arguments in the owner's sense (why the claim and not its denial)")
AUTO(r"\bDerivation(?= \d)", "Argument", "LISTED",
     "derived: Part XVI's items are arguments in the owner's sense (why the claim and not its denial)")
AUTO(r"\*Proof\.\*", "*Why this and not its denial.*", "LISTED",
     "proves: the block argues why the claim and not its denial (the owner's 'why this and not that')")
AUTO(r"\bprimitive layer\b", "object layer", "TRUTH-OR-FOUNDATION",
     "primitive (foundation sense): l. 175's own description, the layer at which there are objects")
AUTO(r"\bnormative relation\b", "appraisal relation", "TRUTH-OR-FOUNDATION",
     "normative: N is someone's appraisal, declared as an input; it binds no one")
AUTO(r"\(EK\)", "(EX)", "BELIEF",
     "knowledge (OWNER ruling): provisional rename to created explanation (EX)")
AUTO(r"\bsatisfies\b", "meets", "TRUTH-OR-FOUNDATION",
     "satisfaction said with one word, 'meets' (sceptic's ruling on rule 3)")
AUTO(r"\bsatisfying\b", "meeting", "TRUTH-OR-FOUNDATION",
     "satisfaction said with one word, 'meets' (sceptic's ruling on rule 3)")
AUTO(r"\bsatisfy\b", "meet", "TRUTH-OR-FOUNDATION",
     "satisfaction said with one word, 'meets' (sceptic's ruling on rule 3)")
AUTO(r"\bobligations\b", "aims", "TRUTH-OR-FOUNDATION",
     "obligation implies someone who obliges; l. 441 already calls them 'the aims'", skip_lines=(45, 443))
AUTO(r"\bobligation\b", "aim", "TRUTH-OR-FOUNDATION",
     "obligation implies someone who obliges; l. 441 already calls them 'the aims'", skip_lines=(75, 443))
AUTO(r"\bconstruction witness\b", "construction trace", "TRUTH-OR-FOUNDATION",
     "witness carried testimony; a trace is the part of a history that identifies the controlled processes")

# ---------------------------------------------------------------- Part 0
E(11, "that is checked only by", "that is tested only by", "MISSED",
  "checked (sceptic's missed word): a test is the making of a record")
E(13, "is not a primitive here", "is not an import here", "TRUTH-OR-FOUNDATION",
  "primitive: says where a thing comes from and nothing about its standing")
E(13, "Declaration is permitted only as a modelling convenience, and a claim about creativity cannot rest on it.",
  "Declaration is used only as a modelling convenience, and a claim about creativity cannot depend on it.",
  "TRUTH-OR-FOUNDATION",
  "permitted (sceptic's missed word) and 'rest on': 'depend on' is the dependence order's own verb (Part XIV)")
E(17, "transports between organizations checked by change-fidelity alone",
  "transports between organizations tested by change-fidelity alone", "MISSED", "checked -> tested")
E(17, "A genuine explanatory achievement that these four cannot represent counts against the conjecture. "
      "A candidate that satisfies all four while plainly explaining nothing counts against it too. "
      "Part XV lists what would count.",
  "An explanatory achievement that these four cannot represent would rule out the conjecture; so would a "
  "candidate that meets all four and explains nothing. Part XV lists what would rule it out.",
  "BELIEF", "'counts against' and 'genuine', 'plainly': said as what would rule the conjecture out", kind="rewording")
E(21, "It does not derive reference from uninterpreted matter. It derives reference from matter",
  "It does not define reference in terms of uninterpreted matter. It defines reference in terms of matter",
  "LISTED", "derive: a definition passes meaning from one term to another and nothing else")
E(25, "It does not supply an objective aesthetics, a probability of truth, a merit function, a measure of worth, "
      "or a ranking of thinkers.",
  "It does not supply an aesthetics independent of any declared appraisal, a probability on claims, an "
  "appraisal of its own, or a function that orders explanations or thinkers.",
  "RANKING", "objective, truth, merit, worth, ranking: each refused item kept, said without the ranking words",
  kind="rewording")
E(25, "a claim of worth or of aesthetic value takes the normative relation as an input (Parts XI, XIV), and a "
      "claim that needs any of the others is unsettled (Part XIV).",
  "a claim that invokes an appraisal or aesthetic value takes the appraisal relation as an input (Parts XI, "
  "XIV), and a claim that needs any of the others is left open (Part XIV).",
  "RANKING", "worth dropped (sceptic: 'Appraisal'); normative -> appraisal; unsettled -> left open")
E(25, "It does not supply a division of credit among contributors beyond what a history establishes (Part XI).",
  "It does not divide an achievement among contributors beyond what a history contains (Part XI).",
  "MISSED", "credit -> attribution of an achievement; establish (no assessor meant) -> contains")
E(27, "It does not prove that any", "It does not decide whether any", "LISTED",
  "prove -> decide, the owner's verb from his definition of argument")
E(29, "## What is primitive, what is an index, and what is derived",
  "## What is imported, what is an index, and what is defined", "LISTED", "primitive -> import; derived -> defined")
E(31, "The semantics has two primitives:", "The semantics has two imports:", "TRUTH-OR-FOUNDATION",
  "primitive -> import")
E(31, "taken as an input wherever a question invokes worth", "taken as an input wherever a question invokes an appraisal",
  "RANKING", "worth dropped; the appraisal is someone's")
E(31, "none is a predicate that could be true or false", "none is a predicate that a case meets or fails",
  "LISTED", "true or false -> meets or fails: the contrast an index lacks")
E(31, "Everything else is derived from the two primitives,", "Everything else is defined in terms of the two imports,",
  "LISTED", "derived from -> defined in terms of")
E(31, 'No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive,',
  'No predicate that says "explains" without a question and a contract, or "is a cause", or "is a created '
  'explanation", is taken as an import,',
  "BELIEF", "really, knowledge, primitive: the refused predicates said without them; (EK) renamed provisionally",
  kind="rewording", owner=True)
E(37, "which is what the semantics checks", "which is what the semantics asks about", "MISSED",
  "checks -> asks about, as l. 127 says the semantics 'asks what its signature is'")
E(39, "which is correct rather than a loss", "which is what that level contains, not a loss",
  "TRUTH-OR-FOUNDATION", "correct: 'correct' added nothing but the forbidden sense")
E(41, "you have made truth a matter of survival", "you have made fidelity a matter of survival", "LISTED",
  "truth (the objection's wording) -> fidelity, the theory's word for what the objection is about")
E(41, "is a fact about the transport and the world, independent of whether it survived",
  "turns on the transport and the world alone, not on whether it survived", "TRUTH-OR-FOUNDATION",
  "fact: (E)'s content carries the independence from assessors")
E(43, 'and there is no objectivity."', 'and nothing is independent of the modeller."', "MISSED",
  "objectivity (sceptic's missed word), in the objection's voice")
E(43, "Within any contract there is a fact of the matter about fidelity.",
  "Within any contract, whether a transport is faithful at a pair turns on the transport and the target, and "
  "no assessor appears in (E).", "TRUTH-OR-FOUNDATION", "fact of the matter -> the proposal's wording, kept by the sceptic")
E(43, "Objectivity lives in the physics and the fidelity facts; scope-honesty lives in the record.",
  "What is independent of the modeller lies in the physics and in fidelity; what the modeller chose to leave "
  "out lies in the stated scope, and so in the record.", "MISSED",
  "objectivity, fidelity facts, scope-honesty (sceptic's missed words)", kind="rewording")
E(45, "imposing physical realization obligations at every attribution",
  "imposing physical realization conditions at every attribution", "TRUTH-OR-FOUNDATION",
  "obligation implies someone who obliges; these are conditions, not Part XI's aims")
E(47, "Construction is a separate provenance with a separate witness,",
  "Construction is a separate provenance with a separate trace,", "TRUTH-OR-FOUNDATION", "witness -> trace")
E(47, "Part XV names its refutation.", "Part XV names what would rule it out.", "TRUTH-OR-FOUNDATION",
  "refutation -> what would rule it out")
E(49, "Removing an axiom,", "Removing a starting assumption,", "TRUTH-OR-FOUNDATION", "axiom (sceptic's missed word)")
E(49, "A proof explains, relative to a question,", "A mathematical argument explains, relative to a question,",
  "LISTED", "proof -> mathematical argument: it decides a proposition against its negation")
E(51, "The semantics does not pretend to know which aesthetic reasons are true.",
  "The semantics does not decide between rival aesthetic reasons.", "BELIEF", "know, true: said contrastively")
E(53, "fallible but checkable in principle", "fallible but testable in principle", "MISSED", "checkable -> testable")
E(55, "Derivation 7 shows the two are consistent.", "Argument 7 rules out a conflict between them.",
  "TRUTH-OR-FOUNDATION", "shows -> rules out, said by an argument")
E(57, '**11. "Kinds obviously exist.', '**11. "Kinds exist.', "MISSED",
  "obviously (sceptic's missed word, the objector's voice): an appeal to what needs no argument")
E(61, "The load-bearing claims,", "The claims the rest depends on,", "MISSED", "load-bearing (sceptic's missed word)")
E(61, "together with what would refute each.", "together with what would rule out each.", "TRUTH-OR-FOUNDATION",
  "refute -> rule out")

# ---------------------------------------------------------------- Part I
E(67, "**Explanatory realism.**", "**Faithfulness without assessors.**", "MISSED",
  "realism (sceptic's missed heading): named for what the paragraph says")
E(67, "independent of whether anyone accepts it.", "independent of whether anyone tentatively accepts it.",
  "ACCEPT", "accept is always tentative (the owner); a person's choice")
E(67, "Systems can be wrong about", "Systems can be in error about", "TRUTH-OR-FOUNDATION",
  "wrong -> in error, defined at l. 211")
E(69, "**Fallibility without falsehood-as-work.** A theory may contain an accurate scoped dependence",
  "**Fallibility without error-as-work.** A theory may contain a faithful scoped dependence",
  "TRUTH-OR-FOUNDATION", "falsehood -> error; accurate -> faithful")
E(69, "a false theory offered as an answer", "a theory in error offered as an answer", "TRUTH-OR-FOUNDATION",
  "false -> in error (l. 211: the content's transport to the world fails)")
E(71, "An idea may be entertained without justification.",
  "An idea may be entertained with no argument that rules out its rivals.", "BELIEF",
  "justification -> the owner's contrastive argument", kind="rewording")
E(71, "A thinker may act on an appraisal without certifying it.",
  "A thinker may act on an appraisal that no argument has decided.", "BELIEF", "certify -> decided by an argument")
E(75, "**Substrate independence with physical obligations.**", "**Substrate independence with physical conditions.**",
  "TRUTH-OR-FOUNDATION", "obligation -> condition, as at l. 45")
E(75, "must be permitted by the adopted physics.",
  "must be possible under the adopted physics; here and throughout, to adopt something is to take it "
  "tentatively, open to replacement.", "ACCEPT",
  "permitted -> possible (Marletto's word); 'adopted' kept and declared tentative once (sceptic's ruling)",
  kind="rewording")
E(75, "substrate independence holds so far as", "substrate independence reaches as far as", "TRUTH-OR-FOUNDATION",
  "holds (satisfaction) said without 'hold'")

# ---------------------------------------------------------------- Parts II-V
E(105, "fields, proofs or histories", "fields, mathematical arguments or histories", "LISTED",
  "proof -> mathematical argument (a kind of port value)")
E(107, "## Roles are derived", "## Roles are defined, not supplied", "LISTED",
  "derived -> defined; the section's own contrast (l. 109: 'No role assignment is supplied')")
E(119, "its anchor, with a port translation (Part IV)", "its counterpart, with a port translation (Part IV)",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart: names the pairing lambda gives, not a fixing")
E(119, "and its anchor \\(\\lambda(k)\\), read on", "and its counterpart \\(\\lambda(k)\\), read on",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(127, "is settled by that signature", "is fixed by that signature", "TRUTH-OR-FOUNDATION",
  "settled -> fixed: dependence, not decision (sceptic)")
E(151, "returns a reachability truth value", "returns reachable or unreachable", "LISTED",
  "truth value named by its two values")
E(151, "with a reliable prediction from it,", "with a prediction from it that is faithful on the contract,",
  "BELIEF", "reliable -> faithful on the contract")
E(155, "with the witness required by Part IV", "with the trace required by Part IV", "TRUTH-OR-FOUNDATION",
  "witness -> trace")
E(155, "for the contract in question, with the witness.", "for the contract in question, with the trace.",
  "TRUTH-OR-FOUNDATION", "witness -> trace")
E(157, "## Scope, and a question that can be wrong", "## Scope, and a question that can be in error",
  "TRUTH-OR-FOUNDATION", "wrong -> in error")
E(159, "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the "
       "claim; the semantics records the restriction and supplies no rule that certifies it. Meeting the "
       "conditions of an account (Part V) on the restricted contract does not certify the restriction as "
       "appropriate.",
  "Why the question asked is answered on this restriction and not on a wider one is a substantive, "
  "criticizable part of the claim; the semantics records the restriction and supplies no rule that decides "
  "it. Meeting the conditions of an account (Part V) on the restricted contract leaves open whether the "
  "restriction drops changes the question asked contains.",
  "BELIEF", "appropriate, certify: contrastive; 'leaves open' for compatibility, not 'does not rule out' "
  "(sceptic's ruling on l. 159)", kind="rewording")
E(159, "Where the claim states the ground of its restriction, a verdict on the restriction is given with that "
       "ground; where it states none and a verdict turns on one, the ground is a missing declared input",
  "Where the claim states why it restricts the contract as it does, an assessment of the restriction is given "
  "with that statement; where it states none and an assessment turns on one, that statement is a missing "
  "declared input",
  "MISSED", "ground, verdict (sceptic's missed words): verdict -> assessment, draft 5's term (l. 55)",
  kind="rewording")
E(177, "is where expectation lives.", "is where prediction lives.", "BELIEF",
  "expectation -> prediction: an output, not an attitude (l. 177 already calls the queries predictions)")
E(201, "that is the expected arrangement", "that is the usual arrangement", "BELIEF", "expected -> usual")
E(203, "## Representation is derived", "## Representation is defined, not supplied", "LISTED",
  "derived -> defined")
E(211, "is thus a fidelity fact with a history. A system can represent a false theory:",
  "is thus a fidelity relation with a history. A system can represent a theory in error:",
  "TRUTH-OR-FOUNDATION", "fact -> relation; false -> in error")
E(211, "a later record derived from the carrier is not a second, independent witness to its history",
  "a later record made from the carrier is not a second, independent trace of its history",
  "LISTED", "derived -> made (sceptic: 'copied' would add a claim draft 5 does not make); witness -> trace")
E(215, "## Expectation, surprise, violation", "## Prediction, surprise, violation", "BELIEF",
  "expectation -> prediction")
E(219, "the **expectation** is", "the **prediction** is", "BELIEF", "expectation -> prediction")
E(223, "is a fact about its population (Derivation 3). Expectation and violation are defined",
  "turns on its population (Argument 3). Prediction and violation are defined", "TRUTH-OR-FOUNDATION",
  "fact -> turns on; expectation -> prediction")
E(231, "satisfies \\(\\operatorname{Account}(\\mathcal E)\\) exactly when the following four conditions hold,",
  "meets \\(\\operatorname{Account}(\\mathcal E)\\) exactly when the following four conditions are met,",
  "TRUTH-OR-FOUNDATION", "satisfies/hold -> meets/is met")
E(233, "with anchor subnetwork", "with counterpart subnetwork", "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(245, "(F1) prevents an assembled match from hiding a wrong decomposition. (F2) prevents a set of locally correct "
       "pieces from hiding a lost shared constraint.",
  "(F1) prevents an assembled match from hiding a decomposition in error. (F2) prevents a set of pieces each "
  "faithful locally from hiding a lost shared constraint.", "TRUTH-OR-FOUNDATION", "wrong -> in error; correct -> faithful")
E(245, "(F1) entails that every component of \\(E\\) has the signature of its anchor;",
  "no component of \\(E\\) whose signature differs from its counterpart's meets (F1);", "TRUTH-OR-FOUNDATION",
  "a condition's exclusion said by the condition itself, not by 'rules out' (sceptic's joints row)",
  kind="rewording")
E(255, "logically equivalent mathematical truths", "logically equivalent mathematical statements", "LISTED",
  "truths -> statements")
E(269, "A table that genuinely encodes", "A table that encodes", "TRUTH-OR-FOUNDATION", "genuinely dropped")
E(269, 'The word "table" settles nothing;', 'The word "table" fixes nothing;', "TRUTH-OR-FOUNDATION",
  "settles -> fixes: the response under the admitted changes is not an argument, and 'decide' is kept for arguments (sceptic)")
E(273, "packaging a genuine dependence", "packaging a dependence", "TRUTH-OR-FOUNDATION", "genuine dropped")
E(277, "(E) does not exclude a true mechanism guessed for bad reasons; the reasons for adopting it are assessed "
       "elsewhere (Part IX).",
  "(E) does not exclude a mechanism that meets (E) whatever led anyone to guess it; how it came to be taken up "
  "is assessed elsewhere (Part IX).", "LISTED",
  "true, bad reasons: sceptic's wording ('reasons since ruled out' would change the claim)", kind="rewording")
E(277, "It does not prefer an elegant account to a less elegant one with the same fidelity.",
  "It draws no line between two candidates with the same fidelity that differ only in elegance: both meet it "
  "or both fail it.", "RANKING",
  "prefer, less elegant: said as no line drawn; 'separate' is kept for admitted changes (l. 11, 281), and "
  "'candidates' because accounts meet (E) by definition", kind="rewording")
E(277, "It does not reject a coarse dependence", "It does not exclude a coarse dependence", "MISSED",
  "reject (sceptic's missed word) -> exclude, the paragraph's own verb")
E(277, "and its strength is fixed by its contract,", "and what it answers is fixed by its contract,", "MISSED",
  "strength (sceptic's missed word)")
E(277, "A proof answering", "A mathematical argument answering", "LISTED", "proof -> mathematical argument")
E(279, "## Why there is no anchoring condition", "## Why there is no counterpart-kind condition",
  "TRUTH-OR-FOUNDATION", "anchoring -> counterpart-kind")
E(281, "(F1) already fails for a component anchored to the wrong one.",
  "(F1) already fails for a component whose counterpart is of the other kind.", "TRUTH-OR-FOUNDATION",
  "anchored, wrong -> counterpart of the other kind")

# ---------------------------------------------------------------- Part VI
E(285, "# Part VI — Work, support, and interference", "# Part VI — Work, routes, and interference", "LISTED",
  "support (member of S) -> route; l. 307 already equates them")
E(299, "Criticality is relative to the support \\(W\\) it is assessed in: a commitment critical in one successful "
       "support need not be critical in the full candidate, and the supports assessed are subsets of the written "
       "\\(\\Gamma\\), whether or not anyone has set them out, not a support someone could write",
  "Criticality is relative to the route \\(W\\) it is assessed in: a commitment critical in one route need not "
  "be critical in the full candidate, and the routes assessed are subsets of the written \\(\\Gamma\\), whether "
  "or not anyone has set them out, not a route someone could write", "LISTED",
  "support -> route; 'successful' dropped: a route is a member of S")
E(305, "**Finite monotone theorem.**", "**Finite monotone claim.**", "TRUTH-OR-FOUNDATION", "theorem -> claim")
E(305, "A member of a minimal support is critical for it.", "A member of a minimal route is critical for it.",
  "LISTED", "support -> route")
E(305, "a support. Deletion of \\(d\\) from \\(\\Gamma\\) preserves support exactly when a minimal support omits "
       "\\(d\\). ∎ The theorem applies only where its assumptions hold; an addition to \\(\\Gamma\\) that destroys "
       "a support is",
  "a route. Deletion of \\(d\\) from \\(\\Gamma\\) leaves a route exactly when a minimal route omits \\(d\\). ∎ "
  "The claim applies only where its assumptions are met; an addition to \\(\\Gamma\\) that stops a route being "
  "one is", "LISTED", "support -> route; theorem -> claim; hold -> are met")
E(307, "Here a route is a support of the candidate, a member of \\(\\mathsf S\\),",
  "Here a route of the candidate is a member of \\(\\mathsf S\\),", "LISTED", "support -> route: one word")
E(307, "which credits a repair to the contributions", "which attributes a repair to the contributions", "MISSED",
  "credits -> attributes")
E(307, "and the new candidate's success is not the old one's.",
  "and whether the new candidate meets (E) is not whether the old one does.", "RANKING", "success -> meets (E)")
E(309, "the full candidate fails although a subset succeeds. Success of a subset does not imply success of the whole;",
  "the full candidate fails (E) although a subset meets it. A subset can meet (E) while the whole fails it;",
  "RANKING", "success -> meets (E)")
E(311, "**Infinitary support.**", "**Infinitary routes.**", "LISTED", "support -> route")
E(311, "no minimal support and no singleton witness exists", "no minimal route and no singleton instance exists",
  "LISTED", "support -> route; witness -> instance (l. 429's word)")
E(313, "that has a support does no work by itself in it when every support stays a support after",
  "that has a route does no work by itself in it when every route stays a route after", "LISTED",
  "support -> route")
E(313, "is critical in no support (B)", "is critical in no route (B)", "LISTED", "support -> route")
E(313, "(Infinitary support)", "(Infinitary routes)", "LISTED", "support -> route")
E(315, "with one anchor have different relations there", "with one counterpart have different relations there",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(315, "A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result "
       "that tells against a candidate tells against it only together with the background and instruments of the "
       "test that yields it. A candidate **fits** what is established for an assessor when no result established "
       "for that assessor shows it failing a condition of (E).",
  "A candidate is **ruled out** for an assessor \\(j\\) when an argument usable by \\(j\\) (Part IX) rules out "
  "that the candidate meets (E); by (K3), an argument from a test's record rules out a candidate only together "
  "with the background and instruments of that test. A candidate is **not ruled out** for \\(j\\) when no "
  "argument usable by \\(j\\) rules it out.",
  "LISTED", "established, receipt, tells against, fits, shows: no positive status; the only status is 'ruled "
  "out for j' (sceptic's finding (a)); 'not ruled out' is the owner's S21 phrase", kind="rewording",
  claim="Draft 5 defined a positive status ('established': the assessor holds a usable receipt for the result) "
        "and 'fits' by it. The scrubbed text has no positive status: only 'ruled out for j', and 'not ruled out' "
        "as its absence.")
E(317, "Two rivals that both fit what is established for an assessor pose, for that assessor, a **problem for "
       "\\(p\\)**: a conflict between ideas that what the assessor has established has not settled.",
  "Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \\(p\\)**: a "
  "conflict between ideas that no argument usable by that assessor has decided.", "LISTED",
  "fit, established, settled -> not ruled out, decided")
E(317, "whether or not anyone can establish what it does; establishing it, the target's relations as well as its "
       "answer where their answers there agree, is a **test** that solves the problem whatever it shows, since "
       "afterwards at most one of them fits; an answer it refutes stays refuted on \\(p\\) (Part VIII).",
  "whether or not anyone records what it does; recording it, the target's relations as well as its answer where "
  "their answers there agree, is a **test** that solves the problem whatever it records, since an argument from "
  "what it records rules out at least one of them for as long as that argument stays usable; an answer it rules "
  "out stays ruled out on \\(p\\) for as long as the argument that rules it out stays usable (Part VIII).",
  "LISTED", "establish -> record; fits, refutes -> ruled out, tentative while the argument stays usable; "
  "'an argument from what it records ... that argument stays usable' where the sceptic wrote 'what it records, "
  "for as long as the record stays usable', since (K2) makes argument steps, not records, usable, and 'rule out' "
  "is kept for arguments", kind="rewording",
  claim="Draft 5: 'an answer it refutes stays refuted on p'. Scrubbed: it stays ruled out only for as long as the "
        "argument that rules it out stays usable. The permanence that needs no assessor stays at Part VIII's (A) level.")
E(317, "so no established answer holds one of them to account without the other; a test inside \\(C\\) can refute "
       "one of them without the other",
  "so no argument from an answer recorded in \\(C\\) rules out one of them without the other; a test inside "
  "\\(C\\) can rule out one of them without the other", "LISTED",
  "established, refute; 'from an answer recorded in C' where the sceptic wrote 'no argument usable by the "
  "assessor', which would contradict the next clause (a test for a failure of its own)", kind="rewording")
E(317, "the term says nothing about which of them is right.",
  "the term says nothing about which of them, and not the other, is an account on a finer contract.",
  "TRUTH-OR-FOUNDATION", "right -> the change that would separate them")
E(317, 'and a claim that one is right and the other wrong is a claim that some admitted change outside \\(C\\) '
       'separates them, and must supply it, as a claim that one assignment of anchors is "really" right must',
  "and a claim that one of them and not the other meets (E) on a contract with some admitted change outside "
  "\\(C\\) is a claim that such a change separates them, and must supply it, as a claim that one assignment of "
  "counterparts, and not the other, is the target's must", "TRUTH-OR-FOUNDATION",
  "right, wrong, really, anchors: contrastive restatement", kind="rewording")
E(317, "they pose a problem of the first kind while both fit;",
  "they pose a problem of the first kind while neither is ruled out;", "LISTED", "fit -> not ruled out")
E(317, "or by whether anyone has checked the candidate against it", "or by whether anyone has tested the candidate on it",
  "MISSED", "checked -> tested")
E(317, "and the problem for \\(p\\) stands until what is established leaves at most one of them fitting.",
  "and the problem for \\(p\\) remains until at least one of them is ruled out for that assessor.", "LISTED",
  "established, fitting -> ruled out")
E(317, "Nothing here counts rivals, grades a candidate or ranks candidates.",
  "Nothing here counts rivals or orders candidates: of one candidate, the only thing said is whether it is ruled "
  "out for an assessor; of two, whether they conflict.", "RANKING",
  "grades, ranks: the text's guard against grading kept (S20, lesson S26), in the word 'orders'", kind="rewording")
E(317, "meets a claimed obligation only by dropping the other, which fits as well, where keeping every rival that "
       "fits is among the protected obligations",
  "meets a claimed aim only by dropping the other, which is not ruled out either, where keeping every rival not "
  "ruled out is among the protected aims", "LISTED", "fits -> not ruled out; obligation -> aim")

# ---------------------------------------------------------------- Part VII
E(325, "Direction is derived from the admitted edits;", "Direction is set by the admitted edits;", "LISTED",
  "derived from -> set by")
E(331, "its support is circular though its content might be true.",
  "it is circular, though its content might be faithful on the contract.", "LISTED",
  "support (evidential, not a member of S) and true (sceptic's ruling)")
E(335, "Equal values do not establish reachability.", "Equal values do not suffice for reachability.", "LISTED",
  "establish (no assessor meant) -> suffice for")
E(335, "and does not refute the scoped result.", "and does not rule out the scoped result.", "TRUTH-OR-FOUNDATION",
  "refute -> rule out")
E(339, "The rival's supposed structure is anchored to a *deleted* subnetwork,",
  "The rival's supposed structure has as its counterpart a *deleted* subnetwork,", "TRUTH-OR-FOUNDATION",
  "anchored -> counterpart")
E(339, "it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be.",
  "it is offered as an account, and is listed under attack (B) in Part XV as a place where it may not be one.",
  "RANKING", "adequate -> an account")
E(343, "Non-circular dependence is witnessed by \\(I_3\\) under removal of skewness and by "
       "\\(\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}\\) under removal of oddness. Non-vacuity is witnessed by any "
       "nonzero odd skew matrix.",
  "Non-circular dependence is met: \\(I_3\\) is an instance under removal of skewness, and "
  "\\(\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}\\) under removal of oddness. Non-vacuity is met: any nonzero odd "
  "skew matrix is an instance.", "TRUTH-OR-FOUNDATION", "witnessed -> instance")
E(343, "That a three-line proof is shorter", "That a three-line mathematical argument is shorter", "LISTED",
  "proof -> mathematical argument")

# ---------------------------------------------------------------- Part VIII
E(353, "the same holds for every admitted finite composition", "the same equation is met by every admitted finite composition",
  "TRUTH-OR-FOUNDATION", "holds (satisfaction) -> is met")
E(363, "satisfies \\(e_n\\le", "meets the bound \\(e_n\\le", "TRUTH-OR-FOUNDATION", "satisfies -> meets")
E(369, "and the same holds on every question with the same target and query",
  "and so on every question with the same target and query", "TRUTH-OR-FOUNDATION",
  "'holds' only a joint here (sceptic's ruling)")
E(369, "Once it is established for an assessor that the target's answer at \\((a,b)\\) is not \\(y\\), this is "
       "established for that assessor of every such candidate alike,",
  "Once an argument usable by an assessor rules out \\(y\\) as the target's answer at \\((a,b)\\), every such "
  "candidate alike is ruled out for that assessor,", "LISTED", "established -> ruled out for an assessor",
  kind="rewording")
E(369, 'Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target\'s answer at '
       '\\((a,b)\\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the '
       'background and instruments it relies on. If a premise about them ceases to be live, the receipt is not usable '
       'and the exclusion ceases to be established, for every such candidate alike; no candidate is thereby shown to '
       'be an account (K2).',
  'Here "ruled out" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that '
  'rules out \\(y\\) as the target\'s answer at \\((a,b)\\), and by (K3) an argument from the test that records it '
  'rules out a candidate only together with the background and instruments the test uses. If a premise about them '
  'ceases to be live, the argument is not usable and those candidates are no longer ruled out by it, every such '
  'candidate alike; no candidate becomes an account by that (K2).',
  "LISTED", "established, receipt, tells against, relies on, shown: ruled out for an assessor; no 'openly' or "
  "'visibly' (sceptic's ruling on hard case 6)", kind="rewording")

# ---------------------------------------------------------------- Part IX
E(373, "# Part IX — Criticism, use, and standing", "# Part IX — Criticism, use, and usable arguments",
  "TRUTH-OR-FOUNDATION", "standing -> usable arguments; (K2) already defines Usable_j(u)")
E(377, "alleged defect \\(\\delta\\), grounds \\(g\\), and a connection.",
  "alleged defect \\(\\delta\\), premise \\(g\\), and a connection.", "TRUTH-OR-FOUNDATION",
  "grounds -> premise, (K2)'s word")
E(383, "until an organization represents it as grounds for an alleged defect in a target.",
  "until an organization represents it as the premise of a criticism alleging a defect in a target.",
  "TRUTH-OR-FOUNDATION", "grounds for -> premise of a criticism (sceptic: a defect has no premises)")
E(385, "Using an invalid objection does not make it valid.",
  "Using an objection gives it no bearing (K1) and makes no argument from it usable (K2).", "BELIEF",
  "valid: names both (K1) and (K2), since draft 5 does not say which 'valid' meant (sceptic)", kind="rewording")
E(387, "**Standing.** For argument application \\(u\\)", "**Usability.** For argument step \\(u\\)",
  "TRUTH-OR-FOUNDATION", "standing -> usability; argument application -> argument step")
E(390, "\\operatorname{Lic}_j(u)", "\\operatorname{Form}_j(u)", "TRUTH-OR-FOUNDATION",
  "license -> form (Claude's reading; draft 5 does not define Lic)")
E(393, "Withdrawing a premise removes a license; it does not make the conclusion false.",
  "\\(\\operatorname{Form}_j(u)\\): the inference form of \\(u\\) is one \\(j\\) admits [Claude's reading; draft 5 "
  "names this predicate and does not define it]. Withdrawing a premise makes the step "
  "unusable; it does not rule the conclusion out.", "TRUTH-OR-FOUNDATION",
  "license, false: 'admit' is draft 5's word for a declared inclusion that can be withdrawn (sceptic)",
  kind="rewording")
E(395, "**What a test refutes.** For \\(T\\land B\\land I\\Rightarrow O\\), an established \\(\\neg O\\) yields "
       "\\(\\neg(T\\land B\\land I)\\) and nothing narrower.",
  "**What a test rules out.** For \\(T\\land B\\land I\\Rightarrow O\\), an argument usable by \\(j\\) that rules "
  "out \\(O\\) rules out \\(T\\land B\\land I\\) together for \\(j\\), and nothing narrower.", "LISTED",
  "refutes, established (sceptic's wording)", kind="rewording")
E(397, "**Receipts.** An evidence leaf is", "**Arguments.** A record leaf is", "BELIEF",
  "receipt -> argument; evidence leaf -> record leaf")
E(397, "A receipt is a derivation tree over leaves.",
  "An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated "
  "assumptions and definitions.", "LISTED",
  "receipt, derivation: leaves other than records, so Arguments 1-10 fall inside the definition (sceptic)",
  kind="rewording")
E(397, "For \\(\\phi\\), \\(P_j(\\phi)\\) and \\(N_j(\\phi)\\) are the usable receipts for and against. Negation "
       "exchanges them; missing evidence stays missing.",
  "For \\(\\psi\\), \\(R_j(\\psi)\\) is the set of arguments usable by \\(j\\) that rule out \\(\\psi\\). Where no "
  "argument usable by \\(j\\) rules out \\(\\phi\\), that absence rules out nothing, neither \\(\\phi\\) nor "
  "\\(\\neg\\phi\\).", "BELIEF",
  "receipts for and against -> one set of arguments that rule out; 'Negation exchanges them' dropped (sceptic)",
  kind="rewording",
  claim="Draft 5 had two sets, usable receipts for and against a claim, exchanged by negation. The scrubbed text has "
        "one set, R_j(psi), the usable arguments that rule out psi; nothing is 'for' a claim.")
E(397, "A record reconstructed from the claim it is meant to support is not a receipt for that claim.",
  "A record reconstructed from a claim does not rule out that claim's denial.", "LISTED",
  "support, receipt for: contrastive, no 'for'")

# ---------------------------------------------------------------- Part X
E(403, "(s,c,\\xi;U)\\) holds when", "(s,c,\\xi;U)\\) is met when", "TRUTH-OR-FOUNDATION", "holds -> is met")
E(403, "and supporting the declared use task \\(U\\)", "and serving the declared use task \\(U\\)", "LISTED",
  "supporting (ordinary sense) -> serving")
E(403, "A system may understand a false theory.", "A system may understand a theory in error.",
  "TRUTH-OR-FOUNDATION", "false -> in error")
E(403, "it establishes neither the wider understanding it falls short of nor a permanent inability to reach it.",
  "it suffices neither for the wider understanding it falls short of nor for a permanent inability to reach it.",
  "LISTED", "establishes (no assessor meant) -> suffices for")
E(405, "(s,c,h,e)\\) holds when", "(s,c,h,e)\\) is met when", "TRUTH-OR-FOUNDATION", "holds -> is met")
E(411, "the witnesses differ.", "the traces differ.", "TRUTH-OR-FOUNDATION", "witness -> trace")
E(427, "Credit for content and ownership of a process are different attributions:",
  "Contribution of content and ownership of a process are different attributions:", "MISSED", "credit dropped")
E(427, "Ownership is not defined by the capability it is meant to ground (Part XII).",
  "Ownership is not defined by the capability attributed through it (Part XII).", "TRUTH-OR-FOUNDATION",
  "ground -> attributed through it")
E(429, "Closing an episode is a decision, not a proof.", "Closing an episode is a choice, not an argument.",
  "LISTED", "S21's line between choosing and the other option being ruled out")

# ---------------------------------------------------------------- Part XI
E(433, "# Part XI — Progress, knowledge, and the normative", "# Part XI — Repair, created explanation, and appraisal",
  "BELIEF", "progress -> repair (Part XI defines Repair); knowledge -> created explanation (provisional); "
  "normative -> appraisal", owner=True)
E(441, "that it held on every occasion it covers", "that it was met on every occasion it covers",
  "TRUTH-OR-FOUNDATION", "held (satisfaction) -> was met")
E(441, "Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives.",
  "Their declaration makes no appraisal of the aims, and (P) puts no order on alternatives.", "RANKING",
  "worth dropped (sceptic); rank (sceptic's missed word) -> order")
E(441, "\\(\\operatorname{ProducedBy}\\) holds when an active route (Part IX) runs from \\(\\Delta\\) to the repair; "
       "it credits each contribution the history establishes, and where two sufficient contributions both ran, both "
       "are credited and the history supplies no division of credit that it does not contain.",
  "\\(\\operatorname{ProducedBy}\\) is met when an active route (Part IX) runs from \\(\\Delta\\) to the repair; it "
  "attributes the repair to each contribution the history contains, and where two sufficient contributions both ran, "
  "the repair is attributed to both and the history supplies no division of the attribution that it does not contain.",
  "MISSED", "credit -> attribution; establishes (no assessor meant) -> contains; holds -> is met")
E(441, "A correct account that produced nothing,", "An account that produced nothing,", "TRUTH-OR-FOUNDATION",
  "correct added nothing")
E(443, "**Created explanatory knowledge.** An epistemic obligation requires a correct account, or the correction of a "
       "use through one, to be deployable. With \\(O_{\\mathrm{ep}}\\subseteq O\\) the epistemic obligations,",
  "**Created explanation** [provisional name, for the owner to decide, as are \"understanding\" (Part X) and "
  "\"surprise\" (Part IV); draft 5's name and the choice are in the vocabulary, as used]. An explanatory aim "
  "requires an account, or the correction of a use through one, to be deployable. With "
  "\\(O_{\\mathrm{ex}}\\subseteq O\\) the explanatory aims,", "BELIEF",
  "knowledge (OWNER ruling): proposal's term used provisionally and marked; epistemic obligation -> explanatory aim; "
  "correct dropped", kind="rewording", owner=True)
E(447, "\\operatorname{CreateEK}", "\\operatorname{CreateEx}", "BELIEF", "knowledge -> created explanation (provisional)",
  owner=True)
E(448, "O_{\\mathrm{ep}}", "O_{\\mathrm{ex}}", "BELIEF", "epistemic -> explanatory aim")
E(450, "\\tag{EK}", "\\tag{EX}", "BELIEF", "knowledge -> created explanation (provisional)", owner=True)
E(453, "(\\Delta,c,o;\\xi,\\xi')\\) holds when", "(\\Delta,c,o;\\xi,\\xi')\\) is met when", "TRUTH-OR-FOUNDATION",
  "holds -> is met")
E(453, "to rescue adequacy is a new claim at a new index, and does not retroactively satisfy (EK).",
  "to rescue its meeting (E) is a new claim at a new index, and does not retroactively meet (EX).", "RANKING",
  "adequacy -> meeting (E); satisfy -> meet")
E(455, "**Worth, and the normative relation.** Repairing an obligation establishes that it was repaired; it "
       "establishes nothing about whether the obligation, or the question that led to it, was worth having. Where a "
       "claim invokes worth, the semantics takes the **normative relation** \\(\\mathcal N\\) (primitive 2, Part XIV)",
  "**Appraisal.** Repairing an aim repairs it and says nothing about how anyone appraises the aim, or the question "
  "that led to it. Where a claim invokes an appraisal, the semantics takes the **appraisal relation** "
  "\\(\\mathcal N\\) (import 2, Part XIV)", "RANKING",
  "worth dropped altogether (sceptic); establishes -> says; normative -> appraisal; primitive -> import",
  kind="rewording")
E(455, "The semantics does not derive \\(\\mathcal N\\),", "The semantics does not define \\(\\mathcal N\\),",
  "LISTED", "derive -> define")

# ---------------------------------------------------------------- Part XII
E(461, "Possibility is the absence of a law-imposed limit short of perfection on performance and retention; it is "
       "not one successful trajectory.",
  "Possibility is the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be "
  "performed and retained; it is not one trajectory that performed the task.", "RANKING",
  "perfection, successful -> tolerance, short of exact; performed", kind="rewording")
E(469, "Execution families are nonempty on legitimate inputs; deadlock is not vacuous success.",
  "Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.",
  "RANKING", "legitimate -> admitted; success -> performance (tasks are performed, conditions met: sceptic)")
E(475, "Ownership is grounded in the processes and resources the boundary includes, never in the capability being "
       "attributed: \"owned because it can, and can because owned\" grounds neither.",
  "Ownership is defined by the processes and resources the boundary includes, never by the capability being "
  "attributed: \"owned because it can, and can because owned\" defines neither.", "TRUTH-OR-FOUNDATION",
  "grounded -> defined by")
E(479, "**Grades.** The accuracy grades of the physical module (Part XIV) form a directed preorder \\(Q_\\Theta\\), "
       "increasingly demanding and short of perfection; \\(q\\in Q_\\Theta\\) is a grade of performance and "
       "\\(r\\in Q_\\Theta\\) a grade of retention.",
  "**Tolerances.** The tolerances of the physical module (Part XIV) form a directed preorder \\(Q_\\Theta\\), each "
  "admitting no performance the one before it excludes, and short of exact; \\(q\\in Q_\\Theta\\) is a tolerance of "
  "performance and \\(r\\in Q_\\Theta\\) a tolerance of retention.", "RANKING",
  "accuracy grades -> tolerances: the order is set inclusion, not merit (lesson S26)")
E(479, "physically achievable at grades \\((q,r)\\)", "physically achievable at tolerances \\((q,r)\\)", "RANKING",
  "grade -> tolerance")
E(479, "at those grades, as owned capability requires", "at those tolerances, as owned capability requires", "RANKING",
  "grade -> tolerance")
E(479, "achievable at every grade, which", "achievable at every tolerance, which", "RANKING", "grade -> tolerance")
E(479, "Finite-grade capability does not imply possibility at all grades.",
  "Capability at a given tolerance does not imply possibility at every tolerance.", "RANKING", "grade -> tolerance")
E(481, "It is fallible and checkable as any physical claim is.", "It is fallible and testable as any physical claim is.",
  "MISSED", "checkable -> testable")

# ---------------------------------------------------------------- Part XIII
E(495, "A finite list of failures is not a barrier proof; a bypass refutes a proposed barrier.",
  "A finite list of failures is not an argument that no bypass exists; one bypass rules out a proposed barrier.",
  "LISTED", "proof, refutes")
E(495, "(s,T,\\chi)\\) holds when", "(s,T,\\chi)\\) is met when", "TRUTH-OR-FOUNDATION", "holds -> is met")
E(509, "a historical extension does not certify it; a finite performance record does not establish it.",
  "a historical extension leaves it open; a finite performance record does not suffice for it.", "BELIEF",
  "certify -> leaves open (compatibility, not 'rule out': sceptic); establish -> suffice for")

# ---------------------------------------------------------------- Part XIV
E(515, "**Primitives.** The semantics has two.", "**Imports.** The semantics has two.", "TRUTH-OR-FOUNDATION",
  "primitive -> import")
E(517, "resources, accuracy grades, and", "resources, tolerances, and", "RANKING", "grades -> tolerances")
E(518, "when a question invokes worth. It is taken as an input and never derived;",
  "when a question invokes an appraisal. It is taken as an input and never defined in terms of anything else;",
  "LISTED", "worth dropped; derived -> defined")
E(520, "Everything else is derived from the two primitives,", "Everything else is defined in terms of the two imports,",
  "LISTED", "derived from -> defined in terms of")
E(520, "origin, repair, knowledge, capability", "origin, repair, created explanation, capability", "BELIEF",
  "knowledge (OWNER ruling) -> created explanation, provisional", owner=True)
E(522, "Besides the two primitives,", "Besides the two imports,", "TRUTH-OR-FOUNDATION", "primitive -> import")
E(522, "the scope of a contract and what makes a restriction appropriate (Part III);",
  "the scope of a contract and why the question asked is answered on that restriction and not on a wider one "
  "(Part III);", "RANKING", "appropriate -> contrastive, as at l. 159")
E(522, "a weighting of credit among several contributions to one achievement, beyond any division of credit its "
       "history contains",
  "a weighting of attribution among several contributions to one achievement, beyond any division its history "
  "contains", "MISSED", "credit -> attribution")
E(522, "A verdict that depends on one of these, or on the normative relation where a claim invokes worth, is a verdict "
       "given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than "
       "choosing the input from the verdict wanted. The semantics supplies no probability of truth, no merit function "
       "and no ranking of thinkers, and a claim that needs one is unsettled.",
  "An assessment that depends on one of these, or on the appraisal relation where a claim invokes an appraisal, is an "
  "assessment given the input; where the input is missing, the assessment is left open and the semantics says so "
  "rather than choosing the input from the assessment wanted. The semantics supplies no probability on claims and no "
  "function that orders explanations or thinkers, and a claim that needs one is left open.", "MISSED",
  "verdict -> assessment; unsettled -> left open; truth, merit, ranking -> as at l. 25", kind="rewording")
E(524, "**Indices, not primitives.**", "**Indices, not imports.**", "TRUTH-OR-FOUNDATION", "primitive -> import")
E(524, "none is a predicate that could be true or false", "none is a predicate that a case meets or fails", "LISTED",
  "true or false -> meets or fails")
E(526, "which are stated, not derived.", "which are stated, not defined.", "LISTED", "derived -> defined")
E(526, "what is established on usable receipts (Part IX), fits on what is established and (E), a problem for \\(p\\) "
       "on rivals and fits,",
  "being ruled out for an assessor on usable arguments (Part IX) and (E), a problem for \\(p\\) on rivals and on "
  "neither being ruled out,", "LISTED", "established, receipts, fits -> ruled out", kind="rewording")
E(526, 'Nothing depends on a predicate meaning "really explains," "is a cause," or "is knowledge."',
  'Nothing depends on a predicate that says "explains" without a question and a contract, or "is a cause," or '
  '"is a created explanation."', "BELIEF", "really, knowledge: as at l. 31", kind="rewording", owner=True)
E(526, "The order is well founded: a representation justified only by its own construction, or an ownership and a "
       "capability justified only by each other, has not supplied its place in it, and a separate proof that would "
       "supply it counts only when the account uses it.",
  "The order has no cycle and no endless descent: a representation defined only by its own construction, or an "
  "ownership and a capability each defined only by the other, has not supplied its place in it, and a separate "
  "argument that would supply it is part of the account only when the account uses it.", "TRUTH-OR-FOUNDATION",
  "well founded, justified, proof, counts: the mathematical content of the order without the foundation words")
E(528, "with correct typing, satisfying physical realization", "with typing as declared, meeting physical realization",
  "TRUTH-OR-FOUNDATION", "correct -> as declared; satisfying -> meeting")
E(528, "The knowledge-creation class: an instance of (EK).", "The explanation-creation class: an instance of (EX).",
  "BELIEF", "knowledge (OWNER ruling), provisional", owner=True)

# ---------------------------------------------------------------- Part XV
E(534, "The load-bearing claims, in the order of how much falls if they fail, each with what would refute it.",
  "The claims the rest depends on, in the order of how much falls if they fail, each with what would rule it out.",
  "MISSED", "load-bearing, refute")
E(534, "A case whose verdict turns on an input the case does not state, where the input is one of the declared inputs "
       "Part XIV lists or the normative relation, is a case with a missing input, not a refutation.",
  "A case whose assessment turns on an input the case does not state, where the input is one of the declared inputs "
  "Part XIV lists or the appraisal relation, is a case with a missing input, not an argument that rules a claim out.",
  "MISSED", "verdict -> assessment; refutation -> argument that rules out")
E(536, "that plainly provides no account.", "that nonetheless explains nothing.", "MISSED",
  "plainly (sceptic's missed word); said as the section's own test ('still explains nothing')")
E(538, "A genuine explanation whose organization",
  "An explanation, argued to be one and not a non-explanation by an argument that does not use (E), whose organization",
  "TRUTH-OR-FOUNDATION", "genuine: the proposal's wording, kept by the sceptic", kind="rewording",
  claim="Draft 5's 'a genuine explanation' becomes 'an explanation, argued to be one and not a non-explanation by an "
        "argument that does not use (E)': what made an explanation genuine is now said as the argument that would "
        "have to be given.")
E(540, "This refutes Derivation 1 and reinstates correspondence as primitive.",
  "Such a case would rule out Argument 1 and make correspondence an import again.", "TRUTH-OR-FOUNDATION",
  "refutes, primitive")
E(542, "is the theorem's own qualification, not a refutation);", "is the claim's own qualification, not an argument that rules it out);",
  "TRUTH-OR-FOUNDATION", "theorem -> claim; refutation")
E(542, "a demonstration that every construction witness can be rewritten",
  "an argument that every construction trace can be rewritten", "TRUTH-OR-FOUNDATION", "demonstration -> argument")
E(542, "or a showing that the primitive layer of Part IV", "or an argument that the object layer of Part IV",
  "TRUTH-OR-FOUNDATION", "showing -> argument; primitive layer -> object layer")
E(544, "A showing that treating", "An argument that treating", "TRUTH-OR-FOUNDATION", "showing -> argument")
E(544, "or fails to capture some genuine case of finding the right question (against Derivation 5).",
  "or fails to capture some case of finding a new question (against Argument 5).", "TRUTH-OR-FOUNDATION",
  "genuine dropped; 'the right question' -> 'a new question' (sceptic: the narrowed clause would change the claim)")
E(546, "A counterexample to the finite monotone theorem,", "A counterexample to the finite monotone claim,",
  "TRUTH-OR-FOUNDATION", "theorem -> claim")

# ---------------------------------------------------------------- Part XVI
E(550, "# Part XVI — Derivations", "# Part XVI — Arguments", "LISTED", "derivation -> argument")
E(552, "## 1. Kind preservation is a theorem, not a condition", "## 1. Kind preservation needs no condition of its own",
  "TRUTH-OR-FOUNDATION", "theorem: the title said contrastively")
E(554, "**Claim.** If a transport satisfies (F1) on \\(C\\), then every active component \\(k\\) of \\(E\\) has the "
       "same signature on \\(\\tau[C]\\) as its anchor \\(\\lambda(k)\\) has on \\(C\\), up to the port translation.",
  "**Claim.** If a transport meets (F1) on \\(C\\), no active component \\(k\\) of \\(E\\) has a signature on "
  "\\(\\tau[C]\\) that differs from the one its counterpart \\(\\lambda(k)\\) has on \\(C\\), up to the port "
  "translation.", "TRUTH-OR-FOUNDATION", "anchor -> counterpart; the claim said as what it excludes (sceptic)",
  kind="rewording")
E(558, "**Corollary.** A condition \"each component must anchor to a component of the same kind\"",
  "**Consequence.** A condition \"each component's counterpart must be a component of the same kind\"",
  "TRUTH-OR-FOUNDATION", "corollary -> consequence; anchor -> counterpart")
E(560, "## 2. Same anchors, one account", "## 2. Same counterparts, one account", "TRUTH-OR-FOUNDATION",
  "anchor -> counterpart")
E(562, "gives each \\(k\\) and \\(\\varphi(k)\\) one anchor,", "gives each \\(k\\) and \\(\\varphi(k)\\) one counterpart,",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(564, "By Derivation 1, \\(k\\) has the signature of its anchor on the ports its translation names, and "
       "\\(\\varphi(k)\\) the signature of the same anchor on the same ports;",
  "By Argument 1, \\(k\\) has the signature of its counterpart on the ports its translation names, and "
  "\\(\\varphi(k)\\) the signature of the same counterpart on the same ports;", "TRUTH-OR-FOUNDATION",
  "anchor -> counterpart; derivation -> argument")
E(566, "candidates that anchor different subnetworks,", "candidates whose counterparts are different subnetworks,",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(568, "differ only in which component carries which anchor,", "differ only in which component has which counterpart,",
  "TRUTH-OR-FOUNDATION", "anchor -> counterpart")
E(568, 'a claim that one assignment is "really" right is a claim', "a claim that one assignment, and not the other, "
  "is the target's is a claim", "TRUTH-OR-FOUNDATION", "really right -> contrastive")
E(572, "The presence of an unseen pair alone does not establish that such a \\(t'\\) exists;",
  "The presence of an unseen pair alone leaves open whether such a \\(t'\\) exists;", "LISTED",
  "establish (no assessor meant) -> leaves open")
E(576, "the guarantee of a differing survivor", "the claim of a differing survivor", "TRUTH-OR-FOUNDATION",
  "guarantee -> claim")
E(582, "there is no expectation and hence no violation", "there is no prediction and hence no violation", "BELIEF",
  "expectation -> prediction")
E(584, "by their witnesses, not by their outcomes", "by their traces, not by their outcomes", "TRUTH-OR-FOUNDATION",
  "witness -> trace")
E(588, "satisfies (G) and, where the other conjuncts hold, (EK).",
  "meets (G) and, where the other conjuncts are met, (EX).", "TRUTH-OR-FOUNDATION",
  "satisfies, hold -> meets, are met; (EK) -> (EX) provisional", owner=True)
E(592, "Finding the right question is a creative act on the same footing as answering one.",
  "Finding a new question is a creative act, as answering one is.", "TRUTH-OR-FOUNDATION",
  "right, same footing (sceptic's ruling)")
E(592, "That a question was found says nothing about its worth (Part XI).",
  "That a question was found says nothing about how anyone appraises it (Part XI).", "RANKING", "worth dropped")
E(594, "## 6. There are two primitives", "## 6. There are two imports", "TRUTH-OR-FOUNDATION", "primitive -> import")
E(596, "is defined from \\(\\Theta\\)", "is defined in terms of \\(\\Theta\\)", "LISTED",
  "one phrase for definition throughout")
E(598, "with the definitions that rest on them, following each definition to its base in the primitives, the indices "
       "and the inputs.",
  "with the definitions that use them, following each definition back until it reaches the imports, the indices or "
  "the declared inputs.", "TRUTH-OR-FOUNDATION", "rest on, base, primitives")
E(600, '"is a cause," or "is knowledge." The two primitives are a theory of matter and, when a question requires it, '
       'a theory of reasons. Neither is a semantic primitive about explanation.',
  '"is a cause," or "is a created explanation." The two imports are a theory of matter and, when a question requires '
  'it, a theory of reasons. Neither is a predicate about explanation taken as an import.', "TRUTH-OR-FOUNDATION",
  "knowledge (provisional), primitive -> import", owner=True)
E(606, "The assessment is indexed to \\(C\\) and its truth is fixed at that index",
  "The assessment is indexed to \\(C\\), and whether \\(\\mathcal E\\) meets (E) on \\(C\\) is fixed at that index",
  "LISTED", "truth -> whether it is met", kind="rewording")
E(606, "are claims at different indices and may both be true.",
  "are claims at different indices, and \\(\\mathcal E\\) can meet (E) on \\(C\\) and fail it on \\(C'\\).",
  "LISTED", "true -> meet and fail at two indices", kind="rewording")
E(608, "not a licensed operation of the semantics", "not an operation the semantics admits", "TRUTH-OR-FOUNDATION",
  "licensed -> admits")
E(610, "## 8. Equivariance under genuine recoding", "## 8. Equivariance under structure-preserving recoding",
  "TRUTH-OR-FOUNDATION", "genuine -> the claim's own condition")
E(616, "The same holds for attribution from emitted text", "The same goes for attribution from emitted text",
  "TRUTH-OR-FOUNDATION", "holds -> goes for")
E(624, "expects nothing there", "predicts nothing there", "BELIEF", "expects -> predicts")
E(628, "then (G) holds.", "then (G) is met.", "TRUTH-OR-FOUNDATION", "holds -> is met")
E(628, "while protecting \"predict displacements correctly,\" then (P) holds; and since the account is adequate on its "
       "contract and deployable, (EK) holds.",
  "while protecting \"predict the displacements that occur,\" then (P) is met; and since \\(S_1\\) is an account on "
  "its contract and deployable, (EX) is met.", "TRUTH-OR-FOUNDATION",
  "correctly, adequate, holds; 'that occur' where the proposal wrote 'observed', which brings in an observer the aim "
  "does not name", owner=True)
E(630, "A claim that \"component 1 is *really* thing 1\" is a claim",
  "A claim that \"component 1 is thing 1 and not thing 2\" is a claim", "TRUTH-OR-FOUNDATION", "really -> contrastive")
E(630, "it is the correct report that identity, at this grain, is exhausted by trajectory.",
  "it is what the contract contains: identity, at this grain, is exhausted by trajectory.", "TRUTH-OR-FOUNDATION",
  "correct report -> what the contract contains")
E(632, "This episode is a relative-consistency witness for the class. It is not a claim that any actual infant, "
       "animal, or program has been shown to instantiate it.",
  "This episode is a relative-consistency instance for the class. It is not a claim that any actual infant, animal, "
  "or program instantiates it.", "TRUTH-OR-FOUNDATION", "witness -> instance; shown dropped")


# ---------------------------------------------------------------- residue left on purpose (BORDERLINE)
POSS = "possession, not satisfaction: someone holds a thing (the proposal's rule 3 keeps 'hold' only for this)"
OWNQ = ("the owner's question, as for 'knowledge' (sceptic's OWNER ruling): defined in the text with no attitude in "
        "it, kept provisionally as the proposal keeps it")
JOINT = "a logical joint between steps, kept (the proposal's rule, the sceptic's joints row)"
ADOPT = "'adopt' kept, declared tentative once in Part I (l. 75), as the sceptic ruled"
B(8, "accept", "the definition the task asks for: accepting is a person's tentative choice")
B(8, "accepted", "the owner's rule, restated in the definition", count=2)
B(8, "accepting", "the definition: the semantics never defines accepting by arguments held")
B(8, "holds", POSS)
B(11, "held", "'held to a target by a transport': the transport joins the organization to its target; not "
  "satisfaction, not possession, and nothing is asserted of it")
B(21, "yields", JOINT)
B(39, "more admitted", "'more admitted changes': a larger set of admitted changes, a count of edits, not a ranking")
B(45, "realism", "'structural realism': the name of another theory, which the objection compares; the theory claims "
  "nothing by it", count=2)
B(67, "accepts", "a person's act, marked tentative as the owner's rule requires (the one ordinary use in draft 5)")
B(75, "adopted", ADOPT, count=2)
B(75, "adopt", "the one declaration that adopting is tentative (sceptic's ruling)")
B(127, "follows", "causal: the reading changes when the part changes; not a joint of an argument and not a status")
B(159, "adopted", ADOPT)
B(201, "hold", POSS)
for n, w, c in ((215, "surprise", 1), (221, "surprise", 1), (223, "surprise", 3), (223, "surprised", 2),
                (576, "surprise", 1), (578, "surprise", 1), (580, "surprised", 1), (582, "surprise", 1),
                (584, "surprise", 1), (624, "surprise", 1)):
    B(n, w, OWNQ + "; 'surprise' is a violation of a selected "
      "transport outside its history (Part IV)", count=c)
B(253, "held", "'held fixed': kept unchanged during the assessment; no satisfaction, no possession")
B(255, "follows", JOINT)
B(277, "elegance", "names the aesthetic property (E) draws no line on; nothing is ordered by it")
B(315, "adopted", ADOPT)
B(343, "real", "the real numbers ('real skew-symmetric matrix')")
B(343, "held", "'held fixed': kept unchanged under the contract's edits")
B(363, "follows", JOINT)
B(369, "holds", POSS)
B(401, "Understanding", OWNQ)
B(403, "holds", POSS)
B(403, "understand", OWNQ)
B(403, "understanding", OWNQ)
B(429, "holds", POSS)
B(443, "understanding", "inside the provisional-name marker, which names the owner's open question")
B(443, "surprise", "inside the provisional-name marker, which names the owner's open question")
B(443, "correction", "the owner's 'error correction'")
B(455, "follows", JOINT)
B(461, "permitted", "physics sense: a transformation the adopted physics does not exclude, as in the constructor-"
  "theoretic formulation l. 461 adopts; no one grants it; dropping the word would change which transformations "
  "count as tasks")
B(461, "adopts", ADOPT)
B(479, "imply", JOINT)
B(497, "advanceable", "a challenge on which a further step can be taken; nothing is compared with anything (kept, as "
  "the proposal ruled)")
B(509, "entail", JOINT)
B(520, "Understanding", OWNQ)
B(526, "adopted", ADOPT)
B(566, "follows", JOINT)
B(580, "holds", POSS)
B(624, "shows", "display sense: 'the occupancy field shows nothing at its cell'")


# ================================================================ engine
def build():
    def manual_spans(n):
        out = []
        for e in ENTRIES:
            if e["line"] == n:
                c = L[n - 1].count(e["old"])
                if c != 1:
                    raise SystemExit("hand entry, line %d, occurs %d times: %r" % (n, c, e["old"][:70]))
                p = L[n - 1].index(e["old"])
                out.append((p, p + len(e["old"])))
        return out

    auto = []
    for n, line in enumerate(L, 1):
        ms = manual_spans(n)
        found = []
        for rx, repl, cat, reason, skip in AUTOS:
            if n in skip:
                continue
            for m in rx.finditer(line):
                a, b = m.span()
                if any(a < q and b > p for p, q in ms):
                    continue
                if any(a < f[1] and b > f[0] for f in found):
                    continue
                found.append((a, b, repl, cat, reason))
        found.sort()
        for i, (a, b, repl, cat, reason) in enumerate(found):
            lo = max([q for p, q in ms if q <= a] + [found[i - 1][1] if i else 0])
            hi = min([p for p, q in ms if p >= b] + [found[i + 1][0] if i + 1 < len(found) else len(line)])
            s, t = a, b
            while line.count(line[s:t]) > 1:
                grew = False
                if t < hi:
                    t += 1; grew = True
                if line.count(line[s:t]) > 1 and s > lo:
                    s -= 1; grew = True
                if not grew:
                    raise SystemExit("cannot make auto span unique on line %d: %r" % (n, line[a:b]))
            while s > lo and not line[s - 1].isspace():
                s -= 1
            while t < hi and not line[t].isspace():
                t += 1
            auto.append(dict(line=n, old=line[s:t], new=line[s:a] + repl + line[b:t], category=cat,
                             reason=reason, kind="swap", generated="AUTO rule"))
            if repl in ("(EX)",):
                auto[-1]["owner"] = "provisional term; the owner decides (sceptic's OWNER ruling on 'knowledge')"
    entries = sorted(ENTRIES + auto, key=lambda e: e["line"])
    R = {
        "about": "S95 Scrub replacements for draft 5 of revision 2 (md5 7f1d8ad02adf96e27622593bd263252e). "
                 "Made by replacements_source.py; applied by scrub_apply.py. Line numbers are draft 5's and "
                 "the scrubbed text's alike.",
        "notes": {
            "residue_scan": "scrub_apply.py --scan runs the register's word families (register.py) plus the sceptic's "
                            "missed families over the scrubbed text; every remaining hit is listed under 'borderline' "
                            "with a one-line reason, matched by draft-5 line and word (line numbers are shared).",
            "kind": "'swap' = a word or phrase exchanged; 'rewording' = the smallest span that needed new wording.",
            "claim_changed": "present only where what the sentence claims changed, not only its words.",
            "owner": "present on entries that use the proposal's provisional 'created explanation' (EX) for "
                     "draft 5's 'knowledge' (EK), the sceptic's one OWNER ruling; the text marks it at l. 443.",
            "fill_blank_lines": "the dated note (l. 2) and the Part 0 definitions of 'argument' and 'tentatively "
                                "accept' (l. 8) go on lines that are blank in draft 5, so no line number moves.",
        },
        "fill_blank_lines": FILL,
        "entries": entries,
        "borderline": BORDER,
    }
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("hand entries:", len(ENTRIES), " generated:", len(auto), " borderline notes:", len(BORDER))


if __name__ == "__main__":
    build()
