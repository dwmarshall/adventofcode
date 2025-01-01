from collections.abc import Iterator
import sys


MULTIPLIER_A = 16807
MULTIPLIER_B = 48271
MODULUS = 2147483647


def generator(start: int, multiplier: int, modulus: int) -> Iterator[int]:
    number = start
    while True:
        number *= multiplier
        number %= MODULUS
        if number % modulus == 0:
            yield number


genA = generator(int(sys.argv[1]), MULTIPLIER_A, 4)
genB = generator(int(sys.argv[2]), MULTIPLIER_B, 8)

matches = 0

for _ in range(5_000_000):
    A = next(genA)
    B = next(genB)
    if A & 65535 == B & 65535:
        matches += 1

print(f"Part 1: There are {matches} matches.")
