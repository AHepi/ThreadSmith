# Testing the execution environment claim in stock Avida

## Summary for the owner

I ran two programs that gave the same answer but kept different working notes. After the same instruction change, one performed NAND and the other performed no recognized task. Both still replicated. Their surroundings were identical; the retained calculation made the difference.

The supplied results support treating the execution environment as a causal part of learning: it supplies instruction meanings, inputs and rewards. They also support treating the programs as causal parts: disabling particular instructions removes capabilities while replication continues. Neither observation makes the other disappear.

The productive version of your proposal is that changing environments may sustain the acquisition of capabilities. The exclusive version—that internal arrangements cannot affect that acquisition—makes a different, testable claim. The existing results do not decide which environments sustain learning, or whether any do so indefinitely.

This report supplies two stock-Avida experiments. The first changes one instruction in two programs that initially perform the same task. The second crosses those starting programs with continuous reward schedules, separating a founder effect, a reward effect and their interaction. It preserves the running population when rewards change.

The experiments address finite task acquisition and retention. They do not equate Avida fitness with knowledge, and they do not treat a changed reward as a newly acquired capability. Local execution status and exact files appear below.

## The case for the environment

**Checked against the supplied brief, “Dependence on the execution environment”; reported measurements, not independently rerun:** changing `nand` to `nor` changed the tasks programs performed; disabling `IO` removed task performance; shuffling all instruction meanings removed replication in the tested programs. A sequence has no computational capability independently of how it is executed. The environment is a working part, not scenery.

**Checked against the brief, “Holding on through instruction changes”:** no instruction checked or repaired copies in those observations. Computational selection removed unsuccessful copies. That supports a population-level account of persistence without assigning copy repair to individual programs. “No task rewards” still permits selection through differential replication; it does not remove computational selection.

**Checked against the brief, “New capabilities” and “What that information is”:** the ancestor performed no task, whereas EQU appeared in six of nine runs; many instruction sequences and routes carried the same circuit. An environment-centered account can therefore explain why particular written routes need not be prescribed. The execution environment admits variations and rewards some of their consequences.

The strongest inference is a research conjecture: once a fixed reward menu no longer differentiates useful new behavior, changing the challenges might allow further acquisition. That inference requires a new test. The six pending environments have no reported results here. Their existence supplies no evidence of continued learning.

The NAND-to-NOR result is especially informative but shared by both accounts. Predicting each changed output from its traced circuit uses instruction semantics **and** the program's wiring. It cannot assign all causal work to either one.

## The case for the programs

**Checked against the brief, “What had to be removed to stop a task”:** for 98% of the reported sequence–task pairs, one instruction ablation removed the task while replication continued. This intervenes inside a program under the same execution rules. Conditional on the reported controls, it already counts against literal internal irrelevance.

**Checked against the brief, “What that information is”:** 7,925 distinct instruction sequences carried one NOT circuit through 347 written routes. This makes a particular spelling dispensable; it does not make the input-to-output dependency dispensable. Likewise, removing an apparently unused `IO` read can change all subsequent input identities. That instruction affects the computation through timing rather than through a stored arithmetic result.

**Checked against the brief, “Holding on through instruction changes”:** evolved programs differed in the instruction changes under which they retained replication and exact Avida fitness. Those are properties of a sequence **in an execution environment**. They provide a reason to test whether different internal arrangements supply different future capabilities or retention, not a guarantee that they will.

Earlier circuits could make later construction possible through retained intermediate results, accessible instruction changes or preserved routing. The supplied endpoint circuits alone do not show historical reuse. A minimal circuit is not necessarily resistant to instruction changes or readily extended.

Nor does an environment's historical role in producing a program remove the program's present role. A reward history can produce a particular arrangement, and changing that arrangement can subsequently change what happens under unchanged rewards.

## Where they predict different results

The frozen question is: **within the nine-task environment, do specified internal instruction changes and reward schedules change task production, acquisition or retention over the stated horizons?** The brief supplies the question; the horizons, founders and thresholds below are added experimental choices. Unlimited learning is outside this finite test.

“Environment” means the interpreter, inputs, rewards and replication rules. It does not absorb the instruction sequence or the current population into its definition after an unfavorable result.

