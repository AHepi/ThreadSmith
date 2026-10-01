// Plain note (log S122, reply 02; written by Claude, Opus 5.5, 1 October 2026).
// A small probe linked against the PATCHED Avida library of Astra's reply 02 (history tasks).
// It is not part of the reply; it is Claude's own check. It runs Avida programs in Avida's test
// processor (no replication happens on the real machine) and prints, for each IO, the event read
// and the number output just before that read. Commands:
//   probe run MODE CASE FILE [TIME_MOD] [SEED]  - HISTORY_MODE=MODE, HISTORY_CASE=CASE: rewards, reads, trace
//   probe stock FILE EVENTS [TIME_MOD]          - history off; the test processor hands in EVENTS
//                                                 (comma list, repeated) through Avida's stock input path
//   probe positions                             - every "respond at these frame positions" rule, ignoring
//                                                 what the events are, scored by the patch's own checker
//                                                 (cHistoryTask) on random pairs
//   probe cycles MODE FILE CYCLES [SEED]       - history on, random pairs: the SAME program runs through
//                                                 CYCLES copy cycles one after another, as a parent does in a
//                                                 world (its stream is not rewound at division; its processor
//                                                 restarts); prints the reads and the pairs paid in each cycle
//   probe pairclock                             - the same, but a rule may answer the two frames of a
//                                                 pair differently (it counts reads up to a whole pair)
// Run it from a folder holding avida.cfg, instset-heads.cfg, environment.cfg and events.cfg.
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
#include "cPhenotype.h"
#include "cTestCPUInterface.h"
#include <cstdlib>
#include <iostream>
#include <random>
#include <sstream>
#include <stdexcept>
#include <vector>
using namespace Avida;

static void need(bool b, const char* s) { if (!b) throw std::runtime_error(s); }
static std::string nums(const std::vector<int>& v) {
  std::ostringstream s; for (size_t i = 0; i < v.size(); ++i) { if (i) s << ','; s << v[i]; } return s.str();
}

// Same recording rule as the reply's history/check.cc: at each IO, the number output (the
// register IO is about to output) and the event that IO then reads.
class Trace : public cHardwareTracer {
  bool pending; int before;
public:
  std::vector<int> in, out;
  Trace() : pending(false), before(0) {}
  void record(cOrganism* o) { if (pending) { in.push_back(o->GetInputBuf()[0]); out.push_back(before); } pending = false; }
  void TraceHardware(cAvidaContext&, cHardwareBase& b, bool, bool, int) {
    cHardwareCPU& c = dynamic_cast<cHardwareCPU&>(b); record(c.GetOrganism());
    pending = c.GetInstSet().GetName(c.IP().GetInst()) == "IO";
    if (pending) {
      cHeadCPU n = c.IP(); n.Advance(); cString name = c.GetInstSet().GetName(n.GetInst());
      int r = name == "nop-A" ? 0 : name == "nop-C" ? 2 : 1;
      before = c.GetRegister(r);
    }
  }
  void PrintSuccess(cOrganism*, int) {}
  void TraceTestCPU(int, int, const cOrganism& o) { record(const_cast<cOrganism*>(&o)); }
};

struct Rig {
  cAvidaConfig* cfg; cWorld* w; cTestCPU* cpu; cCPUTestInfo ti; Trace* trace;
  Rig(int mode, int cas, const char* file, int time, int seed, const std::vector<int>* manual) {
    cUserFeedback fb; cString cwd(Apto::FileSystem::GetCWD()); cfg = new cAvidaConfig;
    need(cfg->Load("avida.cfg", cwd, &fb), "config");
    cfg->RANDOM_SEED.Set(seed); cfg->SPECULATIVE.Set(0);
    cfg->ANTICIPATE_MODE.Set(-1); cfg->HISTORY_MODE.Set(mode); cfg->HISTORY_WINDOW.Set(2); cfg->HISTORY_CASE.Set(cas);
    cfg->TEST_CPU_TIME_MOD.Set(time); cfg->VERBOSITY.Set(0);
    w = cWorld::Initialize(cfg, cwd, new World, &fb); need(w != NULL, "world");
    GenomePtr g = Util::LoadGenomeDetailFile(file, cwd, w->GetHardwareManager(), fb); need(bool(g), "program");
    cpu = w->GetHardwareManager().CreateTestCPU(w->GetDefaultContext()); trace = new Trace;
    if (manual) { Apto::Array<int> a(manual->size()); for (size_t i = 0; i < manual->size(); ++i) a[i] = (*manual)[i]; ti.UseManualInputs(a); }
    ti.SetTraceExecution(HardwareTracerPtr(trace)); cpu->TestGenome(w->GetDefaultContext(), ti, *g);
  }
  // A copy that divides moves its counts to the "last" fields (cPhenotype::TestDivideReset), so a
  // pair paid before the division is counted there; both are added.
  int count(int k) {
    const cPhenotype& p = ti.GetTestPhenotype();
    return p.GetCurReactionCount()[k] + (p.GetNumDivides() > 0 ? p.GetLastReactionCount()[k] : 0);
  }
};

