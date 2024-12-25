import re
import sys

ROWS, COLS = 6, 50


def display(grid: list[list[int]]) -> None:
    for y in range(len(grid)):
        line = ["#" if grid[y][x] == 1 else "." for x in range(len(grid[y]))]
        print("".join(line))
    print("")


def rect(grid: list[list[int]], x: int, y: int) -> None:
    for i in range(y):
        for j in range(x):
            grid[i][j] = 1


def rotate_column(grid: list[list[int]], x: int, n: int) -> None:
    n %= COLS
    original_column = [grid[i][x] for i in range(len(grid))]
    for y in range(len(grid)):
        grid[(y + n) % ROWS][x] = original_column[y]


def rotate_row(grid: list[list[int]], y: int, n: int) -> None:
    y %= ROWS
    original_row = grid[y].copy()
    for x in range(len(grid[y])):
        grid[y][(x + n) % COLS] = original_row[x]


lights = [[0] * COLS for _ in range(ROWS)]

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"rect (\d+)x(\d+)", line):
            x, y = list(map(int, m.groups()))
            rect(lights, x, y)
        elif m := re.match(r"rotate row y=(\d+) by (\d+)", line):
            y, n = list(map(int, m.groups()))
            rotate_row(lights, y, n)
        elif m := re.match(r"rotate column x=(\d+) by (\d+)", line):
            x, n = list(map(int, m.groups()))
            rotate_column(lights, x, n)
        # print(f"after {line.strip()}:")
        # display(lights)

total_lights = sum(sum(lights[y]) for y in range(ROWS))
print(f"There are {total_lights} lights lit.")
display(lights)
