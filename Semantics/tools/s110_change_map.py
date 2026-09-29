#!/usr/bin/env python3
"""s110_change_map.py: the change map of log S110 (decision S58: "I suspect coming up with a change map here might help
as well"), as data. Written 29 September 2026 by the one Opus 5.5 agent of log S110 (decision S56).

Nodes are the commitments, definitions and devices of the owner's six earlier frameworks (FW0, I2, FW2, FW3, FW4, FW5,
kept in tests/S110 Material - earlier frameworks, supplied by the owner/) and of the present theory (tests/107 ..., PT),
each with its place (section heading and a short locator) and a theme. Edges run between versions along the lineage the
documents give; each has a kind (kept, changed, dropped, added, replaced), one line saying how, and a standing:
  stated   - the frameworks' own text or change register says so (which one is named in "by");
  recorded - this project's own records say so (results/S89 ..., results/S95 ..., the decisions record);
  inferred - Claude's reading, marked as such; the step that would show it wrong is in "how".
A dropped edge has no target node ("to": []), or names the node of the later version that records the drop; e48 has no
target because FW3 keeps FW2 whole without repeating it. An added edge has no source node, or names the node of the
earlier version it was added to.

  python3 Semantics/tools/s110_change_map.py          write results/S110 The change map ... .json and print the totals
  python3 Semantics/tools/s110_change_map.py --check  rebuild in memory and compare with the file; write nothing

The Markdown file beside the JSON is written by hand from these data and the printed totals.
"""
import collections, json, os, sys

sys.dont_write_bytecode = True
SEM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = 'results/S110 The change map - the earlier frameworks and the present theory.json'
MAT = 'tests/S110 Material - earlier frameworks, supplied by the owner/'

VERSIONS = {
    'FW0': MAT + 'FW0 REV from M0 - Creative revision events.md',
    'I2': MAT + 'I2 SPEC of FW1a - Executable inquiry.md',
    'FW2': MAT + 'FW2 JUMP from FW1a - Standing and capacity hierarchy.md',
    'FW3': MAT + 'FW3 AMEND of FW2 via D1-D3 - Why-dependence.md',
    'FW4': MAT + 'FW4 RELATED to FW3 - Structural discharge.md',
    'FW5': MAT + 'FW5 JUMP from FW2+FW3+FW4 - Explanatory construction.md',
    'PT': 'tests/107 The semantics, standing alone, after round 4.md',
}
THEMES = OrderedThemes = [
    ('INF', 'information, carriers and media'), ('KNO', 'knowledge'), ('ERR', 'error correction, criticism and repair'),
    ('CRE', 'creativity: origination, newness, construction'), ('EXP', 'explanation'),
    ('PHY', "constructor theory's physical machinery: tasks, possibility, retained capability"),
    ('STA', 'standing, appraisal, records and warrant'), ('HTV', 'hard to vary and reach (mapped only; S34 parks it)'),
    ('REC', 'recursion and universality'), ('MET', 'method commitments')]

STEPS = OrderedStep = [
    ('FW0>FW2', 'FW0 to FW2, across the missing M1, Q1, FW1 and FW1a', 'FW0 leads to M1 and Q1 ("Where this belongs"); FW2 is the successor of FW1a; nothing supplied joins them'),
    ('FW0>I2', 'FW0 to I2, across the missing M1, Q1, FW1 and FW1a', 'I2 specifies FW1a (its authority register); nothing supplied joins it to FW0'),
    ('FW2>FW3', 'FW2 to FW3, through the missing D1, D2 and D3', "FW3's change register, row by row, against FW2"),
    ('FW3>FW4', 'FW3 (and the missing Q2) to FW4: related, production history not authenticated', 'FW4 "Where this belongs": "RELATED is deliberate"'),
    ('>FW5', 'FW2, FW3, FW4 (and the missing D1 to D3, M4) to FW5', "FW5's section \"Reconciliation with the supplied evolution\" and its source register"),
    ('I2>FW5', 'I2 to FW5: FW5 read executable specification 0.1 and an audit of 0.2, not I2 (0.4)', 'FW5 sources S7 and S9 (inside the missing M4)'),
    ('FW5>PT', 'FW5 to the present theory, across the missing Q3, Q4, D4, T3 and through files 10, 11, 12, the revision 2 drafts, 99 and 103 to 107 of this repository', 'authority/NOT-IN-BUNDLE.md: FW5 is "an older, richer predecessor of file 10"; results/S89 and results/S95'),
]

