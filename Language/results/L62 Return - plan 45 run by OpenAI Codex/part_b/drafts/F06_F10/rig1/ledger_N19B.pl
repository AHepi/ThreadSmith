% N19-B. Positive inferential route only; reverse-provenance denial is binned.
line(f1). line(b1). line(r1). line(c1).
holds(rose(flag)) :- line(f1).
holds(rang(bell)) :- line(b1).
holds(rang(bell)) :- line(r1), holds(rose(flag)).
claim_since(c1, rang(bell), rose(flag)) :- line(c1).
