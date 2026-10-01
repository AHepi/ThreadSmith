# Programs that need history patch and execution report

## Summary for the owner

The patch compiled, and the tests produced the expected outputs. It adds three tasks: remembering event order, distinguishing short from long gaps, and recognising A then B then C. For example, a program must respond to B after A, but withhold that response when B arrives first.

Payment waits until the program handles both cases. This prevents a program from earning anything by responding every time. The handwritten programs earned payment; echoing, always responding, and erasing their retained register earned none.

With both features off, a 400-update run matched stock apart from date headers. These tests demonstrate the implemented history tasks, not their discovery through evolutionary computation or an autonomous selector. The report includes one combined patch and reproducible tests. No long experiment was launched.

## What a program can carry

**Checked:** I opened the local source at [Avida commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16). Every source location in this section refers to that unpatched checkout, relative to `avida-core/source`. These are source observations, not recollections.

| State | Across one heads `IO` | Division and reload | Checked source |
|---|---|---|---|
| Three registers, AX/BX/CX | `IO` outputs its selected register and overwrites only that register with the next input. Other registers retain their values. | Default split division resets them to zero. Nondefault inheritance can restore saved register values. Reload constructs fresh hardware. | `cpu/cHardwareCPU.h:61–75`; `cpu/cHardwareCPU.cc:4188–4201, 813–830, 882–893, 2135–2148` |
| Local and global stacks | Both retain their contents unless a stack instruction changes them. Each holds ten integers in a circular structure. | Default processor reset clears both. The inheritance path copies the local stack, not the global stack. | `cpu/cHardwareCPU.h:74–82, 109, 1065–1084`; `cpu/nHardware.h:34`; `cpu/cCPUStack.h:34–76`; `cpu/cHardwareCPU.cc:815–830, 889, 2139–2148` |
| Instruction, read, write and flow heads | Their positions persist and change through execution; the instruction head is itself temporal state. | Default split division resets the heads. Division also crops instruction memory and clears execution flags. | `cpu/nHardware.h:32`; `cpu/cHardwareCPU.h:75`; `cpu/cHardwareCPU.cc:1775–1840, 887` |
| Input/output buffers and stock input cursor | Buffers retain recent values; `DoInput` and explicit `DoOutput` append values. These are runtime records, not extra registers directly readable by this heads instruction set. | Ordinary surviving-parent processor reset does not clear these fields. `ResetInput` clears the input buffer/cursor; `NewTrial` clears both buffers/cursor. Fresh descendants and loaded programs construct new buffers. | `main/cOrganism.h:88–92, 246–252, 293–295`; `main/cOrganism.cc:161–163, 368–405, 635–661, 960–967`; `cpu/cHardwareBase.cc:71–124` |
| Active stack/head choices and labels | Persist until changed; labels support instruction copying and control flow. Instruction memory, allocation state and counters also carry execution history. | Thread reset clears the choices and labels. Hardware reset clears allocation state and its cycle counter. | `cpu/cHardwareCPU.h:76–82, 108–128`; `cpu/cHardwareCPU.cc:813–860, 886–893` |
| Task/reaction accounting | Accumulates between divisions; it is checker state, not a program-owned general register. | Division moves accounting to the previous-cycle fields and resets current counts/bonus. | `main/cPopulation.cc:659–664`; `main/cPhenotype.cc:824–939` |

**Checked:** `DIVIDE_METHOD` defaults to 1 and `EPIGENETIC_METHOD` to 0 (`main/cAvidaConfig.h:379–380`). In the ordinary heads division path, hardware reset is conditional on split division (`cpu/cHardwareCPU.cc:1830–1836`). Do not generalise its reset behaviour to every division setting, parasite configuration or failed division.

**Checked:** `LoadPopulation` constructs a new `cOrganism` at `main/cPopulation.cc:7018`, calls `SetupInject` at 7026 and restores selected saved metadata, including merit at 7040–7061. It does not reconstruct the old live processor. The ordinary descendant path likewise constructs a new program (`main/cBirthChamber.cc:232`). A saved program population is not a complete process checkpoint.

**Checked in the patch:** the new checker state is a private `cOrganism` member. It survives a surviving parent's division, `ResetInput` and processor reset. A new descendant or reloaded program starts a fresh pair. It is not serialized or copied into a descendant. Resetting the processor can therefore lose the program's interpretation of an ongoing stream without rewinding that stream.

## The design

The frozen question is whether this small, disabled-by-default patch makes reliable discrimination depend on retained input history within the supplied stream family. The owner supplied the order, interval, sequence, matched-count and ordinary-run requirements. The following encoding and deferred-payment mechanism are my design choices.

| Setting | Default | Meaning |
|---|---:|---|
| `HISTORY_MODE` | −1 | Off; 0 order; 1 interval; 2 sequence. Only one history task supplies a stream at a time. |
| `HISTORY_WINDOW` | 2 | Inclusive distance between event read indices, from 1 to 32. No wall-clock timing is claimed. |
| `HISTORY_CASE` | −1 | Randomly choose one of ten pair cases each pair. Values 0–9 select diagnostic cases. |

History mode and `ANTICIPATE_MODE` must not be enabled together; a stream operation throws if they are. With history disabled, reply 01's stream and stock input paths remain available. Neither feature being enabled selects the stock path. Live changes to these settings during a pair are outside the tested contract.

Events are whole small integers: X=0, A=1, B=2, C=3. There is no payload or hidden answer in extra bits. A frame contains the following events; its final X lets the checker settle payment after all responses. Each pair contains one positive frame and one negative frame, in a freshly randomised order. Diagnostic cases encode orientation in `case % 2`; sequence's negative permutation is selected by `case / 2`. Order and interval ignore the latter component.

| Task name | Positive frame | Negative frame | Response opportunity |
|---|---|---|---|
| `hist_order` | A B X | B A X | First explicit output following each B |
| `hist_interval` | X A X^(W−1) B X | A X^W B X | First explicit output following each B |
| `hist_sequence` | A B C X | A C B X; B A C X; B C A X; C A B X; or C B A X | First explicit output following each C |

Every matched frame has the same length and event multiset. For interval, B occupies the same position in both frames; A moves one position, so its distance from B is W versus W+1. X repetitions denote repeated reads, not CPU delays. With W=2, the two frames are X A X B X and A X X B X.

Exactly output **1** at the response opportunity means “respond”; every other integer means “withhold.” Outputs after other events have no classification meaning. Input/output ordering is crucial: the output half of `IO` answers the event received by the *previous* read, before `IO` supplies the next event. An initial output before any read earns nothing.

