#! /usr/bin/python3

def paper_needed(h,l,w):
    s1 = h * l
    s2 = h * w
    s3 = w * l
    return 2 * (s1 + s2 +s3) + min(s1, min(s2,s3))

def ribbon_needed(h,l,w):
    return h * l * w + 2 * (h + l + w - max(h, max(l,w)))

with open("input") as f:
    dims = [list(map(int,d)) for d in [line.strip().split("x") for line in f.readlines()]]
    paper = sum(map(lambda d : paper_needed(d[0],d[1],d[2]),dims))
    ribbon = sum(map(lambda d : ribbon_needed(d[0],d[1],d[2]), dims))
    print(f"Paper: {paper}")
    print(f"Ribbon: {ribbon}")

    
