# W19 and W20: Mimo's holes M6 and M3, checked adversarially

*Moved into the repository on 23 September 2026 from the session scratchpad, where it was `revision2/checks/W19 W20 Mimo holes.md`; this paragraph was added and one path changed, to the candidate case book's committed copy. The second of Claude's three checks of the defects later put to Atria and Mimo in S88, written on 23 September 2026 by a Claude subagent for the revision-2 worklist (items W19 and W20). It checks, adversarially, two holes Mimo reported in the S81 trial: M6, Derivation 2's claim about components, and M3, the non-circular dependence condition. They underpin S88: the S88 brief (`tests/S88 Cross-examination - three defects in the theory's own defeat list.md`) states the three defects and the theory's defence that these checks set out, and the S88 reading (`results/S88 Reading of Atria's reply - the three defects.md`) read them under their scratchpad names, `revision2/checks/W31 T2 bound.md`, `W19 W20 Mimo holes.md` and `defence of T2 and Derivation 2.md`, which are 01, 02 and 03 in this folder.*

23 September 2026. Written by Claude (a subagent) for the revision-2 worklist. This is a check, not a decision. The repository was read only; nothing in it was edited.

**Read.**
- Theory files: file 10 and file 11 in full. File 00: lines 90–240, plus the lines cited below.
- The S81 trial (`results/S81 Trial - DeepSeek as a third auditor, three blind readings compared.md`) and project story entry S83 (story L94).
- Worklist items W19 and W20, with the items and the conflicts list that name them.
- From the S81 case book: O1–O10, O22–O24, O33–O36 and O45–O48. From the case-book provenance file: the table only, for the header annotation each case was written under.
- Test 28 (round 4), the source of O5.
- From `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`: N1, N3, N16, N17, N23 and N25.

**Not opened.**
- Any S81 1C, 1K, 2a or 2b return, reasoning file, receipt, sample or table.
- The effort-controls folder and the S81 determination folder.
- Mimo's own return. Mimo's holes are taken from the trial file's statement of them.

**Conventions.** "F10 L270" means file 10, line 270. F11 is file 11. "00:210" is file 00, line 210. S1, S2 and S3 name the three sentences of the non-circular dependence condition (§2.1).

---

## Verdicts

| hole | verdict | decisive lines | counter-instance |
|---|---|---|---|
| **W19 / M6**, Derivation 2 | **CONFIRMED.** The claim is false as stated, not only unproved. Under Part XV's own list it is a defeater of the class. No fixed O-verdict rests on the false half, but the unrestricted claim pulls against O45, O46, O36 and N17. | Claim F10 L561 = F11 L554. Proof F10 L563 = F11 L556. Derivation 1 F10 L553–555 = F11 L546–548. Defeat list F10 L543 = F11 L538. | Two faithful decompositions of one chain, one fine and one coarse. Both satisfy (F1), (F2) and (A) on the same \(C\). Their answer profiles coincide, and no component of one pairs with a component of the other (§1.4). |
| **W20 / M3**, non-circular dependence | **CONFIRMED, in part.** (a) The missing \(\tau,\sigma\) is a drafting fault that the text's own conventions fill. As a misfire it is REFUTED. (b) \(\Gamma\) is never typed, and "the other boundary conditions" presupposes a type. That defect is CONFIRMED, with a live verdict risk. On the one reading where every sentence of Part V agrees, O2, O5 and O33 keep their fixed verdicts in both files. On the reading Part VI invites, O33 and O7 flip, and O5 flips on an ordinary production contract. O2 flips on no reading, because S2 decides it and S3 does not. | S3 at F10 L270 = F11 L257. \(\Gamma\) introduced untyped at F10 L246 = F11 L233. "Named background" at F10 L304 = F11 L289. Replacement rule at F10 L120 = F11 L105. The non-vacuity (NV) relabelings sentence at F10 L272 = F11 L259. | Part VII's pole and shadow, O7's salt and O33's joint knobs, taking \(\Gamma\) to be mechanism only (§2.5). Also: under the worklist's proposed retype, a relabelings-only contract passes non-circular dependence, against F10 L272 = F11 L259 (§2.6). |

The Derivation 2 text and the S3 and NV text are identical in files 10 and 11 (checked by diff). Each repair below therefore applies to both files. File 11 differs only in sentences around them (F11 L161, L271, L275, L279, L301, L309), and those are noted where they matter.

---

## 1. Hole 1 (W19; Mimo M6): Derivation 2

### 1.1 The text

**Claim** (F10 L561 = F11 L554): "Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2), and (A) on \(C\) are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide."

**Proof** (F10 L563 = F11 L556): "Immediate from Derivation 1 and (A). ∎"

**Consequence** (F10 L565 = F11 L558): "Underdetermination of an account by a contract is not a failure of the semantics to decide ... A claim that two such candidates 'really' differ is a claim that some admitted change separates them, and must supply it."

