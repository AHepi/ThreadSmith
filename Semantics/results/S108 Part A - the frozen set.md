# S108 Part A: the frozen set, the parts that are hard to vary

*Claude's reading, not the owner's: the owner has not been asked to approve it (decision S52). Written by program, `tools/s108_frozen_set.py`, from the record, for Part A of decision S52; a Claude subagent (Opus 5.5) wrote the program and this page's frame, 28 September 2026. Nothing in the theory's text, its maths or any earlier record was changed. "Model" here means only a small structure the program builds, never a candidate (S43).*

## 1. The criterion, as applied

Decision S52 asks to freeze "all the parts that are hard to vary". Claude's working reading, recorded in S52: the sentences and definitions that readers tried to vary across the rounds and that came through unchanged while the parts around them kept changing (the owner's own approach of S31). Applied to every sentence of the current text (`tests/107 The semantics, standing alone, after round 4.md`, the state after round 4 (S107)) and every definition and encoding of the current formal core, an item is **FROZEN** when both hold:

- **(a) put to the readers or checkers at least once (challenged or tested).** For a sentence, any of: a proposal the S98 ledger places on it before the review rounds, none applied (S100's count); one of the 29 put to both readers in round 1; quoted beside its maths in one of round 2's 17 parts; quoted as the source of a formal claim the program tests; or named by a finding whose line holds no other sentence. For a definition or encoding: put to both readers in round 2 (every definition of round 2's formal core was, challenged or not), or named by a finding of a later round.
- **(b) no round or step changed it.** For a sentence: untouched in substance through the ten versions the ledger follows (S100's test, which leaves out the scrub's word swaps of S95), and its exact words still a sentence of its line in every text after the ledger's: S99 (the text made to stand alone); round 1 (S103); round 2 (S104); the owner's answers step (S41); round 3 (S105); S106 (the written-in test taken out; S47 inside it); round 4 (S107). A sentence changed and later restored (L13's " and criticism") counts as changed. For a definition: its body, without the change marks and invention references, the same in every formal core after round 2's: round 2's reading, its second check and the owner's answers step; round 3 (S105); S106 (with S47); round 4 (S107) and its second check. A mark with no change of the body (a note, "no change", an invention registered) is not a change.
- **Everything else is the MIDDLE.** A sentence whose line alone was named by a finding, on a line holding other sentences, goes to the middle: the record cannot tell whether that sentence was put.
- A sentence and the definitions that formalize it are separate items. A frozen sentence whose definition is in the middle constrains that definition: any variant of it must still be a reading of the frozen words. A frozen definition whose sentence changed stands as the maths the words now point to.

## 2. Counts

| | frozen | middle | all |
|---|---|---|---|
| sentences of the text | 169 | 519 | 688 |
| definitions and encodings of the formal core | 69 | 58 | 127 |
| all items | 238 | 577 | 815 |

By Part of the text (a definition counts in the Part of the lines it formalizes):

| Part | sentences frozen | sentences middle | definitions frozen | definitions middle | middle items |
|---|---|---|---|---|---|
| Part 0 | 5 | 86 | 1 | 1 | 87 |
| Part I | 1 | 18 | 0 | 0 | 18 |
| Part II | 25 | 17 | 11 | 5 | 22 |
| Part III | 10 | 24 | 4 | 3 | 27 |
| Part IV | 19 | 32 | 6 | 6 | 38 |
| Part V | 10 | 31 | 10 | 7 | 38 |
| Part VI | 23 | 43 | 11 | 8 | 51 |
| Part VII | 12 | 24 | 4 | 2 | 26 |
| Part VIII | 3 | 19 | 1 | 0 | 19 |
| Part IX | 6 | 31 | 3 | 9 | 40 |
| Part X | 11 | 30 | 5 | 3 | 33 |
| Part XI | 5 | 17 | 6 | 2 | 19 |
| Part XII | 5 | 22 | 4 | 4 | 26 |
| Part XIII | 6 | 6 | 2 | 2 | 8 |
| Part XIV | 14 | 28 | 0 | 3 | 31 |
| Part XV | 1 | 12 | 0 | 1 | 13 |
| Part XVI | 13 | 79 | 1 | 2 | 81 |

Why the middle sentences are in the middle:

| reason | sentences |
|---|---|
| changed: before the review rounds | 312 |
| unchanged; only its line named by a finding, the line holding other sentences | 77 |
| unchanged, but the record shows it never put to a reader or checker by itself | 53 |
| its words are new since the ledger's latest text: written by round 2 (S104) | 36 |
| its words are new since the ledger's latest text: written by S99 (the text made to stand alone) | 13 |
| its words are new since the ledger's latest text: written by S106 (the written-in test taken out; S47 inside it) | 11 |
| its words are new since the ledger's latest text: written by round 3 (S105) | 9 |
| its words are new since the ledger's latest text: written by the owner's answers step (S41) | 4 |
| its words are new since the ledger's latest text: written by round 1 (S103) | 3 |
| changed: before the review rounds and round 3 | 1 |

Why the middle definitions are in the middle:

| reason | definitions |
|---|---|
| changed in round 2 (S104) | 27 |
| changed in round 2 (S104); changed in round 3 (S105) | 9 |
| changed in round 2 (S104); changed in round 4 (S107) and its second check | 4 |
| changed in round 3 (S105) | 4 |
| changed in S106 (with S47) | 3 |
| new in round 2 (S104) | 2 |
| changed in the owner's answers step (S41) | 2 |
| changed in round 2 (S104) and the owner's answers step (S41) | 2 |
| changed in round 2 (S104) and the owner's answers step (S41); changed in round 3 (S105) | 2 |
| changed in round 2 (S104) and the owner's answers step (S41); changed in round 3 (S105); changed in round 4 (S107) and its second check | 1 |
| new in round 2 (S104) and the owner's answers step (S41); changed in round 4 (S107) and its second check | 1 |
| changed in round 2 (S104); changed in round 3 (S105); changed in round 4 (S107) and its second check | 1 |

## 3. The frozen sentences

Unit ids are the S98 ledger's (line and sentence of the latest text; every text since keeps its lines). "Formal" gives the definitions that quote the sentence (or, marked *line*, that quote its line) and the claims whose source it is.

| id | line | Part | the sentence | formal | why frozen |
|---|---|---|---|---|---|
| L27.s2 | L27 | Part 0 | It defines the classes. | FC110 | unchanged in every version and step; put to both readers in round 1 and kept |
| L41.s4 | L41 | Part 0 | Survival is how the transport got there; fidelity is what it is. | FC79 | unchanged in every version and step; put to both readers in round 1 and kept |
| L47.s2 | L47 | Part 0 | Construction is a separate provenance with a separate trace, and every creative attribution requires it. | FC84 | unchanged in every version and step; put to both readers in round 1 and kept |
| L51.s1 | L51 | Part 0 | **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation. | — | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L57.s1 | L57 | Part 0 | **11. "Kinds exist. A rule is not a cause."** A rule and a cause differ in how they respond to changes: a rule's application chan… | FC10 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 2) |
| L67.s1 | L67 | Part I | **Faithfulness without assessors.** Whether a transport is faithful on a contract is independent of whether anyone tentatively ac… | FC30 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 6) |
| L87.s1 | L87–L89 | Part II | \[ D=(V,(X_v)_{v\in V},J,B,A,L). \] | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L91.s1 | L91 | Part II | \(V\) is a set of ports, each with a nonempty value domain \(X_v\). | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 4) |
| L91.s2 | L91 | Part II | A valuation is an element of \(X_D=\prod_v X_v\). | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L91.s3 | L91 | Part II | \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\). | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L91.s4 | L91 | Part II | \(B\) is a set of boundary conditions. | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L91.s5 | L91 | Part II | \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\). | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L91.s6 | L91 | Part II | For each \(j\), edit \(a\), and boundary \(b\), the interpretation supplies | D1.1 (*line*) | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L93.s1 | L93–L95 | Part II | \[ L_j(a,b)\subseteq\prod_{v\in V_j}X_v . \] | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L99.s1 | L99–L101 | Part II | \[ \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z\|_{V_j}\in L_j(a,b)\}. \tag{O} \] | D1.2; FC01 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L103.s1 | L103 | Part II | A deleted component imposes the full relation on its ports. | D1.3; FC01 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 17) |
| L103.s2 | L103 | Part II | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one. | D2.1; FC01 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 2, 7) |
| L103.s3 | L103 | Part II | A changed rule is a changed component. | D2.1; FC01 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 2, 7) |
| L105.s2 | L105 | Part II | Cyclic constraints are admitted. | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L105.s3 | L105 | Part II | Several solutions remain several. | D1.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L109.s1 | L109 | Part II | No role assignment is supplied. | D2.2; FC02, FC2.new1, FC07, FC11 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 2) |
| L109.s2 | L109 | Part II | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly. | D2.2, D2.4; FC07, FC11 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 2) |
| L109.s3 | L109 | Part II | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\). | D2.3; FC02, FC2.new1, FC07, FC11 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1, 2) |
| L109.s5 | L109 | Part II | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read. | D2.5; FC02 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L113.s1 | L113 | Part II | Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III). | FC11 | unchanged in every version and step; put to both readers in round 1 and kept |
| L113.s2 | L113 | Part II | The **signature** of component \(j\) on \(C\) is | FC11 | unchanged in every version and step; put to both readers in round 1 and kept |
| L115.s1 | L115–L117 | Part II | \[ \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K} \] | D4.1 | unchanged in every version and step; put to both readers in round 1 and kept |
| L124.s1 | L124 | Part II | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring… | D4.6; FC06, FC12 | unchanged in every version and step; put to both readers in round 1 and kept |
| L125.s1 | L125 | Part II | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule. | D4.6; FC12 | unchanged in every version and step; put to both readers in round 1 and kept |
| L127.s2 | L127 | Part II | The semantics never asks whether a component "is" a cause. | D4.6 (*line*); FC14 | unchanged in every version and step; put to both readers in round 1 and kept |
| L127.s3 | L127 | Part II | It asks what its signature is. | D4.6 (*line*); FC14 | unchanged in every version and step; put to both readers in round 1 and kept |
| L137.s1 | L137–L139 | Part III | \[ p=(D,\ C,\ b_0,\ \mathcal Q,\ O_p,\ \rho_p). \] | D3.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 4) |
| L141.s2 | L141 | Part III | The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the basel… | D3.1; FC15, FC22 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3, 4, 6) |
| L143.s1 | L143–L145 | Part III | \[ \operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b). \tag{Q} \] | D3.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 4) |
| L147.s1 | L147 | Part III | \(O_p\) is the set of aims being addressed or protected. | D3.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 4) |
| L147.s2 | L147 | Part III | \(\rho_p\) is the **provenance** of the contract (below). | D3.1 (*line*) | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L151.s2 | L151 | Part III | A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports. | D3.3; FC27.new1 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L155.s6 | L155 | Part III | A claim that an episode *found* a question requires \(\rho_p=\text{constructed}\) for the contract in question, with the trace. | D3.4 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L161.s1 | L161 | Part III | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements. | D3.6; FC106 | unchanged in every version and step; put to both readers in round 1 and kept |
| L161.s2 | L161 | Part III | Its formulation is still an event. | D3.6 (*line*); FC105 | unchanged in every version and step; put to both readers in round 1 and kept |
| L161.s3 | L161 | Part III | Exposing the defect is another question with its own contract. | D3.6 (*line*); FC107 | unchanged in every version and step; put to both readers in round 1 and kept |
| L169.s1 | L169 | Part IV | An **occurrence** is a physically located carrier. | D11.1; FC105 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L169.s2 | L169 | Part IV | A **content** is an organization together with its contract-relative commitments. | D11.1; FC105 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9, 13) |
| L169.s3 | L169 | Part IV | Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs. | D11.1; FC105 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L177.s1 | L177 | Part IV | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are… | D12.6 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 4, 13, 14) |
| L185.s1 | L185–L187 | Part IV | \[ t=(\pi,\tau,\sigma,\lambda) \] | D5.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3, 5) |
| L189.s1 | L189 | Part IV | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assign… | D5.1; FC104 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L189.s2 | L189 | Part IV | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V. | D5.7; FC104 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L195.s1 | L195 | Part IV | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a fin… | D12.1; FC12.new1, FC77 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L195.s5 | L195 | Part IV | Write \(\operatorname{Sel}(t;\mathcal T,\mu,H)\). | D12.1 (*line*); FC12.new1, FC77 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L199.s1 | L199 | Part IV | **Declared.** Neither of the above. | D12.3 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L199.s3 | L199 | Part IV | Write \(\operatorname{Dec}(t)\). | D12.3 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L201.s2 | L201 | Part IV | Construction may operate on selected material. | FC78 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L201.s3 | L201 | Part IV | Selection may continue to operate beneath construction. | FC78 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L207.s1 | L207–L209 | Part IV | \[ \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Se… | D12.5 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L217.s2 | L217 | Part IV | For an edit–boundary pair \((a,b)\in C\) actually occurring: | D11.5; FC35 | unchanged in every version and step; put to both readers in round 1 and kept |
| L219.s1 | L219 | Part IV | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\); | D12.7; FC20 | unchanged in every version and step; put to both readers in round 1 and kept |
| L225.s1 | L225 | Part IV | Two responses to a violation are distinguished. | D12.8 (*line*); FC82, FC83 | unchanged in every version and step; put to both readers in round 1 and kept |
| L225.s3 | L225 | Part IV | A **construction response** introduces a new organization or a new transport with a construction trace. | D12.8; FC82 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13, 14) |
| L225.s4 | L225 | Part IV | Only the second can be originative under Part X. | D12.8 (*line*); FC83 | unchanged in every version and step; put to both readers in round 1 and kept |
| L241.s1 | L241–L243 | Part V | \[ \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1).… | D5.5; FC15 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3, 5, 6) |
| L245.s1 | L245 | Part V | (F1) prevents an assembled match from hiding a decomposition in error. | D5.7 (*line*); FC19, FC23.new5 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L245.s2 | L245 | Part V | (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint. | D5.7 (*line*); FC19 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L245.s3 | L245 | Part V | Together they are fidelity at every level the contract reaches. | D5.7; FC104 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L247.s1 | L247 | Part V | **Question fidelity.** For every \((a,b)\in C\), | D5.7; FC104 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5) |
| L249.s1 | L249–L251 | Part V | \[ \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A} \] | D5.6; FC20 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5, 6) |
| L253.s1 | L253 | Part V | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one. | D3.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 4) |
| L265.s2 | L265 | Part V | None inspects a label. | FC33 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 6) |
| L281.s3 | L281 | Part V | Where \(C\) contains no such change, the two are one kind on \(C\) by (K), and the condition would be asserting a distinction tha… | FC18 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L281.s4 | L281 | Part V | There is no third case. | FC18 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3) |
| L287.s1 | L287 | Part VI | Fix \(\mathcal E\) and a declared restriction operation. | D7.1 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L289.s1 | L289–L291 | Part VI | \[ \mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E\|W,p)\}. \tag{S} \] | D7.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L293.s1 | L293 | Part VI | No upward closure and no minimal member are assumed. | D7.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L295.s1 | L295–L297 | Part VI | \[ \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B} \] | D7.3 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L299.s1 | L299 | Part VI | A block may be critical while no singleton in it is. | FC42 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L301.s1 | L301–L303 | Part VI | \[ \operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D}… | D7.4 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L307.s1 | L307 | Part VI | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\): each is contributory, neither indispensable. | FC38 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L309.s1 | L309 | Part VI | **Interference.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails (E) although a subset meets it. | FC39 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L311.s2 | L311 | Part VI | (B) records the collective contribution. | FC40 | unchanged in every version and step; put to both readers in round 1 and kept |
| L315.s1 | L315 | Part VI | **Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(… | D8.3; FC44, FC45, FC52, FC53, FC54 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L315.s4 | L315 | Part VI | A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or n… | D8.3, D8.5; FC52 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L315.s5 | L315 | Part VI | Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that take… | D8.6; FC45 | unchanged in every version and step; challenged before the review rounds: 4 proposal(s) placed on it by the ledger, none applied |
| L315.s7 | L315 | Part VI | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out. | D9.8; FC44, FC45, FC52, FC53, FC54 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L315.s8 | L315 | Part VI | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody… | D8.3; FC44, FC45, FC52, FC53, FC54 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L315.s10 | L315 | Part VI | **Conflict with a claim.** A candidate can conflict with a claim as well as with a rival. | D8.1, D8.3, D8.4, D8.5, D8.6, D8.new1, D9.8, D10.5 (*line*); FC44, FC45, FC52, FC53, FC54 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L315.s17 | L315 | Part VI | The conflict does not by itself say which to drop, the candidate, \(\chi\) or another premise of the argument: which one the pers… | D8.1, D8.3, D8.4, D8.5, D8.6, D8.new1, D9.8, D10.5 (*line*); FC44, FC45, FC52, FC53, FC54 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L317.s1 | L317 | Part VI | **Problems.** Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**: a conflict… | D10.1; FC43, FC46, FC47, FC48, FC49, FC50, FC51, FC55 … | unchanged in every version and step; challenged before the review rounds: 4 proposal(s) placed on it by the ledger, none applied |
| L317.s2 | L317 | Part VI | It is of one of two kinds. | D10.1, D10.2, D10.3, D10.4, D10.6 (*line*); FC43, FC46, FC47, FC48, FC49, FC50, FC51, FC55 … | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L317.s3 | L317 | Part VI | (i) The rivals conflict at some \((a,b)\in C\). | D10.2; FC46 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L317.s6 | L317 | Part VI | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict. | D10.2; FC48, FC49 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L317.s12 | L317 | Part VI | A criticism that a candidate is easy to vary must supply such a rival (Part IX). | D10.1, D10.2, D10.3, D10.4, D10.6 (*line*); FC43, FC46, FC47, FC48, FC49, FC50, FC51, FC55 … | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L317.s15 | L317 | Part VI | A contract narrowed to leave out the pairs at which two rivals conflict also makes a different question; it solves nothing on \(p… | D10.1, D10.2, D10.3, D10.4, D10.6 (*line*); FC50 | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L317.s17 | L317 | Part VI | A problem that a system represents can be a recognized difficulty (Part X), as when choosing one of two rivals meets a claimed ai… | D10.1, D10.2, D10.3, D10.4, D10.6 (*line*); FC43, FC46, FC47, FC48, FC49, FC50, FC51, FC55 … | unchanged in every version and step; challenged before the review rounds: 3 proposal(s) placed on it by the ledger, none applied |
| L325.s3 | L325 | Part VII | An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged. | E1 (*line*); FC07 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 2) |
| L325.s4 | L325 | Part VII | The forward organization is faithful under this contract. | E1 (*line*); FC26 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 7) |
| L329.s3 | L329 | Part VII | The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land\|f[Z_y]\|=1\). | E2; FC57, FC58 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L335.s1 | L335 | Part VII | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different inv… | E4; FC61 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L335.s2 | L335 | Part VII | (O1) Equal values do not suffice for reachability. | E4 (*line*); FC61 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L343.s1 | L343 | Part VII | Question: why is every odd-order real skew-symmetric matrix singular? | E6 (*line*); FC63 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L343.s2 | L343 | Part VII | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed. | E6; FC63 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L343.s3 | L343 | Part VII | The full Leibniz expansion with skewness substituted meets (F1) and (F2): every intermediate product is a determinant suborganiza… | E6 (*line*); FC63 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5, 8) |
| L343.s8 | L343 | Part VII | The expansion is an account. | E6 (*line*); FC63 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 8) |
| L347.s1 | L347 | Part VII | A rule relation \(C_r\subseteq Z\times S\) answers "which status under this rule?" by its fibre. | D4.6 (*line*); FC09 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L347.s2 | L347 | Part VII | Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\). | D4.6; FC09 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L347.s3 | L347 | Part VII | Whether the rule governs a practice, and whether it should, are separate questions with separate contracts. | D4.6 (*line*); FC09 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L361.s2 | L361 | Part VIII | Composition of relations preserves both directions when intermediate scopes agree. | FC65 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5) |
| L369.s1 | L369 | Part VIII | **A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). | FC68 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 12) |
| L369.s2 | L369 | Part VIII | By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an accoun… | FC68 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L375.s2 | L375 | Part IX | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose com… | D11.4; FC75 | unchanged in every version and step; put to both readers in round 1 and kept |
| L383.s1 | L383 | Part IX | A criticism occurrence can exist when (K1) fails. | D9.10 (*line*); FC74 | unchanged in every version and step; put to both readers in round 1 and kept |
| L385.s1 | L385 | Part IX | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization p… | D9.11; FC76 | unchanged in every version and step; put to both readers in round 1 and kept |
| L389.s1 | L389–L391 | Part IX | \[ \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\o… | D9.6; FC69 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L397.s5 | L397 | Part IX | For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\). | D9.7; FC56, FC72, FC73 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 12) |
| L397.s13 | L397 | Part IX | A system can be designed that must hold the whole explanation of a premise before using it; that is a detail outside the process… | D9.1, D9.7, D9.8 (*line*); FC56, FC72, FC73 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L403.s2 | L403 | Part X | The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect. | D13.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L403.s3 | L403 | Part X | A system may understand a theory in error. | D13.1 (*line*) | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L407.s1 | L407 | Part X | An inexplicit representation is not an absent one. | — | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L409.s5 | L409 | Part X | A construction trace may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it:… | — | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L409.s6 | L409 | Part X | Use does not by itself construct: received content used as it was received keeps its inherited provenance. | — | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L411.s1 | L411 | Part X | Construction is not selection. | — | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L411.s2 | L411 | Part X | A selected transport has no represented target in its history; a constructed one does. | — | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 13) |
| L415.s1 | L415–L417 | Part X | \[ \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N} \] | D13.5; FC85 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L425.s1 | L425 | Part X | The content \(c\) may be an organization, a transport, or a contract. | — | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L425.s2 | L425 | Part X | When it is a contract, the originative act is the finding of a question. | — | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L427.s3 | L427 | Part X | Contribution of content and ownership of a process are different attributions: a routine written outside the boundary and run ins… | D13.7 (*line*) | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L437.s1 | L437–L439 | Part XI | \[ \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow… | D14.2; FC86 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L441.s2 | L441 | Part XI | In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to… | D14.1; FC86, FC87, FC88 | unchanged in every version and step; challenged before the review rounds: 2 proposal(s) placed on it by the ledger, none applied |
| L441.s4 | L441 | Part XI | Losses outside \(P\) must be exposed. | D14.4; FC88 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L443.s3 | L443 | Part XI | With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims, | D14.5; FC89 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L453.s1 | L453 | Part XI | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. | D14.6 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15) |
| L465.s1 | L465–L467 | Part XII | \[ \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi… | D15.2; FC91 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L469.s1 | L469 | Part XII | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task. | D15.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L475.s1 | L475 | Part XII | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physi… | D15.5 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L477.s1 | L477 | Part XII | **Achievement.** \(\operatorname{CanAdv}(\xi,p;\chi,J_p,C_I)\): for each starting configuration in the independently specified \(… | D15.6 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L479.s4 | L479 | Part XII | (CT3, CT4) Capability at a given tolerance does not imply possibility at every tolerance. | D15.7 (*line*); FC93 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L487.s1 | L487 | Part XIII | **Scrutinizability.** An aspect \(d\) of a system's practice is scrutinizable at \(\xi\) when there is an owned, admitted continu… | D16.1 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L491.s1 | L491–L493 | Part XIII | \[ \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC}… | D16.2 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L495.s1 | L495 | Part XIII | **Barriers.** An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enab… | D16.3 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L499.s1 | L499–L501 | Part XIII | \[ \operatorname{UU}\iff\forall c\in\mathfrak E_\Theta\ \exists\chi,\ \operatorname{Enable}(s,U_c,\chi)\land\operatorname{Can}(\x… | D16.4 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L502.s1 | L502–L504 | Part XIII | \[ \operatorname{UC}\iff\forall p\in\mathfrak P^{\mathrm{adv}}_\Theta\ \exists\chi,\ \operatorname{Enable}(s,A_p,\chi)\land\opera… | D16.4 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L509.s1 | L509 | Part XIII | Recursion does not entail universality; a historical extension leaves it open; a finite performance record does not suffice for i… | FC94 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L517.s1 | L517 | Part XIV | 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation,… | — | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L520.s3 | L520 | Part XIV | Kinds, from signatures (K). | FC31, FC32, FC104 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5, 6) |
| L520.s4 | L520 | Part XIV | The respect of a question, from its query (Part III). | FC31, FC32, FC104 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5, 6) |
| L520.s5 | L520 | Part XIV | Representation, from fidelity and provenance (R). | FC31, FC32, FC104 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5, 6) |
| L526.s2 | L526 | Part XIV | (K) depends on (O) and a contract. | D18.1 (*line*); FC32, FC98 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L526.s3 | L526 | Part XIV | (F1), (F2), (A) depend on (O), (Q), (K). | D18.1 (*line*); FC32 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L526.s6 | L526 | Part XIV | (R) depends on (F1)–(F2) and physical provenance. | D18.1 (*line*); FC32, FC98 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L526.s9 | L526 | Part XIV | Deploy depends on (R) and (CT1). | D18.1 (*line*); FC32, FC98 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L526.s10 | L526 | Part XIV | Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part… | D18.1 (*line*); FC32, FC98 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L526.s14 | L526 | Part XIV | (RC), (U1)–(U3) depend on all of the above. | D18.1 (*line*); FC32, FC98 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L528.s1 | L528 | Part XIV | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherev… | D16.5; FC110 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L528.s2 | L528 | Part XIV | The creative-episode class: base interpretations with an instance of (G) connected to a critical episode. | D16.5; FC110 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L528.s3 | L528 | Part XIV | The explanation-creation class: an instance of (EX). | D16.5; FC110 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L528.s4 | L528 | Part XIV | The recursive class: (RC). | D16.5; FC110 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 16) |
| L546.s1 | L546 | Part XV | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their st… | FC92, FC109 | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L556.s3 | L556 | Part XVI | (F1) equates the third coordinates pointwise. ∎ | FC17 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3) |
| L558.s3 | L558 | Part XVI | The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case. | FC18 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 3) |
| L562.s2 | L562 | Part XVI | (i) Their answer profiles coincide on \(C\). | FC96 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 5) |
| L574.s2 | L574 | Part XVI | The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\). | FC80 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 1) |
| L598.s1 | L598 | Part XVI | *Why this and not its denial.* | — | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L604.s1 | L604 | Part XVI | **Claim.** An assessment event with contract \(C\) and an episode in which \(C\) is replaced by \(C'\) with a construction trace… | FC105 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 9) |
| L616.s1 | L616 | Part XVI | **Claim.** If \(M_0,M_1\) have the same input–output projection and differ on an account claim, no function of the projection agr… | FC101 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |
| L616.s3 | L616 | Part XVI | Equal inputs to a function give equal outputs. ∎ Parallel and priority wiring are an instance. | FC101 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |
| L622.s2 | L622 | Part XVI | \(S_0\) predicts occupancy from recent occupancy. | — | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 15, 17) |
| L624.s3 | L624 | Part XVI | \(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with it… | FC102 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |
| L624.s4 | L624 | Part XVI | This is surprise (Argument 4). | FC102 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |
| L626.s5 | L626 | Part XVI | Under (F1), \(t_1\) is faithful on the extended contract. | FC102 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |
| L630.s2 | L630 | Part XVI | On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things… | FC103 | unchanged in every version and step; quoted beside its maths to both readers in round 2 (part 17) |

## 4. The frozen definitions and encodings

| id | section of the core | lines it formalizes | Part | why frozen |
|---|---|---|---|---|
| D0.1 | §0 Conventions and the frame | L31, L522 | Part 0 | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D1.1 | §1 Organizations (O) | L88, L91, L94, L105 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D1.2 | §1 Organizations (O) | L100 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D1.3 | §1 Organizations (O) | L103, L339 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D2.2 | §2 Setting edits and roles | L109 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D2.3 | §2 Setting edits and roles | L109 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D2.5 | §2 Setting edits and roles | L109 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D3.1 | §3 Questions and contracts | L138, L141, L147 | Part III | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D3.2 | §3 Questions and contracts | L144, L253 | Part III | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D3.5 | §3 Questions and contracts | L159 | Part III | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D3.7 | §3 Questions and contracts | L151 | Part III | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D4.1 | §4 Signatures, kinds and families | L116 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D4.2 | §4 Signatures, kinds and families | L119 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D4.3 | §4 Signatures, kinds and families | L119 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D4.4 | §4 Signatures, kinds and families | L119 | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D4.5 | §4 Signatures, kinds and families | — | Part II | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.1 | §5 Transports and fidelity | L186, L189 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.2 | §5 Transports and fidelity | L233 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.3 | §5 Transports and fidelity | L231 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.4 | §5 Transports and fidelity | L236 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.5 | §5 Transports and fidelity | L242 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D5.6 | §5 Transports and fidelity | L250 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D6.1 | §6 Dependence, non-vacuity, Account [S1… | — | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D6.2 | §6 Dependence, non-vacuity, Account [S1… | L255 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged; its marks are notes only, the body unchanged |
| D6.6 | §6 Dependence, non-vacuity, Account [S1… | L257 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D6.10 | §6 Dependence, non-vacuity, Account [S1… | L269 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D7.1 | §7 Routes: (S), (B), (D) | L231, L287 | Part V | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D7.2 | §7 Routes: (S), (B), (D) | L290, L293 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D7.3 | §7 Routes: (S), (B), (D) | L296 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D7.5 | §7 Routes: (S), (B), (D) | L305 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D7.6 | §7 Routes: (S), (B), (D) | L313 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D8.1 | §8 Conflict, rivals, conflict with a cl… | L315 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D8.4 | §8 Conflict, rivals, conflict with a cl… | L315 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D8.6 | §8 Conflict, rivals, conflict with a cl… | L315 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D9.3 | §9 Arguments, usability, ruling out, be… | L387, L393 | Part IX | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D9.5 | §9 Arguments, usability, ruling out, be… | — | Part IX | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D9.11 | §9 Arguments, usability, ruling out, be… | L385 | Part IX | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D10.1 | §10 Problems and easy to vary | L317 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D10.2 | §10 Problems and easy to vary | L317 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D10.4 | §10 Problems and easy to vary | L317 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D10.5 | §10 Problems and easy to vary | L315 | Part VI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D11.1 | §11 Occurrences, events, contents, hist… | L169 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D11.5 | §11 Occurrences, events, contents, hist… | L217 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D12.4 | §12 Provenance, representation, predict… | L211, L405 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D12.5 | §12 Provenance, representation, predict… | L205, L208 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D12.6 | §12 Provenance, representation, predict… | L175, L177 | Part IV | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D13.1 | §13 Deploy, Build, New, Origin, ownersh… | L403 | Part X | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D13.2 | §13 Deploy, Build, New, Origin, ownersh… | — | Part X | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D13.4 | §13 Deploy, Build, New, Origin, ownersh… | L413 | Part X | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D13.5 | §13 Deploy, Build, New, Origin, ownersh… | L416 | Part X | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D13.6 | §13 Deploy, Build, New, Origin, ownersh… | L422 | Part X | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D14.2 | §14 Repair, created explanation, apprai… | L438 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D14.3 | §14 Repair, created explanation, apprai… | L441 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D14.4 | §14 Repair, created explanation, apprai… | L441 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| D14.5 | §14 Repair, created explanation, apprai… | L443 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D14.6 | §14 Repair, created explanation, apprai… | L453 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D14.8 | §14 Repair, created explanation, apprai… | L455 | Part XI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D15.3 | §15 The physical module | L471 | Part XII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged; its marks are notes only, the body unchanged |
| D15.4 | §15 The physical module | L473 | Part XII | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D15.6 | §15 The physical module | L477 | Part XII | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D15.7 | §15 The physical module | L479 | Part XII | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| D16.1 | §16 Recursion, universality, classes | L487 | Part XIII | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |
| D16.2 | §16 Recursion, universality, classes | L492 | Part XIII | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged |
| E3 | §17 The text's exact constructions, enc… | — | Part VII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| E4 | §17 The text's exact constructions, enc… | L335 | Part VII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| E5 | §17 The text's exact constructions, enc… | — | Part VII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| E6 | §17 The text's exact constructions, enc… | L343 | Part VII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| E7 | §17 The text's exact constructions, enc… | L353, L358, L363 | Part VIII | unchanged since round 2 put it to the readers; put to both readers in round 2, not challenged |
| E8 | §17 The text's exact constructions, enc… | L590 | Part XVI | unchanged since round 2 put it to the readers; put to both readers in round 2, challenged; its marks are notes only, the body unchanged |

## 5. The middle definitions and encodings

| id | lines | Part | why middle |
|---|---|---|---|
| D0.2 | — | Part 0 | changed in round 2 (S104) and the owner's answers step (S41); changed in round 3 (S105); changed in round 4 (S107) and its second check |
| D1.4 | — | Part II | changed in round 2 (S104) |
| D2.1 | L103, L119 | Part II | changed in round 2 (S104) |
| D2.4 | L109 | Part II | changed in round 2 (S104) |
| D2.6 | — | Part II | new in round 2 (S104) |
| D3.3 | L151 | Part III | changed in round 2 (S104); changed in round 3 (S105) |
| D3.4 | L155 | Part III | changed in round 2 (S104) |
| D3.6 | L161, L367 | Part III | changed in round 2 (S104) |
| D4.6 | L123, L124, L125, L127, L347 | Part II | changed in round 2 (S104); changed in round 3 (S105) |
| D5.7 | L189, L245, L247 | Part V | changed in round 2 (S104); changed in round 3 (S105) |
| D6.3 | L255 | Part V | changed in round 2 (S104); changed in round 4 (S107) and its second check |
| D6.4 | L255 | Part V | changed in the owner's answers step (S41) |
| D6.5 | — | Part V | changed in S106 (with S47) |
| D6.7 | L262 | Part V | changed in S106 (with S47) |
| D6.8 | L231 | Part V | changed in S106 (with S47) |
| D6.9 | L257 | Part V | changed in round 2 (S104) |
| D7.4 | L302 | Part VI | changed in round 2 (S104); changed in round 4 (S107) and its second check |
| D8.2 | — | Part VI | changed in round 2 (S104) |
| D8.new1 | L315 | Part VI | new in round 2 (S104) |
| D8.3 | L315 | Part VI | changed in round 2 (S104) |
| D8.5 | L315 | Part VI | changed in round 2 (S104) |
| D9.1 | L397 | Part IX | changed in round 2 (S104) |
| D9.2 | — | Part IX | changed in round 2 (S104) and the owner's answers step (S41) |
| D9.4 | — | Part IX | changed in round 2 (S104) |
| D9.6 | L390 | Part IX | changed in the owner's answers step (S41) |
| D9.7 | L397 | Part IX | changed in round 2 (S104) and the owner's answers step (S41) |
| D9.8 | L315, L397 | Part VI | changed in round 2 (S104) |
| D9.9 | L395 | Part IX | changed in round 2 (S104) |
| D9.10 | L377, L380, L383 | Part IX | changed in round 2 (S104); changed in round 4 (S107) and its second check |
| D10.3 | L317 | Part VI | changed in round 2 (S104) |
| D10.6 | L317 | Part VI | changed in round 2 (S104) |
| D11.2 | — | Part IV | changed in round 3 (S105) |
| D11.3 | L375 | Part IX | changed in round 2 (S104); changed in round 3 (S105) |
| D11.4 | L375 | Part IX | changed in round 2 (S104) |
| D12.1 | L193, L195 | Part IV | changed in round 2 (S104); changed in round 3 (S105) |
| D12.2 | L197 | Part IV | changed in round 2 (S104) and the owner's answers step (S41); changed in round 3 (S105) |
| D12.3 | L199 | Part IV | changed in round 2 (S104); changed in round 3 (S105) |
| D12.7 | L219, L220, L221 | Part IV | changed in round 2 (S104); changed in round 3 (S105) |
| D12.8 | L225 | Part IV | changed in round 2 (S104) |
| D12.9 | L572 | Part XVI | changed in round 3 (S105) |
| D13.3 | L405 | Part X | changed in round 2 (S104); changed in round 3 (S105) |
| D13.7 | L427 | Part X | changed in round 2 (S104) |
| D13.8 | L429 | Part X | changed in round 2 (S104) and the owner's answers step (S41); changed in round 3 (S105) |
| D14.1 | L435, L441 | Part XI | changed in round 2 (S104) |
| D14.7 | L447, L448, L449 | Part XI | changed in round 3 (S105) |
| D15.1 | L461 | Part XII | changed in round 2 (S104) |
| D15.2 | L466, L469 | Part XII | changed in round 2 (S104) |
| D15.5 | L475 | Part XII | changed in round 2 (S104) |
| D15.8 | L481 | Part XII | changed in round 3 (S105) |
| D16.3 | L495 | Part XIII | changed in round 2 (S104) |
| D16.4 | L500, L503, L506 | Part XIII | changed in round 2 (S104); changed in round 3 (S105) |
| D16.5 | L528 | Part XIV | changed in round 2 (S104) |
| D16.XV | — | Part XV | new in round 2 (S104) and the owner's answers step (S41); changed in round 4 (S107) and its second check |
| E1 | L325 | Part VII | changed in round 2 (S104); changed in round 4 (S107) and its second check |
| E2 | L329 | Part VII | changed in round 2 (S104) |
| E9 | L620 | Part XVI | changed in round 2 (S104) |
| D18.1 | L526 | Part XIV | changed in round 2 (S104); changed in round 3 (S105); changed in round 4 (S107) and its second check |
| D18.2 | — | Part XIV | changed in round 2 (S104) |

The 519 middle sentences, each with its reason, are in the `.json` beside this page (`sentences`, `status` "MIDDLE").

## 6. The strong candidates of S100 and S101, now

| unit | S100 list | now | reason |
|---|---|---|---|
| L27.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L41.s4 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L47.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L51.s1 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L113.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L113.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L115.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L123.s1 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L123 now is in the middle |
| L124.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L125.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L127.s1 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L127 now is in the middle |
| L127.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L127.s3 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L161.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L161.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L161.s3 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L217.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L219.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L220.s1 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L220 now is in the middle |
| L225.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L225.s4 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L255.s1 | challenged and kept | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L255 now is in the middle |
| L273.s1 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L273 now is in the middle |
| L311.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L375.s2 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L383.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L385.s1 | never challenged | FROZEN | unchanged in every version and step; put to both readers in round 1 and kept |
| L389.s1 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L393.s4 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L393 now is in the middle |
| L437.s1 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L441.s4 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L443.s2 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L443 now is in the middle |
| L471.s2 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L471 now is in the middle |
| L517.s1 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |
| L520.s7 | never challenged | MIDDLE (its words are gone) | changed by a later round or step; the sentence at L520 now is in the middle |
| L546.s1 | challenged and kept | FROZEN | unchanged in every version and step; challenged before the review rounds: 1 proposal(s) placed on it by the ledger, none applied |

## 7. What the program cannot tell, and choices it made

- Before the review rounds, "challenged" and "changed" are S100's counts from the S98 ledger: a record placed on a whole paragraph counts on each of its sentences, so a sentence may count as challenged by a proposal aimed at its neighbour. The scrub's word swaps (S95) are not counted as changes, as S100 did not count them; the changes of S99 (references to provenance, history and versions removed) are counted.
- A sentence is followed by its exact words on its line: a change of one character makes it changed. A sentence restored after a change counts as changed.
- Quotations are matched to sentences by text (a fragment inside the sentence, or a common stretch of at least 30 characters, or four fifths of the shorter); a loose quotation could reach a neighbour.
- Findings of rounds 2 to 4 name lines, not sentences; they count for (a) only on a line holding one sentence.
- A definition's history is read from its body in each formal core; the core after round 2 was written by round 2's reading, its second check and the owner's answers step, and which of them changed a definition is read from its marks.
- Silence is not agreement: a frozen item held under the attempts made; nothing shows it holds beyond them (S28).
- What hard to vary covers in general stays parked (S33, S34); this set is a working reading for Part A only.

## 8. Inputs

| file | md5 |
|---|---|
| `tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md` | ebca15a047f686b15d5f5766b69825c9 |
| `tests/99 The semantics, standing alone.md` | 74f4a4c7619345747f4fa976ddac9548 |
| `tests/103 The semantics, standing alone, after round 1.md` | f31ebb1f050783f1a84f6136cec20fcd |
| `tests/104 The semantics, standing alone, after round 2.md` | 735ec1e8256cc6a251715a031944ea65 |
| `tests/104 The semantics, standing alone, after round 2, with the owner's answers.md` | bc14045aae3139df710d8339a9c1c81b |
| `tests/105 The semantics, standing alone, after round 3.md` | da9a30cd052d46f2a5ead259cea97d3c |
| `tests/106 The semantics, standing alone, without the written-in test.md` | c7af964c329ab7959243405d394e6574 |
| `tests/107 The semantics, standing alone, after round 4.md` | c7af964c329ab7959243405d394e6574 |
| `results/S104 Round 2 - maths/formal core.md` | 3473b6d486a51a0630e24e0bb22d837b |
| `results/S104 Round 2 - maths after the reading/formal core, after round 2.md` | 96798d3bf3b60da8d67175c39462ef4a |
| `results/S105 Round 3 - maths after the reading/formal core, after round 3.md` | 9202ad317a5987481d4374cf5d718d8b |
| `results/S106 The written-in test taken out/formal core, after S106.md` | 40d7c80ec78574794962fece34a4cb51 |
| `results/S107 Round 4 - maths after the reading/formal core, after round 4.md` | d6e6ec62acbc6ef763e07b7cd7b29540 |
| `results/S107 Round 4 - maths after the reading/formal claims, after round 4.json` | 3d9864f1be8ec8b88914dc2800af4288 |
| `results/S100 Strong candidates and the most altered sections - data.csv` | aafca7e15b1515e58161da95227ac354 |
| `results/S101 What the tested strong candidates depend on - graph.json` | ceb857cb76ebed0d464b1724398f2fe2 |
| `results/S98 Ledger of edits and recommendations/group/sentence index of the latest text.jsonl` | fdaf069a0c1d71be4e17b38d2f6bce82 |
| `results/S104 Round 2 - tabulation of the replies, before any ruling.json` | b641469887d16397a80858d4f367a55f |
| `results/S105 Round 3 - tabulation of the replies, before any ruling.md` | 8e72ea75787a152c245d4d010c956187 |
| `results/S107 Round 4 - tabulation of the replies, before any ruling.md` | 18f6af15a2e99b23d8def45cf17965ea |
| `tests/S104 Round 2 - the maths against the words - part 01, Organizations, setting edits and roles.md` | a4e1c1fc5b9ab69c866e13a1040356a2 |
| `tests/S104 Round 2 - the maths against the words - part 02, The three families of signatures.md` | 31f2a7101f50c0a6e449a82ea08317ff |
| `tests/S104 Round 2 - the maths against the words - part 03, Kinds, and kinds read through a transport.md` | 5d454b5a26af5953dd7c71982890693c |
| `tests/S104 Round 2 - the maths against the words - part 04, Questions and contracts.md` | 8cbbf5bb17ab39d4ed8506f31eb86120 |
| `tests/S104 Round 2 - the maths against the words - part 05, Transports, fidelity and the transport results.md` | 6d92d5e038a758f877bf2775de649181 |
| `tests/S104 Round 2 - the maths against the words - part 06, Account - non-circular dependence and non-vacuity.md` | 472d75b5914972322c9c06c680b9cd82 |
| `tests/S104 Round 2 - the maths against the words - part 07, What (E) excludes - relabelings, tables, and the pole and its shadow.md` | d198d1cdd6227d82928b57f77ff78aca |
| `tests/S104 Round 2 - the maths against the words - part 08, Identification, obstruction, removed structure, skew-symmetric matrices.md` | 04296f0c299ee2a903480f95d769e6ce |
| `tests/S104 Round 2 - the maths against the words - part 09, Routes, and active routes in a history.md` | 36c7f4900174be0a291b66657a962340 |
| `tests/S104 Round 2 - the maths against the words - part 10, Conflict and rivals.md` | 87002509c6ac194e88ea2cea5f060142 |
| `tests/S104 Round 2 - the maths against the words - part 11, Problems, tests and easy to vary.md` | f80196f155c19f42d3b413124cf0108f |
| `tests/S104 Round 2 - the maths against the words - part 12, Arguments, criticism and reason use.md` | 3ccfd162f7e0a79e6554940391b94c36 |
| `tests/S104 Round 2 - the maths against the words - part 13, Selection, construction and representation.md` | 4481c7735ea9926322bd9df2d87cf3d6 |
| `tests/S104 Round 2 - the maths against the words - part 14, Prediction, violation, surprise and the two responses.md` | 1a60df61f2e227c737ea0b6544d40f43 |
| `tests/S104 Round 2 - the maths against the words - part 15, Construction, newness, origin, repair and created explanation.md` | a4af47eaf38e47d14b9ffabd8cf21466 |
| `tests/S104 Round 2 - the maths against the words - part 16, The physical module, recursion, universality and the class collected.md` | 4c484e49183e928707f272e7a4672af3 |
| `tests/S104 Round 2 - the maths against the words - part 17, The Arguments of Part XVI, and what would rule the class out.md` | 4e64265cbd3b689f54b63606a5def456 |

