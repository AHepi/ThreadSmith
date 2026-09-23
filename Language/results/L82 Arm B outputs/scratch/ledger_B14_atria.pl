% ledger_B14_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(nurse).
kind(nurse, nurse) :- line(nurse).
body(nurse, not_stated) :- line(nurse).
line(notes).
kind(notes, handover_notes) :- line(notes).
body(notes, not_stated) :- line(notes).
line(sister).
kind(sister, nurse) :- line(sister).
body(sister, not_stated) :- line(sister).
line(read1).
holds(read(nurse, notes)) :- line(read1).
line(leftby).
holds(left_by(notes, sister)) :- line(leftby).
line(sister_in_notes).
kind(sister, nurse) :- line(sister_in_notes).
body(sister, not_stated) :- line(sister_in_notes).
line(patient).
kind(patient, patient) :- line(patient).
body(patient, not_stated) :- line(patient).
line(desk).
kind(desk, desk) :- line(desk).
body(desk, not_stated) :- line(desk).
line(breathing).
kind(breathing, breathing) :- line(breathing).
body(breathing, not_stated) :- line(breathing).
line(plan).
claim_plan(plan, move(sister, patient, desk), easy_to_monitor(breathing)) :- line(plan).
line(temp).
holds(temperature_normal(patient, at_midnight)) :- line(temp).
