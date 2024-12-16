import copy
import sys
from typing import Tuple

grid = []
moves = ""
position = None


def print_grid() -> None:
    for i in range(len(grid)):
        print("".join(grid[i]))


def process(x: int, y: int, move: str, check_other: bool = True) -> Tuple[int]:
    global grid
    rollback = copy.deepcopy(grid)
    if grid[x][y] in "[]" and check_other:
        if grid[x][y] == "[":
            ox, oy = x, y + 1
        else:
            ox, oy = x, y - 1
        nox, noy = process(ox, oy, move, False)
        if (nox, noy) == (ox, oy):
            # It didn't move!
            grid = rollback
            return x, y
    match move:
        case "^":
            dx, dy = -1, 0
        case "v":
            dx, dy = 1, 0
        case "<":
            dx, dy = 0, -1
        case ">":
            dx, dy = 0, 1
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == "#":
        return x, y
    if grid[nx][ny] != ".":
        process(nx, ny, move)
    if grid[nx][ny] == ".":
        grid[nx][ny] = grid[x][y]
        grid[x][y] = "."
        return nx, ny
    else:
        grid = rollback
        return x, y


with open(sys.argv[1], "r") as file:
    for row, line in enumerate(file):
        if line.startswith("#"):
            row_array = []
            for c in line.strip():
                if c == "#":
                    row_array.extend(["#", "#"])
                elif c == ".":
                    row_array.extend([".", "."])
                elif c == "O":
                    row_array.extend(["[", "]"])
                else:
                    row_array.extend(["@", "."])
            grid.append(row_array)
            if (col := line.find("@")) != -1:
                position = row, 2 * col
        else:
            moves += line.strip()


for m in moves:
    x, y = position
    position = process(x, y, m)

total_GPS = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            total_GPS += 100 * i + j

print(total_GPS)
