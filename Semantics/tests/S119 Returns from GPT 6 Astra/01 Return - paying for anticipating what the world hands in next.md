# Avida next input anticipation patch and execution report

## Summary for the owner

The patch compiled, and its execution tests matched the expected results. It pays an Avida program when its output matches the number it will read next. For example, after receiving 7, a program can output 8 before the increasing stream supplies 8. A program merely repeating 7 receives no reward there.

The patch also supplies random numbers, repeated numbers, and a scheduled rule switch. Ordinary runs with the feature off matched stock across 400 updates, apart from date headers.

This does not yet show that evolutionary computation discovers anticipation. The successful programs were handwritten. Nor does it make the goal unnamed: “say the next number” remains a rule chosen by the designer. The report supplies the patch, reproducible tests, and a conditional experiment option; no costly experiment was launched.

## Where in the source

**Checked:** source was read from [devosoft/avida at 47f13dad](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16). All source descriptions below marked **checked** refer to that local checkout, not recollection. Paths below are relative to `avida-core/source`; line numbers are before the patch.

| Location | Short exact quotation | What was checked |
|---|---|---|
| `cpu/cHardwareCPU.cc`, `Inst_TaskIO`, 4188–4200 | `m_organism->DoOutput(ctx, value_out);` | Output precedes `GetNextInput()` and `DoInput()`. |
| `main/cOrganism.h`, `GetNextInput`, 249–250 | `m_interface->GetInputAt(m_input_pointer)` | Sequential reads currently go to the interface. |
| `main/cOrganism.cc`, `DoInput` / `DoOutput`, 368–405 | `input_buffer.Add(value);` | Input recording and the three explicit-value output frontends are separate. |
| `main/cEnvironment.cc`, `SetupInputs`, 1252–1300 | `input_array.Resize(m_input_size);` | Prepares the stock input array. |
| `main/cEnvironment.cc`, `TestOutput`, 1314, 1376–1399 | `reaction_count[i]++;` | Task quality flows through ordinary reaction processing. The function starts at 1314, not 1337. |
| `main/cOrganism.cc`, `Divide_CheckViable`, 834, 862–879 | `if (single_reaction != 0)` | The replication gate counts performed reaction types. |
| `main/cPhenotype.cc`, `TestOutput`, 1645–1646 | `cur_bonus *= result.GetMultBonus();` | Reaction payments alter the merit bonus. |
| `cpu/cTestCPU.cc`, `TestGenome_Body`, 236–282 | `organism->SetOrgInterface` | Test execution creates a normal `cOrganism`. |

**Checked:** `cTaskLib::AddTask` at `main/cTaskLib.cc:73` supplies the registration point. `Inst_Inc` at `cpu/cHardwareCPU.cc:2864–2868` increments the selected register. The patch changes five existing files; neither CPU instructions nor `SetupInputs` needs changing.

## The design

The fixed question is whether this execution environment supplies private sequences and pays a committed next-read match while preserving stock runs when disabled. Discovery through evolutionary computation is a separate, unrun question.

| Setting | Default | Meaning |
|---|---:|---|
| `ANTICIPATE_MODE` | −1 | −1 off; 0 R0; 1 R1; 2 R2; 3 R-switch. |
| `ANTICIPATE_SWITCH` | 25000 | First world update whose new transaction uses R2 in mode 3. |
| `ANTICIPATE_START` | −1 | Random initial value; 1–65536 fixes the first value for diagnostics only. |

R0 draws each value from 1–65536 using sixteen calls to the existing random generator's half-probability operation. R1 draws an initial value and repeats it. R2 draws an initial value and thereafter adds one. It stops with an explicit exception before exceeding `INT_MAX`; it never wraps. Therefore no R2 input can equal an earlier input received by that same program. R-switch uses R1 before the configured update, then R2. Fresh descendant programs receive fresh streams, including after the switch.

Each program owns its last read, pending next value, and attempt flag. The world generator prepares the pending value independently of the proposed output. The checker then compares only stored value and output; it does not evaluate a target function. The first read is warm-up and earns nothing. Thereafter only the first output before a read is eligible, whether it matches or fails. Reading consumes exactly that pending value and permits another attempt. Resetting input buffers or dividing does not rewind a surviving parent's stream. A pending value already committed by an output stays fixed across a switch; the following transaction uses the new rule. With the specified heads `IO`, output and read occur within one instruction.

Payment uses this environment file:

```text
REACTION ANT anticipate process:value=1:type=pow requisite:max_count=1
```

**Checked:** `cEnvironment.cc:1756–1758` makes `type=pow,value=1` multiply the bonus by $2^1=2$. Ordinary reaction accounting supplies `REQUIRE_SINGLE_REACTION`. Set `MERIT_INC_APPLY_IMMEDIATE 1` for immediate merit increases, or retain the stock timing. One reward per replication cycle prevents unbounded within-cycle multiplication. The proposed experiment uses `REQUIRE_SINGLE_REACTION 0`; gate behavior is tested separately. Use only this reaction, the supplied 26-instruction heads set, `SPECULATIVE 0`, and no avatars or parasites.

Hard-to-vary check: the owner's stream, payment, and disabled-behavior requirements are fixed; private pending state is held by the promised next read; one-attempt state is held by the repeated-guess attack. The particular constant/increment rules and reward magnitude are loose design choices. New-capability discovery remains unknown. Removing equality breaks the requested task; keeping equality does not justify the broader claim of unnamed goals.

## The diff

Complete unified diff against the pinned commit. It adds 71 and removes 2 nonblank, noncomment C++ lines, counting declarations and braces. Each logical change has a one-line comment. Test code is additional and excluded from this count.

