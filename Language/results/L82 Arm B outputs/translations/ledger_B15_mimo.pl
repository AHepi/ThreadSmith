% ledger_B15_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(surveyor).
kind(surveyor, building_surveyor) :- line(surveyor).
body(surveyor, not_stated) :- line(surveyor).
line(report).
kind(report, report) :- line(report).
body(report, not_stated) :- line(report).
line(flood).
kind(flood, flood) :- line(flood).
body(flood, not_stated) :- line(flood).
line(p1).
holds(filed(surveyor, report)) :- line(p1).
line(about).
holds(about(report, flood)) :- line(about).
line(cellar).
kind(cellar, cellar) :- line(cellar).
body(cellar, not_stated) :- line(cellar).
line(valve).
kind(valve, valve) :- line(valve).
body(valve, not_stated) :- line(valve).
line(flooded).
holds(flooded(cellar)) :- line(flooded).
line(open).
holds(left_open(valve)) :- line(open).
line(cause1).
claim_because(cause1, flooded(cellar), left_open(valve)) :- line(cause1).
line(water).
kind(water, water) :- line(water).
body(water, not_stated) :- line(water).
line(step).
kind(step, step) :- line(step).
body(step, not_stated) :- line(step).
line(reached).
holds(reached(water, step)) :- line(reached).
line(caretaker).
kind(caretaker, caretaker) :- line(caretaker).
body(caretaker, not_stated) :- line(caretaker).
line(away).
holds(away(caretaker)) :- line(away).
