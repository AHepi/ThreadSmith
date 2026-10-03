# NOTE (S115, added by Claude): Astra's generator for the two evaluation-inside-programs experiments (stock Avida, extended heads instruction set). It writes stock_avida_evaluation/ beside itself.
# Copied unchanged from GPT 6 Astra's reply 02 (tests/S115 Returns from GPT 6 Astra/02 Return - evaluation inside the program population.md); only these note lines were added.
from pathlib import Path
root=Path(__file__).resolve().parent/'stock_avida_evaluation'
root.mkdir(exist_ok=False)
instructions=['nop-A','nop-B','nop-C','nop-X','one','zero','send','receive','pose','get-neighbors-reputation','rotate-to-next-occupied-cell','if-equ-0','donate-energy-faced10','repro','inc','dec','add','sub','nand']
mutable=set(instructions[14:])
inst='INSTSET evaluator:hw_type=0\n'+'\n'.join(f'INST {x}:redundancy={int(x in mutable)}:cost=1:energy_cost=0' for x in instructions)+'\n'
common='''VERSION_ID 2.14.0
RANDOM_SEED 101
SPECULATIVE 0
#include INST_SET=instset.cfg
INST_SET -
INST_SET_LOAD_LEGACY 0
ENVIRONMENT_FILE environment.cfg
EVENT_FILE events.cfg
ANALYZE_FILE analyze.cfg
DATA_DIR data
MUT_RATE_SOURCE 1
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
COPY_UNIFORM_PROB 0
COPY_SLIP_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIV_UNIFORM_PROB 0
DIV_SLIP_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0
DIVIDE_DEL_PROB 0
DIVIDE_UNIFORM_PROB 0
DIVIDE_SLIP_PROB 0
PARENT_MUT_PROB 0
PARENT_INS_PROB 0
PARENT_DEL_PROB 0
POINT_MUT_PROB 0
POINT_INS_PROB 0
POINT_DEL_PROB 0
INJECT_MUT_PROB 0
INJECT_INS_PROB 0
INJECT_DEL_PROB 0
META_COPY_MUT 0
INST_POINT_MUT_PROB 0
NO_MUT_INSTS abcdefghijklmn
DIVIDE_METHOD 1
MIN_EXE_LINES 0.5
MIN_COPIED_LINES 0.5
DEATH_METHOD 0
PREFER_EMPTY 0
REPRO_METHOD 1
ENERGY_ENABLED 1
ENERGY_GIVEN_ON_INJECT 1000
ENERGY_GIVEN_AT_BIRTH 1000
FRAC_PARENT_ENERGY_GIVEN_TO_ORG_AT_BIRTH 0
FRAC_PARENT_ENERGY_GIVEN_TO_DEME_AT_BIRTH 0
FRAC_ENERGY_DECAY_AT_ORG_BIRTH 0.5
FRAC_ENERGY_TRANSFER 0
NUM_CYCLES_EXC_BEFORE_0_ENERGY 1000
ENERGY_CAP -1
FIX_METABOLIC_RATE -1
ENERGY_SHARING_METHOD 1
ENERGY_SHARING_UPDATE_METABOLIC 1
RESOURCE_SHARING_LOSS 0
AUTO_REPUTATION 0
INHERIT_REPUTATION 0
INHERIT_OPINION 0
OPINION_BUFFER_SIZE 1
'''
# Four prefix executions, five mutable arithmetic executions, four idle executions,
# then branch/action. nop-B on the direct sensor is consumed by that instruction.
for mechanism in ('scalar','reputation'):
    base=root/mechanism
    base.mkdir(exist_ok=True)
    prefix=['one','send','nop-X','receive'] if mechanism=='scalar' else ['one','pose','nop-X','get-neighbors-reputation','nop-B']
    sequence=prefix+['inc','dec','inc','dec','dec']+['nop-X']*4+['if-equ-0','donate-energy-faced10']+['nop-X']*24+['repro']
    ancestor='#inst_set evaluator\n'+'\n'.join(sequence)+'\n'
    for mode in ('evolution','assay','shuffle','off'):
        d=base/mode; d.mkdir(exist_ok=True)
        (d/'instset.cfg').write_text(inst)
        (d/'ancestor.org').write_text(ancestor)
        (d/'environment.cfg').write_text('# No tasks, reactions, or task rewards. Energy supplied at injection and birth.\n')
        (d/'analyze.cfg').write_text('# Intentionally empty; run in normal simulation mode.\n')
        cfg=common
        if mode=='evolution':
            cfg+='WORLD_X 60\nWORLD_Y 60\nWORLD_GEOMETRY 2\nNUM_DEMES 1\nBIRTH_METHOD 0\nSLICING_METHOD 2\nAVE_TIME_SLICE 30\n'
            events='''u begin InjectAll filename=ancestor.org
u 0:100:end PrintAverageData
u 0:100:end PrintCountData
u 0:100:end PrintDemeEnergySharingStats
u 0:1000:end SavePopulation filename=detail
u 0:1000:end DumpEnergyGrid
u 5000 Exit
'''
        else:
            cfg=cfg.replace('COPY_MUT_PROB 0.0075','COPY_MUT_PROB 0')
            if mode=='off': cfg=cfg.replace('ENERGY_SHARING_METHOD 1','ENERGY_SHARING_METHOD 0')
            cfg+='WORLD_X 2\nWORLD_Y 2\nWORLD_GEOMETRY 3\nNUM_DEMES 2\nBIRTH_METHOD 12\nSLICING_METHOD 0\nAVE_TIME_SLICE 1\n'
            for cue in (0,1,2):
                if mechanism=='scalar':
                    tx=['zero' if cue==0 else 'one','nop-X','send'] if cue<2 else ['one','inc','send']
                else:
                    tx=['nop-X','pose' if cue else 'nop-X','pose' if cue==2 else 'nop-X']
                tx+=['nop-X']*60+['repro']
                (d/f'candidate{cue}.org').write_text('#inst_set evaluator\n'+'\n'.join(tx)+'\n')
            events='''u begin Inject ancestor.org 0 -1 10 0 evaluator0.trace
u begin Inject candidate1.org 1 -1 21 0 candidate1.trace
u begin Inject ancestor.org 2 -1 10 0 evaluator2.trace
u begin Inject candidate0.org 3 -1 20 0 candidate0.trace
u 12 DumpEnergyGrid energy_before.dat
u 12 DumpIDGrid ids_before.dat
'''
            if mode=='shuffle': events+='u 12 SwapCells 1 3\n'
            events+='''u 17 DumpEnergyGrid energy_after.dat
u 17 DumpIDGrid ids_after.dat
u 17 PrintDemeEnergySharingStats
u 17 SavePopulation filename=assay
u 17 Exit
'''
        (d/'avida.cfg').write_text(cfg)
        (d/'events.cfg').write_text(events)

