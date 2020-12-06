answers = open("./sample.txt").read().split("\n\n")
print("part1 (test):", sum(len(set(ans.replace("\n", ""))) for ans in answers))

answers = open("./input.txt").read().split("\n\n")
print("part1:", sum(len(set(ans.replace("\n", ""))) for ans in answers))

total = 0
for group in open("./input.txt").read().split("\n\n"):
    groups = group.split("\n")
    s = set()
    for g in groups:
        s.update(set(g))
    group_count = len(groups)
    total += sum(1 for x in s if group.count(x) == group_count)
print("part2:", total)
