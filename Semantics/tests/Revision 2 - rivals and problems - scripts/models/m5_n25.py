#!/usr/bin/env python3
"""M5 - N25, what holds the universe up: the dog and the turtle.

Target D: the universe. Input push (an admitted change inside the universe: something is moved) and
stuff (what the push moves); the query: held (does the universe stay up). The holder is outside: port
holder, which no admitted change reaches.
  dstuff  (push, stuff):   stuff = push
  dholder (holder,):       the holder is present
  dhold   (holder, held):  held iff the holder is present
Contract: the two admitted changes (push 0, push 1), baseline push 0. The answer is 'held' at both.
Candidates:
  dog     exists (dog,) {present} anchored to dholder; holds (dog, held) anchored to dhold.
  turtle  the same with 'turtle' (a label swap: "the same in every respect, except that it says a turtle").
  self    "the universe holds itself up; nothing holds it": one component (held,) {yes}, anchored to
          {dholder, dhold} (a different cut).
Anchoring readings: R-real (as above; the holder port stands for whatever holds it) and R-none (the
dog and turtle components anchored to no component of D).
"""
from engine import Org, Target, Cand, key, one_account, conflict, fits, problem, fmt_problem

PORTS = {'push': (0, 1), 'stuff': (0, 1), 'holder': ('present', 'absent'), 'held': ('yes', 'no')}
D = Target(Org('universe', PORTS,
               {'dstuff': (('push', 'stuff'), frozenset({(0, 0), (1, 1)})),
                'dholder': (('holder',), frozenset({('present',)})),
                'dhold': (('holder', 'held'), frozenset({('present', 'yes'), ('absent', 'no')}))}), 'held')
C = [{'push': 0}, {'push': 1}]
B0 = {'push': 0}


def show(x):
    return 'push=%d' % x['push']


def creature(name, real=True):
    ports = {'push': (0, 1), name: ('present', 'absent'), 'held': ('yes', 'no')}
    org = Org(name, ports, {'exists': ((name,), frozenset({('present',)})),
                            'holds': ((name, 'held'), frozenset({('present', 'yes'), ('absent', 'no')}))})
    A = (lambda s: s) if real else (lambda s: set())
    return Cand(name + ('' if real else '[R-none]'), org, 'held', lambda x: dict(x),
                lambda z, n=name: {'push': z['push'], n: z['holder'], 'held': z['held']},
                {'exists': (A({'dholder'}), {name: 'holder'}), 'holds': (A({'dhold'}), {name: 'holder', 'held': 'held'})},
                {'exists', 'holds'}, 'p')


def main():
    print('=' * 100)
    print('M5  N25, WHAT HOLDS THE UNIVERSE UP')
    print('=' * 100)
    DOG, TUR, DOG0, TUR0 = creature('dog'), creature('turtle'), creature('dog', False), creature('turtle', False)
    SELF = Cand('self', Org('self', {'push': (0, 1), 'held': ('yes', 'no')}, {'self': (('held',), frozenset({('yes',)}))}),
                'held', lambda x: dict(x), lambda z: {'push': z['push'], 'held': z['held']},
                {'self': ({'dholder', 'dhold'}, {'held': 'held'})}, {'self'}, 'p')
    EST = {key(x): ('ans', D.ans(x)) for x in C}
    for c in (DOG, TUR, SELF, DOG0, TUR0):
        print('  %-16s answers %s ; NonCircular=%-5s Account=%-5s fits (answers)=%-5s fits (answers + NonCircular)=%s' % (
            c.name, [sorted(c.ans(x)) for x in C], c.nc(C, B0), c.account(C, B0, D), fits(c, EST, D), fits(c, EST, D, nc=(C, B0))))
    print()
    for a, b, lab in ((DOG, TUR, 'dog vs turtle (R-real)'), (DOG0, TUR0, 'dog vs turtle (R-none)'),
                      (DOG, SELF, 'dog vs self (R-real)'), (DOG0, SELF, 'dog vs self (dog R-none)')):
        print('  %s' % lab)
        print(fmt_problem(problem(a, b, C, D, EST, offered=True), show))
        r2 = problem(a, b, C, D, EST, offered=True, nc=(C, B0))
        print('    with NonCircular counted in "fits": %s' % r2['verdict'])


if __name__ == '__main__':
    main()
