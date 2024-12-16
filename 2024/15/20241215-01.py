import sys
from typing import Tuple

grid = []
moves = ""
position = None


def print_grid() -> None:
    for i in range(len(grid)):
        print("".join(grid[i]))


def process(x: int, y: int, move: str) -> Tuple[int]:
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
        return x, y


with open(sys.argv[1], "r") as file:
    for row, line in enumerate(file):
        if line.startswith("#"):
            grid.append(list(line.strip()))
            if (col := line.find("@")) != -1:
                position = row, col
        else:
            moves += line.strip()


for m in moves:
    x, y = position
    position = process(x, y, m)

total_GPS = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            total_GPS += 100 * i + j

print(total_GPS)
