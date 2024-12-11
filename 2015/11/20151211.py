import re
import string
import sys

password = sys.argv[1]

double_letters = re.compile(r"(.)\1.*(.)\2")


def increment(s: str) -> str:
    letters = list(s)
    for i in range(len(letters) - 1, -1, -1):
        if letters[i] == "z":
            letters[i] = "a"
            continue
        letters[i] = chr(ord(letters[i]) + 1)
        break
    return "".join(letters)


def has_straight(s: str) -> bool:
    for i in range(0, len(string.ascii_lowercase) - 2):
        if string.ascii_lowercase[i : i + 3] in s:
            return True
    return False


def next_password(s: str) -> str:
    while True:
        s = increment(s)
        if any(c in s for c in "iol"):
            continue
        if not has_straight(s):
            continue
        if double_letters.search(s) is None:
            continue
        return s


first = next_password(password)
second = next_password(first)
print(f"Part 1: {first}")
print(f"Part 2: {second}")
