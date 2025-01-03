import sys

STEPS = int(sys.argv[1])

spinlock = [0]
curr = 0

for i in range(1, 2017 + 1):
    insertion_point = (curr + STEPS) % len(spinlock)
    spinlock[insertion_point : insertion_point + 1] = [spinlock[insertion_point], i]
    curr = insertion_point + 1

print(f"Part 1: The value after 2017 is {spinlock[curr + 1]}")

last_added = None
curr = 0

for i in range(1, 50_000_000 + 1):
    insertion_point = (curr + STEPS) % i
    if insertion_point == 0:
        last_added = i
    curr = insertion_point + 1

print(f"Part 2: The value after zero is {last_added}")
