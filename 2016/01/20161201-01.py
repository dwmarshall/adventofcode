import sys

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir = 0

pos = (0, 0)

with open(sys.argv[1], "r") as file:
    turn_list = file.readline()

for turn in turn_list.split(", "):
    if turn[0] == "L":
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4
    blocks = int(turn[1:])
    offset = tuple(x * blocks for x in directions[dir])
    pos = tuple(a + b for a, b in zip(pos, offset))

print(sum(pos))
