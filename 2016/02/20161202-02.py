from collections import defaultdict
import sys

# always go LURD
data = [
    "1D3",
    "2R3D6",
    "3L2U1R4D7",
    "4L3D8",
    "5R6",
    "6L5U2R7DA",
    "7L6U3R8DB",
    "8L7U4R9DC",
    "9L8",
    "AU6RB",
    "BLAU7RCDD",
    "CLBU8",
    "DUB",
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
