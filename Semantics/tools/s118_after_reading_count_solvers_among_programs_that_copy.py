#!/usr/bin/env python3
"""s118_after_reading_count_solvers_among_programs_that_copy.py

What it does, in plain words: a check made AFTER the S118 pilots' results were read (so it is not one of the plan's
tests). The plan's test for the pilot "solve something to replicate, nothing paid" asked for 90 in 100 programs to
perform at least one task, counting every program in the saved program population. About a quarter of the programs in
every execution environment, the control included, are broken copies that cannot copy themselves at all. This check
counts, by Avida's test processor, the share of the programs that CAN copy themselves (judged without the copying
requirement) that also perform at least one of the 77 tasks, at updates 5,000 and 20,000, for both pilots and for
S113's NO TASK REWARDS at 20,000. It also lists which tasks Avida's own count shows in the solve-something pilot at
update 5,250 (just after the requirement was switched on) and at 20,000. Output: s118/posthoc.json in the scratch
space. Avida runs here only in analysis mode, under nice and a timeout. Written 1 October 2026 by the second Opus 5.5
agent of log S118.
"""
import sys, os, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/ThreadSmith/Semantics/tools')
import importlib.util
spec = importlib.util.spec_from_file_location('G', '/home/user/ThreadSmith/Semantics/tools/s118_gather_the_results_fixed.py')
G = importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
tasks = G.ranks(); names=[t for t,_ in tasks]
out = {}
def rep_share(sp):
    pop = G.M113.read_spop(sp); seqs=[s for s,_ in pop]; res=[]
    for i in range(0,len(seqs),G.M113.CHUNK): res += G.M113.evaluate(seqs[i:i+G.M113.CHUNK], len(tasks))
    rep = sum(n for (s,n),(v,t,_) in zip(pop,res) if v)
    rep_task = sum(n for (s,n),(v,t,_) in zip(pop,res) if v and any(t))
    return round(rep_task/rep,4) if rep else None
for s in (1,2,3):
    for p in ('must_solve','any_function'):
        d = os.path.join(G.RUNS, '%s_seed%d'%(p,s))
        out['%s_seed%d'%(p,s)] = {m: rep_share(os.path.join(d,'data','detail-%d.spop'%m)) for m in (5000,20000)}
    d = os.path.join(G.S113RUNS, 'no_rewards_seed%d'%s, 'piece_19','data','detail-1000.spop')
    out['no_rewards_seed%d'%s] = {20000: rep_share(d)}
    t,c = G.avida_count(os.path.join(G.RUNS,'must_solve_seed%d'%s))
    out['must_solve_seed%d_tasks_at_5250'%s] = {names[j]: int(x) for j,x in enumerate(t[5250]) if x>0}
    out['must_solve_seed%d_tasks_at_20000'%s] = {names[j]: int(x) for j,x in enumerate(t[20000]) if x>0}
json.dump(out, open('/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s118/posthoc.json','w'), indent=1)
print(json.dumps(out, indent=0))
