from itertools import combinations
import networkx as nx
import sys

G = nx.Graph()

with open(sys.argv[1], "r") as file:
    for line in file:
        A, B = line.strip().split("-")
        G.add_edge(A, B)


largest_clique = max(nx.find_cliques(G), key=len)

print(",".join(sorted(largest_clique)))
