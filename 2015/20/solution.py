#! /usr/bin/python3

from math import sqrt

TARGET = 29000000

def divisors(n):
    small = [i for i in range(1, int(sqrt(n)) + 1) if not (n % i)]
    large = [n / d for d in small if n != d * d]
    return small + large

p_1, p_2 = None, None
i = 0
while not (p_1 and p_2):
    i += 1
    div = divisors(i)
    if not p_1 and sum(div) * 10 >= TARGET:
        p_1 = i

    if not p_2 and (sum(d for d in div if i / d <= 50) * 11) >= TARGET:
        p_2 = i

print(f'Part 1: {p_1}')
print(f'Part 2: {p_2}')

