import sys

MAX_INT = 2**32 - 1

blocks = []

with open(sys.argv[1], "r") as file:
    for line in file:
        block = tuple(map(int, line.strip().split("-")))
        blocks.append(block)

blocks.sort()

allowed_IPs = 0

current_end_point = 0

for block_start, block_end in blocks:
    if block_start > current_end_point + 1:
        allowed_IPs += block_start - current_end_point - 1
    current_end_point = max(current_end_point, block_end)

allowed_IPs += MAX_INT - current_end_point


print(f"There are {allowed_IPs} allowed IP addresses.")
