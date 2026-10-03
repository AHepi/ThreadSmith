# S135 The owner's machine: general rules to addition. How it will be built and tested, written before building

*Log S135, 3 October 2026, decision S90. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). Written and committed before any of the machine's code exists. Nothing in the theory (text 107, the formal core, claims and program after round 4), any S108 to S134 file, the decisions file, the S61 terms, the S133 or S134 material or `authority/` is written. No outside model, no network, no Avida, no book file opened. The theory is cited from text 107 by line ("L405"), the formal core by definition id.*

The owner's words (S90): "No. The agent didn't do what I wanted. I wanted a set of general rules that could be run autonomously to recognise objects, understand displacement, understand object permeance, have a general notion of amounts of objects, then represent addition with those rules." The goal behind it (S88): "the goal is to build something that can construct first."

## 0. In short

- **What is built**: a small program in plain Python (standard library only; no neural network; no outside model; deterministic from a seed) that lives in a 16 by 16 grid world with coloured blobs and a screen, and runs on its own through a schedule of scenes the world generates from a seed. It sees only the grid, frame by frame.
- **Four general rules, handed in by us** (declared): recognise objects; displacement; object permanence; amounts. Each is a separate, switchable module with its origin logged as HANDED IN.
- **The fifth rung, represent addition, is not written by us.** The machine starts with the expectation the four rules give it (the amount when the screen lifts is the number of objects it is tracking behind the screen). We give it tasks where tracking individuals fails (more objects behind the screen than its tracking can hold). Its predictions fail; from its own ledger it assembles a repair, a relation over held amounts alone, within a small rule language we declare (sums and differences of held amounts), checks it against everything it has seen, and keeps it as a held rule used thereafter. Its origin is logged as BUILT, with the failures that drove it.
- **Two ways of forming the rule, side by side on the same ledger**: the built way (the old expectation held as the target, the correction computed from the failures, every rule that fits kept as a rival until only one is left) and the found way (the first rule in a fixed list that fits the ledger). The order-shuffle check shows which depends on the order of the list.
- **Tests**: the four rules alone; the amounts tests of the infant studies' kind (one joins one behind the screen; the screen lifts on two, on one, on three; two take away one; amounts never shown while building); the building itself with its ledger; knock-outs (permanence removed; the built rule removed; sham; restore); the order-shuffle check; the same-final-frame check.
- **What the verdict can be, by the theory's present reading**: rules 1 to 4 handed in (declared at the machine's boundary; worked out by us). The addition rule built at the machine's own boundary within a class we named (S118's grade 2 for the class), if the five witnesses hold; found, if only the found way produced it or the result moves with the order. Whether "built within a class we named" is worked out in the owner's sense is the question S134 put to the owner, still open (S90's reading).

## 1. The world

**The grid.** 16 by 16 cells. Each cell holds one number: 0 empty; 1 to 6 the colours of objects used while the machine builds; 7 and 8 colours kept back for the tests (never seen while building); 9 the screen.

**The screen** (the occluder). A rectangle of columns 3 to 12 and rows 6 to 15 (10 by 10, resting on the bottom edge, the floor). When it is down it is drawn over everything inside it; when it lifts it is gone and what is behind it shows.

**Objects.** Blobs of one colour: 1 by 1 while building; 1 by 1, 2 by 2, 1 by 2 and 2 by 1 in the tests (sizes never seen while building). An object moves at most one cell per frame in each direction. Objects are kept at least one empty cell apart from others of their colour, except in the one recognition test that shows what rule 1 does when two touch.

**Edges.** Objects may enter and leave the world at the top, left and right edges. The bottom edge is the floor; nothing leaves through it.

**Scenes**, generated from a seed (no scene is written by hand; the generator draws the kind and every number). Each scene begins as a new scene: the machine's short-term state (its tracks, its hidden objects, its held amounts for the scene) is cleared; its long-term store (its rules and its ledger) carries on. Kinds:

