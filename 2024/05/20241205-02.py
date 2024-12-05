from collections import Counter, defaultdict
import sys

requirements = defaultdict(set)
middle_numbers = 0
source_lines = []

for line in sys.stdin:
    if "|" in line:
        required, requiring = line.split("|")
        requirements[int(requiring)].add(int(required))
    elif "," in line:
        source_lines.append(line)


for s in source_lines:
    original_order = list(map(int, s.split(",")))
    incoming = Counter()
    for p in original_order:
        incoming[p] = len([x for x in requirements[p] if x in original_order])
    unvisited = set(original_order)
    topological_sort = []
    while unvisited:
        candidates = set([x for x in incoming if incoming[x] == 0])
        choices = unvisited & candidates
        curr = choices.pop()
        for k in incoming.keys():
            if curr in requirements[k]:
                incoming[k] -= 1
        topological_sort.append(curr)
        unvisited.discard(curr)
    if topological_sort != original_order:
        middle_numbers += topological_sort[len(topological_sort) // 2]

print(middle_numbers)