| Account | Commitment | Distinguishing observation |
|---|---|---|
| Environment as a causal part | Changing instruction meanings, input availability or rewards can change behavior and persistence. | Both accounts accept this; it is not a separating prediction. |
| Exclusive environment account, made precise here | Programs matched on initial tasks and replication are interchangeable under the specified subsequent intervention. | Same intervention, different subsequent capability, counts against this additional invariance claim. |
| Programs as causal parts | Retained intermediate results and routing can change what an instruction change makes accessible. | Experiment A predicts a particular difference, with the same environment and intervention. |
| Environment as a route to continued learning | A changing schedule causes a specified later acquisition or retention effect. | Experiment B tests a finite schedule forecast; either outcome leaves unlimited learning open. |

A broad “both matter” account can also accommodate almost anything. It receives no automatic pass. Experiment A gives it an exact mechanistic forecast. Experiment B gives additional, explicitly conjectural population forecasts that may fail even if Experiment A behaves as predicted.

## Experiments

### Experiment A Same output different retained calculation

Construct founders A and C from the stock 100-instruction ancestor. Replace instructions 20–33, using zero-based positions, with the fourteen-instruction block in the appendix. A and C differ only at position 25: a register modifier makes a NAND calculation remain in register AX in A; C writes it to CX, which is subsequently overwritten. Both are intended to output NOT of the first input. They have identical length, input-read positions and replication scaffold.

Create A_probe and C_probe by applying the **same** second change, position 33 from `nop-B` to `nop-A`: the final `IO` now outputs AX. Preserve all four original files and hashes before execution. Reconstructing A from C by restoring position 25 is the rescue; the unedited founders are the task-preserving controls. The nine-task profile is the measured scope; unregistered capabilities are not claimed absent.

**Forecast, derived from the instruction semantics:** A and C perform NOT and replicate. A_probe performs NAND; C_probe performs neither NOT nor NAND. Thus the same instruction change exposes a retained calculation only where that calculation exists. This is an engineered mechanism test, not evidence that this route appeared spontaneously in the owner's populations.

The environment-only interchangeability claim predicts equal probe capabilities after the matched starting behavior. The predicted unequal probes count against it. Equal probes, failure of the intended NOT baseline, or a replication failure count against the stated mechanistic forecast or its preparation. Diagnose which before changing files; a repair creates a new test version.

Use the common zero-reward nine-task environment and zero instruction-change rates. Run the deterministic test-CPU assay and the prespecified random-input checks in the appendix. Check complete nine-task profiles, viability, length, merit and gestation time. These measurements guard against silently treating unmatched founders as matched. Task-free merit and gestation must be exactly equal between A and C for the intended matched contrast.

**Checked, local execution:** stock Avida 2.14.0 at the pinned commit compiled with no C++ changes. The frozen four programs produced the predicted pattern in the first graded-environment check. The exact appendix generator then ran the neutral assay, three shared cyclic input triples, 32 random-input repetitions and fixed graded/EQU-only baseline checks: 152 program evaluations, 0.790 seconds for that invocation on this host. These are repeated checks of a constructed case, not independent learning trials.

| Program | Recognized tasks in fixed neutral assay | Replicates | Length | Merit | Gestation | Avida fitness |
|---|---|---|---|---|---|---|
| A | NOT | Yes | 100 | 97 | 382 | 0.253927 |
| C | NOT | Yes | 100 | 97 | 382 | 0.253927 |
| A_probe | NAND | Yes | 100 | 97 | 382 | 0.253927 |
| C_probe | None of the nine | Yes | 100 | 97 | 382 | 0.253927 |

All four copied 100 instructions and executed 97 under the fixed neutral assay. A/C were also exactly matched under graded rewards (merit 194, fitness 0.507853) and EQU-only rewards (merit 97, fitness 0.253927); gestation stayed 382. Trace inspection immediately before the final output found AX = −50,332,703 in A and AX = 100 in C, while both had BX = −252,908,704. The probe changed which of those registers was output. Restoring the differing modifier recreates A byte-for-byte; it is not counted as another independent observation.

