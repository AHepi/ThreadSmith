import sys
sys.path.insert(0,'temporal_selector')
from selector import Selector
from checks import obs
order=[2,0,1]
a=Selector(3,eligible=[0,2]); b=Selector(3,eligible=[order.index(i) for i in [0,2]])
cases=[obs([.2,0,0]),obs([.2,0,.3],pairs=[(0,2,.1)]),obs([0,0,.3],[.3,0,.3])]
for o in cases:
 transformed={'p':[o['p'][i] for i in order],'q':[o['q'][i] for i in order],
              'cooc':[[o['cooc'][i][j] for j in order] for i in order]}
 x=a.step(o)['pay']; y=b.step(transformed)['pay']
 assert all(abs(y[j]-x[i])<1e-12 for j,i in enumerate(order))
print('task relabelling with eligibility carried: 3 successive pay vectors commute')
