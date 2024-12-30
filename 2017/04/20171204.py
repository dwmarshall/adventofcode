import sys

valid_passphrases1 = 0
valid_passphrases2 = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        words = line.strip().split()
        if len(words) == len(set(words)):
            valid_passphrases1 += 1
            sorted_words = ["".join(sorted(x)) for x in words]
            if len(sorted_words) == len(set(sorted_words)):
                valid_passphrases2 += 1


print(f"Part 1: There are {valid_passphrases1} valid passphrases.")
print(f"Part 2: There are {valid_passphrases2} valid passphrases.")
