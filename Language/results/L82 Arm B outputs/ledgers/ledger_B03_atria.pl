% ledger_B03_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(clerk).
kind(clerk, dockyard_clerk) :- line(clerk).
body(clerk, not_stated) :- line(clerk).
line(log).
kind(log, harbourmaster_log) :- line(log).
body(log, not_stated) :- line(log).
line(read).
holds(reads(clerk, log)) :- line(read).
line(harbourmaster).
kind(harbourmaster, harbourmaster) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(trawler).
kind(trawler, trawler) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, harbour_bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(cross).
holds(crossed(trawler, bar)) :- line(cross).
line(turn).
holds(turned(tide)) :- line(turn).
line(because2).
claim_because(because2, crossed(trawler, bar), turned(tide)) :- line(because2).
line(rec_names).
holds(records(log, names(crew))) :- line(rec_names).
line(rec_weight).
holds(records(log, weight(catch))) :- line(rec_weight).
line(crew).
kind(crew, crew) :- line(crew).
body(crew, not_stated) :- line(crew).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(boats).
kind(boats, boats) :- line(boats).
body(boats, not_stated) :- line(boats).
line(tied).
holds(tied_up(boats)) :- line(tied).
line(entry).
kind(entry, log_entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(concerns).
holds(concerns(entry, due_on(repairs, north_pier))) :- line(concerns).
line(repairs).
kind(repairs, repairs) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(north_pier).
kind(north_pier, pier) :- line(north_pier).
body(north_pier, not_stated) :- line(north_pier).
