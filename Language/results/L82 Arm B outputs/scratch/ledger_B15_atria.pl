% ledger_B15_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(a).
kind(surveyor, building_surveyor) :- line(a).
body(surveyor, not_stated) :- line(a).
line(b).
kind(report, report) :- line(b).
body(report, not_stated) :- line(b).
line(c).
kind(cellar, cellar) :- line(c).
body(cellar, not_stated) :- line(c).
line(d).
kind(flood, flood) :- line(d).
body(flood, not_stated) :- line(d).
line(e).
holds(filed(surveyor, report)) :- line(e).
line(f).
holds(concerns(report, flood)) :- line(f).
line(g).
kind(valve, valve) :- line(g).
body(valve, not_stated) :- line(g).
line(h).
kind(cellar, cellar) :- line(h).
body(cellar, not_stated) :- line(h).
line(i).
kind(water, water) :- line(i).
body(water, not_stated) :- line(i).
line(j).
kind(step, step) :- line(j).
body(step, not_stated) :- line(j).
line(k).
kind(caretaker, caretaker) :- line(k).
body(caretaker, not_stated) :- line(k).
line(l).
holds(flooded(cellar)) :- line(l).
line(m).
holds(open(valve)) :- line(m).
line(n).
claim_because(n, flooded(cellar), open(valve)) :- line(n).
line(o).
holds(reached(water, step)) :- line(o).
line(p).
holds(away(caretaker)) :- line(p).
