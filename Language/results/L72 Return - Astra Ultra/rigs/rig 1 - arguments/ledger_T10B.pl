% Written by Astra Ultra under L72. T10-B independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(speaker).
kind(speaker, thing) :- line(speaker).
body(speaker, not_stated) :- line(speaker).
doer(speaker) :- line(speaker).
line(window).
kind(window, window) :- line(window).
body(window, not_stated) :- line(window).
line(letter).
kind(letter, letter) :- line(letter).
body(letter, not_stated) :- line(letter).
line(opening).
did(opening, speaker, open, window, not_stated) :- line(opening).
holds(opened(speaker, window)) :- line(opening).
line(plan).
claim_plan(plan, opening, stayed_dry(letter)) :- line(plan).
line(dry).
holds(stayed_dry(letter)) :- line(dry).
line(account).
kind(account, account) :- line(account).
body(account, not_stated) :- line(account).
line(noreason).
holds(gives_no_reason_for(account, dryness(letter))) :- line(noreason).
