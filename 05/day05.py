#!/usr/bin/env python3
def find_seat_id(ticket):
    row = find(ticket[:7], 127, "F")
    col = find(ticket[7:], 7, "L")
    return (row * 8) + col


def find(ticket_part, size, lower_char):
    min_, max_ = 0, size
    for c in ticket_part:
        diff = int(round((max_ - min_) / 2))
        if c == lower_char:
            max_ -= diff
        else:
            min_ += diff
    return min_ if ticket_part[-1] == lower_char else max_


def part1(lines):
    maximum = 0
    for line in lines:
        maximum = max(maximum, find_seat_id(line.strip()))
    return maximum


def part2(lines):
    seats = {find_seat_id(line.strip()) for line in lines}
    for i in range(min(seats), max(seats)):
        if i not in seats:
            return i


lines = open("./input.txt").readlines()
print("part1:", part1(lines))
print("part2:", part2(lines))
