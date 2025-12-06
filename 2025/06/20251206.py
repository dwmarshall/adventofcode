from math import prod
import sys

numbers: list[list[int]] = []
operators: list[str] | None = None

with open(sys.argv[1], "r") as file:
    # handle first line specially
    for first in map(int, file.readline().split()):
        numbers.append([first])
    for line in file:
        if "+" in line or "*" in line:
            operators = line.strip().split()
        else:
            for i, num in enumerate(map(int, line.split())):
                numbers[i].append(num)

part1_total = 0

assert operators is not None

for i in range(len(numbers)):
    if operators[i] == "+":
        part1_total += sum(numbers[i])
    else:
        part1_total += prod(numbers[i])

print(f"Part 1: The total is {part1_total}")

print(numbers)
for i in range(len(numbers)):
    new_numbers: list[int] = [0] * 4
    for number in numbers[i]:
        digit = number % 10
        if digit:
            new_numbers[i] *= 10
            new_numbers[i] += digit
    print(new_numbers)

# Now get the numbers differently
# for i in range(len(numbers)):
#     print(numbers[i])
#     new_numbers = [0] * len(numbers[i])

# for i in range(len(numbers)):
#     new_numbers = [0] * 3
#     for j in range(3):
#         new_numbers[i] *= 10
#         new_numbers[i] += numbers[i][j] % 10
#     print(new_numbers)
