from collections.abc import Iterator
import sys

square = int(sys.argv[1])


def southeast_corners() -> Iterator[tuple[int, int, int]]:
    i, x, y = 1, 0, 0
    while True:
        yield i * i, x, y
        i, x, y = i + 2, x + 1, y + 1


def coordinates(n: int) -> tuple[int, int]:
    se_corners = southeast_corners()
    cn, cx, cy = next(se_corners)
    while cn < n:
        cn, cx, cy = next(se_corners)
    if cn == n:
        return cx, cy
    wn, wx, wy = cn, cx, cy
    # bottom row from right to left
    for _ in range(cx * 2):
        wn -= 1
        wy -= 1
        if wn == n:
            return wx, wy
    # left side up
    for _ in range(cy * 2):
        wn -= 1
        wx -= 1
        if wn == n:
            return wx, wy
    # top side across
    for _ in range(cx * 2):
        wn -= 1
        wy += 1
        if wn == n:
            return wx, wy
    # right side down
    for _ in range(cy * 2):
        wn -= 1
        wx += 1
        if wn == n:
            return wx, wy


x, y = coordinates(square)
distance = abs(x) + abs(y)
print(f"Part 1: It takes {distance} steps to carry from {square} to 1")
