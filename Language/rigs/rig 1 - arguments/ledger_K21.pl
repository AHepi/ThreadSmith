% ledger_K21.pl - F21 withdraw a line, as against make it not so
line(1). line(2).
holds(rang(bell)) :- line(1).
holds(sleeps(guard)) :- line(2), denied(rang(bell)).
