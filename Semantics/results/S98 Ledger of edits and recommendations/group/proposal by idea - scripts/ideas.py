# The idea lexicon for the S98 "by idea" proposal.
# Each idea: key, name, one-line rule, cues (regex, weight).  Cues are matched on
# the wording of sentences; a cue counts once per sentence.  HOME maps a place of
# the latest text (Part, heading, run-in label) to the idea its sentences carry by
# position.  VERSION 1 is the lens as first tried; VERSION 2 is the one adjustment.
import re

I = re.I
IDEAS = [
 ("frame", "The document's frame: title, claims, sources and departures",
  "sentences about the document itself: its title, what it claims and does not claim as a whole, its note of sources and departures, its revision notes",
  [(r"this document|the document|this semantics", 1.5), (r"sources and departures|\bsources?\b|departures?", 2),
   (r"revision note|revision record|\bnote\b", 1.5), (r"\btitle\b", 1.5), (r"version label|\blog S\d|decision S\d|\bdraft \d", 1.5),
   (r"Claude Fable Semantics", 2), (r"Deutsch|Popper|\bbooks?\b", 1.5)]),
 ("account", "What an account requires",
  "sentences about the conditions of (E) on an account: component and question fidelity, non-circular dependence, non-vacuity, and what (E) excludes",
  [(r"\baccounts?\b", 2), (r"faithful|fidelity", 2), (r"\(F1\)|\(F2\)", 2), (r"non-?circular", 2), (r"non-?vacu|vacuous", 2), (r"\(E\)", 2),
   (r"counterpart", 2), (r"adequa", 1), (r"protective", 2), (r"answer profile", 1), (r"\bmechanisms?\b", 1), (r"decomposition|assembled match", 1.5),
   (r"operatorname\{Account", 2)]),
 ("organization", "Organizations, roles and kinds",
  "sentences about organizations, their components and ports, roles, kinds as edit-signatures, levels, and substrate",
  [(r"organi[sz]ations?", 2), (r"\bkinds?\b", 2), (r"edit-signatures?|\bsignatures?\b", 2), (r"\broles?\b", 2), (r"\bports?\b", 2),
   (r"\bcomponents?\b", 1), (r"substrate", 2), (r"\blevels?\b", 1), (r"\bcorrelation", 1), (r"of one kind|kind preservation", 2)]),
 ("question", "Questions, contracts and scope",
  "sentences about questions, contracts of admitted changes, the respect as the query, scope, and a question that can be in error",
  [(r"\bcontracts?\b", 2), (r"\bquestions?\b(?![- ]finding| fidelity)", 1.5), (r"\bquery\b", 2), (r"\brespect\b", 1),
   (r"\bscop(e|ed|es)\b", 1.5), (r"admitted changes?|admits? (each|a|the) (change|edit)", 1), (r"\bfrozen\b|\bfreez", 2), (r"\branges?\b", 1),
   (r"\\operatorname\{Ans", 1), (r"\bin error\b", 1)]),
 ("provenance", "Provenance: selected, constructed and declared correspondence",
  "sentences about where a correspondence comes from: selection, construction, declaration, their traces, and genesis",
  [(r"provenance", 2), (r"\bselect(ed|ion)\b", 2), (r"\bconstructed\b", 2), (r"(construction|selection) response", 2),
   (r"\bgenesis\b|\(Prov\)", 2), (r"evolution|teleosemantic|survival condition|variation operator|\bpopulations?\b", 1.5),
   (r"stipulat", 1), (r"\btraces?\b", 1)]),
 ("layers", "Layers, transports and representation",
  "sentences about occurrences and contents, the object and simulation layers, transports and their results, recoding, and representation",
  [(r"\btransports?\b", 2), (r"object layer|simulation layer|\blayers?\b|two-layer", 2), (r"represent", 2), (r"\boccurrences?\b", 1.5),
   (r"\bcontents?\b", 1), (r"\bcarriers?\b", 1.5), (r"recod", 2), (r"equivarian", 2), (r"historical index", 2), (r"correspondences?", 1)]),
 ("surprise", "Prediction, surprise and violation",
  "sentences about prediction, expectation, violation and surprise",
  [(r"predict", 2), (r"surpris", 2.5), (r"violat", 2), (r"expectation|\bexpects?\b|\bexpected\b", 1.5), (r"incomplete history", 2)]),
 ("work", "Work, routes and commitments that do no work",
  "sentences about routes, criticality, interference, redundant and infinitary routes, and commitments that do no work (easy to vary)",
  [(r"\broutes?\b", 2), (r"critical", 2), (r"interfer", 2), (r"redundant", 2), (r"infinitary", 2), (r"(does|do) no work|\bwork\b", 1.5),
   (r"easy to vary|hard to vary|\bvary\b|variation family", 1.5), (r"contributory|indispensable", 2), (r"monotone claim", 2),
   (r"\bcommitments?\b", 1), (r"\\Gamma", 1), (r"\breach\b", 1)]),
 ("rivals", "Rivals, conflict and problems",
  "sentences about rivals, conflict between candidates, and the problems two rivals pose",
  [(r"\brivals?\b", 2.5), (r"conflict", 2), (r"\bproblems?\b", 2), (r"\bposed?\b|\bposes\b", 1), (r"in place of the other", 1),
   (r"perpetual motion", 1)]),
 ("ruling", "Ruling out and tentative acceptance",
  "sentences about what an assessor rules out or leaves not ruled out, tentative acceptance, and the words for how a claim is held",
  [(r"\brul(e|es|ed|ing)( \S+)? out\b", 2.5), (r"tentativ", 2.5), (r"\baccept(s|ed|ing)?\b", 2), (r"\bassessors?\b|\bassessment", 2),
   (r"usable by", 1), (r"\blive\b", 1.5), (r"stays? (failed|ruled out)", 2),
   (r"\btrue\b|\btruth\b|\bfalse\b|\bfits?\b|establish|refut|\breject|verdict|\bsettle|certif|justif|\bcorrect(ly)?\b|genuine|knowledge|\badopt|guarantee|legitimate|\bproven\b|\bproves?\b|\bwrong\b|\bright\b|\bfact\b", 1.5),
   (r"fallib", 1), (r"conjectur", 1)]),
 ("argument", "Arguments, premises and tests",
  "sentences about what an argument is (why this and not that), its steps, premises and record leaves, bearing, usability, reason use, and tests",
  [(r"\barguments?\b", 1.5), (r"\bpremises?\b", 2), (r"record leaf|\bleaves\b|\bleaf\b", 2), (r"argument steps?|\bsteps?\b", 1),
   (r"usab", 1.5), (r"\bbearing\b|\(K1\)|\(K2\)|\(K3\)", 2), (r"reason use", 2), (r"\btests?\b|\btested\b", 2),
   (r"observation|measurement|\brecord(s|ed|ing)?\b", 1.5), (r"inference form|operatorname\{Form|Form_j", 2),
   (r"\bproofs?\b|derivation|\bderiv|theorem|axiom|corollar|lemma|demonstration", 2), (r"why this and not", 2.5),
   (r"witness|receipt|evidence|\bgrounds?\b", 1.5)]),
 ("criticism", "Criticism, error and repair",
  "sentences about criticism and its use, error and defects, recognized difficulties, aims and repair",
  [(r"critici", 2.5), (r"repair", 2.5), (r"defects?", 2), (r"objections?", 1.5), (r"\berrors?\b|\berror-", 1.5),
   (r"recognized difficult|difficult", 2), (r"\baims?\b", 1.5), (r"obligations?", 1.5), (r"\bprotect", 1), (r"\bfail(ure|ed|s)?\b", 1)]),
 ("creativity", "Creativity, understanding and origin",
  "sentences about understanding, deployment, construction, newness, origin, ownership, episodes, created explanation and question-finding",
  [(r"understand", 2), (r"deploy", 2), (r"\bconstruction\b", 1.5), (r"newness|\bnovel", 2), (r"\borigin", 2), (r"ownership|\bowns?\b|\bowned\b", 1.5),
   (r"\bepisodes?\b", 2), (r"creat(ive|ivity|ion|ed)", 2), (r"question-finding|finding (of )?a (new )?question|\bnew question|\(QF\)", 2.5),
   (r"invent|\bguess", 1), (r"achievement|contributors?|attribut", 1.5)]),
 ("appraisal", "Aims, values and appraisal",
  "sentences about the appraisal relation, values and aesthetics, and how aims are appraised",
  [(r"apprais", 2.5), (r"normative", 2.5), (r"\bworth\b", 2), (r"\bvalues?\b", 1), (r"\bmerit", 2), (r"aesthetic|artistic", 2),
   (r"\\mathcal N", 2), (r"better than|worse than|\bgrades?\b|\branks?\b|ranking|orders? candidates", 1.5), (r"\bgood\b", 1),
   (r"\bsuccess", 1), (r"\bprogress\b", 1)]),
 ("physical", "Physical possibility and the physical module",
  "sentences about the physical module, what is physically possible or admitted, tasks, retention, boundary and continuity, capability, tolerances",
  [(r"physical", 2), (r"\\Theta|Θ", 2), (r"possib", 1.5), (r"perpetual motion", 2), (r"\btasks?\b", 1.5), (r"retain|retention", 2),
   (r"realization|realis", 1.5), (r"fixed point", 2), (r"boundary", 1.5), (r"continuity", 1.5), (r"capabilit", 1.5), (r"toleranc", 2),
   (r"\(CT1\)|\(CT2\)|\(CA\)", 2), (r"constructor", 2), (r"interoperab", 1.5)]),
 ("recursion", "Recursion, scrutiny and universality",
  "sentences about scrutinizability, recursive capacity, barriers and universality",
  [(r"recurs", 2.5), (r"scrutin", 2.5), (r"universal", 2.5), (r"barriers?", 2), (r"operative return", 2), (r"\(RC\)|\(U[123]\)", 2)]),
 ("inputs", "Imports, declared inputs and the dependence order",
  "sentences about the two imports, declared inputs and indices, what is defined from what, the dependence order and membership of the class",
  [(r"\bimports?\b|\bimported\b", 2.5), (r"declared inputs?|stated inputs?|\binputs?\b", 2), (r"declared indices|\bindices\b|\bindex\b", 2),
   (r"dependence order|\bdepends? on\b", 2), (r"membership", 2), (r"primitive", 2), (r"undefined|defined in terms", 1.5), (r"\bdeclared\b", 1)]),
 ("ruleout", "What would rule the class out",
  "sentences stating the cases that would rule the class out (sufficiency, necessity, reinstatement of kinds, genesis, question-finding) and where to attack it",
  [(r"rul(e|es|ed) (this|the) class out|rule out the class", 3), (r"\(Suff\)|sufficiency", 2.5), (r"\(Nec\)|necessity", 2.5),
   (r"\(Elim\)|reinstatement", 2.5), (r"\battack", 2), (r"\bclass\b", 1), (r"mathematical error", 2)]),
 ("constructions", "Exact constructions and mathematics",
  "sentences about the exact constructions: production and direction, identification, obstruction, removing structure, skew-symmetric matrices, constitutive rules, and mathematics",
  [(r"matri", 2), (r"skew", 2.5), (r"obstruction", 2.5), (r"identif", 1.5), (r"\bproduction\b|ProducedBy", 1.5), (r"\bdirection\b", 1.5),
   (r"constitutive", 2), (r"mathemat", 1.5), (r"rule application|\brules?\b(?! out)", 1), (r"remov\w* structure", 2),
   (r"determinant|parity|odd-order", 2)]),
]
KEYS = [k for k, *_ in IDEAS]

