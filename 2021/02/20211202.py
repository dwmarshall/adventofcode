import sys

p1_position, p1_depth = 0, 0
p2_position, p2_depth, p2_aim = 0, 0, 0

with open(sys.argv[1], "r") as file:
    for line in file:
        action, quantity = line.split()
        quantity = int(quantity)
        match action:
            case "forward":
                p1_position += quantity
                p2_position += quantity
                p2_depth += p2_aim * quantity
            case "up":
                p1_depth -= quantity
                p2_aim -= quantity
            case "down":
                p1_depth += quantity
                p2_aim += quantity

print(f"Part 1: The product is {p1_depth * p1_position}")
print(f"Part 2: The product is {p2_depth * p2_position}")
