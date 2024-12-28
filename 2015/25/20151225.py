from collections.abc import Iterator
import sys


def coordinates() -> Iterator[tuple[int, int]]:
    max_r = 1
    r, c = 1, 1
    while True:
        yield r, c
        if r == 1:
            max_r += 1
            r, c = max_r, 1
        else:
            r, c = r - 1, c + 1


def values() -> Iterator[int]:
    v = 20151125
    while True:
        yield v
        v *= 252533
        _, v = divmod(v, 33554393)


goal = (int(sys.argv[1]), int(sys.argv[2]))

for c, v in zip(coordinates(), values()):
    if c == goal:
        print(v)
        break
