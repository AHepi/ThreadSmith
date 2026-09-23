% ledger_B10_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(governors_minutes).
kind(governors_minutes, note) :- line(governors_minutes).
body(governors_minutes, not_stated) :- line(governors_minutes).
line(head_teacher).
kind(head_teacher, person) :- line(head_teacher).
body(head_teacher, heavy_and_standing) :- line(head_teacher).
line(attendance).
kind(attendance, measure) :- line(attendance).
body(attendance, not_stated) :- line(attendance).
line(rise).
holds(risen(attendance)) :- line(rise).
line(meeting).
kind(meeting, meeting) :- line(meeting).
body(meeting, not_stated) :- line(meeting).
line(governors).
kind(governors, group) :- line(governors).
body(governors, not_stated) :- line(governors).
line(canteen_budget).
kind(canteen_budget, budget) :- line(canteen_budget).
body(canteen_budget, not_stated) :- line(canteen_budget).
line(discuss_budget).
holds(discussed(governors, canteen_budget)) :- line(discuss_budget).
line(m_head_teacher).
kind(head_teacher, person) :- line(m_head_teacher).
body(head_teacher, heavy_and_standing) :- line(m_head_teacher).
line(m_attendance).
kind(attendance, measure) :- line(m_attendance).
body(attendance, not_stated) :- line(m_attendance).
line(m_rise).
holds(risen(attendance)) :- line(m_rise).
line(m_explanation).
kind(explanation, explanation) :- line(m_explanation).
body(explanation, not_stated) :- line(m_explanation).
line(m_explained).
holds(explanation_of(explanation, head_teacher, risen(attendance))) :- line(m_explained).
line(m_school).
kind(school, school) :- line(m_school).
body(school, not_stated) :- line(m_school).
line(m_hall).
kind(entrance_hall, hall) :- line(m_hall).
body(entrance_hall, not_stated) :- line(m_hall).
line(m_repaint).
holds(repainted(school, entrance_hall)) :- line(m_repaint).
line(h_attendance).
kind(attendance, measure) :- line(h_attendance).
body(attendance, not_stated) :- line(h_attendance).
line(h_rise).
holds(risen(attendance)) :- line(h_rise).
line(h_route).
kind(new_bus_route, bus_route) :- line(h_route).
body(new_bus_route, not_stated) :- line(h_route).
line(h_estate).
kind(estate, housing_estate) :- line(h_estate).
body(estate, not_stated) :- line(h_estate).
line(h_reaches).
holds(reaches(new_bus_route, estate)) :- line(h_reaches).
line(h_because).
claim_because(h_because, risen(attendance), reaches(new_bus_route, estate)) :- line(h_because).
line(h_school).
kind(school, school) :- line(h_school).
body(school, not_stated) :- line(h_school).
line(h_hall).
kind(entrance_hall, hall) :- line(h_hall).
body(entrance_hall, not_stated) :- line(h_hall).
line(h_repaint).
holds(repainted(school, entrance_hall)) :- line(h_repaint).
line(h_denial).
denied_because(h_denial, risen(attendance), repainted(school, entrance_hall)) :- line(h_denial).
