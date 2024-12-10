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


def dfs(i: int, j: int, ends: set) -> int:
    if grid[i][j] == "9":
        ends.add((i, j))
    next_char = chr(ord(grid[i][j]) + 1)
    trails = 0
    if i > 0 and grid[i - 1][j] == next_char:
        trails += dfs(i - 1, j, ends)
    if i < len(grid) - 1 and grid[i + 1][j] == next_char:
        trails += dfs(i + 1, j, ends)
    if j > 0 and grid[i][j - 1] == next_char:
        trails += dfs(i, j - 1, ends)
    if j < len(grid[i]) - 1 and grid[i][j + 1] == next_char:
        trails += dfs(i, j + 1, ends)
    return trails


total_trails = 0

for x, y in trailheads:
    trail_ends = set()
    dfs(x, y, trail_ends)
    print(f"Trailhead at {x}, {y} has {len(trail_ends)} trails")
    total_trails += len(trail_ends)

print(total_trails)
