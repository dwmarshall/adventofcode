import sys


def max_joltage(s: str, length: int) -> int:
    digits: list[int] = [int(c) for c in s]
    trim = max(0, length - 1)
    digits = digits[:-trim] if trim else digits
    for digit in range(9, 0, -1):
        if digit in digits:
            i = digits.index(digit)
            if length == 1:
                return digit
            else:
                return 10 ** (length - 1) * digit + max_joltage(s[i + 1 :], length - 1)

    assert False


part1_sum = 0
part2_sum = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        part1_sum += max_joltage(line.strip(), 2)
        part2_sum += max_joltage(line.strip(), 12)

print(f"Part 1: Total output is {part1_sum}")
print(f"Part 2: Total output is {part2_sum}")
