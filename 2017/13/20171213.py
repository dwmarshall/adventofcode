from itertools import count
import sys


def severity() -> int:
    return sum(
        t * depths[t]
        for t in range(max(depths) + 1)
        if t in depths and t % (2 * (depths[t] - 1)) == 0
    )


def safe(delay: int) -> bool:
    return all(
        t not in depths or (delay + t) % (2 * (depths[t] - 1)) != 0
        for t in range(max(depths) + 1)
    )


depths = dict()

with open(sys.argv[1], "r") as file:
    for line in file:
        layer, depth = map(int, line.split(":"))
        depths[layer] = depth

print(f"Part 1: Total severity is {severity()}")

for d in count():
    if safe(d):
        print(f"Part 2: Least delay is {d}")
        break
