# S88: reading of Mimo's reply, part F1 (Derivation 2)

*Written by a fresh Claude reader, a subagent, for the orchestrator on 23 September 2026. The reader did not write the findings. The reading follows the S88 rule, `results/S88 How the cross-examination will be read - written after Atria's reply arrived, before it was opened.md` (committed at cc87b45), as amended before sending by `results/S88 Mimo's reply in three parts - how it will be read, written before sending.md` (committed at db05b18).*

**What the reader opened:**

- the F1 receipt, the F1 reply, and the F1 request (for its hash only);
- the F1 part brief, `tests/S88 Cross-examination - part F1, Derivation 2.md`;
- file 10 and file 11 in `authority/`;
- the rule and the note.

**What the reader did not open:**

- the F1 reasoning file;
- Atria's reply, Atria's reasoning, and `S88 Reading of Atria's reply - the three defects.md`;
- the F2 and F3 replies and their readings.

## R1. The receipt comes first

The file `s88_xexam_mimo_F1.receipt.json` shows an accepted call.

- **Finish and acceptance.** It has finish_reason "stop" and saw_done true. The call was accepted on attempt 3.
- **The earlier attempts.** Attempts 1 and 2 ended with status 0 and returned no content. They were not rejected replies.
- **The reply.** It has 11,860 characters, and its last line is END OF REPORT.
- **Tokens.** The call used 43,154 reasoning tokens against the 131,072 ceiling.
- **The text sent.** The receipt's `user_sha256` is 45e210160953…. That equals the sha256 of the part brief and the sha256 of the request's one user message.

**Times.**

- The note was committed at 17:47:42 UTC (db05b18).
- The call was asked at 17:48:46 UTC (`asked_at_unix` 1790185726).
- It ended about 18:49:41 UTC (`total_seconds` 3,655).
- The reply was committed at 18:51:27 UTC (68ab4da).

So R7's late-rule statement does not go with this reading.

## Step 1. Claude's position on F1 after Atria's reading

This is copied verbatim from the note:

> **F1: UPHELD.** The component half of Derivation 2 is false under its stated assumptions, and the answer-profile half is true. The repair is "Same anchors, one account", a recorded change of claim, with the premise tightened and the conclusion qualified:
>
> > **Claim.** Let ℰ, ℰ′ be candidates for the same p that both satisfy (F1), (F2) and (A) on C. (i) Their answer profiles coincide on C. (ii) If a bijection φ of their active components gives each k and φ(k) one anchor, the same subnetwork of D with port translations onto the same ports of D, then k and φ(k) are of one kind on C for every k; so far as (F1), (F2) and (A) reach, the two are one account on C.
>
> The sentence "Without the premise of (ii) nothing more follows …", the Consequence, the sentence after (K) and the Derivation 10 wording are as in the part's brief. The smaller alternative wording is not adopted as it stands.

## Step 2. Mimo's argument

**Verdict line:** `F1: UPHELD`

Mimo's points, restated in the reader's words under Mimo's own numbers:

**1. Mimo finds the counter-instances valid, and every route to refuting them fails.**

- *Route 1: no stated assumption is broken.*
  - C contains the baseline (line 158).
  - The merged anchor is allowed by line 204: "λ assigns each component of E a subnetwork of D with a port translation."
  - The edit do(x=c) replaces j_x, which lies outside m_z's anchor (line 120). So the projection of Sol over {j_y, j_z} is {(s, 2s+1)} at every pair.
  - (F2) and (A) hold.
- *Route 2: the claim fails under every reading of "pairwise of one kind".*
  - There is no bijection between three components and two.
  - Under the existential reading, k_y ({(s,2s)} on {x,y}) and k_z ({(t,t+1)} on {y,z}) match nothing in E_2.
  - Instance 2 has equal counts, but only the input components pair.
  - The two partitions are incomparable.
- *Route 3: sentence readings.* These are deferred to defence (ii).
- *The step Mimo "could not refute".* This is that Derivation 1 relates each component only to its own anchor. Mimo quotes line 555: "(F1) equates the third coordinates pointwise … Nothing in it pairs a component of E with a component of E′."

**2. The four defences fail.**

