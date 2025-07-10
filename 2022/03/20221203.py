import sys


def priority(x: str) -> int:
    if ord(x) - ord("A") <= 26:
        return 27 + ord(x) - ord("A")
    else:
        return 1 + ord(x) - ord("a")


with open(sys.argv[1], "r") as file:
    lines = [line.rstrip("\n") for line in file]

# Part 1
part1_sum = 0

for rucksack in lines:
    midpoint = len(rucksack) // 2
    first_compartment = set(rucksack[:midpoint])
    second_compartment = set(rucksack[midpoint:])
    common_item = (first_compartment & second_compartment).pop()
    part1_sum += priority(common_item)

print(f"Part 1: Sum is {part1_sum}")

# Part 2

part2_sum = 0

for i in range(0, len(lines), 3):
    common_item = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
    part2_sum += priority(common_item.pop())

print(f"Part 2: Sum is {part2_sum}")
