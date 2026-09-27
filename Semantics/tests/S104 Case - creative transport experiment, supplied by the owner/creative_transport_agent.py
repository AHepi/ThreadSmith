#!/usr/bin/env python3
"""A small, reproducible transport-composition agent and adversarial tests.

Python 3.10+, standard library only. No model/API calls, no pretrained solution.
Run: python creative_transport_agent.py --out results.json

The constructor has only two generic input terminals, x and y, and NAND.
It archives one expression per complete two-input Boolean behaviour, composes
archived expressions, and evaluates paired sender/receiver programs. The
only allowed interface expansion is access to the previous received level.
That expansion and the task are supplied by the designer, not invented.

This is an intentionally bounded constructive-search demonstration, not
an empirical test of general human creativity or an autonomous LLM agent.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Expr:
    op: str
    left: Expr | None = None
    right: Expr | None = None

    def run(self, x: int, y: int) -> int:
        if self.op == 'x':
            return x
        if self.op == 'y':
            return y
        assert self.left is not None and self.right is not None
        return 1 - (self.left.run(x, y) & self.right.run(x, y))

    @property
    def signature(self) -> tuple[int, ...]:
        return tuple(self.run(x, y) for x, y in product((0, 1), repeat=2))

    @property
    def gates(self) -> int:
        if self.op != 'N':
            return 0
        assert self.left is not None and self.right is not None
        return 1 + self.left.gates + self.right.gates

    def text(self) -> str:
        if self.op != 'N':
            return self.op
        assert self.left is not None and self.right is not None
        return f'N({self.left.text()},{self.right.text()})'

    @property
    def key(self) -> tuple[int, str]:
        return self.gates, self.text()


def grow_library() -> tuple[list[list[Expr]], list[dict]]:
    """Enumerate a NAND closure, retaining behaviorally distinct parts.

    Representatives are simplified by expression-tree gate count; equivalent
    behaviors can substitute in any Boolean context in this tiny total domain.
    No correctness target, XOR primitive or endpoint solution is used here.
    """
    archive = {e.signature: e for e in (Expr('x'), Expr('y'))}
    snapshots: list[list[Expr]] = []
    log: list[dict] = []
    for round_no in range(10):
        values = sorted(archive.values(), key=lambda e: e.key)
        snapshots.append(values)
        log.append({'round': round_no, 'distinct_behaviors': len(values)})
        old = dict(archive)
        for left, right in product(values, repeat=2):
            expr = Expr('N', left, right)
            sig = expr.signature
            if sig not in archive or expr.key < archive[sig].key:
                archive[sig] = expr
        if archive == old:
            return snapshots, log
    raise RuntimeError('Boolean library did not reach closure in 10 rounds.')


# Full local task table: message bit, previous sent level, channel polarity.
FULL_CASES = tuple(product((0, 1), repeat=3))
NORMAL_ONLY = tuple(c for c in FULL_CASES if c[2] == 0)


def observations(encoder: Expr, message: int, previous_sent: int,
                 polarity: int, history: bool) -> tuple[int, int]:
    sent = encoder.run(previous_sent, message)
    current_received = sent ^ polarity
    previous_received = previous_sent ^ polarity
    # No-history means the first receiver port is disconnected and tied to 0.
    return previous_received if history else 0, current_received


def evaluate(encoder: Expr, decoder: Expr, *, history: bool = True,
             cases: Iterable[tuple[int, int, int]] = FULL_CASES) -> tuple[int, ...]:
    return tuple(int(decoder.run(*observations(encoder, m, s, b, history)) == m)
                 for m, s, b in cases)


def rank_pair(pair: tuple[Expr, Expr], *, history: bool = True,
              cases: Iterable[tuple[int, int, int]] = FULL_CASES) -> tuple:
    encoder, decoder = pair
    bits = evaluate(encoder, decoder, history=history, cases=cases)
    # Higher task performance first; then lower implementation cost.
    return (-sum(bits), encoder.gates + decoder.gates,
            encoder.text(), decoder.text())


def best_pair(library: list[Expr], *, history: bool = True,
              cases: Iterable[tuple[int, int, int]] = FULL_CASES) -> tuple[Expr, Expr]:
    return min(product(library, repeat=2),
               key=lambda pair: rank_pair(pair, history=history, cases=cases))


def fraction(pair: tuple[Expr, Expr], **kwargs) -> float:
    bits = evaluate(*pair, **kwargs)
    return sum(bits) / len(bits)


def pair_record(pair: tuple[Expr, Expr], **kwargs) -> dict:
    encoder, decoder = pair
    return {
        'encoder': encoder.text(), 'decoder': decoder.text(),
        'encoder_truth_table_00_01_10_11': encoder.signature,
        'decoder_truth_table_00_01_10_11': decoder.signature,
        'nand_tree_gates': encoder.gates + decoder.gates,
        'accuracy': fraction(pair, **kwargs),
    }


def greedy_endpoint_search(library: list[Expr]) -> dict:
    """Only accept a strict improvement, changing one endpoint at a time."""
    current = (Expr('y'), Expr('y'))  # Send message directly, read current level.
    evaluated = 0
    moves = 0
    while True:
        neighbors = [(e, current[1]) for e in library]
        neighbors += [(current[0], d) for d in library]
        evaluated += len(neighbors)
        candidate = min(neighbors, key=rank_pair)
        if fraction(candidate) <= fraction(current):
            return {'endpoint_alternatives_tested': evaluated,
                    'accepted_moves': moves, **pair_record(current)}
        current = candidate
        moves += 1


def verify_streams(pair: tuple[Expr, Expr], length: int = 12) -> dict:
    """Check every length-12 word, both starting levels and both polarities.

    The receiver first observes one pilot/reference level. No known polarity
    is supplied. These longer messages are not used during synthesis.
    """
    encoder, decoder = pair
    streams = bit_count = bit_errors = failed_streams = 0
    for message in product((0, 1), repeat=length):
        for initial, polarity in product((0, 1), repeat=2):
            sent = initial
            previous_received = initial ^ polarity
            failed = False
            for bit in message:
                sent = encoder.run(sent, bit)
                received = sent ^ polarity
                recovered = decoder.run(previous_received, received)
                error = int(recovered != bit)
                bit_errors += error
                bit_count += 1
                failed = failed or bool(error)
                previous_received = received
            streams += 1
            failed_streams += int(failed)
    return {'message_length': length, 'streams': streams,
            'bits': bit_count, 'bit_errors': bit_errors,
            'failed_streams': failed_streams,
            'accuracy': 1 - bit_errors / bit_count,
            'initialization': 'One received reference level before payload.'}


def changing_polarity_test(pair: tuple[Expr, Expr]) -> dict:
    encoder, decoder = pair
    errors = 0
    n = 0
    for message, previous_sent, previous_polarity, current_polarity in product((0, 1), repeat=4):
        sent = encoder.run(previous_sent, message)
        recovered = decoder.run(previous_sent ^ previous_polarity,
                                sent ^ current_polarity)
        errors += int(recovered != message)
        n += 1
    return {'cases': n, 'errors': errors, 'accuracy': 1 - errors / n,
            'assumption_changed': 'Polarity may change between adjacent levels.'}


def missing_reference_test(pair: tuple[Expr, Expr]) -> dict:
    encoder, decoder = pair
    errors = 0
    for message, previous_sent, polarity in FULL_CASES:
        received = encoder.run(previous_sent, message) ^ polarity
        recovered = decoder.run(0, received)  # Arbitrary assumed initial reference.
        errors += int(recovered != message)
    return {'first_bit_cases': 8, 'first_bit_errors': errors,
            'first_bit_accuracy': 1 - errors / 8}


def run() -> dict:
    snapshots, build_log = grow_library()
    library = snapshots[-1]
    assert len(library) == 16

    # Agent starts with a narrower receiver interface. Saturation triggers
    # the sole supplied extension: expose the previous received level.
    seen_by_mode: dict[bool, set[tuple[tuple[int, ...], tuple[int, ...]]]] = {False:set(), True:set()}
    trajectory = []
    chosen = None
    for history in (False, True):
        for round_no, parts in enumerate(snapshots):
            for encoder, decoder in product(parts, repeat=2):
                seen_by_mode[history].add((encoder.signature, decoder.signature))
            winner = best_pair(parts, history=history)
            trajectory.append({'receiver_history': history, 'round': round_no,
                               'parts': len(parts),
                               'distinct_program_pairs_available': len(parts)**2,
                               **pair_record(winner, history=history)})
            if fraction(winner, history=history) == 1:
                chosen = winner
                break
        if chosen is not None:
            break
    assert chosen is not None

    pair_records = []
    for e, d in product(library, repeat=2):
        pair_records.append(pair_record((e, d)))
    histogram = Counter(sum(evaluate(e,d)) for e,d in product(library, repeat=2))
    perfect = [r for r in pair_records if r['accuracy'] == 1]
    no_history = best_pair(library, history=False)
    no_composite_reuse = best_pair(snapshots[1])
    naive_training_winner = best_pair(library, cases=NORMAL_ONLY)
    fixed_sender_best = max(fraction((Expr('y'), d)) for d in library)
    fixed_receiver_best = max(fraction((e, Expr('y'))) for e in library)

    result = {
        'experiment': 'NAND-program synthesis of a polarity-robust binary protocol',
        'scope': 'Small, exhaustive symbolic agent; not an LLM benchmark or world-novel invention.',
        'designer_supplied': [
            'A binary channel and message-recovery goal.',
            'Two input terminals and the NAND composition operator.',
            'One-bit sender state and an optional one-bit receiver-history port.',
            'Behavioral archive, exhaustive search, finite task table, and selection rules.',
            'Synchronized symbol boundaries and a starting received reference level.'
        ],
        'library_growth': build_log,
        'trajectory': trajectory,
        'selected_protocol': pair_record(chosen),
        'perfect_pairs_out_of_256': perfect,
        'score_histogram_correct_out_of_8': dict(sorted(histogram.items())),
        'no_history_best': pair_record(no_history, history=False),
        'no_composite_reuse_best': pair_record(no_composite_reuse),
        'greedy_one_endpoint_at_a_time': greedy_endpoint_search(library),
        'fixed_sender_best_accuracy': fixed_sender_best,
        'fixed_receiver_best_accuracy': fixed_receiver_best,
        'normal_only_training': {
            'selected': pair_record(naive_training_winner, cases=NORMAL_ONLY),
            'both_polarities_accuracy': fraction(naive_training_winner),
            'inverted_polarity_accuracy': fraction(naive_training_winner,
                cases=tuple(c for c in FULL_CASES if c[2] == 1)),
        },
        'longer_stream_verification': verify_streams(chosen),
        'changing_polarity': changing_polarity_test(chosen),
        'missing_initial_reference': missing_reference_test(chosen),
        'all_256_pair_results': pair_records,
    }
    assert result['longer_stream_verification']['bit_errors'] == 0
    assert result['no_history_best']['accuracy'] == 0.5
    assert len(perfect) == 2
    assert result['changing_polarity']['accuracy'] == 0.5
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    result = run()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    short = {k:v for k,v in result.items() if k not in {'all_256_pair_results','trajectory'}}
    print(json.dumps(short, indent=2))
    print(f'\nFull results written to {args.out}')


if __name__ == '__main__':
    main()
