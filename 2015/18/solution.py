#! /usr/bin/python3


STEPS = 100

def neighbors(grid, r,c):
    count = 0;
    count += grid[r-1][c-1] if r > 0 and c > 0 else 0
    count += grid[r-1][c] if r > 0 else 0
    count += grid[r-1][c+1] if r > 0 and c+1 < len(grid[0]) else 0
    count += grid[r][c-1] if c > 0 else 0
    count += grid[r][c+1] if c+1 < len(grid[0]) else 0
    count += grid[r+1][c-1] if r+1 < len(grid) and c > 0 else 0
    count += grid[r+1][c] if r+1 < len(grid) else 0
    count += grid[r+1][c+1] if r+1 < len(grid) and c+1 < len(grid[0]) else 0
    return count
    

def p1_update(grid):
    g = [list(l) for l in grid]
    for r in range(len(g)):
        for c in range(len(g[0])):
            n = neighbors(grid, r, c)
            g[r][c] = (n == 3) or (grid[r][c] and (n in [2,3]))

    return g


def p2_update(grid):
    g = [list(l) for l in grid]
    for r in range(len(g)):
        for c in range(len(g[0])):
            n = neighbors(grid, r, c)
            g[r][c] = ((n == 3) or
                        (grid[r][c] and (n in [2,3])) or
                        (r == 0 and c == 0) or
                        (r == 0 and c == len(g[0]) - 1) or
                        (r == len(g) - 1 and c == 0) or
                        (r == len(g) - 1 and c == len(g[0]) - 1))

    return g



with open('input') as f:
    lines = [l.strip() for l in f.readlines()]
    l = [[(c == '#') for c in l] for l in lines]

    l_2 = [list(line) for line in l]
    l_2[0][0] = True
    l_2[0][len(l_2)-1] = True
    l_2[len(l_2[0])-1][0] = True
    l_2[len(l_2[0])-1][len(l_2)-1] = True


    for s in range(STEPS):
        l = p1_update(l)
        l_2 = p2_update(l_2)

    print(f'Part 1: {sum([sum(line) for line in l])}')
    print(f'Part 2: {sum([sum(line) for line in l_2])}')

