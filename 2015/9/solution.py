#! /usr/bin/python3

from itertools import permutations

places = set()
dists = dict()
with open("input") as f:
    for seg in [line.split() for line in f.readlines()]:
        places.add(seg[0])
        places.add(seg[2])
        dists.setdefault(seg[0],dict())[seg[2]] = int(seg[4])
        dists.setdefault(seg[2],dict())[seg[0]] = int(seg[4])

shortest = 10000000 # probably big enough
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: dists[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print(f'shortest: {shortest}')
print(f'longest: {longest}')

