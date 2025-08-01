import re
import sys


def contains(x: range, y: range) -> bool:
    return (x.start <= y.start and x.stop >= y.stop) or (
        y.start <= x.start and y.stop >= x.stop
    )


def overlaps(x: range, y: range) -> bool:
    if x.start <= y.start:
        return x.stop >= y.start
    else:
        return y.stop >= x.start


with open(sys.argv[1], "r") as file:
    lines = [line.rstrip("\n") for line in file]

part1_hits = 0
part2_hits = 0

for line in lines:
    nums = list(map(int, re.split(r"\D+", line)))
    left = range(*nums[0:2])
    right = range(*nums[2:4])
    if contains(left, right):
        part1_hits += 1
    if overlaps(left, right):
        part2_hits += 1

print(f"Part 1: Contained pairs = {part1_hits}")
print(f"Part 2: Overlapping pairs = {part2_hits}")
