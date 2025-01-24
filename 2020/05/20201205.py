import sys


def binary(s: str) -> int:
    lowest = 0
    highest = (1 << len(s)) - 1
    for c in s:
        mid = (lowest + highest + 1) // 2
        if c in "FL":
            highest = mid - 1
        elif c in "BR":
            lowest = mid
    assert lowest == highest
    return lowest


def seat_id(s: str) -> int:
    return binary(s[:7]) * 8 + binary(s[-3:])


max_p1 = 0
all_seats = set()

with open(sys.argv[1], "r") as file:
    for line in file:
        this_id = seat_id(line.strip())
        max_p1 = max(max_p1, this_id)
        all_seats.add(this_id)

print(f"Part 1: The highest seat ID is {max_p1}")

for x in range(min(all_seats) + 1, max(all_seats)):
    if x not in all_seats:
        print(f"Part 2: The missing seat ID is {x}")
