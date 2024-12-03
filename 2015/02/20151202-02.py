from itertools import combinations
from math import prod
import sys

total_ribbon = 0

for line in sys.stdin:
    dimensions = line.strip().split("x")
    dimensions = list(map(int, dimensions))
    perimeters = []
    for a, b in combinations(dimensions, 2):
        perimeters.append(2 * a + 2 * b)
    total_ribbon += min(perimeters) + prod(dimensions)


print(total_ribbon)
