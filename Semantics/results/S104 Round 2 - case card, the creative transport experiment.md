# S104: Round 2 (the maths) — case card: the creative transport experiment

*Written by a Claude subagent (Opus 5.5) for the orchestrator on 27 September 2026, from about 22:40 UTC, while the runs of round 2 were going. When it was written no reply of round 2 had been opened: this agent opened nothing in `results/S104 Round 2 - returns/` and touched no process of the round. The round's reading rule and the earlier addendum were read and not written to; this card is read under `results/S104 Round 2 - addendum to the reading rule, the creative transport case, written before any reply was opened.md`, written with it. No theory text was written. This file obeys decision S23 except where it quotes the text, the case files or the owner.*

**It is a probe, not a case with a fixed verdict.** No one outside the theory has said whether this history is selection, construction, an explanation or a creative act. The card asks what the theory's own definitions make of it, and where they leave the answer open. Its classification is not a case result, and no ruling may treat it as one (the addendum, point 3).

## Contents

- What was supplied, and the rerun
- (a) The history in the theory's own terms
- (b) The definitions applied
- (c) What the classification turns on
- (d) What the case bears on, and the model's encoding
- The card's findings, as items C01–C14
- What this card does not do

## What was supplied, and the rerun

**The owner's words**, as the orchestrator relayed them: "You decide if this helps or not." Claude decided that it helps as a concrete history to classify with the theory's definitions, above all selected against constructed provenance, which the maths of round 2 (FC78, FC82, FC83, the hidden invention H05) and the external cross-examination (its section 4.2, item E14) left open.

**The files.** The owner's zip of 27 September 2026 (md5 53b57757d4a68a70baa0897e4dfafcac) held `creative_transport/README.md`, `creative_transport_agent.py` and `results.json`. They are saved unchanged in `tests/S104 Case - creative transport experiment, supplied by the owner/`, with a note of where they came from. Their md5s, the same for the zip member, the unpacked file and the saved file: README da89b7b85ec06262cadd83f4d4912557 (76 lines), script 777a50780fd6be96e04cb646980a808c (300 lines), results 2becf45d5d1abd41e8876275b361eb2c (4,982 lines). Their author is not named. The README says that "The LLM in the conversation wrote the experiment" (its lines 15–16) and that "The human experiment designer knew this was a solvable task" (line 28). The files are data: their descriptions and disclaimers are their author's words, not verdicts in the theory's terms. Below, "script Lnn" and "README Lnn" name the lines of the saved files; "Lnnn" alone names a line of the text under review, `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd).

**The script, read whole before it was run.** It uses the Python standard library only, opens no network connection, starts no process, and writes only the file named by `--out`. It builds a library of two-input Boolean functions by composing NAND over two terminals, keeping one expression per behaviour (script L63–L85). It pairs library members as sender and receiver, evaluates each pair on eight local cases of a channel whose polarity is unknown but fixed (script L88–L105), and stops at the first round with a pair that recovers the message in all eight (script L217–L236). It then runs the ablations and a check on longer words (script L139–L209, L237–L284).

**The rerun.**

- Command, from a scratchpad folder holding a copy of the script (md5 777a50780fd6be96e04cb646980a808c), with no standard input: `timeout 600 python3 creative_transport_agent.py --out <scratchpad>/ct_rerun/rerun_results.json`.
- Python 3.11.15. Start 2026-09-27T22:43:46.882Z, end 22:43:47.321Z (0.44 s); exit status 0; standard error empty; standard output md5 b859bc76f4eba79f206f69039eea240b.
- An earlier attempt the same minute ran nothing: the wrapper `/usr/bin/time` is not installed (exit 127), so the script never started.
- **Output: byte-identical to the supplied `results.json`** (`cmp` found no difference; both md5 2becf45d5d1abd41e8876275b361eb2c). Nothing else was written in the folder.

## (a) The history in the theory's own terms

**The target.** The script's task (README L9–L13) is recovery of message bits across a binary channel with unknown but fixed polarity, by a sender with one bit of state and a receiver. In the text's terms this is a target D (L141) whose organization (L85–L103) has these ports:

- m, the message bit;
- s, the previous sent level;
- b, the polarity;
- x, the sent level;
- rp and rc, the previous and the current received level.

