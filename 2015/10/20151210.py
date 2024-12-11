from itertools import groupby
import sys

input = sys.argv[1]
rounds = int(sys.argv[2])

for _ in range(rounds):
    pieces = []

    for k, g in groupby(input):
        pieces.append(str(len(list(g))))
        pieces.append(k)

    input = "".join(pieces)

print(len(input))
