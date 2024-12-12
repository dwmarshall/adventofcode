import re
import sys

total = 0

for line in sys.stdin:
    for s in re.findall(r"-?\d+", line):
        total += int(s)

print(total)
