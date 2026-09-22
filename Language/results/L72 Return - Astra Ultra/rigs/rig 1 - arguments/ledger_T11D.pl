% Written by Astra Ultra under L72. T11-D independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(lamp).
kind(lamp, lamp) :- line(lamp).
body(lamp, not_stated) :- line(lamp).
line(burning).
holds(burning(lamp)) :- line(burning).
line(visitor).
kind(visitor, visitor) :- line(visitor).
body(visitor, not_stated) :- line(visitor).
line(drawing).
did(drawing, lamp, draw, visitor, not_stated) :- line(drawing).
holds(drew_back(lamp, visitor)) :- line(drawing).
line(return).
holds(returned(visitor)) :- line(return).
line(because).
claim_because(because, returned(visitor), drew_back(lamp, visitor)) :- line(because).
