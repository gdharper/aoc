#! /usr/bin/python3

import re

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]
    count1 = sum(1 for s in lines if
            len([c for c in s if c in "aeiou"]) > 2
            and not any(ss in s for ss in ["ab", "cd", "pq", "xy"])
            and re.search(r"([a-z])\1", s))
    print(f'Part 1: {count1}')

    count2 = sum(1 for s in lines if
            re.search(r"([a-z]{2}).*\1",s)
            and re.search(r"([a-z]).\1",s))

    print(f'Part 2: {count2}')