- *(i)* Merged anchors are admitted, by lines 204, 248, 356 and 260.
- *(ii)* The shared-anchor reading makes the proof valid, but "cannot support the text that surrounds it". In Mimo's words, "their components are pairwise of one kind" names all components. The title asserts identity, and so do the words "one account". Line 23 makes E_1 and E_2 different organizations, and "No line of the theory states the restriction."
- *(iii)* Subnetwork matching runs one way only in instance 1. In instance 2, Mimo checked every subnetwork of E_b ("all six") against a_w and found no partner. Block-to-block matching rescues both instances, but the theory defines no such notion, and line 609 excludes coarsenings.
- *(iv)* Grain and contract are separate declared indices (line 523). (K) gives k_y, k_z and m_z three distinct relations.

**3. The typing point is correct.** (K) at line 136 is defined within one organization. The finding's reading through τ and τ′ is, in Mimo's words, "the only one that typechecks". No sentence states it.

**4. The repair is sound.**

- Part (i) follows from (A).
- Part (ii): "composing the two port translations yields a footprint bijection under which the signatures coincide. The proof is valid", with the premise "correctly stated as 'same subnetworks'".
- Breakage check:
  - Derivation 1 is unaffected. Mimo adds a "minor imprecision": the sentence after (K) says "Derivations 1 and 2 use kinds in this sense", but Derivation 1 makes the component-to-subnetwork comparison.
  - Derivation 8 is consistent with the repair.
  - The repair states "exactly Derivation 9's thesis", and the original claim "was in tension with it".
  - The literal Derivation 10 sentence is independently defective, because "displace a thing" separates the two components under (K). The replacement is correct.
  - Part VI, Part VII, the paragraphs on what (E) does and does not exclude, and Derivations 3 to 7 are untouched.
- Costs:
  - The full repair is preferred over the alternative, which is "adequate for the claim alone".
  - One residual informality remains: "'one account' is never formally defined in the theory (Account(ℰ) is a predicate on a single candidate, not an equivalence relation on pairs); the repair inherits this."

**5. The classification is apt.** In Mimo's words: "Half (a) of the claim is false as stated under all readings I could construct; half (b) is true. The remedy is a recorded change of claim … not a rereading of the existing words."

## Step 3. Check against the theory text

The theory text between the part brief's markers (brief lines 22 to 650) was compared with file 10 using `cmp`, and the two are byte for byte identical. The line numbers below are file 10's.

### 3.1 The theory lines the argument relies on

| line | text (quoted) | use |
|---|---|---|
| 23 | "Two systems with identical outputs and different internal routes are different organizations here, and the semantics says so." | against defence (ii) |
| 108 | "\(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\)" | the instances' edits: do(x=c₂)do(x=c₁) = do(x=c₂) |
| 120 | "An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one." | do(x=c) replaces j_x, outside m_z's anchor |
| 133–136 | (K); "Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide." | kind is defined within one organization, edit by edit |
| 158 | "it contains the baseline \((1,b_0)\)" | C as stated is admissible |
| 204 | "\(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation." | merged anchors are admitted |
| 248 | "the relation obtained by imposing the constraints of \(\lambda(k)\) and projecting away its hidden ports" | the form of (F1); hidden ports |
| 260 | "(F1) prevents an assembled match from hiding a wrong decomposition." | E_2 passes (F1) |
| 356 | "every intermediate product is a determinant suborganization whose hidden ports project away" | a multi-component anchor is used by the theory itself |
| 523 | "Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices." | defence (iv) |
| 553–555 | Derivation 1: "… up to the port translation"; "(F1) equates the third coordinates pointwise." | component to anchor, one transport |
| 561, 563 | "… are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide."; "Immediate from Derivation 1 and (A)." | the claim and its proof |
| 609 | "The result does not apply to coarsenings, changed boundaries, or lost event identities." | the block rescue is not licensed |
| 613 | "no function of the projection agrees with the claim on both" | Derivation 9 |
| 617, 623, 627 | "admitted edits: displace a thing, …"; "\(t_1\) is faithful on the extended contract"; "the two persistence components are of one kind (Derivation 2)" | Derivation 10 |

### 3.2 Quotations checked word for word

Every quotation Mimo attributes to the theory was searched in file 10 with `grep -F`. The table above covers lines 23, 120, 136, 158, 204, 248, 260, 356, 523, 553, 555, 559, 561, 563, 565, 609, 613, 617 and 627. Every one is verbatim, and the line references are correct.

The quotations from the finding and the repair are also verbatim, with one exception.

- **One misquotation.** In its assessment of costs, Mimo puts "must supply a separating change" in quotation marks as the demand of the new Consequence. The repair's words are "a claim that one assignment is 'really' right is a claim that some admitted change separates them, and must supply it". This is a paraphrase inside quotation marks. It does not change the sense.