Its components are the channel, rp = s xor b and rc = x xor b (script L93–L99), and the sender, x = e(s, m). By L109, m, s and b are inputs (the contract's edits set them), and x, rp and rc are outputs of their components. The receiver never sees b.

The channel exists only in the script's code. Reading it as "an organization of a physical system" (L193) is invention I111. The sender is one of the two things the run generates. Whether the target includes it is the choice on which (E) turns (b1, I109).

**The contract, and what changes are admitted** (L141, L159, L257).

- *The admitted changes and the polarity.* The admitted changes are the eight settings of (m, s, b), the script's `FULL_CASES` (script L89): each message bit, each previous level, each polarity. The polarity is fixed across the two levels a receiver compares. A polarity that changes between adjacent levels is left out by a stated scope ("unknown but fixed polarity", README L11–L12; "not independent evidence about other channel models", README L52–L53), as non-vacuity asks (L257).
- *The messages.* One bit per step. The later check uses every twelve-bit word from both starting levels and both polarities: 16,384 transmissions, 196,608 bits, none of them used in synthesis (script L156–L184).
- *The one predefined interface change.* The receiver's first port is first "disconnected and tied to 0" (script L98). After every no-history round has ended without a pair that recovers all eight cases, the run connects that port to the previous received level (script L217–L235; README L13: "permits one predefined interface change: previous-signal access").

**The candidates.** Pairs of two-input Boolean functions, each an expression over x, y and NAND (script L27–L60), with 16 × 16 = 256 pairs once the library is closed (script L215).

- *As run.* The sender is run as `encoder.run(previous_sent, message)`, the receiver as `decoder.run(previous_received, current_received)`.
- *In the text's terms.* An explanatory candidate (L231): an organization E, a transport t from D to E, and the commitments Γ. Here E is the target copied, with a receiver component added; Γ is the sender and the receiver; the channel and the inputs are named background (I110).

**The transports.** t = (π, τ, σ, λ) (L186–L189).

- π sends the receiver's output y to the message m and every other port to itself; τ and σ are the identity.
- λ gives the receiver the sender and the channel as its counterpart (I110).
- On this encoding, (A) at a setting is the script's own test, that the receiver's output equals m (script L104), and (F2)'s equation at a setting is the same test.
- (F1) asks more: the receiver's relation must equal the relation the sender and the channel put between the received levels and the message, over every polarity. On the eight cases (F1) and (F2) pick exactly the pairs that score 8 of 8 (CT2, below).

**The population and the evaluation.**

- *Rounds.* The library's rounds hold 2, 5, 10 and 16 behaviours (results.json `library_growth`), so 4, 25, 100 and 256 pairs.
- *Score and order.* A pair's score is the number of the eight cases in which the receiver returns m (script L102–L105). Pairs are ordered by score, then by fewer NAND gates, then by the text of the two expressions (script L108–L120). The chosen pair is the first of the first round in which some pair scores 8 (script L231–L233).
- *Without history.* The best is 4 of 8 in every round.
- *With history.* The best is 4, 5, 5 and 8 of 8 in rounds 0 to 3 (50%, 62.5%, 62.5%, 100%; results.json `trajectory`).
- *The two perfect pairs.* Of the 256 pairs, two score 8: equality at both endpoints (chosen) and exclusive-or at both. Each pair has 10 NAND gates in all. The choice between them fell to the text order of the expressions, a rule the designer wrote.
- *Everywhere computed, they agree.* The two pairs give the same result on every case computed here: the eight local cases; the twelve-bit words (0 errors each); the sixteen varying-polarity cases, case by case (8 of 16 each); and the eight first-bit cases without the reference level (4 of 8 each). They differ in what is sent: the equality sender keeps its level for a 1, the exclusive-or sender flips it.

**The novelty archive** (script L63–L85).

- *What it does.* It keeps one expression per complete behaviour (its four-row table), replacing it when a smaller expression has the same behaviour. It grows by composing every pair of archived expressions with NAND, and closes at round 3 with all 16 behaviours.
- *In the text's terms.* Variation (composition) with retention by novelty of behaviour. The retention has no target, so it asks for no fidelity to anything: L195's "a survival condition requiring fidelity on \(H\)" does not describe it. The retained parts are the material the pair search works on. L201's "Construction may operate on selected material. Selection may continue to operate beneath construction." names that arrangement, but the retention beneath is not a selection in L195's sense (items C02, C06).

**The reuse of composite components.** The parts of round k+1 are NAND compositions of the parts of round k, so composites are reused as parts. Equality and exclusive-or appear only at round 3, as compositions of round-2 composites; the round-1 parts, with no reuse, give at best 5 of 8 (results.json `no_composite_reuse_best`). In the text's terms each composition makes a new component from old ones (L103: "A changed rule is a changed component"). Whether a composition made this way is Build's "nontrivial binding construction" (L405) is invention I115.

**The interface change: a change of question or of contract?** Neither, on the text's definitions (I117).

- *What stays the same.* Target, contract and query stay as they were: CT4 runs both populations on one question.
- *What changes.* The candidate's organization gains a connected port, and the population of receivers widens to those whose output depends on the previous level. L425: "it becomes one when the account admits changes to it, and adding it is construction." The adding was done by the designer, before the run; the run only switched it on.
- *L481's clause.* The second clause of L481 applies as written: "a transport that would need a part every member of the population is built without is not in it." Without history every receiver is built without the previous level. No member of that population meets (E) (CT4), so the protocol was not merely unchosen: it was not in the population.
- *L427's example.* L427 lists "an instruction about what to read" among the work supplied from outside a system's boundary that "remains an outside contribution however it is executed inside". The previous-level access is an instruction about what the receiver reads.

**What was provided and what was not: the README's own list** (README L20–L28), in its words.

> README L22–L24 | Provided: binary input format; NAND and wiring; previous-state access; clocked symbols; the message-recovery task; exact finite evaluation; a novelty archive; and a pilot/reference signal at the start of each transmission.

> README L26–L28 | Not provided to the constructor: XOR, equality, differential coding, a final sender program, or a final receiver program. NAND composition generated them. The human experiment designer knew this was a solvable task.

results.json's `designer_supplied` lists five items to the same effect: the channel and the goal; the two terminals and NAND; the one-bit sender state and the optional receiver-history port; the archive, the exhaustive search, the finite task table and the selection rules; synchronized symbol boundaries and a starting reference level.

In the text's terms, the provided items are received content (L405, L409), each an outside contribution (L427). What the run's composition and scoring produced inside its boundary is the two endpoints.

## (b) The definitions applied

### b1. Does the chosen protocol meet (E) on the task's contract?

**On a question whose target includes the protocol's own sender: yes.** Reading R-A (I109, I110) takes that question as: which message bit was sent, read at the receiver, on the eight settings. On it the chosen pair meets every conjunct of (E) (L262):

- (F1) and (F2), with τ a homomorphism;
- (A) at 8 of 8;
- non-circular dependence: deleting the receiver leaves the answer undetermined at the baseline and at a setting where it differs from the baseline;
- non-vacuity: the baseline has a solution, and everything outside the eight settings is out by the stated scope.

This is CT1. Of all 256 pairs, exactly the two perfect pairs meet (E) (CT2). The model's (A) count equals the experiment's score for every one of the 256 pairs, and the histogram is the experiment's own: {0: 2, 2: 16, 3: 32, 4: 156, 5: 32, 6: 16, 8: 2}.

**On the channel without the sender: no pair meets (E)** (reading R-B, CT3). There the sent level is free. So no receiver's relation equals the relation the target puts between the received levels and the message ((F1) fails), and the target's solutions are not carried onto the candidate's ((F2) fails). This holds although the chosen pair's receiver still returns m at every setting ((A) holds).

What the answer turns on is whether the target includes the protocol's own sender. The protocol is not an account of the bare channel. It is an account, on a question about the designed system, of why the receiver returns the message whatever the fixed polarity: the sender writes the message into whether adjacent levels are equal, and a fixed polarity inverts both levels alike, which leaves their equality as it was. Read with Part XII, the pair is also a protocol for a task (L466's π and T), and the 16,384-word check is a finite record of its performance on the task. That check follows from the eight local cases by induction over the steps, as the README says ("The local test already covers all eight possible input cases", README L53). The text's functional transport (L353) is a result of the same shape; this is a reading, not a computation.

