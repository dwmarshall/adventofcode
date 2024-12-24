import sys

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def first_repeat(s: str) -> tuple[int, int]:
    pos = (0, 0)
    dir = 0
    visited = set()
    visited.add(pos)

    for turn in s.split(", "):
        if turn[0] == "L":
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        dx, dy = directions[dir]
        blocks = int(turn[1:])
        for _ in range(blocks):
            pos = (pos[0] + dx, pos[1] + dy)
            if pos in visited:
                return pos
            visited.add(pos)


with open(sys.argv[1], "r") as file:
    turn_list = file.readline()

hq = first_repeat(turn_list)
print(sum(hq))
