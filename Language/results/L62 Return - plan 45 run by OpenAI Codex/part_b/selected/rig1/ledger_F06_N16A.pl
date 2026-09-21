% F06 N16-A rig-1 projection selected before execution.
% The free production attribution is not the rig-2 MAKES word-slot test.
line(t1). line(e1). line(p1).
holds(tends(nora, continue_toward(exit))) :- line(t1).
holds(continued_toward(nora, exit)) :- line(e1).
holds(production_attribution(moving_walkway, nora, continued_toward(exit))) :- line(p1).
