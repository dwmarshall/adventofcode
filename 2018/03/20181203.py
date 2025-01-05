import re
import sys

SIDE = 1000

fabric = [[0] * SIDE for _ in range(SIDE)]

claims = []

with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.search(r"(\d+),(\d+): (\d+)x(\d+)", line)
        start_x, start_y, wx, wy = map(int, m.groups())
        claims.append((start_x, start_y, wx, wy))
        for x in range(wx):
            for y in range(wy):
                fabric[x + start_x][y + start_y] += 1

overlaps = sum(1 if fabric[i][j] > 1 else 0 for i in range(SIDE) for j in range(SIDE))

print(f"Part 1: There are {overlaps} overlapped squares.")

for i, claim in enumerate(claims):
    start_x, start_y, wx, wy = claim
    if all(fabric[x + start_x][y + start_y] == 1 for x in range(wx) for y in range(wy)):
        print(f"Part 2: The only clear claim is {i + 1}")
        break
