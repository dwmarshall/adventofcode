from collections import defaultdict
import sys

G = defaultdict(set)

with open(sys.argv[1], "r") as file:
    for line in file:
        A, B = line.strip().split("-")
        G[A].add(B)
        G[B].add(A)


def bron_kerbosch(
    g: dict[str, set[str]],
    r: set[str],
    p: set[str],
    x: set[str],
    cliques: list[set[str]],
) -> None:
    if not p and not x:
        cliques.append(r)
    while p:
        v = p.pop()
        bron_kerbosch(g, r | {v}, p & g[v], x & g[v], cliques)
        x.add(v)


def find_largest_clique(g: dict[str, set[str]]) -> set[str]:
    cliques = []
    bron_kerbosch(g, set(), set(g), set(), cliques)
    return max(cliques, key=len)


winner = find_largest_clique(G)
print(",".join(sorted(winner)))
