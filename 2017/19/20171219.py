import string
import sys

grid = []

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
C = ["|", "-", "|", "-"]

direction = 0

with open(sys.argv[1], "r") as file:
    first_line = file.readline()
    grid.append(list(first_line.strip("\n")))
    x, y = (first_line.index("|"), 0)
    for line in file:
        grid.append(list(line.strip("\n")))

output = []
steps = 1
last_steps = None

while 0 <= y < len(grid) and 0 <= x <= len(grid[0]):
    if grid[y][x] == "+":
        steps += 1
        dx1, dy1 = D[(direction + 1) % 4]
        dx2, dy2 = D[(direction - 1) % 4]
        nx1, ny1 = x + dx1, y + dy1
        nx2, ny2 = x + dx2, y + dy2
        if 0 <= ny1 < len(grid) and 0 <= nx1 < len(grid[0]) and grid[ny1][nx1] != " ":
            direction = (direction + 1) % 4
            x, y = nx1, ny1
            continue
        elif 0 <= ny2 < len(grid) and 0 <= nx2 < len(grid[0]) and grid[ny2][nx2] != " ":
            direction = (direction - 1) % 4
            x, y = nx2, ny2
            continue
        else:
            print("Something weird happened!")
            break
    if grid[y][x] in string.ascii_letters:
        if grid[y][x] in output:
            print("Loop!")
            break
        last_steps = steps
        output.append(grid[y][x])
    steps += 1
    dx, dy = D[direction]
    x, y = x + dx, y + dy

print(f"Part 1: The order is {"".join(output)}")
print(f"Part 2: There were {last_steps} steps needed.")
