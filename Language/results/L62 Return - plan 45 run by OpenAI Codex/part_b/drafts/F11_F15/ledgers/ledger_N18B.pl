% Written by OpenAI Codex, under plan 45, from the other model's corpus.
% Negative-only control: no claim_because/3 and no produced/1 route is added.
line(1). line(2). line(3).
holds(fleaming_happened) :- line(1).
holds(opening_happened) :- line(2).
denied_because(3, opening_happened, fleaming_happened) :- line(3).
