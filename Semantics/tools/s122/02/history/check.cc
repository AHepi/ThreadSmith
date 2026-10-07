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
