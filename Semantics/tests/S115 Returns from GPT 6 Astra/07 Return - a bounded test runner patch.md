## 1. Summary for the owner.

The patch adds `RUN_BOUNDED`, which runs each loaded Avida program separately on each supplied input triple and records every output, including initial zeros and repeated values. Each trial starts with fresh CPU state, has zero instruction-change probabilities, pauses task rewards, and stops at division, death, or the specified instruction budget. For example, eight `IO` operations on inputs `5, 12, -3` produce `0, 5, 12, -3, 5, 12, -3, 5`.

**Checked by execution:** the patch compiled, and the supplied examples matched their hand-worked expectations. The default ancestor divided at instruction 389. This command supports the project's standard 26-instruction heads set; it rejects incompatible execution settings. It supplies measurements for later experiments. It does not determine whether a program creates new knowledge.

## 2. Why `RECALCULATE` is or is not enough.

**Checked against the pinned source:** `RECALCULATE 0 -1 0 x y z` supplies manual inputs to the current batch. `RECALC use_manual_inputs x y z` is another existing entry point. These commands recompute task and replication summaries through `cCPUTestInfo` and `cTestCPU`. They do not emit the complete ordered output stream or its read count. Their execution allowance comes from `TEST_CPU_TIME_MOD × sequence length`, rather than an arbitrary per-command instruction budget, and the test can follow replicated programs across generations.

**Checked:** setting the first `RECALCULATE` argument to zero does not disable reactions. At this commit, zero selects `RES_INITIAL`. Manual inputs do not remove task rewards. The program's output buffer is a rolling buffer, so reading it only after execution loses earlier outputs. Existing `TRACE` can expose intermediate CPU state, but collecting and interpreting that trace would be a separate implementation.

The requested command therefore needs a patch. It does not replace `RECALCULATE`'s replication and task measurements.

Source locations, **checked** in the downloaded checkout: [cAnalyze.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/analyze/cAnalyze.cc), [cCPUTestInfo.h](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cCPUTestInfo.h), [cTestCPU.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cTestCPU.cc), and [tBuffer.h](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/tools/tBuffer.h).

## 3. The design.

```text
RUN_BOUNDED inputs.txt output.tsv instruction_budget
```

The budget is a nonnegative signed integer; zero executes nothing. Each nonblank input line contains exactly three signed 32-bit decimal integers. `#` starts a comment. Filenames must have no whitespace and are resolved from the process's working directory. The named output is replaced. Inputs and the batch's execution profile are checked before opening it.

The implementation reuses a fresh `cTestCPU` and `cCPUTestInfo(1)` per sequence/triple. **Checked:** the existing test path constructs fresh registers, stacks, heads, buffers, and program state; it copies the test information's mutation rates. Those rates are zero here, including copy, insertion, deletion, and division changes. The existing test interface handles successful division without inserting a replicated program into a population. Source: [cTestCPUInterface.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cTestCPUInterface.cc) and [cMutationRates.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cMutationRates.cc), **checked**.

All reactions are temporarily inactive, including reactions that execute extra instructions. Each original active/inactive setting is restored on normal completion or a C++ exception. Setting just numeric reward values to zero would leave other reaction effects available.

**Checked:** in the admitted heads execution model, one CPU step dispatches one instruction, with at most one `IO`. The patch captures that output immediately. The input buffer's cumulative addition count supplies the read count; the rotating input pointer would give the wrong count after wrapping. Guards reject other instruction sets, execution costs, failure probabilities, promoters, avatars, resource bins, energy mode, and implicit replication. They keep CPU-step counting and output sampling within their stated range. Source: [cHardwareCPU.cc](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cHardwareCPU.cc), **checked**.

Tab-separated columns:

| Column | Meaning |
| --- | --- |
| `sequence_index` | Zero-based position in the loaded batch. |
| `sequence_id` | Existing Avida sequence identifier; it may be nonunique or unset. |
| `triple_index` | Zero-based nonblank input-row position. |
| `x`, `y`, `z` | Supplied signed integers, in input order. |
| `reads` | Number of ordinary `IO` input reads. |
| `instructions` | Dispatched instructions, including unsuccessful attempts; consumed nop modifiers and skipped instructions do not get separate counts. |
| `divided` | `1` after a successful division, not merely an attempted `h-divide`. |
| `hit_budget` | `1` when `instructions == budget`; it can coincide with division or death. For budget zero it is `1`. |
| `outputs` | Every signed output in order, comma-separated; `-` means none. |

