#! /usr/bin/python3

import json

def json_sum(obj, good_val_filter):
    stack = [obj]
    s = 0
    while stack:
        o = stack.pop()
        t = type(o)
        if t is int or t is float:
            s += o
        elif t is dict:
            good = [v for v in o.values() if good_val_filter(v)]
            if len(good) == len(o):
                stack.extend(good)
        elif t is list:
            stack.extend(o)

    return s

with open('input') as f:
    obj = json.load(f)
    print(f'Sum of all numbers: {json_sum(obj, lambda v : True)}')
    print(f'Sum of non-red numbers: {json_sum(obj, lambda v : v != "red")}')
    