The checker resets its event history at each frame. A remembered A makes a later B positive for order; interval additionally requires a read distance at most W. Sequence requires A followed by B before C. B before A, or C before completion of that prefix, is negative. The generated domain has one A and one B, and, for sequence, one C per frame. This is a finite temporal task family, not an arbitrary-event-stream interface.

The first output after each read commits that opportunity. Later guesses cannot amend it. Reading again without output commits withholding; missing a positive response consequently fails the pair. Any false response or missed positive response cancels the entire pair's payment. There is no partial positive payment to collect before the negative frame. On an explicit output after the final X of a successful pair, the relevant task emits one payment pulse, then clears it. Division-only checks and output rechecks cannot mint or replay that pulse. A failed pair adds zero bonus; it does not subtract the program's baseline processor allocation.

A training environment can use, for example:

```text
REACTION O hist_order process:value=1:type=pow requisite:max_count=1
```

Substitute the corresponding task for other modes. **Checked:** ordinary reaction processing applies task quality (`main/cEnvironment.cc:1390–1403`); the capped harness below observed one reaction and bonus 2. Uncapped additive diagnostics expose each successful pair separately.

Worked-out limitation: a deterministic memoryless function of the current event must give the same answer to B (or C) in both frames, so it cannot satisfy both. This covers arbitrary integer outputs, since only equality with 1 matters. Random answers can succeed by accident: independent responses with probability p pass a pair with probability p(1−p), at most 1/4. Thus one payment is not evidence that a capability depends on history. The implementation excludes the requested deterministic shortcuts; it cannot exclude lucky finite traces.

The hard-to-vary check holds the event multiset fixed while changing order or spacing. Stored AX is held by the internal erasure test: erase it and payment disappears. Deferred settlement is held by the always-response attack: immediate positive payment alone would permit that shortcut. The numeric marks, names and exact reward magnitude are conventions. An `inc` in two initial specimens was idle and was removed; the shorter specimens were rerun. The checker is deliberately given the answer rule, so success here does not supply an unnamed goal or an autonomous selector.

## The diff

I applied reply 01's attached diff, then extended it. The following combined unified diff applies directly to clean 47f13dad; do not apply reply 01 again first. It changes five existing files and adds one header. Relative to reply 01, it adds **117 lines and removes one**, within the requested approximate 250-line C++ allowance. The new header needs no build-system change. Both the combined clean-base apply check and the incremental apply check completed with exit 0.

