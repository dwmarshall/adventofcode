from itertools import permutations
import re
import sys

SIZE, USED, AVAIL, PCT = 0, 1, 2, 3

nodes = dict()

with open(sys.argv[1], "r") as file:
    for line in file:
        if re.match(r"/dev/grid", line):
            x, y, *data = re.findall(r"\d+", line)
            nodes[(x, y)] = list(map(int, data))

viable_pairs = 0

for nodeA, nodeB in permutations(nodes.values(), 2):
    if nodeA[USED] > 0 and nodeA[USED] < nodeB[AVAIL]:
        viable_pairs += 1

print(viable_pairs)
