% ledger_B06_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(clerk).
kind(clerk, dockyard_clerk) :- line(clerk).
body(clerk, not_stated) :- line(clerk).
line(harbourlog).
kind(harbour_log, log) :- line(harbourlog).
body(harbour_log, not_stated) :- line(harbourlog).
line(fread).
holds(read_through(clerk, harbour_log)) :- line(fread).
line(harbourmaster).
kind(harbourmaster, harbourmaster) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(fwrite).
holds(wrote_in(harbourmaster, harbour_log)) :- line(fwrite).
line(fadd).
holds(added_to(harbourmaster, harbour_log)) :- line(fadd).
line(trawler).
kind(trawler, trawler) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(cross1).
holds(crossed_bar_early(trawler)) :- line(cross1).
line(turn1).
holds(turned(tide)) :- line(turn1).
line(cause1).
claim_because(cause1, crossed_bar_early(trawler), turned(tide)) :- line(cause1).
line(loadedboat).
kind(loaded_boat, boat) :- line(loadedboat).
body(loaded_boat, not_stated) :- line(loadedboat).
line(harbourthing).
kind(harbour, harbour) :- line(harbourthing).
body(harbour, not_stated) :- line(harbourthing).
line(rule1).
produced(crossed_bar_early(X)) :- line(rule1), kind(X, boat), holds(loaded(X)), holds(at_harbour(X)), holds(turns_before_dawn(tide)).
depends(crossed_bar_early(X), turns_before_dawn(tide)) :- line(rule1), kind(X, boat).
depends(crossed_bar_early(X), loaded(X)) :- line(rule1), kind(X, boat).
depends(crossed_bar_early(X), at_harbour(X)) :- line(rule1), kind(X, boat).
line(crew).
kind(crew, crew) :- line(crew).
body(crew, not_stated) :- line(crew).
line(thecatch).
kind(the_catch, catch) :- line(thecatch).
body(the_catch, not_stated) :- line(thecatch).
line(frec1).
holds(records(harbour_log, names_of(crew))) :- line(frec1).
line(frec2).
holds(records(harbour_log, weight_of(the_catch))) :- line(frec2).
line(countedboats).
kind(counted_boats, boat) :- line(countedboats).
body(counted_boats, not_stated) :- line(countedboats).
line(tied1).
holds(tied_up_before_noon(counted_boats)) :- line(tied1).
line(fnote).
holds(noted_from_own_count(clerk)) :- line(fnote).
line(entrything).
kind(entry, entry) :- line(entrything).
body(entry, not_stated) :- line(entrything).
line(repairs).
kind(repairs, repair) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(northpier).
kind(north_pier, pier) :- line(northpier).
body(north_pier, not_stated) :- line(northpier).
line(fconcern).
holds(rest_concerns_repairs(entry, repairs, north_pier)) :- line(fconcern).
line(flink).
holds(entry_in(entry, harbour_log)) :- line(flink).
