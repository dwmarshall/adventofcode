import sys

all_cals = []

with open(sys.argv[1], "r") as file:
    full_stream = file.read()

for elf in full_stream.split("\n\n"):
    all_cals.append(sum(map(int, elf.split("\n"))))

all_cals.sort(reverse=True)

print(f"Part 1: Maximum calories are {all_cals[0]}")
print(f"Part 2: Top three cals are {sum(all_cals[:3])}")
