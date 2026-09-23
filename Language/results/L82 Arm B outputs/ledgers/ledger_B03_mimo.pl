% ledger_B03_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(clerk).
kind(clerk, person) :- line(clerk).
body(clerk, not_stated) :- line(clerk).
line(log).
kind(log, log) :- line(log).
body(log, not_stated) :- line(log).
line(harbourmaster).
kind(harbourmaster, person) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(poss1).
holds(belongs_to(log, harbourmaster)) :- line(poss1).
line(read1).
holds(reads_through(clerk, log)) :- line(read1).
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
holds(crosses(trawler, bar)) :- line(cross1).
line(across1).
holds(moves(trawler, across(bar))) :- line(across1).
line(turn1).
holds(turns(tide)) :- line(turn1).
line(turned1).
holds(becomes(tide, turned)) :- line(turned1).
line(cause1).
claim_because(cause1, crosses(trawler,bar), becomes(tide,turned)) :- line(cause1).
line(crew).
kind(crew, group) :- line(crew).
body(crew, not_stated) :- line(crew).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(rec1).
holds(records(log, crew_names)) :- line(rec1).
line(rec2).
holds(records(log, catch_weight)) :- line(rec2).
line(boats).
kind(boats, boat) :- line(boats).
body(boats, not_stated) :- line(boats).
line(tie1).
holds(tied_up(boats)) :- line(tie1).
line(entry).
kind(entry, entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(entryof).
holds(entry_of(entry, log)) :- line(entryof).
line(repairs).
kind(repairs, repair_job) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(northpier).
kind(northpier, pier) :- line(northpier).
body(northpier, not_stated) :- line(northpier).
line(concern1).
holds(concerns(entry, repairs)) :- line(concern1).
line(due1).
holds(due_on(repairs, northpier)) :- line(due1).