### b2. Is its correspondence selected?

L195, condition by condition, against the run (I113, I114).

> L195 | There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

- **A population.** Met: the pairs available at each round, as "the physics and the stated construction admit" them (L481).
- **A variation operator on the population.** In part. NAND composition varies components, not pairs, and the pairs are formed exhaustively from the archive. Reading it as a variation operator on 𝒯 is I113.
- **A finite history of pairs actually encountered.** Met in simulation: the eight settings, each evaluated for every pair (I111; "actually encountered" for simulated cases, I119 and H13). H is the whole local contract but for the baseline, which the experiment does not have.
- **A survival condition requiring fidelity on H.** The run's survival is answers on H: a score of 8 of 8. On the eight cases this picks the same two pairs as fidelity, (F1) and (F2) on H (CT2). On the four noninverted cases the two part: the score keeps four pairs and fidelity keeps two (CT5; item C04).

> L195 | The transport \(t\) is a member of \(\mathcal T\) that survived.

Met by both perfect pairs. Which one "the" selected transport is was fixed by the designer's tie-break, not by survival.

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

**The crux.** The run holds carriers of all three:

- the case table (`FULL_CASES`, script L89) carries H;
- the scoring (`evaluate`, script L102–L105, and the test that the score is 1, script L231) carries the survival condition;
- each pair's expression trees (script L27–L60) carry t's generated components.

In the ordinary sense this condition fails. In the sense of (R) (L205), a carrier represents only through a transport whose provenance is selected or constructed. For the designer's code that is the provenance of the script's writing, which the case does not supply. If that writing was declared, the code represents nothing: "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does." (L211) The condition's reading is I114.

> L195 | The population \(\mathcal T\) is part of the claim: what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Argument 3).

It works as written (b9, CT5).

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

> L411 | Construction is not selection. A selected transport has no represented target in its history; a constructed one does.

- *A represented target.* In the ordinary sense, yes. The task's query (the test that the receiver's output equals m, script L104) and the channel model are written in the run's code, and the organization t carries to (the channel model with the generated pair) is built and run for every pair.
- *Criticism.* In the text's sense, no. "An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target" (L383), and the run's scores are signals used to order pairs. No occurrence represents a defect of a pair as the premise of a criticism.

So on the ordinary sense the run's history has a represented target and no criticism: neither of L201's two profiles (item C02).

**Answer:** not selected on any reading on which the run's carriers represent what they carry. Sel holds only where nothing in the run represents t, H or the survival condition under (R): on R5 on either reading of L195, and on R3 and R4 under D12.1 alone, where only the codomain is represented (b6).

### b3. Is it constructed?

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target.

- **An episode.** Under L55 ("An episode is a history in which contracts change, and every change carries a provenance record"), the run is no episode: no contract changes in it (I117), so Con fails on every reading. Under the formal core's D13.8, any subhistory is an episode (H06; I116).
- **A construction trace** (L405): "A construction trace identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation." In the ordinary sense the run leaves one: `library_growth`, `trajectory` and the chosen expressions in results.json, and the code as the incoming carrier.
- **Build**, clause by clause:

> L405 | \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

  - *Owned by s.* Met for s the executed constructor (I112). The script's processes run inside the boundary and are the constructor's own; their content is the designer's (L427).
  - *Prepares a represented organization for explanatory use of c.* The run prepares the pair as expression trees, for use on the task. Whether recovering messages is "explanatory use" is not said (I115).
  - *A nontrivial binding construction relevant to that use.* The compositions bind archived parts into behaviours no part had. They are exhaustive and blind to the task, and no binding is made for a use; nothing in the run is the reason use L409 names for identifying a binding by its use (I115).
  - *Not a composition of content-preserving transfers.* Met: the run makes behaviours none of its inputs had. "Reconstruction by a learner is construction; relay is not" (L405). The run is not relay.
- **The target available as a represented target.** In the ordinary sense, yes (b2). In (R)'s sense, as I114.
- **L201's second profile** ("a constructed one has both"). The run has no criticism in the text's sense, so on L201's wording it is not constructed either. L411 names the represented target alone.

