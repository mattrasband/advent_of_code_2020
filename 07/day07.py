#!/usr/bin/env python3
import re
from typing import Tuple


def search_for_color(color: str, key: str, mapping: dict[str, Tuple[int, str]]):
    if color in [x[1] for x in mapping[key]]:
        return True
    return any(search_for_color(color, item[1], mapping) for item in mapping[key])


def find_total_count(key: str, mapping: dict[str, Tuple[int, str]]):
    return sum(count + count * find_total_count(color, mapping) for count, color in mapping[key])


with open("./input.txt") as f:
    bags = {}
    for line in f:
        if (match := re.findall(r"(?:^(\w+ \w+)|(\d) (\w+ \w+))", line)):
            l = []
            for item in match[1:]:  # these will be a tuple of ('', '\d+', 'color text')
                l.append((int(item[1]), item[2]))
            bags[match[0][0]] = l

    print("part 1:", sum([1 for k in bags.keys() if search_for_color('shiny gold', k, bags)]))
    print("part 2:", find_total_count("shiny gold", bags))
