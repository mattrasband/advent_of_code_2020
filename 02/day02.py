#!/usr/bin/env python3
import re
from dataclasses import dataclass


@dataclass
class Password:
    min_: int
    max_: int
    char: str
    pw: str


def is_valid_password(pw: Password) -> bool:
    count = pw.pw.count(pw.char)
    return pw.min_ <= count <= pw.max_


def parse_line(line: str) -> Password:
    match = re.search(r"^(?P<min>\d+)-(?P<max>\d+) (?P<char>[A-z]): (?P<pw>[A-z]+)$", line)
    if not match:
        raise ValueError("unable to parse string: " + line)
    return Password(
        min_=int(match.group("min")),
        max_=int(match.group("max")),
        char=match.group("char"),
        pw=match.group("pw"),
    )


def part1():
    count = 0
    for line in open("./input.txt"):
            if is_valid_password(parse_line(line)):
                    count += 1
    return count


def is_valid_password2(pw: Password) -> bool:
    indexes = [i+1 for i, char in enumerate(pw.pw) if char == pw.char]
    return sum(1 for i in indexes if i == pw.min_ or i == pw.max_) == 1


def part2(lines):
    count = 0
    for line in lines:
        if is_valid_password2(parse_line(line)):
            count += 1
    return count


print("part1:", part1())
print("part2 (test):", part2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]))
with open("./input.txt") as f:
    print("part2:", part2(f))
