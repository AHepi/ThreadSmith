% ledger_B09_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(n1).
kind(nurse, person) :- line(n1).
line(n2).
body(nurse, heavy_standing) :- line(n2).
line(n3).
kind(notes, handover_note) :- line(n3).
body(notes, not_stated) :- line(n3).
line(n4).
kind(sister, person) :- line(n4).
line(n5).
body(sister, heavy_standing) :- line(n5).
line(n6).
holds(reads(nurse, notes)) :- line(n6).
line(n7).
holds(left_by(notes, sister)) :- line(n7).
line(n8).
kind(medication, medication) :- line(n8).
body(medication, not_stated) :- line(n8).
line(n9).
holds(ends_with_reminder(notes)) :- line(n9).
line(w1).
kind(sister, person) :- line(w1).
line(w2).
body(sister, heavy_standing) :- line(w2).
line(w3).
kind(patient, person) :- line(w3).
line(w4).
body(patient, heavy_standing) :- line(w4).
line(w5).
kind(desk, desk) :- line(w5).
body(desk, not_stated) :- line(w5).
line(w6).
kind(breathing, breathing) :- line(w6).
body(breathing, not_stated) :- line(w6).
line(w7).
kind(temperature, temperature) :- line(w7).
body(temperature, not_stated) :- line(w7).
line(w8).
holds(plans(sister, move(patient, desk))) :- line(w8).
line(w9).
claim_plan(w9, move(sister, patient, desk), easier_to_monitor(breathing)) :- line(w9).
line(w10).
holds(normal_temperature(patient)) :- line(w10).