<!-- artifact: history/full.patch -->
```diff
diff --git a/avida-core/source/main/cAvidaConfig.h b/avida-core/source/main/cAvidaConfig.h
index 14c8b3e62..8ec3b31d2 100644
--- a/avida-core/source/main/cAvidaConfig.h
+++ b/avida-core/source/main/cAvidaConfig.h
@@ -304,6 +304,15 @@ public:
   CONFIG_ADD_VAR(MIGRATION_FILE, cString, "-", "NxN file that describes connectivity weights between demes");   
   
   
+  // Anticipation settings leave the stock input path selected by default.
+  CONFIG_ADD_VAR(ANTICIPATE_MODE, int, -1, "-1=off, 0=random, 1=repeat, 2=increment, 3=repeat then increment");
+  CONFIG_ADD_VAR(ANTICIPATE_SWITCH, int, 25000, "First update using increment in mode 3");
+  CONFIG_ADD_VAR(ANTICIPATE_START, int, -1, "-1=random initial value; 1..65536=diagnostic initial value");
+
+  CONFIG_ADD_VAR(HISTORY_MODE, int, -1, "-1=off, 0=order, 1=interval, 2=sequence; ANTICIPATE_MODE must be off");
+  CONFIG_ADD_VAR(HISTORY_WINDOW, int, 2, "Inclusive read gap, 1..32");
+  CONFIG_ADD_VAR(HISTORY_CASE, int, -1, "-1=random pair; 0..9=diagnostic pair/orientation");
+
   // -------- Mutation config options --------
   CONFIG_ADD_GROUP(MUTATION_GROUP, "Mutation rates");  
   CONFIG_ADD_VAR(COPY_MUT_PROB, double, 0.0075, "Substitution rate (per copy)");
diff --git a/avida-core/source/main/cOrganism.cc b/avida-core/source/main/cOrganism.cc
index 943176891..fe52d2519 100644
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
@@ -365,6 +372,77 @@ int cOrganism::ReceiveValue()
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
+  const cAvidaConfig& cfg = m_world->GetConfig();
+  if (cfg.HISTORY_MODE.Get() != -1) {
+    if (cfg.ANTICIPATE_MODE.Get() != -1)
+      throw std::invalid_argument("HISTORY and ANTICIPATE are exclusive");
+    int choice = cfg.HISTORY_CASE.Get();
+    if (choice < -1 || choice > 9)
+      throw std::invalid_argument("Invalid HISTORY_CASE");
+    if (choice == -1) {
+      choice = 0;
+      if (m_history.NewPair())
+        choice = m_world->GetDefaultContext().GetRandom().GetUInt(10);
+    }
+    return m_history.Read(cfg.HISTORY_MODE.Get(), cfg.HISTORY_WINDOW.Get(), choice);
+  }
+  if (cfg.ANTICIPATE_MODE.Get() == -1)
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
+  m_history.Clear();
+  if (m_world->GetConfig().HISTORY_MODE.Get() != -1) {
+    if (m_world->GetConfig().ANTICIPATE_MODE.Get() != -1)
+      throw std::invalid_argument("HISTORY and ANTICIPATE are exclusive");
+    m_history.Respond(value);
+    return;
+  }
+  if (m_world->GetConfig().ANTICIPATE_MODE.Get() == -1) return;
+  PrepareAnticipation(ctx);
+  m_anticipate_match = m_anticipate_read && !m_anticipate_attempted && value == m_anticipate_next;
+  m_anticipate_attempted = true;
+}
+
 void cOrganism::DoInput(const int value)
 {
   DoInput(m_input_buf, m_output_buf, value);
@@ -384,23 +462,32 @@ void cOrganism::DoOutput(cAvidaContext& ctx, const bool on_divide, cContextPheno
 
 void cOrganism::DoOutput(cAvidaContext& ctx, const int value)
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   m_output_buf.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, m_input_buf, m_output_buf, false, false);
   else doOutput(ctx, m_input_buf, m_output_buf, false, false);
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
+  m_history.Clear();
 }
 
 void cOrganism::DoOutput(cAvidaContext& ctx, const int value, bool is_parasite, cContextPhenotype* context_phenotype) 
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   m_output_buf.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, m_input_buf, m_output_buf, false, (bool)is_parasite, context_phenotype); 
   else doOutput(ctx, m_input_buf, m_output_buf, false, (bool)is_parasite, context_phenotype); 
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
+  m_history.Clear();
 }
 
 void cOrganism::DoOutput(cAvidaContext& ctx, tBuffer<int>& input_buffer, tBuffer<int>& output_buffer, const int value)
 {
+  BeginAnticipation(ctx, value); // Scope prediction credit to this explicit output.
   output_buffer.Add(value);
   if (m_world->GetConfig().USE_AVATARS.Get()) doAVOutput(ctx, input_buffer, output_buffer, false, false);
   else doOutput(ctx, input_buffer, output_buffer, false, false);
+  m_anticipate_match = false; // Prevent later task rechecks from replaying credit.
+  m_history.Clear();
 }
 
 
diff --git a/avida-core/source/main/cOrganism.h b/avida-core/source/main/cOrganism.h
index 63b7e42ea..681c3fd22 100644
--- a/avida-core/source/main/cOrganism.h
+++ b/avida-core/source/main/cOrganism.h
@@ -31,6 +31,7 @@
 #include "cCPUMemory.h"
 #include "cMutationRates.h"
 #include "cPhenotype.h"
+#include "cHistoryTask.h"
 #include "cOrgInterface.h"
 #include "cOrgMessage.h"
 #include "tBuffer.h"
@@ -86,6 +87,12 @@ private:
   Genome m_offspring_genome;              // Child genome, while under construction.
 
   // Input and Output with the environment
+  // Private pending input and one-attempt state belong to this Avida program.
+  cHistoryTask m_history;
+  int m_anticipate_next, m_anticipate_last, m_anticipate_rule;
+  bool m_anticipate_ready, m_anticipate_read, m_anticipate_attempted, m_anticipate_match;
+  void PrepareAnticipation(cAvidaContext& ctx);
+  void BeginAnticipation(cAvidaContext& ctx, int value);
   int m_input_pointer;
   tBuffer<int> m_input_buf;
   tBuffer<int> m_output_buf;
@@ -246,8 +253,11 @@ public:
   void Rotate(cAvidaContext& ctx, int direction) { m_interface->Rotate(ctx, direction); }
 
   int GetInputAt(int i) { return m_interface->GetInputAt(i); }
-  int GetNextInput() { return m_interface->GetInputAt(m_input_pointer); }
-  int GetNextInput(int& in_input_pointer) { return m_interface->GetInputAt(in_input_pointer); }
+  // Both sequential read entry points consume the same private stream when enabled.
+  int GetNextInput() { return GetNextInput(m_input_pointer); }
+  int GetNextInput(int& in_input_pointer);
+  bool HistoryMatch(int mode) const { return m_history.Match(mode); }
+  bool AnticipationMatch() const { return m_anticipate_match; }
   tBuffer<int>& GetInputBuf() { return m_input_buf; }
   tBuffer<int>& GetOutputBuf() { return m_output_buf; }
   void Die(cAvidaContext& ctx) { m_interface->Die(ctx); m_is_dead = true; } 
diff --git a/avida-core/source/main/cTaskLib.cc b/avida-core/source/main/cTaskLib.cc
index afde3d256..86bbcb034 100644
--- a/avida-core/source/main/cTaskLib.cc
+++ b/avida-core/source/main/cTaskLib.cc
@@ -84,6 +84,11 @@ cTaskEntry* cTaskLib::AddTask(const cString& name, const cString& info, cEnvReqs
   // The following if blocks are grouped based on class of task.  Chaining too
   // many if block causes problems block nesting depth in Visual Studio.net 2003.
   
+  // Register the stream match without naming or evaluating a generating rule.
+  if (name == "hist_order") NewTask(name, "Order pair", &cTaskLib::Task_HistoryOrder);
+  if (name == "hist_interval") NewTask(name, "Interval pair", &cTaskLib::Task_HistoryInterval);
+  if (name == "hist_sequence") NewTask(name, "Sequence pair", &cTaskLib::Task_HistorySequence);
+  if (name == "anticipate") NewTask(name, "Next input match", &cTaskLib::Task_Anticipate);
   if (name == "echo")      NewTask(name, "Echo", &cTaskLib::Task_Echo);
   else if (name == "echo_dup")  NewTask(name, "Echo_dup",  &cTaskLib::Task_Echo);
   else if (name == "add")  NewTask(name, "Add",  &cTaskLib::Task_Add);
@@ -448,6 +453,25 @@ void cTaskLib::SetupTests(cTaskContext& ctx) const
 }
 
 
+double cTaskLib::Task_HistoryOrder(cTaskContext& ctx) const
+{
+  return !ctx.GetOnDivide() && ctx.GetOrganism()->HistoryMatch(0) ? 1.0 : 0.0;
+}
+double cTaskLib::Task_HistoryInterval(cTaskContext& ctx) const
+{
+  return !ctx.GetOnDivide() && ctx.GetOrganism()->HistoryMatch(1) ? 1.0 : 0.0;
+}
+double cTaskLib::Task_HistorySequence(cTaskContext& ctx) const
+{
+  return !ctx.GetOnDivide() && ctx.GetOrganism()->HistoryMatch(2) ? 1.0 : 0.0;
+}
+
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
index 638a7abca..80d850a3e 100644
--- a/avida-core/source/main/cTaskLib.h
+++ b/avida-core/source/main/cTaskLib.h
@@ -93,6 +93,10 @@ private:
   // performed.
 
   // Basic Tasks
+  double Task_HistoryOrder(cTaskContext& ctx) const;
+  double Task_HistoryInterval(cTaskContext& ctx) const;
+  double Task_HistorySequence(cTaskContext& ctx) const;
+  double Task_Anticipate(cTaskContext& ctx) const; // Reuse ordinary reaction accounting.
   double Task_Echo(cTaskContext& ctx) const;
   double Task_Add(cTaskContext& ctx) const;
   double Task_Add3(cTaskContext& ctx) const;
diff --git a/avida-core/source/main/cHistoryTask.h b/avida-core/source/main/cHistoryTask.h
new file mode 100644
index 0000000..49e3ad8
--- /dev/null
+++ b/avida-core/source/main/cHistoryTask.h
@@ -0,0 +1,66 @@
+#ifndef cHistoryTask_h
+#define cHistoryTask_h
+
+#include <stdexcept>
+
+// Private checker state. No new instruction exposes it to the virtual machine.
+class cHistoryTask {
+  int mode, window, len, pos, pair_case, last, a_pos, stage;
+  bool ready, attempted, good, expected;
+  int pulse;
+public:
+  cHistoryTask() : mode(-1), window(2), len(0), pos(0), pair_case(0),
+    last(0), a_pos(-1), stage(0), ready(false), attempted(false),
+    good(true), expected(false), pulse(-1) {}
+  bool NewPair() const { return pos == 0 || pos == 2 * len; }
+  bool Match(int task) const { return pulse == task; }
+  void Clear() { pulse = -1; }
+  void Respond(int value, bool explicit_output = true) {
+    pulse = -1;
+    if (!ready || attempted) return;
+    attempted = true;
+    const int terminal = mode == 2 ? 3 : 2;
+    if (last == terminal && ((value == 1) != expected)) good = false;
+    if (pos == 2 * len) {
+      if (good && explicit_output) pulse = mode;
+      pos = 0;
+    }
+  }
+  int Read(int m, int w, int choice) {
+    if (m < 0 || m > 2 || w < 1 || w > 32 || choice < 0 || choice > 9)
+      throw std::invalid_argument("Invalid HISTORY setting");
+    // Skipping an output commits silence; it cannot itself trigger payment.
+    Respond(0, false);
+    if (pos == 0) {
+      mode = m; window = w; pair_case = choice;
+      len = mode == 0 ? 3 : mode == 1 ? window + 3 : 4;
+      good = true;
+    }
+    const int i = pos % len;
+    const bool positive = (pos / len) == (pair_case % 2);
+    if (i == 0) { a_pos = -1; stage = 0; }
+    last = 0;
+    if (mode == 0 && i < 2) last = positive ? i + 1 : 2 - i;
+    if (mode == 1) {
+      if (i == (positive ? 1 : 0)) last = 1;
+      if (i == window + 1) last = 2;
+    }
+    if (mode == 2 && i < 3) {
+      static const int sequences[6][3] = {
+        {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}
+      };
+      last = sequences[positive ? 0 : 1 + pair_case / 2][i];
+    }
+    expected = false;
+    if (last == 1) { a_pos = i; stage = 1; }
+    if (last == 2) {
+      expected = a_pos >= 0 && (mode != 1 || i - a_pos <= window);
+      stage = stage == 1 ? 2 : 0;
+    }
+    if (last == 3) { expected = stage == 2; stage = 0; }
+    ++pos;
+    ready = true; attempted = false;
+    return last;
+  }
+};
+#endif
```

