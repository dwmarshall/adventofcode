from functools import cache
import sys
from typing import List


def possible(s: str, inventory: List[str]) -> bool:
    if s == "" or s in inventory:
        return True
    for choice in inventory:
        if s.startswith(choice) and possible(s[len(choice) :], inventory):
            return True
    return False


wanted = []

with open(sys.argv[1], "r") as file:
    line = file.readline()
    available = line.strip().split(", ")
    file.readline()
    for line in file:
        wanted.append(line.strip())

can_make = 0

for w in wanted:
    if possible(w, available):
        print(f"We can make {w}")
        can_make += 1
    else:
        print(f"{w} is impossible")

print(can_make)
