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

    reverse = [(r[1],r[0]) for r in replacements]

    start = target
    i = 0
    while True:
        i += 1
        poss = set({})
        for pattern, replacement in reverse:
            idx = -1
            while (idx := start.find(pattern,idx+1)) != -1:
                new = start[:idx] + replacement + start[idx+len(pattern):]
                if new == "e":
                    raise Exception('Part 2: ' + str(i))
                poss.add(new)
        start = sorted(poss, key=len)[0] # for me, simply grabbing the shortest result worked - this might not always be the case