## Hand-written programs

These circular heads instruction sequences are execution specimens, not self-replicating programs. Registers start at zero. Each `nop-A` immediately following `IO` selects AX; ordinary `IO` selects BX. **Checked:** the instruction meanings were read in `cpu/cHardwareCPU.cc:235, 4188–4201` and the heads instruction-set file. `nand` with untouched CX=0 produces −1, a withheld response.

| Specimen | Instruction count including modifiers | Retained history |
|---|---:|---|
| Order | 6 | AX holds the first event while BX reads the second. |
| Interval, W=2 | 7 | AX holds the second event until B arrives; the instruction position counts the intervening reads. |
| Sequence | 7 | AX holds the first event through the second and third reads. On the given permutations, C in third position with AX=A identifies ABC. Earlier C receives −1 or 3 and therefore no response. |

These are the shortest specimens I found in this work; no exhaustive minimisation was run. They exploit the declared frame structure. They are not general-purpose recognisers for arbitrary filler placement or changed windows. They start aligned at a fresh stream; execution across real replication with an ongoing stream was not tested.

Order:

```text
#inst_set heads_default
#hw_type 0
IO
nop-A
nand
IO
IO
nop-A
```

Interval, W=2:

```text
#inst_set heads_default
#hw_type 0
IO
IO
nop-A
IO
IO
IO
nop-A
```

Sequence:

```text
#inst_set heads_default
#hw_type 0
IO
nop-A
nand
IO
IO
IO
nop-A
```

The shared memoryless counterexample is `IO` alone, which echoes the last input. Its outputs at B/C are 2/3, never 1. The always-response specimen `nand; inc; inc; IO` outputs 1 after every event; it necessarily gives a false response on the negative frame. Neither earns a pair reward. The harness also checks all sixteen binary maps of X/A/B/C; none earns payment.

## Tests with expected outputs, and build steps

Hand calculations were recorded before the first harness execution. One positive and one negative classification must be correct before any payment. For example, order A B X / B A X with responses after those reads of 0,1,0 / 0,0,0 yields reaction counts 0,0,0 / 0,0,1. Replacing the second frame's response after B by 1 makes the final count zero. For interval W=2, distances 2 and 3 require response and withholding respectively. Only ABC among the six sequence permutations requires a response after C.

| Linked-harness case | Expected result |
|---|---|
| Final order specimen, both orientations and random pairs | 7 completed pair rewards; bonus 8 |
| Final interval specimen, both orientations and random pairs | 6 completed pair rewards; bonus 7 |
| Final sequence specimen, all ten cases and random pairs | 6 completed pair rewards; bonus 7 |
| Each specimen with retained AX erased before its decisive response | 0 rewards; bonus 1 |
| Echo and always-response specimens, each task | 0 rewards; bonus 1 |
| Wrong guess followed by correct guess without reading | No repair of the failed pair |
| Division-only output before settlement; repeated outputs/rechecks after settlement | No extra reward |
| Skip a positive response | No reward |
| Reset input buffer midway through A then B | Next read remains B; retained checker history can finish the pair |
| Capped multiplicative reaction | Stateful count 1, bonus 2; echo count 0, bonus 1 |
| All deterministic present-event binary mappings | Zero rewards on every task/case |
| Window boundaries 1–32, both orientations | Gap W accepted; gap W+1 rejected; one reward per correctly answered pair |

The last two checks exercise the actual production header from the linked executable; their responses are supplied by the C++ rig. They are not executions of heads programs for all 32 window values. The primary specimens, echo, always-response and register-erasure controls run through Avida's test CPU and patched task library.

Why the reward counts differ: `TEST_CPU_TIME_MOD=10` budgets 60,70,70 executed steps for the final instruction sequences. Modifiers are consumed by their preceding instructions. The respective loops use 4,5,5 steps and produce 3,5,4 reads. Actual read totals must therefore be 45,70,56. Payment requires the output following a frame's final X, giving `floor((reads−1)/(2×frame_length))` = 7,6,6. Each uncapped additive reward increases bonus by one from its initial 1.

Save this document as `Brief02_History_Tasks_Execution_Report.md` in an empty working directory. Its code appendix contains the complete fixtures and harness. Extract the embedded files:

