#! /usr/bin/python3

from itertools import product
from math import ceil

weapons = [
    (8,4,0),
    (10,5,0),
    (25,6,0),
    (40,7,0),
    (74,8,0)
]

armor = [
    (0,0,0),
    (13,0,1),
    (31,0,2),
    (53,0,3),
    (75,0,4),
    (102,0,5)
]

rings = [
    (0,0,0),
    (0,0,0),
    (25,1,0),
    (50,2,0),
    (100,3,0),
    (20,0,1),
    (40,0,2),
    (80,0,3)
]

boss = (100,8,2) # This is my input

def turns_to_kill(a,t): return ceil(t[0] / max(a[1] - t[2], 1))

def p1_wins(p1,p2): return turns_to_kill(p1,p2) <= turns_to_kill(p2,p1)

p_1 = 500
p_2 = 0
for e in product(weapons, armor, rings, rings):
    cost = sum(i[0] for i in e)
    me = (100, sum(i[1] for i in e), sum(i[2] for i in e))

    if p1_wins(me, boss) and cost < p_1: p_1 = cost
    elif not p1_wins(me,boss) and cost > p_2: p_2 = cost

print(f'Part 1: {p_1}')
print(f'Part 2: {p_2}')
