from collections import defaultdict
import copy
import sys

starting_grid = defaultdict(lambda: ".")
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction_words = ["up", "right", "down", "left"]


max_x, max_y = 0, 0
with open(sys.argv[1], "r") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            starting_grid[(x, y)] = c
        max_x = x
    max_y = y

original_x, original_y = max_x // 2, max_y // 2

# Part 1
x, y = original_x, original_y
dir = 0
bursts = 0
grid = copy.deepcopy(starting_grid)

for _ in range(10000):
    match grid[(x, y)]:
        case ".":
            bursts += 1
            grid[(x, y)] = "#"
            dir = (dir - 1) % 4  # turn left
        case "#":
            grid[(x, y)] = "."
            dir = (dir + 1) % 4  # turn right
    dx, dy = directions[dir]
    x, y = x + dx, y + dy

print(f"Part 1: there were {bursts} infections.")

# Part 2
x, y = original_x, original_y
dir = 0
bursts = 0
grid = copy.deepcopy(starting_grid)

for _ in range(10000000):
    match grid[(x, y)]:
        case ".":
            grid[(x, y)] = "W"
            dir = (dir - 1) % 4  # turn left
        case "#":
            grid[(x, y)] = "F"
            dir = (dir + 1) % 4  # turn right
        case "W":
            bursts += 1
            grid[(x, y)] = "#"
        case "F":
            grid[(x, y)] = "."
            dir = (dir + 2) % 4  # turn around
    dx, dy = directions[dir]
    x, y = x + dx, y + dy

print(f"Part 2: There were {bursts} infections.")
