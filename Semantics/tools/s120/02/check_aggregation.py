#!/usr/bin/env python3
"""Synthetic counterexample: per-order shares are not same-sequence conjunctions."""
from measure_orders import summarize


source = {101: (5, "sequence-A"), 202: (5, "sequence-B")}
orders = []
for number in range(6):
    # Task x switches between two disjoint halves of the saved program population.
    # Task y stays in sequence A, whose replication flag fails in the last order.
    orders.append({101: (int(number != 5), (int(number < 3), 1)),
                   202: (1, (int(number >= 3), 0))})
result = summarize(source, orders, ["x", "y"])
per_order_x = [sum(source[key][0] for key in source if row[key][1][0] > 0)
               for row in orders]
assert per_order_x == [5] * 6
assert result["native_task_record"]["counts"] == [5, 5]
assert result["all6_task_record"]["counts"] == [0, 5]
assert result["all6_replication_pass"]["counts"] == [0, 0]
print("synthetic x: per-order counts=5,5,5,5,5,5; minimum=5; same-sequence all6=0")
print("synthetic y: all6 task-record count=5; all6 replication-pass count=0")

# The denominator is every saved program, including failed replication tests;
# the 10% boundary is inclusive and uses integer arithmetic.
edge = summarize({1: (1, "a"), 2: (9, "b")},
                 [{1: (1, (1,)), 2: (0, (0,))}] * 6, ["x"])
assert edge["all6_replication_pass"]["shares"] == [0.1]
assert edge["all6_replication_pass"]["common_count"] == 1
print("synthetic boundary: 1/10 remains common; failed tests stay in denominator")
