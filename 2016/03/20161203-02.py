import sys

valid = 0


def valid_triangle(sides: list[int]) -> bool:
    perimeter = sum(sides)
    return all(2 * x < perimeter for x in sides)


lists = [[] for _ in range(3)]

with open(sys.argv[1], "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        for i in range(3):
            lists[i].append(numbers[i])

combined_list = lists[0] + lists[1] + lists[2]

for i in range(0, len(combined_list), 3):
    if valid_triangle(combined_list[i : i + 3]):
        valid += 1


print(f"There are {valid} valid triangles")