Rows follow batch order, then input-file order. There is no deduplication or replication by population abundance. Loaded sequence records are not recalculated or changed. An early death can yield both flags zero; the current lifespan and division-validity settings still apply.

## 4. The diff.

Against **checked** commit `47f13dadb547fcf10f620ace60247f38b30b8b16`. Save this block verbatim as `bounded-runner.patch`. It changes five existing files and adds no source file. **Checked:** applying it to fresh copies from that commit reproduced the compiled source files.

```diff
diff --git a/avida-core/source/analyze/cAnalyze.cc b/avida-core/source/analyze/cAnalyze.cc
index bdf4bbe..8963501 100644
--- a/avida-core/source/analyze/cAnalyze.cc
+++ b/avida-core/source/analyze/cAnalyze.cc
@@ -59,6 +59,7 @@
 #include "cPhenPlastGenotype.h"
 #include "cPlasticPhenotype.h"
 #include "cReaction.h"
+#include "cReactionLib.h" // Temporarily disable and restore all task reactions.
 #include "cReactionProcess.h"
 #include "cResource.h"
 #include "cResourceHistory.h"
@@ -79,6 +80,7 @@
 #include <string>
 #include <queue>
 #include <stack>
+#include <stdexcept>
 #include <stdlib.h>
 
 #include <cerrno>
@@ -10258,6 +10260,120 @@ void cAnalyze::BatchDuplicate(cString cur_string)
   batch[batch_to].SetAligned(false);
 }
 
+// Disabling reactions also disables nonnumeric rewards and bonus instructions.
+namespace {
+  class BoundedReactionPause {
+    cReactionLib& lib;
+    std::vector<bool> active;
+  public:
+    explicit BoundedReactionPause(cReactionLib& reactions)
+      : lib(reactions), active(reactions.GetSize()) {
+      for (int i = 0; i < lib.GetSize(); ++i) {
+        active[i] = lib.GetReaction(i)->GetActive();
+        lib.GetReaction(i)->SetActive(false);
+      }
+    }
+    ~BoundedReactionPause() {
+      for (int i = 0; i < lib.GetSize(); ++i) lib.GetReaction(i)->SetActive(active[i]);
+    }
+  };
+}
+
+void cAnalyze::CommandRunBounded(cString cur_string)
+{
+  try {
+    // Parse completely before opening the output, including integer overflow.
+    std::istringstream args((const char*)cur_string);
+    std::string input_name, output_name, extra;
+    int budget;
+    if (!(args >> input_name >> output_name >> budget) || (args >> extra) || budget < 0)
+      throw std::runtime_error("usage: RUN_BOUNDED inputs.txt output.tsv nonnegative_budget");
+    std::ifstream input(input_name.c_str());
+    if (!input) throw std::runtime_error("cannot open input file");
+    std::vector< Apto::Array<int> > triples;
+    std::string line;
+    while (std::getline(input, line)) {
+      line = line.substr(0, line.find('#'));
+      std::istringstream row(line);
+      row >> std::ws;
+      if (row.eof()) continue;
+      Apto::Array<int> values(3);
+      if (!(row >> values[0] >> values[1] >> values[2]) || (row >> extra))
+        throw std::runtime_error("each input row must contain exactly three signed integers");
+      triples.push_back(values);
+    }
+    if (input.bad() || triples.empty()) throw std::runtime_error("empty or unreadable input file");
+
+    // These guards make one CPU step one dispatched instruction and at most one IO.
+    const cAvidaConfig& cfg = m_world->GetConfig();
+    if (sizeof(int) != 4 || cfg.PROMOTERS_ENABLED.Get() || cfg.CONSTITUTIVE_REGULATION.Get() ||
+        cfg.USE_AVATARS.Get() || cfg.ENERGY_ENABLED.Get() || cfg.USE_RESOURCE_BINS.Get() ||
+        cfg.IMPLICIT_REPRO_BONUS.Get() || cfg.IMPLICIT_REPRO_CPU_CYCLES.Get() ||
+        cfg.IMPLICIT_REPRO_TIME.Get() || cfg.IMPLICIT_REPRO_END.Get() || cfg.IMPLICIT_REPRO_ENERGY.Get())
+      throw std::runtime_error("RUN_BOUNDED requires the ordinary heads execution model");
+    const char* names[] = {"nop-A", "nop-B", "nop-C", "if-n-equ", "if-less", "if-label",
+      "mov-head", "jmp-head", "get-head", "set-flow", "shift-r", "shift-l", "inc", "dec",
+      "push", "pop", "swap-stk", "swap", "add", "sub", "nand", "h-copy", "h-alloc",
+      "h-divide", "IO", "h-search"};
+    tListIterator<cAnalyzeGenotype> check(batch[cur_batch].List());
+    cAnalyzeGenotype* genotype;
+    while ((genotype = check.Next()) != NULL) {
+      const Genome& genome = genotype->GetGenome();
+      const cInstSet& is = m_world->GetHardwareManager().GetInstSet(genome.Properties().Get("instset").StringValue());
+      if (genome.HardwareType() != 0 || is.GetHardwareType() != 0 || is.GetSize() != 26 ||
+          is.HasCosts() || is.HasFTCosts() || is.HasEnergyCosts() || is.HasResCosts() ||
+          is.HasFemResCosts() || is.HasFemaleCosts() || is.HasChoosyFemaleCosts() ||
+          is.HasPostCosts() || is.HasBonusCosts())
+        throw std::runtime_error("RUN_BOUNDED requires the unmodified, unit-cost 26-instruction heads set");
+      for (int i = 0; i < 26; ++i)
+        if (is.GetName(i) != names[i] || is.GetProbFail(Instruction(i)) != 0.0 ||
+            is.GetAddlTimeCost(Instruction(i)) != 0)
+          throw std::runtime_error("RUN_BOUNDED found an altered instruction set");
+      ConstInstructionSequencePtr seq;
+      seq.DynamicCastFrom(genome.Representation());
+      if (!seq || seq->GetSize() == 0) throw std::runtime_error("empty instruction sequence");
+      for (int i = 0; i < seq->GetSize(); ++i)
+        if ((*seq)[i].GetOp() >= 26) throw std::runtime_error("instruction outside the heads set");
+    }
+
+    std::ofstream out(output_name.c_str());
+    if (!out) throw std::runtime_error("cannot open output file");
+    out << "# sequence_index\tsequence_id\ttriple_index\tx\ty\tz\treads\tinstructions\tdivided\thit_budget\toutputs\n";
+    BoundedReactionPause pause(m_world->GetEnvironment().GetReactionLib());
+    tListIterator<cAnalyzeGenotype> entries(batch[cur_batch].List());
+    int sequence_index = 0;
+    while ((genotype = entries.Next()) != NULL) {
+      for (size_t t = 0; t < triples.size(); ++t) {
+        // New settings and test CPU isolate each sequence/triple and suppress all mutations.
+        cCPUTestInfo info(1);
+        info.UseManualInputs(triples[t]);
+        info.MutationRates().Clear();
+        info.GetBoundedRun().budget = budget;
+        cTestCPU cpu(m_ctx, m_world);
+        cpu.TestGenome(m_ctx, info, genotype->GetGenome());
+        const cCPUTestInfo::BoundedRun& run = info.GetBoundedRun();
+        const bool divided = info.GetTestPhenotype().GetNumDivides() != 0;
+        out << sequence_index << '\t' << genotype->GetID() << '\t' << t;
+        for (int k = 0; k < 3; ++k) out << '\t' << triples[t][k];
+        out << '\t' << run.reads << '\t' << run.instructions << '\t' << divided
+            << '\t' << (run.instructions == budget) << '\t';
+        if (run.outputs.empty()) out << '-';
+        for (size_t k = 0; k < run.outputs.size(); ++k) {
+          if (k) out << ',';
+          out << run.outputs[k];
+        }
+        out << '\n';
+      }
+      ++sequence_index;
+    }
+    out.close();
+    if (!out) throw std::runtime_error("output write failed");
+  } catch (const std::exception& error) {
+    cerr << "error: RUN_BOUNDED: " << error.what() << endl;
+    if (exit_on_error) exit(1);
+  }
+}
+
 void cAnalyze::BatchRecalculate(cString cur_string)
 {
   Apto::Array<int> manual_inputs;  // Used only if manual inputs are specified
@@ -11310,6 +11426,7 @@ void cAnalyze::SetupCommandDefLibrary()
   AddLibraryDef("PURGE_BATCH", &cAnalyze::BatchPurge);
   AddLibraryDef("DUPLICATE", &cAnalyze::BatchDuplicate);
   AddLibraryDef("RECALCULATE", &cAnalyze::BatchRecalculate);
+  AddLibraryDef("RUN_BOUNDED", &cAnalyze::CommandRunBounded); // inputs, output, instruction budget
   AddLibraryDef("RECALC", &cAnalyze::BatchRecalculateWithArgs);
   AddLibraryDef("RENAME", &cAnalyze::BatchRename);
   AddLibraryDef("CLOSE_FILE", &cAnalyze::CloseFile);
@@ -11410,4 +11527,3 @@ void cAnalyze::RunInteractive()
   
   if (!saved_analyze) m_ctx.ClearAnalyzeMode();
 }
-
diff --git a/avida-core/source/analyze/cAnalyze.h b/avida-core/source/analyze/cAnalyze.h
index 3a04c87..9e982a3 100644
--- a/avida-core/source/analyze/cAnalyze.h
+++ b/avida-core/source/analyze/cAnalyze.h
@@ -324,6 +324,7 @@ private:
   void BatchPurge(cString cur_string);
   void BatchDuplicate(cString cur_string);
   void BatchRecalculate(cString cur_string);
+  void CommandRunBounded(cString cur_string); // Capture reward-free, bounded IO trials.
   void BatchRecalculateWithArgs(cString cur_string);
   void BatchRename(cString cur_string);
   void CloseFile(cString cur_string);
diff --git a/avida-core/source/cpu/cCPUTestInfo.cc b/avida-core/source/cpu/cCPUTestInfo.cc
index 64e648a..bbedbb7 100644
--- a/avida-core/source/cpu/cCPUTestInfo.cc
+++ b/avida-core/source/cpu/cCPUTestInfo.cc
@@ -57,6 +57,7 @@ cCPUTestInfo::cCPUTestInfo(const cCPUTestInfo& test_info)
 
 cCPUTestInfo& cCPUTestInfo::operator=(const cCPUTestInfo& test_info)
 {
+  m_bounded = test_info.m_bounded; // Preserve the optional capture when copying settings.
   generation_tests = test_info.generation_tests;
   trace_task_order = test_info.trace_task_order;
   use_random_inputs = test_info.use_random_inputs;
@@ -90,6 +91,9 @@ cCPUTestInfo::~cCPUTestInfo()
 
 void cCPUTestInfo::Clear()
 {
+  // Clear observations without discarding the requested instruction budget.
+  m_bounded.instructions = m_bounded.reads = 0;
+  m_bounded.outputs.clear();
   is_viable = false;
   max_depth = -1;
   depth_found = -1;
diff --git a/avida-core/source/cpu/cCPUTestInfo.h b/avida-core/source/cpu/cCPUTestInfo.h
index 2cbf9b6..0b9dcea 100644
--- a/avida-core/source/cpu/cCPUTestInfo.h
+++ b/avida-core/source/cpu/cCPUTestInfo.h
@@ -28,6 +28,7 @@
 #include "nHardware.h"
 #include "cHardwareTracer.h"
 #include "cMutationRates.h"
+#include <vector>
 
 class cOrganism;
 class cPhenotype;
@@ -46,7 +47,15 @@ enum eTestCPUResourceMethod { RES_INITIAL = 0, RES_CONSTANT, RES_UPDATED_DEPLETA
 class cCPUTestInfo
 {
   friend class cTestCPU;
+public:
+  // Optional, single-generation capture for the unit-cost heads instruction set.
+  struct BoundedRun {
+    int budget, instructions, reads;
+    std::vector<int> outputs;
+    BoundedRun() : budget(-1), instructions(0), reads(0) { }
+  };
 private:
+  BoundedRun m_bounded;
   // Inputs...
   int generation_tests; // Maximum depth in generations to test
   bool trace_task_order;      // Should we keep track of ordering of tasks?
@@ -94,6 +103,7 @@ public:
   
   void SetCurrentStateGridID(int sg) { m_cur_sg = sg; }
   cMutationRates& MutationRates() { return m_mut_rates; }
+  BoundedRun& GetBoundedRun() { return m_bounded; }
 
   // Input Accessors
   int GetGenerationTests() const { return generation_tests; }
diff --git a/avida-core/source/cpu/cTestCPU.cc b/avida-core/source/cpu/cTestCPU.cc
index 0c317e3..8f49e34 100644
--- a/avida-core/source/cpu/cTestCPU.cc
+++ b/avida-core/source/cpu/cTestCPU.cc
@@ -150,8 +150,10 @@ bool cTestCPU::ProcessGestation(cAvidaContext& ctx, cCPUTestInfo& test_info, int
   // Determine how long this organism should be tested for...
   ConstInstructionSequencePtr seq;
   seq.DynamicCastFrom(organism.UnitGenome().Representation());
-  int time_allocated = m_world->GetConfig().TEST_CPU_TIME_MOD.Get() * seq->GetSize();
-  time_allocated += m_res_cpu_cycle_offset; // If the resource offset has us starting at a different time, adjust @JEB
+  // Bounded runs use an absolute limit, independent of sequence length.
+  cCPUTestInfo::BoundedRun& run = test_info.GetBoundedRun();
+  int time_allocated = (run.budget >= 0) ? run.budget :
+    m_world->GetConfig().TEST_CPU_TIME_MOD.Get() * seq->GetSize() + m_res_cpu_cycle_offset;
 
   // Prepare the inputs...
   cur_input = 0;
@@ -163,6 +165,7 @@ bool cTestCPU::ProcessGestation(cAvidaContext& ctx, cCPUTestInfo& test_info, int
 	
   // This way of keeping track of time is only used to update resources...
   int time_used = m_res_cpu_cycle_offset; // Note: the offset is zero by default if no resources being used @JEB
+  if (run.budget >= 0) time_used = 0;
   
   organism.GetHardware().SetTrace(test_info.GetTracer());
   while (time_used < time_allocated && organism.GetPhenotype().GetNumDivides() == 0 && !organism.IsDead())
@@ -174,7 +177,15 @@ bool cTestCPU::ProcessGestation(cAvidaContext& ctx, cCPUTestInfo& test_info, int
     // Resources will be updated as if each update takes a number of cpu cycles equal to the average time slice
     UpdateResources(ctx, time_used);
     
+    // Capture each IO before the rolling buffer can overwrite its value.
+    const int outputs_before = (run.budget >= 0) ? organism.GetOutputBuf().GetTotal() : 0;
     organism.GetHardware().SingleProcess(ctx);
+    if (run.budget >= 0) {
+      ++run.instructions;
+      run.reads = organism.GetInputBuf().GetTotal();
+      if (organism.GetOutputBuf().GetTotal() > outputs_before)
+        run.outputs.push_back(organism.GetOutputBuf()[0]);
+    }
   }
   
   organism.GetHardware().SetTrace(HardwareTracerPtr(NULL));
@@ -433,4 +444,3 @@ void cTestCPU::ResetInputs(cAvidaContext& ctx)
 	if (!m_use_manual_inputs)
 		m_world->GetEnvironment().SetupInputs(ctx, input_array, m_use_random_inputs);
 }
-
```

