from math import prod
import re
import sys

# X, Y = 11, 7
X, Y = 101, 103

CENTER_X = (X + 1) // 2 - 1
CENTER_Y = (Y + 1) // 2 - 1

STEPS = 100

robots = []
quadrants = [0] * 4

with open(sys.argv[1], "r") as file:
    for line in file:
        robot = {}
        for t in re.findall(r"(p|v)=(-?\d+),(-?\d+)", line):
            robot[t[0]] = (int(t[1]), int(t[2]))
        robots.append(robot)

for r in robots:
    px, py = r["p"]
    dx, dy = r["v"]
    px += STEPS * dx
    px %= X
    py += STEPS * dy
    py %= Y
    if px == CENTER_X or py == CENTER_Y:
        continue
    if px < CENTER_X:
        q = 0 if py < CENTER_Y else 1
    else:
        q = 2 if py < CENTER_Y else 3
    quadrants[q] += 1

print(quadrants)
print(prod(quadrants))
