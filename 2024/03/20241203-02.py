import re
import sys

total_sum = 0
enabled = True

with open(sys.argv[1], "r") as file:
    for line in file:
        for expr in re.findall(r"(do|don\'t|mul)\(((\d+),(\d+))?\)", line):
            match expr[0]:
                case "do":
                    enabled = True
                case "don't":
                    enabled = False
                case "mul":
                    if enabled:
                        total_sum += int(expr[-1]) * int(expr[-2])


print(total_sum)
