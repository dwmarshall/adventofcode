import sys

x, y = 0, 0
visited = {(0, 0)}

for c in sys.stdin.read():
    match c:
        case "^":
            y += 1
        case "v":
            y -= 1
        case "<":
            x -= 1
        case ">":
            x += 1
    visited.add((x, y))

print(len(visited))
