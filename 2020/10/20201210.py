from itertools import pairwise
import sys

with open(sys.argv[1], "r") as file:
    adapters = list(map(int, file.readlines()))

adapters.sort()

diff1 = 1
diff3 = 1

for a, b in pairwise(adapters):
    if b - a == 1:
        diff1 += 1
    elif b - a == 3:
        diff3 += 1

print(f"Part 1: The product is {diff1 * diff3}")

# Part 2
dp = [0 for _ in range(max(adapters) + 1)]
dp[0] = 1

for i in range(1, max(adapters) + 2):
    if i in adapters:
        for j in range(1, 4):
            dp[i] += dp[i - j]

print(f"Part 2: The number of ways is {dp[-1]}")
