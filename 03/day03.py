#!/usr/bin/env python3
import math

def solve(lines, rise=1, run=3):
    x, y = 0, 0
    count = 0
    while y < len(lines) - 1:
        y += rise
        x += run
        if lines[y][x % len(lines[y])] == "#":
            count += 1
    return count


with open("./input.txt") as f:
    lines = [x.strip() for x in f]


print("part1 (test):", solve([
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]))
print("part1:", solve(lines))

print("part2 (test):", math.prod(solve([
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
], y, x) for x, y in [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]))
print("part2:", math.prod(solve(lines, y, x) for x, y in [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]))
