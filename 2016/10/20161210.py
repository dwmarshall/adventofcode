from collections import defaultdict
from functools import reduce
import operator
import re
import sys

robots_have = defaultdict(list)
robots_give = defaultdict(dict)
output = dict()

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"value (\d+) goes to bot (\d+)", line):
            value, bot = list(map(int, m.groups()))
            robots_have[bot].append(value)
        elif m := re.match(
            r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
            line,
        ):
            bot = int(m.group(1))
            low = (m.group(2), int(m.group(3)))
            high = (m.group(4), int(m.group(5)))
            robots_give[bot] = {"low": low, "high": high}

while q := [k for k in robots_have.keys() if len(robots_have[k]) == 2]:
    for robot in q:
        a, b = sorted(robots_have[robot])
        if a == 17 and b == 61:
            print(f"Part 1: Robot {robot} is comparing 17 and 61")
        inventory = {"low": a, "high": b}
        for level in ["low", "high"]:
            type, id = robots_give[robot][level]
            if type == "bot":
                robots_have[id].append(inventory[level])
            else:
                output[id] = inventory[level]
        robots_have[robot] = []

product = reduce(operator.mul, [output[x] for x in range(3)])
print(f"Part 2: The product is {product}")
