# S104 Round 2 — inventions register, addendum for the creative transport case

*Log S104, review round 2 (the maths round), 27 September 2026. Decision S36: "Also, if implementation forces invention, that needs to be recorded." Written by a Claude subagent (Opus 5.5) while the round's runs were going and before any round-2 reply was opened (see `results/S104 Round 2 - addendum to the reading rule, the creative transport case, written before any reply was opened.md`). It continues the numbering of the committed `inventions register.md` (I01–I102) and of `inventions register - addendum for the external examples.md` (I103–I108); neither is written to. The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (compared by `s104_creative_transport.py` before every run; not written to). Every quotation of the text below was compared by program with the line it names.*

**What this is.** The choices that reading the owner's creative transport experiment (`tests/S104 Case - creative transport experiment, supplied by the owner/`) against the text forced: where the text leaves open how the history is to be classified, and where the encoding on the S104 model had to fill something in. The card that uses them is `results/S104 Round 2 - case card, the creative transport experiment.md`; the program is `s104_creative_transport.py`, which imports the committed `model/` and `s104_external.py` and changes neither. As in the register, nothing invented is the text's own content, and no entry is offered as what the text means: each is a choice made so that the case could be read, open to replacement. The computations are CT1 to CT8 of the card (section d).

**Counts.** 13 inventions, I109–I121. Seven are tagged in the program (I109, I110, I113, I114, I115, I117, I121); six are choices of the card's reading with no code (I111, I112, I116, I118, I119, I120). The case also uses the register's I04, I20, I21, I51, I52, I53, I54, I56, I78, I79, I85 and I90, and the check of the formalization's H05, H06, H09 and H13, as the card says where.

## Index

| id | invention | lines | computations that use it |
| --- | --- | --- | --- |
| I109 | The case's question: the transmission with the sender in place, a port query on the message, the eight settings and a zero baseline | L141, L329 | CT1–CT8 |
| I110 | The candidate: a copy of the target with the receiver added; π sends its output to the message; λ(receiver) the sender and the channel; Γ the two endpoints | L189, L231 | CT1–CT8 |
| I111 | A target given only in code read as an organization of a physical system | L159, L193 | CT8 (by assumption) |
| I112 | The system: the executed constructor; the script's writing and the human's design outside its boundary | L427, L473 | none (reading) |
| I113 | The selection's parameters in the run: population, variation operator, history, survival | L195, L481 | CT2, CT4, CT5 |
| I114 | 'Represents' and 'represented target' for the run's carriers: five readings | L195, L197, L201, L211, L411 | CT8 |
| I115 | Build's three primitives for exhaustive composition scored against a coded task | L405, L409 | CT8 |
| I116 | Whether the run is an episode | L55, L197 | none (reading) |
| I117 | The interface change: a wider population of receivers, not a new question | L161, L425, L481 | CT4 |
| I118 | Provenance per part, applied to the case's transport | L405, L409, L427 | none (reading) |
| I119 | Prediction, violation and surprise for a transport not to the simulation layer | L217, L223 | CT5–CT7 (reading only) |
| I120 | The repertoire for (N): the constructor's and the designer's | L403, L416 | none (reading) |
| I121 | The three ablations encoded | L159, L257, L335 | CT5, CT6, CT7 |

## The entries

### I109 · The case's question: the transmission with the sender in place, a port query on the message, the eight settings and a zero baseline

**The sentence it fills in for.**

> L141 | \(D\) is the target. The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\).

> L329 | It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).

