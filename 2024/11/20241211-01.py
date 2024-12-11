import sys

BLINKS = 25

with open(sys.argv[1], "r") as file:
    line = file.read()
    stones = list(map(int, line.strip().split()))

for i in range(BLINKS):
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
        elif len(str(s)) % 2 == 0:
            t = str(s)
            new_stones.append(int(t[: len(t) // 2]))
            new_stones.append(int(t[len(t) // 2 :]))
        else:
            new_stones.append(2024 * s)
    stones = new_stones

print(len(stones))
