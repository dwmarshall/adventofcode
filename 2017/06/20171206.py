import sys

with open(sys.argv[1], "r") as file:
    blocks = list(map(int, file.readline().split()))

seen = dict()
cycles = 0

while tuple(blocks) not in seen:
    seen[tuple(blocks)] = cycles
    most_blocks = max(blocks)
    most_index = blocks.index(most_blocks)
    blocks[most_index] = 0
    next_index = (most_index + 1) % len(blocks)
    for _ in range(most_blocks):
        blocks[next_index] += 1
        next_index = (next_index + 1) % len(blocks)
    cycles += 1

print(f"Part 1: We looped after {cycles} cycles")
print(f"Part 2: The loop is {cycles - seen[tuple(blocks)]} long")
