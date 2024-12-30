from collections import deque
import re
import sys


def move(s: str, x: int, y: int) -> str:
    s = list(s)
    c = s[x]
    del s[x]
    s = s[:y] + [c] + s[y:]
    return "".join(s)


def rotate(s: str, a: int) -> str:
    s = deque(s)
    s.rotate(a)
    return "".join(s)


def unrotate_by_position(s: str, x: str) -> str:
    t = deque(s)
    while rotate_by_position("".join(t), x) != s:
        t.rotate(-1)
    return "".join(t)


def rotate_by_position(s: str, x: str) -> str:
    s = deque(s)
    i = s.index(x)
    s.rotate(1 + i)
    if i >= 4:
        s.rotate(1)
    return "".join(s)


def reverse_position(s: str, a: int, b: int) -> str:
    s = list(s)
    s = s[:a] + list(reversed(s[a : b + 1])) + s[b + 1 :]
    return "".join(s)


def swap_letter(s: str, X: str, Y: str) -> str:
    s = list(s)
    x = s.index(X)
    y = s.index(Y)
    s[x], s[y] = s[y], s[x]
    return "".join(s)


def swap_position(s: str, a: int, b: int) -> str:
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return "".join(s)


password = sys.argv[2]


with open(sys.argv[1], "r") as file:
    lines = file.readlines()

for line in lines[::-1]:
    if m := re.match(r"swap position (\d+) with position (\d+)", line):
        x, y = list(map(int, m.groups()))
        password = swap_position(password, x, y)
    elif m := re.match(r"swap letter ([a-z]) with letter ([a-z])", line):
        x, y = m.groups()
        password = swap_letter(password, x, y)
    elif m := re.match(r"rotate (left|right) (\d+) step", line):
        x = int(m.group(2))
        if m.group(1) == "right":
            x = -x
        password = rotate(password, x)
    elif m := re.match(r"rotate based on position of letter ([a-z])", line):
        password = unrotate_by_position(password, m.group(1))
    elif m := re.match(r"reverse positions (\d+) through (\d+)", line):
        x, y = list(map(int, m.groups()))
        password = reverse_position(password, x, y)
    elif m := re.match(r"move position (\d+) to position (\d+)", line):
        x, y = list(map(int, m.groups()))
        password = move(password, y, x)
    else:
        print(f"{line.strip()} is unmatched!")

print(password)
