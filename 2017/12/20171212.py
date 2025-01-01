import sys
from unionfind import UnionFind

connections = []

with open(sys.argv[1], "r") as file:
    for line in file:
        id, links = line.strip().split(" <-> ")
        link_list = list(map(int, links.split(", ")))
        connections.append(link_list)

uf = UnionFind(len(connections))
for i in range(len(connections)):
    for j in connections[i]:
        uf.union(i, j)

connected_programs = 0
group_roots = set()
for i in range(len(connections)):
    group_roots.add(uf.find(i))
    if uf.connected(0, i):
        connected_programs += 1

print(f"Part 1: There are {connected_programs} programs connected with process 0.")
print(f"Part 2: There are {len(group_roots)} distinct groups.")