**What was invented.** The experiment states a task, not a question. The question is taken to be: which message bit was sent, read at the receiver. Target D_e: ports m (message bit), s (previous sent level), b (polarity), x (sent level), rp and rc (previous and current received levels), each two-valued; background components c_m, c_s, c_b carrying m = s = b = 0 (the baseline, which the experiment does not have), each replaced by the settings of its port (I04, I78, I79); enc: x = e(s, m), the sender in place (the experiment's `encoder.run(previous_sent, message)`); chp: rp = s xor b and chc: rc = x xor b (its `observations`). Query: the value of m (a port query, I20). Contract: the baseline and the eight full settings of (m, s, b), the experiment's `FULL_CASES`; every other setting excluded by the stated scope (I85). What the experiment asks is identification in L329's sense (the message as the feature, the received levels as the measurement, the receiver as the map f̄); the encoding writes it with a port query on m and a transport that sends the receiver's output to m (I110), not with a fibre query. Since the sender is part of D_e, each pair of sender and receiver has its own target.

**Other choices that were possible.**

- the channel without the sender (x free): reading R-B, computed as CT3; no pair meets (E), since (F1) and (F2) fail
- the task's requirement itself as the target (a component y = m), with the channel carried in computed port translations of the candidate: one target for every pair, so that the two perfect pairs could be rivals (not computed)
- a contract of all 27 partial settings (the same valuations; not computed)
- a fibre query, as I92 does for the pole

**Used by.** Code: `s104_creative_transport.py` (target, question). Computations: CT1–CT8.

**Results that depend on it.** CT1: the chosen pair meets (E); CT2: exactly the two perfect pairs meet (E), and the (A) counts of all 256 pairs are the experiment's scores, pair by pair; CT3: on R-B no pair meets (E).

### I110 · The candidate: a copy of the target with the receiver added; π sends its output to the message; λ(receiver) the sender and the channel; Γ the two endpoints

**The sentence it fills in for.**

> L189 | \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.

> L231 | The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.

**What was invented.** E: the target's ports and components copied, with a port y and a component dec: y = d(rp, rc) (the experiment's `decoder.run(previous_received, current_received)`); for a receiver without history, y = d(0, rc) with the same footprint (the experiment's first port tied to 0). π is the identity on the target's ports and sends y to m; τ and σ are the identity. λ(j) = {j} for the copies; λ(dec) = {enc, chp, chc}, the sender and the channel with no input component, rp and rc translated to themselves and y to m. Γ = {enc, dec}, the two generated endpoints; the channel and the inputs are named background. The grain takes each endpoint as one component, not as its five NAND gates.

**Other choices that were possible.**

- λ(dec) with the polarity's own component c_b as well: then the counterpart's relation changes with the settings of b, and fidelity at the four noninverted settings no longer constrains the receiver at the inverted ones (CT5's fidelity result would change)
- Γ = {dec}, the sender in the named background
- the NAND gates as components (a finer grain ℓ)

**Used by.** Code: `s104_creative_transport.py` (candidate). Computations: CT1–CT8.

**Results that depend on it.** As I109. CT5's fidelity result rests on λ(dec) in particular.

### I111 · A target given only in code read as an organization of a physical system

**The sentence it fills in for.**

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L159 | in whatever the target is: a garden, a mathematical structure, a melody or a philosophical claim.

**What was invented.** The channel, its polarity and the messages exist only in the script (its lines 88–99). They are read as the organization that the computer running the script instantiates at the grain of the program's variables (Org_ℓ, L213), so that L193 applies to the case's transport and a provenance can be asked for.

**Other choices that were possible.**

- the target as a mathematical structure the code specifies: L193 then assigns the transport no provenance, since it speaks only of transports whose domain is an organization of a physical system, and none of the case's provenance questions arises

**Used by.** The card, section b; CT8 assumes it.

**Results that depend on it.** Every provenance result of the card.

### I112 · The system: the executed constructor; the script's writing and the human's design outside its boundary

**The sentence it fills in for.**

> L427 | Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing.

> L473 | Where the system's boundary is not declared explicitly, a statement that names the system and says whether a process runs inside it or outside it declares the boundary for that process

**What was invented.** The system s is the executed constructor: the process that runs the script (its composition, archive, pairing, scoring and the switch of the receiver's port). The README's sentence "the executed agent is a deterministic symbolic constructor" (its line 16) is read as the statement that names the system (L473). The writing of the script, by "The LLM in the conversation" (README line 15), and the human's design are outside the boundary; what they supplied is an outside contribution (L427) that runs inside as the constructor's own process.

**Other choices that were possible.**

- s = the conversation as a whole: the LLM, the human and the run
- s = the run and the LLM that wrote it

**Used by.** The card, section b (Build, ownership, (N), Origin, the attribution of the result).

**Results that depend on it.** Whether the protocol is new (I120), whether a subhistory is owned (Build), and to whom ProducedBy attributes the result.

### I113 · The selection's parameters in the run: population, variation operator, history, survival

**The sentence it fills in for.**

> L195 | There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

**What was invented.** 𝒯: the pairs of archived components available at a round (4, 25, 100 and 256 pairs; the script's lines 222–226), with the receiver's interface fixed for the mode, as the stated construction admits them (L481). μ: the archive's NAND composition of archived parts (its `grow_library`, lines 63–85), which makes new components, pairs being formed from every archived part. H: the eight local cases, each evaluated for every pair. Survival: the experiment's own, (A) at every pair of H (a score of 8 of 8, lines 231–233), with ties between survivors broken by gate count and then by the text of the expressions (lines 108–120). It is read against L195's "requiring fidelity on \(H\)" by computing both.

**Other choices that were possible.**

- μ the identity and 𝒯 = {t}, as the model's `sel` has it (H09)
- 𝒯 the 256 pairs at once, with no rounds
- survival read as fidelity, (F1) and (F2) on H (I52): on the eight cases it admits the same two pairs as the score (CT2); on the four noninverted cases it admits two pairs where the score admits four (CT5)

**Used by.** Code: `s104_creative_transport.py` (CT2, CT4, CT5). Computations: CT2, CT4, CT5, CT8.

**Results that depend on it.** CT2 (same two pairs under both survival conditions), CT4 (no member of the no-history population meets (E)), CT5 (the survival conditions part on the noninverted cases).

### I114 · 'Represents' and 'represented target' for the run's carriers: five readings

**The sentence it fills in for.**

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

> L197 | in which \(t\), or the organization it carries to, is available as a represented target.

> L201 | a selected transport has no represented target and no criticism in its history; a constructed one has both.

> L211 | A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does.

> L411 | A selected transport has no represented target in its history; a constructed one does.

**What was invented.** The run holds carriers of its own task and candidates: the case table (`FULL_CASES`, line 89), the scoring (`evaluate` and the test `fraction(winner, history=history) == 1`, lines 102–105 and 231), the expression trees of each pair (lines 27–60), and the channel model (`observations`, lines 93–99). Whether each represents, in (R)'s sense (L205), turns on the provenance of its own transport, which for the designer's code is the provenance of the script's writing; the case does not supply that history. Five readings are set by hand on one history (I90): R1 and R2, every carrier represents what it carries (the ordinary sense); R3 and R4, the designer's code is declared and so represents nothing (L211), while the expression trees built in the run represent the codomain's generated components; R5, nothing in the run represents under (R). R1 and R3 have Build's primitives met, R2 and R4 not (I115); in R5 Con fails either way. Each is computed with Sel as D12.1 has it (L195 alone) and with L201 and L411 read into it (H05).

**Other choices that were possible.**

- any mixture of these (for example the case table representing H while the scoring does not)
- (R) computed for the trees from their own history: the archive keeps a component when its behaviour is new or cheaper (lines 78–82), a retention with no fidelity condition, which L195 does not describe (I113)

**Used by.** Code: `s104_creative_transport.py` (CT8). Computations: CT8.

**Results that depend on it.** CT8: selected (R4 under D12.1; R5), constructed (R1; R3 with L201 and L411), both (R3 under D12.1), neither (R2; R4 with L201 and L411).

### I115 · Build's three primitives for exhaustive composition scored against a coded task

**The sentence it fills in for.**

> L405 | \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

> L409 | A construction trace may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it

**What was invented.** Prepares, BindingConstruction and ¬TransferComposite (I56's primitives) set by hand both ways. Met: the run prepares the pair as expression trees for use on the task's question; its NAND compositions bind archived parts into components no part had (the equality and exclusive-or behaviours appear only at round 3), which is no composition of content-preserving transfers. Not met: the compositions are exhaustive and blind to the task, so no binding is made for a use; and the use is the task of recovering messages, which is not explanatory use.

**Other choices that were possible.**

- BindingConstruction identified by use, as reason use asks (L409, I56's other choice): then not met, since no response of the run is sensitive to any content of a failure beyond its score

**Used by.** Code: `s104_creative_transport.py` (CT8, the `prepares` flag). Computations: CT8.

**Results that depend on it.** CT8: R1 against R2, R3 against R4.

### I116 · Whether the run is an episode

**The sentence it fills in for.**

> L55 | An episode is a history in which contracts change, and every change carries a provenance record.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\)

**What was invented.** CT8 uses the model's reading (D13.8: an episode is any subhistory; `con` asks for no episode at all). Under L55's reading the run is no episode, since no contract changes in it (I117), and Con fails for the case on every reading of I114.

**Other choices that were possible.**

- L55's reading (H06's other choice)

**Used by.** The card, section b.

**Results that depend on it.** Every 'constructed' in CT8.

### I117 · The interface change: a wider population of receivers, not a new question

**The sentence it fills in for.**

> L425 | A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction.

> L161 | Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one.

> L481 | a transport that would need a part every member of the population is built without is not in it.

**What was invented.** The change connects the receiver's first port to the previous received level (script lines 96–99, 217–235). Target, contract and query stay as they were: CT4 runs both populations on one question. In the encoding the no-history receiver keeps the footprint (rp, rc, y) with a relation that does not depend on rp; the change widens the population to receivers whose relation does. The port was supplied by the designer and switched on by the run when its no-history rounds were exhausted.

**Other choices that were possible.**

- a change of question: the receiver's reading counted in the target, so that exposing the previous level changes D or C; it would then be the finding of a question (Argument 5, L588), supplied by the designer

**Used by.** Code: `s104_creative_transport.py` (CT4). Computations: CT4.

**Results that depend on it.** CT4: the no-history population holds no member that meets (E); the widened one holds two.

### I118 · Provenance per part, applied to the case's transport

**The sentence it fills in for.**

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

> L409 | Use does not by itself construct: received content used as it was received keeps its inherited provenance.

**What was invented.** Under I54 (D12.4), the parts of the transport are: the channel components, the input components, the previous-level port, the reference level, the query and π's sending of y to m, which are received content (the designer's) and keep whatever provenance the designer's history gave them; and the sender and receiver bindings, prepared in the run, which take the run's provenance (CT8's readings).

**Other choices that were possible.**

- one provenance for the whole transport (I53): 'exactly one of three' then asks for a rule of precedence the text does not give

**Used by.** The card, section b.

**Results that depend on it.** The card's answer that the provenances are more than one, part by part.

### I119 · Prediction, violation and surprise for a transport not to the simulation layer

**The sentence it fills in for.**

> L217 | Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\).

> L223 | Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one

**What was invented.** I51's extension (Pred_t(a,b) := Ans_E(τ(a),σ(b)) for any transport) applied to the receiver's output, and the cases the script evaluates read as pairs actually occurring (Occurs set by hand, H13), so that the ablations' failures can be asked about as violations or surprise.

**Other choices that were possible.**

- the text's own scope: the receiver's output is not a simulation layer (L177: its queries are predictions of what a port of P will take), and nothing in the case is a violation or a surprise in the text's sense

**Used by.** The card, section b.

**Results that depend on it.** Every use of 'violation' and 'surprise' in the card.

### I120 · The repertoire for (N): the constructor's and the designer's

**The sentence it fills in for.**

> L403 | The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

**What was invented.** For s the constructor (I112), its repertoire before the round that yields the protocol holds at most the pairs of the archive's earlier rounds, none of which meets (E) on the task's question (CT4: 5 of 8 at best), so none matches the protocol. For s the designer, the README's own words ("These are familiar differential-coding conventions", "The human experiment designer knew this was a solvable task", its lines 42–43 and 28) are read as the protocol's content being deployable in its repertoire.

**Other choices that were possible.**

- the designer's repertoire left open, since the conversation that produced the script is not supplied
- the constructor's repertoire read through Deploy with (R), which asks I114's question again

**Used by.** The card, section b.

**Results that depend on it.** New: yes for the constructor; no for the designer or the whole conversation.

### I121 · The three ablations encoded

**The sentence it fills in for.**

> L335 | permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was.

> L257 | every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently.

> L159 | a narrowing adopted after a failure is a new claim at a new index (Part VIII).

**What was invented.** (a) Training on the noninverted channel: as H_n, the four settings with b = 0 on the full target (for Argument 3), and separately as a target whose polarity cannot invert (b ∈ {0}). (b) Polarity that may change between adjacent levels: a target with two polarity ports, b1 for the previous level and b2 for the current, and sixteen settings (a new question). (c) The missing reference level: the receiver's previous-level input fed 0 (the script's `decoder.run(0, received)`, line 206), which is also its no-history receiver.

**Other choices that were possible.**

- (a) as a contract narrowed on the full target: then (F1)'s counterpart still ranges over both polarities (CT5)
- (b) as edits of the original target excluded by the stated scope "unknown but fixed polarity" (README lines 11–12)
- (c) as a boundary condition of E rather than a changed receiver

**Used by.** Code: `s104_creative_transport.py` (CT5, CT6, CT7). Computations: CT5, CT6, CT7.

**Results that depend on it.** CT5, CT6, CT7.