1. **Walk.** One to four objects move in the open, bounce off walls, sometimes turn, and sometimes jump (a jump of more than two cells, which no continuous motion makes). No screen.
2. **Pass behind.** The screen is up over an empty stage, comes down, and one object (or two side by side) walks across behind it from one side to the other. Variants: it comes out where and when expected; it never comes out (it stopped behind the screen; or, in the tests only, it vanished); a different one comes out (in the tests only: a red one goes in, a blue one comes out). The screen lifts at the end.
3. **Amounts** (the infant studies' kind). The screen is up; some objects rest on the stage (the "before" amount, 0 or more). The screen comes down over them. A group of objects appears at the top in one row, visible together, and descends behind the screen (the "added" amount). Sometimes a group then walks out from behind the screen, one above another, visible together, and leaves at a side edge (the "taken away" amount). The screen lifts and shows what is behind it (the "after" amount). In the tests only, the world can play an impossible event: at the lift it shows one more or one fewer than are really there, as the infant studies did.

**While the machine builds, the world is honest**: no impossible events, no vanishing. The impossible events, vanishings and new colours and sizes appear only in the test phases, after building, with building paused. This is declared now.

**Building schedule.** 120 scenes from seed 1350, mixed: about half amounts scenes, a quarter pass behind, a quarter walk. In amounts scenes while building: before 0 to 4, added 1 to 3, taken away 0 to 2 (never more than there are). **Test amounts** go beyond: before up to 9, added up to 5, taken away up to 4, totals up to 14; pairs never in the building schedule are marked as unseen.

The world keeps a truth log (true identities, positions, true amounts). **The machine never reads it**; only the scoring does.

## 2. The four general rules, handed in by us

Each rule is written in plain words, then in code as its own module that can be switched off, and carries an origin record: **HANDED IN by the builders (Claude, for the owner, S135); written outside the machine, run inside it.**

**Rule 1, recognise objects.** A connected region of cells of one colour (touching side by side) is one object. Empty cells are not objects. The screen's colour is known to the machine as the screen (handed in with rule 1), not as an object. Declared limit: two objects of one colour that touch are seen as one.

**Rule 2, displacement.** An object seen at a new place is the same object moved, if it has the same colour and is the nearest such object to where that object was expected, within a bounded step (2.5 cells). Each tracked object carries its last move; its next place is predicted as its place plus its last move. When the object is found away from the predicted place (more than three quarters of a cell), that is a **violation** of the prediction (D12.7), logged. An object that cannot be matched and was not at the screen or an edge has **vanished in plain sight** (a violation); a new object away from the screen and the edges has **appeared from nowhere** (a violation). Objects entering or leaving at an edge, and every object in the first frame of a scene, are not violations.

**Rule 3, object permanence.** An object that goes out of sight at the screen is still there, at its last predicted place, kept behind the screen (its predicted place moves with its last move but cannot leave the screen or pass the floor). If its predicted path carries it out of the far side, it is **expected to come out** there at that frame; if it does not appear within two frames, that is a violation ("did not come out"), and it is then held at rest behind the screen. An object that appears at the screen's edge is matched to a held one of the same colour (nearest); if none of that colour is held, that is a violation ("a different one came out"). When the screen lifts, a held object not found is a violation ("was not there"). **Capacity, declared**: the machine can hold at most **three** individual hidden objects at once, each with its place and colour (when a fourth goes behind, the oldest is dropped and the drop is logged). This limit is ours, chosen so that tracking individuals fails for larger amounts (the record's infant material says infants track up to about four items; we do not claim to model infants). Rule 3 also lets the machine keep an **amount** for a region it can no longer see (below): what went out of sight is still there. With rule 3 switched off, nothing out of sight is kept, neither individuals nor amounts.

