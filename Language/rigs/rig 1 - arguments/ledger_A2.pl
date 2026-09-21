% ledger_A.pl - the tomato paragraph as a ledger. One "line(N)." per ledger line, so a line can be taken out.
line(1). line(2). line(3). line(4). line(5). line(6). line(7). line(8). line(9). line(10). line(11). line(12). line(k1).

kind(balcony_plants, tomato_plant) :- line(1).
kind(door_plant, tomato_plant) :- line(2).
kind(the_cold, weather) :- line(3).
kind(thermometer, measuring_device) :- line(4).

% line 5, strength USUALLY: holds unless the ledger itself denies the result for that thing
produced(dies(P)) :- line(5), kind(P, tomato_plant), holds(reached(the_cold, P)), not exception(5, P).
exception(5, P) :- denied(dies(P)).
depends(dies(P), reached(the_cold, P)) :- line(5), kind(P, tomato_plant).

holds(reached(the_cold, balcony_plants)) :- line(6).
holds(reached(the_cold, door_plant)) :- line(7).
holds(dies(balcony_plants)) :- line(8).
denied(dies(door_plant)) :- line(9).
claim_because(10, dies(balcony_plants), reached(the_cold, balcony_plants)) :- line(10).
depends(reading(thermometer), reached(the_cold, thermometer)) :- line(11).
claim_plan(12, move(thermometer), dies(balcony_plants)) :- line(12).

% usual-case line about a kind: moving a measuring device changes its reading
changes(move(D), reading(D)) :- line(k1), kind(D, measuring_device).
