# NOTE (added by Claude, log S115): this file is 'map_lineage.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Run stock lineage recalculation and null maps using a generated suite.
Only one continuous, checked asexual path from ancestry-helper.py is accepted.
Outputs do not determine instruction homology. --graded supplies a separate
nine-task-reward reference assay for fitness complexity, keeping task indices.
"""
import argparse, csv, json, re, subprocess
from pathlib import Path

def rows(p):
    with open(p,newline='') as f: return list(csv.DictReader(f,delimiter='\t'))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--suite',type=Path,required=True)
    p.add_argument('--lineage',type=Path,required=True)
    p.add_argument('--target',type=int,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--graded',action='store_true')
    p.add_argument('--run',action='store_true')
    a=p.parse_args();suite=a.suite.resolve();lineage=a.lineage.resolve();out=a.out.resolve()
    if any(re.search(r'\s|[#$]',str(x)) for x in (suite,lineage,out)):
        p.error('Use paths without spaces, # or $')
    if not lineage.is_file():p.error('Missing lineage')
    out.mkdir(parents=True,exist_ok=False);(out/'data').mkdir()
    tasks=[r for r in rows(suite/'tasks.tsv') if r['profile']=='core']
    inputs=[r for r in rows(suite/'inputs.tsv') if r['profile']=='core']
    tasks.sort(key=lambda r:int(r['task_index']))
    fields='viable fitness gest_time env_input.0 env_input.1 env_input.2 '+ ' '.join('task.'+r['task_index'] for r in tasks)
    text=(suite/'core/environment.cfg').read_text()
    if a.graded:
        power=dict(not_=1,nand=1,and_=2,orn=2,or_=3,andn=3,nor=4,xor=4,equ=5)
        power={k.rstrip('_'):v for k,v in power.items()}
        for r in tasks:
            if r['name'] in power:
                old=f"REACTION P{int(r['task_index']):03d} {r['name']} process:value=0:type=pow"
                new=old.replace('value=0:',f"value={power[r['name']]}:")
                if text.count(old)!=1: raise ValueError('Reference reaction not unique')
                text=text.replace(old,new)
    (out/'environment.cfg').write_text(text)
    lines=['PURGE_BATCH',f'LOAD {lineage}',f'FIND_LINEAGE {a.target}','NAME_BATCH reuse']
    first=inputs[0];triple=' '.join(first[f'input{j}'] for j in range(3))
    lines += ['RECALCULATE 0 -1 0 '+triple,'ALIGN',
              'DETAIL lineage-sequences.dat id parent_id depth update_born sequence alignment']
    manifest=[]
    for r in inputs:
        directory=out/'data'/('I'+r['input_id']);directory.mkdir()
        triple=' '.join(r[f'input{j}'] for j in range(3))
        lines.append(f'MAP_TASKS {directory}/ text use_manual_inputs {triple} {fields}')
        manifest.append({**{k:v for k,v in r.items() if k!='profile'},'directory':str(directory)})
    lines+=['FILTER depth > 0','DETAIL lineage-edges.dat id parent_id depth update_born parent_dist parent_muts']
    (out/'analyze.cfg').write_text('\n'.join(lines)+'\n')
    with (out/'maps.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,list(manifest[0]),delimiter='\t');w.writeheader();w.writerows(manifest)
    command=next(r for r in json.loads((suite/'commands.json').read_text()) if r['profile']=='core')
    cmd=list(command['command'])
    for key,val in [('ANALYZE_FILE',out/'analyze.cfg'),('ENVIRONMENT_FILE',out/'environment.cfg'),('DATA_DIR',out/'data')]:
        indexes=[i for i,t in enumerate(cmd) if t==key and i and cmd[i-1]=='-set']
        if len(indexes)!=1: raise ValueError('Ambiguous original command')
        cmd[indexes[0]+1]=str(val)
    (out/'command.json').write_text(json.dumps(dict(cwd=command['cwd'],command=cmd,graded=a.graded),indent=2)+'\n')
    (out/'task_indices.txt').write_text(' '.join(r['task_index'] for r in tasks)+'\n')
    if a.run:
        with (out/'run.log').open('w') as log:
            r=subprocess.run(cmd,cwd=command['cwd'],stdout=log,stderr=subprocess.STDOUT)
        if r.returncode: raise SystemExit(f'Avida exited {r.returncode}; retain run.log')
    print(out)

if __name__=='__main__':main()
