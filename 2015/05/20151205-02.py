import re
import sys

total_nice = 0

paired_letters = re.compile(r"([a-z][a-z]).*\1")
double_letter = re.compile(r"([a-z]).\1")

with open(sys.argv[1], "r") as file:
    for line in file:
        if paired_letters.search(line) is None:
            continue
        if double_letter.search(line) is None:
            continue
        total_nice += 1

print(total_nice)