The cost is a small number of isolated program evaluations, not a 50,000-update population run. Report its actual elapsed time; do not extrapolate population timing to it. This experiment tests immediate accessibility under a specified change. It does not imply that A acquires NAND sooner during unconstrained instruction changes: C has other routes, including changes that expose a value before CX is overwritten.

### Experiment B Cross the founders with continuous reward schedules

Use A and C, without the probe edit. Each seeds all 3,600 cells as a uniform population, an explicit initial-density choice. Each founder receives both schedules and seeds **4101, 4102 and 4103**. This gives twelve runs of **60,000 updates**. Keep copy error at **0.0075** and division insertion and deletion at **0.05 each**. All other mutation channels are zero.

Check that A/C have equal initial profiles, merit and gestation under both graded and EQU-only rewards as well as the neutral assay. Later differences in births can mediate founder and reward effects; equal updates do not mean equal numbers of instruction-change opportunities.

Both schedules initially reward the nine tasks using the brief's exponents. At update 20,000, the switch arm sets all exponents to zero, then EQU to five. At update 40,000 it restores the original nine rewards. The fixed arm writes its existing reward values at the same times as a sham. It continues with the same rewards. Both run continuously; saved populations are measurements, never reload points.

**Checked, pinned source:** `SetReactionValue` changes the configured reaction value without restarting CPUs. `type=pow` uses the value as an exponent; zero gives no reward multiplier beyond one. This action does not retrospectively remove previously accumulated bonuses. `PrintTasksData` uses task counts from completed program cycles, so readings immediately at a switch are not instantaneous assays of the new setting. Source locations are in the appendix.

Record tasks, population counts, generations, cumulative births and averages every 100 updates; save populations every 1,000. Analyze snapshots at 0, 19,000, 20,000, 21,000, 39,000, 40,000, 41,000 and 60,000 in the same zero-reward environment, evaluating every distinct sequence and weighting its task indicator by its saved program count. Keep fractions among viable assay programs and among all saved programs separate. Never replace capability with Avida fitness.

The primary population outcome is EQU prevalence in the common assay at 60,000. Record whether EQU was absent at 20,000: if it was already present, its later increase is spread or retention, not first acquisition. Also report first observed EQU, the first three consecutive 100-update observations with at least 10% EQU, and NOT retention. A run without acquisition remains in the results as “not observed by 60,000.” Extinction also remains in the results.

| Forecast fixed before the twelve runs | Result counting against it |
|---|---|
| Finite founder invariance: exchanging A and C produces no founder-dependent EQU endpoint contrast within either schedule. | A founder contrast of at least 20 percentage points in each of the three seed pairs at 60,000, with the same sign within either schedule, is the prespecified diagnostic against invariance. |
| Added population conjecture: changing the founder modifier leaves the specified final prevalence contrast. Direction is unspecified; the immediate probe does not supply one. | Failure to produce the stated contrast counts against this finite conjecture. It does not undo the immediate mechanism, or demonstrate general founder invariance. |
| Added schedule conjecture: the EQU-only interval increases common-assay EQU prevalence at 39,000 by at least 20 percentage points in each of the three seed pairs relative to fixed rewards, for each founder. | No such contrast, a reversed contrast, or only a fitness change counts against this particular schedule forecast. A ceiling because fixed runs already perform EQU is a failure of this forecast too. |

The 20-point and 10% cutoffs are declared design choices, not facts about knowledge. Report every run and raw contrast. Three seeds make this a diagnostic experiment; satisfying a pattern is not a precise estimate of a population-wide causal probability, and failing to observe an effect is not an equivalence finding. Identical seed numbers block preparation choices but do not guarantee synchronized random draws after programs diverge.

The founder-by-schedule comparison can show that a reward change has different consequences for the two starting programs. A reward effect alone fits both broad accounts. Equal pre-switch output within each same-founder, same-seed schedule pair is a preparation control; unexplained divergence before 20,000 must be resolved before interpreting a paired switch effect.

**Cost estimate derived from the brief:** twelve times 60,000/50,000 hours gives **14.4 process-hours**, approximately **4.8 wall-clock hours** with three simultaneous Avida processes. This excludes compilation, common assays and output overhead; changed program behavior can alter the timing. Use a separate short timing run, preserve its files, and do not select outcome seeds based on it. The appendix launcher never exceeds three Avida processes.

