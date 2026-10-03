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
