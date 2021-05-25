#! /usr/bin/python

from itertools import combinations

with open('input') as f:
    bottles = list(map(int, f.readlines()))

    p1 = 0
    p2 = 0
    for b in range(len(bottles)):
            for c in combinations(bottles, b + 1):
                p1 += ( sum(c) == 150)
            p2 = p2 if p2 else p1

    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')

