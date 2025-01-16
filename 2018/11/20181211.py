import copy
import sys

DEBUG = False

SERIAL_NUMBER = int(sys.argv[1])
SIDE = 300


def power_level(x: int, y: int, serial: int) -> int:
    rack_id = x + 10
    level = rack_id * y
    level += serial
    level *= rack_id
    level = level // 100 % 10
    level -= 5
    return level


cells = [[None] * SIDE for _ in range(SIDE)]

for y in range(SIDE):
    for x in range(SIDE):
        cells[y][x] = power_level(x + 1, y + 1, SERIAL_NUMBER)


dp = [None, cells]

for n in range(2, SIDE + 1):
    # Reduce dp[n - 1] to one less in each dimension
    working_cells = copy.deepcopy(dp[n - 1])
    del working_cells[-1]
    for y in range(len(working_cells)):
        del working_cells[y][-1]
    for y in range(len(working_cells) - n):
        for x in range(len(working_cells) - n):
            if DEBUG:
                print(f"Working on {(x, y)}")
            for i in range(n - 1):
                if DEBUG:
                    print(f"Add {(x + n - 1, y + i)} to {(x, y)})")
                working_cells[y][x] += cells[y + i][x + n - 1]
                if DEBUG:
                    print(f"Add {(x + i, y + n - 1)} to {(x, y)}")
                working_cells[y][x] += cells[y + n - 1][x + i]
            if DEBUG:
                print(f"Add {(x + n - 1), (y + n - 1)} to {(x, y)}")
            working_cells[y][x] += cells[y + n - 1][x + n - 1]
    dp.append(working_cells)

# Part 1: Investigate dp[3]
max_location = None
max_power = 0

for y in range(len(dp[3])):
    for x in range(len(dp[3])):
        if dp[3][y][x] > max_power:
            max_power = dp[3][y][x]
            max_location = (x + 1, y + 1)
print(f"Part 1: The answer is {max_location[0]},{max_location[1]}")

# Part 2: Investigate all the results
max_location = None
max_power = 0
max_square = None

for n_square in range(1, SIDE + 1):
    for y in range(len(dp[n_square])):
        for x in range(len(dp[n_square])):
            if dp[n_square][y][x] > max_power:
                max_location = (x + 1, y + 1)
                max_power = dp[n_square][y][x]
                max_square = n_square
                if DEBUG:
                    print(f"New max power {max_power} at {x + 1},{y + 1},{n_square}")

print(f"Part 2: The answer is {max_location[0]},{max_location[1]},{max_square}")
