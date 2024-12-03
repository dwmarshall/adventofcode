import sys

total_paper = 0

for line in sys.stdin:
    dimensions = line.strip().split("x")
    length, width, depth = list(map(int, dimensions))
    areas = []
    areas.append(length * width)
    areas.append(width * depth)
    areas.append(length * depth)
    total_paper += min(areas) + 2 * sum(areas)

print(total_paper)
