% ledger_B04_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(nurse).
kind(nurse, incoming_nurse) :- line(nurse).
body(nurse, not_stated) :- line(nurse).
line(notes).
kind(notes, handover_notes) :- line(notes).
body(notes, not_stated) :- line(notes).
line(sister).
kind(sister, night_sister) :- line(sister).
body(sister, not_stated) :- line(sister).
line(leaving).
holds(left(sister, notes)) :- line(leaving).
line(reading).
holds(read(nurse, notes)) :- line(reading).
line(patient).
kind(patient, patient) :- line(patient).
body(patient, not_stated) :- line(patient).
line(desk).
kind(desk, desk) :- line(desk).
body(desk, not_stated) :- line(desk).
line(bed).
kind(bed, bed) :- line(bed).
body(bed, not_stated) :- line(bed).
line(staff).
kind(staff, night_staff) :- line(staff).
body(staff, not_stated) :- line(staff).
line(chest).
kind(chest, chest) :- line(chest).
body(chest, not_stated) :- line(chest).
line(breathing).
kind(breathing, breathing) :- line(breathing).
body(breathing, not_stated) :- line(breathing).
line(ward).
kind(ward, ward) :- line(ward).
body(ward, not_stated) :- line(ward).
line(beddesk).
holds(near(bed, desk)) :- line(beddesk).
line(chestup).
holds(rises(chest)) :- line(chestup).
line(lets).
holds(lets(bed, staff, watch_chest_rise(staff))) :- line(lets).
line(withoutwalk).
denied(needs(watch_chest_rise(staff), walks(staff, ward))) :- line(withoutwalk).
line(plan).
claim_plan(plan, move_toward(patient, desk), monitored(breathing)) :- line(plan).
line(patientbed).
holds(lies_in(patient, bed)) :- line(patientbed).
line(chestlink).
holds(monitored(breathing)) :- line(chestlink), holds(watch_chest_rise(staff)).
line(since1).
claim_since(since1, monitored(breathing), lets(bed, staff, watch_chest_rise(staff))) :- line(since1).
line(temp).
holds(normal(temp_of(patient), midnight)) :- line(temp).
line(reminder).
holds(ended_with_reminder(notes)) :- line(reminder).
