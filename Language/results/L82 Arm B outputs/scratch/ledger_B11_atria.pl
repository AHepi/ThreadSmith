% ledger_B11_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(clerk).
kind(clerk, clerk) :- line(clerk).
body(clerk, not_stated) :- line(clerk).
line(harbourmaster).
kind(harbourmaster, harbourmaster) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(log).
kind(log, log) :- line(log).
body(log, not_stated) :- line(log).
line(read1).
holds(read(clerk, log)) :- line(read1).
line(wrote1).
holds(wrote(harbourmaster, log)) :- line(wrote1).
line(trawler).
kind(trawler, trawler) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(crossed).
holds(crossed(trawler, bar)) :- line(crossed).
line(turned).
holds(turned(tide)) :- line(turned).
line(because1).
claim_because(because1, crossed(trawler, bar), turned(tide)) :- line(because1).
line(boat).
kind(boat, boat) :- line(boat).
body(boat, not_stated) :- line(boat).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(lists_crew).
holds(lists(log, crew_of(boat))) :- line(lists_crew).
line(lists_weight).
holds(lists(log, weight_of(catch))) :- line(lists_weight).
line(boats).
kind(boats, boat) :- line(boats).
body(boats, not_stated) :- line(boats).
line(tied).
holds(tied_up(boats)) :- line(tied).
line(entry).
kind(entry, entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(concerns).
holds(concerns(entry, repairs)) :- line(concerns).
