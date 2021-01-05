#! /usr/bin/python3

with open("input") as f:
    lines = list(map(
        lambda line :  line[1:] if line[0] == 'turn' else line,
            [line.strip().split() for line in f.readlines()]))

    on = [list([False] * 1000) for i in range(0,1000)] 
    bright = [list([0]) * 1000 for i in range(0,1000)]
    
    for line in lines:
        start = line[1].split(',')
        end = line[3].split(',')
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                if line[0] == 'on':
                    on[i][j] = True
                    bright[i][j] += 1
                elif line[0] == 'off':
                    on[i][j] = False
                    bright[i][j] = max(0, bright[i][j] - 1)
                else:
                    on[i][j] = not on[i][j]
                    bright[i][j] += 2

    part1 = sum(map(sum, on))
    part2 = sum(map(sum, bright))
    print(f'Part 1 lights: {part1}')
    print(f'Part 2 lights: {part2}')