### 3.3 The instances, redone in exact arithmetic

The script is `s88m/f1_check.py` in the session scratchpad. It works as follows:

- It uses rational arithmetic throughout.
- Each relation is an affine set, reduced to a canonical form.
- Right-hand sides are kept affine in the edit value c. Pivots are taken only on numeric coefficients, so each equality it finds holds for every real c, not just for sampled values.
- The baseline has u = 0.

Results:

- **Instance 1.**
  - E_1 and E_2 both pass (F1) and (F2).
  - The projection onto (x, z) of the solutions over {j_y, j_z} under do(x=c) reduces to x − z/2 = −1/2, that is z = 2x + 1.
  - π[Sol_D] is {(c, 2c+1)} under do(x=c) and {(0, 1)} at the baseline.
  - All three answers are z = 2c + 1.
  - The only pair of one kind across E_1 × E_2 is (k_x, m_x).
  - **Mimo's route 1 and route 2 hold.**
- **Instance 2.**
  - E_a and E_b both pass (F1) and (F2).
  - All answers are w = c + 2.
  - The only pair of one kind across the two candidates is (a_x, b_x), and the best of the six bijections pairs 1 component of 3.
  - Neither partition refines the other.
  - **Mimo's claims hold.**
- **Defence (iii), subnetwork partners.**
  - E_b has exactly 6 subnetworks with at least two ports. {b_x} alone has only one. So Mimo's "all six" is right.
  - None of them, projected onto any ordered pair of its ports, equals a_w's {(t,t)} at every pair of C. b_y and b_w have no subnetwork partner in E_a. k_y and k_z have none in E_2.
  - a_z does have one: {b_y, b_w} on (x, w). This is the block match that Mimo and the finding both mention.
  - The blocks {a_z, a_w} and {b_y, b_w} both project to w = x + 2 on (x, w). The block {k_y, k_z} projects to m_z's relation.
  - **The conclusion holds.**
  - **One slip in the description.** Mimo says every projected relation is "either {(t,t+c)} with c≠0, or a single point varying with c". That list is not complete. {b_x, b_w} projected onto (x, y) or (x, w) is the line {c} × ℝ. That line is not {(t,t)} either, so the conclusion stands.

### 3.4 The readings, and which words fix them

**"Pairwise of one kind" ranges over all components.** The words "their components" (line 561) carry no restriction, and the colon makes the pairing the content of "one account at grain C". The title "Indistinguishable is identical" (line 559) and line 23 point the same way. No word of the theory states the shared-anchor restriction. Mimo's point 2(ii) is right.

**Kinds across two candidates.** (K) at line 136 is written for "Two components j, j′" of one organization D under one contract C. No sentence says how a component of E and a component of E′ are compared. The nearest words are Derivation 1's "up to the port translation" (line 553). No words fix the finding's typing reading.

- **An overstatement in point 3.** Mimo calls the finding's reading "the only one that typechecks", and that goes too far. A second reading also typechecks: compare the two anchors' projected relations inside D. Under (F1), by Derivation 1, it gives the same verdicts. So the counter-instances fail under both readings, and nothing turns on this.

**Hidden ports.** Mimo repeats the finding's aside that hidden ports exist "precisely when an anchor merges components". Line 248 does not imply this. A single-component anchor whose footprint is wider than k's translated ports also has hidden ports. The admissibility of merged anchors does not need this aside: it rests on line 204's "a subnetwork of D" and on line 356.

**Partitions.** Mimo calls the two partitions partitions "of D's non-input components". Both contain {j_x}, the input component, so they are partitions of all D's components. The incomparability is unaffected.

### 3.5 Mimo's judgment of the repair, checked

**(a) "The proof is valid" for (ii), with the premise "correctly stated as 'same subnetworks'".** This holds for the current premise. It fails for the premise as sent, which is the one Mimo was judging.

- **The wording as sent.** The brief's (ii) premise reads "λ′(φ(k)) = λ(k) for every k, up to port translation". This lets the two port translations land on different ports of the same subnetwork. The proof step "composing the two port translations gives a footprint bijection" then fails, because the composition is a bijection between V_k and V_φ(k) only when the two images coincide.
- **The reader's instance.** It uses instance 1's target D, run through the script.
  - **E_3** has components k0: x = u, anchored to {j_x}; ka: y = 2x, anchored to {j_y, j_z} onto (x, y); and kb: z = 2x + 1, anchored to {j_y, j_z} onto (x, z).
  - **E_4** has components h0: x = u; hd: y = 2x, anchored to {j_y, j_z} onto (x, y); and hc: z = y + 1, anchored to {j_y, j_z} onto (y, z).
  - Both candidates pass (F1), (F2) and (A).
  - Two bijections satisfy the premise as sent: {k0→h0, ka→hd, kb→hc} and {k0→h0, ka→hc, kb→hd}. Every paired anchor is the same subnetwork, {j_x} or {j_y, j_z}.
  - Under either bijection some pair is not of one kind. For example, kb is z = 2x + 1 on (x, z) and hc is z = y + 1 on (y, z).
  - So (ii) as sent is false. The current premise, "port translations onto the same ports of D", fails on both bijections, as it should.
