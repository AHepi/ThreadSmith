% Written by OpenAI Codex under frozen plan 45.
% N03-B, new comparison side; actual-ledger standing is recorded in the sibling JSON.
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
