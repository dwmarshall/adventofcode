from collections import defaultdict
from itertools import combinations
import sys

connections = defaultdict(set)

with open(sys.argv[1], "r") as file:
    for line in file:
        A, B = line.strip().split("-")
        connections[A].add(B)
        connections[B].add(A)


starts_with_t = 0
for a, b, c in combinations(connections, 3):
    if a in connections[b] and a in connections[c] and b in connections[c]:
        triple = sorted([a, b, c])
        if any(s[0] == "t" for s in triple):
            print(",".join(triple))
            starts_with_t += 1

print(starts_with_t)
