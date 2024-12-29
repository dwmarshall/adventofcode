import sys

ROWS = int(sys.argv[2])


traps = set(
    [
        (0, 0, 1),
        (1, 0, 0),
        (0, 1, 1),
        (1, 1, 0),
    ]
)


def is_trap(prev: list[int], index: int) -> bool:
    if index == 0:
        t = (1,) + tuple(prev[:2])
    elif index + 1 == len(prev):
        t = tuple(prev[-2:]) + (1,)
    else:
        t = tuple(prev[index - 1 : index + 2])
    return t in traps


with open(sys.argv[1], "r") as file:
    row = [1 if c == "." else 0 for c in file.readline().strip()]


total_safe = sum(row)

for _ in range(ROWS - 1):
    new_row = [0 if is_trap(row, i) else 1 for i in range(len(row))]
    total_safe += sum(new_row)
    row = new_row

print(f"There are {total_safe} safe tiles.")
