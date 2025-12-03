import sys


def matching_doubles(x: int, y: int) -> list[int]:
    result: list[int] = []

    if len(str(x)) % 2 == 1:
        x = int("1" + "0" * len(str(x)))
    halfx = int(str(x)[: len(str(x)) // 2])
    curr = int(str(halfx) * 2)
    while curr <= y:
        if curr >= x:
            result.append(curr)
        halfx += 1
        curr = int(str(halfx) * 2)
    return result


def matching_copies(x: int, y: int) -> set[int]:
    result: set[int] = set()

    max_base = int(str(y)[: 1 + len(str(y)) // 2])
    for base in range(1, 1 + max_base):
        for copies in range(2, 1 + len(str(y)) // len(str(base))):
            candidate = int(str(base) * copies)
            if x <= candidate <= y:
                result.add(candidate)
    return result


input_ranges: list[tuple[int, int]] = []

with open(sys.argv[1], "r") as file:
    for line in file:
        for pair in line.strip(",\n").split(","):
            left, right = pair.split("-")
            input_ranges.append((int(left), int(right)))

part1_sum = 0

for x, y in input_ranges:
    part1_sum += sum(matching_doubles(x, y))

print(f"Part 1: The sum is {part1_sum}")

part2_sum = 0

for x, y in input_ranges:
    res = matching_copies(x, y)
    part2_sum += sum(res)

print(f"Part 2: The sum is {part2_sum}")
