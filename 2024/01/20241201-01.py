import sys

left = []
right = []

for line in sys.stdin:
    numbers = line.strip().split()
    a, b = map(int, numbers)
    left.append(a)
    right.append(b)

left.sort()
right.sort()

total_difference = 0

for a, b in zip(left, right):
    total_difference += abs(b - a)

print(total_difference)
