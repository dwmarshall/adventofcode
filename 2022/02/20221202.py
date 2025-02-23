import sys

# Part 1 is indexed by the opponent shape (ABC) and our shape (XYZ)
PART1 = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

# Part 2 is indexed by the opponent shape and our desired outcome
# XYZ => lose/draw/win
PART2 = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]

part1_points = 0
part2_points = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        them, us = line.split()
        them_index = ord(them) - ord("A")
        us_index = ord(us) - ord("X")
        part1_points += PART1[them_index][us_index]
        part2_points += PART2[them_index][us_index]

print(f"Part 1: Total points are {part1_points}")
print(f"Part 2: Total points are {part2_points}")