**Answer:** constructed exactly when the run is read as an episode (D13.8, not L55) and Build's primitives are read as met (I115), with the target represented. Otherwise not.

### b4. Is it inherited?

In part (I118). The text gives two rules:

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

> L409 | Use does not by itself construct: received content used as it was received keeps its inherited provenance.

The received parts are:

- the channel components and the input components;
- the previous-level port and the reference level;
- the query, and π's sending of the receiver's output to m.

They are used as received and keep whatever provenance the designer's history gave them, which the case does not supply. The two endpoint bindings are prepared in the run. So the transport has more than one provenance, part by part (D12.4, I54). Taken whole, "exactly one of three" (L193) needs a rule of precedence the text does not give (I53's other choice).

### b5. Is it declared?

> L199 | **Declared.** Neither of the above. The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).

Where neither Sel nor Con holds, the formal core's D12.3 gives Dec by exclusion. L199's second sentence then describes a history this one is not. The pair was not entered by its author: "Not provided to the constructor: … a final sender program, or a final receiver program" (README L26–L27). It was computed by a run the author wrote.

Whether a deterministic routine's output counts as "its content", which L427 leaves "its writer's contribution", is not said. On the reading that it does, the author entered the pair by writing the routine that fixes it; on the reading that it does not, no one did (item C01).

### b6. The classification on the model, and what it turns on

CT8 sets one history of the run by hand (I90): H the eight settings, all occurring; Θ admitting the population. It computes Sel as D12.1 has it (L195 alone) and with L201 and L411 read into it (H05), and Con as D12.2 has it.

| reading (I114, I115) | D12.1: Sel, Con | class | with L201 and L411: Sel, Con | class |
|---|---|---|---|---|
| R1: the run's carriers represent H, the survival condition, t and its codomain; Build met | no, yes | constructed | no, yes | constructed |
| R2: as R1; Build not met | no, no | neither | no, no | neither |
| R3: the designer's code declared, so it represents nothing; the expression trees represent the codomain; Build met | yes, yes | both | no, yes | constructed |
| R4: as R3; Build not met | yes, no | selected | no, no | neither |
| R5: nothing in the run represents under (R) | yes, no | selected | yes, no | selected |

"Neither" is Dec by exclusion. Every one of the four answers is reached on some reading the text leaves open. R3 under D12.1 is FC78's counterexample shape, both provenances on one history, on a history modelled on an actual run and not built to be a counterexample; with L201 and L411 read in (H05), it is constructed only. Under L55's episode (I116), every "constructed" in the table becomes "neither".

**What the classification turns on**, in order of how much it moves:

1. Whether the run's carriers of its task and candidates represent in (R)'s sense. This turns on the provenance of the script's writing, which the case does not supply. The provenance of the case's transport turns on the provenance of the transports its history's carriers hold: the loop E03 names (Rep → Con → Build → Rep), met concretely (I114; FC98; D18.1).
2. Whether blind exhaustive composition, scored against a coded task, meets Build's "binding construction" for "explanatory use" (I115; I56).
3. Whether a represented codomain excludes selection: L195 alone, or with L201 and L411 (H05).
4. Whether "episode" needs a contract change (L55) or is any subhistory (D13.8; H06, I116).
5. Where the system's boundary is drawn (I112), and whether provenance is assigned per part (I118) or to the whole transport.

**On the reading that the run's carriers represent what they carry (R1, R2):** it is not selected on either reading of L195. It is constructed exactly when Build's primitives are met and "episode" is any subhistory. Otherwise it is neither, and so declared by exclusion, with L199's description not holding of it. Part by part, the supplied parts are inherited from the designer.

### b7. Is there a represented target in the history?

In the ordinary sense, yes, twice over:

- the task (the case table, the channel model and the test that the output equals m) is written in the run's code;
- the organization the transport carries to (the channel model with the generated pair) is built and evaluated for every pair.

In (R)'s sense, it turns on the provenance of those carriers (b6, point 1). The designer's own history, in which the task was the target of the LLM's writing, is not supplied.

### b8. Is the protocol new, and relative to what?

(N) is relative to the system's own earlier repertoire, not to the world:

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

- *For s the executed constructor (I112, I120): new.* Before round 3 of the history mode, no pair the archive allowed meets (E) on the task's question (CT4: 5 of 8 at best), so none matches the protocol.
- *For s the designer, or the conversation as a whole: not new* on the README's own words: "These are familiar differential-coding conventions, rediscovered by the bounded constructor" (README L42–L43) and "The human experiment designer knew this was a solvable task" (README L28).
- *Relative to the world.* The README's "not a new-to-the-world protocol" (README L18) is about the world, and (N) has no such relation.

**Origin** (G) is Attempt ∧ New ∧ Build (L422).

- *Attempt.* Met: the run uses each pair to address the task.
- *For the constructor.* Origin turns on Build (I115).
- *For the designer.* New fails.

**Attribution** (L441): "where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain". The designer's supplied port and the run's search both ran to the result. Neither alone reaches it: without the port the best is 50%, and without the search no pair is formed. The text attributes the result to each, with no division. L25: the semantics "does not attribute an achievement to contributors beyond what a history contains".

### b9. Is anything surprise or violation? The three ablations

Prediction, violation and surprise are defined for transports to the simulation layer (L217, L223), and the receiver's output is no simulation layer (L177). Each point below uses I119 (I51's extension, and simulated cases as actually occurring).

