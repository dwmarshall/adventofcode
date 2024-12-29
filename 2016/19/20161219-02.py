from collections import deque
import sys

ELVES = int(sys.argv[1])

left = deque(range(1, (ELVES // 2) + 1))
right = deque(range((ELVES // 2) + 1, ELVES + 1))


while left and right:
    if len(left) > len(right):
        left.pop()
    else:
        right.popleft()
    right.append(left.popleft())
    left.append(right.popleft())

winning_elf = left[0] if left else right[0]
print(f"Winning elf is {winning_elf}")
