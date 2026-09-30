# NOTE (added by Claude, log S115): this file is 'summarize_probes.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Summarize the generated core battery. Python 3 standard library only."""
import argparse, csv, math
from collections import defaultdict
from pathlib import Path

def tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def detail(path, spop=False, expected_fields=None):
    fields = None; rows = []
    for line in Path(path).read_text().splitlines():
        if line.startswith('#format '):
            actual = line.split()[1:]
            if expected_fields is not None:
                if actual != [c.split('.')[0] for c in expected_fields]:
                    raise ValueError(f'{path}: header does not match positional schema')
                fields = expected_fields
            else: fields = actual
        elif line.strip() and not line.lstrip().startswith('#'):
            if fields is None: raise ValueError(f'{path}: missing #format')
            vals = line.split()
            row = dict(zip(fields, vals))
            omitted = fields[len(vals):]
            historical_tail = spop and int(row.get('num_units',row.get('num_cpus','-1'))) == 0 and set(omitted) <= {'cells','gest_offset','lineage'} and 'sequence' in row
            if len(vals) != len(fields) and not (len(vals)<len(fields) and historical_tail):
                raise ValueError(f'{path}: malformed row')
            rows.append(row)
    if fields is None: raise ValueError(f'{path}: missing #format')
    return rows

def write(path, fields, rows):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fields, delimiter='\t'); w.writeheader(); w.writerows(rows)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('suite', type=Path)
    p.add_argument('--rewards', type=Path, help='TSV: canonical,first_reward_update; integer, never, or unknown')
    a = p.parse_args(); base = a.suite.resolve()
    snaps = sorted(tsv(base/'snapshots.tsv'), key=lambda r:int(r['update']))
    if not snaps or len({r['label'] for r in snaps}) != len(snaps) or len({r['update'] for r in snaps}) != len(snaps):
        raise ValueError('Need unique labels and strictly ordered updates for ONE run')
    tasks = [r for r in tsv(base/'tasks.tsv') if r['profile']=='core' and r['name']==r['canonical'] and r['name']!='dontcare']
    inputs = [r for r in tsv(base/'inputs.tsv') if r['profile']=='core']
    if not tasks or not inputs: raise ValueError('Missing core task or input definitions')
    if len({r['input_id'] for r in inputs})!=len(inputs) or len({tuple(r[f'input{j}'] for j in range(3)) for r in inputs})!=len(inputs):
        raise ValueError('Input IDs and triples must be distinct')
    if len(inputs)<2: raise ValueError('Need at least two distinct input triples')
    schema = sorted([r for r in tsv(base/'schema.tsv') if r['profile']=='core'],key=lambda r:int(r['position']))
    if [int(r['position']) for r in schema] != list(range(len(schema))):
        raise ValueError('Column positions must be contiguous from zero')
    columns = [r['column'] for r in schema]
    if not columns or len(set(columns))!=len(columns): raise ValueError('Missing or duplicate column definitions')
    required = {'id','num_units','viable','sequence',*[f'env_input.{j}' for j in range(3)],*[f"task.{r['task_index']}" for r in tasks]}
    if not required<=set(columns): raise ValueError('Column schema misses required fields')
    rewards = {} if a.rewards is None else {r['canonical']:r['first_reward_update'] for r in tsv(a.rewards)}
    panel=[]; sets=[]; dynamics=[]; seq_seen=set(); task_seen=set(); previous_seq=set()
    for s in snaps:
        label=s['label']; update=int(s['update'])
        population=detail(s['path'], spop=True)
        living={r['id']:r for r in population if int(r.get('num_units',r.get('num_cpus','0')))>0}
        if len(living) != sum(int(r.get('num_units',r.get('num_cpus','0')))>0 for r in population):
            raise ValueError(f'{label}: duplicate source IDs')
        total=sum(int(r.get('num_units',r.get('num_cpus','0'))) for r in living.values())
        trials=[]
        for inp in inputs:
            file=base/'results'/'core'/f"{label}-input{inp['input_id']}.dat"
            rows=detail(file, expected_fields=columns) if living else []
            byid={r['id']:r for r in rows}
            if len(byid)!=len(rows) or set(byid)!=set(living):
                raise ValueError(f'{file}: incomplete or duplicate living ID set')
            for ident,r in byid.items():
                if r['sequence'] != living[ident]['sequence']:
                    raise ValueError(f'{file}: sequence identity changed')
                if int(r['num_units'])!=int(living[ident].get('num_units',living[ident].get('num_cpus','0'))):
                    raise ValueError(f'{file}: abundance changed')
                for j in range(3):
                    if int(r[f'env_input.{j}'])!=int(inp[f'input{j}']):
                        raise ValueError(f'{file}: input mismatch')
            trials.append(byid)
        present=set()
        for task in tasks:
            col=f"task.{task['task_index']}"; name=task['name']
            any_n=all_n=raw_n=0
            for ident,source in living.items():
                n=int(source.get('num_units',source.get('num_cpus','0')))
                raw=[int(t[ident][col])>0 for t in trials]
                hits=[r and int(t[ident]['viable'])>0 for r,t in zip(raw,trials)]
                raw_n += n*any(raw); any_n += n*any(hits); all_n += n*all(hits)
            exposure=rewards.get(task['canonical'],'unknown')
            if exposure=='never': status='never_rewarded_full_record'
            elif exposure=='unknown': status='reward_history_unknown'
            else: status='rewarded_by_snapshot' if int(exposure)<=update else 'not_yet_rewarded'
            if all_n: present.add(name)
            panel.append(dict(label=label,update=update,task=name,task_kind=task.get('status','unknown'),canonical=task['canonical'],first_reward_update=exposure,
                              reward_status=status,population=total,raw_any=raw_n,viable_any=any_n,viable_all=all_n,
                              fraction_all=all_n/total if total else '',inputs=len(inputs)))
        sets.append(present)
        counts=defaultdict(int)
        for r in living.values(): counts[r['sequence']]+=int(r.get('num_units',r.get('num_cpus','0')))
        seqs=set(counts)
        h=-sum((n/total)*math.log(n/total) for n in counts.values()) if total else 0
        dynamics.append(dict(label=label,update=update,population=total,distinct_sequences=len(seqs),
            sequence_entropy_nats=h,sequence_arrivals=len(seqs-previous_seq),first_observed_sequences=len(seqs-seq_seen),
            core_names_present=len(present),first_observed_core_names=len(present-task_seen)))
        seq_seen |= seqs; task_seen |= present; previous_seq=seqs
    retention=[]
    for i,old in enumerate(sets):
        continuous=set(old)
        for j in range(i,len(sets)):
            continuous &= sets[j]; both=old & sets[j]
            retention.append(dict(from_label=snaps[i]['label'],to_label=snaps[j]['label'],baseline=len(old),
                endpoint_retained=len(both),endpoint_fraction=len(both)/len(old) if old else '',
                every_saved_snapshot=len(continuous),present_after_sampled_gap=len(both-continuous)))
    out=base/'summary'; out.mkdir(exist_ok=True)
    write(out/'capabilities.tsv',list(panel[0]),panel)
    write(out/'retention.tsv',list(retention[0]),retention)
    write(out/'snapshot_dynamics.tsv',list(dynamics[0]),dynamics)
    if a.rewards is None:
        write(out/'reward_history_template.tsv',['canonical','first_reward_update'],
              [dict(canonical=t['canonical'],first_reward_update='unknown') for t in tasks])
    print(out)

if __name__=='__main__': main()
