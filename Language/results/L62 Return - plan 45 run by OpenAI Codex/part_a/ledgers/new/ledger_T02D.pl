% Written by OpenAI Codex under frozen plan 45.
% T02-D, new comparison side; actual-ledger standing is recorded in the sibling JSON.
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
