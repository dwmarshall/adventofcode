import sys

with open(sys.argv[1], "r") as file:
    line = file.read()

blocks = []

file_id = 0

for i, c in enumerate(line):
    digit = int(c)
    if i % 2 == 0:
        blocks.extend([file_id] * digit)
        file_id += 1
    else:
        blocks.extend([None] * digit)

while None in blocks:
    if blocks[-1] is not None:
        new_index = blocks.index(None)
        blocks[new_index] = blocks[-1]
    del blocks[-1]

checksum = 0

for i, id in enumerate(blocks):
    checksum += i * id

print(checksum)