<!-- artifact: work/anticipation.patch -->
```diff
diff --git a/avida-core/source/main/cAvidaConfig.h b/avida-core/source/main/cAvidaConfig.h
index 14c8b3e62..46ed525cf 100644
--- a/avida-core/source/main/cAvidaConfig.h
+++ b/avida-core/source/main/cAvidaConfig.h
@@ -304,6 +304,11 @@ public:
   CONFIG_ADD_VAR(MIGRATION_FILE, cString, "-", "NxN file that describes connectivity weights between demes");   
   
   
+  // Anticipation settings leave the stock input path selected by default.
+  CONFIG_ADD_VAR(ANTICIPATE_MODE, int, -1, "-1=off, 0=random, 1=repeat, 2=increment, 3=repeat then increment");
+  CONFIG_ADD_VAR(ANTICIPATE_SWITCH, int, 25000, "First update using increment in mode 3");
+  CONFIG_ADD_VAR(ANTICIPATE_START, int, -1, "-1=random initial value; 1..65536=diagnostic initial value");
+
   // -------- Mutation config options --------
   CONFIG_ADD_GROUP(MUTATION_GROUP, "Mutation rates");  
   CONFIG_ADD_VAR(COPY_MUT_PROB, double, 0.0075, "Substitution rate (per copy)");
diff --git a/avida-core/source/main/cOrganism.cc b/avida-core/source/main/cOrganism.cc
index 943176891..15350c192 100644
--- a/avida-core/source/main/cOrganism.cc
+++ b/avida-core/source/main/cOrganism.cc
@@ -41,6 +41,9 @@
 #include "cStats.h"
 #include "nHardware.h"
 
+// Numeric exhaustion is explicit: an incrementing stream never wraps into replay.
+#include <climits>
+#include <stdexcept>
 #include <algorithm>
 #include <iomanip>
 #include <iterator>
@@ -158,6 +161,10 @@ cOrganism::cOrganism(cWorld* world, cAvidaContext& ctx, const Genome& genome, in
   , m_queued_display_data(NULL)
   , m_display(false)
   , m_lyse_display(false)
+  // Initializing disabled stream state consumes no random numbers.
+  , m_anticipate_next(0), m_anticipate_last(0), m_anticipate_rule(-1)
+  , m_anticipate_ready(false), m_anticipate_read(false)
+  , m_anticipate_attempted(false), m_anticipate_match(false)
   , m_input_pointer(0)
   , m_input_buf(world->GetEnvironment().GetInputSize())
   , m_output_buf(world->GetEnvironment().GetOutputSize())
@@ -365,6 +372,56 @@ int cOrganism::ReceiveValue()
   return out_value;
 }
 
+// The world produces one pending value; a committed value stays fixed until read.
+void cOrganism::PrepareAnticipation(cAvidaContext& ctx)
+{
+  const cAvidaConfig& cfg = m_world->GetConfig();
+  int rule = cfg.ANTICIPATE_MODE.Get();
+  if (rule == -1) return;
+  if (rule < 0 || rule > 3 || cfg.ANTICIPATE_SWITCH.Get() < 0 ||
+      (cfg.ANTICIPATE_START.Get() != -1 &&
+       (cfg.ANTICIPATE_START.Get() < 1 || cfg.ANTICIPATE_START.Get() > 65536)))
+    throw std::invalid_argument("Invalid ANTICIPATE setting");
+  if (rule == 3) rule = m_world->GetStats().GetUpdate() >= cfg.ANTICIPATE_SWITCH.Get() ? 2 : 1;
+  if (m_anticipate_ready && (m_anticipate_rule == rule || m_anticipate_attempted)) return;
+  if (!m_anticipate_read || rule == 0) {
+    int value = 0;
+    if (!m_anticipate_read && cfg.ANTICIPATE_START.Get() != -1)
+      value = cfg.ANTICIPATE_START.Get() - 1;
+    else for (int bit = 0; bit < 16; ++bit) value = 2 * value + (ctx.GetRandom().P(0.5) ? 1 : 0);
+    m_anticipate_next = value + 1;
+  } else {
+    if (rule == 2 && m_anticipate_last == INT_MAX)
+      throw std::overflow_error("ANTICIPATE increment stream exhausted");
+    m_anticipate_next = m_anticipate_last + (rule == 2 ? 1 : 0);
+  }
+  m_anticipate_rule = rule;
+  m_anticipate_ready = true;
+}
+
+// Sequential reads consume the exact pending number, without rewinding on division.
+int cOrganism::GetNextInput(int& in_input_pointer)
+{
+  if (m_world->GetConfig().ANTICIPATE_MODE.Get() == -1)
+    return m_interface->GetInputAt(in_input_pointer);
+  PrepareAnticipation(m_world->GetDefaultContext());
+  m_anticipate_last = m_anticipate_next;
+  m_anticipate_read = true;
+  m_anticipate_ready = false;
+  m_anticipate_attempted = false;
+  return m_anticipate_last;
+}
+
+// Only the first output before a read is eligible; checking uses stored equality only.
+void cOrganism::BeginAnticipation(cAvidaContext& ctx, int value)
+{
+  m_anticipate_match = false;
+  if (m_world->GetConfig().ANTICIPATE_MODE.Get() == -1) return;
+  PrepareAnticipation(ctx);
+  m_anticipate_match = m_anticipate_read && !m_anticipate_attempted && value == m_anticipate_next;
+  m_anticipate_attempted = true;
+}
+
 void cOrganism::DoInput(const int value)
 {
   DoInput(m_input_buf, m_output_buf, value);
@@ -384,23 +441,29 @@ void cOrganism::DoOutput(cAvidaContext& ctx, const bool on_divide, cContextPheno
 
 void cOrganism::DoOutput(cAvidaContext& ctx, const int value)
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   m_output_buf.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, m_input_buf, m_output_buf, false, false);
   else doOutput(ctx, m_input_buf, m_output_buf, false, false);
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
 }
 
 void cOrganism::DoOutput(cAvidaContext& ctx, const int value, bool is_parasite, cContextPhenotype* context_phenotype) 
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   m_output_buf.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, m_input_buf, m_output_buf, false, (bool)is_parasite, context_phenotype); 
   else doOutput(ctx, m_input_buf, m_output_buf, false, (bool)is_parasite, context_phenotype); 
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
 }
 
 void cOrganism::DoOutput(cAvidaContext& ctx, tBuffer<int>& input_buffer, tBuffer<int>& output_buffer, const int value)
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   output_buffer.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, input_buffer, output_buffer, false, false);
   else doOutput(ctx, input_buffer, output_buffer, false, false);
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
 }
 
 
diff --git a/avida-core/source/main/cOrganism.h b/avida-core/source/main/cOrganism.h
index 63b7e42ea..9711e5699 100644
--- a/avida-core/source/main/cOrganism.h
+++ b/avida-core/source/main/cOrganism.h
@@ -86,6 +86,11 @@ private:
   Genome m_offspring_genome;              // Child genome, while under construction.
 
   // Input and Output with the environment
+  // Private pending input and one-attempt state belong to this Avida program.
+  int m_anticipate_next, m_anticipate_last, m_anticipate_rule;
+  bool m_anticipate_ready, m_anticipate_read, m_anticipate_attempted, m_anticipate_match;
+  void PrepareAnticipation(cAvidaContext& ctx);
+  void BeginAnticipation(cAvidaContext& ctx, int value);
   int m_input_pointer;
   tBuffer<int> m_input_buf;
   tBuffer<int> m_output_buf;
@@ -246,8 +251,10 @@ public:
   void Rotate(cAvidaContext& ctx, int direction) { m_interface->Rotate(ctx, direction); }
 
   int GetInputAt(int i) { return m_interface->GetInputAt(i); }
-  int GetNextInput() { return m_interface->GetInputAt(m_input_pointer); }
-  int GetNextInput(int& in_input_pointer) { return m_interface->GetInputAt(in_input_pointer); }
+  // Both sequential read entry points consume the same private stream when enabled.
+  int GetNextInput() { return GetNextInput(m_input_pointer); }
+  int GetNextInput(int& in_input_pointer);
+  bool AnticipationMatch() const { return m_anticipate_match; }
   tBuffer<int>& GetInputBuf() { return m_input_buf; }
   tBuffer<int>& GetOutputBuf() { return m_output_buf; }
   void Die(cAvidaContext& ctx) { m_interface->Die(ctx); m_is_dead = true; } 
diff --git a/avida-core/source/main/cTaskLib.cc b/avida-core/source/main/cTaskLib.cc
index afde3d256..c9eee6e17 100644
--- a/avida-core/source/main/cTaskLib.cc
+++ b/avida-core/source/main/cTaskLib.cc
@@ -84,6 +84,8 @@ cTaskEntry* cTaskLib::AddTask(const cString& name, const cString& info, cEnvReqs
   // The following if blocks are grouped based on class of task.  Chaining too
   // many if block causes problems block nesting depth in Visual Studio.net 2003.
   
+  // Register the stream match without naming or evaluating a generating rule.
+  if (name == "anticipate") NewTask(name, "Next input match", &cTaskLib::Task_Anticipate);
   if (name == "echo")      NewTask(name, "Echo", &cTaskLib::Task_Echo);
   else if (name == "echo_dup")  NewTask(name, "Echo_dup",  &cTaskLib::Task_Echo);
   else if (name == "add")  NewTask(name, "Add",  &cTaskLib::Task_Add);
@@ -448,6 +450,12 @@ void cTaskLib::SetupTests(cTaskContext& ctx) const
 }
 
 
+// Division-only checks cannot claim prediction credit.
+double cTaskLib::Task_Anticipate(cTaskContext& ctx) const
+{
+  return !ctx.GetOnDivide() && ctx.GetOrganism()->AnticipationMatch() ? 1.0 : 0.0;
+}
+
 double cTaskLib::Task_Echo(cTaskContext& ctx) const
 {
   const tBuffer<int>& input_buffer = ctx.GetInputBuffer();
diff --git a/avida-core/source/main/cTaskLib.h b/avida-core/source/main/cTaskLib.h
index 638a7abca..a84da1cc6 100644
--- a/avida-core/source/main/cTaskLib.h
+++ b/avida-core/source/main/cTaskLib.h
@@ -93,6 +93,7 @@ private:
   // performed.
 
   // Basic Tasks
+  double Task_Anticipate(cTaskContext& ctx) const; // Reuse ordinary reaction accounting.
   double Task_Echo(cTaskContext& ctx) const;
   double Task_Add(cTaskContext& ctx) const;
   double Task_Add3(cTaskContext& ctx) const;
```

