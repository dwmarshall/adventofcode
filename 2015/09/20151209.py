from collections import defaultdict
from itertools import pairwise, permutations
import math
import re
import sys

distances = defaultdict(dict)

with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.match(r"(\S+) to (\S+) = (\d+)", line)
        a, b, dist = m.groups()
        distances[a][b] = int(dist)
        distances[b][a] = int(dist)

shortest = math.inf
longest = 0

for perm in permutations(distances.keys()):
    this_distance = 0
    for a, b in pairwise(perm):
        this_distance += distances[a][b]
    shortest = min(shortest, this_distance)
    longest = max(longest, this_distance)

print(f"shortest is {shortest}")
print(f"longest is {longest}")
