from collections import Counter
import sys

has_two = 0
has_three = 0

p2_counter = Counter()

with open(sys.argv[1], "r") as file:
    for line in file:
        p1_counter = Counter(line.strip())
        if 2 in p1_counter.values():
            has_two += 1
        if 3 in p1_counter.values():
            has_three += 1
        id = line.strip()
        for i in range(len(id)):
            masked = id[:i] + "_" + id[i + 1 :]
            p2_counter[masked] += 1

print(f"Part 1: {has_two * has_three}")

for k, v in p2_counter.items():
    if v == 2:
        print(f"Part 2: Common letters are {k.replace("_", "")}")
        break