## 5. Build instructions.

**Checked by execution:** built with CMake 3.31.10, GNU C++ 13.3.0, C++11, and the repository's pinned submodules. `avida-core/CMakeLists.txt` needs no change. From the repository root:

```bash
git checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git submodule update --init libs/apto
git apply --check bounded-runner.patch
git apply bounded-runner.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S . -B build-bounded \
  -DAVD_CMDLINE=ON -DAVD_GUI_NCURSES=OFF -DAVD_UNIT_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=11
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-bounded --target avida -j 1
mkdir -p bounded-test
cp avida-core/support/config/{avida.cfg,instset-heads.cfg,default-heads.org,environment.cfg,events.cfg} bounded-test/
```

Put the files from section 6 in `bounded-test`, then run:

```bash
cd bounded-test
../build-bounded/bin/avida -a -c avida.cfg \
  -set RANDOM_SEED 1 -set ANALYZE_FILE analyze.cfg
```

`AVIDA_DISABLE_BACKTRACE=1` selects the repository's existing optional-backtrace exclusion. **Checked:** the first parallel build stopped with assembler errors in upstream files; a serial build completed. There were deprecation warnings from upstream code. The patch needed no compiler-error repair.

## 6. The test.

Save `inputs.txt`:

```text
5 12 -3
0 -1 7
```

