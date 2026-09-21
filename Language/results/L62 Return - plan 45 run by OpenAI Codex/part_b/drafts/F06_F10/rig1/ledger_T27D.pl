% T27-D. Exact-one rule is binned; both explicit facts remain.
line(s1). line(f1).
holds(open(side_gate)) :- line(s1).
holds(open(front_gate)) :- line(f1).
