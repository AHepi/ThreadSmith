% Written by OpenAI Codex, under plan 45, from the other model's corpus.
% The positive and negative claims use exactly the same effect and cause atoms.
line(1). line(2). line(3). line(4).
holds(fleaming_happened) :- line(1).
holds(opening_happened) :- line(2).
claim_because(3, opening_happened, fleaming_happened) :- line(3).
denied_because(4, opening_happened, fleaming_happened) :- line(4).

