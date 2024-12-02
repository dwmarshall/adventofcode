from itertools import pairwise
import sys
from typing import List


def is_safe(n: List[int]) -> bool:
    increasing = n[0] < n[1]
    for a, b in pairwise(n):
        if increasing and a >= b:
            return False
        elif not increasing and a <= b:
            return False
        if abs(b - a) > 3:
            return False
    return True


num_safe = 0

for line in sys.stdin:
    digits = line.strip().split()
    numbers = list(map(int, digits))
    if is_safe(numbers):
        print(f"{numbers} is safe")
        num_safe += 1
    else:
        print(f"{numbers} is not safe")

print(num_safe)
