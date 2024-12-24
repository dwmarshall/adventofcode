import sys

valid = 0


def valid_triangle(sides: list[int]) -> bool:
    perimeter = sum(sides)
    return all(2 * x < perimeter for x in sides)


with open(sys.argv[1], "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if valid_triangle(numbers):
            valid += 1


print(f"There are {valid} valid triangles")
