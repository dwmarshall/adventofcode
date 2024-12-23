from itertools import islice
import operator
import sys
from typing import Iterator

mix = operator.__xor__


def prune(x: int) -> int:
    return x % 16777216


def sn_generator(n: int) -> Iterator[int]:
    while True:
        n = prune(mix(n, 64 * n))
        n = prune(mix(n, n // 32))
        n = prune(mix(n, n * 2048))
        yield n


secret_number_sum = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        v = int(line.strip())
        secret_number_sum += list(islice(sn_generator(v), 1999, 2000))[0]

print(secret_number_sum)
