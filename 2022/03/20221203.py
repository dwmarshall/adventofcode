import sys

running_sum = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        first_compartment = set(line[: len(line) // 2])
        second_compartment = set(line[len(line) // 2 : -1])
        common_item = (first_compartment & second_compartment).pop()
        if ord(common_item) - ord("A") <= 26:
            priority = 27 + ord(common_item) - ord("A")
        else:
            priority = 1 + ord(common_item) - ord("a")
        running_sum += priority

print(f"Part 1: Sum is {running_sum}")
