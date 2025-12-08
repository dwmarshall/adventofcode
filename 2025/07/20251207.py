from functools import cache
import sys

with open(sys.argv[1], "r") as file:
    input = file.readlines()

# Part 1: Count the total splits that occur
beams: set[int] = set()

beams.add(input[0].index("S"))

splits = 0

for i in range(1, len(input)):
    new_beams: set[int] = set()
    for b in beams:
        if input[i][b] == "^":
            splits += 1
            new_beams.add(b + 1)
            new_beams.add(b - 1)
        else:
            new_beams.add(b)
    beams = new_beams

print(f"Part 1: Total splits are {splits}")

# Part 2: Count the possible timelines


@cache
def timelines(level: int, position: int) -> int:
    if level == len(input) - 1:
        return 1
    if input[level + 1][position] == "^":
        return timelines(level + 1, position - 1) + timelines(level + 1, position + 1)
    else:
        return timelines(level + 1, position)


print(f"Part 2: Number of timelines is {timelines(0, input[0].index("S"))}")