## Build steps

Use an empty working directory with Git, Python 3, a C++ compiler, and CMake available. Save this document there as `Avida_Anticipation_Report.md`. This extraction command writes its embedded patch and test files:

```bash
python3 - <<'PY'
from pathlib import Path
import re
report=Path('Avida_Anticipation_Report.md').read_text()
for name,body in re.findall(r'<!-- artifact: ([^\n]+) -->\n```[^\n]*\n(.*?)\n```',report,re.S):
    path=Path(name)
    assert not path.is_absolute() and '..' not in path.parts
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(body+'\n')
PY
```

```bash
git clone https://github.com/devosoft/avida.git av_src
git -C av_src checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git -C av_src submodule update --init libs/apto libs/backward-cpp
git clone av_src av_patch
git -C av_patch submodule update --init libs/apto libs/backward-cpp
git -C av_patch apply --check ../work/anticipation.patch
git -C av_patch apply ../work/anticipation.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S av_src -B build-stock -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS='-std=gnu++11'
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-stock --target avida -j4
AVIDA_DISABLE_BACKTRACE=1 cmake -S av_patch -B build-patched -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS='-std=gnu++11'
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-patched --target avida -j4
python3 work/setup_tests.py
python3 work/build_test.py
(cd tests && ./check)
```

