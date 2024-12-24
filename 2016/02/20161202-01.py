from collections import defaultdict
import sys

data = [
    "1R2D4",
    "2L1R3D5",
    "3L2D6",
    "4U1R5D7",
    "5U2L4R6D8",
    "6U3L5D9",
    "7U4R8",
    "8U5L7R9",
    "9U6L8",
]

G = defaultdict(dict)

for datum in data:
    button = datum[0]
    for i in range(1, len(datum), 2):
        G[button][datum[i]] = datum[i + 1]

curr = "5"
code = []

with open(sys.argv[1], "r") as file:
    for line in file:
        for c in line.strip():
            if c not in G[curr]:
                continue
            curr = G[curr][c]
        code.append(curr)

print("".join(code))