S = 3.0   # strong home
W = 1.0   # weak home
HOME_LABEL = {  # (part prefix, heading prefix, label prefix) -> [(idea, weight)]
 ("Front", "", ""): [("frame", S)],
 ("Part 0", "", ""): [("frame", W)],
 ("Part 0", "", "Two words"): [("argument", W), ("ruling", W)],
 ("Part 0", "What this document claims", ""): [("frame", W)],
 ("Part 0", "What this document does not claim", ""): [("frame", W)],
 ("Part 0", "What is imported", ""): [("inputs", S)],
 ("Part 0", "Grievances", ""): [("frame", W)],
 ("Part 0", "Grievances", "1."): [("organization", S)],
 ("Part 0", "Grievances", "2."): [("organization", S)],
 ("Part 0", "Grievances", "3."): [("provenance", S)],
 ("Part 0", "Grievances", "4."): [("question", S)],
 ("Part 0", "Grievances", "5."): [("provenance", S)],
 ("Part 0", "Grievances", "6."): [("provenance", S)],
 ("Part 0", "Grievances", "7."): [("constructions", S)],
 ("Part 0", "Grievances", "8."): [("appraisal", S)],
 ("Part 0", "Grievances", "9."): [("provenance", S)],
 ("Part 0", "Grievances", "10."): [("question", S)],
 ("Part 0", "Grievances", "11."): [("organization", S)],
 ("Part 0", "Where to attack", ""): [("ruleout", S)],
 ("Part I ", "", ""): [("frame", W)],
 ("Part I ", "", "Faithfulness"): [("account", S)],
 ("Part I ", "", "Fallibility"): [("criticism", S)],
 ("Part I ", "", "Conjecture"): [("criticism", S)],
 ("Part I ", "", "Recursive"): [("recursion", S)],
 ("Part I ", "", "Substrate"): [("organization", W), ("physical", W)],
 ("Part I ", "", "Two provenances"): [("provenance", S)],
 ("Part II ", "", ""): [("organization", S)],
 ("Part III ", "", ""): [("question", S)],
 ("Part IV ", "", ""): [("layers", S)],
 ("Part IV ", "Three provenances", ""): [("provenance", S)],
 ("Part IV ", "Prediction", ""): [("surprise", S)],
 ("Part V ", "", ""): [("account", S)],
 ("Part VI ", "", ""): [("work", S)],
 ("Part VI ", "", "Rivals"): [("rivals", S)],
 ("Part VI ", "", "Problems"): [("rivals", S)],
 ("Part VII ", "", ""): [("constructions", S)],
 ("Part VIII ", "", ""): [("layers", S)],
 ("Part VIII ", "", "A failed answer"): [("ruling", S)],
 ("Part IX ", "", ""): [("criticism", W)],
 ("Part IX ", "", "Histories"): [("argument", S)],
 ("Part IX ", "", "Bearing"): [("argument", S)],
 ("Part IX ", "", "Reason use"): [("argument", S)],
 ("Part IX ", "", "Usability"): [("argument", S)],
 ("Part IX ", "", "What a test"): [("argument", S)],
 ("Part IX ", "", "Arguments"): [("argument", S)],
 ("Part X ", "", ""): [("creativity", S)],
 ("Part XI ", "", ""): [("criticism", W)],
 ("Part XI ", "", "Repair"): [("criticism", S)],
 ("Part XI ", "", "Created"): [("creativity", S)],
 ("Part XI ", "", "Appraisal"): [("appraisal", S)],
 ("Part XII ", "", ""): [("physical", S)],
 ("Part XIII ", "", ""): [("recursion", S)],
 ("Part XIV ", "", ""): [("inputs", S)],
 ("Part XV ", "", ""): [("ruleout", S)],
 ("Part XVI ", "", ""): [("argument", W)],
 ("Part XVI ", "1.", ""): [("organization", S)],
 ("Part XVI ", "2.", ""): [("account", S)],
 ("Part XVI ", "3.", ""): [("provenance", S)],
 ("Part XVI ", "4.", ""): [("surprise", S)],
 ("Part XVI ", "5.", ""): [("creativity", S)],
 ("Part XVI ", "6.", ""): [("inputs", S)],
 ("Part XVI ", "7.", ""): [("question", S)],
 ("Part XVI ", "8.", ""): [("layers", S)],
 ("Part XVI ", "9.", ""): [("account", S)],
 ("Part XVI ", "10.", ""): [("creativity", W)],
}
PART_DEFAULT = {"Front": "frame", "Part 0": "frame", "Part I ": "frame", "Part II ": "organization", "Part III ": "question",
 "Part IV ": "layers", "Part V ": "account", "Part VI ": "work", "Part VII ": "constructions", "Part VIII ": "layers",
 "Part IX ": "argument", "Part X ": "creativity", "Part XI ": "criticism", "Part XII ": "physical", "Part XIII ": "recursion",
 "Part XIV ": "inputs", "Part XV ": "ruleout", "Part XVI ": "argument"}

COMPILED = {k: [(re.compile(rx) if "\\\\" in rx else re.compile(rx, I), w)
                for rx, w in cues] for k, name, rule, cues in IDEAS}

def part_key(part):
    p = (part or "") + " "
    for k in sorted(PART_DEFAULT, key=len, reverse=True):
        if p.startswith(k) or (k == "Part 0" and p.startswith("Part 0")):
            return k
    return None

def home(part, heading, label):
    pk = part_key(part)
    if pk is None:
        return []
    best, blen = None, -1
    for (p, h, l), v in HOME_LABEL.items():
        if p != pk:
            continue
        if heading.startswith(h) and label.startswith(l):
            ln = len(h) + len(l)
            if ln > blen:
                best, blen = v, ln
    return best or []
