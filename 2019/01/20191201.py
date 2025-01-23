import sys


def fuel_needed(m: int) -> int:
    fuel = 0
    while m > 0:
        m = max(0, m // 3 - 2)
        fuel += m
    return fuel


with open(sys.argv[1], "r") as file:
    masses = list(map(int, file.readlines()))

p1_fuel = sum(m // 3 - 2 for m in masses)
print(f"Part 1: Total fuel needed is {p1_fuel}")

p2_fuel = sum(fuel_needed(m) for m in masses)
print(f"Part 2: Total fuel needed is {p2_fuel}")
