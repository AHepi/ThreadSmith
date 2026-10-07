"""Self-authored component probes frozen in spec_v1 before this test rig."""
from selector import Selector, UNITS
import math

def obs(q, p=None, pairs=None):
    k=len(q)
    C=[[0.0]*k for _ in range(k)]
    if pairs:
        for i,j,v in pairs: C[i][j]=C[j][i]=v
    return dict(p=q[:] if p is None else p, q=q, cooc=C)

def check():
    s=Selector(3)
    a=[]
    for _ in range(8): a.append(s.step(obs([.5,0,0]))['diagnostics']['adaptation'][0])
    assert a[-1] < a[0]
    for _ in range(16): out=s.step(obs([0,0,0]))
    assert out['diagnostics']['adaptation'][0] > a[-1]
    print('adaptation sustained %.6f -> %.6f; after absence %.6f' % (a[0],a[-1],out['diagnostics']['adaptation'][0]))
    s=Selector(3)
    out=s.step(obs([0,0,0],[.5,0,0]))
    assert out['diagnostics']['latch'][0]==1
    for _ in range(20): out=s.step(obs([0,0,0]))
    assert out['diagnostics']['latch'][0]==1
    one=s.step(obs([.2,0,0])); two=s.step(obs([.2,0,0]))
    assert one['diagnostics']['latch'][0]==1 and two['diagnostics']['latch'][0]==0
    assert two['diagnostics']['release'][0]==1 and two['diagnostics']['rebound'][0]==1
    print('latch held across 20 absent pieces; clears after two robust assays; rebound 1.000000')
    s=Selector(3); s.step(obs([.2,0,0])); out=s.step(obs([.2,.2,0]))
    alone=Selector(3).step(obs([0,.2,0]))
    simultaneous=Selector(3).step(obs([.2,.2,0]))
    assert out['diagnostics']['sequence'][1] > 0
    assert alone['diagnostics']['sequence'][1]==simultaneous['diagnostics']['sequence'][1]==0
    delayed=Selector(3); delayed.step(obs([.2,0,0]))
    for _ in range(10): delayed.step(obs([.2,0,0]))
    late=delayed.step(obs([.2,.2,0]))['diagnostics']['sequence'][1]
    assert late < out['diagnostics']['sequence'][1]
    print('sequence short %.6f; long %.6f; alone 0; simultaneous 0' % (out['diagnostics']['sequence'][1],late))
    together=Selector(3).step(obs([.2,.2,0],pairs=[(0,1,.2)]))
    separate=Selector(3).step(obs([.2,.2,0]))
    assert together['diagnostics']['coincidence'][0] > separate['diagnostics']['coincidence'][0]
    print('same-program coincidence %.6f; separate programs 0' % together['diagnostics']['coincidence'][0])
    s=Selector(77)
    flat=obs([0]*77)
    for _ in range(100): out=s.step(flat)
    assert math.isclose(sum(out['pay']),18) and all(out['pay'][i]==0 for i in range(6,77,7))
    print('constant empty assay after 100 pieces: nominal budget %.6f; withheld 11; eligible 66' % sum(out['pay']))
    for unit in UNITS:
        s=Selector(3,disabled=[unit]); s.step(obs([.2,0,0])); o=s.step(obs([.2,.2,0]))
        assert math.isclose(sum(o['pay']),18)
    s=Selector(3); s.step(obs([.2,0,0])); state=s.state
    a=s.step(obs([.2,.2,0])); b=Selector(3).load(state).step(obs([.2,.2,0]))
    assert a==b
    print('seven ablations preserve nominal budget; serialized state replay identical')
    print('COMPONENT CHECKS COMPLETED')

if __name__=='__main__': check()