## What the experiments would leave open

These tests do not decide whether environmental redesign can produce unbounded novelty. Nine recognized tasks are a finite detector. Registering 77 tasks would expand that detector, not remove its boundary; the two experiments deliberately keep the same nine tasks throughout.

An engineered retained calculation is not evidence of historical reuse in evolved programs. For that claim, recover an actual ancestry, identify an earlier intermediate used in a later capability, and intervene without destroying the intended baseline. Whole-founder effects alone cannot separate robustness, routing, replication cost and other changed features.

The experiments cannot allocate percentages of causal responsibility between programs and environments. They also do not decide constructor theory's account of knowledge, identify a universal minimum of static knowledge, or demonstrate active copy repair. The brief's knowledge framing is a stipulated motivation; task acquisition is the measured proxy here.

They do not settle the separate save/reload check or the six pending environment experiments. Initial injection and offline test-CPU assays deliberately reset programs. They are standardized starting conditions and measurements, not claims to continue complete running state.

## Assumptions and what you are unsure of

All supplied numerical findings were checked against the attachment, not its underlying raw runs. The source and any local execution checks are separately identified. No outside-source claim relies solely on memory.

| Part in the owner's terms and source location | Hard-to-vary mark and reason |
|---|---|
| “instruction meanings,” “inputs,” “rewards”; Terms and Dependence | Held if the brief's reported interventions have the stated controls. The newly checked source fixes the proposed event semantics, not their long-run effects. |
| “required instructions”; task-ablation section | Held if the reported within-program interventions preserve replication and assay conditions. Necessity is relative to that program and ablation, not every possible implementation. |
| A particular “route”; circuit section | Loose where alternative written routes do the same job. The shared computation is the candidate dependency, not one spelling. |
| Internal structure as irrelevant to future acquisition; our precise reading of the owner's quote | Unknown for population acquisition before Experiment B; directly challenged by Experiment A's specified intervention. This extra invariance is not silently attributed to the owner's weaker research recommendation. |
| Earlier circuits being reused | Unknown in the supplied evolved ancestry; the constructed example only tests a possible mechanism. |
| Knowledge and stock-Avida scope | Fixed as the brief's framing and implementation constraints; not settled by these measurements. |

The environment recommendation originated as the owner's conjecture. The circuit and robustness descriptions are fitted to the reported runs. The new mechanisms and population forecasts are built proposals. Their origin is not evidence for their outcomes.

Removing the environment makes the claimed execution undefined; removing working instructions loses the reported task. Swapping one written route for another can preserve it. These checks support joint dependencies without requiring every detail to be unique. Both broad accounts can accommodate either acquisition or stalling; the explicit forecasts prevent that flexibility from passing as a discriminating test.

There is a practical tension: matching present task performance makes the internal contrast interpretable, but can conceal different reachable next states. Experiment A deliberately tests those next states. Conversely, extending an isolated result to freely evolving populations adds competition, alternative instruction changes and historical loss; Experiment B can therefore fail its added program forecast.

The 23,332 endpoint sequences descend from nine runs; they are not that many independent learning trials. Required-instruction counts depend on the ablation and inputs. Zero replicators among 10,000 sampled random programs does not describe every possible sequence. None of these quantities alone identifies a general learning mechanism.

The next action is to execute the frozen Experiment B files after the Experiment A baseline gate, retain every seed, and return task prevalence with the common-assay outputs. That supplies the currently missing population test without modifying Avida's C++.

## Appendix Complete configuration and event files

**Checked source pin:** [devosoft/avida commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16), identifying itself as version 2.14.0. The local build used unchanged C++ source. Build and short-test status are reported in Experiment A; the twelve long runs are not represented as completed.

