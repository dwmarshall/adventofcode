from collections import deque
from itertools import accumulate, combinations
import sys

NUMBERS = 25


with open(sys.argv[1], "r") as file:
    numbers = list(map(int, file.readlines()))

deck = deque(numbers[:NUMBERS], maxlen=NUMBERS)

for i in range(NUMBERS, len(numbers)):
    new_number = numbers[i]
    if any(a + b == new_number for a, b in combinations(deck, 2)):
        deck.append(new_number)
    else:
        break

print(f"Part 1: The first number is {new_number}")

prefix_sums = list(accumulate(numbers))

for i, j in combinations(range(len(numbers)), 2):
    if prefix_sums[j] - prefix_sums[i] == new_number:
        break

slice = numbers[i + 1 : j + 1]
print(f"Part 2: The encryption weakness is {min(slice) + max(slice)}")
