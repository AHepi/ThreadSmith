% N20-B. Two inferential support steps in conventional order.
line(p1). line(b1). line(r1). line(c1). line(g1). line(r2). line(c2).
holds(recorded(press)) :- line(p1).
holds(rang(bell)) :- line(b1).
holds(rang(bell)) :- line(r1), holds(recorded(press)).
holds(opened(gate)) :- line(g1).
holds(opened(gate)) :- line(r2), holds(rang(bell)).
claim_since(c1, rang(bell), recorded(press)) :- line(c1).
claim_since(c2, opened(gate), rang(bell)) :- line(c2).
