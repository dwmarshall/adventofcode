import sys

DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def manhattan_distance(p: tuple[int, int]) -> int:
    return abs(p[0]) + abs(p[1])


def points(s: str) -> list[tuple[int, int]]:
    result = [(0, 0)]
    x, y = 0, 0
    for fragment in s.split(","):
        direction, quantity = fragment[0], int(fragment[1:])
        dx, dy = DIRECTIONS[direction]
        for _ in range(quantity):
            x, y = x + dx, y + dy
            result.append((x, y))

    return result


with open(sys.argv[1], "r") as file:
    w1 = points(file.readline().strip())
    w2 = points(file.readline().strip())

crossings = set(w1) & set(w2) - {(0, 0)}

print(f"Part 1: Closest crossing is {min(map(manhattan_distance, crossings))}")

min_steps = float("inf")

for point in crossings:
    steps1 = w1.index(point)
    steps2 = w2.index(point)
    min_steps = min(min_steps, steps1 + steps2)

print(f"Part 2: The fewest combined steps is {min_steps}")
