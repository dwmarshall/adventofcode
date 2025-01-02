from itertools import pairwise
import re
import sys

SIZE, USED, AVAIL, PCT = 0, 1, 2, 3
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

nodes = dict()


def zero_node(g: dict) -> tuple[int, int]:
    for k, v in g.items():
        if v[USED] == 0:
            return k


def zero_path(g: dict, goal: tuple[int, int]) -> list[tuple[int, int]]:
    """What is the path from the zero to the desired location?"""
    locations = [(zero_node(g), [])]
    visited = set()
    while locations:
        new_locations = []
        for pos, path in locations:
            if pos in visited or pos == (goal[0] + 1, goal[1]):
                continue
            visited.add(pos)
            if pos == goal:
                return path + [goal]
            x, y = pos
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in path:
                    continue
                if (nx, ny) in g and g[(nx, ny)][USED] <= g[(x, y)][SIZE]:
                    new_locations.append(((nx, ny), path + [(x, y)]))
        locations = new_locations


def process_moves(g: dict, moves: list[tuple[int, int]]) -> int:
    """The number of steps to process a move list"""
    moves = list(moves)
    steps = 0
    for a, b in pairwise(list(moves)):
        assert g[a][USED] == 0
        assert g[b][USED] <= g[a][SIZE]
        g[a][USED] = g[b][USED]
        g[b][USED] = 0
        steps += 1
    return steps


with open(sys.argv[1], "r") as file:
    for line in file:
        if re.match(r"/dev/grid", line):
            x, y, *data = re.findall(r"\d+", line)
            nodes[(int(x), int(y))] = list(map(int, data))

max_x = max(x for x, _ in nodes.keys())
total_steps = 0
intermediate_goals = [(x, 0) for x in range(max_x, -1, -1)]

for i in range(len(intermediate_goals) - 1):
    this_path = zero_path(nodes, intermediate_goals[i + 1])
    total_steps += process_moves(nodes, this_path)
    total_steps += process_moves(nodes, reversed(intermediate_goals[i : i + 2]))

print(f"Part 2: It takes {total_steps} total steps.")
