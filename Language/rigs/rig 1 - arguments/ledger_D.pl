% ledger_D.pl - the lateness paragraph
line(1). line(2). line(3). line(4). line(5). line(u1).
holds(misses_deadlines(team)) :- line(1).
claim_because(2, misses_deadlines(team), has_lateness_culture(team)) :- line(2).
holds(has_lateness_culture(T)) :- line(3), holds(misses_deadlines(T)).
produced(misses_deadlines(T)) :- line(4), holds(has_lateness_culture(T)).
depends(misses_deadlines(T), has_lateness_culture(T)) :- line(4).
claim_plan(5, workshop(team), misses_deadlines(team)) :- line(5).
changes(workshop(T), has_lateness_culture(T)) :- line(u1).
