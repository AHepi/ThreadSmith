"""s111x_settling_check_ancestor_lethal.py - log S111, the GLM cross-examination settled (objection Xa10): the ancestor's
2,500 one-change programs in Avida's test processor, the ones that stop copying counted at the 15 essential sites and at the
other 85. Written 29 September 2026; output in the scratch space."""
import sys, json
sys.path.insert(0, '/home/user/ThreadSmith/Semantics/tools')
import s111_avida_test_processor as T
from s111_run_the_avida_worlds import ancestor_letters
a = ancestor_letters()
ess = set(list(range(0, 6)) + list(range(91, 100)))
muts = [(i, a[:i] + c + a[i + 1:]) for i in range(len(a)) for c in T.LETTERS if c != a[i]]
rows = T.evaluate([m for _, m in muts])
le = sum(1 for (i, _), r in zip(muts, rows) if not r['viable'] and i in ess)
ln = sum(1 for (i, _), r in zip(muts, rows) if not r['viable'] and i not in ess)
per = {}
for (i, _), r in zip(muts, rows):
    per.setdefault(i, []).append(r['viable'])
all_lethal = [i + 1 for i, v in per.items() if not any(v)]
noness_sites_with_lethal = sorted(i + 1 for i, v in per.items() if i not in ess and not all(v))
res = {'lethal_at_essential': le, 'lethal_at_non_essential': ln, 'total': len(rows), 'sites_all_lethal': all_lethal,
       'non_essential_sites_with_some_lethal_change': len(noness_sites_with_lethal),
       'non_essential_lethal_by_site': {i + 1: v.count(0) for i, v in per.items() if i not in ess and not all(v)}}
json.dump(res, open('/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s111x_settle/anc_lethal.json', 'w'), indent=1)
print(json.dumps(res)[:1500])