No `CMakeLists.txt` changes. **Checked:** local builds used GCC 13.3.0 and CMake 4.4.3. The local executable was `/root/.local/bin/cmake` after `python -m pip install cmake --quiet`. The stock configure additionally had the unused flag `-DAVD_GUI_FLTK=OFF`; the commands above omit it. Locally, `av_patch` was a Git worktree with its dependency directories linked to the pinned stock dependencies; the commands above use two clones instead.

## Tests

The shortest circular instruction sequences I found for sustained matching are `IO` for R1 and `inc; IO` for R2. These are execution specimens, not self-replicating programs. The only heads instruction that performs input/output is `IO`; by itself it repeats the previous read. Adding `inc` supplies R2's change. No global program-minimization claim is made.

`tests/echo.org`:

```text
#inst_set heads_default
#hw_type 0
IO
```

`tests/inc.org`:

```text
#inst_set heads_default
#hw_type 0
inc
IO
```

The fixtures copy the pinned stock ancestor unchanged. They also prepend three `IO` instructions to that ancestor for `copy-echo.org`, or three `inc; IO` pairs for `copy-inc.org`. All program replication remains inside Avida.

Tests use initial value 7 and an uncapped additive reaction worth 1 per match, so bonus = 1 + match count. This exposes every match without a capped reaction concealing later attempts.

| Case | Outputs | Reads | Expected reaction count |
|---|---|---|---:|
| Stock ancestor, R1 | None | None | 0 |
| `IO`, R1 | 0,7,7,7 | 7,7,7,7 | 3 |
| `IO`, scripted R0 | 0,7,11,19 | 7,11,19,4 | 0 |
| `IO`, R2 | 0,7,8,9 | 7,8,9,10 | 0 |
| `inc; IO`, R2 | 1,8,9,10 | 7,8,9,10 | 3 |
| `inc; IO`, R1 | 1,8,8,8 | 7,7,7,7 | 0 |
| `IO`, switch at update 3 | 0,7,7,7,8 | 7,7,7,8,9 | 2 |

Hand calculation: registers start at zero. `IO` outputs its register then overwrites it with the supplied number. `inc` adds one before output. Ignore the first output for payment, then compare each output to the read in the same position. For the ancestor there is no `IO`. The switch tracer sets the actual world update to 0,1,2,3,4 before these five instructions; it does not use elapsed CPU cycles as an implicit world clock.

The scripted R0 test replaces only the test RNG and supplies sixteen-bit encodings of 10,18,3; adding one produces 11,19,4. It tests the delivery/checking path, not independence. An additional seed-119 R0 execution uses the ordinary generator; its actual numbers appear below, without a preclaimed exact prediction.

Added attack cases checked a failed guess followed by the correct value before a read, later output rechecks, input reset, manual-input overrides, and a committed value crossing the switch. Separate full replication tests use the capped multiplicative reward and require a reaction: the ancestor and R2 echo specimen fail replication; R1 echo and R2 increment specimens replicate with bonus 2.

Chance arithmetic is conditional on the null being tested. **Checked:** Apto at `02e1898`, `Random.h:89` and `AvidaRNG.cc`, uses `P(0.5)` against an even bound of 1,000,000,000. Under independent uniform underlying draws, each half contains 500,000,000 outcomes; sixteen bits give $2^{16}=65,536$ equally likely words.

| Rule | Luck-only comparison | Replay comparison |
|---|---|---|
| R0 | A guess in 1–65536 has $p=1/65536$; an outside guess has zero. | Same chance for any chosen earlier in-range input. |
| R1 | A guess independent of the initial draw has $p=1/65536$. | Last-input repetition matches every eligible attempt. |
| R2 | At fixed read index $k$, a blind guess within 1+k through 65536+k has $p=1/65536$, otherwise zero. | Any earlier input from this program has zero chance. |
| R-switch | Blind guesses have the applicable phase's shifted-support chance. | Repetition matches before the switch and fails after the committed boundary read. |

Thus for R0, $m$ in-range eligible attempts give expected matches $m/65536$; 65,536 attempts give one. Under the independent null, three attempts have no-match probability $(65535/65536)^3$, approximately 0.999954. R1 and R2 conditional on their observed histories are predictable; the blind rates are not their informed-program baselines. Avida uses a deterministic pseudorandom generator, not a mathematical source of independent randomness. Generator-state exploitation or shared-RNG side effects would challenge interpretation of R0.

