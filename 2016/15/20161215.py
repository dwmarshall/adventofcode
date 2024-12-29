from collections.abc import Callable, Iterator
import re
import sys


def ticks(stops: int, initial_pos: int, depth: int) -> Iterator[int]:
    """disc is a depth ticks down with initial_pos and stops positions"""
    offset = (initial_pos + depth) % stops
    next_tick = (stops - offset) % stops
    while True:
        yield next_tick
        next_tick += stops


def passes_gen(stops: int, initial_pos: int, depth: int) -> Callable:
    def passes(t: int) -> bool:
        return (t + depth + initial_pos) % stops == 0

    return passes


discs = []

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"Disc \#(\d+) has (\d+) positions.*position (\d+)", line):
            depth, stops, initial_pos = list(map(int, m.groups()))
            discs.append((stops, initial_pos, depth))

discs.sort(reverse=True)

tests = [passes_gen(*t) for t in discs]

for t in ticks(*discs[0]):
    if all(func(t) for func in tests):
        print(f"Part 1: first time is {t}")
        break

tests.append(passes_gen(11, 0, len(tests) + 1))

for t in ticks(*discs[0]):
    # print(t)
    if all(func(t) for func in tests):
        print(f"Part 2: first time is {t}")
        break
