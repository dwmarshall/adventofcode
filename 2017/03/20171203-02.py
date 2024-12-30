from collections import defaultdict
from collections.abc import Iterator
from itertools import product
import sys

squares = defaultdict(int)
squares[(0, 0)] = 1

INPUT = int(sys.argv[1])


def spiral_coordinates() -> Iterator[tuple[int, int]]:
    x, y = 0, 0
    yield x, y
    ring = 0
    while True:
        if x == y:
            ring += 1
            y += 1
            yield x, y
        # go up ring times
        for _ in range(2 * ring - 1):
            x -= 1
            yield x, y
        # go to the left 2 * ring times
        for _ in range(2 * ring):
            y -= 1
            yield x, y
        # go down ring * 2 times
        for _ in range(2 * ring):
            x += 1
            yield x, y
        # finally, go right 2 * ring times
        for _ in range(2 * ring):
            y += 1
            yield x, y


def adjacent_sum(s: dict, x: int, y: int) -> int:
    neighbor_sum = 0
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        neighbor_sum += squares[(x + dx, y + dy)]
    return neighbor_sum


c = spiral_coordinates()
x, y = next(c)
last_written_number = 1
while last_written_number <= INPUT:
    x, y = next(c)
    last_written_number = squares[(x, y)] = adjacent_sum(squares, x, y)

print(f"The first written number is {last_written_number}")
