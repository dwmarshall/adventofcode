from fractions import Fraction
from functools import cache
import sys

# directions = {
#     "nw": (1, 0, 0),
#     "se": (-1, 0, 0),
#     "n": (0, 1, 0),
#     "s": (0, -1, 0),
#     "ne": (0, 0, 1),
#     "sw": (0, 0, -1),
# }

directions = {
    "n": (-1, 0),
    "ne": (Fraction(-1, 2), Fraction(1, 2)),
    "se": (Fraction(1, 2), Fraction(1, 2)),
    "s": (1, 0),
    "sw": (Fraction(1, 2), Fraction(-1, 2)),
    "nw": (Fraction(-1, 2), Fraction(-1, 2)),
}


@cache
def steps(pos: tuple[Fraction, Fraction]) -> int:
    x, y = pos
    if y == 0:
        return abs(x)
    if y < 0:
        d = "ne" if x > 0 else "se"
    else:
        d = "nw" if x > 0 else "sw"
    dx, dy = directions[d]
    nx, ny = x + dx, y + dy
    return 1 + steps((nx, ny))


with open(sys.argv[1], "r") as file:
    for line in file:
        max_steps = 0
        pos = (0, 0)
        for d in line.strip().split(","):
            pos = tuple(a + b for a, b in zip(pos, directions[d]))
            max_steps = max(max_steps, steps(pos))
        print(f"Part 1: It takes {steps(pos)} steps to get back to (0,0)")
        print(f"Part 2: Maximum distance was {max_steps}")
