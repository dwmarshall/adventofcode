from itertools import batched
import sys

NEEDED_LENGTH = int(sys.argv[1])
INITIAL_STATE = sys.argv[2]

data = INITIAL_STATE

while (len(data)) < NEEDED_LENGTH:
    copy = []
    for c in data[::-1]:
        copy.append("0" if c == "1" else "1")
    data = data + "0" + "".join(copy)

data = data[:NEEDED_LENGTH]

checksum = data
while len(checksum) % 2 == 0:
    new_checksum = []
    for a, b in batched(checksum, 2):
        new_checksum.append("1" if a == b else "0")
    checksum = "".join(new_checksum)

print(f"Checksum is {checksum}")