(root/'prepare_bank.py').write_text(r'''#!/usr/bin/env python3
"""Make fresh, matched stock-Avida assays of every living sequence in a snapshot.
Usage: python prepare_bank.py SNAPSHOT SCALAR_OR_REPUTATION OUTPUT_DIR [PERMUTATION_SEED]
No fitness-based selection. Census counts are preserved as analysis weights.
"""
from pathlib import Path
import csv
import json
import random
import shutil
import sys

snapshot, mechanism, output = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
assert mechanism in ('scalar', 'reputation')
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 701
source = Path(__file__).resolve().parent / mechanism
header = None
records = []
for line in snapshot.read_text().splitlines():
    if line.startswith('#format '):
        header = line.split()[1:]
    elif line.strip() and not line.startswith('#'):
        assert header is not None, 'Missing #format header'
        values = line.split()
        assert len(values) > header.index('num_units'), 'Missing population count'
        row = dict(zip(header, values))
        if int(row['num_units']) > 0:
            assert len(values) == len(header), 'Unexpected living-record fields'
            assert row['hw_type'] == '0' and row['inst_set'] == 'evaluator'
            records.append(row)
assert records, 'No living sequences found'
records.sort(key=lambda x: x['sequence'])
assert len({r['sequence'] for r in records}) == len(records), 'Duplicate sequence records; combine counts explicitly'
mnemonics = [s.split()[1].split(':')[0] for s in (source/'assay'/'instset.cfg').read_text().splitlines() if s.startswith('INST ')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
assert len(mnemonics) <= len(alphabet)
decode = dict(zip(alphabet, mnemonics))
reference = [s for s in (source/'assay'/'ancestor.org').read_text().splitlines() if s and not s.startswith('#')]
core_start = 4 if mechanism == 'scalar' else 5
mutable = {'inc', 'dec', 'add', 'sub', 'nand'}
for row in records:
    row['instructions'] = [decode[c] for c in row['sequence']]
    assert len(row['instructions']) == len(reference), 'Genome length changed'
    for i, (actual, expected) in enumerate(zip(row['instructions'], reference)):
        assert actual in mutable if core_start <= i < core_start+5 else actual == expected, 'Protected scaffold changed'

# Cases fixed before reading any outcomes. Every sequence receives every pair.
# For each pair, identity and swap are both run: this is the exact finite
# distribution of all recipient permutations for a two-recipient panel.
pairs = [(0, 1), (0, 2), (1, 2)]
panels = [(row, pair, side) for row in records for pair in pairs for side in (0, 1)]
# Paired complementary permutations preserve equal identity/swap coverage, while
# a predeclared seed determines which duplicate panel gets which permutation.
rng = random.Random(seed)
flips = {(row['id'], pair): rng.randrange(2) for row in records for pair in pairs}
output.mkdir(parents=True, exist_ok=True)
metadata=[]
for i,(row,pair,side) in enumerate(panels):
    start=4*i
    metadata.append(dict(panel=i, sequence=row['sequence'], id=row['id'], weight=int(row['num_units']),
                         cue_left=pair[0], cue_right=pair[1], evaluator_left=start,
                         candidate_left=start+1, evaluator_right=start+2, candidate_right=start+3,
                         swap=(side ^ flips[(row['id'], pair)])))
(output/'panels.json').write_text(json.dumps(metadata, indent=2)+'\n')
(output/'provenance.json').write_text(json.dumps(dict(snapshot=str(snapshot.resolve()), mechanism=mechanism,
    permutation_seed=seed, frozen_weights='num_units at snapshot', programs=len(records),
    panel_pairs=pairs, fresh_initialization=True), indent=2)+'\n')
for arm in ('active','shuffled','off'):
    d=output/arm
    d.mkdir(exist_ok=True)
    for filename in ('instset.cfg','environment.cfg','analyze.cfg','candidate0.org','candidate1.org','candidate2.org'):
        shutil.copyfile(source/'assay'/filename,d/filename)
    config=(source/('off' if arm=='off' else 'assay')/'avida.cfg').read_text()
    config=config.replace('WORLD_Y 2\n', f'WORLD_Y {2*len(panels)}\n')
    config=config.replace('NUM_DEMES 2\n', f'NUM_DEMES {2*len(panels)}\n')
    (d/'avida.cfg').write_text(config)
    events=[]
    for row in records:
        (d/f"evaluator_{row['id']}.org").write_text('#inst_set evaluator\n'+'\n'.join(row['instructions'])+'\n')
    for meta in metadata:
        for label in ('left','right'):
            events.append(f"u begin Inject evaluator_{meta['id']}.org {meta['evaluator_'+label]} -1 10")
            events.append(f"u begin Inject candidate{meta['cue_'+label]}.org {meta['candidate_'+label]} -1 {20+meta['cue_'+label]}")
    events+=['u 12 DumpEnergyGrid energy_before.dat','u 12 DumpIDGrid ids_before.dat']
    if arm=='shuffled':
        events += [f"u 12 SwapCells {m['candidate_left']} {m['candidate_right']}" for m in metadata if m['swap']]
    events+=['u 17 DumpEnergyGrid energy_after.dat','u 17 DumpIDGrid ids_after.dat',
             'u 17 PrintDemeEnergySharingStats','u 17 Exit']
    (d/'events.cfg').write_text('\n'.join(events)+'\n')
print(f'Prepared {len(records)} sequences, {len(panels)} panels, 3 arms in {output}')
''')

