from collections.abc import Iterator
from math import isqrt
import sys

STARTING_PATTERN = ".#./..#/###"
ITERATIONS = int(sys.argv[2])


def arrangements(s: str) -> Iterator[str]:
    for t in [s, flip_vertically(s), flip_horizontally(s)]:
        yield t
        for _ in range(3):
            t = rotate(t)
            yield (t)


def flip_vertically(s: str) -> str:
    return "/".join(reversed(s.split("/")))


def flip_horizontally(s: str) -> str:
    return "/".join(line[::-1] for line in s.split("/"))


def rotate(s: str) -> str:
    lines = s.split("/")
    output = []
    for i in range(len(lines[0])):
        output.append("".join(x[i] for x in lines[::-1]))
    return "/".join(output)


def divide(s: str) -> list[str]:
    grid = [x for x in s.split("/")]
    assert len(grid) == len(grid[0])
    size = 2 if len(grid) % 2 == 0 else 3
    tiles_per_row = len(grid) // size
    results = []
    for t in range(tiles_per_row * tiles_per_row):
        tile = []
        row, col = divmod(t, tiles_per_row)
        for i in range(size):
            tile.append(grid[row * size + i][size * col : size * col + size])
        results.append("/".join(tile))
    return results


def combine(L: list[str]) -> str:
    if len(L) == 1:
        return L[0]

    tile_group = isqrt(len(L))
    assert tile_group * tile_group == len(L)

    tile_size = L[0].count("/") + 1
    output = [""] * (tile_group * tile_size)

    for i in range(tile_group):
        for j in range(tile_size):
            line = ""
            for k in range(tile_group):
                line += L[i * tile_group + k].split("/")[j]
            output[i * tile_size + j] = line
    return "/".join(output)


rules = dict()
with open(sys.argv[1], "r") as file:
    for line in file:
        left, right = [x.strip() for x in line.split("=>")]
        rules[left] = right

pattern = STARTING_PATTERN
for _ in range(ITERATIONS):
    pieces = divide(pattern)
    new_pieces = [None] * len(pieces)
    for i, p in enumerate(pieces):
        for a in arrangements(p):
            if a in rules:
                new_pieces[i] = rules[a]
                break
        if new_pieces[i] is None:
            print(f"No match for {p}!")

    assert not any(p is None for p in pieces)
    pattern = combine(new_pieces)

print(f"There are {pattern.count("#")} pixels on after {ITERATIONS} iterations.")
