#! /usr/bin/python3

start = [3,1,1,3,3,2,2,1,1,3]

citer = list(start)
for i in range(50):
    niter = []
    last = citer[0]
    count = 0
    for d in citer:
        if d != last:
            niter.append(count)
            niter.append(last)
            last = d
            count = 1
        else:
            count += 1

    niter.append(count)
    niter.append(last)
    citer = niter
    print(f'iteration: {i+1} - length {len(citer)}')