| Checked source | What was inspected |
|---|---|
| [cHardwareCPU.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cHardwareCPU.cc) | `Inst_Nand`, `Inst_TaskIO`, `Inst_Push`, `Inst_Pop`, and register modifiers. |
| [cAvidaConfig.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cAvidaConfig.cc) and [cAvidaConfig.h](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cAvidaConfig.h) | Omitted keys take pinned compiled defaults; instruction definitions can be embedded. |
| [EnvironmentActions.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/EnvironmentActions.cc) and [cEnvironment.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cEnvironment.cc) | `SetReactionValue`, reward processing, task detection and fixed input triplets. |
| [PopulationActions.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/PopulationActions.cc) and [SaveLoadActions.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/SaveLoadActions.cc) | Injection range is end-exclusive; named snapshot syntax and output names. |
| [cStats.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cStats.cc) and [cAnalyze.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/analyze/cAnalyze.cc) | Task logs, birth totals, snapshot loading, fixed/manual/random input assays and output fields. |

Save the following complete code block as `make_runs.py`. It contains the full configuration contents, instruction set, both event schedules, environments, four 100-instruction programs and analysis files. It expands them into separate run directories without downloading anything or modifying Avida. Unlisted configuration options use the pinned executable's compiled defaults; these files are standalone, not overlays on another experiment. The nine explicit assignments at each switch keep all task detectors registered and use the same number of event calls in the sham.

The generator uses seed 1701 for isolated assays. Fixed/manual assays share exact input triples across programs. Its 32 random-input repetitions sample each program separately, so those repetitions are input-variation checks, not matched-input contrasts or instruction-change robustness measurements. Snapshot assays use the fixed triplet; capability beyond that input procedure remains open. The gate checks all four predicted profiles and exact A/C baseline equality before permitting population runs.

