from collections import defaultdict
from itertools import pairwise, permutations
import re
import sys

places = defaultdict(dict)

pattern = re.compile(r"(\S+) would (gain|lose) (\d+).*?(\S+)\.")

with open(sys.argv[1], "r") as file:
    for line in file:
        m = pattern.match(line)
        points = int(m.group(3))
        if m.group(2) == "lose":
            points = -points
        a = m.group(1)
        b = m.group(4)
        places[a][b] = points

max_happiness = 0


for perm in permutations(places.keys()):
    happiness = places[perm[0]][perm[-1]] + places[perm[-1]][perm[0]]
    for a, b in pairwise(perm):
        happiness += places[a][b] + places[b][a]
    max_happiness = max(max_happiness, happiness)

print(max_happiness)
