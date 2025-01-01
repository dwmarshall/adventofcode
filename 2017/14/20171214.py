from functools import reduce
import operator
import sys
from unionfind import UnionFind


def knot_hash(key: str) -> str:

    input_lengths = [ord(c) for c in key]
    input_lengths.extend([17, 31, 73, 47, 23])

    skip = 0
    curr = 0
    elements = list(range(256))

    for _ in range(64):
        for length in input_lengths:
            if length > 1:
                for i in range(length // 2):
                    a = (curr + i) % 256
                    b = (curr + length - 1 - i) % 256
                    elements[a], elements[b] = elements[b], elements[a]
            curr = (curr + length + skip) % 256
            skip += 1

    dense_hash = [
        reduce(operator.__xor__, elements[16 * i : 16 * (i + 1)]) for i in range(16)
    ]

    return "".join(f"{h:08b}" for h in dense_hash)


INPUT = sys.argv[1]

used = dict()

for i in range(128):
    hash = knot_hash(f"{INPUT}-{i}")
    for j, c in enumerate(hash):
        if c == "1":
            used[(i, j)] = len(used)

print(f"Part 1: Total used is {len(used)}")

uf = UnionFind(len(used))

for (x, y), i in used.items():
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in used:
            uf.union(i, used[(nx, ny)])

distinct_roots = set()
for i in used.values():
    distinct_roots.add(uf.find(i))

print(f"Part 2: There are {len(distinct_roots)} regions.")