- **On the local contract**, H is the whole contract but for the baseline. "A system whose history exhausts its contract cannot be surprised" (L223; Argument 4, L580).
- **On the twelve-bit words**, H is strictly smaller than the contract of words. Every pair that survives on H (the two perfect pairs) makes no error on any word. The population holds no differing survivor there, and "the population fixes it" (L574).
- **Training on the noninverted channel** (I121 (a); CT5).
  - *Score survival.* With survival by score on the four settings with b = 0, four pairs survive. Two recover m at 0 of the 4 inverted settings and two at 4 of 4. The value there is underdetermined by that history, as Argument 3 says (L572), and the experiment's order picks the direct pair (the sender sends m, the receiver reads the current level) by its gate count.
  - *Violation or surprise.* Carried to the inverted settings, the direct pair fails (A) and (F2) at all four, a violation under I119. It is a surprise only if its transport is selected (L221), which turns on CT8's readings.
  - *Fidelity survival.* With survival read as fidelity on those four settings (I52), only the two perfect pairs survive, and the direct pair would not have survived at all. Under I110's λ, (F1)'s counterpart ranges over both polarities (item C04).
  - *A narrower target.* On a target whose polarity cannot invert, the direct pair meets (E) (CT5): an account of a narrower question, stated before any failure (L159).
