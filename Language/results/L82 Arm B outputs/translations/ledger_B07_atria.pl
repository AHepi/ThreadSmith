% ledger_B07_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(s1).
kind(shopkeeper, person) :- line(s1).
body(shopkeeper, not_stated) :- line(s1).
line(s2).
kind(stocktaker, person) :- line(s2).
body(stocktaker, not_stated) :- line(s2).
line(s3).
kind(shelf_numbers, numbers) :- line(s3).
body(shelf_numbers, not_stated) :- line(s3).
line(s4).
holds(wrote_down(stocktaker, shelf_numbers)) :- line(s4).
line(t1).
kind(stock, goods) :- line(t1).
body(stock, not_stated) :- line(t1).
line(t2).
holds(came_in(stock)) :- line(t2).
line(t3).
kind(delivery, consignment_of_tinned_fruit) :- line(t3).
body(delivery, not_stated) :- line(t3).
line(t4).
kind(middle_shelf, shelf) :- line(t4).
body(middle_shelf, not_stated) :- line(t4).
line(t5).
kind(window, window) :- line(t5).
body(window, not_stated) :- line(t5).
line(t6).
holds(stacked_on_middle_shelf_by_window(delivery)) :- line(t6).
line(t7).
kind(candles, goods) :- line(t7).
body(candles, not_stated) :- line(t7).
line(t8).
kind(matches, goods) :- line(t8).
body(matches, not_stated) :- line(t8).
line(t9).
kind(writing_paper, goods) :- line(t9).
body(writing_paper, not_stated) :- line(t9).
line(t10).
holds(running_low(candles)) :- line(t10).
line(t11).
holds(running_low(matches)) :- line(t11).
line(t12).
holds(running_low(writing_paper)) :- line(t12).
line(t13).
kind(delivery_van, van) :- line(t13).
body(delivery_van, not_stated) :- line(t13).
line(t14).
holds(arrived(delivery_van)) :- line(t14).
