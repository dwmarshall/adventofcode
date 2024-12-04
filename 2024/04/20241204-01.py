import sys
from typing import Callable

total_hits = 0

grid = []

tests = []


def test_closure(bounds_check: Callable, dx: int, dy: int) -> Callable:
    return lambda x, y: (
        bounds_check(x, y)
        and grid[x][y] == "X"
        and grid[x + dx][y + dy] == "M"
        and grid[x + 2 * dx][y + 2 * dy] == "A"
        and grid[x + 3 * dx][y + 3 * dy] == "S"
    )


right = test_closure(lambda x, y: y + 3 < len(grid[x]), 0, 1)
tests.append(right)

left = test_closure(lambda _, y: y >= 3, 0, -1)
tests.append(left)

down = test_closure(lambda x, _: x + 3 < len(grid), 1, 0)
tests.append(down)

up = test_closure(lambda x, _: x >= 3, -1, 0)
tests.append(up)

northeast = test_closure(lambda x, y: x >= 3 and y + 3 < len(grid[x]), -1, 1)
tests.append(northeast)

northwest = test_closure(lambda x, y: x >= 3 and y >= 3, -1, -1)
tests.append(northwest)

southeast = test_closure(lambda x, y: x + 3 < len(grid) and y >= 3, 1, -1)
tests.append(southeast)

southwest = test_closure(lambda x, y: x + 3 < len(grid) and y + 3 < len(grid[x]), 1, 1)
tests.append(southwest)

with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "X":
            continue
        for test in tests:
            if test(i, j):
                total_hits += 1

print(total_hits)
