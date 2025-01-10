from collections import Counter, defaultdict
import re
import sys

guards = defaultdict(Counter)

with open(sys.argv[1], "r") as file:
    for line in sorted(file):
        if m := re.search(r"(\d+) begins shift", line):
            current_guard = int(m.group(1))
        elif m := re.search(r"(\d+)\].*falls asleep", line):
            sleep_start = int(m.group(1))
        elif m := re.search(r"(\d+)\].*wakes up", line):
            sleep_stop = int(m.group(1))
            for minute in range(sleep_start, sleep_stop):
                guards[current_guard][minute] += 1

# Part 1

ids = list(guards.keys())
ids.sort(key=lambda x: guards[x].total(), reverse=True)
p1_guard = ids[0]
p1_minute = guards[p1_guard].most_common(1)[0][0]

print(f"Part 1: Product = {p1_guard * p1_minute}")

# Part 2
p2_tuples = []

for k, v in guards.items():
    most_common_minute = guards[k].most_common(1)[0][0]
    p2_tuples.append((guards[k][most_common_minute], k, most_common_minute))

p2_tuples.sort(reverse=True)

print(f"Part 2: Product = {p2_tuples[0][1] * p2_tuples[0][2]}")
