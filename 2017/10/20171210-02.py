from functools import reduce
import operator
import sys

LENGTH = 256
input = sys.argv[1]
input_lengths = [ord(c) for c in input]

input_lengths.extend([17, 31, 73, 47, 23])

skip = 0
curr = 0
elements = list(range(LENGTH))

for _ in range(64):
    for length in input_lengths:
        if length > 1:
            for i in range(length // 2):
                a = (curr + i) % LENGTH
                b = (curr + length - 1 - i) % LENGTH
                elements[a], elements[b] = elements[b], elements[a]
        curr = (curr + length + skip) % LENGTH
        skip += 1

dense_hash = [
    reduce(operator.__xor__, elements[16 * i : 16 * (i + 1)]) for i in range(16)
]

output = "".join(f"{h:02x}" for h in dense_hash)
print(f"Part 2: The hash is {output}")
