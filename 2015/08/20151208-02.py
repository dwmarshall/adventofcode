import json
import sys

difference = 0
with open(sys.argv[1], "r") as file:
    for line in file:
        input = line.strip()
        encoded = json.dumps(input)
        difference += len(encoded) - len(input)
        print(f"{input} became {encoded}")

print(difference)
