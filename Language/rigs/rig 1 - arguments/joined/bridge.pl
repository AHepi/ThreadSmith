% bridge.pl
% What this file does: joins the two rigs. It lets a BECAUSE in rig 1 be tested by rig 2's laws of pressing.
#pred happened(E) :: 'happening @(E) took place'.
% a happening the writer stated took place
holds(happened(E)) :- did(E, _, _, _, _).
% a movement the writer stated is so
holds(moves(T, D)) :- said_moves(_, T, D).
% a movement is PRODUCED only when some stated happening could, by the laws of pressing, have produced it
produced(moves(T, D)) :- did(E, _, _, _, _), result_possible(E, T, D).
