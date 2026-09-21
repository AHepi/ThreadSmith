% ledger_B.pl - the buses paragraph (no planted fault)
line(1). line(2). line(3). line(4). line(5). line(6).
produced(runs_late(B)) :- line(1), kind(B, town_bus), not exception(1, B).
exception(1, B) :- denied(runs_late(B)).
kind(bus_nine, town_bus) :- line(2).
denied(runs_late(bus_nine)) :- line(3).
kind(bus_fourteen, town_bus) :- line(4).
claim_because(5, runs_late(bus_fourteen), kind(bus_fourteen, town_bus)) :- line(5).
holds(kind(X, K)) :- kind(X, K).
