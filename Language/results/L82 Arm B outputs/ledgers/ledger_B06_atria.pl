% ledger_B06_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(clerk).
kind(clerk, dockyard_clerk) :- line(clerk).
body(clerk, not_stated) :- line(clerk).
line(log).
kind(log, log) :- line(log).
body(log, not_stated) :- line(log).
line(harbourmaster).
kind(harbourmaster, harbourmaster) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(read).
holds(read_through(clerk, log)) :- line(read).
line(owns).
holds(owned_by(log, harbourmaster)) :- line(owns).
line(crew).
kind(crew, crew) :- line(crew).
body(crew, not_stated) :- line(crew).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(record_names).
holds(records_names(log, crew)) :- line(record_names).
line(record_weight).
holds(records_weight(log, catch)) :- line(record_weight).
line(entry).
kind(entry, entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(repairs).
kind(repairs, repairs) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(north_pier).
kind(north_pier, pier) :- line(north_pier).
body(north_pier, not_stated) :- line(north_pier).
line(concern).
holds(concerns(entry, repairs(north_pier))) :- line(concern).
line(trawler).
kind(trawler, trawler) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(harbour).
kind(harbour, harbour) :- line(harbour).
body(harbour, not_stated) :- line(harbour).
line(loaded_boat).
kind(loaded_boat, loaded_boat) :- line(loaded_boat).
body(loaded_boat, not_stated) :- line(loaded_boat).
line(tide_turned).
holds(turned(tide)) :- line(tide_turned).
line(crossing).
holds(crossed_bar(trawler)) :- line(crossing).
line(because).
claim_because(because, crossed_bar(trawler), turned(tide)) :- line(because).
line(general).
produced(crossed_bar(B)) :- line(general), kind(B, loaded_boat), holds(at_harbour(B)), holds(turned(tide)).
depends(crossed_bar(B), turned(tide)) :- line(general), kind(B, loaded_boat), holds(at_harbour(B)).
line(boats).
kind(boats, boat) :- line(boats).
body(boats, not_stated) :- line(boats).
line(tied_up).
holds(tied_up(boats)) :- line(tied_up).
