from collections import defaultdict
import sys

G = defaultdict(set)

all_cliques = set()

with open(sys.argv[1], "r") as file:
    for line in file:
        A, B = line.strip().split("-")
        G[A].add(B)
        G[B].add(A)
        all_cliques.add(frozenset([A, B]))

all_hosts = set(G)

while len(all_cliques) > 1:
    group_size = min(map(len, all_cliques))
    print(f"Working on group size {group_size}: {len(all_cliques)}")
    new_cliques = set()
    for c in all_cliques:
        for node in all_hosts - c:
            if all(node in G[x] for x in c):
                new_clique = set(c)
                new_clique.add(node)
                new_cliques.add(frozenset(new_clique))
    all_cliques = new_cliques

winner = all_cliques.pop()
print(",".join(sorted(winner)))
