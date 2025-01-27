from itertools import pairwise
import sys

with open(sys.argv[1], "r") as file:
    depths = list(map(int, file.readlines()))

increasing = sum(1 if b > a else 0 for a, b in pairwise(depths))

print(f"Part 1: The number of incresing depths is {increasing}")

windows = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]

increasing = sum(1 if b > a else 0 for a, b in pairwise(windows))

print(f"Part 2: The number of increasing windows is {increasing}")
