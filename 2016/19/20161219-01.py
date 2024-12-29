from collections import deque
import sys

ELVES = int(sys.argv[1])


elves = deque(range(1, ELVES + 1))


while len(elves) > 1:
    del elves[1]
    elves.rotate(-1)

print(f"Winning elf is {elves[0]}")
