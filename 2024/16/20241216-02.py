from functools import cache
import heapq
import sys
from typing import Tuple

grid = []
start = None
goal = None

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(sys.argv[1], "r") as file:
    for row, line in enumerate(file):
        grid.append(list(line.strip()))
        if (col := line.find("S")) != -1:
            start = row, col
        if (col := line.find("E")) != -1:
            goal = row, col


@cache
def minimum_cost(
    location: Tuple[int, int] = start,
    direction: int = 1,
) -> int:
    q = [(0, location, direction)]

    visited = set()

    while q:
        cost, pos, dir = heapq.heappop(q)
        if pos == goal:
            return cost
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        x, y = pos
        # keep going in the same direction
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] in ".E":
            heapq.heappush(q, (cost + 1, (nx, ny), dir))
        clockwise = (dir + 1) % 4
        dx, dy = directions[clockwise]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] in ".E":
            heapq.heappush(q, (cost + 1001, (nx, ny), clockwise))
        ccw = (dir - 1) % 4
        dx, dy = directions[ccw]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] in ".E":
            heapq.heappush(q, (cost + 1001, (nx, ny), ccw))


best_cost = minimum_cost()
print(f"Best cost is {best_cost}")

all_visited = set([goal])

# Now do the BFS again and check from each location whether
# the cost to there plus the cost from there is the best cost.
# If it is, then it's a location on a best path

q = [(0, start, 1)]
visited = set()

while q:
    cost, pos, dir = heapq.heappop(q)
    if pos == goal:
        # because everything cheaper is done!
        break
    if (pos, dir) in visited:
        continue
    cost_from_here = minimum_cost(pos, dir)
    if cost_from_here is None or cost_from_here + cost > best_cost:
        # we're not on a best path
        continue
    all_visited.add(pos)
    visited.add((pos, dir))
    x, y = pos
    # keep going in the same direction
    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] in ".E":
        heapq.heappush(q, (cost + 1, (nx, ny), dir))
    clockwise = (dir + 1) % 4
    dx, dy = directions[clockwise]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] in ".E":
        heapq.heappush(q, (cost + 1001, (nx, ny), clockwise))
    ccw = (dir - 1) % 4
    dx, dy = directions[ccw]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] in ".E":
        heapq.heappush(q, (cost + 1001, (nx, ny), ccw))

print(len(all_visited))
