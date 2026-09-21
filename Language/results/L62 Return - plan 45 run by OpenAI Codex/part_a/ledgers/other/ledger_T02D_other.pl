% Prepared export of the original table for plan 45.
% NOT an independent translation, NOT a comparison result.
% No semantic checker or Prolog parser has run on this export.
line(k).
kind(kingfisher, kingfisher) :- line(k).
line(f).
kind(feathers, feathers) :- line(f).
line(o).
holds(belong_to(feathers, kingfisher)) :- line(o).
line(s).
kind(spark, spark) :- line(s).
line(p).
did(p, spark, struck, feathers, none) :- line(p).
line(c).
holds(caught_fire(kingfisher)) :- line(c).
line(b).
holds(burned(feathers)) :- line(b).
