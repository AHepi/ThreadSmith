% Prepared export of the original table for plan 45.
% NOT an independent translation, NOT a comparison result.
% No semantic checker or Prolog parser has run on this export.
line(a).
kind(painter, painter) :- line(a).
line(p).
kind(pear, pear) :- line(p).
line(f).
kind(finger, finger) :- line(f).
line(r).
holds(red_stained(finger)) :- line(r).
line(t).
did(t, painter, touched, pear, none) :- line(t).
