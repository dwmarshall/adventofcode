import re
import sys

total_sum = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        for expr in re.findall(r"mul\((\d+),(\d+)\)", line):
            total_sum += int(expr[0]) * int(expr[1])

print(total_sum)