```bash
python3 - <<'PY'
from pathlib import Path
import re
report=Path('Brief02_History_Tasks_Execution_Report.md').read_text()
for name,body in re.findall(r'<!-- artifact: ([^\n]+) -->\n```[^\n]*\n(.*?)\n```',report,re.S):
    path=Path(name)
    assert not path.is_absolute() and '..' not in path.parts
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(body+'\n')
PY
```

Build on Linux with Git, Python 3, GCC and the Python CMake package available. Locally I used GCC 13.3.0 and CMake 4.4.3; `python3 -m pip install cmake` supplies the latter if needed. Commands for a fresh directory:

```bash
git clone https://github.com/devosoft/avida.git avida
git -C avida checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git -C avida submodule update --init libs/apto libs/backward-cpp
git clone avida av_patch
git -C av_patch submodule update --init libs/apto libs/backward-cpp
git -C av_patch apply --check ../history/full.patch
git -C av_patch apply ../history/full.patch
ln -s avida av_src
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake -S avida -B build-stock -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS=-std=gnu++11
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake --build build-stock --target avida -j4
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake -S av_patch -B build-patched -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS=-std=gnu++11
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake --build build-patched --target avida -j4
python3 work/setup_tests.py
python3 history/setup.py
python3 history/build.py
(cd history/tests && ./check)
python3 work/build_test.py
(cd tests && ./check)
```

**Checked:** dependency commits were Apto `02e18980071d237f1ea4641f3f35cae469e2ed38` and backward-cpp `dc8b8c76822dcbc8918f032171050ad90e11eb7f`. My patched checkout was a detached worktree; the fresh-directory instructions use a clone. The original anticipation harness and fixtures are embedded unchanged, including their `av_src` path; the symlink above supplies it.

## Ordinary runs unchanged

I ran stock and the combined patch for 400 updates, seed 119, 60×60 cells, stock ancestor/configuration and `SPECULATIVE=0`. Both features were explicitly disabled in the patched run. These commands ran after the fixture script:

```bash
(cd run-stock && ../build-stock/bin/avida -s 119 -set SPECULATIVE 0 > ../stock-run-final.log 2>&1)
(cd run-off && ../build-patched/bin/avida -s 119 -set SPECULATIVE 0 -set ANTICIPATE_MODE -1 -set HISTORY_MODE -1 > ../off-run-final.log 2>&1)
python3 work/compare.py
```

The comparison checks the exact seven-file set, including the saved program population, and replaces only timestamp header lines. It preserves all other comments and bytes. Actual output:

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

Both final run lines were:

```text
UD: 400     Gen: 30.33526   Fit: 0.2466062  Orgs: 1906
```

This is an observed match at one seed and configuration. It does not cover every instruction set or Avida configuration.

## A first experiment

One option for the owner is a small exploratory pilot with six arms: order, interval and sequence, each with payment and without payment. Use the same stream generator in each matched pair of arms, `HISTORY_CASE=-1`, W=2, anticipation off, heads instructions, a stock ancestor, 60×60 cells and three seeds per arm. Run each seed continuously for 5,000 updates, saving program populations without reloading the live run. Use the capped reward above versus an additive reward of zero, leave the replication gate off, and record the chosen processor-allocation settings. Three seeds support an exploratory comparison, not a claimed precision or power guarantee.

That option totals 18 runs and 90,000 updates. **Checked against the supplied brief only:** its planning rate is about one CPU-hour per 50,000 updates in a 3,600-cell world. Transferring that rate gives 1.8 CPU-hours, approximately 36 minutes with three concurrent Avida processes, plus compilation/evaluation. This timing transfer is an assumption; the new tasks' actual throughput was not measured in such a pilot. No pilot or 50,000-update history run was launched.

Evaluate saved instruction sequences in fresh test executions, logging actual input/output streams and both classifications, not just capped task counts. Use all paired orders/permutations, random fresh pairs and retained-state ablations. Keep seed as the experimental unit. Compare payment and zero-payment arms on completed-pair performance and replication capability; repeating the handwritten demonstrations would not measure discovery.

| Observation | What it would count against |
|---|---|
| A deterministic present-event map earns payment | The checker meets the stated history requirement. |
| Payment survives removal of all causally relevant retained state | Attribution of that program's discrimination to its claimed memory mechanism. Erasing AX alone is only appropriate for these specimens. |
| Paid and zero-payment arms show no distinguishable acquisition within the stated pilot | Attribution to this payment scheme within that run budget. |
| Results depend on fixed diagnostic case order | Interpretation as discrimination across the randomised stream family. |
| High reaction counts coexist with wrong negative responses in actual traces | The payment/accounting implementation. |

One interpretation counts demonstrated temporal discrimination as a computational capability; another reserves a knowledge claim for additional explanatory or problem-solving behaviour. A designer's task list can be included in a record of computational selection or tracked separately as external design input. These are options for the owner, not conclusions selected by this patch. Whether a fixed selector counts as an instinct, and which costly run follows, remains open.

## What is still named, by grade

| Commitment | Grade |
|---|---|
| A before B, distance at most W, and A then B then C | Grade 1: three explicitly named target tasks. |
| A/B/C/X identities, response integer 1, frame boundaries and W | Grade 1 parameters fixing those exact tasks. |
| Any successful member of the specified paired stream family | Grade 2 when described as a class; its explicit checks remain the grade-1 tasks above. |
| Random permutation/orientation and deferred pair payment | Grade 2 procedural rules chosen by the designer. |
| Randomly undisclosed next events | Hidden instances, not a grade-3 standard. |

No part meets grade 3. Checking code still computes which response counts as a solution. The execution environment supplies temporal inputs and remembers evaluation history, but does not change its standards, hold its own problem, formulate criticism or invent a new task.

## What you ran, with outputs, and what you are unsure of

I read all three attachments, extracted and applied reply 01, opened the pinned C++ source, built stock and the combined patch, compiled both linked harnesses, ran the history cases and original anticipation cases, checked both patch application routes, and completed the two 400-update runs and their byte comparison. All case preparation and test code were supplied by me, except reply 01's unchanged regression assets. This is a single-agent engineering test, not an independent replication. The supplied neuroscience report was read; its 22 outside studies were not reopened and are not evidence for this patch's results.

Both completed builds exited 0. Their final output lines were:

```text
[100%] Linking CXX executable ../bin/avida
[100%] Built target avida
```

Build setup initially failed because `cmake` was not on PATH and dependency links did not remain available. Using `python -m cmake` and materialising pinned submodules resolved those setup failures. Selected actual earlier diagnostics, not successful build output:

