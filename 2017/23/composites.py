from math import isqrt
import sys


def is_composite(n: int) -> bool:
    for factor in range(2, isqrt(n) + 1):
        if n % factor == 0:
            return True
    return False


left = int(sys.argv[1])
right = int(sys.argv[2])
step = int(sys.argv[3])

composites = 0
for i in range(left, right + 1, step):
    if is_composite(i):
        composites += 1

print(f"There are {composites} composite numbers between {left} and {right} inclusive.")
