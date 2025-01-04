from itertools import cycle
import sys

with open(sys.argv[1], "r") as file:
    changes = list(map(int, file.readlines()))

print(f"Part 1: Resulting change is {sum(changes)}")

seen = {0}
frequency = 0

for n in cycle(changes):
    frequency += n
    if frequency in seen:
        print(f"Part 2: The first repeat is {frequency}")
        break
    seen.add(frequency)
