% Written by Astra Ultra under L72. T11-B independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(lamp).
kind(lamp, lamp) :- line(lamp).
body(lamp, not_stated) :- line(lamp).
line(burning).
holds(burning(lamp)) :- line(burning).
line(toldlamp).
kind(lamp, lamp) :- line(toldlamp).
body(lamp, not_stated) :- line(toldlamp).
line(toldburning).
holds(burning(lamp)) :- line(toldburning).
line(toldvisitor).
kind(visitor, visitor) :- line(toldvisitor).
body(visitor, not_stated) :- line(toldvisitor).
line(toldreturn).
holds(returned(visitor)) :- line(toldreturn).
line(since).
claim_since(since, returned(visitor), burning(lamp)) :- line(since).
line(visitor).
kind(visitor, visitor) :- line(visitor).
body(visitor, not_stated) :- line(visitor).
line(return).
holds(returned(visitor)) :- line(return).
line(notbecause).
denied_because(notbecause, returned(visitor), burning(lamp)) :- line(notbecause).