# id, theme, name, where (section heading, locator), what
N = [
 # ---- FW0 (Revision E of CR-2.0) ----
 ('FW0.1', 'MET', 'model and record kept apart', 'Part I "What the document is for"', 'what holds in a model and what a finite record of evidence currently supports are two things never to be confused'),
 ('FW0.2', 'ERR', 'the kernel applied to its own evidence', 'Part I "What this revision does"; §7.1', 'certificates are content; rejecting one is an attack, itself content and criticisable'),
 ('FW0.3', 'STA', 'four-valued raw ledger (Belnap)', '§7.2 "Raw ledger (Belnap)"; §21', 'OPEN, SUPPORTED, REFUTED, CONTESTED with an information ("knowledge") order; the ledger is monotone in it'),
 ('FW0.4', 'ERR', 'grounded adjudication, attacks propagated along essential dependencies', '§7.3', "Dung's grounded semantics on an acyclic attack graph; the adjudicated view keeps certificates that survive attack"),
 ('FW0.5', 'ERR', 'fallibility contract', '§5; Part I "What is still non-negotiable"', 'a fresh criticism of any eligible template can be recorded against any configuration; "Nothing closes"'),
 ('FW0.6', 'STA', 'no stored status; version-stamped judgments', '§5 last block; §7.7', 'every status is recomputed from a configuration; every judgment carries kernel, profile and cut digest'),
 ('FW0.7', 'INF', 'cross-sort bridges; physical information is not explanatory knowledge', '§1 "Sorts", closing paragraph', 'tokens are not contents; prediction is not explanation; retention is not truth; "physical information is not explanatory knowledge"'),
 ('FW0.8', 'KNO', 'EKC, explanatory knowledge creation', '§16.5', 'a critical creative process result, the success judgment K_E and accessibility; "Retention is availability, not endorsement. K_E, not retention, supplies success."'),
 ('FW0.9', 'KNO', 'K_CT, physical knowledge, a different sort (deferred)', '§16.6; §20; §27 row "K_CT declaration" (source CT-7)', 'declared separate; its non-equivalence with K_E is a theorem obligation, not discharged'),
 ('FW0.10', 'CRE', 'newness relative to a repertoire', '§9', 'new relative to what the system could deploy before; creative reconstruction can be new for the system and not historically'),
 ('FW0.11', 'CRE', 'authorship and the originative creative act, bound to its witness', '§12; §13', 'the public predicate equated with its witness (change register row 8)'),
 ('FW0.12', 'ERR', 'criticism, response, reason use; the critical creative process', '§11; §14', 'the responder must represent the criticism (change register row 10)'),
 ('FW0.13', 'ERR', 'target-correct correction certificate', '§16.3', 'a correction needs a criticism, a revise response, a witness that the defect is addressed and each merit preserved'),
 ('FW0.14', 'ERR', 'outcome-indexed improvement witnesses', '§16.4', 'revision, rejection, rival adoption, reasoned retention, reframe, restandardize; each with a response-indexed envelope'),
 ('FW0.15', 'HTV', 'hard to vary over a declared variant family; reach body', '§18', '"A hard-to-vary candidate is one on which criticism can bind"; reach needs transported structure and discharged obligations'),
 ('FW0.16', 'CRE', 'contrast classes, including NaturalSelection', '§19', 'generator, predictor, deductor, search, learner, computer, natural selection: each may be a component of a creator'),
 ('FW0.17', 'PHY', 'physical realization, deferred', '§20', 'a realization structure with commuting obligations, among them "resources, tolerance, noise, repair"'),
 ('FW0.18', 'REC', 'capacity under perturbations', '§17', 'capacity needs a new critical continuation under every applicable perturbation, the identity included'),
 ('FW0.19', 'EXP', 'decisive relations kept as primitives, each given a witness', 'Part I "What the document is for"; §10', '"explains, authors, uses the reason, improves the situation" stay primitives; explanation objects record them'),
 ('FW0.20', 'MET', 'final criterion: every disputed attribution answerable by a finite, attackable object', '"Final criterion"', 'an event path, an explanation object, a body or a countermodel, each itself attackable'),
 # ---- I2 (executable specification 0.4 of FW1a) ----
 ('I2.1', 'MET', 'inquiry material, not certified truth', 'Part I "The product is creative inquiry material, not certified truth"', 'the engine exports attempts, not a creativity label; its authority lines A1, A7'),
 ('I2.2', 'MET', 'prose is a complete interface', 'Part I "Prose is a complete interface to participation"', 'no participant must code, emit JSON or supply a confidence'),
 ('I2.3', 'ERR', 'error correction is reason-sensitive revision with an operative return', 'Part I, section of that name', '"The error-correction method is conjecture and criticism applied recursively to whatever is doing explanatory work"; mere change is not correction'),
 ('I2.4', 'ERR', 'the collection is not the working set; parking', 'Part II "The collection is not the active working set"', 'error correction stops the operative reuse of an error without erasing it; withdrawal is use-relative'),
 ('I2.5', 'ERR', 'a prose judgment can change use without a formal test', 'Part II, section of that name', 'a mediator enacts one named use change; its reading of the prose stays open to correction'),
 ('I2.6', 'ERR', 'mechanical checks answer only their declared question', 'Part II "Mechanical checking is available without a formatting gate"', 'a quotation check says a string is present, not that the source is accurate or relevant'),
 ('I2.7', 'ERR', 'checks are not the privileged entrance to criticism', 'Part II, section of that name', 'a prose-only objection can lead to withdrawal, replacement or a changed method'),
 ('I2.8', 'HTV', 'hard to vary is an explanatory challenge, not a score', 'Part I, section of that name', 'a variation turn asks what a substantive change would alter; no rigidity coefficient, no threshold'),
 ('I2.9', 'MET', 'no rankings or optimisation objectives', 'Part I, section of that name', 'no merit order, truth probability, novelty score, vote or best-of selection'),
 ('I2.10', 'INF', 'attention learning without expected information gain', 'Part V "The chosen meaning of learning"', 'learning is producing and criticising a method for what to inspect; not "estimating expected information gain"'),
 ('I2.11', 'INF', 'tokens as a flow of computational allowance', 'Part VII; "Why computation does not explode by construction of the controller"', 'reading and generating are counted as allowance; the bound is on traffic, not on "information retained"'),
 ('I2.12', 'KNO', 'knowledge creation needs actual explanatory progress; use does not certify learned knowledge', 'Part I first section; Part V first section', '"Successful explanatory knowledge creation has further requirements, including actual explanatory progress"'),
 ('I2.13', 'CRE', 'daydreaming and jolts', 'Part VIII', 'exploration without immediate usefulness; jolts alter conditions, not scores'),
 ('I2.14', 'PHY', 'finite resources are realisation conditions', 'authority register A10; Parts VI and VII', 'resources bound a realisation; they do not redefine universality'),
 # ---- FW2 ----
 ('FW2.1', 'MET', 'K-REAL: reality is not conferred by a judgment', 'Part I-A "Reality is not conferred by a judgment"', 'errors can be real when nobody has identified them; no procedure turns a fallible judgment into a guarantee'),
 ('FW2.2', 'ERR', 'K-PROBLEM: a problem is an interpreted difficulty that matters', 'Part I-A', 'a tension, inadequacy or unresolved relation among ideas that a system recognises and attends to'),
 ('FW2.3', 'CRE', 'K-CONJECTURE: conjecture precedes criticism of it', 'Part I-A', 'no justification before entertaining; an inexplicit expectation can be the prior conjecture'),
 ('FW2.4', 'ERR', 'K-CRITICISM: criticism has a reason-bearing role', 'Part I-A', 'negative feedback, failure or rejection is not criticism merely because it changes behaviour'),
 ('FW2.5', 'REC', 'K-RECURSION: target closure, role preservation, return relevance', 'Part I-A; Part II "The recursive kernel as a relation, not a scheduler"', 'anything doing explanatory or adjudicative work can become a target, with effect on its use'),
 ('FW2.6', 'STA', 'K-STANDING: generation confers no standing', 'Part I-A (FW2, new)', 'standing is conferred by an appraisal; denial of standing is not deletion'),
 ('FW2.7', 'CRE', 'K-ORIGIN: creation has a provenance; understanding can be reconstructive', 'Part I-A', 'newness, authorship, understanding, correctness and priority are distinct'),
 ('FW2.8', 'KNO', 'K-PROGRESS: knowledge growth is explanatory improvement, not persistence', 'Part I-A', '"Successful explanatory knowledge creation requires an actual improvement ... retention alone does not"'),
 ('FW2.9', 'REC', 'K-UNIVERSALITY: a capacity claim', 'Part I-A', 'not a collection of successful episodes'),
 ('FW2.10', 'PHY', 'K-PHYSICALITY: embodiment constrains without replacing explanation', 'Part I-A', 'constructor theory supplies possible and impossible transformations, information-bearing substrates, retained capacities; physical and explanatory knowledge "related but nonidentical" [M5; M7]'),
 ('FW2.11', 'EXP', 'Account: attempting and actually explaining', 'Part II "Attempting an explanation and actually explaining"', 'Account a substantive relation; prediction is not explanation; statistical "explaining away" is "a relation among representations"'),
 ('FW2.12', 'ERR', 'Bearing and UsesReason', 'Part II "Reason-bearing criticism and counterfactual uptake"', 'a criticism <z,p,b,delta,g,lambda>; uptake needs an account over a contrast family'),
 ('FW2.13', 'ERR', 'Essential and Usable_j', 'Part II "Argument dependencies and the effect of criticizing a premise"', 'withdrawing an essential premise makes an application unusable, not its conclusion false'),
 ('FW2.14', 'STA', 'appraisal is conjectural content; four record descriptions', 'Part II "Appraisal is also conjectural content"', '"no case", "positive", "negative", "both": "optional descriptions of the record, not four kinds of truth"'),
 ('FW2.15', 'CRE', 'newness relative to an attributed system and a grain', 'Part II, section of that name', 'New(s,x,e,h) against the repertoire R before e; initial repertoire domain D0'),
 ('FW2.16', 'CRE', 'authorship and the originative act OCA', 'Part II "Authorship and distributed contribution"; "Originative acts and critical processes"', 'OCA = Attempt, New and Authors; a false one-time conjecture can be one'),
 ('FW2.17', 'CRE', 'productivity is not creativity', 'Part II "Originative acts and critical processes" (from A3.2)', 'a lawful generator that discards what it generates cannot criticise it or originate'),
 ('FW2.18', 'HTV', 'quality: current good explanation, FreeVariation, reach', 'Part II "Explanatory quality, constraint, and reach"', 'merit preference among actual alternatives; FreeVariation over a family; many constraints give preference, not probability'),
 ('FW2.19', 'KNO', 'explanatory knowledge creation', 'Part II "Progress, possession, and historical assessment"', 'a creative critical contribution, actual progress attributable to it, the result available for use; "loss does not make creation not to have occurred"'),
 ('FW2.20', 'ERR', 'first-layer class: retention with fidelity correction, no kernel', 'Part II "The stratified hierarchy"', 'settling, redundancy, suppression, attestation, a lawful generator: every mechanism shown "not criticism" lives here'),
 ('FW2.21', 'KNO', 'physical knowledge in the realization section', 'Part II "Physical realization and constructor-theoretic scope"', '"Physical knowledge is information with a causal capacity for preserving its instantiation"; an adaptation can have it without representing an explanation; merit is not duration'),
 ('FW2.22', 'ERR', 'two layers of error correction', 'Part II realization constraint 2; Part IV "Named criticism routes and conjectures"', 'a layer correcting errors of representation (redundancy, settling) and a layer correcting errors of content (criticism); the second not got by iterating the first [H1; CT1]'),
 ('FW2.23', 'INF', 'the medium constraint; a correlational account of information not adopted', 'Part II realization constraint 1 [P1]; "Source keys", P1', 'the medium must support distinct contents, composition, binding, embedding; "the correlational account of information [is] not adopted"'),
 ('FW2.24', 'INF', 'constructor theory of information as a source (CT1)', '"Source keys and attribution boundaries", CT1', 'Deutsch and Marletto 2015: information media, copying, distinguishability, "error correction as a condition of retained capacity"'),
 ('FW2.25', 'ERR', 'a prediction error is not a criticism', 'Part III, section of that name (from A1.2)', 'a mismatch that repairs a model has no represented defect, grounds or bearing'),
 ('FW2.26', 'KNO', 'biological contrast', 'Part III "Distributed inquiry and biological contrast"', 'a lineage "instantiates physical knowledge without explanatory criticism"'),
 ('FW2.27', 'KNO', 'evolved constraints as provisional background', 'Part II "Argument dependencies ..." last paragraph; Part III', '"physical knowledge in the organism, deployed as premises, withdrawable, and not warrant"'),
 ('FW2.28', 'CRE', 'generator constraints and the extensible class', 'Part II "Methods can be criticized from within inquiry"; "The stratified hierarchy"', 'a standard whose withdrawal changes what the system can conjecture; E1 makes them eligible targets'),
 ('FW2.29', 'EXP', 'a predictive-model account of intelligence as contrast', 'Part III "General model learning is not explanatory organization" (from A1.1); source H1', 'continuous predictive learning with many models and consensus can instantiate no explanatory activity'),
 ('FW2.30', 'MET', 'three standpoints', 'Part II "The model and the three standpoints"', 'model satisfaction, situated judgment, attribution evidence; none identified with another'),
 ('FW2.31', 'ERR', 'Progress: kinds of improvement with no common scale', 'Part II "Progress, possession, and historical assessment"', 'replacing a false mechanism, explaining why an approximation worked, exposing an artifact, a better question, a limit'),
 ('FW2.32', 'INF', 'contents, occurrences and interpretations', 'Part II "Contents, occurrences, and interpretations"', 'an occurrence is a token, artifact or embodied state; its identity is distinct from its interpreted content; an interpretation is indexed by grain, context and attributed system'),
 # ---- FW3 ----
 ('FW3.1', 'EXP', 'K-BECAUSE: why-dependence, the one primitive, bounded by seven prohibitions', 'I.1', 'prohibition 4: not "retention, self-preservation, or physical transformation"'),
 ('FW3.2', 'EXP', 'work by minimal working subsets', 'I.2', 'a commitment does work iff it belongs to some minimal working subset'),
 ('FW3.3', 'HTV', 'constraint and reach as two projections of work', 'I.2; Part II T12', '"An explanation that reaches more is, by the same fact, harder to vary"'),
 ('FW3.4', 'EXP', 'Account A1 to A4, factive over work', 'I.3', 'a minimal working subset, non-circularity, indices, not input-output association'),
 ('FW3.5', 'ERR', 'Bearing as Account on a defect (conjecture)', 'I.4', 'a criticism is a conjecture about a defect; its bearing is the why-dependence of the defect on its grounds'),
 ('FW3.6', 'ERR', 'Progress as a gain in Account or Bearing (conjecture)', 'I.4', 'no common scale; the form of an improvement, not a measure'),
 ('FW3.7', 'KNO', 'Merit', 'I.5', 'Account and withstanding criticism well enough to merit preference; comparative, situation-indexed'),
 ('FW3.8', 'KNO', 'created knowledge', 'I.5', 'Progress by a creative critical contribution, attributed, and the result deployable; loss does not undo creation'),
 ('FW3.9', 'KNO', 'three relations, one word', 'I.5; Part V rule S9', '"knowledge" names adequacy, merit or created knowledge, and each use must say which'),
 ('FW3.10', 'KNO', 'T1: no explanatory relation has a knower argument', 'Part II T1', 'the knower enters only through attribution'),
 ('FW3.11', 'KNO', 'T2: no existential closure; physical knowledge a one-place predicate on information', 'Part II T2', '"physical knowledge (Marletto) is a one-place predicate on information; the two differ in logical type"'),
 ('FW3.12', 'CRE', 'T3: acquisition is creation', 'Part II T3', 'understanding is reconstruction, reconstruction is authorship; transmission moves custody, never knowledge'),
 ('FW3.13', 'KNO', 'T4: knowledge and standing are orthogonal', 'Part II T4; Part IV case 8', 'a system can withdraw standing from its knowledge and give it to a worse content'),
 ('FW3.14', 'KNO', 'T5: explanatory and physical knowledge are extensionally independent', 'Part II T5; Part IV case 10', '"A false belief spread by uptake is self-preserving information without explanatory knowledge; a lost explanation was explanatory knowledge without surviving physical knowledge"'),
 ('FW3.15', 'STA', 'T16: the licensed count', 'Part II T16', 'a count of conjecturally independent features reached licenses preference and nothing else'),
 ('FW3.16', 'STA', 'T17: warrant is eliminated', 'Part II T17', 'what survive are adequacy, merit, standing and preference'),
 ('FW3.17', 'INF', 'T18: occurrence-level questions are ill-formed', 'Part II T18', '"Is this string knowledge?" has no answer until an interpretation is fixed, and fixing it is a conjecture'),
 ('FW3.18', 'KNO', 'T19: roles do not sort knowledge', 'Part II T19', 'a problem, criticism, standard or limit is knowledge relative to the situation it improved'),
 ('FW3.19', 'STA', 'custody and deployability', 'I.6; III.1 table', 'storage of a string is custody, not deployability'),
 ('FW3.20', 'REC', 'T14, T15: target closure over roles; Deployed is a record fact', 'Part II T14, T15', 'what an instance depends on but does not deploy escapes closure'),
 ('FW3.21', 'MET', 'specification discipline; the field "knowledge" forbidden', 'Part V', 'record facts a specification may hold; fields it may not hold: knowledge, accounts_for, does_work, warrant'),
 ('FW3.22', 'EXP', 'R3: statistical explaining-away renamed', 'III.2 R3', '"a relation among representations" becomes "a relation of probabilistic dependency among hypotheses"'),
 ('FW3.23', 'PHY', 'realization addition: the deployed set is a record fact, the working set is not', 'III.4', 'added to FW2\'s realization constraint 3'),
 # ---- FW4 ----
 ('FW4.1', 'MET', 'commitments, with Indexing', 'Part I', 'realism, fallibility, conjecture before criticism, no standing from generation, recursion, indexing'),
 ('FW4.2', 'EXP', 'Because, seven prohibitions, modes changed', 'Part II', 'modes: production, determination, invariant, constitutive, selection; direction fixed by an organization'),
 ('FW4.3', 'EXP', 'support families; work as critical membership', 'III.1', 'finite lemma: work is the union of minimal supports, indispensability their intersection; joint work without contributors'),
 ('FW4.4', 'EXP', 'organizations and recoding', 'III.2', 'supports are defined over the organization, preserved by recoding, not by substitution'),
 ('FW4.5', 'HTV', 'reach and the monotonicity lemma; HTV as indispensability of every commitment', 'III.1; III.3', 'adding a preservation requirement cannot enlarge the permitted variation set; no comparison across contents follows'),
 ('FW4.6', 'EXP', 'transport: recoding, idealization, approximation', 'III.5', 'approximation with a bounded discrepancy on a scope; work is the unit of transport'),
 ('FW4.7', 'EXP', 'type and token', 'III.6', 'which route was active in an occurrence is not recoverable from endpoint variation'),
 ('FW4.8', 'EXP', 'Account A1 to A3; circularity moved to discharge', 'Part IV', 'a circular attempt can be in Account by luck; it cannot be discharged and lacks merit'),
 ('FW4.9', 'ERR', 'Bearing, contribution and progress as instances of Account', 'Part V', 'conjectures; if they hold, one explanatory primitive'),
 ('FW4.10', 'KNO', 'Merit and created knowledge', 'Part VI', 'as in FW3; availability is deployability'),
 ('FW4.11', 'KNO', 'physical knowledge', 'Part VI "Physical knowledge"; Part VIII R2, R5; Part XI case 9', '"a false belief spread by imitation preserves its instantiation and accounts for nothing; an explanation that accounted for its feature and was lost preserved nothing"'),
 ('FW4.12', 'CRE', 'R3: acquisition is creation', 'Part VIII R3', 'as FW3 T3'),
 ('FW4.13', 'EXP', 'the discharge quadruple and its anti-smuggling conditions', 'Part IX', 'a domain model, a structural claim S, an application claim A, a relevance claim R; N1 to N4'),
 ('FW4.14', 'EXP', 'mode modules M1 to M6', 'Part X', 'production, determination, invariant, constitutive, selection; aesthetic open'),
 ('FW4.15', 'STA', 'standing, custody, deployability, operative role, generator constraints', 'Part VII', 'as FW3 I.6, with generator constraints stated'),
 ('FW4.16', 'STA', 'R16 licensed count; R17 warrant eliminated', 'Part VIII', 'as FW3 T16, T17'),
 ('FW4.17', 'MET', 'specification discipline', 'Part XII', 'the field "knowledge" forbidden; a machine may verify S and may not assert A or R'),
 ('FW4.18', 'KNO', 'R1: no explanatory relation has a knower argument', 'Part VIII R1', 'as FW3 T1'),
 ('FW4.19', 'INF', 'R18: occurrence-level questions are ill-formed until an interpretation is fixed', 'Part VIII R18', 'as FW3 T18'),
 ('FW4.20', 'KNO', 'R19: roles do not sort knowledge', 'Part VIII R19', 'as FW3 T19'),
 # ---- FW5 ----
 ('FW5.1', 'EXP', 'no residual Because primitive', '"What \'no gaps\' can responsibly mean"', 'no primitive named Because, ExplanatoryWork, GoodExplanation or Creative'),
 ('FW5.2', 'MET', 'explanatory realism and fallibility', '"The commitments", first section', '"What cannot count as successful explanation is an error in the very dependence alleged to account for that feature"'),
 ('FW5.3', 'PHY', 'substrate independence with physical obligations', '"The commitments", last section', 'any carrier may bear organization; claimed distinctions and retained capacities must be physically permitted'),
 ('FW5.4', 'EXP', 'structural answer (E)', '"Explanatory adequacy without a Because primitive"', 'anchoring, fidelity, question fidelity, non-circular dependence, non-vacuity'),
 ('FW5.5', 'HTV', 'support families without minimality; hard to vary and reach as containment', '"Work, redundancy, interference, and infinity"; "Hard-to-vary and reach"', 'no upward closure assumed; more reach constrains variation for a fixed organization and family, not a count'),
 ('FW5.6', 'ERR', 'approximate transport: accumulated error bound (T2)', '"Transport and preservation", "Approximate transport"', 'e_n <= eps * sum L^k; without a Lipschitz bound or modulus no accumulated bound follows'),
 ('FW5.7', 'ERR', 'criticism and its bearing; reason use as causal organization', '"Criticism, evidence, and operative decisions"', 'reason use is not an output comparison'),
 ('FW5.8', 'ERR', 'elimination without a truth machine; what a test contradicts (K3)', 'same Part, "Elimination without a truth machine"', 'a failed prediction contradicts T and B and I together, not T alone'),
 ('FW5.9', 'STA', 'evidence receipts', '"Evidence receipts without false certainty"', 'P_j and N_j, positive and negative receipt sets: "descriptions of available arguments, not four kinds of reality"'),
 ('FW5.10', 'CRE', 'construction and transfer; newness; the originative act', '"Understanding, provenance, and creative events"', 'realized use, not logical omniscience; construction, transfer, reacquisition distinguished'),
 ('FW5.11', 'ERR', 'obligations and Repair (P)', '"Obligations rather than a hidden score"', 'a declared obligation met, protected ones kept, the change produced by the contribution'),
 ('FW5.12', 'KNO', 'created explanatory knowledge (EK)', '"Created explanatory knowledge"', 'a creative critical episode, a Repair of an epistemic obligation, an originative adequate deployable content on the active route; "Creation is historical"'),
 ('FW5.13', 'STA', 'choice and criticism without Merit', '"Choice and criticism without \'Merit\'"', 'no generic predicate of meriting preference; no count licensed to choose explanations'),
 ('FW5.14', 'CRE', 'inexplicit representation is not absent representation', '"Inexplicit, artistic, and normative inquiry"', 'the pianist, the geometer, the investigator'),
 ('FW5.15', 'INF', 'physical tasks and information', '"Constructor theory as a constitutive part of the semantics", "Physical tasks and information"', 'substrate, attribute, task; "An information variable is ... a clonable computation variable"; interoperability [R2, R3]'),
 ('FW5.16', 'PHY', 'retained realization (CT1) and the retention fixed point (CT2)', 'same Part', 'a protocol that completes its task and returns the constructor to its attribute'),
 ('FW5.17', 'PHY', 'owned capability; a first discovery is not a repeatable first discovery (CA)', 'same Part', 'retention applies to the inquiry-enabling organization'),
 ('FW5.18', 'ERR', 'representational fidelity and content correction are different defects', 'same Part, "Physical realization of semantic organization"', '"A damaged inscription and a false theory are not the same error"; not necessarily two mechanisms'),
 ('FW5.19', 'KNO', "CTK: constructor-theoretic knowledge with its realization ecology; a conditional bridge", 'same Part, "Knowledge that preserves its instantiation"; "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity"', 'no unconditional converse; extensional independence not inferable "merely from the pair of examples"'),
 ('FW5.20', 'PHY', 'capability grades against possibility (CT3, CT4)', 'same Part, "The bridge that matters for creativity"', '"Knowledge acquisition can change these owned repertoires while Poss remains fixed"'),
 ('FW5.21', 'REC', 'recursive openness and universality', '"Recursive openness and explanatory universality"', 'RC, target closure and return; UU, UC'),
 ('FW5.22', 'CRE', 'acquisition is not always creation', '"Reconciliation", "Acquisition, historical origin, and retention cannot be collapsed"', '"The claim that every acquisition is creation is stronger than the definitions and examples support"'),
 ('FW5.23', 'STA', 'actual use is not a host-maintained role label', '"Reconciliation", section of that name', 'a host records invitations and bindings; what the thinker used needs an interpretation'),
 ('FW5.24', 'MET', 'existential closure is legitimate; the attribution discipline is kept', '"Reconciliation", "Factivity, approximation, and historical indexing"', 'closing an indexed relation yields a weaker statement'),
 ('FW5.25', 'INF', 'beauty not defined by compression or surprise', '"What \'no gaps\' can responsibly mean"', '"approval, symmetry, compression, surprise, or successful persuasion" refused as definitions'),
 ('FW5.26', 'KNO', 'biological lineage: preservation without critical episode', '"The bridge that matters for creativity", last paragraph', 'the difference is between physical-semantic organizations, not physical and non-physical'),
 ('FW5.27', 'EXP', 'exact domain constructions', '"Exact domain constructions"', 'production and direction, identification, the two balances, obstruction, constitutive rules'),
 ('FW5.28', 'INF', 'contents and occurrences', '"Mathematical foundations", "Contents and occurrences"', 'contents and their occurrences kept apart'),
 ('FW5.29', 'EXP', 'equivariance under genuine recoding', '"Results and discriminating constructions", first section', 'a stipulated bijection of representations preserves accounts; compression and coarsening are not such bijections'),
 ('FW5.30', 'ERR', 'critical and creative episodes', '"Understanding, provenance, and creative events", "Critical and creative episodes"', 'a critical episode, and a creative one with an originative act connected to it'),
 # ---- PT: the present theory, tests/107 ----
 ('PT.1', 'EXP', 'an explanation is a question-relevant organization held by a transport tested by change-fidelity', 'Part 0 "What this document claims"', 'kinds are edit-signatures'),
 ('PT.2', 'CRE', 'three provenances: selected, constructed, declared', 'Part IV "Three provenances"', 'selected: a population, variation, a survival condition on encountered changes, no represented target; constructed: an episode of conjecture and criticism'),
 ('PT.3', 'EXP', 'being an explanation: Account(E) and not Dec(t)', 'Part V; Part I "Fallibility without error-as-work"', 'a declared correspondence explains nothing'),
 ('PT.4', 'MET', 'faithfulness without assessors', 'Part I', 'whether a transport is faithful is independent of whether anyone accepts it'),
 ('PT.5', 'MET', 'fallibility without error-as-work', 'Part I', 'an error in the very dependence alleged to do the work cannot count as explanation'),
 ('PT.6', 'INF', 'substrate independence reaching as far as contents can pass between media', 'Part I "Substrate independence with physical conditions"', 'where two media cannot exchange what they bear, a barrier; physical possibility enters where a content is held, copied, taught, tested, built or performed'),
 ('PT.7', 'INF', 'occurrences and contents', 'Part IV "Occurrences and contents"', 'an occurrence is a physically located carrier; a content an organization with its commitments'),
 ('PT.8', 'INF', 'representation: a fidelity relation with a history (R)', 'Part IV "Representation is defined, not supplied"', 'a faithful transport from the carrier\'s organization, selected or constructed; a carrier keeps its provenance when access is lost'),
 ('PT.9', 'ERR', 'prediction, violation, surprise; two responses to a violation', 'Part IV "Prediction, surprise, violation"', 'a selection response re-tunes within the population; a construction response introduces a new organization; only the second can be originative'),
 ('PT.10', 'ERR', 'Bearing (K1) as Account on the question whether the target has the defect', 'Part IX "Bearing"', 'an adverse signal is not a criticism until represented as one'),
 ('PT.11', 'ERR', 'reason use', 'Part IX "Reason use"', 'a structural map from the objection into the response, landing on an active route'),
 ('PT.12', 'ERR', 'usability (K2) and what a test rules out (K3)', 'Part IX', 'premises live for the person; a test rules out T and B and I together'),
 ('PT.13', 'ERR', 'premises taken as given: the costly gamble', 'Part IX "Premises taken as given"', '"if this were not possible, error correction could become impossibly costly to perform" (the owner\'s S27)'),
 ('PT.14', 'CRE', 'Deploy and Build; reconstruction is construction, relay is not', 'Part X', 'a construction trace; use does not by itself construct'),
 ('PT.15', 'CRE', 'inexplicit representation is not absent', 'Part X', 'the pianist, the geometer, the investigator'),
 ('PT.16', 'CRE', 'newness (N) and origin (G)', 'Part X "Newness", "Origin"', 'the finding of a question is an originative act when the content is a contract'),
 ('PT.17', 'ERR', 'episodes; recognized difficulty; closing is a choice', 'Part X "Episodes"', 'a failure of a claimed aim, or a conflict that meets one aim only by failing a protected one, when represented'),
 ('PT.18', 'ERR', 'Repair (P)', 'Part XI "Repair"', 'claimed and protected aims as declared inputs; no order on alternatives'),
 ('PT.19', 'KNO', 'created explanation (EX)', 'Part XI "Created explanation"', 'a creative critical episode, a Repair of an explanatory aim, an originative content meeting Account and deployable, on the active route'),
 ('PT.20', 'PHY', 'tasks and possibility', 'Part XII "Tasks"', 'possibility is the absence of a law-imposed limit, short of exact, on performing and retaining a task'),
 ('PT.21', 'PHY', 'retained realization (CT1) and the retention fixed point (CT2)', 'Part XII', 'as FW5'),
 ('PT.22', 'PHY', 'owned capability, achievement, tolerances (CT3, CT4)', 'Part XII', 'capability at a tolerance does not imply possibility at every tolerance'),
 ('PT.23', 'PHY', 'selection in the physical module', 'Part XII "Selection in the physical module"', 'a population, a physically admitted variation operator and a survival condition enacted by the environment'),
 ('PT.24', 'REC', 'recursion, barriers, universality', 'Part XIII', 'RC, U1 to U3; recursion does not entail universality'),
 ('PT.25', 'ERR', 'Arguments 3 and 4: selected transports underdetermined at unseen changes; surprise needs an incomplete history', 'Part XVI, 3 and 4', 'what the history leaves open is what the population leaves open'),
 ('PT.26', 'ERR', 'approximate transport (T2)', 'Part VIII "Approximate transport"', '"Without a modulus, no accumulated bound follows"'),
 ('PT.27', 'ERR', 'a failed answer stays failed', 'Part VIII, section of that name', 'a candidate whose answer at a pair is the answer an argument has ruled out is ruled out there, however it came back'),
 ('PT.28', 'ERR', 'rivals and problems', 'Part VI "Rivals", "Problems"', 'a problem is "a conflict between ideas that no argument usable by that assessor has decided"'),
 ('PT.29', 'HTV', 'easy to vary; commitments that do no work', 'Part VI', 'easy to vary: the candidate and a rival conflict only outside the contract (D10.4); (E) has no condition that each commitment do work'),
 ('PT.30', 'STA', 'arguments usable by a person; an absence rules out nothing', 'Part IX "Arguments"', 'no ledger of values; "that absence rules out nothing"'),
 ('PT.31', 'MET', 'no appraisal of its own; the appraisal relation an import', 'Part 0 "What this document does not claim"; Part XI "Appraisal"', 'no probability, no ordering of explanations or thinkers'),
 ('PT.32', 'KNO', 'neither "information" nor "knowledge" occurs', 'the whole text (0 and 0 occurrences)', 'the knowledge relation of FW5 appears renamed as created explanation (EX); information appears as carriers, contents and representation'),
 ('PT.33', 'EXP', 'Argument 8: equivariance under structure-preserving recoding', 'Part XVI, 8', 'as FW5'),
]

