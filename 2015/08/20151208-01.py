import ast
import sys

difference = 0
with open(sys.argv[1], "r") as file:
    for line in file:
        input = line.strip()
        decoded = ast.literal_eval(input)
        difference += len(input) - len(decoded)
        print(f"{input} has {len(input)}, decoded has {len(decoded)}")

print(difference)
