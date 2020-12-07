#!/usr/bin/env python3
import re


def search_for_color(color: str, key: str, mapping: dict[str, list]):
    if color in mapping[key]:
        return True
    return any(search_for_color(color, item, mapping) for item in mapping[key])


with open("./input.txt") as f:
    bags = {}
    for line in f:
        if (match := re.findall(r"(?:^(\w+ \w+)|(\d) (\w+ \w+))", line)):
            l = []
            for item in match[1:]:  # these will be a tuple of ('', '\d+', 'color text')
                l.append(item[-1])
            bags[match[0][0]] = l

    print("part 1:", sum([1 for k in bags.keys() if search_for_color('shiny gold', k, bags)]))

