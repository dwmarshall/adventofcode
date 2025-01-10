from collections import Counter
import math
import sys

DISTANCE = int(sys.argv[2]) if len(sys.argv) > 2 else 10000

points = []

# NSEW
limits = [-math.inf, math.inf, -math.inf, math.inf]

with open(sys.argv[1], "r") as file:
    for line in file:
        x, y = map(int, line.split(","))
        points.append((x, y))
        limits[0] = max(limits[0], x)
        limits[1] = min(limits[1], x)
        limits[2] = max(limits[2], y)
        limits[3] = min(limits[3], y)

closest = Counter()
safe_points = 0

for xx in range(limits[1], limits[0] + 1):
    for yy in range(limits[3], limits[2] + 1):
        distances = []
        for i, p in enumerate(points):
            distance = abs(xx - p[0]) + abs(yy - p[1])
            distances.append((distance, i))
        distances.sort()
        if distances[0][0] < distances[1][0]:
            closest[distances[0][1]] += 1
        total_distance = sum(d[0] for d in distances)
        if total_distance < DISTANCE:
            safe_points += 1

print(f"Part 1: The biggest area is {closest.most_common(1)[0][1]}")
print(f"Part 2: There are {safe_points} safe points.")
