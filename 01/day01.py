#!/usr/bin/env python3
import itertools
import math


def solve(lines, count=2, match=2020):
    for combo in itertools.combinations(lines, r=count):
        if sum(combo) == match:
            return math.prod(combo)


print("part1 (test):", solve([1721, 979, 366, 299, 675, 1456]))
with open("./input.txt") as f:
    print("part1:", solve([int(x.strip()) for x in f]))

with open("./input.txt") as f:
    print("part2:", solve([int(x.strip()) for x in f], count=3))
