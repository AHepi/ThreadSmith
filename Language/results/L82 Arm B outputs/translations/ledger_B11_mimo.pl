% ledger_B11_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(clerk).
kind(dockyard_clerk, person) :- line(clerk).
body(dockyard_clerk, not_stated) :- line(clerk).
line(harbourmaster).
kind(harbourmaster, person) :- line(harbourmaster).
body(harbourmaster, not_stated) :- line(harbourmaster).
line(log).
kind(log, log) :- line(log).
body(log, not_stated) :- line(log).
line(logown).
holds(kept_by(log, harbourmaster)) :- line(logown).
line(p1).
holds(read(dockyard_clerk, log)) :- line(p1).
line(trawler).
kind(trawler, boat) :- line(trawler).
body(trawler, not_stated) :- line(trawler).
line(bar).
kind(bar, bar) :- line(bar).
body(bar, not_stated) :- line(bar).
line(tide).
kind(tide, tide) :- line(tide).
body(tide, not_stated) :- line(tide).
line(turn).
holds(turned(tide)) :- line(turn).
line(p2).
holds(crossed(trawler, bar)) :- line(p2).
line(cause1).
claim_because(cause1, crossed(trawler, bar), turned(tide)) :- line(cause1).
line(catch).
kind(catch, catch) :- line(catch).
body(catch, not_stated) :- line(catch).
line(crewed).
holds(had_crew(trawler)) :- line(crewed).
line(weighed).
holds(had_weight(catch)) :- line(weighed).
line(boats).
kind(boats, boat) :- line(boats).
body(boats, not_stated) :- line(boats).
line(p3).
holds(tied_up(boats)) :- line(p3).
line(entry).
kind(entry, entry) :- line(entry).
body(entry, not_stated) :- line(entry).
line(entrylink).
holds(entry_of(entry, log)) :- line(entrylink).
line(north_pier).
kind(north_pier, pier) :- line(north_pier).
body(north_pier, not_stated) :- line(north_pier).
line(repairs).
kind(repairs, repair_job) :- line(repairs).
body(repairs, not_stated) :- line(repairs).
line(due).
holds(due_on(repairs, north_pier)) :- line(due).
