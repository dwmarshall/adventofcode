from collections.abc import Iterator
from itertools import combinations
import math
import sys

with open(sys.argv[1], "r") as file:
    packages = set(map(int, file.readlines()))

n = int(sys.argv[2])


def first_partitions(p: set[int], n: int) -> Iterator[list[set[int]]]:

    desired_weight = sum(p) // n

    for r in range(1, len(p)):
        for first_partition in combinations(p, r):
            if sum(first_partition) == desired_weight:
                yield set(first_partition)
            #     continue
            # first_set = set(first_partition)
            # remainder = p - first_set
            # for more_sets in partitions(remainder, n - 1):
            #     yield [first_set] + more_sets


min_length, min_qe = math.inf, math.inf

for t in first_partitions(packages, n):
    print(t)
    if len(t) > min_length:
        continue
    min_length = min(min_length, len(t))
    qe = math.prod(t)
    min_qe = min(min_qe, qe)

print(min_qe)
