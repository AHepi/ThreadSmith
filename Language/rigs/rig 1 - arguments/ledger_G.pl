% ledger_G.pl - the owner's Markus paragraph, in rig 1's vocabulary, translated by the rulebook
line(1). line(2). line(3). line(4). line(5). line(6). line(7). line(8).
kind(markus, person) :- line(1).
holds(is_always(markus, crude_and_impolite)) :- line(2).
kind(the_wedding, wedding) :- line(3).
holds(does(markus, smash_cake, the_wedding)) :- line(4).
% line 5: a habit. USUALLY, and it SHOWS (it is a reason to expect, not a cause)
holds(does(markus, smash_cake, O)) :- line(5), kind(O, wedding), not exception(5, O).
exception(5, O) :- denied(does(markus, smash_cake, O)).
claim_since(6, does(markus, smash_cake, the_wedding), kind(the_wedding, wedding)) :- line(6).
claim_since(7, does(markus, smash_cake, the_wedding), is_always(markus, crude_and_impolite)) :- line(7).
holds(kind(X, K)) :- line(8), kind(X, K).
