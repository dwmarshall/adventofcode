from collections import defaultdict
import re
import sys

colors = {}
graph = defaultdict(dict)


def bag_id(s: str) -> int:
    if s not in colors:
        colors[s] = len(colors)
    return colors[s]


def bags_needed(b: int) -> int:
    total = 1
    for k, v in graph[b].items():
        total += v * bags_needed(k)
    return total


with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.match(r"(.*) bags contain", line)
        requires = bag_id(m.group(1))
        for quantity, color in re.findall(r"(\d+) (.*?) bag", line):
            dependent = bag_id(color)
            graph[requires][dependent] = int(quantity)

bags = set()
working = set()
working.add(bag_id("shiny gold"))

while working:
    curr = working.pop()
    for c, d in graph.items():
        if curr in d and c not in bags:
            bags.add(c)
            working.add(c)

print(f"Part 1: There are {len(bags)} distinct colors")

print(f"Part 2: We hold {bags_needed(bag_id("shiny gold")) - 1} bags")
