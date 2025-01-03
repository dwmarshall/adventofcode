from collections import defaultdict
from itertools import pairwise, permutations
import string
import sys

grid = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

points = set()
start = None

with open(sys.argv[1], "r") as file:
    for y, line in enumerate(file):
        grid.append(list(line.strip()))
        for x, c in enumerate(line):
            if c in string.digits:
                points.add((x, y))
                if c == "0":
                    start = (x, y)


def pair_paths(
    g: list[list[str]], points: set[tuple[int, int]]
) -> dict[tuple[int, int], dict[tuple[int, int], int]]:
    lookup_map = defaultdict(dict)
    for p1 in points:
        found = set(lookup_map[p1].keys())
        visited = set()
        locations = [p1]
        steps = 0
        while len(points) - len(found) > 0:
            new_locations = []
            for p in locations:
                if p in points and p not in found:
                    lookup_map[p1][p] = steps
                    lookup_map[p][p1] = steps
                    found.add(p)
                x, y = p
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in visited:
                        continue
                    if 0 <= nx < len(g[0]) and 0 <= ny < len(g) and g[ny][nx] != "#":
                        new_locations.append((nx, ny))
                        visited.add((nx, ny))

            locations = new_locations
            steps += 1
    return lookup_map


def fewest_steps(part_two: bool = False) -> int:
    min_steps = float("inf")
    for t in permutations(points):
        full_path = (start,) + t
        if part_two:
            full_path += (start,)
        steps = 0
        for a, b in pairwise(full_path):
            steps += pair_map[a][b]
        min_steps = min(min_steps, steps)

    return min_steps


pair_map = pair_paths(grid, points)


# Remove start from points for correct permutations
points.remove(start)

print(f"Part 1: Fewest steps needed is {fewest_steps()}.")
print(f"Part 2: Fewest steps needed is {fewest_steps(True)}")
