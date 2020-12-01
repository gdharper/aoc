#! /usr/bin/python3

floor = 0
with open("input") as f:
 data= f.read()
 idx = 1
 for c in data:
  if c == '(':
   floor += 1
  elif c == ')':
   floor -= 1
  else:
   print(f"Unexpected c: {c}")

  if floor == -1: print(f"inna basement: {idx}")
  idx += 1

print( f"Floor: {floor}")