int main(int argc, char** argv) {
  Avida::Initialize();
  need(argc >= 2, "usage: probe run|stock|positions ...");
  std::string cmd = argv[1];
  if (cmd == "run") {
    need(argc >= 5, "probe run MODE CASE FILE [TIME_MOD] [SEED]");
    int mode = atoi(argv[2]), cas = atoi(argv[3]);
    int time = argc > 5 ? atoi(argv[5]) : 10, seed = argc > 6 ? atoi(argv[6]) : 119;
    Rig r(mode, cas, argv[4], time, seed, NULL);
    std::cout << "mode=" << mode << " case=" << cas << " program=" << argv[4] << " time_mod=" << time << " seed=" << seed
              << " rewards=" << r.count(mode) << " bonus=" << r.ti.GetTestPhenotype().GetCurBonus()
              << " reads=" << r.trace->in.size() << " divided=" << (r.ti.GetTestPhenotype().GetGestationTime() > 0 ? 1 : 0) << "\n";
    std::cout << "  inputs=" << nums(r.trace->in) << "\n  outputs=" << nums(r.trace->out) << "\n";
  } else if (cmd == "stock") {
    need(argc >= 4, "probe stock FILE EVENTS [TIME_MOD]");
    std::vector<int> ev; std::stringstream ss(argv[3]); std::string tok;
    while (std::getline(ss, tok, ',')) ev.push_back(atoi(tok.c_str()));
    int time = argc > 4 ? atoi(argv[4]) : 10;
    Rig r(-1, -1, argv[2], time, 119, &ev);
    std::cout << "reads=" << r.trace->in.size() << "\n  inputs=" << nums(r.trace->in) << "\n  outputs=" << nums(r.trace->out) << "\n";
  } else if (cmd == "positions") {
    // A rule here never looks at an event: it outputs 1 after the reads at the chosen positions of
    // each frame and 0 after every other read, then answers the final X of each pair explicitly.
    std::mt19937 rng(119);
    for (int m = 0; m < 3; ++m) {
      const int len = m == 0 ? 3 : m == 1 ? 5 : 4, pairs = 10000;
      int best_mask = -1; double best = -1; int paying_rules = 0;
      for (int mask = 0; mask < (1 << len); ++mask) {
        cHistoryTask h; int paid = 0;
        for (int p = 0; p < pairs; ++p) {
          int choice = int(rng() % 10);
          for (int i = 0; i < 2 * len; ++i) {
            h.Read(m, 2, choice);
            h.Respond((mask >> i % len) & 1);
            paid += h.Match(m);
          }
        }
        double frac = double(paid) / pairs;
        if (paid) ++paying_rules;
        if (frac > best) { best = frac; best_mask = mask; }
      }
      std::cout << "mode=" << m << " frame_length=" << len << " rules=" << (1 << len) << " rules_that_ever_pay=" << paying_rules
                << " best_rule_positions=";
      bool first = true; for (int i = 0; i < len; ++i) if ((best_mask >> i) & 1) { std::cout << (first ? "" : "+") << i; first = false; }
      std::cout << " best_rule_pairs_paid=" << best << "\n";
    }
  } else if (cmd == "cycles") {
    need(argc >= 5, "probe cycles MODE FILE CYCLES [SEED]");
    int mode = atoi(argv[2]), cycles = atoi(argv[4]), seed = argc > 5 ? atoi(argv[5]) : 119;
    cUserFeedback fb; cString cwd(Apto::FileSystem::GetCWD()); cAvidaConfig* cfg = new cAvidaConfig;
    need(cfg->Load("avida.cfg", cwd, &fb), "config");
    cfg->RANDOM_SEED.Set(seed); cfg->SPECULATIVE.Set(0); cfg->VERBOSITY.Set(0);
    cfg->ANTICIPATE_MODE.Set(-1); cfg->HISTORY_MODE.Set(mode); cfg->HISTORY_WINDOW.Set(2); cfg->HISTORY_CASE.Set(-1);
    cWorld* w = cWorld::Initialize(cfg, cwd, new World, &fb); need(w != NULL, "world");
    cAvidaContext& ctx = w->GetDefaultContext();
    GenomePtr g = Util::LoadGenomeDetailFile(argv[3], cwd, w->GetHardwareManager(), fb); need(bool(g), "program");
    cTestCPU* cpu = w->GetHardwareManager().CreateTestCPU(ctx); cCPUTestInfo ti;
    cOrganism* org = new cOrganism(w, ctx, *g, -1, Systematics::Source(Systematics::DIVISION, "", true));
    org->SetOrgInterface(ctx, new cTestCPUInterface(cpu, ti, 0));
    ConstInstructionSequencePtr seq; seq.DynamicCastFrom(g->Representation());
    org->GetPhenotype().SetupInject(*seq);
    Trace* trace = new Trace; org->GetHardware().SetTrace(HardwareTracerPtr(trace));
    cHardwareCPU& hw = dynamic_cast<cHardwareCPU&>(org->GetHardware());
    const int limit = 50 * seq->GetSize();
    int paid_cycles = 0, done = 0, paid_total = 0;
    std::cout << "mode=" << mode << " program=" << argv[3] << " seed=" << seed << " cycles:";
    for (int c = 0; c < cycles; ++c) {
      // Counts start at zero each copy cycle; at division they move to the "last" fields.
      size_t reads0 = trace->in.size(); int steps = 0; bool divided = false;
      const int divides0 = org->GetPhenotype().GetNumDivides();
      while (steps < limit && !org->IsDead()) {
        hw.SingleProcess(ctx); ++steps;
        if (org->GetPhenotype().GetNumDivides() > divides0) { divided = true; break; }
      }
      if (!divided) break;
      int got = org->GetPhenotype().GetLastReactionCount()[mode];
      if (got > 0) ++paid_cycles;
      paid_total += got;
      ++done;
      std::cout << " [" << (trace->in.size() - reads0) << " reads, " << got << " paid]";
    }
    const int pair_len = 2 * (mode == 0 ? 3 : mode == 1 ? 5 : 4);
    const int pairs = int(trace->in.size()) / pair_len;
    std::cout << "\n  inputs=" << nums(trace->in) << "\n  outputs=" << nums(trace->out);
    std::cout << "\n  copy_cycles=" << done << " cycles_with_a_paid_pair=" << paid_cycles
              << " reads=" << trace->in.size() << " pairs_completed=" << pairs << " pairs_paid=" << paid_total << "\n";
  } else if (cmd == "pairclock") {
    // Like "positions", but the rule may differ between the first and the second frame of a pair:
    // it outputs 1 after the reads at the chosen positions of the whole pair (2 x frame length
    // reads) and 0 after every other read. It still never looks at an event; it only counts reads.
    std::mt19937 rng(119);
    for (int m = 0; m < 3; ++m) {
      const int len = m == 0 ? 3 : m == 1 ? 5 : 4, pairs = 10000;
      int best_mask = -1; double best = -1; int paying_rules = 0;
      for (int mask = 0; mask < (1 << (2 * len)); ++mask) {
        cHistoryTask h; int paid = 0;
        for (int p = 0; p < pairs; ++p) {
          int choice = int(rng() % 10);
          for (int i = 0; i < 2 * len; ++i) {
            h.Read(m, 2, choice);
            h.Respond((mask >> i) & 1);
            paid += h.Match(m);
          }
        }
        double frac = double(paid) / pairs;
        if (paid) ++paying_rules;
        if (frac > best) { best = frac; best_mask = mask; }
      }
      std::cout << "mode=" << m << " pair_length=" << 2 * len << " rules=" << (1 << (2 * len)) << " rules_that_ever_pay=" << paying_rules
                << " best_rule_pair_positions=";
      bool first = true; for (int i = 0; i < 2 * len; ++i) if ((best_mask >> i) & 1) { std::cout << (first ? "" : "+") << i; first = false; }
      std::cout << " best_rule_pairs_paid=" << best << "\n";
    }
  } else throw std::runtime_error("unknown command");
  return 0;
}
