import sys

grid = []

initial_position = None

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(sys.argv[1], "r") as file:
    for row, line in enumerate(file):
        this_row = [True if c == "#" else False for c in line.strip()]
        grid.append(this_row)
        if "^" in line:
            col = line.find("^")
            initial_position = (row, col, 0)

initial_visits = set()
position = initial_position
initial_visits.add(position)

while True:
    row, col, dir = position
    drow, dcol = directions[dir]
    nrow, ncol = row + drow, col + dcol
    if nrow < 0 or nrow >= len(grid) or ncol < 0 or ncol >= len(grid[0]):
        break
    if grid[nrow][ncol]:
        dir = (dir + 1) % len(directions)
    else:
        row, col = nrow, ncol
    position = (row, col, dir)
    initial_visits.add(position)

possible_blockers = set([(r, c) for r, c, _ in initial_visits])
possible_blockers.discard((initial_position[0], initial_position[1]))

blockers = 0

for i, j in possible_blockers:
    if grid[i][j]:
        continue
    grid[i][j] = True
    visited = set()
    position = initial_position
    visited.add(position)
    loop_detected = False
    while True:
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
            loop_detected = True
            break
        visited.add(position)
    grid[i][j] = False
    if loop_detected:
        blockers += 1

print(blockers)