**Definitions it uses.**
- **(K)** (F10 L130–136 = F11 L115–121). A signature is \(\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}\). Two components are "of one kind on \(C\)" when "there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide". Both sentences are stated for components of *one* organization under *one* contract.
- **A candidate** (F10 L246 = F11 L233) is \(E\), its own transport \(t=(\pi,\tau,\sigma,\lambda)\), and \(\Gamma\). Each candidate brings its own \(\lambda\).
- **(F1)** is at F10 L248–251 = F11 L235–238. **(F2)** is at F10 L257 = F11 L244. **(A)** is at F10 L265 = F11 L252.
- **Derivation 1** (F10 L553–555 = F11 L546–548): "every active component \(k\) of \(E\) has the same signature on \(\tau[C]\) as its anchor \(\lambda(k)\) has on \(C\), up to the port translation."
- **Part XV** (F10 L543 = F11 L538) lists as a defeater "A counterexample to ... Derivations 1–3 under their stated assumptions".

**How Mimo stated it.**
- Trial L147: Derivation 1 "only pairs each component with *its own* anchor ... Two candidates with different \(\lambda\), or different numbers of components, are not paired by anything shown. The claim needs shared anchors or a further argument."
- Trial L191: "M6 is a proof gap in a derivation that Part XV exposes to refutation."
- Story S83 (L94): "Derivation 2's proof never shows the components pair up".

### 1.2 The proof, step by step

