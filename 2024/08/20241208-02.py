from collections import defaultdict
from itertools import combinations
import sys

frequencies = defaultdict(list)
antinodes = set()

with open(sys.argv[1], "r") as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line.strip()):
            if c == ".":
                continue
            else:
                frequencies[c].append((i, j))
    rows, cols = i, j

for antennas in frequencies.values():
    for a, b in combinations(antennas, 2):
        di = a[0] - b[0]
        dj = a[1] - b[1]
        an1 = a
        while an1[0] >= 0 and an1[0] <= rows and an1[1] >= 0 and an1[1] <= cols:
            antinodes.add(an1)
            an1 = (an1[0] + di, an1[1] + dj)
        an2 = b
        while an2[0] >= 0 and an2[0] <= rows and an2[1] >= 0 and an2[1] <= cols:
            antinodes.add(an2)
            an2 = (an2[0] - di, an2[1] - dj)

print(len(antinodes))
