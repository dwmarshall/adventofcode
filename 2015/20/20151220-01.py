from itertools import count
from math import isqrt
import sys

goal = int(sys.argv[1])


def proper_divisors(n: int) -> set[int]:
    result = {1, n}
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result


def presents(n: int) -> int:
    return 10 * sum(proper_divisors(n))


for i in count(1):
    if presents(i) > goal:
        print(f"First house is {i}")
        break
