% ledger_B05_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(minutes).
kind(minutes, record) :- line(minutes).
body(minutes, not_stated) :- line(minutes).
line(governors).
kind(governors, group_of_people) :- line(governors).
body(governors, not_stated) :- line(governors).
line(head_teacher).
kind(head_teacher, person) :- line(head_teacher).
body(head_teacher, not_stated) :- line(head_teacher).
line(attendance).
kind(attendance, measure) :- line(attendance).
body(attendance, not_stated) :- line(attendance).
line(rise).
holds(rose(attendance)) :- line(rise).
line(expl).
holds(explained(head_teacher, rose(attendance))) :- line(expl).
line(bus_route).
kind(bus_route, bus_route) :- line(bus_route).
body(bus_route, not_stated) :- line(bus_route).
line(estate).
kind(estate, estate) :- line(estate).
body(estate, not_stated) :- line(estate).
line(new_route).
holds(new(bus_route)) :- line(new_route).
line(p2).
holds(reached(bus_route, estate)) :- line(p2).
line(risen).
holds(rose(attendance)) :- line(risen).
line(because1).
claim_because(because1, rose(attendance), reached(bus_route, estate)) :- line(because1).
line(school).
kind(school, school) :- line(school).
body(school, not_stated) :- line(school).
line(entrance_hall).
kind(entrance_hall, hall) :- line(entrance_hall).
body(entrance_hall, not_stated) :- line(entrance_hall).
line(p1).
holds(repainted(school, entrance_hall)) :- line(p1).
line(r1).
holds(becomes(entrance_hall, repainted)) :- line(r1).
line(denial).
denied_because(denial, rose(attendance), reached(bus_route, estate)) :- line(denial).
line(canteen_budget).
kind(canteen_budget, budget) :- line(canteen_budget).
body(canteen_budget, not_stated) :- line(canteen_budget).
line(took).
holds(took_up(governors, canteen_budget)) :- line(took).