Save `echo.org`:

```text
#inst_set heads_default
#hw_type 0
IO
IO
IO
IO
IO
IO
IO
IO
IO
IO
```

Save `nand.org`:

```text
#inst_set heads_default
#hw_type 0
IO
IO
nop-C
nand
IO
IO
nop-C
nand
IO
IO
nop-C
```

Save `analyze.cfg`:

```text
PURGE_BATCH
LOAD_ORGANISM default-heads.org
LOAD_ORGANISM echo.org
LOAD_ORGANISM nand.org
RENAME 0
RUN_BOUNDED inputs.txt main.tsv 8
PURGE_BATCH
LOAD_ORGANISM default-heads.org
RENAME 0
RUN_BOUNDED inputs.txt before_division.tsv 388
RUN_BOUNDED inputs.txt at_division.tsv 389
RUN_BOUNDED inputs.txt after_division.tsv 390
```

`RENAME 0` assigns predictable identifiers for these tests only. For research batches, omit it to retain their identifiers.

Expected `main.tsv`, including its header and literal tab separators:

```text
# sequence_index	sequence_id	triple_index	x	y	z	reads	instructions	divided	hit_budget	outputs
0	0	0	5	12	-3	0	8	0	1	-
0	0	1	0	-1	7	0	8	0	1	-
1	1	0	5	12	-3	8	8	0	1	0,5,12,-3,5,12,-3,5
1	1	1	0	-1	7	8	8	0	1	0,0,-1,7,0,-1,7,0
2	2	0	5	12	-3	6	8	0	1	0,0,-5,12,-6,5
2	2	1	0	-1	7	6	8	0	1	0,0,-1,-1,-1,0
```

