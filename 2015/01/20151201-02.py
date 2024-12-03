import sys

floor = 0

for i, c in enumerate(sys.stdin.read()):
    match c:
        case "(":
            floor += 1
        case ")":
            floor -= 1
    if floor < 0:
        print(i + 1)
        break
