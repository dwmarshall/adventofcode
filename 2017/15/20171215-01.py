from collections.abc import Iterator
import sys


MULTIPLIER_A = 16807
MULTIPLIER_B = 48271
MODULUS = 2147483647


def generator(start: int, multiplier: int) -> Iterator[int]:
    number = start
    while True:
        number *= multiplier
        number %= MODULUS
        yield number


genA = generator(int(sys.argv[1]), MULTIPLIER_A)
genB = generator(int(sys.argv[2]), MULTIPLIER_B)

matches = 0

for _ in range(40_000_000):
    A = next(genA)
    B = next(genB)
    if A & 65535 == B & 65535:
        matches += 1

print(f"Part 1: There are {matches} matches.")