(root/'summarize_bank.py').write_text(r'''#!/usr/bin/env python3
"""Read prepared bank results and emit per-sequence, per-pair decision contrasts.
Usage: python summarize_bank.py BANK_DIR
No Avida runs are started by this script.
"""
from pathlib import Path
from collections import defaultdict
import csv
import json
import sys
root=Path(sys.argv[1])
metadata=json.loads((root/'panels.json').read_text())
def grid(path, cast=float):
    return [cast(x) for x in path.read_text().split()]
rows=[]
for arm in ('active','shuffled','off'):
    d=root/arm/'data'
    before=grid(d/'energy_before.dat')
    after=grid(d/'energy_after.dat')
    ids0=grid(d/'ids_before.dat',int)
    ids1=grid(d/'ids_after.dat',int)
    assert len(ids1)==len(set(ids1)), 'Missing or duplicated program identity'
    current={x:i for i,x in enumerate(ids1)}
    assert set(ids0)==set(ids1), 'Program identities changed during assay'
    for meta in metadata:
        gain={}
        donor_loss=0
        for side in ('left','right'):
            loc=meta['candidate_'+side]
            gain[side]=after[current[ids0[loc]]]-before[loc]
            eloc=meta['evaluator_'+side]
            donor_loss+=before[eloc]-after[current[ids0[eloc]]]
        assert abs(sum(gain.values())-donor_loss)<1e-8, 'Unmatched transfers'
        assert all(min(abs(v),abs(v-10))<1e-8 for v in gain.values()), 'Unexpected transfer amount'
        rows.append(dict(arm=arm, genotype_id=meta['id'], sequence=meta['sequence'],
            weight=meta['weight'], panel=meta['panel'], cue_left=meta['cue_left'],
            cue_right=meta['cue_right'], grant_left=gain['left'], grant_right=gain['right'],
            contrast=gain['right']-gain['left']))
with (root/'panels.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
groups=defaultdict(list)
for row in rows:
    groups[(row['arm'],row['genotype_id'],row['cue_left'],row['cue_right'])].append(row)
summary=[]
for (arm,genotype_id,left,right),members in sorted(groups.items()):
    assert len(members)==2
    summary.append(dict(arm=arm,genotype_id=genotype_id,weight=members[0]['weight'],
        cue_left=left,cue_right=right,grant_left=sum(r['grant_left'] for r in members)/2,
        grant_right=sum(r['grant_right'] for r in members)/2,
        contrast=sum(r['contrast'] for r in members)/2))
for row in summary:
    if row['arm'] in ('shuffled','off'):
        assert abs(row['contrast'])<1e-8, 'Recipient-permutation/off control has a cue-dependent contrast'
with (root/'contrasts.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(summary[0]));writer.writeheader();writer.writerows(summary)
aggregate=defaultdict(list)
for row in summary:
    aggregate[(row['arm'],row['cue_left'],row['cue_right'])].append(row)
weighted=[]
for (arm,left,right),members in sorted(aggregate.items()):
    total=sum(r['weight'] for r in members)
    weighted.append(dict(arm=arm,cue_left=left,cue_right=right,census_weight=total,
        grant_left=sum(r['weight']*r['grant_left'] for r in members)/total,
        grant_right=sum(r['weight']*r['grant_right'] for r in members)/total,
        contrast=sum(r['weight']*r['contrast'] for r in members)/total))
with (root/'weighted_contrasts.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(weighted[0]));writer.writeheader();writer.writerows(weighted)
print(f'Read {len(rows)} panels; wrote panels.csv, contrasts.csv, weighted_contrasts.csv.')
''')