**Rule 4, amounts.** The amount in a region, or in a set of objects picked out at one moment, is the number of distinct tracked objects in it, including those held behind the screen through rule 3. An amount is held as a number the machine can compare with another (equal, more, fewer), and is general: it does not depend on colour, size or place. The machine records, for each screen scene, these held amounts:

- **before**: the amount on the stage at the last frame the stage was seen (the frame before the screen came down), kept while the screen is down (needs rule 3);
- **added**: the amount in the set of objects that went out of sight at the screen in one frame;
- **taken away**: the amount in the set of objects that came out from behind the screen in one frame;
- **tracked**: the number of individual objects held behind the screen (rule 3, at most three);
- **after**: the amount counted when the screen lifts.

A scene whose objects went behind the screen (or came out) in more than one frame has no single "added" (or "taken away") set; that row is marked not usable for amounts (rule 4 counts sets; it does not add counts). The amounts scenes the world generates have one group each way.

**What the four rules give the machine before anything is built.** Its expectation for the amount when the screen lifts is **the number it is tracking behind the screen** (rule 3 with rule 4). It holds the other amounts (before, added, taken away) as numbers, but it has **no way to combine them**: no rule we hand in adds, subtracts or relates amounts. This expectation, "the amount after = the amount tracked", is held as the machine's first rule over amounts, origin HANDED IN (it is rules 3 and 4 in use).

**The theory's words for this.** The four rules are the theory's object layer and simulation layer (L175, L177; D12.6): things with boundaries and identity, whose admitted changes include "displacement, occlusion and re-identification" (L175), and predictions of what a thing will do under a change. At the machine's boundary each rule is a routine written outside it and run inside it: the process is the machine's own, its content our contribution (L427); its correspondence enters the boundary whole and is declared there (Reading C, I200); so by (R) (D12.5) **the machine does not represent these rules**; we do (at a boundary taking in us, we worked them out). That is what "handed in" means here.

## 3. What "represent addition" means here, by the theory

The content to be represented: the relation **"the amount behind the screen after a group of k more goes behind it is the amount before plus k"** (and, with a group taken away, minus that group). By the theory the machine represents it when all of these hold:

1. **A held occurrence** (D12.5, D18.1): one stored rule over amounts, kept in the machine's rule store as one thing, used for every later scene: any colour, any size, any place, any amounts.
2. **Faithful on its contract** (D12.5 with Part V's fidelity): the contract is the amounts scenes the world admits (before, added and taken away amounts, at any colour, size and place). The rule's answer must agree with the world's on every admitted case tested, **including amounts never shown while building**; and its parts must answer to edits of their parts (a part-level check, in the spirit of F1): edit one held amount (one more added, one fewer before) and the rule's answer must change as the world's does.
3. **Provenance selected or constructed** (R): a rule we wrote in would be declared, and by (R) "a declared transport does not make an occurrence represent anything" (L211). So **if we wrote addition in, the machine would not represent addition by the theory**; that is why it must form it.
4. **Prediction and violation** (D12.7): the rule predicts the amount when the screen lifts; when the world shows another amount (the impossible events: one joins one and the screen lifts on one, or on three), that is a violation, logged with its direction (fewer, more than expected). **Words**: the owner's and the infant studies' word is "surprise" (an infant looks longer). The theory keeps "surprise" for the violation of a **selected** rule at a case outside its history (D12.7; L221), and calls the failure of a constructed one a violation, which can be a recognized difficulty (Part X). So the results will say "violation (surprise, in the everyday sense)", and give the theory's word for each variant: a found rule's violations at unseen cases are surprise in the theory's sense; a built rule's are violations.
5. **Causal work** (S126's knock-out; Dependence; ProducesVia, D14.7): remove the rule after it is built and the right predictions on large amounts go; a sham edit of the same size changes nothing; restoring it brings them back.

**Layers.** Rules 1 to 3 make the object layer; rule 4 and the predictions are the simulation layer; the addition rule is a transport in the simulation layer built over the amounts of the object layer (L201: "Construction may operate on selected material", here on declared material).

## 4. How addition could be built rather than handed in

**The difficulty** (Part X, L429: a recognized difficulty is "a failure of a claimed aim"). The machine's claimed aim, handed in: predict the amount when the screen lifts. Its expectation, "after = tracked", is right while there are at most three behind the screen and fails beyond (tracking holds three). It fails also where an object it no longer holds comes out. Each failure is logged in the machine's **ledger** with the held amounts of the scene (before, added, taken away, tracked), its prediction and the amount it then counted.

**The rule language, declared now** (the class of what can be built; S118's grade 2: the class is named by us): a rule is "after = c0 + cB x before + cA x added + cT x taken away + cK x tracked", each of cB, cA, cT, cK one of -1, 0, +1 and c0 one of -2 to +2: 405 rules in all. It holds sums and differences of held amounts; comparisons are used to check a prediction against what is counted (equal, more, fewer). The language includes the old expectation itself ("after = tracked") and the relation to be built ("after = before + added - taken away"), and many others ("after = added", "after = before + 1", ...). This is the naming trap in plain view: **the relation is one of the 405 rules we let it hold**; we did not say which, and the machine is never told.

**The built way (the machine's repair).** Triggered by the first failure of its held expectation; learning stays on during the building schedule.

1. **Hold the old expectation as the target of the repair**: "after = tracked", and with it every ledger row: those where it was right (to be protected: a repair must not break them, Part XI's protected aims) and those where it failed (to be repaired: the claimed aim).
2. **Compute the failure's content**: for every row, the error of the old expectation, "after minus tracked".
3. **Assemble a correction from it**: solve, exactly (whole numbers and fractions, Gaussian elimination), for the coefficients that make "correction = c0 + cB x before + cA x added + cT x taken away + cK x tracked" equal the error on **every** row seen. The solution is a set (a fixed part plus free directions); every member of it inside the language's bounds is a rival repair. The new rule is "after = tracked + correction".
4. **If one rule is left, hold it** (origin BUILT, with the failures that forced it). **If several are left, hold them all as rivals**: predict where they agree, and say "undetermined" where they disagree (a problem in D10.1's sense, held by the machine, S134's proposal 2); each new row narrows the set. **If none is left**, no relation in the language fits: log it and keep the old expectation.
5. **Use the held rule** for every later prediction when the screen lifts, in place of tracking. After building, during the tests, learning is paused (declared), so a violation is logged and not repaired.

The procedure never draws a rule from a list: it computes the set of all rules that fit from the content of the rows. Every step is logged: which row triggered it, the error on each failed row, the rival set before and after each new row, the moment the set became one.

**The found way (the control, on the same ledger).** The 405 rules in a fixed order (fewest terms first, then the smaller constant, then a fixed order of the amounts: tracked, before, added, taken away); at the first failure, and whenever its held rule fails again, it takes **the first rule in the list that fits every row** and holds it. This is S133's reading S and S134's route (a): "selecting an already-complete answer" (S125's check of reply 04). Origin FOUND, with its place in the list.

**What the theory says each way is, on its present reading** (written now, to be checked against the run):

- **Found way**: at the machine's boundary, selected (a population: the 405 rules; a finite history: the ledger; survival: fitting every row; nothing earlier inside the boundary represents them); at a boundary taking in us, declared (we wrote the list and the survival condition). Evolved knowledge, not worked out, at either (S133, S134).
- **Built way**: at the machine's boundary, constructed within a named class, on the present reading (S134 route (b): a held target that asks no provenance, S129 K8; a binding prepared from the failure's content, not drawn from a list), if the five witnesses hold; at a boundary taking in us, constructed by the same trace, with the class ours. Worked out in the owner's sense only if the owner counts a repair checked against the machine's own record, inside a class its builders named, as worked out (S134's question, open).

**What tells them apart, by intervention** (S134 section 3.5):

- **Order shuffle**: rerun both on the same ledger with the order changed: for the found way, the list's order (50 random orders, and 50 that keep "fewest terms first" and shuffle only within it); for the built way, the order of the rows and of the amounts (50 orders). A rule picked first from a list moves with the order wherever several rules fit; a rule computed from the rows does not.
- **Same ledger without the failures**: rerun the built way on the ledger with every failed row removed. If it forms the same rule, the failures did no work.
- **No difficulty, no building**: a control schedule whose amounts never exceed three (tracking never fails). Nothing should be built.
- **Without permanence, can it build?** Build from scratch with rule 3 off: the "before" amount is lost when the screen comes down, so no rule in the language should fit; nothing built.

## 5. The tests, with what each must show

All runs from fixed seeds (building 1350; tests 2350 onward), under `timeout` and `nice -n 19`; raw output in the scratchpad, never in git.

**(a) The four rules alone** (on 200 generated scenes of all kinds, sizes and colours, impossible events included where named):

- recognise objects: the machine's count of objects in a frame equals the true number of visible objects, on frames where no two of one colour touch: expected 100 per cent; frames where two of one colour touch, reported separately (expected: counted as one, the declared limit);
- displacement: predictions of the next place right on straight runs; violations logged at turns, bounces and jumps (counted against the world's own log of those events); identity kept along tracks (a track keeps its true object): expected every jump and every reversal flagged, and no violation on a straight step in the open;
- permanence: an object passing behind the screen is expected out and re-identified when it comes out (no violation); a violation when it never comes out, when it was not there at the lift, and when a different one comes out;
- amounts: the machine's amount in the screen region (visible plus held) equals the true amount whenever at most three are behind it; beyond three, wrong (the declared limit, which the building needs).

**(b) The amounts tests of the infant studies' kind**, each run on the machine with the four rules only, after building (built way) and after finding (found way):

- one object joins one behind the screen; the screen lifts on two (expected: no violation), on one (violation, fewer), on three (violation, more);
- two behind, one taken away; the screen lifts on one (no violation), on two (violation);
- several amounts, half never shown while building (for example 4 + 3, 5 + 5, 7 + 4, 6 + 2 - 3, 9 + 5 - 4), each with the possible outcome and the two impossible ones (one more, one fewer), in new colours and sizes. Measured: the share of possible outcomes not flagged and of impossible ones flagged, for seen and unseen amounts separately.

**(c) The building of addition**: the building schedule run once with the built way and once with the found way from one start; the ledger; the failures and what each changed; the rule formed and its origin record; then its use on 300 unseen test scenes (amounts beyond the building range, new colours and sizes). The part-level check: for 100 test scenes, one held amount edited (before, added or taken away up or down by one, the world replayed with the same edit) and the rule's new answer compared with the world's.

**(d) The knock-outs**, on the same 300 test scenes, learning paused:

- permanence (rule 3) switched off: amount predictions behind the screen should fail, and so should the built rule's use (its "before" is lost);
- the built rule removed: predictions go back to tracking and fail where tracking fails (more than three behind);
- sham removal: the rule rewritten with its terms in another order and its name changed, and the ledger's oldest ten rows deleted (neither should change any prediction);
- restore: the rule put back; the predictions return.
- Also displacement (rule 2) switched off, for completeness (tracks cannot be kept from frame to frame).

**(e) The order-shuffle check**: section 4.

**(f) The same-final-frame check** (S134; the critique's clock): 50 pairs of scenes, each pair the same number of frames long and ending in the same frame (the screen down, nothing visible), with different right answers for "how many are behind the screen" (the amounts differ, the timing of the group's arrival is varied apart from the answer). A rival that reads only the frame count and the final frame gives both scenes of a pair the same answer, so it can be right on at most one of each pair (at most 50 per cent; also run as a concrete rival fitted to the building ledger by frame count). The machine answers from its held amounts with its built rule. Then the machine's held amounts for the scene are wiped at the last frame and it is asked again.

## 6. What counts as built, found or handed in, and what counts against

**Handed in**: rules 1 to 4, the screen's colour, the capacity of three, the rule language, the repair procedure, the found way's list and order, the tasks and the world, the choice of what amounts to record and when. All ours. The results list them.

**Built** (the addition rule, by the built way), on the theory's present reading, if all hold:
1. a rule is formed in the building schedule, only after the old expectation failed, and its origin record names those failures;
2. it is the same rule under every one of the 50 shuffled orders of rows and amounts;
3. without the failed rows, the same procedure does **not** reach that rule alone (it keeps rivals, or the old expectation);
4. the control schedule (never more than three) builds nothing;
5. it predicts right on at least 99 per cent of possible outcomes of the 300 unseen test scenes, and flags at least 99 per cent of the impossible ones;
6. removing it brings back tracking's failures (right on no more than the scenes with at most three behind), the sham changes no prediction, restoring it brings back the 99 per cent;
7. with permanence off its use fails wherever the "before" amount is not zero;
8. in the same-final-frame pairs it answers at least 95 per cent right, and with its held amounts wiped no more than 50 per cent.

**Found** (by the found way, or the built way if (2) or (3) fails): the rule is in the list, picked by order or by a filter. The found way's result is reported whether or not it equals the built way's: if both end on the same rule, the difference is in how, which the shuffle shows at the moments the ledger left several rules open.

**Counts against "built"**: the built way's rule changes with the order; or it forms the same rule from successes alone; or it forms a rule in the control schedule; or the knock-out does not remove the large-amount predictions; or the sham changes them.

**Counts against "represents addition"**: wrong on unseen amounts, colours or sizes; impossible events not flagged, or possible ones flagged; the part-level edits not followed.

**Counts against the design** (the test cannot tell): the found way gives the same rule under every shuffle at every step (the order then never mattered on this ledger, and the shuffle cannot separate the two ways here; reported, not hidden).

## 7. The five witnesses, as they will be checked

S125's check of reply 04, at the machine's own boundary and at one taking in us:

1. **An owned subhistory**: the building runs inside the machine (its log is the trace); the procedure is our contribution (L427). Read off the code and the log.
2. **A represented target held in the episode**: the old expectation and the counted amounts are held in the ledger before the repair. Holds on the core's reading (Held, D12.2 with T'); fails on reply 04's stricter one (the ledger is kept by routines we wrote, entered whole, I200), as S134 found for the bounded constructor.
3. **A newly prepared binding**: the coefficients are computed from the errors on the machine's own rows, not drawn from a list. The order shuffle and the same-ledger-without-failures run test it.
4. **A held representation for explanatory use**: used to predict every later lift, and the part-level edits. No claim "this is an account" is made by the machine (D13.3's ExplUse is read by hand), so at most partly.
5. **More than content-preserving transfer**: no input to the machine contains the relation; the frames show blobs, not rules. The world's code is ours, and the world keeps objects in being, from which the relation follows; the machine never reads that code (the relay trap closed: S132, S134).

## 8. What is not tested

- The machine does not build the rule language, rules 1 to 4, the tasks, the world, or the choice of what to record; it does not find a question (Argument 5; QF).
- No explanation verdict (Part V's (E), (EX)) is computed by the theory's program; the results read the theory by hand.
- Nothing about infants is tested; the infant studies are the shape of the tests only.
- One world, one set of seeds, no noise in seeing; amounts are counted exactly, never estimated; large amounts beyond 14 are not shown.
- The owner's open question (is a repair inside a class its builders named worked out, or found?) is not answered by any run.

## 9. Budget

About 1,000 to 1,500 lines of Python with self-tests in `tools/s135_the_owners_machine/`; every run under `timeout` and `nice -n 19`; the whole job well under 1 CPU-hour (the scenes are small; the estimate is minutes). The CPU time of every run is recorded.