```python
#!/usr/bin/env python3
"""Create exact Brief 04 inputs; run only the explicitly chosen phase."""
import concurrent.futures as cf
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

PIN = "47f13dadb547fcf10f620ace60247f38b30b8b16"
TASKS = "NOT NAND AND ORN OR ANDN NOR XOR EQU".split()
VALUES = [1, 1, 2, 2, 3, 3, 4, 4, 5]
OPS = ("nop-A nop-B nop-C if-n-equ if-less if-label mov-head jmp-head "
       "get-head set-flow shift-r shift-l inc dec push pop swap-stk swap "
       "add sub nand h-copy h-alloc h-divide IO h-search").split()
CONFIG = """VERSION_ID 2.14.0
VERBOSITY 0
RANDOM_SEED 4101
MAX_CONCURRENCY 1
WORLD_X 60
WORLD_Y 60
WORLD_GEOMETRY 2
EVENT_FILE events.cfg
ENVIRONMENT_FILE environment.cfg
ANALYZE_FILE analyze.cfg
DATA_DIR data
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
COPY_UNIFORM_PROB 0
COPY_SLIP_PROB 0
POINT_MUT_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIV_UNIFORM_PROB 0
DIV_SLIP_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0.05
DIVIDE_DEL_PROB 0.05
DIVIDE_UNIFORM_PROB 0
DIVIDE_SLIP_PROB 0
DIVIDE_POISSON_MUT_MEAN 0
DIVIDE_POISSON_INS_MEAN 0
DIVIDE_POISSON_DEL_MEAN 0
DIVIDE_POISSON_SLIP_MEAN 0
INJECT_MUT_PROB 0
INJECT_INS_PROB 0
INJECT_DEL_PROB 0
PARENT_MUT_PROB 0
META_COPY_MUT 0
BIRTH_METHOD 0
PREFER_EMPTY 1
AVE_TIME_SLICE 30
SLICING_METHOD 1
TEST_CPU_TIME_MOD 20
""" + "INSTSET heads_default:hw_type=0\n" + "".join(
    "INST " + op + "\n" for op in OPS)
FIELDS = ("name viable length merit gest_time fitness copy_length exe_length "
          + " ".join("task." + str(i) for i in range(9))
          + " sequence env_input.0 env_input.1 env_input.2")
SNAPSHOTS = [0, 19000, 20000, 21000, 39000, 40000, 41000, 60000]

def put(path, text):
    path.write_text(text, encoding="utf-8")

def environment(values):
    return "".join(f"REACTION {t} {t.lower()} process:value={v}:type=pow "
                   "requisite:max_count=1\n" for t, v in zip(TASKS, values))

def config(seed, assay=False):
    s = CONFIG.replace("RANDOM_SEED 4101", f"RANDOM_SEED {seed}")
    if assay:
        for key, old in [("COPY_MUT_PROB", "0.0075"),
                         ("DIVIDE_INS_PROB", "0.05"),
                         ("DIVIDE_DEL_PROB", "0.05")]:
            s = s.replace(f"{key} {old}\n", f"{key} 0\n")
    return s

def founders():
    ancestor = (["h-alloc", "h-search", "nop-C", "nop-A", "mov-head"]
                + ["nop-C"] * 86
                + ["h-search", "h-copy", "if-label", "nop-C", "nop-A",
                   "h-divide", "mov-head", "nop-A", "nop-B"])
    assert len(ancestor) == 100
    a = ancestor.copy()
    a[20:34] = "IO nop-B IO nop-C nand nop-A push nop-B pop nop-C nand nop-B IO nop-B".split()
    c = a.copy()
    c[25] = "nop-C"
    result = {"A": a, "C": c}
    for name, tokens in list(result.items()):
        probe = tokens.copy()
        probe[33] = "nop-A"
        result[name + "_probe"] = probe
    return {n: "#inst_set heads_default\n#hw_type 0\n\n" + "\n".join(v) + "\n"
            for n, v in result.items()}

def events(schedule):
    lines = ["u begin InjectRange founder.org 0 3600"]
    for action in ["PrintTasksData", "PrintCountData", "PrintAverageData",
                   "PrintTimeData", "PrintTotalsData"]:
        lines.append(f"u 0:100:60000 {action}")
    lines.append("u 0:1000:60000 SavePopulation filename=detail:save_historic=0")
    for update in [20000, 40000]:
        values = [0] * 8 + [5] if schedule == "switch" and update == 20000 else VALUES
        for task, value in zip(TASKS, values):
            lines.append(f"u {update} SetReactionValue {task} {value}")
    lines.append("u 60000 Exit")
    return "\n".join(lines) + "\n"

def make(root):
    root.mkdir(parents=True, exist_ok=False)
    inputs = founders()
    assay = root / "A_assay"
    assay.mkdir()
    put(assay / "avida.cfg", config(1701, True))
    put(assay / "environment.cfg", environment([0] * 9))
    put(assay / "events.cfg", "u 0 Exit\n")
    for name, text in inputs.items():
        put(assay / (name + ".org"), text)
    lines = [f"LOAD_ORGANISM {n}.org" for n in inputs]
    lines += ["RECALCULATE 0 -1 0", f"DETAIL fixed.dat {FIELDS}", "TRACE traces/ 0 -1 0"]
    triple = [252908703, 856220990, 1432502763]
    for i in range(3):
        rotated = triple[i:] + triple[:i]
        lines += ["RECALCULATE 0 -1 0 " + " ".join(map(str, rotated)),
                  f"DETAIL rotation-{i}.dat {FIELDS}"]
    for i in range(32):
        lines += ["RECALCULATE 0 -1 1", f"DETAIL random-{i:02d}.dat {FIELDS}"]
    put(assay / "analyze.cfg", "\n".join(lines) + "\n")
    for label, values in [("graded", VALUES), ("equ", [0] * 8 + [5])]:
        baseline = root / ("A_baseline_" + label)
        baseline.mkdir()
        put(baseline / "avida.cfg", config(1701, True))
        put(baseline / "environment.cfg", environment(values))
        put(baseline / "events.cfg", "u 0 Exit\n")
        for name, text in inputs.items():
            put(baseline / (name + ".org"), text)
        put(baseline / "analyze.cfg", "\n".join(
            [f"LOAD_ORGANISM {n}.org" for n in inputs]
            + ["RECALCULATE 0 -1 0", f"DETAIL fixed.dat {FIELDS}"]) + "\n")
    for name in ["A", "C"]:
        for schedule in ["fixed", "switch"]:
            for seed in [4101, 4102, 4103]:
                job = root / f"B_{name}_{schedule}_{seed}"
                job.mkdir()
                put(job / "avida.cfg", config(seed))
                put(job / "environment.cfg", environment(VALUES))
                put(job / "events.cfg", events(schedule))
                put(job / "founder.org", inputs[name])
                put(job / "analyze.cfg", "# Offline common assays use separate folders.\n")
    manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(root.rglob("*")) if p.is_file()}
    put(root / "input_manifest.json", json.dumps({"source_commit": PIN,
        "sha256": manifest}, indent=2) + "\n")
    print(root)

def execute(job, binary, analyze=False):
    log = job / ("assay.log" if analyze else "run.log")
    command = [str(binary), "-c", "avida.cfg"] + (["-a"] if analyze else [])
    with log.open("x", encoding="utf-8") as output:
        result = subprocess.run(command, cwd=job, stdout=output,
                                stderr=subprocess.STDOUT, check=False)
    if result.returncode:
        raise RuntimeError(f"Run failed: {job}; preserve {log}")
    return str(job)

def gate(root):
    files = [root / "A_assay" / "data" / "fixed.dat"]
    files += sorted((root / "A_assay" / "data").glob("rotation-*.dat"))
    files += sorted((root / "A_assay" / "data").glob("random-*.dat"))
    if len(files) != 36:
        raise RuntimeError("Expected fixed, three rotation, and 32 random outputs")
    files += [root / ("A_baseline_" + label) / "data" / "fixed.dat"
              for label in ["graded", "equ"]]
    for file in files:
        rows = {}
        for line in file.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            cells = line.split()
            name = cells[0].removesuffix(".org")
            rows[name] = [float(x) for x in cells[1:17]]
        if set(rows) != {"A", "C", "A_probe", "C_probe"}:
            raise RuntimeError(f"Unexpected assay rows: {file}")
        for name, values in rows.items():
            expected = [0] * 9
            if name in ("A", "C"):
                expected[0] = 1
            elif name == "A_probe":
                expected[1] = 1
            if values[0] != 1 or values[1] != 100 or [int(x > 0) for x in values[7:]] != expected:
                raise RuntimeError(f"Frozen prediction failed: {file}, {name}")
        if rows["A"][:7] != rows["C"][:7]:
            raise RuntimeError(f"Unmatched baseline: {file}")

def parallel(jobs, binary, analyze=False):
    with cf.ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(execute, job, binary, analyze) for job in jobs]
        errors = []
        for future in cf.as_completed(futures):
            try:
                print(future.result())
            except Exception as error:
                errors.append(str(error))
        if errors:
            raise RuntimeError("\n".join(errors))

def snapshots(root, binary):
    jobs = []
    for run in sorted(root.glob("B_*")):
        for update in SNAPSHOTS:
            src = run / "data" / f"detail-{update}.spop"
            if not src.is_file():
                raise RuntimeError(f"Missing snapshot: {src}")
            job = root / "common_assays" / run.name / str(update)
            job.mkdir(parents=True, exist_ok=False)
            shutil.copyfile(src, job / "population.spop")
            put(job / "avida.cfg", config(1701, True))
            put(job / "environment.cfg", environment([0] * 9))
            put(job / "events.cfg", "u 0 Exit\n")
            fields = "id num_cpus viable length merit gest_time fitness " + " ".join(
                f"task.{i}:binary" for i in range(9)) + " sequence"
            put(job / "analyze.cfg", "LOAD population.spop\nFILTER num_cpus > 0\n"
                "RECALCULATE 0 -1 0\nDETAIL common.dat " + fields + "\n")
            jobs.append(job)
    parallel(jobs, binary, True)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        make(Path(sys.argv[1]).resolve())
    elif len(sys.argv) == 4:
        phase, directory, executable = sys.argv[1:]
        root, binary = Path(directory).resolve(), Path(executable).resolve()
        if phase == "--assay":
            execute(root / "A_assay", binary, True)
            execute(root / "A_baseline_graded", binary, True)
            execute(root / "A_baseline_equ", binary, True)
            gate(root)
        elif phase == "--run":
            gate(root)
            parallel(sorted(root.glob("B_*")), binary)
        elif phase == "--snapshots":
            snapshots(root, binary)
        else:
            raise SystemExit("Unknown phase")
    else:
        raise SystemExit("make_runs.py OUTPUT | --assay/--run/--snapshots OUTPUT AVIDA")
```