(root/'run_suite.py').write_text(r'''#!/usr/bin/env python3
"""Run the proposed continuous evolution and matched stock-Avida bank assays.
Usage: python run_suite.py --avida /absolute/path/to/avida --output results
Defaults: 2 mechanisms, seeds 101/102/103, 5000 updates, at most 3 processes.
This file is supplied for future execution; preparing it starts no runs.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
import re
import shutil
import subprocess
import sys
import time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--avida',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
parser.add_argument('--updates',type=int,default=5000)
parser.add_argument('--seeds',type=int,nargs='+',default=[101,102,103])
parser.add_argument('--processes',type=int,choices=[1,2,3],default=3)
args=parser.parse_args()
assert args.updates >= 1000 and args.updates % 1000 == 0
avida=args.avida.resolve();out=args.output.resolve()
assert avida.is_file()
assert not out.exists(), 'Use a new output directory; preserve previous results'
out.mkdir(parents=True)
source=Path(__file__).resolve().parent
jobs=[]
for mechanism in ('scalar','reputation'):
    template=source/mechanism/'evolution'
    for seed in args.seeds:
        d=out/mechanism/f'seed-{seed}'/'evolution';d.mkdir(parents=True)
        for filename in ('avida.cfg','events.cfg','environment.cfg','instset.cfg','ancestor.org','analyze.cfg'):
            shutil.copyfile(template/filename,d/filename)
        config=(d/'avida.cfg').read_text().replace('RANDOM_SEED 101\n',f'RANDOM_SEED {seed}\n')
        (d/'avida.cfg').write_text(config)
        events=(d/'events.cfg').read_text().replace('u 5000 Exit',f'u {args.updates} Exit')
        (d/'events.cfg').write_text(events)
        jobs.append((mechanism,seed,d))

# Each timing wrapper has exactly one Avida child. This avoids mixing CPU
# measurements from concurrently running children of the threaded runner.
timed_driver = """
import json, resource, subprocess, sys
from pathlib import Path
p = subprocess.run(sys.argv[1:])
u = resource.getrusage(resource.RUSAGE_CHILDREN)
Path('cpu_time.json').write_text(json.dumps(dict(exit_code=p.returncode,
    user_seconds=u.ru_utime, system_seconds=u.ru_stime,
    cpu_seconds=u.ru_utime+u.ru_stime)))
raise SystemExit(p.returncode)
"""

def run(d):
    t=time.monotonic()
    with (d/'run.log').open('w') as logfile:
        completed=subprocess.run([sys.executable,'-c',timed_driver,str(avida),'-c','avida.cfg'],cwd=d,stdout=logfile,stderr=subprocess.STDOUT)
    logfile_text=(d/'run.log').read_text()
    log_errors=re.findall(r'(?im)^error:.*$',logfile_text)
    status=re.findall(r'UD:\s*(\d+).*?Orgs:\s*(\d+)',logfile_text)
    requested=int(re.findall(r'^u (\d+) Exit$',(d/'events.cfg').read_text(),re.M)[-1])
    reached=int(status[-1][0]) if status else None
    living=int(status[-1][1]) if status else 0
    cpu=json.loads((d/'cpu_time.json').read_text()) if (d/'cpu_time.json').exists() else {}
    result=dict(directory=str(d),exit_code=completed.returncode,wall_seconds=time.monotonic()-t,cpu=cpu,
                requested_update=requested,final_update=reached,living_programs=living,log_errors=log_errors)
    (d/'run_status.json').write_text(json.dumps(result,indent=2)+'\n')
    if completed.returncode or log_errors or reached != requested or living == 0:
        raise RuntimeError(f'Avida did not satisfy completion checks (exit {completed.returncode}); see {d / "run.log"} and run_status.json')
    return result

# Dependencies are sequential: evolution, snapshot preparation, then fresh assays.
with ThreadPoolExecutor(max_workers=args.processes) as pool:
    evolution_results=list(pool.map(run,[d for _,_,d in jobs]))
assay_jobs=[]
for mechanism,seed,d in jobs:
    for update in sorted({1000,args.updates}):
        snapshot=d/'data'/f'detail-{update}.spop'
        assert snapshot.is_file(),f'Expected stock snapshot missing: {snapshot}'
        bank=d.parent/f'bank-{update}'
        subprocess.run([sys.executable,str(source/'prepare_bank.py'),str(snapshot),mechanism,str(bank),'701'],check=True)
        assay_jobs += [bank/arm for arm in ('active','shuffled','off')]
with ThreadPoolExecutor(max_workers=args.processes) as pool:
    assay_results=list(pool.map(run,assay_jobs))
for mechanism,seed,d in jobs:
    for update in sorted({1000,args.updates}):
        subprocess.run([sys.executable,str(source/'summarize_bank.py'),str(d.parent/f'bank-{update}')],check=True)
(out/'runs.json').write_text(json.dumps(dict(evolution=evolution_results,assays=assay_results),indent=2)+'\n')
print(f'Finished {len(evolution_results)} evolution runs and {len(assay_results)} bank assays. Results: {out}')
''')

minimal = {
    'scalar': ['one','send','receive','dec','if-equ-0','donate-energy-faced10','nop-X','repro'],
    'reputation': ['one','pose','get-neighbors-reputation','nop-B','dec','if-equ-0','donate-energy-faced10','repro']
}
for mechanism, instructions in minimal.items():
    (root / mechanism / 'minimal.org').write_text('#inst_set evaluator\n' + '\n'.join(instructions) + '\n')
import hashlib, json
manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}
(root/'files.sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(root)
