import re
import sys


def supports_TLS(s: str) -> bool:
    parts = [[], []]
    for i, part in enumerate(re.split(r"[\[\]]", s)):
        parts[i % 2].append(part)

    return any(has_ABBA(inner) for inner in parts[0]) and not any(
        has_ABBA(outer) for outer in parts[1]
    )


def has_ABBA(s: str) -> bool:
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


total_IPs = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        if supports_TLS(line):
            total_IPs += 1

print(total_IPs)