# id, step, from, to, kind, how, standing, by
E = [
 # FW0 -> FW2 (gap)
 ('e1', 'FW0>FW2', ['FW0.1'], ['FW2.30'], 'changed', 'model against record becomes three standpoints: a situated judgment is added between them', 'inferred', 'the wording of both; no document joins them'),
 ('e2', 'FW0>FW2', ['FW0.3'], ['FW2.14'], 'changed', 'the four-valued ledger with an adjudication operator becomes four optional descriptions of a record, "not four kinds of truth"', 'inferred', 'FW2 Part II "Appraisal is also conjectural content"'),
 ('e3', 'FW0>FW2', ['FW0.4'], [], 'dropped', "grounded (Dung) adjudication has no counterpart; FW2: a schematic attack edge cannot supply bearing", 'inferred', 'FW2 Part II "Argument dependencies ..."'),
 ('e4', 'FW0>FW2', ['FW0.5'], ['FW2.5'], 'changed', 'recordability of any criticism becomes target closure, role preservation and return relevance', 'inferred', ''),
 ('e5', 'FW0>FW2', ['FW0.7'], ['FW2.10'], 'changed', '"physical information is not explanatory knowledge" becomes "related but nonidentical"', 'inferred', ''),
 ('e6', 'FW0>FW2', ['FW0.8'], ['FW2.19'], 'kept', 'knowledge creation is a critical creative result plus success plus availability; retention is availability, not success', 'inferred', ''),
 ('e7', 'FW0>FW2', ['FW0.9'], ['FW2.21'], 'changed', 'the deferred sort K_CT gets a characterization (information with a causal capacity for preserving its instantiation); still no bridge theorem', 'inferred', ''),
 ('e8', 'FW0>FW2', ['FW0.10'], ['FW2.15'], 'kept', 'newness relative to the repertoire before the event', 'inferred', ''),
 ('e9', 'FW0>FW2', ['FW0.11'], ['FW2.16'], 'kept', 'authorship and the originative act', 'inferred', ''),
 ('e10', 'FW0>FW2', ['FW0.12'], ['FW2.12'], 'changed', 'the critical process with its witness becomes Bearing and UsesReason over a contrast family', 'inferred', ''),
 ('e11', 'FW0>FW2', ['FW0.13', 'FW0.14'], ['FW2.31'], 'replaced', 'correction certificates and outcome-indexed witnesses give way to a Progress relation with kinds of improvement and no common scale', 'inferred', ''),
 ('e12', 'FW0>FW2', ['FW0.15'], ['FW2.18'], 'changed', 'hard to vary over a declared family becomes the FreeVariation diagnostic, comparative and respect-relative', 'inferred', ''),
 ('e13', 'FW0>FW2', ['FW0.16'], ['FW2.20', 'FW2.29'], 'changed', 'neutral contrast classes become the first-layer comparison class and named contrast cases', 'inferred', ''),
 ('e14', 'FW0>FW2', ['FW0.17'], ['FW2.22'], 'changed', 'a deferred realization with "noise, repair" obligations becomes six realization constraints, one of them two layers of error correction', 'inferred', ''),
 ('e15', 'FW0>FW2', ['FW0.18'], ['FW2.9'], 'changed', 'capacity under perturbations becomes K-UNIVERSALITY and the modal Can', 'inferred', ''),
 ('e16', 'FW0>FW2', ['FW0.19'], ['FW2.11'], 'changed', 'primitive relations with witnesses become substantive relations (Account, Bearing, Progress, Capacity) with attribution evidence apart', 'inferred', ''),
 ('e17', 'FW0>FW2', ['FW0.20'], [], 'dropped', 'the demand that every attribution be answerable by a finite object; FW2: "A finite record does not logically determine universal capacity"', 'inferred', 'FW2 Part III, section of that name'),
 ('e18', 'FW0>FW2', ['FW0.6'], ['FW2.14'], 'changed', 'no stored status becomes: record states describe the record', 'inferred', ''),
 # FW0 -> I2 (gap)
 ('e19', 'FW0>I2', ['FW0.5'], ['I2.3'], 'changed', 'recordable criticism becomes error correction with an operative return that a host must check', 'inferred', ''),
 ('e20', 'FW0>I2', ['FW0.2'], ['I2.6'], 'changed', 'certificates as attackable content become bounded mechanical checks whose results are open to criticism', 'inferred', ''),
 ('e21', 'FW0>I2', ['FW0.4'], ['I2.9'], 'replaced', 'automatic adjudication gives way to no rankings and no automatic semantic adjudication', 'inferred', 'I2 "P: subordinate supplied profile": "automatic semantic adjudication ... not inherited" (of M8, not of FW0)'),
 ('e22', 'FW0>I2', ['FW0.1'], ['I2.1'], 'changed', 'model against record becomes material against certified truth', 'inferred', ''),
 ('e23', 'FW0>I2', ['FW0.8'], ['I2.12'], 'changed', 'knowledge creation needs actual progress; I2 adds that continued use of a method certifies nothing', 'inferred', ''),
 ('e24', 'FW0>FW2', ['FW0.7'], ['FW2.32'], 'changed', '"tokens are not their contents" becomes contents, occurrences and interpretations indexed by grain', 'inferred', ''),
 # FW2 -> FW3 (stated by FW3's change register)
 ('e30', 'FW2>FW3', ['FW2.11'], ['FW3.4'], 'changed', 'Account restated through minimal working subsets (A1 to A4); background includes every essential standard', 'stated', 'FW3 change register, row "Part II, attempting"'),
 ('e31', 'FW2>FW3', [], ['FW3.1'], 'added', 'why-dependence declared the one explanatory primitive, the "why" K-REAL invokes', 'stated', 'FW3 change register, rows "Part I-A, new" and "Part I-A, K-REAL"'),
 ('e32', 'FW2>FW3', ['FW2.18'], ['FW3.3'], 'changed', 'work set-level; constraint and reach as projections of work; FreeVariation over subsets', 'stated', 'FW3 change register, row "Part II, quality"'),
 ('e33', 'FW2>FW3', ['FW2.12'], ['FW3.5'], 'changed', 'Bearing conjectured to be Account on a defect', 'stated', 'FW3 change register, row "Part II, criticism"'),
 ('e34', 'FW2>FW3', ['FW2.19'], ['FW3.8'], 'changed', 'created knowledge displayed; availability as repertoire-availability', 'stated', 'FW3 change register, row "Part II, progress"'),
 ('e35', 'FW2>FW3', ['FW2.18'], ['FW3.7'], 'changed', '"current good explanation" becomes the relation Merit', 'stated', 'FW3 change register, row "Part II, progress"'),
 ('e36', 'FW2>FW3', ['FW2.8', 'FW2.19'], ['FW3.9'], 'added', 'FW2\'s one word "knowledge" split into adequacy, merit and created knowledge', 'stated', 'FW3 change register, row "Part II, progress"'),
 ('e37', 'FW2>FW3', ['FW2.10'], ['FW3.14'], 'changed', '"related but nonidentical" becomes "extensionally independent; differ in logical type"', 'stated', 'FW3 change register, row "Part I-A, K-PHYSICALITY"'),
 ('e38', 'FW2>FW3', ['FW2.21'], ['FW3.11'], 'changed', 'physical knowledge read as a one-place predicate on information, explanatory knowledge as a relation with a problem argument', 'stated', 'FW3 T2, citing D1 §3 and §6 C1'),
 ('e39', 'FW2>FW3', ['FW2.16'], ['FW3.12'], 'added', 'acquisition is creation, as a consequence FW2 is said to entail', 'stated', 'FW3 change register, row "Part II, originative acts"'),
 ('e40', 'FW2>FW3', ['FW2.6'], ['FW3.13'], 'added', 'knowledge and standing orthogonal', 'stated', 'FW3 T4 (D1 §6 C3)'),
 ('e41', 'FW2>FW3', ['FW2.18'], ['FW3.15'], 'added', 'one count licensed: of conjecturally independent features reached, for preference only', 'stated', 'FW3 change register, row "Part II, quality"'),
 ('e42', 'FW2>FW3', ['FW2.18'], ['FW3.16'], 'added', 'warrant eliminated; many constraints give preference and nothing else', 'stated', 'FW3 change register, row "Part I-A, K-STANDING commentary"'),
 ('e43', 'FW2>FW3', ['FW2.14'], ['FW3.21'], 'added', 'specification discipline S1 to S10; "knowledge" a forbidden field', 'stated', 'FW3 change register, row "Part IV, refinement"'),
 ('e44', 'FW2>FW3', ['FW2.5'], ['FW3.20'], 'changed', '"doing work in an instance" becomes "deployed in an instance"; Deployed against DependsOn', 'stated', 'FW3 change register, rows "K-RECURSION headline" and "kernel and methods"'),
 ('e45', 'FW2>FW3', ['FW2.11'], ['FW3.22'], 'changed', 'statistical explaining-away: "a relation among representations" narrowed to "a relation of probabilistic dependency among hypotheses"', 'stated', 'FW3 III.2 R3'),
 ('e46', 'FW2>FW3', ['FW2.22'], ['FW3.23'], 'kept', 'the realization constraints kept; the deployed set added as a record fact of the realization', 'stated', 'FW3 change register, row "Part II, realization"; "No displayed definition of FW2 is withdrawn"'),
 ('e47', 'FW2>FW3', ['FW2.15', 'FW2.16'], ['FW3.19'], 'changed', '"possession" split into custody and deployability', 'stated', 'FW3 change register, row "Part II, newness and authorship"'),
 ('e48', 'FW2>FW3', ['FW2.1', 'FW2.2', 'FW2.3', 'FW2.4', 'FW2.7', 'FW2.9', 'FW2.13', 'FW2.17', 'FW2.20', 'FW2.25', 'FW2.26', 'FW2.27', 'FW2.28'], [], 'kept', 'kept as FW3\'s underlying layer: FW3 is an amendment and withdraws no displayed definition (no FW3 node repeats them)', 'stated', 'FW3 "Purpose and standing"; closing paragraph of its change register'),
 ('e49', 'FW2>FW3', ['FW2.32'], ['FW3.17'], 'added', 'occurrence-level questions ("Is this string knowledge?") ill-formed until an interpretation is fixed', 'stated', 'FW3 change register, row "Part II, contents"'),
 # FW3 -> FW4 (related)
 ('e50', 'FW3>FW4', ['FW3.1'], ['FW4.2'], 'changed', 'the same seven prohibitions; the open mode list changes from mechanism, geometry ... to production, determination, invariant, constitutive, selection', 'inferred', 'the two lists'),
 ('e51', 'FW3>FW4', ['FW3.2'], ['FW4.3'], 'replaced', 'minimal working subsets replaced by critical membership in support families', 'stated', 'FW5 "Reconciliation", "What the structurally extended source had already repaired"'),
 ('e52', 'FW3>FW4', ['FW3.3'], ['FW4.5'], 'changed', '"reaches more, harder to vary" restricted to the monotonicity lemma for one organization and family', 'stated', 'FW5 "Reconciliation", "More reach is not a count-based warrant"'),
 ('e53', 'FW3>FW4', ['FW3.4'], ['FW4.8'], 'changed', 'non-circularity (A2) moved out of Account into discharge', 'stated', 'FW5 "Reconciliation": FW4 "relocates circular evidential support away from the truth of a content"'),
 ('e54', 'FW3>FW4', [], ['FW4.13'], 'added', 'the discharge quadruple with anti-smuggling conditions', 'stated', 'FW4 "Where this belongs"'),
 ('e55', 'FW3>FW4', [], ['FW4.14'], 'added', 'mode modules M1 to M6', 'inferred', ''),
 ('e56', 'FW3>FW4', [], ['FW4.6'], 'added', 'transport with recoding, idealization and bounded approximation', 'stated', 'FW4 "Where this belongs" ("transport")'),
 ('e57', 'FW3>FW4', [], ['FW4.7'], 'added', 'type and token separated', 'inferred', ''),
 ('e58', 'FW3>FW4', ['FW3.7', 'FW3.8', 'FW3.9'], ['FW4.10'], 'kept', 'merit, created knowledge, three relations one word', 'inferred', 'wording nearly identical'),
 ('e59', 'FW3>FW4', ['FW3.11', 'FW3.14'], ['FW4.11'], 'kept', 'physical knowledge one-place, different type, extensionally independent; "uptake" becomes "imitation"', 'inferred', 'FW3 T2, T5 against FW4 Part VI'),
 ('e60', 'FW3>FW4', ['FW3.12'], ['FW4.12'], 'kept', 'acquisition is creation', 'inferred', ''),
 ('e61', 'FW3>FW4', ['FW3.15', 'FW3.16'], ['FW4.16'], 'kept', 'licensed count; warrant eliminated', 'inferred', ''),
 ('e62', 'FW3>FW4', ['FW3.21'], ['FW4.17'], 'changed', 'discipline kept; a machine may verify a structural claim and may not assert application or relevance', 'inferred', ''),
 ('e63', 'FW3>FW4', ['FW3.19', 'FW3.20'], ['FW4.15'], 'kept', 'custody, deployability, operative role; generator constraints now stated in the relation', 'inferred', ''),
 ('e64', 'FW3>FW4', ['FW3.5', 'FW3.6'], ['FW4.9'], 'kept', 'Bearing and Progress as instances of Account, still conjectures', 'inferred', ''),
 ('e65', 'FW3>FW4', ['FW3.22', 'FW3.23'], [], 'dropped', "the repairs addressed to FW2's text are not in FW4, which stands alone", 'inferred', 'FW4 "Where this belongs": "standalone rather than a patch"'),
 ('e66', 'FW3>FW4', ['FW3.10'], ['FW4.18'], 'kept', 'no knower argument', 'inferred', ''),
 ('e67', 'FW3>FW4', ['FW3.17'], ['FW4.19'], 'kept', 'occurrence-level questions ill-formed', 'inferred', ''),
 ('e68', 'FW3>FW4', ['FW3.18'], ['FW4.20'], 'kept', 'roles do not sort knowledge', 'inferred', ''),
 # FW2, FW3, FW4 -> FW5 (stated by FW5)
 ('e70', '>FW5', ['FW2.1'], ['FW5.2'], 'kept', 'explanatory realism and fallibility', 'stated', 'FW5 "Reconciliation", "What is retained"'),
 ('e71', '>FW5', ['FW2.5', 'FW2.9'], ['FW5.21'], 'kept', 'recursive scrutiny with operative return; universality as a modal claim', 'stated', 'same'),
 ('e72', '>FW5', ['FW2.16', 'FW2.7'], ['FW5.10'], 'kept', 'substantive authorship', 'stated', 'same'),
 ('e73', '>FW5', ['FW2.4', 'FW2.12'], ['FW5.7'], 'kept', 'criticism as itself conjectural and reason-bearing', 'stated', 'same'),
 ('e74', '>FW5', ['FW2.2'], ['FW5.11'], 'kept', 'problem recognition and values inside inquiry, now carried by declared obligations', 'stated', 'same (retained); "obligations" is FW5\'s form'),
 ('e75', '>FW5', ['FW3.1', 'FW4.2'], ['FW5.1', 'FW5.4'], 'replaced', 'the Because primitive replaced in the core definition by a structural account', 'stated', 'FW5 "Where this belongs"; "What \'no gaps\' can responsibly mean"'),
 ('e76', '>FW5', ['FW4.3'], ['FW5.5'], 'changed', 'critical membership kept; no upward closure and no minimal member assumed; collective contribution', 'stated', 'FW5 "Reconciliation", "What the structurally extended source had already repaired"'),
 ('e77', '>FW5', ['FW4.5', 'FW3.3'], ['FW5.5'], 'kept', 'only the containment for a fixed organization and family', 'stated', 'FW5 "Reconciliation", "More reach is not a count-based warrant"'),
 ('e78', '>FW5', ['FW3.15', 'FW4.16'], [], 'dropped', 'the licensed count withdrawn: "A numerical division into features can change without any increase in explanatory content"', 'stated', 'same section'),
 ('e79', '>FW5', ['FW3.7', 'FW4.10'], ['FW5.13'], 'dropped', 'Merit dropped as circular: preference would explain merit and merit preference', 'stated', 'FW5 "Choice and criticism without \'Merit\'"'),
 ('e80', '>FW5', ['FW3.8', 'FW4.10', 'FW2.19'], ['FW5.12'], 'changed', 'created knowledge becomes (EK): Repair of an epistemic obligation, Origin, Account, Deploy, ProducesVia; creation is historical', 'stated', 'FW5 "Created explanatory knowledge" (the parts); the lineage to FW3 I.5 is inferred'),
 ('e81', '>FW5', ['FW3.14', 'FW4.11'], ['FW5.19'], 'replaced', 'extensional independence replaced by a conditional common-realization bridge; the examples "mix content, instantiation, current capability, and historical events"', 'stated', 'FW5 "Knowledge that preserves its instantiation"; "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity"'),
 ('e82', '>FW5', ['FW3.11'], ['FW5.24'], 'changed', 'existential closure is ordinary logic giving a weaker statement; the display of indices stays a discipline', 'stated', 'FW5 "Reconciliation", "Factivity, approximation, and historical indexing"'),
 ('e83', '>FW5', ['FW3.12', 'FW4.12'], ['FW5.22'], 'dropped', 'acquisition is creation withdrawn as "stronger than the definitions and examples support"', 'stated', 'FW5 "Reconciliation", "Acquisition, historical origin, and retention cannot be collapsed"'),
 ('e84', '>FW5', ['FW3.20', 'FW4.15'], ['FW5.23'], 'changed', 'operative role is not a record a host can keep', 'stated', 'FW5 "Reconciliation", "Actual use is not a host-maintained role label"'),
 ('e85', '>FW5', ['FW2.22'], ['FW5.18'], 'changed', 'two layers kept as two kinds of defect; not "two anatomically separate mechanisms"', 'inferred', 'FW5 does not cite FW2 here; the wording matches'),
 ('e86', '>FW5', ['FW2.21'], ['FW5.19'], 'changed', 'physical knowledge becomes CTK with its realization ecology displayed', 'stated', 'FW5 "Knowledge that preserves its instantiation" [R4]'),
 ('e87', '>FW5', ['FW2.24'], ['FW5.15'], 'changed', 'the source on information media becomes an imported definition: information variables as clonable computation variables, interoperability', 'inferred', 'both cite Deutsch and Marletto 2015 (FW2 CT1; FW5 R3)'),
 ('e88', '>FW5', ['FW2.10'], ['FW5.20', 'FW5.3'], 'changed', 'constructor theory from "language" to "a constitutive part of the semantics"; knowledge changes owned repertoires, not what is possible', 'inferred', 'FW5 Part title and "The bridge that matters for creativity"'),
 ('e89', '>FW5', ['FW4.6'], ['FW5.6'], 'changed', 'bounded discrepancy on a scope, plus the accumulated error bound over steps', 'inferred', ''),
 ('e90', '>FW5', ['FW4.13'], ['FW5.4'], 'changed', 'the separation of structural theorem, application and question fidelity retained; structural accounting made a definition', 'stated', 'FW5 "Reconciliation", "What the structurally extended source had already repaired"'),
 ('e91', '>FW5', ['FW4.14'], ['FW5.27'], 'kept', 'production, identification (the balances), obstruction, constitutive rules', 'inferred', ''),
 ('e92', '>FW5', ['FW2.26'], ['FW5.26'], 'kept', 'the biological contrast', 'stated', 'FW5 "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity": "retains the biological contrast"'),
 ('e93', '>FW5', ['FW2.14'], ['FW5.9'], 'changed', 'record descriptions become positive and negative receipt sets', 'inferred', ''),
 ('e94', '>FW5', ['FW2.29'], ['FW5.8'], 'changed', '"not sufficient" no longer read as "cannot participate": a prediction can be a constituent of an explanatory argument', 'stated', 'FW5 "Reconciliation", "Why the negative deductions did not finish the positive theory"'),
 ('e95', '>FW5', ['FW2.23'], ['FW5.3'], 'changed', 'the medium constraint gives way to substrate independence with physical obligations', 'inferred', ''),
 ('e130', '>FW5', ['FW4.19'], ['FW5.28'], 'changed', 'contents and occurrences stay apart; nothing is called ill-formed', 'inferred', ''),
 ('e131', '>FW5', ['FW4.18', 'FW4.1'], ['FW5.2'], 'kept', 'realism: a relation holds whatever anyone accepts', 'inferred', ''),
 ('e132', '>FW5', ['FW4.20'], ['FW5.12'], 'changed', '(EK) counts accounts of a defect, a scope distinction, a mistaken question or an impossibility', 'inferred', 'FW5 "Created explanatory knowledge", first paragraph'),
 ('e133', '>FW5', ['FW4.4'], ['FW5.29'], 'kept', 'recoding preserves; substitution does not', 'inferred', ''),
 ('e134', '>FW5', ['FW2.5'], ['FW5.30'], 'kept', 'the complete critical episode and the creative one', 'inferred', ''),
 ('e99', 'I2>FW5', ['I2.2'], ['FW5.3'], 'kept', 'no complete translation into a formal language required of the thinker', 'inferred', 'FW5 "Substrate independence with physical obligations"'),
 ('e135', 'I2>FW5', ['I2.7'], ['FW5.8'], 'kept', 'formal backing gives no immunity from prose criticism', 'inferred', 'FW5 "Reconciliation", "What the executable audit does and does not settle" (of the 0.2 audit)'),
 ('e136', 'I2>FW5', ['I2.8'], ['FW5.5'], 'kept', 'hard to vary is no score; no count chooses explanations', 'inferred', ''),
 ('e96', 'I2>FW5', ['I2.4', 'I2.5'], ['FW5.8'], 'kept', 'admitting prose, enacting a working-use change and certifying a semantic conclusion kept apart', 'inferred', 'FW5 "What is retained" says this of specification 0.1 (S7); I2 is 0.4'),
 ('e97', 'I2>FW5', ['I2.6'], ['FW5.8'], 'kept', 'a machine check establishes a limited proposition, never immunity from prose criticism', 'inferred', 'FW5 "Elimination without a truth machine"; version gap as e96'),
 ('e98', 'I2>FW5', ['I2.10', 'I2.11', 'I2.13', 'I2.14'], [], 'dropped', 'implementation choices (scheduler, token allowance, storage policy) are "not a condition of this class"', 'stated', 'FW5 "Reconciliation", "What is retained" (of S7)'),
 # FW5 -> PT (through files 10 to 107)
 ('e100', 'FW5>PT', ['FW5.4'], ['PT.1', 'PT.3'], 'changed', '(E) kept in shape; being an explanation adds that the transport is not merely declared', 'recorded', 'results/S108 Part A round 2 (D16.XV, the owner\'s answer Q2 of S41)'),
 ('e101', 'FW5>PT', [], ['PT.2', 'PT.8', 'PT.23'], 'added', 'selected, constructed and declared provenances; selected: blind variation and survival, as in natural selection', 'recorded', 'results/S89, observation 9 (file 10, line 216); where between FW5 and file 10 it came in is not documented'),
 ('e102', 'FW5>PT', ['FW5.19'], [], 'dropped', 'CTK and the conditional bridge dropped at file 10', 'recorded', 'results/S89, observation 8: "File 10 dropped both"'),
 ('e103', 'FW5>PT', ['FW5.15'], ['PT.20'], 'changed', 'tasks and possibility kept; information variables dropped (information 0 times from file 10 on); copying kept as a transformation', 'recorded', 'results/S89, observations 3 and 8'),
 ('e104', 'FW5>PT', ['FW5.15', 'FW5.3'], ['PT.6'], 'changed', 'interoperability returns without its name: contents passing between media, and a barrier where they cannot', 'inferred', 'results/S89 missed relation M4 proposed it; the revision that added it is not traced here'),
 ('e105', 'FW5>PT', ['FW5.16'], ['PT.21'], 'kept', 'CT1 and CT2', 'recorded', 'results/S89, observation 3 (10:464 "nearly repeats" FW5)'),
 ('e106', 'FW5>PT', ['FW5.17', 'FW5.20'], ['PT.22'], 'kept', 'owned capability, achievement, CT3 and CT4 as tolerances', 'inferred', ''),
 ('e107', 'FW5>PT', ['FW5.12'], ['PT.19'], 'replaced', '(EK), created explanatory knowledge, renamed (EX), created explanation, at the S95 scrub, "pending the owner"', 'recorded', 'results/S95 Does the semantics hold without verificationist words.md, lines on (EK) and the OWNER row'),
 ('e108', 'FW5>PT', ['FW5.11'], ['PT.18'], 'kept', 'Repair (P); obligations become aims', 'inferred', ''),
 ('e109', 'FW5>PT', ['FW5.7'], ['PT.10', 'PT.11'], 'kept', 'Bearing as Account on the defect question (K1); reason use', 'inferred', ''),
 ('e110', 'FW5>PT', ['FW5.8'], ['PT.12'], 'changed', 'K3 kept; usability tied to premises live for the person, a premise taken as given allowed', 'recorded', 'decisions S23, S27; results/S96'),
 ('e111', 'FW5>PT', ['FW5.9'], ['PT.30'], 'changed', 'receipt sets become arguments usable by a person that rule a claim out; an absence rules out nothing', 'inferred', 'the S23 scrub is the likely step'),
 ('e112', 'FW5>PT', ['FW5.6'], ['PT.26'], 'kept', 'the accumulated error bound', 'recorded', 'results/S89, observation 14 (T2 in file 10)'),
 ('e113', 'FW5>PT', ['FW5.18'], [], 'dropped', 'the paragraph on representational fidelity against content correction is not in the present text', 'inferred', 'search of tests/107 for "inscription": 0'),
 ('e114', 'FW5>PT', ['FW5.14'], ['PT.15'], 'kept', 'dropped at file 10, back by the present text', 'recorded', 'results/S89, observation 14 (the drop); tests/107 Part X (the return)'),
 ('e115', 'FW5>PT', ['FW5.10', 'FW5.22'], ['PT.14', 'PT.16'], 'kept', 'Build and Origin; reconstruction by a learner is construction, relay is not; no theorem that every acquisition is creation', 'inferred', ''),
 ('e116', 'FW5>PT', ['FW5.21'], ['PT.24'], 'kept', 'recursion and universality', 'inferred', ''),
 ('e117', 'FW5>PT', ['FW5.13'], ['PT.31'], 'kept', 'no merit predicate; the appraisal relation an import', 'inferred', ''),
 ('e118', 'FW5>PT', ['FW5.2'], ['PT.5', 'PT.4'], 'kept', 'an error in the working dependence cannot explain; a relation holds whatever anyone accepts', 'inferred', ''),
 ('e119', 'FW5>PT', ['FW5.5'], ['PT.29'], 'changed', 'routes without minimality kept; hard to vary gives way to "easy to vary" as a problem of the second kind (rivals conflicting only outside the contract)', 'recorded', 'tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md'),
 ('e120', 'FW5>PT', [], ['PT.9', 'PT.25'], 'added', 'prediction, violation and surprise, and two responses to a violation, selection or construction', 'recorded', 'results/S89, observation 13 (file 10, lines 232 to 238)'),
 ('e121', 'FW5>PT', [], ['PT.13'], 'added', 'premises taken as given; the costly gamble of correcting errors with claims one does not contain', 'recorded', "decision S27, the owner's second footnote"),
 ('e122', 'FW5>PT', [], ['PT.27'], 'added', 'a failed answer stays failed', 'inferred', "matches the owner's S20, \"the mistake shouldn't be able to creep back in\"; the revision that added it is not traced here"),
 ('e123', 'FW5>PT', [], ['PT.28'], 'added', 'rivals and problems: a problem as a conflict no usable argument has decided', 'recorded', 'decision S20; tests/Revision 2 - hard to vary restated through rivals and problems'),
 ('e124', 'FW5>PT', ['FW5.15', 'FW5.12', 'FW5.19'], ['PT.32'], 'dropped', 'the words themselves: information from file 10 on, knowledge at the S95 scrub', 'recorded', 'results/S89, observation 8; results/S95'),
 ('e125', 'FW5>PT', ['FW5.3'], ['PT.6'], 'changed', 'physical possibility enters only where a content is instantiated or transformed, and as content a candidate can conflict with', 'recorded', "decisions S25, S26, S27; results/S96"),
 ('e126', 'FW5>PT', ['FW5.25'], ['PT.31'], 'changed', 'the refusal of compression or surprise as beauty gives way to aesthetics as a declared appraisal relation', 'inferred', ''),
 ('e127', 'FW5>PT', ['FW5.27'], ['PT.1'], 'kept', 'the exact constructions (production, identification, obstruction, constitutive rules) stay as Part VII', 'inferred', 'tests/107 Part VII headings'),
 ('e128', 'FW5>PT', ['FW5.23', 'FW5.24'], [], 'dropped', 'the reconciliation notes addressed to the earlier frameworks are not in the standalone text (decision S31: no provenance)', 'recorded', "decision S31, \"remove all reference to provenance, history or versions\""),
 ('e140', 'FW5>PT', ['FW5.28'], ['PT.7'], 'kept', 'occurrences and contents', 'inferred', ''),
 ('e141', 'FW5>PT', ['FW5.29'], ['PT.33'], 'kept', 'equivariance under recoding', 'inferred', ''),
 ('e142', 'FW5>PT', ['FW5.30'], ['PT.17'], 'kept', 'episodes; the recognized difficulty added', 'inferred', ''),
]

