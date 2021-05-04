#! /usr/bin/python3

from itertools import permutations

def compute_happy(names, mods):
    optimal = 0

    for items in permutations(names):
        rr = items[1:] + items[:1]
        rl = items[-1:] + items[:-1]
        optimal = max(optimal, sum([mods[z[1]][z[0]] + mods[z[1]][z[2]] for z in zip(rl, items,rr)]))
    
    return optimal

names = set()
happy = dict()
with open("input") as f:
    for seg in [line.split() for line in f.readlines()]:
        name = seg[0]
        gain_lose = seg[2]
        change = seg[3]
        frenemy = seg[10][:-1]
        names.add(name)
        multiplier = 1 if gain_lose == 'gain' else -1
        happy.setdefault(name,dict())[frenemy] = int(change) * multiplier

print(f'optimal happiness: {compute_happy(names,happy)}')

happy['greg'] = {}
for name in names:
    happy[name]['greg'] = 0
    happy['greg'][name] = 0

names.add('greg')

print(f'optimal happiness with me: {compute_happy(names,happy)}')

