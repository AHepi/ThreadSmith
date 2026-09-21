% N16-A. Exact-text adapter; no rig patch.
line(t1). line(m1). line(p1).
tends(nora, continue_toward(exit)) :- line(t1).
social(n16a, makes, moving_walkway, nora, continue_toward(exit)) :- line(m1).
holds(producer_of(moving_walkway, continued_movement(nora, toward(exit)))) :- line(p1).
