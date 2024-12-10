import sys

grid = []
trailheads = []

with open(sys.argv[1], "r") as file:
    for i, line in enumerate(file):
        row = list(line.strip())
        for j, c in enumerate(row):
            if c == "0":
                trailheads.append((i, j))
        grid.append(row)


def dfs(i: int, j: int) -> int:
    if grid[i][j] == "9":
        return 1
    next_char = chr(ord(grid[i][j]) + 1)
    trails = 0
    if i > 0 and grid[i - 1][j] == next_char:
        trails += dfs(i - 1, j)
    if i < len(grid) - 1 and grid[i + 1][j] == next_char:
        trails += dfs(i + 1, j)
    if j > 0 and grid[i][j - 1] == next_char:
        trails += dfs(i, j - 1)
    if j < len(grid[i]) - 1 and grid[i][j + 1] == next_char:
        trails += dfs(i, j + 1)
    return trails


total_trails = 0

for x, y in trailheads:
    trails = dfs(x, y)
    print(f"Trailhead at {x}, {y} has a rating of {trails}")
    total_trails += trails

print(total_trails)
