# S110 The change map - the earlier frameworks and the present theory

*Written 29 September 2026 by one Opus 5.5 agent (decision S56) for the owner's decision S58, "I suspect coming up with a change map here might help as well", before the GLM cross-examination of this file was sent. Claude's reading of "change map", recorded in S58: a map of how the attempts changed, one into the next and into the present theory (what each added, changed, kept and dropped, with where), and of how each treats information, knowledge and error correction, set beside constructor theory's account. The data are in the `.json` beside this file, written by `tools/s110_change_map.py` (its `--check` rebuilds and compares); the tables in section 10 are that file's contents. Nothing in the theory, the frameworks or any Part A or Part B file is written. Nothing here is settled (S28); nothing is ranked (S20); what hard to vary covers stays parked (S34): its nodes are mapped only. "Candidate" or "explanation", never "model", for what the theory judges (S43). The frameworks' own words are in straight quotation marks; book quotations, in curly ones, are checked by `tools/s110_quote_check.py`.*

## In brief

- **172 nodes** (FW0 20, I2 14, FW2 32, FW3 23, FW4 20, FW5 30, the present theory 33) in ten themes; **132 edges**: 54 changed, 44 kept, 17 added, 11 dropped, 6 replaced. **Standing**: 45 stated by the frameworks' own text or change registers, 16 recorded by this project's records, **71 inferred by Claude** (every edge across a missing link is inferred).
- **The lineage is broken in three places**: FW0 reaches FW2 and I2 only through the missing M1, Q1, FW1 and FW1a; FW4's link to FW3 is "RELATED", its production "not authenticated"; FW5 reaches the present theory through the missing Q3, Q4, D4, T3 and then through this repository's files 10 to 107.
- **Five telling changes**: (1) FW3 made why-dependence ("Because") the one primitive; FW5 replaced it by a structural account, which the present theory keeps. (2) FW3 split "knowledge" into three relations and declared constructor theory's knowledge a different logical type, "extensionally independent"; FW5 answered that the two examples "mix content, instantiation, current capability, and historical events" and put a conditional bridge in its place; file 10 dropped the bridge; the S95 scrub renamed the remaining knowledge relation "created explanation". (3) Merit and the licensed count, FW3's last comparative devices, were dropped by FW5. (4) FW2's "two layers of error correction" (fidelity against content) was softened by FW5 to two kinds of defect and is not in the present text. (5) Between FW5 and file 10 the selected / constructed / declared provenances came in, and with them, in the present theory, the question of being an explanation turns on provenance (Part A round 2).
- **What persisted through every supplied version**: newness relative to what the system could already deploy; authorship of a construction; criticism that bears on a defect with reasons, as against a signal or a mismatch; that prediction is not explanation; that contents and their carriers are different things; that success and retention are different things (creation is not undone by loss); no score, ranking or probability on explanations; fallibility with no immunity for anything.
- **Information theory**: Shannon's never entered (0 mentions in all seven texts). What entered: Belnap's four-valued ledger (FW0, gone by the present theory); constructor theory of information (FW2, FW5; the word "information" gone from file 10 on, its machinery of tasks and retained capability kept, interoperability back without its name); constructor-theoretic knowledge (FW0 to FW5; dropped at file 10); predictive and statistical accounts as contrasts (FW2, FW3; now only "prediction" and "surprise" in the theory's own sense); a correlational account and expected information gain, both refused (FW2, I2).
- **Missing links**: 20, listed in section 9.

## 0. What was read

All six frameworks were read: FW3 and FW4 in full; FW2 in full except most of Part III's cases (read by heading and search); FW5 in full at every section on explanation, error, criticism, knowledge, constructor theory and the reconciliation, the rest by heading and search; FW0 at its reading guide, sorts, fallibility contract, later slices (§§16 to 20), change register and source map, the rest by heading; I2 at Parts I, II and V and its two registers ("Authority register", "Research register"), the rest by heading. The present theory (`tests/107`) was read at Parts 0, I, IV, VI (in part), VIII (in part), IX to XIII; searched in full for "information", "knowledge", "error", "inscription", "reach", "hard to vary", "easy to vary", "merit", "custody", "interoperab-", "resilien-", "catalys-". `authority/10` was searched for "knowledge". The S89 audit was read in full and is built on, not redone. What was not read line by line may hold a node this map misses; section 11 says where that matters.

## 1. The lineage, as the documents give it

| step | edges | what joins the two, and how sure the documents are |
|---|---|---|
| FW0 → FW2 | 19, all inferred | FW0 "Where this belongs": it leads to M1 and Q1, and "The route from this family to M1 is not documented by the supplied files". FW2 is the successor of FW1a. Nothing supplied joins FW0 to FW1a. |
| FW0 → I2 | 5, all inferred | as above; I2 specifies FW1a. |
| FW1a → I2 and FW1a → FW2 | none (FW1a not supplied) | **Both give FW1a the same SHA-256** (`823f5088…`), so I2 and FW2 are two children of the same bytes. I2's "Authority register" gives FW1a's sections with line ranges (A1 to A12); FW2's change register lists what FW2 added and says "Nothing in FW1a is withdrawn". What in FW2 is not in its register was, by FW2's own statement, in FW1a. |
| FW2 → FW3 | 20, all stated | FW3's change register, row by row, through the missing D1 to D3. FW3 is "a candidate amendment layer": it withdraws no displayed definition of FW2 (edge e48 records what it keeps without repeating). |
| FW3 → FW4 | 19: 5 stated, 14 inferred | FW4 "Where this belongs": "RELATED is deliberate: the conceptual connection is visible, but the archive does not authenticate a direct FW3/Q2-to-FW4 production history." The five stated edges are stated by FW5, which calls FW4 "the structurally extended source" and lists what it "already" repaired in FW3. |
| FW2, FW3, FW4 → FW5 | 31: 19 stated, 12 inferred | FW5's "Reconciliation with the supplied evolution" and source register (S1 to S10), through the missing D1 to D3 and M4. |
| I2 → FW5 | 6: 1 stated, 5 inferred | FW5 read executable specification **0.1** (S7) and an audit of **0.2** (S9); I2 is **0.4**, dated 7 September 2026, the day before FW5. No document says FW5 read I2. |
| FW5 → the present theory | 32: 16 recorded, 16 inferred | Nothing supplied: FW5 leads to the missing Q3, Q4, D4, T3. This repository holds FW5 byte for byte as `authority/00 …` (the supplied copy differs only by its "Where this belongs" header; checked by `diff`), and records it as "an older, richer predecessor of file 10" (`authority/NOT-IN-BUNDLE.md`). From file 10 on, the changes are in this project's records (S89, S95 and the decisions). |

Two checks on the documents: the supplied files are "renamed reading editions", and their bytes do not match the hashes FW5 gives for FW2, FW3 and FW4 (checked on the text after the editorial header; the headers say "Hashes bind the unchanged originals, not this reading copy", so no mismatch of content is shown). FW3's internal title and file name disagreed ("V1" and "V2"), as its header says.

## 2. Totals

| version | nodes | | theme | nodes |
|---|---|---|---|---|
| FW0 | 20 | | error correction, criticism and repair (ERR) | 39 |
| I2 | 14 | | knowledge (KNO) | 25 |
| FW2 | 32 | | explanation (EXP) | 22 |
| FW3 | 23 | | creativity (CRE) | 19 |
| FW4 | 20 | | method (MET) | 15 |
| FW5 | 30 | | information (INF) | 14 |
| present theory (PT) | 33 | | standing, appraisal, records (STA) | 13 |
| | | | constructor theory's machinery (PHY) | 12 |
| | | | hard to vary and reach (HTV, mapped only) | 7 |
| | | | recursion and universality (REC) | 6 |
| **all** | **172** | | | **172** |

| step | kept | changed | added | dropped | replaced | stated | recorded | inferred |
|---|---|---|---|---|---|---|---|---|
| FW0 → FW2 | 3 | 13 | 0 | 2 | 1 | 0 | 0 | 19 |
| FW0 → I2 | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 5 |
| FW2 → FW3 | 2 | 10 | 8 | 0 | 0 | 20 | 0 | 0 |
| FW3 → FW4 | 9 | 4 | 4 | 1 | 1 | 5 | 0 | 14 |
| FW2, FW3, FW4 → FW5 | 11 | 15 | 0 | 3 | 2 | 19 | 0 | 12 |
| I2 → FW5 | 5 | 0 | 0 | 1 | 0 | 1 | 0 | 5 |
| FW5 → PT | 14 | 8 | 5 | 4 | 1 | 0 | 16 | 16 |
| **all** | **44** | **54** | **17** | **11** | **6** | **45** | **16** | **71** |

A node can sit on several edges; an edge can join several nodes (e48 joins 13 FW2 nodes to FW3 as "kept"). The counts are of edges as recorded, not of ideas: a finer or coarser cut of the same documents would give other numbers (S20: no count is a warrant here).

## 3. The five most telling changes

1. **The primitive of explanation, put in and taken out** (e31, e75, e100). FW3 declared "why-dependence" the theory's "one explanatory primitive", bounded by seven prohibitions, and built work, adequacy and knowledge on it ("the theory has a single explanatory primitive, 'because'"). FW5 answered that "Calling the final word regulative does not establish its extension" and replaced it in the core definition by a structural account: anchoring, fidelity, question fidelity, non-circular dependence, non-vacuity. The present theory keeps FW5's shape as (E), and adds that a merely declared correspondence explains nothing (PT.3). *Standing: stated to FW5; recorded to PT.*
2. **Knowledge split, set against constructor theory, and then let go** (e36 to e38, e81, e102, e107, e124). FW2 said physical and explanatory knowledge are "related but nonidentical". FW3 split FW2's one word into three relations (adequacy, merit, created knowledge) and made constructor theory's knowledge a different logical type, "extensionally independent" of explanatory knowledge, on two examples. FW4 kept both. FW5 kept the split in effect (it has created explanatory knowledge and CTK) but refused the independence claim and gave a conditional bridge instead. File 10 dropped CTK and the bridge (S89, observation 8); the S95 scrub renamed (EK) "created explanation", pending the owner. The present theory has neither word. Section 8 follows this in full.
3. **The last comparative devices dropped** (e79, e78). FW3 had Merit ("withstands the criticism ... sufficiently well to merit preference") and one licensed count (of independent features reached, "for preference and nothing else"). FW5 dropped both: Merit "makes preference explain merit and merit explain preference"; a count of features "can change without any increase in explanatory content". Nothing comparative has come back since. *Stated.*
4. **Two layers of error correction, softened and then gone from the text** (e14, e85, e113). FW2 made it a realization constraint and a named conjecture: a layer correcting errors of representation "by redundancy and settling" and a layer correcting errors of content, the second "not obtainable by iterating the first" ("consensus among consensuses is still consensus"). FW5 kept the two kinds of defect ("A damaged inscription and a false theory are not the same error") and dropped the two mechanisms. The present text has no such paragraph. *Inferred for both steps.* This is the frameworks' nearest point to the book's two kinds of correction (file 1, I5).
5. **Provenance enters the definition of explanation** (e101, e100). No supplied framework has "selected" and "constructed" as the two histories a correspondence can have. File 10 has them, and the present theory makes being an explanation depend on not being merely declared; Part A round 2 found that whether a candidate is an explanation moved far more with readings of "declared" than with any other part of the definition. So the present theory decides "explanation" partly by where a correspondence came from: from selection (variation and survival, the book's route to knowledge without design) or from construction (conjecture and criticism, the book's route in a mind) [reading]. *Recorded for the fact (S89 observation 9; S108 results); where between FW5 and file 10 it came in is not documented.*

## 4. How each version treats information, knowledge, error correction, creativity and explanation

Constructor theory's column is from file 1 (`results/S110 Error correction from constructor theory's perspective.md`), where every statement is marked as the book's, implied or Claude's reading.

| | information | knowledge | error correction | creativity | explanation |
|---|---|---|---|---|---|
| **constructor theory (the book)** | what can be flipped and copied; information media; interoperability | information able to keep itself instantiated (resilient information); needs no knower; in an abstract catalyst | not defined; needed under no-design laws for anything complex to persist; the cell, the scribe, the factory, the cricket; criticism as the correction of errors in conjectures | the ability to create new knowledge, by thinking; how, open | physical theories are conjectured explanations; not defined |
| **FW0** | a sort: "physical information is not explanatory knowledge" (FW0.7); Belnap's four-valued ledger for evidence (FW0.3) | two sorts: K_E, explanatory knowledge creation (critical result, success, access); K_CT, physical, deferred, non-equivalence an open obligation | the kernel applied to its own evidence; recordable criticism; grounded adjudication; correction certificates and improvement witnesses | an originative act with a witness; newness against a repertoire; natural selection a contrast class | decisive relations kept as primitives, each with a witness |
| **I2** | refused as a quantity: no "expected information gain"; tokens counted as allowance, not as information retained | needs "actual explanatory progress"; continued use certifies nothing | "reason-sensitive revision with an operative return": stop the reuse of an error without erasing it; checks answer only their question | daydreaming, jolts; creativity is not correctness | carried by FW1a (not supplied) |
| **FW2** | constructor theory of information as a source (CT1); the medium constraint; a correlational account "not adopted"; contents against occurrences | "explanatory improvement, not persistence" (K-PROGRESS); explanatory knowledge creation; physical knowledge "information with a causal capacity for preserving its instantiation", "related but nonidentical" | reason-bearing criticism (K-CRITICISM), not feedback or prediction error; two layers of error correction; a first-layer class of mere fidelity correction | K-ORIGIN, OCA, productivity is not creativity; generator constraints | Account a substantive relation; prediction is not explanation |
| **FW3** | "Is this string knowledge?" ill-formed until an interpretation is fixed (T18) | three relations, one word (adequacy, merit, created knowledge); no knower; physical knowledge one-place, a different type, extensionally independent (T2, T5) | Bearing as Account on a defect (conjecture); Progress as a gain in Account or Bearing | acquisition is creation (T3) | why-dependence the one primitive, seven prohibitions; work by minimal working subsets |
| **FW4** | as FW3 (R18) | as FW3; the independence example worded with "imitation" | as FW3; circularity moved to discharge | as FW3 | the primitive kept; "supports", organizations, transport, discharge with anti-smuggling, mode modules |
| **FW5** | constructor theory "a constitutive part": information variables as clonable computation variables; interoperability; compression refused as beauty | (EK) created explanatory knowledge; CTK with its realization ecology; a conditional bridge; independence "not inferable" from the examples | criticism and bearing; "Elimination without a truth machine"; Repair (P); accumulated error bound (T2); fidelity and content correction two kinds of defect | construction and transfer; acquisition-is-creation withdrawn; inexplicit representation | no Because: a structural account (E) |
| **present theory** | the word absent; carriers and contents; representation a fidelity relation with a history; contents passing between media | the word absent; (EX) created explanation in (EK)'s place; selected transports as knowledge-like correspondences without a represented target [reading] | K1 to K3; repair; a failed answer stays failed; two responses to a violation; the "costly gamble" of premises taken as given, without which "error correction could become impossibly costly" | construction against selection; Origin; question-finding | Account(E) and not declared |

## 5. What persisted through every supplied version

"Persisted" means: a chain of kept or changed edges runs from FW0 (or from FW2, where FW0 has no counterpart) through FW3, FW4 and FW5 to the present theory, with the core of the commitment unchanged. This is the change-map counterpart of the owner's approach of S31 (look for what came through many rounds untouched while the text around it changed); what hard to vary covers is not decided by it (S34).

| commitment | chain (node ids) | what changed along it |
|---|---|---|
| newness is relative to what the system could already deploy | FW0.10 → FW2.15 → (FW3 keeps FW2) → FW5.10 → PT.16 | the baseline's grain and boundary made explicit |
| authorship and origination need a construction, not an emission | FW0.11 → FW2.16 → (FW3 keeps) → FW5.10 → PT.14, PT.16 | "acquisition is creation" came in (FW3, FW4) and went out (FW5) |
| criticism bears on a defect with reasons; a signal, a failure or a prediction error is not criticism | FW0.12 → FW2.12 → FW3.5 → FW4.9 → FW5.7 → PT.10 | bearing became Account on the defect question (FW3 conjecture, PT's K1) |
| prediction is not explanation | FW0.7 → FW2.11 → FW3.1 (prohibition 1) → FW4.2 → FW5.4 → PT.1 ("It does not say prediction is explanation") | FW5 allowed a prediction to be a constituent of an explanatory argument |
| contents and carriers are different | FW0.7 → FW2.32 → FW3.17 → FW4.19 → FW5.28 → PT.7, PT.8 | FW3/FW4's "ill-formed" dropped; PT defines representation by fidelity and history |
| success, retention and creation are distinct; loss does not undo creation | FW0.8 → FW2.19 → FW3.8 → FW4.10 → FW5.12 → PT.19 | the success condition went from a judgment K_E to Repair (P) of an explanatory aim |
| no score, ranking, probability or aggregate on explanations | FW0.4 (dropped) / I2.9 → FW2.18, FW2.31 → FW3.15 (one count licensed) → FW5.13 (dropped) → PT.31 | FW3's licensed count is the one exception, and it was dropped |
| fallibility with nothing immune | FW0.5 → FW2.5 → (FW3 keeps) → FW4.1 → FW5.2 → PT.4, PT.5 | from a contract on records to commitments on relations |
| a retained capability, not one occurrence, is what physics is asked about | FW0.17 → FW2.21, FW2.10 → FW3.23 → FW5.16, FW5.17 → PT.20 to PT.22 | FW5 imported constructor theory's tasks and made retention exact (CT1, CT2) |

## 6. What was tried and dropped

| tried in | what | dropped in | why, as the documents say (or Claude's reading, marked) |
|---|---|---|---|
| FW0 | grounded adjudication of attacks; a four-valued evidence ledger | FW2 (the ledger kept only as descriptions) | inferred: FW2 says a schematic attack edge cannot supply bearing, and record states are "not four kinds of truth" |
| FW0 | every attribution answerable by a finite object | FW2 | inferred: "A finite record does not logically determine universal capacity" |
| FW0 | K_CT and a theorem of its non-equivalence with K_E | never discharged; FW3 asserted independence instead | inferred |
| FW2 | two layers of error correction as a realization constraint | FW5 (softened), the present text (absent) | FW5: different defects need not mean "two anatomically separate mechanisms" |
| FW3 | why-dependence as the one primitive | FW5 | stated: a declared primitive "cannot by itself answer the request to explain what distinguishes the relation's positive instances" |
| FW3 | minimal working subsets | FW4 | stated by FW5: replaced by critical membership |
| FW3 | "reaches more, harder to vary" across contents | FW4 | stated by FW5: valid only as a containment for a fixed organization and family |
| FW3, FW4 | Merit; the licensed count | FW5 | stated (section 3, item 3) |
| FW3, FW4 | acquisition is creation | FW5 | stated: "stronger than the definitions and examples support" |
| FW3, FW4 | extensional independence of the two knowledges | FW5 | stated (section 8) |
| FW3, FW4 | host-maintained role labels as facts | FW5 | stated: "being shown a source is not understanding or using it" |
| FW3, FW4 | existential closure forbidden | FW5 | stated: it "yields a weaker statement that omits the witness" |
| FW5 | CTK and the conditional bridge | file 10 | recorded (S89, observation 8); why is not documented |
| FW5 | the word "information" | file 10 | recorded (S89: 0 occurrences in 10, 11, 12) |
| FW5 → file 10 | (EK) under the name "knowledge" | S95 scrub | recorded: renamed (EX) "pending the owner"; the S23 list removes "anything belief related"; S95's reader asked the owner to rule on "knowledge" (results/S95, the OWNER row) |
| FW5 | inexplicit representation | file 10, then back | recorded for the drop (S89, observation 14); present in the present theory's Part X |

## 7. Where each attempt to bring in information theory went

| attempt | where it entered | what it was used for | what became of it |
|---|---|---|---|
| **Shannon's theory** (entropy, channel, codes) | nowhere: 0 occurrences of "Shannon" or "entropy" in all seven texts | | never entered. The book does not use it either (file 1, section 8) |
| **Belnap's four-valued logic** (an information ordering of evidence states) | FW0 §7.2, "Raw ledger (Belnap)", with a "knowledge" order and a monotonicity theorem (§21) | the state of the evidence for a claim: no case, positive, negative, both | FW2: four optional descriptions of a record, "not four kinds of truth"; FW3, FW4: record states as descriptions; FW5: positive and negative receipt sets, "not four kinds of reality"; the present theory: arguments usable by a person, and "that absence rules out nothing". Gone as a logic; the refusal to let a record decide a content persisted |
| **constructor theory of information** (Deutsch and Marletto 2015) | FW2 source CT1 ("error correction as a condition of retained capacity"), K-PHYSICALITY, the realization section | a language for what a realization must be able to do | FW5 made it "a constitutive part": substrate, attribute, task; information variables "clonable computation variables"; interoperability; CT1 to CT4. From file 10: tasks, possibility, retained realization and tolerances kept (Part XII); the word "information" and its variables dropped; interoperability back as contents passing between media (Part I) |
| **constructor-theoretic knowledge** (Marletto) | FW0 K_CT (deferred); FW2 "physical knowledge", M5, M7 | a second knowledge relation beside the explanatory one | FW3, FW4: one-place, different type, extensionally independent; FW5: CTK with a realization ecology and a conditional bridge; file 10: dropped; the present theory: absent. S89 (observation 8) offered restoring the bridge as a defined relation, or leaving it out with a reason; neither was taken up |
| **predictive and statistical accounts** ("contrast cases from a predictive-model account of intelligence"; statistical "explaining away") | FW2 addenda A1, A2; sources H1, H2 | contrasts: continuous predictive learning with consensus, and prediction-error repair, "instantiate no explanatory activity" | FW3 R3 named explaining-away "a relation of probabilistic dependency among hypotheses"; FW5 allowed a prediction to be a constituent of an explanation; the present theory keeps prediction and surprise in its own sense (Part IV). Its "surprise" is a violation at a change the history never met, not Shannon's surprisal [reading] |
| **a correlational account of information** (named with source P1) | FW2 source keys | none: "the correlational account of information [is] not adopted" | never used. The source was not opened for this job (the task forbids opening that book) |
| **expected information gain** | I2 Part V | refused as the meaning of attention learning | not seen again |
| **compression** | FW5 "What 'no gaps' can responsibly mean" | refused as a definition of beauty | the present theory makes aesthetics an imported appraisal relation |
| **error accumulation in approximate computation** (Deutsch's digital error correction, which S89 set beside it) | FW4 III.5 (bounded discrepancy); FW5 (T2) | how far a representation can drift from its target over steps | kept as the present theory's (T2): "Without a modulus, no accumulated bound follows". S89 (observation 14) proposed a lemma on error correction built from it; not taken up |

## 8. The knowledge position of FW3 and FW4: how it arose, changed and fared

**What it says.** FW3 T2: "physical knowledge (Marletto) is a one-place predicate on information; the two differ in logical type". FW3 T5 and case 10, FW4 Part VI, R2, R5 and case 9: the two are "extensionally independent": "a false belief spread by imitation preserves its instantiation and accounts for nothing; an explanation that accounted for its feature and was lost preserved nothing." With it: "knowledge" names three relations (adequacy, merit, created knowledge); none has a knower argument (T1); roles do not sort knowledge (T19); "Is this string knowledge?" has no answer until an interpretation is fixed (T18); FW2's K-PROGRESS stands behind all of it: knowledge growth "is explanatory improvement, not persistence".

**How it arose.** FW0 already kept the two apart as sorts ("physical information is not explanatory knowledge") and left their non-equivalence as an undischarged theorem obligation (FW0.7, FW0.9). FW2 characterized physical knowledge in Marletto's terms and said the two are "related but nonidentical" (FW2.10, FW2.21), and that "the merit of an explanatory discovery is not the duration for which one copy survives". FW3's change register cites the missing D1 ("What knowledge cannot be", §3 and §6 C4) for the step from "nonidentical" to "extensionally independent" and "different logical type" (e37, e38). *Stated.*

**How it changed.** FW4 kept it word for word in substance (e59). FW5 rejected the inference and kept the difference: "It is therefore a mistake to infer 'extensional independence' of explanatory and physical knowledge merely from the pair of examples", because the examples "mix content, instantiation, current capability, and historical events" and "A comparison needs a common domain, a time, and a realization ecology before any logical implication can be assessed" (e81). In its place FW5 put a conditional bridge: if an explanatory organization is instantiated as information, and a vehicle uses it in a retained task organization that maintains or reconstructs it, and its specific organization contributes causally to that maintenance, then the realization instantiates the constructor-theoretic preservation role. No unconditional converse. FW5 also said existential closure is ordinary logic (against T2's "not permitted") (e82). *Stated.*

**How it fared.** File 10 dropped CTK and the bridge (S89, observation 8, e102), keeping only created explanatory knowledge (EK) and the refusal of any "is knowledge" predicate. The S95 scrub renamed (EK) "created explanation" (EX), "pending the owner" (e107); S95's reader named the loss: "The rename loses the direct bridge to the sources' non-belief sense of the word". **What the present theory kept of the position**: the separation of creation from persistence ((EX) asks only that the new content be deployable at the end of the episode, not that it last; a carrier keeps its provenance when access to it is lost); no knower argument in any relation (faithfulness without assessors, PT.4); contents apart from carriers (PT.7). **What it did not keep**: the word "knowledge"; any relation for constructor theory's knowledge; the independence claim; the three-way split (merit is gone; adequacy is (E); created knowledge is (EX)). *Recorded and inferred as marked on each edge.*

**Beside the book** (file 1). [reading throughout this paragraph] The book's definition is literally one-place: “Knowledge is defined entirely via counterfactuals: it is information that is capable of remaining instantiated in physical systems.” (Marletto, ch. 5) But its own examples make it relative to an environment, since it says that “To be resilient in a given environment, an adaptation needs to be useful” (Marletto, ch. 5), and they give it an object, since in the first chapter the book says of adaptations that “for adaptations, it is knowledge of some features of the environment” (Marletto, ch. 1). So FW3's "one-place predicate" holds of the book's wording and not of its use: on the book's use it has at least an environment place, which is close to what FW5 called the "realization ecology". FW3/FW4's first example, the spreading falsehood, is exactly Deutsch's anti-rational meme, which Deutsch counts as carrying knowledge, of its hosts' vulnerabilities, while of its overt content he writes that it “need contain no truth.” (Deutsch, ch. 15) So on Deutsch's reading the example does not show preservation without knowledge; it shows knowledge whose "of" differs from what the idea says. The second example, the lost explanation, is one the book does not discuss; the book's closing chapter treats knowledge created while reading as lasting while the reader's mind lasts (ch. 7, paraphrase), which is a conditional persistence, not none. File 3 takes the tension up for the owner's question and leaves it open.

## 9. The missing links

Named by the supplied documents and not supplied (20):

| missing | named by | what it is, as named |
|---|---|---|
| M0 | FW0 | the earlier event semantics and its audit (FW0's stated predecessors: Revision C, Revision D and its second audit; CR-1.0 with its constructor dossier and source key CT-7) |
| M1 | FW0 ("where it leads") | the semantics before hardening |
| Q1 | FW0 ("where it leads") | the audit of M1 and M2, hardening repairs |
| M2 | Q1's title only | not described |
| FW1 | FW1a's title ("SAME as FW1") | the recursive semantics after hardening |
| FW1a | I2 and FW2 (the same SHA-256) | the Astra presentation copy of FW1; known only through I2's register A1 to A12 and FW2's change register |
| M8 | I2 | the LLM profile for I2 |
| A1, A2, A3 | FW2 | addenda: prediction is not explanation; explanation from consensus; blocking, retention and uptake |
| C1, C2 | FW2 | addenda: combinatorial media and closure; learnability and standing |
| E1 | FW2 (provenance list) | the extensible-class addendum (by hash) |
| M3 | FW2 ("Where this belongs") | the extensible-class addendum (perhaps E1 under another name; not settled here) |
| D1, D2, D3 | FW3 (as N1 to N3); FW5 (S2 to S4) | the negative deductions: what knowledge cannot be; when accounts cannot hold; what work cannot be. D1 carries the argument for the two-types result |
| Q2 | FW3, FW4 | the audit of FW3, "the closure gap" |
| M4 | FW5 | executable specification 0.1, design decisions, the audit of specification 0.2, the h-EPI review |
| O1, O2 | FW5 | the source-cited Deutsch books and constructor theory (also S89, observation 1) |
| Q3, Q4 | FW5 ("where it leads") | audits of FW5: structural weaknesses; proofs and anti-smuggling |
| D4 | FW5 | the audit theory: audits and conformance |
| T3 | FW5 | the "Language-model study" |
| layout.md | every file | the naming key and family tree |
| file 20 | this repository | the revised standalone theory, kept out on purpose (decision S4); nothing supplied lies between FW5 and file 10 |

No gap was filled by guess: every edge across one of them is marked inferred. Sources cited by the frameworks and not read for this job: Deutsch, *The Fabric of Reality* (F1, F3); Hawkins (H1, H2, H5, H6); the source P1 and P2 (the task forbids opening one of them); the papers R1 to R7 of FW5.

## 10. The nodes and edges

The full lists, by theme and by step, are in the `.json` beside this file (`nodes`, `edges`, `missing`), each node with its version, theme, name, place and one line, each edge with its step, kind, one line, standing and what states it. The tables below are generated from it.

### Nodes: information, carriers and media (INF, 14)

| id | name | where |
|---|---|---|
| FW0.7 | cross-sort bridges; physical information is not explanatory knowledge | §1 "Sorts", closing paragraph |
| I2.10 | attention learning without expected information gain | Part V "The chosen meaning of learning" |
| I2.11 | tokens as a flow of computational allowance | Part VII; "Why computation does not explode by construction of the controller" |
| FW2.23 | the medium constraint; a correlational account of information not adopted | Part II realization constraint 1 [P1]; "Source keys", P1 |
| FW2.24 | constructor theory of information as a source (CT1) | "Source keys and attribution boundaries", CT1 |
| FW2.32 | contents, occurrences and interpretations | Part II "Contents, occurrences, and interpretations" |
| FW3.17 | T18: occurrence-level questions are ill-formed | Part II T18 |
| FW4.19 | R18: occurrence-level questions are ill-formed until an interpretation is fixed | Part VIII R18 |
| FW5.15 | physical tasks and information | "Constructor theory as a constitutive part of the semantics", "Physical tasks and information" |
| FW5.25 | beauty not defined by compression or surprise | "What 'no gaps' can responsibly mean" |
| FW5.28 | contents and occurrences | "Mathematical foundations", "Contents and occurrences" |
| PT.6 | substrate independence reaching as far as contents can pass between media | Part I "Substrate independence with physical conditions" |
| PT.7 | occurrences and contents | Part IV "Occurrences and contents" |
| PT.8 | representation: a fidelity relation with a history (R) | Part IV "Representation is defined, not supplied" |

### Nodes: knowledge (KNO, 25)

| id | name | where |
|---|---|---|
| FW0.8 | EKC, explanatory knowledge creation | §16.5 |
| FW0.9 | K_CT, physical knowledge, a different sort (deferred) | §16.6; §20; §27 row "K_CT declaration" (source CT-7) |
| I2.12 | knowledge creation needs actual explanatory progress; use does not certify learned knowledge | Part I first section; Part V first section |
| FW2.8 | K-PROGRESS: knowledge growth is explanatory improvement, not persistence | Part I-A |
| FW2.19 | explanatory knowledge creation | Part II "Progress, possession, and historical assessment" |
| FW2.21 | physical knowledge in the realization section | Part II "Physical realization and constructor-theoretic scope" |
| FW2.26 | biological contrast | Part III "Distributed inquiry and biological contrast" |
| FW2.27 | evolved constraints as provisional background | Part II "Argument dependencies ..." last paragraph; Part III |
| FW3.7 | Merit | I.5 |
| FW3.8 | created knowledge | I.5 |
| FW3.9 | three relations, one word | I.5; Part V rule S9 |
| FW3.10 | T1: no explanatory relation has a knower argument | Part II T1 |
| FW3.11 | T2: no existential closure; physical knowledge a one-place predicate on information | Part II T2 |
| FW3.13 | T4: knowledge and standing are orthogonal | Part II T4; Part IV case 8 |
| FW3.14 | T5: explanatory and physical knowledge are extensionally independent | Part II T5; Part IV case 10 |
| FW3.18 | T19: roles do not sort knowledge | Part II T19 |
| FW4.10 | Merit and created knowledge | Part VI |
| FW4.11 | physical knowledge | Part VI "Physical knowledge"; Part VIII R2, R5; Part XI case 9 |
| FW4.18 | R1: no explanatory relation has a knower argument | Part VIII R1 |
| FW4.20 | R19: roles do not sort knowledge | Part VIII R19 |
| FW5.12 | created explanatory knowledge (EK) | "Created explanatory knowledge" |
| FW5.19 | CTK: constructor-theoretic knowledge with its realization ecology; a conditional bridge | same Part, "Knowledge that preserves its instantiation"; "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity" |
| FW5.26 | biological lineage: preservation without critical episode | "The bridge that matters for creativity", last paragraph |
| PT.19 | created explanation (EX) | Part XI "Created explanation" |
| PT.32 | neither "information" nor "knowledge" occurs | the whole text (0 and 0 occurrences) |

### Nodes: error correction, criticism and repair (ERR, 39)

| id | name | where |
|---|---|---|
| FW0.2 | the kernel applied to its own evidence | Part I "What this revision does"; §7.1 |
| FW0.4 | grounded adjudication, attacks propagated along essential dependencies | §7.3 |
| FW0.5 | fallibility contract | §5; Part I "What is still non-negotiable" |
| FW0.12 | criticism, response, reason use; the critical creative process | §11; §14 |
| FW0.13 | target-correct correction certificate | §16.3 |
| FW0.14 | outcome-indexed improvement witnesses | §16.4 |
| I2.3 | error correction is reason-sensitive revision with an operative return | Part I, section of that name |
| I2.4 | the collection is not the working set; parking | Part II "The collection is not the active working set" |
| I2.5 | a prose judgment can change use without a formal test | Part II, section of that name |
| I2.6 | mechanical checks answer only their declared question | Part II "Mechanical checking is available without a formatting gate" |
| I2.7 | checks are not the privileged entrance to criticism | Part II, section of that name |
| FW2.2 | K-PROBLEM: a problem is an interpreted difficulty that matters | Part I-A |
| FW2.4 | K-CRITICISM: criticism has a reason-bearing role | Part I-A |
| FW2.12 | Bearing and UsesReason | Part II "Reason-bearing criticism and counterfactual uptake" |
| FW2.13 | Essential and Usable_j | Part II "Argument dependencies and the effect of criticizing a premise" |
| FW2.20 | first-layer class: retention with fidelity correction, no kernel | Part II "The stratified hierarchy" |
| FW2.22 | two layers of error correction | Part II realization constraint 2; Part IV "Named criticism routes and conjectures" |
| FW2.25 | a prediction error is not a criticism | Part III, section of that name (from A1.2) |
| FW2.31 | Progress: kinds of improvement with no common scale | Part II "Progress, possession, and historical assessment" |
| FW3.5 | Bearing as Account on a defect (conjecture) | I.4 |
| FW3.6 | Progress as a gain in Account or Bearing (conjecture) | I.4 |
| FW4.9 | Bearing, contribution and progress as instances of Account | Part V |
| FW5.6 | approximate transport: accumulated error bound (T2) | "Transport and preservation", "Approximate transport" |
| FW5.7 | criticism and its bearing; reason use as causal organization | "Criticism, evidence, and operative decisions" |
| FW5.8 | "Elimination without a truth machine"; what a test contradicts (K3) | same Part, "Elimination without a truth machine" |
| FW5.11 | obligations and Repair (P) | "Obligations rather than a hidden score" |
| FW5.18 | representational fidelity and content correction are different defects | same Part, "Physical realization of semantic organization" |
| FW5.30 | critical and creative episodes | "Understanding, provenance, and creative events", "Critical and creative episodes" |
| PT.9 | prediction, violation, surprise; two responses to a violation | Part IV "Prediction, surprise, violation" |
| PT.10 | Bearing (K1) as Account on the question whether the target has the defect | Part IX "Bearing" |
| PT.11 | reason use | Part IX "Reason use" |
| PT.12 | usability (K2) and what a test rules out (K3) | Part IX |
| PT.13 | premises taken as given: the costly gamble | Part IX "Premises taken as given" |
| PT.17 | episodes; recognized difficulty; closing is a choice | Part X "Episodes" |
| PT.18 | Repair (P) | Part XI "Repair" |
| PT.25 | Arguments 3 and 4: selected transports underdetermined at unseen changes; surprise needs an incomplete history | Part XVI, 3 and 4 |
| PT.26 | approximate transport (T2) | Part VIII "Approximate transport" |
| PT.27 | a failed answer stays failed | Part VIII, section of that name |
| PT.28 | rivals and problems | Part VI "Rivals", "Problems" |

### Nodes: creativity: origination, newness, construction (CRE, 19)

| id | name | where |
|---|---|---|
| FW0.10 | newness relative to a repertoire | §9 |
| FW0.11 | authorship and the originative creative act, bound to its witness | §12; §13 |
| FW0.16 | contrast classes, including NaturalSelection | §19 |
| I2.13 | daydreaming and jolts | Part VIII |
| FW2.3 | K-CONJECTURE: conjecture precedes criticism of it | Part I-A |
| FW2.7 | K-ORIGIN: creation has a provenance; understanding can be reconstructive | Part I-A |
| FW2.15 | newness relative to an attributed system and a grain | Part II, section of that name |
| FW2.16 | authorship and the originative act OCA | Part II "Authorship and distributed contribution"; "Originative acts and critical processes" |
| FW2.17 | productivity is not creativity | Part II "Originative acts and critical processes" (from A3.2) |
| FW2.28 | generator constraints and the extensible class | Part II "Methods can be criticized from within inquiry"; "The stratified hierarchy" |
| FW3.12 | T3: acquisition is creation | Part II T3 |
| FW4.12 | R3: acquisition is creation | Part VIII R3 |
| FW5.10 | construction and transfer; newness; the originative act | "Understanding, provenance, and creative events" |
| FW5.14 | inexplicit representation is not absent representation | "Inexplicit, artistic, and normative inquiry" |
| FW5.22 | acquisition is not always creation | "Reconciliation", "Acquisition, historical origin, and retention cannot be collapsed" |
| PT.2 | three provenances: selected, constructed, declared | Part IV "Three provenances" |
| PT.14 | Deploy and Build; reconstruction is construction, relay is not | Part X |
| PT.15 | inexplicit representation is not absent | Part X |
| PT.16 | newness (N) and origin (G) | Part X "Newness", "Origin" |

### Nodes: explanation (EXP, 22)

| id | name | where |
|---|---|---|
| FW0.19 | decisive relations kept as primitives, each given a witness | Part I "What the document is for"; §10 |
| FW2.11 | Account: attempting and actually explaining | Part II "Attempting an explanation and actually explaining" |
| FW2.29 | a "predictive-model account of intelligence" as contrast | Part III "General model learning is not explanatory organization" (from A1.1); source H1 |
| FW3.1 | K-BECAUSE: why-dependence, the one primitive, bounded by seven prohibitions | I.1 |
| FW3.2 | work by minimal working subsets | I.2 |
| FW3.4 | Account A1 to A4, factive over work | I.3 |
| FW3.22 | R3: statistical explaining-away renamed | III.2 R3 |
| FW4.2 | Because, seven prohibitions, modes changed | Part II |
| FW4.3 | "support families"; work as critical membership | III.1 |
| FW4.4 | organizations and recoding | III.2 |
| FW4.6 | transport: recoding, idealization, approximation | III.5 |
| FW4.7 | type and token | III.6 |
| FW4.8 | Account A1 to A3; circularity moved to discharge | Part IV |
| FW4.13 | the discharge quadruple and its anti-smuggling conditions | Part IX |
| FW4.14 | mode modules M1 to M6 | Part X |
| FW5.1 | no residual Because primitive | "What 'no gaps' can responsibly mean" |
| FW5.4 | structural answer (E) | "Explanatory adequacy without a Because primitive" |
| FW5.27 | exact domain constructions | "Exact domain constructions" |
| FW5.29 | equivariance under genuine recoding | "Results and discriminating constructions", first section |
| PT.1 | an explanation is a question-relevant organization held by a transport tested by change-fidelity | Part 0 "What this document claims" |
| PT.3 | being an explanation: Account(E) and not Dec(t) | Part V; Part I "Fallibility without error-as-work" |
| PT.33 | Argument 8: equivariance under structure-preserving recoding | Part XVI, 8 |

### Nodes: constructor theory's physical machinery: tasks, possibility, retained capability (PHY, 12)

| id | name | where |
|---|---|---|
| FW0.17 | physical realization, deferred | §20 |
| I2.14 | finite resources are realisation conditions | "Authority register" A10; Parts VI and VII |
| FW2.10 | K-PHYSICALITY: embodiment constrains without replacing explanation | Part I-A |
| FW3.23 | realization addition: the deployed set is a record fact, the working set is not | III.4 |
| FW5.3 | substrate independence with physical obligations | "The commitments", last section |
| FW5.16 | retained realization (CT1) and the retention fixed point (CT2) | same Part |
| FW5.17 | owned capability; a first discovery is not a repeatable first discovery (CA) | same Part |
| FW5.20 | capability grades against possibility (CT3, CT4) | same Part, "The bridge that matters for creativity" |
| PT.20 | tasks and possibility | Part XII "Tasks" |
| PT.21 | retained realization (CT1) and the retention fixed point (CT2) | Part XII |
| PT.22 | owned capability, achievement, tolerances (CT3, CT4) | Part XII |
| PT.23 | selection in the physical module | Part XII "Selection in the physical module" |

### Nodes: standing, appraisal, records and warrant (STA, 13)

| id | name | where |
|---|---|---|
| FW0.3 | four-valued raw ledger (Belnap) | §7.2 "Raw ledger (Belnap)"; §21 |
| FW0.6 | no stored status; version-stamped judgments | §5 last block; §7.7 |
| FW2.6 | K-STANDING: generation confers no standing | Part I-A (FW2, new) |
| FW2.14 | appraisal is conjectural content; four record descriptions | Part II "Appraisal is also conjectural content" |
| FW3.15 | T16: the licensed count | Part II T16 |
| FW3.16 | T17: warrant is eliminated | Part II T17 |
| FW3.19 | custody and deployability | I.6; III.1 table |
| FW4.15 | standing, custody, deployability, operative role, generator constraints | Part VII |
| FW4.16 | R16 licensed count; R17 warrant eliminated | Part VIII |
| FW5.9 | evidence receipts | "Evidence receipts without false certainty" |
| FW5.13 | choice and criticism without Merit | "Choice and criticism without 'Merit'" |
| FW5.23 | actual use is not a host-maintained role label | "Reconciliation", section of that name |
| PT.30 | arguments usable by a person; an absence rules out nothing | Part IX "Arguments" |

### Nodes: hard to vary and reach (mapped only; S34 parks it) (HTV, 7)

| id | name | where |
|---|---|---|
| FW0.15 | hard to vary over a declared variant family; reach body | §18 |
| I2.8 | hard to vary is an explanatory challenge, not a score | Part I, section of that name |
| FW2.18 | quality: current good explanation, FreeVariation, reach | Part II "Explanatory quality, constraint, and reach" |
| FW3.3 | constraint and reach as two projections of work | I.2; Part II T12 |
| FW4.5 | reach and the monotonicity lemma; HTV as indispensability of every commitment | III.1; III.3 |
| FW5.5 | "support families" without minimality; hard to vary and reach as containment | "Work, redundancy, interference, and infinity"; "Hard-to-vary and reach" |
| PT.29 | easy to vary; commitments that do no work | Part VI |

### Nodes: recursion and universality (REC, 6)

| id | name | where |
|---|---|---|
| FW0.18 | capacity under perturbations | §17 |
| FW2.5 | K-RECURSION: target closure, role preservation, return relevance | Part I-A; Part II "The recursive kernel as a relation, not a scheduler" |
| FW2.9 | K-UNIVERSALITY: a capacity claim | Part I-A |
| FW3.20 | T14, T15: target closure over roles; Deployed is a record fact | Part II T14, T15 |
| FW5.21 | recursive openness and universality | "Recursive openness and explanatory universality" |
| PT.24 | recursion, barriers, universality | Part XIII |

### Nodes: method commitments (MET, 15)

| id | name | where |
|---|---|---|
| FW0.1 | "model" and "record" kept apart | Part I "What the document is for" |
| FW0.20 | final criterion: every disputed attribution answerable by a finite, attackable object | "Final criterion" |
| I2.1 | "creative inquiry material, not certified truth" | Part I "The product is creative inquiry material, not certified truth" |
| I2.2 | prose is a complete interface | Part I "Prose is a complete interface to participation" |
| I2.9 | no rankings or optimisation objectives | Part I, section of that name |
| FW2.1 | K-REAL: reality is not conferred by a judgment | Part I-A "Reality is not conferred by a judgment" |
| FW2.30 | three standpoints | Part II "The model and the three standpoints" |
| FW3.21 | specification discipline; the field "knowledge" forbidden | Part V |
| FW4.1 | commitments, with Indexing | Part I |
| FW4.17 | specification discipline | Part XII |
| FW5.2 | explanatory realism and fallibility | "The commitments", first section |
| FW5.24 | existential closure is legitimate; the attribution discipline is kept | "Reconciliation", "Factivity, approximation, and historical indexing" |
| PT.4 | faithfulness without assessors | Part I |
| PT.5 | fallibility without error-as-work | Part I |
| PT.31 | no appraisal of its own; the appraisal relation an import | Part 0 "What this document does not claim"; Part XI "Appraisal" |

### Edges: FW0 to FW2, across the missing M1, Q1, FW1 and FW1a (19)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e1 | FW0.1 | FW2.30 | changed | "model" against "record" becomes three standpoints: a situated judgment is added between them | inferred: the wording of both; no document joins them |
| e2 | FW0.3 | FW2.14 | changed | the four-valued ledger with an adjudication operator becomes four optional descriptions of a record, "not four kinds of truth" | inferred: FW2 Part II "Appraisal is also conjectural content" |
| e3 | FW0.4 | (none) | dropped | grounded (Dung) adjudication has no counterpart; FW2: a schematic attack edge cannot supply bearing | inferred: FW2 Part II "Argument dependencies ..." |
| e4 | FW0.5 | FW2.5 | changed | recordability of any criticism becomes target closure, role preservation and return relevance | inferred |
| e5 | FW0.7 | FW2.10 | changed | "physical information is not explanatory knowledge" becomes "related but nonidentical" | inferred |
| e6 | FW0.8 | FW2.19 | kept | knowledge creation is a critical creative result plus success plus availability; retention is availability, not success | inferred |
| e7 | FW0.9 | FW2.21 | changed | the deferred sort K_CT gets a characterization (information with a causal capacity for preserving its instantiation); still no bridge theorem | inferred |
| e8 | FW0.10 | FW2.15 | kept | newness relative to the repertoire before the event | inferred |
| e9 | FW0.11 | FW2.16 | kept | authorship and the originative act | inferred |
| e10 | FW0.12 | FW2.12 | changed | the critical process with its witness becomes Bearing and UsesReason over a contrast family | inferred |
| e11 | FW0.13, FW0.14 | FW2.31 | replaced | correction certificates and outcome-indexed witnesses give way to a Progress relation with kinds of improvement and no common scale | inferred |
| e12 | FW0.15 | FW2.18 | changed | hard to vary over a declared family becomes the FreeVariation diagnostic, comparative and respect-relative | inferred |
| e13 | FW0.16 | FW2.20, FW2.29 | changed | neutral contrast classes become the first-layer comparison class and named contrast cases | inferred |
| e14 | FW0.17 | FW2.22 | changed | a deferred realization with "noise, repair" obligations becomes six realization constraints, one of them two layers of error correction | inferred |
| e15 | FW0.18 | FW2.9 | changed | capacity under perturbations becomes K-UNIVERSALITY and the modal Can | inferred |
| e16 | FW0.19 | FW2.11 | changed | primitive relations with witnesses become substantive relations (Account, Bearing, Progress, Capacity) with attribution evidence apart | inferred |
| e17 | FW0.20 | (none) | dropped | the demand that every attribution be answerable by a finite object; FW2: "A finite record does not logically determine universal capacity" | inferred: FW2 Part III, section of that name |
| e18 | FW0.6 | FW2.14 | changed | no stored status becomes: record states describe the record | inferred |
| e24 | FW0.7 | FW2.32 | changed | "tokens are not their contents" becomes contents, occurrences and interpretations indexed by grain | inferred |

### Edges: FW0 to I2, across the missing M1, Q1, FW1 and FW1a (5)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e19 | FW0.5 | I2.3 | changed | recordable criticism becomes error correction with an operative return that a host must check | inferred |
| e20 | FW0.2 | I2.6 | changed | certificates as attackable content become bounded mechanical checks whose results are open to criticism | inferred |
| e21 | FW0.4 | I2.9 | replaced | automatic adjudication gives way to no rankings and no automatic semantic adjudication | inferred: I2 "P: subordinate supplied profile": "automatic semantic adjudication ... not inherited" (of M8, not of FW0) |
| e22 | FW0.1 | I2.1 | changed | "model" against "record" becomes "material" against "certified truth" | inferred |
| e23 | FW0.8 | I2.12 | changed | knowledge creation needs actual progress; I2 adds that continued use of a method certifies nothing | inferred |

### Edges: FW2 to FW3, through the missing D1, D2 and D3 (20)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e30 | FW2.11 | FW3.4 | changed | Account restated through minimal working subsets (A1 to A4); background includes every essential standard | stated: FW3 change register, row "Part II, attempting" |
| e31 | (none) | FW3.1 | added | why-dependence declared the one explanatory primitive, the "why" K-REAL invokes | stated: FW3 change register, rows "Part I-A, new" and "Part I-A, K-REAL" |
| e32 | FW2.18 | FW3.3 | changed | work set-level; constraint and reach as projections of work; FreeVariation over subsets | stated: FW3 change register, row "Part II, quality" |
| e33 | FW2.12 | FW3.5 | changed | Bearing conjectured to be Account on a defect | stated: FW3 change register, row "Part II, criticism" |
| e34 | FW2.19 | FW3.8 | changed | created knowledge displayed; availability as repertoire-availability | stated: FW3 change register, row "Part II, progress" |
| e35 | FW2.18 | FW3.7 | changed | "current good explanation" becomes the relation Merit | stated: FW3 change register, row "Part II, progress" |
| e36 | FW2.8, FW2.19 | FW3.9 | added | FW2's one word "knowledge" split into adequacy, merit and created knowledge | stated: FW3 change register, row "Part II, progress" |
| e37 | FW2.10 | FW3.14 | changed | "related but nonidentical" becomes "extensionally independent; differ in logical type" | stated: FW3 change register, row "Part I-A, K-PHYSICALITY" |
| e38 | FW2.21 | FW3.11 | changed | physical knowledge read as a one-place predicate on information, explanatory knowledge as a relation with a problem argument | stated: FW3 T2, citing D1 §3 and §6 C1 |
| e39 | FW2.16 | FW3.12 | added | acquisition is creation, as a consequence FW2 is said to entail | stated: FW3 change register, row "Part II, originative acts" |
| e40 | FW2.6 | FW3.13 | added | knowledge and standing orthogonal | stated: FW3 T4 (D1 §6 C3) |
| e41 | FW2.18 | FW3.15 | added | one count licensed: of conjecturally independent features reached, for preference only | stated: FW3 change register, row "Part II, quality" |
| e42 | FW2.18 | FW3.16 | added | warrant eliminated; many constraints give preference and nothing else | stated: FW3 change register, row "Part I-A, K-STANDING commentary" |
| e43 | FW2.14 | FW3.21 | added | specification discipline S1 to S10; "knowledge" a forbidden field | stated: FW3 change register, row "Part IV, refinement" |
| e44 | FW2.5 | FW3.20 | changed | "doing work in an instance" becomes "deployed in an instance"; Deployed against DependsOn | stated: FW3 change register, rows "K-RECURSION headline" and "kernel and methods" |
| e45 | FW2.11 | FW3.22 | changed | statistical explaining-away: "a relation among representations" narrowed to "a relation of probabilistic dependency among hypotheses" | stated: FW3 III.2 R3 |
| e46 | FW2.22 | FW3.23 | kept | the realization constraints kept; the deployed set added as a record fact of the realization | stated: FW3 change register, row "Part II, realization"; "No displayed definition of FW2 is withdrawn" |
| e47 | FW2.15, FW2.16 | FW3.19 | changed | "possession" split into custody and deployability | stated: FW3 change register, row "Part II, newness and authorship" |
| e48 | FW2.1, FW2.2, FW2.3, FW2.4, FW2.7, FW2.9, FW2.13, FW2.17, FW2.20, FW2.25, FW2.26, FW2.27, FW2.28 | (none) | kept | kept as FW3's underlying layer: FW3 is an amendment and withdraws no displayed definition (no FW3 node repeats them) | stated: FW3 "Purpose and standing"; closing paragraph of its change register |
| e49 | FW2.32 | FW3.17 | added | occurrence-level questions ("Is this string knowledge?") ill-formed until an interpretation is fixed | stated: FW3 change register, row "Part II, contents" |

### Edges: FW3 (and the missing Q2) to FW4: related, production history not authenticated (19)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e50 | FW3.1 | FW4.2 | changed | the same seven prohibitions; the open mode list changes from mechanism, geometry ... to production, determination, invariant, constitutive, selection | inferred: the two lists |
| e51 | FW3.2 | FW4.3 | replaced | minimal working subsets replaced by critical membership in "support families" | stated: FW5 "Reconciliation", "What the structurally extended source had already repaired" |
| e52 | FW3.3 | FW4.5 | changed | "reaches more, harder to vary" restricted to the monotonicity lemma for one organization and family | stated: FW5 "Reconciliation", "More reach is not a count-based warrant" |
| e53 | FW3.4 | FW4.8 | changed | non-circularity (A2) moved out of Account into discharge | stated: FW5 "Reconciliation": FW4 "relocates circular evidential support away from the truth of a content" |
| e54 | (none) | FW4.13 | added | the discharge quadruple with anti-smuggling conditions | stated: FW4 "Where this belongs" |
| e55 | (none) | FW4.14 | added | mode modules M1 to M6 | inferred |
| e56 | (none) | FW4.6 | added | transport with recoding, idealization and bounded approximation | stated: FW4 "Where this belongs" ("transport") |
| e57 | (none) | FW4.7 | added | type and token separated | inferred |
| e58 | FW3.7, FW3.8, FW3.9 | FW4.10 | kept | merit, created knowledge, three relations one word | inferred: wording nearly identical |
| e59 | FW3.11, FW3.14 | FW4.11 | kept | physical knowledge one-place, different type, extensionally independent; "uptake" becomes "imitation" | inferred: FW3 T2, T5 against FW4 Part VI |
| e60 | FW3.12 | FW4.12 | kept | acquisition is creation | inferred |
| e61 | FW3.15, FW3.16 | FW4.16 | kept | licensed count; warrant eliminated | inferred |
| e62 | FW3.21 | FW4.17 | changed | discipline kept; a machine "may verify S" (the structural claim) and may not assert application or relevance | inferred |
| e63 | FW3.19, FW3.20 | FW4.15 | kept | custody, deployability, operative role; generator constraints now stated in the relation | inferred |
| e64 | FW3.5, FW3.6 | FW4.9 | kept | Bearing and Progress as instances of Account, still conjectures | inferred |
| e65 | FW3.22, FW3.23 | (none) | dropped | the repairs addressed to FW2's text are not in FW4, which stands alone | inferred: FW4 "Where this belongs": "standalone rather than a patch" |
| e66 | FW3.10 | FW4.18 | kept | no knower argument | inferred |
| e67 | FW3.17 | FW4.19 | kept | occurrence-level questions ill-formed | inferred |
| e68 | FW3.18 | FW4.20 | kept | roles do not sort knowledge | inferred |

### Edges: FW2, FW3, FW4 (and the missing D1 to D3, M4) to FW5 (31)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e70 | FW2.1 | FW5.2 | kept | explanatory realism and fallibility | stated: FW5 "Reconciliation", "What is retained" |
| e71 | FW2.5, FW2.9 | FW5.21 | kept | recursive scrutiny with operative return; universality as a modal claim | stated: same |
| e72 | FW2.16, FW2.7 | FW5.10 | kept | substantive authorship | stated: same |
| e73 | FW2.4, FW2.12 | FW5.7 | kept | criticism as itself conjectural and reason-bearing | stated: same |
| e74 | FW2.2 | FW5.11 | kept | problem recognition and values inside inquiry, now carried by declared obligations | stated: same (retained); "obligations" is FW5's form |
| e75 | FW3.1, FW4.2 | FW5.1, FW5.4 | replaced | the Because primitive replaced in the core definition by a structural account | stated: FW5 "Where this belongs"; "What 'no gaps' can responsibly mean" |
| e76 | FW4.3 | FW5.5 | changed | critical membership kept; no upward closure and no minimal member assumed; collective contribution | stated: FW5 "Reconciliation", "What the structurally extended source had already repaired" |
| e77 | FW4.5, FW3.3 | FW5.5 | kept | only the containment for a fixed organization and family | stated: FW5 "Reconciliation", "More reach is not a count-based warrant" |
| e78 | FW3.15, FW4.16 | (none) | dropped | the licensed count withdrawn: "A numerical division into features can change without any increase in explanatory content" | stated: same section |
| e79 | FW3.7, FW4.10 | FW5.13 | dropped | Merit dropped as circular: preference would explain merit and merit preference | stated: FW5 "Choice and criticism without 'Merit'" |
| e80 | FW3.8, FW4.10, FW2.19 | FW5.12 | changed | created knowledge becomes (EK): Repair of an epistemic obligation, Origin, Account, Deploy, ProducesVia; creation is historical | stated: FW5 "Created explanatory knowledge" (the parts); the lineage to FW3 I.5 is inferred |
| e81 | FW3.14, FW4.11 | FW5.19 | replaced | extensional independence replaced by a conditional common-realization bridge; the examples "mix content, instantiation, current capability, and historical events" | stated: FW5 "Knowledge that preserves its instantiation"; "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity" |
| e82 | FW3.11 | FW5.24 | changed | existential closure is ordinary logic giving a weaker statement; the display of indices stays a discipline | stated: FW5 "Reconciliation", "Factivity, approximation, and historical indexing" |
| e83 | FW3.12, FW4.12 | FW5.22 | dropped | acquisition is creation withdrawn as "stronger than the definitions and examples support" | stated: FW5 "Reconciliation", "Acquisition, historical origin, and retention cannot be collapsed" |
| e84 | FW3.20, FW4.15 | FW5.23 | changed | operative role is not a record a host can keep | stated: FW5 "Reconciliation", "Actual use is not a host-maintained role label" |
| e85 | FW2.22 | FW5.18 | changed | two layers kept as two kinds of defect; not "two anatomically separate mechanisms" | inferred: FW5 does not cite FW2 here; the wording matches |
| e86 | FW2.21 | FW5.19 | changed | physical knowledge becomes CTK with its realization ecology displayed | stated: FW5 "Knowledge that preserves its instantiation" [R4] |
| e87 | FW2.24 | FW5.15 | changed | the source on information media becomes an imported definition: information variables as clonable computation variables, interoperability | inferred: both cite Deutsch and Marletto 2015 (FW2 CT1; FW5 R3) |
| e88 | FW2.10 | FW5.20, FW5.3 | changed | constructor theory from "language" to "a constitutive part of the semantics"; knowledge changes owned repertoires, not what is possible | inferred: FW5 Part title and "The bridge that matters for creativity" |
| e89 | FW4.6 | FW5.6 | changed | bounded discrepancy on a scope, plus the accumulated error bound over steps | inferred |
| e90 | FW4.13 | FW5.4 | changed | the separation of structural theorem, application and question fidelity retained; structural accounting made a definition | stated: FW5 "Reconciliation", "What the structurally extended source had already repaired" |
| e91 | FW4.14 | FW5.27 | kept | production, identification (the balances), obstruction, constitutive rules | inferred |
| e92 | FW2.26 | FW5.26 | kept | the biological contrast | stated: FW5 "Reconciliation", "Constructor-theoretic knowledge is not accidental longevity": "retains the biological contrast" |
| e93 | FW2.14 | FW5.9 | changed | record descriptions become positive and negative receipt sets | inferred |
| e94 | FW2.29 | FW5.8 | changed | "not sufficient" no longer read as "cannot participate": a prediction can be a constituent of an explanatory argument | stated: FW5 "Reconciliation", "Why the negative deductions did not finish the positive theory" |
| e95 | FW2.23 | FW5.3 | changed | the medium constraint gives way to substrate independence with physical obligations | inferred |
| e130 | FW4.19 | FW5.28 | changed | contents and occurrences stay apart; nothing is called ill-formed | inferred |
| e131 | FW4.18, FW4.1 | FW5.2 | kept | realism: a relation holds whatever anyone accepts | inferred |
| e132 | FW4.20 | FW5.12 | changed | (EK) counts accounts of a defect, a scope distinction, a mistaken question or an impossibility | inferred: FW5 "Created explanatory knowledge", first paragraph |
| e133 | FW4.4 | FW5.29 | kept | recoding preserves; substitution does not | inferred |
| e134 | FW2.5 | FW5.30 | kept | the complete critical episode and the creative one | inferred |

### Edges: I2 to FW5: FW5 read executable specification 0.1 and an audit of 0.2, not I2 (0.4) (6)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e99 | I2.2 | FW5.3 | kept | no complete translation into a formal language required of the thinker | inferred: FW5 "Substrate independence with physical obligations" |
| e135 | I2.7 | FW5.8 | kept | formal backing gives no immunity from prose criticism | inferred: FW5 "Reconciliation", "What the executable audit does and does not settle" (of the 0.2 audit) |
| e136 | I2.8 | FW5.5 | kept | hard to vary is no score; no count chooses explanations | inferred |
| e96 | I2.4, I2.5 | FW5.8 | kept | admitting prose, enacting a working-use change and certifying a semantic conclusion kept apart | inferred: FW5 "What is retained" says this of specification 0.1 (S7); I2 is 0.4 |
| e97 | I2.6 | FW5.8 | kept | a machine check "can establish a limited proposition", never immunity from prose criticism | inferred: FW5 "Elimination without a truth machine"; version gap as e96 |
| e98 | I2.10, I2.11, I2.13, I2.14 | (none) | dropped | implementation choices (scheduler, token allowance, storage policy) are "not a condition of this class" | stated: FW5 "Reconciliation", "What is retained" (of S7) |

### Edges: FW5 to the present theory, across the missing Q3, Q4, D4, T3 and through files 10, 11, 12, the revision 2 drafts, 99 and 103 to 107 of this repository (32)

| id | from | to | kind | how | standing |
|---|---|---|---|---|---|
| e100 | FW5.4 | PT.1, PT.3 | changed | (E) kept in shape; being an explanation adds that the transport is not merely declared | recorded: results/S108 Part A round 2 (D16.XV, the owner's answer Q2 of S41) |
| e101 | (none) | PT.2, PT.8, PT.23 | added | selected, constructed and declared provenances; selected: blind variation and survival, as in natural selection | recorded: results/S89, observation 9 (file 10, line 216); where between FW5 and file 10 it came in is not documented |
| e102 | FW5.19 | (none) | dropped | CTK and the conditional bridge dropped at file 10 | recorded: results/S89, observation 8: "File 10 dropped both" |
| e103 | FW5.15 | PT.20 | changed | tasks and possibility kept; information variables dropped (information 0 times from file 10 on); copying kept as a transformation | recorded: results/S89, observations 3 and 8 |
| e104 | FW5.15, FW5.3 | PT.6 | changed | interoperability returns without its name: contents passing between media, and a barrier where they cannot | inferred: results/S89 missed relation M4 proposed it; the revision that added it is not traced here |
| e105 | FW5.16 | PT.21 | kept | CT1 and CT2 | recorded: results/S89, observation 3 (10:464 "nearly repeats" FW5) |
| e106 | FW5.17, FW5.20 | PT.22 | kept | owned capability, achievement, CT3 and CT4 as tolerances | inferred |
| e107 | FW5.12 | PT.19 | replaced | (EK), created explanatory knowledge, renamed (EX), created explanation, at the S95 scrub, "pending the owner" | recorded: `results/S95 Does the semantics hold without verificationist words.md`, lines on (EK) and the OWNER row |
| e108 | FW5.11 | PT.18 | kept | Repair (P); obligations become aims | inferred |
| e109 | FW5.7 | PT.10, PT.11 | kept | Bearing as Account on the defect question (K1); reason use | inferred |
| e110 | FW5.8 | PT.12 | changed | K3 kept; usability tied to premises live for the person, a premise taken as given allowed | recorded: decisions S23, S27; results/S96 |
| e111 | FW5.9 | PT.30 | changed | receipt sets become arguments usable by a person that rule a claim out; an absence rules out nothing | inferred: the S23 scrub is the likely step |
| e112 | FW5.6 | PT.26 | kept | the accumulated error bound | recorded: results/S89, observation 14 (T2 in file 10) |
| e113 | FW5.18 | (none) | dropped | the paragraph on representational fidelity against content correction is not in the present text | inferred: search of tests/107 for "inscription": 0 |
| e114 | FW5.14 | PT.15 | kept | dropped at file 10, back by the present text | recorded: results/S89, observation 14 (the drop); tests/107 Part X (the return) |
| e115 | FW5.10, FW5.22 | PT.14, PT.16 | kept | Build and Origin; reconstruction by a learner is construction, relay is not; no theorem that every acquisition is creation | inferred |
| e116 | FW5.21 | PT.24 | kept | recursion and universality | inferred |
| e117 | FW5.13 | PT.31 | kept | no merit predicate; the appraisal relation an import | inferred |
| e118 | FW5.2 | PT.5, PT.4 | kept | an error in the working dependence cannot explain; a relation holds whatever anyone accepts | inferred |
| e119 | FW5.5 | PT.29 | changed | routes without minimality kept; hard to vary gives way to "easy to vary" as a problem of the second kind (rivals conflicting only outside the contract) | recorded: tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md |
| e120 | (none) | PT.9, PT.25 | added | prediction, violation and surprise, and two responses to a violation, selection or construction | recorded: results/S89, observation 13 (file 10, lines 232 to 238) |
| e121 | (none) | PT.13 | added | premises taken as given; the costly gamble of correcting errors with claims one does not contain | recorded: decision S27, the owner's second footnote |
| e122 | (none) | PT.27 | added | a failed answer stays failed | inferred: matches the owner's S20, "the mistake shouldn't be able to creep back in"; the revision that added it is not traced here |
| e123 | (none) | PT.28 | added | rivals and problems: a problem as a conflict no usable argument has decided | recorded: decision S20; tests/Revision 2 - hard to vary restated through rivals and problems |
| e124 | FW5.15, FW5.12, FW5.19 | PT.32 | dropped | the words themselves: information from file 10 on, knowledge at the S95 scrub | recorded: results/S89, observation 8; results/S95 |
| e125 | FW5.3 | PT.6 | changed | physical possibility enters only where a content is instantiated or transformed, and as content a candidate can conflict with | recorded: decisions S25, S26, S27; results/S96 |
| e126 | FW5.25 | PT.31 | changed | the refusal of compression or surprise as beauty gives way to aesthetics as a declared appraisal relation | inferred |
| e127 | FW5.27 | PT.1 | kept | the exact constructions (production, identification, obstruction, constitutive rules) stay as Part VII | inferred: tests/107 Part VII headings |
| e128 | FW5.23, FW5.24 | (none) | dropped | the reconciliation notes addressed to the earlier frameworks are not in the standalone text (decision S31: no provenance) | recorded: decision S31, "remove all reference to provenance, history or versions" |
| e140 | FW5.28 | PT.7 | kept | occurrences and contents | inferred |
| e141 | FW5.29 | PT.33 | kept | equivariance under recoding | inferred |
| e142 | FW5.30 | PT.17 | kept | episodes; the recognized difficulty added | inferred |


## 11. Unsure

- 71 of 132 edges are Claude's reading. Every FW0 edge and every FW5-to-file-10 edge crosses a missing document; a missing document could show a different route (for instance, the selected / constructed split may have come from Q3 or Q4, or from file 20).
- FW0, I2 and FW2 were not read line by line in full; a node that matters for information or error correction may be missing from them (the searches in section 0 make this less likely for those two themes).
- The kinds "changed" and "replaced" are Claude's cut; the difference is whether the later node still answers the same question (changed) or answers it by other means (replaced).
- Theme assignments are Claude's; several nodes belong to two themes (for instance FW3.14 to knowledge and information).
- Whether M3 and E1 are the same addendum is not settled.
