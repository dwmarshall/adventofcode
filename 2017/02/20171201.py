from itertools import permutations
import sys

checksum1 = 0
checksum2 = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        digits = list(map(int, line.split()))
        checksum1 += max(digits) - min(digits)
        for a, b in permutations(digits, 2):
            if a % b == 0:
                checksum2 += a // b
                break

print(f"Part 1: {checksum1}")
print(f"Part 2: {checksum2}")
