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

blocks = set(bytes[:B])

q = [(0, (0, 0), (0, 0))]

while True:
    visited = set()
    q = [(0, (0, 0), ((0, 0),))]
    possible_path = None
    while q:
        steps, pos, path = heapq.heappop(q)
        if pos == (N, N):
            possible_path = path
        if pos in blocks | visited:
            continue
        visited.add(pos)
        x, y = pos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= N and (nx, ny) not in blocks | visited:
                heapq.heappush(q, (steps + 1, (nx, ny), path + ((nx, ny),)))
    if possible_path is None:
        break
    while bytes[B] not in possible_path:
        print(f"Adding {bytes[B]} to the grid")
        blocks.add(bytes[B])
        B += 1
    print(f"{bytes[B]} was in the old path, adding it")
    blocks.add(bytes[B])


print(f"Critical block was {bytes[B]}")
