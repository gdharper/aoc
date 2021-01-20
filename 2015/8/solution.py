#! /usr/bin/python3

import re

with open("input") as f:
    lit = 0
    mem = 0
    enc = 0
    for line in f.readlines():
        line = line.strip()
        lit += len(line)
        mem += len(line) - 2 # quotes
        enc += len(line) + 4 # new quotes + escapes for existing quotes
        line = line[1:-1]
        q = len(re.findall(r'\\"', line))
        s = len(re.findall(r'\\\\', line))
        h = len(re.findall(r'\\x[0-9a-fA-F]{2}', line))
        mem -= (q + s + 3 * h)
        enc += (2 * q + 2 * s + h)

    print(f'Literal characters: {lit}')
    print(f'Characters in memeort: {mem}')
    print(f'Re-encoded characters: {enc}')
    print(f'Part 1: {lit - mem}')
    print(f'Part 2: {enc - lit}')

