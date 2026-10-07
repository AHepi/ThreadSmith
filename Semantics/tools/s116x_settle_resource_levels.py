"""Settling X2.2(c): the AND resource in each competition run (read only from S116's scratch output)."""
import glob, json, os
C = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116/competition'
out = {}
for d in sorted(glob.glob(C + '/share*_place*')):
    rows = [l.split() for l in open(d + '/data/resource.dat') if l.strip() and not l.startswith('#')]
    a = [(int(r[0]), float(r[3])) for r in rows]
    late = [v for u, v in a if u >= 500]
    out[os.path.basename(d)] = {'AND at update 0': a[0][1], 'AND min, updates 500-2000': round(min(late), 1),
                                'AND max, updates 500-2000': round(max(late), 1), 'AND at 2000': a[-1][1], 'rows': len(a)}
json.dump(out, open('/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116x_settle/resource_levels.json', 'w'), indent=1)
for k, v in out.items(): print(k, v)
