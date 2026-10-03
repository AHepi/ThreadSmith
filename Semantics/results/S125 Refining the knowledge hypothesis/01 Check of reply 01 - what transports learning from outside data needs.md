# 01 Check of reply 01: what transports learning from outside data needs

*Log S125, 2 October 2026 (decisions S77, S78, S79). One Opus 5.5 agent doing the whole S125 job (S56, S68; no subagent or workflow; no outside model; no GLM check, following S70's latest word on GLM). The reply is `tests/S123 Returns from GPT 6 Astra/01 Return - what transports learning from outside data needs.md` (md5 d69537bc9be00435d1d534b0531f0813, the same bytes as the owner's upload), kept unchanged; it is cited "R01 L" + line. The brief is `tests/S123 Briefs for GPT 6 Astra/01 ...md`. Avida's source was read at commit 47f13dad (`avida-core/source/` unless stated), read only. The semantics is `tests/107 The semantics, standing alone, after round 4.md` (the attached copy has the same md5, c7af964c329ab7959243405d394e6574), cited "L" + line, and its formal core (`results/S107 Round 4 - maths after the reading/formal core, after round 4.md`) by definition id and "core L". The plan followed is the S123 refinement plan (written before sending), with the S125 task's folder and file names in place of the plan's `S123 Checking the Astra returns/`. Verdicts: **holds**, **in part** (content right, a detail off, or only part of the claim stands), **does not hold**, **unverified** (could not be opened).*

## 1. What it offers, against the brief

| The brief asked for | The reply gives | Where |
|---|---|---|
| For owner, at most 150 words | 93 words; plain | R01 L5-9 |
| A hypothesis and what counts against it | An *enabling* hypothesis: the whole execution environment can acquire a retained, source-dependent capability when an outside observation or consequence reaches variable candidates, affects what is retained, and can affect later behaviour; with counter-observations (no loss when every source-to-update route is cut; equal gain with source feedback replaced by a source-independent control; gain explained by a shortcut) | R01 L13-15 |
| The L1-L7 table completed, with file and line | Done for every row, with a second table on code and patches, a third on what each history would need | R01 L55-99 |
| The composite L1 then L3, and the smallest set | The composite is not defined as written; the smallest set is a set of causal jobs, with a new link our list lacked (source-dependent update to retention) | R01 L101-111 |
| Five tests, each with set-up, expected outcome, control, counter, cost, new C++ | All five, plus a rig check; costs 23.8 CPU-hours in all | R01 L134-226 |
| What it ran | Source inspection only, with commands and output; no Avida build or run | R01 L228-262 |
| Sources marked | A register C1 to C10 of source ranges; outside sources marked checked or not | R01 L264-292 |

It also opens with eight **corrections** of our claims (R01 L25-41); each is judged in `00 Corrections of our own claims.md`.

## 2. Its claims about Avida's source

