import sys
from typing import List


def is_safe(n: List[int]) -> bool:
    print(n)
    increasing = n[0] < n[1]
    for i in range(1, len(n)):
        if increasing and n[i] <= n[i - 1]:
            return False
        if not increasing and n[i] >= n[i - 1]:
            return False
        if abs(n[i] - n[i - 1]) > 3:
            return False
    return True


num_safe = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        digits = line.strip().split()
        numbers = list(map(int, digits))
        if is_safe(numbers):
            print(f"{numbers} is safe")
            num_safe += 1
        elif any(is_safe(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers))):
            num_safe += 1
print(num_safe)
