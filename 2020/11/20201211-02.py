import copy
import sys

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def visibly_filled(g: list[list[str]], i: int, j: int) -> int:
    filled = 0
    for di, dj in DIRECTIONS:
        ni, nj = i + di, j + dj
        while 0 <= ni < len(g) and 0 <= nj < len(g[ni]) and g[ni][nj] == ".":
            ni, nj = ni + di, nj + dj
        if 0 <= ni < len(g) and 0 <= nj < len(g[ni]) and g[ni][nj] == "#":
            filled += 1
    return filled


def display(g: list[list[str]]) -> None:
    lines = []
    for row in grid:
        lines.append("".join(row))
    print("\n".join(lines))


grid = []

with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(list(line.strip()))

changed = True
iteration = 0
while changed:
    iteration += 1
    changed = False
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                f = visibly_filled(grid, i, j)
                if f >= 5:
                    new_grid[i][j] = "L"
                    if grid[i][j] != "L":
                        changed = True
                elif f == 0:
                    new_grid[i][j] = "#"
                    if grid[i][j] != "#":
                        changed = True
    grid = new_grid

occupied = sum(sum(1 if c == "#" else 0 for c in row) for row in grid)
print(f"Part 1: The number of occupied seats is {occupied}")