| # | Claim | Source at 47f13dad | Verdict |
|---|---|---|---|
| 1 | The three-number cycle is a configuration: `SetupInputs` also takes specified inputs (which "trump everything"), a true-random mode and a deterministic test set (R01 L27) | `main/cEnvironment.cc` 1252-1295 | holds |
| 2 | Cyclic read; its receipts lines 216, 217 | `main/cPopulationCell.h` 214-218 | holds (grep reproduces 216, 217) |
| 3 | `SetEnvironmentInputs` takes exactly three integers whose top bytes must be 0F, 33, 55, applies them to every cell and resets programs' input buffers; receipts lines 1014, 1020 | `actions/EnvironmentActions.cc` 999-1040; `main/cPopulation.cc` 7434-7447; `cOrganism.h` 294 | holds (grep reproduces 1014, 1020; confirmed by run, section 5) |
| 4 | So a driver can put an encoded recording into an events file with no C++ | as 3 | holds (confirmed by run, section 5: event-set inputs reach the programs and change the run) |
| 5 | `IO` outputs first, then reads the next input into the same register | `cpu/cHardwareCPU.cc` 4188-4201; `main/cOrganism.cc` 368-403 | holds |
| 6 | `nand` and the logic checker | `cpu/cHardwareCPU.cc` 3018-3024; `main/cTaskLib.cc` 369-447 | holds |
| 7 | Default division (split) resets the processor when epigenetic inheritance is off | `cpu/cHardwareCPU.cc` 1813-1839; `main/cAvidaConfig.h` 379 (`DIVIDE_METHOD` 1) | holds |
| 8 | The default also passes merit to the descendant program | `main/cAvidaConfig.h` 383 (`INHERIT_MERIT` 1); `main/cBirthChamber.cc` 249-254; `main/cPhenotype.cc` 349-352 | holds |
| 9 | Optional modes keep or pass registers and the local stack | `main/cAvidaConfig.h` 380 (`EPIGENETIC_METHOD` 0 default); `cpu/cHardwareCPU.cc` 813-831, 1831-1834, 2133-2146; `main/cPopulation.cc` 959-967; `cpu/cHardwareCPU.h` 67-80 | holds (confirmed live by run E1, section 5) |
| 10 | Pay accumulates as a bonus and becomes merit at division; immediate merit increases are optional | `main/cAvidaConfig.h` 559 (`MERIT_INC_APPLY_IMMEDIATE` 0); `main/cOrganism.cc` 490-493; `main/cPhenotype.cc` 1644-1646, 824-843 | holds |
| 11 | Programs that do no task still replicate; task requirements for division are optional | `main/cAvidaConfig.h` 399-403 (`REQUIRED_TASK` -1, `REQUIRE_SINGLE_REACTION` 0 and others); `main/cOrganism.cc` 788-844 | holds |
| 12 | The heads instruction set reports no membership label to a program | `support/config/instset-heads.cfg` (26 instructions, no `IO-Feedback`) | holds |
| 13 | `IO-Feedback` exists and pushes -1, 0 or +1 by the change in bonus | `cpu/cHardwareCPU.cc` 236, 4214-4250 | holds |
| 14 | Resource sensing, collecting and state-grid instructions are registered | `cpu/cHardwareCPU.cc` 241-265, 330-333 | holds |
| 15 | `cEnvironment::TestOutput` calls `cTaskLib::SetupTests` | `main/cEnvironment.cc` 1328 | holds |
| 16 | The top bytes 0F, 33, 55 show all eight three-input rows across their bit positions | arithmetic (bit 7 to bit 0 give 000, 001, 010, 011, 100, 101, 110, 111); the source's own comment, `main/cEnvironment.cc` 1284-1285 | holds |
| 17 | Commit identity 47f13dad...b16 | `git rev-parse HEAD` in the clone | holds |
| 18 | The pay and scheduling chain (C6: `cEnvironment.cc` 1314-1405, 1664-1714; `cPhenotype.cc` 1493-1523, 1644-1678; `cOrganism.cc` 485-505; `cPopulation.cc` 613-618, 653-660, 914-940, 1388-1389, 8003-8019; `cAvidaConfig.h` 557-559) | the ranges named | holds |
| 19 | Variation, instruction weights and limits (C10: `cpu/cHardwareCPU.cc` 7130-7166; `cpu/cInstSet.cc` 155-170, 215-240, 301-311; `cpu/cHardwareBase.cc` 140-237; `include/public/avida/core/Definitions.h` 28-35) | the ranges named, spot-read | holds |

**19 hold, 0 in part, 0 do not hold.** The sensing range it cites (4352-4382) starts inside `DoSense` (which begins at 4293); the content is right.

## 3. Its claims about the semantics

