% ledger_B12_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(surv).
kind(surveyor, building_surveyor) :- line(surv).
body(surveyor, not_stated) :- line(surv).
line(rep).
kind(report, report) :- line(rep).
body(report, not_stated) :- line(rep).
line(cell).
kind(cellar, cellar) :- line(cell).
body(cellar, not_stated) :- line(cell).
line(flood1).
holds(flooded(cellar)) :- line(flood1).
line(topic).
holds(about(report, flooded(cellar))) :- line(topic).
line(filing).
holds(filed(surveyor, report)) :- line(filing).
line(wcell).
kind(cellar, cellar) :- line(wcell).
body(cellar, not_stated) :- line(wcell).
line(wvalve).
kind(valve, valve) :- line(wvalve).
body(valve, not_stated) :- line(wvalve).
line(wflood).
holds(flooded(cellar)) :- line(wflood).
line(wopen).
holds(left_open(valve)) :- line(wopen).
line(wbecause).
claim_because(wbecause, flooded(cellar), left_open(valve)) :- line(wbecause).
line(wwater).
kind(water, water) :- line(wwater).
body(water, not_stated) :- line(wwater).
line(wstep).
kind(step, step) :- line(wstep).
body(step, not_stated) :- line(wstep).
line(wreach).
holds(reached(water, step)) :- line(wreach).
line(wcare).
kind(caretaker, caretaker) :- line(wcare).
body(caretaker, not_stated) :- line(wcare).
line(waway).
holds(away(caretaker)) :- line(waway).
