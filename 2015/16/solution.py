#! /usr/bin/python3

TARGET = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def part_1_match(sue):
    for k,v in TARGET.items():
        if k in sue and sue[k] != v:
            return False
    return True

def part_2_match(sue):
    gt = ['cats', 'trees']
    lt = ['pomeranians', 'goldfish']
    for k,v in TARGET.items():
        if k in sue and k in gt and sue[k] <= v: return False
        if k in sue and k in lt and sue[k] >= v: return False
        if k in sue and k not in gt and k not in lt and sue[k] != v: return False
    return True

with open('input') as f:
    lines = [line.split() for line in f.readlines()]
    
    sues = {int(line[1][:-1]) : dict(zip(
                                    [l[:-1] for l in line[2::2]],
                                    [int(l[0]) for l in line[3::2]]))
            for line in lines}

    print(f'Part 1: {[k for k,v in sues.items() if part_1_match(v)][0]}')
    print(f'Part 2: {[k for k,v in sues.items() if part_2_match(v)][0]}')

