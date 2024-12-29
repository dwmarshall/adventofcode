from hashlib import md5
import heapq
from itertools import compress
import sys

CELLS = 4

start = (0, 0)
goal = (3, 3)

INPUT = sys.argv[1]

directions = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]


def available_directions(input: str, path: str = "") -> list[tuple[int, int]]:
    key = f"{input}{path}"
    digest = md5(key.encode()).hexdigest()
    passes = [c in "bcdef" for c in digest[:4]]
    return list(compress(directions, passes))


q = []

initial_state = (0, start, "")
heapq.heappush(q, initial_state)

shortest_path = None
longest_path = 0

while q:
    _, location, path = heapq.heappop(q)
    if location == goal:
        if shortest_path is None:
            shortest_path = path
        longest_path = max(longest_path, len(path))
        continue
    x, y = location
    for step, dx, dy in available_directions(INPUT, path):
        nx, ny = x + dx, y + dy
        if 0 <= nx < CELLS and 0 <= ny < CELLS:
            new_path = path + step
            heapq.heappush(q, (len(path), (nx, ny), new_path))

print(f"Shortest path: {shortest_path}")
print(f"Longest path has {longest_path} steps")