| # | Reading | Against | Verdict |
|---|---|---|---|
| S1 | L4 and L7 are not transports by their names; a transport needs organizations on both sides and π, τ, σ, λ (R01 L31) | L183-189; D5.1 | holds |
| S2 | "L1 then L3" is not defined: L1 ends in input states, L3 starts from a program's organization; an execution step must join them, with agreeing scopes (R01 L33, L103) | L189, L361 (composition "when intermediate scopes agree") | holds |
| S3 | Where the numbers came from does not settle what a program represents: a circuit computing NAND is not a model of the random generator (R01 L33) | L205-213, D12.5 (representation is a transport *to a content*, faithful on that content's contract) | holds |
| S4 | Higher replication success is weaker than D12.1, whose survival condition requires fidelity on H; programs that do no task still replicate, so Reading A is conditional, not automatic (R01 L35) | L195; D12.1 (core L454: surv(t, H) ⟺ Faithful_H(t) ∧ Env); S117's own unit B4 ("In Avida, lasting does not require doing the task") | holds |
| S5 | Argument 3 leaves an unseen value open only where an admitted alternative survives H and differs there; a restriction plus data can settle it (R01 L39) | L572-576 | holds |
| S6 | A carrier-to-content transport can be faithful while the target-to-content one fails (R01 L99) | L211 | holds |
| S7 | Under Reading B a faithful correspondence may be declared while an operational learning result can still be measured; different predicates (R01 L296) | L199, L211 | holds |
| S8 | A relay of recorded content keeps its source's history (R01 L85) | L211, L365; D12.3 | holds |
| S9 | Authorship alone does not settle Reading B: (R) asks whether the earlier occurrence *represents* the content (R01 L97) | D12.1 (core L454: ¬∃o ... Rep(o, x)) | holds |
| S10 | Strict prediction needs the object and simulation organizations; forecasting a number does not supply them (R01 L77) | L171-179, L217 | holds |
| S11 | It did not have the formal core; it cites definition ids only as the guide gives them (R01 L23) | the attachments sent | holds |

**11 hold.** It uses "transport", "selected", "constructed", "declared", "representation" and "prediction" as defined; it keeps representation apart from a correspondence that merely holds (R01 L11, L63, L99); it gives Reading A and Reading B separately (R01 L91, L97, L296). No misuse found.

## 4. Books, Pinker and other outside sources

| Source | The reply's mark | Checked here | Verdict |
|---|---|---|---|
| Gold 1967, pp. 450-453 (text and informant; the class boundary) | checked | Opened (the PDF at the address given): a text gives only members of the language; an informant says of any string whether it belongs; a "super-finite" class (all finite languages and at least one infinite one) is the boundary for learning from text | holds |
| PhysioNet BIDMC v1.0.0 (53 recordings of 8 minutes; PPG, respiration, ECG at 125 Hz) | checked (documentation) | Opened: "The 53 recordings within the dataset, each of 8-minute duration" with PPG, impedance respiration and ECG "sampled at 125 Hz" | holds |
| Pinker 2004, pp. 949-950 (constraints on hypotheses) | checked | Opened: a learner must respect prior constraints on its hypothesis space | holds |
| Pinker 1979, pp. 243-246 (sentence-meaning pairs) | checked | Not opened here (a 4.9 MB scan; S124 checked other pages of it) | unverified here |
| Marletto's and Deutsch's books | "not independently checked; inherited" | Not opened (S125's rule) | its mark is right |

No book is quoted by the reply. The Pinker note's marks are kept as given (R01 L287).

## 5. What it ran, reproduced; and two confirming runs

It ran no Avida; its receipts are a `git clone`, `git rev-parse` and two `rg` searches (R01 L232-260). The searches reproduce exactly here (lines 1014, 1020; 216, 217). No code to extract or rerun.

**Confirming runs (S125, raw output in `<scratchpad>/s125/runs/`).** What would count was written to a file before any run; it is quoted here unchanged:

> R0 and R0rep (no input events): identical tasks.dat and average.dat (the run is deterministic at a fixed seed). R1 and R1rep (SetEnvironmentInputs every update from series s1): identical (replay of the same inputs gives the same execution). R1 vs R2 (s2 differs from s1 only in the low 24 bits): files differ (event-set inputs reach the programs and change what happens). R1 vs R0: files differ. Rbad (one line with top byte 0x10): Avida exits with "Inputs must begin 0F, 33, 55". E1 (EPIGENETIC_METHOD 1, otherwise R0): runs to 3000; differs from R0 (the setting is live, not dead code). Counts against: R1 == R2 (inputs do not reach execution); R1 != R1rep or R0 != R0rep (no determinism, so a replay null means nothing); Rbad runs on; E1 identical to R0.

Stock Avida built from 47f13dad (`avida/cbuild/bin/avida`, md5 347560bf...), stock configuration files except a 30 by 30 world and seed 101, 3,000 updates, each under `timeout 600` and `nice -n 19`. Series s1 is a sine wave written for the purpose (a route test: it is not outside data), one `SetEnvironmentInputs` line per update with the top bytes kept; s2 is s1 with its low bits altered.

| Run | Exit | Programs doing NOT / NAND / AND / ORN / OR / ANDN at update 3,000 | Data files compared (header comments, which carry the clock time, left out) |
|---|---|---|---|
| R0 | 0 | 129 / 29 / 0 / 691 / 648 / 0 | R0rep: identical |
| R1 | 0 | 501 / 24 / 0 / 379 / 6 / 295 | R1rep: identical; R2: differ; R0: differ |
| R2 | 0 | 285 / 14 / 0 / 199 / 6 / 0 | |
| Rbad | 1 | (exits at load: "Inputs must begin 0F, 33, 55 for SetEnvironmentInputs") | |
| E1 | 0 | 801 / 820 / 0 / 814 / 0 / 0 | R0: differ |

Every expectation was met; no counter-observation was made. So: (i) a file of event lines carries numbers into every program's input with no C++; (ii) the same file replayed gives byte-identical data, which is the simplest form of the reply's "byte-identical internal replay" null; (iii) the epigenetic setting is live. What these runs do **not** show: that any program learned anything about the series, or anything about a recording from outside; E1's higher counts are one seed and are not read as a finding. CPU time for all seven runs: 98 CPU-seconds.

## 6. Its tests

| Test | Well formed? | What it can split | Do its controls separate what it says? | Cost (its figure; checked) |
|---|---|---|---|---|
| Rig step: a frozen source-forecast-pay transcript through the adapter, a hand-written predictor, byte-identical internal replay (R01 L300) | yes; a check of the rig, not of a hypothesis | none directly; it shows whether a later result could be made by the rig | yes | about 0 CPU-hours; needs the adapter |
| 1. Outside recording against a matched surrogate, a shuffled recording and yoked pay | yes: arms, held-out recordings, comparators (persistence, frequency), counter-observations, a planted predictor | whether a source's own structure, beyond what a surrogate keeps, is used (H5's advantage form) | yes, and it says what it does not separate: physical origin as such (byte-identical inputs give identical execution) | 16 runs, 5.6 (4 × 4 × 0.35 = 5.6, holds); new gated C++ for per-frame scoring |
| 2. What fixes the unseen: pay on H = {(0,0), (1,1)}, f = x and g = z | yes; needs hand-written witnesses that both are admitted programs | whether unseen answers follow the candidate class (L7) | yes; recoding control | 8 runs, 2.8 (holds); a small gated scalar task |
| 3. Positive evidence only, with a committed acceptance mask | yes, careful about hidden penalties | positive-only learning; Baker's paradox in a finite form | yes; yoked and explicit-feedback arms | 16 runs, 5.6 (holds); new scorer, decoder, probe mode |
| 4. A second view of the same events | yes; with mismatched pairing | whether combining views helps (L5 "held if") | yes | 16 runs, 5.6 (holds) |
| 5. Outputs change later data | yes; emulator first (a rig control), then an outside process | when a source stays outside | yes; it marks the emulator as not outside evidence | 12 runs, 4.2 (holds); plus 4.2 for an outside source |
| Total | | | | 68 runs, 23.8 (holds; 17 arms) |

The BIDMC arithmetic holds: every 25th sample of 125 Hz is 5 Hz, one step 0.2 s. Every block above about 3 CPU-hours needs the owner's word.

## 7. Grades

Used strictly: nothing is called grade 3; a fixed evaluator "can enact the process called selection ... without itself acquiring a selected standard" (R01 L92). No effect grades (E1 to E3) used.

## 8. Strengths and weaknesses

**Strengths.** Every source claim holds; it found the stock event route that our assessment and briefs had listed but not drawn the consequence from; it found the missing link (source-dependent change of what is retained); it typed the transports and showed our composite was not defined; its tests carry controls that say what they cannot separate. **Weaknesses.** Its own budget is large (23.8 CPU-hours, every block over 3); it did not open the book pages and says so; its "enabling hypothesis" is, by its own account, hard to fail ("A finite failed search does not by itself refute this enabling claim", R01 L15), so it is a frame for tests more than a hypothesis that can fail; it gives no single cheap discriminating experiment beyond the rig step.

**Count for reply 01:** Avida source 19 hold / 0 in part / 0 not; semantics 11 hold; outside sources 3 hold, 1 unverified here; arithmetic 7 of 7 hold.