MISSING = [
    ('M0', 'FW0', 'the earlier event semantics and its audit (FW0\'s stated predecessors: Revision C, Revision D and its second audit; CR-1.0 with its constructor dossier and source key CT-7)'),
    ('M1', 'FW0 leads to it', 'the semantics before hardening'),
    ('Q1', 'FW0 leads to it', 'the audit of M1 and M2, hardening repairs'),
    ('M2', 'named in Q1\'s title only', 'not described'),
    ('FW1', 'FW1a is "SAME as FW1"', 'the recursive semantics after hardening'),
    ('FW1a', 'I2 and FW2 both descend from it (the same SHA-256 in both)', 'the Astra presentation copy of FW1; its sections are known only from I2\'s authority register (A1 to A12, with line ranges) and FW2\'s change register'),
    ('M8', 'I2', 'the LLM profile for I2 (the subordinate design profile)'),
    ('A1, A2, A3', 'FW2', 'addenda: prediction is not explanation; explanation from consensus; blocking, retention and uptake'),
    ('C1, C2', 'FW2', 'addenda: combinatorial media and closure; learnability and standing'),
    ('E1', 'FW2 (provenance list)', 'the extensible-class addendum (FW2 cites it by hash; "Where this belongs" names M3)'),
    ('M3', 'FW2', 'the extensible-class addendum'),
    ('D1, D2, D3', 'FW3 (as N1 to N3), FW5 (S2 to S4)', 'the three negative deductions: what knowledge cannot be; when accounts cannot hold; what work cannot be'),
    ('Q2', 'FW3 leads to it; FW4 names it as input', 'the audit of FW3, the closure gap'),
    ('M4', 'FW5', 'four exact inputs: executable specification 0.1 (S7), design decisions (S8), the audit of specification 0.2 (S9), the h-EPI dependency review (S10)'),
    ('O1, O2', 'FW5', 'the source-cited Deutsch books and constructor theory (S89, observation 1)'),
    ('Q3, Q4', 'FW5 leads to them', 'audits of FW5: structural weaknesses; proofs and anti-smuggling'),
    ('D4', 'FW5 leads to it', 'the audit theory: audits and conformance'),
    ('T3', 'FW5 leads to it', 'the language-model study'),
    ('layout.md', 'every file', 'the naming key and family tree'),
    ('file 20', 'this repository', 'the revised standalone theory, kept out on purpose (decision S4); between FW5 and file 10 nothing is supplied'),
]


