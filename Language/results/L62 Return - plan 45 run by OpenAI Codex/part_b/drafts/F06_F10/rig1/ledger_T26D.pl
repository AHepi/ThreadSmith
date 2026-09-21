% T26-D. The explicit side-gate fact is preserved; exclusivity is binned.
line(e1). line(s1).
holds(entered(cart)) :- line(e1).
holds(open(side_gate)) :- line(s1).
