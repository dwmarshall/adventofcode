import copy
import sys

grid = []

STEPS = int(sys.argv[1])


def perform_step(i: int, j: int) -> int:
    lit_neighbors = -grid[i][j]
    start_row = max(i - 1, 0)
    end_row = min(i + 1, len(grid) - 1)
    start_col = max(j - 1, 0)
    end_col = min(j + 1, len(grid[i]) - 1)
    for ii in range(start_row, end_row + 1):
        for jj in range(start_col, end_col + 1):
            lit_neighbors += grid[ii][jj]
    if grid[i][j] == 1:
        return 1 if 2 <= lit_neighbors <= 3 else 0
    else:
        return 1 if lit_neighbors == 3 else 0


with open(sys.argv[2], "r") as file:
    for line in file:
        row = [1 if x == "#" else 0 for x in line.strip()]
        grid.append(row)
    for i in [0, -1]:
        for j in [0, -1]:
            grid[i][j] = 1

for _ in range(STEPS):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = perform_step(i, j)
    grid = new_grid
    for i in [0, -1]:
        for j in [0, -1]:
            grid[i][j] = 1

lights_on = 0
for row in grid:
    lights_on += sum(row)

print(lights_on)
