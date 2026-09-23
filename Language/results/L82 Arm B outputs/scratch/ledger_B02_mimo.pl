% ledger_B02_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(tech).
kind(technician, laboratory_technician) :- line(tech).
body(technician, not_stated) :- line(tech).
line(routine).
kind(morning_routine, routine) :- line(routine).
body(morning_routine, not_stated) :- line(routine).
line(book).
kind(notebook, notebook) :- line(book).
body(notebook, not_stated) :- line(book).
line(desc).
holds(described(technician, morning_routine)) :- line(desc).
line(samples).
kind(samples, sample_set) :- line(samples).
body(samples, not_stated) :- line(samples).
line(tank).
kind(water_tank, water_tank) :- line(tank).
body(water_tank, not_stated) :- line(tank).
line(trays).
kind(soil_trays, soil_trays) :- line(trays).
body(soil_trays, not_stated) :- line(trays).
line(list).
holds(listed(technician, samples)) :- line(list).
line(test).
holds(tested(technician, samples)) :- line(test).
line(order).
holds(listed_in_test_order(samples)) :- line(order).
line(first).
holds(first_in_order(water_tank)) :- line(first).
line(last).
holds(last_in_order(soil_trays)) :- line(last).
line(incubator).
kind(incubator, incubator) :- line(incubator).
body(incubator, not_stated) :- line(incubator).
line(temp).
kind(incubator_temperature, temperature) :- line(temp).
body(incubator_temperature, not_stated) :- line(temp).
line(record).
holds(recorded(technician, incubator_temperature)) :- line(record).
line(labels).
kind(labels, label_set) :- line(labels).
body(labels, not_stated) :- line(labels).
line(supplier).
kind(supplier, supplier) :- line(supplier).
body(supplier, not_stated) :- line(supplier).
line(desc2).
holds(described(notebook, labels)) :- line(desc2).
line(send).
holds(sent(supplier, labels)) :- line(send).
line(entry).
kind(cleaning_record, record) :- line(entry).
body(cleaning_record, not_stated) :- line(entry).
line(note).
holds(noted(technician, cleaning_record)) :- line(note).
line(nlabels).
kind(labels, label_set) :- line(nlabels).
body(labels, not_stated) :- line(nlabels).
line(nnew).
holds(new(labels)) :- line(nnew).
line(nink).
kind(blue_ink, ink) :- line(nink).
body(blue_ink, not_stated) :- line(nink).
line(nprinted).
holds(printed_with(labels, blue_ink)) :- line(nprinted).
line(ncupboard).
kind(fume_cupboard, fume_cupboard) :- line(ncupboard).
body(fume_cupboard, not_stated) :- line(ncupboard).
line(ncleaned).
holds(cleaned(fume_cupboard)) :- line(ncleaned).