**Worked out from checked instruction semantics, before execution:** `IO` outputs its selected register before replacing it with the next input. Registers begin at zero. Unmodified `IO` uses BX; the immediately following `nop-C` selects CX and is consumed as a modifier. `nand` writes `~(BX & CX)` into BX. The eight dispatched instructions of `nand.org` are therefore:

| Dispatch | Operation | First triple's output |
| --- | --- | --- |
| 1 | IO through BX; read 5 | 0 |
| 2 | IO through CX; read 12 | 0 |
| 3 | BX becomes `~(5 & 12) = -5` | None |
| 4 | IO through BX; read -3 | -5 |
| 5 | IO through CX; read 5 | 12 |
| 6 | BX becomes `~(-3 & 5) = -6` | None |
| 7 | IO through BX; read 12 | -6 |
| 8 | IO through CX; read -3 | 5 |

For the second triple, the NAND results are `~(0 & -1) = -1` and `~(7 & 0) = -1`. The echo sequence repeatedly outputs its previous input, starting with zero. The ancestor executes no `IO`.

**Worked out from the checked default ancestor:** its first division takes 3 setup dispatches, 85 padding nop dispatches, one loop-marker search, 99 three-dispatch copy-loop iterations, and a final copy/check/divide: `3 + 85 + 1 + 99×3 + 3 = 389`. Modifiers and skipped division attempts are not separately dispatched. Source: [default-heads.org](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/support/config/default-heads.org), **checked**.

