#! /usr/bin/python3

from collections import defaultdict
from operator import sub
from operator import add

class Santa:

    def present(self):
        self.visited[self.current] += 1
 
    def reset(self, visitedDict):
        self.visited = visitedDict
        self.current = (0,0)
        self.present()

    def __init__(self, visitedDict):
        self.reset(visitedDict)

    def move(self, c):
        if c == '<':
            self.current = tuple(map(sub, self.current , (1, 0)))
            self.present()
        elif c == '^':
            self.current = tuple(map(add, self.current , (0, 1)))
            self.present()
        elif c == '>':
            self.current = tuple(map(add, self.current , (1,0)))
            self.present()
        elif c == 'v' or c == 'V':
            self.current = tuple(map(sub, self.current , (0,1)))
            self.present()

    def where(self):
        return self.current

    def total(self):
        return len(self.visited)


with open("input") as f:
    lines = f.readlines()
    chars = [c for line in lines for c in line]
    visited = defaultdict(int)
    santa = Santa(visited)
    for c in chars:
        santa.move(c)
    
    print(f"Santa delivered {santa.total()} presents")
    print(f"Robot Santa Time!")   
    visited = defaultdict(int)
    santa.reset(visited)
    robot = Santa(visited)
    isRobot = False
    for c in chars:
        if isRobot:
            robot.move(c)
        else:
            santa.move(c)
        isRobot = not isRobot

    print(f"Santa delivered {santa.total()} presents")

