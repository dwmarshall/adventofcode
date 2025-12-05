import sys

ADJACENCIES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def accessibles(p: set[tuple[int, int]]) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    for i, j in p:
        if adjacents(p, i, j) < 4:
            result.add((i, j))
    return result


def adjacents(p: set[tuple[int, int]], i: int, j: int) -> int:
    result = 0
    for di, dj in ADJACENCIES:
        if (i + di, j + dj) in p:
            result += 1
    return result


paper: set[tuple[int, int]] = set()

with open(sys.argv[1], "r") as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line):
            if c == "@":
                paper.add((i, j))


accessible = accessibles(paper)

print(f"Part 1: {len(accessible)} rolls are accessible")

removable = len(accessible)
while accessible:
    paper -= accessible
    accessible = accessibles(paper)
    removable += len(accessible)
print(f"Part 2: There are {removable} removable")
