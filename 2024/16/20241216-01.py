import heapq
import sys

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

q = [(0, start, 1)]

visited = set()

while q:
    # print(q)
    cost, pos, dir = heapq.heappop(q)
    if pos == goal:
        print(f"Cost: {cost}")
        break
    if (pos, dir) in visited:
        continue
    visited.add((pos, dir))
    x, y = pos
    grid[x][y] = "X"
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
