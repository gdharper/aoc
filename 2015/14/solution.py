#! /usr/bin/python3

NAME = 0
SPEED = 1
ON = 2
OFF = 3

def compute_dist(raindeer, time):
    period = raindeer[ON] + raindeer[OFF]
    whole = time // period
    rem = time % period
    total = whole * raindeer[SPEED] * raindeer[ON]
    total += min(rem, raindeer[ON]) * raindeer[SPEED]
    return total

with open('input') as f:
    lines = [line.split() for line in f.readlines()]
    deer = [(l[0], int(l[3]), int(l[6]), int(l[13])) for l in lines]
    
    print(f'Part 1: {max([compute_dist(r, 2503) for r in deer])}')

    points = {r[NAME] : 0 for r in deer}
    for i in range(1, 2504):
        dists = {r[NAME] : compute_dist(r,i) for r in deer}
        for k,v in dists.items():
            if v == max(dists.values()):
                points[k] = points[k] + 1

    print(f'Part 2: {max(points.values())}')

