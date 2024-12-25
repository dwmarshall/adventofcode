from itertools import product
import sys

keys = []
locks = []

with open(sys.argv[1], "r") as file:
    while line := file.readline():
        if line.strip() == "#" * 5:
            lock = [0] * 5
            for _ in range(5):
                lock_line = file.readline()
                for i in range(5):
                    if lock_line[i] == "#":
                        lock[i] += 1
            locks.append(lock)
            file.readline()  # discard line of dots
        elif line.strip() == "." * 5:
            key = [0] * 5
            for _ in range(5):
                key_line = file.readline()
                for i in range(5):
                    if key_line[i] == "#":
                        key[i] += 1
            keys.append(key)
            file.readline()  # discard line of octothorpes

valid_combinations = 0
for L, K in product(locks, keys):
    if all(L[i] + K[i] <= 5 for i in range(5)):
        valid_combinations += 1

print(valid_combinations)
