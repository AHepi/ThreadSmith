% ledger_B02_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(t1).
kind(technician, person) :- line(t1).
line(t2).
body(technician, heavy_and_standing) :- line(t2).
line(t3).
kind(notebook, notebook) :- line(t3).
body(notebook, not_stated) :- line(t3).
line(t4).
kind(routine, routine) :- line(t4).
body(routine, not_stated) :- line(t4).
line(t5).
kind(samples, samples) :- line(t5).
body(samples, not_stated) :- line(t5).
line(t6).
kind(watertank, water_tank) :- line(t6).
body(watertank, not_stated) :- line(t6).
line(t7).
kind(soiltrays, soil_trays) :- line(t7).
body(soiltrays, not_stated) :- line(t7).
line(t8).
kind(incubator, incubator) :- line(t8).
body(incubator, not_stated) :- line(t8).
line(t9).
kind(temperature, temperature) :- line(t9).
body(temperature, not_stated) :- line(t9).
line(t10).
kind(labels, labels) :- line(t10).
body(labels, not_stated) :- line(t10).
line(t11).
kind(supplier, person) :- line(t11).
line(t12).
body(supplier, heavy_and_standing) :- line(t12).
line(t13).
kind(ink, ink) :- line(t13).
body(ink, not_stated) :- line(t13).
line(t14).
kind(fume_cupboard, fume_cupboard) :- line(t14).
body(fume_cupboard, not_stated) :- line(t14).
line(h1).
holds(described(technician, routine)) :- line(h1).
line(h2).
holds(listed(technician, samples)) :- line(h2).
line(h3).
holds(tested(technician, samples)) :- line(h3).
line(h4).
holds(recorded(technician, temperature)) :- line(h4).
line(h5).
holds(described(notebook, labels)) :- line(h5).
line(h6).
holds(sent(supplier, labels)) :- line(h6).
line(h7).
holds(noted(technician, cleaned(fume_cupboard))) :- line(h7).
line(r1).
holds(tested_in_order(samples, watertank, soiltrays)) :- line(r1).
line(f2).
holds(printed_in(labels, ink)) :- line(f2).
line(f3).
holds(cleaned(fume_cupboard)) :- line(f3).
line(l1).
holds(needs(h2, tested_in_order(samples, watertank, soiltrays))) :- line(l1).
