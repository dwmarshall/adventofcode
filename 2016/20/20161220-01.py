import sys

blocks = []

with open(sys.argv[1], "r") as file:
    for line in file:
        block = tuple(map(int, line.strip().split("-")))
        blocks.append(block)

blocks.sort()

current_block_end = 0

for block_start, block_end in blocks:
    if block_start - 1 <= current_block_end:
        current_block_end = max(current_block_end, block_end)

print(current_block_end + 1)