**Checked:** the test CPU executes through the patched `cOrganism`, so enabled modes override its manual/random input triple. The trace tests deliberately supply 123,456,789 and still read the streams above. `GetTestCPUInputs()` still describes the legacy triple, not the delivered stream. Record actual reads. Analyze-mode resource-update arguments do not advance `cStats`' world update: test switch phases explicitly. The provided `RUN_BOUNDED` source was unavailable. If it executes this heads `IO` path, the same override applies; do not claim its supplied triple is the stream. Its integration remains unrun. With the feature off, its stock input route remains selected.

## Ordinary runs unchanged

Both binaries ran from identical stock configuration files, 60×60 cells, one stock ancestor, seed 119, and 400 updates. No long experiment was used for this comparison. Exact reproduction commands, after the fixture script:

```bash
(cd run-stock && ../build-stock/bin/avida -s 119 -set SPECULATIVE 0 > ../stock-run-final.log 2>&1)
(cd run-off && ../build-patched/bin/avida -s 119 -set SPECULATIVE 0 -set ANTICIPATE_MODE -1 > ../off-run-final.log 2>&1)
python3 work/compare.py
```

**Checked by execution:** all seven files, including the saved program population, match after replacing only the wall-clock timestamp header. Raw bytes do not match because those dates differ. The comparison preserves every other comment, column definition, data byte, and saved instruction sequence; it does not simply strip all comments. This is the completed check at one seed and configuration, not a claim covering every Avida configuration.

## The first experiment

This is an option for the owner, not a decision to launch it. Use the stock ancestor, 60×60 world, 50,000 updates, copy-change probability 0.0075, insertion/deletion probabilities 0.05 each per division, the single capped reaction, `ANTICIPATE_START -1`, `SPECULATIVE 0`, immediate merit increases, and no replication gate.

| Arm | Mode | Switch | Seeds | Nominal CPU-hours |
|---|---:|---|---:|---:|
| R0 | 0 | None | 21 | 21 |
| R1 | 1 | None | 21 | 21 |
| R2 | 2 | None | 21 | 21 |
| R-switch | 3 | R1→R2 at update 25000 | 21 | 21 |

Seed arithmetic needs an explicit limitation. **Checked against the supplied brief, not rerun:** the reported ranges are 17,28,9,1,0,0 tasks across three seeds. For three values spanning range $r$, their sample standard deviation is at most $r/\sqrt3$, with the third value at an endpoint. The largest supplied range gives $28/\sqrt3=16.166$, or $16.166/77=0.20995$ after normalization.

A **planning assumption**, not evidence about anticipation, transfers that dispersion to the per-seed fraction of sampled programs demonstrating R2 anticipation. Choose an illustrative mean half-width of $7/77=0.09091$. A normal approximation gives $n=\lceil(1.96×16.166/7)^2\rceil=21$. This does not supply a power calculation or a guaranteed interval: three-seed ranges do not bound population variance, and task counts are a different outcome. If a precision guarantee is required, the supplied spreads cannot determine the seed count. This conditional option makes that missing assumption visible.

Using the brief's reported one CPU-hour per 50,000-update run gives $4×21×1=84$ CPU-hours, or roughly 28 hours with three simultaneous processes. **Checked against the brief only:** that timing describes nine paid tasks, not this patch. Sixteen RNG draws per R0 input, program length, reward dynamics, and evaluation work can change it. Measure a pilot's throughput before authorizing that budget; analysis costs are additional.

Save program populations and task data every 1,000 updates, with closer sampling around 25,000. Evaluate frozen instruction sequences across fresh initial values and streams. Use uncapped diagnostic counting plus actual I/O traces to obtain eligible attempts, matches, and replay matches; capped training reaction counts alone are insufficient. Sample the same number of programs per seed, and treat the seed—not every output—as the independent experimental unit. Keep held-out evaluation randomness separate from training runs.

Results counting against the proposed effect include no R2 matching beyond an appropriate blind baseline, matching entirely explained by replay, behavior confined to the diagnostic start value, or no recovery after the switch. R1 alone cannot exclude replay. Apparent recovery entirely due to expansion of already-present incrementing programs would not demonstrate creation of a new capability after the switch. To attribute discovery specifically to payment, an additional matched R2 zero-payment arm is an option; the requested four arms alone do not isolate payment from a changed input distribution.

## What is still named

| Commitment | Grade and reason |
|---|---|
| Say the next number | Grade 2: an explicit relation is the task. |
| Exact equality and the chosen reward/cap | Grade 2: the success and payment rules are specified. |
| Constant/increment/random family and scheduled change | Grade 2: the designer chooses the admissible family and switch. |
| Fixed R1/R2 viewed as extensional objectives | They can be restated as grade-1 tasks: output the previous input, or that input plus one. Moving their formulas out of the checker does not erase this equivalence. |
| Undisclosed future stream value | A private outcome, not a grade-3 objective. |

The checker does not calculate the generating rule, but that architectural separation does not satisfy the brief's literal “no checking code computes what counts as a solution”: equality still does so. The whole setup therefore cannot be reported as truly unnamed. It implements the requested operational comparison while leaving that conceptual limit explicit.

Matching next input is not by itself anticipation in a substantive sense. R1 demonstrates the distinction: copying the last value succeeds. **Checked against the supplied S116 account only:** changing input order disrupted some earlier task performance. That motivates fresh-start, reordered/perturbed-stream, and cross-rule evaluations here. Reordering the sequence also changes the regularity; failure on an arbitrary shuffle does not by itself refute successful prediction of the original increasing stream. Neither these tests nor the patch decides what knowledge is, how task-list authorship belongs in program history, or whether to fund further runs.

## What you ran, and what you are unsure of