Use a new output directory and the absolute path of the already built pinned executable. These commands are phases to run in order; the population phase is the unrun experiment specified for Claude.

```bash
python3 make_runs.py brief04_runs
python3 make_runs.py --assay brief04_runs /absolute/path/to/avida
python3 make_runs.py --run brief04_runs /absolute/path/to/avida
python3 make_runs.py --snapshots brief04_runs /absolute/path/to/avida
```

The only path to supply is the actual local Avida executable; it is not guessed here. Each phase preserves logs; rerunning into an existing log fails rather than overwriting it. A failed gate preserves the first result and stops the population phase. If a population run fails, preserve it and report its reason; the script does not replace it with another seed. Missing snapshots stop the common-assay phase, including when a run went extinct before the planned endpoint.

For each `common.dat`, let `n` be `num_cpus`, `v` the viability indicator, and `t` the binary task indicator. Report `sum(n*v*t)/sum(n)` and, separately, `sum(n*v*t)/sum(n*v)` where the second denominator is nonzero. Also report `sum(n*v)/sum(n)`. Counts are weights within a run, not independent replications. For the live logs, divide each task count by the living-program count at that update. `totals.dat` records cumulative program births under the source's birth counter; subtract its update-zero value to exclude initialization and retain executed-instruction totals separately. Do not approximate cumulative births by summing the 100-update samples in `count.dat`.