```text
/bin/bash: line 10: cmake: command not found
The source directory
  /workspace/scratch/189121d17942/av_patch/libs/apto
 does not contain a CMakeLists.txt file.
cc1plus: fatal error: /workspace/scratch/189121d17942/av_patch/libs/apto/src/scheduler/RoundRobin.cc: No such file or directory
```

The first history harness compiled and matched its precomputed counts, using order/sequence specimens with an extra `inc`. After that run, I removed the unnecessary `inc`, revised the order expectation from six to seven rewards for its changed execution budget, and added mid-frame reset, mixed-mode and capped-payment controls. There was no production-code change after the first harness run. The appendix preserves the first output alongside the final output; the subsequent changes concern specimen size and the rig's added controls.

Actual final history-harness output:

```text
mode=0 case=0 program=order.org erase=0 rewards=7 bonus=8 reads=45
  inputs=1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0
  outputs=0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1,0,-1,2,0,-1,1
mode=0 case=1 program=order.org erase=0 rewards=7 bonus=8 reads=45
mode=0 case=-1 program=order.org erase=0 rewards=7 bonus=8 reads=45
mode=0 case=0 program=order.org erase=1 rewards=0 bonus=1 reads=45
mode=0 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=0 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
mode=1 case=0 program=interval.org erase=0 rewards=6 bonus=7 reads=70
  inputs=0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0
  outputs=0,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0
mode=1 case=1 program=interval.org erase=0 rewards=6 bonus=7 reads=70
mode=1 case=-1 program=interval.org erase=0 rewards=6 bonus=7 reads=70
mode=1 case=0 program=interval.org erase=1 rewards=0 bonus=1 reads=70
mode=1 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=1 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
mode=2 case=0 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
  inputs=1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0
  outputs=0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1,0,-1,2,1,0,-1,3,1
mode=2 case=1 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=2 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=3 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=4 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=5 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=6 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=7 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=8 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=9 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=-1 program=sequence.org erase=0 rewards=6 bonus=7 reads=56
mode=2 case=0 program=sequence.org erase=1 rewards=0 bonus=1 reads=56
mode=2 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=2 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
guards deferred=1 division=0 replay=0 repeated_guess=0 reset_continues=1
skip_positive=0
all_16_memoryless_event_maps x 3_modes x 10_cases: rewards=0
windows_1_to_32 both_orientations: gap_W=yes gap_W_plus_1=no rewards=1
midframe_reset next=B pair_reward=1
mixed_modes rejected=1
capped mode=0 stateful_reward=1 bonus=2 echo_reward=0 bonus=1
capped mode=1 stateful_reward=1 bonus=2 echo_reward=0 bonus=1
capped mode=2 stateful_reward=1 bonus=2 echo_reward=0 bonus=1
ALL HISTORY EXPECTATIONS MATCHED
```

Actual anticipation-regression output:

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

Both harness compilations exited 0, printing `History harness compile exit 0` and `test harness compile exit 0`. The final combined patch has SHA-256 `2c0457b79294a6f0c8562588a31e48149dcc4f71c8650e8a1982fc0e62975ef6`.

Unrun questions include discovery through evolutionary computation, generalisation outside the generated frames, persistence of these handwritten programs' behaviour across replication, performance with other hardware sets, avatars or parasites, configuration changes mid-pair, and integration with the unavailable `RUN_BOUNDED` source. Buffer/task summaries from stock analyze mode must not be mistaken for the delivered private stream; this harness records actual reads. Enabled streams are not restored by population reload. Random lucky responses and programs exploiting frame position require explicit controls before inferring a general memory mechanism. No claim is made that these specimens are globally minimal, that read intervals reproduce neuronal physiology, or that the selector now learns its own standards.

### Code appendix

The full production patch is embedded in “The diff.” These are reproducible test assets. The initial-output file and frozen specification retain the development record. All program replication in the inherited regression fixtures remains inside Avida.

#### history/spec-v1.txt

<!-- artifact: history/spec-v1.txt -->
```text
Frozen v1 before implementation or test execution. Owner-required: order, read interval, ABC sequence; equal multisets; stateful positive and memoryless negative; disabled unchanged. Author choices: marks X=0,A=1,B=2,C=3, response=1 only after B (order/interval) or C(sequence); others mean no response. Frame includes trailing X. Ordered pair contains one positive, one negative with randomly chosen order. Payment deferred to explicit output after final X in pair. Pair must classify both; false positives/negatives cancel entire pair, no partial reward. First output after each read commits; rereads without output commit no response. No division/recheck credit. Per-parent stream and pair survive division/reset-input; descendants/reloaded programs start anew. HISTORY_MODE mutually exclusive with anticipation. Fixed diagnostic HISTORY_CASE 0..9; randomized -1. Interval gap inclusive W, negative W+1. Order ABX/BAX; interval X A X^(W-1) B X / A X^W B X; sequence ABCX against one of ACBX,BACX,BCAX,CABX,CBAX. All frames identical multiset within task. Deterministic y=f(current event) cannot finish a pair; randomized memoryless strategies may pass by chance, requiring repeated held-out diagnosis. This is finite generated input scope, not unrestricted event streams. State erasure of stored AX in specimens must remove successful classification. Unexpected nonzero net payment for always-respond/echo or replay is failure. No costly experiments authorized here.
```

#### history/setup.py

<!-- artifact: history/setup.py -->
```python
from pathlib import Path
import shutil
p=Path('history/tests');p.mkdir(exist_ok=True)
for n in ['avida.cfg','instset-heads.cfg','default-heads.org']: shutil.copyfile(Path('tests')/n,p/n)
(p/'events.cfg').write_text('')
(p/'environment-cap.cfg').write_text('REACTION O hist_order process:value=1:type=pow requisite:max_count=1\nREACTION I hist_interval process:value=1:type=pow requisite:max_count=1\nREACTION S hist_sequence process:value=1:type=pow requisite:max_count=1\n')
(p/'environment.cfg').write_text('REACTION O hist_order process:value=1:type=add\nREACTION I hist_interval process:value=1:type=add\nREACTION S hist_sequence process:value=1:type=add\n')
programs={'order':'IO nop-A nand IO IO nop-A','interval':'IO IO nop-A IO IO IO nop-A','sequence':'IO nop-A nand IO IO IO nop-A','echo':'IO','always':'nand inc inc IO'}
for n,body in programs.items(): (p/(n+'.org')).write_text('#inst_set heads_default\n#hw_type 0\n'+'\n'.join(body.split())+'\n')
print('History fixtures written; W=2; stateful expected counts=7,6,6 at time_mod=10')
```