- **Step 0 (typing).** (K) compares components of one organization. A component of \(E\) lives on \(\tau[C]\) and a component of \(E'\) on \(\tau'[C]\). Their signature sets carry different first coordinates whenever \(\tau\neq\tau'\), so the sets can "coincide" only when both are read on \(C\). The reading needed is this: \(k\) and \(k'\) are of one kind on \(C\) when, for some footprint bijection \(\beta\), \(\beta[L_k(\tau(a),\sigma(b))]=L_{k'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). Derivation 1 already reads signatures this way ("up to the port translation"). **Holds by convention.** No sentence states the convention.
- **Step 1.** Derivation 1 for \(E\) gives each active \(k\) the signature of \(\lambda(k)\). Derivation 1 for \(E'\) gives each \(k'\) the signature of \(\lambda'(k')\). **Holds.**
- **Step 2.** Kind on \(C\) is an equivalence (F10 L136: "A kind is an equivalence class"). So \(k\) and \(k'\) are of one kind exactly when \(\lambda(k)\) and \(\lambda'(k')\) have one signature on \(C\). **Holds.**
- **Step 3 ("pairwise").** This needs a bijection \(\varphi\) from the active components of \(E\) to those of \(E'\) with \(\lambda(k)\) and \(\lambda'(\varphi(k))\) of one signature. **Breaks.** Nothing supplies \(\varphi\):
  - (F1) constrains each candidate against \(D\) separately.
  - (F2) constrains only the assembled solution sets: \(\pi[\operatorname{Sol}_D]=\operatorname{Sol}_E\) and \(\pi'[\operatorname{Sol}_D]=\operatorname{Sol}_{E'}\).
  - (A) constrains only answers.
  - The proof's word "Immediate" skips exactly this step.
- **Step 4 (answer profiles).** \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\), by (A) twice. **Holds**, read on \(C\).

### 1.3 Attempts to refute: does anything else supply Step 3?

| place | what it gives | supplies \(\varphi\)? |
|---|---|---|
| (K) as an equivalence, F10 L136 = F11 L121 | transitivity (Step 2) | no |
| "Why there is no anchoring condition", F10 L296–298 = F11 L281–283 | compares one candidate with \(D\) | no |
| F1's gloss, F10 L260 = F11 L247: "(F1) prevents an assembled match from hiding a *wrong* decomposition" | excludes wrong decompositions; says nothing about two right ones | no |
| Derivation 8, F10 L609 = F11 L602 | identity along a given structure-preserving bijection; "does not apply to coarsenings" | no: it presupposes the bijection, and it excludes the counter-instance's case |
| Derivation 9 (F10 L613 = F11 L606); Part VI "Redundant routes" (F10 L324 = F11 L309); Part 0 "Two systems with identical outputs and different internal routes are different organizations here" (F10 L23 = F11 L25) | the opposite: same answers do not make the same organization | no |
| "at grain \(C\)" in the claim | grain is a declared index (F10 L523 = F11 L516) and is never defined as a decomposition. If the phrase was meant to carry a shared decomposition, that is the missing premise, unstated. | no |
| File 00 | 00 has no Derivation 2, and says the opposite: "Coarsening is not automatically an isomorphism. Bundling two commitments into one can change the answer to a question about individual contribution while preserving an answer about their joint organization." (00:154) | no |

**Not refuted.**

### 1.4 Counter-instance

The instance is a production question in Part III's sense (F10 L168 = F11 L153).

**Target \(D\).**
- Ports: \(x,y,z\), real-valued.
- Components:
  - \(j_x\): \(x=u\), where \(u\) is the boundary value, \(u=0\) at \(b_0\).
  - \(j_y\): \(y=2x\).
  - \(j_z\): \(z=y+1\).
- Admitted edits: the identity, and \(\mathrm{do}(x{=}c)\) for each real \(c\). Setting \(x\) replaces \(j_x\) (F10 L120 = F11 L105).
- Contract: \(C=\{(1,b_0)\}\cup\{(\mathrm{do}(x{=}c),b_0)\}\).
- Query: \(\mathcal Q\) reads \(z\), so \(\operatorname{Ans}_p(\mathrm{do}(x{=}c),b_0)=2c+1\).

**Candidate \(E_1\)** is \(D\) itself, with \(\lambda\), \(\pi\), \(\tau\) and \(\sigma\) the identity. (F1), (F2) and (A) hold trivially.

**Candidate \(E_2\)** has ports \(x,z\) and two components:
- \(m_x\): \(x=u\), anchored to \(j_x\).
- \(m_z\): \(z=2x+1\), anchored to the subnetwork \(\{j_y,j_z\}\), with its hidden port \(y\) projected away.

Take \(\pi(x,y,z)=(x,z)\) and let \(\tau\) be the identity on each \(\mathrm{do}(x{=}c)\).

**The three conditions hold for \(E_2\).**
- **(F1).** \(\operatorname{proj}_{x,z}\operatorname{Sol}_{\{j_y,j_z\}}(a,b_0)=\{(s,2s+1)\}=L_{m_z}\) for every \((a,b_0)\in C\). The edit \(\mathrm{do}(x{=}c)\) replaces \(j_x\), which lies outside that anchor. For \(m_x\), both sides are \(\{c\}\) under \(\mathrm{do}(x{=}c)\) and \(\{u\}\) at the baseline.
- **(F2).** \(\pi[\operatorname{Sol}_D(\mathrm{do}(x{=}c),b_0)]=\{(c,2c+1)\}=\operatorname{Sol}_{E_2}(\mathrm{do}(x{=}c),b_0)\). Also \(\tau(1)=1\), and \(\mathrm{do}(x{=}c_2)\mathrm{do}(x{=}c_1)=\mathrm{do}(x{=}c_2)\) on both sides.
- **(A).** Both candidates answer \(2c+1\).

**The components do not pair.**
- \(E_1\) has three active components and \(E_2\) has two, so no bijection exists.
- Worse, \(m_z\) is of one kind with no component of \(E_1\). Under either footprint bijection, \(\{(s,2s+1)\}\) differs from \(k_y\)'s \(\{(s,2s)\}\) and from \(k_z\)'s \(\{(s,s+1)\}\).
- The answer profiles coincide.

**Conclusion.** Both candidates meet the claim's hypotheses. On any reading of S3 that lets an intervention on an input witness, they meet all of (E). Yet their components are not pairwise of one kind. **Derivation 2's first conjunct is false.**

**The construction is not exotic.**
- (F1) itself is written to project away hidden ports.
- Part VII's skew case relies on "a determinant suborganization whose hidden ports project away" (F10 L356 = F11 L341).
- F11 L279 accepts "a coarse dependence ... for omitting finer workings".

**Equal component counts do not save the claim.** Let \(D\) have \(x=u\), \(y=x+1\), \(z=y+1\) and \(w=z\).
- \(E_a\) cuts \(D\) as \(\{x=u\},\{z=x+2\},\{w=z\}\).
- \(E_b\) cuts \(D\) as \(\{x=u\},\{y=x+1\},\{w=y+1\}\).
- Both have three components, and both satisfy (F1), (F2) and (A) under \(\mathrm{do}(x{=}c)\).
- Only the two input components pair.

### 1.5 What rests on Derivation 2

**Derivation 10** (F10 L627 = F11 L620) says: "On any contract containing it, the two persistence components are of one kind (Derivation 2)." It is the only use of Derivation 2 in either file.
- **Intended content.** It is a claim about two *transports*. \(t_1\) anchors component 1 to thing 1. \(t_2\) exchanges the two anchors. Both are faithful, and which one is "right" is not a further fact.
- **That is the shared-anchor case, where Step 3 holds**, with \(\varphi\) the exchange.
- **Read literally, it fails under (K) itself.** The literal reading is a claim about two components inside \(S_1\). But Derivation 10's contract includes "displace a thing" (F10 L617 = F11 L610). Under that edit one persistence component's relation is replaced and the other's is not, and (K) compares signatures edit by edit.
- **Consequence for W10(b).** Its proposed erratum, "cite (K) instead", would cite a definition that does not deliver the sentence. The right fix is to restate the sentence as the two-transport claim and keep citing a repaired Derivation 2 (§1.7).

**Derivation 2's own Consequence** (F10 L565 = F11 L558) is used as an argument against claims that two candidates "really differ". Grievance 2 and attack (C) rest on (K) and Derivation 1, not on Derivation 2.

**W21.** \(\equiv_\ell\) in (N) must not be defined through Derivation 2 (worklist conflict 7).

**Fixed verdicts.** None of the 52 needs the unrestricted claim. Applied, the unrestricted claim pushes several cases toward the wrong verdict:
- **O46.** The spring account and the reassigned cable account would both be faithful and so "one account". That is against the fixed verdict, and against F11 L309: "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment".
- **O45.** The two springs' supports would be one account. That is against Part VI's "Redundant routes" (F10 L324 = F11 L309).
- **O36.** An unwritten route would be identified with the written one. That is against F11 L301: "the supports assessed are the ones actually written".
- **N17.** The electron calculation and the factoring answer would be "one account". That is against the fixed "each tells the asker something the other does not".

### 1.6 Verdict

**CONFIRMED.**
- The proof secures the answer-profile half.
- For the component half, it secures only that each candidate's components have their own anchors' kinds.
- The component half, as stated, has a counter-instance within its stated assumptions. Under F10 L543 = F11 L538 that is a listed defeater.
- Derivation 1 stands.

### 1.7 Repair (same text in both files; a claim change, to be recorded as one)

**Replace F10 L559–565 = F11 L552–558 with:**

> ## 2. Same anchors, one account
>
> **Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\). (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components satisfies \(\lambda'(\varphi(k))=\lambda(k)\) for every \(k\), up to port translation, then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\), and the two are one account on \(C\).
>
> *Proof.* (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). (ii) By Derivation 1, \(k\) has the signature of \(\lambda(k)\), and \(\varphi(k)\) the signature of \(\lambda'(\varphi(k))=\lambda(k)\); composing the two port translations gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎
>
> Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes). A coarsening is not a recoding (Derivation 8).
>
> **Consequence.** Where two faithful candidates differ only in which component carries which anchor, the contract does not contain the distinction; a claim that one assignment is "really" right is a claim that some admitted change separates them, and must supply it. The remedy is a finer contract, which is a new question.

**Two supporting edits.**
- **After (K)** (F10 L136 = F11 L121), add one sentence: "A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense."
- **Derivation 10** (F10 L627 = F11 L620), erratum. Replace "the two persistence components are of one kind (Derivation 2)" with "exchanging the two persistence components' anchors gives a second faithful transport, and the two transports are one account (Derivation 2)".

**Why "the same subnetworks" and not "anchors of one kind".** The weaker premise would identify O45's two springs, and O46's spring and cable, whenever \(C\) does not separate them. That collides with Part VI's redundant routes and with F11 L309.

**Gained.**
- The claim is true and the proof matches it.
- It is consistent with Derivations 8 and 9, Part VI, F11 L301 and L309, and Part 0 (F10 L23 = F11 L25).
- Derivation 10 keeps a correct citation.
- Part XV no longer lists a false result.

**Lost.**
- The slogan "indistinguishable is identical".
- The Consequence's reach narrows to anchor assignments.
- Identity of differently decomposed candidates is left undefined. If it is needed, it must come from W21, defined independently of (ii).
- File 11's revision note ("One claim changes") would need a second claim change recorded.

**Cases that test the repair.**
- **O46: the decisive one**, between "same subnetworks" and "anchors of one kind". The repair must keep "a new account with a cable in it".
- **O45 and O36:** Derivation 2 must stay silent.
- **O24:** not triggered, since the reachable setting is in \(C\) and at most one arrangement satisfies (A).
- **O10:** kinds within one organization, decided by (K). Untouched.
- **N17:** two candidates with one answer profile. This agrees with "each tells the asker something the other does not".
- **N25:** if the dog and the turtle are faithful at all, they share the holder's anchor, so they are one account at the grain. This agrees with "the difference ... is idle".
- **N23:** on a baseline-only contract, forward and backward are one relation. Direction comes from the production contract, where the backward calculation fails (F2).

---

## 2. Hole 2 (W20; Mimo M3): the non-circular dependence condition

### 2.1 The text

**Non-circular dependence** (F10 L270 = F11 L257, identical):
- **S1:** "The answer follows by evaluating \(E\) under its independent boundary conditions."
- **S2:** "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named 'law' does not discharge this."
- **S3:** "There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) while preserving the other boundary conditions, under which the answer profile changes or ceases to be determined in the claimed way."

**NV's last sentence** (F10 L272 = F11 L259): "A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), does not satisfy non-circular dependence and is therefore not a contract on which an account can be claimed."

**Definitions used.**
- **\(C\subseteq A\times B\)** is "the set of admitted edit–boundary pairs the claim ranges over" (F10 L158 = F11 L143). Here \(A\) and \(B\) are those of the target \(D\).
- **\(\Gamma\)** is "an identified set \(\Gamma\) of active commitments in \(E\)" (F10 L246 = F11 L233). It occurs only there, in S3 and in Part VI. It is typed nowhere.
- **Part VI:** "let \(E|W\) retain the commitments in \(W\) with the named background fixed" (F10 L304 = F11 L289).
- **Part II:** "An edit that sets a port replaces the component assigning that port" (F10 L120 = F11 L105).
- **(F1), (F2) and (A)** read every \((a,b)\in C\) on \(E\) as \((\tau(a),\sigma(b))\).

**Sentences only in file 11.**
- L161: scope, "supplies no rule that certifies it".
- L271: a table encoding every response "is an account".
- L275: restating component; packaging.
- L279: coarse dependence.

**File 00.**
- 00:210 is the same clause, with an "admitted contrast" that "removes or changes a nonempty block of active organizational commitments, while preserving the other declared boundary conditions". It adds: "The contrast may concern a counterfactual law or rule rather than a physically executable intervention. Its formal meaning must still be stated."
- 00:176 bridges contract edits to explanatory components: "every component edit in the contrast contract must translate to the corresponding replacement of that subnetwork relation".
- 00:165 fixes the commitments by the claim: "not permission for an assessor to rescue a failed argument by selecting whichever fragments happen to be true".
- Files 10 and 11 dropped the last two with the Anchoring condition.

**How Mimo stated it.**
- Trial L144: "a \(D\)-edit is said to act on \(E\)'s commitments, with no \(\tau\), and 'other boundary conditions' treats blocks of \(\Gamma\) as boundary conditions. This is the defining clause of the condition that decides O2, O5 and O33."
- Also trial L136, the A6 note ("The real defect in this sentence is a different one, M3"), L157 (Mimo on O2), and L191 ("a type error in the defining clause of one of the four conditions of Account").
- Story S83 (L94): "the non-circular dependence condition's edit on the target acting on the explanation's commitments".

### 2.2 Type check

1. **The edit acts on the wrong organization.** \((a,b)\in A_D\times B_D\), but S3 has it "remove or replace a nonempty block of \(\Gamma\)", and \(\Gamma\) lies in \(E\). A \(D\)-edit reaches \(E\) only through \(\tau,\sigma\), and S3 names neither. This is Mimo's first half.
2. **\(\Gamma\)'s elements are never typed**, and three places pull three ways:
   - (F1) speaks of "active component \(k\)", which makes commitments components.
   - S3's "the *other* boundary conditions" presupposes that the removed block is boundary conditions. This is Mimo's second half.
   - Part VI sets "commitments" against "the named background", which suggests that input settings are background, not commitments.
   - A notational point makes this worse: (B) at F10 L310–313 = F11 L295–298 names a block of commitments \(B\), the letter the organization uses for its boundary conditions (F10 L105).
3. **S3 is not an anti-circularity test on any reading.** "\(p\) because \(p\)" meets S3 whenever the installed answer can be removed (the answer then "ceases to be determined") or intervened on. What excludes circularity is S2, together with L275 in file 11. The condition's name covers two tests: a prohibition (S2) and a dependence requirement (S3).

### 2.3 Attempts to refute

- **The \(\tau\) half: the text's conventions supply it.**
  - Every other conjunct of Part V reads a pair from \(C\) on \(E\) as \((\tau(a),\sigma(b))\).
  - Part V calls each conjunct "a condition on supplied relations under the changes in \(C\)" (F10 L246 = F11 L233).
  - (F1) forces a \(C\)-edit that alters an anchor \(\lambda(k)\) to alter \(k\) to match.
  - The only worked Account in either file applies S3 exactly this way. The skew case says "Non-circular dependence is witnessed by \(I_3\) under removal of skewness and by \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) under removal of oddness" (F10 L356 = F11 L341). There the contract's edits remove the target's constraints, and, through \(\tau\), the expansion's commitments. "Field arithmetic and determinant–invertibility held fixed" are the other boundary conditions.
  - So the missing \(\tau\), taken alone, is a drafting fault. **As a misfire, REFUTED.**
- **The \(\Gamma\) half: nothing fixes its type.**
  - Part II's replacement rule settles what an intervention on an input *does*: it replaces the component that assigns the input. It does not settle whether that component is in \(\Gamma\).
  - The candidate "identifies" \(\Gamma\), but no sentence says whether an input setting may be identified as a commitment or is "named background".
  - The only worked Account (the skew case) uses commitment-removing edits and no input interventions. Part VII's production case claims only "faithful" (F10 L338 = F11 L323).
  - So the text shows no Account passing S3 through input interventions alone, and none failing it. **Not refuted.**

### 2.4 Four readings of S3

| label | witness | \(\Gamma\) holds | where it comes from |
|---|---|---|---|
| **R-lit** | \((a,b)\in C\), evaluated on \(D\) | \(D\)'s own components | the words as written. It has a truth value only where \(E\) shares components with \(D\), as in the skew case. |
| **R-τ-in** | \((a,b)\in C\) whose \((\tau(a),\sigma(b))\) removes or replaces a block, with the rest of \(\sigma(b_0)\) kept | components of \(E\), including those assigning the inputs (and boundary values) the candidate commits to | (F1), (F2) and (A)'s pattern; Part II; "other boundary conditions" |
| **R-τ-mech** | the same | only the mechanism the candidate offers; input settings are background | Part VI's "named background" |
| **R-E** | an organization edit on \(E\) (Part VI), judged by the answer profile on \(C\) | the candidate's commitments | the worklist's proposed retype (W20, "Handling") |

### 2.5 The three cases, worked, and two more

#### O2: the tide table with a real bell

The situation: "Take the bell mechanism away and what her account establishes does change ... The bell mechanism is physically real and independently grounded." The verdict: "explained nothing about the tide. The almanac is the answer written down."

Here \(\Gamma=\{\text{almanac},\text{bell mechanism}\}\), and \(\mathcal Q\) reads the water height at noon.

- **S2 fires in both files, on every reading.** The almanac is "the target's answer ... as a component".
  - File 11 adds L275: "So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this".
  - File 10 has L288, "'\(p\) because \(p\)' fails non-circular dependence", and S2 itself.
- **S3 under each reading:**
  - **R-τ-in.** If \(C\) holds production interventions on the tide, the almanac fails (F1) first (F10 L284 = F11 L271). If \(C\) holds only date changes, a date change may witness S3 through the almanac, and S2 still fails the candidate.
  - **R-τ-mech.** No \(C\)-edit replaces the almanac with a change in the answer, and the bell edits do not change what \(\mathcal Q\) reads. S3 fails.
  - **R-E.** Deleting the almanac leaves the answer undetermined, so S3 holds through the circular block itself. Deleting the bell changes nothing \(\mathcal Q\) reads.
  - **R-lit.** No \(D\)-edit removes a printed book, and removing the lever changes no water height. S3 fails.
- **The situation's lure** ("what her account establishes does change") is blocked in both files by the definition of the answer profile ((Q), F10 L161 = F11 L146) and by "The query \(\mathcal Q\) is held fixed" (F10 L268 = F11 L255).
- **Result.** The fixed verdict holds in both files on every reading. **S3 never decides O2; S2 does.** The two halves "pull apart" only in that S3 can pass (R-τ-in on a date contract, R-E) while S2 fails. (E) is a conjunction, so the candidate fails.
- **"She has explained the bell"** holds on every reading. For the bell question, the lever is a \(D\)-component. Removing it stops the ringing, and the water height enters as an independent boundary value.
- **A tension in file 11 only (W11).** On a date-only contract the almanac "genuinely encodes an organization's response to every admitted change". F11 L271 says such a table "satisfies (F1) as a decomposition does, and it is an account". That contradicts S2 and L275 on O2. File 10 L284 says only "is not excluded" (by F1), so file 10 does not conflict.

#### O5: Greta's dough

The verdict: "a legitimate narrowing. The limit follows from a part of her account." The case was written as a control that should pass (the provenance table: "clause A-prime, as a control that should pass").

- **S2 passes.** The doubling is derived from the yeast, not installed.
- **The narrowed contract** is "rooms warmer than twenty degrees", a stated scope (F10 L272 = F11 L259; F11 L161). Inside the scope the dough doubles in two hours throughout. So the commitment that holds the limit in place (yeast is slow in the cold) cannot witness S3 there, on any reading that keeps the witness in \(C\). Some other block has to.
- **S3 under each reading:**
  - **R-τ-in.** A production contract contains "interventions on upstream ports" (F10 L168 = F11 L153), for example leaving the yeast out. That replaces the component assigning the yeast input (Part II), and the doubling fails. S3 holds, so the narrowed claim is an account at its stated scope. This matches the fixed verdict.
  - **R-τ-mech.** Leaving the yeast out sets an input and replaces no mechanism component. Unless \(C\) also holds an edit that deletes or replaces the yeast's gas production, there is no witness. NV's last sentence then says the narrowed contract "does not satisfy non-circular dependence". **O5 flips.**
  - **R-E.** Deleting the yeast block leaves the doubling undetermined. S3 holds on any contract.
- **The Tuesday comparison.** On no reading does S3 separate the two limits: they have the same \(\Gamma\) and the same witnesses. What separates them, if anything, is (A): a "days other than Tuesdays" rule keeps the cold January days on which it fails. F11 L161 says the semantics "supplies no rule that certifies" a restriction. So "the limit follows from a part of her account" is not a finding S3 produces in either file. The trial's statement that this clause "decides" O5 is right only for whether the narrowed claim is an account at all.
- **Result.** The fixed verdict holds under R-τ-in and R-E, and flips under R-τ-mech on an ordinary production contract. The same holds in both files.

#### O33: the table with empty columns

The verdict: "The table is faithful ... A form that could ask more has not asked more." Here \(C\) is joint turns only.

- **S2 passes.**
- **S3 under each reading:**
  - **R-τ-in.** A joint turn sets both knob ports, replacing the components that assign them (Part II), with the rest of the baseline kept, and the compartment temperatures change. S3 holds, so Lea's joint question is a contract on which an account can be claimed. The table has the same \((C,\mathcal Q)\), so it is the same question (F10 L168 = F11 L153) and it is faithful. This matches the fixed verdict.
  - **R-E.** Deleting the linkage, or one knob's dependence, changes the answer on joint turns. S3 holds. This matches.
  - **R-τ-mech.** No joint turn deletes or replaces a mechanism component, so no candidate has a witness. NV's last sentence then makes Lea's contract "not a contract on which an account can be claimed". That is Atria's reading, which the trial scored D x (trial L108). **O33 flips.**
- **The trial's own scoring of this row depends on the typing.** Its rebuttal of Atria ("the joint turns themselves change the answer") is sound only under R-τ-in or R-E. The trial's scoring of O33 therefore rests on the untyped \(\Gamma\).
- **Result.** The fixed verdict holds under R-τ-in and R-E, and flips under R-τ-mech. The same holds in both files. O22's joint question sits on the same contract.

#### Two cleaner counter-instances to R-τ-mech

- **Part VII production** (F10 L338 = F11 L323).
  - Setup: \(E=\{H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\}\), and \(C\) is interventions on \(H\) and \(\theta\).
  - With \(\Gamma=\{L:=H\cot\theta\}\), no \(C\)-edit replaces the commitment, so S3 fails.
  - The forward organization then fails to be an Account on the production contract. Yet Part V's reversed-calculation paragraph treats it as the production answer (F10 L286 = F11 L273).
  - Part VII itself says only "faithful", so no sentence is contradicted outright.
- **O7, salt on the icy step.**
  - Setup: \(C\) is spreading and sweeping.
  - With \(\Gamma=\{\text{salt melts ice}\}\), sweeping sets the salt port and replaces no mechanism. S3 fails.
  - The fixed "a genuine explanation, a coarse one" flips.

### 2.6 The worklist's proposed retype (R-E) breaks another sentence

- **NV's relabelings sentence becomes false.** Take any honest mechanism \(E\), and \(C=\{(1,b_0)\}\) plus relabelings. Under R-E, deleting a working block leaves the answer at \((1,b_0)\) undetermined, so S3 holds. S2 holds too, so non-circular dependence is met. But NV's last sentence (F10 L272 = F11 L259) says a contract "consisting only of relabelings ... does not satisfy non-circular dependence".
- **N25 and N3 get through S3.** The same retype lets N25's dog and N3's bargain pass S3: delete the holder or the bargain, and the answer ceases to be determined. Only S2 is left to stop them.
- **So the "\((a,b)\in C\)" in S3 is load-bearing.** It is what ties dependence to the contract and gives scope-honesty its bite. A retype must keep the witnessing contrast inside \(C\).

### 2.7 Verdict

**CONFIRMED, in part.**
- **The missing \(\tau,\sigma\)** is a drafting fault that the text's conventions fill: (F1), (F2) and (A), and the skew case. As a misfire, REFUTED.
- **The untyped \(\Gamma\) and "the other boundary conditions"** are CONFIRMED, with a live verdict risk:
  - R-τ-in is the only reading on which S3, NV's last sentence and the fixed verdicts all agree. On it, O2, O5 and O33 keep their fixed verdicts in both files.
  - R-τ-mech is the reading Part VI invites. On it, O33 and O7 flip, and O5 flips on an ordinary production contract.
  - O2 flips on no reading, because S2 (and L275 in file 11) decides it.
  - Files 10 and 11 do not choose between the readings.
- **"This clause decides O2, O5 and O33"** (trial L144) is right for O33, and for whether O5's narrowed claim is an account at all. It is not right for O2, which S2 decides.

### 2.8 Repair (same text in both files)

#### Option A: erratum plus clarification (minimal)

- **S3 becomes:** "There exists \((a,b)\in C\) whose translation \((\tau(a),\sigma(b))\) removes or replaces a nonempty block of \(\Gamma\), with \(\sigma(b)\) keeping the rest of the baseline \(\sigma(b_0)\), under which the answer profile changes or ceases to be determined in the claimed way."
- **At F10 L246 = F11 L233, add:** "The commitments \(\Gamma\) are components and boundary values of \(E\), including the components that assign the inputs the candidate commits to; since an edit that sets a port replaces the component assigning it (Part II), an intervention in \(C\) on such an input removes or replaces a block of \(\Gamma\)."
- **Restore from 00:210:** "The change may concern a counterfactual law or rule rather than a physically executable intervention; its formal meaning is stated in \(C\)." This protects the skew case (the W39 context).

**Gained.**
- The clause is well typed.
- The text now secures O33, O7, O5 and Part VII's production case.
- NV's last sentence stays true.
- S2, with L275 in file 11, still decides O2.
- N25 and N3 fail S3, because no admitted change reaches the holder or the bargain.

**Lost.**
- Input settings become commitments. In Part VI they then sit in every support and are reported critical in every support. That is noise in (B) reports, though harmless for proof cases such as O36, which have no inputs.
- "Commitment" loses file 00's sense of what the claim offers as doing the work (00:165).

#### Option B: a new step (preferred)

**S3 becomes:** "There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and in \(E|(\Gamma\setminus G)\), with the named background fixed, that difference is lost or the answer ceases to be determined."

**What it keeps.** The witnessing contrast stays in \(C\), so NV's last sentence stays true; it becomes literally the gloss of S3. The dependence is placed on \(\Gamma\) through Part VI's restriction, as the worklist wanted, without making input settings commitments.

**How the cases come out.**
- **O33.** A joint turn changes the answer, and removing the linkage or a knob's dependence loses the change. It holds.
- **O7, Part VII production, and O5 on a production contract** all hold the same way.
- **The skew case** holds: removal of skewness changes the answer, and dropping the skewness commitment loses the change.
- **O2.** On a date contract, removing the almanac loses the difference, so S3 holds. Removing the bell does not, so the bell can never witness; this derives half of L275. S2 still fails the candidate.
- **N25.** No admitted change alters the answer, so S3 fails.
- **N1.** The tilt witnesses; removing the sun god loses nothing.

**Lost.**
- The logical form changes. That is a claim change to record, not an erratum.
- The restriction \(E|W\) must be introduced before Part V.
- The dependence order (F10 L525 = F11 L518) must say that non-circular dependence uses the restriction. It uses the operation, not (S), so the order stays well founded.

#### Keep in either option

- S2 unchanged.
- F11 L275's rule. Its example's name is W9's point.
- If \(\tau\)'s role needs stating once, restore 00:176's bridge.

#### Do not adopt R-E alone

The worklist's first handling is R-E. It falsifies NV's last sentence and lets N25 and N3 through S3 (§2.6). The worklist's second handling, "link the target-side contrast in C to the E-side edit through \(\tau\)", is Option A, and it needs \(\Gamma\) typed to work.

#### Cases that test the repair

- **O33:** decides between R-τ-in or Option B on one side and R-τ-mech on the other.
- **O7.**
- **O5:** once with an upstream intervention in \(C\), once without.
- **O2:** S2 and L275 must still decide it, and the bell must not witness.
- **O4:** dilution witnesses; S2 and W29 decide it.
- **O36 and Part VII's skew case:** contrasts that remove a rule must still witness.
- **O22:** the joint question must stay answerable.
- **N25 and N3:** decide against R-E.
- **N1:** the tilt witnesses, and the god is idle.
- **N16:** answer A fails on S2.

---

## 3. Side findings (not asked; flagged for the worklist)

1. **W10(b) as proposed would not work.** Read within one candidate, Derivation 10's "the two persistence components are of one kind" fails (K), because the contract holds single-thing displacements. The fix is the two-transport wording in §1.7.
2. **F11 L271 contradicts S2 and L275 on O2** under a date-only contract (W11).
3. **The letter \(B\)** names both a block of commitments in (B) and the organization's boundary conditions. This feeds Mimo's "other boundary conditions" point.
4. **"At grain \(C\)."** Derivation 2 speaks of grain \(C\), while grain is \(\ell\) everywhere else. This links to M4 and W21.
5. **The trial's scoring of O33 depends on the typing.** The trial scored Atria's O33 reading D x, but that scoring rests on the reading of S3 that W20 would fix. Were R-τ-mech adopted, Atria's reading would become the theory's.

## 4. Limits

- Every case check here is worked by hand from the theory text. None was run against a model.
- Where a verdict depends on what a case's contract contains, this file says so. The situations in the case book do not state their contracts.
- Mimo's own wording was not read, only the trial's statement of it.
- The determination file det 02 C40, which the worklist cites for O2, was not opened.