I retrieved the pinned repository and dependencies, compiled stock and patched Avida, applied the diff check against clean stock, compiled the linked C++ test harness, executed the listed test-CPU cases, and ran the seed-119 stock/off comparisons. No S113–S118 experiment or 50,000-update anticipation experiment was run. No GitHub changes were published.

Actual selected build output; both build commands exited 0:

```text
[100%] Linking CXX executable ../bin/avida
[100%] Built target avida
```

The first harness compilation failed because the test code used a nonexistent smart-pointer `.Get()` method. It was replaced with the source's `if (!g)` pattern; no production patch change was needed. Actual diagnostic:

```text
error: ‘Avida::GenomePtr’ {aka ‘class Apto::SmartPtr<Avida::Genome>’} has no member named ‘Get’
```

The first stock-comparison fixture supplied a bare save filename; it produced `-400.spop`. The fixture was corrected to `filename=population`, both runs were repeated, and the comparison was tightened to require exactly the intended seven files. The earlier comparison also matched apart from timestamps. The added manual-input, boundary-lock, and full replication cases followed the initial successful execution tests; these are author-built checks, not independent experimental evidence.

Actual final harness output:

```text
R1-ancestor out= in= reactions=0 bonus=1
R1-echo out=0,7,7,7 in=7,7,7,7 reactions=3 bonus=4
R0-echo-scripted out=0,7,11,19 in=7,11,19,4 reactions=0 bonus=1
R0-echo-seed119 out=0,7,35967,31186 in=7,35967,31186,24357 reactions=0 bonus=1
R2-echo out=0,7,8,9 in=7,8,9,10 reactions=0 bonus=1
R2-inc out=1,8,9,10 in=7,8,9,10 reactions=3 bonus=4
guard repeated_guess=0 recheck=0 reset_next=12
R1-inc out=1,8,8,8 in=7,7,7,7 reactions=0 bonus=1
switch-echo out=0,7,7,7,8 in=7,7,7,8,9 reactions=2 bonus=3
switch-boundary committed=9 following=10 reactions=4
gate-ancestor replication=0 bonus=1
gate-R1-echo replication=1 bonus=2
gate-R2-inc replication=1 bonus=2
gate-R2-echo replication=0 bonus=1
ALL EXPECTED CHECKS MATCHED
```

Actual final comparison output:

```text
average.dat: raw_equal=False timestamp_normalized_equal=True
count.dat: raw_equal=False timestamp_normalized_equal=True
dominant.dat: raw_equal=False timestamp_normalized_equal=True
population-400.spop: raw_equal=False timestamp_normalized_equal=True
resource.dat: raw_equal=False timestamp_normalized_equal=True
tasks.dat: raw_equal=False timestamp_normalized_equal=True
time.dat: raw_equal=False timestamp_normalized_equal=True
7/7 files match after replacing only timestamp header lines
```

The last line from each 400-update run was:

```text
UD: 400     Gen: 30.33526   Fit: 0.2466062  Orgs: 1906
```

Remaining uncertainty includes discovery through evolutionary computation, experiment duration, the transfer assumption behind 21 seeds, and the unavailable `RUN_BOUNDED` patch. Other hardware sets, parasites, avatars, mid-run enable/disable changes, checkpoint restoration of private stream state, and integer exhaustion were not execution-tested. Saved program populations do not serialize the new stream fields; loading them begins fresh streams, so they are evaluation snapshots rather than exact enabled-run restarts. Arbitrary indexed reads retain their stock interface behavior; the stated heads set uses the patched sequential path. Invalid settings throw on the first stream operation. These boundaries must remain visible when interpreting a run.

### Code appendix

The following test assets are embedded for the extraction command above. The production diff is the five-file block in “The diff”; the appendix does not add production changes.

#### work/setup_tests.py

<!-- artifact: work/setup_tests.py -->
```python
from pathlib import Path
import shutil
source=Path('av_src/avida-core/support/config')
tests=Path('tests');tests.mkdir(exist_ok=True)
for name in ['avida.cfg','instset-heads.cfg','default-heads.org']:
 shutil.copyfile(source/name,tests/name)
(tests/'events.cfg').write_text('')
(tests/'environment.cfg').write_text('REACTION ANT anticipate process:value=1:type=add\n')
(tests/'environment-cap.cfg').write_text('REACTION ANT anticipate process:value=1:type=pow requisite:max_count=1\n')
for name,body in [('echo','IO\n'),('inc','inc\nIO\n')]:
 (tests/(name+'.org')).write_text('#inst_set heads_default\n#hw_type 0\n'+body)
base=(source/'default-heads.org').read_text()
(tests/'copy-echo.org').write_text(base.replace('h-alloc','IO\nIO\nIO\nh-alloc',1))
(tests/'copy-inc.org').write_text(base.replace('h-alloc','inc\nIO\ninc\nIO\ninc\nIO\nh-alloc',1))
events='''u begin Inject default-heads.org
u 0:100:end PrintAverageData
u 0:100:end PrintDominantData
u 0:100:end PrintCountData
u 0:100:end PrintTasksData
u 0:100:end PrintTimeData
u 0:100:end PrintResourceData
u 400 SavePopulation filename=population
u 400 Exit
'''
for name in ['run-stock','run-off']:
 target=Path(name);target.mkdir(exist_ok=True)
 for file in ['avida.cfg','instset-heads.cfg','default-heads.org','environment.cfg']:
  shutil.copyfile(source/file,target/file)
 (target/'events.cfg').write_text(events)
print('Test fixtures written')
```

#### work/build_test.py

