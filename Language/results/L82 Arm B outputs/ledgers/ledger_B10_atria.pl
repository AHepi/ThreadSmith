% ledger_B10_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(gov).
kind(governors, group) :- line(gov).
body(governors, heavy_and_standing) :- line(gov).
line(min).
kind(minutes, document) :- line(min).
body(minutes, not_stated) :- line(min).
line(ht).
kind(head_teacher, person) :- line(ht).
body(head_teacher, heavy_and_standing) :- line(ht).
line(expl).
kind(explanation, explanation) :- line(expl).
body(explanation, not_stated) :- line(expl).
line(att).
kind(attendance, measure_of_pupils_present) :- line(att).
body(attendance, not_stated) :- line(att).
line(p1).
holds(recorded(minutes, explanation)) :- line(p1).
line(f1).
holds(explanation_for(explanation, attendance)) :- line(f1).
line(sch).
kind(school, school) :- line(sch).
body(school, not_stated) :- line(sch).
line(hall).
kind(entrance_hall, entrance_hall) :- line(hall).
body(entrance_hall, not_stated) :- line(hall).
line(p3).
holds(noted(minutes, repainted(school, entrance_hall))) :- line(p3).
line(cb).
kind(canteen_budget, budget) :- line(cb).
body(canteen_budget, not_stated) :- line(cb).
line(p5).
holds(discussed(governors, canteen_budget)) :- line(p5).
line(m_att).
kind(attendance, measure_of_pupils_present) :- line(m_att).
body(attendance, not_stated) :- line(m_att).
line(m_route).
kind(bus_route, route) :- line(m_route).
body(bus_route, not_stated) :- line(m_route).
line(m_estate).
kind(estate, housing_estate) :- line(m_estate).
body(estate, not_stated) :- line(m_estate).
line(m_school).
kind(school, school) :- line(m_school).
body(school, not_stated) :- line(m_school).
line(m_hall).
kind(entrance_hall, entrance_hall) :- line(m_hall).
body(entrance_hall, not_stated) :- line(m_hall).
line(m_rise).
holds(rose(attendance)) :- line(m_rise).
line(m_reach).
holds(reaches(bus_route, estate)) :- line(m_reach).
line(m_bec).
claim_because(m_bec, rose(attendance), reaches(bus_route, estate)) :- line(m_bec).
line(m_repaint).
holds(repainted(school, entrance_hall)) :- line(m_repaint).
line(h_att).
kind(attendance, measure_of_pupils_present) :- line(h_att).
body(attendance, not_stated) :- line(h_att).
line(h_hall).
kind(entrance_hall, entrance_hall) :- line(h_hall).
body(entrance_hall, not_stated) :- line(h_hall).
line(h_rise).
holds(rose(attendance)) :- line(h_rise).
line(h_repaint).
holds(repainted(entrance_hall)) :- line(h_repaint).
line(h_denied).
denied_because(h_denied, rose(attendance), repainted(entrance_hall)) :- line(h_denied).
