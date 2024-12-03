import sys

x = [0, 0]
y = [0, 0]

visited = {(0, 0)}

for i, c in enumerate(sys.stdin.read()):
    index = i % 2
    match c:
        case "^":
            y[index] += 1
        case "v":
            y[index] -= 1
        case "<":
            x[index] -= 1
        case ">":
            x[index] += 1
    visited.add((x[index], y[index]))

print(len(visited))
