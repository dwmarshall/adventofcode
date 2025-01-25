import sys

CARDINAL = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

sx, sy = 0, 0
wx, wy = 10, -1
direction = 90

with open(sys.argv[1], "r") as file:
    for line in file:
        action = line[0]
        value = int(line[1:])
        match action:
            case "N" | "S" | "E" | "W":
                dx, dy = CARDINAL[action]
                wx, wy = wx + value * dx, wy + value * dy
            case "L":
                for _ in range(value // 90):
                    wx, wy = wy, -wx
            case "R":
                for _ in range(value // 90):
                    wx, wy = -wy, wx
            case "F":
                sx, sy = sx + value * wx, sy + value * wy

distance = abs(sx) + abs(sy)
print(f"Part 2: The distance is {distance}")
