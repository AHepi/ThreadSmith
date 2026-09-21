% N19-A. Inferential routes remain SINCE/SHOWS.
line(p1). line(b1). line(r1). line(c1). line(f1). line(r2). line(c2). line(c3).
holds(recorded(press)) :- line(p1).
holds(rang(bell)) :- line(b1).
holds(rang(bell)) :- line(r1), holds(recorded(press)).
holds(rose(flag)) :- line(f1).
holds(rose(flag)) :- line(r2), holds(rang(bell)).
claim_since(c1, rang(bell), recorded(press)) :- line(c1).
claim_since(c2, rose(flag), rang(bell)) :- line(c2).
claim_since(c3, rang(bell), rose(flag)) :- line(c3).