The three division files use the same header as `main.tsv`. Expected data lines for `before_division.tsv`:

```text
0	0	0	5	12	-3	0	388	0	1	-
0	0	1	0	-1	7	0	388	0	1	-
```

For `at_division.tsv`:

```text
0	0	0	5	12	-3	0	389	1	1	-
0	0	1	0	-1	7	0	389	1	1	-
```

For `after_division.tsv`:

```text
0	0	0	5	12	-3	0	389	1	0	-
0	0	1	0	-1	7	0	389	1	0	-
```

**Checked by execution:** all these lines matched. Additional executed checks covered budgets 0, 7, and 9; reordered/repeated triples; both signed 32-bit endpoints; malformed rows and budgets; a two-cycle `IO` rejected before output creation; and death at instruction 200 for the ten-instruction echo sequence with budget 201. Setting seven world mutation probabilities to 1 left both the main rows and ancestor division rows unchanged.

An additional reaction test used this environment:

```text
REACTION active dontcare process:value=3:type=pow:inst=swap requisite:max_count=2
REACTION paused dontcare process:value=9:type=pow:inst=inc requisite:max_count=1
SET_ACTIVE REACTION paused 0
```

Run `TRACE before/ 0 -1 0 5 12 -3`, the bounded command, and `TRACE after/ 0 -1 0 5 12 -3` on the two hand-written sequences. **Checked by execution:** bounded outputs remained as above. Ordinary execution with the active reaction changed the NAND sequence's third output from -5 to -1. Ordinary traces before and after the command matched byte for byte, including bonus 64; the originally inactive reaction stayed inactive. This distinguishes disabling whole reactions from merely ignoring reward numbers.

