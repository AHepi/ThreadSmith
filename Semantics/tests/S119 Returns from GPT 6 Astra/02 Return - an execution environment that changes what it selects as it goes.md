# Avida selectors with a memory of their history

## 1. Summary for the owner

These designs let the execution environment change its rewards using its own record. One pays for capabilities whose share is rising; the other pays more for capabilities with little recorded exposure. For example, if NAND stops spreading while XOR starts spreading, the first rule moves its reward towards XOR. Neither follows a prescribed sequence of targets.

The stock version still sees only 77 named task classes. Its targets are therefore named one level up: grade 2. An archive of arbitrary Boolean output tables also remains grade 2 and has a finite ceiling.

The files below implement the stock selectors and controls. The report separates small software checks from the substantial experiment, which has not been run. It leaves the meaning of knowledge, the contribution of the human-written task list, and the choice of costly experiments with you.

## 2. The selectors

**Proposed specification v1.** The question is whether feedback from the current program population sustains acquisition after 25,000 updates, compared with a fixed reward vector and a changing schedule produced elsewhere. The selector is the execution environment together with its Python memory. Its rule remains fixed; its memory and reward allocation change. This does not test a selector inventing its own standard of success.

Both arms use 3,600 cells, the stock heads instructions, the same task-free ancestor, all 77 detectors throughout, and pieces of 1,000 actual updates. Let p[j,t] be the share recorded as performing task j at boundary t. Initially p[j,0]=0. The first piece offers exponent 0.1 to every task. Afterwards the two rules diverge. W=5 pieces and B=7.7 are proposed settings, not results selected from experiments.

**A, learning progress.** Keep the recent shares. Set w=min(t,W), q[j]=max(0,(p[j,t]−p[j,t−w])/w), and next-piece reward v[j]=Bq[j]/max(1,Σq). The fastest-rising share receives the largest exponent. A flat or falling share receives zero; if nothing rises, all rewards become zero. There is no rescue rule that silently reinstates rewards. Program replication can continue without task rewards; acquisition may stall.

This predicts pay following positive changes with a one-piece delay. It does not predict that every increase is a new capability: a lost capability returning can also generate progress. Record first appearances, returns, and the cumulative set ever reaching the common-task threshold separately. A preliminary uniform fallback was removed before implementation because it would pay flat capabilities again.

**B, rarity against an archive.** Keep a[j,t]=Σ(r=1..t)p[j,r]. Set s[j]=1/(1+a[j,t]) and v[j]=Bs[j]/Σs. The archive records accumulated prevalence at boundaries, without decay. This is an archive of task-class exposure, not individual output tables. Unseen classes retain their initial score; familiar classes receive less relative weight. The prediction is a shift towards classes with less archived exposure, not a guarantee that a reachable program performs them. This differs from paying for current rarity: an absent class can remain familiar because it was common earlier.

**Checked, source:** `process:type=pow` makes v an exponent of a factor 2^v; it is not a quantity of processor time. Each reaction has one process and `requisite:max_count=1`. The sum of available exponents is at most B for A and B for B, so the combined task factor is bounded by 2^7.7≈207.94 under these requisites. Rewards still interact with copying speed and other Avida scheduling rules. Matching offered exponents cannot match realized processor time.

The hard-to-vary reading maps the brief's “memory” to stored shares/archive exposure, “rule” to the formulas, “responds to the population” to the adaptive-versus-replay contrast, and “keeps rising” to later counts. These are the given jobs. Parsing safeguards and fixed measurement procedures are added rig requirements.

| Part and origin | Assessment for the stated question | Change that distinguishes its role |
|---|---|---|
| Recent-share memory, built | Held for the specified A calculation; sustained acquisition unknown | Identical present shares with different recent histories must produce different pay |
| Cumulative archive, built | Held for historical rarity; sustained acquisition unknown | Identical present shares with different past exposure must produce different pay |
| W, B, piece length and bootstrap, proposed | Loose numeric choices | Change them in separately labelled sensitivity runs; do not retune the reported experiment |
| Blind replay, given | Held for separating this feedback from time variation | Disconnect recipient measurements while retaining every donor reward vector |
| Task catalogue, fixed for stock implementation | Fixed observational boundary | Behaviours outside it cannot alter Stage 1 pay |
| Continued-acquisition explanation | Unknown | Flat later counts or no separation from replay count against it |

Progress rewards pull against retention: once a capability plateaus, A removes its pay. Archive rarity pulls against paying for useful familiar behaviour. Neither tension is repaired after seeing outcomes. A flat result cannot be relabelled “successful exploration.”

## 3. Stage 1 files and commands

The appendices contain the executable Python 3 standard-library driver, exact generated configuration templates, the measurement helper, and test material. Copy each fenced file into the indicated filename. Use a clean checkout of [Avida commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16). Source statements below are **checked** against that checkout; historical run descriptions are **checked against the supplied brief only**, not independently rerun.

The driver creates a separate directory per piece, saves the program population before exit, updates its JSON history, and prepares the next environment. A donor's schedule must be complete before its fixed and replay controls are generated. Each control receives a different seed and starts from the ancestor, not the donor's final program population. Replay reads its own output for reporting only. It does not feed that output into its reward schedule.

The default length is 50 pieces; specify 100 for the proposed continuation. Commands and smoke outputs are included with the code. No command in this report launches the full experiment automatically.

**Checked, source:** `SetReactionValue` is registered in `actions/EnvironmentActions.cc:1731`; its constructor at lines 651–670 captures a literal reaction name and numeric value. `cEnvironment.cc:1877–1915` changes the value in the running world. A fixed or donor-replay schedule can therefore be compiled into timed events without reloads. The headless event list is loaded at startup (`cWorld.cc:198–203`; `cEventList.cc:56–100`); editing its disk file does not supply an adaptive channel. The inspected action registry contains no stock rolling-progress/archive controller. The viewer's in-process setter is not a Python standard-library interface to the headless binary.

Keep reloads identical in the main comparisons. A precompiled, unbroken replay is a separate restart-sensitivity option. It changes both the controller schedule's delivery and the restart treatment if compared directly with fragmented adaptive runs.

**Checked:** changing a reaction value affects later calculations; it does not erase bonuses already accumulated (`cPhenotype.cc:1644–1646`; `cOrganism.cc:489–492`). Do not interpret an event as an instantaneous reset of all processor allocations. The driver saves selector state and refuses existing output directories; automatic recovery of an interrupted Python run is not implemented.

**Measures, frozen before costly runs.** Save each boundary. Report the live last-cycle count of tasks represented in at least 10% of the current program population, and separately in at least 360 cells. An underfilled world can otherwise inflate a share. The selector uses the former share; occupancy is always reported.

Fresh standardized assays use the deterministic test-input triple in its native order and all six permutations. For task j and saved instruction sequence g, let I[g,j,π] indicate performance in order π. Compute Σg n[g]I[g,j,native]/Σg n[g] and Σg n[g]minπ I[g,j,π]/Σg n[g]. Intersect within the same sequence before summing. Taking the minimum of six population-level shares can give a positive answer even when no single sequence passes all orders. Record replication capability separately.

**Checked, source:** live default inputs retain a fixed order of top-byte patterns while lower bits are randomized (`cEnvironment::SetupInputs`, lines 1252–1295). A standardized native-order assay therefore does not reproduce every live program's current numbers or CPU state. Test an additional frozen panel of triples before claiming input-value generality. The delivered helper tests the stated diagnostic triple; that additional panel is an unrun option.

At 25,000, 50,000, 75,000 and 100,000 updates, report current common-task counts, cumulative first crossings of 10%, losses and reacquisitions. Primary comparison: live common-task count at 50,000. Later changes and same-sequence all-order counts address continuation and order dependence; the sizing calculation does not independently size every secondary measure.

All 77 classes are offered positive pay during bootstrap. Thus there are **zero eligible never-offered-pay classes inside this panel**. A count of zero there is structurally uninformative. Boundary snapshots also cannot determine every reward actually earned between boundaries. Report that earned-pay question as unmeasured. For a broader never-paid measure, freeze an external output-table assay, exclude every behaviour eligible for a training reward, and evaluate saved sequences with the owner's `RUN_BOUNDED` implementation. That patch was not supplied here, so no broader count is reported or fabricated. The catalogue and exclusion rule still name the measurement domain.

## 4. Restart cautions handled

