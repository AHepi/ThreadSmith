"""Settling X3.2(ii): never-rewarded arithmetic ever seen by 50,000, per run, from the probe summariser's capabilities.tsv
(read only), with the same definitions as S116's probe script (viable_all > 0; echo, add, add3, sub, math_*)."""
import csv, json
P = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116/probes'
ENVS = ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']
def arith(n): return n in ('echo', 'add', 'add3', 'sub') or n.startswith('math_')
out = {}
for e in ENVS:
    v = []
    for s in (1, 2, 3):
        ever = set()
        for r in csv.DictReader(open('%s/%s_seed%d/summary/capabilities.tsv' % (P, e, s)), delimiter='\t'):
            if arith(r['task']) and int(r['update']) <= 50000 and int(r['viable_all']) > 0:
                ever.add(r['task'])
        v.append(len(ever))
    out[e] = v
base = out['no_rewards']
def three(a, b): return 'more' if min(a) > max(b) else ('fewer' if max(a) < min(b) else 'not separated by three seeds')
res = {e: {'seeds': out[e], 'against NO TASK REWARDS': three(out[e], base)} for e in ENVS if e != 'no_rewards'}
res['NO TASK REWARDS'] = base
json.dump(res, open('arith_ever_seen.json', 'w'), indent=1); print(json.dumps(res))
