from collections import Counter
import sys

left = []
right = []

for line in sys.stdin:
    numbers = line.strip().split()
    a, b = map(int, numbers)
    left.append(a)
    right.append(b)


total_similarity = 0

c = Counter(right)

for a in left:
    total_similarity += a * c[a]

print(total_similarity)
