import sys

total_hits = 0

grid = []


def down(x: int, y: int) -> bool:
    return (
        x + 3 < len(grid)
        and grid[x][y] == "X"
        and grid[x + 1][y] == "M"
        and grid[x + 2][y] == "A"
        and grid[x + 3][y] == "S"
    )


def up(x: int, y: int) -> bool:
    return (
        x >= 3
        and grid[x][y] == "X"
        and grid[x - 1][y] == "M"
        and grid[x - 2][y] == "A"
        and grid[x - 3][y] == "S"
    )


def northeast(x: int, y: int) -> bool:
    return (
        x >= 3
        and y + 3 < len(grid[0])
        and grid[x][y] == "X"
        and grid[x - 1][y + 1] == "M"
        and grid[x - 2][y + 2] == "A"
        and grid[x - 3][y + 3] == "S"
    )


def northwest(x: int, y: int) -> bool:
    return (
        x >= 3
        and y >= 3
        and grid[x][y] == "X"
        and grid[x - 1][y - 1] == "M"
        and grid[x - 2][y - 2] == "A"
        and grid[x - 3][y - 3] == "S"
    )


def southeast(x: int, y: int) -> bool:
    return (
        x + 3 < len(grid)
        and y >= 3
        and grid[x][y] == "X"
        and grid[x + 1][y - 1] == "M"
        and grid[x + 2][y - 2] == "A"
        and grid[x + 3][y - 3] == "S"
    )


def southwest(x: int, y: int) -> bool:
    return (
        x + 3 < len(grid)
        and y + 3 < len(grid[0])
        and grid[x][y] == "X"
        and grid[x + 1][y + 1] == "M"
        and grid[x + 2][y + 2] == "A"
        and grid[x + 3][y + 3] == "S"
    )


with open(sys.argv[1], "r") as file:
    for line in file:
        total_hits += line.count("XMAS")
        total_hits += line.count("SAMX")
        grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "X":
            continue
        if down(i, j):
            total_hits += 1
        if up(i, j):
            total_hits += 1
        if northeast(i, j):
            total_hits += 1
        if northwest(i, j):
            total_hits += 1
        if southeast(i, j):
            total_hits += 1
        if southwest(i, j):
            total_hits += 1

print(total_hits)