| Supplied caution | Treatment and remaining consequence |
|---|---|
| Instruction sequences, cells and averages survive | Save/load the complete stock population file; retain the source file, hash and piece metadata. Restoring these fields is not restoring a running world. |
| CPU state does not survive | Every arm uses the same piece boundaries. Reloaded programs restart execution; existing averages do not reconstruct registers, stacks or instruction positions. |
| Random state does not survive | Record a distinct deterministic seed for every piece. The resulting experiment is a specified sequence of restarts, not a continuation of the original random stream. |
| Resource levels do not survive | These templates use no depleting resources. S118 P1 is therefore a related, separate arm. Resource-based reference recipes require their own restart accounting. |
| Generation counts and task records do not survive | Keep elapsed updates and selector memory outside Avida. Observe tasks at the end of each piece; never treat the first post-load records as inherited capability. Report the boundary observation's last-cycle limitation. |
| Local label 1,000 means 1,001 executed updates | Save and exit at N−1. The stock counter starts at −1; events are processed before incrementing and executing the next update. Global elapsed updates are kept by Python. |
| S114 found matched births and copying times in two environments | Checked against the supplied brief only. That limited comparison does not settle reset effects on these selectors, archives or input-order capability. |

**Checked, source:** the update ordering is in `targets/avida/Avida2Driver.cc:91–98`, with initialization in `cStats.cc:65`. The driver does not supply a restored global label to `LoadPopulation`. This prevents local events from silently missing their intended boundary.

## 5. Stage 2

Stock Avida suffices for the two task-class selectors. It cannot pay directly for a raw output table outside its declared task checks using these files. The following extension is therefore a separate option, **not an implemented patch**. **Estimate:** 450–750 production lines plus 150–250 test lines; the supplied brief permits an outline above approximately 200 lines.

**Checked, source:** `cTaskLib::SetupTests` (`main/cTaskLib.cc:369–448`) infers a logic ID from bit positions in one output and its input buffer. It does not execute the program on all input cases. Arbitrary heads programs can branch, shift, add or depend on execution history. An archive around `GetLogicId()` would archive an observation, not a tested general function. Source extraction found 251 accepted logic IDs across the 77 classes; missing IDs are 0, 170, 204, 240 and 255. These are constants and direct-input maps. Expanding to all Boolean tables adds only those five maps.

**Proposed probe contract.** For each distinct saved instruction sequence, run eight fresh isolated probes. Row r=a+2b+4c supplies the ordered triple (a,b,c), encoding zero as `0x00000000` and one as `0xffffffff`. Preserve heads instruction meanings; disable copying variation and instruction failure only in the assay, with a private fixed RNG. Cache by full sequence, hardware, instruction set and protocol version. Unsupported hardware is rejected.

Collect raw output only after three input reads have completed. **Checked:** `IO` outputs before reading (`cpu/cHardwareCPU.cc:4188–4199`), so the third IO's output is too early. Stop at first successful division, execution termination, 2,000 executed instructions, or 16 eligible outputs. For output ordinal j, admit a table only if all eight probes produced that ordinal. Never replace a missing output with zero. The descriptor is the vector of eight unsigned 32-bit outputs; deduplicate equal vectors across ordinals and sequences.

The literal Boolean variant admits only all-zero/all-one output words, yielding an eight-bit table ID. Pay on its designated-order table set. Report all-order task performance separately. Requiring the identical canonically labelled map under every permutation was discarded before implementation: it silently demands symmetry and excludes ordinary order-dependent functions. Running all six permutations of all eight scalar rows was also removed: it repeats the same eight physical input tuples under deterministic reset. Full-width input tests supply the separate transfer challenge.

**Archive and payment.** At an epoch, freeze archive C and snapshot multiplicities n[g]. Let S[g] be each sequence's table set. Set F[g]=2 if any table in S[g] is absent from C, otherwise 1, including the empty set. Compute every F from the same old archive; only then add Σg n[g]1[table∈S[g]] to each archive count. This prevents cell traversal order from deciding who receives novelty pay. Hold F for the next 1,000 updates; a newly varied sequence receives 1 until the next epoch. Repeated outputs cannot stack payments. Conventional task rewards are zero in this arm.

| Source location, checked | Proposed change |
|---|---|
| `cpu/cTestCPU.h/.cc`, `cpu/cCPUTestInfo.h/.cc` | Add bounded fresh-execution tracing, stop reasons and no descendant recursion; existing execution/recursion sites are `cTestCPU.cc:143–187,233–275,317–321` |
| `main/cOrganism.h/.cc:368–407` | Optional probe sink records completed reads/raw output; bypass ordinary task/reaction scoring, including division-triggered scoring, only in probe mode |
| New `main/cNoveltySelector.h/.cc`, owned by `cWorld` | Store archive, protocol, cache, frozen multiplier map and atomic state-file operations |
| `actions/EnvironmentActions.cc` | Add epoch and state save/load actions; reject mismatched protocols, duplicate epochs and overflow |
| `main/cPopulation.cc:613–618` | Multiply positive scheduling weight by F in `AdjustSchedule`; refresh every occupied cell at epoch boundaries; empty-cell weight stays zero |
| `main/cAvidaConfig.h`, `avida-core/CMakeLists.txt` | Default feature off, validate a merit-sensitive scheduler, register source files |

Keep underlying merit unchanged. Apply F afresh when inserting a program or updating its merit; otherwise factors can compound or be inherited by a different sequence. **Checked:** relevant calls occur at `cPopulation.cc:1353–1389,2316–2322,8003–8019`; the constant round-robin slicer at `7450–7474` would not implement the intended merit-weighted allocation.

**Checked:** scalar probes do not populate every bit-lane combination expected by ordinary task scoring (`cTaskLib.cc:391–442`). Bypassing that scoring is necessary; merely supplying scalar manual inputs to the current checker is insufficient.

Persist protocol/settings, archive counts and full keys, epoch/global labels, current multiplier map and source/instruction-set identity atomically. Check full descriptors even when indexing by hash. Refuse mismatches and repeated epochs. A memory limit stops the run; silent eviction would change novelty. Selector persistence does not recover missing live CPU or RNG state after a population-only reload.

**Unrun tests and expected outputs:**

| Fixture | Expected output |
|---|---|
| No complete ordinal | `tables=0 multiplier=1` |
| NOT-first-delivered / echo-first in designated order | Boolean `table_id=85` / `table_id=170` |
| Output missing on one row | `complete=0 paid=0` |
| Two sequences first expose the same table | `new_tables=1`; both factors 2; count gains both multiplicities |
| Repeat next epoch / reverse cell traversal | Factors 1 / identical report |
| Exactly three IO calls | `eligible_outputs=0` |
| Save/reload selector state | Identical archive and next-interval factors; no duplicate bonus |
| Probe-only mode with every F forced to 1 | Same live trajectory/RNG fingerprint as no probes |

Also test merit updates/division for noncompounding factors, and a program agreeing on scalar rows but failing the unused full-width panel. Log bound hits, incomplete tables and constant-only novelty. A Boolean archive has at most 256 keys; this raw descriptor has at most 2^256 keys, still finite. Neither count demonstrates useful capability growth or grade 3. Without cache hits, each sampled sequence can require 8×2,000=16,000 assay instructions; no extension timing is measured.

## 6. Controls, sizes and cost

Each independent block contains an adaptive donor, its blind replay, and its fixed control, all from the ancestor on distinct seed streams. The fixed value for task j is Σk N[k]v[k,j]/Σk N[k], which reduces to the arithmetic mean for these equal pieces. It matches **mean offered exponents**, not mean reward multipliers or realized earnings. For a 100,000-update donor, this is the whole-run mean, including its second half; it need not match the first-half mean.

Analyse donor-minus-replay differences across blocks. Independent recipient seeds do not make the endpoints independent: they share the donor's schedule. Do not count cells, tasks or snapshots as additional seeds. Donor-minus-fixed contrasts and references are secondary comparisons.

The two S113 reference recipes must come from the archived configurations. The supplied brief does not contain them. The delivered `all77` mode is a new equal-offer reference, not a reproduction of S113. S118 P1 remains a related arm with no assumed result.

**Calculated from the brief:**

| Group | Counts | Mean | Squared deviations | Sample variance | Sample SD |
|---|---|---:|---:|---:|---:|
| Growing list | 48, 55, 65 | 56 | 49+1+100=146 | 146/2=73 | 8.5440 |
| All 77 | 13, 32, 41 | 28.6667 | 408.6667 | 408.6667/2=204.3333 | 14.2945 |

The pooled variance would be (146+408.6667)/4=138.6667. The options below instead provisionally assign variance 204.3333 to each new arm. Three observations do not establish a reliable variance bound, and the exact S113 counting procedure still needs comparison with the delivered live-count measure.

