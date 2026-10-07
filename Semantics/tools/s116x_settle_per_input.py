"""Settling S116's GLM objections X2.2(a)/X3.3: per-input viable and NOT counts from the probe's raw DETAIL files (read only)."""
import csv, os, sys, json
S = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116/probes'
def read(key, prof, m, i):
    out = os.path.join(S, key)
    schema = [r['column'] for r in sorted((r for r in csv.DictReader(open(out + '/schema.tsv'), delimiter='\t') if r['profile'] == prof), key=lambda r: int(r['position']))]
    tasks = {r['name']: r['task_index'] for r in csv.DictReader(open(out + '/tasks.tsv'), delimiter='\t') if r['profile'] == prof}
    tot = via = notv = 0
    for line in open(os.path.join(out, 'results', prof, 'u%d-input%d.dat' % (m, i))):
        if line.startswith('#') or not line.strip(): continue
        r = dict(zip(schema, line.split())); n = int(r['num_units']); tot += n
        if int(r['viable']): via += n
        if int(r['viable']) and 'not' in tasks and int(r['task.%s' % tasks['not']]) > 0: notv += n
    return tot, via, notv
def inputs(key, prof):
    return {int(r['input_id']): [int(r['input%d' % j]) >> 24 for j in range(3)] for r in csv.DictReader(open(os.path.join(S, key, 'inputs.tsv')), delimiter='\t') if r['profile'] == prof}
res = {}
for key in sys.argv[1:]:
    for prof in ('core', 'logic_high'):
        top = inputs(key, prof)
        for i in range(8):
            t, v, n = read(key, prof, 50000, i)
            res['%s %s input%d top%s' % (key, prof, i, top[i])] = {'programs': t, 'viable': v, 'viable_and_NOT': n}
print(json.dumps(res, indent=0))
