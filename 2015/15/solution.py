#! /usr/bin/python3

TSP = 100
CAP = 0
DUR = 1
FLA = 2
TEX = 3
CAL = 4


def parse_line(l):
    return [int(l[2][:-1]),
            int(l[4][:-1]),
            int(l[6][:-1]),
            int(l[8][:-1]),
            int(l[10])]

with open('input') as f:
    lines = [line.split() for line in f.readlines()]

    ings = [parse_line(l) for l in lines]
    best_p1 = 0
    best_p2 = 0
    for i in range(0, TSP):
        for j in range(0, TSP - i):
            for k in range(0, TSP - i - j):
                l = TSP - i - j - k
                cap = max(0, (i * ings[0][CAP] + j* ings[1][CAP] + k * ings[2][CAP] + l * ings[3][CAP]))
                dur = max(0, (i * ings[0][DUR] + j* ings[1][DUR] + k * ings[2][DUR] + l * ings[3][DUR]))
                fla = max(0, (i * ings[0][FLA] + j* ings[1][FLA] + k * ings[2][FLA] + l * ings[3][FLA]))
                tex = max(0, (i * ings[0][TEX] + j* ings[1][TEX] + k * ings[2][TEX] + l * ings[3][TEX]))
                cal = max(0, (i * ings[0][CAL] + j* ings[1][CAL] + k * ings[2][CAL] + l * ings[3][CAL]))

                prod = cap * dur * fla * tex
                best_p1 = max(best_p1, prod)
                best_p2 = max(best_p2, prod) if cal == 500 else best_p2

    print(f'Part 1: {best_p1}')
    print(f'Part 2: {best_p2}')
        

