#!/usr/bin/env python3
"""Written by Claude (log S115), not by Astra. Rewrites one S113 saved program population
(piece_PP/data/detail-1000.spop) so that its update_born column holds the update counted from
the start of the whole run, not from the start of the piece in which the group was born.

Why: S113 restarts Avida at every piece, so update_born in a save is piece-local (0 to 1000),
while group IDs are renumbered at every reload in the order the groups were created. Sorted by
ID, update_born therefore falls back exactly once at each piece boundary. With the piece of the
save known (PP), the piece of each group is the number of fall-backs before it. The rewrite is
refused (exit 1) when the number of fall-backs differs from PP, because then a boundary is hidden.
The Avida ancestor (update_born -1) is given 0. Nothing else in the file is changed.

Usage: python3 s115_give_s113_snapshots_global_birth_updates.py IN.spop PIECE OUT.spop
"""
import sys

def main(src, piece, dst):
    piece = int(piece)
    lines = open(src).read().splitlines()
    cols = next(l.split()[1:] for l in lines if l.startswith('#format '))
    iu, ii = cols.index('update_born'), cols.index('id')
    data = [(n, l.split()) for n, l in enumerate(lines) if l.strip() and not l.startswith('#')]
    order = sorted(data, key=lambda x: int(x[1][ii]))
    drops, last, piece_of = 0, None, {}
    for n, v in order:
        u = int(v[iu])
        if last is not None and u < last and u >= 0:
            drops += 1
        piece_of[n] = drops
        if u >= 0:
            last = u
    if drops != piece:
        sys.exit(f'{src}: {drops} fall-backs in update_born, expected {piece}; not rewritten')
    out = []
    for n, l in enumerate(lines):
        if not l.strip() or l.startswith('#'):
            out.append(l)
            continue
        v = l.split()
        u = int(v[iu])
        v[iu] = str(0 if u < 0 else 1000 * piece_of[n] + u)
        out.append(' '.join(v))
    open(dst, 'w').write('\n'.join(out) + '\n')
    print(f'{dst}: {len(data)} groups, pieces 0..{piece}')

if __name__ == '__main__':
    main(*sys.argv[1:])
