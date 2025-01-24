import sys

grid = []


def trees(right: int, down: int) -> int:
    i, j = 0, 0
    tree_counter = 0

    while i < len(grid) - 1:
        i += down
        j += right
        j %= len(grid[0])
        if grid[i][j] == "#":
            tree_counter += 1

    return tree_counter


with open(sys.argv[1], "r") as file:
    for line in file:
        grid.append(list(line.strip()))


print(f"Part 1: There are {trees(3, 1)} trees.")

all_trees = 1

for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    all_trees *= trees(r, d)

print(f"Part 2: The product is {all_trees}")
