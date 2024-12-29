from functools import cache
import sys


@cache
def is_open(x: int, y: int, n: int) -> bool:
    value = x * x + 3 * x + 2 * x * y + y + y * y + n
    return not bool(value.bit_count() % 2)


gx, gy, number = list(map(int, sys.argv[1:4]))

start = (1, 1)
goal = (gx, gy)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

step = 0
winning_steps = None
locations = [start]
visited = set()

while winning_steps is None:
    next_steps = []
    for x, y in locations:
        if (x, y) == goal:
            winning_steps = step
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_open(nx, ny, number) and (nx, ny) not in visited:
                next_steps.append((nx, ny))
    locations = next_steps
    step += 1

print(f"It takes {winning_steps} steps to get to {(gx, gy)}")