**Checked local execution receipt.** The exact generator above produced the neutral/graded/EQU-only assays and its prediction gate exited with code zero. Separate event checks copied its A/4101 fixed and switch runs, changing only observation/snapshot intervals to ten updates and switch/end times to 20, 40 and 60. They exited with code zero in 8.600 and 4.835 seconds respectively, each producing seven snapshots and initially occupying all 3,600 cells. Task, count, average, time and totals data matched through update 20. These shortened checks test file execution and preparation, not the 60,000-update forecasts. An additional stock snapshot load/filter/common-assay check also exited with code zero. The twelve full population runs remain **unrun**.

The first neutral fixed-input data rows are preserved verbatim below; columns are `name viable length merit gest_time fitness copy_length exe_length`, the nine task counts in the fixed order, encoded instruction sequence, and the three inputs.

```text
A.org 1 100 97 382 0.253927 100 97 1 0 0 0 0 0 0 0 0 wzcagcccccccccccccccybycuaobpcubybccccccccccccccccccccccccccccccccccccccccccccccccccccccccczvfcaxgab 252908703 856220990 1432502763 
C.org 1 100 97 382 0.253927 100 97 1 0 0 0 0 0 0 0 0 wzcagcccccccccccccccybycucobpcubybccccccccccccccccccccccccccccccccccccccccccccccccccccccccczvfcaxgab 252908703 856220990 1432502763 
A_probe.org 1 100 97 382 0.253927 100 97 0 1 0 0 0 0 0 0 0 wzcagcccccccccccccccybycuaobpcubyaccccccccccccccccccccccccccccccccccccccccccccccccccccccccczvfcaxgab 252908703 856220990 1432502763 
C_probe.org 1 100 97 382 0.253927 100 97 0 0 0 0 0 0 0 0 0 wzcagcccccccccccccccybycucobpcubyaccccccccccccccccccccccccccccccccccccccccccccccccccccccccczvfcaxgab 252908703 856220990 1432502763 
```

The exact four instruction-file SHA-256 values and the generated neutral fixed-output hash are recorded for comparison. The complete generated input manifest accompanies any run directory.

```json
{
  "A.org": "2e7b75f84651c3dd0230e6d7e3c67314db2ec9b6ab76c0520a7404dbefadfa16",
  "C.org": "0c3ccb93c6cbd4e3b802f5a6e9fee2ef96baa471864da5c342b549363affdb3d",
  "A_probe.org": "fadc72eb5486fa0bfa6ddc247f208e2c6b32b64ac83a2270cb50315b991b2ef4",
  "C_probe.org": "7242f41a001a8f170c98a20f41c513d003bdb0e1efeceedf471b03fd29ba392a",
  "data/fixed.dat": "5e8fac0e01a70823f92f917fd4e7914d1e7df2ff0331efdb88002f52e5a6ed81"
}
```



END OF REPORT
