% Prepared export of the original table for plan 45.
% NOT an independent translation, NOT a comparison result.
% No semantic checker or Prolog parser has run on this export.
line(k).
kind(kingfisher, kingfisher) :- line(k).
line(f).
kind(feathers, feathers) :- line(f).
line(o).
holds(belong_to(feathers, kingfisher)) :- line(o).
line(u).
holds(unharmed(feathers)) :- line(u).
line(d).
holds(subject_of_colour_description(feathers, mara)) :- line(d).
