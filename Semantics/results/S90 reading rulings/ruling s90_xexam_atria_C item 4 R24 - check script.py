# Brute force over every family S of subsets of Gamma={0,1,2} (2^8 = 256 families), d = 0.
from itertools import combinations
G = (0, 1, 2); d = 0
subsets = [frozenset(c) for r in range(4) for c in combinations(G, r)]
def test(S):      # every support stays a support after d is added and after d is removed
    return all((W | {d}) in S and (W - {d}) in S for W in S)
def removal(S):   # removal half only
    return all((W - {d}) in S for W in S)
def nocrit(S):    # {d} critical in no support (B)
    return not any(d in W and (W - {d}) not in S for W in S)
def same_E(S):    # every candidate E|W carrying d meets (E) iff E|(W - d) does
    return all((W in S) == ((W - {d}) in S) for W in subsets if d in W)
fwd = [0, 0]; conv_nocrit = conv_same = 0; nocrit_eq_removal = True
for m in range(1 << len(subsets)):
    S = {subsets[i] for i in range(len(subsets)) if m >> i & 1}
    if test(S):
        fwd[0] += 1; fwd[1] += nocrit(S) and same_E(S)
    if nocrit(S) and not test(S): conv_nocrit += 1
    if same_E(S) and not test(S): conv_same += 1
    nocrit_eq_removal &= (nocrit(S) == removal(S))
print("families passing the test:", fwd[0], "; of these, both consequences hold:", fwd[1])
print("{d} critical in no support, test fails:", conv_nocrit)
print("E-standing unchanged for every W, test fails:", conv_same)
print("{d} critical in no support == removal half, all families:", nocrit_eq_removal)
# the text's Interference example: Gamma={a,b}, S={{a}}, d=b
S = {frozenset({1})}; d = 2
print("Interference, d=b: nocrit", not any(d in W and (W - {d}) not in S for W in S),
      "; addition half", all((W | {d}) in S for W in S))
