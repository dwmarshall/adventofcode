from collections import Counter
from itertools import pairwise
import re
import sys


def p1_valid(p: str) -> bool:
    return (
        len(p) == 6
        and re.search(r"(\d)\1", p) is not None
        and all(a <= b for a, b in pairwise(p))
    )


def p2_valid(p: str) -> bool:
    c = Counter(p)
    return 2 in c.values()


lower, higher = map(int, sys.argv[1].split("-"))

p1_passes = [str(x) for x in range(lower, higher + 1) if p1_valid(str(x))]

print(f"Part 1: Number of passwords is {len(p1_passes)}")

p2_passes = [x for x in p1_passes if p2_valid(x)]

print(f"Part 2: Number of passwords is {len(p2_passes)}")
