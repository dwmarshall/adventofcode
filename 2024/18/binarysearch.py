import heapq
import sys

N = int(sys.argv[2])
B = int(sys.argv[3])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

bytes = []


with open(sys.argv[1], "r") as file:
    for line in file:
        x, y = line.strip().split(",")
        bytes.append((int(x), int(y)))

left = B
right = len(bytes)

while left < right:
    mid = (left + right) // 2
    blocks = set(bytes[:mid])
    visited = set()
    q = [(0, (0, 0))]
    while q:
        steps, pos = heapq.heappop(q)
        if pos == (N, N):
            break
        if pos in blocks | visited:
            continue
        visited.add(pos)
        x, y = pos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= N and (nx, ny) not in blocks | visited:
                heapq.heappush(q, (steps + 1, (nx, ny)))
    if pos == (N, N):
        left = mid + 1
    else:
        right = mid - 1

print(bytes[left - 1])
