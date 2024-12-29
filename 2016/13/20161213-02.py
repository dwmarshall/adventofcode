from functools import cache
import sys


@cache
def is_open(x: int, y: int, n: int) -> bool:
    if x < 0 or y < 0:
        return False
    value = x * x + 3 * x + 2 * x * y + y + y * y + n
    return not bool(value.bit_count() % 2)


number = int(sys.argv[1])

start = (1, 1)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

locations = [start + (0,)]
visited = set()
visited.add(start)

while locations:
    next_steps = []
    for x, y, steps in locations:
        if steps > 50:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_open(nx, ny, number) and (nx, ny) not in visited:
                next_steps.append((nx, ny, steps + 1))
    locations = next_steps

print(visited)
print(f"There are {len(visited)} distinct locations")
