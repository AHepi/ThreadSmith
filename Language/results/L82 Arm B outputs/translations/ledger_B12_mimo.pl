% ledger_B12_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(surveyor).
kind(surveyor, person) :- line(surveyor).
body(surveyor, heavy_and_standing) :- line(surveyor).
line(report).
kind(report, report) :- line(report).
body(report, not_stated) :- line(report).
line(flood).
kind(flood, flood) :- line(flood).
body(flood, not_stated) :- line(flood).
line(cellar).
kind(cellar, cellar) :- line(cellar).
body(cellar, not_stated) :- line(cellar).
line(p1).
holds(filed(surveyor, report)) :- line(p1).
line(f_short).
holds(short(report)) :- line(f_short).
line(f_about).
holds(about(report, flood)) :- line(f_about).
line(f_in).
holds(in(flood, cellar)) :- line(f_in).
line(valve).
kind(valve, valve) :- line(valve).
body(valve, not_stated) :- line(valve).
line(f_flooded).
holds(flooded(cellar)) :- line(f_flooded).
line(f_valve_open).
holds(left_open(valve)) :- line(f_valve_open).
line(b1).
claim_because(b1, flooded(cellar), left_open(valve)) :- line(b1).
line(water).
kind(water, water) :- line(water).
body(water, not_stated) :- line(water).
line(second_step).
kind(second_step, step) :- line(second_step).
body(second_step, not_stated) :- line(second_step).
line(f_reached).
holds(at_stage(by_morning, reached(water, second_step))) :- line(f_reached).
line(caretaker).
kind(caretaker, person) :- line(caretaker).
body(caretaker, heavy_and_standing) :- line(caretaker).
line(f_away).
holds(away(caretaker)) :- line(f_away).
