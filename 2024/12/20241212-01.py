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
    if r < rows - 1 and grid[r][c] == grid[r + 1][c]:
        uf.union(curr, curr + rows)
    if c > 0 and grid[r][c] == grid[r][c - 1]:
        uf.union(curr, curr - 1)
    if c < cols - 1 and grid[r][c] == grid[r][c + 1]:
        uf.union(curr, curr + 1)

roots = set(uf.root)
root_map = {x: i for i, x in enumerate(roots)}

area = [0] * len(roots)
perimeter = [0] * len(roots)

for r in range(rows):
    for c in range(cols):
        x = r * rows + c
        root = uf.find(x)
        index = root_map[root]
        area[index] += 1
        if r == 0 or not uf.connected(x, x - rows):
            perimeter[index] += 1
        if r == rows - 1 or not uf.connected(x, x + rows):
            perimeter[index] += 1
        if c == 0 or not uf.connected(x, x - 1):
            perimeter[index] += 1
        if c == cols - 1 or not uf.connected(x, x + 1):
            perimeter[index] += 1

total_price = 0

for a, p in zip(area, perimeter):
    total_price += a * p

print(total_price)
