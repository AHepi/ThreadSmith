% Written by OpenAI Codex under frozen plan 45.
% T02-B, new comparison side; actual-ledger standing is recorded in the sibling JSON.
line(k).
kind(kingfisher, kingfisher) :- line(k).
line(f).
kind(feathers, feathers) :- line(f).
line(o).
holds(belong_to(feathers, kingfisher)) :- line(o).
line(u).
holds(unharmed(feathers)) :- line(u).
