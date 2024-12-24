from collections import Counter
import sys

grid = []
message = []

with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(line.strip())

for i in range(len(grid[0])):
    c = Counter(x[i] for x in grid)
    message.append(c.most_common(1)[0][0])

print("".join(message))
