import sys

with open(sys.argv[1], "r") as file:
    line = file.read().strip()

file_id = 0
block_pointer = 0

file_map = dict()
free_map = []

for i, c in enumerate(line):
    digit = int(c)
    if i % 2 == 0:
        file_map[file_id] = (block_pointer, digit)
        file_id += 1
    else:
        free_map.append((block_pointer, digit))
    block_pointer += digit

for inode in range(file_id - 1, -1, -1):
    file_loc, file_size = file_map[inode]
    for i, (loc, size) in enumerate(free_map):
        if loc < file_loc and size >= file_size:
            file_map[inode] = (loc, file_size)
            free_map[i] = (loc + file_size, size - file_size)
            break

checksum = 0

for inode, (loc, size) in file_map.items():
    first_block = loc
    last_block = loc + size - 1
    checksum += inode * (first_block + last_block) * (last_block - first_block + 1) // 2

print(checksum)
