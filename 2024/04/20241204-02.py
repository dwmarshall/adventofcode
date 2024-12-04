import sys
from typing import Callable

total_hits = 0

grid = []


def matches(x: int, y: int) -> bool:

    if x < 1 or x + 1 >= len(grid) or y < 1 or y + 1 >= len(grid[x]):
        return False

    main = [grid[x - 1][y - 1], grid[x][y], grid[x + 1][y + 1]]
    main = "".join(main)
    if main != "MAS" and main != "SAM":
        return False

    secondary = [grid[x - 1][y + 1], grid[x][y], grid[x + 1][y - 1]]
    secondary = "".join(secondary)

    return secondary == "MAS" or secondary == "SAM"


with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "A":
            continue
        if matches(i, j):
            total_hits += 1

print(total_hits)
