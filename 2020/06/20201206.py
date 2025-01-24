from functools import reduce
import operator
import sys


def common_questions(s: str) -> int:
    return len(reduce(operator.__and__, [set(x) for x in s.split("\n")]))


def distinct_questions(s: str) -> int:
    return len(reduce(operator.__or__, [set(x) for x in s.split("\n")]))


with open(sys.argv[1], "r") as file:
    responses = file.read(None).split("\n\n")

p1_total = sum(map(distinct_questions, responses))
print(f"Part 1: The total sum is {p1_total}")

p2_total = sum(map(common_questions, responses))
print(f"Part 2: The total sum is {p2_total}")
