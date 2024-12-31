import sys

LENGTH = int(sys.argv[2]) if len(sys.argv) > 2 else 256


with open(sys.argv[1], "r") as file:
    input_lengths = list(map(int, file.readline().split(",")))

skip = 0
curr = 0
elements = list(range(LENGTH))

for length in input_lengths:
    sublist = list(reversed([elements[(curr + i) % LENGTH] for i in range(length)]))
    for i in range(length):
        elements[(curr + i) % LENGTH] = sublist[i]
    curr = (curr + length + skip) % LENGTH
    skip += 1

print(f"Part 1: The product is {elements[0] * elements[1]}")
