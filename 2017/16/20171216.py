from collections import deque
from functools import cache
from itertools import count
import re
import string
import sys


@cache
def perform_dance(s: str, moves: tuple[str]) -> str:
    dancers = deque(s)

    for move in moves:
        if m := re.match(r"s(\d+)", move):
            dancers.rotate(int(m.group(1)))
        elif m := re.match(r"x(\d+)/(\d+)", move):
            a = int(m.group(1))
            b = int(m.group(2))
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif m := re.match(r"p([a-z])/([a-z])", move):
            a = dancers.index(m.group(1))
            b = dancers.index(m.group(2))
            dancers[a], dancers[b] = dancers[b], dancers[a]
    return "".join(dancers)


num_dancers = int(sys.argv[2]) if len(sys.argv) > 2 else 16

with open(sys.argv[1], "r") as file:
    moves = tuple(file.read().strip().split(","))

original_dancers = string.ascii_lowercase[:num_dancers]
dancers = original_dancers
cycle = None

for i in count():
    dancers = perform_dance(dancers, moves)
    if dancers == original_dancers:
        cycle = i + 1
        break


part1_dancers = perform_dance(original_dancers, moves)
print(f"Part 1: After one dance: {part1_dancers}")

dancers = original_dancers
for _ in range(1_000_000_000 % cycle):
    dancers = perform_dance(dancers, moves)

print(f"Part 2: After the last dance: {dancers}")
