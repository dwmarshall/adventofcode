import sys

floor = 0

while True:
    c = sys.stdin.read(1)
    if not c:
        break
    match c:
        case "(":
            floor += 1
        case ")":
            floor -= 1

print(floor)
