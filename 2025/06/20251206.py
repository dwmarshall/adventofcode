from math import prod
import sys

input: list[str]

with open(sys.argv[1], "r") as file:
    input = file.readlines()

p1_numbers: list[list[int]] = []
p1_operators: list[str] | None = None

# Part 1
# handle first line specially
for first in map(int, input[0].split()):
    p1_numbers.append([first])
for line in input[1:]:
    if "+" in line or "*" in line:
        p1_operators = line.strip().split()
    else:
        for i, num in enumerate(map(int, line.split())):
            p1_numbers[i].append(num)

part1_total = 0

assert p1_operators is not None

for i in range(len(p1_numbers)):
    if p1_operators[i] == "+":
        part1_total += sum(p1_numbers[i])
    else:
        part1_total += prod(p1_numbers[i])

print(f"Part 1: The total is {part1_total}")

# For part 2, we do numbers vertically
part2_total = 0

p2_ops: list[tuple[str, int]] = []

for i, c in enumerate(input[-1]):
    if c in "*+":
        p2_ops.append((c, i))
p2_ops.append(("X", len(input[-1]) + 1))

for p in range(len(p2_ops) - 1):
    problem_length = p2_ops[p + 1][1] - p2_ops[p][1] - 1
    numbers: list[int] = [0] * problem_length
    offset = p2_ops[p][1]
    for col in range(problem_length):
        for j in range(len(input) - 1):
            if input[j][col + offset] != " ":
                numbers[col] *= 10
                numbers[col] += int(input[j][col + offset])
    if p2_ops[p][0] == "+":
        part2_total += sum(numbers)
    else:
        part2_total += prod(numbers)

print(f"Part 2: The new total is {part2_total}")