Name the difference as **ten additional common tasks at 50,000 updates**, adaptive versus replay. There are two primary comparisons, A and B; allocate two-sided α=0.025 to each, with model power 0.80. **Checked:** [NIST's sample-size formula](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm) supplies n≈(z[1−α/2]+z[0.8])²σ²/δ²; [its paired-observation procedure](https://www.itl.nist.gov/div898/handbook/prc/section3/prc311.htm) applies inference to within-block differences. Here (2.241403+0.841621)²=9.505037, δ²=100, and Var(D−R)=Var(D)+Var(R)−2Cov(D,R).

| Conditional option | Difference variance | Normal calculation | Paired-t model calculation |
|---|---:|---|---|
| Assume zero outcome covariance | 2×204.3333=408.6667 | 9.505037×408.6667/100=38.8439 → 39 | 42 blocks per selector; power 0.806585 |
| Allow any covariance, assuming both marginal variances ≤204.3333 | ≤4×204.3333=817.3333 | 9.505037×817.3333/100=77.6878 → 78 | 81 blocks per selector; power 0.804282 |

The second bound uses Var(D−R)≤(SD(D)+SD(R))². Neither option guarantees power when the assumed marginal variances or model fail. These sizes detect a departure from zero if the mean difference is ten; they do not give 80% power to demonstrate a difference of at least ten. Report effect intervals. A separately funded calibration can estimate missing variance; no such budget is chosen here.

Run length is 100,000 actual updates, with the primary endpoint at 50,000 and continuation checkpoints at 25,000, 75,000 and 100,000. Cost eight arms: A/replay/fixed, B/replay/fixed, and the two references conditional on their recipes. The supplied nine-task timing gives 2 CPU-hours per 100,000-update run, hence 8n×2=16n nominal CPU-hours.

| Seeds per arm | Runs | Nominal CPU-hours | Donor phase with three processes | Remaining phase | Nominal wall time |
|---:|---:|---:|---:|---:|---:|
| 42 | 336 | 672 | ceil(84/3)×2=56 h | ceil(252/3)×2=168 h | 224 h, or 9.33 days |
| 81 | 648 | 1,296 | ceil(162/3)×2=108 h | ceil(486/3)×2=324 h | 432 h, or 18 days |

These are **nine-task timing equivalents**, not observed 77-task costs. With an unmeasured timing ratio q and per-run restart/analysis costs h[r],h[a], CPU-hours become 8n(2q+h[r]+h[a]). Do not multiply by 77/9 without a timing model. All analyze processes count towards the three-process limit. Stage 2 probing adds a separate unmeasured cost. Benchmarking the exact configuration is necessary before assigning a calendar duration.

## 7. What counts against

These criteria precede the substantial runs. A or B failing to separate from its blind replay counts against the claim that responding to its own program population adds capability under this design. An interval containing both zero and the named ten-task difference is inconclusive; it is not evidence of equality. If the upper confidence limit falls below ten, the named effect is unsupported at that precision.

A rise only in cumulative archive entries, with no rise in current or all-order capabilities, does not answer the owner's progressive-acquisition question. Repeated loss and reacquisition with no first crossings after 25,000 counts against continued discovery. No positive later increment through 100,000, especially while many classes remain unexpressed, counts against sustained growth under these settings; it does not settle all possible execution environments.

If native-order counts rise but same-sequence all-order counts do not, the result is order-bound. If A spends long periods with zero rewards and acquires nothing, report the stall. If B keeps paying unavailable classes, report the unused offers. Neither observation licenses silently adding a curriculum, archive decay or a new bootstrap.

Unmatched restart treatment, altered task manifests, recipient feedback entering replay, or evaluating different sequences in different orders invalidates the intended comparison. Those are rig failures, to be repaired and rerun under a new recorded version. They are not selector successes or failures.

S118 outcomes remain unknown. The counts do not decide what knowledge is or whether the human-written catalogue belongs in its history.

## 8. What is still named, by grade

| Component | Naming grade and what remains specified |
|---|---|
| Each stock task detector | Grade 1: an exact named function class |
| A as a whole | Grade 2: select from those classes using a written recent-growth rule |
| B as a whole | Grade 2: select from those classes using a written historical-rarity rule |
| W, B, piece length, bootstrap, archive update and tests | Explicit parameters of the grade-2 rule; their changing stored values do not create a new naming grade |
| Generic Boolean-table archive | Grade 2: a written behaviour class, probe protocol, equality test and novelty rule; at most 256 tables |
| Longer response-table or stream archive | Grade 2: a larger predeclared observation space, with fixed bounds and comparison rules |
| Grade 3 | Not reached by either stage. Removing task names while retaining a fixed checker does not remove the checker. |

The instruction meanings, input process, scheduling, program-copying rules, layout and resource treatment also remain specified. The whole execution environment is under test, but this intervention changes only its rewards and remembered observations.

## 9. What you ran, with outputs, and what you are unsure of

**Checked by execution, this session:** built the clean pinned source as Avida 2.14.0 release without C++ changes. The final stock driver and measurement helper use Python 3 standard-library modules; Git and the Avida executable are external prerequisites. The sizing calculation separately used SciPy 1.17.0.

The configure/build commands were:

```sh
SRC=/workspace/scratch/4213a51f9bba/av_src
BASE=/workspace/scratch/fbaa94d665d5
CMAKE=/root/.local/lib/python3.12/site-packages/cmake/data/bin/cmake
AVIDA_DISABLE_BACKTRACE=1 "$CMAKE" -S "$SRC" -B "$BASE/build" \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_FLAGS=-std=gnu++11 -DAVD_GUI_NCURSES=OFF \
  -DAVD_GUI_PROTOTYPE_TEXT=OFF -DAVD_UNIT_TESTS=OFF -DAPTO_UNIT_TESTS=OFF
AVIDA_DISABLE_BACKTRACE=1 "$CMAKE" --build "$BASE/build" --target avida -j 3
```

Build output excerpts, with compiler deprecation warnings omitted:

```text
-- Configuring done (0.3s)
-- Generating done (0.0s)
-- Build files have been written to: /workspace/scratch/fbaa94d665d5/build
[100%] Linking CXX executable ../bin/avida
[100%] Built target avida
```

The binary identified itself as `Avida 2.14.0` and `release build`. SHA256: `1b581ab457cca05fcc61dc3e3d6e0d473bf765345ed6e1aa146be371ce13d071`. The pinned source's `git status --short` printed no entries. Source extraction of the task-check functions printed:

```text
functions_scanned: 77
logic_ids_accepted: 251
missing_ids: [0, 170, 204, 240, 255]
```

The following aliases abbreviate the exact absolute paths in the actual commands:

```sh
S=/workspace/scratch/fbaa94d665d5/stage1
SRC=/workspace/scratch/4213a51f9bba/av_src
BIN=/workspace/scratch/fbaa94d665d5/build/bin/avida
```

One development arithmetic command imported `run.progress([[0.0],[0.2]],5,7.7)`,
asserted absolute difference from 1.54 below 1e-12, and printed:

```text
development: A 0 -> 0.2 gives 1.54
```

```sh
python3 "$S/run.py" --source "$SRC" --avida "$BIN" --out "$S/dry-progress" --mode progress --seed 1201 --piece-updates 100 --pieces 2 --dry-run
```

Expected before this command, and observed:

```text
DRY RUN: prepared piece 1 only; no Avida process executed
tasks=77 world=60x60 local_exit=99 actual_updates=100
next pieces require observed counts or a donor schedule; no counts fabricated
```

```sh
python3 "$S/run.py" --source "$SRC" --avida "$BIN" --out "$S/smoke-progress" --mode progress --seed 1201 --piece-updates 100 --pieces 2
```

Observed development smoke (before adding the independent fixed-seed guard and
extra acquisition/loss fields; preserved in `development-driver.py`):

```text
piece=1 global_updates=100 local_label=99 live=40 present=0 common10=0 pay_total=7.7
piece=2 global_updates=200 local_label=99 live=312 present=0 common10=0 pay_total=0
complete pieces=2 actual_updates=200
```

```sh
python3 "$S/selftest.py"
```

```text
development: A 0 -> 0.2 gives 1.54
selectors: plateau=0 decline=0 growth_ratio=2 archive_ratio=1:2 fixed_means=1,3
tables: reordered descriptions accepted; missing/duplicate/misaligned/oversized/empty rejected
controls: replay unchanged; same-seed fixed/replay rejected; N=2 exits at label 1
measurement: first=[2] reacquired=[0] lost=[1] cumulative=3
selftest complete; no Avida process executed
```

```sh
python3 "$S/run.py" --source "$SRC" --avida "$BIN" --out "$S/smoke-archive" --mode archive --seed 1301 --piece-updates 100 --pieces 2
```

```text
piece=1 global_updates=100 local_label=99 live=70 present=0 common10=0 pay_total=7.7
piece=2 global_updates=200 local_label=99 live=376 present=0 common10=0 pay_total=7.7
complete pieces=2 actual_updates=200
```

```sh
python3 "$S/run.py" --source "$SRC" --avida "$BIN" --out "$S/smoke-replay" --mode replay --seed 2201 --piece-updates 100 --pieces 2 --schedule "$S/smoke-progress/schedule.json"
```

```text
piece=1 global_updates=100 local_label=99 live=65 present=0 common10=0 pay_total=7.7
piece=2 global_updates=200 local_label=99 live=360 present=0 common10=0 pay_total=0
complete pieces=2 actual_updates=200
```

```sh
python3 "$S/run.py" --source "$SRC" --avida "$BIN" --out "$S/smoke-fixed" --mode fixed --seed 3201 --piece-updates 100 --pieces 2 --schedule "$S/smoke-progress/schedule.json"
```

```text
piece=1 global_updates=100 local_label=99 live=48 present=0 common10=0 pay_total=3.85
piece=2 global_updates=200 local_label=99 live=329 present=0 common10=0 pay_total=3.85
complete pieces=2 actual_updates=200
```

```sh
python3 "$S/attack.py"
```

```text
rejected: incomplete schedule
rejected: different rig
added adversarial cases complete; no Avida process executed
```

Each smoke used 60×60 cells and two 100-update pieces. Expected conditions were positive occupancy, 77 task columns, two saved/reloaded snapshots, and correct update labels. Counts were not predicted. No smoke recorded task acquisition. Full subprocess logs were captured; the exact driver summaries are above. Measurement commands use `$BASE` and `$SRC` defined earlier.

Ran `python3 $BASE/measurement/check_aggregation.py`:

```text
synthetic x: per-order counts=5,5,5,5,5,5; minimum=5; same-sequence all6=0
synthetic y: all6 task-record count=5; all6 replication-pass count=0
synthetic boundary: 1/10 remains common; failed tests stay in denominator
```

Ran the following command first with output `smoke-orders`; it stopped after
one Avida invocation because the initial parser expected distinct indexed task
header names. The preserved output was:

```text
measurement error: Invalid #format in /workspace/scratch/fbaa94d665d5/measurement/smoke-orders/order-0/counts.dat
```

The parser was changed to read the actual repeated `task` names and to check
all numbered task descriptions. Reran with a new output directory:

```sh
python3 $BASE/measurement/measure_orders.py \
  --avida $BASE/build/bin/avida \
  --piece $BASE/stage1/smoke-progress/piece-00001 \
  --snapshot $BASE/stage1/smoke-progress/piece-00001/data/population-99.spop \
  --manifest $BASE/stage1/smoke-progress/task_manifest.json \
  --schedule $BASE/stage1/smoke-progress/schedule.json \
  --out $BASE/measurement/smoke-orders-v2
```

```text
programs=312
orders=6; all6 uses the same saved sequence in every order
native_task_record common=0
native_replication_pass common=0
all6_task_record common=0
all6_replication_pass common=0
never_offered=0
```

The resulting JSON contains 226 saved sequence rows and 54 failed-replication
programs in each order. These zeros exercise the saved-snapshot path, not
sustained acquisition. Full process output was captured in
`measurement/smoke-orders-v2/order-0/avida.log` through `order-5/avida.log`;
the failed first attempt is retained separately.

To exercise nonzero task records, ran:

```sh
python3 $BASE/measurement/make_positive_fixture.py $SRC \
  $BASE/stage1/smoke-progress/piece-00001 \
  $BASE/measurement/positive-fixture.spop
```

```text
synthetic fixture: stock 9task.org abundance=1; stock ancestor abundance=9
instruction counts=67,100
```

This re-encoded the existing stock virtual-machine fixture
`tests/resources_9r/config/9task.org` by instruction names in the driver's
instruction alphabet, and assigned artificial abundances. It did not create
or run a live program population. Ran:

```sh
python3 $BASE/measurement/measure_orders.py --avida $BASE/build/bin/avida \
  --piece $BASE/stage1/smoke-progress/piece-00001 \
  --snapshot $BASE/measurement/positive-fixture.spop \
  --manifest $BASE/stage1/smoke-progress/task_manifest.json \
  --out $BASE/measurement/positive-orders
```

```text
programs=10
orders=6; all6 uses the same saved sequence in every order
native_task_record common=9
native_replication_pass common=9
all6_task_record common=8
all6_replication_pass common=8
never_offered=unknown
```

The nine native-order tasks were `not,nand,and,orn,or,andn,nor,xor,equ`; all-six
retained those except `and`. No replication test failed. These are constructed
fixture assay results, not results from any proposed selector. Full logs were captured under `measurement/positive-orders/order-{0..5}/avida.log`.

Help listings were inspected. Measurement ran 13 analyze-only calls, including the first failed attempt.

Independent inspection of the eight saved smoke snapshots and control schedules printed:

```text
Replay vectors equal donor: PASS
Fixed vectors equal per-task donor means: PASS
Eight snapshots match recorded living counts: PASS
Eight smoke piece seeds are distinct: PASS
```

`python3 calculate_sizes.py` printed:

```text
sample_variances=73.000000,204.333333
z_sum_squared=9.505037
n=42; difference=10; difference_variance=408.666667; model_power=0.806585; total_runs=336; cpu_hours_100k=672; phased_wall_hours_100k=224
n=81; difference=10; difference_variance=817.333333; model_power=0.804282; total_runs=648; cpu_hours_100k=1296; phased_wall_hours_100k=432
Python SciPy version: 1.17.0
```

The positive fixture was added after the zero smoke to exercise nonzero records. The optional baseline-comparison path was not exercised end to end.

**Checked, source:** the helper's task vector is the original tested program's last-cycle record (`cAnalyzeGenotype.cc:559–590`; `cCPUTestInfo.cc:120–124`). The test has a bound of 20 times instruction-sequence length per execution and can follow up to three copies for its replication verdict (`cTestCPU.cc:144–183,283–321`; `nHardware.h:30`). It does not record every output or settle task performance before a failed replication. Its replication flag is therefore kept separate from its task-record counts. The broader bounded-output assay remains unrun.


The unresolved research question is whether these feedback rules sustain acquisition under matched controls. The small runs below address software paths only. Stage 2 is an implementation outline, and the costly experiment, extended input panel and broader never-paid assay remain unrun. The S113 reference configuration files and the owner's `RUN_BOUNDED` patch are not supplied in this brief; recreating their contents from their descriptions would not be an exact reproduction.

The costly-run choice remains with the owner.

## Code and configuration appendices

These are the final files. The progress development smoke preceded a rig revision adding the fixed-control seed guard and trajectory fields; its selection rule did not change. Later archive/replay/fixed smokes and the arithmetic/parser tests used the revised driver. The final driver SHA256 is `379388e059e0e8234739e8b85c4c100d5de935caad2fe0c9b0e5a7ff270fdc57`.

The configuration fragments use substitution markers. `run.py` performs those substitutions and writes complete runnable files; do not send marker-containing templates directly to Avida. It copies the exact pinned instruction-set, ancestor and base configuration files.

To extract the code/configuration files from this document into a new directory, run this standard-library snippet beside the downloaded report:

```sh
python3 - <<'EXTRACT'
from pathlib import Path
import re
source=Path('Brief02_History_Selector_Execution_Report.md').read_text()
out=Path('selector-files')
out.mkdir(exist_ok=False)
for name,content in re.findall(r'^### File: ([A-Za-z0-9_.-]+)\n\n```[^\n]*\n(.*?)^```',source,re.M|re.S):
    (out/name).write_text(content)
print('Files extracted to',out)
EXTRACT
```

Illustrative 100,000-update commands below are **unrun options**. Set `SRC` to the pinned checkout and `BIN` to its built executable; run at most three Avida processes, including assays, concurrently. Each `--out` must be new. Replay/fixed commands wait for their donor to finish.

```sh
python3 run.py --source "$SRC" --avida "$BIN" --out A-001 --mode progress --seed 1001 --pieces 100
python3 run.py --source "$SRC" --avida "$BIN" --out A-replay-001 --mode replay --seed 2001 --pieces 100 --schedule A-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out A-fixed-001 --mode fixed --seed 3001 --pieces 100 --schedule A-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out B-001 --mode archive --seed 4001 --pieces 100
python3 run.py --source "$SRC" --avida "$BIN" --out B-replay-001 --mode replay --seed 5001 --pieces 100 --schedule B-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out B-fixed-001 --mode fixed --seed 6001 --pieces 100 --schedule B-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out uniform-001 --mode all77 --seed 7001 --pieces 100
python3 measure_orders.py --avida "$BIN" --piece A-001/piece-00024 --snapshot A-001/piece-00024/data/population-999.spop --manifest A-001/task_manifest.json --schedule A-001/schedule.json --out measure-A-25000
python3 measure_orders.py --avida "$BIN" --piece A-001/piece-00049 --snapshot A-001/piece-00049/data/population-999.spop --manifest A-001/task_manifest.json --schedule A-001/schedule.json --baseline measure-A-25000/measurement.json --out measure-A-50000
```

The S113 growing-list and all-77 references require their archived recipes; `uniform-001` is only the newly specified equal-offer arm. Continue the same assays at piece indices 74 and 99 for 75,000 and 100,000 updates. Independent master seeds are needed for every experimental block.

### File: run.py

```python
#!/usr/bin/env python3
"""Stock Avida selector v1. Python 3 standard library; see SPEC-v1.md.

Reads only pinned stock sources; runs Avida in newly created piece directories.
All replication is performed by Avida virtual-machine instructions in Avida.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys

PIN = "47f13dadb547fcf10f620ace60247f38b30b8b16"
SPEC = "selector-v1"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def manifest(source):
    support = source / "avida-core/support/config"
    entries = re.findall(r'^REACTION\s+(\S+)\s+(\S+)\s+',
                         (support / "misc/environment-all-logic.cfg").read_text(), re.M)
    # Capture the task key and full printed description, not a guessed column order.
    descriptions = dict(re.findall(r'name\s*==\s*"([^"\n]+)"\)\s*NewTask\(name,\s*"([^"\n]+)"',
                                   (source / "avida-core/source/main/cTaskLib.cc").read_text()))
    expected = "not nand and orn or andn nor xor equ".split()
    expected += ["logic_3" + a + b for a in "ABC" for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                 if a != "C" or b <= "P"]
    require(len(entries) == 77 and {t for _, t in entries} == set(expected),
            "expected exactly the pinned stock 77-task manifest")
    require(all(t in descriptions for _, t in entries), "task description missing in source")
    result = [{"reaction": r, "task": t, "description": descriptions[t]} for r, t in entries]
    require(len({m["description"] for m in result}) == 77, "duplicate task description")
    return result


def table(path):
    columns, rows = {}, []
    for line in Path(path).read_text().splitlines():
        match = re.match(r'^\s*#\s*(\d+)\s*:\s*(.*?)\s*$', line)
        if match:
            index, name = int(match[1]) - 1, match[2].casefold()
            require(index >= 0 and index not in columns and name not in columns.values(),
                    "duplicate/invalid column in " + str(path))
            columns[index] = name
        elif line.strip() and not line.lstrip().startswith("#"):
            row = [float(x) for x in line.split()]
            require(all(math.isfinite(x) for x in row), "nonfinite data in " + str(path))
            rows.append(row)
    require(columns and rows, "empty table " + str(path))
    require(set(columns) == set(range(len(columns))), "noncontiguous columns in " + str(path))
    require(all(len(row) == len(columns) for row in rows), "ragged data in " + str(path))
    return [{columns[i]: value for i, value in enumerate(row)} for row in rows]


def observe(piece, tasks, boundary):
    task_rows, count_rows = table(piece / "data/tasks.dat"), table(piece / "data/count.dat")
    tr, cr = task_rows[-1], count_rows[-1]
    require(tr.get("update") == cr.get("update") == boundary, "missing/mismatched boundary update")
    require("number of organisms" in cr, "living-program count column missing")
    count = cr["number of organisms"]
    require(count == int(count) and 0 < count <= 3600, "empty/invalid living program population")
    require(set(tr) == {"update"} | {m["description"].casefold() for m in tasks},
            "task columns differ from source manifest")
    counts = [tr[m["description"].casefold()] for m in tasks]
    require(all(x == int(x) and 0 <= x <= count for x in counts), "invalid per-program task count")
    return int(count), [int(x) for x in counts], [x / count for x in counts]


def progress(history, window, budget):
    width = min(window, len(history) - 1)
    require(width > 0, "progress needs one observed piece")
    slopes = [max(0.0, (new - old) / width)
              for new, old in zip(history[-1], history[-1 - width])]
    scale = budget / max(1.0, sum(slopes))
    return [scale * slope for slope in slopes]


def rarity(exposure, budget):
    scores = [1.0 / (1.0 + x) for x in exposure]
    return [budget * x / sum(scores) for x in scores]


def mean_schedule(values):
    require(values and len({len(row) for row in values}) == 1, "empty/ragged schedule")
    return [sum(column) / len(values) for column in zip(*values)]


def common_changes(shares, counts, previous, cumulative):
    current = {j for j, p in enumerate(shares) if p >= 0.1}
    return current, {"common_360cells": sum(x >= 360 for x in counts),
                     "cumulative_common": len(cumulative | current),
                     "first_common": sorted(current - cumulative),
                     "reacquired": sorted((current & cumulative) - previous),
                     "lost": sorted(previous - current)}


def piece_seed(master, index):
    raw = hashlib.sha256((SPEC + ":" + str(master) + ":" + str(index)).encode()).digest()
    return 1 + int.from_bytes(raw[:8], "big") % 2147483646


def configured(base, overrides):
    for key, value in overrides.items():
        base, count = re.subn(r'^' + re.escape(key) + r'\s+[^\n]*$', key + " " + str(value), base, flags=re.M)
        require(count == 1, "missing/duplicate config key " + key)
    return base


def event_text(boundary, reload):
    first = "u begin LoadPopulation input.spop" if reload else "u begin Inject ancestor.org"
    return first + "\n" + "\n".join(
        "u " + str(boundary) + " " + action for action in (
            "PrintTasksData", "PrintCountData", "PrintAverageData", "PrintTimeData",
            "SavePopulation filename=population:save_historic=0", "Exit")) + "\n"


def prepare(piece, support, tasks, values, seed, boundary, previous):
    piece.mkdir()
    for original, dest in (("instset-heads.cfg", "instset-heads.cfg"),
                           ("default-heads.org", "ancestor.org"), ("analyze.cfg", "analyze.cfg")):
        shutil.copyfile(support / original, piece / dest)
    overrides = {"RANDOM_SEED": seed, "VERBOSITY": 0, "WORLD_X": 60, "WORLD_Y": 60,
                 "WORLD_GEOMETRY": 2, "DATA_DIR": "data", "ENVIRONMENT_FILE": "environment.cfg",
                 "EVENT_FILE": "events.cfg", "COPY_MUT_PROB": 0.0075,
                 "DIVIDE_INS_PROB": 0.05, "DIVIDE_DEL_PROB": 0.05}
    (piece / "avida.cfg").write_text(configured((support / "avida.cfg").read_text(), overrides))
    (piece / "environment.cfg").write_text("# selector-v1; all 77 detectors remain present\n" + "".join(
        "REACTION {reaction} {task} process:value={value:.17g}:type=pow requisite:max_count=1\n".format(
            **task, value=value) for task, value in zip(tasks, values)))
    (piece / "events.cfg").write_text(event_text(boundary, previous is not None))
    if previous is not None:
        shutil.copyfile(previous, piece / "input.spop")
    dump(piece / "pay.json", {"seed": seed, "values": values})


def load_control(path, tasks, rig, args):
    donor = json.loads(Path(path).read_text())
    require(donor.get("complete") is True, "donor schedule is incomplete")
    require(donor["tasks"] == tasks and donor["rig"] == rig, "donor task manifest/rig differs")
    require(donor["piece_updates"] == args.piece_updates and len(donor["values"]) == args.pieces,
            "donor duration differs")
    require(donor["seed"] != args.seed, "fixed/replay requires a different recipient seed")
    require(all(len(row) == len(tasks) and all(isinstance(x, (int, float)) and math.isfinite(x) and x >= 0
                                            for x in row) for row in donor["values"]), "invalid pay vector")
    return donor["values"]


def run(args):
    source, binary, output = Path(args.source).resolve(), Path(args.avida).resolve(), Path(args.out).resolve()
    require(binary.is_file(), "Avida executable missing")
    head = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    require(head == PIN, "source checkout is not pinned commit " + PIN)
    clean = subprocess.run(["git", "-C", str(source), "diff", "--quiet", "HEAD", "--"])
    require(clean.returncode == 0, "pinned source has tracked modifications")
    tasks = manifest(source)
    support = source / "avida-core/support/config"
    rig_files = [support / n for n in ("avida.cfg", "instset-heads.cfg", "default-heads.org", "analyze.cfg")]
    rig_files += [support / "misc/environment-all-logic.cfg", source / "avida-core/source/main/cTaskLib.cc"]
    rig = {"commit": head, "spec": SPEC, "binary_sha256": sha(binary),
           "inputs": {str(p.relative_to(source)): sha(p) for p in rig_files}, "world": [60, 60]}
    require(not output.exists(), "output directory already exists; preserve it and choose a new path")
    donor_values = load_control(args.schedule, tasks, rig, args) if args.mode in ("replay", "fixed") else None
    fixed = mean_schedule(donor_values) if args.mode == "fixed" else None
    output.mkdir(parents=True)
    dump(output / "task_manifest.json", tasks)
    dump(output / "run_config.json", {"args": vars(args), "rig": rig, "driver_sha256": sha(__file__)})
    history, exposure = [[0.0] * len(tasks)], [0.0] * len(tasks)
    schedule = {"spec": SPEC, "rig": rig, "tasks": tasks, "mode": args.mode, "seed": args.seed,
                "piece_updates": args.piece_updates, "values": [], "complete": False}
    observations, previous = [], None
    previous_common, cumulative_common = set(), set()
    boundary = args.piece_updates - 1
    for index in range(args.pieces):
        if args.mode == "replay":
            values = list(donor_values[index])
        elif args.mode == "fixed":
            values = list(fixed)
        elif index == 0 or args.mode == "all77":
            values = [args.budget / len(tasks)] * len(tasks)
        elif args.mode == "progress":
            values = progress(history, args.window, args.budget)
        else:
            values = rarity(exposure, args.budget)
        require(all(math.isfinite(v) and v >= 0 for v in values), "invalid selector output")
        piece = output / ("piece-%05d" % index)
        seed = piece_seed(args.seed, index)
        prepare(piece, support, tasks, values, seed, boundary, previous)
        command = [str(binary), "-c", "avida.cfg"]
        dump(piece / "command.json", {"cwd": str(piece), "argv": command})
        if args.dry_run:
            print("DRY RUN: prepared piece 1 only; no Avida process executed")
            print("tasks=77 world=60x60 local_exit=" + str(boundary) + " actual_updates=" + str(args.piece_updates))
            print("next pieces require observed counts or a donor schedule; no counts fabricated")
            return
        with (piece / "stdout.log").open("w") as out, (piece / "stderr.log").open("w") as err:
            result = subprocess.run(command, cwd=piece, stdout=out, stderr=err)
        require(result.returncode == 0, "Avida failed; inspect " + str(piece / "stderr.log"))
        count, counts, shares = observe(piece, tasks, boundary)
        previous = piece / "data" / ("population-%d.spop" % boundary)
        require(previous.is_file() and previous.stat().st_size > 0, "saved program population missing")
        history.append(shares)
        exposure = [a + p for a, p in zip(exposure, shares)]
        schedule["values"].append(values)
        offered = [any(row[j] > 0 for row in schedule["values"]) for j in range(len(tasks))]
        current_common, changes = common_changes(shares, counts, previous_common, cumulative_common)
        record = {"piece": index, "global_updates": (index + 1) * args.piece_updates,
                  "local_label": boundary, "seed": seed, "living": count, "counts": counts, "shares": shares,
                  "tasks_present": sum(x > 0 for x in counts), "common_10pct": sum(x >= 0.1 for x in shares),
                  "never_offered_pay_common": sum(p >= 0.1 and not paid for p, paid in zip(shares, offered)),
                  "pay_total": sum(values), "zero_pay": not any(values),
                  "snapshot": str(previous.relative_to(output)), "snapshot_sha256": sha(previous)}
        record.update(changes)
        previous_common = current_common
        cumulative_common |= current_common
        observations.append(record)
        dump(output / "observations.json", observations)
        dump(output / "state.json", {"history": history, "exposure": exposure, "completed_pieces": index + 1})
        dump(output / "schedule.json", schedule)
        print("piece=%d global_updates=%d local_label=%d live=%d present=%d common10=%d pay_total=%.6g" % (
            index + 1, record["global_updates"], boundary, count, record["tasks_present"],
            record["common_10pct"], record["pay_total"]), flush=True)
    schedule["complete"] = True
    dump(output / "schedule.json", schedule)
    dump(output / "fixed_values.json", {"tasks": tasks, "values": mean_schedule(schedule["values"])})
    print("complete pieces=%d actual_updates=%d" % (args.pieces, args.pieces * args.piece_updates))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="read-only pinned Avida git checkout")
    parser.add_argument("--avida", required=True)
    parser.add_argument("--out", required=True, help="new output directory")
    parser.add_argument("--mode", choices=("progress", "archive", "fixed", "replay", "all77"), required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--piece-updates", type=int, default=1000)
    parser.add_argument("--pieces", type=int, default=50)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--budget", type=float, default=7.7)
    parser.add_argument("--schedule", help="complete donor schedule.json for fixed/replay")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    require(args.piece_updates > 0 and args.pieces > 0 and args.window > 0, "lengths/window must be positive")
    require(math.isfinite(args.budget) and 0 < args.budget <= 20, "budget must be in (0,20]")
    require((args.mode in ("replay", "fixed")) == bool(args.schedule), "schedule required only for fixed/replay")
    run(args)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(1)
```

### File: avida.cfg.changes

```text
# Replace these entries in pinned support/config/avida.cfg, once each.
# All other entries and the stock #include INST_SET=instset-heads.cfg remain.
# @SEED@ is the positive deterministic per-piece seed written by run.py.
RANDOM_SEED @SEED@
VERBOSITY 0
WORLD_X 60
WORLD_Y 60
WORLD_GEOMETRY 2
DATA_DIR data
ENVIRONMENT_FILE environment.cfg
EVENT_FILE events.cfg
COPY_MUT_PROB 0.0075
DIVIDE_INS_PROB 0.05
DIVIDE_DEL_PROB 0.05
```

### File: environment.cfg.template

```text
# Repeat the following line once for each of the 77 manifest entries.
# @REACTION@ and @TASK@ are from pinned misc/environment-all-logic.cfg.
# @VALUE@ is the selected nonnegative exponent, printed with 17 significant digits.
# Initial values are all 0.1 for B=7.7. All detectors stay present when value is 0.
REACTION @REACTION@ @TASK@ process:value=@VALUE@:type=pow requisite:max_count=1
```

### File: events-first.cfg

```text
# N=1000 actual updates: local labels 0 through 999.
u begin Inject ancestor.org
u 999 PrintTasksData
u 999 PrintCountData
u 999 PrintAverageData
u 999 PrintTimeData
u 999 SavePopulation filename=population:save_historic=0
u 999 Exit
```

### File: events-reload.cfg

```text
# input.spop is an exact file copy of the previous piece's saved snapshot.
# No optional update argument: the new process retains its initial label -1.
u begin LoadPopulation input.spop
u 999 PrintTasksData
u 999 PrintCountData
u 999 PrintAverageData
u 999 PrintTimeData
u 999 SavePopulation filename=population:save_historic=0
u 999 Exit
```

### File: measure_orders.py

```python
#!/usr/bin/env python3
"""Stock 47f13dad saved-sequence assays; Python 3 standard library only.

Run six serial test-CPU assays. This measures the stock last-cycle task record,
not every output, and uses a fixed diagnostic triple rather than live cell input
numbers. An all-orders task requires the SAME saved sequence to pass all orders.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess
import sys


DEFAULT_INPUTS = (0x0F13149F, 0x3308E53E, 0x556241EB)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_table(path):
    columns, rows, legends = None, [], {}
    for line in Path(path).read_text().splitlines():
        if line.startswith("#format "):
            require(columns is None, f"Duplicate #format in {path}")
            columns = line.split()[1:]
        match = re.fullmatch(r"#\s*(\d+):\s*(.*)", line)
        if match:
            key = int(match[1]) - 1
            require(key not in legends, f"Duplicate legend in {path}")
            legends[key] = match[2].strip()
        if line.strip() and not line.startswith("#"):
            rows.append(line.split())
    require(columns, f"Missing #format in {path}")
    require(rows, f"No saved sequence rows in {path}")
    require(all(len(row) == len(columns) for row in rows), f"Wrong row width in {path}")
    return columns, rows, legends


def source_rows(path):
    columns, rows, _ = read_table(path)
    require({"id", "sequence", "num_units"} <= set(columns),
            "Snapshot must be stock SavePopulation with id, sequence, num_units")
    require(len(columns) == len(set(columns)), "Repeated snapshot column")
    result = {}
    for values in rows:
        row = dict(zip(columns, values))
        key, count = int(row["id"]), int(row["num_units"])
        require(key not in result and count >= 0, "Duplicate ID or negative abundance")
        result[key] = (count, row["sequence"])
    require(sum(r[0] for r in result.values()) > 0, "Empty program population")
    return result


def assay_rows(path, source, manifest):
    columns, rows, legends = read_table(path)
    expected = ["id", "num_cpus", "sequence", "viable"]
    # This pinned build writes repeated 'task' names; match numbered descriptions.
    expected += ["task"] * len(manifest)
    require(columns == expected, f"Unexpected assay columns in {path}")
    for j, task in enumerate(manifest):
        require(legends.get(4 + j) == task["description"],
                f"Absent or mismatched task detector {task['task']} in {path}")
    result = {}
    for values in rows:
        row = dict(zip(columns[:4], values[:4]))
        key, count, passes = int(row["id"]), int(row["num_cpus"]), int(row["viable"])
        require(key not in result, "Repeated ID in assay")
        require(key in source and source[key] == (count, row["sequence"]),
                "Assay ID, abundance or sequence differs from snapshot")
        require(passes in (0, 1), "Invalid replication-pass flag")
        counts = tuple(map(int, values[4:]))
        require(all(n >= 0 for n in counts), "Negative task count")
        result[key] = (passes, counts)
    require(set(result) == set(source), "Missing saved sequences in assay")
    return result


def weighted_counts(source, orders, task_count, require_replication=False):
    return [sum(n for key, (n, _) in source.items()
                if all(row[key][1][j] > 0 and
                       (not require_replication or row[key][0] == 1)
                       for row in orders))
            for j in range(task_count)]


def summarize(source, orders, task_names):
    total = sum(n for n, _ in source.values())
    result = {}
    for scope, selected in (("native", orders[:1]), ("all6", orders)):
        for replication in (False, True):
            label = scope + ("_replication_pass" if replication else "_task_record")
            counts = weighted_counts(source, selected, len(task_names), replication)
            common = [name for name, count in zip(task_names, counts) if 10 * count >= total]
            result[label] = {"counts": counts, "shares": [n / total for n in counts],
                             "common_tasks": common, "common_count": len(common)}
    return result


def file_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--avida", type=Path, required=True)
    parser.add_argument("--piece", type=Path, required=True, help="Driver piece directory")
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="New output directory")
    parser.add_argument("--inputs", type=lambda s: int(s, 0), nargs=3, default=DEFAULT_INPUTS)
    parser.add_argument("--baseline", type=Path, help="Earlier measurement.json for the same assay")
    parser.add_argument("--schedule", type=Path, help="Driver schedule.json; include offers through this piece")
    parser.add_argument("--ever-offered", type=Path,
                        help="JSON array of task names offered positive pay up to this snapshot")
    parser.add_argument("--timeout", type=float, default=600.0, help="Seconds per order")
    args = parser.parse_args()
    args.avida, args.piece = args.avida.resolve(), args.piece.resolve()
    args.snapshot, args.manifest = args.snapshot.resolve(), args.manifest.resolve()
    args.out = args.out.resolve()
    require(not args.out.exists(), "Output directory already exists; use a new directory")
    require(args.timeout > 0, "Timeout must be positive")
    require(all(-(1 << 31) <= n < (1 << 31) for n in args.inputs), "Inputs need signed 32-bit range")
    require(len(set(args.inputs)) == 3, "Use three distinct input numbers")
    require({sum(((n >> bit) & 1) << j for j, n in enumerate(args.inputs))
             for bit in range(32)} == set(range(8)),
            "Diagnostic triple must contain every three-input bit combination")
    # Avida's LOAD/DETAIL command parser separates words on whitespace.
    for path in (args.snapshot, args.out):
        require(not any(c.isspace() for c in str(path)), "Use paths without whitespace")
    manifest = json.loads(args.manifest.read_text())
    require(isinstance(manifest, list) and len(manifest) == 77, "Expected the ordered 77-task manifest")
    names = [item["task"] for item in manifest]
    require(len(set(names)) == 77, "Duplicate task name in manifest")
    require(not (args.schedule and args.ever_offered), "Use schedule or ever-offered, not both")
    offered = None
    if args.schedule:
        schedule = json.loads(args.schedule.read_text())
        match = re.fullmatch(r"piece-(\d+)", args.piece.name)
        require(match is not None, "Schedule requires driver directory piece-NNNNN")
        number = int(match[1])
        require(schedule["tasks"] == manifest and len(schedule["values"]) > number,
                "Schedule does not match manifest or cover this piece")
        values = schedule["values"][:number + 1]
        require(all(len(row) == 77 and all(isinstance(v, (int, float)) and
                    v >= 0 and v < float("inf") for v in row) for row in values),
                "Invalid schedule values")
        offered = [name for j, name in enumerate(names) if any(row[j] > 0 for row in values)]
    elif args.ever_offered:
        offered = json.loads(args.ever_offered.read_text())
        require(isinstance(offered, list) and set(offered) <= set(names), "Invalid offered-task list")
    source = source_rows(args.snapshot)
    args.out.mkdir(parents=True)
    orders, invocations = [], []
    for k, permutation in enumerate(itertools.permutations(args.inputs)):
        directory = args.out / f"order-{k}"
        directory.mkdir()
        analyze = directory / "analyze.cfg"
        detail = directory / "counts.dat"
        fields = " ".join(f"task.{j}" for j in range(77))
        analyze.write_text(f"LOAD {args.snapshot}\nRECALCULATE 0 -1 0 " +
                           " ".join(map(str, permutation)) +
                           f"\nDETAIL {detail} id num_cpus sequence viable {fields}\n")
        (directory / "events.cfg").write_text("# No simulation events in this assay.\n")
        command = [str(args.avida), "-a", "-c", "avida.cfg", "-s", "1",
                   "-set", "ANALYZE_FILE", str(analyze),
                   "-set", "DATA_DIR", str(directory / "data"),
                   "-set", "EVENT_FILE", str(directory / "events.cfg")]
        record = {"cwd": str(args.piece), "argv": command, "inputs": list(permutation)}
        invocations.append(record)
        (directory / "command.json").write_text(json.dumps(record, indent=2) + "\n")
        with (directory / "avida.log").open("w") as log:
            completed = subprocess.run(command, cwd=args.piece, stdout=log,
                                       stderr=subprocess.STDOUT, timeout=args.timeout)
        require(completed.returncode == 0, f"Avida failed in {directory}; inspect avida.log")
        log = (directory / "avida.log").read_text()
        require(not re.search(r"(?im)^\s*(?:error|fatal)(?:\s|:)", log),
                f"Avida reported an error in {directory}")
        require(detail.is_file(), f"No assay output in {directory}")
        orders.append(assay_rows(detail, source, manifest))
    result = {"schema": 1, "method": "stock_last_cycle_fixed_input_diagnostic",
              "native_inputs": list(args.inputs), "task_names": names,
              "total_programs": sum(n for n, _ in source.values()),
              "saved_sequence_rows": len(source),
              "assays": invocations,
              "sha256": {"avida": file_sha256(args.avida),
                         "snapshot": file_sha256(args.snapshot),
                         "manifest": file_sha256(args.manifest),
                         "avida.cfg": file_sha256(args.piece / "avida.cfg"),
                         "environment.cfg": file_sha256(args.piece / "environment.cfg"),
                         "instset-heads.cfg": file_sha256(args.piece / "instset-heads.cfg")},
              "replication_failed_programs_per_order":
                  [sum(n for key, (n, _) in source.items() if order[key][0] == 0)
                   for order in orders],
              "measures": summarize(source, orders, names)}
    if offered is not None:
        result["never_offered_tasks"] = [name for name in names if name not in offered]
        for measure in result["measures"].values():
            measure["common_never_offered"] = [name for name in measure["common_tasks"] if name not in offered]
    else:
        result["never_offered_tasks"] = None
    if args.baseline:
        baseline = json.loads(args.baseline.read_text())
        require(baseline["method"] == result["method"] and
                baseline["native_inputs"] == result["native_inputs"] and
                baseline["task_names"] == names and
                baseline["sha256"]["instset-heads.cfg"] == result["sha256"]["instset-heads.cfg"] and
                baseline["sha256"]["avida"] == result["sha256"]["avida"],
                "Baseline assay differs in method, inputs, tasks, instruction set or executable")
        for key, measure in result["measures"].items():
            initial = set(baseline["measures"][key]["common_tasks"])
            measure["newly_common_since_baseline"] = [n for n in measure["common_tasks"] if n not in initial]
            measure["common_count_change"] = measure["common_count"] - len(initial)
    destination = args.out / "measurement.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print("programs=" + str(result["total_programs"]))
    print("orders=6; all6 uses the same saved sequence in every order")
    for key, measure in result["measures"].items():
        print(key + " common=" + str(measure["common_count"]))
    print("never_offered=" + ("unknown" if result["never_offered_tasks"] is None
                              else str(len(result["never_offered_tasks"]))))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.TimeoutExpired) as error:
        print("measurement error: " + str(error), file=sys.stderr)
        sys.exit(1)
```

### File: selftest.py

```python
#!/usr/bin/env python3
"""Self-authored rig cases fixed in SPEC-v1.md; no Avida process is invoked."""
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import run


def close(actual, expected):
    assert len(actual) == len(expected)
    assert all(abs(a - e) < 1e-12 for a, e in zip(actual, expected)), (actual, expected)


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError("case was not rejected")


def main():
    close(run.progress([[0.0], [0.2]], 5, 7.7), [1.54])
    print("development: A 0 -> 0.2 gives 1.54")
    close(run.progress([[0.0], [0.2], [0.2]], 1, 7.7), [0.0])
    close(run.progress([[0.2], [0.1]], 5, 7.7), [0.0])
    close(run.progress([[0.0, 0.0], [0.2, 0.1]], 5, 7.7), [1.54, 0.77])
    close(run.rarity([0, 0], 7.7), [3.85, 3.85])
    close(run.rarity([1, 0], 7.7), [7.7 / 3, 7.7 * 2 / 3])
    close(run.mean_schedule([[0.0, 2.0], [2.0, 4.0]]), [1.0, 3.0])
    current, changes = run.common_changes([0.2, 0.0, 0.2], [720, 0, 720], {1}, {0, 1})
    assert current == {0, 2}
    assert changes == {"common_360cells": 2, "cumulative_common": 3,
                       "first_common": [2], "reacquired": [0], "lost": [1]}
    assert "u 1 Exit\n" in run.event_text(2 - 1, False)
    assert "u begin LoadPopulation input.spop\n" in run.event_text(1, True)
    print("selectors: plateau=0 decline=0 growth_ratio=2 archive_ratio=1:2 fixed_means=1,3")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "data").mkdir()
        tp, cp = root / "data/tasks.dat", root / "data/count.dat"
        tasks = [{"description": "Alpha"}, {"description": "Beta"}]
        good_tasks = "# 3: Alpha\n# 1: Update\n# 2: Beta\n1 2 4\n"
        good_counts = "# 1: update\n# 2: number of organisms\n1 10\n"
        tp.write_text(good_tasks)
        cp.write_text(good_counts)
        count, counts, shares = run.observe(root, tasks, 1)
        assert count == 10 and counts == [4, 2]
        close(shares, [0.4, 0.2])
        for bad in ("# 1: Update\n# 2: Beta\n1 2\n",
                    good_tasks.replace("# 3: Alpha", "# 2: Alpha"),
                    good_tasks.replace("1 2 4", "2 2 4"),
                    good_tasks.replace("1 2 4", "1 2 11")):
            tp.write_text(bad)
            rejects(lambda: run.observe(root, tasks, 1))
        tp.write_text(good_tasks)
        cp.write_text(good_counts.replace("1 10", "1 0"))
        rejects(lambda: run.observe(root, tasks, 1))
        path = root / "schedule.json"
        values = [[0.0, 2.0], [2.0, 4.0]]
        path.write_text(json.dumps({"complete": True, "tasks": tasks, "rig": {},
                                    "piece_updates": 2, "values": values, "seed": 1}))
        args = SimpleNamespace(piece_updates=2, pieces=2, mode="replay", seed=2)
        assert run.load_control(path, tasks, {}, args) == values
        args.seed = 1
        rejects(lambda: run.load_control(path, tasks, {}, args))
        args.mode = "fixed"
        rejects(lambda: run.load_control(path, tasks, {}, args))
    print("tables: reordered descriptions accepted; missing/duplicate/misaligned/oversized/empty rejected")
    print("controls: replay unchanged; same-seed fixed/replay rejected; N=2 exits at label 1")
    print("measurement: first=[2] reacquired=[0] lost=[1] cumulative=3")
    print("selftest complete; no Avida process executed")


if __name__ == "__main__":
    main()
```

### File: attack.py

```python
#!/usr/bin/env python3
"""Added after planned cases passed: reject damaged donor schedules, without Avida."""
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import run

with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "schedule.json"
    args = SimpleNamespace(piece_updates=100, pieces=1, mode="replay", seed=2)
    original = {"complete": True, "tasks": [], "rig": {}, "piece_updates": 100,
                "values": [[]], "seed": 1}
    for key, value, label in (("complete", False, "incomplete schedule"),
                              ("rig", {"different": 1}, "different rig")):
        changed = dict(original)
        changed[key] = value
        path.write_text(json.dumps(changed))
        try:
            run.load_control(path, [], {}, args)
        except ValueError:
            print("rejected: " + label)
        else:
            raise AssertionError("accepted " + label)
print("added adversarial cases complete; no Avida process executed")
```

### File: check_aggregation.py

```python
#!/usr/bin/env python3
"""Synthetic counterexample: per-order shares are not same-sequence conjunctions."""
from measure_orders import summarize


source = {101: (5, "sequence-A"), 202: (5, "sequence-B")}
orders = []
for number in range(6):
    # Task x switches between two disjoint halves of the saved program population.
    # Task y stays in sequence A, whose replication flag fails in the last order.
    orders.append({101: (int(number != 5), (int(number < 3), 1)),
                   202: (1, (int(number >= 3), 0))})
result = summarize(source, orders, ["x", "y"])
per_order_x = [sum(source[key][0] for key in source if row[key][1][0] > 0)
               for row in orders]
assert per_order_x == [5] * 6
assert result["native_task_record"]["counts"] == [5, 5]
assert result["all6_task_record"]["counts"] == [0, 5]
assert result["all6_replication_pass"]["counts"] == [0, 0]
print("synthetic x: per-order counts=5,5,5,5,5,5; minimum=5; same-sequence all6=0")
print("synthetic y: all6 task-record count=5; all6 replication-pass count=0")

# The denominator is every saved program, including failed replication tests;
# the 10% boundary is inclusive and uses integer arithmetic.
edge = summarize({1: (1, "a"), 2: (9, "b")},
                 [{1: (1, (1,)), 2: (0, (0,))}] * 6, ["x"])
assert edge["all6_replication_pass"]["shares"] == [0.1]
assert edge["all6_replication_pass"]["common_count"] == 1
print("synthetic boundary: 1/10 remains common; failed tests stay in denominator")
```

### File: make_positive_fixture.py

```python
#!/usr/bin/env python3
"""Re-encode a pinned stock Avida test fixture by instruction name; no live run."""
from pathlib import Path
import sys


def words(path):
    return [text.split() for line in path.read_text().splitlines()
            if (text := line.split("#", 1)[0].strip())]


source, piece, destination = map(Path, sys.argv[1:])
instructions = [row[1] for row in words(piece / "instset-heads.cfg") if row[0] == "INST"]
assert len(instructions) == 26 and len(set(instructions)) == 26
symbols = dict(zip(instructions, "abcdefghijklmnopqrstuvwxyz"))
paths = [source / "avida-core/tests/resources_9r/config/9task.org", piece / "ancestor.org"]
sequences = ["".join(symbols[row[0]] for row in words(path)) for path in paths]
with destination.open("x") as stream:
    stream.write("#filetype genotype_data\n#format id num_units sequence\n")
    for key, count, sequence in zip((1, 2), (1, 9), sequences):
        stream.write(f"{key} {count} {sequence}\n")
print("synthetic fixture: stock 9task.org abundance=1; stock ancestor abundance=9")
print("instruction counts=" + ",".join(str(len(s)) for s in sequences))
```

### File: calculate_sizes.py

```python
from math import sqrt
from statistics import NormalDist, variance
import scipy
from scipy.stats import nct, t
zsum2 = (NormalDist().inv_cdf(.9875) + NormalDist().inv_cdf(.8)) ** 2
print('sample_variances=%.6f,%.6f' % (variance([48,55,65]), variance([13,32,41])))
print('z_sum_squared=%.6f' % zsum2)
for difference_variance in [2*variance([13,32,41]), 4*variance([13,32,41])]:
    for n in range(2, 1000):
        critical = t.ppf(.9875, n-1)
        shift = 10*sqrt(n/difference_variance)
        power = nct.sf(critical,n-1,shift)+nct.cdf(-critical,n-1,shift)
        if power >= .8:
            print('n=%d; difference=10; difference_variance=%.6f; model_power=%.6f; total_runs=%d; cpu_hours_100k=%d; phased_wall_hours_100k=%d' %
                  (n,difference_variance,power,8*n,16*n,2*((2*n+2)//3+(6*n+2)//3)))
            break
print('Python SciPy version:',scipy.__version__)
```

END OF REPORT
