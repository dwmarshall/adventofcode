from itertools import combinations, count
from math import inf
import re
import sys
from unionfind import UnionFind

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def analyze(r: list[list[int, int, int, int]]) -> set[int]:
    p = [(x[0], x[1]) for x in r]

    uf = UnionFind(len(r))

    for i, j in combinations(range(len(r)), 2):
        if manhattan_distance(p[i], p[j]) <= 2:
            uf.union(i, j)

    islands = {uf.find(i) for i in range(len(r))}
    return islands


def advance(r: list[list[int, int, int, int]], t: int = 1) -> None:
    for i in range(len(r)):
        r[i][0] += t * r[i][2]
        r[i][1] += t * r[i][3]


def display(r: list[list[int, int, int, int]]) -> None:
    positions = [x[0:2] for x in r]
    min_x = min(x[0] for x in positions)
    max_x = max(x[0] for x in positions)
    min_y = min(x[1] for x in positions)
    max_y = max(x[1] for x in positions)
    grid = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for px, py in positions:
        grid[py - min_y][px - min_x] = "#"
    lines = []
    for i in range(len(grid)):
        lines.append("".join(grid[i]))
    print("\n".join(lines))


NUMBER = r"-?\d+"
PAIR = rf"\<\s*({NUMBER}),\s*({NUMBER})\>"

robots = []

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(rf"position={PAIR} velocity={PAIR}", line):
            robots.append(list(map(int, m.groups())))
        else:
            print("Bogus line!")
            print(line)

# Decide about how many seconds we need to advance things
minmax = [inf, -inf, inf, -inf]
minmax_robots = [None] * 4
for i in range(len(robots)):
    if robots[i][0] < minmax[0]:
        minmax[0] = robots[i][0]
        minmax_robots[0] = robots[i]
    if robots[i][0] > minmax[1]:
        minmax[1] = robots[i][0]
        minmax_robots[1] = robots[i]
    if robots[i][1] < minmax[2]:
        minmax[2] = robots[i][1]
        minmax_robots[2] = robots[i]
    if robots[i][1] > minmax[3]:
        minmax[3] = robots[i][1]
        minmax_robots[3] = robots[i]

# Find the time when they're about 1000 apart
x_seconds = (100 + minmax_robots[0][0] - minmax_robots[1][0]) // (
    minmax_robots[1][2] - minmax_robots[0][2]
)
y_seconds = (100 + minmax_robots[2][1] - minmax_robots[3][1]) // (
    minmax_robots[3][3] - minmax_robots[2][3]
)

starting_seconds = min(x_seconds, y_seconds)
advance(robots, starting_seconds)
least_islands = float("inf")

for t in count():
    islands = len(analyze(robots))
    print(f"{t}: {islands}")
    if islands < least_islands:
        least_islands = islands
    if len(analyze(robots)) < 10:
        print("Part 1:")
        display(robots)
        print(f"Part 2: This took {starting_seconds + t} seconds.")
        break
    advance(robots)
