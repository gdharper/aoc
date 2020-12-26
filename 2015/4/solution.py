#! /usr/bin/python3

import hashlib

with open("input") as f:
    key = f.readline().strip();
    val = 1
    part1 = None
    part2 = None
    while not part1 or not part2:
        hashIn = key + str(val)
        hashOut = hashlib.md5(hashIn.encode()).hexdigest()
        if hashOut[:5] == "00000" and not part1:
            part1 = val

        if hashOut[:6] == "000000":
            part2 = val

        val += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

