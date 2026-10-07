# Case 01: memory improves planning

From an engineer's results summary:

"Our planner chooses among up to 8 supplied action programs for a simulated robot arm pushing a puck. A cheap learned predictor ranks the programs; an exact simulator then checks them in ranked order and picks the first that reaches the goal in every physics model in our supplied model list. The new predictor keeps two running totals of the applied forces (force summed, and that sum summed again) and maps them to positions with 16 learned numbers. We compared five ranking arms on our fixed 8-case benchmark: new predictor, a predictor without the running totals, the new predictor with its numbers set to zero, fixed order, and lowest-effort-first. Results: exact checks needed 9 / 11 / 12 / 12 / 12; supported program on the first try 7/8, 5/8, 4/8, 4/8, 4/8. Prediction error was 82% lower than the predictor without totals, over 672 coordinates. All arms were trained on the same five lessons. We conclude that learned persistent memory makes planning more efficient, and that the exact check guarantees every chosen program reaches the goal."

Task: before this conclusion is accepted, what must be questioned or tested?
