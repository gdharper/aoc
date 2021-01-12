#! /usr/bin/python3

from enum import Enum

class operation(Enum):
    NOT = 0
    PASS = 1
    AND = 2
    OR = 3
    LS = 4
    RS = 5

# 16 bit bitwise operators
def n( x: int) -> int: return ~x & 0xffff
def a( x: int, y:int) -> int: return x & y & 0xffff
def o( x: int, y:int) -> int: return x | y & 0xffff
def ls( x: int, y:int) -> int: return x << y & 0xffff
def rs( x: int, y:int) -> int: return x >> y & 0xffff


def parse (line):
    if len(line) == 4:
        return (line[3], operation.NOT, [line[1]])
    elif len(line) == 3:
        return (line[2], operation.PASS, [line[0]])
    elif line[1] == 'AND':
        return (line[4], operation.AND, [line[0], line[2]])
    elif line[1] == 'OR':
        return (line[4], operation.OR, [line[0], line[2]])
    elif line[1] == 'LSHIFT':
        return (line[4], operation.LS, [line[0], line[2]])
    elif line[1] == 'RSHIFT':
        return (line[4], operation.RS, [line[0], line[2]])
    else:
        print(line)
        raise "AHHHHHHH"

def evaluate(wire, circuit):
    try: return int(wire)
    except:
        val = circuit[wire]
        if type(val) is int: return val
        else:
            operation, iput = val
            if operation == operation.NOT:
                val = n(evaluate(iput[0], circuit))
            elif operation == operation.PASS:
                val = evaluate(iput[0], circuit)
            elif operation == operation.AND:
                val = a(evaluate(iput[0], circuit), evaluate(iput[1], circuit))
            elif operation == operation.OR:
                val = o(evaluate(iput[0], circuit), evaluate(iput[1], circuit))
            elif operation == operation.LS:
                val = ls(evaluate(iput[0], circuit), evaluate(iput[1], circuit))
            elif operation == operation.RS:
                val = rs(evaluate(iput[0], circuit), evaluate(iput[1], circuit))
            else:
                print(wire)
                raise "AHHHHH"

        circuit[wire] = val
        return val

with open("input") as f:
    circuit = {operation[0]:(operation[1], operation[2]) for operation in
            map(parse, [line.strip().split() for line in f.readlines()])}

    print("parsing complete")

    part1 = evaluate('a', dict(circuit))
    print(f'Part 1: {part1}')

    circuit['b'] = part1
    part2 = evaluate('a', dict(circuit))
    print(f'Part 2: {part2}')

