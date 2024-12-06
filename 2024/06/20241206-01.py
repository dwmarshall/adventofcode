import sys

grid = []

position = None

visited = set()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(sys.argv[1], "r") as file:
    for row, line in enumerate(file):
        this_row = [True if c == "#" else False for c in line.strip()]
        grid.append(this_row)
        if "^" in line:
            col = line.find("^")
            position = (row, col, 0)
            visited.add(position)

while True:
    # print(position)
    row, col, dir = position
    drow, dcol = directions[dir]
    nrow, ncol = row + drow, col + dcol
    if ncol < 0 or ncol >= len(grid[0]):
        break
    if nrow < 0 or nrow >= len(grid):
        break
    if grid[nrow][ncol]:
        # print(f"obstacle at {nrow}, {ncol}")
        dir = (dir + 1) % len(directions)
    else:
        row, col = nrow, ncol
    position = (row, col, dir)
    if position in visited:
        break
    visited.add(position)

points = set((x[0], x[1]) for x in visited)
print(len(points))
