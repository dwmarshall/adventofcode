import sys

fresh: list[tuple[int, int]] = []
ingredients: list[int] = []

with open(sys.argv[1], "r") as file:
    while (line := file.readline()) != "\n":
        low, high = map(int, line.strip().split("-"))
        fresh.append((low, high))
    for line in file:
        ingredients.append(int(line))

fresh.sort()

# Start combining ranges
i = 0
while i < len(fresh) - 1:
    this_low, this_high = fresh[i]
    that_low, that_high = fresh[i + 1]
    if this_high >= that_low:
        fresh[i : i + 2] = [(this_low, max(this_high, that_high))]
        continue
    i += 1


ingredient_count = 0

for ingredient in ingredients:
    for low, high in fresh:
        if low <= ingredient <= high:
            ingredient_count += 1
            break

print(f"Part 1: Ingredient count is {ingredient_count}")

# Count the ingredients
fresh_count = 0

for low, high in fresh:
    fresh_count += high - low + 1

print(f"Part 2: Total fresh = {fresh_count}")
