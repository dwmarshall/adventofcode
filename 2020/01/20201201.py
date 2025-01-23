from math import prod
import sys


def entries(numbers: set[int], desired: int, n: int) -> set[int]:
    if n == 1:
        return {desired} if desired in numbers else None
    else:
        for x in numbers:
            if (s := entries(numbers, desired - x, n - 1)) is not None:
                return {x} | s
        return None


with open(sys.argv[1], "r") as file:
    numbers = set(map(int, file.readlines()))

print(f"Part 1: The product is {prod(entries(numbers, 2020, 2))}")
print(f"Part 2: The product is {prod(entries(numbers, 2020, 3))}")