- **Polarity that may change between adjacent levels** (I121 (b); CT6). This is a different target, with a polarity port for each level, and so a new question: "the scoped result on its own question is as it was" (L335). Both perfect pairs recover m at 8 of 16 settings and neither meets (E) there. The chosen protocol's standing on the fixed-polarity question is unchanged, and the README states the scope that excludes the change (L257).
- **Omitting the reference level** (I121 (c); CT7). This is a different receiver, with its previous-level input fed 0 (the experiment's no-history receiver), on the same question. It recovers m at 4 of 8 settings and fails (A). It is not a violation of the chosen transport but another candidate that is not an account. The reference level is supplied content (README L24).

**Answer:** nothing in the history is a surprise in the text's sense. The failures of the ablations are violations only under I119, and a surprise only if the transport is selected, which turns on CT8.

### b10. A created explanation (EX), or an attribution the text would refuse?

(EX) (L447–L449) needs, among its conjuncts, a creative critical episode, and "A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response" (L429). In the run:

- *A recognized difficulty.* Arguably present in the ordinary sense: the no-history rounds end with no pair at 8 of 8, and the run registers it and switches.
- *A target available before its criticism.* Present: the task is coded.
- *A conjectural objection.* None: no occurrence represents why the no-history receivers fail.
- *A content-sensitive response.* None: the switch is fixed in advance and would be the same whatever the failure's content. It is a rule the designer wrote.

So the run holds no complete critical episode, and (EX) is not met for s the executed constructor, whatever its aims.

(P) and (EX) also take declared aims (L441, L522), and the case declares none. The task's aim, recovering messages, is a use aim, and whether any aim is explanatory is not stated. For (EX) as a whole the case is one "with a missing input, not an argument that rules a claim out" (L534). The card declares no aim, since the text asks that the input not be chosen "from the assessment wanted" (L522).

For the designer the history is not supplied. The README's paragraph on the ablations (README L55–L58) reads like criticism of the direct protocol. It is the designer's, outside the run.

To say that the constructor created an explanation, on the strength of its output and of the README's plain-language account of the protocol (README L32–L39), would be attribution from emitted text. That is what Argument 9 refuses: "The same goes for attribution from emitted text and for use inferred from delivery logs." (L616) The README's author makes no such claim: "The experiment demonstrates synthesis within a small specified language, not a new-to-the-world protocol or a validated general theory of creativity." (README L17–L18)

## (c) What the classification turns on

Each place where the text leaves the answer open is recorded as an invention in `results/S104 Round 2 - maths/inventions register - addendum for the creative transport case.md`, continuing the numbering as I109–I121. The committed registers are not written to. In short:

| id | where the text leaves it open | what it moves |
|---|---|---|
| I109 | which question the task is: the target with or without the protocol's own sender (L141, L329) | whether the protocol meets (E) at all (CT1 against CT3) |
| I110 | the candidate's organization, π, λ(receiver) and Γ (L189, L231) | CT1–CT8; CT5's fidelity result in particular |
| I111 | whether a target given only in code is "an organization of a physical system" (L193) | whether provenance is defined for the case at all |
| I112 | the system and its boundary: the executed constructor, the LLM, the human (L427, L473) | New, Build's ownership, attribution |
| I113 | the selection's parameters: population, variation operator, history, survival (L195, L481) | whether the run's search is a selection, and on which survival condition |
| I114 | "represents" and "represented target" for the run's carriers (L195, L197, L201, L211, L411) | CT8: every class, selected to neither |
| I115 | Build's primitives for exhaustive composition scored against a coded task (L405, L409) | constructed or not |
| I116 | whether the run is an episode (L55, L197) | constructed or not |
| I117 | the interface change: a wider population, not a new question (L161, L425, L481) | whether the case holds a question-finding |
| I118 | provenance per part (L405, L409, L427) | whether "exactly one" (L193) holds of the whole transport, or its provenances are more than one, part by part |
| I119 | prediction, violation and surprise for a transport not to the simulation layer (L217, L223) | whether the ablations hold any violation or surprise |
| I120 | the repertoire for (N) (L403, L416) | new or not |
| I121 | the three ablations encoded (L159, L257, L335) | CT5–CT7 |

The earlier entries the case also rests on: I04, I20, I21, I51, I52, I53, I54, I56, I78, I79, I85 and I90 of the register, and H05, H06, H09 and H13 of the check of the formalization.

## (d) What the case bears on, and the model's encoding

**The S104 formal claims.**

- **FC77** (without a physical witness, selection is met by every transport). The case's selection has a real population (256 pairs at closure) and a real composition step, so the trivial witness 𝒯 = {t} does not arise here. The model's `sel` still reads the population as {t} (H09). L481's equality ("The population is the set of transports the physics and the stated construction admit") has a concrete reading in the case: the stated construction is NAND closure over two inputs, with the receiver's interface. CT4 shows its second clause at work.
- **FC78** (exactly one of three provenances). CT8's R3 reproduces FC78's counterexample shape under D12.1 on a history modelled on an actual run; with L201 and L411 (H05) it is constructed only. Other readings give each single class. Taken whole, "exactly one" fails on R3 under D12.1, and on the rows marked neither it holds only because Dec is defined by exclusion (b5, item C01). Part by part, the answer is more than one (b4).
- **FC79** (survival is how it got there; fidelity is what it is). Nothing in the case tells against it. CT2's fidelity computations take no population.
- **FC80** (Argument 3). CT5 is an instance. With the score as survival on the noninverted settings, the survivors differ at the inverted settings, so the value there is underdetermined. With fidelity as survival no survivor differs, and the population fixes the value. The twelve-bit words are a case of the second kind.
- **FC81** (Argument 4). On the local contract, H exhausts C, and no surprise is possible (b9). Part (d) (a constructed transport, violated, is not surprised) rests on Sel excluding Con (I53). On R3 under D12.1 the case's transport is both, so that premise fails there as in FC81's counterexample. No pair outside H occurs on the local contract, so nothing further was computed.
- **FC82, FC83** (the two responses; only the construction response originative). The interface change is neither of L225's two responses as the run performs it. It does not extend H and let μ act. It widens the population by a part the designer supplied (L481), with a construction trace that is the designer's, run inside the constructor (L427). This bears on H08 (the responses L225 distinguishes are not what the model computes); item C05.
- **FC84** (every creative attribution requires construction). This holds by construction. The case's creative attribution to the constructor turns on Build (I115).
- **FC85, FC86–FC90** (newness, repair, created explanation). (N) is relative to the repertoire, and the case's New turns on the boundary (I112, I120). (EX) is not met by the run (b10).
- **FC98** (the dependence order, the loop build → prov → rep). The case makes the loop concrete (b6, point 1; I114).

**The check of the formalization.**

- *H05.* The case gives it a history: D12.1 without L201 and L411 lets R3 be both, and with them R3 is constructed.
- *H06.* The run changes no contract, so L55's reading of "episode" leaves the case with no Con on any reading (I116).
- *H08.* See FC82 and FC83.
- *H09.* The population is the set the stated construction admits; the model's {t} is not the case's population.
- *H13.* L217's "actually occurring" for simulated cases (I119).

**The external items.**

- **E14 (its 4.2)**, directly. The external reader wrote: "An evolutionary search procedure could contain representations of candidates, explicit counterexamples, and content-sensitive revision. Under the document’s definitions, that history might qualify as construction rather than pure selection." The case is such a search with represented candidates and a coded survival condition, but with no counterexample represented as a criticism and no content-sensitive revision. On the text it qualifies as selection, construction, both or neither according to readings the text leaves open (CT8). That sharpens the reader's point that "The prohibition on represented targets in selected histories guarantees a classificatory difference. It does not, by itself, establish a mechanistic irreducibility result." The case's mechanism is fixed and fully known; only its classification moves. The reader's demand ("Identify what a construction mechanism does that is not already captured by the independently specified physical processes, representations, memory, and feedback in its history") meets here a history with processes, carriers of the task, memory (the archive) and feedback (scores), whose classification turns on Build's primitives (I115), which the text leaves as primitives (I56).
- **E03** (representation and construction depend on each other): met concretely (b6, point 1).
- **E08** (surprise): the ablations' failures are surprise only if the transport is selected and read as a transport to S (b9).
- **E09** (representable, not yet classified): the case is representable, and its classification stays open, as E09 finds for infants.
- **E11** (model-based learning): the run uses a supplied channel model through a fixed procedure, with no criticism, close to what the external reader says of planning: "A system can use a learned transition model through a retained procedure without newly constructing a binding or criticizing a represented target during the relevant episode."
- **E12** (finding questions): no question is found in the case, on I117.
- **E17** (capability conditions): the supplied previous-level port is scaffolding that comes close to "supplying the very explanation or discovery being attributed": differential decoding is reading the previous level. The case bears on the text's "non-question-begging" enabling conditions (L495).
- **E22** (the proposed benchmark): the reader's benchmark asks to "fix the candidate classifications before revealing the critical interventions". This card fixes its readings (I109–I121) in writing before any reply of round 2 is opened. But its writer knew the ablations from the README, so it is not the blind test the benchmark proposes.

**The claims of the text not formalized.** NF05 (L542, (Prov)'s second disjunct) and NF07 (L201). The case does not rewrite every construction trace as a selection history. It shows one history whose classification between the two turns on readings, which bears on L201's "Neither provenance is reducible to the other" as a difference of classification (E14's words), not of mechanism.

**Can the S104 model encode the case? Yes, in the parts above.** The program is `results/S104 Round 2 - maths/s104_creative_transport.py` (md5 68a1ddfacd41cc4eca4ac5ace5acbb06). It imports the committed `model/` and `s104_external.py` (md5 98738cb462ad36481263f072a0193d13) and changes neither. It compares the md5 of the text and of the three saved case files before running, imports the saved experiment script only for its archive's rounds and its scores, and writes nothing. The command:

`cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -B s104_creative_transport.py`

Run at about 22:55 UTC: 2.1 s, exit status 0, output md5 62cac6e63f0cdc6cffac236080eed38a; a run before a tidy that removed unused variables gave the same output, byte for byte. The output, whole (the program's words):

```
CT1  (E) for the chosen pair (sender and receiver both equality) on the question p_EQ: target D_EQ (the sender in place),
     query the value of m, contract the baseline and the eight settings of (m, s, b).
     F1 yes, F2eq yes, Hom yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
     (A) at 8 of the 8 settings; the experiment's score for the pair: 8 of 8.
CT2  All 256 pairs of two-input tables, each on its own target (reading R-A):
     (A) counts per pair, histogram {0: 2, 2: 16, 3: 32, 4: 156, 5: 32, 6: 16, 8: 2}; the experiment's histogram {0: 2, 2: 16, 3: 32, 4: 156, 5: 32, 6: 16, 8: 2}; same: yes; pairs whose (A) count differs from the experiment's score: 0.
     pairs meeting (E): ['0110/0110', '1001/1001']
     pairs faithful ((F1) and (F2)) on H = the eight settings: 2; the same pairs: yes
CT3  Reading R-B, the target without the sender (x free), the chosen pair with Γ = {dec}:
     F1 no, F2eq no, Hom yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) no
     any of the 256 pairs meeting (E) on R-B: no
CT4  Per round of the archive (the experiment's grow_library), best (A) count over its pairs:
     no history round 0 (2 parts): best (A) 4 of 8
     no history round 1 (5 parts): best (A) 4 of 8
     no history round 2 (10 parts): best (A) 4 of 8
     no history round 3 (16 parts): best (A) 4 of 8
     history round 0 (2 parts): best (A) 4 of 8
     history round 1 (5 parts): best (A) 5 of 8
     history round 2 (10 parts): best (A) 5 of 8
     history round 3 (16 parts): best (A) 8 of 8
     the experiment's trajectory: - r0 0.500, - r1 0.500, - r2 0.500, - r3 0.500, h r0 0.500, h r1 0.625, h r2 0.625, h r3 1.000
     any pair of the no-history population meeting (E): no (L481: a transport that needs a part every member is built without is not in the population)
CT5  Noninverted training, as H_n = the four settings with b = 0 on the full target (reading R-A):
     survivors when survival is (A) at every pair of H_n (the experiment's score): 4; their (A) counts at the four inverted settings: [0, 0, 4, 4]
     survivors when survival is fidelity on H_n ((F1) and (F2), I52): 2; their (A) counts at the four inverted settings: [4, 4]
     the direct pair (sender sends m, receiver reads the current level) among the (A) survivors: yes; among the fidelity survivors: no
     on a target whose polarity cannot invert (b ∈ {0}): the direct pair: F1 yes, F2 yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
     the direct pair on the full target p (b ∈ {0,1}): (E) no; (A) at 4 of 8
CT6  Varying polarity (b1 for the previous level, b2 for the current), the equality pair: (A) at 8 of 16 settings; (E) no (F2 no)
CT6  Varying polarity (b1 for the previous level, b2 for the current), the xor pair: (A) at 8 of 16 settings; (E) no (F2 no)
     the experiment's changing-polarity accuracy for its chosen pair: 0.5
CT7  The chosen pair with the previous-level port fed 0 (no reference level): (A) at 4 of 8; (E) no; the experiment's first-bit accuracy 0.5
CT8  Provenance of the chosen pair's transport on one history of the run (Θ set by hand, I90): H = the eight settings, all occurring;
     Sel as D12.1 has it (L195 alone), and with L201 and L411 read into it (H05: no represented target in a selection history).
     R1  the run's carriers represent in the ordinary sense: its case table H, its scoring (the survival condition), the pair t, and the codomain; Build's primitives met
         D12.1: Sel no, Con yes => constructed;  with L201 and L411: Sel no, Con yes => constructed
     R2  as R1; Build's primitives not met (exhaustive composition is not a binding construction for explanatory use)
         D12.1: Sel no, Con no => neither (declared by exclusion);  with L201 and L411: Sel no, Con no => neither (declared by exclusion)
     R3  the designer's code declared, so it represents nothing under (R); the expression trees built in the run represent the codomain's generated components; Build met
         D12.1: Sel yes, Con yes => both;  with L201 and L411: Sel no, Con yes => constructed
     R4  as R3; Build not met
         D12.1: Sel yes, Con no => selected;  with L201 and L411: Sel no, Con no => neither (declared by exclusion)
     R5  nothing in the run represents under (R) (the designer's code declared, the trees' own correspondences not representations); Build met or not
         D12.1: Sel yes, Con no => selected;  with L201 and L411: Sel yes, Con no => selected
     faithful on H (the survival condition read as fidelity): yes
```

**What the model settles and what it does not.**

- *Computed.* Fidelity, (A), (E) and their conjuncts on every pair and target named. It matches the experiment's own numbers wherever the two measure the same thing: CT2's histogram, CT4's trajectory, CT6 and CT7's accuracies.
- *Set by hand.* Who represents what, whether Build's primitives are met, and which pairs occur (I90, I114, I115). CT8 shows what the definitions give on each setting, not which setting the history is.
- *Not encoded.* The NAND gates as components (a finer grain), the twelve-bit words as a contract of sequences, and the designer's history.

## The card's findings, as items C01–C14

Each item names the lines it bears on, the finding in one or two sentences, whether it challenges the text, and what S104 has on the same place.

- **Yes** (it names a sentence of the text and a defect in it) and **in doubt** (it may): the item goes to a checker (the addendum, point 2).
- **No** (it names no line to change, or it shows a sentence working as written): recorded here and given as context to the checker of any group whose lines it names.

Nothing here rules on an item.

| id | lines | finding | challenges | S104 on the same place |
|---|---|---|---|---|
| C01 | L193, L199 (with L13) | Where neither Sel nor Con holds (R2; R4 with L201 and L411), the case's transport has exactly one provenance only because Dec is defined by exclusion, and L199's "The transport is entered into the model by its author" and L13's "merely *declared* by whoever writes the model down" describe a history this is not: the pair was computed, not written. Whether a deterministic routine's output is its writer's content (L427) is not said. | yes | FC78; D12.3; I53, I54; H05 |
| C02 | L201, L411, L195 | L201 tells the two provenances apart by two profiles: no represented target and no criticism, or both. The run's history, on the ordinary sense of "represents", has a represented target (its coded task and the codomain it builds) and no criticism (L383). The novelty archive beneath it retains by novelty, with no fidelity condition. Neither profile, and not L195's survival condition, describes these. | yes | E14; NF07; H05; FC78, FC82, FC83 |
| C03 | L195, L205–L211 | Whether "No member of the history represents \(t\), \(H\), or the survival condition" holds of a machine search that codes its own task and scoring turns, under (R), on the provenance of the code's writing. If that writing is declared, L211 makes the code represent nothing and the condition holds; if constructed, it fails. The classification of the run turns on the classification of its carriers' history, which the case does not supply: E03's loop, met concretely. | in doubt | E03; FC98; D18.1; I56, I90, I114 |
| C04 | L195 ("a survival condition requiring fidelity on \(H\)") | The experiment's survival condition is answers at the pairs of H. On the eight cases it picks the same pairs as fidelity (CT2); on the four noninverted cases it keeps four pairs where fidelity keeps two (CT5). Read as fidelity (I52), the noninverted training is not a selection of the direct pair at all; read as answers, it is, and Argument 3 applies as written. Which extent of "fidelity" L195 asks for is I49's question. | in doubt | I49, I50, I52; FC80 |
| C05 | L225 (with L481, L427) | The interface change is a third kind of response to a failure, which L225 does not name: it neither extends H and lets μ act, nor is a construction in the system's own trace. It widens the population by a part supplied from outside the boundary. Read as a construction response by the designer, L225 covers it and leaves "by whom" to L427. | in doubt | FC82, FC83; H08; E11 |
| C06 | L405, L409 (Build) | Whether exhaustive composition, blind to the task and scored against a coded task, is "a nontrivial binding construction relevant to that use", and whether use on a task is "explanatory use", is not said. Between R1 and R2, and between R3 and R4, the class turns on it. | in doubt | I56, I115; FC83, FC84; E03, E14 |
| C07 | L55, L197 (and L429) | Con asks for "an episode" (L197). Under L55's sentence the run is none, since no contract changes in it, and Con fails on every reading. Under D13.8 any subhistory is one. The text's body does not define "episode" by itself. | in doubt | H06; I116 |
| C08 | L217–L223 | Prediction, violation and surprise are defined for transports to the simulation layer. The ablations' failures are violations or surprise only under I51's extension. | no (a finding about scope) | I51, I119; E08; H13 |
| C09 | L413–L416, L473 | (N) is relative to the system's repertoire. The protocol is new for the executed constructor and not for its designer, and the README's "not a new-to-the-world" and "rediscovered" are about the world, which (N) does not use. The sentence works as written, given a declared boundary. | no | FC85; I112, I120 |
| C10 | L429, L441, L443–L453, L522, L534 | (EX) is not met by the run: it holds no conjectural objection and no content-sensitive response. Its aims are a missing declared input. The designer's history, which may hold criticism (README L55–L58), is not supplied. | no | FC86–FC90; E09 |
| C11 | L193 (with L159) | Provenance is defined only for a transport "whose domain is an organization of a physical system". A target given only in code is a mathematical structure (L159) run on a physical computer. Whether the case has a provenance at all turns on that (I111). | in doubt | I90, I111 |
| C12 | L231, L262 (with L466) | The protocol meets (E) only on a question whose target includes its own sender (CT1). On the channel alone no pair meets (E) (CT3). For a design, (E) reaches the designed system, not the world before the design. | no (a finding about scope) | I109, I110 |
| C13 | L481, L572–L576, L195 (last sentence) | The no-history population holds no pair meeting (E) (CT4), as L481's second clause says of a part every member is built without. Argument 3 works as written on the noninverted history (CT5) and on the twelve-bit words. | no | FC80; H09 |
| C14 | L427, L441 | The previous-level access is "an instruction about what to read", L427's own example of an outside contribution. ProducedBy attributes the result to the designer's contribution and to the run's search, with no division (L441). The sentences work as written. | no | E17 |

## What this card does not do

- It rules on nothing, changes no line of the text, and moves nothing in the maths' committed files. Its inventions are recorded, not moves (decision S36).
- It says nothing about what hard to vary covers (decisions S33, S34) and nothing about where values are placed, which is the owner's question.
- It gives no verdict on the case. No one outside the theory has given one. The README's descriptions ("rediscovered", "not a new-to-the-world protocol", "This is exhaustive within that test set") are its author's, and none of them is read as the case's verdict in the theory's terms.

Written at the orchestrator's instruction, under decisions S13, S17, S18, S35 and S36. 27 September 2026.
