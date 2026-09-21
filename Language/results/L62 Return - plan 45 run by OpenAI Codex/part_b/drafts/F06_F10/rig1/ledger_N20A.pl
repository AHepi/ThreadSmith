% N20-A. The source's mixed SINCE/BECAUSE structure is preserved.
line(g1). line(b1). line(r1). line(c1). line(p1). line(r2). line(c2).
holds(opened(gate)) :- line(g1).
holds(rang(bell)) :- line(b1).
holds(opened(gate)) :- line(r1), holds(rang(bell)).
holds(recorded(press)) :- line(p1).
produced(rang(bell)) :- line(r2), holds(recorded(press)).
claim_since(c1, opened(gate), rang(bell)) :- line(c1).
claim_because(c2, rang(bell), recorded(press)) :- line(c2).
