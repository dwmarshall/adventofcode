from itertools import permutations
import sys


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        # Some ranks may become obsolete so they are not updated
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


grid = []

with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

unvisited = {x * rows + y for x in range(rows) for y in range(cols)}

uf = UnionFind(rows * cols)

while unvisited:
    curr = unvisited.pop()
    r, c = divmod(curr, rows)
    if r > 0 and grid[r][c] == grid[r - 1][c]:
        uf.union(curr, curr - rows)
    if c > 0 and grid[r][c] == grid[r][c - 1]:
        uf.union(curr, curr - 1)
    if r < rows - 1 and grid[r][c] == grid[r + 1][c]:
        uf.union(curr, curr + rows)
    if c < cols - 1 and grid[r][c] == grid[r][c + 1]:
        uf.union(curr, curr + 1)

roots = set(uf.find(x) for x in range(rows * cols))
root_map = {x: i for i, x in enumerate(roots)}

area = [0] * len(roots)
fences = [[] for _ in range(len(roots))]

for r in range(rows):
    for c in range(cols):
        x = r * rows + c
        root = uf.find(x)
        index = root_map[root]
        area[index] += 1
        # check the cell above
        if r == 0 or not uf.connected(x, x - rows):
            fences[index].append(((r, c), (r, c + 1), "down"))
        # check the cell below
        if r == rows - 1 or not uf.connected(x, x + rows):
            fences[index].append(((r + 1, c), (r + 1, c + 1), "up"))
        # check the cell to the left
        if c == 0 or not uf.connected(x, x - 1):
            fences[index].append(((r, c), (r + 1, c), "right"))
        # check to the right
        if c == cols - 1 or not uf.connected(x, x + 1):
            fences[index].append(((r, c + 1), (r + 1, c + 1), "left"))

for i in range(len(fences)):
    f = fences[i]
    merged = True
    while merged:
        merged = False
        for a, b in permutations(f, 2):
            if a[2] != b[2] or a[1] != b[0]:
                continue
            if a[0][0] == b[1][0] or a[0][1] == b[1][1]:
                new_span = (a[0], b[1], a[2])
                f.append(new_span)
                a_index = f.index(a)
                del f[a_index]
                b_index = f.index(b)
                del f[b_index]
                merged = True
                break

total_cost = 0
for a, num_sides in zip(area, [len(x) for x in fences]):
    total_cost += a * num_sides

print(total_cost)
