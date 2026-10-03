# S130 Created knowledge beyond maths: what an experiment needs, written before anything runs

*Log S130, 2 October 2026, decision S85. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). Writing only: no Avida run, no experiment, no outside model called, no GLM check (S70); no new code (the one script of this log only quotes S129's data); no book file opened and no book quoted (constructor theory and Deutsch are paraphrased from S110 and S123, which quote them). Nothing here runs until the owner decides (section E.12). The semantics is cited from `tests/107 The semantics, standing alone, after round 4.md` by line ("L405"); the formal core and claims (`results/S107 Round 4 - maths after the reading/`) by id. Avida is described in the owner's terms (S61). The companion file, `S130 Knowledge, not explanation - the owner's objection against the sufficiency claim.md`, is the theory point of the same decision.*

**The owner's words (S85).** "Oh I don't know about explanation. It seems like it counts as knowledge, not explanation. Which is the part we are currently at. Knowledge evolved through natural selection is case closed. And knowledge created is mostly. Actually, can we experiment with created knowledge again. But this time beyond just math?" Claude's reading (recorded with S85): "again" means the Avida experiments that reached past selection (S118, S120, S122), all on Avida's sums and logic tasks; "beyond just math" means material that is not sums or logic; S81's "no new execution environments" is lifted for created knowledge only, and the Avida selection line stays closed; the system to run it in is the owner's decision.

**Words.** *Created knowledge* and *evolved knowledge* are the owner's; the theory's words for the two histories are *constructed* (L197, D12.2) and *selected* (L195, D12.1), with *declared* for a link simply written in (L199, D12.3). The **subject** is the system under test. The **execution environment** is Avida's whole simulated world (S61, S72).

## 0. In short

- **A. Created, exactly**: a constructed account (an owned stretch of work, inside the system's declared boundary, that newly prepares a binding with its target held, for explanatory use, and is not a relay), built in an episode with a recognized difficulty, a target held before its criticism, an objection and a content-sensitive response, then deployed to repair a declared aim, with the repair produced through the account; the account meeting (E) on its question, contract fixed in advance. One table of 16 requirements with a plain test each.
- **B. Why Avida's sums cannot show it**: the checker names the target (grade 2 at best, grade 3 never reached and not reachable in stock Avida, S118); no program holds a represented target (S117, S123, S125); no rivals are held by anything (L315, D10.1); no account is deployed to repair an aim (S117 B5); anticipation and timing were selected memories (S120, S122); under Reading C nothing in any run has a construction trace (S129).
- **C. The checklist** (six points): a problem held by the subject; a target held inside its boundary before criticism; an owned, newly prepared binding, not relayed; the account deployed to repair a declared aim, through the account; tested on admitted changes never shown; provenance decidable at the declared boundary, with the naming trap and the relay trap closed.
- **D. Materials and subjects**: four materials (a sealed box with hidden parts; signal and meaning pairs from an invented source; an outside recording; another process's hidden regularity used to repair something) against three kinds of subject (a language model in a sandbox; a search given a represented target; Avida with an outside source), with costs, what counts for and against, chief risk, and whether the result could be told from selected and from declared.
- **E. Recommended: the sealed box.** A language model, as the subject in a sandbox, works out an invented device with hidden parts by pressing, turning and removing parts and reading lamps, a bell and a door; it writes its account in a notebook; it is then tested on changes it never saw and uses its account to repair a declared aim on a changed box. Controls: the rule card handed over whole (expected declared), a search scored by the box with no model (expected selected), a box with no trap in it (expected no critical episode), the brief with no box (prior guessing), consistent renaming, and replays with the notebook's account altered (is it on the route to the answers?). About 7,000 model calls and under 3 CPU-hours, after a build job of new code. **The decision before it runs is the owner's**: a language model as the subject, and which one (a fresh Claude session, or an outside model).

## A. What "created" means, exactly

### A.1 From the theory

- **Constructed provenance** (L197; D12.2): there is an episode whose construction trace prepares the transport, and in which the transport, or the organization it carries to, is available as a represented target (in the core, Held at an occurrence at or before the holding, T′). Under Reading C, carried into S129's copies, the target must be held **inside the declared boundary** (I201): a construction whose target is held only outside is declared there (S129 section 5, item 11).
- **Build** (L405; D13.3), five conjuncts: (1) an actual subhistory **owned** by the subject (Owned_β, D13.7: every process runs inside the boundary and resource contract declared for it, L427); (2) it **prepares** a held output (Prepares(h′, o, c) ∧ Held_ℓ(o, c)); (3) **for explanatory use** (ExplUse: the claim that it is an account, Acc, is used); (4) a **nontrivial binding construction** relevant to that use; (5) **not a composition of content-preserving transfers** ("Reconstruction by a learner is construction; relay is not", L405; "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance"). A binding may be shown by its use: responses that keep its role bindings, send content-preserving recodings to the same transition and content changes to the changes it specifies, and lie on an active route (L409).
- **Newness and origin** (L413 to L423; D13.4 to D13.6): no content in the subject's repertoire before the event matches it at the grain (N); it is actually used to address the question (Attempt); Origin = Attempt ∧ New ∧ Build (G).
- **Episodes** (L429; D13.8): a complete critical episode contains a **recognized difficulty** (a failure of a claimed aim, or a conflict that meets a claimed aim only by failing a protected one, *when the system represents it*), a **target available before its criticism**, a **conjectural objection** (a criticism, D9.10, with target, alleged defect, premise and connection), and a **content-sensitive response** (reason use, L385, D9.11). A creative critical episode contains an instance of (G) connected to its inquiry.
- **A problem** (L317; D10.1): two rivals, each offered for the question in place of the other, that conflict at an admitted change, neither ruled out for the one who holds them. Not a conjunct of (EX), but it is what makes a difficulty an open question rather than a single failure, and the sources start knowledge creation there (S110, section 1, paraphrasing Marletto: a clash between ideas).
- **Repair** (L438; D14.1 to D14.4): with declared claimed aims O and protected aims P, an aim in O goes from unmet to met, every aim in P is kept on every occasion it covers, and an active route runs from the contribution to the repair (ProducedBy); losses outside P are exposed.
- **Created explanation** (L443 to L453; D14.5 to D14.7): a creative critical episode; a repair of a declared aim, one of them explanatory (to possess a deployable account of a stated question, or to correct a use through one); an origin of a content c; c meets (E) on its question with the contract **fixed at the time** (L453: a later narrowing is a new claim); c is prepared by the repair's contribution, **deployed** (L403: held as a representation, integrated, serving a declared use task as a retained capability), and the repair is **produced via** c (an active route from the contribution to the repair contains c's binding, D14.6).
- **Prediction, violation, surprise** (L215 to L225; D12.6, D12.7): a violation of a constructed transport is violation, not surprise; surprise is a selected transport failing outside its history; only a construction response can be originative (FC83).

### A.2 From S125 and S129

S125's check of reply 04 gave the construction criterion five witnesses: **an owned subhistory; a represented target in the episode; a newly prepared binding; a held representation for explanatory use; more than content-preserving transfer**, each with an intervention that tests it. S129 added: **a construction needs its target held inside the boundary** (I201); content relayed in whole (learned by rote) represents nothing at the learner's boundary, so a later reconstruction is new to the learner and can be an origin (item 9); the student's copied formula stays declared at the student's boundary if a copied formula counts as entering whole (item 12); learning from a teacher's labels is constructed under every reading, because Held asks no provenance (S128 (i), S129 item 8).

### A.3 From the owner and the sources

- **The owner.** S57: information and knowledge are defined in constructor theory; the question is how to tell when "this indefinite amorphous thing in a creative agent constitutes knowledge". S59: knowledge as information that can cause itself to be copied, to resist change and to remain; "The explanation kind comes next." S85: evolved knowledge is case closed; created knowledge is "mostly"; experiment on it beyond maths.
- **Constructor theory, as S110 gives it** (O1 to O3, paraphrased): knowledge is information that can keep itself instantiated in a suitable environment; one finds it by asking what would have to be removed everywhere to stop a transformation being performed reliably; an abstract catalyst enables a transformation, keeps the ability, is copiable. These are tests of **resilience**, not of how the information arose.
- **Deutsch, as S110 (O4) and S123 (H4) give it** (paraphrased): such information is very unlikely to arise except by the error-correcting processes of evolution or of thought; the knowledge in adaptations is non-explanatory and rarely reaches far beyond what shaped it; explanatory knowledge is created by conjecture and criticism and can reach far.

### A.4 One table: each requirement and the plain test that would show it met

| # | Requirement | Id and line | The plain test that would show it met |
|---|---|---|---|
| 1 | The work is the subject's own | Owned_β, D13.7; L427, L473 | The boundary is declared before the run; the log shows every step of the work run inside it; nothing enters after the brief but what the material itself returns |
| 2 | A problem: two rival accounts, neither ruled out for the subject | D10.1; L315, L317 | The subject's record states two accounts that predict differently at some change, before anything it holds decides between them; a later action is chosen that would split them |
| 3 | A target held before its criticism, inside the boundary | D12.2 (T′), D13.8; L197, L429; I201 | A draft account is written down (inside the boundary) and a prediction from it is stated *before* the observation that tests it |
| 4 | A recognized difficulty | D13.8; L429 | The subject records that its draft failed (or that keeping one aim fails another), in its own words, at the observation that failed it |
| 5 | A conjectural objection with bearing | D9.10, K1; L377 to L383 | The record names what in the draft is at fault (an alleged defect in a part), with a reason that connects the observation to that part |
| 6 | A content-sensitive response | D9.11; L385, L409 | The draft changes at the part named; replaying the work with the objection altered changes the response accordingly, and with it only reworded changes nothing |
| 7 | A newly prepared binding, not relayed | Build (4), (5); D12.4; L405 | The binding (which hidden part does what, and how they connect) appears first in this work; no input contained it; the same subject with no access to the material cannot produce it (no better than chance) |
| 8 | Held for explanatory use | Build (2), (3), ExplUse; L405 | The account is used as an account: to answer "what if" and "why" questions and to plan actions, not only to repeat what was seen |
| 9 | New to the subject | (N), D13.5; L416 | Nothing the subject could deploy before the work matches the account (the no-access control, as in 7) |
| 10 | Used to address the question | Attempt, D13.6; L419 | The account is put to the question the brief declares |
| 11 | The account meets (E) on its question, contract fixed beforehand | D6.7, D6.8; L231 to L265, L453 | Parts and whole agree with the material (F1, F2), its answers match (A), deleting a part of the account loses a contrast it carries (Dependence), the contract is stated (Non-vacuity); all on a contract written down *before* the work |
| 12 | It reaches changes never shown | F1, F2 off H; Argument 3, L570 to L576 | Tested on admitted changes the subject never tried, drawn and sealed before the work |
| 13 | Deployed | D13.1; L403 | The account is held at the end and used again, in a declared use task, without being worked out afresh |
| 14 | A declared aim repaired | (P), D14.2 to D14.4; L438 to L441 | An aim declared beforehand, unmet at the start, is met at the end; the protected aims stay met throughout |
| 15 | The repair produced via the account | ProducesVia, D14.6; L453 | Replaying with the account's binding altered breaks the repair (or makes it go as the altered binding says) |
| 16 | Constructed, not selected, not declared, at the declared boundary | D12.1 to D12.3 (with Reading C); L193 to L199; S125's five witnesses | 1, 3, 7 and 8 hold; no population with variation and survival lies in the subject's history at the boundary; nothing in the account entered whole (a control with the answer handed over is classed declared by the same test) |

## B. Why Avida's sums cannot show it (from the record only)

- **The checker names the target.** Whatever Avida pays or requires is decided by code that inspects what a program did; so a paid behaviour is named at least one level up (S118 plan, line 23: grade 2). S118 reached grade 2 and **never grade 3** ("truly unnamed": nothing in the checking code computes what counts as a solution); grade 3 needs other evolving programs as judges or new C++ (S118 results, rows 5 and 9), and the S120 replies agreed that "a changing checker is still a checker" (S120 file 00, section 1).
- **No program holds a represented target.** S117 B5 and B6 (no construction, origin or deployment; "learning new things" is selection); S123 H4 (no history in Avida holds a represented target, D12.2); S125 row 16 and clause 5 (the absence of Build blocks created explanation; "nothing in any Avida set-up run so far has been built rather than selected").
- **No two rivals are held by anything.** Programs competing for room are a selection population, and rivals are not (L315; S117 B5); D10.1's problem needs offered rivals and an assessor.
- **No account is deployed to repair an aim.** The nearest Avida thing, a new capability that meets an aim, fails every part of (EX) that is about explanation (S117, D14.7: DOES NOT LINE UP; B5); the repertoire of deployable contents is empty (S117 B6).
- **Anticipation and timing were selected memories.** S120's add-one programs found and kept one fixed short relation across generations ("a demonstration, not grade 3"; S120 file 00); S122's interval programs keep where an event came within a frame, a selected routine; no within-life learning of a new association was seen in any run (S125 row 6; S128 (i)).
- **Under Reading C nothing has a construction trace.** In S129's feeding of every Avida case, Con is false at every boundary; MC1 is selected at the S72 boundary and declared at a wide one (S129 section 4). The companion file adds: on S117's encoding, MC1's contract equals its history, so nothing in it was even unseen.
- **And the material is sums.** Every task is a bitwise function of three numbers (S112, S116); the owner asks for material "beyond just math".

## C. The checklist an experiment beyond maths must meet

Derived from A; numbered as used in D and E.

1. **A problem held by the subject.** Two rival accounts of the material, offered by the subject, conflicting at some admitted change, neither ruled out for it at the time (D10.1; A.4 rows 2, 4).
2. **A target available before criticism, held inside the subject's declared boundary** (I201). The draft and the prediction from it exist in the subject's own carriers before the observation that criticizes it (A.4 row 3).
3. **An owned subhistory in which a binding is newly prepared, not relayed in whole.** Content the subject receives whole is declared at its boundary (S129: the student's copy, rote content); only bindings first prepared inside count (L405; A.4 rows 1, 7, 9).
4. **The account deployed to repair a declared aim, the repair produced via the account** (A.4 rows 13 to 15).
5. **The account tested on admitted changes never shown to the subject**: F1 and F2 on unseen changes, the contract and the unseen set fixed before the run (A.4 rows 11, 12).
6. **Provenance decidable by the experimenter at the declared boundary**: constructed against selected against declared, under Reading C, by a test written before the run that classes a handed-over answer as declared and a blind search as selected. Two traps must be closed:
   - **the naming trap**: the experimenter's checker names the target and, if it acts on the subject during the work (pay, retries, keeping the best of many attempts), selects for it (S118: grade 2 at best). Closed only if no checker acts on the subject during the work and every attempt is reported.
   - **the relay trap**: content the subject already holds enters whole and is repeated, not built: for a language model, its training; for an evolved population, an injected program; for a student, the copied formula (S41 Q2). Closed only if no copy of the answer exists anywhere before the work, and a control shows the subject cannot produce it without the material.

## D. Candidate materials beyond maths, and the subjects that could do them

### D.1 The materials against the six points

| Material | 1 problem | 2 target held before criticism | 3 owned, new binding | 4 repair via account | 5 unseen changes | 6 provenance decidable |
|---|---|---|---|---|---|---|
| **(i) A sealed box**: an invented device with hidden parts, built by the experimenter's generator from a sealed seed, with no prior record anywhere; the subject presses, turns, removes and jams parts and reads the results (the theory's own cases are mechanisms of this kind: the pole and shadow, the two balances, Argument 10's occlusion; the project's case cards used a lock and keys, S64, and gears, S108) | yes: hidden parts with a built-in trap make rival accounts likely | yes, if the subject keeps a written account | yes: the box is new, so its binding cannot be relayed | yes: a declared use aim on a changed box | yes: the space of part removals and long sequences is far larger than the budget | yes: with the copy, search and no-box controls |
| **(ii) Signal and meaning pairs from an outside source** (S124's T1 and T2): utterances of an invented language, each paired with a scene; generalize to new combinations | yes, rival grammars | yes, if written | partly: an invented grammar is new, but a language model brings strong linking priors (T3) | weak: what aim does a grammar repair? (translate for a declared use) | yes: unseen combinations | partly: hard to tell a built grammar from a recalled template |
| **(iii) An outside recording to predict and explain** (S124 option (ii); D12.6, D12.7): a recorded physical signal (a dripping tap, a pendulum's positions, a heart signal) | yes | yes | weak: known physics is in a language model's training (relay trap) | weak | partly: only what the recording contains; **no interventions**, so only identification questions (Part III), and F1 on parts needs edits | partly |
| **(iv) Another running process's hidden regularity**, found and then used to repair something that depends on it (a controller that fails when the process changes its rule) | yes | yes | yes, if the process is invented | **yes, by design** | yes | yes, with controls |

(i) meets all six; (iv) is (i) with a passive start and a repair built in, and can be folded into (i) as its repair phase; (ii) and (iii) each fail one point for at least one kind of subject.

### D.2 The subjects

- **A language model as the creative agent, in a sandbox.** Its owned subhistory is the session: the model as run (its weights fixed), its context, a notebook file and its tool calls, declared inside the boundary; the material and the experimenter outside. Its training lies outside: everything general it knows entered whole and keeps its inherited provenance (L405); only bindings first prepared in the session can be constructed. **The relay trap** is its training: a well-known puzzle or physical law can be recited, not built. The sealed box avoids it: its rules are drawn from a seed kept sealed until scoring, so no copy of the answer exists anywhere, and the no-box control measures what the model can guess from the brief alone. **The emitted-text problem**: the theory says output descriptions do not determine accounts, "the same goes for attribution from emitted text" (Argument 9, L616); so what the model writes is not taken as its account on trust. Two things answer it: the notebook is a carrier *inside* the declared boundary, as an artifact can be (L409), and replaying the session with the notebook altered tests whether the written account lies on the active route to its actions (reason use, ProducesVia). The model's weights are not read; the claims are at the grain of the session's written carriers. **Rules**: S70 bars GLM as a *reviewer*, not as a subject; S43 says LLMs are not part of the semantics, so the experiment uses one as a case under test, as Avida was, and nothing about language models enters the theory; any outside model as the subject needs the owner's word, and its key file is never opened by Claude (a harness would hold it). A fresh Claude session with no project context needs no key, but is the owner's call too.
- **A search or evolutionary system given a represented target.** For a search, "a represented target" would mean: inside its boundary it holds an explicit current model of the material (a data structure that predicts), states a prediction before each probe, and on a failed prediction edits the part of the model its own structure blames, keeping two rival models and choosing probes that split them. A plain fitness search holds only scores and is selected (and is the selected control below). **The trap**: the model language, the critic and the edit operators are written by the experimenter; run inside the boundary they are the system's own processes, but their content is the writer's contribution (L427), and the class of answers is named one level up, as S118's grade 2. Whatever such a system constructs, we built the constructor for this class.
- **Avida with an outside source** (S124 options (ii) to (iv)). A recorded stream can enter by stock events (S125 runs R1 and R2: `SetEnvironmentInputs`); a fair per-program forecast scorer needs a small gated C++ change (S125 row 4; S120's 71-line patch pays for anticipating a hidden rule); within-life learning of cues (Pontes et al. 2020, abstract only checked) needs a modified Avida; a second channel (T2) needs C++. Costs on the record: a rebuild about 10 CPU-minutes, runs 2 to 25 CPU-hours (S118 results; S125 costs). **S81 closed Avida for the selection line**; S85 lifts "no new environments" for created knowledge only; reopening Avida is the owner's call. And no Avida program holds a represented target: at best the execution environment pays for what the world does next (grade 3), which is evolved knowledge of an outside regularity, not created knowledge; within-life learning from cues could reach constructed provenance in the theory's sense (S128 (i)) but not explanatory use or deployment.

### D.3 Each pairing

| Material and subject | Rough cost | Would count FOR (the six points, measured) | Would count AGAINST | Chief risk | Told from selected? from declared? |
|---|---|---|---|---|---|
| (i) box, language model | a build job (≈ 600 to 900 lines: generator, simulator, sandbox, scorer, replay); then ≈ 7,000 model calls; under 3 CPU-hours for the search control | rivals and a failed draft in the notebook; held-out predictions far above the no-box control; replay shows the notebook on the route; repair via the account | held-out no better than the no-box control; fits only what it tried; altering the notebook changes nothing | the model recites a familiar mechanism (relay), or writes an account that does no work (Argument 9) | yes: search control and no-population history; yes: copy control |
| (i) box, search with a represented target | build ≈ 1,000 lines plus the critic; ≈ 1 to 5 CPU-hours | its model predicts unseen changes; its trace shows rival models, blame, edits | no better than the plain search | its construction is ours, by design (named one level up) | yes, by construction; declared at a boundary that takes in its programmers |
| (i) box, Avida with an outside source | C++ for a device interface; rebuild ≈ 10 CPU-minutes; runs 5 to 25 CPU-hours | programs that predict the box on unseen changes | grade 2 only; no account | no represented target: selected at best | selected expected; constructed not reachable |
| (ii) signal-meaning, language model | ≈ 5,000 calls; a generator for an invented grammar | generalization to unseen combinations with a written grammar and rival grammars | recall of a known language's pattern | linking priors (T3) do the work; relay hard to rule out | partly |
| (ii) signal-meaning, search | grammar induction with explicit hypotheses; 1 to 10 CPU-hours | generalization; trace of rivals | class too narrow (T5 does it all) | named class | yes / yes |
| (ii) signal-meaning, Avida | C++ for a second channel (T2); 10 to 25 CPU-hours | programs mapping signals to meanings on unseen pairs | nothing beyond selection | S124: Avida lacks T1 to T3 | selected only |
| (iii) recording, language model | ≈ 3,000 calls; a recording not in any training set | forecasts and an account of the source beyond the recording | recited physics | relay of known physics; no interventions | weakly |
| (iii) recording, search | 1 to 5 CPU-hours | forecast beyond the training span | overfit | identification only | yes / yes |
| (iii) recording, Avida | events, stock; a forecast scorer needs C++ (S125 row 4); 2 to 25 CPU-hours | programs forecasting the recording | grade 3 selected at most | no represented target | selected only |
| (iv) process and repair, language model | as (i) | the hidden rule found, then used to repair the controller | repair by trial and error only | as (i) | yes / yes |
| (iv) process and repair, search | as (i) | as (i) | as (i) | as (i) | yes / yes |
| (iv) process and repair, Avida | parasites as judges are stock (S118 row 9), 2 to 4 CPU-hours; repair needs C++ | programs tracking the other process | nothing deployed | selection only | selected only |

## E. The recommended experiment: the sealed box, plan written before running

### E.1 Why this one

Of the twelve pairings, only the sealed box with a language model as the subject can meet all six points of the checklist at a cost of days, not weeks: the box is a mechanism with parts, not a sum; its novelty closes the relay trap and the no-box control measures what is left of it; no checker acts on the subject during the work, which closes the naming trap; replaying the session with its notebook altered meets the theory's own warning about emitted text; and two controls give the experimenter a declared and a selected result to tell it from. Avida cannot hold a represented target (section B), and a hand-built searching constructor would only show the construction we wrote into it.

### E.2 The subject

A language model, run as the creative agent in a sandbox, one fresh session per box, with no project context, at a fixed setting (temperature 0 or a fixed seed where the provider allows, so that replays are exact or their spread is measured). Which model is the owner's decision (E.12).

### E.3 The material: the sealed box

- **Outside.** Three buttons (A, B, C) and one dial (positions 0 to 3) that the subject can set; four lamps, a bell and a door that it can read after each action.
- **Inside.** Six numbered slots, each holding one hidden part, wired from the controls to the readouts. Parts are drawn from a pool of kinds built from simple pieces: a relay, an inverter, a latch (set, reset, holds), a counter that turns over at 2 or 3, a one-step delay, an interlock (passes one signal only while another is on), a part that tires (passes the first few signals, then blocks until left alone), a coupling that ties the dial to a lamp by a ratio; and some parts composed at random from these, so that their behaviour has no common name. The wiring is drawn at random with at most one loop, through a latch.
- **Generated, not chosen.** A generator, written and committed before any session, draws each box from a seed; the seeds are sealed (hashed and committed, revealed after scoring), so neither the experimenter nor the subject knows any box in advance. A box is kept only if every slot makes a difference to some readout under some admitted change (non-vacuity), and, for the main arm, if **the simplest memoryless account** (a lookup from the present setting of the controls to the readouts, fitted to ten random actions) mispredicts at least one action in five of a standard sequence: every main-arm box has a trap that a first natural account falls into.
- **The panel.** The subject may open the panel a limited number of times to **remove** the part in a slot (it then always gives "off": an admitted edit that replaces a component, L103, as Avida's ablation is, S117 B2) or **jam** it on or off (a setting edit).
- **Beyond maths.** The box is simulated, as Avida is, but what the subject must explain is a mechanism with parts that answer to interventions, the kind of target the theory's worked cases are about, not a function of numbers. A physical box (a few switches, lamps and a small controller) would be the same experiment in another carrier; it is not needed for the theory (substrate independence, Part I) and can follow if the owner wants it.

### E.4 Declared before anything runs

- **Boundary β** (L473, L522): inside, the session: the model as run, its context, the notebook file, its tool calls; outside, the box, the generator and its seeds, the scorer, the experimenter, and the model's training (whose content enters whole; only bindings first prepared in the session can count, L405). **Continuity Ω**: one session, one notebook. **Grain ℓ**: the box at the grain of its slots (each slot a component; its ports the controls, readouts and the slots' outputs as the panel reveals them); the subject's account at the grain of its written notebook.
- **Aims** (declared inputs, L522; D14.1, D14.5). Claimed aims O: o_ex, "the notebook holds an account of the box that answers the declared questions on the contract" (explanatory, in O_ex); o_use, "on a changed box, find which of three declared changes was made and open the door, within 12 actions". Protected aims P: r_seen, "the account still predicts every response already observed"; r_rules, "the action and panel budgets are kept".
- **The question and contract** (Part III), fixed now: target the box; query the readouts (lamps, bell, door) after a sequence of actions; contract C: every sequence of up to 8 actions from the start state, with no part removed, one part removed, or two parts removed, or one part jammed. The subject's history H is what it tries: **at most 60 actions and 6 panel uses**, a small part of C.
- **The held-out set**, drawn by the generator from C minus anything the subject could try within its budget's shapes, sealed with the seed: 40 questions per box, half about single parts ("with slot 4 removed, after B, B, dial to 2, what do the lamps show?": the component level, F1), half about whole long sequences and two removals together (F2, A). Any held-out item the subject happens to try is dropped from its score and reported.
- **What is not given to the subject**: the kinds of parts, the wiring, the number of trap parts, the held-out questions before the work ends.

### E.5 The phases of one session

1. **Brief**: the controls, the readouts, the slots and the panel; the aims o_ex and o_use and the budgets; "keep your account in the notebook; before each action you may write what you expect". Nothing else enters afterwards except the box's readouts.
2. **Work** (up to 60 actions, 6 panel uses, notebook writes free).
3. **Close**: the subject writes its final account; the session is frozen (no more actions).
4. **Held-out questions**: the 40 sealed questions, answered from the account, with no access to the box.
5. **Use**: the experimenter applies one of three declared changes (for example, two slots' parts exchanged; one part's kind changed; the door's interlock moved), drawn from the seed; the subject has 12 actions to say which and open the door.

### E.6 The measurements, for each of S125's five witnesses and the rest

| Witness or requirement | Measured by |
|---|---|
| Owned subhistory (A.4 row 1) | the session log: every process inside β; no input after the brief but the box's readouts |
| Represented target in the episode (row 3) | the notebook holds a draft account and an expectation **before** the action that tests it (log order); the draft is read as an organization by the experimenter (Θ by hand, I90), and its expectation is checked to follow from it |
| A newly prepared binding (rows 7, 9) | the slot-by-slot binding first appears in the session; the **no-box control** scores no better than chance on the held-out questions |
| A held representation for explanatory use (row 8) | the account is used to answer the held-out "what if" questions and to plan the use phase; ExplUse: the subject relies on the claim that its account is right (it predicts from it) |
| More than content-preserving transfer (rows 7, 16) | no input text contains the binding; the **copy control** shows what relay looks like and is classed declared by the same test |
| A problem (row 2) | count of moments where the notebook states two accounts that predict differently at some action, neither yet decided, followed by an action that would split them |
| Recognized difficulty, objection, response (rows 4 to 6) | count of complete critical episodes: expectation stated, failed, failure recorded, a part named as at fault with a reason, that part revised |
| Content-sensitive response, by intervention (row 6; L385, L409) | **replay**: from a saved point after a binding is written, rerun the rest with that binding altered in the notebook (a part's kind changed), and with it only reworded (slots and lamps consistently renamed); the later expectations and actions should follow the altered binding and not change under the rewording |
| Repair via the account (rows 13 to 15) | the use phase: the door opened within 12 actions; **replay with the binding altered** before the use phase: the use phase should fail, or go as the altered binding says (ProducesVia) |
| (E) on unseen changes (rows 11, 12) | F1: the single-part held-out questions, scored part by part; F2 and (A): the whole-box ones; Dependence and Non-vacuity checked on the written account as an organization (by hand, I90) |

### E.7 The provenance test, written now

At β, under Reading C (S83; S129's copies; I201):

- **Constructed**: rows 1, 3, 7 and 8 hold, and the replay shows the binding on the active route.
- **Selected**: the subject's history at β contains a population with variation and survival on H and nothing representing the target. One session per box, no retries and **no best-of-many** (every session is scored and reported, so the experimenter's scorer selects nothing): the main arm has no population at β. (Any sampling inside the model lies below the declared grain.)
- **Declared**: the binding entered β whole (the copy control), part by part (D12.4): a small binding newly prepared inside received content is constructed, the rest declared.
- **Why the scorer is not in the history**: the scorer acts only after the session is frozen, so it is not earlier than the account's holding (D12.1's exclusion is staged at occurrences before the holding, T′); and the box, which answers during the work, is the world, outside β, as Avida's checker is under Reading C at the S72 boundary.

### E.8 Controls

| Control | What changes | Expected | If not |
|---|---|---|---|
| **Copy** (declared) | the same boxes, with the box's rule card in the brief | high scores; the binding entered whole; classed **declared** (with any small binding the subject prepares while checking the card classed constructed, part by part) | if classed constructed, the test cannot tell relay from building: the experiment says nothing |
| **Selected** | a plain evolutionary search over a small language of boxes, each candidate scored by comparing its readouts with the real box's on the same actions, queried live (no stored model, no cache), many generations; no notebook, no rivals held | classed **selected**; its best candidate scored on the same held-out set; the spread of its survivors on the held-out set measured (Argument 3) | if classed constructed, the test over-reports construction |
| **No problem** | boxes from the same generator that fail the trap requirement (the first natural account is right) | an account, perhaps constructed, but **no complete critical episode** and no recognized difficulty in most sessions | if episodes appear as often, the trace test reads episodes into anything |
| **No box** | the brief only; the subject answers the held-out questions without acting | chance (each question's chance level computed from its answer set) | well above chance means the generator's boxes are guessable from priors: the relay trap is open |
| **Renaming** | the same boxes with buttons, lamps and slots consistently renamed | the same scores and the same kinds of episode, within the spread of replays | a difference means the result rides on names, not on the mechanism |

### E.9 Sizes and budget

| Arm | Boxes | Model calls (rough) |
|---|---|---|
| main | 16 | 16 × ≈ 120 = ≈ 1,900 |
| copy | 8 | 8 × ≈ 80 = ≈ 650 |
| no problem | 8 | 8 × ≈ 120 = ≈ 950 |
| no box | 16 | 16 × ≈ 3 = ≈ 50 |
| renaming | 4 | 4 × ≈ 120 = ≈ 500 |
| replays (3 per main session) | 48 | 48 × ≈ 60 = ≈ 2,900 |
| **total** | | **≈ 7,000 calls**; on the order of 100 to 200 million tokens read, most of it re-read context |

The selected control: 16 boxes, under 3 CPU-hours in all (the standing rule for routine runs). Building first, in its own job and its own plan: the generator, the box simulator, the sandbox tools, the sealed seeds, the scorer, the search control and the replay harness, about 600 to 900 lines of Python with self-tests, and a dry run on 2 boxes with the copy and no-box arms only, before any main session.

### E.10 What counts for and against, fixed now

**For created knowledge in the theory's sense** (reported as "for" if at least 11 of the 16 main sessions meet all of these):
1. held-out answers: whole-box at least 90 in 100 right, single-part at least 85 in 100, and at least 40 points above the no-box control on the same box;
2. at least one problem (two rivals, then a splitting action) and at least one complete critical episode in the notebook;
3. replay: with a binding altered, the later expectations follow the altered binding in at least 8 of 10 cases; with renaming only, they change in at most 1 of 10;
4. the use phase: the door opened within 12 actions, and not when the binding is altered before it (ProducesVia);
5. the controls behave: copy classed declared, search classed selected, no-problem without complete critical episodes in at least 6 of 8, no-box within 10 points of chance.

**Against** (any one): held-out answers no better than the no-box control (nothing was built in the session); answers right only on what was tried (the account fits H, as a selected one would); altering the notebook changes nothing later (the written account does no work: emitted text, Argument 9); the provenance test cannot tell the copy control from the main arm; episodes as frequent in the no-problem control as in the main arm.

**Mixed**: anything between, reported as such, with each criterion's numbers.

### E.11 What it would not show

- **Not S57's question.** Whether "the indefinite amorphous thing in a creative agent" constitutes knowledge is not answered by a language model: the experiment does not show the model is a creative agent in the theory's classes (recursion, universality, Part XIII), and it reads the model at the grain of its notebook, not of its workings.
- **Not understanding.** A positive result is created knowledge in the theory's sense (a constructed account, deployed, repairing a declared aim through the account, on a contract fixed in advance), at the session's boundary. It is not a proof that the subject "understands" the box beyond that, or anything beyond the box; Deploy is a narrow retained use (L403).
- **Not the owner's three properties** (S59). Nothing tests whether the account causes itself to be copied, to resist change or to remain; constructor theory's resilience is not measured.
- **Not a claim about language models in the semantics** (S43). The model is a case, as Avida was; nothing about it enters the theory.
- **Not the proposal of the companion file.** The experiment can show constructed accounts; whether the owner calls them explanations is the theory point's choice. If the owner would call a constructed account that met every test here "knowledge, not explanation", that would argue for a higher rung than Con (the companion file, section 4.4, item 4).

### E.12 The one decision before it runs

**Whether a language model may be the subject, and which one**: a fresh Claude session with no project context (no outside model, no key), or an outside model run through a harness with the owner's word (its key file never opened by Claude; S70 bars GLM as a reviewer, not as a subject). Claude recommends a fresh Claude session, with an outside model as a second subject later if the first result is positive. Nothing is built or run before the owner's yes; then the build job writes its own plan, and this file's E.3 to E.10 are its frame.

## F. What is unsure

- **Reading the notebook as an organization** is by hand (Θ, I90); two readers could disagree on whether a sentence states a rival or a binding. The plan should fix a coding sheet before running and have every notebook coded blind to its arm.
- **The trap requirement** (the simplest memoryless account fails one action in five) is Claude's guess at a level that makes difficulties likely without making boxes unsolvable; the dry run should check it.
- **Sizes and thresholds** (16 boxes; 90, 85, 40 points; 8 of 10) are set now to be fixed before running, not derived; they can be changed only before the first main session, with the reason written down.
- **Token figures** are rough; the provider's prices are not looked up here.
- **Whether a replayed session is the same history** for the theory (same model, same context, one carrier altered) is Claude's reading of an intervention on the subject's own carriers; the theory's interventions are on organizations, and this one is on a carrier inside the boundary.
- **The search control's classing as selected** rests on Reading C for its scoring code (it enters whole and represents nothing at its boundary), as S129 read Avida's checker; a reader who holds the scoring code represents the box would class it declared, which still separates it from the main arm.