## 7. Assumptions and what you are unsure of.

**Compilation status: compiled and executed here.** These are tests of this runner, using the default ancestor and cases constructed here. The owner's saved populations were unavailable, and the research measurements supplied in the brief were not independently checked. No conclusion about knowledge creation follows from the runner tests.

The scope is the stated standard heads instruction set at this commit. It is not a general runner for every Avida hardware model. Extending that scope would require counting at instruction dispatch and capturing at output emission, with separate tests for threads, delays, and extra instructions. Allocation, lifespan, division eligibility, and the existing virtual-machine arithmetic remain inherited settings. “No instruction changes” means zero mutation probabilities; copying and other instruction-defined memory operations retain their ordinary meanings. Reaction pausing assumes this command is not concurrent with other work on the same `cWorld`. Memory for outputs grows with the supplied budget.

The hard-to-vary question was frozen as: **does this design deliver independent, reward-free, bounded IO trials for the project's heads programs?** The requested observations and isolation constraints were **given** jobs; the pinned commit was **fixed**. Rejection of malformed inputs was an **added** job. Restoring reaction settings was tested as a consequence of making a temporary change.

| Part | Status and what holds it | Scope | Dependency | Provenance |
| --- | --- | --- | --- | --- |
| Fresh test objects and zero mutation rates | Held by isolation; repeat and mutation-setting changes preserved results. Explicit clearing duplicates the constructor's zero defaults and is idle as additional protection here. | In test | Upstream test construction and mutation copying, checked in source | Built |
| Absolute instruction limit | Held jointly with the execution-profile guards by the 0/8 and 388/389/390 boundaries. | In test | Heads dispatch semantics, checked in source and examples | Built |
| Immediate output capture and cumulative reads | Held by eight-output cases, repeated zeros, and rotation beyond three reads. Keeping only the final buffer fails this job. | In test | Ordinary IO and buffer semantics, checked | Built |
| Reaction pause and restoration | Held by the bonus-instruction contrast and unchanged before/after traces. | In test | Upstream reaction activation, checked | Built |
| Profile guards | Held jointly with step counting within the declared scope; the delayed-IO neighbor was rejected. The exact validation arrangement can change. | In test | Admitted instruction meanings, checked | Built |
| Strict input parsing | Held if rejecting malformed input is accepted as a requirement; valid negative endpoints remain accepted. | In test | Integer-stream extraction | Built |
| Command name and TSV conventions | Loose, harmless choices; another unambiguous format could serve the same jobs. | In test | None named | Built |

Whole-design checks:

- **Remove/swap — result:** final-buffer-only capture loses outputs; the rotating pointer loses cumulative reads. Reimplementing the virtual CPU and adding output hooks were unnecessary within the admitted profile. The explicit mutation-clear call is redundant but documents intent.
- **Flip — result:** a nonzero fresh-register output or a division count of 388 would contradict the frozen predictions; neither can be rescued without changing an input, rule, or implementation.
- **Reverse — result, source reasoning:** trial execution precedes serialization. Changing a printed identifier cannot change an already completed computation.
- **Answer hidden in premises — result:** expected values came from instruction semantics and arithmetic, not observed runner outputs. Shared reliance on Avida's implementation remains a dependency.
- **Jobs and added job — result:** the brief supplied the core jobs. Reaction restoration survived a separate trace comparison and rules out a permanent global disable.
- **Look inside and rivals — result:** source inspection plus the active bonus-instruction trace distinguishes whole-reaction suppression from zero-valued numeric rewards. Long output cases distinguish complete capture from a retained tail.
- **Pull — result:** small step-based capture conflicts with unrestricted hardware support. The guards expose that boundary instead of silently miscounting. Arbitrary hardware support is not assessed.
- **Check patches — result:** one arithmetic expectation was corrected before execution. Adversarial test preparation needed path/syntax corrections and a corrected instruction-set include. The runner needed no behavioral repair after its first executed case. Error paths are explicit; there is no fallback that silently accepts unsupported models.
- **Change list and provenance — result:** budgets, input values/order, mutation settings, reaction effects, malformed files, instruction costs, and early death were varied. Design parts were built here. Production populations and every configuration combination remain untested.

These checks identify what constrains this design; they do not certify all possible programs. **One next step:** run the supplied script on Claude's build, then try a small saved batch under the same admitted execution profile and inspect its raw output rows.

END OF REPORT
