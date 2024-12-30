from collections import defaultdict
import re
import sys

weights = dict()
graph = dict()

with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.match(r"(\S+) \((\d+)\)(?: -> (.*))?", line)
        name, weight, dependencies = m.groups()
        weights[name] = int(weight)
        if dependencies is not None:
            others = dependencies.split(", ")
            graph[name] = set(others)

incoming = defaultdict(int)

for name in weights.keys():
    if name not in graph:
        continue
    for dependency in graph[name]:
        incoming[dependency] += 1

topological_sort = []

unvisited = set(weights.keys())
while unvisited:
    nodes = [x for x in unvisited if incoming[x] == 0]
    curr = nodes[0]
    topological_sort.append(curr)
    unvisited.remove(curr)
    if curr in graph:
        for x in graph[curr]:
            incoming[x] -= 1

print(f"Part 1: The root program is {topological_sort[0]}")


def combined_weight(p: str) -> int:
    if p not in graph:
        return weights[p]
    weight = weights[p]
    for d in graph[p]:
        weight += combined_weight(d)
    return weight


def correct_weight(p: str, expected_weight: int = 0) -> None:
    if p not in graph:
        return -1
    weight_tuples = []
    for d in graph[p]:
        weight_tuples.append((combined_weight(d), d))
    weight_tuples.sort()
    first_weight = weight_tuples[0][0]
    if all(t[0] == first_weight for t in weight_tuples):
        new_weight = expected_weight - first_weight * len(weight_tuples)
        print(f"Part 2: {p} should have a weight of {new_weight}")
    if weight_tuples[0][0] != weight_tuples[1][0]:
        return correct_weight(weight_tuples[0][1], weight_tuples[1][0])
    else:
        return correct_weight(weight_tuples[-1][1], weight_tuples[0][0])


correct_weight(topological_sort[0])