#### history/check.cc

<!-- artifact: history/check.cc -->
```cpp
#include "avida/Avida.h"
#include "avida/core/World.h"
#include "avida/private/util/GenomeLoader.h"
#include "apto/core/FileSystem.h"
#include "cAvidaConfig.h"
#include "cAvidaContext.h"
#include "cWorld.h"
#include "cEnvironment.h"
#include "cHardwareManager.h"
#include "cHardwareCPU.h"
#include "cHardwareTracer.h"
#include "cTestCPU.h"
#include "cCPUTestInfo.h"
#include "cOrganism.h"
#include "cUserFeedback.h"
#include <iostream>
#include <sstream>
#include <stdexcept>
using namespace Avida;
void need(bool b,const char* s){if(!b) throw std::runtime_error(s);}
std::string nums(const std::vector<int>& v){std::ostringstream s;for(size_t i=0;i<v.size();++i){if(i)s<<',';s<<v[i];}return s.str();}
class Trace: public cHardwareTracer {
 bool pending, erase; int before;
public:
 std::vector<int> in,out;
 Trace(bool e):pending(false),erase(e),before(0){}
 void record(cOrganism* o){if(pending){in.push_back(o->GetInputBuf()[0]);out.push_back(before);}pending=false;}
 void TraceHardware(cAvidaContext&,cHardwareBase& b,bool,bool,int){
  cHardwareCPU& c=dynamic_cast<cHardwareCPU&>(b);record(c.GetOrganism());
  pending=c.GetInstSet().GetName(c.IP().GetInst())=="IO";
  if(pending){
   cHeadCPU n=c.IP();n.Advance();cString name=c.GetInstSet().GetName(n.GetInst());
   int r=name=="nop-A"?0:name=="nop-C"?2:1;
   // Internal cut: erase retained AX just before its response, after another register read B/C.
   if(erase && r==0 && c.GetOrganism()->GetInputBuf().GetNumStored()>0 &&
      (c.GetOrganism()->GetInputBuf()[0]==2 || c.GetOrganism()->GetInputBuf()[0]==3))c.GetRegister(0)=0;
   before=c.GetRegister(r);
  }
 }
 void PrintSuccess(cOrganism*,int){}
 void TraceTestCPU(int,int,const cOrganism& o){record(const_cast<cOrganism*>(&o));}
};
struct Rig {
 cAvidaConfig* cfg; cWorld* w; cTestCPU* cpu; cCPUTestInfo ti; Trace* trace;
 Rig(int mode,int cas,const char* file,bool erase=false,int time=10,bool cap=false){
  cUserFeedback fb;cString cwd(Apto::FileSystem::GetCWD());cfg=new cAvidaConfig;
  need(cfg->Load("avida.cfg",cwd,&fb),"config");if(cap)cfg->ENVIRONMENT_FILE.Set("environment-cap.cfg");cfg->RANDOM_SEED.Set(119);cfg->SPECULATIVE.Set(0);
  cfg->ANTICIPATE_MODE.Set(-1);cfg->HISTORY_MODE.Set(mode);cfg->HISTORY_WINDOW.Set(2);cfg->HISTORY_CASE.Set(cas);
  cfg->TEST_CPU_TIME_MOD.Set(time);cfg->VERBOSITY.Set(0);
  w=cWorld::Initialize(cfg,cwd,new World,&fb);need(w!=NULL,"world");
  GenomePtr g=Util::LoadGenomeDetailFile(file,cwd,w->GetHardwareManager(),fb);need(bool(g),"program");
  cpu=w->GetHardwareManager().CreateTestCPU(w->GetDefaultContext());trace=new Trace(erase);
  ti.SetTraceExecution(HardwareTracerPtr(trace));cpu->TestGenome(w->GetDefaultContext(),ti,*g);
 }
 int count(int k){return ti.GetTestPhenotype().GetCurReactionCount()[k];}
 cOrganism* org(){return ti.GetTestOrganism();}
 ~Rig(){delete cpu;} // world outlives test-info's program; process exit reclaims it
};
void specimen(int m,int cs,const char* f,int expected,bool erase=false,bool show=false){
 Rig r(m,cs,f,erase);need(r.count(m)==expected,"specimen count");
 for(int k=0;k<3;++k)if(k!=m)need(r.count(k)==0,"cross-task credit");
 std::cout<<"mode="<<m<<" case="<<cs<<" program="<<f<<" erase="<<erase<<" rewards="<<r.count(m)<<" bonus="<<r.ti.GetTestPhenotype().GetCurBonus()<<" reads="<<r.trace->in.size()<<'\n';
 if(show)std::cout<<"  inputs="<<nums(r.trace->in)<<"\n  outputs="<<nums(r.trace->out)<<'\n';
}
// Linked-library API controls start from a stock ancestor with no IO.
void controls(){
 Rig r(0,0,"default-heads.org",false,1);cOrganism* o=r.org();cAvidaContext& c=r.w->GetDefaultContext();
 int in[6]={1,2,0,2,1,0};int out[6]={0,1,0,0,0,0};
 for(int i=0;i<6;++i){need(o->GetNextInput()==in[i],"order stream");o->DoInput(in[i]);
  if(i==5){o->DoOutput(c,true);need(r.count(0)==0,"division minted payment");}
  o->DoOutput(c,out[i]);need(r.count(0)==(i==5?1:0),"deferred payment");
 }
 o->DoOutput(c,0);o->DoOutput(c,false);o->DoOutput(c,true);need(r.count(0)==1,"replay credit");
 o->ResetInput();need(o->GetNextInput()==1,"reset rewound or skipped");o->DoInput(1);o->DoOutput(c,0);
 need(o->GetNextInput()==2,"guard B");o->DoInput(2);o->DoOutput(c,0);o->DoOutput(c,1);
 for(int i=2;i<6;++i){int x=o->GetNextInput();o->DoInput(x);o->DoOutput(c,0);}
 need(r.count(0)==1,"failed first guess repaired by second");
 std::cout<<"guards deferred=1 division=0 replay=0 repeated_guess=0 reset_continues=1\n";
 // Skip a positive target response; a later read counts silence.
 for(int i=0;i<6;++i){int x=o->GetNextInput();o->DoInput(x);if(i!=1)o->DoOutput(c,0);}
 need(r.count(0)==1,"skipped positive paid");std::cout<<"skip_positive=0\n";
}
void arithmetic(){
 // All deterministic present-event policies reduce to yes/no on terminal B or C.
 for(int m=0;m<3;++m)for(int cs=0;cs<10;++cs)for(int policy=0;policy<16;++policy){
  cHistoryTask h;int len=m==0?3:m==1?5:4;int pay=0;
  for(int i=0;i<2*len;++i){int x=h.Read(m,2,cs);h.Respond((policy>>x)&1);pay+=h.Match(m);}
  need(pay==0,"memoryless mapping paid");
 }
 std::cout<<"all_16_memoryless_event_maps x 3_modes x 10_cases: rewards=0\n";
 for(int w=1;w<=32;++w)for(int cs=0;cs<2;++cs){
  cHistoryTask h;int len=w+3,apos=-1,pay=0;std::vector<int> gaps;
  for(int i=0;i<2*len;++i){int x=h.Read(1,w,cs);if(i%len==0)apos=-1;if(x==1)apos=i;
   int y=0;if(x==2){gaps.push_back(i-apos);y=i-apos<=w;}
   h.Respond(y);pay+=h.Match(1);
  }
  need(pay==1,"interval boundary");need(gaps[cs]==w && gaps[1-cs]==w+1,"gap definition");
 }
 std::cout<<"windows_1_to_32 both_orientations: gap_W=yes gap_W_plus_1=no rewards=1\n";
}
int main(){Avida::Initialize();
 for(int m=0;m<3;++m){const char* f=m==0?"order.org":m==1?"interval.org":"sequence.org";
  for(int cs=0;cs<(m==2?10:2);++cs)specimen(m,cs,f,m==0?7:6,false,cs==0);
  specimen(m,-1,f,m==0?7:6);specimen(m,0,f,0,true);specimen(m,0,"echo.org",0);specimen(m,0,"always.org",0);
 }
 controls();arithmetic();
 // Added after the first run: reset in mid-frame and attempt to lose false-response history.
 {Rig r(0,0,"default-heads.org",false,1);cOrganism* o=r.org();auto& c=r.w->GetDefaultContext();
  need(o->GetNextInput()==1,"midreset A");o->DoInput(1);o->ResetInput();
  need(o->GetNextInput()==2,"midreset rewound");o->DoInput(2);o->DoOutput(c,1);
  int ins[]={0,2,1,0};for(int x:ins){need(o->GetNextInput()==x,"midreset stream");o->DoInput(x);o->DoOutput(c,0);}
  need(r.count(0)==1,"reset lost checker history");std::cout<<"midframe_reset next=B pair_reward=1\n";
  r.cfg->ANTICIPATE_MODE.Set(1);bool threw=false;try{o->GetNextInput();}catch(const std::invalid_argument&){threw=true;}
  need(threw,"mixed modes accepted");std::cout<<"mixed_modes rejected=1\n";
 }
 for(int m=0;m<3;++m){const char* f=m==0?"order.org":m==1?"interval.org":"sequence.org";
  Rig r(m,-1,f,false,10,true);Rig e(m,-1,"echo.org",false,10,true);
  need(r.count(m)==1 && r.ti.GetTestPhenotype().GetCurBonus()==2,"capped stateful");
  need(e.count(m)==0 && e.ti.GetTestPhenotype().GetCurBonus()==1,"capped echo");
  std::cout<<"capped mode="<<m<<" stateful_reward=1 bonus=2 echo_reward=0 bonus=1\n";
 }
std::cout<<"ALL HISTORY EXPECTATIONS MATCHED\n";
}
```

