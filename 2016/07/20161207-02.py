import re
import sys


def BABs(s: list[str], reverse: bool = False) -> set[str]:
    result = set()
    for t in s:
        for i in range(len(t) - 2):
            a, b, c = t[i : i + 3]
            if a == c and a != b:
                bab = f"{b}{a}{b}" if reverse else f"{a}{b}{a}"
                result.add(bab)
    return result


def supports_SSL(s: str) -> bool:
    parts = [[], []]
    for i, part in enumerate(re.split(r"[\[\]]", s)):
        parts[i % 2].append(part)
    wants = BABs(parts[0], reverse=True)
    has = BABs(parts[1])
    return not wants.isdisjoint(has)


total_IPs = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        if supports_SSL(line):
            total_IPs += 1

print(total_IPs)
