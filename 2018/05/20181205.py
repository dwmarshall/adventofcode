import string
import sys

stack = []


def reacted(s: str) -> int:
    stack = []
    for c in s:
        opposite = c.upper() if c in string.ascii_lowercase else c.lower()
        if stack and stack[-1] == opposite:
            stack.pop()
        else:
            stack.append(c)

    return len(stack)


with open(sys.argv[1], "r") as file:
    polymer = file.readline()

print(f"Part 1: Remaining units = {reacted(polymer)}")

p2_length = reacted(polymer)
for lc, uc in zip(string.ascii_lowercase, string.ascii_uppercase):
    if lc in polymer or uc in polymer:
        test_polymer = polymer.replace(lc, "").replace(uc, "")
        test_length = reacted(test_polymer)
        p2_length = min(p2_length, test_length)

print(f"Part 2: Shortest length is {p2_length}")
