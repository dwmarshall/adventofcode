from itertools import product
import operator
import re
import sys

operators = [operator.__add__, operator.__mul__]

line_regex = re.compile(r"(\d+):((?: \d+)+)")

total_sum = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        match = line_regex.search(line)
        if not match:
            continue
        desired_result = int(match.group(1))
        terms = list(map(int, match.group(2).strip().split()))
        for ops in product(operators, repeat=len(terms) - 1):
            value = ops[0](terms[0], terms[1])
            for i in range(1, len(ops)):
                value = ops[i](value, terms[i + 1])
            if value == desired_result:
                total_sum += desired_result
                break

print(total_sum)
