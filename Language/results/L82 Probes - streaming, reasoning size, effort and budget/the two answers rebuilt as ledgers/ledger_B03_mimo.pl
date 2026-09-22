% ledger_B03_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(clerk).
kind(clerk, person) :- line(clerk).
body(clerk, heavy_and_standing) :- line(clerk).
line(log).
kind(log, log) :- line(log).
body(log, not_stated) :- line(log).
line(harbourmaster).
kind(harbourmaster, person) :- line(harbourmaster).
body(harbourmaster, heavy_and_standing) :- line(harbourmaster).
line(logowner).
holds(log_of(log, harbourmaster)) :- line(logowner).
line(p1).
holds(reads(clerk, log)) :- line(p1).
line(trawler).
kind(trawler, trawler) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(p2).
holds(crossed(trawler, bar)) :- line(p2).
line(tide_turn).
holds(turned(tide)) :- line(tide_turn).
line(bc1).
claim_because(bc1, crossed(trawler, bar), turned(tide)) :- line(bc1).
line(crew).
kind(crew, group_of_persons) :- line(crew).
body(crew, not_stated) :- line(crew).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(t3).
holds(has_names(crew)) :- line(t3).
line(t4).
holds(has_weight(catch)) :- line(t4).
line(crewlink).
holds(crew_of(crew, trawler)) :- line(crewlink).
line(catchlink).
holds(catch_of(catch, trawler)) :- line(catchlink).
line(entry).
kind(entry, log_entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(repairs).
kind(repairs, repair_work) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(pier).
kind(pier, pier) :- line(pier).
body(pier, not_stated) :- line(pier).
line(t5).
holds(concerns_repairs(entry, pier)) :- line(t5).
line(boats).
kind(boats, group_of_boats) :- line(boats).
body(boats, not_stated) :- line(boats).
line(c1).
holds(tied_up(boats)) :- line(c1).