<!-- artifact: work/build_test.py -->
```python
from pathlib import Path
import shlex,subprocess
flags=Path('build-patched/avida-core/CMakeFiles/avida.dir/flags.make').read_text()
incs=next(x.split('=',1)[1] for x in flags.splitlines() if x.startswith('CXX_INCLUDES'))
cmd=['g++','-std=gnu++11','-O0','-DNDEBUG']+shlex.split(incs)+['tests/check.cc','-Wl,--start-group','build-patched/lib/libavida-core.a','build-patched/lib/libapto.a','build-patched/lib/libtcmalloc-1.4.a','-Wl,--end-group','-lpthread','-o','tests/check']
p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
Path('test-build.log').write_text(p.stdout)
print('test harness compile exit',p.returncode)
if p.returncode: print(p.stdout[-2400:])
raise SystemExit(p.returncode)
```

#### tests/check.cc

<!-- artifact: tests/check.cc -->
```cpp
#include "avida/Avida.h"
#include "avida/core/World.h"
#include "avida/private/util/GenomeLoader.h"
#include "apto/core/FileSystem.h"
#include "cAvidaConfig.h"
#include "cAvidaContext.h"
#include "cWorld.h"
#include "cStats.h"
#include "cEnvironment.h"
#include "cHardwareManager.h"
#include "cHardwareCPU.h"
#include "cHardwareTracer.h"
#include "cTestCPU.h"
#include "cCPUTestInfo.h"
#include "cOrganism.h"
#include "cUserFeedback.h"
#include <cstdlib>
#include <sstream>
#include <stdexcept>
using namespace Avida;
void need(bool b, const char* s) { if (!b) throw std::runtime_error(s); }
// Test-only RNG supplies next words 11,19,4 after diagnostic start 7.
class ScriptRandom : public Apto::Random {
  int pos;
  void reset() {}
  unsigned int getNext() {
    const int words[3] = {10,18,3};
    int bit = (words[(pos/16)%3] >> (15-pos%16)) & 1;
    ++pos; return bit ? 0 : 500000000;
  }
public:
  ScriptRandom() : Random(1000000000, 1000000000), pos(0) {}
};
class Trace : public cHardwareTracer {
  cWorld* world;
  bool previous_io;
  int previous_out, ticks;
public:
  std::vector<int> outs, ins;
  bool clock;
  Trace(cWorld* w, bool c) : world(w), previous_io(false), previous_out(0), ticks(0), clock(c) {}
  void record(cOrganism* org) {
    if (previous_io) { outs.push_back(previous_out); ins.push_back(org->GetInputBuf()[0]); }
    previous_io = false;
  }
  void TraceHardware(cAvidaContext&, cHardwareBase& base, bool, bool, int) {
    cHardwareCPU& cpu = dynamic_cast<cHardwareCPU&>(base);
    record(cpu.GetOrganism());
    if (clock) world->GetStats().SetCurrentUpdate(ticks);
    ++ticks;
    previous_io = cpu.GetInstSet().GetName(cpu.IP().GetInst()) == "IO";
    previous_out = cpu.GetRegister(1);
  }
  void PrintSuccess(cOrganism*, int) {}
  void TraceTestCPU(int, int, const cOrganism& org) { record(const_cast<cOrganism*>(&org)); }
};
std::string numbers(const std::vector<int>& v) {
  std::ostringstream s; for (size_t i=0;i<v.size();++i) { if(i) s<<",";s<<v[i]; } return s.str();
}
void run(const char* label, int mode, const char* file, int time_mod,
         const char* expected_out, const char* expected_in, int matches, bool scripted=false, bool clock=false) {
  cUserFeedback fb;
  cAvidaConfig* cfg = new cAvidaConfig;
  cString cwd(Apto::FileSystem::GetCWD());
  need(cfg->Load("avida.cfg",cwd,&fb), "config load");
  cfg->RANDOM_SEED.Set(119); cfg->SPECULATIVE.Set(0);
  cfg->ANTICIPATE_MODE.Set(mode); cfg->ANTICIPATE_START.Set(7); cfg->ANTICIPATE_SWITCH.Set(3);
  cfg->TEST_CPU_TIME_MOD.Set(time_mod); cfg->VERBOSITY.Set(0);
  cWorld* w = cWorld::Initialize(cfg,cwd,new World,&fb);
  need(w != NULL,"world initialization");
  ScriptRandom rng; if (scripted) w->GetDefaultContext().SetRandom(rng);
  GenomePtr g=Util::LoadGenomeDetailFile(file,cwd,w->GetHardwareManager(),fb);
  if (!g) throw std::runtime_error("program load");
  cTestCPU* cpu=w->GetHardwareManager().CreateTestCPU(w->GetDefaultContext());
  cCPUTestInfo ti; Trace* trace=new Trace(w,clock); ti.SetTraceExecution(HardwareTracerPtr(trace));
  Apto::Array<int> manual(3); manual[0]=123; manual[1]=456; manual[2]=789;
  ti.UseManualInputs(manual);
  cpu->TestGenome(w->GetDefaultContext(),ti,*g);
  int count=ti.GetTestPhenotype().GetCurReactionCount()[0];
  if(expected_out) need(numbers(trace->outs)==expected_out,"output sequence");
  if(expected_in) need(numbers(trace->ins)==expected_in,"input sequence");
  if (matches>=0) need(count==matches,"reaction count");
  std::cout<<label<<" out="<<numbers(trace->outs)<<" in="<<numbers(trace->ins)<<" reactions="<<count<<" bonus="<<ti.GetTestPhenotype().GetCurBonus()<<"\n";
  // The test CPU's completed nonreplicating program can also exercise output/read API guards.
  if (std::string(label)=="R2-inc") {
    cOrganism* org=ti.GetTestOrganism(); cAvidaContext& ctx=w->GetDefaultContext();
    org->DoOutput(ctx,12345); org->DoOutput(ctx,11);
    need(org->GetPhenotype().GetCurReactionCount()[0]==3,"repeated guess got credit");
    need(org->GetNextInput()==11,"pending target changed");
    org->DoOutput(ctx,12); need(org->GetPhenotype().GetCurReactionCount()[0]==4,"new read not eligible");
    org->DoOutput(ctx,false); org->DoOutput(ctx,true);
    need(org->GetPhenotype().GetCurReactionCount()[0]==4,"recheck replay");
    org->ResetInput(); need(org->GetNextInput()==12,"reset rewound stream");
    std::cout<<"guard repeated_guess=0 recheck=0 reset_next=12\n";
  }
  if (std::string(label)=="switch-echo") {
    cOrganism* org=ti.GetTestOrganism(); cAvidaContext& ctx=w->GetDefaultContext();
    cfg->ANTICIPATE_SWITCH.Set(10); w->GetStats().SetCurrentUpdate(9);
    org->DoOutput(ctx,9); w->GetStats().SetCurrentUpdate(10);
    need(org->GetNextInput()==9,"switch changed committed target");
    org->DoOutput(ctx,10); need(org->GetNextInput()==10,"switch did not change next transaction");
    need(org->GetPhenotype().GetCurReactionCount()[0]==4,"switch boundary payment");
    std::cout<<"switch-boundary committed=9 following=10 reactions=4\n";
  }
  // ti owns its program until after this function; worlds intentionally live to process exit.
  delete cpu;
}

void gate(const char* label, int mode, const char* file, bool expected) {
  cUserFeedback fb; cAvidaConfig* cfg=new cAvidaConfig;
  cString cwd(Apto::FileSystem::GetCWD()); need(cfg->Load("avida.cfg",cwd,&fb),"config");
  cfg->ENVIRONMENT_FILE.Set("environment-cap.cfg"); cfg->RANDOM_SEED.Set(119);
  cfg->ANTICIPATE_MODE.Set(mode); cfg->ANTICIPATE_START.Set(7); cfg->SPECULATIVE.Set(0);
  cfg->TEST_CPU_TIME_MOD.Set(20); cfg->REQUIRE_SINGLE_REACTION.Set(1); cfg->VERBOSITY.Set(0);
  cWorld* w=cWorld::Initialize(cfg,cwd,new World,&fb); need(w!=NULL,"world");
  GenomePtr g=Util::LoadGenomeDetailFile(file,cwd,w->GetHardwareManager(),fb);
  if (!g) throw std::runtime_error("program");
  cTestCPU* cpu=w->GetHardwareManager().CreateTestCPU(w->GetDefaultContext()); cCPUTestInfo ti;
  cpu->TestGenome(w->GetDefaultContext(),ti,*g);
  need(ti.IsViable()==expected,"replication gate");
  double bonus=expected ? ti.GetTestPhenotype().GetLastBonus() : ti.GetTestPhenotype().GetCurBonus();
  need(bonus==(expected ? 2.0 : 1.0),"capped payment");
  std::cout<<label<<" replication="<<ti.IsViable()<<" bonus="<<bonus<<"\n";
  delete cpu;
}

int main() {
  Avida::Initialize();
  run("R1-ancestor",1,"default-heads.org",1,"","",0);
  run("R1-echo",1,"echo.org",4,"0,7,7,7","7,7,7,7",3);
  run("R0-echo-scripted",0,"echo.org",4,"0,7,11,19","7,11,19,4",0,true);
  run("R0-echo-seed119",0,"echo.org",4,NULL,NULL,-1);
  run("R2-echo",2,"echo.org",4,"0,7,8,9","7,8,9,10",0);
  run("R2-inc",2,"inc.org",4,"1,8,9,10","7,8,9,10",3);
  run("R1-inc",1,"inc.org",4,"1,8,8,8","7,7,7,7",0);
  run("switch-echo",3,"echo.org",5,"0,7,7,7,8","7,7,7,8,9",2,false,true);
  gate("gate-ancestor",1,"default-heads.org",false);
  gate("gate-R1-echo",1,"copy-echo.org",true);
  gate("gate-R2-inc",2,"copy-inc.org",true);
  gate("gate-R2-echo",2,"copy-echo.org",false);
  std::cout<<"ALL EXPECTED CHECKS MATCHED\n";
}
```

#### work/compare.py

<!-- artifact: work/compare.py -->
```python
from pathlib import Path
import re
stamp=re.compile(rb'^# (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [ \d]\d \d\d:\d\d:\d\d \d{4}\r?\n',re.M)
a=Path('run-stock/data'); b=Path('run-off/data')
expected={'population-400.spop','average.dat','count.dat','dominant.dat','resource.dat','tasks.dat','time.dat'}
assert {p.name for p in a.iterdir()} == {p.name for p in b.iterdir()} == expected
for p in sorted(a.iterdir()):
 if not p.is_file():continue
 s=p.read_bytes();t=(b/p.name).read_bytes()
 ns=stamp.sub(b'# TIMESTAMP\n',s);nt=stamp.sub(b'# TIMESTAMP\n',t)
 assert ns==nt,p.name
 print(p.name+': raw_equal='+str(s==t)+' timestamp_normalized_equal=True')
print('7/7 files match after replacing only timestamp header lines')
```

END OF REPORT
