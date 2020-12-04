#!/usr/bin/env python3
import re


fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def load_passports(file_):
    with open(file_) as f:
        passports = f.read().split("\n\n")

    for passport in passports:
        passport = passport.replace("\n", " ")
        p = {}
        for entry in passport.split(" "):
            if not entry.strip():
                continue
            k, v = entry.split(":")
            p[k] = v
        yield p


def is_valid(p, field_validator):
    return all(k in p and field_validator(k, p[k]) for k in fields)


part1_validator = lambda *args: True


def part2_validator(field, value):
    if field == "byr":
        return 1920 <= int(value) <= 2002
    elif field == "iyr":
        return 2010 <= int(value) <= 2020
    elif field == "eyr":
        return 2020 <= int(value) <= 2030
    elif field == "hgt":
        match = re.search(r"(\d+)(cm|in)", value)
        if match is None:
            return False
        if match.group(2) == "cm":
            return 150 <= int(match.group(1)) <= 193
        else:
            return 59 <= int(match.group(1)) <= 76
    elif field == "hcl":
        return re.search(r"#[0-9a-f]{6}", value) is not None
    elif field == "ecl":
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif field == "pid":
        return re.search(r"^[0-9]{9}$", value) is not None
    return True


def solve(file_, validator):
    return list(is_valid(p, validator) for p in load_passports(file_)).count(True)


print(solve("./sample.txt", part1_validator))
print(solve("./input.txt", part1_validator))
print(solve("./sample.txt",  part2_validator))
print(solve("./input.txt", part2_validator))
