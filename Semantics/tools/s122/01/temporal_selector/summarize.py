#!/usr/bin/env python3
"""Read completed run records; do not treat pieces as independent runs."""
import argparse
import json
from pathlib import Path

def summarize(directory):
    directory=Path(directory)
    manifest=json.loads((directory/'manifest.json').read_text())
    paths=sorted(directory.glob('piece_*/complete.json'))
    if len(paths) != manifest['pieces']:
        raise ValueError('run is incomplete')
    records=[json.loads(p.read_text()) for p in paths]
    applied=[r['applied_pay'] for r in records]
    k=len(manifest['tasks'])
    never=[j for j in range(k) if all(row[j] == 0 for row in applied)]
    ever=set(); prior=set(); trajectory=[]; episodes=[]; open_latches={}
    for i,(path,record) in enumerate(zip(paths,records)):
        observation=json.loads((path.parent/'assay/observation.json').read_text())
        common={j for j,v in enumerate(observation['q']) if v >= .1}
        ever |= common
        current_latches={j for j,v in enumerate(record['diagnostics'].get('latch',[])) if v}
        for j in current_latches-set(open_latches):
            open_latches[j]=i+1
        for j in set(open_latches)-current_latches:
            episodes.append(dict(task=j,set_piece=open_latches.pop(j),clear_piece=i+1))
        trajectory.append(dict(piece=i+1,world_common=sum(v>=.1 for v in observation['p']),
                               all_order_common=len(common),ever_common=len(ever),
                               gained=sorted(common-prior),lost=sorted(prior-common),
                               never_directly_paid_common=len(common & set(never))))
        prior=common
    for j,start in open_latches.items():
        episodes.append(dict(task=j,set_piece=start,clear_piece=None))
    delta=slope=None
    if len(trajectory)>=50:
        delta=trajectory[49]['all_order_common']-trajectory[24]['all_order_common']
        x=list(range(26,51)); y=[trajectory[i-1]['all_order_common'] for i in x]
        xm=sum(x)/len(x); ym=sum(y)/len(y)
        slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
    return dict(arm=manifest['arm'],seed=manifest['seed'],completed_pieces=len(paths),
                never_directly_paid_indices=never,trajectory=trajectory,latch_episodes=episodes,
                late_delta_50_minus_25=delta,late_slope_per_piece=slope,
                note='Late outcomes require 50 pieces; latch continuity applies only to stateful arms.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    args=parser.parse_args()
    print(json.dumps(summarize(args.run),indent=2,sort_keys=True))
