import heapq
import sys

N = 70
B = 1024

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

bytes = []


with open(sys.argv[1], "r") as file:
    for line in file:
        col, row = line.strip().split(",")
        bytes.append((int(row), int(col)))

unavailable = set(bytes[:B])

q = [(0, (0, 0))]

while q:
    steps, pos = heapq.heappop(q)
    if pos == (N, N):
        print(f"Reached goal in {steps} steps")
        break
    if pos in unavailable:
        continue
    unavailable.add(pos)
    row, col = pos
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr <= N and 0 <= nc <= N and (nr, nc) not in unavailable:
            heapq.heappush(q, (steps + 1, (nr, nc)))
