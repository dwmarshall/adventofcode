from collections import Counter
from functools import cache
import heapq
import math
import sys
from typing import Iterator, List, Tuple

sys.setrecursionlimit(10000)

grid = []
start = None
goal = None

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

RADIUS = int(sys.argv[2])
SAVINGS = int(sys.argv[3])


def cheats(pos: Tuple[int, int], radius: int) -> Iterator[Tuple[int, Tuple[int, int]]]:
    x, y = pos
    for cx in range(-radius, radius + 1):
        for cy in range(abs(cx) - radius, radius - abs(cx) + 1):
            nx, ny = x + cx, y + cy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and pos != (nx, ny)
                and grid[nx][ny] in ".E"
            ):
                distance = abs(nx - x) + abs(ny - y)
                yield distance, (nx, ny)


@cache
def distance(pos: Tuple[int, int]) -> int:
    q = [(0, pos)]
    visited = set()

    while q:
        steps, location = heapq.heappop(q)
        if location == goal:
            return steps
        visited.add(location)
        x, y = location
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and grid[nx][ny] in ".E"
                and (nx, ny) not in visited
            ):
                heapq.heappush(q, (steps + 1, (nx, ny)))


def best_path() -> List[Tuple[int, int]]:
    q = [(0, start, tuple())]
    visited = set()

    while q:
        steps, location, path = heapq.heappop(q)
        path = path + (location,)
        if location == goal:
            return path
        visited.add(location)
        x, y = location
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[x])
                and grid[nx][ny] != "#"
                and (nx, ny) not in visited
            ):
                heapq.heappush(
                    q,
                    (steps + 1, (nx, ny), path),
                )
    return math.inf


with open(sys.argv[1], "r") as file:
    for x, line in enumerate(file):
        grid.append(list(line.strip()))
        if (y := line.find("S")) != -1:
            start = x, y
        if (y := line.find("E")) != -1:
            goal = x, y

baseline_path = best_path()
baseline = distance(start)
savings = Counter()


for i in range(len(baseline_path)):
    print(f"{i + 1}/{baseline}")
    for d, cheat in cheats(baseline_path[i], RADIUS):
        new_distance = i + d + distance(cheat)
        if new_distance < baseline:
            savings[baseline - new_distance] += 1

qualifying = 0

for k in sorted(savings.keys()):
    print(f"{k}: {savings[k]}")
    if k >= SAVINGS:
        qualifying += savings[k]

print(f"Total of {qualifying} cheats that save >= {SAVINGS}")
