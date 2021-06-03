#! /usr/bin/python3

def possible_replacements(start, replacements):
    chunks = []
    chunk = start[0]
    for c in start[1:]:
        if c.isupper():
            chunks.append(chunk)
            chunk = c
        else:
            chunk = chunk + c
    if chunk:
        chunks.append(chunk)

    results = set({})
    for i in range(len(chunks)):
        c = chunks[i]
        for r in replacements:
            if r[0] == c:
                chunks[i] = r[1]
                results.add("".join(chunks))
        chunks[i] = c

    return len(results)

with open('input') as f:
    lines = [l.strip().split() for l in f.readlines()]
    *replacements,[target] = lines
    replacements = [(r[0], r[2]) for r in replacements if r]

    print(f'Part 1: {possible_replacements(target, replacements)}')
    print()

    i = 0
    while True:
        i += 1
        poss = set({})
        for r in replacements:
            idx = -1
            while (idx := target.find(r[1],idx+1)) != -1:
                if target.replace(r[1],r[0],1) == 'e': raise Exception('Part 2: ' + str(i))
                poss.add(target.replace(r[1], r[0], 1))
        target = sorted(poss, key=len)[0] # for me, simply grabbing the shortest result worked - this might not always be the case

