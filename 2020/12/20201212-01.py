import sys

DIRECTION = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}
CARDINAL = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

x, y = 0, 0
direction = 90

with open(sys.argv[1], "r") as file:
    for line in file:
        action = line[0]
        value = int(line[1:])
        match action:
            case "N" | "S" | "E" | "W":
                dx, dy = CARDINAL[action]
                x, y = x + value * dx, y + value * dy
            case "L":
                direction -= value
                direction %= 360
            case "R":
                direction += value
                direction %= 360
            case "F":
                dx, dy = DIRECTION[direction]
                x, y = x + value * dx, y + value * dy
            case "B":
                dx, dy = DIRECTION[direction]
                x, y = x - value * dx, y - value * dy

distance = abs(x) + abs(y)
print(f"Part 1: The distance is {distance}")
