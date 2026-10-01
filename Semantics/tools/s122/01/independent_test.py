"""Independent selector challenge cases; no Avida evolutionary run is performed."""
import copy
import json
import math

from temporal_selector.selector import Selector, UNITS


def population(k, rows):
    """Rows are (abundance share, world-order task set, all-order task set)."""
    assert math.isclose(sum(row[0] for row in rows), 1.0, abs_tol=1e-12)
    out = {"p": [0.0] * k, "q": [0.0] * k,
           "cooc": [[0.0] * k for _ in range(k)]}
    for weight, world, robust in rows:
        world, robust = set(world), set(robust)
        assert robust <= world
        for j in world:
            out["p"][j] += weight
        for j in robust:
            out["q"][j] += weight
            for i in robust:
                out["cooc"][j][i] += weight
    return out


def out(name, **values):
    def rounded(x):
        if isinstance(x, float):
            return round(x, 9)
        if isinstance(x, list):
            return [rounded(y) for y in x]
        return x
    print(name + ": " + json.dumps({k: rounded(v) for k, v in values.items()}, sort_keys=True))


def main():
    # Case 1: the observations come from a same-program pair, so cooc is physical.
    collective = Selector(2, eligible=[0, 1])
    initial = collective.step(population(2, [(0.1, [0, 1], [0, 1]), (0.9, [], [])]))
    for _ in range(40):
        final = collective.step(population(2, [(0.9, [0, 1], [0, 1]), (0.1, [], [])]))
    assert final["diagnostics"]["adaptation"][0] < initial["diagnostics"]["adaptation"][0]
    assert initial["pay"] == final["pay"] == [9.0, 9.0]
    out("collective_suppression", initial_adaptation=initial["diagnostics"]["adaptation"],
        final_adaptation=final["diagnostics"]["adaptation"], initial_pay=initial["pay"],
        final_pay=final["pay"])

    # Case 2: hold every contribution except latch and release response constant.
    disabled = set(UNITS) - {"latch", "rebound"}
    with_rebound = Selector(2, eligible=[0, 1], disabled=disabled)
    no_rebound = Selector(2, eligible=[0, 1], disabled=disabled | {"rebound"})
    bad = population(2, [(0.2, [0], []), (0.8, [], [])])
    resolved = population(2, [(0.1, [0], [0]), (0.1, [0], []), (0.8, [], [])])
    for selector in (with_rebound, no_rebound):
        selector.step(bad)
    before = with_rebound.step(resolved)
    no_rebound.step(resolved)
    after = with_rebound.step(resolved)
    removed = no_rebound.step(resolved)
    assert before["pay"][0] > after["pay"][0] > removed["pay"][0]
    assert after["diagnostics"]["release"] == [1, 0]
    out("release_response", latched_pay=before["pay"][0], released_pay=after["pay"][0],
        released_without_rebound_pay=removed["pay"][0],
        release_contribution=0.5 * after["diagnostics"]["rebound"][0])

    # Case 3: existing specialist proportions cross the threshold in opposite phases.
    oscillating = Selector(2, eligible=[0, 1], disabled=set(UNITS) - {"sequence"})
    stable = Selector(2, eligible=[0, 1], disabled=set(UNITS) - {"sequence"})
    responses, stable_responses = [], []
    for t in range(10):
        a, b = (0.101, 0.099) if t % 2 == 0 else (0.099, 0.101)
        result = oscillating.step(population(2, [(a, [0], [0]), (b, [1], [1]), (0.8, [], [])]))
        control = stable.step(population(2, [(0.101, [0], [0]), (0.101, [1], [1]), (0.798, [], [])]))
        responses.append(sum(result["diagnostics"]["sequence"]))
        stable_responses.append(sum(control["diagnostics"]["sequence"]))
    assert responses[0] == 0 and all(x > 0 for x in responses[1:])
    assert stable_responses == [0] * 10
    out("threshold_recrossing", sequence_responses=responses, stationary_responses=stable_responses,
        task_identities_present_throughout=2)

    # Case 4: only withheld incidences differ, including pair incidence and prior event.
    quiet = Selector(3, eligible=[0, 1])
    heldout = Selector(3, eligible=[0, 1])
    quiet_rows = [
        [(1.0, [], [])],
        [(0.2, [0], [0]), (0.8, [], [])],
        [(0.2, [0, 1], [0, 1]), (0.8, [], [])],
    ]
    heldout_rows = [
        [(0.3, [2], [2]), (0.7, [], [])],
        [(0.2, [0, 2], [0, 2]), (0.1, [2], [2]), (0.7, [], [])],
        [(0.2, [0, 1, 2], [0, 1, 2]), (0.8, [2], [])],
    ]
    differences = []
    for left, right in zip(quiet_rows, heldout_rows):
        a = quiet.step(population(3, left))
        b = heldout.step(population(3, right))
        assert a == b and quiet.state == heldout.state
        differences.append(max(abs(x - y) for x, y in zip(a["pay"], b["pay"])))
    out("heldout_mask", maximum_pay_difference_each_piece=differences)

    # Case 5: an offered schedule does not create a performed task.
    empty = Selector(77)
    for _ in range(200):
        nothing = empty.step(population(77, [(1.0, [], [])]))
    assert math.isclose(sum(nothing["pay"]), 18)
    out("empty_task_set", pieces=200, nominal_sum=sum(nothing["pay"]),
        offered_eligible_bonus=min(nothing["pay"][i] for i in empty.eligible),
        earned_log2_task_bonus_for_empty_set=sum(nothing["pay"][i] for i in []))

    # Case 6: absence cannot close the persistent problem.
    unresolved = Selector(2, eligible=[0, 1])
    for _ in range(200):
        result = unresolved.step(bad)
    assert result["diagnostics"]["latch"] == [1, 0]
    assert result["diagnostics"]["rebound"] == [0.0, 0.0]
    out("unresolved_latch", pieces=200, latch=result["diagnostics"]["latch"],
        rebound=result["diagnostics"]["rebound"], pay=result["pay"])

    # Case 7: serialize plain state, not the Python object or a generator seed.
    restored = Selector(2, eligible=[0, 1]).load(json.loads(json.dumps(unresolved.state)))
    for obs in (resolved, bad, resolved, resolved):
        assert unresolved.step(obs) == restored.step(obs)
    out("selector_continuation", equal_future_steps=4)

    # Case 8: joint membership changes while every marginal stays fixed.
    only_coincidence = set(UNITS) - {"coincidence"}
    specialist = Selector(3, eligible=[0, 1, 2], disabled=only_coincidence)
    pair = Selector(3, eligible=[0, 1, 2], disabled=only_coincidence)
    single_obs = population(3, [(0.25, [0], [0]), (0.25, [1], [1]),
                                (0.25, [2], [2]), (0.25, [], [])])
    pair_obs = population(3, [(0.25, [0, 1], [0, 1]), (0.25, [2], [2]), (0.5, [], [])])
    assert single_obs["p"] == pair_obs["p"] and single_obs["q"] == pair_obs["q"]
    one = specialist.step(single_obs)
    two = pair.step(pair_obs)
    assert one["diagnostics"]["coincidence"] == [0, 0, 0]
    assert two["pay"][0] > one["pay"][0] and two["pay"][2] < one["pay"][2]
    out("joint_membership", specialist_pay=one["pay"], pair_pay=two["pay"],
        specialist_coincidence=one["diagnostics"]["coincidence"],
        pair_coincidence=two["diagnostics"]["coincidence"])

    # Added after the initial run: common observed share and common trace differ.
    exact, nearby = Selector(2, eligible=[0, 1]), Selector(2, eligible=[0, 1])
    for _ in range(200):
        for selector, share in ((exact, 0.1), (nearby, 361 / 3600)):
            selector.step(population(2, [(share, [0], [0]), (1 - share, [], [])]))
    histories = [format(x.state["h"][0], ".17g") for x in (exact, nearby)]
    absence = population(2, [(1.0, [], [])])
    exact_loss, nearby_loss = exact.step(absence), nearby.step(absence)
    assert exact_loss["diagnostics"]["latch"] == [1, 0]
    assert nearby_loss["diagnostics"]["latch"] == [1, 0]
    out("common_threshold_loss", historical_traces=histories,
        exact_common_loss_latch=exact_loss["diagnostics"]["latch"],
        nearby_common_loss_latch=nearby_loss["diagnostics"]["latch"])

    # v1.2 regression neighbours, declared after the initial boundary finding.
    below = Selector(2, eligible=[0, 1])
    for _ in range(200):
        below.step(population(2, [(0.099, [0], [0]), (0.901, [], [])]))
    below_loss = below.step(absence)
    assert below_loss["diagnostics"]["latch"] == [0, 0]
    slow = Selector(2, eligible=[0, 1])
    for _ in range(10):
        slow.step(population(2, [(0.8, [0], [0]), (0.2, [], [])]))
    slow.step(population(2, [(0.05, [0], [0]), (0.95, [], [])]))
    slow_prior_q, slow_prior_h = slow.state["q"][0], slow.state["h"][0]
    assert slow_prior_q < 0.1 and slow_prior_h >= 0.1
    slow_loss = slow.step(absence)
    assert slow_loss["diagnostics"]["latch"] == [1, 0]
    transient = Selector(2, eligible=[0, 1])
    transient.step(population(2, [(0.1, [0], [0]), (0.9, [], [])]))
    transient_loss = transient.step(absence)
    assert transient_loss["diagnostics"]["latch"] == [1, 0]
    out("loss_amendment_neighbours", below_common_loss_latch=below_loss["diagnostics"]["latch"],
        slow_prior_q=slow_prior_q, slow_prior_h=slow_prior_h,
        slow_loss_latch=slow_loss["diagnostics"]["latch"],
        one_piece_common_loss_latch=transient_loss["diagnostics"]["latch"])
    print("Audit cases completed. No Avida evolutionary run was performed.")


if __name__ == "__main__":
    main()