- **With the current premise.** Take β = ρ′⁻¹∘ρ. By (F1) for each candidate, β[L_k(τ(a),σ(b))] = proj Sol_{λ(k)}(a,b) = L_φ(k)(τ′(a),σ′(b)) for every (a,b) ∈ C. So (ii) holds.
- **How this is recorded.** Mimo's argument bears on wording that has since been tightened. Mimo endorses the premise as sent. Mimo's endorsement does not hold there, and it bears on no current wording. Under the note, it neither reopens the tightening nor counts as support for it.

**(b) "The alternative compact wording is adequate for the claim alone."** This does not hold. The alternative reads "a component of E and a component of E′ anchored to one subnetwork of D, up to port translation, are of one kind on C". It has the same gap, and the same instance refutes it. Claude's current position, that the alternative is "not adopted as it stands", is unaffected.

**(c) The sentence after (K): "Derivations 1 and 2 use kinds in this sense."** Mimo's point holds in a narrowed form. The sentence defines kind between "a component of E and a component of E′", read through τ and τ′.

- Derivation 1's claim (line 553) compares a component of E with its anchor, a subnetwork of D. It reads that anchor on C directly, through no τ′.
- Its Corollary (line 557) speaks of "a component of the same kind" in D.

So Derivation 1 uses kinds across organizations, which is where Mimo is wrong, but it does not use them in the sentence's exact sense. The sentence is loose, and it breaks nothing. A wording change is proposed below.

**(d) "'one account' is never formally defined".** This holds in a narrowed form.

- **In file 10.** "One account" occurs only at line 561, where the colon gives it content: the pairing and the coincidence of profiles. Account(ℰ) at line 277 is a predicate on one candidate. So file 10 defines the phrase in place, and "never" is too strong.
- **In the repair.** The repair drops the colon. In the part brief and in the current wording, "the two are one account on C" is a further conclusion that no sentence defines.
- **The current qualifier.** The words "so far as (F1), (F2) and (A) reach" limit the conclusion's reach, but they do not say what it means.
- The point therefore bears on the current wording. A wording change is proposed below.

**(e) Derivation 9.** The repair's reference to Derivation 9 is apt. Two claims of Mimo's go further than the text:

- "Exactly Derivation 9's thesis" goes too far. Derivation 9 (line 613) concerns functions of an input–output projection, not answer profiles of faithful candidates.
- "The original claim was in tension with it" goes too far as well. Derivation 9 is conditional ("differ on an account claim"), so the original Derivation 2 does not contradict it.

Neither point bears on the ruling.

**(f) Derivation 10.** Mimo's reasoning holds.

- **The literal sentence fails.** Read literally, line 627 fails (K). The extended contract on which t₁ is faithful (line 623) contains displacements (lines 617 and 619). At "displace thing 1", persistence component 1's relation is replaced and component 2's is not. (K) compares signatures pair by pair (line 133), so no footprint bijection makes them coincide. The claim "On any contract containing it" is universal, so this contract is enough.
- **The replacement satisfies the current premise.** Under the exchanged transport, component 2 and thing 1's continuity subnetwork share one anchor, on thing 1's ports.
- **One gap in Mimo's check.** Mimo does not check the replacement's other assertion, that the exchange "gives a second faithful transport". It holds if S₁ treats its two persistence components alike. Line 623 builds "a component per thing" but does not say so in words.

**(g) The breakage list.** Searching file 10 finds "Derivation 2" cited only at line 627. Mimo's list of untouched parts is correct:

- Part VI;
- the Part VII cases;
- the paragraphs at lines 282–294;
- Derivations 3 to 7.

### 3.6 File 11

File 11 carries the defect unchanged:

