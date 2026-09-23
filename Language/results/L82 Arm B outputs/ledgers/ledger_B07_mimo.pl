% ledger_B07_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(shop).
kind(shopkeeper, shopkeeper) :- line(shop).
body(shopkeeper, heavy_and_standing) :- line(shop).
line(take).
kind(stocktaker, stocktaker) :- line(take).
body(stocktaker, heavy_and_standing) :- line(take).
line(t1).
holds(told(shopkeeper, stocktaker)) :- line(t1).
line(tin).
kind(tinned_fruit, new_delivery_of_tinned_fruit) :- line(tin).
body(tinned_fruit, not_stated) :- line(tin).
line(shelf).
kind(middle_shelf, shelf) :- line(shelf).
body(middle_shelf, not_stated) :- line(shelf).
line(win).
kind(window, window) :- line(win).
body(window, not_stated) :- line(win).
line(t2).
holds(described(shopkeeper, tinned_fruit)) :- line(t2).
line(stack).
holds(stacked_on(tinned_fruit, middle_shelf)) :- line(stack).
line(bywin).
holds(by_the_window(middle_shelf)) :- line(bywin).
line(t3).
holds(listed(shopkeeper, candles)) :- line(t3).
holds(listed(shopkeeper, matches)) :- line(t3).
holds(listed(shopkeeper, paper)) :- line(t3).
line(candle).
kind(candles, candle) :- line(candle).
body(candles, not_stated) :- line(candle).
line(match).
kind(matches, match) :- line(match).
body(matches, not_stated) :- line(match).
line(paper).
kind(paper, writing_paper) :- line(paper).
body(paper, not_stated) :- line(paper).
line(lowc).
holds(running_low(candles)) :- line(lowc).
line(lowm).
holds(running_low(matches)) :- line(lowm).
line(lowp).
holds(running_low(paper)) :- line(lowp).
line(t4).
holds(mentioned(shopkeeper, van)) :- line(t4).
line(van).
kind(van, delivery_van) :- line(van).
body(van, not_stated) :- line(van).
line(va1).
holds(arrived(van, tuesday)) :- line(va1).
line(num).
kind(shelf_numbers, shelf_number) :- line(num).
body(shelf_numbers, not_stated) :- line(num).
line(w1).
holds(wrote_down(stocktaker, shelf_numbers)) :- line(w1).
line(sp1).
holds(spoke_during(shopkeeper, w1)) :- line(sp1).
