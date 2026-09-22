% Written by Astra Ultra under L72. T10-D independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(account).
kind(account, account) :- line(account).
body(account, not_stated) :- line(account).
line(window).
kind(window, window) :- line(window).
body(window, not_stated) :- line(window).
line(letter).
kind(letter, letter) :- line(letter).
body(letter, not_stated) :- line(letter).
line(opening).
holds(opened(window)) :- line(opening).
line(dry).
holds(stayed_dry(letter)) :- line(dry).
line(because).
claim_because(because, stayed_dry(letter), opened(window)) :- line(because).