- Derivation 2 is at lines 552–558, with the same claim text at line 554.
- The Derivation 10 sentence is at line 620.
- (K) is at line 121. That line adds only "two components of one kind on C may separate on a finer contract".
- Lines 25, 105, 143, 191, 247, 516, 602 and 606 carry the sentences quoted above from lines 23, 120, 158, 204, 260, 523, 609 and 613. Line 25 adds "(Derivation 9)".

So both instances, and Mimo's argument, hold against file 11 with only the line numbers shifted.

## Step 4. Ruling: UPHELD

The finding stands as stated, and so does its classification: false as stated, remedied by a recorded change of claim.

1. **Both counter-instances satisfy every stated assumption.** This is checked against lines 108, 120, 158, 204 and 248, and in exact arithmetic for all real c.
2. **Half (a) fails on them under every reading the text supports.** It fails for bijections, for existential pairing, and for subnetwork partners in both directions for instance 2. Half (b) follows from (A).
3. **No words of the theory state the only reading that would save half (a),** which is pairing through shared anchors. The words "their components", the colon at line 561, the title and line 23 speak against it.
4. **"Immediate from Derivation 1 and (A)" omits the pairing step.** Derivation 1 (line 555) relates each component only to its own anchor.

The ruling follows from these checks, not from Mimo's verdict line.

Mimo's errors do not touch the finding. There are five small slips:

- the one misquotation;
- "precisely when an anchor merges components";
- "non-input components";
- the incomplete description of the projected relations;
- "the only one that typechecks".

Two further claims about the repair fail:

- that (ii) as sent is valid;
- that the alternative wording is adequate.

## R4. Further counterexamples

The part asked for none, and Mimo offers none as such. Its remarks on Derivation 10, on the sentence after (K), and on "one account" are variants of F1 or comments on the repair. They are checked under F1 above, and none is a new finding.

## R6. The repair: changes, with reasons

**The premise of (ii): no change.** The current premise ("port translations onto the same ports of D") stands.

- Mimo's endorsement of the premise as sent bears on wording that has since been tightened. It fails there on the reader's instance in 3.5(a).
- It neither reopens the tightening nor counts as support for it.

**The smaller alternative: no change.** It stays "not adopted as it stands". Mimo's praise of it fails on the same instance.

**Change A: the conclusion of (ii) gives "one account" its content.**

- **Prompted by** Mimo's reply to part F1, point 4, "Assessment of costs". The change comes after the cross-examination.
- **Reason.** File 10 defines "one account" only through the colon at line 561. The repair drops that colon, so the qualified conclusion names a relation that no sentence defines.
- **The change** restores the colon construction and adds no new claim.

Replace

> …then k and φ(k) are of one kind on C for every k; so far as (F1), (F2) and (A) reach, the two are one account on C.

with

> …then k and φ(k) are of one kind on C for every k; so far as (F1), (F2) and (A) reach, the two are one account on C: φ pairs their active components, each pair of one kind on C, and by (i) their answer profiles coincide.

**Change B: the sentence after (K) says how Derivation 1 uses kinds.**

- **Prompted by** Mimo's reply to part F1, point 4, the breakage check on Derivation 1. The change comes after the cross-examination.
- **Reason.** Derivation 1 compares a component of E with an anchor subnetwork of D, read on C directly. That is not a comparison of a component of E with a component of E′ through τ and τ′.

Replace

> A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense.

with

> A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense, and Derivation 1 compares a component of \(E\) with its anchor \(\lambda(k)\) in the same way, the anchor's hidden ports projected away and its signature read on \(C\) directly.

**Everything else is unchanged:**

- (i);
- the proof, which is valid under the current premise;
- "Without the premise of (ii) nothing more follows …";
- the Consequence;
- the Derivation 10 replacement.

**A note from the reader, not prompted by Mimo, with no change proposed.** The Consequence says "two faithful candidates". Line 204 defines "faithful" for a transport, by "the component and global fidelity conditions of Part V". It is not stated whether (A) is among those conditions. The claim's premise includes (A).

## For the side-by-side comparison

This reading started from Claude's positions after Atria's reading, as the note requires. Atria's reading started from the positions frozen at 15:35 UTC. The comparison must say so.

- **The premise.** Mimo, which saw only the wording as sent, did not find the port-image gap that the current premise closes. It endorsed the as-sent proof.
- **What Mimo adds.** The two looser points that survive in narrowed form, on "one account" and on the sentence after (K), bear on wording that is still current.

## Files

- `/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s88m/f1_check.py`: the exact-arithmetic check, run and read for this note.
- `/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s88m/f1_theory.txt`: the brief's theory text, confirmed identical to file 10 with `cmp`.