#### history/build.py

<!-- artifact: history/build.py -->
```python
from pathlib import Path
import shlex,subprocess
s=Path('build-patched/avida-core/CMakeFiles/avida.dir/flags.make').read_text()
a=next(x.split('=',1)[1] for x in s.splitlines() if x.startswith('CXX_INCLUDES'))
cmd=['g++','-std=gnu++11','-O0','-DNDEBUG']+shlex.split(a)+['history/check.cc','-Wl,--start-group','build-patched/lib/libavida-core.a','build-patched/lib/libapto.a','build-patched/lib/libtcmalloc-1.4.a','-Wl,--end-group','-lpthread','-o','history/tests/check']
p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
Path('history/build.log').write_text(p.stdout);print('History harness compile exit',p.returncode)
if p.returncode:print(p.stdout[-3000:])
raise SystemExit(p.returncode)
```

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

#### history/test-first.log

<!-- artifact: history/test-first.log -->
```text
mode=0 case=0 program=order.org erase=0 rewards=6 bonus=7 reads=42
  inputs=1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0,1,2,0,2,1,0
  outputs=0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2
mode=0 case=1 program=order.org erase=0 rewards=6 bonus=7 reads=42
mode=0 case=-1 program=order.org erase=0 rewards=6 bonus=7 reads=42
mode=0 case=0 program=order.org erase=1 rewards=0 bonus=1 reads=42
mode=0 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=0 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
mode=1 case=0 program=interval.org erase=0 rewards=6 bonus=7 reads=70
  inputs=0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0,0,1,0,2,0,1,0,0,2,0
  outputs=0,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0,2,0,0,0,1,2,0,1,0,0
mode=1 case=1 program=interval.org erase=0 rewards=6 bonus=7 reads=70
mode=1 case=-1 program=interval.org erase=0 rewards=6 bonus=7 reads=70
mode=1 case=0 program=interval.org erase=1 rewards=0 bonus=1 reads=70
mode=1 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=1 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
mode=2 case=0 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
  inputs=1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1,3,2,0,1,2,3,0,1
  outputs=0,0,2,1,0,0,3,1,0,0,2,1,0,0,3,1,0,0,2,1,0,0,3,1,0,0,2,1,0,0,3,1,0,0,2,1,0,0,3,1,0,0,2,1,0,0,3,1,0,0,2,1,0
mode=2 case=1 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=2 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=3 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=4 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=5 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=6 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=7 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=8 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=9 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=-1 program=sequence.org erase=0 rewards=6 bonus=7 reads=53
mode=2 case=0 program=sequence.org erase=1 rewards=0 bonus=1 reads=53
mode=2 case=0 program=echo.org erase=0 rewards=0 bonus=1 reads=10
mode=2 case=0 program=always.org erase=0 rewards=0 bonus=1 reads=10
guards deferred=1 division=0 replay=0 repeated_guess=0 reset_continues=1
skip_positive=0
all_16_memoryless_event_maps x 3_modes x 10_cases: rewards=0
windows_1_to_32 both_orientations: gap_W=yes gap_W_plus_1=no rewards=1
ALL HISTORY EXPECTATIONS MATCHED
```

END OF REPORT
