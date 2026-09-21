% N16-B. Plain source commitments; no lexical substitution into social/5.
line(t1). line(e1). line(p1).
holds(tends(nora, continue_toward(exit))) :- line(t1).
holds(continued_toward(nora, exit)) :- line(e1).
holds(production_attribution(moving_walkway, nora, continued_toward(exit))) :- line(p1).