def build():
    ids = [n[0] for n in N]
    assert len(ids) == len(set(ids)), 'duplicate node id'
    themes = [t for t, _ in THEMES]
    for n in N:
        assert n[1] in themes, n
        assert n[0].split('.')[0] in VERSIONS, n
    steps = [s for s, _, _ in STEPS]
    eids = [e[0] for e in E]
    assert len(eids) == len(set(eids)), 'duplicate edge id'
    for e in E:
        assert e[1] in steps, e
        for x in e[2] + e[3]:
            assert x in ids, (e[0], x)
        assert e[4] in ('kept', 'changed', 'dropped', 'added', 'replaced'), e
        assert e[6] in ('stated', 'recorded', 'inferred'), e
        assert e[3] or e[4] == 'dropped' or e[0] == 'e48', e    # a dropped edge may name the node that records the drop
        assert e[2] or e[4] == 'added', e    # an added edge may name the node it was added to
    nodes = [dict(id=i, version=i.split('.')[0], theme=t, name=nm, where=w, what=wh) for i, t, nm, w, wh in N]
    edges = [dict(id=i, step=s, **{'from': f}, to=t, kind=k, how=h, standing=st, by=b) for i, s, f, t, k, h, st, b in E]
    data = collections.OrderedDict([
        ('title', 'S110 The change map - the earlier frameworks and the present theory'),
        ('written', '29 September 2026, by the one Opus 5.5 agent of log S110 (decision S56), before the GLM cross-examination'),
        ('instruction', "decision S58: \"I suspect coming up with a change map here might help as well\" (Claude's reading of it is in the decision)"),
        ('versions', VERSIONS), ('themes', collections.OrderedDict(THEMES)),
        ('steps', [dict(id=s, name=n, basis=b) for s, n, b in STEPS]),
        ('standing_legend', {'stated': "the frameworks' own text or change register", 'recorded': "this project's records",
                             'inferred': "Claude's reading, marked"}),
        ('nodes', nodes), ('edges', edges),
        ('missing', [dict(id=a, named_by=b, what=c) for a, b, c in MISSING]),
    ])
    return json.dumps(data, indent=1, ensure_ascii=False) + '\n', nodes, edges


def main():
    text, nodes, edges = build()
    p = os.path.join(SEM, OUT)
    if '--check' in sys.argv[1:]:
        same = os.path.exists(p) and open(p, encoding='utf-8').read() == text
        print('check: %s' % ('identical to the build' if same else 'DIFFERS from the build'))
        sys.exit(0 if same else 1)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)
    c = collections.Counter
    print('nodes %d; by version %s' % (len(nodes), dict(c(n['version'] for n in nodes))))
    print('by theme %s' % dict(c(n['theme'] for n in nodes)))
    print('edges %d; by kind %s; by standing %s' % (len(edges), dict(c(e['kind'] for e in edges)), dict(c(e['standing'] for e in edges))))
    for s, name, _ in STEPS:
        es = [e for e in edges if e['step'] == s]
        print('  step %-8s %3d edges; kinds %s; standing %s' % (s, len(es), dict(c(e['kind'] for e in es)), dict(c(e['standing'] for e in es))))
    touched = {x for e in edges for x in e['from'] + e['to']}
    print('nodes on no edge: %s' % sorted(set(n['id'] for n in nodes) - touched))


if __name__ == '__main__':
    main()
