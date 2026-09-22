% ledger_B05_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(gov).
kind(governors, group) :- line(gov).
body(governors, not_stated) :- line(gov).
line(min).
kind(minutes, record) :- line(min).
body(minutes, not_stated) :- line(min).
line(ht).
kind(head_teacher, person) :- line(ht).
body(head_teacher, not_stated) :- line(ht).
line(att).
kind(attendance, measure) :- line(att).
body(attendance, not_stated) :- line(att).
line(rise).
holds(rose(attendance)) :- line(rise).
line(budget).
kind(canteen_budget, budget) :- line(budget).
body(canteen_budget, not_stated) :- line(budget).
line(discuss).
holds(discussed(governors, canteen_budget)) :- line(discuss).
line(matt).
kind(attendance, measure) :- line(matt).
body(attendance, not_stated) :- line(matt).
line(mroute).
kind(bus_route, bus_route) :- line(mroute).
body(bus_route, not_stated) :- line(mroute).
line(mestate).
kind(estate, place) :- line(mestate).
body(estate, not_stated) :- line(mestate).
line(mrise).
holds(rose(attendance)) :- line(mrise).
line(mreach).
holds(reaches(bus_route, estate)) :- line(mreach).
line(mbecause).
claim_because(mbecause, rose(attendance), reaches(bus_route, estate)) :- line(mbecause).
line(mschool).
kind(school, school) :- line(mschool).
body(school, not_stated) :- line(mschool).
line(mhall).
kind(entrance_hall, hall) :- line(mhall).
body(entrance_hall, not_stated) :- line(mhall).
line(mrepaint).
holds(repainted(school, entrance_hall)) :- line(mrepaint).
line(mdenied).
denied_because(mdenied, rose(attendance), reaches(bus_route, estate)) :- line(mdenied).
