% ledger_B09_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(nurse).
kind(nurse, person) :- line(nurse).
body(nurse, heavy_and_standing) :- line(nurse).
line(fin).
holds(incoming(nurse)) :- line(fin).
line(notes).
kind(notes, handover_note) :- line(notes).
body(notes, not_stated) :- line(notes).
line(sister).
kind(sister, person) :- line(sister).
body(sister, heavy_and_standing) :- line(sister).
line(fnight).
holds(night_sister(sister)) :- line(fnight).
line(p2).
holds(left(sister, notes)) :- line(p2).
line(p1).
holds(read(nurse, notes)) :- line(p1).
line(siw).
kind(sister, person) :- line(siw).
body(sister, heavy_and_standing) :- line(siw).
line(patient).
kind(patient, person) :- line(patient).
body(patient, heavy_and_standing) :- line(patient).
line(desk).
kind(desk, desk) :- line(desk).
body(desk, not_stated) :- line(desk).
line(mg).
holds(monitored(breathing(patient))) :- line(mg).
line(pl).
claim_plan(pl, move(sister, patient, toward(desk)), monitored(breathing(patient))) :- line(pl).
line(tn).
holds(temperature_normal(patient, midnight)) :- line(tn).
line(reminder).
kind(reminder, reminder) :- line(reminder).
body(reminder, not_stated) :- line(reminder).
line(end).
holds(ended_with(notes, reminder)) :- line(end).
